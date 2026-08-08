---
title: "ADFS Device Trust Level not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/295461/adfs-device-trust-level-not-working
question_id: 295461
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Device Trust Level not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/295461/adfs-device-trust-level-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

ADFS Device Trust Level not working  

I currently have Intune configured with Azure Device writeback enabled. I have Azure AD P2 and Mobility and security E5 licenses. I can see all devices and their attributes in AD under RegisteredDevice OU.  I am trying to restrict external access to an App to only Managed devices. Whenever I set the relay trust to only allow managed devices, I notice the Device claims are not showing up, so all access externally gets blocked.  

I used Claims Xray, and the device Claims are not listed like ISManaged. Does something else need done to get this working?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-03-03*

Device Authentication only works in the legacy IE browser.    

The recommended direction is to use Azure AD Conditonal Access Policies when we need to do device filtering.    

In your case, you would need to migrate the relying party trust from ADFS to an Enterprise App in Azure AD.    

If you installed Azure AD Connect Health for ADFS you will have access to a report in Azure AD telling you if and how to migrate the application to Azure AD:
