---
title: "EWS Error \"Access is denied. Only the subscription owner may access the subscription\" Since 01.02.2021"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/255601/ews-error-access-is-denied-only-the-subscription-o
question_id: 255601
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# EWS Error "Access is denied. Only the subscription owner may access the subscription" Since 01.02.2021

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/255601/ews-error-access-is-denied-only-the-subscription-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

we have a problem with EWS subscriptions since 02/01/2021.  

This has worked for many years so far.  

As far as I know, the problem affects all customers who use office365 Exchange.  

We have an Exchange Admin user who has full access to a specific user mailbox.  

With the help of the EWS Managed API (https://github.com/OfficeDev/ews-managed-api) I create a subscription to a user mailbox in order to regularly ask for new emails that have landed in the mailbox.  

When calling GetEvents(), however, the error message "Access is denied. Only the subscription owner may access the subscription" has recently appeared.  

I isolated the problem in C #:  

```
using Microsoft.Exchange.WebServices.Data;
.....
private void btnDummy_Click(object sender, EventArgs e)
        {
            var adminUser = "******@test.com"; //Admin User. Who has full access to user1
            var adminPass = "password"; //Does anyone know what has changed in exchange online recently? Is this just a temporary problem? As I said, it always worked until recently.

## Answers

_No answers on this thread._
