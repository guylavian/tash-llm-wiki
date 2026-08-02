---
title: "when i run the connect-exchangeonline to connect it it should open a authentications window but it gives the error  A window handle must be configured. See https://aka.ms/msal-net-wam#parent-window-handles At C:\\Program Files\\WindowsPowerShell\\Modules\\Exc"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2127369/when-i-run-the-connect-exchangeonline-to-connect-i
question_id: 2127369
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 9
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# when i run the connect-exchangeonline to connect it it should open a authentications window but it gives the error  A window handle must be configured. See https://aka.ms/msal-net-wam#parent-window-handles At C:\Program Files\WindowsPowerShell\Modules\Exc

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2127369/when-i-run-the-connect-exchangeonline-to-connect-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

when i connect-exchangeonline i get this error :  

A window handle must be configured. See https://aka.ms/msal-net-wam#parent-window-handles

At C:\Program Files\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.7.0\netFramework\ExchangeOnlineManag

ement.psm1:751 char:21

- 

```
throw $_.Exception.InnerException;
```

- 

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

-  CategoryInfo          : OperationStopped: (:) [], MsalClientException

-  FullyQualifiedErrorId : A window handle must be configured. See https://aka.ms/msal-net-wam#parent-win 

   dow-handles

## Answer (community) — Q&A User

*upvotes: 39 · updated: 2025-02-04*

Got it up an running again. Just go in your ISE and install the new PowerShell 7.5:  

winget install --id Microsoft.PowerShell --source winget

after that, you are able to connect to exchangeonline again.

## Answer (community) — Q&A User

*upvotes: 6 · updated: 2025-02-27*

Better fix is updating your Powershell, run below in your ISE.  Kudos to Michael Kronschnabl.  

winget install --id Microsoft.PowerShell --source winget

## Answer (community) — Q&A User

*upvotes: 3 · updated: 2025-01-24*

Hello, I've had the same problem and looked into this - I've written everything I found here.  

https://www.centrel-solutions.com/blog/exchange-online-powershell-window-handle-error  

This includes the -DisableWAM parameter that the Connect-ExchangeOnline cmdlet now has.  

Older blog article  

https://david-homer.blogspot.com/2025/01/exchange-online-management-powershell.html

Looks like Microsoft makes it that interactive login windows need a parent window now (so they don't disappear behind your application). They have however used some archaic method to get the console window handle. Therefore if you're not in a console application (for example a .NET or other Windows application, or PowerShell ISE etc etc) there is no console window therefore it crashes. I've reported it on the PowerShell gallery.

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2024-12-06*

I had the exact same issue the other day. I figured it was maybe a "just me" thing because I don't use the module very often and was using it inside a Windows 10 22H2 sandbox.

I posted about the issue on Reddit, see below:

https://old.reddit.com/r/microsoft365/comments/1h6tffz/exchangeonlinemanagement_powershell_module_bug_in/

I don't know the best way to complain about this issue to MS. The best method I figure is to "Contact Owners" in the powershell gallery: https://www.powershellgallery.com/packages/ExchangeOnlineManagement/3.7.0

And just now my coworker made me aware they had the same issue and shared this thread, so adding my couple cents.
