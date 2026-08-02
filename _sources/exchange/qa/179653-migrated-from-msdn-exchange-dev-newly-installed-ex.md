---
title: "[Migrated from MSDN Exchange Dev] Newly installed exchange 2013 inbound not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/179653/migrated-from-msdn-exchange-dev-newly-installed-ex
question_id: 179653
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Newly installed exchange 2013 inbound not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/179653/migrated-from-msdn-exchange-dev-newly-installed-ex (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.    

[MSDN thread link] Newly installed exchange 2013 inbound not working    

I feel like a complete noob. as i havent worked on exchange since o365 came out. I require a lab environment and so I installed exchange server 2013 SP1 on server 2012 R2. (The DC is also on server 2012R2)    

the exchange is a single server with all the roles installed. My local domain is domain.local but I added a second accepted domain as domain.com. domain.com is also the default domain.  All my users have domain.com email addresses.I created a send connector and mail is going out (Although it goes junkmail on the recipient domain) despite having SPF records in place.The Receive connector seems to be the problem.    

the MX records resolve and looking at the transport log, the message is received but each message inbound gets the error:    

"2020-11-27T09:34:39.143Z,Domain\Default Frontend Domain,08D892B7A9441226,36,10.0.1.5:25,40.107.19.96:54368,,SMTPSubmit SMTPAcceptAnySender SMTPAcceptAuthoritativeDomainSender AcceptRoutingHeaders,Set Session Permissions    

2020-11-27T09:34:39.159Z,THegeekzoneEX\Default Frontend THEGEEKZONE,08D892B7A9441226,37,10.0.1.5:25,40.107.19.96:54368,,08D892B7A9441226;2020-11-27T09:34:38.956Z;1,receiving message    

2020-11-27T09:34:39.159Z,Servername\Default Frontend Domain,08D892B7A9441226,38,10.0.1.5:25,40.107.19.96:54368,<,RCPT TO:<user@keyman  .com>,    

2020-11-27T09:34:39.159Z,Servername\Default Frontend Domain,08D892B7A9441226,39,10.0.1.5:25,40.107.19.96:54368,*,Tarpit for '0.00:00:05',    

2020-11-27T09:34:44.175Z,Servername\Default Frontend Domain,08D892B7A9441226,40,10.0.1.5:25,40.107.19.96:54368,>,250 2.1.0 Sender OK,    

2020-11-27T09:34:44.175Z,Servername\Default Frontend Domain,08D892B7A9441226,41,10.0.1.5:25,40.107.19.96:54368,>,550 5.7.1 Unable to relay,    

2020-11-27T09:34:44.191Z,Servername\Default Frontend Domain,08D892B7A9441226,42,10.0.1.5:25,40.107.19.96:54368,<,QUIT,    

2020-11-27T09:34:44.191Z,Servername\Default Frontend Domain,08D892B7A9441226,43,10.0.1.5:25,40.107.19.96:54368,-,,Local"    

I dont understand what it is trying to relay. is it relaying from the frontend to the hub transport?    

This should not be so difficult but i cant seem to figure out how to receive email from external.    

OWA and ECP are allworking on the domain.com url.    

Any assistance will be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-30*

Hi,    

Please try using below command to resolve the issue 550 5.7.1 Unable to relay    

```
Get-ReceiveConnector -Identity "your Relay" | Add-ADPermission -User "NT AUTHORITY\ANONYMOUS LOGON" -ExtendedRights "Ms-Exch-SMTP-Accept-Any-Recipient"
```

You could refer to below thread discussed the similar issue as yours:    

Exchange 2013 550 5.7.1 unable to relay    

And some detailed information about the configuration for relay connector    

How to Configure a Relay Connector in Exchange Server 2013    

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
