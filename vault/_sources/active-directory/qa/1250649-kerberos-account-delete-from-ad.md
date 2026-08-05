---
title: "Kerberos account delete from AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1250649/kerberos-account-delete-from-ad
question_id: 1250649
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Kerberos account delete from AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1250649/kerberos-account-delete-from-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

One of my customer deleted Kerberos account from AD and post that RODC replication & login was stopped. But they restored from old backup. The replication and login issue resolved.  after 15 days some RODC servers are getting issue regarding the replication and the tried to share the folder to respective users. But user name not showing in list.
Also Kerberos service is stopped we tried to start the service but failed to start. File share.JPG

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-20*

Verify if krbtgt account exist under users in users and computers.  

What is the error you are getting when trying to start kerberos service?  

You may need to reset krbtgt account password.  

Follow this article to reset krbtgt account password  

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-forest-recovery-resetting-the-krbtgt-password
