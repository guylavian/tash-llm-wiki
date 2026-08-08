---
title: "Windows 2019 Domain Controller- SMBv1 disabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/68476/windows-2019-domain-controller-smbv1-disabled
question_id: 68476
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Windows 2019 Domain Controller- SMBv1 disabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/68476/windows-2019-domain-controller-smbv1-disabled (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

We are in process of upgrade of our Domain Controller from windows 2012 to windows 2019. And as far i know SMBv1 protocol will be disabled by default  

So by default winXP & win2003 will not able to join to Domain  

now can any one tell if the uses continue to use winxp or window 2003 member to login , files share etc?  

Regards  

Aamir Masthan

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-08-21*

Hi  

Keeping a windows 2003 and Windows XP in your environment and upgrade your domain controllers to Windows 2019 , it's not a good idea. Because Windows XP and Windows 2003 are not supported to communicate with a domain controller on Windows 2019.   

It's time to think to upgrade all unsupported operating system as Windows 2003 and WIndows XP to supported version.  

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-17*

Hi Again  

According to this article, XP will not work on server 2019. You can try a lower functionality level but you are likely on your own as far as testing and figuring it out, since XP is long out of support.  

https://social.microsoft.com/Forums/Azure/en-US/05b74c9c-7a80-4a03-8136-455cba9f95cc/windows-xp-and-active-directory-2019?forum=ws2019

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-17*

Hello Aamir,    

SMB is a protocol for allowing file shares/transfers in a Windows environment (shared files & folders) it has nothing to do with joining a domain.    

Your domain functional level will need to be raised to server 2008R2 - 2012R2, in order to get 2003 and 2019 DC's working together. This may work, but will be unsupported due to 2003 being out of support.    

With that said, Windows XP is also out of support. You might be able to get it to join by using a lower domain functionality level, but that does not change the fact that it is still unsupported, and will present a broad range of problems, including security issues.    

Regards,    

Miguel Fra    

www.falconitservices.com

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-08-17*

Hi Aaamir,    

can you please be more specific with the question "now can any one tell if the uses continue to use winxp or window 2003 member to login , files share etc?" I think I am missing something here.    

In General you can enable SMBv1 (although not recommended) and ensure the backwards compatibility, but you need to consider one more thing - enabling the support for older encryption algorithms like RC4. You can refer to the following MS Docs article for more detail on the Kerberos encryption protocol compatibility:    

network-security-configure-encryption-types-allowed-for-kerberos     

Regards    

=========================================================    

Please don't forget to "Accept Answer" and upvote if the response helped you.    

Stoyan
