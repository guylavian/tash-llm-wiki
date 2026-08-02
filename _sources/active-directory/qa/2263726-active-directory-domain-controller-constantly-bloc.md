---
title: "Active directory domain controller constantly blocks some users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2263726/active-directory-domain-controller-constantly-bloc
question_id: 2263726
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Active directory domain controller constantly blocks some users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2263726/active-directory-domain-controller-constantly-bloc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Active Directory is located on 2 servers, both with Windows Server 2016 Standard. And so far only 2 users have encountered this problem.

They use the access normally for approximately 2 or 3 hours and AD automatically blocks the users.

We tried to see if they generated any logs on the local machine or on the server where AD is located, but we were unable to identify any logs of the case.

Thank you in advance for your help.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-08*

Hi Cesar,

There can be multiple sources of account lockouts.

The obvious one, which I assume you have ruled out is that the user is entering the wrong password too many times. 

The other common scenarios include:

-  The user has set up a service or scheduled task under their credentials but not updated after a password change

-  The user has cached their password somewhere (e.g. another machine) and not updated the cache after last password change.

-  Mobile devices.

-  etc.

There are a number of online guides and tools for troubleshooting account lockouts.

Here is one or two examples

https://woshub.com/troubleshooting-identify-source-of-active-directory-account-lockouts/

https://4sysops.com/archives/find-the-source-of-account-lockouts-in-ad/

Good luck
