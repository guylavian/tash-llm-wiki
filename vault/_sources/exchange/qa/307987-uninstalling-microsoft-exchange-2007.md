---
title: "Uninstalling Microsoft Exchange 2007"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/307987/uninstalling-microsoft-exchange-2007
question_id: 307987
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Uninstalling Microsoft Exchange 2007

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/307987/uninstalling-microsoft-exchange-2007 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,   

I'm having some trouble uninstalling Mircosoft Exchange 2007 having completed a migration to Microsoft 365.   

-  Background -  

I inherited looking after IT for our small business and after a lot of pushing we’ve migrated our email from our in-house server to Microsoft 365 (at last!). The in-house server was Exchange 2007 (V08.03.0485.001) running in a SBS 2008 (SP2) environment. The migration from Exchange 2007 to Microsoft 365 went well following these instructions from Microsoft and our email is now running in 365 and the Exchange 2007 server application is redundant. The final step in the migration instructions is to ‘Decommission on-premises Exchange server(s)’ and gives a link to instructions for Exchange 2007, which links forward to here for the instructions.  Currently we are retaining the SBS2008 server while we finish migrating off it.   

-  Problem -   

Using the Control Panel > Programs & Features > Uninstall option produces the following error:   

Error: Unistall cannot continue. Database ‘Public Folder Database’: Exchange is unable to check the public folder replicas for “SERVER\Second Storage Group\Public Folder Database”. Verify the Microsoft Information Store service is running on SERVER.domain.local, and that the database is properly mounted.   

Services says that the Microsoft Exchange Information Store service is started. The Exchange management console shows in Server Configuration > Mailbox that the Public Folder Database is dismounted. From memory, this database has never been mounted in all the time I’ve been involved. But, when I try to mount it I get the following:  

Microsoft Exchange Error  

Failed to mount database 'Public Folder Database'.  

Public Folder Database  

Failed  

Error:  

Exchange is unable to mount the database that you specified. Specified database: SERVER\Second Storage Group\Public Folder Database; Error code: MapiExceptionCallFailed: Unable to mount database. (hr=0x80004005, ec=-515).   

I’ve run the Database Troubleshooter from the Exchange Management Console Toolbox, which returns the following error:   

Public Folders Container Deleted or Missing Required Attributes.   

One or more MSExchangeIS 9519 Events with error code 0x972 were detected in the Application log.   

Clicking through the ‘how to resolve this issue’ button, the help file suggests using ADSI Edit to check that both the CN=Folder Hierarchies container and that the CN=Public Folders object exists, which they do.   

It then goes on to suggest checking that the msExchOwningPFTreeBL attribute value of the CN=Public Folders object matches the affected Public Folder Store, but msExchOwningPFTreeBL doesn’t exist in the attribute list. I do have msExchPFTreeType, but no other msExch….. attributes.   

Also, the distinguishedName of the CN=Public Folders object (CN=Public Folders,CN=Folder Hierarchies,CN=Exchange Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=First Organization,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=domain,DC=local ) matches the value of  msExchOwningPFTree of the CN=Public Folder Database at CN=Public Folder Database,CN=Second Storage Group,CN=InformationStore,CN=MLSERVER,CN=Servers,CN=Exchange Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=First Organization,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=domain,DC=local  

From what I can tell, I need the database to be mounted before I can uninstall Exchange.    

Any help greatly appreciated!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-25*

Hi @Martin Hale   ,    

Please try to the methods in following article to remove the public folder database. If you remove the public folder successfully, then try to uninstall Exchange server 2007 again.    

Please refer to: How to Remove a Public Folder Database and Removing Public Folder Databases    

For your situation, please run the following command to remove the the service connection point (SCP) value. Then clean the local cached credentials in Windows Credentitals and recreate the Outlook profile.     

```
Get-ClientAccessServer | Set-ClientAccessServer -AutoDiscoverServiceInternalUri $Null
```

In addtion, Although Microsoft does not recommend it, but considering that your environment does not have any data that needs to be retained, you can also try to delete the public file database through ADSI: Remove public folder using ADSIEdit        

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-24*

Hi @Lucas Liu-MSFT  ,     

Apologies for the delay in responding.     

I'm afraid there's nothing more specific in command line.     

    

I have now found the attribute 'msExchOwningPFTreeBL' within the properties of CN=Public Folders - it was hidden by a filter. The attribute value shows as 'CN=Public Folder Database,CN=Second Storage Group,CN=Infortmation Store,CN=SERVERNAME,CN=Servers,CN=Exchange Administrative Group (FYDIBOHF23SDPLT),CN=Administrative Groups,CN=First Organization,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=domainname,DC=local', which i believe is correct.     

    

We have migrated all the data we need out of Exchange 2007 now and into Microsoft 365. The reason I need to uninstall Exchange is that currently, whenever I launch Outlook on any of our Windows 10 desktops, the Outlook application gets stuck in a loop of asking for credentials. If you press cancel, you eventually get the below pop up. I'm assuming this is because there's an entry in the AD on the in house domain server telling outlook to look at Exchange 2007? I'm hoping that correctly uninstalling exchange would resolve this.     

    

Thanks,     

Martin

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Hi @Lucas Liu-MSFT       

Thanks for your suggestions.     

Regarding the first resolution to your first suggestion, The Exchange Server CD is not available. Following the instructions 'How To Prepare Active Directory and Domains' from the help file, command prompt returns the following:    

C:\Users\MLADMIN>setup /PrepareSchema    

Welcome to Microsoft Exchange Server 2007 Unattended Setup    

Preparing Exchange Setup    

Exchange Server setup encountered an error.    

This is also true for 'setup /PrepareLegacyExchangePermissions', 'setup /ps' and 'setup /pl'.     

From the second resolution, 'Domain Controller Security Policy' is not available from my Administrative Tools list. From the Group Policy Management MMC I can see that for the 'Default Domain Controller Policy > Settings> Security Settings> Local Policies/User Rights Assignment > Manage auditing and security log', 'Server Name\Exchange Servers is present.     

Regarding your second suggestion, the CN=Public Folders object does exist at CN=Public Folders,CN=Folder Hierarchies,CN=Exchange Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=First Organization,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=mlexecs,DC=local.     

But: the attribute 'msExchOwningPFTreeBL' does not exist within the properties of CN=Public Folders. Might this be the root of my problems?    

However, the value of the 'distinguishedName' attribute of CN=Public Folders is the same as the value of 'msExchOwningPFTree' attribute of the container CN=Public Folder Database at CN=Public Folder Database,CN=Second Storage Group,CN=InformationStore,CN=MLSERVER,CN=Servers,CN=Exchange Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=First Organization,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=mlexecs,DC=local    

Thanks,     

Martin

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

Hi @Martin Hale   ,    

Is there any data that needs to be retained in your database and on-premises Exchange server?    

Based on the research of the error information you proviede, I found an official article for this error, you can try the solution first to see if you can successfully mount the database.    

For more information: Event ID 9519 and error 0x80004005 when you try to mount a database in Exchange Server    

For the error 0x972 and MSExchangeIS 9519, there are many possibilities for this error. You can try to fix it through the solution provided in the link below.    

For more information: MSExchangeIS 9519 0x972: Public Folders Container Deleted, or Missing Required Attributes    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
