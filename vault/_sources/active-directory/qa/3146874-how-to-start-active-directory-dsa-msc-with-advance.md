---
title: "How to start Active Directory dsa.msc with Advances Features enabled at startup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3146874/how-to-start-active-directory-dsa-msc-with-advance
question_id: 3146874
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 98
qa_tags: []
---
# How to start Active Directory dsa.msc with Advances Features enabled at startup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3146874/how-to-start-active-directory-dsa-msc-with-advance (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to log in to AD with advanced features already enabled with a shortcut.

I had no success finding the right switch for dsa.msc for my shortcut. The help section in the service didn't provide anything useful info, neither pages on the net. I also tried command line for help with C:\Windows\System32\dsa.msc /? to see if I could
 find params for lauching, but to no avail.

The shortcut I made so far looks something like this:

C:\Windows\System32\runas.exe /netonly /user:_DOMAIN\USERNAME_ "mmc %SystemRoot%\system32\dsa.msc /SERVER=_SERVERNAME_"  

How should I amend it?

I can't save the console setting, btw as I am not an admin for the workstation.

Could you also please provide me with a list of shortcut for startup parameters or where to find those? 

Thanks in advance.

## Answer (community) — community member

*upvotes: 14 · updated: 2018-10-22*

Solved it.

I just had to clear the cache of AD. 

File → Options → Delete files

After that I set up the Advanced features by View → Advanced features.

Then File → Exit

When I logged back to AD advanced features was already enabled. :)

This site could be also useful, but not in my case:

https://www.it-etc.com/2010/06/08/keep-the-%E2%80%9Cadvanced-features%E2%80%9D-view-always-on-in-active-directory-users-and-computers-mmc/
