---
title: "server 2016 domain controller transfer FMSO rolls"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/427342/server-2016-domain-controller-transfer-fmso-rolls
question_id: 427342
fetched: 2026-07-25
answer_count: 14
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# server 2016 domain controller transfer FMSO rolls

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/427342/server-2016-domain-controller-transfer-fmso-rolls (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Needing to move an old 2008 R2 DC to new 2016 standard.  

We have 2, DC's.   

DC1 - 2008 R2  

DC2 - 2012 R2  

Made a new DC 2016 Standard, fully licensed, installed roles and features, added to domain.  

Needing to move all FSMO roles to 2016 DC. Issue is, when attempting to use the Snap-In for AD Schema or other Snap-ins to move the roles, when needing to select the new DC, it is not in the list of servers. It is only showing the current 2 we have.  

When attempting to do this through the Run > ntdsutil , when entering the new DC name to connect too to transfer the rolls, I am getting a Syntex error.   

When I look at the AD settings, I see all 2 DC listed, the new DC has the AD forest and fully populated. Can login with my domain user account. My account is a member of Enterprise Admins and Schema Admins.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-08*

Do you want me to share the file directly with you?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-08*

Check the C:\ for the new files.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-08*

Nothing happened on any of the DC's when running the first two commands in CMD

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-08*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.
