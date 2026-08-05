---
title: "ExchangeOnline Powershell - Get-QuarantineMessage -ReleaseStatus Requested: no results"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1687232/exchangeonline-powershell-get-quarantinemessage-re
question_id: 1687232
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# ExchangeOnline Powershell - Get-QuarantineMessage -ReleaseStatus Requested: no results

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1687232/exchangeonline-powershell-get-quarantinemessage-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm having a problem running a Get-QuarantineMessage Powershell script for ExchangeOnline in Powershell. My manager is able to run it connecting to the exact same account and get results. When I run it, I just get brought back to the prompt without any output.  

What could be the reason that my manager is able to run a script and get results, while I run it and get nothing? We are both successfully connecting to the same email address. I have confirmed that there are emails with the release status of requested. I'm able to run other Get-QuarantineMessage scripts and see results in the same session.     

I'm running Powershell as an Admin and on VPN. I've tried uninstalling and reinstalling ExchangeOnline, disconnecting/reconnecting, and updating.   

Thanks

`#user notification area for modules`

`write-host -foreground yellow "Importing AD Module"`

`Import-Module ActiveDirectory`

`write-host -foreground yellow "Importing ExchangeOnlineManagement Module"`

`Import-Module -Name ExchangeOnlineManagement`

`#connection to exchange online here`

`write-host -foreground yellow "Connecting to ExchangeOnLine"`

`#$corpusername = $env:USERNAME`

`$corpusername = "email address"`

`write-host -foreground yellow "Logging in as $corpusername"`

`Connect-ExchangeOnline -UserPrincipalName $corpusername -ShowBanner:$false -ShowProgress $true`

`#get the quarantined messages with a release status of requested, ignore all others`

`$qmsgs= Get-QuarantineMessage -ReleaseStatus Requested`

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-31*

I see that variable used in only one place: `$qmsgs= Get-QuarantineMessage -ReleaseStatus Requested`, and that's on the left side of an assignment operator. If you run your code as you posted it that variable would still be available. However, if the code you posted is part of a function, the variable would disappear when the code returned to whatever invoked the function.

If you removed the `$qmsgs =` from the code the results of the Get-QuarainteMessage would be sent into the success stream.

So, what's missing here is context. How is the code you posted used?

Just for fun, add this at the end of the code you posted: `$qmsgs.` Then run the code again. Do you see the results you expect?
