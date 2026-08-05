---
title: "A problem with MS Exchange or why outlook does not want to synchronize? 0X80040115 error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1640728/a-problem-with-ms-exchange-or-why-outlook-does-not
question_id: 1640728
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator"]
---
# A problem with MS Exchange or why outlook does not want to synchronize? 0X80040115 error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1640728/a-problem-with-ms-exchange-or-why-outlook-does-not (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

today 2. april 2024 around lunchtime, we had a problem with two users connecting their outlook to the exchange server.

In the event logo of Windows there is a recurring message about the loss and restoration of the connection with the MS Exchange server, but in principle the synchronization does not work at all.

Restarting and repairing the office package didn't help. Even deleting the account and adding it again didn't help.

Any halp?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-04-03*

Hi @Tomáš Rovňák

Could you provide the screenshot of the error message to us?

According to your description, it seems you have error 0x80040115 code when you connect to Exchange Server. In this way, we recommend you check the following suggestions:

1)You should first check if your network is stable and not encountering any issues while connecting to the mailbox server. One way to verify this is to log in to your email using a web browser or webmail.

2)Ensure that the drive where OST is stored (usually C: drive) has more than 10% of the overall drive size space available.

3)Run the following command in the Command Prompt window to flush the DNS cache:

ipconfig /flushdns

For more detail about its steps, you could refer to this blog.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
