---
title: "Server 2019 DC - Kerberos RC4 Authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/317491/server-2019-dc-kerberos-rc4-authentication
question_id: 317491
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Server 2019 DC - Kerberos RC4 Authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/317491/server-2019-dc-kerberos-rc4-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have recently updated our DCs from Windows Server 2016 to Windows Server 2019 and all our legacy systems (Windows XP + Windows 2000) are no longer able to login and retrieve group policies. It's been suggested in quite a few forums, in particular https://social.technet.microsoft.com/Forums/ie/en-US/7420a288-7111-458a-bf32-efad80d5e5e5/server-2019-dc-kerberos-rc4-authentication?forum=ws2019 that the issue is due to Windows Server 2019 lacking RC4 support for Kerberos authentication. It hasn't been listed on any official documentation that WS 2019 doesn't support it, yet I've tried all the methods outlined in the forum I linked above but to no avail.   

Any assistance would be greatly appreciated.  

(And yes I know RC4 is more insecure and that we should upgrade our legacy systems, this is in the pipeline but we need a solution in the mean time)

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-17*

Hi,    

You can check if there are any policies defined for the Supported Kerberos Encryption Types.    

If not policies defined , you can check the attribute for the DC If the RC4 is supported:    

    

More details for your reference:    

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/decrypting-the-selection-of-supported-kerberos-encryption-types/ba-p/1628797    

Since there is no longer support for the Windows XP + Windows 2000 ,there also is no patching or testing for XP scenarios.    

More unexpected incompatibilities may occur .    

It is suggested to upgrade the old clients.     

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-16*

Not sure what is meant. Windows XP is officially no longer supported. The only solution is to keep the older domain controllers until you can upgrade the desktops.    

https://learn.microsoft.com/en-us/lifecycle/products/windows-xp    

--please don't forget to Accept as answer if the reply is helpful--
