---
title: "Data from active directory users and computers[dc.local.xx] is not available from domain controller dc.local.xx because the specified directory service attribute or value does not exist...."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/708934/data-from-active-directory-users-and-computers-dc
question_id: 708934
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Data from active directory users and computers[dc.local.xx] is not available from domain controller dc.local.xx because the specified directory service attribute or value does not exist....

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/708934/data-from-active-directory-users-and-computers-dc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

we are encountering the following issue as shown in the attached screenshot whenever we log in to the domain controller.    

I need your help please as soon as possible

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-01*

Hello Etech-6440,

Thank you for your question.

I just did some testing on my test domain, dsacls doesn't provide the ability to remove a specific ace that has been set. You will need to use ldp to remove the deny permission.

1) If you open ldp connect and link to your ad

2) Select the tree in the view menu and select your default NC

3) In the tree pane right click your domain root and select advanced, security descriptor

4) In the dialog check all nt authority entries/authenticated users to find the deny permission  

When you find the deny permission offensive, delete it and update

This worked on my test domain!

See also the article below that contains useful information:

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/dcpromo-demotion-fails

If the answer is helpful, please upvote and accept it as an answer.
