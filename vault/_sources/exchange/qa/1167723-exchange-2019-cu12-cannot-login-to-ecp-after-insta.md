---
title: "Exchange 2019 CU12 Cannot login to ECP after installing new SSL certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1167723/exchange-2019-cu12-cannot-login-to-ecp-after-insta
question_id: 1167723
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
---
# Exchange 2019 CU12 Cannot login to ECP after installing new SSL certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1167723/exchange-2019-cu12-cannot-login-to-ecp-after-insta (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone.

Recently on our Exchange 2019 CU12 server, I updated an Auth Certificate and installed the new certificate with no issues. It has been verified that I can access and log into OWA from the IP address of both exchanges, and the new certificate is being used. But my environment is using SLB, the IP is using SLB VIP, when I log in using SLB VIP, when I go to ECP URL, it redirects to OWA URL:

.../owa/auth/logon.aspx?replaceCurrent=1&url..., but after 8 hours, it can be accessed normally again. I think CU12 has not fundamentally solved the problem of time zone.

The recovery command has been executed, but it still keeps jumping to the login page

Restart-WebAppPool "MSExchangeOWAAppPool"

Restart-WebAppPool "MSExchangeECPAppPool"

I checked the default web site bindings in IIS and port 443 is using the new certificate. And for the Exchange backend, port 444 uses the "Microsoft Exchange" certificate, which will still be valid until next year.

We can still log into OWA fine, and I can access the Exchange Management Shell. So at least I wasn't completely locked out by the admin. In the application and system event logs, I don't see any obvious problems.

## Answers

_No answers on this thread._
