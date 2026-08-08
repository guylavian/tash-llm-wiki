---
title: "Exchange 2016 autodiscover SCP response and clients connection behavior"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/416485/exchange-2016-autodiscover-scp-response-and-client
question_id: 416485
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange 2016 autodiscover SCP response and clients connection behavior

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/416485/exchange-2016-autodiscover-scp-response-and-client (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have an Exchange 2016 CU19 environment, on premise only, in one domain, one site.  

I wanted to deploy an additional exchange in the same site, for testing purpose, to not disturb the users, and test the kerberos auth in wthe production.  

Before deploying, this server, we blocked port 80 and 443 and the firewall level, and I added a IPsec policy on the test server (EXCH-test), blocking ports TCP 443, 25 and 2525 from any incoming IP/port.  

Around 5-10 min after installing the exchange setup, we changed the Exch-test SCP to a URL, pointing to the other Exchange servers (EXCH-serv).  

That, apparently was enough to cause Outlook disconnection, for around 10% of all users, which is a lot. I removed the Exch-test, and yet, the problem last for another hour. Outlook was still trying to connect to Exch-test.  

No problem of DC replication, no GPO regarding autodiscover behavior.  

I understand that before changing the EXCH-test SCP, some Outlook clients tried to retrieve the autodiscover xml from EXCH-test. what I don't get is, from my understanding:  

-  outlook clients should have failed and try the other URI (ports 443, 80 blocked)  

-  what is "WEB" part in the autodiscover.xml response  

-  Why Outlook clients tried to connect to the Exch-test? Did the Exch-servers made Exch-test available to connect to?  

I think recycling the autodiscover app pool on all Exch servers would have solved the problem, but I don't get why Outlook clients tried to connect to Exch-test (and failed as it was blocked).  

Thank you.  

Chris

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-01*

Hi ZhengqiLou-MSFT,  

We changed the SCP for Exch-test to point to the Exch-serv, but we had 5-10min between the end of Exch-test installation and the DC replication.  

We blocked port 443, first to avoid the Outlook popup to all users, which worked, and I assumed, Outlook after failing getting autodiscover response from Exch-test, would try the next SCP url.  

I'm not sure if Outlook was able to get an autodiscover response from Exch-test, as in the xml response, under 'WEB' provider, internalOWA is Exch-test server fqdn, thus my questions:  

-  what is the purpose of 'WEB' provider in the autodiscover xml (if I can name it a provider....)  

-  why blocking 443/80 was not enough to fail and skip it to the Exch-serv.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-01*

Hi @ChKhayat-8418 ,    

For a test environment with no ports blocked, I changed the serviceBindingInformation of EX2 and EX3 to point to EX1.    

I could successfully contact with Exchange server:    

    

The whole processes were done on EX2.    

But as you said that the outlook was still trying to connect with exch-test but not exch-server, I'm considering if it is related with SCP, what does "I removed the Exch-test" mean?    

And I think you should open Port 443 to use autodiscover or connect with SCP, whatever, I believe it should be the key to the vault.    

Best regards,    

Lou

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-31*

Thank you AndyDavid for you quick answer.  

I checked the autodiscover link: "An attempt is then made to each URL that's returned by the SCP lookup to try to retrieve the Autodiscover payload"  

and with "The Outlook autodiscover check is about an hour".  

How come users that were trying to connect, got a autodiscover from Exch-test? (I assume they succeeded, as users probably lost connection for an hour at least, and restarting Outlook did not solved it). Blocking port 443 and 80 was not enough?  

I forgot to add a weird event MSExchangeADTopology I noticed on the Exch-serv: saying the LDAP service was down on Exch-test...it seems they considered Exch-test as a DC...I have no clue why...  

Thank you.  

Chris

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-31*

The Outlook autodiscover check is about an hour, so you may been seeing that.   

https://support.microsoft.com/en-us/topic/outlook-2016-implementation-of-autodiscover-0d7b2709-958a-7249-1c87-434d257b9087  

Autodiscover timing  

Autodiscover runs at the following times:  

During account creation.  

At set intervals to collect changes to URLs that provide Exchange Web Service features (OOF, Availability Service, and so on). If this process is successful, another try is made one hour later. If the attempt isn't successful, the next try is made 5 minutes later. Each attempt can potentially be staggered by as much as 25 percent because of the background task infrastructure used by all Microsoft Office applications.  

In response to certain connectivity failures. In various scenarios, when a connection attempt fails, Outlook starts an Autodiscover task to retrieve new settings in any attempt to correct the connection problem.  

When another application invokes it by using MAPI. For more information about MAPI, see the following MSDN article: Outlook MAPI Reference.
