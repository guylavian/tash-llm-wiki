---
title: "Exchange 2019 coexistence with Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1611492/exchange-2019-coexistence-with-exchange-2016
question_id: 1611492
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 coexistence with Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1611492/exchange-2019-coexistence-with-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an Exchange Environment with 2 X Exchange 2016 servers and 1 X Exchange 2019. EX2016 is running on Server 2016 and EX2019 on server 2019.  One issue we are experiencing is when Outlook clients connect via the EX2019 server and their mailbox resides on the EX2019 server, the mailbox opens fine.  If they are then opening shared mailboxes or mailboxes with delegated access which reside on either of the Exchange 2016 servers, they are not able to view the mailboxes.  The Outlook connection status just shows as 'Connecting' and an 'Error' status under Authn.

If they connect via either of the Exchange 2016 servers, all works completely fine!

As testing on this, I am simply connecting from a remote PC running Outlook 365 and changing the NAT rule to point to either the EX2019 server (which doesn't work) or the EX2016 server (which does work).

As far as I can see all settings on virtual DIRs are identical.

ExcludeExplicitO365Endpoint added to reg  

Has anyone experienced this issue or got any suggestions, please?

Thank you in advance.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-03-18*

Morning Jayce,  unfortunately this doesn't appears to be a Cypher issue.  I currently have a support request open with Microsoft who haven't been able to resolve the issue so far.  I will provide a further update once Microsoft has found the cause, so that this can be shared with the community.

Kind regards - Paul

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-08*

Thanks Andy.  I will go through your article to check the points mentioned.  We will be moving the customer to EXO later this year, with a Hybrid setup with the EX2019 server remaining on premise.  I will provide you with a further update once I have gone through the article provided.  

Thank you again for your kind assistance.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-08*

Could be a TLS issue. Ensure they are set to TLS 1.2

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-tls-configuration?view=exchserver-2019

Any reason you are not running all 2019?
