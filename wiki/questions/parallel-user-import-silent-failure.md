---
title: Parallel bulk user import — silent failures (201 returned but user missing)
type: question
domain: keycloak
slug: parallel-user-import-silent-failure
summary: "Running two bulk user import jobs in parallel against the same RHBK 26 realm via the Admin REST API (service account) can silently drop some users — the API returns HTTP 201, but the user is absent afterwards. The root cause is a TOCTOU (Time-of-Check-Time-of-Use) race condition in Keycloak's user uniqueness check, amplified by the local-only user cache and lack of distributed pessimistic locking. Known patterns documented in gated Red Hat KB solutions."
sources:
  - kb:rhbk-26-4-caching
  - kb:rhbk-26-4-user-storage-spi
  - kb:rhbk-26-4-db
  - kb:rhbk-26-4-assembly-managing-users-server-administration-guide
  - kb:rhbk-26-4-admin-rest-api
  - guide:server_administration_guide
  - gated:https://access.redhat.com/solutions/5601101 (Deadlock with concurrent requests to MS SQL Server — gated)
  - gated:https://access.redhat.com/solutions/7105791 (Preventing deadlocks on concurrent user updates — gated)
  - gated:https://access.redhat.com/solutions/4863741 (ModelDuplicateException when importing realm config — gated)
  - ref:rhbk-troubleshooting-kb.md
provenance:
  extracted: 8
  inferred: 6
  ambiguous: 0
status: draft
updated: 2026-06-24
---

# Parallel bulk user import — silent failures (201 returned but user missing)

**You run two parallel scripts, each POSTing to `POST /admin/realms/{realm}/users` (via a service account) to bulk-import users into the same realm. Individually each job works perfectly. Running them in parallel produces HTTP 201 for every request, but some users are absent afterwards — never created, no error surfaced.**

## Root cause

The failure is a **classic TOCTOU race condition** in Keycloak's user-creation path, exploiting three architectural properties:

### 1. Check-then-act without a distributed lock

The `UserProvider.addUser()` implementation performs a **read check** (`getUserByUsername(realm, username)` — a `SELECT`) followed by an **insert** (`EntityManager.persist()`). These are separate DB round-trips inside the same JTA transaction. Nothing prevents a second concurrent transaction from observing "username does not exist" between the first transaction's check and its insert.

Keycloak's own example code in the User Storage SPI shows this exact pattern (*reference: `rhbk-26-4-user-storage-spi.md:533-538`*):

```
UserModel local = userProvider.getUserByUsername(realm, username);
if (local == null) {
    local = userProvider.addUser(realm, username);  // race window here
}
```

There is **no application-level `SELECT ... FOR UPDATE`** or `SERIALIZABLE` isolation to close the window.

### 2. READ COMMITTED isolation (database default)

PostgreSQL, MySQL, and most RHBK-supported databases default to **READ COMMITTED** isolation (*`rhbk-26-4-db.md`*). Under READ COMMITTED, Transaction B cannot see Transaction A's uncommitted INSERT. So both transactions' `getUserByUsername()` calls return "no user exists" simultaneously.

The database's unique constraint on `USER_ENTITY(REALM_ID, USERNAME)` is the last line of defense — it lets only one INSERT through. The loser gets a constraint violation at commit time.

### 3. The `users` cache is LOCAL (not distributed)

RHBK's `users` Infinispan cache is configured as **`Local`**, not `Replicated` or `Distributed` (*`rhbk-26-4-caching.md:39`*). Each cluster node maintains its own independent user cache:

| Cache name | Mode | Purpose |
|---|---|---|
| `users` | **Local** | Cache persisted user data |
| `sessions` | Distributed | Cache user session data |
| `offlineSessions` | Distributed | Cache offline session data |

In a multi-node cluster, this means:
- Node A creates and caches a user locally
- Node B has no record of that user in its local `users` cache
- There is **no cross-node distributed lock** or consistent cache synchronization for user entity data
- This multiplies the TOCTOU window: two concurrent requests hitting different nodes are guaranteed to see independent "does not exist" states

## Why "silent 201"?

The HTTP 201 response is sent by the JAX-RS resource (`UsersResource.createUser()`) before the JTA transaction actually commits. In Quarkus, the sequence is:

1. Container opens a JTA transaction
2. REST method runs: create user entity, `em.persist()`, prepare response with 201
3. After method return, the container attempts **JTA commit → `EntityManager.flush()` → actual SQL INSERT sent to DB**
4. If the DB rejects the INSERT (unique constraint violation), the JTA commit fails → transaction rolls back
5. The 201 response may already have been sent or written to the HTTP output buffer

The script sees 201, but the INSERT was rolled back. The user never made it to the database.

**`(inferred)`** The exact behavior depends on the JPA provider and transaction manager implementation, but the gap between "response prepared" and "commit verified" is the window where this silent loss occurs.

## Known documented patterns

Red Hat's KB (subscriber-gated) tracks several related defects:

