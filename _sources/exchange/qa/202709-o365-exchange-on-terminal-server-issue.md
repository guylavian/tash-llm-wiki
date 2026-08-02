---
title: "o365 / Exchange on Terminal Server issue."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/202709/o365-exchange-on-terminal-server-issue
question_id: 202709
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# o365 / Exchange on Terminal Server issue.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/202709/o365-exchange-on-terminal-server-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a question that is currently pondering my mind completely.  

I have a Terminal Server environment running Exchange / O365 with cache mode disabled,  

Everything works perfectly until one of the users mentioned that their outlook contact groups just  

Vanish after re-opening outlook (locally made ones ) Which subsequently aren't synced with OWA as this would not be necessary.   

I have been looking for a solution for roughly one week with no luck.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-18*

Hi @Kieran Forrest   ,    

Only one user have this issue?    

Did only the contact group disappear? Is the contact complete?    

I noticed that you mentioned "aren't synced with OWA". Do you mean that all items in Outlook are not synchronized with OWA? If I understand it wrong, please correct me    

-  Please try to create a test contact group in outlook, then log in to OWA and see if you can see the contact group.    

-  Please try to create a test contact group in OWA and check it in Outlook.    

-  Please run the “outlook /safe” to open outlook as safe mode, to rule out the possibility of add-in causing the issue, Then please create a test contact group and re-opening outlook as safe mode again.     

-  Hold CTRL and Click the outlook Icon in the system tray and select “Test Email Auto Configuration”, to test whether the autodiscover service can work normally.    

     

-  Re-create a new outlook profile.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
