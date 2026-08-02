---
title: "Non-unique proxy address in exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1502797/non-unique-proxy-address-in-exchange-online
question_id: 1502797
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
---
# Non-unique proxy address in exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1502797/non-unique-proxy-address-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We are having a hybrid environment and O365 licenses are assigned through a security group. So, whoever present in the group will obtain the O365 license.   

However, for one of the user, there is some issue. When we check the status of license for this user, we are getting "Non-unique proxy address in exchange online"   This is the status shown in azure AD. On the other hand, in the M365 admin portal, it shows unlicensed.
**  

We tried to find duplicate proxy in the tenant, however it went vain. We ran following PowerShell command:

```
get-recipient | where-object {$_.emailaddresses -match  "******@contoso.com"} | fl
```

Can someone help me how to resolve this?

## Answers

_No answers on this thread._
