---
title: "Difficulty communicating exchanges with Outlook from outside the domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/352048/difficulty-communicating-exchanges-with-outlook-fr
question_id: 352048
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Difficulty communicating exchanges with Outlook from outside the domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/352048/difficulty-communicating-exchanges-with-outlook-fr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

I launched Exchange 2016 for the company.  

The problem I have now is that computers that are in the domain can easily connect to Exchange via Outlook, but computers that are in the network but are not domain domains can not be connected to their account with Outlook.  

The same problem exists for mobile devices.  

 On the other hand, I gave Exchange a policy to send emails with the name of another domain I have on the Internet.  

Thank you very much for guiding me to resolve this issue  

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-12*

Hi, @navid Talesh       

Agree with Alex, if the device is domain-joined, Outlook will first search for SCP(Service Connection Point) object in Active Directory.    

When Outlook client attempts to autodiscover, it will follow this order:    

-  URL defined in SCP (Service Connection Point) in On-premises Active Directory. (If the device is not domain-joined, this process will fail and Outlook will move on to try step 2)    

-  https://<SMTP-address-domain>/autodiscover/autodiscover.xml    

-  https://autodisocver.<SMTP-address-domain>/autodiscover/autodiscover.xml    

-  <SMTP-address-domain> defined in Local XML    

-  http://autodisocver.<SMTP-address-domain>/autodiscover/autodiscover.xml    

-  _Autodiscover._tcp. <SMTP-address-domain> (SRV Record)    

If all these steps fail, Outlook will not be able to use Autodiscover to connect to Exchange server.    

To resolve the issue, you may need to setup a CNAME or an A record of autodisocver.<SMTP-address-domain> on your internal DNS server to point to your Exchange server.    

If you would like to also allow clients to connect from external network, you may need to setup the DNS records in public DNS.    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
