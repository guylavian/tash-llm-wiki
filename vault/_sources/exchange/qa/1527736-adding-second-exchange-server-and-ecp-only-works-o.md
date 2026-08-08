---
title: "Adding Second Exchange Server and ECP only works on the first one."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1527736/adding-second-exchange-server-and-ecp-only-works-o
question_id: 1527736
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Adding Second Exchange Server and ECP only works on the first one.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1527736/adding-second-exchange-server-and-ecp-only-works-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm working in lab.  Preparing for some new installs.   

Single domain.  One DC.   

I configured the lab with two exchange servers.    

I installed the first exchange sever and have it working with public certs and hybrid mode.  

I added the second exchange server.  I have not changed anything from default after the install.  

When I try to login to the new servers ECP I am redirected to OWA.  If I try to login to the ECP on the first Exchange server, it works fine.  

Is this normal behavior?    

Why wouldn't the ECP work for the second box?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-09*

Hi @ComputerHabit ，

Great to know that the issue has already been resolved.

Since Microsoft Q&A forum has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer : )

[Adding Second Exchange Server and ECP only works on the first one.]
Issue Symptom:
I installed the first exchange sever and have it working with public certs and hybrid mode.

I added the second exchange server. I have not changed anything from default after the install.

When I try to login to the new servers ECP I am redirected to OWA. If I try to login to the ECP on the first Exchange server, it works fine.

Solution:

Waited for some time and the issue was gone.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-08*

Never mind.  I was impatient.  

The server ecp works.  Never mind.  :)  

Maybe replication or something like that.  Timer jobs?
