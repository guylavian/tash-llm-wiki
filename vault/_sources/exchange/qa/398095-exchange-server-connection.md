---
title: "Exchange Server Connection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/398095/exchange-server-connection
question_id: 398095
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server Connection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/398095/exchange-server-connection (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Question that I can't quite figure out  

I have a customer who bought a server to host their email.  Exchange 2016, fully patched and updated.  

Their website/domain is hosted externally with an online hoster/designer, and the customer called and asked me to come in and get their Exchange connected and setup.    

I can't quite figure out how to get it connected to the offsite hoster.  They customer does not have their own Static IP address.  

I have set the MX records in DNS, firewall is as open as I can make it - but the send/receive just doesn't work - at least not consistently.  I have gotten a few emails to send out, but can't receive anything - internal or external.  

Any thoughts?  Suggestions of things to check?  

Thanks  

Randy

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-21*

INBOUND SMTP results  

Testing inbound SMTP mail flow for domain 'user@someemail.address'  

The Microsoft Connectivity Analyzer failed to test inbound SMTP mail flow.  

Test Steps  

  

Attempting to retrieve DNS MX records for domain 'someemail.address'.  

One or more MX records were successfully retrieved from DNS.  

Additional Details  

  

Testing Mail Exchanger mail.someemail.address.  

One or more SMTP tests failed for this Mail Exchanger.  

Test Steps  

  

Attempting to resolve the host name mail.someemail.address in DNS.  

The host name resolved successfully.  

Additional Details  

  

Testing mx record configuration mx value 'someemail.address'.  

Mx values do not match allowed values.  

 Tell me more about this issue and how to resolve it  

Additional Details  

MX Records don't exist or aren't correctly configured for your domain in Office 365. The MX value 'someemail.address' doesn't match one of the allowed values: mail.eo.outlook.com, mail.protection.outlook.com, mail.messaging.microsoft.com, invalid.outlook.com  

I'm not entirely sure why it's saying that about the MX record ... I believe I have them setup correctly
