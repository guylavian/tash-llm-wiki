---
name: llm-wiki
description: Multi-domain offline LLM knowledge wiki (keycloak / active-directory / openshift / cisco-ios-xe) — an Obsidian vault of LLM-maintained synthesis pages over immutable reference corpora, with the wikikb toolchain (retrieval, confidence gate, identifier guard, temporal knowledge graph, MCP server). Activate for Keycloak/RHBK administration (realms, clients, OAuth2/OIDC & SAML, federation/LDAP/AD, tokens, operator/OpenShift deployment, HA, RH-SSO→RHBK migration), Active Directory, OpenShift, and Cisco IOS-XE questions. Includes an OFFLINE reference distilled from official docs (Keycloak 26 / RHBK 26.6 docs+KB: 1,840 records, 800 full doc bodies) queried with `python3 -m wikikb kb` (or grep) — no internet required.
allowed-tools:
  - Bash
  - Read
  - Glob
  - Grep
  - Edit
  - Write
triggers:
  - keycloak
  - realm
  - client
  - oauth
  - oidc
  - saml
  - authentication
  - user management
  - identity provider
  - ldap federation
  - token configuration
  - authorization services
  - rhbk
  - red hat build of keycloak
  - operator
  - openshift
  - rh-sso
  - setup wizard
  - init environment
  - bootstrap cluster
---

# Keycloak Administration

Vendor-neutral reference and task cookbook for administering Keycloak (and Red Hat build of Keycloak / RH-SSO) via the **Admin REST API** and the **`kcadm.sh`** CLI. Built to work **offline / air-gapped** — the `references/` files embed the core of the official Keycloak 26 documentation, so no internet access is required.

## When to use this skill
- Creating/configuring realms, clients (OIDC/SAML), client scopes, and protocol mappers
- Managing users, credentials, required actions, roles, groups, and default roles
- Setting up authentication flows, MFA (OTP/WebAuthn/X.509/Kerberos), and step-up auth
- Identity brokering (external OIDC/SAML IdPs) and user federation (LDAP/Active Directory)
- Token/session lifetimes, signing-key rotation, logout, and offline access
- Fine-grained authorization (resources, scopes, policies, permissions, UMA)
- Wiring application SSO (e.g. OpenShift, ArgoCD, Grafana) to a Keycloak realm
- Operating/configuring the server: `kc.sh build`/`start`, hostname v2, DB, TLS, reverse proxy, bootstrap admin, health/metrics, features, vault
- Deploying for High Availability: Infinispan caches, session persistence, multi-site (cross-DC), load-balancer/failover
- Extending the server with SPIs/providers: custom authenticators, OIDC protocol mappers, event listeners, custom REST, user storage
- Red Hat build of Keycloak (RHBK): supported-config matrix, lifecycle/EOL, subscriptions, container images & Operator, errata/CVE mapping, RHBK-vs-upstream + Preview/Supported/Deprecated feature status
- RHBK/OpenShift troubleshooting (Operator, hostname/proxy, DB, TLS, Infinispan, login/SSO) and RH-SSO→RHBK migration breakages

## Setup & Onboarding Wizard (Interactive Mode)
When the user triggers a new deployment setup (e.g., using keywords like "start setup", "init cluster", or "bootstrap environment"), you MUST enter an interactive Setup Wizard mode to architect the solution before writing any configuration files.

