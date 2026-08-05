---
title: "Exchange 2010 & EOP Failing to deliver External Emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/304252/exchange-2010-eop-failing-to-deliver-external-emai
question_id: 304252
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange 2010 & EOP Failing to deliver External Emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/304252/exchange-2010-eop-failing-to-deliver-external-emai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi There External Outbound emails from MyDomain.COM randomly fail to get delivered and return the following NDR; Delivery has failed to these recipients or groups: User name (ExternalUser_EmailAddress@keyman  .com) Your message wasn't delivered because the recipient's e-mail provider rejected it. The following organization rejected your message: AM5EUR02FT025.mail.protection.outlook.com. Diagnostic information for administrators: Generating server: ServerName.MyDomain.com ExternalUser_EmailAddress@keyman  .com AM5EUR02FT025.mail.protection.outlook.com #550 5.7.64 TenantAttribution; Relay Access Denied [AM5EUR02FT025.eop-EUR02.prod.protection.outlook.com] ## Original message headers: We have an on premise Exchange 2010 server will RU15 installed, our outbound & Inbound emails get routed via EOP. We have had this "hybrid" setup since 2015 and its been working fine all this time, till earlier this month (March) some of our users reported these "Delivery Failed Reports" I can't recall anything that has changed our on premise Exchange server nor any setting changes on our EOP specifically no connector settings have been changed by our admin team both on our on premise server and on EOP. I think i am out of my depth and can't seem to find what the issue is, more so as failed emails eventually get delivered after several attempts. Any help or advice will be greatlly appreciated. Regards Schwarzee

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Noted. Done. Thanks again Manuel (KyleXu-MSFT)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

Hi KyleXu-MSFT    

Thank you for your response and suggested solution. However upon further troubleshooting of the issue, i'd like to clarify that our organisation does not have a Hybrid Exchange environment setup, as i earlier thought. We however route all our inbound and outbound emails via EOP, primarily for the spam filtering service Microsoft offers us.    

In light of this, we then changed the SMTP connector details (under Mailflow) on EOP by entering the public IP range used by our on premises server to send outbound emails to O365. previously we only had entered our domain name i.e. for example *.contoso.com but now it is for example 10.3.1.5/24    

The following article, referenced by KyleXu-MSFT was helpful on the matter https://learn.microsoft.com/en-us/exchange/troubleshoot/email-delivery/relay-access-denied-smtp particularly Option 2 on this referenced link.     

Ever since we made the config change on EOP no emails have been bounced back.    

Hope this is useful to those who might experience a similar issue we did.    

And thanks again KyleXu-MSFT for setting us off on the right path to our eventual solution.
