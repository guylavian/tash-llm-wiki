---
title: "ADFS migration from one farm to another"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/29424/adfs-migration-from-one-farm-to-another
question_id: 29424
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS migration from one farm to another

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/29424/adfs-migration-from-one-farm-to-another (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My company own 2 ADFS farms, lets call them fed1.company.com and fed2.company.com. Both farms run on server 2016 and consist of 2 ADFS servers and 3 WAP servers.  

Fed1 currently hosts the RPT for O365, fed2 hosts several 3th party RPT's. The goal is to move the O365 RPT to fed2, and eventually get rid of the fed1 farm.  

What steps would I need to perform to move the current O365 RPT from fed1 to fed2?  

I have been searching online but the information I found seems to be a bit inconclusive.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-07-05*

I would suggest to re-create the RPT to new farm similar to old RPT including claim rules.  

then communicate to application owner with new metadata and certificate (if required).  

post switch over from app team you can disable/delete the RPT from old farm.  

If in case of more RPT then do it in Powershell.  

I have performed similar activity (approx. 250+) from 2012 to 2019.   

All the best.!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-05-25*

I would start by saying that you do not require ADFS for Single Sign On with Azure AD. You can use the Azure AD Connect Seamless SSO option to achieve this. So the easiest way for you might just be to get rid of ADFS for Azure AD workload (such as Office 365).    

Now, you can set up the trust on ADFS and update it in Azure AD using the Azure AD Connect wizard. Look at the section Modify the AD FS configuration.
