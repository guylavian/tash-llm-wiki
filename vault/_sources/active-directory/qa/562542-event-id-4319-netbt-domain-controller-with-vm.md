---
title: "Event ID 4319, NetBT, Domain Controller with VM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/562542/event-id-4319-netbt-domain-controller-with-vm
question_id: 562542
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_affiliations: ["Mvp"]
---
# Event ID 4319, NetBT, Domain Controller with VM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/562542/event-id-4319-netbt-domain-controller-with-vm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am getting the error 4319 on my domain controller that has a hyper-v VM on it.  

The first nic is for the DC, the second one does not have IPv4 protocol checked (I copied the last server).  

Obviously there is a VSwitch also shown for the hyper-v vm which is set to DHCP.  

On the VM, the nic is set to static IP and it shows up in the DNS of the DC with this static IP.  

However, there are two entries in DNS for the DC.  One is the static IP of the first nic and the other is the DHCP address of the VSwitch adapter.  

Is this setup correct?  

If so, why do I get error 4319?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-23*

A better option is to install the hyper-v role (as only role) on host, then stand up a dedicated virtual machine for active directory domain services. Then add other virtual machines for other roles or applications.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-23*

Hello @RiverWild  ,    

This is a logical error and can be ignored as long your services run as expected. The main reason is that Microsoft does not recommend to configure Hyper-V on a Domain Controller precisely for the different interactions that may have over the function of the server.    

In this scenario, you should have 2 NICs in order to assign an interface for DC and another for the VMs to avoid conflict. Even in this case (or if you have only 1 NIC) you are at risk to have what is called a "Multihomed" DC.    

Recommendation is: DC should only have ADDS and DNS, DHCP is even a stretch if you ask me.     

Hope this helps you,    

------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
