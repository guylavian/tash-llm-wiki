---
title: "Setting up Exchange Hybrid - Question about Accepted Domains"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1062593/setting-up-exchange-hybrid-question-about-accepted
question_id: 1062593
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Setting up Exchange Hybrid - Question about Accepted Domains

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1062593/setting-up-exchange-hybrid-question-about-accepted (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I am getting ready to migrate our on-prem Exchange 2016 environment to Hybrid Exchange and I was wondering about custom and accepted domains.  Our AD domain is ACME.COM but our default accepted domain is ALPHACHARLIEMIKEECHO.COM.  We have both domains listed as authoritative accepted domains in Exchange 2016 and I have ACME.COM registered as a custom domain in Office365.  Do I also need to have ALPHACHARLIEMIKEECHO.COM registered as a custom domain in Office365 or will it simply be a matter of setting up the MX and autodiscover records for ALPHACHARLIEMIKEECHO.COM in DNS?    

When we changed our organization's name we set up everything to use the shortform (ACME.COM) version as the AD and SMTP domain. At the last second we were told to use the longform version of the name for email so we simply set the long version domain name as the default accepted domain.  We're at a point now where we want both to work.     

Thank you!

## Answers

_No answers on this thread._
