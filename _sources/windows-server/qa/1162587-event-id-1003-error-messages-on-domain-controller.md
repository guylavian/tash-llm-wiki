---
title: "event id 1003 error messages on Domain Controller application log"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1162587/event-id-1003-error-messages-on-domain-controller
question_id: 1162587
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# event id 1003 error messages on Domain Controller application log

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1162587/event-id-1003-error-messages-on-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have windows 2012 domain controllers. The event viewer application log is showing event id 1003.  The source is SCeSRV

The message is below.  I do not have the SID in AD. I used powershell and another tool to dump the SIDs.  What can I do to resolve the errors?  Thank you.

Notification of policy change from LSA/SAM has been retried and failed.

Error 4312 to save policy change for account S-1-5-21-1240842779-1673249513-1429243679-19111 in the default GPOs.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-23*

Hi. Thank you for your question and reaching out. I’d be more than happy to help you with your query.

This error could be the result of a device driver program problem, a faulty or inadequate driver, or poor installation of the driver. Examine the RAM dump file that may typically be produced by this event. This will aid in your search for the offending driver.

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.
