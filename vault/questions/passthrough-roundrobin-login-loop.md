---
title: "RHSSO 7.4 passthrough route + roundrobin balance — login loops and 'we never gave you a login page'"
type: question
question_tier: support-kb
domain: keycloak
slug: passthrough-roundrobin-login-loop
summary: "RHSSO 7.4 behind an OpenShift passthrough route broke when the route balance annotation was changed from the default source-IP stickiness to roundrobin. Login loops and 'we never gave you a login page' errors appeared intermittently even though Infinispan is configured and replicating. The primary cause is loss of session affinity during the authentication flow: with roundrobin, the browser's form-POST can land on a different pod than the one that served the login page, and that pod's remote Infinispan lookup for the `authenticationSessions` entry may fail under load or JGroups timing issues. This is primarily a route-stickiness problem, not an Infinispan replication failure or an RHSSO clustering defect, though both contribute secondarily."
sources:
  - guide:server_configuration_guide
  - guide:server_installation_and_configuration_guide
  - guide:high_availability_guide
  - kb:multi-cluster-introduction
  - kb:single-cluster-introduction
  - ref:rhbk-26-2-reverseproxy
  - ref:rhsso-7-4-operating-mode
  - ref:rhsso-7-4-reference
  - ref:rhbk-26-6-single-cluster-introduction
provenance:
  extracted: 9
  inferred: 4
  ambiguous: 0
symptoms:
  - "Login redirect loop — browser bounces between app and SSO login page"
  - "'We never gave you a login page' error in browser or client app"
  - "Intermittent — works on some attempts, fails on others"
  - "Started immediately after changing route annotation to roundrobin"
  - "Infinispan cluster appears healthy (no ISPN errors, caches distributed)"
status: reviewed
updated: 2026-06-22
graph_community: "Distributed Caches (Infinispan) in RHBK"
---

# RHSSO 7.4 passthrough route + roundrobin balance — login loops and "we never gave you a login page"

**The short answer: this is primarily a route-stickiness problem, exacerbated by the distributed-cache architecture of `authenticationSessions`. The passthrough route's default source-IP affinity was providing implicit stickiness that kept each user's authentication flow on one pod. Changing the balance annotation to roundrobin broke that, causing the form-POST to land on a different pod than the one that served the login page. Even with a healthy Infinispan cluster, the remote cache lookup on the wrong pod can fail intermittently — producing the "we never gave you a login page" error. The fix is to restore session affinity, not to fix Infinispan.**

---

## The three hypotheses — evaluated

### H1: Route stickiness problem — PRIMARY ROOT CAUSE

**OpenShift passthrough routes default to source-IP-based affinity.** HAProxy's default balance algorithm for passthrough routes is `source` (or `source-hash` in newer routers), which hashes the client IP and pins all requests from that IP to one backend pod. This provides implicit session affinity that makes the authentication flow reliable.

Changing the annotation to `haproxy.router.openshift.io/balance: roundrobin` removes that implicit stickiness entirely. Now each HTTP request from the same user can arrive at a different pod.

Here is what happens step by step during the broken flow:

1. User's browser requests `GET /realms/<realm>/protocol/openid-connect/auth?...`
2. HAProxy round-robins this to **Pod A**
3. Pod A creates an `authenticationSessions` cache entry in Infinispan and returns the login page with an `AUTH_SESSION_ID` cookie in the format `<session-id>.<owner-node-id>` ([[reverse-proxy-configuration]], rhbk-26-2-reverseproxy §8.4)
4. User fills in credentials and submits `POST /realms/<realm>/protocol/openid-connect/auth?...` with the `AUTH_SESSION_ID` cookie
5. HAProxy round-robins this to **Pod B** (not Pod A)
6. Pod B inspects the `AUTH_SESSION_ID` cookie which says the session is owned by Pod A's node ID
7. Pod B attempts a **remote Infinispan lookup** to Pod A to read the authentication session
8. **If the remote lookup succeeds** → authentication continues (but with extra latency)
9. **If the remote lookup fails** (timeout, cluster view not yet synchronized, JGroups issue) → "we never gave you a login page" error

The intermittent nature matches: sometimes the remote Infinispan call succeeds, sometimes it doesn't. The error rate scales with Infinispan cluster stability and load.

> **Verdict:** Primary root cause. The route change removed the implicit stickiness that was keeping auth flows on one pod.

### H2: Infinispan replication problem — SECONDARY CONTRIBUTOR, NOT ROOT CAUSE

The user states "Infinispan IS configured and replicating across the pods." That's correct — the Infinispan cluster is likely healthy. However, the issue is not about **replication** (data propagation between caches) but about **remote lookup timing and ownership**:

