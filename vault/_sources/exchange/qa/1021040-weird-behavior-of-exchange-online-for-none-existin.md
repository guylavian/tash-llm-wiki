---
title: "Weird behavior of Exchange Online for none-existing email address"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1021040/weird-behavior-of-exchange-online-for-none-existin
question_id: 1021040
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Weird behavior of Exchange Online for none-existing email address

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1021040/weird-behavior-of-exchange-online-for-none-existin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am see a weird behavior of Exchange Online for none-existing email address, wondering if anyone can explain it.    

I am setting up a Fortimail Cloud service ( third party email protection service ) to Exchange Online, but noticed one function "Recipient address Verification" (using RCPT method) doesn't work as I thought. I did some troubleshooting, my understanding is Fortimail will send a "RCPT TO:" to Exchange Online to verify if the recipient is a valid email.    

I did traffic capture from Fortimail to Exchange Online :     

		    

Somehow Exchange Online replied with "250 2.1.5" for the fake email !    

But when I do a manual test from a random azure machine,  with all the same input, same recipient, Exchange Online return "550 5.4.1" :    

    

Now I am really confused why this is happenning.    

I tested with a second test M365 tenant with a different email domain and it behave same way, the test domain 's MX and TXT SPF record doesn't have any reference to Fortimail Cloud, so there shouldn't be any reason it's treated differently.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-23*

After some testing, It looks like a issue with Exchange Online Canada service, it might have some special rules for Fortimail Cloud.    

I searched Microsoft Partners and found two partners using Exchange Online and does send 550 for none-existing users :    

Sherweb.com :  MX sherweb-com.mail.protection.outlook.com, Canada.    

carahsoft.com: MX carahsoft.mail.protection.outlook.com. US.    

Test result from Fortimail Cloud :

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-23*

Is there an inbound connector setup on the ExO side or any sort of safelisting of the Fortimail IPs setup for that tenant?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-23*

If the accepted domain in the ExO tenant is set to internal relay then you will see the behavior you describe and the emails wont be rejected during the SMTP conversation, but will later if non-existent:    

https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/manage-accepted-domains/manage-accepted-domains
