---
title: "Sharepoint 2019 OnPremise and ADFS authentication loop"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1178889/sharepoint-2019-onpremise-and-adfs-authentication
question_id: 1178889
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Sharepoint 2019 OnPremise and ADFS authentication loop

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1178889/sharepoint-2019-onpremise-and-adfs-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I'm setting up ADFS for Sharepoint 2019 OnPremise. Sucessfully integrated SPTrustedIdentityTokenIssuer with ADFS endpoint. I can also sucessfully login in ADFS test page.

I'm stuck on the Sharepoint Sing in page loop after succesful ADFS user logon. I can see the eventid 4634 "logoff session" for that user in ADFS events.

I need some assistance or guidelines as I've found nothing useful in forums.

Your help is much appreciated.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-10*

Hi @Pablo Alcover ，

I'm glad to hear you solve the problem, if you have any issue about SharePoint, you are welcome to raise a ticket in this forum.

By the way, since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others." and according to the scenario introduced here: Answering your own questions on Microsoft Q&A, I would make a brief summary of this thread:

[Sharepoint 2019 OnPremise and ADFS authentication loop]

Issue Symptom:

I'm stuck on the Sharepoint Sing in page loop after succesful ADFS user logon. I can see the eventid 4634 "logoff session" for that user in ADFS events.

Certificate issues: PartialChain: A certificate chain could not be built to a trusted root authority. RevocationStatusUnknown: The revocation function was unable to check revocation for the certificate. OfflineRevocation: The revocation function was unable to check revocation because the revocation server was offline.

Current status:

The issue has been solved by importing Sharepoint's root authority into Trusted Root Certificates of every Sharepoint Server.

You could click the "Accept Answer" button for this summary to close this thread, and this can make it easier for other community member's to see the useful information when reading this thread. Thanks for your understanding!

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-09*

The last error is easy resolved by importing Sharepoint's root authority into Trusted Root Certificates of every Sharepoint Server.

Problems solved. Integration working.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-09*

The loop has been solved adding the email address to the AD profile of the user account trying to login.

Now I'm getting new certificate issues:

 PartialChain: A certificate chain could not be built to a trusted root authority. RevocationStatusUnknown: The revocation function was unable to check revocation for the certificate. OfflineRevocation: The revocation function was unable to check revocation because the revocation server was offline.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-09*

I did follow documentation to implement the integration. As said I checked ADFS with it's test page.

I PREVIOUSLY faced the error "Ensure that the SecurityTokenResolver is populated with the correct key" and figured out that the certificate that has to be imported in Sharepoint has to be exported from the Token-singing of ADFS (really not well explained in documentation). So I'm sure that this is NO MORE THE ISSUE so the behaviour I'm facing now has not to do with that.

There is a succesfull logon and a subsequent logoff in event viewer as mentioned.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-09*

Hi @Pablo Alcover ,

Please check the steps to configure federated authentication in SharePoint 2019 with Active Directory Federation Services (AD FS).

-  Install ADFS Server

-  Create a trusted relying party for SharePoint 2019 in ADFS

-  Configure SharePoint 2019 to trust ADFS

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
