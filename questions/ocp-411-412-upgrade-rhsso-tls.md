---
title: "OCP 4.11 → 4.12 master upgrade breaks RHSSO — HAProxy TLS error on re-encrypt route"
type: question
domain: keycloak
slug: ocp-411-412-upgrade-rhsso-tls
summary: "Diagnostic guide (provisional — break-fix tier not in corpus). After an OCP 4.11→4.12 control-plane upgrade the HAProxy router is rebuilt; the RH-SSO 7.6 Operator's default reencrypt Route does a second router→pod TLS handshake that can now fail. Two grounded mechanisms: (a) the router's effective Intermediate TLS profile may change across releases, (b) the 4.12-era router moved toward a RHEL 9 / OpenSSL 3 base that rejects SHA-1-signed certs and legacy renegotiation. Read the exact HAProxy error first — it disambiguates cipher vs cert/CA vs protocol."
sources:
  - kb:rhbk-26-6-migrating-operator
  - ref:security-4-22-tls-security-profiles
  - ref:doc-2342861
  - ref:networking-4-22-securing-routes
  - ref:networking-4-22-creating-advanced-routes
provenance:
  extracted: 5
  inferred: 8
  ambiguous: 1
symptoms:
  - "OCP control-plane (master) upgraded from 4.11 to 4.12"
  - "RHSSO stops working immediately after upgrade"
  - "HAProxy TLS / SSL handshake error in router logs"
  - "Route is re-encrypt type (default for RH-SSO 7.6 Operator)"
  - "Ingress Controller TLS security profile is Intermediate or has changed"
tags: [migration, server-config]
status: draft
updated: 2026-06-26
---

# OCP 4.11 → 4.12 master upgrade breaks RHSSO — HAProxy TLS error on re-encrypt route

⚠️ **Provisional — out of corpus coverage.** This is a *break-fix scenario* question; that tier (RH Solution articles on this exact symptom) is **not ingested**. The mechanism below is synthesis from conceptual docs, not a confirmed root-cause article — **verify against the actual HAProxy error and the RH KB before acting.**

**The grounded part (high confidence):** the RH-SSO 7.6 Operator creates a `reencrypt` Route by default (kb:rhbk-26-6-migrating-operator), so HAProxy terminates the outer TLS and opens a **second** TLS connection to the backend RHSSO pod. A control-plane upgrade rebuilds the router pods, so anything that changes that router→pod handshake breaks RHSSO at the router with a TLS error.

**The inferred part (two competing hypotheses — read the error string to choose):**
1. *(inferred)* the router's effective `Intermediate` TLS profile / cipher list changed across the release (the docs warn it "is subject to change between releases"), so a cipher the RHSSO JVM offers is no longer accepted → `no shared cipher`.
2. *(inferred)* the 4.12-era router moved toward a **RHEL 9 / OpenSSL 3** base, which rejects **SHA-1-signed certificates**, small keys, and legacy/unsafe renegotiation → `certificate verify failed` / handshake failure even with a fine cipher. This is the more commonly reported "everything-TLS-broke-after-the-upgrade" class.

**Do this first:** read the exact HAProxy error — it picks the hypothesis. `no shared cipher` → §profile/cipher; `certificate verify failed` / `unknown ca` → §cert/CA (OpenSSL-3 SHA-1 or stale `destinationCACertificate`); `unsupported protocol` → §minTLS.

---

## Root cause analysis

### 1. TLS security profile changes between OCP 4.11 and 4.12

The OpenShift TLS security profile documentation explicitly warns that profile configurations are subject to change:

> *"When using one of the predefined profile types, the effective profile configuration is subject to change between releases. For example, given a specification to use the Intermediate profile deployed on release X.Y.Z, an upgrade to release X.Y.Z+1 might cause a new profile configuration to be applied, resulting in a rollout."* (ref: `security-4-22-tls-security-profiles.md`, line 88–89)

Both OCP 4.11 and 4.12 default to the `Intermediate` TLS security profile (min TLS 1.2), but the effective cipher-suite list hardened between releases. The Ingress Controller HAProxy image was also updated (newer HAProxy + OpenSSL versions), which may reject cipher suites that an older RHSSO JVM negotiates.

The control-plane ("master") upgrade from 4.11 to 4.12 triggers the Ingress Operator to roll out new router pods with the new TLS profile.

### 2. RH-SSO 7.6 Operator creates a re-encrypt Route

The migration guide confirms:

> *"The Red Hat Single Sign-On 7.6 Operator used the reencrypt TLS termination strategy by default on Route."* (ref: `kb:rhbk-26-6-migrating-operator`)

