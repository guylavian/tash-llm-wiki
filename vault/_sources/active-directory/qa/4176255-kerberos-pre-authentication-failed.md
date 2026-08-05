---
title: "Kerberos pre-authentication failed."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4176255/kerberos-pre-authentication-failed
question_id: 4176255
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: []
---
# Kerberos pre-authentication failed.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4176255/kerberos-pre-authentication-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Kerberos pre-authentication failed.

Account Information:

```
Security ID:		NIACL\33338

Account Name:		33338
```

Service Information:

```
Service Name:		krbtgt/NIACL.CO.IN
```

Network Information:

```
Client Address:		::ffff:10.54.1.188

Client Port:		50207
```

Additional Information:

```
Ticket Options:		0x40810010

Failure Code:		0x12

Pre-Authentication Type:	0
```

Certificate Information:

```
Certificate Issuer Name:		

Certificate Serial Number: 	

Certificate Thumbprint:
```

Certificate information is only provided if a certificate was used for pre-authentication.

Pre-authentication types, ticket options and failure codes are defined in RFC 4120.

If the ticket was malformed or damaged during transit and could not be decrypted, then many fields in this event might not be present.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-16*

Hi there, DMS! I hope you are well. My name is, Zadee. I'm an Independent Advisor and a Microsoft user like you. Sorry to hear about your experience. 

The error mentioned in your title looks like what is also discussed in the article below.

https://learn.microsoft.com/en-us/windows/secur...

If this is an error you are getting within your Windows Server, then it's best to post this to the sister forum MS Q & A as this forum is focused on supporting Consumer Windows Versions. IT professionals that use Windows Servers are in that forum as well and will likely be able to find and answer your query more quickly.

https://learn.microsoft.com/en-us/answers/quest...

Thank you for your understanding.
