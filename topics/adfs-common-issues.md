---
title: AD FS Common Issues
type: topic
domain: active-directory
slug: adfs-common-issues
summary: The dominant recurring AD FS failure cluster from the community corpus — certificate-lifecycle breakage (token-signing/service-comm rollover, farm-member propagation, TLS/SSL vs. service-comm cert confusion), WAP/proxy 503s, and claims-rule pass-through gaps — framed as ranked, often-unconfirmed hypotheses since no vendor doc backs this material.
sources:
  - "web:https://learn.microsoft.com/en-us/answers/questions/1004218/adfs-server-suddenly-starts-failing-exactly-1-mont (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1121969/adfs-farm-member-not-getting-updated-certificate (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1479054/how-to-update-adfs-server-ssl-certificate (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/122472/adfs-token-signing-certificate-auto-rollover (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1105569/nov-08-2022-updates-broke-adfs (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1179045/adfs-external-facing-site-error-with-service-unava (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/112917/port-443-incoming-is-not-working-on-adfs-wap (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1253700/cannot-replace-existing-adfs-communication-certifi (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1046539/adfs-claims-provider-not-receiving-username-email (Microsoft Q&A, fetched 2026-07-25)"
provenance_extracted: 9
provenance_inferred: 2
provenance_ambiguous: 2
tags: [ad-authn, ad-certificate-services, troubleshooting]
status: draft
updated: 2026-07-25
---

# AD FS Common Issues

**AD FS has no coverage in this wiki's vendor-doc reference corpus —
[[windows-server-identity-coverage-gaps]] explicitly notes it was out of
scope — but it is the single largest recurring problem cluster in the
Microsoft Q&A harvest. The dominant failure mode by far is certificate
lifecycle management: AD FS separates several certificate roles (TLS/SSL,
service-communications, token-signing, token-decrypting) that operators
routinely conflate, and rotating any of them incorrectly tends to surface as a
farm-wide outage weeks after the change, not immediately (inferred).**

## Community Q&A (upstream)

> Every claim below comes from a Microsoft Q&A community thread, not a
> Microsoft support statement or product documentation. Answerer roles are
> noted per claim. Several flagship threads here end **unresolved** — ranked
> hypotheses only, no confirmed root cause — and are presented that way
> deliberately; do not read an unresolved thread's leading hypothesis as a
> confirmed fix.

### Flagship, unresolved: farm fails exactly one month after a "successful" cert renewal

A farm renewed its service-communications, token-signing, and
token-decrypting certificates together, and everything worked for **exactly
31 days** before failing completely: every AD FS endpoint returned 503, the
AD FS service itself would not start (Error 1064), and Server Manager logged
paired **381/102** errors — an `MSIS2013` message that the certificate chain
could not be built because a certificate was outside its validity period,
referencing the thumbprint of the **old, already-expired** certificate (not
the new one). Deleting the old cert from the store did not help — it produced
a **249** warning instead ("certificate...could not be found in the
certificate store...can potentially cause a failure when the Federation
Service is signing or decrypting"), meaning AD FS was still internally
referencing the old thumbprint regardless of whether it existed. Attempting
the standard PowerShell fix (`Set-AdfsSslCertificate`) itself failed —
`Get-AdfsCertificate`/`Set-AdfsSslCertificate` connect to `adfssrv` over
`net.tcp://localhost:1500/policy`, and that endpoint refused the connection
because the AD FS service was down — a circular dependency where the fix
requires the broken service. Two hypotheses were offered, **neither confirmed
by the original poster**:
- *Community member*: check whether the **AD FS configuration database**
  service is running — Windows Internal Database (WID) if used, or SQL
  Server if used — since the management cmdlets depend on it.
- *Microsoft Moderator*: the exact "one month" timing is suspicious for a
  **CRL-expiry-driven revocation check**; separately, check
  `netsh http show sslcert` — the HTTP.sys SSL binding may still reference
  the **old** certificate's thumbprint even though AD FS's own configuration
  shows the new one, and can be repointed with
  `netsh http add sslcert ipport=<ADFS URL>:443 certhash=<new cert hash>
  appid={5d89a20c-beab-4389-9447-324788eb944a}`.

Both are plausible, neither is confirmed — this thread is the clearest example
in the corpus of a cert-rollover break-fix question with only ranked
hypotheses, not a resolution (web:1004218) **(ambiguous)**.

### Cert rollover does not reliably propagate to farm members

A separate report: after updating the service-communications certificate on
the primary AD FS node via `Set-AdfsCertificate`/`Set-AdfsSslCertificate`, a
farm member kept showing the **old** thumbprint even after a service and
server restart — while otherwise functioning normally. This thread received
**zero community answers**; there is no confirmed fix for farm-member cert
propagation lag in this corpus (web:1121969).

### TLS/SSL certificate vs. service-communications certificate — a recurring point of confusion

AD FS's **TLS/SSL certificate** (bound at the HTTP.sys level, changed via
`Set-AdfsSslCertificate -Thumbprint <thumbprint>`) is a **different object**
from the **Service Communications certificate** shown in the AD FS Management
snap-in — conflating the two is common. AD FS has not used IIS "in over a
decade," so IIS-era documentation for changing this certificate is stale;
current guidance is the `manage-ssl-certificates-ad-fs-wap` Microsoft Learn
page, or the Microsoft Entra Connect GUI if federation is managed that way. A
second, MVP-authored answer in the same thread adds the operational checklist:
obtain a publicly trusted cert for production farms, import it to the local
machine store on **every** AD FS and WAP server, then run
`Set-AdfsSslCertificate` on the primary node (web:1479054).

