---
title: "Exchange 2013 and Exchange 2019 coexistence"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1078949/exchange-2013-and-exchange-2019-coexistence
question_id: 1078949
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 and Exchange 2019 coexistence

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1078949/exchange-2013-and-exchange-2019-coexistence (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

I am going to introduce Exchange 2019 to an existing Exchange 2013 Hybrid environment and have a few questions    

Current setup    

-  Exchange 2013 CAS and Mailbox Servers    

-  Domain Forest Functional Level - Windows 2012    

-  Schema already updated to support Exchange 2019, so this will just be the installation and config of Exchange 2019    

-  On-Premises Citrix ADCs - Azure load balancers not ready as yet    

Proposed actions    

-  2 Multi-role Exchage 2019 servers built in Azure which Exchange 2019 will be installed on and configured to the point where they will be part of the environment but will not participate in any services like SMTP relay. The only config tasks I'll perform as part of the install will as follows    

-  Configure Logging   

-  Configure Virtual Directories  

-  Configure Offline Address Book  

-  Install and Bind Exchange Server Certificates  

-  Configure new Mailbox DAG  

Once the servers are introduced, we will be moving the services off 2013 to the 2019 servers in a few weeks time like SMTP relay, OAB generation etc.    

My main question is that when I install Exchange 2019, will it affect the current Exchange 2013 setup in any way, like insert itself into send or receive connectors or force some kind of change to the environment that makes the new Exchange 2019 part of mail routes or any other Exchange service, yet I think that the current Hybrid config won't be affected by the introduction on Exchange 2019 until we run it again to introduce the Exchange 2019 servers. I don't want to have to back track and remove the new servers out of existing configurations.    

I know of a customer that introduced Exhange 2016 to an Exchange 2010 environment and from what I heard, it had no effect until they made DNS changes to point away from 2010 to 2016, so I am assuming that doing the same in a 2013 environment and introducing 2019 into it will be the same.    

Thanks for taking the time to look at my question.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-08*

In relation to disk sizes for Exchange 2019 - I understand this may not be right place to ask - but we had an Azure VM provisioned with the following drives    

C Drive = 126GB    

D Drive (Temporary Storage) = 32GB    

E Drive = 100GB (Exchange Install)    

F Drive = 100GB (Logging)    

G Drive = 100GB (Mailbox Database)    

When I try to choose the E Drive as my Exchange installation drive I get the following error "The selected installation directory isn't a valid directory for installing Exchange Server."    

I can choose C Drive but that isn't best practice, but not any other drive. They are setup correctly, formatted etc. and I don't think it is permissions related     

I came across this thread, but cannot see a resolution ... https://learn.microsoft.com/en-us/answers/questions/18461/exchange-2019.html    

My next step will be to provision a 200GB drive to the server and try again to see if it will allow me to install Exchange on it.    

Any thoughts?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-07*

Our autodiscover DNS record points to an F5 load balancer pool that has the Exchange 2013 servers in it. This isn't going to change just yet.     

All of the Exchange URLs go through the F5s as well and I will configure them on 2019, just as they are on 2013.    

https://autodiscover.domainname.com.au/AutoDiscover/AutoDiscover.xml    

https://domainname.com.au/owa    

https://domainname.com.au/oab    

https://domainname.com.au/mapi    

https://domainname.com.au/ews    

https://domainname.com.au/owa    

https://domainname.com.au/Microsoft-Server-ActiveSync    

I've also got the Exchange 2013 certs ready and will install and configure them on 2019, just like 2013 is currently.    

So really at the end of it, I'll just have 2 Exchange 2019 servers not doing anything, but ready to be cutover to in a few weeks time.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-07*

The biggest issue is that once the 2019 servers are up, Outlook clients can use them for autodiscover.    

So you have really two options:    

Set the client URLs to the same as the 2013 URLs or add trusted certificates with the 2019 FQDNs as subject names to the 2019 servers    

I prefer the first option:    

Set the 2019 virtual directory and autodiscover URI to the same as the 2013 server and import and enable the services on the 2013 certs on the 2019 servers so that all the servers match.    

The deployment guide is useful here:    

https://setup.microsoft.com/wizard/exchangedeployment
