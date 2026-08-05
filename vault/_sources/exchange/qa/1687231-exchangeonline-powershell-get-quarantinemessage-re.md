---
title: "ExchangeOnline Powershell - Get-QuarantineMessage -ReleaseStatus Requested  no results"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1687231/exchangeonline-powershell-get-quarantinemessage-re
question_id: 1687231
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# ExchangeOnline Powershell - Get-QuarantineMessage -ReleaseStatus Requested  no results

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1687231/exchangeonline-powershell-get-quarantinemessage-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm having a problem running a Get-QuarantineMessage Powershell script for ExchangeOnline in Powershell. My manager is able to run it connecting to the exact same account and get results. When I run it, I just get brought back to the prompt without any output.   

`#user notification area for modules``write-host -foreground yellow "Importing AD Module"`

`Import-Module ActiveDirectory`

`write-host -foreground yellow "Importing ExchangeOnlineManagement Module"`

`Import-Module -Name ExchangeOnlineManagement`

`#connection to exchange online here`

`write-host -foreground yellow "Connecting to ExchangeOnLine"`

`#$corpusername = $env:USERNAME`

`$corpusername = "******@email.com"`

`write-host -foreground yellow "Logging in as $corpusername"`

`Connect-ExchangeOnline -UserPrincipalName $corpusername -ShowBanner:$false -ShowProgress $true`

`#get the quarantined messages with a release status of requested, ignore all others`

`$qmsgs= Get-QuarantineMessage -ReleaseStatus Requested`

What makes it confusing, is that I can run other Get-QuarantineMessage scripts and see results, such as:  

`Get-QuarantineMessage -StartReceivedDate 04/01/2024 -EndReceivedDate 04/30/2024`

What could be the reason that my manager is able to run a script and get results, while I run it and get nothing? We are both successfully connecting to ******@test.com. I have confirmed that there are emails with the release status of requested.   

Thanks

## Answers

_No answers on this thread._
