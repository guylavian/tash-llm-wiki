---
title: "Exchange shared mailbox quota warning notification for admin"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1054285/exchange-shared-mailbox-quota-warning-notification
question_id: 1054285
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange shared mailbox quota warning notification for admin

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1054285/exchange-shared-mailbox-quota-warning-notification (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The problem:    

On a hybrid Exchange deployment, we have several shared litigation hold mailboxes. These are mainly used to store messages that we need to hold for a certain period of time and are not viewed by users on a daily basis. Because of this, the mailboxes were filling up because no one could read the message with the quota warning.    

Possible solutions:    

-  I know that we can set up a Mail Flow Rule to forward warnings to the administrator, but it is applied to all mailboxes and there is no way to select only shared mailboxes. Of course, we can use Custom Attribute on shared mailboxes and filter by it but every time a new shared mailbox is created someone has to remember to fill in the custom attribute. So there is a high risk that someone will just forget to fill it in.    

2 We can also use a script and put it in the task scheduler. But we want to avoid the scripts and look for a more "clean" solution.    

-  checking the status of mailboxes in MS Purview. This is still manual, so it is not safe.    

Question:    

Is there another solution using a tools provided by MS to automatically notify exchange administrators when a shared mailbox fills up or reach quota warning?

## Answers

_No answers on this thread._
