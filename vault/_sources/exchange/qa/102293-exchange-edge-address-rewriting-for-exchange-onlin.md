---
title: "Exchange Edge Address rewriting for Exchange Online?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/102293/exchange-edge-address-rewriting-for-exchange-onlin
question_id: 102293
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Edge Address rewriting for Exchange Online?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/102293/exchange-edge-address-rewriting-for-exchange-onlin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've configured my edge server to rewrite the email address for some users, the user's mailbox are on Exchange Server and it works fine.  

Later, I've migrated that user mailbox to Exchange Online and the rewrite function stopped doing it´s job.  

The email flow from Office 365 to the internet it's routed through the on premises infrastructure. So, should it work? Is this an unsupported scenario?  

Regards

## Answer (community) — community member

*upvotes: 3 · updated: 2020-09-23*

Hi @Fernando Crespo   , agree with the reply above from Andy.    

You could refer to the link here discussed the similar issue as yours: Microsoft Exchange Edge Address Rewrite with Exchange Online    

I configured a new receive connector on the Edge server that set Exchange Online Protection IP addresses as authoritative and this enabled the rewrite to work as expected. The below command is an example of what I ran:    

```
New-ReceiveConnector -Name “Exchange Online Protection” -RemoteIPRanges 23.103.132.1-23.103.159.254,23.103.198.1-23.103.203.254 -Usage Custom -AuthMechanism Tls -PermissionGroups AnonymousUsers, ExchangeServers, Partners -Bindings 0.0.0.0:25  
Get-ReceiveConnector *Exchange* | Set-ReceiveConnector -AuthMechanism ExternalAuthoritative, Tls -RequireTls:$true -TlsDomainCapabilities mail.protection.outlook.com:AcceptOorgProtocol -Fqdn “mail.domain.co.uk” -TlsCertificateName “CN=GlobalSign Organization Validation CA – SHA256 – G2, O=GlobalSign nv-sa, C=BECN=hybrid.domain.co.uk, O=Company L=Town, S=County, C=GB”
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 3 · updated: 2020-09-22*

It only works if the messages are seen as authenticated.   

the Address Rewrite Outbound agent will work only when the sender’s SMTP address is internal, and the session is authenticated  

 You can force Exchange to treat the message as submitted from an authenticated source by creating a Receive Connector with the “ExternalAuthoritative” Authentication mechanism. Make sure you only have the IP address of the application or third-party source under the remote IP Address range in this receive connector. This is important, since when you select ExternalAuthoritative for authentication, you’re telling Exchange to completely trust the IP address(es) or subnets specified in the RemoteIPRanges parameter of that connector, allowing those IP addresses to relay through your server. You can run the below commands to create a connector with ExternalAuthoritative Authentication enabled:  

https://techcommunity.microsoft.com/t5/exchange-team-blog/why-is-my-address-rewriting-not-working-as-expected/ba-p/607458

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-22*

Hi,  

After opening a case with Microsoft Support, the answer was that this is an unsupported configuration, so the case is closed.  

The Office 365 team is developing an alternative for Office 365.   

https://techcommunity.microsoft.com/t5/exchange-team-blog/sender-rewriting-scheme-srs-coming-to-office-365/ba-p/607932  

There is no release date at this point.  

Thanks for all the help

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-28*

Hi,    

The txt file with the header its in atach28832-header.txt
