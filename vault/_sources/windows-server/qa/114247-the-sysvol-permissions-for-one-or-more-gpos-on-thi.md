---
title: "The sysvol permissions for one or more GPOs on this domain controller are not in sync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/114247/the-sysvol-permissions-for-one-or-more-gpos-on-thi
question_id: 114247
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# The sysvol permissions for one or more GPOs on this domain controller are not in sync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/114247/the-sysvol-permissions-for-one-or-more-gpos-on-thi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I stood up 4 new domain controllers and it looked as if everything was happy.  Dcdiag shows no issues, repadmin shows no issuss, etc.  However, I ran an infrastructure report from the GPMC and it shows my new domain controllers are all with replication in progress.  When I click the ACLs link, it lists maybe 20 of my 25 GPOs and says at the top:  

"The SysVol permissions for one or more GPOs on this domain controller are not in sync with permissions for the GPOs on the Baseline domain controller."  

I checked the permissions and they seem to match.  Any ideas on what I can do next?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-01*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

`ipconfig /all > C:\dc4.txt`  

then put `unzipped` text files up on OneDrive and share a link.
