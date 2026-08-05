---
title: "Need a fix on why I can't send Exchange email to Yahoo users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1632166/need-a-fix-on-why-i-cant-send-exchange-email-to-ya
question_id: 1632166
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Need a fix on why I can't send Exchange email to Yahoo users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1632166/need-a-fix-on-why-i-cant-send-exchange-email-to-ya (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

I'm having an issue where my email server (Exchange Server 2016 on-prem) can't send to Yahoo Mail users. 

Before I made this question, I have done several troubleshooting's to our email server, where first we restart the Exchange Server service, but that's only proven as temporary solution. Next what I did was to change the SPF and the DKIM configuration. After checking with mail tester website, it seems our DKIM and SPF for our email server are okay after change, but we still can't send emails and attachments to Yahoo Mail users.

After further investigating, it's related to DNS, more likely due to Yahoo couldn't find our mail checker (IMSVA) server's A record, and I reached to other people that they mentioned that the ISP needs to delegate the IP provided by them to our gateway. Is that correct? Or we can do something about this to mitigate this issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-03*

Hi Jimmy,

-  I believe the server doesn't associate with Microsoft 365 as it's an in-house domain, if I can say that. Haven't checked if our network bypassed the office 365 URL and IP address ranges but will check it out from time to time.

-  It may be due to our last Public IP address reported by Yahoo as abusive, although not enough evidence to proof so. After our network migration, we have reached to our ISP provider to delegate the public IP address they gave us to resolve the issue. After quick troubleshooting, we managed to email to Yahoo users within 3 days at least.

Thanks for the help, Jimmy.
