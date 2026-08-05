---
title: "Sharepoint with saml authentication(ADFS)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/607565/sharepoint-with-saml-authentication-adfs
question_id: 607565
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-development-routing", "microsoft-security-security-active-directory-federation-services"]
---
# Sharepoint with saml authentication(ADFS)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/607565/sharepoint-with-saml-authentication-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,  

We were able to integrate Sharepoint with ADFS with upn as primaru input claim type.  

Now we want to show display name inplace of upn in created by of lists and on topright side of the SharePoint.  

alon with upn, we are bringing displayname, role and emailaddress from adfs  

Please let us know how to do this  

Thanks  

Athulya

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-29*

Hi @Athulya Pillai  ,

You need to be able to import the identity store into the UPA.

1.Configure synchronization settings in “Manage Profile Service: User Profile Service” page.  

2.Modify user properties.  

3.Verify that the profiles have been imported.

More details about how to configure user Profile Service For ADFS Provider for your reference: SharePoint 2013 Configure User Profile Service For ADFS Provider  

Note: Microsoft is providing this information as a convenience to you. The sites are not controlled by Microsoft. Microsoft cannot make any representations regarding the quality, safety, or suitability of any software or information found there. Please make sure that you completely understand the risk before retrieving any suggestions from the above link.

Similiar issue: SAML-based claims authentication in SharePoint: how to show Display Name instead of email address?

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
