# OpenShift Container Platform — what it adds over Kubernetes — distilled notes

Source: Red Hat OpenShift Container Platform 4 docs
(<https://docs.redhat.com/en/documentation/openshift_container_platform/4.22>), versions
4.8 → 4.22. Paraphrased. OpenShift IS a Kubernetes distribution — everything in the
kubernetes-* notes applies; below are the platform additions.

## Cluster operating model — "operators all the way down"
- An OCP 4 cluster is managed by the **Cluster Version Operator (CVO)**, which drives a
  set of **ClusterOperators** (one per platform subsystem: `authentication`, `ingress`,
  `network`, `etcd`, `monitoring`, …). `oc get clusteroperators` shows
  Available/Progressing/Degraded — the first triage surface for cluster health.
- **MachineConfig / Machine Config Operator (MCO)** manages node OS config (RHCOS);
  changes roll out by draining + rebooting nodes per MachineConfigPool.
- **Operator Lifecycle Manager (OLM)** installs/updates Operators from catalogs via
  `Subscription` + `ClusterServiceVersion (CSV)` objects.

## App-facing additions
- **Route** — native external HTTP(S) exposure via the HAProxy Ingress router
  (edge/passthrough/re-encrypt TLS). See [[kubernetes-networking]].
- **BuildConfig + Source-to-Image (S2I)** — build container images *in-cluster* from
  source; **ImageStreams** track image tags and trigger redeploys on a new image.
- **Projects** — an OpenShift Project is a Kubernetes Namespace with extra annotations +
  self-service lifecycle.

## Security additions (stricter than vanilla Kubernetes by default)
- **Security Context Constraints (SCC)** — cluster policy controlling what a pod may do
  (run as root?, host networking?, volume types?). The default `restricted-v2` SCC runs
  containers with a **random non-root UID** and drops capabilities — a frequent reason a
  community image that assumes root fails on OCP but runs on plain Kubernetes.
- **Built-in OAuth server** — OCP ships an integrated OAuth server + identity providers
  (htpasswd, LDAP, OIDC, …); users/groups bind to RBAC. (Note: OCP's OAuth server is its
  own component, distinct from a Keycloak/RHBK deployment, though RHBK can be an OIDC IdP.)
- **RBAC** is enabled and enforced by default; **ServiceAccounts** carry pod identity.

## Versioning
- OCP 4 releases are tied to upstream Kubernetes versions (each OCP minor ≈ one k8s
  minor). Upgrades are operator-driven over channels (`stable-4.x`); EUS (Extended Update
  Support) channels allow even-minor-to-even-minor hops. Version-specific behavior should
  always name the OCP minor (4.8 … 4.22).
