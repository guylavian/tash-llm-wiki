---
title: "ADFS Bypass MFA for Outlook Mobile Clients"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1112362/adfs-bypass-mfa-for-outlook-mobile-clients
question_id: 1112362
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# ADFS Bypass MFA for Outlook Mobile Clients

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1112362/adfs-bypass-mfa-for-outlook-mobile-clients (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have some users using a basic auth app for email using ActiveSync - they current use ADFS to logon and there is no MFA for them as they dont support modern auth. All fine so far.     

We want to migrate them to Outlook Mobile (android mainly but some iOS) but we dont want them prompted for MFA (well not yet anyway). MFA is enabled for most office 365 services at the moment.     

What can i add to my claim rule (or other areas in MFA) to allow Outlook Mobile users (but not other outlook users) to bypass MFA.    

We dont want the user to be bypassed, just the outlook mobile app. or if thats not possible just the mobile phone.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-07*

This is for on-prem MFA via on-prem ADFS not azure based so I don't think that would work?    

Basically we want this: https://newsignature.com/articles/bypassing-multi-factor-authentication-using-ad-fs-claims-rule/    

But instead of activesync it would be for whatever protocol Outlook Mobile uses (which i dont think is activesync anymore).    

Thanks

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2022-12-06*

Hi @GaryKane-8672     

if you use Security Defaults in your tenant, all users will be prompted for MFA.    

However, if using Azure AD Premium P1/P2, you can use Conditional Access policies to bypass MFA for certain platforms, apps or devices if required.    

    

Hope this helps,    

Thanks    

Michael Durkan    

-  If the reply was helpful please upvote and/or accept as answer as this helps others in the community with similar questions. Thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-06*

I dont think your answer is right, you can have claims rules bypass MFA for various application or device based attributes.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-02*

Hi @GaryKane-8672 ,    

Welcome to our forum!    

As i know, MFA can only be enabled or disabled for accounts, but not enabled for devices. I'm afraid that your requirement cannot be achieved. More information: Enable or disable modern authentication for Outlook in Exchange Online.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
