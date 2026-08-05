---
title: "how can i Disable-AdfsClaimsProviderTrust  -TargetName \"Active Directory\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/338912/how-can-i-disable-adfsclaimsprovidertrust-targetna
question_id: 338912
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# how can i Disable-AdfsClaimsProviderTrust  -TargetName "Active Directory"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/338912/how-can-i-disable-adfsclaimsprovidertrust-targetna (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I just want to use custom Claims Provider Trust  .    

so i execution Disable-AdfsClaimsProviderTrust  -TargetName "Active Directory"    

i has an error    

    

how can i disable "Active Directory"     

I don’t want to select on this page, I want to jump directly to my Claims Provider Trust  “cas”

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-10-18*

set both of these    

Set-AdfsProperties -IntranetUseLocalClaimsProvider $false    

Set-AdfsProperties -EnableLocalAuthenticationTypes $false
