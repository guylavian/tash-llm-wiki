---
title: "Physically moving Exchange 2013 Server to new location (Away from DC's)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/170115/physically-moving-exchange-2013-server-to-new-loca
question_id: 170115
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Physically moving Exchange 2013 Server to new location (Away from DC's)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/170115/physically-moving-exchange-2013-server-to-new-loca (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey all,  

Recently a customer needs their Exchange 2013 server moved to a new location due to power issues (new location has a generator). The new site is not far away at all (1 mile~), but it is on a different network.  

All of the DNS and IP issues should be straightforward and easy, we work closely with our ISP and will be able to keep the current WAN settings so no changed will be needed there.  

What I'm worried about it that I will be moving the Exchange server away from the Domain Controllers. I created a VPN tunnel between the current and new site, but will that work with what I'm doing? Will the Exchange server at the new site see the DC's via VPN tunnel that I created and recognize new users added in the DC's?  

If anyone has any tips or suggestions I'd love to hear them.   

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-20*

Yes, you can use the PortQryUI tool   

https://www.microsoft.com/en-us/download/details.aspx?id=24009  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-20*

Thanks for the quick reply.  

Is there a good way to test that all the ports are correctly opened before I physically move the server to the new location?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-20*

Just make sure the ports are flowing between sites.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/network-ports?view=exchserver-2019    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements    

https://www.microsoft.com/en-us/download/details.aspx?id=24009    

--please don't forget to Accept as answer if the reply is helpful--
