---
title: "Communication between exchange server , email send and receive"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1182786/communication-between-exchange-server-email-send-a
question_id: 1182786
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Communication between exchange server , email send and receive

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1182786/communication-between-exchange-server-email-send-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Support,

We have two location with exchange servers in both location

Site A -we have two Exchange server and ad and also Email gateway 

Site B -we have two exchange server but email send/receive from Site A email gateway only (it located in different country )

both sites are connected over MPLS lan connectivity and same forest extended 

so if site a users wants to send email site B vice versa it consumed MPLS connectivity 

and site B users wants to send/ receive email to/from external so its also consumed the MPLS connectivity because email comes from Site B to Site A email gateway and from there it out and same way comes inside.

my question , is it possible that if Site B users want to send/receive email from external should not use MPLS direct use their internet connection, like by keep two email gateway or any other option 

please advice

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-22*

Hi @Yasar mistry,

In the same forest, you can create a new send connector with siteB's Exchange server as source server to allow routing emails through the siteB server, but emails still need to be received from siteA to siteB.

If you need, you can check this article about creating send connectors: Create a Send connector in Exchange Server to send mail to the internet.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
