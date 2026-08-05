---
title: "How to add Domain Controllers in Load balancer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297022/how-to-add-domain-controllers-in-load-balancer
question_id: 297022
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to add Domain Controllers in Load balancer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297022/how-to-add-domain-controllers-in-load-balancer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 6 domain controllers  placed in different region APAC, EMEA and AMS. Is there any way to put them in load balancer method like I put them behind F5 LB.  

Also,  

I migrated my DC01 to DC02. I swapped the IP address. However, DC name is changed. If I create a CNAME pointing DC01 to DC02 , will it work???

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-03-05*

Hi,  

Welcome to share here!  

For the  F5 LB configuration , i'm afraid i can't give you any professional advice.  

I would suggest you ask advices from the vendor of the F5 LB.  

For the DC migration, you mean the old DC was demoted and removed from the domain,  and the new DC(DC02) was configured with the old IP address of DC01, but with a new name, right?  

If so , we just need to run the following command to update the DNS records for the new DC:  

 ipconfig /flushdns   

 ipconfig /registerdns   

 net stop netlogon && net start netlogon  

Best Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-16*

Actually, I just hate coming on this QnA page. It is worst whatever I saw in my whole career. Social technet was very good but this page, god damn bullshit.   

Well, I am checking with F5 and we can close this ticket. I prefer some other site for tech questions not this useless QnA portal of MS
