---
title: "Windows Authentication Silent Login with ADFS on Edge Chromium / Chrome"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/92242/windows-authentication-silent-login-with-adfs-on-e
question_id: 92242
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Windows Authentication Silent Login with ADFS on Edge Chromium / Chrome

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/92242/windows-authentication-silent-login-with-adfs-on-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi     

I have read up on https://learn.microsoft.com/en-us/answers/questions/64583/how-to-bypass-sso-screen-when-using-saml-20-via-ad.html    

And have done all the changes needed, e.g    

-  Set-AdfsPRoperties to add "Mozilla/5.0" into WiaSupportedAgent    

-  Set Intranet Zone with added "https://adfs.exmple.com" into sites, and "enable logon using current username and password"    

-  Have also enable integerated windows authentication in "advanced" tab    

Please kindly refer to the comments here https://learn.microsoft.com/answers/comments/88886/view.html    

I will need help to achieve silent login for ADFS in our intranet.    

However we all the suggested modification, I can only achieve the following    

-  On every PC restart, I will be prompt at least once for user credential when doing /adfs/ls/wis?SAMLRequest=xxx    

-  After entering user credential successfully, I will not be prompted again until i restart my pc or i signout from ADFS.    

Is this expected behavior? or is it possible to achieve silent login?     

Thanks and Regards

## Answers

_No answers on this thread._
