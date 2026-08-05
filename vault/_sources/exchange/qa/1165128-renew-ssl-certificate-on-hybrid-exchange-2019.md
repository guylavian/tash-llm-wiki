---
title: "Renew SSL certificate on Hybrid exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1165128/renew-ssl-certificate-on-hybrid-exchange-2019
question_id: 1165128
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Renew SSL certificate on Hybrid exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1165128/renew-ssl-certificate-on-hybrid-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears,

We are looking to renew our SSL certificate on Hybrid exchange 2019, what is the proper way to do it? How to remove old SSL certificate too?

Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-01*

Hi @Ibrahim AlHusari ,

You could refer to this article to renew your certificate: Renew certificate in Exchange Hybrid

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-30*

Based on my experience, renewing or replacing the certificate are both supported in Exchange hybrid environment. There is no difference between hybrid and on-prems. To renew a certificate that was issued by a CA, you create a certificate renewal request, and then you send the request to the CA. The CA then sends you the actual certificate file that you need to install on the Exchange server.

Also, check this article for more insight into Certificate Requirements for Hybrid Deployments.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-01-29*

Hi,

Please follow the steps over here https://www.alitajran.com/renew-microsoft-exchange-certificate/

and Microsoft guidance documentaiton - https://learn.microsoft.com/en-us/exchange/architecture/client-access/renew-certificates?view=exchserver-2019

Hope this helps.

JS

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
