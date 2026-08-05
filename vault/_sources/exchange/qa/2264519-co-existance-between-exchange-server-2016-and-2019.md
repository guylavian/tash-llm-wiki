---
title: "co-existance between exchange server 2016 and 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2264519/co-existance-between-exchange-server-2016-and-2019
question_id: 2264519
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# co-existance between exchange server 2016 and 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2264519/co-existance-between-exchange-server-2016-and-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have both on-prim exchange 2016 and 2019 DAG. once I moved a mailbox from exch2016 to 2019, the user cannot connect outlook. It ask username/password and but never works. Once I point server from loadbalancer directly to the exchange 2019 server, it works. It looks like exch2016 doesn't proxy connection to exchange 2019. I checked SCP, URL, they are all fine. What could be the issue?

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 1 · updated: 2025-05-14*

Hi alan g,

Thank you for posting your question in the Microsoft Q&A forum.

Starting with Exchange 2019 CU14, Windows Extended Protection (EP) feature on the Exchange server will be enabled by default. There are some prerequisites and unsupported scenario for EP, and Outlook connection could be affected. For example, you must not be using SSL offloading with your Load Balancers.

We could disable EP manually if you are using Exchange 2019 CU14 or CU15.

.\ExchangeExtendedProtectionManagement.ps1 -DisableExtendedProtection

Then try to reset IIS on all your Exchange servers. Wait for some time and test Outlook connection again.

iisreset

For more information about Extended protection and the script to disable EP, please check:

Exchange Server support for Windows Extended Protection | Microsoft Learn

ExchangeExtendedProtectionManagement - Microsoft - CSS-Exchange

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-08*

what is default TLS version exchange 2019 use? Isit not compatible with Exch 2016? I installed it using default setting.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-05-08*

Yea you should verify its enabled for TLS 1.2 on both ( 1.3 is avail for enabling as well)

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-tls-configuration?view=exchserver-2019

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-08*

The cert matches and same on 2016 and 2019.  I don't think it is loadbalancer because I tested it by enter an entry using exchange 2016 server IP as the loadbalancer IP in host file, it still doesn't work. This bypassed the load balancer. The exch2016 server should proxy to 2019 server directly. 

Regarding TLS, does 2016 and 2019 use different version and not compatible?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-05-08*

It does proxy but if it fails at the load balancer, I would suspect the certs do not match between 2019 and 2016 or perhaps a TLS issue such as 1.2 not working through the load balancer perhaps.
