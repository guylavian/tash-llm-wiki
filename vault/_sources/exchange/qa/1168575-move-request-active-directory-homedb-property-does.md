---
title: "Move-Request - Active Directory homeDB property does not support recording in the recipient"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1168575/move-request-active-directory-homedb-property-does
question_id: 1168575
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Move-Request - Active Directory homeDB property does not support recording in the recipient

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1168575/move-request-active-directory-homedb-property-does (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. Hello. I am migrating mailboxes from Exchange 2007 to Exchange 2013 and some mailboxes are getting an error: Move-Request - Active Directory homeDB property does not support recording in the recipient

I found a thread on technet that suggested resetting the permissions in aduc, but that didn't help.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-08*

Please refer to the following steps to check that all servers that are running Exchange Server in the organization are the members of the Exchange Servers and Exchange Trusted Sub Systems role groups.

-  Open Active Directory Users and Computers.

-  Select Microsoft Exchange Security Groups.

-  Select Exchange Servers/Exchange Trusted Sub Systems, select Properties, and then select Members.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-08*

Hi @Андрей Михалевский ,

I am migrating mailboxes from Exchange 2007 to Exchange 2013 and some mailboxes are getting an error:

By "some mailboxes", do you mean it's not affecting all mailboxes?

And regarding "resetting the permissions in aduc", you meant you've set the option to include inheritable permissions from this objects parents, right?  

If this has been tried with no luck, please refer to the steps below to make sure all servers that are running Exchange Server in the organization are the members of the Exchange Servers and Exchange Trusted Sub Systems role groups：

-  Open Active Directory Users and Computers.

-  Select Microsoft Exchange Security Groups.

-  Select Exchange Servers/Exchange Trusted Sub Systems, select Properties, and then select Members.

-  Select Add.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
