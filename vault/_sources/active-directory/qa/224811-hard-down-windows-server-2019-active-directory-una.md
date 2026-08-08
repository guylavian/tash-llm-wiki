---
title: "Hard Down: Windows server 2019 active directory unable to start"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/224811/hard-down-windows-server-2019-active-directory-una
question_id: 224811
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Hard Down: Windows server 2019 active directory unable to start

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/224811/hard-down-windows-server-2019-active-directory-una (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After a DC demotion the domain is no longer available.   

After to run ADSI edit and see the domain  

The response when attempting to start active directory domain services is naming information cannot be located because the specified domain either does not exist or could not be contacted.   

DNS looks clean.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-09*

Something here may help.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

What errors are present in the event log?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-09*

There was not a procedure of FRS - DFS migration    

Does this mean it was already confirmed to be DFS?    

I'd check the Global Catalog is checked

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-09*

What was the OS of demoted domain controller? Had the FRS->DFS migration been performed? Are sysvol and netlogon shares present on new one?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-09*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.
