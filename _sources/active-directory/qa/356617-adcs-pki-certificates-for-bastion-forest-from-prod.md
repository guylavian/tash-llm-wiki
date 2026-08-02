---
title: "ADCS PKI: Certificates for Bastion Forest from Production Forest (on premise no Azure)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/356617/adcs-pki-certificates-for-bastion-forest-from-prod
question_id: 356617
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-identity-manager", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# ADCS PKI: Certificates for Bastion Forest from Production Forest (on premise no Azure)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/356617/adcs-pki-certificates-for-bastion-forest-from-prod (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there any guidance in regards to whether a Windows Server 2019 Bastion forest should be issued certificates from the Windows Server 2019 Production forest for a on premise solution? I have searched and cannot find any answers to this question. Any advice would be appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-29*

Hey @RedWhiteBlack  ,    

The best practice here I believe would be to deploy a separate PKI solution in the Bastion forest. This means the Bastion environment won't be impacted if the PKI in the Corporate forest is compromised.    

Hope this helps.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-22*

Hi Daisy,  

Thank you. Just some feedback, it would be good if there was a "PKI" tag that could be attached to PKI questions rather than having to tag them as "windows server". When we still had technet social, Brian Komar, Mark Cooper, vadmins and other PKI experts would be very nice and get back to you fairly promptly. Which was always appreciated by the community.  

What you have said wouln't maintain logical separation as the bastion PRIV forest needs to provide its own services and not be reliant on the CORP forest. However it would be really appreciated if one of your PKI experts, could clarify this issue definitively.   

Kind Regards

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-16*

Hello @RedWhiteBlack  ,    

Thank you for your update.    

Does that logical separation extend to PKI as well? Or can cross forest certificates be used without breaking the bastion model?    

For cross forest certificates:    

If there is two-way trust relationship between two forests, we can set up Cross-Forest Certificate Enrollment.    

For more information we can refer to link below.    

AD CS: Deploying Cross-forest Certificate Enrollment    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff955845(v=ws.10)    

If there is no two-way trust relationship between two forests, we can set up Cross-Forest Certificate Enrollment.    

For more information we can refer to link below.    

Test Lab Guide Mini-Module: Cross-Forest Certificate Enrollment using Certificate Enrollment Web Services    

https://social.technet.microsoft.com/wiki/contents/articles/14715.test-lab-guide-mini-module-cross-forest-certificate-enrollment-using-certificate-enrollment-web-services.aspx    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-15*

Hello @RedWhiteBlack  ,

Thank you for posting here.

Based on the description, I understand you have PKI in your Production forest.

1.Would you please describe the meaning of the "Bastion Forest" in your case, so that we can help you better?  

2.What is the relationship between Bastion Forest and Production forest?  

3.Do they ahve any trust relationship?

Here we can see a bastion environment planing.  

Planning a bastion environment  

https://learn.microsoft.com/en-us/microsoft-identity-manager/pam/planning-bastion-environment

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
