---
title: "Exchange 2019 coxisting with 2013 Topology question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1033344/exchange-2019-coxisting-with-2013-topology-questio
question_id: 1033344
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 coxisting with 2013 Topology question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1033344/exchange-2019-coxisting-with-2013-topology-questio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I deployed 4 new Exchange 2019 servers along with my Exchange 2013 servers, wanting to move to Exchange 2019    

the Microsoft.Exchange.Directory.TopologyService.exe is only picking up the old 4 Exchange 2013 servers after I have installed the new 2019 Exchange servers,    

to my understanding it should show 8 servers in the Topology event 2080 being detected or would it only show the 4 new Exchange 2019 servers afterward or is there something i am missing?

## Answer (community) — community member

*upvotes: 1 · updated: 2022-10-04*

Hi @IT Guy      

Thanks for sharing more information about this question here! Yes, Event 2080 does not apply to Exchange 2019.     

And Exchange 2013 is one of the supported coexistence scenarios for Exchange 2019, so don't worry about your deployment.    

    

Since our forum has the policy that The question author cannot accept their own answer. They can only accept answers by others, and according to the scenario introduced here: Answering your own questions on Microsoft Q&A, you could "Accept Answer" for any helpful reply to close this thread, and your action would be helpful to other users who encounter the same issue and read this thread. Thanks for your understanding!    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-03*

this might just be my old mindset of working on previous Exchange years ago,    

but i see the Event 2080 does not apply to 2019    

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/msexchangedsaccess-event-id-2080    

Applies to: Exchange Server 2016, Exchange Server 2013, Exchange Server 2010
