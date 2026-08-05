# RHBK Operator on OpenShift — Keycloak CR Reference — RHBK 26.6 (Offline Reference)

Operator install, basic deploy, realm import, advanced CR tuning, rolling updates, and custom images for the Red Hat build of Keycloak Operator on OpenShift. All CR YAML keys are verbatim from the docs. Pinned to RHBK 26.6.

CR group/version: `k8s.keycloak.org/v2beta1` (some fields documented under `v2alpha1`). Kinds: `Keycloak`, `KeycloakRealmImport`.

---

## 1. Operator installation (OLM / OperatorHub)

Install via OperatorHub: **Home → Operators → OperatorHub**, search "Keycloak", select, follow the screen. In the default Catalog the Operator is named `rhbk-operator`. Use the **channel** matching your desired RHBK version.

**Air-gap note:** OperatorHub on a disconnected cluster serves only from a **mirrored catalog** (your internal registry, e.g. `registry.example.internal`). The `rhbk-operator` package and the corresponding RHBK operand image must already be mirrored into that catalog/registry before install; the `redhat-operators` source must point at the mirrored catalog.

### 1.1 Manual approval for OLM upgrades (recommended)

Default OLM behavior auto-upgrades the Operator, which can: pull a matching RHBK operand image (unintended operand upgrade), break existing Keycloak CR config on major Operator upgrades, introduce new/changed CR fields, and block downgrade (DB migration is one-way). Use **Manual** approval.

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: rhbk-operator
  namespace: <target-namespace>
spec:
  channel: <desired-channel>
  name: rhbk-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  installPlanApproval: Manual
```

After install, every upgrade requires manual approval via OLM UI or CLI.

### 1.2 Namespace scope / multiple Operators

Watching multiple/all namespaces is **not fully supported**. To watch multiple namespaces, install multiple Operators. Key constraints:

| Concern | Behavior |
|---|---|
| CRDs | Shared cluster-wide; the **last installed** Operator's CRDs win and override existing ones. |
| Backward compat | Newer CRDs generally backward compatible (except eventual removal of long-deprecated fields). |
| Forward compat | Older CRDs may not be forward compatible; new fields can block install of older Operators. |
| Older Operators + new fields | Fail with a **deserialization error** for unrecognized fields. |

Recommendation: keep Operator versions aligned as closely as possible.

---

## 2. Basic deployment (Keycloak CR)

Prerequisites you provision yourself: **Database**, **Hostname**, **TLS certificate + key**. The Operator does **not** manage the database.

### 2.1 Secrets

```bash
oc create secret generic keycloak-db-secret \
  --from-literal=username=[your_database_username] \
  --from-literal=password=[your_database_password]
oc create secret tls example-tls-secret --cert certificate.pem --key key.pem
```

**Air-gap note:** store DB and TLS material in cluster Secrets; reference `registry.example.internal` for any operand image. Use `***` placeholders for secret values in shared runbooks; never commit real credentials.

### 2.2 Basic CR (TLS passthrough)

```yaml
apiVersion: k8s.keycloak.org/v2beta1
kind: Keycloak
metadata:
  name: example-kc
spec:
  instances: 1
  db:
    vendor: postgres
    host: postgres-db
    usernameSecret:
      name: keycloak-db-secret
      key: username
    passwordSecret:
      name: keycloak-db-secret
      key: password
  http:
    tlsSecret: example-tls-secret
  hostname:
    hostname: test.keycloak.org
  proxy:
    headers: xforwarded
