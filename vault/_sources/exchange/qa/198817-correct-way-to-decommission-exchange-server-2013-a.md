---
title: "Correct way to decommission Exchange Server 2013 after Cutover migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/198817/correct-way-to-decommission-exchange-server-2013-a
question_id: 198817
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-online-server", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Correct way to decommission Exchange Server 2013 after Cutover migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/198817/correct-way-to-decommission-exchange-server-2013-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

First of all, I've found numerous topics and websites on this question, but also found that there are lots solutions which are in conflict with each other. I would like to get clarification on whether I can remove my last Exchange Server 2013 or not. Here's my setup and background:  

-  Cutover migration to O365 Exchange Online done a few weeks ago  

-  All mail flow now in O365  

-  No Hybrid configuration  

-  OnPremise Azure AD Connect in use (users, mailgroups, passwords, machines) (Server 2019)  

-  Onpremise Exchange is not in use anymore (Had also one Edge Server, which is now decommissioned)  

-  I have executed "Set-ClientAccessServer –Identity ServerName -AutoDiscoverServiceInternalUri $null"  

-  Clients cannot sign in to the OnPremise Exchange anymore  

-  Exchange Server Version 15.0 ‎(Build 847.32)‎ SP1  

Now, what I would liked to do, is to cleanly remove my Exchange server without affecting Azure AD Connect syncing. Is there a way to achieve this? I'm not very happy about just shutting it down and leaving it be, because I'm still seeing lots of Exchange related entries in AD Sites and Services. I'm certain that we will not need Onpremise Exchange Server in the future.  

I'm sorry about the possibility of a duplicate question, but I would need some expert advise. Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

Thank you, this has been very helpful.   

I'm going to bother you once more:  

Can I delete all the mailboxes, public folders, mailbox databases? After this I'm planning to run the old exchange as a virtual machine. Or would it be better to clean install a newer version of Exchange for management purposes only?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

@Aki Tuhkanen      

First, under normal circumstances, the Cutover Migration is copy all data from local AD and Exchange on-premises to Exchange online(Create new account and mailbox in Office 365), they are two different organization. So, after coping data, you could uninstall Exchange on-premises directly, it will not affect the Exchange online. Before Cutover Migration, you need to stop the directory synchronization:    

     

However, in your organization, you still using the AAD connector to directory synchronization, the uninstall of Exchange on-premises action will delete mail attributes, then this action may sync to Exchange online.    

So, in this situation, I would suggest you stop directory synchronization first:    

If there doesn't exist issue on Exchange online. You can remove AAD connect first, then uninstall Exchange on-premises, then recreate AAD connect to write AAD account back to local AD.    

If has an issue occur on Exchange online, it means your will cannot uninstall Exchange on-premises directly, you need keep at least one Exchange server to remain the mail attributes.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-15*

Hi,    

You can remove the hybrid configuration but when the identities are synced then atleast one exchange server to be available for management purpose because Azure AD Connect locks the Source Of Authority (SoA) of the objects to your Active Directory.    

When directory synchronization is enabled for a tenant and a user is synchronized from on-premises, most of the attributes cannot be managed from Exchange Online and must be managed from on-premises. This is not due to the hybrid configuration, but it occurs because of directory synchronization. In addition, even if you have directory synchronization in place without running the Hybrid Configuration Wizard, you still cannot manage most of the recipient tasks from the cloud.    

https://learn.microsoft.com/en-us/exchange/troubleshoot/groups-and-distribution-lists/cannot-manage-dg    

https://learn.microsoft.com/en-us/exchange/decommission-on-premises-exchange#why-you-may-not-want-to-decommission-exchange-servers-from-on-premises (Scenario 2)     

"Need to have at least one Exchange Server", I guess I can shut it down? - No, it has to be up and running    

Can I clean up Active Directory somehow? - Not really sure what exactly it means, cleaning up AD objects?    

Can I remove Exchange services I don't need? And how to know which are needed for the Azure AD Connect? - AD connect will synchronize the Exchange attributes  https://learn.microsoft.com/en-us/azure/active-directory/hybrid/reference-connect-sync-attributes-synchronized    

What are the AD-attributes that will be removed if I uninstall Exchange? Could I test removing them from one user and see what happens after the sync? - Uninstalling Exchange will not remove the existing values and attributes, however, you wouldn't be able to make changes to those attributes    

What management tasks are needed to be done in the old server? I can manage my user attributes straight from AD - User attributes such as proxy addresses need to be able to manage those attributes in your Active Directory using Exchange Admin Center (EAC) or Exchange Management Shell (EMS) and also synchronize them to Office 365. Moreover, using other tools such as ADSI Edit to manage your users isn’t supported at the moment.    

If the above suggestion helps, please click on "Accept Answer" and upvote it

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-15*

Hi,    

You need to have at least one Exchange server on-premise when the identities are synced using AADConnect. This exchange server will be used for management purpose.    

https://techcommunity.microsoft.com/t5/exchange-team-blog/decommissioning-your-exchange-2010-servers-in-a-hybrid/ba-p/597185    

https://learn.microsoft.com/en-us/exchange/decommission-on-premises-exchange    

If the above suggestion helps, please click on "Accept Answer" and upvote it
