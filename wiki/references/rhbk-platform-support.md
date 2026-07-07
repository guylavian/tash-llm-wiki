# RHBK Platform & Support — Offline Reference

_Distilled from Red Hat docs & KB (docs.redhat.com / access.redhat.com / catalog.redhat.com); some content subscriber-gated._
_Red Hat build of Keycloak (RHBK) productizes upstream Keycloak. **Validate against your own subscription + exact version** — supported matrices and lifecycle dates change per release; gated articles need a Red Hat login._

## 1. Version & release cadence
- **Current GA: RHBK 26.6** (image stream tags `26.6`, e.g. `26.6.2`).
- Minor versions track **even-numbered** upstream Keycloak (`26.0, 26.2, 26.4, 26.6 …`), ~every **6 months**; odd upstream quarterlies are skipped.
- Productized components per release (article **7027683**): e.g. RHBK 26.4.z = Keycloak 26.4.12 / Quarkus 3.27.3 / Infinispan 15.0.19; RHBK 22.0.z = Keycloak 22.0.13 / Quarkus 3.2.12 / Infinispan 14.0.27. Marshalling switched from JBoss Marshalling to Infinispan Protostream starting RHBK 26.

## 2. Supported configurations matrix (article 7033107, RHBK 26.6.x)
| Axis | Supported (26.6.x) |
|---|---|
| OpenShift | OCP 4.21, 4.20, 4.19, 4.18, 4.16, 4.14, 4.12 (HA via Operator needs **OCP 4.18+**) |
| Host OS (non-container) | RHEL 10/9/8 (x86_64); Windows Server 2022/2019 |
| Architectures | x86_64, s390x, ppc64le, aarch64 |
| JVM | Red Hat OpenJDK 25/21/17; Eclipse Temurin 25/21/17 |
| Databases | PostgreSQL 18.x–14.x; MySQL 8.4/8.0 (LTS); MariaDB 11.8/11.4/10.11/10.6 (LTS); MS SQL 2022/2019; Oracle 23ai/19c (LTR); Aurora PostgreSQL 17.x–15.x; Azure SQL 2022; EDB Postgres Advanced 18.x/17.x |
| HA cache | **Red Hat Data Grid 8.5.3+** (external Infinispan) for multi-site |
| User federation | Active Directory; Red Hat Directory Server 12/11; IdM on RHEL 10/9/8 |
| Browsers | Chrome, Firefox, Edge, Safari (latest) |

> The **container image is supported only on OpenShift** for production — not bare-metal container runtimes. (26.4.x matrix differs: OCP 4.20–4.14 excl. 4.15; RHEL 9/8; JDK 21/17; PostgreSQL 17.x–14.x.)

## 3. Lifecycle & support phases (policy: …/red_hat_build_of_keycloak_notes)
- **Full Support** (GA → next major; new features, certs, all patches) → **Maintenance Support** (≥6 months; Critical/Important security + select mission-critical bug fixes only; Moderate at Red Hat discretion).
- **26.x ≥ 2-year** full lifecycle; **27.x+ ≥ 3-year**. ≥2 major.minor streams supported concurrently. A minor is supported ~12 months / until a 2nd-subsequent minor ships.
- 24.x ≈ 12 months; 22.x got a 3-month maintenance extension. Authoritative date table is gated (article **7040805**) / the Product Life Cycles dashboard.

## 4. Subscriptions & entitlements (article 7044244)
- **Not sold standalone.** Entitled via **Red Hat Runtimes**, **Application Foundations (RHAF)**, **OpenShift (OCP)**, **OpenShift Platform Plus**, or any bundle including Runtimes/OCP. IBM Cloud Paks entitle via bundled OCP restricted license.
- Core usage **counts against the enclosing bundle's cores** (change from RH-SSO).
- On managed OpenShift (ROSA/ARO/OSD), RHBK is **customer-installed** software — fully supported but **not operationally managed**. There is **no RHBK managed-service**.

## 5. Container images & Operator
**Images (catalog.redhat.com, namespace `rhbk/`):** all UBI9-Micro, **run as UID 1000**, GA, maintained by the Red Hat SSO team.
| Image | Tag | Ports / notes |
|---|---|---|
| `rhbk/keycloak-rhel9` | `26.6` / `26.6-3` | 8080 HTTP, 8443 HTTPS, **9000 management** (`/health`, `/metrics`); ~254 MB compressed |
| `rhbk/keycloak-rhel9-operator` | `26.6` / `26.6-3` | component image (installed via OLM, not pulled directly); level-4 operator |
| `rhbk/keycloak-operator-bundle` | `26.6.2` | OLM metadata (CRDs/RBAC/CSV) |

