---
title: "Exchange 365 / Office 365 shared mail account & display names"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/137966/exchange-365-office-365-shared-mail-account-displa
question_id: 137966
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 365 / Office 365 shared mail account & display names

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/137966/exchange-365-office-365-shared-mail-account-displa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings,    

I have an issue that I hope you can help me with...    

I have a software application (ASP.NET v4.8 hosted on Azure Web App) that I have running for 2 different companies that use our Exchange Online mail server to send notifications from.     

I have set them up each with a Shared Mailbox account, and the Display Name for each Shared Mailbox is different based on the Company.    

e.g. ******@ourcomain.com  displays as Company1 Notifications, and ******@ourcomain.com  displays as Company2 Notifications. This is shown in both the Exchange Admin Center Mailboxes list and the Microsoft 365 admin center Active Users list.    

The connection string for each application looks like this:  <network host="smtp.office365.com" port="587" userName="******@ourdomain.com" password="[password]" enableSsl="true" />    

When I send a test email from Company1 to my company email account (e.g. ******@ourdomain.com), each email comes from the correct email address and shows as the correct Display Name. When I send a test email to my personal account (myname@/c/  _email.com), they each come from the correct email address, but one of them appears to come from the other's Display Name (e.g. ******@ourcomain.com  displays as Company1 Notifications)    

Is there something wrong with the way I have set these up or is there something potentially wrong with Exchange? I have other accounts that do not have these issues (e.g. No Reply / ******@ourdomain.com), so I'm not sure what is wrong here...    

Does anyone have any ideas as to why this is happening?    

Thanks in advance,    

Adam

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-25*

If it only happens with your personal account, I'd suggest checking whether you have some stored contacts matching the address(es) in question, thus overriding the display name. Of course, also make sure to check the header info, in particular From, mail from, Reply-to.
