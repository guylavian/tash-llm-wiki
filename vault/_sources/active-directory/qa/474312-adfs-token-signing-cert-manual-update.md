---
title: "adfs token signing cert manual update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/474312/adfs-token-signing-cert-manual-update
question_id: 474312
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# adfs token signing cert manual update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/474312/adfs-token-signing-cert-manual-update (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A question regarding token signing cert manual update. Some articles mention enabling auto rollover then generate the cert and then disable auto rollover. Is that the correct procedure (currently auto rollover is set to false)?   

Also, when two certs are present with the current one as primary and the renewed as secondary, will the relying party trust me able to connect through the new cert/thumbprint or does the new one have to set up as primary for that?   

Any pointers to how this needs to be updated in WAP? Microsoft document talked about renewal and didn't have reference to wap.   

Thanks!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-07-19*

Hum, that's a good question.  

To be on the safe side I would do the following:  

-  Take an ADFS Rapid Restore backup of your farm inclufding DKM info.   

-  Set the CertificatePromotionThreshold and CertificateCriticalThreshold to 1.  

-  Restart the ADFS service.  

-  Enable the roll over.  

-  Generate the new certificates (for both signing and decrytping)  

-  Disable the roll over.  

You should have two certificates. And you can promote the new one manually when you want from the GUI.  

I never tried this. Ideally I would do that in a lab before going prod with it. Altough, if you have a valid backup, you might want to do that in a low activity period (nights or week-end) and roll back if you see the cert changing.  

Ultimately, you can also export the token signin certs using different tools available in GitHub (for a quick restore). At your own risks...

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-07-19*

It depends if you are using your own certificates or if you are using the self-signed certificates. At the end of the day, you can change the certificate when you want, it just has a massive impact on the applications (RPT) if you don't communicate effectivelely with them.   

ADFS always signs tokens with the primary token signing certificate. The secondary is just added to the federation metadata to give a change to the RPT to know about it. Ideally the application should be accepting token signed with any valid certificate. That way you don't have to time the change of certificate with the application. The reallity is that most application are not checking metadata nor capabable of having two possible signing certs. So the change has to be "synchronized" with the application owner to ensure minumum service interuption.  

WAPs don't care about token signing certificate. They don't do any token signing operation. They are not affected by token signing (or token encrypting) certificate changes.
