---
title: "active directory login and teams account are different"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1685631/active-directory-login-and-teams-account-are-diffe
question_id: 1685631
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-teams-teams-business-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# active directory login and teams account are different

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1685631/active-directory-login-and-teams-account-are-diffe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Teams account that is different than the AAD Azure Active Directory account. Changing meeting options is difficult because the url when changing the meeting options does not allow the active directory account the ability to change the meeting option because the AD account is not an organizer of the meeting (even though I have setup 2 organizers - the AAD account holder and the Teams meeting account holder).

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-24*

Hi @Scott Clamp  

According to our official documentation, co-organizers have many of the same features as meeting organizers during a meeting, but they cannot make changes to the meeting before it starts.

To allow co-organizers to change meeting options in a channel meeting, they must be invited directly in the channel meeting invitation. This means that if co-organizers are added after the meeting starts, they may not be able to change meeting options.

In Microsoft Teams, if you want to invite co-organizers directly in your channel meeting invitation, you can follow these steps.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
