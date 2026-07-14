---
title: "RHBK login storm OOMed despite the request-queue cap — what was missing"
type: question
domain: keycloak
slug: rhbk-login-storm-oom-queue-cap
summary: >
  The `http-max-queued-requests` option exists, but RHBK has NO queue limit by
  default (it queues infinitely). The "1000" the user remembers is only an
  example value. A login storm still OOMs because the HTTP queue is just one of
  several memory dimensions (executor threads, DB pool, auth-session caches,
  CPU throttling) and because the queue itself consumes Pod memory.
sources:
  - kb:rhbk-26-2-concepts-threads
  - kb:rhbk-26-2-configuration-production
  - kb:rhbk-26-2-concepts-memory-and-cpu-sizing
  - kb:rhbk-26-2-getting-started-scaling-and-tuning
  - kb:rhbk-26-2-containers
  - kb:rhbk-26-0-deploy-keycloak-kubernetes
  - kb:rhbk-26-0-red-hat-build-of-keycloak-26-0
  - kb:rhbk-26-2-metrics-for-troubleshooting
question_tier: support-kb
provenance:
  extracted: 12
  inferred: 2
  ambiguous: 0
status: draft
updated: 2026-07-12
---

# RHBK login storm OOMed despite the request-queue cap — what was missing

**GATE**

TOKEN: `http-max-queued-requests`
VERBATIM_MATCH: yes
VERDICT: EXISTS

The token exists verbatim in the RHBK corpus. But the question's *premise* —
"RHBK caps its request queue at 1000 by default" — is false. The documented
default is **no limit at all**; `1000` is only an example value used in the
docs. That false assumption is the first thing you are missing.

## 1. The default is NOT 1000 — it is unlimited

RHBK explicitly documents that, out of the box, it does **not** cap the queue:

- "By default, there is no limit set. Set the option `http-max-queued-requests`
  to limit the number of queued requests to a given threshold matching your
  environment. Any request that exceeds this limit would return with an
  immediate 503 Server not Available." — `rhbk-26-2-configuration-production.md:36-39`
- "By default, Red Hat build of Keycloak will queue all incoming requests
  infinitely, even if the request processing stalls." —
  `rhbk-26-2-concepts-threads.md:36`

The `1000` figure appears **only as an illustration**, not as a default:
- In the thread-pool concepts chapter: "Assuming a Red Hat build of Keycloak Pod
  processes around 200 requests per second, a queue of 1000 would lead to
  maximum waiting times of around 5 seconds." — `rhbk-26-2-concepts-threads.md:38`
- As a sample `additionalOptions` value `value: "1000"` in a Kubernetes deploy
  snippet — `rhbk-26-0-deploy-keycloak-kubernetes.md:37`.

**Conclusion (inferred):** if your cluster was relying on a "default 1000 cap"
for load shedding, that cap was never actually active — the queue was unbounded,
grew without limit during the storm, and **"this will use additional memory in
the Pod"** (`rhbk-26-2-concepts-threads.md:36`), driving the OOM directly. The
503 shedding only triggers once `http-max-queued-requests` is *explicitly set*.

## 2. Even with the queue capped, a login storm OOMs through other dimensions

The HTTP request queue is just one memory surface. A login storm still pins
memory via several others, none of which the queue cap addresses:

- **Quarkus executor pool (`http-pool-max-threads`).** Requests are handled by an
  executor pool sized to the CPU (max 50+ threads). "Each thread will also
  consume memory, and the container memory limits need to be set to a value that
  allows for this or the Pod will be killed by Kubernetes." —
  `rhbk-26-2-concepts-threads.md:24-27, 43-45`. On Kubernetes you must tune the
  worker-thread count to your CPU limit, or the Pod is throttled → congestion →
  longer response times → increased memory → unstable system.
- **Database connection pool (`db-pool-max-size` / `db-pool-min-size` /
  `db-pool-initial-size`).** Under a storm, threads queue for a DB connection;
  "Once a request cannot acquire a database connection within 5 seconds, it will
  fail … Unable to acquire JDBC Connection" with a 5xx to the caller —
  `rhbk-26-2-concepts-threads.md:28-34`. A saturated pool means congestion and
  more in-flight state held in memory. The troubleshooting guide notes the DB
  pool is "often exhausted, and there are threads queuing for a connection" —
  `rhbk-26-2-metrics-for-troubleshooting.md:25`.
- **Authentication sessions in the Infinispan caches.** Each in-flight login
  creates an authentication session held in the distributed caches (by default
  two owners per entry) — `rhbk-26-2-concepts-memory-and-cpu-sizing.md:117`. A
  storm of concurrent logins = a spike in cache/heap-resident session objects.
