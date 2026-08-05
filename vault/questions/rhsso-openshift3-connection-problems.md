---
title: RHSSO / RHBK connection problems with OpenShift 3
type: question
question_tier: conceptual
domain: keycloak
slug: rhsso-openshift3-connection-problems
summary: "Common causes of connection failures between Red Hat Single Sign-On (RH-SSO) or Red Hat Build of Keycloak (RHBK) and OpenShift Container Platform 3.x — TLS/certificate issues, master-config misconfiguration, template version incompatibility, and product lifecycle blocks"
sources:
  - reference/keycloak/rhbk-26-6-migrating-openshift.md
  - reference/keycloak/rhsso-7-6-tutorials.md
  - reference/keycloak/rhsso-7-4-identity-broker.md
  - reference/keycloak/rhsso-7-3-red-hat-single-sign-on-7-3.md
  - reference/keycloak/doc-5115291.md
  - reference/keycloak/rhsso-7-6-performing-advanced-procedures.md
  - reference/keycloak/rhsso-7-6-introduction-to-red-hat-single-sign-on-for-openshift.md
provenance:
  extracted: 10
  inferred: 1
tags: [migration]
status: draft
updated: 2026-07-02
graph_community: "RHBK Server Configuration — sources, build vs runtime, precedence"
---

# RHSSO / RHBK connection problems with OpenShift 3

**OpenShift Container Platform 3.x reached end of life (ELS ended June 30, 2024). RHBK 26.x explicitly drops OpenShift 3.x support. RH-SSO 7.x remains the last RH product line with OpenShift 3.11 support, and even that is ELS-only. Connection failures usually fall into five categories.**

## Body

### 1. Product lifecycle block — the most likely root cause

**RHBK 26.x does not support OpenShift 3.x.** The migration guide for every RHBK 26.x version (26.0 through 26.6) states this outright: *"OpenShift 3.x is no longer supported."* (ref: `rhbk-26-6-migrating-openshift.md`) The OpenShift templates (`sso76-ocp3-https`, `sso76-ocp3-postgresql`, etc.) were deprecated and removed from RHBK container images. If you're trying to connect RHBK to an OpenShift 3 cluster, the connection will fail because RHBK does not ship the required template resources or integration code for OCP 3.

Additionally, Red Hat Middleware products are supported on **OpenShift 3.x only in the 3.11 version** (older 3.x versions are not supported at all). OpenShift 3.11 moved to ELS on June 30, 2022, with ELS ending June 30, 2024 (ref: `doc-5115291.md`). An ELS entitlement is required for continued support during that period; after ELS expiry no support or updates are available.

**If you are using RHBK (not RH-SSO 7.6), you must migrate to OpenShift 4.x.** If you are still on RH-SSO 7.6, you can deploy it on OCP 3.11 (ELS only), but you will need an ELS entitlement.

### 2. TLS / certificate trust mismatch

OpenShift 3 uses **service serving x509 certificate secrets** — the `service-ca.crt` CA bundle (`/var/run/secrets/kubernetes.io/serviceaccount/service-ca.crt`) — to generate TLS certificates for pods and services. The RH-SSO re-encryption templates (e.g. `sso76-ocp3-x509-https`, `sso76-ocp3-x509-postgresql-persistent`) rely on this internal CA to automatically create HTTPS and JGroups keystores and populate the RH-SSO server truststore (ref: `rhsso-7-6-introduction-to-red-hat-single-sign-on-for-openshift.md`).

When connecting RHSSO as an **OpenID identity provider for OpenShift 3** (editing `/etc/origin/master/master-config.yaml`), the `ca:` field in the `OpenIDIdentityProvider` configuration must point to the correct CA certificate file. The tutorials use a self-generated CA (`ca: xpaas.crt`) for demonstration, and that file must be copied into `/etc/origin/master/` on the OpenShift master node. If using a self-signed or internal CA without placing the CA certificate in the right location, the OIDC handshake fails at the token/userinfo endpoint verification.

Common TLS failure symptoms:
- OpenShift login page shows the `rh-sso` identity provider option but login fails silently
- `curl -k` works but the OpenShift OIDC client validation (which respects `ca:`) fails
- The RH-SSO pod logs show TLS handshake errors
- The `atomic-openshift-master` service fails to restart with certificate errors

### 3. `/etc/origin/master/master-config.yaml` misconfiguration

OpenShift 3 uses a **different identity provider configuration model** than OpenShift 4. The relevant section is `identityProviders` in `/etc/origin/master/master-config.yaml` with `kind: OpenIDIdentityProvider`. The full configuration block looks like (ref: `rhsso-7-6-tutorials.md`):

