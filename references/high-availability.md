# Red Hat build of Keycloak 26.6 — High Availability & Clustering

Internal runbook for HA/clustering of RHBK 26.6. Grounded in the RHBK High Availability Guide
(26.6 overview/single-cluster/multi-cluster + 26.2 concepts/blueprints; noted where 26.2-shared).
Air-gap lens applied: no cloud cache/DB services exist disconnected — use Red Hat Data Grid (RHDG)
on OpenShift and an on-prem PostgreSQL; replace public hosts with `example.internal`, secrets as `***`.

> Platform requirement (all architectures): RHBK must run on a properly configured OpenShift
> cluster. Clusters spanning multiple sites (single-cluster multi-AZ, or multi-cluster) must follow
> the *Guidance for Red Hat OpenShift Container Platform Clusters*. Availability of the overall
> service is the customer's responsibility.

---

## 1. Architectures at a glance

RHBK 26.6 documents **two** HA architectures.

| Architecture | Topology | Tolerates | Key cost / constraint |
|---|---|---|---|
| **Single-cluster** | One OpenShift cluster, optionally spread across up to 3 AZs / data centers | AZ / data-center failure (if multi-AZ) | OpenShift cluster is a single point of failure; control-plane failure can hit all pods |
| **Multi-cluster** (cross-site / active-active) | Two RHBK clusters in two OpenShift clusters, two AZs / data centers | AZ failure **and** OpenShift-cluster failure; bridges non-transparent networks | External load balancer + a separate Data Grid cluster per site; 2 control planes; **not supported with 3+ AZs** |

Single-cluster uses RHBK's **embedded Infinispan** caches with all instances on a transparent
network. Multi-cluster adds an **external Data Grid (RHDG)** per site to bridge non-transparent
networks and survive a whole OpenShift cluster loss.

---

## 2. Single-cluster deployments

### 2.1 When to use
- Infrastructure with transparent networking (e.g. a single OpenShift cluster).
- All healthy RHBK instances handle user requests.
- Constrained to a single region; planned maintenance outages permitted.
- Within a defined user/request count; periodic outages acceptable.

### 2.2 Tested / supported configuration
- OpenShift **4.17 or later** (regularly tested on **4.18**); ROSA HCP across three AWS AZs in one
  region in the tested setup.
- At least one worker node per AZ.
- Pods schedulable across **up to three** AZs (cloud) or **up to three** data centers (on-prem) *if*
  OpenShift supports spanning them and latency requirements are met.
- Database: from the supported list; multi-AZ deployments need a DB that tolerates zone failures and
  **synchronously replicates** between replicas. Tested with **Amazon Aurora PostgreSQL 17.5** (multi-AZ).

### 2.3 Latency requirement (hard)
- Round-trip latency **less than 10 ms** between RHBK instances is **required**.
- **< 5 ms suggested.** Reliable network between zones required to avoid latency/throughput/connectivity issues.

### 2.4 Maximum tested load
- 1,000,000 users
- 300 requests per second

### 2.5 Cache topology (embedded Infinispan)
Operator default topology spread constraints prefer distinct nodes and distinct AZs (`whenUnsatisfiable: ScheduleAnyway`):

```yaml
topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: "topology.kubernetes.io/zone"
    whenUnsatisfiable: "ScheduleAnyway"
    labelSelector:
      matchLabels:
        app: "keycloak"
        app.kubernetes.io/managed-by: "keycloak-operator"
        app.kubernetes.io/instance: "keycloak"
        app.kubernetes.io/component: "server"
  - maxSkew: 1
    topologyKey: "kubernetes.io/hostname"
    whenUnsatisfiable: "ScheduleAnyway"
    labelSelector:
      matchLabels: { ... same as above ... }
```

### 2.6 Failures survived (single-cluster)

**Single zone** (tested):

| Failure | RPO | RT (max observed) |
|---|---|---|
| RHBK Pod | No data loss | < 30 s |
| OpenShift Node | No data loss | < 30 s |
| RHBK clustering connectivity (unreachable pods removed from local view) | No data loss | Seconds to minutes |

**Multiple zones** (tested, assumes DB replicated across AZs):

