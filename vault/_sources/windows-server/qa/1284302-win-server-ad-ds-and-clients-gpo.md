---
title: "Win Server AD DS and Clients GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1284302/win-server-ad-ds-and-clients-gpo
question_id: 1284302
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Win Server AD DS and Clients GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1284302/win-server-ad-ds-and-clients-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have a scenario office environment with a Win Server AD DS and several clients Win 10/11 Pro

All clients join the Domain and receive GPO from Win Server. 

At the beginning of the day, when users arrive at the office, they log in to Client with domain credentials and start working. They have mapped network drives managed by GPO that loads up automatically. 

During the day, users who have a notebook, often time go out of the office, keep working outside LAN/Domain. When they return to the office, sometimes they are unable to access mapped network drives. I tried to run “`gpupdate /force`” but it does not resolve the issue: mapped network drives are still not accessible. The only way to solve the problem is logging out and again logging in. So far, this is the solution I found. 

The drawback of this action (log out/in) is a huge discomfort because they are forced to close all applications opened and anything that they were working on. 

**  

Question**: is there a way to avoid logging out/in when they return to the office? 

To me, there must be a way because it would make no sense especially for those users who frequently go in and out of the office. 

Please let me know if anyone has had this issue and if is there an alternative solution to log out/in

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-14*

Hi,  

thank you for your reply.

I wish to clarify what you stated "Mapped Drives are gone".

Mapped Drives are still there but when I click on them they are not accessible. So the only way to gain access is to log out/in.

I will try to keep your suggestion in mind and try to replicate the issue and see if it will work

Will let you know.

One simple question: why would this help if credential is the issue?

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-05-14*

Hello @SAngeli!

Welocme to Microsoft QnA!

I understand that your users are leaving Office during Office hours and when returning the Mapped Drives are gone 

You want to be able to reconnect them a easy as possible withou having to log off log on again

I can think some solutions :

First of all , have you tried the persistent option :

net use X: \server\share /persistent:yes 

For this i am not sure if it wil work but taken from here it should 

https://lazyadmin.nl/it/net-use-command/

Manual User Click a Script :

Create a Script that users hit when returning that reconnects the drives :

net use X: /delete

net use X: \server\share1

I hope this helps!

Kindly mark the answer as Accepted and Upvote in case it helped!

Regards
