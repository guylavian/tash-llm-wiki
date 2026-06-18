---
title: "Chapter 4. Updates for 26.2.14 - Red Hat build of Keycloak 26.2 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-2-updates-for-26-2-14
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/release_notes/updates_for_26_2_14
guide: release_notes
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 4. Updates for 26.2.14 - Red Hat build of Keycloak 26.2 Release Notes

Chapter 5. Updates for 26.2.14
This release contains several fixed issues and changes related to upgrading. For details, see the Upgrading Guide.
5.1. CVE fixes

- CVE-2026-3047 A SAML client marked Disabled in the broker realm still completes IdP-initiated broker login and creates a realm SSO session.
- CVE-2026-3009 Improper Authorization vulnerability. The flaw occurs because the broker login endpoint does not re-validate the enabled/disabled status of the configured Identity Provider (IdP) at the time of login processing.
- CVE-2026-2603 A SAML Identity Provider that is disabled in the broker realm can still complete IdP‑initiated broker logins.
-
CVE-2026-2092 Unauthorized access via improper validation of encrypted SAML assertions. Keycloak validates that plaintext
<Assertion>
elements are signed when the response root is not signed, but it does not apply the same binding requirement to<EncryptedAssertion>
.
