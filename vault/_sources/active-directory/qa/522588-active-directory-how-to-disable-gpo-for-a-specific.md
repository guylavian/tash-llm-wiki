---
title: "Active Directory - How to disable GPO for a specific admin group (not standard users)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/522588/active-directory-how-to-disable-gpo-for-a-specific
question_id: 522588
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory - How to disable GPO for a specific admin group (not standard users)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/522588/active-directory-how-to-disable-gpo-for-a-specific (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

After multiple searches, I unfortunately cannot find a solution to a problem with GPO's (Windows 2019 Server).  

I created a GPO which activates the firewall (Computer Configuration), computers present in an OU (Dekstops). This one works perfectly to users. But I want to deactivate it for a specific admin group. To do this I applied in the delegation a "Deny" in "Apply group policy" (admins group).  

Also, this group is a member of local Administrators (with another GPO, I used "Restricted Groups" to do that)  

After performing several tests with a member of this admin group and executed some "gpupdate /force", the GPO still applied. Do you have a solution to bypass this GPO for my admin group ?  

I also tried to apply the loopback on this GPO but still the same result ... Thank you for your help and advices.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-25*

Anyone have a solution or an idea to resolve this problem ?  

Is it possible to bypass the "computer configuration" policies for a specific group ?  

Many thanks.  

Best,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-20*

Hello @Andreas Baumgarten  ,    

Thanks for the reply. Yes, I tried the "Group Policy loopback" with the both modes : Merge / Replace. Unfortunately, same result...    

Below the configuration :

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-08-20*

Hi @Maverick128   ,    

have you tried the loopback processing for the GPO?    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/loopback-processing-of-group-policy    

----------    

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)    

Regards    

Andreas Baumgarten