- **CPU throttling → memory blow-up.** The sizing guide warns: "Performance of
  Red Hat build of Keycloak dropped significantly when its Pods were throttled in
  our tests," and recommends 150% CPU head-room for spikes —
  `rhbk-26-2-concepts-memory-and-cpu-sizing.md:35`. Throttling lengthens request
  lifetimes, keeping more threads/sessions alive simultaneously → more heap.
- **Heap sizing floor.** In containers, RHBK allocates **70% of the memory limit
  to heap** plus **~300 MB non-heap** —
  `rhbk-26-2-concepts-memory-and-cpu-sizing.md:29`,
  `rhbk-26-2-containers.md:216-222`. If your memory *limit* is set too low, the
  heap is small and a storm tips it over; if the limit is **unset**, the heap can
  grow up to 70% of total container memory and "is returned to the OS
  reluctantly" — `rhbk-26-2-containers.md:234`.
- **Readiness probe can block under load.** "The overall health probe and the
  readiness probe can in some cases block to check the connection to the
  database, so they might fail under a high load. Due to this, a Pod can become
  non-ready under a high load" — `rhbk-26-2-concepts-threads.md:40-42`. A
  non-ready Pod is pulled from the LB, but the unbounded internal queue keeps
  growing.

## 3. What to actually do (the missing pieces)

1. **Set `http-max-queued-requests` explicitly** to a value matched to your
   throughput (e.g. ~5 s of capacity at your req/s). This is the load-shed
   switch — off by default. Configure it at the LB *and* in RHBK.
2. **Cap the executor pool to your CPU limit** (`http-pool-max-threads`) and
   leave 150% CPU head-room so Pods aren't throttled — `rhbk-26-2-concepts-threads.md:24-27`,
   `rhbk-26-2-concepts-memory-and-cpu-sizing.md:35`.
3. **Right-size the DB pool** (`db-pool-max-size`) so threads aren't piling up
   waiting for connections — `rhbk-26-2-concepts-threads.md:28-34`.
4. **Set a real container memory limit** and size it from the 70% heap / 300 MB
   non-heap formula; don't leave it unset — `rhbk-26-2-containers.md:216-234`.
5. **Diagnose before adding RAM.** "Before increasing the amount of memory
   available to the JVM, in particular when experiencing an out of memory error,
   it is best to determine what is contributing to the increased footprint using
   a heap dump. Excessive response times may also indicate the HTTP work queue
   is too large and tuning for load shedding would be better than simply
   providing more memory." — `rhbk-26-2-getting-started-scaling-and-tuning.md:27`.

**Caveat (inferred):** the exact root cause in *your* cluster needs the
discriminating evidence — a heap dump plus the DB-pool / thread-queue metrics.
If you never set the queue cap, the unbounded queue is the prime suspect; if you
did set it, look at thread-count vs CPU-limit throttling and DB-pool exhaustion
next. Also note a separate, security-driven memory-exhaustion path:
CVE-2025-2559 (unbounded JWT token caching from a trusted client with long-lived
tokens) — `rhbk-26-0-red-hat-build-of-keycloak-26-0.md:52`.

## See also

- [[rhbk-oscp-scaling-resources]]  (wanted page — scaling/resource tuning synthesis)
- [[sso-implementation-review]]   (review MOC — symptom→cause index)

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)

- `kb:rhbk-26-2-concepts-threads` — Concepts for configuring thread pools (HA Guide 26.2), §5.1.2–5.1.5
- `kb:rhbk-26-2-configuration-production` — Configuring RHBK for production (Server Config Guide 26.2), §2.4 "Limit the number of queued requests"
- `kb:rhbk-26-2-concepts-memory-and-cpu-sizing` — Concepts for sizing CPU and memory (HA Guide 26.2), §6.1
- `kb:rhbk-26-2-getting-started-scaling-and-tuning` — Scaling (Getting Started Guide 26.2), §2.1
- `kb:rhbk-26-2-containers` — Container heap percentages (`-XX:MaxRAMPercentage=70`, ~300 MB non-heap)
- `kb:rhbk-26-0-deploy-keycloak-kubernetes` — example `http-max-queued-requests` value `"1000"`
- `kb:rhbk-26-0-red-hat-build-of-keycloak-26-0` — CVE-2025-2559 JWT token cache exhaustion (DoS)
- `kb:rhbk-26-2-metrics-for-troubleshooting` — DB connection pool exhaustion metric

### Wiki

- Newly filed: [[rhbk-login-storm-oom-queue-cap]] (this page)
- Wanted (not yet written): [[rhbk-oscp-scaling-resources]], [[sso-implementation-review]]
- No pre-existing synthesis page was used; the answer was derived directly from
  the `reference/keycloak/` ground-truth tier (extractive).
