---
title: "Exchange 2019 shared calendar email notifications still being after permissions removed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1051103/exchange-2019-shared-calendar-email-notifications
question_id: 1051103
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 shared calendar email notifications still being after permissions removed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1051103/exchange-2019-shared-calendar-email-notifications (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,      

I am an admin for Exchange 2019 and was working on an access issue for the office admin where I added my admin account to their shared calendar by sending myself an invite by logging in as the share account's user via OWA.       

We resolved the issues, and I went to remove my calendar permissions in OWA, and they were not there, but I was still getting calendar invite email notifications.      

I checked the calendar permission via Exchange PowerShell, and I did see them and remove them successfully via remove-mailboxfolderpermission command.  Unfortunately, I am still getting event notifications, and I cannot find anywhere to remove my access.     

Michael

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-17*

Hi Andy,    

I think that might have done it.  My admin account was listed as a delegate, and I was able to remove it.  I will give it a few hours and see if I get any new notifications.    

Curious, was there a way to check this from the Exchange PowerShell?    

Michael

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-17*

Can you give yourself full access to the mailbox, create a sep Outlook profile as that shared mailbox and then check delegates?    

Could be its set there
