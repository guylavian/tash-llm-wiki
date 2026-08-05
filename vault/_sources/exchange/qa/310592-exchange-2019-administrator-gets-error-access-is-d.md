---
title: "Exchange 2019 administrator gets error Access is denied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/310592/exchange-2019-administrator-gets-error-access-is-d
question_id: 310592
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 administrator gets error Access is denied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/310592/exchange-2019-administrator-gets-error-access-is-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am the Exchange organization administrator.  I installed a new Exchange 2019 CU8 server last night.  Everything works.  I can do everything as expected.  I can make a new mailbox database, change policies, migrate users, everything.... except check server certs.    

When I go to Servers, Certificates and select our old Exchange 2016, it works fine.  But pick our new Exchange 2019 (or another Exchange 2016 in the organization, I get    

error The Exchange certificate operation has failed with an exception on server Exch19.  The error message is Access is denied.

## Answer (community) — Microsoft Moderator

*upvotes: 5 · updated: 2021-03-12*

Hi, @Neal Blackie       

Please locate "Computer Management> Local Users and Groups>Groups>Administrators" on each of your Exchange servers.    

And make sure "Domain\Exchange Trusted Subsystem" is a member of this group.    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