```

### 2.3 Core CR field reference

| Field | Purpose |
|---|---|
| `spec.instances` | Replica count. |
| `spec.image` | Custom container image (see §6). |
| `spec.startOptimized` | `false` to allow non-optimized/build-time options with a custom image. |
| `spec.db.vendor` | DB vendor (e.g. `postgres`). |
| `spec.db.host` / `database` / `port` / `schema` | DB connection. |
| `spec.db.usernameSecret` / `passwordSecret` | `{name,key}` Secret refs for DB creds. |
| `spec.db.poolInitialSize` / `poolMinSize` / `poolMaxSize` | Connection pool sizing. |
| `spec.http.tlsSecret` | TLS Secret for HTTPS (passthrough when set on `http`). |
| `spec.http.httpEnabled` | Enable HTTP (required for edge/TLS termination). |
| `spec.http.httpPort` / `httpsPort` | Pod listen ports. |
| `spec.http.serviceHttpPort` / `serviceHttpsPort` | Override port exposed on the Service. |
| `spec.http.serviceName` | Override default `<cr-name>-service`. |
| `spec.http.labels` / `annotations` | Custom Service labels/annotations. |
| `spec.hostname.hostname` | Public hostname. |
| `spec.hostname.admin` / `hostname-admin` | Separate admin hostname (no ingress auto-created for it). |
| `spec.hostname.strict` | `false` to relax hostname (dev only). |
| `spec.hostname.backchannelDynamic` | Dynamic backchannel resolution. |
| `spec.ingress.enabled` | `false` disables built-in Ingress. |
| `spec.ingress.className` | IngressClass (e.g. `openshift-default`). |
| `spec.ingress.tlsSecret` | TLS Secret on Ingress (TLS termination/edge). |
| `spec.proxy.headers` | `forwarded` \| `xforwarded` \| `forwarded\|xforwarded`. |

If `proxy.headers` is unset, the Operator falls back to implicit `proxy=passthrough` (deprecation warnings; fallback to be removed). Passthrough TLS does not let Ingress rewrite headers — use reencrypt or edge when relying on `proxy.headers`.

### 2.4 Apply & verify

```bash
oc apply -f example-kc.yaml
oc get keycloaks/example-kc -o go-template='{{range .status.conditions}}CONDITION: {{.type}}{{"\n"}} STATUS: {{.status}}{{"\n"}} MESSAGE: {{.message}}{{"\n"}}{{end}}'
```

Ready output shows `Ready=true`, `HasErrors=false`, `RollingUpdate=false`.

### 2.5 Ingress / access modes

| Mode | How |
|---|---|
| TLS passthrough | `http.tlsSecret` set, Ingress enabled with **no** `tlsSecret` on it. |
| TLS termination (edge) | `http.httpEnabled: true` + `ingress.tlsSecret`. |
| Custom access | `ingress.enabled: false`, then create your own Route/Ingress to `<cr-name>-service`. |

OpenShift caveat: wildcard certs are not allowed on passthrough Routes with HTTP/2. In that case disable built-in ingress and create a reencrypt Route:

```bash
oc create route reencrypt --service=<keycloak-cr-name>-service --cert=<configured-certificate> --key=<certificate-key> --dest-ca-cert=<ca-certificate> --ca-cert=<ca-certificate> --hostname=<hostname>
```

With `ingress.className: openshift-default` you may leave `hostname.hostname` unset; the Operator assigns `ingress-namespace.appsDomain`.

### 2.6 Initial admin

Operator generates an arbitrary admin user/password stored in Secret `<cr-name>-initial-admin` (default user `temp-admin`).

```bash
oc get secret example-kc-initial-admin -o jsonpath='{.data.username}' | base64 --decode
oc get secret example-kc-initial-admin -o jsonpath='{.data.password}' | base64 --decode
```

Change default admin creds and enable MFA before production. Anyone able to create/edit `Keycloak`/`KeycloakRealmImport` CRs, set `spec.image`, or use `unsupported.podTemplate` must be a namespace-level admin (Secret access risk).

---

## 3. Automating realm import (KeycloakRealmImport CR)

```yaml
apiVersion: k8s.keycloak.org/v2beta1
kind: KeycloakRealmImport
metadata:
  name: my-realm-kc
spec:
  keycloakCRName: <name of the keycloak CR>
  realm:
    id: example-realm
    realm: example-realm
    displayName: ExampleRealm
    enabled: true