| Failure | RPO | RT |
|---|---|---|
| Database node (reader promoted to writer) | No data loss | Seconds to minutes (DB-dependent) |
| RHBK pod | No data loss | < 30 s |
| OpenShift Node | No data loss | < 30 s |
| Availability-zone failure (deploy ≥ as many RHBK replicas as AZs) | No data loss | Seconds |
| Connectivity database (sync replication fails) | No data loss | Seconds to minutes (DB-dependent) |
| RHBK clustering connectivity | No data loss | Seconds to minutes |

### 2.7 Known limitations (single-cluster)
- **Downtime during RHBK upgrade rollouts.** For patch releases, enable *Checking if rolling updates are possible*.
- Multiple node failures can lose entries from the `authenticationSessions`, `loginFailures`, and
  `actionTokens` caches if failures ≥ the cache's `num_owners` (default **2**).
- Default `topologySpreadConstraints` with `whenUnsatisfiable: ScheduleAnyway` may cause data loss on
  node/zone failure if multiple pods land on the failed node/zone. Mitigate with
  `whenUnsatisfiable: DoNotSchedule` (evenly schedules, but constraints may leave instances undeployed).
  Infinispan is unaware of network topology, so loss is still possible if all `num_owner` copies sit
  on the failed node/zone — restrict instance count to nodes/zones via
  `requiredDuringSchedulingIgnoredDuringExecution` (at the cost of scalability).
- The Operator does not configure the site name in Pods (value not in the Downward API); the machine
  name is set from `spec.nodeName` of the scheduling node.

### 2.8 Building blocks (install order)
1. Two-or-more AZs with low-latency connection (< 5 ms suggested, < 10 ms required).
2. Synchronously replicated database across all AZs (blueprints: AWS Aurora multi-AZ; **CloudNativePG**
   multi-AZ — preferred on-prem option, with scheduled S3 backups + S3 restore + PITR).
3. Clustered RHBK with pods distributed across AZs (Operator blueprint).

> **Air-gap:** Aurora/ROSA blueprints are AWS-specific. On a disconnected OpenShift cluster, use
> **CloudNativePG** (Operator installed from a mirrored catalog) as the synchronously replicated
> PostgreSQL, store WAL/backups in an on-prem S3-compatible object store, and mirror the RHBK image
> to your internal registry (`registry.example.internal`).

---

## 3. Multi-cluster deployments (cross-site / active-active)

Two independent RHBK deployments in **two sites**, connected by a low-latency network. Users, realms,
clients, sessions, and other entities live in a database **synchronously replicated** across both
sites; data is also cached in RHBK's local Infinispan caches. On change, the database is updated and
an invalidation message is sent to the other site via the **`work`** cache. Each site has its own
**external Data Grid (RHDG)** cluster leveraging Data Grid Cross-DC.

### 3.1 When to use
- Tolerate a full OpenShift-cluster failure.
- Bridge two networks without transparent networking.
- Regulatory compliance requiring distinct deployments.
- Constrained to a single AWS Region; planned maintenance outages permitted.

### 3.2 Tested / supported configuration
- **Two OpenShift single-AZ clusters in the same AWS Region**, ROSA HCP (supported: ROSA HCP **or**
  ROSA classic), each with all workers in a single AZ, OpenShift **4.18 (or later)**.
- Amazon Aurora PostgreSQL **17.5**: HA with a primary writer in one AZ and a synchronously
  replicated reader in the second AZ; both sites connect to the **same DB writer instance**.
- **AWS Global Accelerator** sending traffic to both ROSA clusters.
- **AWS Lambda** to automate failover (triggered by Prometheus / Alert Manager).
- **Only Data Grid version 8.5.3 or more recent patch releases** are supported for external Data Grid.

### 3.3 Latency requirement (hard)
- Round-trip latency **< 10 ms required**, **< 5 ms suggested**, reliable network between zones.
- **Two-site restriction:** tested and supported **only with two sites**. Each extra site amplifies
  latency (synchronous writes to every site) and failure probability — 3+ sites are **not supported**.

### 3.4 Maximum tested load
- 1,000,000 users
- 300 requests per second

### 3.5 Failures survived (multi-cluster)

