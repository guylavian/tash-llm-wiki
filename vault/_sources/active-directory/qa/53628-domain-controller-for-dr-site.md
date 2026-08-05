---
title: "Domain Controller for DR Site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/53628/domain-controller-for-dr-site
question_id: 53628
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Domain Controller for DR Site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/53628/domain-controller-for-dr-site (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
We're in the process of adding one domain controller in a different site for disaster recovery, but we don't want users to be authenticated from this DC and/or use the DNS server in the DR site.
```

is there a way to specify that the new DC in the DR site will have lowest priority for DNS and authentication ?  

also it would be highly appreciated if you shared best practices guide for adding a new DC in a DR site.   

Thank you.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-07-31*

Hi,  

   

Just checking in to see if the information provided was helpful. Please let us know if you would like further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-03*

Hi,  

   

Just want to confirm the current situations.  

   

Please feel free to let us know if you need further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-29*

By default all dc's have a priority of 0, the lower the priority the first in priority.  The dc with the lowest priority in the site will receive ALL authentication requests unless it is unavailable.  If the lowest priority dc is unavailable then the next lowest dc in the site will receive all requests, etc…  

To modify the priority of a dc the registry key, use:  

 HKLM\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\LdapSrvPriority  

Hope this information can help you  

Best wishes  

Vicky