```

| Field | Notes |
|---|---|
| `spec.keycloakCRName` | Target Keycloak CR; **must be same namespace**. |
| `spec.realm` | Full `RealmRepresentation` (export JSON → convert to YAML → paste). |
| `spec.placeholders.<ENV_KEY>.secret` | `{name,key}` Secret ref → injects env var for placeholder replacement. |

**Caveats:** creates new realms only — never updates/overwrites/deletes; existing realm of same name is left untouched; drift back into the CR is not synced. **Delete the CR after import** to clean up the associated Job/Pod. Placeholders: Secrets only, same namespace; placeholder replacement exposes **all** env vars including sensitive ones.

```bash
oc get keycloakrealmimports/my-realm-kc -o go-template='{{range .status.conditions}}CONDITION: {{.type}}{{"\n"}} STATUS: {{.status}}{{"\n"}} MESSAGE: {{.message}}{{"\n"}}{{end}}'
```

Success: `Done=true`, `Started=false`, `HasErrors=false`.

---

## 4. Advanced configuration

### 4.1 First-class server options & additionalOptions

CR fields mirror server config names (e.g. server `https-port` → CR `httpsPort`). Options without a dedicated field go in `additionalOptions` as key-value pairs (name format = config-file key format):

```yaml
spec:
  additionalOptions:
    - name: spi-connections-http-client--default--connection-pool-size
      secret:
        name: http-client-secret
        key: poolSize
    - name: spi-email-template--mycustomprovider--enabled
      value: 'true'   # quote numbers/booleans
```

mTLS note: if `https-client-auth: required`, the management interface inherits it — also set `https-management-client-auth` to `request` or `none` so probes don't require a client cert.

### 4.2 Advanced CR field reference

| Field | Purpose |
|---|---|
| `spec.additionalOptions[]` | Arbitrary server options (`value` or `secret` ref). |
| `spec.env[]` | Raw container env vars (`value` or Secret ref). Do **not** use for anything with a first-class field/additionalOption (Operator logic ignores `spec.env`). |
| `spec.features.enabled` / `disabled` | Toggle server features. |
| `spec.transaction.xaEnabled` | XA transactions. |
| `spec.resources.requests` / `limits` | CPU/memory; defaults: requests memory `1700MiB`, limits memory `2GiB`. |
| `spec.readinessProbe` / `livenessProbe` / `startupProbe` | `periodSeconds`, `failureThreshold`. |
| `spec.scheduling` | `affinity`, `tolerations`, `topologySpreadConstraints`, `priorityClassName`. |
| `spec.update.scheduling` / `spec.import.scheduling` | Override server-Pod scheduling inherited by update/import Jobs (e.g. `{}` to clear). |
| `spec.httpManagement.port` | Management interface port. |
| `spec.truststores` | Map of named truststores from Secret/ConfigMap. |
| `spec.automountServiceAccountToken` | `false` to not mount SA token (also disables K8s CA truststore auto-discovery; cannot be `false` with external Infinispan / K8s SA IdP / custom providers using the K8s API). |
| `spec.bootstrapAdmin` | Bootstrap user/service-account Secret refs (`username`/`password` or `client-id`/`client-secret`). |
| `spec.tracing` | OpenTelemetry tracing (see §4.5). |
| `spec.networkPolicy.enabled` | Toggle auto NetworkPolicy; `http`/`https`/`management` rule lists. |
| `spec.serviceMonitor` | Tune/disable generated ServiceMonitor. |
| `spec.unsupported.podTemplate` | Raw Pod template merge (Tech Preview). |

### 4.3 Secret / ConfigMap references

Referenced Secrets/ConfigMaps must be in the **same namespace** as the CR. The Operator polls ~every minute; on a meaningful change it performs a **rolling restart** to pick up changes.

### 4.4 Truststores

```yaml
spec:
  truststores:
    my-truststore:
      secret:
        name: my-secret
```

Accepts PEM files or PKCS12 (`.p12`, `.pfx`, `.pkcs12`). On K8s/OpenShift the server auto-includes `/var/run/secrets/kubernetes.io/serviceaccount/ca.crt` and `.../service-ca.crt` (enabled by default); disable via `additionalOptions: truststore-kubernetes-enabled=false`.

**Air-gap note:** load internal CA chains (e.g. `registry.example.internal`, OTLP collector at `otel-collector.example.internal`) into a `truststores` Secret so the server trusts on-prem TLS endpoints.

### 4.5 Tracing (OpenTelemetry)

```yaml
spec:
  tracing:
    enabled: true              # default 'false'
    endpoint: http://my-tracing:4317   # default 'http://localhost:4317'
    samplerType: parentbased_traceidratio  # default 'traceidratio'
    samplerRatio: 0.01         # default '1'
    resourceAttributes:
      some.attribute: something
