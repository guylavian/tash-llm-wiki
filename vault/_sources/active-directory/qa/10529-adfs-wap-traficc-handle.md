---
title: "ADFS - WAP traficc handle"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/10529/adfs-wap-traficc-handle
question_id: 10529
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS - WAP traficc handle

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/10529/adfs-wap-traficc-handle (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!    

My ADFS solution idea looks like this:    

Internet  to FW to NLB to WAP1 and WAP2 to FW to ADFS1/ADFS2/ADFS3/ADFS4 to AD.    

The NLB distribute the incoming traffic to the WAP servers (Round-robin) and the WAP servers distribute the traffic to the ADFS servers. Now the question is: How does the WAP works? Do they choose a specific ADFS server all the time or do they distribute the trafic (requests) between diferent ADFS servers?    

Do I need one WAP for every ADFS server or can I have a WAP serve plenty ADFS servers in a farm?    

\EC

## Answer (community) — community member

*upvotes: 0 · updated: 2020-03-03*

Thanks for your answer Piaudonn! But I don't get the answer I want:     

From Internet to FW to NLB (F5) to WAP1 and WAP2 to FW to ADFS1/ADFS2/ADFS3/ADFS4 to AD.    

The NLB (F5) distribute the traffic (requests) between the WAP1 and WAP2. But how the traffic goes to the ADFS servers from the WAPs? How choose the WAPs a ADFS server? The WAPs seems not to have a own LB funktion så how do they when they choose if there are many ADFS serves? Do I need an other NLB between the WAPS and the ADFS to get LB?    

\EC

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-03-02*

Hello -     

Are you using NLB or DNS round-robin? Neither are great for network load balancing :) The NLB feature on Windows is agnostic of the state of the service running on the top of the stack. So if you stop the ADFS service, unless you are using some automation (or SCOM management pack) the NLB will still redirect some traffic to the node. And DNS round-robin, well, same problem, unless you are using some automation with DNS policies (DNS policies are a Windows Server 2016 feature) you don't know if the user will end up using a healthy node, and if the TTL is high, then the client might even cache the result of a broken node.    

You can use the aforementioned two as long as you understand and accept the risks of their associated shortcomings. Ideally you would use a hardware load balancer.    

WAPs find their ADFS servers (or rather its associated farm) using DNS by resolving the FQDN of the ADFS farm it is attached to.    

Regarding the number of ADFS and WAP and their pairing there are no rules. You can have 3 WAPs and only 1 ADFS servers (weird scenarios if WAPs are only used as ADFS proxy and not used to publish applications), you can have 1 WAP and 3 ADFS servers (if you don't have that many external clients - and that you don't mind the single point of failure). As long as the WAP can talk to the ADFS farm you are good to go. And they don't need to talk to a particular node. As a matter of fact, the WAPs can also reach out to the ADFS servers through the load balancing. Sometimes you can pair WAP and ADFS servers to make troubleshooting slightly easier as you will know that if the user hits WAP 1 they will use ADFS 1.    

You want the network latency to be low between the WAP and the ADFS server though. Just to make sure the user's experience is not negatively affected. So if you have ADFS servers across different geographical regions, it might make sense to use (in priority, not necessarily "hardcoded") the local ADFS server.
