---
title: "Verification of prerequisites for active directory preparation failed. Unable to create ADPrep Log Files."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1155666/verification-of-prerequisites-for-active-directory
question_id: 1155666
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Verification of prerequisites for active directory preparation failed. Unable to create ADPrep Log Files.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1155666/verification-of-prerequisites-for-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I already assigned user a Admin permission but I am still getting the 2nd error, not sure how to fix the first problem.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-09*

Hi. Thank you for your question and reaching out. I’d be more than happy to help you with your query.    

You can try to adjust the group membership, try making the Enterprise Admin group the primary group, logging out the server, and then logging back in.    

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-08*

Hi,    

Check if the account you are using is member of local administrators group of the server where you want launch the adprep.    

Please don't forget to mark helpful reply as answer

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-01-08*

Not much to go on but looks like the user does not have permissions. Might try again with a domain administrator account.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
