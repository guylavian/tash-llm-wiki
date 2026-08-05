---
title: "Update ADFS Certificate with Microsoft 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5213326/update-adfs-certificate-with-microsoft-365
question_id: 5213326
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["active-directory-federation-services"]
---
# Update ADFS Certificate with Microsoft 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5213326/update-adfs-certificate-with-microsoft-365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, our ADFS cert is coming due and we have generated new Token Signing/Decrypting certificates. I'm confused on a couple steps in this Microsoft doc that I will outline https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-o365-certs 

Step 2: Confirm that AD FS and Azure AD are in sync

"Get-MsolFederationProperty -DomainName <domain.name> | FL Source, TokenSigningCertificate"

I'm assuming <domain.name> is my company.onmicrosoft.com correct?? If Yes, when I run this it says our domain does not exist which I suspect is because we're not necessarily Federated. We're a Managed Domain where we sync objects to Azure AD. 

Step 2: Update the new token signing certificates for the Microsoft 365 trust

Update-MSOLFederatedDomain –DomainName <domain> 

If the above statement is true, then shouldn't Microsoft 365 detect the new certificates automatically once I set them to Primary? Seems this next command is only if we're a Federated so I'm apprehensive to run it. 

the overall end goal is to ensure no hiccup in services or users being able to sign in.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-21*

Dear Jaded Smith,

Good day. 

Thanks for posting in Microsoft Community. 

Regarding your query on Update ADFS Certificate with Microsoft 365.  Please understand that this query is outside of our support boundaries.   

For you to be assisted properly, please reach out to Microsoft Q&A by visiting this website Active Directory Federation Services - Microsoft Q&A; I am sure that our experts from that team can address your query effectively and accurately. 

Thank you for your cooperation and understanding.  Please do not hesitate to post your queries in Microsoft Community and we will always do our best to assist you! 

Sincerely, 

Simbarashe | Microsoft Community Moderator
