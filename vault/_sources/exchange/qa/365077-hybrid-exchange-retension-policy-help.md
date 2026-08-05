---
title: "hybrid exchange retension policy help"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/365077/hybrid-exchange-retension-policy-help
question_id: 365077
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# hybrid exchange retension policy help

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/365077/hybrid-exchange-retension-policy-help (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello all    

hoping someone might be able to help point me in the right direction.    

so, we have a hybrid exchange setup and want to setup a retention policy to delete anything from the 'Deleted Items' folder older than 90 days.    

to test, i created a retention tag to delete anything over a day old, added that tag to a test retention policy and assigned it to my mailbox.    

when i check in owa i can see a label appear such as:    

    

I've also tested using Start-ManagedFolderAssistant -Identity "xxx" to force the ManagedFolderAssistgant to process the retention policy on the Deleted Items folder.    

This is where my lack of knowledge shows and what i need help with. When i run the above powershell i can see the label above appear on any email in deleted items folder that HASN'T previously been processed.    

What I don't know is what actually does the removal of email? is it the same ManagedFolderAssistgant that not only applies the retention policy but also goes through and says to an email i see you have gone past the date/time in your applied retention policy so i am going to remove you from the folder or is there a separate exchange process that does the actual email removal?    

also, is it a live process that as soon as the date/time is reached the email is removed, or is it a process that runs say once a week and goes through the mailbox?    

hope it makes sense and thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-22*

@tim richards      

Whether are those emails deleted by retention policy now?    

The retention policy will mark the expiration time of emails, but expired emails will not be deleted immediately. There will be a 1~2 days delay before the expired email is deleted. Just wait for it.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-21*

Where is the mailbox located? The MFA runs on a 7day workcycle in Exchange Online, so a "1 day delete" policy is a bit too optimistic :)  

Also, in Exchange Online the Deleted Items tag is ignored in the default policy, you either need to create a new policy and assign the tag, or rename the Default one.
