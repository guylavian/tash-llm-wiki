---
title: "How to find out which transport rule was applied to an email EXCHANGE ONLINE"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1289675/how-to-find-out-which-transport-rule-was-applied-t
question_id: 1289675
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to find out which transport rule was applied to an email EXCHANGE ONLINE

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1289675/how-to-find-out-which-transport-rule-was-applied-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I have going through all the Microsoft docs. however, I couldn't find anything there!!  

I'd like to know how can I identify which transport rule was applied to a specific email in Exchange Online?  

My 2nd question is related to the picture attached:  

is the Guid mentioned belongs to one of the Exchange Transport rule or it's a miss leading and it's related to the impactful Anti-Spam?

## Answer (community) — Microsoft Moderator

*upvotes: 2 · updated: 2023-05-23*

Hi @It.sam1,

I'd like to know how can I identify which transport rule was applied to a specific email in Exchange Online?

You can check which rule was applied in Exchange Admin Center>Mail flow>Message trace.

Please see the following screenshot:

My 2nd question is related to the picture attached:  

is the Guid mentioned belongs to one of the Exchange Transport rule or it's a miss leading and it's related to the impactful

Based on my test, this field should be in the format like <mail flow rule name>/<guid>.

Please see the screenshot:

While this guid (in my test 51d970e8-5fd5-4949-b863-e8301fd2f76a) does refer to the mail flow rule applied.

You can check a mail flow rule's guid either in Exchange Admin Center or via Exchange Online Powershell.

In Exchange admin Center:

In Exchange Online Powershell:

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