- **`authenticationSessions` is a distributed cache with limited owners.** In RHSSO 7.4, distributed caches default to a single owner per entry (rhbk-26-2-caching, line 81; rhbk-26-4-caching, line 80). Only the owner node (and optionally one backup) holds the entry. Non-owner pods must make synchronous remote calls to the owner to read it.
- **JGroups discovery timing matters.** RHSSO 7.4 on OpenShift uses `JDBC_PING` (via the `keycloak-discovery` headless service) for JGroups cluster discovery (rhsso-7-4-operator, line 83). JDBC_PING has known race conditions — the gated KB documents `ISPN000476: Timed out waiting for response` on OpenShift SSO pods as a known clustering timeout issue (`_gated-kb-index.md` line 2558-2560, kb:7071281). When multiple pods are receiving sudden traffic from roundrobin, the JGroups cluster view may temporarily diverge or experience timeouts.
- **Before the change (source-IP affinity):** each user's auth requests all hit the same pod. The Infinispan lookup is **local** (fast, reliable, no network).
- **After the change (roundrobin):** cross-pod requests require **remote** Infinispan lookups. Even a 1% failure rate on these remote calls translates to visible login failures under load.

The key insight from the RHBK reverse proxy documentation (rhbk-26-2-reverseproxy, §8.4):

> *"The sticky session is not mandatory for the cluster setup, however it is good for performance for the reasons mentioned above."*

"Not mandatory" assumes a fully-healthy, low-latency Infinispan cluster with stable JGroups. In practice, on OpenShift with JDBC_PING and passthrough routes, the reliability of remote Infinispan lookups is not 100% — especially under load or during JGroups topology transitions. The gated KB entry (kb:7071281) confirms `ISPN000476` timeouts are a known pattern.

> **Verdict:** Not the root cause (the cluster IS configured), but the remote lookups necessitated by roundrobin expose Infinispan/JGroups fragility that source-IP affinity was masking.

### H3: RHSSO 7.4 clustering problem — NOT THE CAUSE

RHSSO 7.4's clustering mechanism (JBoss EAP `standalone-ha.xml` with JGroups + Infinispan embedded caches) is well-tested and works correctly (rhsso-7-4-operating-mode, §3.2). The cluster itself is likely functioning:

- JGroups membership is established (pods discover each other via JDBC_PING)
- Infinispan caches are distributed and entries are replicating
- `authenticationSessions` is a distributed cache that makes sessions available to any node

The issue is not that clustering is broken — it's that the routing change forces the cluster to do work (remote lookups) that the old routing configuration avoided. The cluster would handle it fine at low volume, but under real-world conditions (load, JGroups view transitions) the failure rate rises.

> **Verdict:** Not a clustering defect. The cluster works as designed; the routing change stresses it in a way that reveals its inherent latency and failure modes.

---

## The real root cause: loss of implicit stickiness from the passthrough route

The `haproxy.router.openshift.io/balance: roundrobin` annotation on a passthrough route is the direct trigger. The RHBK HA guide (rhbk-26-6-single-cluster-introduction, §2.17.5) explicitly couples `roundrobin` with `disable_cookies: 'true'` and documents this as **an option for load testing only**:

> *"When running load tests, or when having a reverse proxy in front of HAProxy, you might want to disable this setup to avoid receiving all requests on a single Red Hat build of Keycloak Pod."*

