---
title: "Exchange Online Retention Policy Exclusion Folder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1406518/exchange-online-retention-policy-exclusion-folder
question_id: 1406518
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online Retention Policy Exclusion Folder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1406518/exchange-online-retention-policy-exclusion-folder (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We want to implement an email retention policy of 2 years but want to provide a folder named "Exempt" for employees to store emails in that is exempt from the retention policy - meaning, if I put an email in that folder, it will remain indefinitely and not be auto-deleted by the Retention Policy. Is this possible? If so, where are instructions to do it via the GUI (I don't know PowerShell)? I see lots and lots of documentation but nothing specific to this scenario.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-30*

Hello @Julie Johnson  

You need to use personal tags (Never Delete) here.

More details: https://learn.microsoft.com/en-us/exchange/security-and-compliance/messaging-records-management/retention-tags-and-policies#more-about-personal-tags

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
