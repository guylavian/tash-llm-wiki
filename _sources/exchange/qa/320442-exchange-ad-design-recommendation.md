---
title: "Exchange -AD Design Recommendation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/320442/exchange-ad-design-recommendation
question_id: 320442
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange -AD Design Recommendation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/320442/exchange-ad-design-recommendation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

```
We have two domains. One production and one development.

  1. Prod.mydomain.com
   2. dev.mydomain.com

Both have an Exchange environment and production has moved to 0365 and has an on-premise exchange server ( hybrid server)
```

  I need to decommission this dev exchange environment.   

 How do I allow dev.mydomain.com users to test applications using O365 or On-premise Exchange server?  

They only required test the mail functionality.  

As

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-22*

Hi All,  

  Thank you. This Dev environment is an internal-only AD domain for application testing.   Simply test SMTP email functionality and login to the OWA and check these emails. ( On-prem  only)  

As

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-19*

Hi @TankSupport   ,    

May I ask what tests are you going to do? On-prem or Online?    

I'm a bit confused, if you only want to do some tests with mail function, why not creating a test account in the product server..?    

Or you could create a O365 account and sync with your AD accounts like Andy said: How to use SMTP matching to match on-premises user accounts to Office 365 user accounts for directory synchronization    

Sorry for these stupid questions, if you could please let know more about this issue, thanks..    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-18*

-  Add dev.mydomain.com as an accepted domain to the on-prem Exchange Server:    

 https://learn.microsoft.com/en-us/exchange/mail-flow/accepted-domains/accepted-domains?view=exchserver-2019    

-  Add dev.mydomain.com as a domain in 365: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-domain?view=o365-worldwide    

Set DNS records ( Mx / autodiscover tc.. ) to 365    

 Create the necessary dev.mydomain.com AD accounts on-prem to sync to 365. add dev.mydomain.com as an allowed UPN:    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/prepare-a-non-routable-domain-for-directory-synchronization?view=o365-worldwide#step-1-add-the-new-upn-suffix
