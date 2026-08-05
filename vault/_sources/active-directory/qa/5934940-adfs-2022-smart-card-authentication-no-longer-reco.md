---
title: "ADFS 2022 Smart Card Authentication No Longer Recognized as MFA After Upgrade from Windows Server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5934940/adfs-2022-smart-card-authentication-no-longer-reco
question_id: 5934940
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS 2022 Smart Card Authentication No Longer Recognized as MFA After Upgrade from Windows Server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5934940/adfs-2022-smart-card-authentication-no-longer-reco (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are currently investigating a behavioral difference between AD FS on Windows Server 2016 and on Windows Server 2022 regarding smart card/certificate-based authentication.

In our Windows Server 2016 AD FS environment, all relying parties (RPs) authenticate successfully using a smart card and the authentication is treated as a multi-factor authentication (MFA) event. Users are able to sign in using only their smart card (certificate + PIN) without being prompted for any additional authentication factor.

After migrating the AD FS servers to Windows Server 2022, the same smart cards, certificates, users, and relying party configurations continue to authenticate successfully. However, AD FS 2022 appears to treat the smart card as only a single authentication factor.

The observed behavior is:

-  If a user signs in using a smart card, authentication succeeds, but AD FS prompts for an additional MFA factor (OTP or SMS).

-  If a user signs in using username/password as the primary factor, the smart card can be used as the secondary factor.

-  In other words, AD FS 2022 recognizes the smart card as either a primary or secondary authentication method, but does not appear to consider it a complete MFA method as AD FS 2016 did.

Given that:

-  The same smart cards and certificates are used in both environments.

-  Certificate mapping and user identification are successful.

-  Authentication itself succeeds.

-  The only difference is the Windows Server / AD FS version.

What changes in AD FS 2022 could cause certificate-based (smart card) authentication to no longer be treated as a completed MFA event, and what is the recommended approach to restore the AD FS 2016 behavior where smart card authentication satisfies MFA requirements on its own?

## Answers

_No answers on this thread._
