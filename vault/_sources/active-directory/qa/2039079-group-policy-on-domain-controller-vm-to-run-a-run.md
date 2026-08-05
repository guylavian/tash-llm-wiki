---
title: "Group policy on domain controller VM, to run a run command"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2039079/group-policy-on-domain-controller-vm-to-run-a-run
question_id: 2039079
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
---
# Group policy on domain controller VM, to run a run command

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2039079/group-policy-on-domain-controller-vm-to-run-a-run (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have 58 vms all on the same domain, I require to run a specific command on each of those vms

However instead of doing it one by one, I'm aware I can do a Group policy on domain controller VM, to run the command to all the vms at one go.

However i haven't done this before and documentation I've used hasn't helped me.

Could i get a step by step guide on how to do it? 

script is 

```
Set-MpPreference -EnableNetworkProtection Enabled
Set-MpPreference -AllowNetworkProtectionOnWinServer 1
Set-MpPreference -AllowNetworkProtectionDownLevel 1
Set-MpPreference -AllowDatagramProcessingOnWinServer 1
```

## Answers

_No answers on this thread._
