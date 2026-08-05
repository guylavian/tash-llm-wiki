---
title: "Exchange 2013 - OWA Error due to JavaScript Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1368238/exchange-2013-owa-error-due-to-javascript-issue
question_id: 1368238
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2013 - OWA Error due to JavaScript Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1368238/exchange-2013-owa-error-due-to-javascript-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.

We are using version 15.1 (Build 2375.7) of Exchange 2013.

When you read a specific mail in Exchange OWA, it turns out that there is no body content.

If you print out the content part, it is caused by Javascript as shown below.

[Script declaration part is not annotated, there is no ending (</script>).]

If you look at the contents of other mails without the contents of the mail, it has the same javascript structure,

It seems that you sent these emails through M365.

I am asking if there is a way to control javascript in Exchange ECP or Shell as above.

Thank you.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-15*

Hi partner,  

I don't think there is a way to control javascript in Exchange ECP or Shell. This is not performed by the exchange server.

In addition, Exchange 2013 is no longer supported by Microsoft. It is recommended that you upgrade to a supported version.

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
