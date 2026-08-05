---
title: "Exchange Online - Purview Retention Policy Not Working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1663527/exchange-online-purview-retention-policy-not-worki
question_id: 1663527
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online - Purview Retention Policy Not Working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1663527/exchange-online-purview-retention-policy-not-worki (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am having issues with an Exchange Online retention policy not taking affect properly.  I created a Purview tag and rule to permanently delete any Deleted Items email older than 31 days old.  I assigned that rule to one specific user, myself, to test, but the policy has not taken any action.  I also followed along with the troubleshooting steps in the below link to no avail.  Any help would be greatly appreciated.  

https://answers.microsoft.com/en-us/msoffice/forum/all/retention-policies-not-working/300b2497-cd7e-40fc-b1e7-22e6406e4fbc?page=3 

Thanks,

Phil

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-07*

The retention "age" for items in the Deleted items folder is calculated differently, as detailed here: https://learn.microsoft.com/en-us/exchange/security-and-compliance/messaging-records-management/retention-age#determining-the-age-of-different-types-of-items

Other than that, there are some caveats for the tag itself, as at one point Microsoft decided items within the Deleted items folder should not be automatically removed. Long story short, they ignore the "default" Delete items tag, so you either have to create a new one, or create a new MRM policy (or rename the default one). Details are here: https://www.michev.info/blog/post/5868/make-sure-deleted-items-are-automatically-removed-from-microsoft-365-mailboxes
