---
title: "Exchange Hybrid free / busy not working after changing certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1296869/exchange-hybrid-free-busy-not-working-after-changi
question_id: 1296869
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-exchange-other-l1"]
---
# Exchange Hybrid free / busy not working after changing certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1296869/exchange-hybrid-free-busy-not-working-after-changi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,

I hope someone can help me with this one, because I have tried everything.

We have two Exchange Servers 2016 in DAG and a full Hybrid Setup for a while now.  

Last week we switched out the main frontend certificate (not the Exchange Server auth certificate!) and since then the hybrid free/busy calendar access stopped working in both directions.  

The users are getting a warning when opening the other calendar, that it couldn't be updated.  

The remote connectivity analyzer is giving me the following error:  

`The mail recipient is not found in Active Directory., inner exception: Microsoft.Exchange.InfoWorker.Common.Availability.InvalidOrganizationRelationshipForRequestDispatcherException: The organization relationship O365 to On-premises - <...> can't be used. Please confirm that the organization relationship is configured correctly. . Name of the server where exception originated: BE0P281MB0196. LID: 52108`

I already tried the following things:

-  reran Exchange hcw multiple times. It completes successfully, but says it can't setup OAUTH

-  checked OAUTH Setup. Successfully ran test-oauthconnectivity in both directions

-  compared the organizationrelationship with other working setups

-  checked if any certificates expired

-  checked every article I found regarding hybrid free busy errors

I am not sure, whether the certificate is actually the reason, or just bad timing. Maybe somebody has an idea for me.

Thank you,  

Patrick

Update: The on premise User can see the Online Calendar after enabling the IntraOrganizationConnector on the on permise Server. Apparently the hcw turns it off, because of the OAUTH Error.

Sadly, doing the same in Exchange Online didn't do anything. This was also disabled.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-02*

solved. Activating the IntraOrganizationConnector in EXO seems to be the fix.
