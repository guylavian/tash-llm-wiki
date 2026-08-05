---
title: "[Migrated from MSDN Exchange Dev] email messages to gmail accounts being rejected"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/200164/migrated-from-msdn-exchange-dev-email-messages-to
question_id: 200164
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# [Migrated from MSDN Exchange Dev] email messages to gmail accounts being rejected

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/200164/migrated-from-msdn-exchange-dev-email-messages-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

mx.google.com rejected your message to the following email addresses:  

Getting this message when I press reply button to any messages coming from gmail.  This has suddenly started happening and happens from the "mail app" and also from my desktop installed outlook. Have cleared the suggested names list and it still happens.  I wws wondering if my pc has picked up some malware although other servers addresses seem fine. (Can send a message to myself for example). I noticed that their are a lot of other people having the same problem.  

Source Link: https://social.msdn.microsoft.com/Forums/office/en-US/8e4ea278-65b6-4cc8-b8c2-9d14da6fd1b4/email-messages-to-gmail-accounts-being-rejected?forum=exchangesvrdevelopment

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-12-16*

Known Issue. I am seeing this as well. The issue is with Gmail, not Exchange.  

https://techcrunch.com/2020/12/15/gmail-is-a-little-broken-right-now-one-day-after-a-massive-outage-errors/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAADwFtJ0OJtpihZerarHYxxYhLYveqk6lYPZCFddGXp5TRCpiDhhNApxEdjcaJTg1T7mFce4AzXrGL5LYse0u3lEXRzq65bp5dw_w5vbnjntZfJmv0NS_1_KdayK_3y9WdT1Bt34hQVYHRhxoKkjfq1QCoeVUXb5qfaaTGReBgLPG  

https://www.google.com/appsstatus#hl=en&v=issue&sid=1&iid=a8b67908fadee664c68c240ff9f529ab

## Answer (community) — community member

*upvotes: 1 · updated: 2020-12-16*

Do you using an Exchange server mailbox? What is the version of your Exchange server?  

Could you send email(not reply) from your mailbox to Gmail mailbox? If you cannot send email from your mailbox to Gmail mailbox, could your provide a detailed information about the NDR email?  

I guess your server does not meet Gmail’s security regulations or your mailbox or mail server is blocked by Gmail.
