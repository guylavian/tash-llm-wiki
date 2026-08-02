---
title: "Sharepoint ADFS with SSRS report"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/375191/sharepoint-adfs-with-ssrs-report
question_id: 375191
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "microsoft-security-security-active-directory-federation-services"]
---
# Sharepoint ADFS with SSRS report

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/375191/sharepoint-adfs-with-ssrs-report (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have :

1) A Sharepoint 2013 server running on Windows Server 2012 R2 Standard. SSRS reporting 12 (12.0.5000.0) is installed here in Native mode. Currently the SSRS report uses http, if that makes any difference.

2) An ADFS server running Windows Server 2019 Standard. Not sure how to check the ADFS version.

I can reach Sharepoint via ADFS authentication. Currently SSRS reporting is only reachable from within the SP/SSRS server itself. I want it reachable from Sharepoint with ADFS. Is it possible to have SSRS in Native mode or must it be in Integrated mode? How do i get user to be able to authenticate to SSRS?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-29*

Hello @Frank LOH   ,    

According to my understanding of your question, you want to use ADFS in Windows Server 2019 Standard to access SSRS(SQL Server Reporting Service) in Windows Server 2012 R2 Standard.    

Based on my research, due to version reasons, this is impossible to achieve.    

SSRS reporting 12 (12.0.5000.0): The SQL Server 2014 SP2 Reporting Services    

    

The following SQL server versions are supported with AD FS in Windows Server 2012 R2:    

-  SQL Server 2008 / R2    

-  SQL Server 2012    

-  SQL Server 2014    

However, in Windows Server 2019, your need Microsoft SQL Server 2019 Reporting Services(15.0.1102.896).    

Thanks,    

Echo Du    

=============================    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
