---
title: "Remove Office 365 Federation from ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/757012/remove-office-365-federation-from-adfs
question_id: 757012
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Remove Office 365 Federation from ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/757012/remove-office-365-federation-from-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello   

I am currently trying to remove Office 365 authenication from our adfs server.  

I came across this article:  

https://social.technet.microsoft.com/wiki/contents/articles/34464.remove-office-365-federation-from-adfs-server.aspx  

My question is by performing the above steps, will the users now authenticate directly with Office 365 instead of the ADFS server and is there any other config required?  

Thanks

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-03-03*

Launch the Azure AD Connect wizard.    

Select Change user-sign.    

    

Pick the method you want (you should be set to Federation with AD FS) at the moment. For example PHS:    

    

Then Next and follow the steps.
