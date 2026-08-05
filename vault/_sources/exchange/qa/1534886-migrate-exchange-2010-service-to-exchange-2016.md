---
title: "Migrate Exchange 2010 service to Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1534886/migrate-exchange-2010-service-to-exchange-2016
question_id: 1534886
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migrate Exchange 2010 service to Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1534886/migrate-exchange-2010-service-to-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have 

-  1 Exchange 2010

-  SMTP Relay is on this server. Any Outgoing emails are going thought this server

-  POP3 is setup on this Server

-  IMAP4 is setup on this Server

-  Server has following roles - Mailbox, Client Access, Hub transport

-  Removed all mailbox/Public folders

-  2 Exchange 2016

-  Manage all mailbox

-  All external emails are delivery to these servers

-  Exchange online connect to these servers

Do I need to check anything else on Exchange 2010 to make sure it is migrate without any service being down.

I like to Migrate all services from Exchange 2010 to Exchange 2016 Servers.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-19*

Hello @lalajee  ,

As a supplement to Thameur-BOURBITA suggestion, you could also use Exchange deployment assistant to guide you to plan to plan migration. Consider all your failure domains, such as disk, network, entire node, virtualization loss, entire datacenter failure, etc. In addition, hopefully you could also find the links below helpful:Exchange 2010 to 2016 migration steps    Exchange On-Premises Best Practices for Migrations from 2010 to 2016

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-16*

Hi @lalajee  

It seems ok if all mailbox are moved  and all  connectors moved to Exchange 2016.
You should check also if there is any application still sending email through Exchange 2010 and migrate it to Exchange 2016.
Before uninstall Exchange 2010 , try to make a preventive shutdown on Exchange 2010 to check if there is any impact on production service and migrated users still able to sens and receive email without any issue.
If you don't have any issue during the preventive shutdown you can uninstall it.

Please don't forget to accept helpful answer
