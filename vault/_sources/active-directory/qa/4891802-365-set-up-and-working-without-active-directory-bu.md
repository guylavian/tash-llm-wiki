---
title: "365 set up and working without active directory but I want to set it up now"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4891802/365-set-up-and-working-without-active-directory-bu
question_id: 4891802
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# 365 set up and working without active directory but I want to set it up now

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4891802/365-set-up-and-working-without-active-directory-bu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When we transitioned to 365, I did not set up the Azure active directory or anything.  I just added users and then had them logging into to the portal once they were logged into their pcs.  I did set up explorer shortcuts for them but that's about it.  I'm
 now being told this wasn't really the best way to do this for things like deploying updates, security, etc.  So, i have no idea how to go back and add this.  All the references I can find are to how to bring existing active directory from your existing server
 into 365.  Has anyone done what I (think) I need to do?  Is their a guide?  Is it worth the effort as most of the pcs we are have are remote from our very small (and only) office?  Thanks for any advice...

## Answer (community) — community member

*upvotes: 0 · updated: 2015-12-24*

Hi AdminUDC,  

For the detailed procedure of setting up an on-premises Active Directory server, I suggest you visit the
Windows Server support forum since the engineers and community members there are professional about it. Our forum mainly focuses on Office 365 online services.  

As to the fact that you have already created online user accounts before setting up your on-premises Active Directory server, I'd like to let you know that you can use
SMTP matching to link an Office 365 online user account with an on-premises Active Directory user account, so they can be synchronized thereafter. Please refer to
How to use SMTP matching to match on-premises user accounts to Office 365 user accounts for directory synchronization.  

Thanks,  

Allen
