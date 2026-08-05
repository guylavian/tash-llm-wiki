---
title: "Cutover migration from Exchange 2010 to 365 with different domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/282976/cutover-migration-from-exchange-2010-to-365-with-d
question_id: 282976
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Cutover migration from Exchange 2010 to 365 with different domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/282976/cutover-migration-from-exchange-2010-to-365-with-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. Is it possible to do a cutover migration from Exchange 2010 to 365 when the 365 have a different domain? Or do Exchange domain and 365 domain have to be the same? When I am trying to migrate and choose data from Exchange I got this message: Looks like you have not run the Office 365 Hybrid Configuration Wizard yet. Requirements: -running a Windows operating system -connected and joined to the same domain as the On-Premises Exchange Server Does that mean that I need to do the migration from a pc joined to the same domain as the Exchange? So I have two problems here: 1) Cannot do this from anywhere - have to do it onsite with domain joined pc 2) Cannot migrate from oldcompany.com to newcompany.com Comments?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-23*

Hi  

-  The company is splitting up into two domains. Only a part of the users in Exchange will move to 365 at this point with a new domain "newcompany.com" The "oldcompany.com" domain name will still be active in Exchange for a while longer so I cannot use that domain in 365 at the moment. 365 is prepared with "newcompany.com", users and licenses.

2) When I try to set up Migration Endpoint in 365 and choose Exchange as source I got this error:  

Looks like you have not run the Office 365 Hybrid Configuration Wizard yet.

This application will configure your Tenant and Exchange environments so you can start moving your mailboxes to Exchange Online. Learn More.

Requirements:  

-running a Windows operating system  

-connected and joined to the same domain as the On-Premises Exchange Server

3) I did number 2) with 365 wizard but when I changed to Exchange Online admin, the wizard was different and I got further but stopped on wizard not finding/connection to exchange 2010 the right way.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-23*

Hi @Tommy Forsman   ,  

In order to better solve this issue, I want to confirm with you the following points:  

1.What your means that Exchange 2010 and Office 365 have different domain names? Do you mean the domain used after the migration and the Exchange 2010 domain?  

When you migration the mailboxes from Exchange 2010 to Exchange online, you need to verify your on-premises Exchange domain in Microsoft 365 admin center. If you want to using other domain, you could add the domain to Microsoft 365 and change the default domain after completing the migration. Then you could change the primary email address. But please note that reasonably change your DNS records.  

For more information : Domains FAQ and Add a domain to Microsoft 365.

2.Did you create the migration endpoints in Exchange online to ensure that connect Microsoft 365 or office 365 to your email system? What do you need to do in the domain-added PC?  

Based on my knowledge, you need to create migration endpoints and create the cutover migration batch in EAC in Exchange online. And please make sure that you select the “Cutover migration” migration type.  

Here is an official article introducing the detailed steps of cutover migration, you can refer to: Migrate email using the Exchange cutover method

In addition, please shared the complete error information with us, pay attention to covering your personal information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
