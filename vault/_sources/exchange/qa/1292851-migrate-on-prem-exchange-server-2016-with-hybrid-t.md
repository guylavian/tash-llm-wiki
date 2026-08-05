---
title: "Migrate On-prem Exchange server 2016 with Hybrid to a new exchange 2019 forest --cross forest migration."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1292851/migrate-on-prem-exchange-server-2016-with-hybrid-t
question_id: 1292851
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migrate On-prem Exchange server 2016 with Hybrid to a new exchange 2019 forest --cross forest migration.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1292851/migrate-on-prem-exchange-server-2016-with-hybrid-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

As part of separation\AD consolidation our company decided to migrate the existing exchange 2016 environment to a new forest with exchange 2019 . 

Current\Source Exchange 2016 Environment as below.

Account forest 1- AccForestA.com

Account Forest 2 - AccForestB.com

Resource forest - ResForest.com  (Where exchange 2016 is installed)

Forest Trust- Two way trust between these forests

Hybrid - Current Exchange 2016 is in Hybrid setup -                TenantExch2016.onmicrosoft.com

Target Forest - Target.com

Exchange sever - Have one Exchange server 2019 installed. 

Trust -- Yet to create

Hybrid - Yet to create (with the existing Tenant)

Due to some application dependencies we need to keep some mailboxes in on-prem. We are looking for a high-level plan\approach to achieve following requirements .

-  How to setup Hybrid  from new Exchange 2019 to existing tenant

-  How to migrate the on-prem mailboxes to new 2019 forest

-  Decommission existing exchange 2016 environment. 

Any help is much appreciated !!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-08*

Any suggestions?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-01*

@Jarvis Sun-MSFT

Thanks for your input. But my scenario is different as it is a cross forest Migration-- Migrating mailboxes from one forest to an exchange server in another forest. Any help in this subject is highly appreciated .

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-31*

@Jarvis Sun-MSFT  

Thanks for your input. But my scenario is different as it is a cross forest Migration-- Migrating mailboxes from one forest to an exchange server in another forest. Any help in this subject is highly appreciated .

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-29*

Hi @Acloudguy  ,

 

The general steps on how to migrate from Hybrid Exchange 2016 to 2019 are as follows:

-  Update Exchange 2016 at least to CU 11 which supported coexist with Exchange 2019. Supported coexistence scenarios for Exchange 2019

-  Setup Service Connection Point (SCP)

-   Import SSL Certificate

-   Update Virtual Directories and OWA

-   Update DNS and Send Connectors

-   Move Mailboxes (If Required)

-  Decommission Exchange Server 2016

-  Run Hybrid Configuration Wizard (HCW) Hybrid Configuration wizard

More detailed steps you can refer to: How to Upgrade Exchange Hybrid Server 2016 to 2019?

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

Meanwhile here is a similar thread for your reference: Migrate Hybrid Exchange from 2016 to 2019 - Microsoft Q&A

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
