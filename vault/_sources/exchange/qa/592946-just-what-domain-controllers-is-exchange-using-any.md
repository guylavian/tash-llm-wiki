---
title: "Just what domain controllers is Exchange using anyway?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/592946/just-what-domain-controllers-is-exchange-using-any
question_id: 592946
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Just what domain controllers is Exchange using anyway?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/592946/just-what-domain-controllers-is-exchange-using-any (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can someone help me understand the different output given with these commands from the Exchange PowerShell prompt?    

Get-ExchangeServer    

Get-ADServerSettings    

Get-ADDomainController    

I had to hard code an Exchange server recently to a particular DC and was told by Microsoft to use the "Set-ExchangeServer" CmdLet.  M$ said that I would need to reboot the server before the change would take affect, but I've read elsewhere these settings changes will take affect without a reboot, it just takes a couple of hours.  Does anyone know for sure?    

I ran this for example:    

set-exchangeserver SvrHostName -staticdomaincontrollers DC03.domain.local -staticglobalcatalogs DC03.domain.local -staticconfigdomaincontroller DC03.domain.local    

What is further confusing, if I run a Get-ExchangeServer command, I get output like this.  Note I have not rebooted yet.  Where is my DC03 setting?    

    

And are Get-ADServerSettings and Get-ADDomainController related to the set-ExchangeServer command?  For example, would I run Get-ADServerSettings to see if the command Set-ExchangeServer was completed successfully and applied?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-19*

@Kai Yao  , hi.    

I have two DNS servers in my network adapter, two global directories. But the output is one controller. And you have two. Why so?    

CurrentDomainControllers : {Dattum-dc-01.resoleasing.com}    

CurrentGlobalCatalogs : {Dattum-dc-01.resoleasing.com}    

CurrentConfigDomainController : {Dattum-dc-01.resoleasing.com}
