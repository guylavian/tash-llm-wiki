---
title: "Exchange server 2016 error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1183032/exchange-server-2016-error
question_id: 1183032
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange server 2016 error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1183032/exchange-server-2016-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi 

I use exchange 2016 server in my organization recently we were unable to send or receive email outside our domain like Gmail for example the error message says

Diagnostic information for administrators:

Generating server: EMI-EX-01.emi.gov.et  

Receiving server: EMI-EX-01.emi.gov.et

******@gmail.com  

1/22/2023 11:33:24 AM - Server at EMI-EX-01.emi.gov.et returned '550 5.4.300 Message expired -> 451 4.4.0 DNS query failed. The error was: SMTPSEND.DNS.NonExistentDomain; nonexistent domain edgesync - default-first-site-name to internet -> DnsDomainDoesNotExist: InfoDomainNonexistent'  

1/22/2023 11:32:16 AM - Server at edgesync - default-first-site-name to internet returned '451 4.4.0 DNS query failed. The error was: SMTPSEND.DNS.NonExistentDomain; nonexistent domain edgesync - default-first-site-name to internet -> DnsDomainDoesNotExist: InfoDomainNonexistent'

Original message headers:

```
Received: from EMI-EX-01.emi.gov.et (172.23.27.16) by EMI-EX-01.emi.gov.et
 (172.23.27.16) with Microsoft SMTP Server (version=TLS1_2,
 cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id 15.1.1591.10; Fri, 20 Jan
 2023 14:15:11 +0300
Received: from EMI-EX-01.emi.gov.et ([::1]) by EMI-EX-01.emi.gov.et ([::1])
 with mapi id 15.01.1591.008; Fri, 20 Jan 2023 14:15:11 +0300
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-24*

Hi @Shehun Ayele,

-  According to the non-existent domain displayed in the error message, it seems that the domain DNS records cannot be resolved correctly by Exchange server. First, you can check the DNS settings on the Exchange server where the error is reported. Meanwhile, like Juan said, you can use NSlookup to check.
   

-  Since you are also having trouble with receiving external emails, please use Mxtoolbox（https://mxtoolbox.com/ ）to check if your domain has an active MX record and also an A record pointing to your Exchange server's public ip address in public DNS.

Note: Microsoft is providing this information as a convenience to you. The sites are not controlled by Microsoft. Microsoft cannot make any representations regarding the quality, safety, or suitability of any software or information found there. Please make sure that you completely understand the risk before retrieving any suggestions from the above link.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-23*

Hi @Shehun Ayele  ,

The message says that the DNS query failed. How you are using the conector to send emails to internet? are you using a MX record or SmartHost. 

If you are using a MX record option :

Please open de CMD an run nslookup in your exchange server:

And it show your DNS local that you are using :

type gmail.com and if you see that resolve the names 

a) if you not able to see something like that is because your local DNS is not resolving the domain name so you need to check the local dns, a quick test that you can do is type server 8.8.8.8 to chose the dns into the nslookup command, after this type again gmail.com if now you are able to see the addresses that mean that you need go to your nick of the exchange server and change the DNS "Maybe can be add an aditional DNS Server setting and not move the first one because its must be point to your Domain Controller.

b) If the option a is not working for you you need check if the port is open.

-  install in features the telnet client into the exchange server

-  use the cmd to run telnet 8.8.8.8 53 
   *The step two means that will try to connect to the ip 8.8.8.8 goolge dns to the port 53 (Port used to the DNS query)

-  Maybe recive a message that is not possible to connect.   So thats mean that you need check your endpoint firewall, firewall apliance or network restriction.

Other wise if you are using the smart host please check the same situation into the appliance or your smart host provider!.

Please let us know if its works for you!
