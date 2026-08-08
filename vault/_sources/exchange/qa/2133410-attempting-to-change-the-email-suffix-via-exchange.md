---
title: "Attempting to change the email suffix via Exchange Server Failure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2133410/attempting-to-change-the-email-suffix-via-exchange
question_id: 2133410
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Attempting to change the email suffix via Exchange Server Failure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2133410/attempting-to-change-the-email-suffix-via-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Everyone else is on a different email suffix. Everyone else's suffix I'm able to change change, however I'm having issues with this user. They are on the .onmicrosoft and I'm hoping to drop that and switch to the companies normal suffix. I've switched the alias however the user cannot receive as their alias email name only their .onmicrosoft. Any help and/or suggestions are welcome. Much appreciated!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-19*

Hi @Chase Sartain，

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, you change the email suffix, the error "Error executing request. An Azure Active Directory call was made to keep object in sync between Azure Active Directory and Exchange Online." appears. Since users are synchronized with your local Active Directory, you need to add the alias locally instead of in the cloud. You can try the following steps to solve the problem:

-  Log in to the local Exchange admin center and double-click the mailbox to open the properties.

-  Click the email address and add it, uncheck Automatically update email addresses based on the email address policy applied to this recipient.

-  After adding the alias address, you can wait for a cycle (about thirty minutes) or use the AD powershell command `Start-ADSyncSyncCycle -PolicyType Delta` to force DirSync, then wait a few minutes and return to the Exchange Online mailbox organization information page to view the results.

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

Best,

Jeanne

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-12-18*

Are syncing from on-prem? The change has to be made there
