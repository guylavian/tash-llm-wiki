---
title: "Reverse DNS for hybrid exchange setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/308311/reverse-dns-for-hybrid-exchange-setup
question_id: 308311
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management"]
---
# Reverse DNS for hybrid exchange setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/308311/reverse-dns-for-hybrid-exchange-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have an Exchange hybrid setup between O365 and a linux server installed on a VPS. O365 is the front server and all inbound and outbound emails are relayed through it.  

Before connecting the two servers, we setup successfully the reverse DNS on the VPS. Now that we have connected the two servers, we don't know how to setup the reverse DNS for O365. We don't pass Mail-tester anymore and get the following error message:  

"Your IP address 40.107.xxx.xxx is associated with the domain mail-viXXXXXXXXXXX.outbound.protection.outlook.com.  

Nevertheless your message appears to be sent from EUR05-XXXXXX.outbound.protection.outlook.com."  

Our DNS are managed by Squarespace and we have added an TXT spf record: "v=spf1 ip4:xxx.xxx.xxx.xxx include:spf.protection.outlook.com -all" with "xxx.xxx.xxx.xxx" the IP of the VPS.  

We read a number of answers on this forum, but without founding a solution.  

It would be great if someone could help.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

Hi @MicMac      

First make sure the A and ptr records configured correctly for your domain, we could use MXTOOLBOX to check that.    

Reverse DNS  is something set at your ISP level, not on your Exchange server. If you have a static IP from your provider you should be able to contact them (or log into the ISP's portal) to change the reverse DNS.    

Here is also an article introduces about Managing SPF and reverse DNS in Exchange Server (Part 3)    

And a related thread here for your reference as well: unable to send emails to hotmail/outlook or live email address    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
