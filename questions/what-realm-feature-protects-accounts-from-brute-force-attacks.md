---
origin: eval-cohort
title: What realm feature protects accounts from brute force attacks?
type: question
domain: keycloak
slug: what-realm-feature-protects-accounts-from-brute-force-attacks
summary: "Brute Force Detection — a realm-level security feature that temporarily or permanently locks accounts after repeated failed logins; disabled by default."
sources:
  - guide:server_administration_guide
  - kb:mitigating_security_threats
provenance:
  extracted: 4
  inferred: 1
  ambiguous: 0
question_tier: conceptual
status: draft
updated: 2026-07-12
---

# What realm feature protects accounts from brute force attacks?

**Brute Force Detection** — a realm-level security feature configured under *Realm Settings → Security Defenses → Brute Force Detection* that temporarily or permanently disables user accounts after repeated login failures. Disabled by default (`rhbk-26-4-mitigating-security-threats.md:30`).

## Behavior

The feature tracks failed login attempts per user. Once the threshold (`Max Login Failures`, default 30) is exceeded, RHBK locks the account — temporarily, permanently, or a mix of both depending on the chosen mode (`rhbk-26-4-mitigating-security-threats.md:27-29`). Locked users see the generic `Invalid username or password` message, the same as for an invalid username, so attackers can't distinguish a disabled account from a bad credential (`rhbk-26-4-mitigating-security-threats.md:28-29`).

## Lockout modes

- **Lockout permanently** — account stays locked until an admin re-enables it (`rhbk-26-4-mitigating-security-threats.md:37-39`).
- **Lockout temporarily** — account is locked for a growing period; the wait time increases with each breach of the threshold using either a *By multiples* or *Linear* strategy (`rhbk-26-4-mitigating-security-threats.md:68`).
- **Lockout permanently after temporary lockout** — starts as temporary, then escalates to permanent after a configurable number of temporary lockouts (`rhbk-26-4-mitigating-security-threats.md:176-178`).

## Key parameters

| Parameter | Default |
|---|---|
| Max Login Failures | 30 |
| Quick Login Check Milliseconds | 1000 ms |
| Minimum Quick Login Wait | 1 minute |
| Wait Increment | 1 minute |
| Max Wait | 15 minutes |
| Failure Reset Time | 12 hours |

(`rhbk-26-4-mitigating-security-threats.md:40-46,71-81`)

## Caveats

- **DoS exposure:** An attacker who knows account names can deliberately trigger lockouts, making the server vulnerable to denial-of-service (`rhbk-26-4-mitigating-security-threats.md:262-264`). Combine with strong [[password-policies]] and [[otp-policies]] rather than relying on lockout alone (inferred).
- **Volatile state:** Failure counters are stored in memory (Infinispan caches); a server restart clears them (`rhbk-26-4-upgrading.md:32`).
- **26.6+ Secondary Authentication Failures Lockout:** A new mechanism permanently locks the account when secondary factor failures (e.g. OTP) exceed a maximum, even in temporary lockout mode (`rhbk-26-6-migration-changes.md:138-141`).

## See also

- [[brute-force-detection]]
- [[password-policies]]
- [[otp-policies]]
- [[security-hardening-checklist]]

## References

**RH ground-truth (kb:/guide:/ref:):**
- `guide:server_administration_guide` → Chapter 16, Mitigating security threats (RHBK 26.4)
- `kb:mitigating_security_threats` → `rhbk-26-4-mitigating-security-threats.md`
- `kb:migration_changes` → `rhbk-26-6-migration-changes.md` (Secondary Authentication Failures Lockout)

**Wiki:**
- [[brute-force-detection]]
- [[password-policies]]
- [[otp-policies]]
- [[security-hardening-checklist]]
