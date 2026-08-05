---
title: "SSl certificated renewal for exchange 2016 with powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1275260/ssl-certificated-renewal-for-exchange-2016-with-po
question_id: 1275260
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SSl certificated renewal for exchange 2016 with powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1275260/ssl-certificated-renewal-for-exchange-2016-with-po (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have my SSL certificate expired in Exchange 2016. I am not sure how to renew it by power shell because eac es not an option any more.Thank you

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-03*

Hi @GiovannaMicheel Salinas Rosas  ,

 

Since you submitted a similar question, you can refer to my other answer: Renew SSL certificate Ecchange 2016 with a Goddady Certificate - Microsoft Q&A

 

First of all, please make sure you have successfully installed the intermediate certificate to your Exchange Server 2016, detailed steps you can refer to: Exchange Server 2016: Install a certificate | SSL Certificates

_  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information._

 

Then you can use below powershell cmdlet to renew your certificate, detailed steps please refer to: Renew an Exchange Server certificate | Microsoft Learn

```
Get-ExchangeCertificate -Thumbprint  | New-ExchangeCertificate [-Force]
```

 

If you don't know how to open the Exchange Management Shell in your on-premises Exchange organization, see Open the Exchange Management Shell | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-03*

Check this article - https://learn.microsoft.com/en-us/Exchange/architecture/client-access/renew-certificates?view=exchserver-2019
