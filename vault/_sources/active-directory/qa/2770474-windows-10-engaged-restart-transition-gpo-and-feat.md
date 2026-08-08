---
title: "Windows 10 \"Engaged Restart Transition\" GPO and Feature Updates Behavior"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2770474/windows-10-engaged-restart-transition-gpo-and-feat
question_id: 2770474
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 21
qa_tags: []
---
# Windows 10 "Engaged Restart Transition" GPO and Feature Updates Behavior

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2770474/windows-10-engaged-restart-transition-gpo-and-feat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to transition to a GPO/Windows Update for Business update model, but I am frustrated with the behavior of the GPO "Specify engaged restart transition and notification schedule for updates." I have the following configured:

For the normal monthly/security updates, this behaves as expected.

For the "Feature Updates", it doesn't seem to respect the "deadline", and will be constantly waiting for the user to manually run the Feature Update. Is this normal behavior? Do Feature Updates not follow the same "deadline" as quality/security updates?
 Is there a way to force the Feature Updates to install while still maintaining the control/user friendliness of the "engaged restart" GPO?

## Answer (community) — community member

*upvotes: 0 · updated: 2018-02-05*

Due to the scope of your question, it is best you redirect it to the dedicated Group Policy forums on Technet:

Technet forums - Group Policy - Microsoft

https://social.technet.microsoft.com/Forums/ie/...
