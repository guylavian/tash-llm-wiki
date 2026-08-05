---
title: "[Migrated from MSDN Exchange Dev] Cmdlet Import-Contactlist into subfolder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/142243/migrated-from-msdn-exchange-dev-cmdlet-import-cont
question_id: 142243
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] Cmdlet Import-Contactlist into subfolder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/142243/migrated-from-msdn-exchange-dev-cmdlet-import-cont (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange has been locked down and transitioned to Microsoft Q&A for support, we manually migrated this thread to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link]Cmdlet Import-Contactlist into subfolder  

[Original post]  

Hi,   

I want use PowerShell to Import contacts to  Outlook.   

The Import-Contactlist cmdlet reads a CSV file into the contacts Folder.  

How can I read into a Subfolder of the Contacts folder (Mailbox)  

thanks, Vlady

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-28*

Hi Vlady,    

To the best of my knowledge, I am afraid it's not feasible to use the Import-Contactlist cmdlet to import contacts into a Subfolder of the Contacts folder of a mailbox.    

As indicated in the parameter explanation section in Import-ContactList, the -Identity parameter specifies the target mailbox, and there is no other parameters available to specify a subfolder path. So the contacts can only be imported into the default Contacts folder of the mailbox.     

That being said, if you would like to import the csv file into a subfolder, it's suggested to use the Outlook client instead which allows you to  select a destination folder. For mode details, you may refer to:    

Import contacts to Outlook    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
