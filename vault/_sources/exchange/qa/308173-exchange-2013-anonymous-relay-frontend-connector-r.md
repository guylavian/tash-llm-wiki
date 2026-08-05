---
title: "Exchange 2013 - Anonymous relay frontend connector - Removal of \"ms-Exch-SMTP-Accept-Any-Sender\" permission has no effect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/308173/exchange-2013-anonymous-relay-frontend-connector-r
question_id: 308173
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 - Anonymous relay frontend connector - Removal of "ms-Exch-SMTP-Accept-Any-Sender" permission has no effect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/308173/exchange-2013-anonymous-relay-frontend-connector-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I ran in a strange behavior while setting up a receive connector on Exchange 2013 to work as Anonymous Relay. I'm in the process of migrating from Exchange 2010, so I'm recreating the same Receive connectors that I have in XCH2010.  

Permissions on both Exchange servers RCs are the same:  

User                                          ExtendedRights  

NT AUTHORITY\ANONYMOUS LOGON                  {ms-Exch-SMTP-Accept-Any-Recipient}  

NT AUTHORITY\ANONYMOUS LOGON                  {ms-Exch-Accept-Headers-Routing}  

NT AUTHORITY\ANONYMOUS LOGON                  {ms-Exch-SMTP-Submit}  

NT AUTHORITY\ANONYMOUS LOGON                  {ms-Exch-SMTP-Accept-Authoritative-Domain-Sender}  

As you can see, "ms-Exch-SMTP-Accept-Any-Sender" permission has been removed from the default set of permissions that are applied when ticking "Anonymous Users" in the GUI to setup anonymous relay connector. That is, I set up the connector ticking "anonymous user" and after saving I manually removed in EMS "ms-Exch-SMTP-Accept-Any-Sender" permission.  

The goal is to allow anonymous relay to any recipients (@anydomain.any) from a small subset of internal IPs, but only using @mydomain.xx smtp domain as sender address (mail from:).   

This works and has always worked for Exchange 2010: when issuing the <crlf>.<crlf> sequence (using a non local smtp domain in mail from:), the hub transport tells me:   

550 5.7.1 Anonymous client does not have permissions to send as this sender  

Setting up the same connector in Exchange 2013 (latest CU), ignores the absence of the extended right, letting me to use any domain in the sender address. Connector has been set as frontend connector, as it's the recommended method on Microsoft documentation to create receive connectors that act as anonymous relays.  

I read around that someone has workarounded the problem by setting up a connector as a TransportHub connector instead of Frontend.   

Can someone explain this behavior change and how can I achieve the above said goal in a supported/clean way?  

Thank you,  

Francesco B. B.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-16*

@Yuki Sun-MSFT  ,    

I take advantage of your kindness for another question related to this topic.     

Just for the sake of improving my skills and learning... The option 2), where it tells to create a Receive Connector that requires authentication: I don't understand two things. The article says that you prevent internal email spoofing by creating a connector this way:    

```
New-ReceiveConnector –Name ”Internal Client SMTP” –TransportRole FrontendTransport –Usage Custom –Bindings 0.0.0.0:25 –RemoteIPRanges 192.168.23.0/24,192.168.170.0/24 –AuthMechanism TLS,Integrated –PermissionGroups ExchangeUsers
```

Now:    

-  It expects Integrated/Kerberos authentication. I'm not aware of any basic smtp client or network device (i.e. printers) that is able to provide Integrated authentication mechanism. Usually you provide clear text credential in them, isn't it? What am I missing or don't understand?    

-  If you plan to use a common username/password to authenticate clients, what does prevent you to spoof someone else? The receive connector just needs you to authenticate, no matter with whose credentials, right? Moreover, once authenticated, who prevents you to use "@anydomain" as the domain portion of smtp address?    

Thank you very much.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

Hi @Yuki Sun-MSFT  ,

I have two choices that I know here, provided the information you kindly gave me:

1) Configure a HubTransport Receive Connector on the 2525 port, since two receive connectors with same bindings on different transport roles (FrontEnd or HubTransport) cannot listen on the same port. So, it will theorically honorate the "ms-Exch-SMTP-Accept-Any-Sender" permission.  

2) Configure a FrontEnd or HubTransport Receive Connector that requires authentication (https://www.codetwo.com/admins-blog/how-to-prevent-internal-email-spoofing-in-exchange/).

The main problem for us by implementing either 1) or the 2) method, is that I will have to change all smtp clients (printers, monitoring applications, etc.) to either use a different smtp port or to provide credentials.

The third (not appreciated) method is to leave things as they currently are accordingly to Exchange 2013 and later behavior change, that is, accept the risk of internal email spoofing.

If you have any other idea, that has less admin activity overhead, it would be really appreciated.

Thank you very much for help.

Francesco B. B.
