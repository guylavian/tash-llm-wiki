---
title: "ADFS Promote secondary to primary"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1068643/adfs-promote-secondary-to-primary
question_id: 1068643
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
---
# ADFS Promote secondary to primary

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1068643/adfs-promote-secondary-to-primary (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Am planning to promote secondary ADFS to primary ADFS, as stated here I can change using PS commands https://hippidikki.wordpress.com/2016/04/19/changing-adfs-primarysecondary-federation-serverin-a-farm    

But thing is will this also move the token signing certificates, Relying party trusts and Claim issuance as well?    

Thanks in advance.     

Regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-03*

Yes it worked fine on one of the test machine.     

In production I tried to install Federation service, I stuck in SPN account creation. I tried to setspn -Q http/einvpdssoadfs and got the results as one service user and used that in the secondary server to configure the ADFS service but got failed with SPN account.     

Attaching screenshot of the same.     

I tried creating SPN in primary server, but looks like it already created and not able to create new one. Any help would be much appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-03*

Hello there,    

The Token signing certificates will not be moved. It is common to think that a specific Enhanced Key Usage (EKU) is needed for the token-signing certificate, but this is, in fact, not correct. The only requirement for usage is that Key Usage (KU) must contain at least Digital Signature.    

You can follow this article to move the certificates or create new ones     

https://social.technet.microsoft.com/wiki/contents/articles/2311.ad-fs-1-0-and-1-1-how-to-replace-the-ssl-token-signing-and-federation-server-proxy-certificates.aspx    

--------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–
