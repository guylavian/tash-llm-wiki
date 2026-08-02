---
title: "How do I list out all Exchange updates installed from PowerShell or CMD?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/300686/how-do-i-list-out-all-exchange-updates-installed-f
question_id: 300686
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How do I list out all Exchange updates installed from PowerShell or CMD?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/300686/how-do-i-list-out-all-exchange-updates-installed-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,  

I'm looking for a way to list out all (or the latest) Exchange installed security updates (can be found in Programs and Features>Installed Updates) via PowerShell or CMD.  

I tried running these commands below but none of them showed me my desired output:  

DISM /online /Get-Packages  

gcm ExSetup.exe | %{$_.FileVersionInfo}  

wmic qfe list brief  

Get-Hotfix  

Appreciate if anyone could point me out to the correct direction.  

Thank you in advance

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-03-06*

https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/exchange-security-update-issues?WT.mc_id=twitter#check-vulnerabilities-and-verify-the-update    

Get-Command Exsetup.exe | ForEach {$_.FileVersionInfo}