```yaml
identityProviders:
  - challenge: true
    login: true
    name: htpasswd_auth
    provider:
      apiVersion: v1
      kind: HTPasswdPasswordIdentityProvider
      file: /etc/origin/openshift-passwd
  - name: rh_sso
    challenge: false
    login: true
    mappingMethod: add
    provider:
      apiVersion: v1
      kind: OpenIDIdentityProvider
      clientID: openshift-demo
      clientSecret: "<secret-from-rhsso>"
      ca: xpaas.crt
      urls:
        authorize: https://secure-sso-<app>.example.com/auth/realms/OpenShift/protocol/openid-connect/auth
        token: https://secure-sso-<app>.example.com/auth/realms/OpenShift/protocol/openid-connect/token
        userInfo: https://secure-sso-<app>.example.com/auth/realms/OpenShift/protocol/openid-connect/userinfo
      claims:
        id:
          - sub
        preferredUsername:
          - preferred_username
        name:
          - name
        email:
          - email
```

**Common mistakes:**
- **`clientID` / `clientSecret` mismatch** — these must match the RHSSO OIDC client credentials exactly. The secret is visible in the RHSSO Admin Console under Clients → `<client>` → Credentials.
- **Wrong `urls`** — the authorize, token, and userinfo endpoints must be retrieved from the RHSSO realm's OIDC discovery document at `https://<rhsso-host>/auth/realms/<realm>/.well-known/openid-configuration`. A typo in the realm name, hostname, or path (`/auth` prefix is critical) will break the connection.
- **Missing or wrong `ca:`** — if using a non-public CA, the CA certificate file must exist on the OpenShift master node. Not providing `ca:` when the RHSSO server uses a self-signed certificate causes OIDC token validation to fail.
- **`challenge: false` vs `challenge: true`** — the OpenShift 3 OIDC provider only supports browser-based login (`login: true`), not challenge-based (`challenge: false`). Setting `challenge: true` for an OIDC provider causes a connection error.
- **No master restart** — after editing `master-config.yaml`, the master API service must be restarted: `systemctl restart atomic-openshift-master`.

### 4. RHSSO OIDC client configuration errors

On the RHSSO side, the client registered for OpenShift 3 must be configured correctly (ref: `rhsso-7-6-tutorials.md`):
- **Access Type**: must be `confidential`
- **Valid Redirect URIs**: must include the OpenShift web console URL (e.g. `https://openshift.example.com:8443/*`)
- **Client Protocol**: `openid-connect`
- **Realm**: a dedicated realm (e.g. `OpenShift`) simplifies management

If redirect URIs are wrong, OpenShift 3's OAuth callback to RHSSO fails with a redirect mismatch error.

### 5. Template deployment version mismatch

RH-SSO 7.6 ships specific OpenShift templates in separate directories for OCP 3 vs OCP 4 (ref: `rhsso-7-6-tutorials.md`):
- **OCP 3.x**: `passthrough/ocp-3.x/sso76-ocp3-https.json`, `reencrypt/ocp-3.x/sso76-ocp3-x509-https.json`, `passthrough/ocp-3.x/sso76-ocp3-postgresql.json`, etc.
- **OCP 4.x**: separate `ocp-4.x/` counterparts

Deploying the OCP 4 template on an OCP 3 cluster will fail because the Kubernetes/OpenShift API versions differ (e.g. `DeploymentConfig` vs `Deployment`, route API versions). Conversely, deploying the OCP 3 template on OCP 4 may work but misses OCP 4-specific features.

The template resource URL is:
```
https://raw.githubusercontent.com/jboss-container-images/redhat-sso-7-openshift-image/sso76-dev/templates/
```

### 6. OpenShift 3 as identity provider in RHSSO (reverse direction)

If you are using OpenShift 3 as an identity provider *inside* RHSSO (brokering), the OAuth client is registered on the OpenShift 3 side using an `OAuthClient` resource (ref: `rhsso-7-4-identity-broker.md`):

```yaml
kind: OAuthClient
apiVersion: v1
metadata:
  name: kc-client
secret: "..."
redirectURIs:
  - "http://www.example.com/"
grantMethod: prompt
```

This uses OpenShift 3's older `apiVersion: v1` OAuthClient API. The client ID and secret from this resource must be entered into the RHSSO Add Identity Provider → OpenShift 3 form. Common issues include incorrect redirect URIs and the `grantMethod` not matching the desired user experience.

