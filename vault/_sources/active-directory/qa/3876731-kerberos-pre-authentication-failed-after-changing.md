---
title: "Kerberos pre-authentication failed after changing domain administrator password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3876731/kerberos-pre-authentication-failed-after-changing
question_id: 3876731
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Kerberos pre-authentication failed after changing domain administrator password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3876731/kerberos-pre-authentication-failed-after-changing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Repeated event generation of Kerberos pre-authentication failed with event ID 4771 and failure code 0x18 and the event is generating from multiple instances targeting event source to domain controller.

The issue occurred after change the domain administrator password and unable to dig insides to find the root cause of generation. As since we already update the scheduler service in all member servers. 

 "  Kerberos pre-authentication failed. Account Information: Security ID: S-1-5-21-16834707280-224241925-162353504729-500 Account Name: Administrator Service Information: Service Name: krbtgt/veeamsw.com Network Information: Client Address: ::ffff:172.16.36.3 Client Port: 65280 Additional Information: Ticket Options: 0x40810010 Failure Code: 0x18 Pre-Authentication Type: 2 Certificate Information: Certificate Issuer Name: Certificate Serial Number: Certificate Thumbprint: Certificate information is only provided if a certificate was used for pre-authentication. Pre-authentication types, ticket options and failure codes are defined in RFC 4120. If the ticket was malformed or damaged during transit and could not be decrypted, then many fields in this event might not be present."

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-04-08*

Hi, I am Dave, I will help you with this.

I apologize, Community is just a home user to user consumer forum, due to the scope of your question can you please post this question to our sister forum on Microsoft Q&A (The System Administrates and IT Pro Forum).

Over there you will have access to a host of System Administrators and IT Pro experts and will get a knowledgeable and quick answer to this question.

https://docs.microsoft.com/en-us/answers/index....
