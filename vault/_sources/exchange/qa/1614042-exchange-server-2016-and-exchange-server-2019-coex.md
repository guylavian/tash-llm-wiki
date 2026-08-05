---
title: "Exchange server 2016 and Exchange server 2019 coexistence"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1614042/exchange-server-2016-and-exchange-server-2019-coex
question_id: 1614042
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange server 2016 and Exchange server 2019 coexistence

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1614042/exchange-server-2016-and-exchange-server-2019-coex (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We have 4 exchange server 2016 and client connection for https/smtp relay happens via Load balancer. (for ex. connection to 'owa.abc.com'/'autodiscover.abc.com'/'smtp.abc.com' goes to VIP used for exchange 2016 servers)  

We have installed 4 exchange servers 2019 (no change with namespace, same URL and certificate is used), we plan to test client connectivity and SMTP relay function.  

Our plan is to create new VIP with exchange 2019 as backend servers on LB.  

Then test by updating local host file where outlook/owa/smtp server name (owa.abc.com/autodiscover.abc.com) points to new VIP.

Once all tests are successful, update DNS record for 'owa.abc.com'/'autodiscover.abc.com/smtp.abc.com' to point new VIP used for exchange 2019 servers.

Questions -  

-Is it proffered way (creating new VIP and server pools) or should we add Exchange 2019 servers to existing server pool along with 2016 servers? This way DNS change is not needed. (If yes, then what are the ways to do all test prior to adding exchange 2019 to existing pool?)

-How to make test for ActiveSync, is there any tool ? (not possible on mobile device to point server connection to private VIP)

Thank you for any feedback/help.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-03-11*

I would add the new 2019 servers to the existing pool and not create a new VIP. Use the same cert names and and add the same cert to the new 2019 servers, they can all seamlessly share the same pool:

https://learn.microsoft.com/en-us/exchange/architecture/client-access/load-balancing?view=exchserver-2019

to test for activeSync, you could add one 2019 server to the existing pool and then off-hours, disable all the 2016 servers in that pool. Then test using the 2019 server which is the only active server in the pool.
