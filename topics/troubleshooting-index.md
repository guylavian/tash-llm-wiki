---
title: RHBK Troubleshooting — index by area
type: topic
domain: keycloak
slug: troubleshooting-index
summary: "Triage map for Red Hat build of Keycloak / RH-SSO, organized by area, linking the public-fix entity pages and pointing at the gated KB solutions"
sources:
  - ref:rhbk-troubleshooting-kb.md
  - kb:7142778
  - kb:7135882
  - kb:7138771
  - kb:7135122
  - kb:7135124
  - kb:7128352
  - kb:7073090
  - kb:7126933
  - kb:7128299
  - kb:7142577
  - kb:7141508
source_notes:
  - "[[doc-7142778]]"
  - "[[doc-7135882]]"
  - "[[doc-7138771]]"
  - "[[doc-7135122]]"
  - "[[doc-7135124]]"
  - "[[doc-7128352]]"
  - "[[doc-7073090]]"
  - "[[doc-7126933]]"
  - "[[doc-7128299]]"
  - "[[doc-7142577]]"
  - "[[doc-7141508]]"
provenance_extracted: 22
provenance_inferred: 2
provenance_ambiguous: 0
tags: [concept]
status: draft
updated: 2026-07-02
---

# RHBK Troubleshooting — index by area

**Triage map for Red Hat build of Keycloak / RH-SSO, organized by area, linking the
public-fix entity pages and pointing at the gated KB solutions.**

