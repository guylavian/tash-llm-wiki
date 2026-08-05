---
title: "How to encrypt connection between Exchanger server and Exchange online?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1427034/how-to-encrypt-connection-between-exchanger-server
question_id: 1427034
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to encrypt connection between Exchanger server and Exchange online?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1427034/how-to-encrypt-connection-between-exchanger-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello guys.

In a Hybrid environment.

I am facing an issue with keep getting this alert from SEIM server  

Error: "Outbound cleartext password usage from non guest network on port 25"

The source of this alert is my On-premises exchange server and the destination is O365.

I tried to enabling TLS 1.2 on my exchange servers and changed the send connector port from 25 to (465or587) with restarting exchnage transport service , after that change, the exchnage online wasn't able to receive emails from my exchnage server, as they keep stuck in exchnage server queue.

Also, I have checked the certificate assigned to smtp and it is valid.

So the question here, how can i configure SMTPS or a secure connection between Exchanger server and Exchange online.

Appreciate your cooperation.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-17*

Hi @Abdallah Sho  

By default the connection between Exchange on-premises and Exchange Online should be encrypted if you have configured the hybrid deployment with HCW.

Could you provide more details about this alert? For example, would it be possible to capture these network packets for analysis?

Since further analysis is required for this issue, if possible please contact support by phone or email for better assistance.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
