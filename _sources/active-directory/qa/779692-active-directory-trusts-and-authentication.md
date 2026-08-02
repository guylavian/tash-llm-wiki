---
title: "Active Directory Trusts and Authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/779692/active-directory-trusts-and-authentication
question_id: 779692
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory Trusts and Authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/779692/active-directory-trusts-and-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For example let's assume we have writable DCs, if I have a domain called local.com and another called local1.local.com and have a two-way trust relationship what will happen if the connection is broken between the domains? Will users in local.com domain still be able to access resources in local1.local.com if they were logged on to the local1.local.com before. In other words are information like passwords cached for  local.com domain on local1.local.com domain?   

As from my experience I know that local1.local.com domain will only store passwords for accounts belonging to the same domain, and will only store things like SIDs etc and not passwords for the external domain and if the link between them are broken users from an external domain local.com will not be able to authenticate, is this correct?   

Please verify: The only why to circumvent this will be to have a read only DC  for local.com in the same location as local1.local.com, so that if there is a failure users that have already logged onto local.com using the local DC will have a copy stored of their information and will then be able to authenticate to local1.local.com using their local.com credentials in case of a WAN failure

## Answers

_No answers on this thread._
