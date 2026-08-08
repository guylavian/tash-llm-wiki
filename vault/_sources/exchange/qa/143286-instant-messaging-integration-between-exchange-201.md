---
title: "Instant Messaging Integration between Exchange 2016 OWA and Skype for Business 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/143286/instant-messaging-integration-between-exchange-201
question_id: 143286
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-skype-business-platform-windows", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Instant Messaging Integration between Exchange 2016 OWA and Skype for Business 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/143286/instant-messaging-integration-between-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We migrated exchange server 2010 to 2016.We have renewed our SSL certificate so thumbprint has been change.anyone have any idea how to we can change thumbprint  for Instant Messaging I Exchange 2016 OWA and Skype for Business 2013.  

We tried below cmd line with new certificate thumbprint,  

New-SettingOverride -Name "IM Override"  -Component OwaServer -Section IMSettings -Parameters @("IMServerName=WS2K16SFB.lab.com","IMCertificateThumbprint=0F4E220212440250F92B9CEA7FD8D40BA51374B0") -Reason "Configure IM" -Server WS2K16EXG  

But we got error  

"Active Directory operation failed on WS2K16EXG. The object 'CN=IM Override,CN=Setting  

Overrides,CN=Global Settings,CN=cyberThink Inc,CN=Microsoft  

Exchange,CN=Administrator,CN=Configuration,DC=WS2K16EXG,DC=lab,DC=com' already exists.ADObjectAlreadyExistsException"  

Thank you.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-29*

Hi @Jemin Prajapati  ,    

Have you decommissioned Exchange 2010 server in your environment?    

According to your error message, it indicates that the value for the “CN = xxx” is taken from the alias property of the user being migrated from the old exchange server. In this case, we recommend you compare your AD properties between two servers. You can also try to delete the old “IM Override” and renew another name.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
