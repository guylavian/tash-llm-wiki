---
title: "ATAGateway Certificates in Domain Controllers?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/305390/atagateway-certificates-in-domain-controllers
question_id: 305390
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
---
# ATAGateway Certificates in Domain Controllers?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/305390/atagateway-certificates-in-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I recently found 2 certificates in my DC's personal certificate store, 1 expired a few years ago and one is about to expire. They are self signed by ATAGateway and also have ATAGateway as their friendly name.  

I guess ATA automatically creates these certificates when I install a lightweight gateway on my DCs but my questions are :   

Can I delete the expired one?  

Will the gateway automatically create a new cert when the 2nd one expires?  

I have certificate monitors alerting me when a certificate is about to expire, is there a way to manually make ATA re-create a certificate so I can just have a new one that isn't about to expire?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-16*

The certificate the article refers is the certificate used by the ATA Center and the web access. This is a certificate I created and know of.  

I'm speaking of certificates I found in my DC's store, they seem self signed by ATA and I never knew of their existence until my monitor for expired certificates showed them.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hi MercuryZ,    

Thanks for your reply.    

Have you checked ahether the certificate of ATA Center is about to expire or not? If yes, please refer to the below link to create a new certificate and replace the old one.    

https://learn.microsoft.com/en-us/advanced-threat-analytics/modifying-ata-center-configuration    

According to the above link, the ATA Center service will activate the new certificate and the ATA Gateway will connect to the ATA Center using the new certificate.     

Hope the above will be helpful.    

Regards,    

Rita    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
