---
title: "Moving ADFS to new Server confusion"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/599390/moving-adfs-to-new-server-confusion
question_id: 599390
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Moving ADFS to new Server confusion

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/599390/moving-adfs-to-new-server-confusion (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Moving my ADFS to a new on-prem server.  Followed guidance from Microsoft Support...   

The URL for my adfs is https://adfs.mydomain.net - and it goes there for the login... however, when loggin in, I now get the message   

Sign in  

Sorry, but we’re having trouble signing you in.  

AADSTS50107: The requested federation realm object 'http://mydomain.net/adfs/services/trust/' does not exist.  

Well, yeah - its supposed to be adfs.mydomain.net - what happened and how to fix it?? Only have powershell access...   

( on the new server, already ran :  

connect-msolservice  

Set-MsolADFSContext -Computer My-ADFS-Server.mylocaldomain.local  

Update-MsolFederatedDomain -DomainName mydomain.net  

per Microsoft support)

## Answers

_No answers on this thread._
