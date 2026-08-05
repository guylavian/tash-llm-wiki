---
title: "Licensing after on-premise migration to Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/156801/licensing-after-on-premise-migration-to-exchange-o
question_id: 156801
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Licensing after on-premise migration to Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/156801/licensing-after-on-premise-migration-to-exchange-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am in the process of migrating from Exchange on-premise to exchange online.  I am setup with a hybrid approach right now and I can successfully migrating mailboxes to Exchange Online.  My question is this, when I tried to add an exchange online license to an account PRIOR to migrating, it created a new primary mailbox for the user in Exchange Online which I did not want.  So, I removed the license THEN migrated the on-premise mailbox to Exchange Online successfully.  I was thinking the license for Exchange Online would be added in the admin portal automatically BUT I still see the user that i migrated without a license for Exchange Online BUT working successfully.    

Is the next step to just add the license to the account?  Will this effect the current mailbox in any way?  Is this the correct process? to not add a license to the user account before migration THEN add it after the mailbox has been migrated to Exchange Online?  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-10*

Hi @dtd646   ,     

Please open a new powershell window to run the below command first, then you will be able to install the module.    

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

    

    

In addition, note that: if you migrate mailboxes in Exchange hybrid, the official document lists that: The Microsoft 365 or Office 365 Exchange license must be assigned only after the migration is complete. You then have 30 days to assign the license.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Seems trivial but not working.  If you run the link you offered:  

PS C:\WINDOWS\system32> Import-Module ExchangeOnlineManagement  

Import-Module : The specified module 'ExchangeOnlineManagement' was not loaded because no valid module file was found  

in any module directory.  

At line:1 char:1  

-  Import-Module ExchangeOnlineManagement  

Which then points you to install the EXO V2 Module.  When I run that, i get this error:  

PS C:\WINDOWS\system32> Install-Module -Name ExchangeOnlineManagement -RequiredVersion 2.0.3  

WARNING: Unable to resolve package source 'https://www.powershellgallery.com/api/v2'.  

PackageManagement\Install-Package : No match was found for the specified search criteria and module name  

'ExchangeOnlineManagement'. Try Get-PSRepository to see all available registered module repositories.  

At C:\Program Files\WindowsPowerShell\Modules\PowerShellGet\1.0.0.1\PSModule.psm1:1809 char:21  

Seems like the process should be easier but maybe I am missing something..

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

As soon as I can get Exchange Online Powershell working I will check that.  Any good articles on how to set that up?  Been trying for a couple hours now with no avail, many errors mostly:  

PS C:\WINDOWS\system32> Install-Module MSOnline  

WARNING: Unable to resolve package source 'https://www.powershellgallery.com/api/v2'.  

This looks correct though:  

PS C:\WINDOWS\system32> Get-PSRepository  

Name                      InstallationPolicy   SourceLocation  

PSGallery                 Untrusted            https://www.powershellgallery.com/api/v2  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Actually, under optional features I found Exchange Hybrid checkbox checked,  Was that the setting you were referring to?  Anything else I should be checking? Any other thoughts on why the AADC wouldn't be syncing that data?  

Had one other thought on this, TLS 1.0 was disabled incorrectly on this server a while back, which was causing some intermittant issues.  Maybe the Hybrid checkbox got enabled BUT not all the settings went through because of the TLS issue?  That issue has since been resolved, would it do anything to uncheck the box and recheck the box?  Or is there something in powershell that I can run to check a setting that isn't working?  

Thanks
