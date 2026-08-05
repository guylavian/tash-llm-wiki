---
title: "Chapter 5. Updates for 26.4.10 - Red Hat build of Keycloak 26.4 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-4-updates-for-26-4-10
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/release_notes/updates_for_26_4_10
guide: release_notes
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "This release contains several fixed issues and changes related to upgrading. For details, see the Upgrading Guide. 5.1. CVE fixes CVE-2026-0707 Keycloak’s authentication pipeline excessively tolerates non-standard Bearer token formats (case variations, Tab characters, multiple spaces, mixed whitespace) in the Authorization header, creating inconsistencies with front-end security controls (WAF/prox…"
---

# Chapter 5. Updates for 26.4.10 - Red Hat build of Keycloak 26.4 Release Notes

Chapter 5. Updates for 26.4.10
This release contains several fixed issues and changes related to upgrading. For details, see the Upgrading Guide.
5.1. CVE fixes

- CVE-2026-0707 Keycloak’s authentication pipeline excessively tolerates non-standard Bearer token formats (case variations, Tab characters, multiple spaces, mixed whitespace) in the Authorization header, creating inconsistencies with front-end security controls (WAF/proxies) and enabling potential bypass risks.
- CVE-2026-1190 When SAML is configured to act as a client (SAML brokering) it does not check NotOnOrAfter is defined inside the SubjectConfirmationData. This just affects in the sense that an attacker can delay the response for more of the expected time..
-
CVE-2026-2092 Unauthorized access by improper validation of encrypted SAML assertions. Keycloak validates that plaintext
<Assertion>
elements are signed when the response root is not signed, but it does not apply the same binding requirement to<EncryptedAssertion>
- CVE-2026-2575 An unauthenticated remote attacker can trigger a Denial of Service (DoS) by sending a highly compressed SAMLRequest by the SAML Redirect Binding. The server fails to enforce size limits during DEFLATE decompression, leading to an OutOfMemoryError (OOM) and process termination.
- CVE-2026-2603 A SAML Identity Provider that is disabled in the broker realm can still complete IdP‑initiated broker logins.
- CVE-2026-2733 Improper Authorization vulnerability in the Docker v2 authentication endpoint (/protocol/docker-v2/auth) of Keycloak. Even after the client is administratively disabled, the endpoint continues to issue valid authentication tokens when provided with valid user credentials and client ID.
- CVE-2026-3047 A SAML client marked Disabled in the broker realm still completes IdP-initiated broker login and creates a realm SSO session.
- CVE-2026-3009 Improper Authorization vulnerability. The flaw occurs because the broker login endpoint does not re-validate the enabled/disabled status of the configured Identity Provider (IdP) at the time of login processing.
