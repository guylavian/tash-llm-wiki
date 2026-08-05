---
title: "Exchange server 2016 issue send email to gmail account"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180940/exchange-server-2016-issue-send-email-to-gmail-acc
question_id: 1180940
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange server 2016 issue send email to gmail account

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180940/exchange-server-2016-issue-send-email-to-gmail-acc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Hello everyone, I have set up an exchange server. There is no problem sending and receiving hotmail letters. But letters sent to gmail account will be returned, but receiving is ok.

It displays as follows:

 
mx.google.com has this error:
[x.x.x.x] Our system has detected that this message is likely unsolicited mail. To reduce the amount of spam sent to Gmail, this message has been blocked. Please visit https://support.google.com/mail/?p= UnsolicitedMessageError for more information.  - gsmtp.

SPF, DKIM, and DMARC have all been set in DNS hosting. The reverse is also set..

May I ask how to solve this problem??
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-15*

Not much you can do. This is being blocked for any number of reasons:

https://support.google.com/mail/thread/178636716/our-system-has-detected-that-this-message-is-550-5-7-1-likely-unsolicited-mail?hl=en
