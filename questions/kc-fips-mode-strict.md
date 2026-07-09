---
title: What does the kc.sh --fips-mode=strict flag do?
type: question
question_tier: conceptual
domain: keycloak
slug: kc-fips-mode-strict
summary: "--fips-mode=strict enables BCFIPS approved mode (tighter crypto constraints); without it BCFIPS runs in non-approved mode. Mandates BCFKS keystores, ≥2048-bit RSA, ≥14-char passwords, blocks PKCS12/JKS and RSA1_5 JWE."
sources:
  - guide:server_configuration_guide
provenance:
  extracted: 8
  inferred: 0
  ambiguous: 0
status: draft
updated: 2026-07-07
---

# What does the `kc.sh --fips-mode=strict` flag do?

`--fips-mode=strict` (used with `--features=fips`) tells the BouncyCastle FIPS provider to run in **approved mode** — stricter cryptographic constraints. Without it, BCFIPS runs in non-approved mode with relaxed requirements.

## Answer

See [[fips-mode]] for the full breakdown. Key differences from non-strict:

- **Keystores:** BCFKS required; PKCS12 and JKS unsupported
- **Passwords:** ≥14 characters (112-bit PBKDF2 minimum)
- **RSA keys:** ≥2048 bits
- **HMAC-SHA secrets:** ≥14 characters
- **JWE:** RSA1_5 blocked
- **Password hashing:** Argon2 disabled; only PBKDF2 available

## See also
- [[fips-mode]]
- [[fips-startup-bouncycastle]]
- [[feature-flags]]

## References
### RH ground-truth
- `guide:server_configuration_guide` — Chapter 17: FIPS 140-2 support (RHBK 26.4)

### Wiki
- [[fips-mode]] — entity page for the `--fips-mode` option
- [[fips-startup-bouncycastle]] — FIPS startup failures and fixes
- [[feature-flags]] — which features exist and how to enable them
