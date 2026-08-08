---
title: "Exchange 2019 mgmt tools vs. Windows 10"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/351668/exchange-2019-mgmt-tools-vs-windows-10
question_id: 351668
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 mgmt tools vs. Windows 10

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/351668/exchange-2019-mgmt-tools-vs-windows-10 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Running an isolated test environment with restored domain controllers and exchange 2016 CU19 to test bringing in exchange 2019 for a migration.  Exchange was installed earlier this week on 2019 server core.    

Built a new windows 10 20H2 system on that same network and installed the prerequisites but still fails in the readiness checks stating it can't access the registry.  Both the remote registry service and tcp/ip netbios helper services are running.  File/printer sharing are enabled; ran setup elevated with my domain admin account.  No surprise that sfc/dism scans returned no issues since it was just built today.  Firewall profiles are disabled.    

There is a 'more info' link which, of course, takes you to a page that says they haven't added content for that subject yet.    

to take it a step further, the setup log states that it tried to run 'get-exchangeserver' with the identity option as my windows 10 machine and returns the error that it searched for my computer name as type 'server' and the domain controller said the object doesn't exist.  The computer account is fine; i have removed and added back to the domain but didn't make a difference.  also tried running as the domain administrator with the same result.    

anyone get this to work or know why it throws that error?    

    

86369-exchangesetup.log

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-12*

If you have disabled SMB v1, you may suffer this error, please check it with this cmdlet(PowerShell):

1) where is that documented?  

2) what would SMB v1 have anything to do with this? It's insecure and disabled by default; makes no sense how that could be a factor here.

Also run the prerequisite cmdlets on PowerShell:

Already installed the prerequisites it asked for which is only the IIS metabase. I tried the tools on a different 2019 server with a GUI and had the same prerequisites and installed fine there. Don't know why the same thing doesn't work in Windows 10.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-12*

Hi @Seth Simmons   ,    

If you have disabled SMB v1, you may suffer this error, please check it with this cmdlet(PowerShell):    

```
Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
```

You'll could enable it first and try installing.    

```
Enable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
```

How to remove SMB v1    

Also run the prerequisite cmdlets on PowerShell:    

```
Enable-WindowsOptionalFeature -Online -FeatureName IIS-ManagementScriptingTools,IIS-ManagementScriptingTools,IIS-IIS6ManagementCompatibility,IIS-LegacySnapIn,IIS-ManagementConsole,IIS-Metabase,IIS-WebServerManagementTools,IIS-WebServerRole
```

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
