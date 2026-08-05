---
title: "Can't Use Enable-Mailbox on Powershell ExchangeOnlineManagement"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1011962/cant-use-enable-mailbox-on-powershell-exchangeonli
question_id: 1011962
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Can't Use Enable-Mailbox on Powershell ExchangeOnlineManagement

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1011962/cant-use-enable-mailbox-on-powershell-exchangeonli (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I already enable auto expanding for my organizations/tenant, but if this configuration enabled, will make all user in my organization using auto-expanding archiving. (documentation: https://learn.microsoft.com/en-us/microsoft-365/compliance/enable-autoexpanding-archiving?view=o365-worldwide)    

    

Then I want to restrict auto-expanding archiving for specific user. As per information in documentation, i need to run this command in PowerShell:    

Enable-Mailbox <user mailbox> -AutoExpandingArchive    

But I'm getting error Enable-Mailbox : The term 'Enable-Mailbox' is not recognized as the name of a cmdlet, function, script file, or operable program.    

    

I'm using  ExchangeOnlineManagement version 2.0.5 .    

    

License Office version: Office 365 E5     

i can use command Connect-ExchangeOnline, Get-EXOMailbox and other, but why i can't use command Enable-Mailbox .    

Please advice.    

Thank you.

## Answers

_No answers on this thread._
