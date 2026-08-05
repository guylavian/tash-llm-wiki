---
title: "Active Directory - DNS Zone - Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1367883/active-directory-dns-zone-issue
question_id: 1367883
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory - DNS Zone - Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1367883/active-directory-dns-zone-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good evening everyone,

In my Active Directory, following the standard procedure without forcing or similar, I removed 2 Secondary Domain Controllers.

These Domain Controllers are called: DC2-CORE & DC3.

So now the primary domain controller (SERVER-AD) is alone.

The problem is that: in the DNS server, in particular in the _msdcs.mycompany.local zone and in the mycompany.local zone, in the various subfolders such as _sites _tcp _DomainDnsZone  _ldap and _kerberos records still extist and they still contain both of the old Secondary Domain Controllers such as:

•	_ldap server-ad.mycompany.local

•	_ldap dc2-core.mycompany.local

•	_ldap dc3.mycompany.local

•	_kerberos server-ad.mycompany.local

•	_kerberos dc2-core.mycompany.local

•	_kerberos dc3.mycompany.local

The problem is that when I delete records that contain the old servers and then attempt to clean the zone, they immediately reappear. So the cancellation is in vain.

I checked the NON-presence of the two Secondary Domain Controllers in Active Directory Site and Services and everything is OK.

DCDIAG does not give me any malfunctions.

On the AD structure, the old servers no longer appear as Domain Controller

Since I want to dispose of the primary domain controller (it is a Windows Server 2012 R2), before adding a new Domain Controller with OS Windows Server 2022 and transferring fsmo roles to it, I wanted to have clean active directory and dns.

Unfortunately I can't. I searched online for half a day and couldn't find a solution.

I hope the explanation is clear :)

Can you help me?

## Answers

_No answers on this thread._
