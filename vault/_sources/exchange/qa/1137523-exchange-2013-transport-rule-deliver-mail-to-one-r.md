---
title: "Exchange 2013. Transport rule deliver mail to one recepient and reject to others."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1137523/exchange-2013-transport-rule-deliver-mail-to-one-r
question_id: 1137523
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013. Transport rule deliver mail to one recepient and reject to others.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1137523/exchange-2013-transport-rule-deliver-mail-to-one-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. Colud you help please.    

Is there any rule to deliver mail to target recepient and drop to others if the mail was sent to multiple receepients in Exchange 2013?    

For example there is user ivanov@test  .com who sent mail to: petrov@test  .com, sidorov@test  .com, support@test  .com. Is there any option (transport rule) that will receive mail to support@ only, not to other ones? TY.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-22*

Hi @NTforGood   ,    

You coud set the following email flow rules, and you could also choose to delete the message directly.    

    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
