---
title: "Error Encountered When Configuring ADFS for SAML Authentication (ServiceDesk Plus Cloud)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5855044/error-encountered-when-configuring-adfs-for-saml-a
question_id: 5855044
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Error Encountered When Configuring ADFS for SAML Authentication (ServiceDesk Plus Cloud)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5855044/error-encountered-when-configuring-adfs-for-saml-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I’m currently implementing a proof of concept (POC) for a client using ManageEngine ServiceDesk Plus (Cloud edition) and I’m seeking guidance on an issue I’m encountering while configuring SAML authentication.

As part of the setup, I’m following ManageEngine’s official documentation (SAML Authentication) for configuring SAML using an on-premises Identity Provider. Per the guide, I installed and configured Active Directory Federation Services (ADFS) on the client’s network. However, during the Federation Service configuration, after entering all the required details in the configuration wizard, the process fails with an error (see attached screenshot).

To rule out documentation issues, I contacted the ManageEngine support team, who confirmed that the steps in their guide are current and working. They recommended that I raise this issue here for assistance with the ADFS configuration error.

Has anyone encountered a similar issue when configuring ADFS for SAML with a third-party SaaS application? Any guidance on troubleshooting this error or common misconfigurations to check would be greatly appreciated.

Thank you in advance for your assistance.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-04-08*

Because the exact ADFS configuration error text isn’t provided, only general ADFS–SAML troubleshooting steps that apply to third‑party SaaS integrations can be given.

When configuring ADFS as an IdP for a SAML application such as ServiceDesk Plus Cloud, the most common causes of failures during sign‑in or token issuance are:

-  Federation realm / IssuerURI mismatch

-  If the third‑party IdP or SP returns or expects the wrong Issuer URI, Microsoft Entra ID or the application can show errors like “The requested federation realm object '<Object ID>' does not exist.”

-  For SAML, the Issuer in the SAML response must match what the relying party (or Microsoft Entra ID, if involved) is configured to expect.

-  Resolution path:

-  Verify the IssuerURI configured in ADFS for the relying party trust matches exactly what the SaaS app expects.

-  If the SaaS app is acting as IdP in any flow, contact its support to correct the IssuerURI it returns in the SAML response.

-  Unsupported or incorrect authentication method (AuthnContext / WAUTH)

-  If the request enforces a specific authentication method that ADFS does not support or is misconfigured, ADFS can fail before authentication completes, sometimes with an “Unknown Auth method” or similar error.

-  For WS‑Federation, the enforced method is passed via the `wauth` query string.

-  For SAML 2.0, it is passed via `saml:AuthnContext` / `saml:AuthnContextClassRef`.

-  ADFS supports specific URIs only, for example:

-  `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport`

-  `urn:oasis:names:tc:SAML:2.0:ac:classes:Password`

-  `urn:oasis:names:tc:SAML:2.0:ac:classes:TLSClient`

-  `urn:oasis:names:tc:SAML:2.0:ac:classes:X509`

-  `urn:federation:authentication:windows`

-  `urn:oasis:names:tc:SAML:2.0:ac:classes:Kerberos`

-  Troubleshooting steps:

-  Capture the SAML/WS‑Fed request from the SaaS app to ADFS (for example with Fiddler as described in the ADFS troubleshooting article) and inspect:

-  For WS‑Fed: the `wauth` parameter.

-  For SAML: the `<saml:AuthnContextClassRef>` value.

-  Confirm that the value is one of the supported URIs listed above.

-  On ADFS:

-  For AD FS 2.0, check `/adfs/ls/web.config` under `<localAuthenticationTypes>` to ensure the corresponding authentication type is configured (Forms, Integrated, TlsClient, Basic).

-  For AD FS 2012 R2 and later, review Authentication Policies in the ADFS Management console to ensure the required primary authentication methods are enabled (for intranet/extranet as appropriate).

-  If the SaaS app sends an unsupported AuthnContext, adjust its configuration to use a supported one (for example `PasswordProtectedTransport`).

-  Claims and token issuance issues

-  After ADFS issues a token, if the relying party (ServiceDesk Plus Cloud) or Microsoft Entra ID rejects it, the problem is often with claims or certificates.

-  Common issues:

-  Required claims (such as NameID, email, or ImmutableID equivalents) are missing or mapped incorrectly.

-  Token‑signing certificate mismatch between ADFS and the relying party configuration.

-  Troubleshooting steps:

-  Enable ADFS auditing and review the Security log to confirm whether a token is issued or denied and which claims are present.

-  Use Fiddler to locate the SAML token issued by ADFS and decode it (FromDeflatedSAML for SAML 2.0) to inspect the claims.

-  Compare the claims in the token with what the SaaS application expects (for example, which attribute is used as NameID / user identifier).

-  Verify that the token‑signing certificate configured in the SaaS app matches the current ADFS token‑signing certificate.

-  General ADFS–Azure/Microsoft Entra federation checks (if Entra ID is in the flow)

-  If the sign‑in flow involves Microsoft Entra ID (for example, ServiceDesk Plus uses Entra as SP and ADFS as IdP), also verify:

-  The Microsoft Entra tenant is enabled for federation.

-  The custom domain is verified and configured for federation.

-  DNS for ADFS/WAP endpoints is resolvable externally.

-  If Microsoft Entra ID reports errors after ADFS issues a token, check:

-  That UPN / IDPEmail and ImmutableID / NAMEID claims from ADFS match the user attributes in Entra ID.

-  Practical step‑by‑step troubleshooting for this scenario

-  Reproduce the error and capture the traffic with Fiddler.

-  Identify whether the failure occurs:

-  Before ADFS sign‑in page (likely DNS/federation/redirect issue), or

-  After credentials are entered (likely AuthnContext, claims, or certificate issue).

-  If the error appears immediately after redirect from the SaaS app to ADFS:

-  Inspect the request for `wauth` or `AuthnContextClassRef` and validate against the supported URIs.

-  If the error appears after ADFS attempts to issue a token:

-  Enable ADFS auditing and check Security logs for token issuance/denial events and claim details.

-  Decode the SAML token and verify claims and IssuerURI.

-  Cross‑check the relying party trust configuration in ADFS:

-  Identifier(s) / realm match the SaaS app configuration.

-  Endpoints (SAML Assertion Consumer Service URL) are correct.

-  Token‑signing certificate exported to the SaaS app is current.

If the exact error message from the ADFS configuration wizard or from the browser sign‑in flow is captured, it can be mapped directly to one of the above areas (realm/IssuerURI, AuthnContext, claims, or certificates) using the same troubleshooting workflow.

References:

-  Authentication fails with an error stating "The requested federation realm object '< Object ID >' does not exist"

-  Troubleshoot AD FS issues in Microsoft Entra ID and Office 365

-  AD FS troubleshooting: Microsoft Entra ID

-  ADFS 2.0 error: Access is denied

-  Troubleshoot SSO issues with Active Directory Federation Services (AD FS)

-  "The request sent by client is not signed" error AADSTS76021 in SAML authentication
