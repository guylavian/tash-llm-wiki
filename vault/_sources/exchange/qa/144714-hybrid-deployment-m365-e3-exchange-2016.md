---
title: "Hybrid Deployment M365 E3 Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/144714/hybrid-deployment-m365-e3-exchange-2016
question_id: 144714
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Hybrid Deployment M365 E3 Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/144714/hybrid-deployment-m365-e3-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I create an Archive in Exchange on Prem the Archive works fine in OWA.  

I am having an Issue when I move the Users Email Archive to the Cloud.   

The Archive no longer works in OWA.   

It shows it but it gives me an error.  

You archive appears to be unavailable. Please try again later.   

However it works fine In Outlook.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-01*

Hi,    

Apart from the suggestions provided above, please check the solutions shared in this article    

https://learn.microsoft.com/en-us/office365/troubleshoot/archive-mailboxes/cloud-based-archive-unavailable    

Also, does the user able to update Archive mailbox in outlook or its  just showing there? Please also check if Exchange online archiving license is enabled for the user

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-30*

@Mike King       

What's the detailed version of your Exchange 2016? You can check with the following command:    

```
Get-ExchangeServer | Format-List Name,Edition,AdminDisplayVersion
```

Does this issue occur with other archive mailbox moving from on-premises to Exchange Online?    

Clear the cached data and re-log into your mailbox.     

Please also try to use other Browsers with latest versions to see if it is caused by specific browser.     

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
