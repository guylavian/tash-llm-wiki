---
title: "EXCHANGE not send email (and seems not receive it)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1306271/exchange-not-send-email-and-seems-not-receive-it
question_id: 1306271
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# EXCHANGE not send email (and seems not receive it)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1306271/exchange-not-send-email-and-seems-not-receive-it (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

 

Latest Alma Linux with latest postfix as relayhost.  

Exchange 2016 last CU

 

Email is sent. All ok in postfix maillog. With wireshark on exchange, i can see that email is sent from postfix to exchange.  

But exchange does not send email, and with get-messagetrackinglog, i have no trace.

How can i find full mail trace to debug this issue?

Regards.

Alex.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-06-16*

Hi @Alex,

Have you created a custom receive connector on Exchange server used for SMTP relay?

Refer to this link: Allow anonymous relay on Exchange servers

If not yet, please follow the guide to create the receive connector and specify the ip address of your postfix server.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
