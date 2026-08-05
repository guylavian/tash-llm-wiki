---
title: "ADFS farm - Secondary server HTTP ERROR 400"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/982101/adfs-farm-secondary-server-http-error-400
question_id: 982101
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS farm - Secondary server HTTP ERROR 400

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/982101/adfs-farm-secondary-server-http-error-400 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I've been trying to create and ADFS farm for my org. I managed to create a standalone server with a wildcard certificate and it is behaving as expected. For redundancy, I wanted a second server in the farm that could handle the SAML requests if the primary server is down. So, I've added a second server to the existing farm. However, when I try to test sign in on the secondary server https://adfs-server-2.domain.com/adfs/ls/idpinitatedsignon.aspx I get the HTTP ERROR 400. I'm not sure what I missing. I have tried to go through quite a few MSDN articles and MS forums but to no avail.     

I am not seeing any errors under the 2nd server's Event Viewer -> Application and Service Logs -> ADFS -> Admin.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-08-25*

You cannot access the second server by its server name. AD FS uses the SNI extension of TLS. You can only establish a connection using the FQDN of the farm. And if you have 2 servers, you need a load balancer technology on the front (and the FQDN of the farm has to resolve to the load balanced IP address).    

If you want to test your second server, you can configure the HOSTS file of you machine to make the FQDN of the farm point to a specific node.
