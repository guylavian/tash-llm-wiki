---
title: "Skype for business server2019 & Exchange server 2016 integration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/166374/skype-for-business-server2019-exchange-server-2016
question_id: 166374
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-skype-business-platform-windows", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Skype for business server2019 & Exchange server 2016 integration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/166374/skype-for-business-server2019-exchange-server-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We are using Skype for business server2019 & Exchange server 2016 and trying to implement the voicemail feature in skype for business.  

FYI: I don't find the dial pad in my skype for business client 2016  

Can you help us to do the implementation  

Thanks and regards  

Navinkumar S

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-18*

Hi @Navin Kumar  ,

What is your current environment? On-premise or Online?

In general, Configuring Cloud Voicemail involves the following tasks:

1.Ensure that you have met the prerequisites as described in Plan Cloud Voicemail service.  

https://learn.microsoft.com/en-us/skypeforbusiness/hybrid/plan-cloud-voicemail

2.Ensure that you have set up hybrid connectivity as described in Plan hybrid connectivity and Configure hybrid connectivity.

3.Configure Cloud Voicemail as the hosting provider on the Front End Server

4.Configure a hosted voicemail policy

5.Assign a hosted voicemail policy

6.Enable a user for Cloud Voicemail

For more detailed steps, you can learn it from:

https://learn.microsoft.com/en-us/skypeforbusiness/hybrid/configure-cloud-voicemail

If the response is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
