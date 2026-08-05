---
title: "WinNT provider fails to locate server but LDAP does not"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2746444/winnt-provider-fails-to-locate-server-but-ldap-doe
question_id: 2746444
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 26
qa_tags: []
---
# WinNT provider fails to locate server but LDAP does not

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2746444/winnt-provider-fails-to-locate-server-but-ldap-doe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a script that finds all users on a domain. I am using WinNT ADSI protocol (Set objNTUser = GetObject("WinNT://" & fqdn & "/" & serviceAccount & ",user"))

The serviceaccount is an arguments to the script. (the fqdn is %USERDNSDOMAIN%, and the serviceaccount is a valid domain user. The script works on server 2012, but it fails on server 2016 with error code 462 (cannot locate server or server unavailable)

I then tried the same type of operation using LDAP, and it worked! In PowerShell, the WinNT command gives the error "The RPC Server is unavailable", but that's probably because it cannot locate the server.

What is the communications mechanism that is different between WinNT and LDAP on Windows Server 2016. I'm at my wit's end - opening up virtually all firewalls and setting all roles and features.

## Answer (community) — community member

*upvotes: 0 · updated: 2017-07-14*

Hi,

Your question is beyond the scope of these Forums

This Community is mainly for home users and their computer problems, not business systems.

Kindly post your question in the TechNet Server Forums.

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