**CRITICAL Wizard Rules:**
1. **Ask One Question at a Time:** You MUST NOT output a list of all questions. Ask the first question, wait for the user's response, and only then proceed to the next step.
2. **Context Awareness:** Assume the target is **air-gapped**, with **RHBK running on OpenShift** and managed via **Argo CD (GitOps)** — the **server** deployed from the **`codecentric/keycloakx` Helm chart** (pointed at the mirrored RHBK image), and **realms / clients / identity providers provisioned as IaC via the Keycloak Terraform provider** (`keycloak/keycloak`) — unless the user specifies otherwise. *(Two layers: **Helm + Argo CD = the running server**; **Terraform = realm & client configuration**. Both `codecentric/keycloakx` and the Terraform provider are community tooling pointed at RHBK; Red Hat's supported server path is the Operator + `Keycloak` CR — offer it if Red Hat support is required.)*

**Wizard Sequential Steps:**
* **Step 1 - Database:** "Which backing database vendor (e.g., postgres, mssql) are we using, and what are the specific JDBC requirements for this air-gapped environment?"
* **Step 2 - HA & Caching:** "How many Keycloak replicas are planned? Are we relying on `jdbc-ping` for discovery, and will the embedded Infinispan cache suffice, or is an external Data Grid required?"
* **Step 3 - Network & TLS:** "What are the primary `--hostname` and `--hostname-admin`? Is TLS terminated at the ingress (Edge) or passed through to the pods?"
* **Step 4 - Secrets Management:** "How will credentials be mounted into the pods? (e.g., Kubernetes Secrets mapped to Keycloak's `--vault=file` via Helm extraVolumes)."
* **Step 5 - Realm & Client IaC (Terraform):** "Which realms, clients, and identity providers does the **Keycloak Terraform provider** (`keycloak/keycloak`) manage (e.g., SharePoint SE OIDC client, oauth2-proxy client, generic OIDC clients, ADFS SAML federation)? How does Terraform authenticate to Keycloak (a dedicated **service-account client** via `client_credentials`), where is the provider **mirrored** for the air-gap (Terraform `network_mirror` / internal registry), and what is the **state backend** (e.g., GitLab HTTP or MinIO/S3)?"

**Final Output Generation:**
Only AFTER all steps are completed and data is collected, synthesize the final GitOps artifacts:
1. The exact `kc.sh build` command with all necessary build-time flags.
2. A customized **`values.yaml`** tailored for the `codecentric/keycloakx` Helm chart, injecting the required `extraEnv` (e.g., `KC_DB_URL_HOST`, `KC_HOSTNAME`), `args` (`start --optimized`), and Ingress configurations.
3. An **Argo CD `Application` manifest** that points to the internal Helm registry and applies the generated values.
4. **Terraform realm/client IaC** for the `keycloak/keycloak` provider: pinned `required_providers` + an air-gapped `provider_installation { network_mirror }`; a `provider "keycloak"` block authenticating via the Terraform **service-account client** (`client_id`/`client_secret` from env, `***`); and the `keycloak_realm` / `keycloak_openid_client` / `keycloak_saml_identity_provider` / `keycloak_generic_protocol_mapper` resources for the env's clients & IdPs. **Apply order:** server first (Helm/Argo CD), then `terraform apply` against the live endpoint.

**Guardrails:** confirm `values.yaml` keys against the chart, Terraform resource/argument names against the `keycloak/keycloak` provider, and all flags/versions against the offline `references/` (DB → `server-configuration.md` §4 + `rhbk-troubleshooting-kb.md`; HA/`jdbc-ping` → `high-availability.md`; hostname/TLS → `server-configuration.md` §3/§5/§6; vault → §11; supported vendors → `rhbk-platform-support.md`) — do not invent. Never present a Preview feature as production-ready. Keep secrets **out of Git** *and out of Terraform state in Git*: mounted Kubernetes Secrets / `--vault=file` for the server, a **remote encrypted state backend** for Terraform, `***` placeholders only.

## Offline documentation reference

Open the matching file in `references/` for depth. Each is distilled from the Keycloak 26 official guides.

| Reference file | Covers |
|---|---|
| `references/server-administration.md` | Realms, users, roles/groups, realm keys & rotation, authentication flows & MFA, identity brokering, LDAP/AD federation, sessions/tokens, `kcadm.sh`, realm import/export, security checklist |
| `references/admin-rest-api.md` | Admin REST API: auth, every major resource's endpoints (tables), query params, and the key representation objects with their fields |
| `references/securing-apps-oidc-saml.md` | OIDC vs SAML, protocol flows, client types, the standard OIDC endpoints, client-auth methods, token validation (JWKS vs introspection), logout, FAPI/OAuth-2.1/DPoP profiles |
| `references/authorization-services.md` | Fine-grained authorization: resources/scopes/policies/permissions, policy types, decision strategies, Protection API, obtaining an RPT, the policy enforcer |
| `references/server-configuration.md` | Operating the server: build vs runtime + config precedence, hostname v2, database, TLS, reverse proxy, bootstrap admin & recovery, health/metrics endpoints, features, vault, production checklist |
| `references/high-availability.md` | Clustering & HA: embedded vs external Infinispan, cache roles, session persistence, Active/Passive multi-site, load balancer & failover, known constraints (supported vs preview) |
| `references/server-development.md` | SPIs & extensions: provider/factory model, JAR deployment + `kc.sh build`, key SPIs, a minimal OIDC ProtocolMapper skeleton (computed claim), the scripts-must-be-a-JAR constraint |
| `references/rhbk-platform-support.md` | **RHBK-specific:** version/cadence, supported-config matrix (OCP/OS/JVM/DB/RHDG), lifecycle & subscriptions, container images & Operator (channels/install modes/CRDs), sizing, errata/RHSA→CVE map, feature status (Supported/TP/DP/Deprecated), RHBK-vs-upstream, RH-SSO→RHBK migration |
| `references/rhbk-troubleshooting-kb.md` | **RHBK-specific:** **28 distilled public KB fixes** (symptom→cause→fix, verbatim commands) from the harvest's public-body solutions, plus the **1,030-solution index by area** (40 public / 990 gated) and how to query the rest offline via `kb.py` over `reference/keycloak/` (gated pointers in `_gated-kb-index.md`). Gated resolution bodies are subscriber-only (pointers). |
| `references/rhbk-operator.md` | **RHBK-specific (grounded in RHBK 26.6 Operator Guide):** OLM install (disconnected note), the `Keycloak` CR for a basic deploy (hostname/DB/TLS/ingress), `KeycloakRealmImport`, advanced CR tuning (additionalOptions, truststores, podTemplate, scheduling, secrets), rolling updates, and custom pre-optimized images for air-gapped registries |
| `references/observability.md` | **RHBK-specific (grounded in RHBK 26.6 Observability Guide):** OpenTelemetry centralization (`telemetry-*`), health endpoints/probes on the management port, metrics (`/metrics`, families), event metrics, SLIs, tracing (OTLP exporter/sampling), dashboards/exemplars — with air-gap notes on repointing/disabling external collectors |
| `references/migration-upgrading.md` | **RHBK-specific (grounded in RHBK 26.6 Migration + Upgrading Guides):** RH-SSO 7.6→RHBK (server, Operator, Templates, apps/adapters, custom providers/themes, upstream→RHBK) and RHBK version upgrades (procedure, DB auto-migration, release-specific changes, adapters) — offline-staged |

> **How to use:** identify the task → answer common ones from the cookbook below → open the matching reference file for exact fields, endpoints, and options.

## Local knowledge base (bundled, offline) — `kb/`

Beyond the distilled `references/`, this skill bundles a **searchable local mirror** of the
official RHBK/RH-SSO documentation and Red Hat KB — usable with **no internet**. Reach for it
when a question needs the *exact* wording, a specific version, or a long-tail topic the
distilled references don't cover.

- **Query tool:** `python3 -m wikikb kb --domain keycloak …` (Python 3 stdlib only,
  air-gapped) — or plain `grep reference/keycloak/`.
- **Corpus (now folded into the vault):** `reference/keycloak/` — one Markdown note per
  source (741 RHBK/RH-SSO doc chapters across **26.0/26.2/26.4/26.6**, 40 solutions, 14 articles,
  5 discussions = 800 bodies) + `_gated-kb-index.md`. `kb.py` reads these notes; plain
  `grep reference/keycloak/` works too. (`kb/index.jsonl` + `kb/bodies/` no longer exist.)
- **Gated KBs:** 1,040 Red Hat **Solutions/Articles are subscriber-gated** — bundled as
  *pointers* (title + abstract + URL) in `_gated-kb-index.md`, body absent. Excluded from search
  unless you pass `--gated`.

```bash
python3 -m wikikb kb --domain keycloak search "ldap truststore operator"   # ranked hits + snippets
python3 -m wikikb kb --domain keycloak search "fips bcfips strict" --kind doc --primary
python3 -m wikikb kb --domain keycloak search "disconnected mirror image" --gated
python3 -m wikikb kb --domain keycloak search "cross-site infinispan" --guide high_availability_guide --full
python3 -m wikikb kb --domain keycloak show 7032207            # full body (or URL if gated)
python3 -m wikikb kb --domain keycloak guides ; python3 -m wikikb kb --domain keycloak stats
```

**When answering RHBK questions, prefer grounding in the vault reference tier over memory** —
run a search, cite the returned title/URL/version, and quote the body. Newest-version chapters
rank first (`--primary` to force it); RH-SSO 7.x is demoted (legacy, kept for migration context).

## Compiled wiki (LLM-maintained synthesis) — `wiki/`

On top of the raw `reference/` + `references/` tier, `wiki/` is an **LLM-maintained
knowledge wiki** (Karpathy's "LLM Wiki" pattern): cross-linked `topics/`,
`entities/`, and answered `questions/` pages that *compile* the raw sources into
durable synthesis, so conclusions are filed once instead of re-derived each
session. The raw layer stays immutable; the wiki is regenerable downstream of it.

- **Read `CLAUDE.md` first** — it defines the page format (`summary:`,
  two-tier `sources:`, per-claim `provenance:`), the `[[slug]]` cross-link
  convention, and the operations: **INGEST** (fold a source/answer into pages,
  consulting the delta manifest so only new/changed sources are processed),
  **QUERY** (tiered: read titles + summaries first, open bodies only when needed;
  fall back to grep / `kb.py`; file the answer back), **LINT**, and **STATUS** (audit).
- **Tooling** lives in `_meta/wikikb/` (stdlib only, air-gapped):
  - `python3 -m wikikb lint [--status]` — broken/wanted links, orphans,
    missing summary/sources/provenance, provenance drift, auto-seeded summaries,
    link hubs, stale pages; `--status` adds the delta-manifest audit.
  - `python3 -m wikikb manifest {seed,status,record}` — the delta manifest
    (`vault/.manifest.json`): which sources are ingested vs pending/changed.
- **Operations are packaged** as Agent Skills in `.skills/` (`wiki-ingest`,
  `wiki-query`, `wiki-lint`, `wiki-status`) and OpenCode commands in `.opencode/`
  (`/ingest`, `/query`, `/lint`, `/status`) — thin pointers to `CLAUDE.md`.
- When a QUERY surfaces a reusable fact, run a mini-INGEST so the wiki grows.

## Conventions used in examples

Set these once; every snippet below is neutral and portable:

```bash
KC=https://keycloak.example.internal      # base URL (no trailing slash)
REALM=corp                                # target realm
# Obtain an admin token (prefer a dedicated service-account client for automation)
TOKEN=$(curl -s -X POST "$KC/realms/master/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d grant_type=client_credentials -d client_id=automation -d client_secret='***' \
  | jq -r .access_token)
auth=(-H "Authorization: Bearer $TOKEN")
```

For interactive admins, `kcadm.sh` is usually faster — `kcadm.sh config credentials --server "$KC" --realm master --client admin-cli --client-secret '***'` then use the verbs in `references/server-administration.md`.

## Task cookbook (Admin REST API)

### Create a realm
```bash
curl -X POST "$KC/admin/realms" "${auth[@]}" -H "Content-Type: application/json" -d '{
  "realm": "corp",
  "enabled": true,
  "displayName": "Corporate SSO",
  "sslRequired": "all",
  "registrationAllowed": false,
  "loginWithEmailAllowed": true,
  "bruteForceProtected": true,
  "permanentLockout": false,
  "failureFactor": 5,
  "maxFailureWaitSeconds": 900,
  "defaultSignatureAlgorithm": "RS256",
  "accessTokenLifespan": 300,
  "ssoSessionIdleTimeout": 1800,
  "ssoSessionMaxLifespan": 36000,
  "offlineSessionIdleTimeout": 2592000
}'
```

### Create a confidential OIDC client (Authorization Code + PKCE)
```bash
curl -X POST "$KC/admin/realms/$REALM/clients" "${auth[@]}" -H "Content-Type: application/json" -d '{
  "clientId": "web-portal",
  "name": "Web Portal",
  "enabled": true,
  "protocol": "openid-connect",
  "publicClient": false,
  "standardFlowEnabled": true,
  "implicitFlowEnabled": false,
  "directAccessGrantsEnabled": false,
  "serviceAccountsEnabled": false,
  "redirectUris": ["https://portal.example.internal/*"],
  "webOrigins": ["https://portal.example.internal"],
  "attributes": { "pkce.code.challenge.method": "S256" },
  "defaultClientScopes": ["email","profile","roles","web-origins"],
  "optionalClientScopes": ["offline_access"]
}'

# Fetch the client UUID + secret (paths use the UUID, not clientId)
CID=$(curl -s "${auth[@]}" "$KC/admin/realms/$REALM/clients?clientId=web-portal" | jq -r '.[0].id')
curl -s "${auth[@]}" "$KC/admin/realms/$REALM/clients/$CID/client-secret" | jq -r .value
```

### Create a user and set a password
```bash
curl -X POST "$KC/admin/realms/$REALM/users" "${auth[@]}" -H "Content-Type: application/json" -d '{
  "username": "jdoe",
  "email": "jdoe@example.internal",
  "firstName": "Jane", "lastName": "Doe",
  "enabled": true, "emailVerified": true,
  "attributes": { "department": ["platform"] }
}'
UID=$(curl -s "${auth[@]}" "$KC/admin/realms/$REALM/users?username=jdoe&exact=true" | jq -r '.[0].id')
curl -X PUT "$KC/admin/realms/$REALM/users/$UID/reset-password" "${auth[@]}" -H "Content-Type: application/json" \
  -d '{ "type":"password", "value":"***", "temporary":true }'
```

### Realm roles, client roles, and mappings
```bash
# Realm role
curl -X POST "$KC/admin/realms/$REALM/roles" "${auth[@]}" -H "Content-Type: application/json" \
  -d '{ "name":"app-admin", "description":"Application administrator" }'
# Assign to a user
ROLE=$(curl -s "${auth[@]}" "$KC/admin/realms/$REALM/roles/app-admin")
curl -X POST "$KC/admin/realms/$REALM/users/$UID/role-mappings/realm" "${auth[@]}" \
  -H "Content-Type: application/json" -d "[$ROLE]"
```

### Group with attributes, add a user
```bash
curl -X POST "$KC/admin/realms/$REALM/groups" "${auth[@]}" -H "Content-Type: application/json" \
  -d '{ "name":"platform-team", "attributes": { "cost_center": ["CC-100"] } }'
GID=$(curl -s "${auth[@]}" "$KC/admin/realms/$REALM/groups?search=platform-team" | jq -r '.[0].id')
curl -X PUT "$KC/admin/realms/$REALM/users/$UID/groups/$GID" "${auth[@]}"
```

### Add a custom claim via a protocol mapper
```bash
curl -X POST "$KC/admin/realms/$REALM/clients/$CID/protocol-mappers/models" "${auth[@]}" \
  -H "Content-Type: application/json" -d '{
    "name": "department",
    "protocol": "openid-connect",
    "protocolMapper": "oidc-usermodel-attribute-mapper",
    "config": {
      "user.attribute": "department",
      "claim.name": "department",
      "jsonType.label": "String",
      "id.token.claim": "true",
      "access.token.claim": "true",
      "userinfo.token.claim": "true"
    }
  }'
```

### Token lifetimes (realm-wide)
```bash
curl -X PUT "$KC/admin/realms/$REALM" "${auth[@]}" -H "Content-Type: application/json" -d '{
  "accessTokenLifespan": 300,
  "ssoSessionIdleTimeout": 1800,
  "ssoSessionMaxLifespan": 36000,
  "offlineSessionIdleTimeout": 2592000
}'
```

## Wiring app SSO (pattern)
For each app (OpenShift OAuth, ArgoCD Dex/OIDC, Grafana generic OAuth): create a **confidential OIDC client**, set its exact `redirectUris`, share `clientId`/secret with the app, map the claims it expects (groups/roles via a **group membership** or **realm/client role** mapper), and point the app at the realm's discovery doc `…/.well-known/openid-configuration`. Validate tokens locally via JWKS (`/certs`). See `references/securing-apps-oidc-saml.md`.

## Troubleshooting (quick)
- **CORS errors** → set the client's `webOrigins` (exact origins; `+` to mirror redirect URIs).
- **Invalid redirect URI** → the request URI must match a `redirectUris` entry exactly (mind trailing `/` and wildcards).
- **Custom claim missing from token** → mapper must be on a client scope that's in the client's default/optional scopes and the right `*.token.claim` flags set; check with the client's *evaluate-scopes / generate-example-access-token* endpoint.
- **User cannot log in** → enabled? required actions pending? brute-force lockout (Security defenses / attack-detection API)? email-verify required?
- **LDAP sync fails** → verify server URL/SSL, Bind DN + credential, Users DN, username attribute; enable logger `org.keycloak.storage.ldap`.

## Air-gap & version notes
- **Most references are regenerated directly from the bundled RHBK 26.6 documentation bodies (now `reference/keycloak/`)** — `securing-apps-oidc-saml.md`, `server-configuration.md`, `server-administration.md`, `high-availability.md`, `authorization-services.md`, `server-development.md`, plus `rhbk-operator.md`, `observability.md`, `migration-upgrading.md`. Every flag, endpoint, field, and class name in them is copied verbatim from the RHBK 26.6 guide chapters (docs.redhat.com). `admin-rest-api.md` remains distilled from the upstream Keycloak 26 docs; `rhbk-platform-support.md` and `rhbk-troubleshooting-kb.md` are Red Hat support/KB-derived. Pinned to RHBK 26.6 (productizes upstream Keycloak 26.6.3). Verify against your exact build; flags/paths/field names occasionally shift between releases.
- All previously-flagged `TODO` markers have been **resolved** — values confirmed against keycloak.org / `github.com/keycloak/keycloak` (SPI signatures) / Red Hat docs, or removed where genuinely unverifiable. The `references/` carry **no** unresolved TODOs.
- **Red Hat build of Keycloak (RHBK):** `rhbk-platform-support.md` and `rhbk-troubleshooting-kb.md` are distilled from Red Hat docs/KB (docs.redhat.com / access.redhat.com / catalog.redhat.com), pinned to **RHBK 26.6 GA** (productizes upstream Keycloak 26.6). KB **resolution bodies are subscriber-gated** — those files index IDs + Verified/Unverified status as offline pointers, not full solutions. RHBK feature status (Supported/Tech-Preview/Dev-Preview/Deprecated) and RHBK-vs-upstream deltas are called out per item; **never treat a Preview feature as production-ready**. Validate matrices/lifecycle dates against your subscription + exact version.
- The `references/` files make this skill usable **without internet**. The only outbound strings in this skill are `keycloak.org` / `redhat.com` doc attributions and Red Hat KB/RHSA IDs — there are **no** network calls.
- **Bundled local KB (in the vault, `reference/keycloak/`):** a searchable mirror of 1,840 RHBK/RH-SSO records (800 full doc/solution bodies, 26.0→26.6) as Markdown notes, queried offline via `_meta/wikikb/kb.py` (or `grep`). It is a *filtered* slice of a Customer Portal harvest — coverage is best-effort, not exhaustive; subscriber-gated KB **bodies are absent** (pointers only). Prefer it for exact wording/version lookups; treat the distilled `references/` as the fast top layer.
- For a byte-perfect local copy of the full docs, download the official Keycloak/RHBK documentation distribution on a connected host and stage it internally.

_Source: Keycloak Documentation (keycloak.org) + Red Hat build of Keycloak docs & KB (docs.redhat.com / access.redhat.com), distilled into a self-contained offline skill._