| Failure | RPO | RT |
|---|---|---|
| Database node (reader promoted) | No data loss | Seconds to minutes (DB-dependent) |
| RHBK node | No data loss | < 30 s |
| Data Grid node (entries on ≥ 2 nodes) | No data loss | < 30 s |
| Data Grid cluster failure (site unavailable; LB detects → degraded) | No data loss¹ | Seconds to minutes (LB-dependent) |
| Connectivity Data Grid (other site marked offline; one site must be taken offline in LB) | No data loss¹ | Seconds to minutes (LB-dependent) |
| Connectivity database (sync replication fails) | No data loss¹ | Seconds to minutes (DB-dependent) |
| Site failure (LB redirects to other site) | No data loss¹ | Less than two minutes |

¹ Manual operations needed to restore the degraded setup. "No data loss" holds only if the setup is
not already degraded from a prior failure (all pending re-syncs complete).

### 3.6 Limitations (multi-cluster)
- During certain failure scenarios, downtime up to **5 minutes**.
- After certain failures, **manual intervention** may be required to bring the failed site back and restore redundancy.
- During certain switchover scenarios, downtime up to **5 minutes**.
- **Out-of-sync sites** (a synchronous Data Grid request fails) are hard to monitor and need a full
  manual Data Grid re-sync. Monitor cache-entry counts in both sites + the RHBK log.
- Manual re-sync issues a **full state transfer**, stressing the system.

### 3.7 Consistency model (Q&A)
- Synchronous DB + synchronous Data Grid replication chosen to **prioritize consistency over
  availability**: the next request never returns stale data regardless of which site serves it.
- Low latency is required because each update can involve multiple inter-site round trips, amplifying latency.
- An asynchronous cluster would survive network failures more gracefully but risks data loss
  (e.g. users logging in with an old password after lost/uninvalidated changes). RHBK opts for consistency.

### 3.8 Building blocks (install order)
1. Two sites with low-latency connection (two AWS AZs in one region; not multi-region).
2. ROSA per AZ (not a single stretched cluster — would be a SPOF if misconfigured).
3. Synchronously replicated database across both sites (Aurora multi-AZ blueprint).
4. Data Grid (RHDG) using Cross-DC, sites connected via Data Grid's **Gossip Router**.
5. Clustered RHBK per site, connected to the external Data Grid.
6. Load balancer probing `/lb-check` per site + automation to detect inter-site Data Grid connectivity loss.

> **Air-gap:** Global Accelerator/Lambda/Aurora are AWS-only. On-prem, replace with two RHDG clusters
> on two OpenShift clusters (Cross-DC over OpenShift Route/Gossip Router), an external L4 load balancer
> with health-based fencing, and an on-prem synchronously replicated PostgreSQL. Mirror RHDG ≥ 8.5.3
> and RHBK images to `registry.example.internal`.

---

## 4. Cache names, roles, and persistent user sessions

RHBK distributed caches used in multi-site (created in the external Data Grid). RHBK **auto-creates**
these caches on first startup if missing; with the Operator, deploy the `Cache` CRs **before any RHBK
Pod starts**.

| Cache | Role |
|---|---|
| `actionTokens` | Action tokens (e.g. email-action / reset flows) |
| `authenticationSessions` | In-flight authentication sessions (indexed entity `keycloak.RootAuthenticationSessionEntity`) |
| `loginFailures` | Login-failure / brute-force counters (indexed entity `keycloak.LoginFailureEntity`) |
| `work` | Cross-node / cross-site cache-invalidation messages |

**Persistent user sessions:** By default RHBK **stores user sessions in the database**, not in
in-memory caches. In the multi-cluster reference architecture all user and client sessions are stored
in the DB and are **not cached in-memory** (single-site setups may cache a fixed number for slightly
higher performance). DB budget for sessions: **1400 Write IOPS** and **0.35–0.7 vCPU** per 100
login/logout/refresh requests per second on an Aurora multi-AZ DB.

> Recovery note: after a DB point-in-time restore, the `offline_user_session` / `offline_client_session`
> tables can **revive logged-out sessions** (security concern). Options: `TRUNCATE` both tables (clear
> all), `DELETE` rows where `offline_flag = '0'` (clear regular, keep offline), or leave them to expire
> by idle timeout. Also run `TRUNCATE jgroups_ping;` after a restore to avoid up-to-20-second startup
> delays from stale discovery entries.

### Example `Cache` CR (Site-A, active-active — best data consistency)

