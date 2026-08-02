---
title: "Private Personal Identifier with 2 nodes ADFS : how generate same PPID from both servers ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/11776/private-personal-identifier-with-2-nodes-adfs-how
question_id: 11776
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Private Personal Identifier with 2 nodes ADFS : how generate same PPID from both servers ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/11776/private-personal-identifier-with-2-nodes-adfs-how (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I try to generate a PPID claim on ADFS windows 2019 with the rule (from https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/technical-reference/when-to-use-a-custom-claim-rule) :    

c:[Type == "https://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]      

 => issue(store = "_OpaqueIdStore", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/privatepersonalidentifier"), query = "{0};{1};{2}", param = "ppid", param = c.Value, param = c.OriginalIssuer);    

But my setup is a two nodes ADFS Farm (with SQL cluster as a back end) behind a load balancer    

My problem is that each node generate a different PPID for the same user.    

To my understing adfs should generate the same PPID from both servers?    

Is it possible (and how) with _OpaqueIdStore to generate same PPID from different servers of the same ADFS farm ?    

Thank you in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-04-15*

Hello, sorry for the delay to follow up but I was a bit busy.... you were on the right track ! Simplified the rules and tested against Claims X-Ray....

And it shows that the problem is NOT in store _OpaqueIdStore, whose arguments are case-sensitive (sound logical) but, as strangely seems, that the CASE of http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname is not consistent beetween node A and node B of my farm

-    on node A Windows Account name is like CONTOSO\ds123456

-    on node B Windows Account Name is like CONTOSO\DS123456 (for the very same user, same AD ....) : different case

very strange behaviour...

my simplifed rule

```
c1:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]
  => issue(store = "_OpaqueIdStore", types = ("http://i-idd.silab.cea.fr/internal/ppidwan"), query = "{0};{1};{2}", param = "ppid", param = c1.Value, param = c1.OriginalIssuer);
```