**Operator install (OperatorHub/OLM):** package **`rhbk-operator`**, source **`redhat-operators`** in **`openshift-marketplace`**, channel **`stable-v26`** (pattern `stable-v{major}`). **Namespace-scoped only** — supports **OwnNamespace / SingleNamespace**, **NOT AllNamespaces** (one instance per watched namespace). CRDs: **`Keycloak`** + **`KeycloakRealmImport`** under `k8s.keycloak.org` (`v2alpha1` — note: `v2alpha1` is being deprecated, see §9).
```yaml
# air-gap note: mirror the operator + images into your internal registry first (see KB 7059012)
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata: { name: rhbk-operator, namespace: keycloak }
spec:
  channel: stable-v26
  name: rhbk-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```

## 6. Sizing (HA Guide — concepts-memory-and-cpu-sizing)
- Baseline pod ≈ **1250 MB** (realm cache + 10k sessions); **+~500 MB per 100k active sessions** (3-node, tested to 200k). JVM heap = **70% of container limit**; +300 MB non-heap.
- CPU (3-node): 1 vCPU per **8 password logins/s**; 26.2 ratios: 1 vCPU/cluster per **120 client-credential grants/s** and per **120 refresh-token req/s**. Leave **150% CPU headroom**; DB ≈ **1400 write IOPS per 100 login/logout/refresh req/s**. **Load-test before production.**

## 7. Errata / RHSA & CVE pointers (map CVEs → fixed-in RHBK)
| RHSA | Severity | Date | Fixes (selected CVEs) | Fixed-in |
|---|---|---|---|---|
| RHEA-2026:22858 | Enhancement | 2026-06-03 | CVE-2026-2100/4046/4437/4438/4878 | 26.6.2 images |
| RHSA-2025:22091 | Moderate | 2025-11-25 | CVE-2025-13467 (LDAP deserialization → RCE) | 26.4.6 |
| RHSA-2025:22088 | Moderate | 2025-11-25 | CVE-2025-13467, -12390 (offline session takeover) + 7 more | 26.2.11 images |
| RHSA-2025:19925 | Moderate | 2025-11-07 | CVE-2025-10044 (error_description injection) | 26.0.17 |
| RHSA-2025:8690/8672 | Important | 2025-06-09 | CVE-2024-47072 (XStream DoS), CVE-2025-3501 (hostname verify) | 26.2.5 |
| RHSA-2025:0300 | Moderate | 2025-01-13 | CVE-2024-11734, -11736 | 26.0.8 |
| RHSA-2024:10178/10175 | Important | 2024-11-21 | CVE-2024-9666 (proxy-header DoS), -10039 (mTLS), -10451, -10270, -10492 | 26.0.6 / 24.0.9 |
| RHSA-2024:6887 | Important | 2024-09-19 | CVE-2024-8698 (SAML verify → privesc), -8883 (open redirect) | 22.0.13 images |
| RHSA-2024:1868 | Important | 2024-04-16 | CVE-2023-3597 (step-up bypass), CVE-2024-1249 (iframe CSRF) +6 | 22.0.10 |

> For an air-gapped estate, map upstream Quarkus/Infinispan CVEs to RHBK via the **component-version table (7027683)**, then to the fixing RHSA.

## 8. RHBK feature status map (Supported / TP / DP / Deprecated)
| Feature | Status in 26.6 | Flag / note |
|---|---|---|
| Standard Token Exchange v2 | **Supported** (default since 26.2) | `token-exchange-standard:v2` |
| DPoP | **Supported** (since 26.4, all grant types) | — |
| Recovery codes | **Supported** (since 26.4) | — |
| Fine-grained admin permissions v2 | **Supported** (since 26.2) | `admin-fine-grained-authz:v2` |
| FIPS 140-2 mode | **Supported** | `--features=fips`; **BCFIPS not bundled** (license) — install manually; RHEL-only (see §9) |
| JWT Authorization Grant (RFC 7523) | **Supported** (26.6) | external-signed JWT → access token |
| Federated Client Authentication | **Supported** (26.6) | trust external OIDC IdP / K8s SA instead of client secret |
| Workflows (IGA) | **Supported** (26.6) | YAML-defined admin tasks, event/schedule-driven |
| Zero-downtime patch releases | **Supported** (26.6) | rolling x.y.z patches; set Operator update strategy **Auto** |
| Passkeys (Conditional UI) | **Technology Preview** | `--features=passkeys` |
| Step-up Authentication for SAML | **Technology Preview** (26.6) | `step-up-authentication-saml` |
| Identity Brokering APIs v2 | **Technology Preview** (26.6) | `identity-brokering-api:v2`; session-based token store; successor to Token Exchange v1 |
| JavaScript Providers (scripts SPI) | **Technology Preview** (disabled by default) | `--features=scripts` |
| Quick Theme | **Technology Preview** | `--features=quick-theme` |
| OAuth Client ID Metadata Doc (CIMD) | **Developer Preview** | MCP authz; experimental |
| Admin REST OpenAPI spec | **Technology Preview** | the spec itself is TP |
| Legacy Token Exchange v1 | **Deprecated** (26.6) | `token-exchange:v1` → migrate to v2 / Brokering v2 |
| `v2alpha1` Keycloak/RealmImport CRDs | **Deprecated** | migrate per migration guide |

