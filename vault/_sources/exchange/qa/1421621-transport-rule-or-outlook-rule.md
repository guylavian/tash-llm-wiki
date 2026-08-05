---
title: "Transport rule or outlook rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1421621/transport-rule-or-outlook-rule
question_id: 1421621
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Transport rule or outlook rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1421621/transport-rule-or-outlook-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All

we are using exchange 2016 hybrid environment. we create users in onprem and migrate to online. i have few shared mailboxes created in onprem and migrated to online and few created as remote shared mailboxes from onprem. i have shared mailbox and i want to create transport rule or outlook rule i am not sure. Lets say when any external user sends email to this shared mailbox and has these words in email body lets say test abc, i want to move these emails to a specific folder in outlook and also i want to forward those emails to an external email address. experts guide me with the rule. if it is transport rule should it be created in onprem or online?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-10*

test abc is in email body not email subject

is it possible to create transport rule like if an external email is received having test abc in the email body add some kind of an header lets say header is abc.  can i create an outlook rule like if email is received with header abc moved it to a folder and foward the email. will this achieve it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-11-10*

Transport rules cannot be used to move messages to specific folders (well, apart from Junk), so use Outlook rules for that part. Forwarding can be done by either type.

If using mail flow rule, it should be created where the mailbox resides. If you have migrated the shared mailbox to Exchange online, create the rule in the service.
