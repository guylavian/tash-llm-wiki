---
title: "Exchange 2013 bounce incoming email after certificate renewal RRS feed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/181927/exchange-2013-bounce-incoming-email-after-certific
question_id: 181927
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 bounce incoming email after certificate renewal RRS feed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/181927/exchange-2013-bounce-incoming-email-after-certific (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone.

First of all, I'm not skilled with Exchange, I inherited from the previous technician.

Recently I renewed my domain certificate with Let'sEncrypt. I did it the same way as always:

1) renew from Let's Encrypts app.

2) go to IIS, remove the 443 binding from Exchange Back End.

3) Restart IIS.

But this time the server doesn't receive mail. When I do a test with gmail it get's through, but I get complaints from my boss that he doesn't receive specific mail. I've added thoses emails to the whitelist but it doesn't seems to work.

When I do a "Get-MessageTracking Log", I got a huge ammount of Fail SMTP emails, but I don't know how to continue.

Thank you for your time.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-02*

Hi @Drageir Armanre      

According to your information above, your organization failed receiving messages after renewing certificate. Did you get any error information when access outlook or OWA or ECP after that?    

Could you please provide the complete message tracking log you received for troubleshooting?(note to erase personal information)    

We could firstly use the ExRCA Tool to help us check the Inbound SMTP Email for our organization    

    

In addition, please also check the configuration of the certificates with command below (note to erase personal information):    

```
Get-ExchangeCertificate -Thumbprint XXXXXXXX | Format-List
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
