---
title: "ADFS Setup and O365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/765694/adfs-setup-and-o365
question_id: 765694
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Setup and O365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/765694/adfs-setup-and-o365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am very new to Office 365 as well as setting up ADFS.  I have watched a few videos on setting up ADFS and it seems fairly straight forward.  However, enabling ADFS with Office 365 seems a bit more complex that some other vendors.  I am going to install ADFS, then a few weeks later configure Office 365 for SSO.  The videos I have seen talk about configuring ADFS and Office 365 at the same time which we are not doing.  Is there a good step by step (preferably video) guide on how to setup ADFS and Office 365 after ADFS server is up and running?  Also, do I need a webproxy?  If so, is there a step by step on setting up a webproxy for ADFS\Office 365?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-10*

My boss wants ADFS with O365.  I have been with the company 2 months and have zero O365 experience so I do not have the knowledge to change his thinking.  Any info on this would be helpful.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-03-10*

You do not need AD FS to use Office 365. Is there a reason why you are looking at deploying AD FS? If that's for SSO, that's not required. If that's to have authentication taking place on premises because you don't want to sync the hash of your users' passwords, that's also not required. The list of cases were AD FS is needed for Azure AD is very slim. Usually in 2022, customers are looking at moving away from the AD FS dependency.     

That said, the easiest way to deploy AD FS (and again, I think you shouldn't) is to use the Azure AD Connect wizard. There is a step by step documentation with screenshots available here: https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-install-custom#configuring-federation-with-ad-fs     

But please, do tell us more about the why AD FS? :)
