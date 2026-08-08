---
title: "MS Graph Exchange with shared mailbox correlation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1411017/ms-graph-exchange-with-shared-mailbox-correlation
question_id: 1411017
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-online"]
---
# MS Graph Exchange with shared mailbox correlation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1411017/ms-graph-exchange-with-shared-mailbox-correlation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are working on an app which fetches all the messages for a particular user in their Mailbox using the MS Graph endpoint.

The mailbox is defined as a user mailbox. When disabling the Exchange license for this user, the endpoint no longer returns a valid response, instead it returns 404 error code, describing that the mailbox is inactive, which is expected behavior.

The interesting part begins when I switch this user's mailbox to a shared mailbox:

After I changes the mailbox for "user1" to a SharedMailbox I disabled the Exchange license:

The fetch getLiceseDetails endpoint returns for this user that the License is disabled:

Now when I try fetching the messages for this user I am getting a good result back with status 200:

How is this possible? The license is disabled and I am able to get back results for this user, but previously when the Mailbox was a UserMailbox type when I disabled the license I got status 404 back.

A few questions that I would kindly ask you to clarify for me please:

-  What is the effect of converting a user mailbox to a SharedMailbox in respect to MS Graph endpoint to fetch user messages?

-  Why does the license being disabled have no effect on a SharedMailbox and the messages endpoint returns data with status code 200 (even if I remove the whole license package I still get back messages)?

-  Since the above bulletpoint works for SharedMailbox, why is for accessing UserMailbox a license required with MS Graph

-  Is it possible for the users to log into their Outlook mail when having a shared mailbox and no licenses attached? According to a few posts online it is possible, user can access its sharedMailbox through outlook without having any licenses active, but I was not able to get this to work, I would receive a status 500 and Microsoft.Exchange.Clients.Owa2.Server.Core.OwaUserHasNoMailboxAndNoLicensesAssignedException. Could you point me to some documentation how to make it possible for the user to sign into his Outlook sharedMailbox type without having any licenses attached?

## Answers

_No answers on this thread._
