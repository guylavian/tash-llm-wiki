---
title: "Exchange 2019 cu12 Exchange Administrative Center does not load correctly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1147071/exchange-2019-cu12-exchange-administrative-center
question_id: 1147071
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 cu12 Exchange Administrative Center does not load correctly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1147071/exchange-2019-cu12-exchange-administrative-center (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2019 cu12 Exchange Administrative Center does not load correctly. I uninstalled CU12 with no change. Everything comes out like its text based and none of the links work.    

    

![275039-eacbfn.png][2]

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-09*

Now when I try to logon it has a spinning circle in the upper left corner that just spins and never times out.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-06*

Nope. I installed cu12 back in October. Installed the latest version over the top last night and now I cant get past the login.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-06*

Hi @Michael Gasparich  ，    

Did you install SU before missing pictures?     

According to this link (Missing images in ECP - Exchange | Microsoft Learn), this issue occurs if the SU is not installed correctly.     

Please reinstall the security update and restart the server to see if there are any changes.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-03*

I did both of the above and I am still having the same issue.
