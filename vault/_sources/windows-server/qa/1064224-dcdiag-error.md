---
title: "DCDIAG error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1064224/dcdiag-error
question_id: 1064224
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# DCDIAG error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1064224/dcdiag-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm preparing to migrate our 2012 R2 DC's sysvol from FRS to DFSR and when I run DCDIAG I'm getting the errors in the attached screenshot.  Since DFSR is not in use currently I'm unsure what this error means and/or if it needs to be resolved prior to migrating.  I checked KB Q312862 and it seems unapplicable

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-10-26*

Probably is Ok, read on here.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/dcdiag-verifyreferences-test-fails    

also check the FRS Replication and System event logs for errors    

or also put up the files here and I'll take a look    

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`    

`repadmin /showrepl >C:\repl.txt`    

`ipconfig /all > C:\dc1.txt`    

`ipconfig /all > C:\dc2.txt`    

`ipconfig /all > C:\dc3.txt`    

then put `unzipped` text files up on OneDrive and share a link.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
