---
title: "LAPS installation on Domain controller DC1 and replicated to DC2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/504214/laps-installation-on-domain-controller-dc1-and-rep
question_id: 504214
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# LAPS installation on Domain controller DC1 and replicated to DC2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/504214/laps-installation-on-domain-controller-dc1-and-rep (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I want to configure LAPS on my domain and i have some queries related to installation. Please help on these.

We have DC1 (Primary) and Replicated to DC2 (Secondary).

-   Where should I have to install LAPS? When I run the command 'nltest.exe /dsgetdc: /writable /force'  

    Result: DC2 shows as result.  

    Flags: GC DS LDAP KDC TIMESERV WRITABLE DNS_DC DNS_DOMAIN DNS_FOREST  

    CLOSE_SITE FULL_SECRET WS DS_8 DS_9 DS_10 0x20000

-   If I install it on DC2, would it impact AD environment or replication?

-   How to Install LAPS extension on client side via GPO? As through GPO, LAPS package will install all the features including FAT Client UI, which may show machines password. So how can i install only GPO Extension on client side via GPO?

-   Is Domain admin password will also get changed without any notice? If so domain account will get locked out. Please give me clarification on this.

## Answers

_No answers on this thread._
