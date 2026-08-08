---
title: "powerpoint - disable autocorrect through GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5312635/powerpoint-disable-autocorrect-through-gpo
question_id: 5312635
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# powerpoint - disable autocorrect through GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5312635/powerpoint-disable-autocorrect-through-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In Reference to : Powerpoint - can't disable autocorrect - Microsoft Community

We had an issue trying to disable the autocorrect for a set of machines in an OU through GPO, please find the details below:

The registry value we used to uncheck both these check boxes are as follows:

Windows Registry Editor Version 5.00 

[HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\AutoCorrect] 

"replacetext"=dword:00000000 

[HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\AutoCorrect] 

"Iac"=dword:00000000

please note: this last value is capital "i" not small letter "L"

Posting here for others reference.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-08*

Dear Libin Mathew,

Thank you for sharing your solution to disable autocorrect for PowerPoint through GPO. It's great to see community members helping each other out. For those who may not be familiar with GPO, it stands for Group Policy, which is a feature in Windows that allows administrators to manage user and computer settings centrally.

Sincerely,

Tina | Microsoft Community Moderator
