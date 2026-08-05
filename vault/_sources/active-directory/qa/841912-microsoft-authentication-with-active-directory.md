---
title: "Microsoft Authentication with Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/841912/microsoft-authentication-with-active-directory
question_id: 841912
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Microsoft Authentication with Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/841912/microsoft-authentication-with-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone. Please, i would love to know if it's possible to use Microsoft Authenticator with Active Directory on premise that is not Azure. I've been looking online to find the answer but all I'm seeing is azure. Is there an alternative way to use Microsoft Authenticator with Active Directory that's not Azure for maintain a company's users security as part of MFA.  

Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-09*

Hi @olumide lawal      

I'm not aware of a method to enable Azure MFA with on-premise Active Directory logon.  The closest you can get is use a smartcard or a FIDO2 device to provide second factor when used with RDP and NLA authentication, which will support smartcard access.    

Happy to be corrected.    

Gary.
