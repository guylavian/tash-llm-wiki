---
title: "[Migrated from MSDN Exchange Dev]Exchange Server 2016 OnPremise for Mobile Protection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/140635/migrated-from-msdn-exchange-dev-exchange-server-20
question_id: 140635
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]Exchange Server 2016 OnPremise for Mobile Protection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/140635/migrated-from-msdn-exchange-dev-exchange-server-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Non-developer Exchange forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

Exchange Server 2016 OnPremise for Mobile Protection  

[Original post]  

Hi everyone,  

Our company has exchange server 2016 on premise license.  

Few query:-  

i. Is it possible to restrict download email attachment in mobile email is configured, however once user forward the email to their own personal email account, they will be able to open the attachment, anyway to control this?  

ii.Restrict user from sending email to their own self, scenario like user send email from laptop (Outlook) to their own email address, in their mobile email , they can forwarded the email attachment to their personal email, is it able to control this via exchange 2016 on premise licenses?  

Appreciate any feedback on this.  

Thank you!!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-27*

Hi,    

Is it possible to restrict download email attachment in mobile email is configured, however once user forward the email to their own personal email account, they will be able to open the attachment, anyway to control this?    

You can setup a ActiveSyncMailboxPolicy and set the "AttachmentsEnabled" parameter to false,to prevent all users from downloading attachments via mobile phones.    

While,in some posts administrators also find that iphones don't follow this policy and users can still download the attachments.    

If you want to enable the owner to download the attachment only,sorry I don't have ideas of how to do it.    

Restrict user from sending email to their own self, scenario like user send email from laptop (Outlook) to their own email address, in their mobile email , they can forwarded the email attachment to their personal email, is it able to control this via exchange 2016 on premise licenses?    

Appreciate any feedback on this.    

If you want to restrict user from sending email to themselves,I suppose configuring "Message Delivery Restrictions" on their mailboxes via EAC might help.    

You can add their mailboxes to the reject list and there will be a warning like "You don't have permission to send to ..." when the user tries to send emails to himself.    

    

While,in this case forwarded emails would also be rejected,so I don't have ideas of how to let them forward messages to their mailboxes.    

In addtion,I'm not sure if it can be achived via GPO.    

However,it has more to do with active directory.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
