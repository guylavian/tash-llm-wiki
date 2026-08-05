---
title: "Computer default printer GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/907930/computer-default-printer-gpo
question_id: 907930
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Computer default printer GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/907930/computer-default-printer-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to create a default printer GPO that only applies to a certain computer security group. The problem that I am running into is that is the "set a default printer" that option only shows up under the "user" GPO. Meaning under the computer settings it is grayed out.     

How can I apply a default printer to a security group that the members are computers?    

All domain controllers are server 2019.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-07-02*

The default printer is an option defined per-user, Windows can't set a default printer for the system.    

I recommend you to create a User GPO and use Item-Level Targeting to specify the target Computer group:

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-03*

Hi there,    

This is by design that it has been greyed out. Unfortunately, when pushing printers with GPP at the Computer level, there is no way to set the default printer. You should use either logon scripts to set the default or GPP at the User configuration level to set the default one.    

Setting default printer in group policy using computer configuration https://social.technet.microsoft.com/Forums/lync/en-US/9117e7fe-5264-4645-a8f3-30518a3db3df/setting-default-printer-in-group-policy-using-computer-configuration-server-2008-r2?forum=winserverGP    

Use Group Policy settings to control printers in Active Directory https://learn.microsoft.com/en-us/troubleshoot/windows-server/printing/use-group-policy-to-control-ad-printer    

------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–
