---
title: "Exchange 2016 in resource forest port requirments"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/133144/exchange-2016-in-resource-forest-port-requirments
question_id: 133144
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Exchange 2016 in resource forest port requirments

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/133144/exchange-2016-in-resource-forest-port-requirments (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,   

What are the communication ports required between exchange mailbox servers deployed in a resource forest and domain controllers in account forest.  

Is there any documentation for this type of deployment?

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-21*

@EhabNafea-6156     

I did some research, but cannot find any official documents explain what ports are needed for Exchange in resource forest to connect to DCs in account forest. Based on my knowledge, the required ports you are looking for should be included in those needed for AD forest trust. You can check this blog for what ports should be unblocked between two forests: Active Directory Forest Trust: Attention Points.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-20*

Well, that's what is supported. :) Here is another similar doc that you can use to determine the ports, but , again, blocking anything make work just fine, but it's not supported so if you run into any issues, keep that in mind!     

Notice that they say " in any and all types of topologies". So that would include resource forests.    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/network-ports?view=exchserver-2019    

We do not support restricting or altering network traffic between internal Exchange servers, between internal Exchange servers and internal Lync or Skype for Business servers, or between internal Exchange servers and internal Active Directory domain controllers in any and all types of topologies. If you have firewalls or network devices that could potentially restrict or alter this kind of internal network traffic, you need to configure rules that allow free and unrestricted communication between these servers: rules that allow incoming and outgoing network traffic on any port (including random RPC ports) and any protocol that never alter bits on the wire.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-20*

its not supported to have any firewall rules that prevent communication between Exchange and Domain Controllers or to other Exchange Servers  

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-firewalls-and-support-8230-oh-my/ba-p/595710  

Starting with Exchange Server 2007 and current as of Exchange Server 2013, having network devices blocking ports/protocols between Exchange servers within a single organization or between Exchange servers and domain controllers in an organization is not supported. A network device may sit in the communication path between the servers, but a rule allowing “ANY/ANY” port and protocol communication must be in place allowing free communication between Exchange servers as well as between Exchange servers and domain controllers.
