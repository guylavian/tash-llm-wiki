---
title: "OWA & ECP does not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/153349/owa-ecp-does-not-working
question_id: 153349
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
---
# OWA & ECP does not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/153349/owa-ecp-does-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we have two exchange 2016 DAG servers and client connect to ECP and OWA through AD federation service and the dedicated certificate for ADFS is expired on exchange servers and we have a new ADFS certificate so how to assign this certificate to exchange service to solve disconnected issue for OWA and ECP

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-11-11*

While working on system its quite natural having such issue, this error may be due to accessing outlook multiple times in a network. But mostly this happens because of entering an incorrect method for “OWA” and “ECP” Virtual directories.  

How to Rebuild ECP Virtual Directory  

Follow the below points:  

First use Remove-ECPVirtualDirectory to remove Exchange control Panel virtual directories.  

Then use New-ECPVirtualDirectory for creating an Exchange Control Panel virtual directory.  

please also check mentioned link   

https://expert-advice.org/exchange-server/how-to-fix-exchange-20132016-cannot-login-ecp-or-owa-error/  

If issue resolve please accept answer thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-09*

Hi @Bebo Edward  ,    

Based on my research, please try to install the new certificate into the Trusted Root Certification Authorities container in the certificates MMC (Local Computer account) on each Exchange server and restart IIS. Then run the command below, restart IIS again and check the result:    

```
Set-OrganizationConfig -AdfsSignCertificate 
```

Here is a relevant thread for your reference:     

Exchange 2016 ECP and OWA unavailable after ADFS token certificate rollover    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
