---
title: "Should any Domain Controller accounts be members of the Protected Users Group?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1274331/should-any-domain-controller-accounts-be-members-o
question_id: 1274331
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Should any Domain Controller accounts be members of the Protected Users Group?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1274331/should-any-domain-controller-accounts-be-members-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Windows Server 2019 Environment.

An auditing tool flagged a finding related to not having certain AD-level objects in the Protected Users Group. I'm suspicious of this finding because in addition to flagging things that are not in the group it also flagged things that demonstrably are.

One of its suggestions was the machine account for one specific Domain Controller, the one which holds all of the FSMO roles. Should this machine account also be in the Protected Users Group? The guidance I have says that one account should be left out in case something goes wrong with Kerberos - I opted to leave one Domain Admin account out for this - which makes me wonder if by adding the FSMO role holder if a Kerberos issue might make things go sideways fast.

## Answers

_No answers on this thread._
