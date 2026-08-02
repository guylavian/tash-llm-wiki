---
title: "burflag D4 NTFRS restore, deletes the sysvol contents?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/201468/burflag-d4-ntfrs-restore-deletes-the-sysvol-conten
question_id: 201468
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# burflag D4 NTFRS restore, deletes the sysvol contents?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/201468/burflag-d4-ntfrs-restore-deletes-the-sysvol-conten (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have a customer that still is using 3 Win2008 R2 DCs. All the 3 DCs are getting the 13568 error on event viewer denoting ntfrs issues. We decide to do the burflags D4 / D2 restore procedure (D4 on the PDC emulator, and D2 on the other ones). The question is, does the burflag D4 procedure on the PDC emulator deletes de sysvol content? because it has the master copy and we want it to be replicated to the other DCs.  

thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-17*

Ok, thanks for the references.  

But the question is if when doing the D4 authoritative restore procedure on the DC with the good copy of sysvol, Does the sysvol content be deleted?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-17*

Regardless I'd work through these ones, its the only method to recovery.    

https://learn.microsoft.com/en-us/services-hub/health/remediation-steps-ad/investigate-file-replication-service-frs-journal-wrap-conditions-on-domain-controllers    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/use-burflags-to-reinitialize-frs    

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-17*

3 DCs are the problematics, 3 DCs are reporting NTFRS errors.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-17*

You wouldn't do both at same time. The safer thing is to do the nonauthoritative restore on the problematic one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/use-burflags-to-reinitialize-frs    

https://learn.microsoft.com/en-us/services-hub/health/remediation-steps-ad/investigate-file-replication-service-frs-journal-wrap-conditions-on-domain-controllers    

--please don't forget to Accept as answer if the reply is helpful--
