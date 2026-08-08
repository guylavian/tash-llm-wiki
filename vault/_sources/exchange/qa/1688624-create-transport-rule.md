---
title: "Create Transport Rule."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1688624/create-transport-rule
question_id: 1688624
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
---
# Create Transport Rule.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1688624/create-transport-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Distribution List (DL) (******@contoso.com) in Exchange Online with 30,000 internal users. Only ******@contoso.com is allowed to send emails to this DL (Delivery Management: Specified Senders: ******@contoso.com).

User1 is planning to send an email to this DL with the subject "Important Email," and the DL will be in Bcc. My requirement is that none of the DL members should be able to reply to ******@contoso.com with subjects like "RE: Important Email" or "Important Email."

Will the following transport rule work?

If any user replies back by changing the email subject, then this transport rule will not work. Is there any other way to restrict users from replying to user1 to this one email even if the email subject is changed? Can we create a rule based on the message ID once the email is triggered?

## Answers

_No answers on this thread._
