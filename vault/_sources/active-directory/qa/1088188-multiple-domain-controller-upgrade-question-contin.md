---
title: "Multiple Domain Controller Upgrade Question (continue)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1088188/multiple-domain-controller-upgrade-question-contin
question_id: 1088188
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Multiple Domain Controller Upgrade Question (continue)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1088188/multiple-domain-controller-upgrade-question-contin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

continue from this post  

https://learn.microsoft.com/en-us/answers/questions/1086643/challenging-multiple-domain-controller-upgrade-que.html

5) for 4, on location D, the DC has a DHCP service, assigning ip 192.168.4.x to all its device.  

location A has 192.168.1.x , and location B has 192.168.2.x , and location C has 192.168.3.x subnet.  

assume we have a direct secure line between A,B,C,D location.  

do you know how I can remove the DC in location D, and assign all the device in location D to location C?

note,  

2 parent DC, all its device windows login domain is example.com  

all 4 child DC, all its device windows login domain is fe.example.com  

which mean location A, B, C, D share the same windows login domain "fe.example.com"

6) I know  

6.1 PC use config "obtain an ip address automatically" and "obtain DNS server address automatically" from DHCP server.  

6.2 and DHCP server got a IP limited time until that IP expire and ask the DHCP server to get a new or renew the current ip.  

what I don't understand is, in location D, after its PC joining a domain fe.example.com ,  

how does it know to get the 192.168.4.x subnet ip, and not the location A 192.168.1.x subnet IP?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-14*

do you know the answer to Q5?    

Should just be a matter of configuring the VPN clients to connect to the C location. Then once done you can demote / decommission D domain controller.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
