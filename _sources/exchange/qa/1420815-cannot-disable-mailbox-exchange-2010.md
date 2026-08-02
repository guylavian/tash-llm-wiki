---
title: "Cannot disable Mailbox Exchange 2010"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1420815/cannot-disable-mailbox-exchange-2010
question_id: 1420815
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Cannot disable Mailbox Exchange 2010

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1420815/cannot-disable-mailbox-exchange-2010 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello guys,

I have a strange issue with Exchange 2010 S3.

We have migrate all mailbox to exchange online and use Adsync.

Now i need to decomission the old exchange 2010 server.

We have Windows 2008R2 servers (yes i know) with 2008 fonctionnal domain and forest.

When i tried to desactivate a mail box i have this message for all the mailboxes:

"Error: Active Directory operation failed on srvdc1. This error is not retriable. Additional information: The parameter is incorrect. Active directory response: 00000057: LdapErr: DSID-0C090C03, comment: Error in attribute conversion operation, data 0, v1db1 --> The requested attribute does not exist."

And DC just return:

"Internal event: The LDAP server returned an error.

Additional Data

Error value:

00000057: LdapErr: DSID-0C090C03, comment: Error in attribute conversion operation, data 0, v1db1"

When i tried to delete an attribute (blank it wih del touch) i have the same error.

When i tried to delete an attribute with the button "delete" on ad ui, no error.

This is what i have tried:

-  Update Windows

-  Update Exchange

-  Install Exchange tools on a 2012r2 server

-  Add a 2012r2 serveur as ad

-  setup /adprepare and /adschema

Do you have some idea about this?

I think my last move will be to delete Exchange VM and clean traces on ad but i think its not clean.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-10*

Hi @Pierre Brébec ,

He is not in use and i know how to decomission an exchange 2010 server in this case.
Just i cannot proceed as usual because of this error.

Thanks for the clarification. Could you elaborate it a bit more about the time point when the error occurs? Was it triggered by any command?  

I've been searching on the errors you provided earlier and found the article below which includes the similar error messages:

Error when you install Exchange Server: Organization Preparation FAILED  

From the article, we can learn that the error can be solved by changing the value of the lDAPDisplayName attribute to msExchResourceSchema. But seems like this cannot be adapted to your situation because we cannot identify the schema object using the current information included in the errors. Did you by any chance see any additional error message from your end which might help locate the culprit schema object?

If there's no more clues for proceeding, I agree with the "last move" as you mentioned to remove it from AD. Here's an article on steps to removing an Exchange from AD for reference: How to remove Exchange from Active Directory.(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-10*

Hi @Pierre Brébec  ,

When i tried to desactivate a mail box i have this message for all the mailboxes:

I read through the issue description but got a little confused about why you tried to disable mailboxes on Exchange 2010, provided that all mailboxes have already been migrated to Exchange Online. Did I misunderstand anything here?

Now i need to decomission the old exchange 2010 server.

Is this the last Exchange on-premises server in your environment and you are now attempting to decommission it and remove the hybrid deployment? If this is the main task now, it's recommended to follow the instructions in the blog below: Decommissioning your Exchange 2010 servers in a Hybrid Deployment. If your organization is maintaining the hybrid and there are some other Exchange presence on-premises, refer to: Best practices when decommissioning Exchange 2010.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
