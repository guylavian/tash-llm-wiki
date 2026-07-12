---
origin: eval-cohort
title: "End-to-end path for running RHBK on OpenShift"
type: question
domain: keycloak
slug: rhbk-openshift-end-to-end-path
summary: "The end-to-end path: install the RHBK Operator via OLM, provision DB/hostname/TLS prerequisites yourself, declare a Keycloak CR that the Operator reconciles into a StatefulSet+Service+Ingress, verify via status conditions, and access the initial admin credentials"
sources:
  - topic:operator-deployment
  - entity:rhbk-operator
  - entity:operator-olm-install
  - entity:keycloak-cr
  - ref:rhbk-operator
provenance_extracted: 14
provenance_inferred: 1
provenance_ambiguous: 0
tags: "[operator, deployment, openshift]"
question_tier: conceptual
status: draft
updated: 2026-07-12
---

# End-to-end path for running RHBK on OpenShift

The end-to-end path has **six stages**: Operator install → prerequisite provisioning → Secret creation → `Keycloak` CR apply → verify → access.

## 1. Install the RHBK Operator via OLM

Install the `rhbk-operator` from OperatorHub (search "Keycloak") or via a `Subscription` CR. Pick the channel matching your target RHBK version. **Manual approval** (`installPlanApproval: Manual`) is strongly recommended — automatic upgrades can pull an unintended RHBK operand image, break CR compatibility, and have no downgrade path after DB migration (`topics/operator-deployment.md:33-35`; `references/rhbk-operator.md:15-17`).

For disconnected/air-gapped clusters, mirror the operator catalog and images into a local registry first (`entities/operator-olm-install.md:39-43`).

## 2. Provision prerequisites (Operator does NOT manage these)

| Prerequisite | Detail |
|---|---|
| **Database** | A supported DB (e.g. PostgreSQL) reachable from the namespace. The Operator does not provision or manage it (`topics/operator-deployment.md:14-16`). |
| **Hostname** | A production hostname. On OpenShift with `spec.ingress.className: openshift-default`, the Operator can auto-assign a default route host (`topics/operator-deployment.md:18-20`). |
| **TLS** | A `kubernetes.io/tls` Secret with the cert + key (`references/rhbk-operator.md:52`). |

## 3. Create Secrets

```bash
oc create secret generic keycloak-db-secret \
  --from-literal=username=<user> \
  --from-literal=password=<pass>
oc create secret tls example-tls-secret --cert=cert.pem --key=key.pem
```

The DB Secret is referenced via `db.usernameSecret` / `db.passwordSecret` on the CR (`topics/operator-deployment.md:22-24`; `references/rhbk-operator.md:56-61`).

## 4. Apply the Keycloak CR

The CR (`apiVersion: k8s.keycloak.org/v2beta1` as of RHBK 26.6; `v2alpha1` on 26.0–26.4) is the single declarative spec. The Operator reconciles it into a **StatefulSet, Service, and optional Ingress** (`topics/operator-deployment.md:1-3`).

Minimal example (`references/rhbk-operator.md:67-89`):

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

Key CR fields: `spec.instances`, `spec.db`, `spec.http.tlsSecret`, `spec.hostname`, `spec.proxy.headers`, `spec.ingress`, `spec.features`, `spec.resources`, `spec.scheduling`, `spec.truststores`, `spec.additionalOptions` (escape hatch), `spec.image`/`spec.startOptimized` (custom images), `spec.bootstrapAdmin`, `spec.update.strategy` (`entities/keycloak-cr.md:5-27`).

## 5. Verify

Check status conditions (`entities/keycloak-cr.md:31-32`):
```bash
oc get keycloaks/example-kc \
  -o go-template='{{range .status.conditions}}{{.type}}={{.status}} {{end}}'
```
Expected: `Ready=True`, `HasErrors=False`.

## 6. Access

The Operator generates an initial admin into a `<cr-name>-initial-admin` basic-auth Secret (`topics/operator-deployment.md:31-33`). Decode with:
```bash
oc get secret example-kc-initial-admin \
  -o go-template='{{.data.username|base64decode}}:{{.data.password|base64decode}}'
```

## Caveats

- `apiVersion` varies by Operator version — `v2alpha1` on 26.0–26.4, `v2beta1` on 26.6+ (`topics/operator-deployment.md:25-28`). CRDs are shared cluster-wide; the last-installed Operator's CRDs win (`entities/operator-olm-install.md:35-37`).
- If `proxy.headers` is unset, the Operator falls back to the legacy `proxy=passthrough` (deprecated; will be removed in a future release) (`topics/operator-deployment.md:36-38`).
- For multi-site/HA, pair with an external Red Hat Data Grid — see [[ha-cross-site]] (`entities/rhbk-operator.md:29-30`).
- Anyone who can create/edit `Keycloak` CRs effectively has namespace-admin-level trust (can mount Secrets via `spec.image`/`podTemplate`) (`topics/operator-deployment.md:46-50`).

## References

### RH ground-truth
- `references/rhbk-operator.md` — RHBK Operator on OpenShift — Keycloak CR Reference (RHBK 26.6)
- `rhbk-26-6-basic-deployment` — Chapter 2. Basic Red Hat build of Keycloak deployment
- `rhbk-26-6-installation` — Chapter 1. RHBK Operator installation
- `rhbk-26-6-advanced-configuration` — Chapter 4. Advanced configuration
- `_ref-keycloak-operator_guide` — keycloak reference — operator_guide

### Wiki
- [[operator-deployment]] — the main synthesis page for this path
- [[rhbk-operator]] — Operator overview
- [[operator-olm-install]] — detailed OLM install (disconnected, manual approval)
- [[keycloak-cr]] — Keycloak CR field reference
- [[operator-ingress]] — ingress/proxy-headers details
- [[operator-advanced-config]] — truststores, podTemplate, scheduling
- [[operator-rolling-updates]] — update strategies
- [[custom-keycloak-image]] — pre-optimized images
- [[keycloak-realm-import]] — realm bootstrap
- [[kc-bootstrap-admin]] — admin bootstrap
- [[ha-cross-site]] — multi-site HA

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[references/rhbk-operator|RHBK Operator on OpenShift — Keycloak CR Reference — RHBK 26.6 (Offline Reference)]]
<!-- crosslink:end -->
