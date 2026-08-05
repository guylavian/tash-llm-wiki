---
title: "Read Only Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1283723/read-only-domain-controller
question_id: 1283723
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Read Only Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1283723/read-only-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,

I have setup and environment with one Writable Domain Controller with one Readonly Domain Controller. I have created one user for as RODC ADMIN for managing RODC, till now everything is fine. 

Now when I use Administrator Account to login to that RODC it successfully login, and I can easily make some changes in Domain from RODC as well, which should not be like that as it is Ready Only and as per its features. How to overcome this problem.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-14*

At the very top of the dialog you can check what domain controller the MMC is actually connected to.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-13*

In the MMC at top of tree, right-click, Change Domain Controller and check that MMC is connected to the expected domain controller.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
