---
title: "ADFS - Claim Provider Authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/468641/adfs-claim-provider-authentication
question_id: 468641
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS - Claim Provider Authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/468641/adfs-claim-provider-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

How to disable the default "Active Directory" Claims Provider Trusts and use the new one was added?    

When the new one is enabled, it shows in the screen for the user to chose which one to go. When I disable the new one, it goes straight to the default Active Directory, so in my case now I want to disable the AD and have only the new one enabled.    

How to make this change?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-07-09*

Changing the claim provider is a very impactful operation. I doubt you we will have to swtich back and forth between two. I mean, it would require the applications to handle new IDs, and the CPs to have some mapping rules to maintain access when switching.  

But in theory, you can script it. Eventually, you can do a loop, instead of calling manually the cmdLet.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-08*

oh I found this - https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/home-realm-discovery-customization that says I have to use this command:    

Set-AdfsRelyingPartyTrust -TargetName App1 -ClaimsProviderName @("New One Just Added and Working")    

So, if I have 50 Apps, I have to maybe do this command 50 times, what is not a problem.    

But in case, for some reason, the "New One Just Added and Working" stopped working, and I need to rollback, I will need to 50 times do the same command, but using:    

Set-AdfsRelyingPartyTrust -TargetName App1 -ClaimsProviderName @("Active Directory")    

Maybe there is no efficient way like a simple "enable/disable" right click for the "Active Directory" as it has for the "New One Just Added and Working"? And that's why the above command is needed?
