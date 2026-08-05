---
title: "I have doubt in GPO, could someone kindly confirm it."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186494/i-have-doubt-in-gpo-could-someone-kindly-confirm-i
question_id: 2186494
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-devices-other"]
---
# I have doubt in GPO, could someone kindly confirm it.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186494/i-have-doubt-in-gpo-could-someone-kindly-confirm-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts,  

   We are applying GPO to disable windows auto update and disable browsers (Chrome, Edge and Mozilla) auto update in Windows Server 2012 & 2019. We have so many environments, so we don't know which all environments were GPO applied already. So, we are planning to apply the GPO in all our 2012 & 2019 environments.  

 If the GPO was already applied in an environment where we are attempting to apply same GPO to disable auto updates, what would happen in that specific scenario? Will it lead to conflict, or will it have no effect at all? 

When try to apply the same GPOs, we believe no impact at all. But we are not sure about that.   

 Someone from Microsoft kindly confirm it.   

I am looking forward to hearing from you.   

Thanks  

Leo

## Answer (community) — community member

*upvotes: 1 · updated: 2024-06-10*

Hello,

Thank you for posting in Microsoft Community forum.

Based on the description, I understand your question is related to GPO.

Technical, yes, there is no conflict. If the GPO is already applied in an environment, reapplying the same GPO will not cause conflicts. Group Policies are cumulative, and the settings do not conflict with each other. The existing GPO settings will remain intact, and the new settings will be added. If the GPO was previously applied, it will continue to affect the computers in that environment.

Have a nice day. 

Best Regards,

Molly

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-11*

@Molly Lu,  

Hi Molly,  

Thanks for the clarifying my query.  It's really helpful.   

 I have marked your answer as right answer.   

Regards  

Leo

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-10*

@Molly Lu  

Hi Molly,  

I am waiting for your reply.   

Regards  

Leo

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-10*

@Molly Lu  

Hello Molly,   

Thanks for your reply and the explanation. I got it. Only one thing I want to understand.   

You have mentioned it will continue affect the computers in that environment.   

What does that meant? Could you please let me know what the impact that will create when we are trying to apply the same GPO again  

I am waiting for your reply.  

Regards  

Leo
