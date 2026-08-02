---
title: "adfs respond blank from secondary server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/60590/adfs-respond-blank-from-secondary-server
question_id: 60590
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# adfs respond blank from secondary server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/60590/adfs-respond-blank-from-secondary-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

i have configured an adfs farm with 2 adfs servers.  

From my primary server all pages correctly works:  

https://<ip_address>/adfs/ls  

https://<ip_address>/FederationMetadata/2007-06/FederationMetadata.xml  

https://<ip_address>/adfs/ls/federationserverservice.asmx  

https://<ip_address>/adfs/ls/idpinitiatedsignon.htm  

etc..  

https://<fqdn>/adfs/ls  

https://<fqdn>/FederationMetadata/2007-06/FederationMetadata.xml  

https://<fqdn>/adfs/ls/federationserverservice.asmx  

https://<fqdn>/adfs/ls/idpinitiatedsignon.htm  

etc..  

From my secondary server some pages return blank, giving 400 error:  

https://<ip_address>/adfs/ls    --> blank page  

https://<ip_address>/adfs/portal/updatepassword --> blank page  

https://<ip_address>/FederationMetadata/2007-06/FederationMetadata.xml --> it works  

https://<ip_address>/adfs/ls/federationserverservice.asmx --> it works  

https://<ip_address>/adfs/ls/idpinitiatedsignon.htm --> blank page  

etc..  

https://<fqdn>/adfs/ls --> it works  

https://<fqdn>/adfs/portal/updatepassword  --> it works  

https://<fqdn>/FederationMetadata/2007-06/FederationMetadata.xml --> it works  

https://<fqdn>/adfs/ls/federationserverservice.asmx --> it works  

https://<fqdn>/adfs/ls/idpinitiatedsignon.htm --> it works  

etc..  

If i use:  

https://<fqdn>/someurl/  

all works correctly,  

instead if i use:  

https://<ip_address>/someurl/  

interaction pages doesnt works.  

I checked my dns configuration, all correctly configured, tried with a nslookup <ip_address>, retrieve fqdn informations.  

I need the configuration to work also from ip_addr, as in the primary server, because using an NLB the calls are made directly to the ip address  

Any hint?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-07*

@Pierre Audonnet - MSFT   thanks for your answer,    

okay, now I understand the 400 error.    

What I cannot understand is that in the event of a node failure (e.g. the primary), the nlb will direct traffic to the secondary, (therefore to the IP address of the secondary, not on fqdn), all masked by the call of the IP address of the NLB, but what will always come back will always be a 400 error. In other words, if the primary node goes down, the requests to the ADFS will return a 400 error. There is no availability in this, should I change the SNI settings?    

EDIT: for information: when navigate into https://<ip_addr>/adfs/ls it still continue 400 error (and from my server with same <ip_addr>)

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-06*

"https://<ip_address>/someurl" is not supposed to work (unless you try it locally on the ADFS server).  

The HTTP driver is using SNI to for the bindings. There are only 2 bindings for the port 443:  

-  127.0.0.1 (this is why it works when you try locally)   

-  <fqdn of the farm>  

You can see those bindings with the command:  

```
netsh http show sslcert
```

Besides, NLB is agnostic of HTTPS. NLB "balances" the traffic as long as the host is still sending heartbeat. And that doesn't even check if the actual service is running. In other words, you can stop the ADFS service and NLB will still "direct" some traffic to the (now broken) node. This is why NLB alone is not a great solution for high availability. And hardware load balancer are preferred as they have the ability to check the service's health before redirecting the traffic..  

That said, if you are using SCOM, you could leverage the NLB management pack to do some health probe before considering the node in the NLB cluster. Or DNS policies in Windows Server 2016 (and a lot of scripting), do do the same.
