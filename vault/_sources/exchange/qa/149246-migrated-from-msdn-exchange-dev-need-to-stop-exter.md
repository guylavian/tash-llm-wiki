---
title: "[Migrated from MSDN Exchange Dev]Need to stop external OWA on exchange 2016 on premises environment."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/149246/migrated-from-msdn-exchange-dev-need-to-stop-exter
question_id: 149246
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Need to stop external OWA on exchange 2016 on premises environment.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/149246/migrated-from-msdn-exchange-dev-need-to-stop-exter (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear's,

We have exchange 2016 on Premises with 4 hosts with all the services on each server.

Internally, OWA and outlook can be operational. But from External network we need to stop publishing OWA.

Currently on external; OWA and autodiscover is published with port 443 and 80

Source link: https://social.msdn.microsoft.com/Forums/office/en-US/b14fe8bb-656e-468e-9346-881a7a13d548/need-to-stop-external-owa-on-exchange-2016-on-premises-environment?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-03*

Here are some ways that could block OWA access from external of your organization:    

-  Create rule on your firewall to block the OWA access.    

-  Installing Web-IP-Security to do limitation on OWA(Only allow access from specific IP address segment):    

     

-  Install Exchange 2019 and use the new function of Exchange 2019: Client Access Rules in Exchange 2019    

You can choose one of them to use in your organization.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
