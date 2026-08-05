---
title: "Newly created users in Active Directory show up as account uknown"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/586305/newly-created-users-in-active-directory-show-up-as
question_id: 586305
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Newly created users in Active Directory show up as account uknown

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/586305/newly-created-users-in-active-directory-show-up-as (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After a new user has been created in AD when adding the user to folder security properties the user instantly shows up account unknown.  The new user and the account unknown have the same SID.    

Also when searching for the user I have to select Entire Directory, if I choose the domain and the OU the user is in nothing comes up.  Any ideas on what would cause this?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-12*

Hello @Brian A. Shook       

Generally, Account Unknown may appear if the system cannot find the account SID which was recorded in ACL of an object in local system or AD database. This issue may occur if user accounts were deleted or the Account Unknown belongs to other system(dual boot configuration). This is reason that we recommend granting permission on resources to the Domain Local security group instead of individual users. It will be much easier for management and will not generate orphaned SID because user group is stabler.    

Hope this helps with your query!    

------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-10-11*

Might try connecting to a different domain controller. Sounds like there may be some broken replication. This tool might help.  

https://www.microsoft.com/en-us/download/details.aspx?id=30005  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
