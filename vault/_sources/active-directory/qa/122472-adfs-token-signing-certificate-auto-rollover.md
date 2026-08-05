---
title: "ADFS Token signing Certificate Auto-Rollover"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/122472/adfs-token-signing-certificate-auto-rollover
question_id: 122472
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Token signing Certificate Auto-Rollover

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/122472/adfs-token-signing-certificate-auto-rollover (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have auto rollover enabled with following setting  

CertificateCriticalThreshold   : 2  

CertificateDuration            : 1095  

CertificateGenerationThreshold : 20  

CertificatePromotionThreshold  : 5  

CertificateRolloverInterval    : 720  

CertificateThresholdMultiplier : 1440  

The existing token signing cert expiring on 30th of sept 2020 at 8:39:40 PM. According to Microsoft blogs I predicted  following activities  

1-New secondary certificates generated at 10th of sept 2020 at 8:39:40 PM (20 days before expiry)  

2-New secondary certificates promoted to primary ( 5 days after generation)  

But I notice that Auto rollover kicked in 6 hours late at 10/11/2020 2:32:12 AM.  

Now I am trying to figure out when the CertificatePromotion will occur ?   

Question:  

I had lined up relying party vendors to renew cert on 15th of Oct at 8:39 PM but since the renew occurred 6 hours late, does this mean the existing secondary will promote to primary 6 hours late too?  

We are trying to minimise the down time as much as possible

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-11*

Did that happen exactly 6 hours late? I am thinking maybe there was some TZ conversion challenges.  

But regardless, if you want to control when it is issued as primary, you can temporary disable the AutoCertificateRollover feature, then manually set the Secondary as Primary when you wish and then re-enable the AutoCertificateRollover.  

The point of the auto roll over is to publish two valid signing certificates in the metadata that the relying parties which read them can be configured to accept both. Then whenever the switch takes place is irrelevant for the application really. I see a lot applications not capable of accepting two different certificates, that's this issue (so it's really an app issue :) )... And if that's the case of all your apps, then you'd better go for a manual switch over regardless.
