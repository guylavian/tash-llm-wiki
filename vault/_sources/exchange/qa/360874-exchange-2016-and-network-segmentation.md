---
title: "Exchange 2016 and network segmentation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/360874/exchange-2016-and-network-segmentation
question_id: 360874
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 and network segmentation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/360874/exchange-2016-and-network-segmentation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'd like to confirm the firewall policy requirements around an Exchange 2016 deployment.  My goal is to allow only required ports to and from Exchange.  

I've found that it is not recommended to restrict any traffic between Domain Controllers and Exchange servers in either direction.  It's also a good idea to have more than one Domain Controller within the AD site where the Exchange server resides.  

It not recommended to restrict any traffic between Exchange Servers in any AD site.  

From clients to Exchange it appears you need only TCP:443, unless you need to run the Exchange tools local on that client, then you need TCP:80.  This is only inbound from the client to Exchange server.  Yes remote PowerShell is an alternative to this, but let's ignore that for the sake of this conversation.  

Are these statements still valid?  

If that is still all true, I have a question regarding Domain Controllers in OTHER AD sites.  I would venture to guess that Exchange needs no connectivity in/out to these servers?  

Regards,  

Adam Tyler

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-04-19*

Hi @AdamTyler-3751   ,    

Its really about support versus what works. You can certainly block those remote DCs with firewall rules and set the Exchange Servers to only use local DCs:    

(Exluding the remote DCs)    

-StaticExcludedDomainControllers    

https://learn.microsoft.com/en-us/powershell/module/exchange/set-exchangeserver?view=exchange-ps    

```
set-exchangeServer  -StaticExcludedDomainControllers  , 
```

If that works and Exchange is fine, do that. If you find it doesn't work , undo it.    

The support issue comes if you open a ticket and then support determines the issue is because Exch is trying to contact a Remote DC , then they will tell you what you are doing is not suported.  :)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-19*

Hi @AdamTyler-3751      

Do suggestions above from AshokM help? We could also refer to the discussion in below thread about Exchange 2013 firewall ports    

And a previous article introduces the relationship between Exchange and firewall for your reference as well: https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-firewalls-and-support-8230-oh-my/ba-p/595710    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-17*

Hi @AdamTyler-3751   ,    

As you have stated, yes, its not recommended to restrict firewall ports between Exchange servers and Domain controllers. This includes domain controllers in other sites as well. This is because the exchange will get the list of all domain controllers and keep a track of reachability/SACL rights, etc. Event ID 2080 provides more details. Lets assume there is only one domain controller in the Exchange server site and in an event if that goes down, exchange should be able to communicate with the other domain controllers which are listed as out of site in event 2080. Thus, it has to be allowed.    

    

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/msexchangedsaccess-event-id-2080    

Also, for the clients, SMTP/IMAP/POP protocol ports to be allowed.    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/network-ports?view=exchserver-2016#network-ports-required-for-clients-and-services    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
