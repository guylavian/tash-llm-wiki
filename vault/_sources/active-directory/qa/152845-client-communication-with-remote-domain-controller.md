---
title: "Client communication with remote domain controller - Best Practice?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/152845/client-communication-with-remote-domain-controller
question_id: 152845
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Microsoft Moderator"]
---
# Client communication with remote domain controller - Best Practice?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/152845/client-communication-with-remote-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have several remote sites all on a single domain. Through firewall policies, clients can not communicate with clients at other locations. We do allow DC's to talk to each other.  One situation I realized is happening today is Clients can sometimes not ping domainname.com because DNS gives them a DC outside of the site which they can't communicate with.  I'm assuming that this would also affect group policy as the client can not reach the sysvol on the remote DC.  

What is the best practice for clients at remote sites? should all clients in the domain be able to communicate with all DC's in the domain? My google-fu was weak on this one and couldn't find any documentation on this specific topic.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Thank you for your comment. However, the suggestion you provided is not correct for this situation. Finding the closest DC via the dclocator process for authentication purposes is not the same as pinging the domain name and getting a response. Ping is not site-aware... when a request is made to the DNS server to resolve domainname.com a random DC in the network is presented in more like a round-robin fashion. Because of our network firewalls many DC's do not respond to ping.   

The reason I see our current configuration as an issue is if lets say I wanted to deploy a GPO script or shortcut and the location of these is \domainname.com\NETLOGON...  If the domainname.com doesn't resolve via DNS to a local DC then the client can not get the file.  I hope this more clearly explains what I am asking.  

Should all clients in the domain be able to communicate with all DC's in the domain?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

 Vicky

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-05*

Hi,    

The best practice is to align the active directory topology with your network topology. I recommend you to to perform the following actions through the console "sites and services active directory":    

-  Create a active directory site for each remote site    

-   Move the closest domain controller on active directory site    

-  Create a subnet for each remote physical site and assign it to the active directory site where there is the closest domain controller    

Once you complete those steps, the client will find the closest domain controller based on active directory topology via dclocator process.    

active-directory-replication-concepts    

Please don't forget to mark this reply as answer if it help you to fix your issue
