---
title: "[Exchange On-Premise]List risky attachments"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/295038/exchange-on-premise-list-risky-attachments
question_id: 295038
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# [Exchange On-Premise]List risky attachments

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/295038/exchange-on-premise-list-risky-attachments (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have transport rule which blocking attachments with specific extension. How to check which attachments are dangerous while sending message which rejected by transport rule? In message track i can check only which rule rejected the message.  

Regards, Mateusz

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-05*

Dear AnyDavid,  

I only has been received report in which no have information which attachment has been dangerous.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-05*

Why not generate an incident report in the rule and send it to another mailbox so you can view the original email that was blocked and see what attachment was in there?    

    

for the Content, select "Original Mail"

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-03*

Hi @mbandurski18   ,    

According to my research, seems like there is no way to 'list' the rejected attachments.    

Since you could check the rule that blocked the message, you can use Get-TransportRule to check the details.    

Also the best practice is to add a notification to Sender or Recipient when the rule is doing it's job.    

    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
