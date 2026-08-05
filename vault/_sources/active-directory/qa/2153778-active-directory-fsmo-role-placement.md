---
title: "Active Directory FSMO role placement"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2153778/active-directory-fsmo-role-placement
question_id: 2153778
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory FSMO role placement

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2153778/active-directory-fsmo-role-placement (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts,

We have five domain controllers in HQ site listed as below:

DC1

DC2

DC3

DC4

and two domain controllers in the DR site.

 All FSMO roles are placement on DC1.

What's the best practice to distribute the roles.?

Thanks

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-03*

Hello Ahmed Essam,  

Thank you for posting in Q&A forum. 

Here is a document about detailed FSMO placement, you can read it.

FSMO placement and optimization on Active Directory domain controllers

https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/fsmo-placement-and-optimization-on-ad-dcs

I hope the information above is helpful. 

If you have any questions or concerns, please feel free to let us know. 

Best Regards, 

Daisy Zhou

 ============================================ 

If the Answer is helpful, please click "Accept Answer" and upvote it.
