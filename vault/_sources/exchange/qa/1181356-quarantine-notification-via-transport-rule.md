---
title: "Quarantine notification via Transport Rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181356/quarantine-notification-via-transport-rule
question_id: 1181356
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-defender-defender-identity", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# Quarantine notification via Transport Rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181356/quarantine-notification-via-transport-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I work in a SOC and I'd like our team to be notified whenever an employee from a VIP group, has one of their emails quarantined.

I do not know of any way that Defender can do this - currently it only notifies the recipient that their mail has been quarantined. Because of this, I'm now looking down the route of creating a mail flow rule. 

This is the current Quarantine rule that's in place and is functioning ok:

And this is the 2nd rule I'd like to run in unison with the above rule. This rule picks up on the auto-generated mail from postmaster to the employee above - redirects it to our security mailbox to review, and posts them a message to let them know. 

For some reason, the 2nd rule won't run, as if it's disabled. I have read online previously that auto-generated "mails" won't be picked up by transport rules, which may explain it, however I'm not confident of that.  

If anybody has any advice/possible workarounds it'd be much appreciated!

## Answers

_No answers on this thread._
