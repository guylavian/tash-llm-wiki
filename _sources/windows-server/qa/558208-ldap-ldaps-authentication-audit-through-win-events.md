---
title: "LDAP/LDAPS authentication Audit through win events"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/558208/ldap-ldaps-authentication-audit-through-win-events
question_id: 558208
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# LDAP/LDAPS authentication Audit through win events

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/558208/ldap-ldaps-authentication-audit-through-win-events (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I looking for the best way to get information about the LDAP/LDAPS authentication from applications to my DC (2016)  

I found :  

-  Events ID 2889 for LDAP requests    

-  Events ID 4624 that I only plan to keep only if the logon type is "network logon" (3)  

What else can I get? How can I more information? How can I filter the 4624 events to only keep LDAP(S) request to my DC?  

Thanks in advance

## Answer (community) — community member

*upvotes: 3 · updated: 2021-09-20*

Hello,    

You may enable LDAP Signing for better security.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/enable-ldap-signing-in-windows-server    

Also you can enable additional event login for LDAP.    

Open Registry Editor. Go to HKEY_LOCAL_MACHINE → SYSTEM → CurrentControlSet → Services → NTDS → Diagnostics. Note: Set '15 Field Engineering' to '5'. This enables Expensive and Inefficient LDAP calls to be logged in Event Viewer.    

View the logs    

Unsecure LDAP binds    

Go to Event Viewer → Filter Directory Service logs to locate the event ID 2889 (Windows Server 2003 to 2012)    

Number of daily unsecure LDAP bind    

Go to Event Viewer → Filter Directory Service logs to locate the event ID 2887 (Windows Server 2003 to 2012)    

Number of LDAP queries    

Go to Event Viewer → Filter Directory Service logs to locate the event ID 1643 (Windows Server 2003 to 2012)    

Recent LDAP queries    

Go to Event Viewer → Filter Directory Service logs to locate the event ID 1644 (Windows Server 2003 to 2012)    

Error from LDAP server    

Go to Event Viewer → Filter Directory Service logs to locate the event ID 1535 (Windows Server 2003 to 2012)    

Time-out LDAP connection    

Go to Event Viewer → Filter Directory Service logs to locate the event ID 1317 (Windows Server 2003 to 2012)    

Hope this helps.

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2023-03-02*

And for Server 2022?
