---
title: "unable to create transport rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1488107/unable-to-create-transport-rule
question_id: 1488107
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
---
# unable to create transport rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1488107/unable-to-create-transport-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All
I am trying to create a transport rule, i.e when any email is triggered to one of the DL lets say ******@contoso.com. i want this email to be received to one of my other user say @contoso.com.@contoso.com is not the member of this DL nor can be added as a member. So i want to crate a transport rule.
When i am trying to create transport rule in onprem and online i am getting below errors.

```
Exchange Onprem 
The recipient is : ******@contoso.com  
Bcc the message to: ******@contoso.com  
Error: SentTo predicate does not allow distribution groups. 'DL1'.
```

```
Exchange Online
Apply this rule if: The recipient is '******@contoso.com'
Do the following
Blind carbon copy (bcc) the message to '******@contoso.com'  
Error:  
Error executing cmdlet:   |System.ArgumentException|SentTo predicate does not allow distribution groups. '******@contoso.com'. 
Exception of type 'Microsoft.Exchange.Management.PSDirectInvoke.DirectInvokeCmdletExecutionException' was thrown.
```

## Answers

_No answers on this thread._
