---
title: "PS script deployed via GPO not installing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1689823/ps-script-deployed-via-gpo-not-installing
question_id: 1689823
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
---
# PS script deployed via GPO not installing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1689823/ps-script-deployed-via-gpo-not-installing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello experts,

I could use some help determining why a PS script deployed via Group Policy is not applying.  I suspect it is due to the ExecutionPolicy restriction however I have attempted to bypass in the script parameters as well as adding the bypass to the script itself (Set-ExecutionPolicy Bypass -Confirm:$false -Force).

GPResult shows the server is applying the policy, but the script does not run.
Included in the script is a log output, but no log is saved so I am suspecting the GPO is applying but the script never runs.  The servers are 2019.  Any suggestions?

Thanks,  

Eric

## Answers

_No answers on this thread._
