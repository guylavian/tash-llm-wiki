---
title: "Challenging Multiple Domain Controller Upgrade Questions (parent and child)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1086643/challenging-multiple-domain-controller-upgrade-que
question_id: 1086643
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Challenging Multiple Domain Controller Upgrade Questions (parent and child)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1086643/challenging-multiple-domain-controller-upgrade-que (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am new to this domain controller and new to the company.    

all the below domain controller are in windows 2008.    

we got two parent controller    

-  parent-DC1-2008.example.com    

-  parent-DC2-2008.example.com    

we got 4 physical location office, each location has its own child controller,     

all the location office domain controller connected to the parent controller above.    

and they are    

-  locationA-DC1-2008.example.com    

-  locationA-DC2-2008.example.com    

-  locationB-DC1-2008.example.com    

-  locationB-DC2-2008-read-only-for-wifi.example.com    

-  locationC-DC1-2008.example.com    

-  locationD-DC1-2008.example.com    

now due to budget, the company only upgrade the below domain controller to windows 2016.    

-  locationA-DC1-2016.example.com    

-  locationB-DC1-2016.example.com    

-  locationC-DC1-2016.example.com    

which mean, the below domain controller are not upgraded    

-  parent-DC1-2008.example.com       (keep as its)    

-  parent-DC2-2008.example.com       (keep as its)    

-  locationA-DC2-2008.example.com    (will decommission)    

-  locationB-DC2-2008-read-only-for-wifi.example.com    (will    

   decommission)    

-  locationD-DC1-2008.example.com    (will decommission)    

now the questions.    

1 if we only upgrade the child domain controller to 2016, and not the parent domain controller, will it work?    

2 for location A, original 2 domain controller, after upgrade only have 1, will it work?    

what I really mean is, what if some of the device hard code to use the 2nd domain controller?    

how do we find out those device?    

3 for location B, I got no idea why there is a read only DC for wifi.    

if this got decommission, what is the best way to handle it?    

force the location B wifi to use the main location B DC? is that a security concern    

4 for location D, we still got some limited device there,     

is it possible to vpn all these device and use the domain controller in other location?    

thank you for taking your time to reading this, much appreciated.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-14*

To promote clarity in forums it is suggested to limit each thread to a single question. I already answered four, please close this one by marking answer and start a new thread for additional questions. Thanks for understanding.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-14*

you are awesome, just got more question.    

Glad to hear and you're quite welcome. Please close up this thread by  and open a new one for these new asks.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-13*

where do you recommend I place the wireshark to sniff out the hard code dc?    

You could do the wireshark from anywhere on the same network.    

do you recommend to use some vpn device like firewall/peplink/cisco in the final hub, to vpn to the other site?    

I don't see a problem with that idea.    

I know ldap is using 636 port of DC to do verify, do you know another service and port that will use the DC?    

You'll find the ports required listed here.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts#windows-server-2008-and-later-versions    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
