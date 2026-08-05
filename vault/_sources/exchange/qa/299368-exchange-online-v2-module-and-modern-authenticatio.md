---
title: "Exchange online V2 Module and Modern authentication  EXO V2 But only Get-?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299368/exchange-online-v2-module-and-modern-authenticatio
question_id: 299368
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange online V2 Module and Modern authentication  EXO V2 But only Get-?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299368/exchange-online-v2-module-and-modern-authenticatio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We want to execute some tasks  (non-interactive)  as service account, ( against Microsoft Exchange such as Created Achieve Mailbox, Created Shared Mailbox,  this looks like we do not have to use basic authentication with Connect-ExchangeOnline as this is deprecated, and we have to use EXO V2 module with modern authentication.  

When we read and see what we can do with EXO V2 module, it only has very few  Get- operations available not all  the Set- operations which works with old Connect-ExchangeOnline   module, so we are bit confused what to use then?  

any best practices?  

Our best runtime options are  Azure functions as preferable if thats possible to run it from there.  

/Maqsood.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-05*

Hi,    

I've tried connecting to Exchange Online PowerShell V2 module using modern authentication and the commands work for me.    

What error did you meet?    

Reference steps: Connect to Exchange Online PowerShell using modern authentication    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-04*

As far as I know they are not exposed right now outside of the ExO module. - Perhaps in the future.  

But all those commands can be run with V2 module.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-04*

@Andy David - MVP   command that we want to execute non - interactively     

Enable-Mailbox -Identity <username> -Archive    

Set-Mailbox "Dan Jump" -EmailAddresses @{add="******@northamerica.contoso.com"}    

New-Mailbox -Shared -Name "Sales Department" -DisplayName "Sales Department" -Alias Sales |     

Set-Mailbox -GrantSendOnBehalfTo MarketingSG | Add-MailboxPermission -User MarketingSG -AccessRights FullAccess -InheritanceType All    

as we understand EXO V2 is backed by new REST API, do you know if the above functions are exposed in the REST API? (we can call the REST API) directly if these are available.    

https://outlook.office.com/adminApi/beta/xxxxxxxx-352a-4eda-bece-09d0684d0cfb/Mailbox    

/Maqsood

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-04*

Which specific commands are you referring to? They are all available using Connect-ExchangeOnline
