---
title: "How to properly restore a domain controller and Exchange Server from backup?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1128493/how-to-properly-restore-a-domain-controller-and-ex
question_id: 1128493
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
---
# How to properly restore a domain controller and Exchange Server from backup?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1128493/how-to-properly-restore-a-domain-controller-and-ex (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The environment has 3 domain controllers, one of them is the main one with FSMO roles. It also has Exchange Server 2013.    

Now we are preparing for migrations to Exchange Server 2019 versions and would like to know how to properly roll back a domain controller in case of failure?    

Is it enough to roll back the main domain controller with FSMO roles through the regular backup system Windows Server Backup in authoritative mode?    

Or it is necessary to roll back all domain controllers? Judging by the manual, Exchange stores the configuration on the controller.    

(With the scenario that the old Exch2013 was removed and 2019 installed. After that, it would be necessary to roll back to the 2013 version from a 2-week old backup)

## Answers

_No answers on this thread._