```yaml
apiVersion: infinispan.org/v2beta1
kind: Cache
metadata:
  name: actiontokens
  namespace: keycloak
spec:
  clusterName: infinispan
  name: actionTokens
  template: |-
    distributedCache:
      mode: "SYNC"
      owners: "2"
      statistics: "true"
      remoteTimeout: "5000"
      encoding:
        media-type: "application/x-protostream"
      locking:
        acquireTimeout: "4000"
      transaction:
        mode: "NON_DURABLE_XA"
        locking: "PESSIMISTIC"
      stateTransfer:
        chunkSize: "16"
      backups:
        site-b:
          backup:
            strategy: "SYNC"
            timeout: "4500"
            failurePolicy: "FAIL"
            stateTransfer:
              chunkSize: "16"
```

Consistency rationale (active-active):
- `transaction.mode: NON_DURABLE_XA` rolls back on concurrent cross-site conflicts.
- `backup.failurePolicy: FAIL` is **required** with `NON_DURABLE_XA`; throws an error so the
  transaction safely rolls back (RHBK then retries). Also prevents updating one site while the other is unreachable.
- `transaction.locking: PESSIMISTIC` is the **only supported** locking mode (`OPTIMISTIC` not recommended — network cost).
- `backup.strategy: SYNC` makes data visible/stored in the other site before the request completes.
- `backup.timeout` **must** be higher than `locking.acquireTimeout` (reduce `acquireTimeout` to fail fast on deadlock).

For Site-B, the same CRs use `backups.site-a` instead of `backups.site-b`.

---

## 5. Connecting RHBK to an external Infinispan / Red Hat Data Grid

RHBK CR options to point at an external Data Grid (set via `spec.additionalOptions`):

| Option | Type | Default / notes |
|---|---|---|
| `cache-remote-host` | String | Hostname of the remote Data Grid cluster (e.g. `infinispan.keycloak.svc`) |
| `cache-remote-port` | Integer | Optional; defaults to `11222` (available only when remote host is set) |
| `cache-remote-username` | String | Available only when remote host is set; from a Secret `name`/`key` |
| `cache-remote-password` | String | Available only when remote host is set; from a Secret `name`/`key` |
| `cache-remote-backup-sites` | List | Available only when remote host is set; names of remote site(s) for **automatic cache creation** (caches created only if absent) |

> **Important:** `cache-remote-backup-sites` only creates caches in the **local** site. You must
> deploy the `Keycloak` CR in the **other** cluster too, or RHBK will not start until the caches exist
> in both clusters. (Same applies to auto-creation: RHBK does not start until all caches are present in both clusters.)

Connection security: RHBK connects to Data Grid over **TCP secured by TLS 1.3**, verifying Data Grid's
server certificate via RHBK's truststore. With the RHBK Operator on OpenShift, the Operator adds
`service-ca.crt` (which signs Data Grid certs) to the truststore automatically. In other environments,
add the necessary certificates to RHBK's truststore manually.

### Remote-store credential Secret + RHBK CR snippet

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: remote-store-secret
  namespace: keycloak
type: Opaque
data:
  username: ***   # base64 of the Data Grid user
  password: ***   # base64 of the Data Grid password
---
apiVersion: k8s.keycloak.org/v2beta1
kind: Keycloak
metadata:
  name: keycloak
  namespace: keycloak
spec:
  additionalOptions:
    - name: cache-remote-host
      value: "infinispan.keycloak.svc"
    - name: cache-remote-port
      value: "11222"
    - name: cache-remote-username
      secret: { name: remote-store-secret, key: username }
    - name: cache-remote-password
      secret: { name: remote-store-secret, key: password }
```

### Enabling multi-site features on the RHBK CR

```yaml
spec:
  update:
    strategy: Auto
  features:
    enabled:
      - rolling-updates:v2
      - multi-site            # enables multi-cluster support incl. the /lb-check probe
```

### Data Grid `Infinispan` CR (Cross-Site, Site-A — key fields)

```yaml
apiVersion: infinispan.org/v1
kind: Infinispan
metadata:
  name: infinispan
  namespace: keycloak
  annotations:
    infinispan.org/monitoring: 'true'     # allow Prometheus scraping
