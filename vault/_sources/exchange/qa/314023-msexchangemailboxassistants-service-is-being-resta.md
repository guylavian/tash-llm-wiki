---
title: "msexchangemailboxassistants service is being restarted"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/314023/msexchangemailboxassistants-service-is-being-resta
question_id: 314023
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# msexchangemailboxassistants service is being restarted

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/314023/msexchangemailboxassistants-service-is-being-resta (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have the single server Exchange 2019 CU 8. There is clean installing, isn't migration. Auto-acceptance of resource groups is not work. The msexchangemailboxassistants service starts and stops immediately. Errors 4999 in logs Watson report about to be sent for process id: 16676, with parameters: E1211S, c-RTL-AMD64, 15.02.0792.010, MSExchangeMailboxAssistants, M.Exchange.Assistants, M.E.A.AssistantsRpcServer.RegisterAssistant, SystemArgumentException, 503a-dumptidset, 15.02.0792.010. ErrorReportingEnabled: False And error 7031 The Microsoft Exchange Mailbox Assistant service terminated unexpectedly. This happened once. The next corrective action will be taken after 5000 msec: Restart the service. We need some advices about this problem. Thx.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-04-09*

Hi! I made a second server. Made DAG, replicated bases, deformed DAG. Removed the first server. Now there are no problems.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-19*

Yes, the exploit detected in the Exchange server made me stay awake for several nights, over the past 2 weeks I've installed KB5000871 on many servers.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-18*

Hi Lou!  

When I enter the command Stop-ManagedFolderAssistant, I see a message that the mailbox service is not running on the server. Error from RPC 1753.  

I have full control to the V15 folder.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-16*

Hello Lou!  

The service msexchangemailboxassistants does not have time to use 2GB because it restarts.  

I've already tried changing MFA cycles and moving the arbitration box, but it didn't help.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-16*

Hi @AndreyDataFort   ,    

When this happens, will it cause the high CPU or RAM occupancy? Please check it first.     

MSExchangeMailboxAssistants service crashes when memory usage exceeds 2 GB    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

And also please try this cmdlet to stop the MFA service and check if the Mailbox Assistant stops crashing.    

```
Stop-ManagedFolderAssistant
```

If this could work, you can change the MFA workcycle by     

```
New-SettingOverride -Name "MFA WorkCycle Override" -Component TimeBasedAssistants -Section ELCAssistant -Parameters @("WorkCycle=7.00:00:00") -Reason "Process mailboxes every 7 days"
```

Then apply this setting to Exchange servers.    

```
Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -Component VariantConfiguration -Argument Refresh
```

You can find all the processes here: Configure and run the Managed Folder Assistant in Exchange Server    

Otherwise, you could try to move the arbitration mailboxes to another database.    

Move arbitration mailboxes in Exchange Server    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
