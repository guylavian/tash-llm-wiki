---
title: "Missing GPO for LAPs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191818/missing-gpo-for-laps
question_id: 2191818
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 6
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# Missing GPO for LAPs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191818/missing-gpo-for-laps (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a domain controller running on 2019 server, with domain/forest function level of 2016, and all updates are installed. I am enabled LAPs for our servers and trying to implement GPOs to start this process. However, there seems to be a group policy rule missing that was in our dev and stage environments ( different domain controllers in their own domain separate from production). The group policy is:  

Computer Configuration -> Policies -> Admin Templates -> Systems -> LAPS -> Enable Local Admin Password Management. 

Has anyone come across this issue before? or know how to import this into group policy management? google searches always seem to point to installing KB5025229 (which it was previously installed). any help would be appreciated.

as a side note i did try and copy the admx from the dev and stage over to prod, however i go some premission denied error related the "trusted installer" being the owner.

## Answer (community) — community member

*upvotes: 1 · updated: 2025-01-04*

Thank you, but i still have problems.  

I found "LAPS" in administrative template\system but not in administrative template root. There are 9 settingsand but not the  "enable local password management" setting . I Folowed all the steps (included copy files in policydefinitions folder

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-29*

Hello 

Thank you for posting in Microsoft Community forum.  

1.Make sure you are update the schema in the forest.

2.How does the ADMX file retrieve from? Local computer or central store？

C:\Windows\PolicyDefinitions

C:\Windows\PolicyDefinitions\En-US

Or

\a.com\SYSVOL\a.com\Policies\PolicyDefinitions

\a.com\SYSVOL\a.com\Policies\PolicyDefinitions\En-US

 Please check it here.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