> **Never present a Preview feature as production-ready.** TP/DP features are disabled by default and excluded from production support.

## 9. Version deltas vs RHBK-specific deltas
> Important framing: most "RHBK 26" behavior changes are actually **upstream Keycloak 26** changes (verified against keycloak.org) — they are *not* RHBK-vs-upstream differences. Only group 9b is genuinely Red Hat-specific.

### 9a. RH-SSO 7.x / legacy → Keycloak 26 (shared with upstream Keycloak 26)
| Change | Note |
|---|---|
| HA model | Active-active multi-site + **mandatory persistent DB-backed user sessions** (replaces the RH-SSO-era in-memory / active-passive model). This is the upstream Keycloak 26 default — see `high-availability.md` §3–§4. |
| Runtime | WildFly/JBoss EAP → **Quarkus**; `standalone.xml`/`jboss-cli` → `keycloak.conf` / env / CLI; context root `/auth` → `/`. |
| Feature toggles | Enabled at **build time** (`kc.sh build --features=…`), not the legacy `-Dkeycloak.profile.feature.*` system property. |
| Reverse proxy | `--proxy-headers` (`forwarded`/`xforwarded`); the Undertow `proxy-address-forwarding` knob is gone. |
| Token Exchange | Standard v2 GA/default; legacy v1 deprecated. |
| FIPS BCFIPS jars | **Not bundled** (BouncyCastle-FIPS licensing) — must be added manually. *Also true upstream.* |

### 9b. RHBK packaging/support deltas vs upstream Keycloak (genuinely Red Hat-specific)
| Delta | Note |
|---|---|
| Container JVM | RHBK images are pinned to **OpenJDK 21** even though RHBK's *standalone* supported-JVM matrix (§2) lists Java 25. (Upstream images also use 21, so this is a packaging-consistency caveat — just don't claim Java 25 *in containers*.) |
| FIPS support scope | Red Hat **supports** FIPS mode (`fips:v1`) **only on a RHEL-based OS** — a Red Hat support restriction, not an upstream code limit. |

> Broader RHBK packaging/support deltas — the supported-config matrix, lifecycle/EOL, subscriptions, container images, Operator, and errata — are documented canonically in **§1–§7** above and are not repeated here.

## 10. RH-SSO → RHBK migration
- **RH-SSO 7.x Full + Maintenance support ended 2025-06-30** (article 5252391); **no ELS**. RHBK is the named successor; RH-SSO 7.6 was the last feature release.
- **Architecture:** WildFly/JBoss EAP → **Quarkus**. `standalone.xml`/`jboss-cli`/subsystems → flat **`keycloak.conf`** (+ env vars / CLI). Context root **`/auth` → `/`** (restore with `--http-relative-path=/auth`). Custom providers move `standalone/deployments/` → **`providers/`** + `kc.sh build`.
- **Server migration:** stop RH-SSO so it no longer touches the shared DB → back up DB → install OpenJDK → start RHBK (DB migration auto, or manual SQL file for DBA review).
- **Adapters:** legacy Keycloak client adapters (OIDC servlet filter, JAAS, Spring Boot adapter, EAP OIDC adapter) **deprecated in 22, removed in 26.x** → use EAP 8 native OIDC / Spring Security native OAuth2; EAP 8 SAML feature pack remains the SAML path.
- **Known migration breakages** → see `rhbk-troubleshooting-kb.md` (redirect_uri strictness, SAML RSA-SHA1 blocked, account-theme `index.ftl`, default-IdP-in-Browser-flow lockout).

_Source: Red Hat docs (docs.redhat.com), Customer Portal (access.redhat.com), Ecosystem Catalog (catalog.redhat.com). Some articles/KB bodies are subscriber-gated; validate dates/matrices against your subscription and exact RHBK version._
