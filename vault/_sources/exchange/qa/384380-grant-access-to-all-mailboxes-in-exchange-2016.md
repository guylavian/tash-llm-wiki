---
title: "Grant Access to All Mailboxes in Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/384380/grant-access-to-all-mailboxes-in-exchange-2016
question_id: 384380
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Grant Access to All Mailboxes in Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/384380/grant-access-to-all-mailboxes-in-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have inherited an Exchange 2016 infra and I have a requirement for the following:  

-  Grant an Active Directory group read access to all mailboxes (new and existing)  

-  Grant an Active Directory group full access to all mailboxes (new and existing)  

The idea is this is a one off config so new mailboxes don't require anything to be done to them once created and inherit this permission.  

How can I accomplish this? is this setup with Exchange or Active Directory. Any guidance would be much appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-06*

I'm somewhat new to Exchange so excuse my ignorance. The Active Directory group is a security group but no reason it could not be a distribution group if required. We have a 3rd party product that need the read access. I see the user themselves can delegate our read access (at mailbox or mailbox folder/subfolder level) but that is user driven. I guess you are saying the admin can only delegated out SendAs,SendOnBehalf and Full Access at the mailbox level?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-06*

@shockoMS       

Does this "Active Directory group" is an Exchange distribution group?     

What do you mean about "read access" permission? There only exist "Send as", "Send on behalf" and "Full Access" permission in Exchange. For detailed information, you can have a look about this article: Manage permissions for recipients    

Exchange distribution group is a distribution list which used to send emails to multiple mailboxes, there doesn't exist anything in group. There doesnot exist full access permission for a distribution group:    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
