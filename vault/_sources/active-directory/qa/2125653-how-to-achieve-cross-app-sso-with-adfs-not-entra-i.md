---
title: "How to achieve cross app sso with ADFS not entra ID"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2125653/how-to-achieve-cross-app-sso-with-adfs-not-entra-i
question_id: 2125653
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-authenticator", "microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to achieve cross app sso with ADFS not entra ID

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2125653/how-to-achieve-cross-app-sso-with-adfs-not-entra-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Based on this article https://learn.microsoft.com/en-us/entra/identity-platform/msal-android-single-sign-on

How to achieve Cross APP SSO with ADFS Account?

I have my environment running full on premise with ADFS 2019, Exchange server 2019 CU 14.

I've already tried the cross app SSO with entra id. But how to achieve it with on premise account with my environment account?

My Goal is to have cross app sso but with adfs account (auto logged in with outlook). I already achieve it with entra id but can't with adfs account.

Is it possible?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-04*

Hi @Bayu Aji Setyawan  ,

Welcome to the Microsoft Q&A platform!

Yes, it is possible to achieve cross-app Single Sign-On (SSO) with an ADFS account in your on-premises environment. Here is a high-level overview of the configuration steps:

-  ADFS Configuration:

-  Set up relying party trusts for your applications.

-  Configure claims rules to pass the necessary user information.

-  MSAL Configuration:

-  Use the authority parameter in MSAL to point to your ADFS instance.

-  Enable brokered authentication by setting the broker_redirect_uri.

-  Ensure the Microsoft Authenticator or Intune Company Portal app is installed on the user's device.

For detailed guidance, you can refer to the Microsoft documentation on enabling cross-app SSO using MSAL.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
