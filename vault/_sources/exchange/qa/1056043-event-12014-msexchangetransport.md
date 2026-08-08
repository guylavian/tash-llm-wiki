---
title: "Event 12014, MSExchangeTransport"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1056043/event-12014-msexchangetransport
question_id: 1056043
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Event 12014, MSExchangeTransport

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1056043/event-12014-msexchangetransport (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

I had this error for one of my relay connectors that is using FQDN (myserver.mylocal.mydomain.com), everything has been working fine, the error kept on coming so often, I decided to renew the SSL that includes myserver.mylocal.mydomain.com and installed it on the Exchange server 2010 (that is a hybrid server),  the event seems to have been fine with no 12014 message since then. However the relay has stopped sending emails internally and externally completely.    

Any help would be much appreciated.    

Cheers

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-21*

Hi KyleXu,    

Thanks for the response.    

I'll be upgrading the Exchange server that is in my project list.    

Event 12014    

Microsoft Exchange could not find a certificate that contains the domain name myserver.mylocal.mydomain.com  in the personal store on the local computer. Therefore, it is unable to support the STARTTLS SMTP verb for the connector Relay - My relay with a FQDN parameter of myserver.mylocal.mydomain.com. If the connector's FQDN is not specified, the computer's FQDN is used. Verify the connector configuration and the installed certificates to make sure that there is a certificate with a domain name for that FQDN. If this certificate exists, run Enable-ExchangeCertificate -Services SMTP to make sure that the Microsoft Exchange Transport service has access to the certificate key.    

Due to the urgent matter, I had to rekey excluding the domain myserver.mylocal.mydomain.com, the relay is working and sending emails as usual. but obviously the event is now flooding with the message above.    

Cheers

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-21*

@vdz      

Exchange 2010 end of support on October 13, 2020, for a safer environment and for help, it is suggested to update to Exchange 2016 or later.    

What is the detailed error message about the "Event 12014"?    

About mail flow stopped, I would suggest you disable the old one, then follow this article to recreate a new relay connector: How to Configure a Relay Connector for Exchange Server 2010    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
