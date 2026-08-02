---
title: "Migrate to Microsoft 365 from Exchange 2016 - Change route to EOP, reconfigure clients."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1003216/migrate-to-microsoft-365-from-exchange-2016-change
question_id: 1003216
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
---
# Migrate to Microsoft 365 from Exchange 2016 - Change route to EOP, reconfigure clients.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1003216/migrate-to-microsoft-365-from-exchange-2016-change (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,    

I got a question regarding a migration from Exchange 2016 to Microsoft 365.    

We are running Exchange 2016 in a full classic hybrid and plan to remote move to Exchange Online.    

E-mail is currently routed through the local Exchange Server.    

The last thing I want is users having to reconfigure their mailboxes after or during migration.    

Usually everything is done by autodiscover, but how can I prevent users from having to reconfigure their Outlook profile?    

Last time I changed the e-mailrouting users needed to reconfigure Outlook.    

I wish to route all e-mail through Microsoft 365 EOP and migrate users in batches from the Exchange Server so they notice the least.    

But what will happen if I change the current e-mailrouting from Exchange on Premises to the Exchange Online Protection?    

Microsoft has documentation on how to route the traffic but it's not very clear what will happen to the configured Outlook client, especially on a RDS server.     

Moving mailboxes etc. won't be the issue bit deciding which way traffic will flow is a bit of a question for me.     

https://learn.microsoft.com/en-us/exchange/transport-routing    

Anyone got experience in this field?    

Best regards,    

Tim

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-14*

Thank you very much!
