---
title: "Active DIrectory Replication Status Tool - expired license on install"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/932735/active-directory-replication-status-tool-expired-l
question_id: 932735
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active DIrectory Replication Status Tool - expired license on install

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/932735/active-directory-replication-status-tool-expired-l (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there any fix for the issue of the Active Directory Replication Status Tool having an expired license on a fresh download and install please?   https://www.microsoft.com/en-us/download/details.aspx?id=30005    

I'm getting fed up of trying it every day only to find it isn't fixed.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-19*

and it didn't say this yesterday the last time I looked!!!  Just having another go at the install ...    

Version:    

-  1    

File Name:    

adreplstatusInstaller.msi    

Date Published:    

7/18/2022    

File Size:    

7. 9 MB

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-19*

All I'm seeing is the 7820Kb version :-(  Hopefully that 8140Kb version is the fixed one, but I'm not getting it downloading :-(

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-07-19*

Ok, well I can tell you it showed expired, so I opened a ticket here.    

https://github.com/MicrosoftDocs/feedback/issues/3823    

then today I download and install and it prompts .Net 4.8 is required so I installed 4.8, then after reboot the ADRST worked. Even though there's no update on ticket something has changed (note the file sizes here)    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-19*

Nope ... .Net 4.8 installed - fresh install of the AD tool says 'License Expired' - next idea please?  I'll try anything once !!    

reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full"    

...    

    Version    REG_SZ    4.8.04084

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-07-19*

Should be working but you'll need to have .Net 4.8 as a prerequisite.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
