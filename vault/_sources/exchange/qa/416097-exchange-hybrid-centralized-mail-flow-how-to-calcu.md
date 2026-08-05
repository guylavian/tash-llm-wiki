---
title: "Exchange Hybrid centralized mail flow how to calculate number of hybrid server required"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/416097/exchange-hybrid-centralized-mail-flow-how-to-calcu
question_id: 416097
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Hybrid centralized mail flow how to calculate number of hybrid server required

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/416097/exchange-hybrid-centralized-mail-flow-how-to-calcu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would Like to setup Exchange 2019 Hybrid for 100000 users already in office 365 and around 5000 users in on-premises . with   

Exchange Hybrid centralized mail flow .How we calculate the number of hybrid exchange server.  

in our case we need to separate the mailbox/cas server and hybrid server.  

Do we have any formula to calculate the number of hybrid servers.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-01*

@Kutta 2019       

For Exchange 2019, there only exist Mailbox server(Contains CAS service) and Edge server.    

You can only choose one Exchange server as hybrid server:    

    

If you want to guarantee the performance of the Exchange on-premises, you could use this tool to calculate how many Exchange server you need to install.    

You don't need to calculate the server for centralized mail flow.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-31*

Use the existing 2019 servers, no need to calculate that or to separate them.
