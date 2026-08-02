---
title: "[Migrated from MSDN Exchange Dev]One user multiple email addresses to send from"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/186183/migrated-from-msdn-exchange-dev-one-user-multiple
question_id: 186183
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]One user multiple email addresses to send from

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/186183/migrated-from-msdn-exchange-dev-one-user-multiple (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.

Hello.

We have exchange 2013 and one user needs to be able to send email from our secondary domain. I can added as smtp which solves receiving but unsure how I could accomplish to have the user send mail using the secondary domain.

Thank you.

Juraj.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-04*

Hi ,    

You can create an authoritative accept domain, then use the authoritative accept domain as an email address format to create an email address policy, and then apply the email address policy to specific users. Because there is only one default email address policy in Exchange by default, and the priority is the lowest, if you still want to keep the default primary SMTP address, then you can create an email address policy using the authoritative accepted domain that exists by default in Exchange and set the priority is higher than the email address policy created by the second domain.     

But it should be noted that, according to my research and testing, you can successfully receive mail using the secondary SMTP address, but if you use the secondary SMTP to send mail, the recipient will still see the sender’s address as the primary SMTP address.    

For more information: Create an Email Address Policy and Accepted domains    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
