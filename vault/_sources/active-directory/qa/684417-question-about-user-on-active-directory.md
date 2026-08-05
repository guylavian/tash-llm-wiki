---
title: "QUESTION ABOUT USER ON ACTIVE DIRECTORY"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/684417/question-about-user-on-active-directory
question_id: 684417
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# QUESTION ABOUT USER ON ACTIVE DIRECTORY

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/684417/question-about-user-on-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello, recently the server 2012 r2 was formatted and i lost the active directory settings, i reinstalled the operating system and put the same domain in the case the name, and i'm creating users again, but some machines when reboots lose all settings. what can be causing this? would it be a conflict of the same domain name?  

alguns usuarios quando reinicia a maquina nao perde as informações, é como se fosse um perfil temporario mais não é.  

some users when restarting the machine do not lose the information, it is as if it were a temporary profile but it is not.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-07*

Hi there,  

If you are using the roaming user profile instead of a local user profile, add the user to the local workstation Users group and see if that can help you.  

-Press WIN+R, type lusrmgr.msc.  

-Click Group in the left navigating pane, click Users group, click Add to add the Domain Users group into the local Users group.  

After that, restart the computer and log in with the domain user to try again and see if the settings remain.  

Here is a thread as well which discusses the same issue and you can try out some troubleshooting steps from this and see if that helps you to sort the Issue.  

https://social.technet.microsoft.com/Forums/en-US/f7228ab1-8715-4a73-93b1-4ee9d48f344f/every-time-domain-users-log-off-or-reboot-win10-pc-profile-data-is-lost?forum=w7itproui  

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-01-05*

Hi,  

If the server you formatted is the last domain controller , you have to restore it from a backup to avoid lost the domain and all domain settings  (GPO, user profile , computer object , DFS settings ...ect). If you install new domain with same name , you will loose all domain settings and all member machines must be rejoin the new domain and loose all domain settings.  

Please don't forget to mark helpful reply as answer

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-05*

Even with creating a new domain with the same domain, it is in fact a new and different underlying GUID so the desktops will all need to be joined to the new domain and users will get new domain profiles. One work-around is to logon once as the new domain user so the new profile gets created, then logon as another user with local admin rights, navigate to  

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList  

find the new domain profile and point the expand string ProfileImagePath to the old profile.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
