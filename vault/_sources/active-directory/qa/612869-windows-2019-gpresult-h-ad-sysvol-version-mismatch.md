---
title: "Windows 2019 gpresult /h AD / SYSVOL Version Mismatch"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/612869/windows-2019-gpresult-h-ad-sysvol-version-mismatch
question_id: 612869
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Windows 2019 gpresult /h AD / SYSVOL Version Mismatch

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/612869/windows-2019-gpresult-h-ad-sysvol-version-mismatch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.    

I'm trying to understand how to solve this issue: some GPO are not applied to some server due to a AD / SYSVOL Version Mismatch.    

I'm looking for a solution for Windows 2019.    

The only solution I found is about Windows 8.1 or Windows 2012: it's about a fix to install, but I use Windows 2019, not 2012.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-11-02*

Hi @Lorenzo Fongaro      

The error/warning is caused because the versions numbers of the GPT and GPC components of the GPO don't match.  The GPT version number is stored in the AD against the GPO object and the GPC version number is stored in the gpt.ini in the sysvol share.     

Normally as you edit the policy these numbers are incremented and is used to confirm that the GPT and GPC are in sync. For some reason the version number on this policy don't match, hence the warning.    

The easy way to fix this is, is to edit the policy again, by adding and removing a setting, this will cause the version numbers to be updated and should sync the GPT and GPC version numbers.    

Gary.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-02*

Not a lot to go on but you could try a non authoritative synchronization for    

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo    

Also note the two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

--please don't forget to `upvote` and  if the reply is helpful--
