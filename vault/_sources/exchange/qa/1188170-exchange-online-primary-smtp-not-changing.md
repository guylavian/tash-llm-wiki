---
title: "Exchange Online primary smtp not changing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1188170/exchange-online-primary-smtp-not-changing
question_id: 1188170
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
---
# Exchange Online primary smtp not changing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1188170/exchange-online-primary-smtp-not-changing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Have a user in Exchange admin center, who was with the company then left and account was disabled for some time. I believe someone enabled the account and thought everthing was good to go. Its not, turns out the user is synced from Onprem but the primary smtp isnt set right. I go to EXO and set it there and get this lovely error:

Users account show e.g. ******@domain.onmicrosoft.com it should be showing ******@domain.com

Error:

Error executing request. An Azure Active Directory call was made to keep object in sync between Azure Active Directory and Exchange Online. However, it failed. Detailed error message: Unable to update the specified properties for on-premises mastered Directory Sync objects or objects currently undergoing migration. DualWrite (Graph) RequestId: 96f09612-9b8f-4ed4-9420-61feecbba3df The issue may be transient and please retry a couple of minutes later. If issue persists, please see exception members for more information.

I do have a ticket open with Microsoft and they're stumped as well but investigating. 

I've checked all the onpremise attributes and ensured that Primary SMTP reflects ******@domain.com as well as userPrincipalName set to ******@domain.com.

Not sure what to do?

## Answers

_No answers on this thread._
