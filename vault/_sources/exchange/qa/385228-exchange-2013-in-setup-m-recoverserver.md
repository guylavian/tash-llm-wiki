---
title: "Exchange 2013 in \"Setup /m:RecoverServer\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/385228/exchange-2013-in-setup-m-recoverserver
question_id: 385228
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2013 in "Setup /m:RecoverServer"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/385228/exchange-2013-in-setup-m-recoverserver (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After recover Exchange 2013 in "Setup /m:RecoverServer" mode, the server does not allow to change any settings or create new mailboxes, giving the same error:

Active Directory operation over DC failed. This error does not allow retry.  

Additional information: You do not have enough permissions to execute the operation.  

Active Directory Reaction: 00002098: SecErr: DSID-03150BC1, problem 4003 (INSUFF_ACCESS_RIGHTS), data 0  

-  CategoryInfo : NotSpecified: (:) [Enable-Mailbox], ADOperationException  

-  FullyQualifiedErrorId : [Server=EMAIL,RequestId=d85a204a-cc37-4819-93de-8b6a46693bd5,TimeStamp=05.05.2021 11:47:  

43] [FailureCategory=Cmdlet-ADOperationException] 268CEFB0,Microsoft.Exchange.Management.RecipientTasks.EnableMail  

box  

-  PSComputerName : email.contoso.com

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-07*

Hi @Юрий Герасимов  ,    

Additional information: You do not have enough permissions to execute the operation.    

Active Directory Reaction: 00002098: SecErr: DSID-03150BC1, problem 4003 (INSUFF_ACCESS_RIGHTS), data 0    

From the error message, it's likely to be a permission issue. By default the built-in administrator have the following permissions, you can have a check at your end and see if any permission is missing:     

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-06*

Check out these    

-  https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/insufficient-access-rights-perform-operation    

-  https://social.technet.microsoft.com/Forums/azure/en-US/6331f602-4a21-43cb-af71-b5b1c4fcb140/active-directory-response-00002098-secerr-dsid03150bb9-problem-4003-insuffaccessrights?forum=exchange2010    

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope
