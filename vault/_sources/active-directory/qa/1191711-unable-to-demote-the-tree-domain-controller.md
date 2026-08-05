---
title: "unable to demote the Tree domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191711/unable-to-demote-the-tree-domain-controller
question_id: 1191711
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# unable to demote the Tree domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191711/unable-to-demote-the-tree-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

Please, need help

I created a new Tree DC, with a different namespace than the root DC, both are connected through the Windows server 2022 Router.

Root DC:

-  namespace: ABC.com

-  IP: 192.168.10.1

Tree DC:

-  namespace: ECST.com

-  IP: 10.255.255.1

In the process of creating Tree DC, I did not join the server to the domain (ABC.com), I just went through the process of adding the AD services rule, then selected Tree and wrote the credentials (ABC.com\Administrator) and it acknowledged the root DC(ABC.com) and I continued normally until I finished creating the new Tree DC ECST.com

I also configured sites, and subnets for both root and tree, also configured trust.

Both are pinging with IP and name.

When I tried to demote the Tree DC(Last DC) I got the following error:

so, after that error, I removed DNS from Tree DC but I failed to demote the Tree DC, so I deleted the sites and subnets and configured the IP of Tree DC to be in the same range as Root DC, although both are pinging unfortunately still demote fails.

I really don't want to use force removal.

How to fix it

## Answers

_No answers on this thread._
