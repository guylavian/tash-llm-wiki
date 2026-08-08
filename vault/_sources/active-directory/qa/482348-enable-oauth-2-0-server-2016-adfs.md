---
title: "Enable oauth 2.0 server 2016 adfs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/482348/enable-oauth-2-0-server-2016-adfs
question_id: 482348
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Enable oauth 2.0 server 2016 adfs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/482348/enable-oauth-2-0-server-2016-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have a server 2016 with ADFS on it. I just CRM and they asked to provide following details:  

-  Client ID  

-  Tenant ID  

and OAuth version should be 2.0.  

The ADFS and AD server is on-Prem.  

ADFS is on Server 2016  

We will have (physical) App server provided by vendor.  

We got the link from the vendor saying - "Link to enable Auth"-  

http://shorturl.at/jsHLN  

on which we need Single Page App.  

However, what information I would need to configure the same? and How to configure it?  

I am not sure how to go about that. Can someone help with the instructions on this?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-07-20*

Here is the documentation to build a Single App Page with ADFS: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/development/single-page-application-with-ad-fs    

But since here you are talking about a Tenant ID, is that possibe that your app wants un fact an Azure AD domain?
