---
title: "MS Exchange active sync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/282343/ms-exchange-active-sync
question_id: 282343
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# MS Exchange active sync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/282343/ms-exchange-active-sync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I am using MS Exchange 2013, I notice that when user change their password & also new user are unable to configure outlook on their android device, web access is ok, for users who already using it working fine for them, for some reason active sync is not working, even its enable in users mail box feature, what's the best way to to troubleshoot it, same URL is working fine for web mail. Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-23*

Hi, @Salman Arshad       

I notice that when user change their password & also new user are unable to configure outlook on their android device    

Did the users use the new passwords to login?    

Are they able to login with the old passwords?    

I would recommend using the ExRCA tool (Microsoft Remote Connectivity Analyzer Tool) to troubleshoot the problem.    

You may test with a newly created account and check if there are some errors in the result.    

Besides, please also check if there are some error or warning events related to activesync generated in the event viewer>application log.    

And here is also a Microsoft KB on how to troubleshoot activesync for your reference: Troubleshoot ActiveSync with Exchange Server    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
