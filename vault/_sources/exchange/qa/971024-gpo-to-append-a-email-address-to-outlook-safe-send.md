---
title: "GPO to append a email address to Outlook safe senders list for everyone"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/971024/gpo-to-append-a-email-address-to-outlook-safe-send
question_id: 971024
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# GPO to append a email address to Outlook safe senders list for everyone

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/971024/gpo-to-append-a-email-address-to-outlook-safe-send (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our AD environment is all 2012r2    

Our OL environment is mostly all Version 2202 build 14931    

I would like to know step by step best way to roll out a GPO to add an address to everyone's safe senders list and not remove what they currently have in place today.    

Issue is that from a certain external email address a red X shows in body where we would have to right click and download picture, workaround is to add this external email address to safe senders for everyone. I worked with Microsoft to add this to the Security\Anti-spam\inbound policy safe senders list and while this works for OWA it doesn't for OL clients.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-08-18*

Additionally, from registry I'm assuming you want me to go to User Configuration\Preferences\Windows settings\Registry and create a new DWORD value?     

I do not see your path when I edit the GPO

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-18*

I do not specifically see 'Microsoft Office Outlook 2016', can or should I be okay with using 'Microsoft Outlook 2016'?
