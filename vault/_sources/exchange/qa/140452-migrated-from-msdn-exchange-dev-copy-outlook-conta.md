---
title: "[Migrated from MSDN Exchange Dev] copy outlook contacts from 1 user to 1000 users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/140452/migrated-from-msdn-exchange-dev-copy-outlook-conta
question_id: 140452
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# [Migrated from MSDN Exchange Dev] copy outlook contacts from 1 user to 1000 users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/140452/migrated-from-msdn-exchange-dev-copy-outlook-conta (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange have been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link] copy outlook contacts from 1 user to 1000 users  

[Original post]  

Assuming I have a mailbox with 4 contact folders, these folders have to be exported and imported to 1000 users so they have the same contacts with me.  

It is easy for 1 or 2 users, i could have export and import.  But we are talking about 1000 users. are there any tools out there that can help me on this?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-10-27*

If you need the contacts available by that many users, store them in the GAL. If storing them inside individual mailboxes is a must, you can use EWS/Graph API to copy them between mailboxes programmatically. Or adjust the default permissions so that anyone in the company can access them, as already suggested above.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-27*

Hi,    

are there any tools out there that can help me on this?    

To the best of my knowledge, I am afraid there is no official recommended tool for this requirement. That being said, instead of manually exporting/importing the contact folders, personally I would like to suggest sharing the contact folders with the other users so that all the users can use the same contact folders.     

-  In People, select the contact folder you would like to share, go to Home > Share > Share Contacts.    

-  In the To field, enter the recipients for the sharing invitation message, you can select the checkbox below if you want to grant the recipients with the edit permissions.    

    

If you are going to share the contact folders to all users in the organization, you can right click the folder, go to Properties > Permission, change the permission of "Default":    

    

Here is an official article for your reference: Share a contacts folder with others    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
