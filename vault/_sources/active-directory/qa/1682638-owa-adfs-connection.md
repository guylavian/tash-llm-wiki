---
title: "OWA ADFS connection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1682638/owa-adfs-connection
question_id: 1682638
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
---
# OWA ADFS connection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1682638/owa-adfs-connection (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I have a problem related to OWA. I receive a SAML request from the keycloak, which is my IDP for ADFS. ADFS later sends a WS-Federation request to OWA. The page is redirected to the endpoint /owa/auth/errorfe.aspx?msg=WrongAudienceUriOrBadSigningCert. In the logs it shows me the following information: ID1044: An encrypted security token was received at the relying party which could not be decrypted. Configure the relying party with a suitable decryption certificate. Current relying party decryption certificate info: No Certificate Configured.

In the ADFS settings, in the certificates tab, I have certificates attached as Token-Decrypting and as Token-Signing. When receiving messages from Adfs, OWA displays in the logs the certificate with which this request was signed, cn=test.

In relying party trusts, as OWA I have encryption and signature certificate cn=test.

After using the command Get-ADFSCertificate all fields show the certificate cn=test.

Where could there be an error that OWA cannot load the certificate to decrypt the adfs message? Any commands that will help display the OWA certificate configuration?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-22*

It seems like there might be a mismatch or misconfiguration in the certificate settings between ADFS and OWA. Here's a suggested solution:

-  Verify that the certificate configured in ADFS for Token-Decrypting and Token-Signing is the same as the one configured in OWA for encryption and signature. Also Ensure that the certificate being used for decryption in OWA is valid and trusted.

-  In ADFS, ensure that the relying party trust for OWA is correctly configured with the appropriate encryption and signing certificates.

-  Double-check the settings to confirm that the correct certificate is selected for decryption in the relying party trust configuration.

-  Validate the certificates being used by both ADFS and OWA to ensure they are not expired, revoked, or otherwise invalid.

-  Ensure that the certificate chain is complete and all intermediate certificates are properly installed 

-  Confirm that the thumbprint of the certificate configured in OWA matches the thumbprint of the certificate used by ADFS for token decryption.

-  Continue reviewing logs and error messages in both ADFS and OWA for any additional clues or errors that might help diagnose the issue further.

-  Enable verbose logging if necessary to capture more detailed information about the SAML requests and responses.
