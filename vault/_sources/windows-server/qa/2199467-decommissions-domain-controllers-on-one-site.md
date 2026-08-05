---
title: "decommissions domain controllers on one site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199467/decommissions-domain-controllers-on-one-site
question_id: 2199467
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# decommissions domain controllers on one site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199467/decommissions-domain-controllers-on-one-site (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI everyone.

Just seems easy question but i want to be sure in my action.

We have 3 different sites with mpls connection between .

Each site content 2 DC's

We need to demote one site dc completely. Lets say it site 3. The PDC emulator  on site 1.

Here is my action plan.

1, On the site 3 (that what going to be demoted) on DHCP scope option Change  DNS settings to IP dc from site 1

-  Change all static IP dns on servers on each server in site 3

-  In Active directory Sites  subnets related to site 3 move to site 1

Start decommission  2 dc on site 3 without remove DHCP server.

Please suggest if I forgot any additional steps. The target get users from site 3 (where I'm going to decommissions DC)  connect (login) with Site 1

Many Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-19*

Many thanks for your help.

 I made a change in the DHCP scope Dns settings  and check how many computers  authenticated with site3.

I use PowerShell  command :

Get-WmiObject Win32_LoggedOnUser | Select Antecedent -Unique

to get actual information and track authentication login.

1.Can you  please maybe suggest some script or applications that's allow collect information from all dc's in one.

Event viewer it is nice , but not comfortable when you want to see all in one 

Many Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-19*

Hi Jeff,

Thank you for posting in the Microsoft Community Forums.

Your action plan is already fairly comprehensive, but to ensure the least amount of disruption and risk possible when downgrading the DC at Site 3, here are some additional steps and recommendations for you to consider:

-  Preparation

Backup: ensure that a full backup of all DCs at Site 3 is taken. This includes system state backups, AD database backups, and backups of any critical data, as well.

Documentation: Record the current configuration and status of all DCs in Site 3, including IP addresses, DNS settings, replication partnerships, and so on.

Notify Users: Notify Site 3 users and administrators in advance about upcoming maintenance activities so they can be prepared.

-  DNS Changes

DHCP Scope Changes: You have planned to change DNS settings in the DHCP Scope option, which is a good first step. Make sure that these changes are applied correctly in the DHCP scope and that the scope has been reactivated.

Static DNS Changes: In addition to DHCP-assigned clients, check and update the DNS settings for all servers and devices with static IP addresses in Site 3.

Verify DNS resolution: After changing the DNS settings, verify that the clients in Site 3 are able to properly resolve and connect to the new DNS servers (DCs in Site 1).

-  Active Directory Adjustment

Subnet reassignment: move the subnet in Site 3 to the AD site configuration in Site 1. This helps ensure that Kerberos authentication and other AD services are properly routed to the nearest DC.

Site Linking and Replication: Check and adjust the site linking and replication settings to ensure that Site 1's DC can continue to effectively serve the users and servers at the original Site 3.

Best regards

Neuvi Jiang
