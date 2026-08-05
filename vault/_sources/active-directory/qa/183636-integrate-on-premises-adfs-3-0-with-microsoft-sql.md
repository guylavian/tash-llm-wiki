---
title: "Integrate On-Premises ADFS 3.0 with Microsoft SQL Server 2017 Reporting Services"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/183636/integrate-on-premises-adfs-3-0-with-microsoft-sql
question_id: 183636
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "sql-server-reporting-services"]
answer_author_roles: ["Q&A User"]
---
# Integrate On-Premises ADFS 3.0 with Microsoft SQL Server 2017 Reporting Services

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/183636/integrate-on-premises-adfs-3-0-with-microsoft-sql (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have setup a SQL Server 2017 and SSRS 2017 on my on premise server.  I am able to login via windows authentication and create SSRS 2017 reports.  

I am trying to provide SSRS 2017 reporting services capabilities to my customer.  I am only allowed to use ADFS 3.0 (Windows 2016) authentication.  

Are there any referenced resources that provide detailed steps on how to get this done?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-03*

Hi @kescott  ,    

Below links are both centered around using OAuth in mobile apps, but it should give you pointers on how to configure SSRS to use ADFS for authenticating users.    

https://learn.microsoft.com/en-us/power-bi/consumer/mobile/mobile-oauth-ssrs#active-directory-federation-services-adfs-configuration    

https://learn.microsoft.com/en-us/archive/blogs/sqlrsteamblog/leveraging-web-application-proxy-in-windows-server-2016-to-provide-secure-access-to-your-sql-server-reporting-services-environment    

Some other related articles for your reference:    

https://social.msdn.microsoft.com/Forums/sqlserver/en-US/36d6d0de-0576-4242-97a8-44820af5c043/adfs-20-and-ssrs?forum=sqlreportingservices    

Regards，    

Zoe    

If the answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.    

Hot issues October
