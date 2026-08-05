---
title: "Exchange 2016 OAB in child domain cannot download"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/245090/exchange-2016-oab-in-child-domain-cannot-download
question_id: 245090
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 OAB in child domain cannot download

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/245090/exchange-2016-oab-in-child-domain-cannot-download (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,  

We have exchange 2016 in both root and child domain. All client access are working fine.  

The OAB system mailbox is located in root domain and OAB can be download in root domain user, but the child domain user cannot.  

The OAB url in root domain setting is:  

Internal: https://owa.contoso.com/oab  

External: https://owa.contoso.com/oab  

The OAB url in child domain setting is:  

Internal: https://owa.child.contoso.com/oab  

External:   

How can the child domain user download the OAB  

Thanks  

Chong

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-27*

Hi,Chong.    

Please run a Test E-mail AutoConfiguration via Outlook clients in child domain.    

Check the OAB url returned under the "Results" tag.    

    

And please run the following commands via EMS to enable all OAB virtual directories in the organization to accept requests to download the OAB.    

```
Set-OfflineAddressBook -Identity "Default Offline Address Book" -VirtualDirectories $null  
Set-OfflineAddressBook -Identity "Default Offline Address Book" -GlobalWebDistributionEnabled $true
```

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
