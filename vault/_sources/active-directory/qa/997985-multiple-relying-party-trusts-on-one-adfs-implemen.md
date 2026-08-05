---
title: "Multiple Relying Party trusts on one ADFS implementation - drawbacks?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/997985/multiple-relying-party-trusts-on-one-adfs-implemen
question_id: 997985
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Multiple Relying Party trusts on one ADFS implementation - drawbacks?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/997985/multiple-relying-party-trusts-on-one-adfs-implemen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 365 as the only relying party trust.    

If we add another for another service, is it muddying the waters in any way? Is it adding more overhead or complexity to updates, certificate renewals, troubleshooting, migrations, etc?    

I just want to be able to speak intelligently about it and understand the risks.    

thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-09*

Appreciate the follow-up.    

Our business utilizes on-premise datacenter resources that we don't want in Azure, so moving all those workloads to Azure isn't a priority. Also, Microsoft MFA kind of sucks. There are third party vendors that do it better that are more flexible with other third party products.     

Again if you are pure microsoft house, using web apps, then sure. if you have business apps that require applications that aren't web-based, then what you are suggesting is thousands of miles away.    

Could you elaborate on using 365 authentication on our on-premise AD accounts? or is that not what you're referring to?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-07*

I guess your reply is more of a philosophical one, or maybe more accurately a Microsoft azure monolithic view. I do understand that opinion. I do understand Microsoft wants everyone to move in that direction and to see any on-prem or third-party activity as legacy, however that's not practical nor realistic.    

Thanks for your input, but If we need ADFS for 365 sso authentication for our on-premise users, but also have a need for another 3rd-party authentication piece, the original question still stands.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-07*

Well, every time you add a relying party it adds more "complexity" -  ADFS is in of itself additional legacy complexity.     

I would argue that if you have a presence in Azure, you should adding any new federation with new services there and not in ADFS.     

The goal should be to move off of ADFS and into a managed Azure auth architecture and not adding more relying parties to ADFS. :)     

https://learn.microsoft.com/en-us/azure/active-directory/hybrid/migrate-from-federation-to-cloud-authentication
