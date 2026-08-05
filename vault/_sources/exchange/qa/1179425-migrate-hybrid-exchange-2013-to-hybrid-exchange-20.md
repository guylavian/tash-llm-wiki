---
title: "Migrate Hybrid Exchange 2013 to Hybrid Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179425/migrate-hybrid-exchange-2013-to-hybrid-exchange-20
question_id: 1179425
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Migrate Hybrid Exchange 2013 to Hybrid Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179425/migrate-hybrid-exchange-2013-to-hybrid-exchange-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,

I have a Hybrid Exchange 2013 running in server 2012 r2 in my organisation and now planning to migrate to Hybrid Exchange 2019 on a server 2019 vm and completed the prerequists as mentioned in Microsoft portal.

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2019

Am working on this Exchange first time - if you could please provide me with a detailed step by step Instructions that will be much helpful.

## Answer (community) — Q&A User

*upvotes: 3 · updated: 2023-02-16*

You just need to create a new Exchange 2019 that coexists with Exchange 2013. Then configure external virtual directories for Exchange 2019 from the Exchange admin center:

Then enable MRSProxy for Exchange 2019:

`Get-WebServicesVirtualDirectory | Set-WebServicesVirtualDirectory -MRSProxyEnabled $true`

After that, you could rerun HCW to switch hybrid end point from Exchange 2013 to Exchange 2019.

Finally, you could change the public DNS record point to Exchange 2019 server if you want.

The Exchange Deployment Assistant could provide detailed steps for you to deploy Exchange 2019 coexists with Exchange 2013.

If you have migrated mailboxes and DNS records to Exchange 2019.

## Answer (community) — Microsoft Moderator

*upvotes: 2 · updated: 2023-02-13*

Hi @Gopal Shanmugam,

The general steps would be like:

-  install Exchange 2019 to co-exist with Exchange 2013

-  configure Exchange 2019 virtual directories, certificates, then migrate mailboxes (including arbitration mailboxes) from Exchange 2013 to 2019

-  run HCW (Hybrid Configuration wizard) and choose the new Exchange 2019 server as the endpoint

-  turn off Exchange 2013 to see if any problems will occur

-  decommission Exchange 2013 server

For Exchange 2019 installation and configuration, you can use the Exchange Deployment Assistant which would guide you step by step.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-16*

After step 3, if there are problem, what are the steps to rollback?
