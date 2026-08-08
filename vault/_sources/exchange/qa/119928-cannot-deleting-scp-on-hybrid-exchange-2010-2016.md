---
title: "Cannot deleting SCP on Hybrid Exchange 2010 & 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/119928/cannot-deleting-scp-on-hybrid-exchange-2010-2016
question_id: 119928
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Cannot deleting SCP on Hybrid Exchange 2010 & 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/119928/cannot-deleting-scp-on-hybrid-exchange-2010-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi I have been removing the Old AutoDiscover SCP on Exchange server 2010 from our Hybrid Environment (Exchange 2010 & Exchange 2016 & Office 365) .

Now if run: set-ClientAccessServer -identity ex2010 -AutoDiscoverServiceInternalUri $null on our new Server 2016 Server, it gave me this error:

You can't make this change because 'CN=EX2010,CN=Servers,CN=Exchange Administrative Group  

(FYDIBOHF23SPDLT),CN=Administrative Groupsxxxxx

=au' is read-only to the current version of  

Exchange.

-    CategoryInfo : InvalidOperation: (:) [Set-ClientAccessServer], CannotModifyCrossVersionObjectException

-    FullyQualifiedErrorId : [Server=ex2016,RequestId=09188cba-c798-42ed-8d28-a89f27ec9438,TimeStamp=7/10/2020 11:38:  

    08 PM] [FailureCategory=Cmdlet-CannotModifyCrossVersionObjectException] C84E4D3D,Microsoft.Exchange.Management.Sys  

    temConfigurationTasks.SetClientAccessServer

-    PSComputerName : ex2016.domainname.edu

Did a bit research, it might be related to Mailbox Anchoring issue. Also someone suggested to move Administrator@keyman   mailbox to the 2016 Server, as I checked, it is already on the new server..

Also, I noticed:

[PS] C:\Windows\system32>Get-Mailbox -Arbitration

Name Alias ServerName ProhibitSendQuota  

SystemMailbox{1f05a927... SystemMailbox{1f0... ex01 Unlimited  

SystemMailbox{e0dc1c29... SystemMailbox{e0d... ex01 Unlimited  

FederatedEmail.4c1f4d8... FederatedEmail.4c... ex01 1 MB (1,048,576 bytes)  

SystemMailbox{bb558c35... SystemMailbox{bb5... mail01 Unlimited  

Migration.8f3e7716-201... Migration.8f3e771... mail01 300 MB (314,572,800 bytes)  

SystemMailbox{D0E409A0... SystemMailbox{D0E... mail01 Unlimited  

SystemMailbox{2CE34405... SystemMailbox{2CE... mail01 Unlimited

What else can I do? Move the three Arbitration mailboxes from Old exchange database to New Exchange Server database? Will it fix the issue of cannot delete SCP connector? Also, it would not have any impact on our hybrid Ex2010 and Ex2016 environment (There are still some disabled User mailboxes on Ex2010) ?

Thanks,  

ML

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-09*

Hi @Lydia Zhou - MSFT      

After moved all three Arbitration Mailboxes to the new database on ex2016, I am still getting this error when I was running: Set-ClientAccessService -identity EX01 -AutoDiscoverServiceInternalUri $null on Ex2016:    

You can't make this change because 'CN=ex2010,CN=Servers,CN=Exchange Administrative Group    

(FYDIBOHF23SPDLT),CN=Administrative Groups,CN=Mercedes,CN=Microsoft    

Exchange,CN=Services,CN=Configuration' is read-only to the current version of    

Exchange.    

    + CategoryInfo          : InvalidOperation: (:) [Set-ClientAccessService], CannotModifyCrossVersionObjectException  

    + FullyQualifiedErrorId : [Server=MAIL01,RequestId=09188cba-c798-42ed-8d28-a89f27ec9438,TimeStamp=9/10/2020 5:28:1  

   7 AM] [FailureCategory=Cmdlet-CannotModifyCrossVersionObjectException] C84E4D3D,Microsoft.Exchange.Management.Syst    

  emConfigurationTasks.SetClientAccessService    

    + PSComputerName        : ex2016.domainname.edu etc  

What else should I try? Run the command on Ex2010?     

ML

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-09*

@Namless Shelter       

Arbitration mailboxes are used for storing different types of system data and for managing messaging approval workflow. When we upgrade from Exchange 2010 to Exchange 2016, it's suggested to move all arbitration mailboxes to Exchange 2016 before moving user mailboxes. Otherwise, some action may not be taken from Exchange 2016.     

As AshokM-8240 mentioned, please move arbitration mailboxes to Exchange 2016, then run the command again.    

Here is a blog about arbitration mailboxes, you can check for more details: Arbitration Mailboxes – Lay of The Land.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-08*

Hi,  

Can you try the below steps and see if that helps,  

-  If admin mailbox is on Exchange 2016, are you able to see both the exchange servers listed in Get-ExchangeServer command from Exchange 2016 EMS  

-  Can you try with a different administrator account by providing the necessary Exchange permissions  

-  Try removing the powershell cookie and see if the resolves it  

-  Move the arbitration mailboxes from Exchange 2010 to 2016   

https://exchangemaster.wordpress.com/2016/01/06/mailbox-anchoring-affecting-new-deployments-upgrades/  

https://blog.rmilne.ca/2016/09/15/when-to-move-arbitration-mailboxes/  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information. Also, export the registry before making any changes and incorrect configuration may lead to other issues.
