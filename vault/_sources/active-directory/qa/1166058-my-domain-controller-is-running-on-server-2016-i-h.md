---
title: "My Domain controller is running on Server 2016. I have a new machine in my network which is running on Serer 2019. Can I add Server 2019 machine to the existing DC which is running on Server 2016?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166058/my-domain-controller-is-running-on-server-2016-i-h
question_id: 1166058
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# My Domain controller is running on Server 2016. I have a new machine in my network which is running on Serer 2019. Can I add Server 2019 machine to the existing DC which is running on Server 2016?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166058/my-domain-controller-is-running-on-server-2016-i-h (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My Domain controller is running on Server 2016. I have a new machine in my network which is running on Serer 2019. Can I add Server 2019 machine to the existing DC which is running on Server 2016?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-02*

Hello @Prasanth Gunnam,

Thank you for posting in our Q&A forum.  

Based on the description, whether you can add a Windows 2019 server to the existing DC which is running on Server 2016? Or whether you can add a Windows 2019 Domain Controller to the existing DC which is running on Server 2016?   

If you mean it is a Windows 2019 server, of course, you can, because:  

Functional levels determine the available Active Directory Domain Services (AD DS) domain or forest capabilities. They also determine which Windows Server operating systems you can run on domain controllers in the domain or forest. However, functional levels do not affect which operating systems you can run on workstations and member servers that are joined to the domain or forest.  

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels  

If you mean it is a Windows 2019 Domain Controller, I hope the answers provided by the two persons above are helpful.   

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou

===============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-02-01*

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-01*

Hi @Prasanth Gunnam  

yes you can add a additional domain controller windows 2019 in a existing domain with domain controller under windows 2016

take note ,to promote the first domain controller on windows 2019, the domain and forest function level must be windows 2008r2 or higher and the replication system for sysvol folder is DFSR.

Please don’t forget to mark helpful answer as accepted