With a **re-encrypt route**:
- Client → HAProxy: TLS terminator at the router (uses the route's certificate)
- HAProxy → RHSSO pod: **new TLS connection** (uses `destinationCACertificate` or router's default CA trust)

The second TLS connection (router→pod) must match the Ingress Controller's TLS security profile. If the cipher or protocol negotiated between HAProxy and the RHSSO pod's Undertow HTTPS listener is not in the profile's allowlist, the TLS handshake fails.

### 3. HAProxy logs show the error

In the router logs (`openshift-ingress` namespace), you'll see backend TLS handshake failures:

```
TLS handshake error: ... error:1408...
backend connection failure: tls: handshake failure
```

The HAProxy backend server for the re-encrypt route will show connection errors or `DOWN` status.

---

## Verification steps

### 1. Check the Ingress Controller TLS security profile
```sh
oc get ingresscontroller default -n openshift-ingress-operator -o yaml | grep -A 20 tlsSecurityProfile
```
If no `tlsSecurityProfile` is explicitly set, the default is `Intermediate`. If it was explicitly set to `Old` (min TLS 1.0/1.1) in 4.11 and reverted to default `Intermediate` in 4.12, that would also cause a mismatch.

### 2. Confirm the Route type is re-encrypt
```sh
oc get route <rhsso-route> -n <namespace> -o jsonpath='{.spec.tls.termination}'
```
Should output `reencrypt` (default for RH-SSO 7.6 Operator). If it's `passthrough`, the backend TLS handshake is not the issue.

### 3. Check router logs for backend TLS errors
```sh
oc logs -n openshift-ingress -l ingresscontroller.operator.openshift.io/deployment-ingresscontroller=default --tail=200 | grep -i "tls\|ssl\|handshake\|backend\|error"
```

### 4. Check the RHSSO pod's serving cert and TLS configuration
For RH-SSO 7.6 on JBoss EAP, the HTTPS listener cipher/protocol set is configured in the EAP subsystem (`standalone-ha.xml` / `standalone-openshift.xml`), not via a documented env var. Inspect it inside the pod, and — for hypothesis #2 — check the **signature algorithm of the pod's serving certificate** (OpenSSL 3 rejects SHA-1):
```sh
oc rsh <rhsso-pod> grep -i cipher /opt/eap/standalone/configuration/standalone-openshift.xml
# serving cert signature algorithm (SHA1withRSA -> the OpenSSL-3 reject case):
oc get secret <serving-cert-secret> -n <ns> -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -noout -text | grep -i "signature algorithm"
```

### 5. Check Service CA certificate validity
If the Route embeds a `destinationCACertificate`, verify it matches the current Service CA:
```sh
oc get route <rhsso-route> -n <ns> -o yaml | grep -A 10 destinationCACertificate
```
The Service CA is rotated automatically; a stale pinned CA would also cause HAProxy to reject the backend TLS connection.

### 6. Verify Operator version compatibility
```sh
oc get csv -n <rhsso-ns> -o jsonpath='{.items[*].spec.version}'
```
Per ref:`doc-2342861`, RH-SSO Operator 7.6.3+ fully supports OCP 4.12. Earlier versions may have untested interactions.

---

## Fixes (in priority order)

### 1. Add a Custom TLS security profile to the Ingress Controller (fastest fix)

If the RHSSO pod cannot easily change its cipher suites, relax the Ingress Controller profile to include the ciphers the RHSSO JVM uses:

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  tlsSecurityProfile:
    type: Custom
    custom:
      ciphers:
        - ECDHE-ECDSA-CHACHA20-POLY1305
        - ECDHE-RSA-CHACHA20-POLY1305
        - ECDHE-RSA-AES128-GCM-SHA256
        - ECDHE-ECDSA-AES128-GCM-SHA256
        - ECDHE-RSA-AES256-GCM-SHA384
        - ECDHE-ECDSA-AES256-GCM-SHA384
        - DHE-RSA-AES128-GCM-SHA256
        - DHE-RSA-AES256-GCM-SHA384
      minTLSVersion: VersionTLS12
```

Apply it, wait for the HAProxy router to roll out, then test RHSSO.

Use `oc explain ingresscontroller.spec.tlsSecurityProfile.intermediate` to see the full `Intermediate` cipher list for the current version, then compare with what the RHSSO pod supports.

### 2. Switch to a passthrough Route (eliminates the backend TLS problem)

With a passthrough route, TLS goes directly from the client to the RHSSO pod — HAProxy only does TCP forwarding and never performs a backend TLS handshake. This completely avoids the Ingress Controller TLS profile issue.

Create a passthrough route manually and disable the Operator's built-in ingress:
```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: rhsso-passthrough
  namespace: <namespace>
spec:
  host: sso.apps.<cluster-domain>
  to:
    kind: Service
    name: <rhsso-service>
  tls:
    termination: passthrough
```

Note: passthrough routes lose cookie-based stickiness (HAProxy cannot read cookies at TCP level). The route defaults to source-IP affinity, which is adequate for RHSSO (see [[passthrough-roundrobin-login-loop]] for roundrobin caveats).

### 3. Re-issue the RHSSO serving certificate (if hypothesis #2 — OpenSSL-3 / SHA-1)

If step 4 shows the pod's serving cert is **SHA-1-signed**, an OpenSSL-3 router will reject the backend handshake regardless of cipher. Re-issue it with a SHA-256 signature — e.g. delete the OpenShift service-serving-cert secret so the `service-ca` controller regenerates a modern one, or replace a manually-supplied keystore with a SHA-256-signed cert. *(inferred — the OpenSSL-3 SHA-1 rejection is a documented behavior class, not confirmed for this exact symptom; verify with the error string.)*

> **Note on the RHSSO JVM cipher list:** RH-SSO 7.6 configures HTTPS ciphers/protocols in the EAP subsystem (`standalone-*.xml`), **not** via any product environment variable — earlier drafts of this page cited a non-existent `sso-https-cipher-suites` env var; it does not exist. RHBK (Quarkus) does expose `--https-cipher-suites` / `--https-protocols`, but this question is about RH-SSO 7.6. Prefer fixes #1/#2 over editing the EAP cipher list.

### 4. Refresh the Route's destinationCACertificate

If the `destinationCACertificate` is stale from a Service CA rotation:
```sh
# Remove the stale secret and let the service-ca controller regenerate it
oc delete secret <serving-cert-secret-name> -n <namespace>
# The controller recreates it automatically
# Then either remove the route (Operator recreates) or update destinationCACertificate manually
```

### 5. Update the RH-SSO Operator to a version tested with OCP 4.12

Upgrade to at least RH-SSO Operator 7.6.3 (or the latest available 7.6.z) via OLM. This ensures the Operator's image is tested with OCP 4.12's HAProxy router.

---

## Summary

| Hypothesis | Role | Why |
|------------|------|-----|
| **Ingress Controller TLS profile hardened in 4.12** | **Primary root cause** | The `Intermediate` profile's effective cipher list and/or HAProxy/OpenSSL stack changed between 4.11 and 4.12. The router rollout broke the re-encrypt backend TLS handshake. |
| **Service CA certificate rotation** | Contributor | If `destinationCACertificate` was pinned to a pre-upgrade CA, the upgraded router may reject the backend cert. |
| **Operator version untested with 4.12** | Possible contributor | Very old RH-SSO Operator releases may never have been validated against the 4.12 HAProxy image. |
| **Route type changed** | Unlikely | Operator reconciliation preserves the TLS termination type. |

---

## References

### RH ground-truth (`ref:` / `kb:` / `guide:`)

- **ref:security-4-22-tls-security-profiles** (OCP 4.22, Security → TLS Security Profiles) — *"the effective profile configuration is subject to change between releases"*; documents the `Intermediate` profile ciphers (TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256, ECDHE-*, DHE-RSA-*) and min TLS version.
- **kb:rhbk-26-6-migrating-operator** (RHBK 26.6 Migration Guide, §3) — *"The Red Hat Single Sign-On 7.6 Operator used the reencrypt TLS termination strategy by default on Route."* — confirms the route type.
- **ref:doc-2342861** (Supported Configurations article) — Support matrix RH-SSO Operator → OCP: 7.6.3 / 7.6.4 fully supported on OCP 4.12.
- **ref:networking-4-22-securing-routes** (OCP 4.22, Networking → Securing Routes) — re-encrypt route creation, `destinationCACertificate` field documentation.
- **ref:networking-4-22-creating-advanced-routes** (OCP 4.22, Networking → Configuring Routes) — `destinationCACertificate` usage in re-encrypt routes.
- **ref:networking-4-22-nw-ingress-operator** (OCP 4.22, Networking → Ingress Operator) — Ingress Operator TLS security profile handling.

### Wiki (cross-linked synthesis pages)

- [[openshift-route]] — Route TLS termination modes (edge / passthrough / re-encrypt) and common gotchas.
- [[passthrough-roundrobin-login-loop]] — Q&A on passthrough route session affinity; relevant if switching from re-encrypt to passthrough.
- [[reverse-proxy-configuration]] — RHBK/RHSSO proxy-headers, sticky sessions, cookie-based affinity.
- [[tls-configuration]] — RHBK/RHSSO TLS configuration (keystore, cipher suites, protocols).
- [[troubleshooting-index]] — Operator / OpenShift section; gated pointers for related TLS/cert issues.
- [[rhsso-to-rhbk-migration]] — RH-SSO 7.6 → RHBK migration; RHBK uses a passthrough ingress by default.
- [[operator-deployment]] — RHBK Operator deployment model (for comparison with RH-SSO Operator).
- [[security-hardening-checklist]] — TLS hardening on RHBK/RHSSO server.
- [[operator-advanced-config]] — TLS/truststore configuration on the Keycloak CR.
- [[keycloak-truststores]] — Trusted certificate configuration.

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-migrating-operator|Chapter 3. Migrating Operator deployments on Openshift]]
<!-- crosslink:end -->
