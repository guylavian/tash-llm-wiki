---
title: "Exchange 2016 cu 19 update failed on Mailbox Service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/304339/exchange-2016-cu-19-update-failed-on-mailbox-servi
question_id: 304339
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2016 cu 19 update failed on Mailbox Service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/304339/exchange-2016-cu-19-update-failed-on-mailbox-servi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Trying to update exchang e2016 server on 2012R2 vmware, single local domain, single exchange serv er. Error at 95% on mailbox service, Hybrid Here is the error:  

3/8 at 2  

Mailbox role: Mailbox service FAILED

The following error was generated when "$error.Clear();  

if  

(!$RoleIsDatacenter -and !$RoleIsDatacenterDedicated)  

{  

$arbUsers =  

@(get-user -Filter {lastname -eq "MSExchApproval  

1f05a927-3be2-4fb9-aa03-b59fe3b56f4c"} -IgnoreDefaultScope -ResultSize 1);  

if  

($arbUsers.Length -ne 0)  

{  

$mbxname = $arbUsers[0].name;  

$mbxs = @(  

get-mailbox -arbitration -Filter {name -eq $mbxname} -IgnoreDefaultScope  

-resultSize 1 );  

if ( $mbxs.length -eq 0)  

{  

$dbs = @(get-MailboxDatabase  

-Server:$RoleFqdnOrName -DomainController $RoleDomainController);  

if  

($dbs.Length -ne 0)  

{  

enable-mailbox -Arbitration -identity $arbUsers[0]  

-database $dbs[0].Identity;  

}  

}  

}  

}  

" was run:  

"Microsoft.Exchange.Data.DataValidationException: ExternalEmailAddress is  

mandatory on MailUser.  

at  

Microsoft.Exchange.Data.Directory.ADDataSession.Save(ADObject instanceToSave,  

IEnumerable`1 properties, Boolean bypassValidation)  

at  

Microsoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.Save(ADReci  

pient  

instanceToSave, String callerFilePath, Int32 callerFileLine, String memberName)

at  

Microsoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.Microsoft.E  

xchange.Data.IConfigDataProvider.Save(IConfigurable  

instance, String callerFilePath, Int32 callerFileLine, String memberName)  

at  

Microsoft.Exchange.Management.RecipientTasks.EnableMailbox.PrepareRecipientObjec  

t(ADUser&  

user)  

at  

Microsoft.Exchange.Management.RecipientTasks.EnableRecipientObjectTask`2.Prepare  

DataObject()

at Microsoft.Exchange.Configuration.Tasks.SetTaskBase`1.InternalValidate()

at  

Microsoft.Exchange.Configuration.Tasks.RecipientObjectActionTask`2.InternalValid  

ate()

at  

Microsoft.Exchange.Management.RecipientTasks.EnableMailbox.InternalValidate()

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at  

Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String  

funcName, Action func, Boolean terminatePipelineIfFailed)".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-10*

Thanks YukiSun. I am working on the PS1 you suggested. Here is the error in EAC  

Server Error in '/ecp' Application.  

Configuration Error Description: An error occurred during the processing of a configuration file required to service this request. Please review the specific error details below and modify your configuration file appropriately.  

Parser Error Message: Could not load file or assembly 'Microsoft.Exchange.Clients.Strings, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.  

Source Error: Line 60: the compiler. All assemblies in the GAC and owa\bin are referenced automatically.Line 61: -->  

Line 62: <add assembly="Microsoft.Exchange.Clients.Strings, Version=15.0.0.0, Culture=neutral, publicKeyToken=31bf3856ad364e35" />  

Line 63: <add assembly="Microsoft.Exchange.Data.Directory, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />  

Line 64: <add assembly="Microsoft.Exchange.Clients.Common, Version=15.0.0.0,Culture=neutral, publicKeyToken=31bf3856ad364e35" />  

Source File: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp\web.config Line: 62 Assembly Load Trace: The following information can be helpful to determine why the assembly 'Microsoft.Exchange.Clients.Strings, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' could not be loaded.  

WRN: Assembly binding logging is turned OFF.To enable assembly bind failure logging, set the registry value [HKLM\Software\Microsoft\Fusion!EnableLog] (DWORD) to 1.  

Note: There is some performance penalty associated with assembly bind failure logging.  

To turn this feature off, remove the registry value [HKLM\Software\Microsoft\Fusion!EnableLog].  

Version Information: Microsoft .NET Framework Version:4.0.30319; ASP.NET Version:4.8.4330.0

ESM error:  

ew-PSSession : [computername.domain.local] Connecting to remote server computername.domain.locall failed with the  

following error message : The WinRM client cannot process the request. It cannot determine the content type of the  

HTTP response from the destination computer. The content type is absent or invalid. For more information, see the  

about_Remote_Troubleshooting Help topic.  

At line:1 char:1  

-  New-PSSession -ConnectionURI "$connectionUri" -ConfigurationName Microsoft.Excha ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin  

gTransportException  

-  FullyQualifiedErrorId : -2144108297,PSSessionOpenFailed  

VERBOSE: Connecting to computername.domain.local.  

New-PSSession : [computername.domain.local Connecting to remote server omputername.domain.local failed with the  

following error message : The WinRM client cannot process the request. It cannot determine the content type of the  

HTTP response from the destination computer. The content type is absent or invalid. For more information, see the  

about_Remote_Troubleshooting Help topic.  

At line:1 char:1  

-  New-PSSession -ConnectionURI "$connectionUri" -ConfigurationName Microsoft.Excha ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin  

gTransportException  

-  FullyQualifiedErrorId : -2144108297,PSSessionOpenFailed  

Failed to connect to an Exchange server in the current site.  

Enter the server FQDN where you want to connect.:

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-09*

Hi @jennylee  ,    

From the error you shared above, it seems that the setup is failing when trying to set properties on the Arbitration Mailbox "MSExchApproval 1f05a927-3be2-4fb9-aa03-b59fe3b56f4c".     

Agree with you that it's worth trying to recreate the arbitration mailboxes and rerun the setup to see how it goes. But before that, personally I'd recommend checking if the homeMDB has been set for the problematic arbitration mailbox:    

-  Open the ADSI edit, connect to “Default naming context”.     

-  Expand and locate the CN=SystemMailbox{1f05a927-2390-47c4-81b3-55dc22299269} under the Users container, right click it and choose Properties, scroll down and find homeMDB parameter. If it hasn't been set, you may copy the homeMDB value from another arbitration mailbox:    

     

If this isn't applicable or doesn't work, then you can go ahead recreating the arbitration mailboxes as mentioned earlier.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
