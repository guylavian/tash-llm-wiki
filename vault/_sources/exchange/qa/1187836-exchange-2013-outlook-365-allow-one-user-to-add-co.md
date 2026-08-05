---
title: "Exchange 2013, Outlook 365, allow one user to add contacts to Global Address List"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187836/exchange-2013-outlook-365-allow-one-user-to-add-co
question_id: 1187836
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# Exchange 2013, Outlook 365, allow one user to add contacts to Global Address List

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187836/exchange-2013-outlook-365-allow-one-user-to-add-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

-  On-prem Exchange 2013

-  Windows 10 clients running Outlook 365

I need to allow one staff member to add contacts to the Global Address List from within Outlook. When she tries to do that now (select GAL, add new contact) she gets a message "You cannot create entries for this Address Book".

I don't want to grant full organizational management access, just access to this one narrowly defined function.

What I've tried so far is to create a new Admin role in Exchange EAC:

-  Role name: "Address Lists Management"

-  Write scope: Default

-  Roles: "Address Lists"

-  Members: < the staff member in question >

However, the staff member is still receiving the error message in Outlook and can't create new contacts in the GAL.

## Answers

_No answers on this thread._
