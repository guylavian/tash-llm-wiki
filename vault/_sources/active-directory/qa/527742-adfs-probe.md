---
title: "ADFS probe"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/527742/adfs-probe
question_id: 527742
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Volunteer Moderator"]
---
# ADFS probe

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/527742/adfs-probe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

If i install ADFS only without wap , can i use probe by loadbalancer?  

I cannot find the probe in my ADFS at all!!

## Answer (community) — Volunteer Moderator

*upvotes: 1 · updated: 2021-08-31*

Hello @yasser Mohamed AbdelMoneim  ,    

Thanks for reaching out.    

ADFS HTTP based probe endpoint introduced from 2016 server, the HTTP probe can be accessed over HTTP using the path ‘/adfs/probe'    

-  http://<Web Application Proxy name>/adfs/probe    

-  http://<ADFS server name>/adfs/probe    

-  http://<Web Application Proxy IP address>/adfs/probe    

-  http://<ADFS IP address>/adfs/probe    

It is recommended to use the HTTP (not HTTPS) health probe endpoints to perform load balancer health checks for routing traffic. This avoids any issues relating to SNI. The response to these probe endpoints is an HTTP 200 OK and is served locally with no dependence on back-end services.     

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/overview/ad-fs-requirements#BKMK_7    

Hope this helps.    

------    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
