---
title: "Problem with account blocked in active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4034790/problem-with-account-blocked-in-active-directory
question_id: 4034790
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Problem with account blocked in active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4034790/problem-with-account-blocked-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a problem with several Active Directory accounts. The account on the new computer is blocked at random times (this is not a problem with incorrect password entry).

I was able to check the basic problems and:  

-  the computer has no data saved in the credential manager

-  does not store old login details, e.g. on another device

-  mapped drives using old credentials is not connected 

-  system not using old cached credentials

-  windows Services not using expired credentials 

-  scheduled Tasks not using domain credentials.

I see this message in the event viewer:  

Event ID: 4740

A user account was locked out.

Subject:

```
Security ID:		SYSTEM

Account Name:		XYZ-DC01$

Account Domain:		XY

Logon ID:		0x3E7
```

Account That Was Locked Out:

```
Security ID:		XY\XYZ

Account Name:		XYZ
```

Additional Information:

```
Caller Computer Name:	PR\_XYZ
```

what else can cause a problem with account blocking on a new computer where the only application installed is Office365?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2024-04-29*

Hi, good day! I'm John DeV a Windows user like you and I'll be happy to assist you today.

I want to apologize that this is just a consumer forum for home users. Due to the scope of your question, it is best to ask Active Directory related questions on Microsoft Site Q&A which is a technical community platform where most of the members were IT professionals that would greatly help you with the issue.

Microsoft Site Q&A

https://learn.microsoft.com/en-us/answers/quest...

Kind regards,

John DeV

Independent Advisor
