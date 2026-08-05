---
title: "Restricting Desktop Customization with GPO on Windows Server 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2150748/restricting-desktop-customization-with-gpo-on-wind
question_id: 2150748
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Restricting Desktop Customization with GPO on Windows Server 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2150748/restricting-desktop-customization-with-gpo-on-wind (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm aiming to create a Group Policy Object (GPO) to make the local desktop read-only for all users. This means users should be able to view all icons on the desktop but not modify their arrangement, add new ones, or delete existing ones.

What is the most effective GPO configuration to achieve this? Which specific settings should I modify to completely block desktop customization while still allowing all icons to be visible?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-23*

Hello Raffaele Leto，  

Thank you for posting in Q&A forum.

You can try the method in the similar thread below.

https://answers.microsoft.com/pt-br/windowserver/forum/all/impedir-salvamento-local-na-%C3%A1rea-de-trabalho/ef871e34-20dd-4430-ada9-84765553eb60

Note: Deny everyone all permissions （except Read） on the desktop, so this user only can read his/her desktop.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
