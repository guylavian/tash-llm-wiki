---
title: "Can log into ADFS internally but not externally"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/872051/can-log-into-adfs-internally-but-not-externally
question_id: 872051
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Can log into ADFS internally but not externally

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/872051/can-log-into-adfs-internally-but-not-externally (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,   

I have an ADFS server built internal to my environment, it federates to a SaaS platform that we use for CRM.  When on internal do our domain the federation works fine, but when outside of the domain there is no response from the server.  Interestingly, when outside of the domain I can ping both the IP and the DNS name of the ADFS server and I can telnet to the server on 443 and 80.  But when I try to access the URL to the SaaS or to our DNS name it times out.  We do not use a DMZ and internally I modify the hosts file on each machine so that they don't try to resolve externally first.  Any thoughts here.   

Thanks,   

Brandon

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-01-31*

First, I would suggest running a packet capture from the internal network and from the external network to see if there is a difference in the traffic being sent. This will help you identify if there is a firewall rule or routing issue that may be preventing the traffic from reaching the ADFS server. If there is no difference in the traffic, then it could be an issue with the ADFS server itself. I would suggest checking the event logs on the ADFS server to see if there are any errors that could be related to the issue. Additionally, you may want to check to make sure that the SSL certificate is configured correctly and that the DNS entries for the ADFS server are properly configured.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-22*

You should not be exposing ADFS directly to the internet. See https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/best-practices-securing-ad-fs. We also have guides on how to migrate off ADFS https://techcommunity.microsoft.com/t5/community-events-list/microsoft-workshops-how-to-successfully-migrate-away-from-ad-fs/m-p/3668480 & https://www.microsoft.com/en-us/security/business/identity-access/upgrade-adfs
