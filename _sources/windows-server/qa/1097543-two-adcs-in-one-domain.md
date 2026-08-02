---
title: "Two ADCS in one domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1097543/two-adcs-in-one-domain
question_id: 1097543
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Volunteer Moderator"]
---
# Two ADCS in one domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1097543/two-adcs-in-one-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, i am having a standalone root CA and subordinate CA server is available in our domain. This is an old CS used SHA1 algorithm. I would like to setup or upgrade this old CA to new server with SHA256.     

My Question is    

-  Can i able to create a new standalone root CA and subordinate CA and use SHA 256 template in the same domain?    

-  Two CA in single domain is possible?    

-  Any other way to use SHA256 algorithm in certificates?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-21*

Thanks for your reply.    

So you are suggesting to migrate the CA with new server 2019.    

In my case old server will still be available.     

Also if i migrate to new server, can i able to upgrade the certificate to SHA256? or i need to use old SHA1?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-11-21*

Hi,    

AFAIK, it is not possible and will add complexity to the current setup of issuing certificates and already issued certificates in case the old server is down. I will suggest you to migrate the CA Server to the new server and carry out the migration with all the new settings.    

Also check this link. 0001473    

move-certification-authority-to-another-server    

Hope this helps.    

JS    

==    

Please Accept the answer if the information helped you. This will help us and others in the community as well.
