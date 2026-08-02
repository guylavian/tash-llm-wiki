---
title: "Exchange Server retrieve email to html or pdf"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/362458/exchange-server-retrieve-email-to-html-or-pdf
question_id: 362458
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Exchange Server retrieve email to html or pdf

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/362458/exchange-server-retrieve-email-to-html-or-pdf (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team,  

Could you help to guide if any api which could retrieve email to html or pdf?  

ps: email including Subject from to cc body attachment  

We have a requirement which need to retrieve the email and save it to pdf purpose for archive.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-20*

What do you actually need in the PDF ? just the body of the Message ? the MIME Content including the attachments ?    

You can use the Graph API to get Body or the Mime Content eg https://learn.microsoft.com/en-us/graph/outlook-get-mime-message
