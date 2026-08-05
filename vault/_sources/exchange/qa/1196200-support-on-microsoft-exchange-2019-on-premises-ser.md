---
title: "Support on Microsoft Exchange 2019 on premises server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1196200/support-on-microsoft-exchange-2019-on-premises-ser
question_id: 1196200
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Support on Microsoft Exchange 2019 on premises server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1196200/support-on-microsoft-exchange-2019-on-premises-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our company needs to use Proof point Enterprise protection for our email server, it is on premises Microsoft exchange server 2019 with 2 redundant servers and one Edge server, and we need to get Inbound and outbound email volume in Hourly peak volume and daily Volume. So I need your help to guide me how to get those data from our system

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-04-05*

Hi @Rahel Kiros  

There is no built-in feature in Exchange on-premises to achieve this.

However, you can use scripts to get the information from message tracking log (by default the age of this log is 30 days, which means you can only track messages sent or received within the last 30 days) and then custom your report.

While kindly note that we mainly focus on general usage issues about Exchange, so we do not support scripting.
If you need help or advise on scripting, please consider posting in scripting forums.

Thanks for your understanding.

Below are some threads with the similar requirement.
For your reference:

How to check total mails(IN and OUT) of one month in exchange server 2016 

(Please refer to Kyle's answer, you can modify the timestamp part to meet your needs)

Script to count number of emails for multiple users

(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
