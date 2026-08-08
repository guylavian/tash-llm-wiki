---
title: "On premise Exchange after update to 2019 slow saving drafts in Outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/417725/on-premise-exchange-after-update-to-2019-slow-savi
question_id: 417725
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# On premise Exchange after update to 2019 slow saving drafts in Outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/417725/on-premise-exchange-after-update-to-2019-slow-savi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I've upgraded Exchange 2013 to 2019 and everything seemed fine, but some users (not all, but significant amount) expirienced troubles: when they trying to save a draft of message or create and send a message outside of organization, Outlook window with message became fozen fo a while (15-30 secounds). Inside mail not causing such thing. After that, message sending/saving normally. Somebody can help me with that? What can it be?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-06-02*

Hi @Александр Мольский  ,    

Before going further, what's the version of your Exchange Server 2019 and Outlook clients? Please make sure you have upgraded them all to the latest version.    

when they trying to save a draft of message or create and send a message outside of organization, Outlook window with message became fozen fo a while (15-30 secounds).    

Do you mean that Outlook will be frozen for a while before successfully saving your emails in the Draft folder?    

When this performance issue occurs, are those emails you create and send being stuck in the Outbox folder?    

I noticed you have also mentioned that this kind of performance issue only happens to part of the users. If possible, it is suggested for you to try configuring those problematic email accounts to those normal users' Outlook desktop client and see if the issue has any difference there. You could also try the same operations on the web mail side and see how everything goes there.    

If those problematic email account can work fine on other users' Outlook client or on web mail, I'm afraid that your issue might be more related to your Outlook clients. As I know, there could be some add-ins in your Outlook client that cause this issue, so it is suggested to start your Outlook in safe mode (Press Win + R, type “outlook /safe”, press Enter.) and see if the issue continues. Here is some other troubleshooting methods for Outlook performance issue, please check: Outlook not responding error or Outlook freezes when you open a file or send mail.    

If you have any update about this issue, please feel free to post back.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
