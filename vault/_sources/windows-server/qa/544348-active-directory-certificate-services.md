---
title: "Active Directory Certificate Services"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/544348/active-directory-certificate-services
question_id: 544348
fetched: 2026-07-25
answer_count: 10
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Certificate Services

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/544348/active-directory-certificate-services (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am researching how to implement Active Directory Certificate Services to our existing domain.  The primary purpose is to use it for 802.1X Wireless authentication.    

Since our environment has iPads and Windows 10 PC's I intend to use AD user credentials for Wireless authentication.   

We have 20K users, so I would think 1 ADCS dedicated server would be ok and 2 separate RADUIS/NPS servers.  

Can anyone help me understand the following:  

-  Does this sound reasonable for what I am trying to do?  

-  If I install and configure ADCS as an Enterprise Server will that have any affect on the current users or servers?

## Answer (community) — community member

*upvotes: 1 · updated: 2021-09-09*

Hello @Aaron       

Firstly installing and configuring ADCS as an Enterprise Server will never affect your current users and servers. as it doesn't have the authority to do so.    

Do have a look at the Network Policy Server Management with Administration Tools using the below link for a better understanding    

https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-admintools    

Hope this answers all your queries, if not please do repost back.     

If an Answer is helpful, please click "Accept Answer" and upvote it : )    

Regards,

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-09-08*

Here is a good document that will help you configure this    

https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-manage-cert-requirements    

For the other question, Apple has published a document how to connect Apple devices to 802.1x network    

https://support.apple.com/en-ca/guide/deployment-reference-ios/apd7b6d34790/web    

hth

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-09-08*

Correct.  Event if a user receive a certificate, it does not cause any issue because the certificate will not be used by any application.  

When the user will connect to the Wi-Fi and the NPS policy will be configured, at this time, the certificate will be used to authenticate the client.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-09-08*

I would recommend to look at those articles for the ADCS and NPS/Radius design    

https://social.technet.microsoft.com/wiki/contents/articles/7421.active-directory-certificate-services-ad-cs-public-key-infrastructure-pki-design-guide.aspx    

https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-top    

For the second question, adding a Enterprise CA in your organization should not cause any effect on your current environment    

hth
