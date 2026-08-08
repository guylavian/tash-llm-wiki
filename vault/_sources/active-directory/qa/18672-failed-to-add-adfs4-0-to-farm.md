---
title: "Failed to add ADFS4.0 to farm"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/18672/failed-to-add-adfs4-0-to-farm
question_id: 18672
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Failed to add ADFS4.0 to farm

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/18672/failed-to-add-adfs4-0-to-farm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have two ADFS 3.0 servers and two ADFSproxy servers(DMZ). All located in Azure. The machines all or load balanced.  

Now i try to add a windows 2016 server (ADFS 4.0) on a different VNET but peer with the old VNET.  

When i try to add the ADFS 4.0 (windows 2016 machine) I get this error.  

Unable to retrieve configuration from the primary server. The specified DNS name of the primary federation server could not be resolved.  Verify that the DNS name is correct, and that the AD FS service is running on the primary federation server and try again.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-03-26*

When i open the port 80 on the adfsproxy server. i get another error:  

The HTTP service located at http://****************/adfs/services/policystoretransfer is unavailable. This could be because the service is too busy or because no endpoint was found listening at the specified address. Please ensure that the address is correct and try accessing the service again later.