### Auto certificate rollover: relying parties must trust both certs at once

With AD FS's automatic token-signing certificate rollover enabled
(`CertificateGenerationThreshold`, `CertificatePromotionThreshold`, etc.), a
new secondary certificate generates roughly `CertificateGenerationThreshold`
days before the current one expires and is promoted to primary roughly
`CertificatePromotionThreshold` days after that — but the exact timing can
drift by hours (one environment reported 6 hours late, which a Microsoft
Moderator attributed, tentatively, to timezone conversion). The moderator's
key point: AD FS publishes **both** the primary and secondary signing
certificates in its federation metadata specifically so relying parties can
be configured to accept either — meaning the exact rollover moment should be
irrelevant to a correctly configured application. If a relying party breaks
during rollover, that indicates the RP **cannot accept two signing
certificates**, which the moderator frames explicitly as "an app issue," not
an AD FS defect. Administrators who need precise control can temporarily
disable `AutoCertificateRollover`, promote manually, then re-enable it
(web:122472).

### A cumulative update broke Kerberos auth for an AD FS-fronted environment

After rebooting DCs following a November 2022 patch, AD FS stopped working; a
subsequent out-of-band update (KB5021656) did not fix it either. The one
community reply — self-reported as "what fixed this for us," **not
independently confirmed elsewhere in the thread** — was clearing the
`ms-DS-SupportedEncryptionTypes` AD attribute entirely on the accounts used
for Kerberos auth; the reporter states *any* value in that attribute, even
`0x0`, triggered authentication failures post-patch (web:1105569).

### WAP "Service Unavailable" (HTTP 503) — three commonly reported causes

For the externally facing AD FS/WAP sign-in page returning "HTTP Error 503.
The service is unavailable," a 2024 community answer lists three causes seen
repeatedly: (1) the relying party's configured SAML login-redirect base
address doesn't exactly match AD FS's own configured address; (2) the AD FS
Windows service isn't running, frequently because the AD FS service
account's password expired or was rotated without updating the service; and
(3) the request isn't hitting the correct resource path — it must be
`/adfs/ls`, not just the bare hostname (web:1179045).

### WAP health-probe 503s: SNI mismatch, not an actual outage

Separately, a load balancer (F5) reported WAP as completely unresponsive on
port 443 despite a valid certificate and an established WAP↔AD FS trust. A
Microsoft Moderator explains: AD FS and WAP both rely on **TLS SNI**, so they
only respond to an HTTPS request for the AD FS farm's specific FQDN — if the
health-probe's TLS ClientHello doesn't send SNI (as was the case with F5's
probe), the endpoint looks offline even though it's healthy. Fix: point the
probe at the plain-HTTP `/adfs/probe` endpoint instead of the HTTPS
FQDN, or configure an SNI fallback certificate (web:112917).

### "Cannot replace AD FS communication certificate" — a checklist, not a guaranteed fix

Running `Set-AdfsSslCertificate` with a valid, already-installed thumbprint
can abort the `adfssrv` service ("the socket connection was aborted") with
nothing useful logged. An MVP-authored checklist: confirm the new certificate
has a private key and sits in the correct store; run PowerShell elevated;
**restart `adfssrv` before retrying** the command (rather than after a
failure); consider raising the AD FS endpoint execution-time-limit if it's a
timeout; and follow `Set-AdfsSslCertificate` with `Update-AdfsSslCertificate`
(web:1253700).

### Claims Provider Trust pass-through requires rules on both sides

For an SP↔AD FS↔IDP claims-provider chain, a claim (e.g. NameID/username/email)
received from the upstream SP is **not** automatically forwarded to the
downstream Claims Provider (IDP) — a Microsoft Moderator confirms a pass-through
rule is required on **both** the Claim Provider Trust (for the IDP) **and**
the Relying Party Trust (for the SP); a rule on only one side silently drops
the claim (web:1046539).

## Contradictions / caveats

- Several of the threads above (web:1004218, web:1121969, web:1105569) end
  without the original poster confirming the proposed fix worked. Cert-rollover
  problems in particular are presented here as **ranked hypotheses**, not
  confirmed root causes — see [[windows-server-identity-coverage-gaps]] for why
  no vendor-backed AD FS reference exists in this wiki to cross-check against.
- The pattern across this cluster — separate TLS/SSL, service-communications,
  and token-signing/decrypting certificate objects, each with its own
  rotation mechanism and none of them obviously unified in tooling — is the
  single biggest source of AD FS outages in this corpus and is worth treating
  as a design hazard in its own right, not just a collection of unrelated
  incidents (inferred).

## See also
- [[ad-certificate-services]]
- [[certificate-templates]]
- [[ad-trusts]]
- [[windows-server-identity-coverage-gaps]]
- [[active-directory-implementation-review]]
