---
title: "Can Active Directory Users and Computers RSAT tool be configured to prompt for password at launch?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/238893/can-active-directory-users-and-computers-rsat-tool
question_id: 238893
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Can Active Directory Users and Computers RSAT tool be configured to prompt for password at launch?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/238893/can-active-directory-users-and-computers-rsat-tool (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We all know that the RSAT tool Active Directory Users and Computers will allow a "user" to run it and view everything and the security doesn't kick in until you try to do something in it (create an account, reset passwords, move or delete items, etc...). Now we don't really have a concern with a regular user installing the tool and poking around because our users have no rights to install programs themselves. However on our IT workstations a lot of us have ADUC either pinned to the taskbar or start menu for ease of access. However there are times where I accidently just click the icon and I'm down in the tree like 8 layers deep until I realize I can't do something becuase I just opened the icon rather than right clicked it and selected Run as Administrator. Is there any way to configure the ADUC yellow book icon to just automatically pop up a password prompt, much like if you were to try to access a c$ share or RDP to something? That way we could just regularlly click the icon in the start menu or taskbar and then the screen could dim and show us the prompt for username and password, and we could fill in our administrator username and credentials there. We don't run our day to day systems as a Domain admin. Even us in IT have a second user account for admin stuff so if I'm online posting this message its my regular account, but if I run an MMC tool or need to move files behind the scenes and access administrative shares, I use a second administrative ID assigned to me.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-26*

FanFan, this is great way to limit non admins from  

Even opening the snap in.  That way it won’t load if I forget to click the special “run as administrator” right click, so I don’t waste time drilling down and then realizing my mistake.  That’s fantastic, thanks!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-20*

Still should have worked. Check Task Manager\Details\Elevated  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-20*

Well I don't want to save credentials, just a pop up is fine, so I tried this in the run box without /savecred.  I think if it would work there it should work as a shortcut...  

runas /user:domain\myadminuseracct %SystemRoot%\system32\dsa.msc  

A command line box comes up (sadly not a windows ui) and I type in my password there, no way to tell what im typing, it doesn't even star or blank out, and obviously there's no eyeball icon to reveal and ensure its right, but I entered it and hit enter, the command window goes away but then nothing happens.  

Part of the problem I think is that these tools are not EXE files.  They are .msc files.  dsa.msc is Active Directory Users and Computers.  

I'm surprised after all these years, like over 21 years at least (thinking of Active Directory's debut in Windows 2000), Microsoft never accommodated this.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-20*

This one may sort it.  

https://www.howtogeek.com/124087/how-to-create-a-shortcut-that-lets-a-standard-user-run-an-application-as-administrator/  

--please don't forget to Accept as answer if the reply is helpful--
