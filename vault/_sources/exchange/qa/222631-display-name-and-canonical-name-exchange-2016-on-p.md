---
title: "\"Display Name\" and Canonical Name (Exchange 2016 On-Premise)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/222631/display-name-and-canonical-name-exchange-2016-on-p
question_id: 222631
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# "Display Name" and Canonical Name (Exchange 2016 On-Premise)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/222631/display-name-and-canonical-name-exchange-2016-on-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We wish to have a different "Display Name" to the Canonical Name for Resource and Shared mailboxes. This can be done easily using PowerShell but not all admins are able to use it and instead will use the "Exchange admin center".  

Is there a way to do this using the "Exchange admin center" so that we can either have a CN field or that the CN will take its value from the "alias" field?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-08*

@Neil Hiorns       

Hi,    

This can be done easily using PowerShell but not all admins are able to use it and instead will use the "Exchange admin center".    

Did you mean by using the "set-mailbox -identity <mailbox name> -displayname <displayname in EAC>" command via EMS?    

I suppose that you can simply do it in EAC by editing the "Display name" of the shared mailbox.    

For resource mailboxes,edit the "Room name" or the "Equipment name".    

    

In admin audit log, we can also see that it performed the same command as in EMS.    

    

In addition,by default the Canonical Name will be the "Display name" ("Room name" or "Equipment name" for resource mailboxes) when you create the mailbox.    

If you would like to change the Canonical Name of the mailbox in Active Directory, you may need to run the "set-mailbox -identity <mailbox name> -name <Canonical Name in Active Directory>" command via EMS.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
