---
title: "DL on Exchange Online not being used by on-prem server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/100146/dl-on-exchange-online-not-being-used-by-on-prem-se
question_id: 100146
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# DL on Exchange Online not being used by on-prem server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/100146/dl-on-exchange-online-not-being-used-by-on-prem-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have migrated all DLs/shared mailbox to exchange online, sql team uses a dl to send emails to team when specific alerts are generated.  

Now we have created a DL for them online but when they are trying to configure from SQL server its not working.  

Do i need to create a mail contact on on-prem exchange server? if yes, should the external email address be ******@mydomain.com or ******@mydomain.mail.onmicrosoft.com or ******@mydomain.microsoft.com?  

If the above is not the correct solution then what is missing as they can still use the old dl (was created on-prem and then moved to cloud) from the sql server.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-21*

Hi @Karun Khanna   , agree with the reply above from Andy, please verify whether the DL could receive messages properly from external or on-premise.    

In addition, two ways to migrate DLs in hybrid environment:    

-  Use AADConnect to synchronize the on-premises DLs with AAD so that they appear in the cloud GAL. Note, the groups will have to be managed on-premises because they are "owned" by that environment.    

-  If you want to manage the DLs in cloud,  you can recreate the DLs in the cloud. Then add the members to the group. PowerShell Script to Move Exchange Distribution Groups to the Cloud    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-09-20*

How did you "move" the DLs? Are you still in Exchange Hybrid mode and are there send connectors on-prem that route to 365?    

You don't need a contact necessarily. If the group email address is:    

******@mydomain.mail.onmicrosoft.com and If you have a send connector on-prem that is set for the address space of     

  mydomain.mail.onmicrosoft.com , then all you need to do is have the SQL server alerts go to ******@mydomain.mail.onmicrosoft.com and have the SQL server send to that through the on-prem Exchange Server. Then Exchange will route that to 365 and it should work.     

Important:    

Ensure the  Exchange Online DL (******@mydomain.mail.onmicrosoft.com) allows messages from unauthenticated senders as well:    

https://learn.microsoft.com/en-us/exchange/recipients/distribution-groups?view=exchserver-2019#delivery-management    

Use this section to manage who can send email to this group.    

Only senders inside my organization: Select this option to allow only senders in your organization to send messages to the group. This means that if someone outside of your organization sends an email message to this group, it will be rejected. This is the default setting.    

Senders inside and outside of my organization: Select this option to allow anyone to send messages to the group.    

You can further limit who can send messages to the group by allowing only specific senders to send messages to this group. Click Add Add icon and then select one or more recipients. If you add senders to this list, they are the only ones who can send mail to the group. Mail sent by anyone not in the list will be rejected.    

To remove a person or a group from the list, select them in the list and then click Remove Remove icon.
