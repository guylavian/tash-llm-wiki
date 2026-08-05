---
title: "Exchange 2016 CU 23 Outlook 2013 keep asking password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190255/exchange-2016-cu-23-outlook-2013-keep-asking-passw
question_id: 1190255
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# Exchange 2016 CU 23 Outlook 2013 keep asking password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190255/exchange-2016-cu-23-outlook-2013-keep-asking-passw (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We updated Exchange 2016 to CU23.

But now, remote client (outlook anywhere) can't connect, outlook keep asking password.

When client is on site, it is ok.

MAPI client on phones are not impacted. Only Outlook. We have Outlook 2013.

Can you help me?

Thanks.

Alex.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-17*

Hello,

Source :

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-online-email-applications-stopped-signing-in-or-keep/ba-p/3641943

It is working with that (basic auth does not work with CU23 anymore):

https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/enable-modern-authentication?view=o365-worldwide

And delete saved password

cmdkey /delete:MicrosoftOffice15_Data:SSPI:%******@domain.com

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-17*

Hello,

Source : 

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-online-email-applications-stopped-signing-in-or-keep/ba-p/3641943

It is working with that (basic auth does not work with CU23 anymore): 

https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/enable-modern-authentication?view=o365-worldwide

And delete saved password

cmdkey /delete:MicrosoftOffice15_Data:SSPI:%******@domain.com

Thanks.
