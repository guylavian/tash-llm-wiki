---
title: "Exchange 2019 Remove Public Calender"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1184202/exchange-2019-remove-public-calender
question_id: 1184202
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 Remove Public Calender

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1184202/exchange-2019-remove-public-calender (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there no way to remove the public calendar option within Exchange owa? Using sharing policies with Anonymous to allow external users defined by end user to share calendar. However, it also allows a html link for public usage. So if a user adds a specific external user its assigned to them, but the option of "Public Calendar" is also prevented. If I remove Anonymous from policy the "Public Calendar" option is gone, but then specific external users are not allowed. It seems they are tied together. Is there any way around this. I do not want users to be able to just post publicly.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-27*

Hi @Bman9111  ,

Is there no way to remove the public calendar option within Exchange owa? 

As far as I know, this is currently not feasible. As mentioned in this official blog, once the calendar is published for anonymous users, it allows "anyone with the link to the calendar to view it without having to log-on". (The blog only mentions about Exchange Online and Exchange 2013, but can be applied to Exchange 2019 as well.)

And for your scenario, seems like setting up federation is not applicable, right? Given this, I am afraid there's no way around it at present. 

I've tried submitting this idea to the official feedback portal for Exchange server. The link would be left below in case you or other community users would like to add vote or comment there as well:

https://feedbackportal.microsoft.com/feedback/idea/81a352b0-4eb6-ed11-a81b-000d3a0450e3

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