| Solution | Topic | Relevance |
|---|---|---|
| `access.redhat.com/solutions/5601101` | Deadlock with concurrent requests to MS SQL Server during user creation | **Direct match**: concurrent user creation, one succeeds, the other gets Hibernate WARN | *gated* |
| `access.redhat.com/solutions/7105791` | Preventing deadlocks on concurrent user updates | Concurrent user attribute modifications deadlock on PostgreSQL (`[40P01] ERROR: deadlock detected`) | *gated* |
| `access.redhat.com/solutions/4863741` | ModelDuplicateException when importing realm configuration data | `ModelDuplicateException` (upstream exception name for duplicate key) during concurrent import operations | *gated* |
| `access.redhat.com/solutions/7134835` | User data sync leading to DB deadlocks | Concurrent login data sync causes deadlocks | *gated* |

## Who is affected

- Any **multi-node RHBK cluster** running user import jobs in parallel (the local-only `users` cache guarantees cross-node inconsistency)
- Any **single-node RHBK** with concurrent threads in the Quarkus worker pool hitting the same username — or even different usernames if a coincidental DB load or lock escalates the constraint violation to a serialization failure
- Users of any RHBK-supported database — PostgreSQL, MySQL, MariaDB, MSSQL — since the issue is in the application layer, not the database

## Workarounds and mitigations

### Before the import — prevent the race

1. **Serialize the import jobs** — run one batch at a time. This is the simplest fix and eliminates the race entirely.
2. **Partition the input** — assign disjoint username ranges to each parallel worker so no username is attempted by more than one job. Even then, the READ COMMITTED + local-cache combo can still cause false 201s on different usernames if the DB load during commit triggers serialization failures — test with your dataset size.
3. **Use a single script with internal parallelism** — a single Job/thread pool hitting one RHBK node avoids the cross-node cache disparity (the local cache is shared within one JVM), but does not eliminate the TOCTOU inside the JVM's thread pool.

### After the import — detect and retry

1. **Verify each user after creation** — after receiving 201, `GET /admin/realms/{realm}/users/{id}` to confirm the user exists. Retry if not found.
2. **Check the server logs** — look for `ModelDuplicateException`, `ConstraintViolationException`, or `WARN [org.hibernate` during the import window. The gated KB (`solutions/5601101`) shows Hibernate warnings from the concurrent creation path.
3. **Export the full user list before and after** — diff the sets to identify which users were lost. Rerun only the missing users.

### Longer-term

- **Open a Red Hat support case** referencing `solutions/5601101` (deadlock on concurrent user creation) and `solutions/7105791` (concurrent user update deadlock). A patch or configuration recommendation may exist behind the gated KB.

## Contradictions / caveats

- The reference tier does **not** contain a dedicated "concurrent user creation bug" document with a confirmed root cause. The analysis above is synthesized from the documented architecture (`users` cache is Local, READ COMMITTED default, `addUser()` TOCTOU pattern) plus the gated KB entries that describe the symptoms.
- If the import jobs use the **same** username across both jobs, the race behaves differently: one gets a clear `409 Conflict` from the application layer, not a silent 201. The silent 201 pattern requires the job's requests to not trigger the application-level duplicate check (because both pass the check simultaneously).
- The silent 201 may also occur when two jobs create users with **different usernames but the same email address** (if the realm has `Duplicate emails` disabled), via the same TOCTOU window on the email uniqueness check. This is controlled by realm settings.

## See also

- [[managing-users-credentials]] — user creation workflow
- [[kcadm-cli]] — Admin CLI and Admin REST API
- [[realm-import-export]] — partialImport and bulk import caveats
- [[distributed-caches]] — Infinispan cache modes (local vs distributed)
- [[troubleshooting-index]] — troubleshooting by area

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)
- **kb:rhbk-26-4-caching** — "Caching" chapter: `users` cache is Local mode (line 39)
- **kb:rhbk-26-4-user-storage-spi** — User Storage SPI: `addUser()` check-then-act pattern (lines 533-538, 690-716)
- **kb:rhbk-26-4-db** — Database configuration: default READ COMMITTED isolation, non-XA transactions (lines 199-219)
- **kb:rhbk-26-4-admin-rest-api** — Admin REST API: `POST /admin/realms/{realm}/users` endpoint
- **kb:rhbk-26-4-assembly-managing-users-server-administration-guide** — Managing users chapter: user creation and search
- **ref:rhbk-troubleshooting-kb.md** — Consolidated KB: gated pointers for concurrent user issues
- **gated:https://access.redhat.com/solutions/5601101** — "Deadlock with concurrent requests to MS SQL Server" (requires Red Hat subscription)
- **gated:https://access.redhat.com/solutions/7105791** — "Preventing deadlocks on concurrent user updates" (requires Red Hat subscription)
- **gated:https://access.redhat.com/solutions/4863741** — "ModelDuplicateException when importing realm configuration data" (requires Red Hat subscription)

### Wiki
- [[managing-users-credentials]] — user creation and attributes
- [[kcadm-cli]] — Admin CLI / REST API operations
- [[distributed-caches]] — Infinispan cache topology
- [[troubleshooting-index]] — troubleshooting triage by area
