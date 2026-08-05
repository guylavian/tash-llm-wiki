---
title: "CU23 exchange 216 single server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185867/cu23-exchange-216-single-server
question_id: 1185867
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# CU23 exchange 216 single server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185867/cu23-exchange-216-single-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I'am installaing CU23 for exchange 2016 in a single server environment en running into the following issue:

I did al the prerquiremnents and they all where completed succesfull but when running the update it fails during update CAS. 

Hope you can help solve this issue

Greetings

Roel

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-03*

Hi @Roel Knippen  ,

In my experience, installing Exchange Server in a new environment with all prerequisites can usually be successfully installed by restarting the server and then running Exchange Server Setup.

In addition, I found a similar thread with error, the user resolved the error by replacing the corrupted file in the current server with the ConfigureCafeResponseHeaders.ps1 file from another functioning server.

 

For more information, please refer to this link:

Exchange 2019 CU12 Fails at Mailbox Service Role: Client Access Service - Microsoft Q&A

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
