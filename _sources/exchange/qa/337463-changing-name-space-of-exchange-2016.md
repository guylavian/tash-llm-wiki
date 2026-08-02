---
title: "Changing Name Space of Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/337463/changing-name-space-of-exchange-2016
question_id: 337463
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Changing Name Space of Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/337463/changing-name-space-of-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Exchange name space ( mail.domain-abc.com and autodiscover ( autodiscover.domain-abc.com ).   

Due to change in company, we would like to change the name space to ( mail.domain-xyz.com and autodiscover-xyz.com).   

I will apply the new certificate and will change the virtual directories URLs.   

But actual concern is that outlook clients would require to reconfigure or they will automatically pickup the new name space. Like currently outlook is pointed to under account settings to ( https://mail.domain-abc.com). What will happen once i set the new URL ( NameSpace) to ( https://mail.domain-xyz.com).

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-30*

In these cases, Outlook should pick up the new settings and be ok. However, users may get a popup requiring them to restart Outlook ( An Administrator has made a change...) or in some cases, a new profile may be required unfortunately.     

I assume you are also changing the internal SCP:    

```
Set-ClientAccessService -Identity "MBX-01" -AutoDiscoverServiceInternalUri "https://mbx01.contoso.com/autodiscover/autodiscover.xml" -AutoDiscoverSiteScope "Mail"
```

https://learn.microsoft.com/en-us/powershell/module/exchange/set-clientaccessservice?view=exchange-ps
