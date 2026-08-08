---
title: "How to decommission an on-prem Exchange server in a hybrid config without losing functionality?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1691937/how-to-decommission-an-on-prem-exchange-server-in
question_id: 1691937
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# How to decommission an on-prem Exchange server in a hybrid config without losing functionality?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1691937/how-to-decommission-an-on-prem-exchange-server-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a Windows 2012R2 with an Exchange 2013. We set up everything to a hybrid environment with 365. That was no problem (hybrid configuration wizard).

We also, of course, have an AD sync with 365. We have no ADFS.

We migrated all mailboxes to 365, except some users we don't want at the side of 365. So we are ready to decommission the Exchange on-prem.

But I read this: https://learn.microsoft.com/en-us/exchange/decommission-on-premises-exchange.

We want to keep the AD sync for new users to create on the AD on-prem. But we don't need the Exchange anymore and want to manage all mailbox related management on 365.

We configured the MX records to 365 and not to the Exchange anymore. So there will be no forwarding of messages anymore from on-prem to 365 via the name.mail.onmicrosoft.com.

But, if I'm not wrong, if we remove the Exchange on-prem we will not be able to change the properties of the mailboxes which were migrated in the hybrid environment? Is that correct?

And, you see how old that server is, is there a possiblility we can totally remove that on-prem Exchange without losing the functionality we definitely need in the future, like adding an alias to a mailbox e.g.?

Thanks for your feedback.

Kurt

## Answers

_No answers on this thread._
