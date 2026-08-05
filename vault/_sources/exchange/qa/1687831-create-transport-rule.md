---
title: "create transport rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1687831/create-transport-rule
question_id: 1687831
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
---
# create transport rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1687831/create-transport-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am using an Exchange hybrid environment. I have a DL(mydl) in Exchange on-premises. I want to create the following transport rule. I can create this in Exchange Online, but I cannot create it in Exchange on-premises as I don't see all the options. I am using Exchange 2016. The DL is on-premises and all my users are online. Will just creating the transport rule online work?

Additionally, I need to know if there's an option to reject emails triggered in Bcc to the DL.

```
Name:Test1

Apply this rule if: The message: The To or Cc box contains '******@mydomain.com'

Do the following:
Block the message: Reject the message with the explaination 'DL is restricted'

Except if: the sender: 
The senders domain is '1.com' or '1.org'
```

## Answers

_No answers on this thread._