Note: OpenShift 3 as an IdP in RHSSO was **developer preview / technology preview** (ref: `rhsso-7-3-red-hat-single-sign-on-7-3.md` — "It is now possible to fully secure OpenShift 3.11 with Red Hat Single Sign-On, including the ability to automatically expose Service Accounts as OAuth clients… This feature is currently in technology preview"). It should not be used in production.

### Diagnostic checklist

| Symptom | Likely cause | Action |
|---|---|---|
| Login page shows `rh-sso` option but auth fails silently | TLS cert not trusted by OpenShift master (`ca:` missing in master-config.yaml) | Copy CA cert to `/etc/origin/master/` and reference in `ca:` field |
| `curl -k` to RHSSO OIDC endpoints works but OpenShift auth fails | Same as above — OpenShift master validates TLS certs, `curl -k` skips them | Fix CA configuration |
| OpenShift master service fails to restart | Syntax error in `master-config.yaml` or invalid cert path | Validate YAML, verify cert file exists |
| Redirect mismatch error | `Valid Redirect URIs` in RHSSO client doesn't include the OpenShift console URL | Add `https://<openshift-master>:8443/*` to valid redirect URIs |
| "No supported authentication" or provider not shown | Wrong template type deployed (OCP 4 template on OCP 3) | Use `ocp-3.x/` templates for OCP 3 |
| OpenShift 3 as RHSSO IdP not working | `OAuthClient` v1 resource misconfigured or redirect URIs wrong | Verify `redirectURIs` in the `OAuthClient` resource |
| Template instantiation fails | OCP version mismatch or unsupported API version | Only use `ocp-3.x/` templates on OpenShift 3.11 |

## Contradictions / caveats
- **RHBK vs RH-SSO**: If you're running RHBK (not RH-SSO 7.6), OpenShift 3.x is simply not supported — this is not a fixable configuration. You must upgrade both products. The RH-SSO 7.6 knowledge in this answer applies to that legacy product only.
- **OpenShift 3.11 ELS has ended**: As of June 30, 2024, OpenShift 3.11 is fully end-of-life. Red Hat no longer provides security patches or support. Running any SSO product on OCP 3.11 carries significant security and compliance risk.
- **Technology Preview features**: The OpenShift 3 identity provider inside RHSSO (brokering OpenShift 3 users) was a Tech Preview feature in RH-SSO 7.3+ and should not be used in production.

## See also
- [[rhsso-to-rhbk-migration]]
- [[troubleshooting-index]]
- [[tls-configuration]]
- [[reverse-proxy-configuration]]

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)

| ID | Title |
|---|---|
| `ref:rhbk-26-6-migrating-openshift.md` | Chapter 4. Migrating Templates deployments on OpenShift — RHBK 26.6 Migration Guide (states "OpenShift 3.x is no longer supported") |
| `ref:rhsso-7-6-tutorials.md` | RH-SSO 7.6 Tutorials — §4.3 Configuring OpenShift 3.11 to use Red Hat Single Sign-On for Authentication (the full OIDC identity provider setup procedure) |
| `ref:rhsso-7-4-identity-broker.md` | RH-SSO 7.4 Identity Broker Guide — §12.4.8 OpenShift 3 (OAuthClient setup for OpenShift 3 as IdP in RHSSO) |
| `ref:rhsso-7-3-red-hat-single-sign-on-7-3.md` | RH-SSO 7.3 Release Notes — §1.2.2 OpenShift Integration (Tech Preview: securing OpenShift 3.11 with RH-SSO) |
| `ref:doc-5115291.md` | Support of Red Hat Middleware products and components on Red Hat OpenShift (OCP 3.x support policy: 3.11 only, ELS ended 2024-06-30) |
| `ref:rhsso-7-6-performing-advanced-procedures.md` | RH-SSO 7.6 Performing Advanced Procedures — template deployment, admin account creation, TEMPLATE parameter mapping |
| `ref:rhsso-7-6-introduction-to-red-hat-single-sign-on-for-openshift.md` | RH-SSO 7.6 Introduction — TLS termination modes, OCP 3 vs 4 template differences |

### Wiki pages

| Page | Notes |
|---|---|
| [[rhsso-to-rhbk-migration]] | The migration path from RH-SSO 7.6 to RHBK — includes OpenShift Operator migration |
| [[troubleshooting-index]] | RHBK/RH-SSO triage by area |
| [[tls-configuration]] | TLS configuration for RHBK |
| [[reverse-proxy-configuration]] | Proxy/Route configuration behind OpenShift |
