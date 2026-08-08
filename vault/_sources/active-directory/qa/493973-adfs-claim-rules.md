---
title: "ADFS Claim Rules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/493973/adfs-claim-rules
question_id: 493973
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Claim Rules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/493973/adfs-claim-rules (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello folks! We have a bit of situation. I will try to sum it up. We have a mdm server, and our staff wants our adfs to block other traffics if the request comes through active sync protocol. I have written these rules below, but whenever i activate them and restart adfs service, some random users getting asked their passwords again and again on Outlook client (the small window where outlook asks for your username and password).  

```
c1:[Type == "https://schemas.microsoft.com/2012/01/requestcontext/claims/x-ms-forwarded-client-ip", Value =~ "\b100\.100\.100\.100\b"]

=> issue(Type = "http://custom/mdm", Value = "true");
```

 This rule defines the server i was talking about, which has the 100.100.100.100 ip let's say.  

```
c1:[Type == "http://custom/mdm", Value != "true"] 

&& c2:[Type == "https://schemas.microsoft.com/2012/01/requestcontext/claims/x-ms-client-application", Value =~ "Microsoft.Exchange.ActiveSync"]

=> issue(Type = "https://schemas.microsoft.com/authorization/claims/deny", Value = "DenyUsersWithClaim");
```

Second rule is, if the traffic is not coming from 100.100.100.100 AND protocol is active sync, block the connection. I am not sure about this one.   

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid", Value == "S-1-5....", Issuer =~ "^AD AUTHORITY$"]

=> issue(Type = "http://schemas.microsoft.com/authorization/claims/permit", Value = "true");
```

We also have a exception active directory group, this one works well, no problems.  

```
c:[]
=> issue(Type = "https://schemas.microsoft.com/authorization/claims/permit", Value = "true");
```

And lastly permit all other connections rule. I have tried this one with c:[] and without c:[]. I am not sure if i should put it there.   

Any ideas? What could be the reason of these Outlook password behaviours?

## Answers

_No answers on this thread._
