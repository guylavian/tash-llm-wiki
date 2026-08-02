---
title: "Howto change exchange online journal mailboxses sender domain - SPF issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/383850/howto-change-exchange-online-journal-mailboxses-se
question_id: 383850
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
---
# Howto change exchange online journal mailboxses sender domain - SPF issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/383850/howto-change-exchange-online-journal-mailboxses-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

we use an external journal mailbox with a transport rule for all outgoing/incoming mails - setup in exchange admin center onilne.    

However the SENDER address of all that mails is not configurable. It's something@tenant  .onmicrosoft.com    

As the SPF-policy for onmicrosoft.com is strict (-all), problems arise if mail is forwarded, as it breaks SPF.    

How can we set the real domain as sender address (@customer.com). These domain is the primary mail domain, that is routed to exchange online.    

Thank you.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-05-06*

Check what SPF is again. The TXT record is to be added to DNS of customer.com, not onmicrosoft.com.    

When adding the TXT record, the content should look something like this for Exchange Online.    

```
v=spf1 include:spf.protection.outlook.com -all
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-06*

Hi @Stefan Bauer   ,    

Beased on my knowledge and test, Journal mail is sent by the system mailbox on behalf of your Exchange online mailbox with the "SendonBehalf" permission. We could not change the this email address. And the address mailbox is a specific address.     

Please following the steps in this official atricle to create a safe sender lists for this specific email address, then try to send an test email and see if the journal email breaks SPF.    

Please refer to: Create safe sender lists in EOP    

    

Or change the SPF record and add the domain of the address that sends the journal mail to the SPF record.    

Please refer to: Form your SPF TXT record for Microsoft 365    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
