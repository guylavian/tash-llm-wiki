---
title: "SCCM PXE boot/IP Helper"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1003044/sccm-pxe-boot-ip-helper
question_id: 1003044
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-deployment", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SCCM PXE boot/IP Helper

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1003044/sccm-pxe-boot-ip-helper (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Currently we are using DHCP to PXE boot but I would like to setup IP helpers.    

We already have IP Helpers for DHCP servers.    

How do we add IP helpers for PXE boot servers.    

Do I need to create new line for IP helper and add each DP (PXE) to each site switch or it has to be primary site IP address?    

We have 5 sites with DP which are also PXE servers

## Answer (community) — community member

*upvotes: 1 · updated: 2022-09-12*

Hello there,    

For PXE requests, you just need to configure the routers to forward the client request to the PXE server, just like you do with the DHCP server. Locate your router, find the DHCP IP helper entry, and add another entry that looks exactly like the first one but uses the IP address of the PXE server. For more information, see the blog post You want to PXE Boot? Don't use DHCP options.    

https://techcommunity.microsoft.com/t5/configuration-manager-blog/you-want-to-pxe-boot-don-t-use-dhcp-options/ba-p/275562    

Besides, you can add an IP helper entry for each PXE server. In a load-balancing scenario (multiple PXE servers), PXE servers can be up or down in a group, and you don't have to do any extra configuration. In diverse environments (Windows, Linux, and Router PXE servers all coexisting), the different PXE servers can selectively respond to the clients that they recognize.    

https://learn.microsoft.com/en-us/troubleshoot/mem/configmgr/boot-from-pxe-server    

------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-12*

Hi,    

Each PXE server should have an entry in the IP helper tables. That way, all the PXE servers will get the client boot discovery and request, and only the PXE that needs to respond will respond. The configuration is like this:    

IP helper-address <IP address of DHCP server>    

IP helper-address <IP address of PXE server>    

IP forward-protocol UDP 4011     

In an environment where there are multiple PXE servers, each PXE server will only reply to the clients that it cares about. In the case of SCCM, the SCCM PXE server only cares about its own clients and will only respond to those clients that have task sequence deployed to them.    

Refer to: IP Helper-Address Configuration for PXE Boot    

Thanks for your time,    

Best regards,    

Simon    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
