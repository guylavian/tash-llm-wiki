---
title: "Exchange 2016 keeps trying to access demoted Domain Controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1183031/exchange-2016-keeps-trying-to-access-demoted-domai
question_id: 1183031
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 keeps trying to access demoted Domain Controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1183031/exchange-2016-keeps-trying-to-access-demoted-domai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We have decommissioned 2 Domain Controllers and installed 2 new DCs.

When looking in Exchange Server 2016 CU23 event viewer, we still see, Exchange tries to reach to those old controllers.

EventID 2070:

`Process Microsoft.Exchange.Directory.TopologyService.exe (PID=5036).  Exchange Active Directory Provider lost contact with domain controller DC1.company.com.  Error was 0x51 (ServerDown) (Active directory response: The LDAP server is unavailable.).  Exchange Active Directory Provider will attempt to reconnect with this domain controller when it is reachable.`  

I have already checked with related articles, where it is told to:

Close all open MMCs and then delete the file "Exchange Management Console.msc" at C:\Users<USERID>\AppData\Roaming\Microsoft\MMC

There is no such file available.

I have run CMD command to check, if there is stored DNS record in Exchange server for 2 old DCs, and there it is:

ipconfig /displaydns | findstr DC1.company.com

or

ipconfig /displaydns | findstr DC2.company.com

But after server restart, DNS cache is cleared and flushing DNS is not solution too.

This is how it looks in Event Viewer, there are problematic Event IDs: 2070. But should be only EventID 2080 (which shows connection to actual Domain Controller and is fine).

The only idea what we have at the moment is to exclude 2 old DCs by runing this command from Exchange Management Shell:

```
Set-Exchangeserver Exchange-server.company.com -StaticExcludedDomainControllers DC1,DC2
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-02-22*

Check AD Sites and Services and see if the old DCs are still there:

Default-First-Site/Servers

DSSITE.MSC
