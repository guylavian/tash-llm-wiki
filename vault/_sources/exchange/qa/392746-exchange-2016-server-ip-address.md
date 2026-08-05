---
title: "Exchange 2016 server IP Address"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/392746/exchange-2016-server-ip-address
question_id: 392746
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 server IP Address

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/392746/exchange-2016-server-ip-address (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We are hosting our Exchange 2016 server on the premise.  When email going out, instead of showing the email coming from the Exchange server IP address, its shown it's from our firewall ip address.  For this reason, we have our emails blocked by some recipients' email servers.    

We have PTR records of our firewall and Exchange server ip addresses point to our domain name, but still some emails got rejected because of it, especially emails go to msn.com and live.com etc.  

Any comment or suggestion will be greatly appreciated.  

Thanks  

Tee

## Answer (community) — community member

*upvotes: 1 · updated: 2021-05-17*

Lou,    

@Anonymous      

This is our "Send Connect" in "delivery" setting:    

Selected - MX record associated with recipient domain    

None - Smart host authentication    

Last couple days, the outgoing mails is shown coming from the Exchange server instead of firewall.  I don't know what has changed, but all of sudden, it's shown correctly.    

Thanks for all your help.    

Tee

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-12*

Andy,  

Thanks for your response.  Correction, I meant the PTR record is pointing to our public FQDN of the Exchange server.    

I have checked with the firewall support and they have found nothing that indicated the firewall is acting as a smarthost.  I will try to reach out to firewall support again.  

Thanks  

Tee
