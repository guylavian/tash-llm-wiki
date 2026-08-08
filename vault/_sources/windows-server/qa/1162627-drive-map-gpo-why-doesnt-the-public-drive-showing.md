---
title: "Drive Map GPO: Why doesn't the Public Drive showing for the user ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1162627/drive-map-gpo-why-doesnt-the-public-drive-showing
question_id: 1162627
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Drive Map GPO: Why doesn't the Public Drive showing for the user ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1162627/drive-map-gpo-why-doesnt-the-public-drive-showing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[

](https://learn-attachment.microsoft.com/api/attachments/59ab8e27-e294-4fb0-bf9f-c5377beeb8c8?platform=QnA"https://learn-attachment.microsoft.com/api/attachments/6d03f33f-2023-4d7a-98a4-a5fb908a97fb?platform=QnA" alt="Image" />

](https://learn-attachment.microsoft.com/api/attachments/6d03f33f-2023-4d7a-98a4-a5fb908a97fb?platform=QnA"https://learn-attachment.microsoft.com/api/attachments/991f6818-5c4c-4828-8371-72ba8a61caf6?platform=QnA" alt="Image" />

](https://learn-attachment.microsoft.com/api/attachments/991f6818-5c4c-4828-8371-72ba8a61caf6?platform=QnA"https://learn-attachment.microsoft.com/api/attachments/e036552d-0287-4e5a-b220-8a47d0c2ec2d?platform=QnA" alt="Image" />

](https://learn-attachment.microsoft.com/api/attachments/e036552d-0287-4e5a-b220-8a47d0c2ec2d?platform=QnA"https://learn-attachment.microsoft.com/api/attachments/2b61ea08-ed0c-4f40-aa2d-e176af3c383b?platform=QnA" alt="Image" />

](https://learn-attachment.microsoft.com/api/attachments/2b61ea08-ed0c-4f40-aa2d-e176af3c383b?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-20*

Hello

Thank you for your question and reaching out. I can understand you are  having query\issues related  to Mapping of Drive using GPO.

On Client computer where the public drive is not mapped  run the command rsop.msc from the client computer.

It is always good idea to organise the OU groups and seperate computers and users which in the login run makes creating GPO's for each object (User or Computer) easier to target.

Reference:

https://techcommunity.microsoft.com/t5/windows-server-for-it-pro/map-drive-group-policy-preferences-not-applying-consistently/m-p/2340407

--If the reply is helpful, please Upvote and Accept as answer--
