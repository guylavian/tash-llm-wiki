---
title: "Windows 11 authentication with kerberos trust: date/time difference between client and server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4164631/windows-11-authentication-with-kerberos-trust-date
question_id: 4164631
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Windows 11 authentication with kerberos trust: date/time difference between client and server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4164631/windows-11-authentication-with-kerberos-trust-date (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We operate a kerberos trust between our domain controllers and a Linux-based kerberos KDC for user authentication; users in Active Directory have an altSecurityIdentity field set pointing to "Kerberos:<username>@<REALM>" to authenticate user <username> via the kerberos KDC. We have a significant Linux install base, and this allows us to keep all password authentication in one source.

Windows 11 clients, once joined to our domain, report "There is a time and/or date difference between the client and server." Windows 10 clients and Server 2016/2019/2022 systems authenticate as expected without the time/date error. All are configured to sync clocks from a local NTP server on-site. Time and date, as seen on the desktop or via the "date" and "time" commands. Windows 11 clients do correctly report if the kerberos password is typed incorrectly.

Any idea why Windows 11 is failing these kerberos authentications? It's as if Windows 11 isn't using the same base time when authenticating against our KDCs.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2023-05-09*

Good day John! I am glad to be able to provide assistance to you today. I would suggest to post this query to our neighbor forum from the link belowas this is best suited in there. They are more oriented on with regards to this type queries/issues and there will be IT Pros/System Admins/Server Admins/AD Admins who are available that will be able to fulfill your query as we are more of home/personal consumer based forum.

https://learn.microsoft.com/en-us/answers/quest...

Regards,

Paul R.
