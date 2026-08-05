---
title: "ADFS cluster can't start WAP service when using VIP on NLB"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/513885/adfs-cluster-cant-start-wap-service-when-using-vip
question_id: 513885
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
---
# ADFS cluster can't start WAP service when using VIP on NLB

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/513885/adfs-cluster-cant-start-wap-service-when-using-vip (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. I have ADFS cluster: two adfs servers and WAP cluster: two wap servers.  

adfs1 has ip 192.168.30.63  

adfs2 has ip 192.168.30.64  

VIP for ADFS cluster is 192.168.30.65  

wap1 has ip 192.168.30.60  

wap2 has ip 192.168.30.62  

VIP for WAP cluster is 192.168.30.66  

WAP cluster on my load balancer is working ok.  

When I set in host file in wap1 ip address of adfs cluster as "192.168.30.65 adfs.mycompany.com" WAP service doesn't start. When I use in host file ip address of adfs1 or adfs2 servers it is working ok.  

PLease help me. How can I use adfs cluster VIP?  

Why it doesn't work?   

I can open the page https://adfs.mycompany.com/adfs/ls/idpinitiatedsignon with 192.168.30.65 and other ips of adfs servers. Maybe I need to use other ports apart from 443 for NLB VIP?

## Answers

_No answers on this thread._
