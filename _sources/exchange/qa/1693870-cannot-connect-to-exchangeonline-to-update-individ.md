---
title: "Cannot Connect to ExchangeOnline, to Update Individual Mailbox RulesQuota"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1693870/cannot-connect-to-exchangeonline-to-update-individ
question_id: 1693870
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
---
# Cannot Connect to ExchangeOnline, to Update Individual Mailbox RulesQuota

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1693870/cannot-connect-to-exchangeonline-to-update-individ (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange Gurus -  

Totally lost here.  Recently, I switched to 'New Outlook' on my Windows 11 desktop.  I tried to update Inbox Rules for an existing Inbox Filter.  After trying to Save the additional condition, I get an error message stating Unable to Update Rules, Try again later.  Doing a search in MS KB, it appears I need to update RulesQuota using command:  

Set-Mailbox -Identity ******@msn.com -RulesQuota 256k (since default in KB is 64K)

Now the rabbit hole starts...  

I was able to do the following based on this forum's docs (PS is elevated as Admin):  

C:\Program Files\PowerShell\7> Install-Module -Name PSWSMan  

C:\Program Files\PowerShell\7> Set-ExecutionPolicy RemoteSigned  

C:\Program Files\PowerShell\7> Install-Module -Name ExchangeOnlineManagement  

C:\Program Files\PowerShell\7> Get-InstalledModule ExchangeOnlineManagement | Format-List Name,Version,InstalledLocation  

which returns:    

  Name              : ExchangeOnlineManagement  

  Version           : 3.5.0  

  InstalledLocation : C:\Users\xxxxx\OneDrive\xxxxx Cloud\Documents Cloud\PowerShell\Modules\ExchangeOnlineManagement\3.5.0

Then I tried to connect to the Exchange Online using:  

C:\Program Files\PowerShell\7> Connect-ExchangeOnline

This errors out trying to sign in with my Live Account: (see attached screenshot)

I have no clue where to go from here and appreciate any help available!

Thanks,

Dale Barnes.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-06-10*

Hi Dale,  

Your error indicates that you are trying login ******@msn.com in exchange Online (business) with personal account (personal).
