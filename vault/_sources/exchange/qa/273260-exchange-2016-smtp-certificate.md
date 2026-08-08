---
title: "Exchange 2016 SMTP certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/273260/exchange-2016-smtp-certificate
question_id: 273260
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 SMTP certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/273260/exchange-2016-smtp-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

how can I find default(primary) certificate which is  bind to SMTP on Exchange 2016.  

I have 3 cerificates binded to SMTP.One self signed ,one 3rd party and one internal CA cert. I want to unbind one cerificate from smtp services and delete because it is expired(internal CA certificate)  

Is this right procedure to remove smtp certificate:  

https://practical365.com/exchange-server/remove-ssl-certificate-exchange-server-2013/   

How can I find which name should certificate have to support SMTP?  

Is it receive connector-client frontend connector-fqdn ,name that certificate should have or is it on send connector?  

https://social.msdn.microsoft.com/Forums/en-US/f94b7f3b-164e-49aa-a15d-1fe36e32341d/create-and-install-a-certificate-for-tls-smtp-connector-on-exchange-2010?forum=exchange2010   

What is the purpose of  smtp certificate?  

Thank you

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-02-16*

Hi @Andy  ，    

-  To find the currently default SMTP certificate, you can run the powershell script in the blog below, just need to specifying a target exchange server:    

Field notes: What is the current default SMTP certificate for your Exchange Server environment?    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

I've tried it in my test lab and it worked:    

    

-  Yes, you can refer to that article to remove the unwanted certificate.    

-  As regards to the names need to be included in the certificate, according to the article as follows, "The certificate must include the DNS name that's used by the SMTP clients or servers to connect to the Receive connector. To simplify certificate management, consider including all DNS names for which you have to support TLS traffic in a single certificate."See:    

Certificate requirements for Exchange services    

-  The SMTP certificate is used for the mutual TLS connections between the Exchange Servers within an Exchange Organization and is also presented to external mail systems when mutual TLS is required.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
