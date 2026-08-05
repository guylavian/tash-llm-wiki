---
title: "Mail mailboxes from Exchange 365 Hybrid Environment to O365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1033821/mail-mailboxes-from-exchange-365-hybrid-environmen
question_id: 1033821
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Mail mailboxes from Exchange 365 Hybrid Environment to O365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1033821/mail-mailboxes-from-exchange-365-hybrid-environmen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an Exchange 365 Hybrid environment.  We would like to move all mailboxes other than admin off the on-Premises Exchange server and then stop the services on the  Exchange server.  We however want all email going to the on-premises Exchange admin account to be forwarded to our 365 Admin account.  Is there a way to do this, one specific service/role we have to keep active?  While this may not be best practice we want to know if it's technically possible?  Ok to let us know what the pitfalls might be  but more importantly if it can be done and how - strictly technical feasibility answer we are looking for.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-03*

What is the On-Prem Admin account exactly?     

Its really not recommended to mailbox enable elevated accounts either on-prem or in 365.    

If you are going to mailbox enable the global admin, then give it a shared mailbox and forward to regular user mailboxes.    

https://learn.microsoft.com/en-us/azure/active-directory/roles/security-planning#ensure-separate-user-accounts-and-mail-forwarding-for-global-administrator-accounts
