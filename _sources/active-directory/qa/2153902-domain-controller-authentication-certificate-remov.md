---
title: "Domain Controller Authentication certificate removal"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2153902/domain-controller-authentication-certificate-remov
question_id: 2153902
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Domain Controller Authentication certificate removal

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2153902/domain-controller-authentication-certificate-remov (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I just want to confirm is Domain Controller Authentication certificate auto enrolled to all domain controllers obsolete and completely replaced with Kerberos Authentication certificate? If so, can this certificate template be stopped from auto enrollment/renew first and eventually completely removed.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-04*

Hello Bojan Zivkovic,

Thank you for posting in Q&A forum. 

There has been some evolution in the certificate templates that domain controllers use over the years. In modern (post–Windows Server 2012) Active Directory environments, Microsoft introduced the Kerberos Authentication certificate template to support certificate‐based Kerberos authentication. For many organizations running fully updated environments, the Kerberos Authentication certificate is now the preferred option, and the older Domain Controller Authentication certificate template is increasingly seen as a legacy mechanism. 

That said, before “removing” or disabling the autoenrollment of the Domain Controller Authentication certificate template, there are some important points to consider: 

-  Environment and Dependency Check.  

• Although many organizations have moved to certificate–based Kerberos with the newer template, some environments (especially those with legacy systems or mixed server OS versions) may still have dependencies on the Domain Controller Authentication certificate.  

• It’s essential to review your environment (including services like LDAPS, smart card logon, or any custom solution that might reference the older template) to be 100% sure that no clients or services expect this certificate. 

-  Autoenrollment Control.  

• Autoenrollment is driven by Group Policy and the certificate template’s security settings. If you are confident the Domain Controller Authentication certificate is no longer needed, you can stop it from auto enrolling. This is typically done either by:   

Removing or altering the relevant autoenrollment Group Policy settings (or disabling autoenrollment rights in the template’s security configuration), or 

Adjusting the template’s configuration in your enterprise CA so that it no longer issues certificates automatically to domain controllers. 

-  Phased Removal Process.  

• It is a best practice to first disable autoenrollment/renewal so that no new Domain Controller Authentication certificates are issued. Monitor the environment to ensure that no unexpected issues occur over the certificate’s lifetime.  

• Once you are satisfied that no services are using these certificates (and after waiting for the existing ones to naturally expire or be retired), you can remove the template from the CA (or at least stop publishing it) so that it will not be available for future enrollment.

I hope the information above is helpful. 

If you have any questions or concerns, please feel free to let us know. 

Best Regards, 

Daisy Zhou 

============================================ 

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-02-04*

As of Windows Server 2022 and recent updates to Windows Server 2019, the Domain Controller Authentication certificate has been replaced by the Kerberos Authentication certificate. 

You can stop the auto-enrollment of this certificate by modifying the certificate template properties and disabling auto-enrollment.
