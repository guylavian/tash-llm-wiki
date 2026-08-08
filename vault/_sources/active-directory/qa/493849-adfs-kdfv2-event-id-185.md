---
title: "ADFS KDFv2 Event-ID: 185"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/493849/adfs-kdfv2-event-id-185
question_id: 493849
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS KDFv2 Event-ID: 185

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/493849/adfs-kdfv2-event-id-185 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello @all  ,    

we gettings the Error Message that KDFv2 are not enabled Event-ID: 185:    

Das KDFv2-Feature ist in der AD FS-Farm nicht aktiviert. Bitte stellen Sie sicher, dass alle Farmknoten mit den neuesten Windows-Updates gepatcht sind und die KDFv2-Funktion aktiviert ist, um die Sicherheit der Farm zu erhöhen. Weiter Informationen darüber finden Sie unter https://go.microsoft.com/fwlink/?linkid=2153807.    

We using ADFS for Passwort Selfservice and i don't know how to solve the Problem?    

Can someone help me?    

many thanks in advanced.    

TheBob

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-12-10*

For anyone that finds this thread - you should enable KDFv2    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/what-is-kdfv2    

If your servers are 2019 or later and fully patched run this on the primary server: Set-AdfsProperties -KdfV2Support enforce    

If your servers are 2016 or earlier or not fully patched then run this on the primary server: Set-AdfsProperties -KdfV2Support enable    

You need to restart ADFS services on all machines afterwards.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-04*

Good Morning piaudonn,  

thank's again for helping!  

Now i have no more adfs error or warning Messages.  

Thank you very much and have a good day!
