---
title: "How to set up SAML with an IdP URL using ADFS?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/928580/how-to-set-up-saml-with-an-idp-url-using-adfs
question_id: 928580
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# How to set up SAML with an IdP URL using ADFS?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/928580/how-to-set-up-saml-with-an-idp-url-using-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a vendor that cannot do a direct relaying party trust with claims as is normal. Their engineer has asked if we can, using our ADFS, authenticate to them using an IdP URL. I am not finding much information about this for ADFS. Our ADFS is Server 2019, version 4.     

Is this setting up a trust and just using the IDP initiated sign on page?  ie. https://sts.contoso.com/adfs/ls/idpinitiatedsignon.aspx    

Can anyone point me in the right direction.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-15*

Take a look at this documentation for AD FS Troubleshooting - Idp-Initiated Sign On    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/troubleshooting/ad-fs-tshoot-initiatedsignon    

---------------------    

If this helps please don't forget to mark as correct answer. Thanks!
