---
title: "second domain controller cant add user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1571396/second-domain-controller-cant-add-user
question_id: 1571396
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# second domain controller cant add user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1571396/second-domain-controller-cant-add-user (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,
We can't add users from our second domain controller. we are getting this error.
Windows cannot set the password for <user> because

The specified directory object is not bound to a remote resource

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-22*

Hi @rtuesca  

Check if the RID master is available when you try to create new user.

RID muster shoule be available when you  create new object in active directory.
To identy the domain controller with RID master role you can run the following command:

```
netdom query fsmo
```

Start by checking replication health between all domain controllers by runnning the commands below.

If the replication health is ok and the admin has required permission , he should be able to modify object AD from second domain controller.

```
repadmin /showrepl
repadmin /replsummary
dcdiag
```

Please don't forget to accept helpful answer
