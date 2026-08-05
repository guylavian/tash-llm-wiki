---
title: "[Migrated from MSDN Exchange Dev]  SPF Record Question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/138608/migrated-from-msdn-exchange-dev-spf-record-questio
question_id: 138608
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]  SPF Record Question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/138608/migrated-from-msdn-exchange-dev-spf-record-questio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/a608de95-bf62-4cda-8f74-f9c03123c4c2/spf-record-question?forum=exchangesvrdevelopment  

So we are utilizing a 3rd party mailer to send mail as our organization. They are signing a DKIM signature for our domain on all emails. Because of that the emails are passing DKIM authentication and DKIM alignment therefore passing DMARC.  

They also want us to put their IPs in our SPF record. The issue is, since they are using an envelope sender address that is from their domain, not ours, I do not see the point in adding their IPs to our SPF record.  

SPF will check the SPF record from the domain of the envelope senders email address, not the header "From" address, so SPF will always fail in this scenario, correct?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-26*

When you send a message through the mailer, who is the "envelope sender address". That's the thing we want to figure out first, you should contact the mailer support for this.    

Anyway, after adding his domain address to your SPF, no matter whose domain becomes "envelope sender address", SPF will not fail because both of your domains' IP addresses are added to SPF record.    

You can test it on https://mxtoolbox.com/spf.aspx.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
