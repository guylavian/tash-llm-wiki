---
title: "Get Contacts and Groups from Exchange Online Default Global Address List folder Microsoft Graph API"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1233405/get-contacts-and-groups-from-exchange-online-defau
question_id: 1233405
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-development-routing-development-other", "microsoft-security-ms-graph", "office-exchange-online"]
---
# Get Contacts and Groups from Exchange Online Default Global Address List folder Microsoft Graph API

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1233405/get-contacts-and-groups-from-exchange-online-defau (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to get contacts and groups from the Exchange Online Default Global Address List folder using Microsoft Graph API.
I want to fetch all the data in this folder

I have tried using contacts api but it does not return groups and some contact are also missing

I have also tried using prople api but it does return contacts and groups but it still does not match with Default Global Address List contents

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-14*

Hello Sajid Hussain,

Thanks for reaching out!

As per my research, only contacts found in user mailboxes or the org-wide storage on the Azure AD side are exposed through the Graph API. There is currently no endpoint supported for using Exchange objects or address lists. 

Hope this helps. 

If the answer is helpful, please click Accept Answer and kindly upvote. If you have any further questions about this answer, please click Comment.
