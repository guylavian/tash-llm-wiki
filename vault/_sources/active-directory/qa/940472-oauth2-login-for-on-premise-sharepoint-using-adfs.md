---
title: "OAuth2 login for on premise sharepoint using ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/940472/oauth2-login-for-on-premise-sharepoint-using-adfs
question_id: 940472
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# OAuth2 login for on premise sharepoint using ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/940472/oauth2-login-for-on-premise-sharepoint-using-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am looking to set up on premise Sharepoint API access using OAuth2.  I am wanting to use the device code flow to get an access token, then use that access token as a bearer token in api calls.    

I have struggled to find any documentation on this, the closest I have found is for AzureAD.  Is this authorization method even possible?    

My attempts to configure this in sharepoint return this error "Invalid audience Uri".  Which leads me to believe that I need to configure sharepoint different;y, but I can't seem to find any documentation for this.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-07-26*

Hi @tom harlock   ,    

You can refer to following steps to     

-  Adding SharePoint on-premises from the gallery    

-  Configure Azure AD single sign-on    

-  Configure SharePoint on-premises Single Sign-On    

-  Enable Azure Authentication provider to Sharepoint Web application    

-  Setup People picker to assign permission to the SharePoint site    

-  Test the single-sign-on    

Here is the document for details    

https://learn.microsoft.com/en-us/azure/active-directory/saas-apps/sharepoint-on-premises-tutorial    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
