---
title: "ADFS 4 - set REMOTE_USER from value of claim or claim store lookup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/74069/adfs-4-set-remote-user-from-value-of-claim-or-clai
question_id: 74069
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS 4 - set REMOTE_USER from value of claim or claim store lookup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/74069/adfs-4-set-remote-user-from-value-of-claim-or-clai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a web application that does auto-logon using REMOTE_USER http value that maps to a LDAP user of the same name. my issue is that the partner IDP is ADFS and i would like to use ADFS on my side of the trust in front of the web application (SP)  

I need to set the value REMOTE_USER property either in the http headers of the session. the value of the REMOTE_USER should come ideally from the claim or claim lookup value. is this even possible in a claims processing pipeline. any customization or path forward please advise on ideas or solutions.  

i see there is a shibboleth/apache/tomcat way of mapping into a http or environment variable, but i dont want to go learn shibboleth from ground up while i know my way around ADFS a lot more.  

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-25*

You can manipulate incoming claims by using ADFS claims rules and issue custom claims to your applications. The key is to understand the incoming claims provided by ADFS and then use custom rules to issue the desired claims, such as `REMOTE_USER`, for your web application.
