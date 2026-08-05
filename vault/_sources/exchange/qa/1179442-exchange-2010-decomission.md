---
title: "Exchange 2010 decomission"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179442/exchange-2010-decomission
question_id: 1179442
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2010 decomission

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179442/exchange-2010-decomission (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to decom an old Exchange 2010 server. We still require AD sync so I plan to deactivate rather than uninstall it to retain the AD email attributes.

I am planning to install the Exchange admin tools from the Exchange 2019 iso on anoher member server. My question is, can I do this ahead of time without causing any issues?. There are still a few remaining local mailboxes and DL's that I can't migrate easily.  Also, do the Exchange tools require a reboot (2012R2)

Also, if anyone has any clear steps on what needs to be done in this scenario to remove the Exchnage 2010, that would be appreciated, I'm not completely certain what needs to be done to remove the hybrid config. There's many articles about this but the info isn't always consistent.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-13*

Hi @Bob Pants  ,

As far as I know, it is not feasible for Exchange 2010 and 2019 deployments to coexist.. Therefore, for your current situation, we recommend that you upgrade to Exchange 2016 Hybrid before upgrading to Exchange 2019.

Hybrid deployment prerequisites | Microsoft Learn

Here are some general steps for a hybrid upgrade that we hope will help you improve your upgrade process：

-  Add and Install Exchange 2016 in your environment.

-  Export the hybriddomain.com certificate from Exchange 2010 and binding to Exchange 2016 IIS with SMTP services.

-  Update the ExchangeVirtualDirectory URLs and points to Exchange 2016. If you use the same FQDN as the old one, you don't need to update the DNS records otherwise you need to update your DNS.

-  Migrate mailboxes in Exchange 2010 to Exchange 2016

-  Remove the old Exchange 2010.

-  Re-run HCW with Exchange 2016 and make sure the mail flow in Microsoft 365 and Exchange 2016 working fine.

-  (Optional) add Exchange 2019 into your environment, and then deploy Exchange2019-based Hybrid then.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-10*

Hello Bob.

I'm assuming you know about exchange administration, so let's go. a small checklist.

-  check if all mailflow are poiting to Exchange online

-  Ensure all mailboxes are moved to cloud including the arbitration mailboxes 

-  delete conectors.

-  Remove all database (do u have DAG? if yes, remove COPY before and after DAG)

-  turn off the exchange server for a few days.

-  after that, unistall.

Microsoft have a document about that.

https://techcommunity.microsoft.com/t5/exchange-team-blog/best-practices-when-decommissioning-exchange-2010/ba-p/1247559

or in this another document>

https://community.spiceworks.com/how_to/168367-how-and-when-to-decommission-on-premises-exchange-server-in-a-hybrid-deployment

I hope this help you.

good luck

Regards