spec:
  replicas: 3
  jmx: { enabled: true }
  security:
    endpointSecretName: connect-secret    # username/password (role: admin)
  service:
    type: DataGrid
    sites:
      local:
        name: site-a
        expose: { type: Route }           # Cross-site over OpenShift Route + TLS SNI
        maxRelayNodes: 128
        encryption:
          transportKeyStore: { secretName: xsite-keystore-secret, alias: xsite, filename: keystore.p12 }
          routerKeyStore:    { secretName: xsite-keystore-secret, alias: xsite, filename: keystore.p12 }
          trustStore:        { secretName: xsite-truststore-secret, filename: truststore.p12 }
      locations:
        - name: site-b
          clusterName: infinispan
          namespace: keycloak
          url: openshift://api.site-b      # remote OpenShift API URL
          secretName: xsite-token-secret   # remote site access token
  upgrades: { type: InPlaceRolling }
```

Cross-site uses JGroups TLS sockets (keystore/truststore in OpenShift Secrets) and the **Gossip
Router**, reached via an OpenShift `Route` with TLS SNI. A `service-account-token` Secret + `view`
role per site lets the Data Grid Operator inspect the remote network and configure the local cluster.
The Data Grid `connect-secret` holds the endpoint credentials (`identities.yaml` with role `admin`).

Verify formation:

```bash
oc wait --for condition=WellFormed --timeout=300s infinispans.infinispan.org -n keycloak infinispan
oc wait --for condition=CrossSiteViewFormed --timeout=300s infinispans.infinispan.org -n keycloak infinispan
```

> **Air-gap:** No cloud cache service exists disconnected. Run **RHDG on OpenShift** via the Data Grid
> Operator (mirrored OLM catalog, RHDG ≥ 8.5.3). Generate keystore/truststore from your internal CA,
> point `url:` at the peer cluster's internal API (`openshift://api.site-b.example.internal`), and keep
> all credentials in OpenShift Secrets (`***`).

---

## 6. Load balancer, `/lb-check`, and health-based failover (fencing)

### 6.1 `/lb-check`
The load balancer probes the **`/lb-check`** URL of each site's RHBK deployment. A site staying in the
LB configuration means it is serving requests. The probe is exposed when the `multi-site` feature is enabled.

AWS Global Accelerator blueprint uses an NLB per ROSA cluster with these health-check service annotations:

| Annotation | Value (blueprint) | Meaning |
|---|---|---|
| `service.beta.kubernetes.io/aws-load-balancer-type` | `nlb` | Network Load Balancer |
| `aws-load-balancer-healthcheck-path` | `/lb-check` | Probe path |
| `aws-load-balancer-healthcheck-protocol` | `https` | Probe protocol |
| `aws-load-balancer-healthcheck-interval` | `10` | Probe interval (s) |
| `aws-load-balancer-healthcheck-healthy-threshold` | `3` | Probes to pass → healthy |
| `aws-load-balancer-healthcheck-unhealthy-threshold` | `3` | Probes to fail → unhealthy |

Each endpoint gets **weight 128** (half of max 255) so traffic splits evenly when both sites are
healthy. If a site fails, the Accelerator routes all traffic to the healthy site; if **both** are
unhealthy it **fails open** (forwards to a random site). RHBK CR for accelerator mode sets
`spec.hostname.hostname` to the Accelerator DNS name (`DnsName` or `DualStackDnsName`) and
`spec.ingress.enabled: false`.

### 6.2 Fencing (split-brain handling)
With only two sites a quorum is impossible, so RHBK uses **fencing**: when one site cannot reach the
other, only **one** site remains in the LB configuration and serves requests. Fencing also **disables
replication** between the two Data Grid clusters (Data Grid is configured with the `FAIL` failure
policy — consistency over availability), so the sites go **out-of-sync**.

Blueprint mechanism (AWS): a **Prometheus Alert** (`SiteOffline`, raised from Data Grid metrics) →
**Prometheus AlertManager** → **AWS Lambda** webhook. The Lambda inspects the Global Accelerator
EndpointGroup and removes the offline site, then calls the Data Grid REST endpoint to take the offline
site's backups offline:

```
POST https://{infinispan-endpoint}/rest/v2/container/x-site/backups/{offlinesite}?action=take-offline
```

Both sites may fire simultaneously in a true split-brain; the Lambda guards by allowing only one
instance at a time and always leaving one site in the LB. A fenced site is **not re-added
automatically** — re-add it only **after** re-synchronizing (see §7), via *Bringing a site online*.

> **Air-gap:** No Global Accelerator/Lambda. Implement the same pattern on-prem with your external L4
> LB's health checks against `/lb-check`, an Alertmanager webhook to an internal automation service,
> and the Data Grid REST `take-offline` call. Keep the webhook credential in a Secret (`***`).

