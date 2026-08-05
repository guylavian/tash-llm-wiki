---
title: "Under what circumstances are kerberos tickets created, that are visible in the output of klist.exe"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/749589/under-what-circumstances-are-kerberos-tickets-crea
question_id: 749589
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-print-jobs"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Under what circumstances are kerberos tickets created, that are visible in the output of klist.exe

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/749589/under-what-circumstances-are-kerberos-tickets-crea (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On my Windows 10 laptop, several SMB shares are mapped.  

I also use remote-desktop to access other Windows systems.  

When I execute C:\windows\system32\klist.exe I see several Kerberos tickets.  

I see some tickets with the account of the mapped SMB shares, but not for all mapped SMB shares.

2> Client: eager2learn @ MS-PRINT.LOCAL

```
Server: host/NL-MAIL-PR01.ms-print.local @ MS-PRINT.LOCAL
            KerbTicket Encryption Type: AES-256-CTS-HMAC-SHA1-96
            Ticket Flags 0x40a10000 -> forwardable renewable pre_authent name_canonicalize
            Start Time: 2/23/2022 17:18:42 (local)
            End Time:   2/24/2022 3:18:42 (local)
            Renew Time: 3/11/2022 17:18:18 (local)
            Session Key Type: AES-256-CTS-HMAC-SHA1-96
            Cache Flags: 0
            Kdc Called: DC2017.ms-print.local
```

Under what circumstances are kerberos tickets created?  

Windows itself doesn't have a kinit.exe to create a Kerberos ticket.  

Is it possible to create a kerberos ticket?  

I tried to create a kerberos ticket with ktpass but that give not the right result.

In Java the executable s klist and kinit exist.  

Are the kerberos tickets created with Java kinit a separate set of Kerberos tickets, that can be listed with  

the klist ofm Java and not with the klist of Windows itself?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-03-01*

Moving to Windows-Server-Print as this seems to be print routing related?
