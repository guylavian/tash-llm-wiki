---
title: "Error on Exchange 2016 reinstall"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/357735/error-on-exchange-2016-reinstall
question_id: 357735
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Error on Exchange 2016 reinstall

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/357735/error-on-exchange-2016-reinstall (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Microsoft's error message are less than helpful most of the time but I am really stumped right now. I am trying to do a re-install after having my exisiting Exchange 2016 server throw error 500 messages when I tried to connect to its management page.

Endstate goal: Migrate from Exchange 2010 to Exchange 2016

Currently I am getting hung up at installing the mailbox role (step 9) with the following error:

[04/14/2021 16:40:14.0358] [2] Active Directory session settings for 'Get-Mailbox' are: View Entire Forest: 'True', Configuration Domain Controller: 'redacteddc.local', Preferred Global Catalog: 'redacteddc.local', Preferred Domain Controllers: '{ redacteddc.local }'  

[04/14/2021 16:40:14.0358] [2] User specified parameters: -Arbitration:'True' -Filter:'name -eq $name' -IgnoreDefaultScope:'True' -ResultSize:'1'  

[04/14/2021 16:40:14.0358] [2] Beginning processing get-mailbox  

[04/14/2021 16:40:14.0379] [2] Searching objects of type "ADMailboxRecipient" with filter "(&((RecipientTypeDetails Equal ArbitrationMailbox)(Name Equal SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9})))", scope "SubTree" under the root "$null".  

[04/14/2021 16:40:14.0382] [2] Request filter in Get Task: (&(!(!(objectClass=user)))(objectCategory=person)(mailNickname=)(msExchHomeServerName=)(msExchRecipientTypeDetails=8388608)(name=SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9})(!(msExchCU=))(|(&(msExchVersion<=2251799813685248)(!(msExchVersion=2251799813685248)))(!(msExchVersion=)))).  

[04/14/2021 16:40:14.0382] [2] Internal Query Filter in Get Task: (&((RecipientTypeDetails Equal ArbitrationMailbox)(Name Equal SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}))).  

[04/14/2021 16:40:14.0395] [2] Previous operation run on global catalog server 'redacteddc.local'.  

[04/14/2021 16:40:14.0395] [2] Preparing to output objects. The maximum size of the result set is "1".  

[04/14/2021 16:40:14.0403] [2] Searching objects "Mailbox Database 1840237472" of type "MailboxDatabase" under the root "$null".  

[04/14/2021 16:40:14.0418] [2] Previous operation run on domain controller 'redacteddc.local '.  

[04/14/2021 16:40:14.0512] [2] [ERROR] Database is mandatory on UserMailbox.  

[04/14/2021 16:40:14.0516] [2] Ending processing get-mailbox  

[04/14/2021 16:40:14.0525] [1] The following 1 error(s) occurred during task execution:  

[04/14/2021 16:40:14.0529] [1] 0. ErrorRecord: Database is mandatory on UserMailbox.  

[04/14/2021 16:40:14.0529] [1] 0. ErrorRecord: Microsoft.Exchange.Data.DataValidationException: Database is mandatory on UserMailbox.

Now, whenever I try to run a get-mailbox command, I get this:

[PS] C:\Windows\system32>Get-Mailbox -Arbitration | ft Name, ServerName, Database -Auto  

Database is mandatory on UserMailbox.  

-  CategoryInfo : NotSpecified: (:) [Get-Mailbox], DataValidationException  

-  FullyQualifiedErrorId : [Server= exchangeservername ,RequestId=327bcf7b-0efa-4065-a1f9-e2f2f7619c6f,TimeStamp=4/14/2021 8:27:29 PM] [FailureCategory=Cmdlet-DataValidationException] C7D089CE,Microsoft.Exchange.Management.RecipientTasks.GetMailbox  

-  PSComputerName : exchangeservername.redacted

I have nowhere to go and I have no idea what to do next, if anybody has an idea what to do or look for I'd appreciate it.

Thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-05*

I hate Exchange.  With a burning passion.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-21*

[04/21/2021 21:26:48.0338] [1] [ERROR] Database is mandatory on UserMailbox.  

[04/21/2021 21:26:48.0339] [1] [ERROR-REFERENCE] Id=MailboxServiceControlLast___34385f18e6894267a2ec43ac827316a5 Component=EXCHANGE14:\Current\Release\PIM Storage\Archive Workflow  

[04/21/2021 21:26:48.0339] [1] Setup is stopping now because of one or more critical errors.  

[04/21/2021 21:26:48.0339] [1] Finished executing component tasks.  

[04/21/2021 21:26:48.0392] [1] Ending processing Install-MailboxRole  

[04/21/2021 21:30:57.0450] [0] CurrentResult setupbase.maincore:396: 0  

[04/21/2021 21:30:57.0450] [0] End of Setup  

[04/21/2021 21:30:57.0451] [0] **********************************************

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-15*

Hi @Dennis Aston   ,    

Good day.    

Do you mean you first uninstalled the Exchange server and then reinstall it on the same machine?    

Please check the ADSI Edit -> Connect to Default Naming Context -> CN=User -> Check the Properties "homeMDB"of the System/DiscoverySearchMailboxes and FederatedEmail, they are system mailboxes, they should be like, if any of them are blank, please copy this value from another system mailbox.    

```
CN=Mailbox Database 1840237472,CN=Databases,CN=Exchange Administrative Group (GUID),CN=Administrative Groups,CN=Contoso,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=domain,DC=com
```

Then restart the MS Exchange Information Store service to test.    

Also if you want a fresh Exchange, you could delete the system mailboxes or everything about Exchange:    

https://www.alitajran.com/how-to-remove-exchange-from-active-directory/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
