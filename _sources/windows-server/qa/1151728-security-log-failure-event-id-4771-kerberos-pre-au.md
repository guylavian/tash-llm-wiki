---
title: "Security Log Failure Event ID 4771 Kerberos pre-authentication failed. Mapped Drives not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1151728/security-log-failure-event-id-4771-kerberos-pre-au
question_id: 1151728
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Security Log Failure Event ID 4771 Kerberos pre-authentication failed. Mapped Drives not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1151728/security-log-failure-event-id-4771-kerberos-pre-au (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have someone with a laptop and desktop. Periodically mapped drives will not work. They have a green dot but you cannot expand the list of subfolders, see files, etc. This are DFS shares. If I sign in on the laptop as a different user, everything works. He told me the desktop also does this at times. There are eventid 4771 entries for the user in the event log of the server.    

Account Information:     

```
Security ID:		********************   

Account Name:		***************************
```

Service Information:     

```
Service Name:		krbtgt/**************************
```

Network Information:     

```
Client Address:		::ffff:192.168.*****************  

Client Port:		50607
```

Additional Information:     

```
Ticket Options:		0x40810010   

Failure Code:		0xE   

Pre-Authentication Type:	0
```

Certificate Information:     

```
Certificate Issuer Name:		   

Certificate Serial Number: 	   

Certificate Thumbprint:
```

Additionally, he has seen a box pop up perodically called Windows Login reminder. The problem will go away and the mapped drives will work againImage but always comes back time and time again.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-04*

Hi,    

The following Microsoft link will help you to understand and fix this issue:    

event-4771    

Please don't forget to mark helpful reply as answer
