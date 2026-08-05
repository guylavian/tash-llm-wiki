---
title: "adfs migration 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/329991/adfs-migration-2019
question_id: 329991
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# adfs migration 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/329991/adfs-migration-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Current environment: Load balancer --> Two WAP servers (each wap has local host dns file pointing to a specific adfs server) --> two adfs servers. Version is 3.0. and database is hosted in external SQL server with adfsconfiguration and artifact databases.     

My plan:    

Create a new 2019 in parallel with 2 wap and 2 adfs. But this time I do not want to host the database externally and use WID for new environment. So, one of the adfs server will be primary and the other secondary. My questions then:     

-  What should the architecture be like? Eg. with new WAP behind network load balancer how to best set up the backend adfs with WID since one acts as primary and the other secondary? Is it still required that the local host file of each wap point to a specific adfs? Trying to understand how the requests would be routed from load balancer to wap to adfs in such case.     

-  The current environment has custom onload.js for appending the domain name to the username and also some changes on the default placeholder names. What is the best way to migrate the current config and settings to the new one?     

-  I am not sure if artifact database is used in the current scenario. It sounds like with WID option the artifact db doesn't get installed. How to verify if that is being used currently? Or, does it even make any difference?     

It would be nice to be able to create an environment in parallel, have configs and settings from current migrated over, test, and then cutover at convenience. Couldn't find a good documentation that provided at least an overview for such scenario. Most point to doing an inplace upgrade.     

I have gone through     

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/upgrading-to-ad-fs-in-windows-server     

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/upgrading-to-ad-fs-in-windows-server-sql

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-03-25*

What you could do for a start is use ADFS Rapid Restore to backup your currentenvironment and restore it using WID. So you would get rid of SQL (upgrade with SQL is often more complicated).    

Once you have a classic ADFS on Windows Server 2012 R2 on WID, you can add Windows Server 2019 nodes to the existing farm. And you don't have to put them on the load balancer yet. That way you can test them by using a HOSTS file on your machine.     

Then you can configure your load balancer to use only the 2019 (but you keep the 2012 R2 for a little while to be able to roll back if needed).    

And finally, when you are confident that the 2019 nodes are doing the job, you remove the 2012 R2 nodes and raise the behavior level of the farm.    

All your JS customizations will be kept in the process as well as you entire configuration. The tweak you would have to do is if you enabled the SAML RelayState for IDP-initiated flow (as it used to be done in the .configfile on each server in 2012 R2 and is now a config to do with PowerShell in 2019).
