---
title: "ADFS authentication (intranet) for Cloud Users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/89351/adfs-authentication-intranet-for-cloud-users
question_id: 89351
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
---
# ADFS authentication (intranet) for Cloud Users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/89351/adfs-authentication-intranet-for-cloud-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys,  

I have a sitution, we have a situation in which we want to use ADFS authentication for users accessing Office online.  

We only want users who are a part of Intranet ( either connected to LAN or VPN ) to access office apps outside of it is not allowed . This means , we dont need ADFS Proxy Servers in DMZ.  

Question is :  

Once we install ADFS in intranet ( no proxy) , and just convert the domain in Azure from managed to Federated. It should work right ?  

Any specific firewall related things i need to consider as my concern is that the Azure AD in the public internet will redirect the user to On-premise ADFS ( no proxy ) in Intranet.  

Over all picture -  

Domain in Azure AD (verified) - abc.com  

On-premise ADFS DNS ( load balancer ) - sts.xy.abc.com  

Your inputs would be very helpful.  

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-09*

Hello @Anonymous  , Please find below the port, load balancer and DNS requirements:    

Port requirements:    

For this scenario to work, you need to have TCP port 443 enabled inbound on the firewall. If you want to perform user certificate authentication, TCP port 49443 also needs to be enabled inbound on the firewall as the certauth endpoint on port 443 is not enabled by default (can be configured for port 443). If firewall blocks 49443 or interferes with user certificate authentication traffic, you will see a blank screen or a 500 server error during certificate based authentication.    

Load Balancer requirements:    

-  The load balancer MUST NOT terminate SSL. AD FS supports multiple use cases with certificate authentication which will break when terminating SSL. Terminating SSL at the load balancer is not supported for any use case.    

-  It is recommended to use a load balancer that supports SNI. In the event it does not, using the 0.0.0.0 fallback binding on your AD FS should provide a workaround.    

-  It is recommended to use the HTTP (not HTTPS) health probe endpoints to perform load balancer health checks for routing traffic. This avoids any issues relating to SNI. The response to these probe endpoints is an HTTP 200 OK and is served locally with no dependence on back-end services. The HTTP probe can be accessed over HTTP using the path ‘/adfs/probe'        http://<ADFS server name>/adfs/probe  

    http://<ADFS IP address>/adfs/probe  

-  It is NOT recommended to use DNS round robin as a way to load balance. Using this type of load balancing does not provide an automated way to remove a node from the load balancer using health probes.    

-  It is NOT recommended to use IP based session affinity or sticky sessions for authentication traffic to AD FS within the load balancer. This can cause an overload of certain nodes when using legacy authentication protocol for mail clients to connect to Office 365 mail services (Exchange Online).    

DNS Requirements:    

-  For intranet access, all clients accessing AD FS service within the internal corporate network (intranet) must be able to resolve the AD FS service name to the load balancer for the AD FS servers.    

-  For extranet access, all clients accessing AD FS service from outside the corporate network (extranet/internet) must be able to resolve the AD FS service name to the load balancer for the AD FS servers.    

-  For Windows Integrated authentication, you must use a DNS A record (not CNAME) for the federation service name.    

-  For user certificate authentication on port 443, "certauth.<federation service name>" must be configured in DNS to resolve to the load balancer for AD FS servers.    

-----------------------------------------------------------------------------------------------------------    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
