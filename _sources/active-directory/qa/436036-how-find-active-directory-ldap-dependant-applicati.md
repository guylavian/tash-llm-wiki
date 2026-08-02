---
title: "how find active directory/ldap dependant application ADDS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/436036/how-find-active-directory-ldap-dependant-applicati
question_id: 436036
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# how find active directory/ldap dependant application ADDS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/436036/how-find-active-directory-ldap-dependant-applicati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

how find active directory/ldap dependent application ADDS is there any tool available. since we migrating ADDS to another forest we need to migrate active directory/ldap dependent applications also.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-29*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-22*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-16*

Hi，    

Thank you for posting in our forum.    

To correctly resolve the managed domain from the on-premises environment, you may need to add forwarders to the existing DNS servers. If you haven't configured the on-premises environment to communicate with the managed domain, complete the following steps from a management workstation for the on-premises AD DS domain:    

Select Start > Administrative Tools > DNS.    

Right-select DNS server, such as myAD01, then select Properties.    

Choose Forwarders, then Edit to add additional forwarders.    

Add the IP addresses of the managed domain, such as 10.0.2.4 and 10.0.2.5.    

reference：https://learn.microsoft.com/en-us/azure/active-directory-domain-services/tutorial-create-forest-trust    

Hope this information can help you    

Best wishes    

Vicky
