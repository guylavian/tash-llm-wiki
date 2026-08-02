---
title: "GPO problems between 2 DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/811964/gpo-problems-between-2-dc
question_id: 811964
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# GPO problems between 2 DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/811964/gpo-problems-between-2-dc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

we have 2 CD, DC1 and DC2, then there is a PC, I will call it COMPUTER1.   

The initial problem was the following:  

GPO not applying on COMPUTER1  

What I discovered is:  

-  DC1 and DC2 have different files inside SYSVOL/domain/policies, DC1 has all the policies (total 11 policies) and DC2 has only 2 old policies  

-  there are a lot pf DFS errors in the event viewer of both DCs  

-  DC1 is attemping to reach DC2 for replication with errors 5014, 5002, 4612, 5004  

-  DC2 is attempting to reach himself (???) with events 1102, 1104, 6102, 1206  

-  the Windows feature DFS Management is not installed on both DCs  

-  COMPUTER1 when I do a "gpupdate" and he retriever them from DC1, no problem occours but with "gpresult /r" I see that the new policies are not applied  

-  COMPUTER1 when I do a "gpupdate" and he retriever them from DC2, an error about 2 policies that says that "Group Policy processing failed. Cannot read the \XXXXXXX.local \ SysVol \ XXXXXXX.local \ Policies \ {XXXXXXXXX-XXXX-XXX-XXXXX-XXXXX} \ gpt.ini file from a domain controller."  

So now I have some questions:  

If COMPUTER1 is taking updates from DC1, why the policies are not apllying? How can I fix the replication issue in the safer way possile?  

Thank You

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-04-13*

How long has it been happening? If still inside the tomstone period you can try a non authoritative sync  

If you're using older FRS you can follow along here.  

https://support.microsoft.com/en-us/help/290762/using-the-burflags-registry-key-to-reinitialize-file-replication-servi  

or for DFSR follow along here.  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
