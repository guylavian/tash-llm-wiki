---
title: "Migrate Hybrid Exchange from 2016 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161549/migrate-hybrid-exchange-from-2016-to-2019
question_id: 1161549
fetched: 2026-07-25
answer_count: 14
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Migrate Hybrid Exchange from 2016 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161549/migrate-hybrid-exchange-from-2016-to-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am currently in the process of planning our Exchange migration from Exchange 2016 to Exchange 2019.

We use Exchange in a hybrid configuration.  I am seeing various conflicting options for the migration so I am looking for some advice, please.

We do not have any public folders.

We have a single on prem domain and forest.

All mailboxes are hosted in Exchange OnLine.

We have a single Exchange 2016 server.  We used to have two but one was decommissioned some time ago.

Any and all advice / replies will be greatly appreciated.  Thanks.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2023-01-25*

-  Yes, run through all the steps including PrepareAD. If this is a single domain forest, then running setup will do all that for you.

-  Yes you can however note that the when you bring up the 2019 server, you should apply the correct , trusted 3rd party cert to it.

-  To be supported you need to keep at least one Exchange Server for mgmt if you are using AADConnect to sync from on-prem to Azure.. However, once you upgrade to the 2019 plus the lastest CU and security updates, you can remove it and use powershell to manage:   [https://learn.microsoft.com/en-us/exchange/manage-hybrid-exchange-recipients-with-management-toolshttps://learn.microsoft.com/en-us/exchange/manage-hybrid-exchange-recipients-with-management-tools

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-01-18*

Hi @Michael Lawson  ,

The general steps on how to upgrade from Hybrid Exchange 2016 to 2019 are as follows:

1.      You need to create a new Exchange 2019 to coexist with Exchange 2016. Then configure the external virtual directories for Exchange 2019 from the Exchange admin center.

2.      Enable MRSProxy for Exchange 2019.

3.      You could rerun HCW to switch hybrid end point from Exchange 2016 to Exchange 2019.

4.      Then, you could change the public DNS record point to Exchange 2019 server.

5.      Finally, you could uninstall Exchange 2016 if you want.

I found a detailed hybrid upgrade guide for your reference:How to Upgrade Exchange Hybrid Server 2016 to 2019? (linkedin.com)

Hope it helps you!

 (Note:Microsoft provides third-party contact information to help you find additional information about this topic. This contact information may change without notice. Microsoft does not guarantee the accuracy of third-party contact information.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-25*

I've been reading the links, I have a few queries.

-  I know I need to extend the AD Schema, but do I also need prepare AD?  My thought process says no as we already have an Exchange server, but the guide isn't clear on this.

-  Can I install Exchange 2019 on a new server before I do the migration, without upsetting the current Exchange server?

-  As we use Hybrid Exchange, we do not have any Mailboxes or Public Folders on prem, does this make things easier?

Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-25*

Hi,

Thanks for your replies, I will give the links a good read!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-18*

Here are some other articles which will be helpful to you during updating:

-  Exchange Server supportability matrix

-  Exchange Deployment Assistant

-  Exchange 2016 to 2019 Migration 

Also check this thread for help - https://learn.microsoft.com/en-us/answers/questions/841892/migrate-from-exchnage-2016-to-2019-on-prime
