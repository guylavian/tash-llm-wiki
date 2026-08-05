---
title: "Intra-Site latency only for Active Directory DNS zones"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1099534/intra-site-latency-only-for-active-directory-dns-z
question_id: 1099534
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Intra-Site latency only for Active Directory DNS zones

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1099534/intra-site-latency-only-for-active-directory-dns-z (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello support,

we've 2 DCs in the same site that are currently working for AD changes.  

Same DCs have delays in replicating DNS zone (AD integrated): replica can take few seconds up to few minutes to replicate.  

We see that every DC in the same zone has:  

* itself in SOA  

* a different serial

Can someone help us to identify the root cause?

Thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-07*

Hi @Anonymous   ,    

i'm an @Andrea Cerrito   partner,    

following log report requested    

268079-rep1.txt268165-rep2.txt268115-repsumcsv.txt    

Serial-numbers (NOW):    

_msdcs SN is 258 on ADNODE-1 (SiteB) e ADNODE-3 (SiteC) and 259 on ADNODE-2 (SiteB)    

new.mydomain.it SN is same on all nodes.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-11-25*

Hello AndreaCerrito-0508,    

Thank you for posting in our Q&A forum.    

Please run the following commands to on PDC and check the result.    

repadmin /showrepl C:\rep1.txt    

repadmin /replsum C:\rep2.txt    

repadmin /showrepl * /csv >c:\repsum.csv    

If all the results are OK, it seems AD replication works fine.    

We can see "By default, this interval is 15 seconds in Windows Server 2003 and later versions." in the link below.    

How to Modify the Default Intra-Site Domain Controller Replication Interval    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/modify-default-intra-site-dc-replication-interval    

Also, I can see different "Serial Number" in forest zones and domain zones on one DC, but they are the same result on different DCs.    

I mean "Serial Number" is 16 in forest zones on DC1,    

and "Serial Number" is 368 in domain zones on DC1.    

I mean "Serial Number" is 16 in forest zones on DC2,    

and "Serial Number" is 368 in domain zones on DC2.    

    

    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