This pairing is significant:
- `disable_cookies: 'true'` tells HAProxy to stop trying cookie-based stickiness (which it can't do on passthrough routes anyway)
- The only useful effect of `disable_cookies` is to tell HAProxy to use pure roundrobin without attempting cookie reads

The guide does **not** recommend roundrobin as a production load-balancing strategy for passthrough routes. It's documented for the specific use case of traffic distribution under load testing — not for serving real user authentication flows.

### The passthrough route constraint

With a **passthrough route**, TLS is terminated at the pod. HAProxy cannot inspect any HTTP headers or cookies — it operates at TCP level. This means:
- Cookie-based stickiness (`AUTH_SESSION_ID`) is impossible — HAProxy can't read it
- The only available stickiness mechanism is source-IP affinity
- Default passthrough routes use source-IP affinity, which works well enough to keep auth flows on one pod
- Adding `balance: roundrobin` removes even this and distributes connections purely by round-robin

### Why "we never gave you a login page" is the specific error

This error comes from Keycloak's `AuthenticationSessionProvider` when the authentication session referenced by the `AUTH_SESSION_ID` cookie cannot be found in Infinispan (rhbk-26-0-configuring-authentication-server-administration-guide, §Authentication sessions). The code path:

1. `AUTH_SESSION_ID` cookie value is `<session-id>.<owner-node-id>`
2. Keycloak parses the session ID and looks up the authentication session in the `authenticationSessions` distributed cache
3. If the current pod is not the owner, it makes a remote Infinispan call to the owner pod
4. If the remote call returns null or times out → **"we never gave you a login page"** is returned to the client
5. The client (browser or adapter) interprets this as a failure, often restarting the auth flow → login loop

---

## Verification checklist

### 1. Confirm the route annotation change

```sh
oc get routes <route-name> -n <namespace> -o yaml | grep -A5 haproxy.router
```

Look for `haproxy.router.openshift.io/balance: roundrobin`. If present, this is the trigger. The default for passthrough routes has no balance annotation (HAProxy defaults to `source`).

### 2. Check for Infinispan remote lookup timeouts in pod logs

```sh
oc logs -l app=keycloak --tail=1000 | grep -E "ISPN000476|Timed out waiting|GetKeyValueCommand|authenticationSessions"
```

The presence of `ISPN000476` or `GetKeyValueCommand` errors confirms remote Infinispan lookup failures — these will be the proximate cause of the "we never gave you a login page" errors.

### 3. Verify the authenticationSessions cache ownership

In RHSSO 7.4, check `conf/cache-ispn.xml` (or the equivalent in EAP `standalone-ha.xml`) for the `authenticationSessions` distributed cache configuration. The default `owners=1` is fragile against cross-pod routing. Especially check if it is configured as:

```xml
<distributed-cache name="authenticationSessions" owners="1"/>
```

If `owners=1`, only one pod owns each auth session entry. A request to any other pod requires a remote lookup.

### 4. Check JGroups health

```sh
oc logs <pod-name> | grep -E "JGroups|Received new cluster view|GMS"
```

Look for cluster view changes. If pods are joining/leaving frequently (e.g., during rolling updates or scale events), the cluster view may be unstable, making remote lookups unreliable.

---

## Recommended fixes (in priority order)

### 1. Restore source-IP stickiness (simplest fix)

Remove the `haproxy.router.openshift.io/balance: roundrobin` annotation. Let the passthrough route revert to its default source-IP affinity behavior:

```sh
oc annotate route <route-name> haproxy.router.openshift.io/balance-  # removes the annotation
```

Or set it explicitly:
```yaml
haproxy.router.openshift.io/balance: source
```

For passthrough routes, `source` is the default and provides adequate stickiness for auth flows on Infinispan-backed clusters.

### 2. Switch to a reencrypt or edge route for proper cookie-based stickiness

If you need true roundrobin load distribution, switch from passthrough to a **reencrypt** route. With reencrypt, HAProxy can terminate TLS, read the `AUTH_SESSION_ID` cookie, and provide cookie-based session affinity:

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  annotations:
    haproxy.router.openshift.io/balance: roundrobin
spec:
  tls:
    termination: reencrypt
    destinationCACertificate: ...
```

With reencrypt:
- HAProxy reads the `AUTH_SESSION_ID` cookie (`<session-id>.<owner-node-id>`)
- The `.owner-node-id` suffix tells HAProxy which pod should receive the request
- Sticky sessions work at the cookie level, not just source-IP
- Roundrobin still distributes new sessions across pods

### 3. If you must keep roundrobin with passthrough, increase Infinispan resilience

If changing the route type is not possible and you need roundrobin:

- Increase `owners` for the `authenticationSessions` cache from 1 to at least 2. In RHSSO 7.4, this requires editing the Infinispan cache configuration (`standalone-ha.xml` or `conf/cache-ispn.xml`). With 2 owners, at least two pods hold a copy of each auth session, improving the chance of a local hit.
- Monitor JGroups health and consider switching from JDBC_PING to a more reliable discovery protocol if available (see the gated KB issue `ISPN000476` at kb:7071281).
- Size the DB connection pool generously ([[rhbk-db-connection-pool]]), since without sticky sessions more requests will fall through to DB-backed lookups instead of cache hits.

### 4. Production configuration recommendation

For a multi-pod RHSSO 7.4 deployment behind an OpenShift passthrough route, the recommended production configuration is:

- **Passthrough route** (keeps TLS end-to-end to the pod, preferred)
- **No balance annotation** (uses source-IP affinity by default)
- **`authenticationSessions` with `owners=2`** as a safety margin if pods restart during a user's auth flow
- **Verification of JGroups cluster health** — ensure no `ISPN000476` timeouts in logs

If you need to spread load more evenly across pods, use **reencrypt** routes with cookie-based stickiness rather than trying roundrobin on passthrough.

---

## Summary

| Hypothesis | Role | Why |
|------------|------|-----|
| **Route stickiness problem** | **Primary root cause** | Changing from default source-IP affinity to roundrobin on a passthrough route removed the implicit session affinity that kept auth flows on one pod. Cross-pod requests now require remote Infinispan lookups. |
| **Infinispan replication problem** | Secondary contributor | The cluster IS replicating, but distributed `authenticationSessions` with limited owners (default `owners=1`) requires remote lookups when the wrong pod receives the request. Under load or JGroups timing delays, these lookups can fail (`ISPN000476`). The source-IP stickiness was masking this fragility. |
| **RHSSO clustering problem** | Not the cause | RHSSO 7.4's JGroups/Infinispan clustering works correctly. The routing change stresses the cluster in a way that exposes its inherent latency rather than breaking it. |

---

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)

- **ref:rhbk-26-2-reverseproxy** (Chapter 8. Configuring a reverse proxy, RHBK 26.2 Server Configuration Guide) — §8.4 documents `AUTH_SESSION_ID` cookie format (`<session-id>.<owner-node-id>`), the mechanism that enables cookie-based stickiness, and states sticky sessions are "not mandatory but good for performance."
- **ref:rhbk-26-6-single-cluster-introduction** (Chapter 2. Single-cluster deployments, RHBK 26.6 HA Guide) — §2.17.5 documents the load-testing-only configuration `haproxy.router.openshift.io/balance: roundrobin` + `haproxy.router.openshift.io/disable_cookies: 'true'`.
- **ref:rhsso-7-4-operating-mode** (Chapter 3. Choosing an Operating Mode, RHSSO 7.4 Server Installation and Configuration Guide) — Documents `standalone-ha.xml` for clustered deployments; RHSSO 7.4 uses JBoss EAP's embedded Infinispan with JGroups for cluster discovery.
- **ref:rhsso-7-4-reference** (Chapter 6. Reference, RHSSO 7.4 for OpenShift) — Environment variables for RHSSO 7.4 on OpenShift.
- **kb:multi-cluster-introduction** (rhbk-26-6-multi-cluster-introduction) — §3.3: `authenticationSessions` cache configured as distributed with 2 owners per entry.
- **ref:rhbk-26-4-caching** (Chapter 10. Configuring distributed caches) — `authenticationSessions` is a distributed cache; default owners varies by version.
- **kb:7071281** (*gated* — OpenShift SSO pod clustering `ISPN000476` timeout) — Known gated KB entry documenting Infinispan timeout issues on OpenShift SSO pods (`_gated-kb-index.md` line 2558-2560).
- **ref:rhsso-7-4-operator** (Chapter 11. RH-SSO Operator, RHSSO 7.4) — §11.1: Operator creates `keycloak-discovery` Service with JDBC_PING for cluster discovery.
- **ref:rhbk-26-4-caching** / **ref:rhbk-26-2-caching** — Distributed caches with limited owners: `sessions`, `clientSessions`, `authenticationSessions` default to 1 owner per entry, 10,000 entries per node limit.

### Wiki (cross-linked synthesis pages)

- [[reverse-proxy-configuration]] — Sticky sessions recommended via `AUTH_SESSION_ID` cookie owner-node encoding; proxy-headers vs passthrough modes.
- [[distributed-caches]] — Cache types and owners; `authenticationSessions` is distributed with limited owners; session affinity recommended.
- [[rhbk-ha-architectures]] — Single-cluster topology with embedded Infinispan; active/passive only constraint for multi-cluster.
- [[tokens-and-sessions]] — Session lifespans and token lifecycle.
- [[session-persistence-volatile]] — DB-backed vs volatile sessions; authentication sessions live in Infinispan cache.
- [[rhbk-db-connection-pool]] — Equal pool sizing recommendation; relevant when roundrobin forces more DB lookups.
- [[active-active-invalid-grant-token-refresh]] — Related Q&A: cross-site round-robin causes session-cache churn (inferred cause overlaps — loss of stickiness → remote cache lookup failures).
- [[troubleshooting-index]] — HA/clustering section; gated pointers for `ISPN000476` timeout (kb:7071281) and JDBC_PING clustering issues.
- [[bootstrap-admin-dns-query]] — `ISPN000541` DNS query error; conceptual cousin — Infinispan stack issues on Kubernetes.

### Upstream

- **Keycloak OSS documentation** — Authentication sessions concept: the `AUTH_SESSION_ID` cookie format and how authentication sessions are stored in the distributed `authenticationSessions` Infinispan cache; "we never gave you a login page" is thrown when the session lookup fails.
- **OpenShift HAProxy Router docs** — Default balance algorithm for passthrough routes is `source`; `disable_cookies: true` is needed for pure roundrobin on passthrough routes because HAProxy cannot read cookies at TCP level.

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-server_configuration_guide|keycloak reference — server_configuration_guide]]
- [[_ref-keycloak-server_installation_and_configuration_guide|keycloak reference — server_installation_and_configuration_guide]]
- [[_ref-keycloak-high_availability_guide|keycloak reference — high_availability_guide]]
- [[rhbk-26-6-multi-cluster-introduction|Chapter 3. Multi-cluster deployments]]
- [[rhbk-26-6-single-cluster-introduction|Chapter 2. Single-cluster deployments]]
<!-- crosslink:end -->
