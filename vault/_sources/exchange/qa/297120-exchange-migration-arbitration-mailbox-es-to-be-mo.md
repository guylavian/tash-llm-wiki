---
title: "Exchange migration - Arbitration mailbox(es) to be moved"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297120/exchange-migration-arbitration-mailbox-es-to-be-mo
question_id: 297120
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange migration - Arbitration mailbox(es) to be moved

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297120/exchange-migration-arbitration-mailbox-es-to-be-mo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I'm upgrading (migrating) my Exchange environment from Exchange 2010 to 2013 (staging migration, until we will have budget for Exchange 2022 licenses next year). I need to move, as stated on both Technet and Deployment Assistant, the System mailbox(es). The question is: which Arbitration/System mailboxes do have to be moved? As per Technet/Deplyment Assistant it is just the one named "SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}", but in many others tutorials it's said to move all the arbitration mailboxes. From my Exchange, by querying for Arbitration mailboxes, I get:    

```
[PS] C:\>Get-Mailbox -Arbitration | fl name, displayname, database, admindisplayversion  
  
  
Name                : SystemMailbox{1f05a927-608a-45a6-bf83-467dc6314b2e}  
DisplayName         : Approvazione guidata di Microsoft Exchange  
Database            : Mailbox Database 1250618726  
AdminDisplayVersion : Version 14.3 (Build 123.4)  
  
Name                : SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}  
DisplayName         : Microsoft Exchange  
Database            : Mailbox Database 1250618726  
AdminDisplayVersion : Version 14.3 (Build 123.4)  
  
Name                : FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042  
DisplayName         : Microsoft Exchange Federation Mailbox  
Database            : Mailbox Database 1250618726  
AdminDisplayVersion : Version 14.3 (Build 123.4)  
  
Name                : SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}  
DisplayName         : Microsoft Exchange  
Database            : Mailbox Database 1 2013  
AdminDisplayVersion : Version 15.0 (Build 1497.2)  
  
Name                : Migration.8f3e7716-2011-43e4-96b1-aba62d229136  
DisplayName         : Microsoft Exchange Migration  
Database            : Mailbox Database 1 2013  
AdminDisplayVersion : Version 15.0 (Build 1497.2)
```

Do I have to migrate just the one reported on Technet or all the arbitration mailboxes as stated on many other places (here and here for example)?    

Thank you,    

Francesco B. B.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-03-04*

Hi, @BK IT Staff       

The function of the arbitration mailboxes is introduced in this document: Recreating arbitration mailboxes    

    

If you only move the arbitration mailbox "SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}", I suppose that later you may run into trouble with migrating mailboxes and OAB generation.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-03-03*

During migration, the sooner you move them the better. Often if arbitration mailboxes are on an older version, some processes handled by the newer version of Exchange may not work so well:  

https://blog.rmilne.ca/2016/09/15/when-to-move-arbitration-mailboxes/  

When To Move  

The above discussion unpacks the history and reason why arbitration mailboxes are often found in the above situation.  However this should not be the case.  

Arbitration mailboxes must be moved at the beginning of the project, before moving user mailboxes onto the new version of Exchange.  It is expected and required that the arbitration mailboxes are moved to the latest version of exchange unless a specific article discusses an issue.  

If you fail to do this simple step, then big issues are heading your way.  They include:  

Administrator actions are not saved to the administrator audit log  

Cannot run E-Discovery searches  

Unified Messaging prompts may not function as expected  

https://blog.rmilne.ca/2018/03/19/arbitration-mailboxes-lay-of-the-land/

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-04*

Thank you all guys, @Kai Yao   and @Andy David - MVP  , for the detailed answers and links (I eagerly read them). I also saved in my boormarks Rhoderick Milne blog. Great!    

I just wonder why Technet doumentation and Exchange Deploy Assistant instruct to move just the "SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}" arbitration mailbox and not  all the arbitration mailboxes. I don't think Microsoft wants customer Exchange installations to get broken. Is there any reason for it?    

Again, thank you!    

Francesco B. B.
