---
title: "Cross Forest Migration from Exchange 2013 to Exchange 2019 PrepareMoveRequest.ps1 first and then using ADMT to migrate the Sid History"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1074856/cross-forest-migration-from-exchange-2013-to-excha
question_id: 1074856
fetched: 2026-07-25
answer_count: 12
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Cross Forest Migration from Exchange 2013 to Exchange 2019 PrepareMoveRequest.ps1 first and then using ADMT to migrate the Sid History

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1074856/cross-forest-migration-from-exchange-2013-to-excha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Steps completed:    

•	Trusts are in place on Source forest and Target forest    

•	ADMT is installed on the Target DC    

•	MRS Proxy is Enabled on the Source Forest Client Access Server    

•	Admin User of the Target forest is a member of administrators group in the Source forest     

•	Self signed Cert -They have been Exported from the target and imported in source     

•	Password Export Service is Configured and PES service is Started in the Source Domain    

Preparing a Moved a single clark_kent@jaswant  .net from Source forest to Target forest completed    

.\Prepare-MoveRequest.Ps1 -Identity EmailAddress -RemoteForestDomainController FQDN of Source DC -RemoteForestCredential $RemoteCredentials -LocalForestDomainController FQDNofTargetForestDC -LocalForestCredential $LocalCredentials -TargetMailUserOU Distinguished name of OU in TargetForest –UseLocalObject -Verbose    

clark_kent@jaswant  .net is disabled Target forest, I use ADMT to migrate the sid and enable clark_kent@jaswant  .net in target forest, clark_kent@jaswant  .net gets enable, clark_kent@jaswant  .net with sid and password has been moved to target forest.    

Tried to move clark_kent@jaswant  .net maibox to target ex2019a (exchange server 2019) receive an error as below:    

[PS] E:\Program Files\Microsoft\Exchange Server\V15\Scripts>New-MoveRequest -Identity ‘clark_kent@jaswant  .net’ -Remote -Remotehostname ‘exchang1.abc.net’ -RemoteCredential $RemoteCredentials -TargetDeliverydomain ‘abbb.net’    

The target recipient ‘Clark_Kent’ must be a mail-enabled user when the primary mailbox is moving cross forest.    

-  CategoryInfo : InvalidArgument: (clark_kent@jaswant  .net:MailboxOrMailUserIdParameter) [New-MoveRequest], RecipientTaskException    

-  FullyQualifiedErrorId : [Server=EX2019A,RequestId=6c45f065-cd58-4db0-8e27-00f5e91528e7,TimeStamp=11/2/2022 6:54:03 PM] [FailureCategory=Cmdlet    

-RecipientTaskException] 202CD93F,Microsoft.Exchange.Management.Migration.MailboxReplication.MoveRequest.NewMoveRequest    

-  PSComputerName : ex2019a.abbb.net    

Moving Mailbox failed, what should I do to resolve the problem?    

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-15*

@Aholic Liang-MSFT  , here were the output    

VERBOSE: Connected to ex2019a.abc.net.    

[PS] C:\Windows\system32>Get-moverequest    

DisplayName    Status    TargetDatabase    

-----------    

    ------    --------------  

Clark Kent     Completed ex2019a-db1    

[PS] C:\Windows\system32>$dbs = Get-MailboxDatabase    

[PS] C:\Windows\system32>$dbs | foreach {Get-MailboxStatistics -Database $.DistinguishedName} | where {$.DisplayName -eq " clark_kent "} | Format-List DisplayName,Database,DisconnectReason    

[PS] C:\Windows\system32>

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-09*

@Aholic Liang-MSFT   @KurtBMayer       

Unable to recovered the mailbox    

[PS] E:\Program Files\Microsoft\Exchange Server\V15\Scripts>Connect-Mailbox -Identity "clark_kent" -Database ex2019a-db1 -user "clark_kent"    

Mailbox "clark_kent" doesn't exist on database "ex2019a-db1".    

    + CategoryInfo          : NotSpecified: (clark_kent:StoreMailboxIdParameter) [Connect-Mailbox], MdbAdminTaskException  

    + FullyQualifiedErrorId : [Server=EX2019A,RequestId=dc1431e3-c41b-4c0a-a5ec-a986753f53,TimeStamp=11/9/2022 9:50:14 PM] [FailureCategory=Cm  

   dlet-MdbAdminTaskException] 762CA2D5,Microsoft.Exchange.Management.MapiTasks.ConnectMailbox    

    + PSComputerName        : ex2019a.abc.net  

I am going to recover missing this test mailbox,     

I've successfully cross forest migrated few of mailboxes to target Exchange server by using ADMT with no merge.    

I am facing an issue, Outlook client internal network and ActiveSync are not working with error: Outlook automatically configure failed, then "Log onto Exchange ActiveSync mail server (EAS) failed,  only Outlook web is working fine.    

If a mailbox created in target Exchange server (not migrated maibox) everything is working properly, including Outlook, ActiveSync.    

Can anyone help me determine where the issue is for this?     

Thank you in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-04*

@Kai Yao      

@Aholic Liang-MSFT       

The mailbox Clark_Kent@jaswant  .net migrated cross forest moved to target forest Exchange server successfully by ran command to Removed -UseLocallObject or -Verbose parameter as you suggested    

Clark_Kent is in Exchange Admin center while I am test send/receive functional however Clark_Kent is disappearing from Recipients from Exchange Admin Center, now Clark_Kent can send but can' receive mail, It was abled receive when Clark Ken is in Exchange Admin Center    

Any suggestion to fix the issue    

Thank you in advance

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-11-04*

Hi @Happee   ,    

In what order do you perform the migration? Did you run the script called Prepare-MoveRequest.ps1 in the target forest first? And then use the ADMT to migration SID?    

If so, I would suggest you refer to the following command (without –UseLocalObject or-Verbose parameters） to run in the target forest.    

```
./Prepare-MoveRequest.ps1 -Identity  -RemoteForestDomainController  -RemoteForestCredential (Get-Credential SourceForest\Administrator) -LocalForestDomainController  -LocalForestCredential (Get-Credential TargetForest\Administrator) -TargetMailUserOU 
```

Below is a similar thread on how to cross forests migration, and the answerer explains in detail the steps required for the different sequences, hope it can help you!    

Cross-forest mailbox migration with ADMT - Microsoft Q&A    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-03*

@Happee       

See this article for detailed information on the attributes needed for x-forest move. It seems the target account must be mail-enabled before you trigger the move request from the source side.    

prepare-mailboxes-for-cross-forest-move-requests-exchange-2013-help    

Please upvote and accept this thread as answered if it's helpful, thanks!
