---
title: "add a third Exchange node in a remote location"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1034316/add-a-third-exchange-node-in-a-remote-location
question_id: 1034316
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# add a third Exchange node in a remote location

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1034316/add-a-third-exchange-node-in-a-remote-location (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I have a couple of questions regarding a new configuration.    

I currently have an exchange infrastructure 2016 in DAG based on 2 servers.    

A balancer has been implemented to balance the load between the two servers.    

The vitual directories are configured like this for Internal and External UR:    

AutoDiscover https://autodiscover.exoip.com/Autodiscover/Autodiscover.xml    

Exchange Control Panel https://mail.exoip.com/ecp    

Exchange Web Services https://mail.exoip.com/EWS/Exchange.asmx    

MAPI over HTTP https://mail.exoip.com/mapi    

Exchange ActiveSync https://mail.exoip.com/Microsoft-Server-ActiveSync    

Offline Address Book https://mail.exoip.com/OAB    

Outlook Web Access https://mail.exoip.com/owa    

PowerShell https://mail.exoip.com/powershell    

Outlook Anywhere mail.exoip.com    

The ip of the various virtual directories points to the balancer and everything works correctly.    

Now my company has taken a remote office where there are about 100 users.    

I would like if it were possible to install a third exchange node here and create the 100 mailboxes here. These mailboxes would not be part of the DAG. Is it possible?    

How should I configure the virtual directories in this exchange?    

Thank you    

Greetings

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-05*

AndyDavid and KyleXu-MSFT thanks for the replies.    

Excuse my ignorance but I have never configured an exchange infrastructure split on two different locations and I would not want to do any damage.    

KyleXu-MSFT the link you gave me talks about active copies of the database for which I guess a DAG has been implemented.    

Do the configurations proposed in the Client Connectivity in an Exchange 2016 Coexistence Environment with Exchange 2013 link work in my configuration?    

If I choose to use the first site configuration for the second site the as the Internet facing site from what I understand, the exetrnalURLs of the virtual directories must be $ NULL that is without any value. Correct?    

What value should internal url have?    

Do I always have to use the url mail.contoso.com which in the dns points to the load balancer (the load balancer then divides the load to the site 1)?    

AndyDavid in my scenario I use the split-brain DNS infrastructure for which also in the second site the dns records of the exoip.com domain are resolved by this dns.    

Since the dns records, for the exoip zone, that are there now point to the load balancer located in the first site in the second site, do I have to use a different name with for example mail2.exoip.com?    

The exchange server in the second site will be called exch02 and the remote Active Directory site will be called Remote Office.    

So to make the autodiscover use the exch02 server in an authoritative way for the remote offfice site, I have to type:    

Set-ClientAccessServer -Identity "exch02" -AutoDiscoverServiceInternalUri "https://mail2.exoip.com/autodiscover/autodiscover.xml" -AutoDiscoverSiteScope "Remote Office"    

Correct?    

Does the autodiscover dns records always have to point to the load balancer and then the autodiscover service redirects the user base to the serevr to which it belongs?    

Thank you    

Greetings

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-05*

@pazzoide76      

Here are two ways for you second site.     

You could use first site the as the Internet facing site for the second site. In this way, Internet client request will be redirected from the first site to the second site. (As the relationship between the site 1 and site 3 in the following blog)    

You can also configure the second site as a stand-alone Internet facing site. (As the relationship between the site 1 and site 2 in the following blog)    

    

For more detailed information, you could have a look about this article (it same to configure for third Exchange 2016): Client Connectivity in an Exchange 2016 Coexistence Environment with Exchange 2013    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
