---
title: "Domain Controller SRV Records remain after DC Demotionn"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/775057/domain-controller-srv-records-remain-after-dc-demo
question_id: 775057
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller SRV Records remain after DC Demotionn

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/775057/domain-controller-srv-records-remain-after-dc-demo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a client that has an issue with SRV records being not removed after a Domain Controller is demoted.  I have to manually search through all sites, _tcp, _udp, etc and manually delete the SRV records.   Additionally after I removed some unused sites in AD Sites and Services, they were partially removed from DNS. There are no errors during demotion, no related errors in DCDIAG and no replication errors. The client's DNS is setup different than I normally set them up but should be fine.  

They have 2 zones (both Active Directory Replicated Zones)  

contoso.com (all host records, srv records, sites etc)  - SRV records are left after DC demotion. Removing sites using AD Sites and Services works here.   

_msdcs.contoso.com (Only SRV records and sites, DC, GC, etc - No host records) - SRV records are left after DC demotion. Removing sites using AD Sites and Services does not work here.    

Has anyone seen this before?  Feels like permissions issue.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-17*

I have a similar issue. I have a Windows Server 2012 R2 server as domain controller(named DC2), then I setup a QNAP TS-831X NAS(named NAS1) to be "additional domain controller" and joined to Active Directory. The NAS suddenly stopped to be domain controller after I changed the domain controller setting of NAS1.  

Since I don't want to give another try, I seized all FSMO roles to DC2, and manully deleted NAS1 from:  

Active Directory Sites & Services > Sites > Servers  

Active Directory Users & Computers > [Domain Name] > Domain Controllers  

But when I remove NAS1 from:  

DNS Manager > Forward Lookup Zones > [Domain Name] > Named Servers tab  

DNS Manager > Forward Lookup Zones > _msdcs.[Domain Name] > Named Servers tab  

, it added back automatically after I click refresh.  

How to fix it?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-16*

Great information guys!  I appreciate your help!  

Any thoughts on why when I delete a Site in AD Sites and Services it deletes out of the contoso.com zone but not _msdcs.contoso.com?  

My assumption is that it has something to do with the way the previous engineer setup the separate zones.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-16*

A possible work-around for the upper / lower case.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/dns-registers-duplicate-srv-records-for-dc#workaround-1-prevent-duplicate-srv-records    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-16*

You can follow along here to do metadata cleanup.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
