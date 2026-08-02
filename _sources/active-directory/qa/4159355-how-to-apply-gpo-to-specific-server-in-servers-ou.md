---
title: "How to apply GPO to specific server in SERVERS OU?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4159355/how-to-apply-gpo-to-specific-server-in-servers-ou
question_id: 4159355
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# How to apply GPO to specific server in SERVERS OU?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4159355/how-to-apply-gpo-to-specific-server-in-servers-ou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

-  Servers OU - contains all servers, including server1. Main OU for applying GPOs on servers. So, shifting server1 to another OU isn't an option for me.

-  Users OU - Contains all users.

I want to apply a GPO to server1, that will run a logon script when users log in to it. Others servers should not be affected.

How to do it?

What I have done. 

-  Created GPO, set user Logon script, enabled loopback policy with the merge option in Computer Configuration.

-  Applied the GPO to Servers OU.

-  Set the security filtering, and added server1, given permissions are Read, Apply GPO.

-  Removed Authenticated users.

What is wrong here?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-29*

Hello,  

Thanks for reaching out! I'm Microsoft user like you.  

As you have applied User logon  policy , permission need to given to user also , please also give permission to that user or groups to whom those settings will be applied.  

In case of additional questions,  reach out back to me, and I will be happy to help and try our best to resolve your issue.  

Best Regards,  

Prakash
