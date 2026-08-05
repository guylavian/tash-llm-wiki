---
title: "STOP: 0x0000007B at W.S. 2008 R2 domain controller after ransomware infection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1290804/stop-0x0000007b-at-w-s-2008-r2-domain-controller-a
question_id: 1290804
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# STOP: 0x0000007B at W.S. 2008 R2 domain controller after ransomware infection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1290804/stop-0x0000007b-at-w-s-2008-r2-domain-controller-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all!, 

i'm trying to repair a Windows Server 2008 R2 installation after a ransomware infection. The hacker who attaks us deleted all our full machine backups, we can restore our data and databases from cloud backups but we need to replicate our domain controller to a new machine, the problem?, Windows don't start, we get a blue screen: STOP: 0x0000007B. We can't start on Secure Mode, etc. 

There is a way to restore the basic Windows installation or to export the Active Directory data to import it on a new domain controller?.

Thank you!.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-25*

I booted the machine with an Windows Server 2008 R2 ISO and try the StartRep.exe but this is the result.  I have other machines with the same OS, maybe trying to copy the Windows files from there?.

Thank you!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-24*

0x7b usually means a disk controller and or driver issue.    

Might try a Startup Repair.  

https://support.microsoft.com/en-us/topic/you-receive-error-stop-error-code-0x0000007b-inaccessible-boot-device-after-you-install-windows-updates-7cc844e4-4daf-a71c-cd23-f99b50d53e31  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
