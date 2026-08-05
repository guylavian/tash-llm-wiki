---
title: "Autodiscover setting in exchange hybird environemt for multi-domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/250387/autodiscover-setting-in-exchange-hybird-environemt
question_id: 250387
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Autodiscover setting in exchange hybird environemt for multi-domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/250387/autodiscover-setting-in-exchange-hybird-environemt (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,  

We have serval domain in our exchange 2010 environment. The abc.com is our main domain in our exchange, all certificate and client access URL using this domain (mail.abc.com and autodiscover.abc.com).   

We will migrate one domain xyz.com to o365 and setup a exchange 2016 for hybrid server.    

In public and internal DNS, autodiscover.abc.com is point to ex2010, and autodiscover.xyz.com is point to ex2016. For the ex2010 client access server uri setting, it is configured to "https://autodiscover.abc.com/........". And the ex2016 uri setting is configured to "https://autodiscover.xyz.com/........". So the o365 will connect to ex2016 when run hybrid wizard.  

After this configuration, our user outlook prompt the autodiscover change to "autodiscover.xyz.com" and some user connect to ex2016   

How to configure the autodiscover setting if we just planned to migrate the additional domain to o365 with no user impact (all other domain)  

Thanks  

Chong

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-01*

After this configuration, our user outlook prompt the autodiscover change to "autodiscover.xyz.com" and some user connect to ex2016    

In a coexist environment, it is suggested and needed to use Exchange 2016 as client access point(if only publish one Exchange server to the Internet), because Exchange 2016 could proxy request to Exchange 2010, but not vice versa. Client Connectivity in an Exchange 2016 Coexistence Environment with Exchange 2010    

The URLs geted by Autodiscover service also decided by where mailbox hosted. So, make sure all "@jaswant  .com" mailboxes are hosted on Exchange 2010 database.     

Then, use command below to check and backup autodiscover original configuration:    

```
Get-ClientAccessServer | fl Identity,*uri*
```

Then use command below to remove SCP from all Exchange servers:    

```
Get-ClientAccessServer | Set-ClientAccessServer -AutoDiscoverServiceInternalUri $null
```

After that, make Exchange 2010/2016 use the same internal URL as their external URL(Exchange 2010 using "abc.com" and Exchange 2016 using "xyz.com").    

Then restart IIS service(Run "IISReset" command in CMD) on all Exchange servers. Wait for a while, then check again.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
