---
title: "My active Domain Domain controller stopped working while i was creating a domain account, on further analysis the AD DS and AD CS services were disabled, I tried enabling them in vain. On the server manager there is a notification for post-deployment conf"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5638975/my-active-domain-domain-controller-stopped-working
question_id: 5638975
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# My active Domain Domain controller stopped working while i was creating a domain account, on further analysis the AD DS and AD CS services were disabled, I tried enabling them in vain. On the server manager there is a notification for post-deployment conf

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5638975/my-active-domain-domain-controller-stopped-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Has 

has anyone ever experienced this issue, and how do i resolve it to avoid disruptions, note users can still authenticate and login to the domain, however am afraid if i restart the server i may lose access and users fail to login. Please help.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 1 · updated: 2025-11-28*

Hello @Jones Kioko Waka  

Hope you have a nice day!

It appears that the computer where you are creating the user cannot contact a Global Catalog (GC). Please help make sure the GC server is online and available. 

To verify, you can list the available GCs using bellow cmd:

```
dsquery server -domain  | dsget server -isgc -dnsname
```

Next, test connectivity by Ping the GC servers. Make sure TCP port and port 3268 are not blocked

-  Use Telnet on port `3268` (e.g., `telnet <GC-hostname> 3268`) or run PortQry (https://www.microsoft.com/en-us/download/details.aspx?id=17148) to check connection on port 3268, which is required for Global Catalog access.  

If you believe this information adds some value, please accept the answer so that your experience with the issue would help contribute to the whole community.

Regards,

Kate
