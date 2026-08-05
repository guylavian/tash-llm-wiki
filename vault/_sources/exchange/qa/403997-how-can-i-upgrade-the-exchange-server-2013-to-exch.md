---
title: "How can i upgrade the Exchange Server 2013 to Exchange Server 2019 with existing Hybrid Setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/403997/how-can-i-upgrade-the-exchange-server-2013-to-exch
question_id: 403997
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How can i upgrade the Exchange Server 2013 to Exchange Server 2019 with existing Hybrid Setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/403997/how-can-i-upgrade-the-exchange-server-2013-to-exch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Good Day!  

Requesting for assistance on how can we upgrade the Exchange Server 2013 to Exchange Server 2019 with hybrid configured.  

Thanks,  

Raymond

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-08-25*

Make sure your environment is the supported coexistence scenarios for Exchange 2019:    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/system-requirements?view=exchserver-2019    

Exchange 2013 - Supported with Exchange 2013 Cumulative Update 21 (CU21) or later on all Exchange 2013 servers in the organization, including Edge Transport servers.    

You need to update Exchange 2013 to CU21. Then install Exchange 2019 into your organization directly and re-run HCW to configure Exchange 2019 as a 'hybrid server'.    

Don't forget to change related DNS records to Exchange 2019.     

You could refer to Exchange Deployment Assistant for detailed steps:    

https://assistants.microsoft.com/     

Exchange Migration Checklist and Guide

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-24*

anonymous user     

Install Exchange 2019 coexists with Exchange 2013 directly. After that, enable MRSProxy for your Exchange 2019 server:    

```
Set-WebServicesVirtualDirectory -Identity "[\]EWS (Default Web Site)" -MRSProxyEnabled $true
```

After that, you will could rerun HCW to choose Exchange 2019 as hybrid server. If you want to uninstall Exchange 2013, you also need to configure virtual directory for Exchange 2019 and change public DNS(such as mail.domain.com, autodiscover.domain.com) record from Exchange 2013 to Exchange 2019.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-21*

Same as if you have Exchange installed without hybrid.  

https://assistants.microsoft.com/assistants/#/session/0bdd81d4-f507-4ee9-a4e2-8e8860f10663  

Then when done, re-run the Hybrid Wizard and choose the 2019 server as the endpoint.  

Ensure your firewall rules are updated as needed.
