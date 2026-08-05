---
title: "Domain controller (maximum off time)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/95982/domain-controller-maximum-off-time
question_id: 95982
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Domain controller (maximum off time)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/95982/domain-controller-maximum-off-time (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have to depromote a DC and as a precaution to verify that everything works, we have an idea to turn it off for a week or two.  

What is the maximum time that a DC can be off without problems of decoupling? 90 days?  

I'm not sure how long that is.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-09-15*

Hi @Angel Garcia Gomez  ,    

By default it should be 60 days on older operating system versions, it may depend the operating system and Service pack level, on newer operating systems (Windows Server 2012 and later) the default is 180 days.    

    

It is ultimately determined by the Tombstone Lifetime in the forest, you'll find some more information here:    

Determine the tombstone lifetime for the forest      

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc784932(v=ws.10)    

----------    

(If the reply was helpful please don't forget to upvote or accept as answer, thank you)    

Best regards,    

Leon

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-16*

Hello @Angel Garcia Gomez   ,    

Thank you for posting here,    

Just like the previous two replies, your current operation will not have any impact. At the same time, you can also check the time of DC's tombstone lifetime and change the time. You can refer to the link below:    

https://www.windowstechno.com/how-can-i-check-the-tombstone-lifetime-of-my-active-directory-forest/    

Best regards,    

Stephanie Yu    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-15*

Hi,  

Two week should be ok because tombstone lifetime is 60 days or more (it depend of domain controller operating system ).  

If a DC stay offline during a period exceeded the tombstone lifetime, it will be able to replicate with others replication partners and you have to demote it using metadata cleanup , rebuild it and promote it again.  

Please don't forget to mark this reply as answer if it help you to fix your issue
