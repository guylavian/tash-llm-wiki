---
title: "OWA - ADFS - ID4175 IssuerNameRegistry"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1685025/owa-adfs-id4175-issuernameregistry
question_id: 1685025
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
---
# OWA - ADFS - ID4175 IssuerNameRegistry

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1685025/owa-adfs-id4175-issuernameregistry (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have encountered a problem with an ADFS in Exchange Server 2019. x-adfserror: ID4175: The issuer of the security token was not recognized by the IssuerNameRegistry. To accept security tokens from this issuer, configure the IssuerNameRegistry to return a valid name for this issuer.

Im using keycloak as IDP to login to OWA. The connection between is setup like this OWA - ADFS - KEYCLOAK(our mfa handling) - ADFS - OWA.

In relying party trust in ADFS for OWA i have put identifier: https://link/owa/. Should it be https://link/adfs/services/trust/? Tried but im getting 503 error while accessing this link.

I saw that there is a STS configuration, but cannot find what exacly it is doing for ADFS.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-22*

The error message "ID4175: The issuer of the security token was not recognized by the IssuerNameRegistry" indicates that the ADFS is not recognizing the issuer of the security token. To resolve this issue, you need to configure the IssuerNameRegistry to return a valid name for this issuer.

In the relying party trust in ADFS for OWA, the identifier should be set to the URL of the OWA application, which in this case is "https://link/owa/". It should not be set to "https://link/adfs/services/trust/".

The STS (Security Token Service) is responsible for issuing and validating security tokens. It is used by ADFS to issue security tokens to clients that request them.

References:

-  Troubleshoot AD FS issues in Microsoft Entra ID and Office 365

-  ADFS SSL Certificate Trust
