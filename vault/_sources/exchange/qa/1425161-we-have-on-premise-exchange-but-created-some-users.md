---
title: "We have on-premise exchange, but created some users directly in Azure Ad so they have an online exchange mailbox.   How do I delete the Online Exchange mailbox for a user that also has an on premise mailbox without deleting the user?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1425161/we-have-on-premise-exchange-but-created-some-users
question_id: 1425161
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# We have on-premise exchange, but created some users directly in Azure Ad so they have an online exchange mailbox.   How do I delete the Online Exchange mailbox for a user that also has an on premise mailbox without deleting the user?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1425161/we-have-on-premise-exchange-but-created-some-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When we originally signed up for Microsoft 365, I created some users directly in Azure AD.    When doing this, it created an online mailbox for those users.   After that point, we implemented AD sync in out hybrid AD environment which created all of the other user accounts in Azure AD.

But now these users I originally created still show that they have an online mailbox, even though all users still user on premise exchange only.

Now I am looking to do a cutover migration to online exchange and am worried that the migration will not work for those who already have the online exchange mailbox setup.  Therefore, I am looking to delete their online mailbox so that Azure AD listed them as still having on premise mailboxes like the rest of our users.

So the questions are 1) is there a way to  delete the online mailboxes that were created and have azure ad list these users as having on premise mailboxes, and 2) is this something I need to worry about when planning a cutover migration?

Thanks,

Jeff

## Answers

_No answers on this thread._
