---
title: "Metadata Cleanup of a Domain controller - SERVER 2012R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/216173/metadata-cleanup-of-a-domain-controller-server-201
question_id: 216173
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Metadata Cleanup of a Domain controller - SERVER 2012R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/216173/metadata-cleanup-of-a-domain-controller-server-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

For Server 2012R2: After a DC is dead, we have to use the following to cleanup metadata:    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

As far I understand, this will not remove the DNS records of this dead domain controller. We have to remove the DNS records manually.    

Do we also have to delete DNS records in root domain (example.com) of DNS? Or do we only delete the DNS records from _msdcs.root domain ( _msdcs.example.com)? As far as I understand, there are always two zones for domain example.com:    

example.com and _msdcs.example.com

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-06*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-03*

Hi,  

As far I understand, this will not remove the DNS records of this dead domain controller. We have to remove the DNS records manually.  

Some DNS records  can't be deleted automatically, you have to check and cleanup DNS records manually (NS,SRV,A,AAAA).  

Do we also have to delete DNS records in root domain (example.com) of DNS? Or do we only delete the DNS records from _msdcs.root domain ( _msdcs.example.com)? As far as I understand, there are always two zones for domain example.com:  

example.com and _msdcs.example.com  

Yes you should delete all DNS records of deleted domain controller in the different domains example.com and _msdcs.example.com.  

Please don't forget to mark helpful reply as answer

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-01*

This one may help to that end.  

https://devblogs.microsoft.com/scripting/clean-up-domain-controller-dns-records-with-powershell/  

--please don't forget to Accept as answer if the reply is helpful--
