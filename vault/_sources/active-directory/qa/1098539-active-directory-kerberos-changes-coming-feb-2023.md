---
title: "Active Directory Kerberos Changes (coming Feb 2023) and appropriate patches"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1098539/active-directory-kerberos-changes-coming-feb-2023
question_id: 1098539
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory Kerberos Changes (coming Feb 2023) and appropriate patches

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1098539/active-directory-kerberos-changes-coming-feb-2023 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'm requesting some guidance / clarification on documents that initiated back in Nov 2021 & May 2022 regarding the Kerberos Distribution Center (KDC) and how it will be servicing a certificate-based authentication request with strong bindings only. After may 2023, clients will no longer be able to authenticate with a "weak" certificate mapping. I'm late to the game on this one and most of the patches mentioned will not install on my Server 2019 Test DC's or the CA. I get a dialog that this patch is not applicable to my computer. I believe I understand now using the catalog that only the latest update will install. The problem is when I install the latest relevant patch, I don't get the behavior described in the docs(such as the registry keys for StrongCertificateBindingEnforcement on domain controllers ).     

Here are the articles I'm attempting to follow:    

https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16#bkmk_kdcregkey    

https://support.microsoft.com/en-gb/topic/kb5008380-authentication-updates-cve-2021-42287-9dafac11-e0d0-4cb8-959a-143bd0201041    

https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-kerberos-auth-issues-in-emergency-updates/    

The final article seems to suggest that patch KB5021655 should resolve all of the issues that were laid out in the previous year (for Server 2019). It also seems when Using the Microsoft Update Catalog that this patch supersedes most of the earlier patches.    

My concerns are that I never did see the Registry Key on the domain controllers for  StrongCertificateBindingEnforcement so I can't verify if I'm progressing correctly. I saw some of the event activity very briefly (maybe because I installed the latest patch too soon) I would also like to know if this applies to Device Certificates since we don't use User Certs.    

Any guidance here is appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-14*

Well,    

The bottom line appears to be that you can not install previous patches if you already have a superseding patch installed, so It seems to do no good to back trace steps.  According to this unofficial post:    

https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-kerberos-auth-issues-in-emergency-updates/    

kb5021655 is supposed to fix everything, and the advise is to undue any workaround previously implemented. I think for the time being, I'm going to assume that installing this patch on Server2019 DC's takes care of all issues.    

Thanks for your responses.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-22*

Something here could help.    

https://www.cisa.gov/guidance-applying-june-microsoft-patch    

 --please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
