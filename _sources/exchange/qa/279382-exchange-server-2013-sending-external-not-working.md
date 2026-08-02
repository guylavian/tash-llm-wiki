---
title: "Exchange Server 2013 sending external not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/279382/exchange-server-2013-sending-external-not-working
question_id: 279382
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server 2013 sending external not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/279382/exchange-server-2013-sending-external-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a domain(DC01) and Exchange Server 2013(EX01,EX02) host in Azura. wild card cert installed. I can send mail internally and receive mail internally. I receive mail from an external source but I can't send external emails. The Firewall is set to allow ports 25, 587, 80, and 443. ![69689-dns.jpg][1] ![69690-dc01dns.jpg][2]![69811-smtp.jpg][3]![69821-nslookup.jpg][4] the problem lies with Reverse Entries for MX records https://www.dnsinspect.com/ mail.gerti.net ![69822-mx-records.jpg][5] This is the Configuration in Azure DNS Zone ![69812-dns-zone-azure.jpg][6] [1]: /api/attachments/69689-dns.jpg?platform=QnA [2]: /api/attachments/69690-dc01dns.jpg?platform=QnA [3]: /api/attachments/69811-smtp.jpg?platform=QnA [4]: /api/attachments/69821-nslookup.jpg?platform=QnA [5]: /api/attachments/69822-mx-records.jpg?platform=QnA [6]: /api/attachments/69812-dns-zone-azure.jpg?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-28*

unfortunately I haven't had time yet.  

I'll get back to you

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-19*

Thanks for your suggestion!    

I edited the PRT    

    

I have created a new Send Connector    

![70236-gerti.jpg][2]  [2]: /api/attachments/70236-gerti.jpg?platform=QnA    

what am I doing wrong here, please

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-19*

Hi,     

The screenshots you post includes personal information, like domain name/IP address, please cover those information.    

It seems you don't have PTR record for the IP address that mail.contoso.com pointing to, can you try adding a PTR record in your DNS Zone? Create a DNS PTR record    

Also, the fqdn of your send connector misses "." in the fqdn, please correct it with Set-sendconnector(or create a new one, fqdn is blank by default):     

```
Set-SendConnector "name" -fqdn mail.contoso.com
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
