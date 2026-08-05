---
title: "Connecting to Exchange powershell locally"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/256812/connecting-to-exchange-powershell-locally
question_id: 256812
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Connecting to Exchange powershell locally

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/256812/connecting-to-exchange-powershell-locally (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey guys,  

I'm in charge to restore some mails from an Exchange Server 2013 queue. Our customer had an cyber security incident and we had to restore a lot of systems. Meanwhile he migrated to Exchange Online. But now the lost mails in the Exchange Server queues are getting important.  

I already have restored the mails from the Edge servers in the DMZ (without domain membership), but now I have to restore the mails from the main database servers. It does not really work well restoring the whole transport and database servers including domain controllers in a new isolated VM network.  

So I asked myself if it would be possible to start the Exchange powershell without all the domain dependencies.  

When I start the Exchange powershell I get the error "Failed to connect to an Exchange server in the current site."  

Is it possible to get the powershell running without connecting to a domain?  

Thanks for your help.  

Kind regards,  

woelki

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-02-03*

It's unlikely. Everything related to Exchange is in the Active Directory. Maybe the Exchange folks know something I've forgotten, but I was an Exchange server MVP for more than 16 years before I retired.  

PowerShell will run without access to the AD, but none of the Exchange stuff will

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-04*

Hi there,  

I guess so. I have some experience in Exchange On-Premises as well, but I hope there is somebody knowing more than me.  

Then let's try getting those DC's up and running. Wish me luck.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-04*

Hi @Christian Wölk  ,    

Is it possible to get the powershell running without connecting to a domain?    

Exchange stores and retrieves information in Active Directory, so if the domain controllers are dead, I'm afraid it's not feasible to run Exchange powershell.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
