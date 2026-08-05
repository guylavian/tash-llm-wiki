---
title: "Best practice to create room mailbox in Exchange Hybrid setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/377085/best-practice-to-create-room-mailbox-in-exchange-h
question_id: 377085
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Best practice to create room mailbox in Exchange Hybrid setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/377085/best-practice-to-create-room-mailbox-in-exchange-h (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I am running Exchange Hybrid setup, Exchange 2019 with Exchange online. All our mailboxes (user\shared\room etc.) are migrated to Exchange online. All the users & room mailboxes has 'IsDirSynced' property value of 'TRUE'. AzureAD connect is in place for AD sync.  

Now I want to cerate new Room Mailbox. Shall I create it in Exchange Online EAC directly or on On-prem Exchange ECP?   

Anybody has some tips about what would be the best practice going forward to create Room\Shared mailbox?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-30*

Hi @prabhash-jena   ,  

1.For the room mailbox. If you don't need to create a remote mailbox or manage it through On-premises Exchange management tools. You can create it directly in Exchange online. If needed, you could create it on-premises Exchange.

2.For the shared mailbox, I recommend that you first create Shared mailbox in on-premises Exchange server. Because of this known issue I found below, if we create a shared mailbox directly in Exchange online, it will may cause the following problems.  

Please refer to: Users in a hybrid deployment can't access a shared mailbox that was created in Exchange Online

1).Users can't open the shared mailbox in Outlook.  

2).Users can't view free/busy information for the shared mailbox.  

3).Users can't send mail to the shared mailbox.

About remote mailbox, please refer to：Enable-RemoteMailbox  

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-29*

You may find this helpful:  

https://answers.microsoft.com/en-us/msoffice/forum/msoffice_o365admin-mso_exchon-mso_o365b/room-mailbox-in-hybrid/ce04b900-5fab-4657-9cba-6bd909f73511
