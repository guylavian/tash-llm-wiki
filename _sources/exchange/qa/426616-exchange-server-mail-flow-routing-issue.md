---
title: "Exchange Server mail flow routing issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/426616/exchange-server-mail-flow-routing-issue
question_id: 426616
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server mail flow routing issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/426616/exchange-server-mail-flow-routing-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey,  

At the moment I am with a customer who has two Exchange Server 2013 and two Exchange Server 2016 servers.  

We want to create a send connector with one of the two Exchange Server 2016 machines as source. When created via the command below, Exchange tries to route the mail to the Exchange Server 2013 machine. Do you know a reason why the mail keeps routing to the Exchange Server 2013 machine?  

New-SendConnector -Name OutgoingViaEOP -AddressSpaces testdomain.com -CloudServicesMailEnabled $true -Fqdn mail.example.com -RequireTLS $true -DNSRoutingEnabled $false -SmartHosts ***.mail.microsoft.com -TlsAuthLevel  CertificateValidation -Usage Internet -SourceTransportServers ex16-1

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-09*

Hi @Nieck   ,    

Sorry but I just confused about the smart host you're using, is it a o365/ExchangeOnline smart host? I believe it is also the 4th question Andy asked.    

And about the environment, is it a coexistence of Ex 2013 and Ex 2016 servers?    

I think you should create the send connector on Exchange 2013 servers and specify the server FQDN or IP address as the smart host.    

Create a Send connector to route outbound mail through a smart host    

As you want to use the ex16 to route, you may use it's FQDN to add the smart host.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