---

## 7. Operational procedures (multi-site)

### 7.1 Take a site offline (maintenance/upgrade)
Remove the site from the LB so no traffic is routed to it. With Global Accelerator: find the NLB ARN
of the site to **keep online**, then `aws globalaccelerator update-endpoint-group` with **only** that
NLB's EndpointId (weight 128). On-prem: drop the offline site from the external LB pool.

### 7.2 Bring a site online
Re-add the site's NLB EndpointId back into the EndpointGroup (both sites, weight 128 each). **Only do
this after the two sites are synchronized** (§7.3).

### 7.3 Synchronize sites (after split-brain / maintenance)
Replaces the offline (secondary) site's data with the active site's data; all offline-site caches are
cleared first. Here `site-a` = active, `site-b` = offline (not in the LB EndpointGroup). Transferring
state may increase Data Grid response time / resource usage.

1. On the **offline** site, scale RHBK to **0** (clears RHBK caches; prevents RHBK↔Data Grid drift):
   set `spec.instances: 0` in the Keycloak CR.
2. Connect to Data Grid on the offline site:
   ```bash
   oc -n keycloak exec -it pods/infinispan-0 -- ./bin/cli.sh --trustall --connect https://127.0.0.1:11222
   ```
3. Disable replication offline→active so the clear does not propagate, and confirm `offline`:
   ```
   site take-offline --all-caches --site=site-a
   site status --all-caches --site=site-a      # expect: "offline"
   ```
   > **Warning:** ensure status is `offline`, otherwise the clear wipes **both** sites.
4. Clear the offline site's caches:
   ```
   clearcache actionTokens
   clearcache authenticationSessions
   clearcache loginFailures
   clearcache work
   ```
5. Re-enable replication offline→active and confirm `online`:
   ```
   site bring-online --all-caches --site=site-a
   site status --all-caches --site=site-a       # expect: "online"
   ```
6. On the **active** site (connect via CLI as above), push state to the offline site and wait:
   ```
   site push-site-state --all-caches --site=site-b
   site status --all-caches --site=site-b        # expect: "online"
   site push-site-status --cache=actionTokens
   site push-site-status --cache=authenticationSessions
   site push-site-status --cache=loginFailures
   site push-site-status --cache=work            # expect each: { "site-b" : "OK" }
   ```
   Retry per cache on error: `site push-site-state --cache=<cache-name> --site=site-b`. Then clear status:
   ```
   site clear-push-site-status --cache=actionTokens
   site clear-push-site-status --cache=authenticationSessions
   site clear-push-site-status --cache=loginFailures
   site clear-push-site-status --cache=work
   ```
7. On the secondary site, scale RHBK back to its original `spec.instances`.
8. AWS Aurora: no action. Global Accelerator / LB: re-add the site (§7.2).

### 7.4 Automating Data Grid CLI via the `Batch` CR
Automate the CLI on OpenShift (avoids passing credentials / parsing shell output). The RHBK 26.6
multi-cluster chapter uses `infinispan.org/v2beta1` (the 26.2 concepts chapter shows `v2alpha1`):

```yaml
apiVersion: infinispan.org/v2beta1
kind: Batch
metadata:
  name: take-offline
  namespace: keycloak
spec:
  cluster: infinispan
  config: |
    site take-offline --all-caches --site=site-a
    site status --all-caches --site=site-a
```

```bash
oc -n keycloak wait --for=jsonpath='{.status.phase}'=Succeeded Batch/take-offline
```

A `Batch` CR is a one-time event; modifying it has no effect. To re-run or after a failure, create a **new** `Batch` CR.

---

## 8. Health checks (multi-site)

