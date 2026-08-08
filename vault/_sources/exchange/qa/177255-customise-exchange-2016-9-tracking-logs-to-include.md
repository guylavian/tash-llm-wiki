---
title: "Customise Exchange 2016/9 tracking logs to include values from X-headers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/177255/customise-exchange-2016-9-tracking-logs-to-include
question_id: 177255
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Customise Exchange 2016/9 tracking logs to include values from X-headers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/177255/customise-exchange-2016-9-tracking-logs-to-include (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Does anyone know how to I can enhance the message tracking logs of Exchange 2016/9 to include the value of a custom X-Header in the emails?  

For example, my customer has Outlook automatically put an x-header in every message. They have now asked me to produce audit data of all mails, to, from date, time etc, but to also include the value of this X-header.  

Message tracking Logs contain all the other values they want audited.  

Thanks in advance.  

Martyn

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-27*

Hi @NASH Martyn       

I agree with Andy, your requirement is hard to achieve. X-header is not recorded in the message tracking log.    

And the information recorded in the message tracking log here: Fields in the message tracking log files    

We are not able to customize the fields in message tracking log.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-26*

You arent going to be able to grab those from the message logs    

If you were in Exchange Online, you could see what rules were triggered for a message in message tracking, but that funcationality doesnt exist on-prem    

https://learn.microsoft.com/en-us/archive/blogs/eopfieldnotes/auditing-transport-rules    

(Even though in on-prem EAC the option is there, that option on-prem is for incident report generation and that gets stamped in the message tracking logs. )
