---
title: "Add new AdfsAudienceUris to organization configuration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/571593/add-new-adfsaudienceuris-to-organization-configura
question_id: 571593
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Add new AdfsAudienceUris to organization configuration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/571593/add-new-adfsaudienceuris-to-organization-configura (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to update(add new ) URL's to  AdfsAudienceUris to set the ADFS configuration on organization configuration level .    

As per microsoft documentation , to add new URL without  overwriting the existing ones , you have to Add like below :     

https://learn.microsoft.com/en-us/powershell/module/exchange/set-organizationconfig?view=exchange-ps    

    

Set-OrganizationConfig  -AdfsAudienceUris @{Add="https://mail.contoso.com/owa","https://mail.contoso.com/ecp"}    

but I'm getting the below error :     

The ADFS Authentication Configuration string must contain at least one audience Uri.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-09-30*

Hi @Hamzeh Smadi       

I tested in my lab (Exchange 2019) and got the same error.    

While if using Set-OrganizationConfig -AdfsAudienceUris "https://mail.contoso.com/owa","https://mail.contoso.com/ecp" instead, the values can be added correctly.    

As a workaround, I suppose you may need to also contain the existing uris in this command to add the new AdfsAudienceUris.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
