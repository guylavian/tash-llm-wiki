---
title: "exchange 2016 ecp HMACprovider.GetCertificates:ProtectionCertificates.Length<1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1095344/exchange-2016-ecp-hmacprovider-getcertificates-pro
question_id: 1095344
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# exchange 2016 ecp HMACprovider.GetCertificates:ProtectionCertificates.Length<1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1095344/exchange-2016-ecp-hmacprovider-getcertificates-pro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

as above error, however, i have already checked the certificate and it is normal, i also had done the same steps as suggestion by microsoft,     

New-ExchangeCertificate -KeySize 2048 -PrivateKeyExportable $true -SubjectName "cn=Microsoft Exchange Server Auth Certificate" -FriendlyName "Microsoft Exchange Server Auth Certificate" -DomainName @()    

Set-AuthConfig -NewCertificateThumbprint <新的证书ID> -NewCertificateEffectiveDate (Get-Date)    

Set-AuthConfig -PublishCertificate    

Set-AuthConfig -ClearPreviousCertificate    

————————————————    

but when i accessed the ecp, the same error shown:    

HMACprovider.GetCertificates:ProtectionCertificates.Length<1    

how can i resolve the issue?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-29*

many thanks LilyLi2, the ECP is working. however, i have restarted the IIS and even restarted the server, but actually it took a night to effect as i can access the ECP the second morning.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-21*

Hi @老马 负轭  ,    

Welcome to our forum.    

Is ECP working now?    

“While actually i had done it yesterday in accordance with Microsoft, but i didn't work. this morning i open the ecp again and find it working.”    

After creating and deploy a new OAuth certificate to the Exchange server, you need to wait for a few hours for the ECP to work. It should take effect immediately if you restart IIS or recycle the Outlook on the web and EAC application pools.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-18*

Are you sure the new certificate thumbprint is assigned to ECP and OWA virtual directories?    

If so, you can try an IISreset, to restart all the web services, this error web page comes after you put the credentials for login to ECP?    

Regards.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-18*

Use this to create a new certificate:    

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/cannot-access-owa-or-ecp-if-oauth-expired    

Make sure you restart the WebAppPools mentioned in the documentation. It should take effect immediately but can take up to an hour to take effect.
