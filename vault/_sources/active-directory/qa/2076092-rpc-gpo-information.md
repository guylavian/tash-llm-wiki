---
title: "RPC GPO information"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2076092/rpc-gpo-information
question_id: 2076092
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-print-jobs", "windows-business-windows-server-user-experience-user-experience-other"]
---
# RPC GPO information

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2076092/rpc-gpo-information (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All

I have been asked to enable the following printer-related GPOs, but I am not fully aware of their impact. Could anyone help me understand the pros and cons of these settings? The last one i dont think its printer related but i need information on that as well.

```
Computer Configuration-->Policies-->Administrative Templates-->Printers-->Configure Redirection Guard:Enabled: Redirection Guard Enabled

Computer Configuration-->Policies-->Administrative Templates-->Printers-->Configure RPC connection settings: Protocol to use for outgoing RPC connections:Enabled: Redirection Guard Enabled

Computer Configuration-->Policies-->Administrative Templates-->Printers-->Configure RPC connection settings: Use authentication for outgoing RPC connections: Enabled: Default

Computer Configuration-->Policies-->Administrative Templates-->Printers-->Configure RPC listener settings: Configure protocol options for incoming RPC connections: Enabled: RPC over TCP

Computer Configuration-->Policies-->Administrative Templates-->Printers-->Configure RPC listener settings: Configure protocol options for incoming RPC connections: Enabled: Negotiate or higher

Computer Configuration-->Policies-->Administrative Templates-->Printers-->Configure RPC over TCP port: Enabled: 0

Computer Configuration-->Policies-->Administrative Templates-->MS Security Guide-->Configure RPC packet level privacy setting for incoming connections:Enabled
```

## Answers

_No answers on this thread._
