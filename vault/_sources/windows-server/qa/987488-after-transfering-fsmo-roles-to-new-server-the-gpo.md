---
title: "After transfering FSMO roles to new server the GPO management app isn't working on the server the FSMO was transferred to"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/987488/after-transfering-fsmo-roles-to-new-server-the-gpo
question_id: 987488
fetched: 2026-07-25
answer_count: 21
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# After transfering FSMO roles to new server the GPO management app isn't working on the server the FSMO was transferred to

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/987488/after-transfering-fsmo-roles-to-new-server-the-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,    

After I transferred FSMO roles from my old Win 2K8 SBS server to the new Win 2019 server I tried to access GPO manager on the new 2019 server but when I do I get this:    

    

    

    

I am logging in to both servers with the same admin account.    

On the old (original) server the FSMO was transferred from the GPO works and opens with no errors.    

Any thoughts on what is going wrong

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-08-31*

Sounds good, not that big of a deal really.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-30*

Should  try on the original server the FSMO roles were transferred from?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-30*

When I run DCDiag I get an error

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-08-30*

Please run;    

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`    

`repadmin /showrepl >C:\repl.txt`    

`ipconfig /all > C:\dc1.txt`    

`ipconfig /all > C:\dc2.txt`    

then put `unzipped` text files up on OneDrive and share a link.