> **Honesty rule.** The bundled KB has **1,030 solutions but only 40 public
> bodies**; the other ~990 are **subscriber-gated** — their resolution steps are
> NOT present here. Gated items below are pointers only (symptom + URL). Items
> marked *gated — resolution requires Red Hat login* must be opened on
> [access.redhat.com](https://access.redhat.com) with a subscription.
> Full offline search: see the QUERY op in [`CLAUDE.md`](../CLAUDE.md) — grep
> `reference/keycloak/`, or `kb.py --domain keycloak search "<terms>" --gated` to
> include gated pointers.

## Database & JDBC
Public fixes exist for Oracle TCPS failover and PostgreSQL session-row buildup.
Most DB issues (URL format, vendor field, pool timeouts) are gated.

- [[oracle-jdbc-failover]] — `ORA-17002 ... Authentication lapse 0 ms`; driver
  23.2.0.0.0 defect, replace the JDBC JAR (kb:7142778, public).
- [[persistent-sessions-db-cleanup]] — `user_session` rows linger after
  logout/expiry; tune `spi-user-sessions-jpa-*` or disable persistent sessions
  (kb:7135882, public).
- [[rhbk-db-connection-pool]] — equal initial/min/max pool sizing for HA.
- Gated pointers (resolution requires Red Hat login):
  - JDBC "URL format error" on operator start — https://access.redhat.com/solutions/7059141
  - Configure RHBK with Oracle DB — https://access.redhat.com/solutions/7133553
  - Optimal MySQL `max_user_connections` — https://access.redhat.com/solutions/7136302

## HA / clustering / Infinispan
No public bodies in the Infinispan/HA bucket (24 solutions, all gated). Architecture
guidance lives in the wiki topics below; the KB pointers cover specific cluster faults.

- [[rhbk-ha-architectures]] · [[ha-cross-site]] · [[distributed-caches]] ·
  [[site-synchronization]] — design and split-brain recovery.
- [[uneven-pod-load-master-realm]] — one hot pod + `LOGIN_ERROR` flood; auth was
  hitting the empty **master** realm (kb:7142577, public).
- Gated pointers (resolution requires Red Hat login):
  - OpenShift SSO pod clustering `ISPN000476` timeout — https://access.redhat.com/solutions/7071281
  - JGroups TUNNEL + GossipRouter clustering not working — https://access.redhat.com/solutions/7132929
  - Retransmission Count > 0, is the cluster unhealthy? — https://access.redhat.com/solutions/7137777
  - Replacing distributed-cache with replicated-cache — https://access.redhat.com/solutions/7143556
  - Is distributed cache config required on OCP? — https://access.redhat.com/solutions/7127556

## TLS / certificates / truststore
Three public bodies across this area; truststore/LDAPS cert imports are gated.

- [[fips-startup-bouncycastle]] — FIPS BC native link error + Argon2 admin-login
  failure (kb:7135122, kb:7135124, public).
- [[keycloak-truststores]] — trusted-certificate config on the Keycloak CR.
- Gated pointers (resolution requires Red Hat login):
  - Import LDAPS certificate on RHBK Operator (`PKIX path building failed`) — https://access.redhat.com/solutions/7051525
  - Importing certificates into the Operator truststore — https://access.redhat.com/solutions/7070482
  - `Algorithm constraints check failed ... RSA 1024 bit key` trusting LDAP cert — https://access.redhat.com/solutions/7132186

## LDAP / federation / Kerberos
Six public LDAP/AD bodies — the richest public area after operator (inferred —
a comparative count across buckets, not a single-source claim).

- [[ad-idp-link-loss-objectguid]] — sporadic AD link loss / merge prompts; switch
  the IdP username template to immutable `objectGUID` (kb:7128299, public).
- AD Kerberos/SPNEGO SSO on an IdM-enrolled RHEL host — isolated
  `/opt/keycloak/conf/krb5-ad.conf` + AD keytab; no forest trust needed
  (kb:7141508, public). Captured inline in [[ldap-user-federation]].
- [[ldap-user-federation]] · [[ldap-storage-mode]] · [[ldap-mappers]] — federation
  model, edit modes, mappers.
- Related public bodies (distilled in `references/rhbk-troubleshooting-kb.md`):
  group deletion not propagated to LDAP (kb:7086086); generic "Could not modify
  attribute for DN" on password reset (kb:7086512); admin user-search with spaces
  needs quotes (kb:7115290).
- Gated pointers (resolution requires Red Hat login):
  - `Cannot find key of appropriate type to decrypt AP REP - RC4` Kerberos — https://access.redhat.com/solutions/5494481

## Operator / OpenShift
The largest bucket (218 solutions) — almost entirely gated; 4 public bodies
(inferred — a comparative count across buckets, not a single-source claim).

- [[operator-proxy-port-required]] — `Proxy port is required!`; add a port to the
  cluster-wide `Proxy` CR (kb:7073090, public).
- [[bootstrap-admin-dns-query]] — `dns_query can not be null or empty`
  (`ISPN000541`) creating a temp admin; use `--cache=local` for the bootstrap
  (kb:7128352, public).
- OpenShift HPA for the Keycloak CR (added in RHBK 26.2) — `autoscaling/v2`
  targeting `k8s.keycloak.org/v2alpha1` (kb:7078215, public).
- [[rhbk-operator]] · [[operator-deployment]] · [[operator-advanced-config]] ·
  [[keycloak-cr]] · [[operator-rolling-updates]] — operator model.
- Gated pointers (resolution requires Red Hat login):
  - Admin Console stuck "Loading the Admin UI" — https://access.redhat.com/solutions/7074762
  - RHBK loses all data after restart/upgrade to 26.2 on OCP — https://access.redhat.com/solutions/7131466
  - `podTemplate` section removed after operator upgrade — https://access.redhat.com/solutions/7131476

## Hostname / proxy / networking
Three public bodies; many proxy-header/route issues are gated.

- [[separate-sso-admin-hostnames]] — serve distinct sso/admin hosts without forced
  redirect via `hostname-strict=false` + proxy rewriting (kb:7126933, public).
- Other public bodies: missing `frame-ancestors` on static HTML is expected
  (kb:7074235); one CIBA channel URI per instance only (kb:7078728).
- Gated pointer (resolution requires Red Hat login):
  - Setting proxy headers in the Operator / RHBK 24→26 login break — https://access.redhat.com/solutions/7104900

## Tokens / sessions
**No public bodies** in the tokens/sessions bucket (41 solutions, all gated). Use
the wiki token/session topics for behavior, and the DB section above for the
session-row cleanup fix.

- [[tokens-and-sessions]] · [[session-persistence-volatile]] ·
  [[oidc-token-validation]] — lifespans, persistence model, validation.
- [[persistent-sessions-db-cleanup]] — the one public, DB-side session fix.
- Gated pointers (resolution requires Red Hat login):
  - Signed-JWT auth breaks after 26.0.11: "Token expiration too far in the future / iat missing" — https://access.redhat.com/solutions/7118179
  - Frequent re-auth in ArgoCD UI with direct RHBK OIDC — https://access.redhat.com/solutions/7143557

## Upgrade / RH-SSO → RHBK migration
One public body (the "Users in Role" read-only bug fixed in RHBK 22, kb:7064052);
the rest are gated.

- [[rhsso-to-rhbk-migration]] — server, operator, and adapter migration.
- Gated pointers (resolution requires Red Hat login):
  - FAQ: RH-SSO → RHBK upgrade — https://access.redhat.com/solutions/7132513
  - How to upgrade RHBK 26.x on OpenShift via the Operator — https://access.redhat.com/solutions/7133940
  - Operator upgrade fails `Cannot invoke "java.util.List.size()"` — https://access.redhat.com/solutions/7133712
  - Duplicate `MIGRATION_MODEL` entry blocks admin console (24→26, Oracle, manual) — https://access.redhat.com/solutions/7121862

## Performance & sizing
Only 1 solution catalogued (gated); FIPS/JVM tuning notes are public for legacy
RH-SSO (kb:3419601, heap via `standalone.conf`).

- [[rhbk-db-connection-pool]] — pool sizing for HA throughput.
- Gated pointer (resolution requires Red Hat login):
  - Perf degradation under sustained password-grant load (session persistence + Apache thread starvation) — https://access.redhat.com/solutions/7133616

## Contradictions / caveats
- Counts: `references/rhbk-troubleshooting-kb.md` distills **28** public fixes
  while the area table totals **40** public bodies across 1,030 solutions — the
  difference is non-technical / RFE / licensing Q&A intentionally skipped.
- Version sensitivity: persistent-user-sessions is default in RHBK 25/26; FIPS
  bundled-BC versions are pinned per release (26.2.10 values cited). Always check
  the exact RHBK version (26.0 / 26.2 / 26.4 / 26.6) before applying a fix.

## See also
- [[rhbk-operator]]
- [[ldap-user-federation]]
- [[tokens-and-sessions]]
- [[rhbk-ha-architectures]]
- [[rhsso-to-rhbk-migration]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[references/rhbk-troubleshooting-kb|RHBK / RH-SSO Troubleshooting — Offline KB Reference]]
- [[doc-7142778|Failover not working correctly when configuring Red Hat build of Keycloak with an Oracle Database]]
- [[doc-7135882|User sessions remain in PostgreSQL database after logout or expiration in RHBK]]
- [[doc-7138771|Unable to access Keycloak Admin WebUI after enabling Client Authentication on security-admin-console]]
- [[doc-7135122|Red Hat build of Keycloak fails to start in FIPS mode with \"UnsatisfiedLinkError\" due to incompatible Bouncy Castle libraries]]
- [[doc-7135124|Admin login fails with \"Invalid credentials\" after enabling FIPS mode due to Argon2 password hashing]]
- [[doc-7128352|RHBK Getting \"dns_query can not be null or empty\" when creating a temporary admin user]]
- [[doc-7073090|When starting the Red Hat build of Keycloak (RHBK) Operator, \"Failure in creating proxy URL. Proxy port is required!\" is returned]]
- [[doc-7126933|Configuring Keycloak with Separate Hostname URLs for SSO and Admin Console]]
- [[doc-7128299|Intermittent Loss of Active Directory Identity Provider Link in RHBK]]
- [[doc-7142577|RHBK/Keycloak Requests Are Not Being Shared Evenly Between Pods Behind Kong / NGINX Ingress]]
- [[doc-7141508|Integrating Active Directory Kerberos SSO with Keycloak on Red Hat IdM Clients]]
<!-- crosslink:end -->