| What | Command |
|---|---|
| RHBK overall/DB health (management port only; `health/ready` makes the Pod ready) | `curl -s https://keycloak:managementport/health` |
| LB cluster up | `curl -s https://keycloak-load-balancer-url/lb-check` |
| Per-site up | `curl -s https://keycloak_site_a_url/lb-check` / `..._site_b_url/lb-check` |
| Data Grid cache-manager health (no creds) | `curl -s https://infinispan_rest_url/rest/v2/cache-managers/default/health/status` |
| Data Grid full cache health (creds) | `curl -u <user>:<pwd> -s https://infinispan_rest_url/rest/v2/cache-managers/default/health` (pipe `jq` to compute `HEALTHY`/`UNHEALTHY`) |
| Data Grid cluster distribution | `curl <user>:<pwd> -s https://infinispan_rest_url/rest/v2/cluster\?action\=distribution` (`jq --argjson expectedCount 3 ...`) |
| Overall Data Grid system health | `oc get infinispan -n <NS> -o json \| jq '.items[].status.conditions' ...` |
| RHBK readiness / no rolling update | `oc wait --for=condition=Ready --timeout=10s keycloaks.k8s.keycloak.org/keycloak -n <NS>` and `oc wait --for=condition=RollingUpdate=False --timeout=10s ...` |

> Set `expectedCount` to the total number of Data Grid nodes when checking distribution.

---

## 9. Sizing, pools & threads (concepts — 26.2-shared)

### 9.1 CPU / memory
- Base memory for a Pod (Realm caches + 10,000 cached sessions): **1250 MB RAM**.
- Containers: RHBK uses **70%** of the memory limit for heap, ~**300 MB** non-heap. Memory limit =
  (target − 300 MB) / 0.7.
- **1 vCPU per 15 password-based logins/s** (tested to 300/s). **1 vCPU per 120 client-credential
  grants/s** (tested to 2000/s). **1 vCPU per 120 refresh-token requests/s** (tested to 435/s).
- Leave **150% extra CPU head-room** for spikes/startup/failover. Throttled pods degrade sharply.
- DB per 100 login/logout/refresh req/s: **1400 Write IOPS**, **0.35–0.7 vCPU**.
- With > 2500 concurrent clients, default 10,000-entry caches overflow → increase `users` cache by 2×
  and `realms` cache by 4× the concurrent client count.

### 9.2 Sizing a multi-cluster (active-active) setup
- Mirror the same pod count + memory on the second site; **DB sizing unchanged** (both sites → same writer).
- CPU/limit options: (a) full requests/limits on site 2 = immediate failover, costlier; (b) **−50%**
  requests/limits, scale 3→6 pods on failover (manual/HPA), cheaper, slower; (c) −50% requests but
  keep limits = no pod scaling but CPU pressure / slower responses at peak.

### 9.3 DB connection pool
- Set initial = min = max (`poolInitialSize` = `poolMinSize` = `poolMaxSize`, blueprint uses **30**) to
  avoid costly new connections and preserve server-side statement caching. PostgreSQL needs a query run
  ≥ 5× before it uses a server-side prepared statement.

### 9.4 Thread pools / load shedding
- JGroups (single-cluster inter-node comms) benefits from **virtual threads** on **OpenJDK 21+** with
  ≥ 4 cores (best: OpenJDK 25+) — reduces memory, removes thread-pool tuning.
- Quarkus executor pool: default max **50** (or more by cores); tune via `http-pool-max-threads`.
- Load shedding: `http-max-queued-requests` caps the queue; over-limit requests get **HTTP 503**
  (~200 req/s ⇒ queue 1000 ≈ 5 s max wait). Example CR: `additionalOptions: [{name: http-max-queued-requests, value: "1000"}]`.
- Liveness probe is non-blocking; overall/readiness probes can block on the DB and fail under high load.
- Ensure enough OS file handles (`ulimit -n`) and container memory for the thread count.

---

## 10. Quick decision matrix

| Need | Choose |
|---|---|
| Single OpenShift cluster, transparent network, simplest | **Single-cluster** (embedded Infinispan), multi-AZ for AZ-failure tolerance |
| Survive a full OpenShift-cluster loss / bridge non-transparent networks / regulatory separation | **Multi-cluster** (external RHDG Cross-DC, active-active) |
| 3+ sites in the cross-site sense | **Not supported** — max 2 sites multi-cluster; max 3 AZs single-cluster |
| Inter-instance / inter-site RTT | **< 10 ms required**, < 5 ms suggested |
| Air-gapped on-prem | RHDG on OpenShift via Operator (≥ 8.5.3), CloudNativePG sync replication, internal registry/CA, external LB with `/lb-check` fencing — **no cloud cache/DB/LB services** |

> **Support note:** any deviation from the tested/supported configurations is untested; issues may need
> to be reproduced in a tested environment for Red Hat support.

_Source: Red Hat build of Keycloak 26.6 High Availability Guide (docs.redhat.com), distilled offline._
