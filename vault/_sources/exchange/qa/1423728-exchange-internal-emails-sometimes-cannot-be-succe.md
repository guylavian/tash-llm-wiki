---
title: "Exchange internal emails sometimes cannot be successfully sent"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1423728/exchange-internal-emails-sometimes-cannot-be-succe
question_id: 1423728
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange internal emails sometimes cannot be successfully sent

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1423728/exchange-internal-emails-sometimes-cannot-be-succe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The company used the Exchange2019 server, established in the local computer room, without using cloud email, and sent and received emails through Outlook 2016. Sometimes users feedback that sending multiple emails to internal users may result in a return message stating that the delivery of the email to the following recipients or groups failed:

Kevin_ Wang

There is a problem with the recipient's email. Please try sending the email again. If the problem persists, please contact your email administrator.

The following organization has rejected your email: EX2019-1.sgssemi.com.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-13*

Hello Ming

Try removing the autocomplete list and manually entering the recipient's email address to see if that produces any different results.

Also, if you are an administrator, try viewing the message delivery report in the Exchange admin center for more information about message delivery issues.

Please check this： https://learn.microsoft.com/en-us/exchange/mail-flow/non-delivery-reports-and-bounce-messages/non-delivery-reports-and-bounce-messages?view=exchserver-2019

Regards

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
