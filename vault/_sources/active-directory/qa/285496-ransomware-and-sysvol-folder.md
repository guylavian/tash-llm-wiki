---
title: "Ransomware and SYSVOL folder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/285496/ransomware-and-sysvol-folder
question_id: 285496
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Ransomware and SYSVOL folder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/285496/ransomware-and-sysvol-folder (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have an old setup with 4 Domain Controllers 3 Windows Server 2003 and one Windows 2008 R2. Last Week we had a Ransomware attack and it corrupted the SYSVOL folder. I have Recent AD back which I restored in my Lab and copied the clean SYSVOL folder to the existing SYSVOL (deleted the Contents in Sysvol).  

Reference Server is build and changed the Registry value to D4 and all other ADC I did D2 after restarting the ntrs and netlogon I see  

NtFrs_PreExisting___See_EventLog in the SYSVOL, how can I avoid this ?  

https://support.microsoft.com/en-us/help/315457/how-to-rebuild-the-sysvol-tree-and-its-content-in-a-domain

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-02-23*

I'd try the authoritative restore    

https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/use-burflags-to-reinitialize-frs#authoritative-frs-restore    

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-23*

ur right i have used the same link for restore

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-02-23*

Definitely not a good scenario to install exchange on a domain controller. You can follow along here.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/rebuild-sysvol-tree-and-content-in-a-domain    

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-23*

DSpatrick thanks for the answer I have a dc with exchange 2007 installed on it. Again my question is after restore why I see NtFrs_PreExisting___See_EventLog in the SYSVOL

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-02-23*

If you have restored a domain controller from a recent backup then the recommended (and simplest) method is to rebuild the other ones.  

--please don't forget to Accept as answer if the reply is helpful--
