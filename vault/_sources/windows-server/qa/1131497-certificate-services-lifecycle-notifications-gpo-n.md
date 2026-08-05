---
title: "Certificate Services Lifecycle Notifications GPO not working?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1131497/certificate-services-lifecycle-notifications-gpo-n
question_id: 1131497
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Certificate Services Lifecycle Notifications GPO not working?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1131497/certificate-services-lifecycle-notifications-gpo-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

14250.certificate-services-lifecycle-notifications.aspx    

Configured a GPO for Computer and User:    

    

BUT, if I review the settings the configured policies are NOT showing in the computer settings:    

    

HOWEVER, I do see them under user settings:    

    

Same for Group Policy Results and the Local Policies on a server with that policy!    

Tested in on 3 different domains.    

What is going on here?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-16*

I found the registry keys, so I can confirm that the percentage setting is enrolled to the servers.    

HKLM and HKCU registry hives:	SOFTWARE\Policies\Microsoft\Cryptography\AutoEnrollment\    

Keys: OfflineExpirationPercent, OfflineExpirationStoreNames=MY and AEPolicy=7    

So, why do I get event ID 1003 when certificates are on 50% lifetime?