```

`tracing-jdbc-enabled` must be set via `additionalOptions` (not first-class). **Air-gap note:** point `endpoint` at an in-cluster/on-prem OTLP collector (e.g. `http://otel-collector.example.internal:4317`); no egress to public collectors. Auth headers via `tracing-header-Authorization` with a Secret ref (`***`).

### 4.6 NetworkPolicy & ServiceMonitor

Operator auto-creates a NetworkPolicy denying access to the clustering port; HTTP(S) stays open. ServiceMonitor is generated only when `metrics-enabled` is set and requires `monitoring.coreos.com/v1:ServiceMonitor` CRD ≥ `v0.72.0`. Default scrape: `path: /metrics`, `port: management`, `interval: 30s`, `scrapeTimeout: 10s`, `insecureSkipVerify: true`. Tune via `spec.serviceMonitor` or disable with `spec.serviceMonitor.enabled: false`.

### 4.7 Unsupported podTemplate (Tech Preview)

```yaml
spec:
  unsupported:
    podTemplate:
      metadata:
        labels:
          my-label: "keycloak"
      spec:
        containers:
          - volumeMounts:
              - name: test-volume
                mountPath: /mnt/test
        volumes:
          - name: test-volume
            secret:
              secretName: keycloak-additional-secret
```

Merged into the Deployment template; no guarantee it works as expected. Grants deploy of alternative workloads with Operator-level permissions — namespace-admin trust required.

---

## 5. Rolling updates / avoiding downtime

Default: rolling updates on config changes (no downtime), recreate on image name/tag change. Set strategy in `spec.update`:

```yaml
spec:
  update:
    strategy: RecreateOnImageChange|Auto|Explicit
    revision: "abc"
```

| Strategy | Downtime | Behavior |
|---|---|---|
| `RecreateOnImageChange` | On image name/tag change | Mimics RHBK 26.1-or-older: scale down StatefulSet before applying new image. |
| `Auto` | On incompatible changes | Operator detects whether rolling or recreate is possible; rolling for same version or newer patch in same minor. Runs a Job to assess feasibility (consumes resources, slight delay). |
| `Explicit` | Per the `revision` trigger | User-controlled: changing the CR while `revision` is unchanged prompts a rolling update. |

Rolling updates avoid downtime only with **at least two replicas** running. With `unsupported.podTemplate`, `Auto` may draw wrong conclusions (Job may miss template/Secret/ConfigMap/Volume settings) — prefer another strategy. With `Explicit` + auto Operator upgrades (OLM), an unsupported rolling update may be attempted on upgrade — test in non-prod first.

**CR status** `RecreateUpdateUsed` records the strategy used last (`lastTransitionTime` = when). Values: initial (no update), rolling applied, or recreate applied.

---

## 6. Custom images

Specify `spec.image` to run a custom RHBK server image. **Align the RHBK version in the image with the Operator version.**

```yaml
spec:
  instances: 1
  image: quay.io/my-company/my-keycloak:latest
  http:
    tlsSecret: example-tls-secret
  hostname:
    hostname: test.keycloak.org
```

**When the Operator skips the build:** with a custom (optimized) image the augmentation is built-in, so the server skips the costly per-Pod re-augmentation, and **every build-time option (dedicated field or `additionalOptions`) is ignored**. The Operator is unaware of options baked into the image — use the CR for anything needing Operator awareness (TLS, HTTP(S) settings for services/probes; `tlsSecret` + `truststores` if the image's management interface uses HTTPS).

Optimized images must explicitly set `health-enabled` and `metrics-enabled` in the Containerfile.

**Non-optimized image:** to use build-time properties / a non-augmented image, set `startOptimized: false` (incurs re-augmentation on every start):

```yaml
spec:
  instances: 1
  image: quay.io/my-company/my-keycloak:latest
  startOptimized: false
```

**Air-gap note:** custom images must be **pre-built and pushed to an internal registry** (e.g. `image: registry.example.internal/rhbk/my-keycloak:26.6`) before the Operator can pull them. Build the optimized image once (Containerfile with `health-enabled`/`metrics-enabled` set), bake in providers/themes/extensions, mirror it, and reference it by digest where possible. The cluster needs pull access (pull secret) to `registry.example.internal`; there is no egress to `quay.io`.

_Source: Red Hat build of Keycloak 26.6 Operator Guide (docs.redhat.com), distilled offline._
