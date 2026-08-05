---
title: "How can I edit the Name field in Exchange Contacts?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1444587/how-can-i-edit-the-name-field-in-exchange-contacts
question_id: 1444587
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# How can I edit the Name field in Exchange Contacts?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1444587/how-can-i-edit-the-name-field-in-exchange-contacts (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I export contacts from Exchange, there is a Name field, in addition to Display name, First name and Last name. I cannot find where to edit this Name field. I've tried looking in the Microsoft 365 admin center and the Exchange admin center.

Note - When I add a new contact, this name field does not appear.

Thanks.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-30*

Hi @Gidget Kimble  

The Name field is used when you create a mail contact via Exchange Online Powershell. (If you create the mail contact in Exchange Admin Center, it will share the same value as DisplayName)

Example cmdlet:

```
New-MailContact -Name "Chris Ashton" -ExternalEmailAddress "******@tailspintoys.com"
```

It is used to specific the unique identity of the mail contact.

To modify the Name field, you may need to connect to Exchange Online Powershell as an Exchange admin and use Set-MailUser cmdlet.

Example cmdlet:

```
Set-MailContact -identity "name of this contact" -Name "unique new name"
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
