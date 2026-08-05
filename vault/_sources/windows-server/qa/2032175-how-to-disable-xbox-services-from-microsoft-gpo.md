---
title: "How to disable xbox services from Microsoft GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2032175/how-to-disable-xbox-services-from-microsoft-gpo
question_id: 2032175
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-iot", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to disable xbox services from Microsoft GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2032175/how-to-disable-xbox-services-from-microsoft-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi gents,

I wanted to ask if you know why domain controller  GPM services in a GPO won't show XBOX services in the list.

some workstations in the domain have XBOX services in them and we want to have them disabled, to do that we want to apply a GPO and push to devices but when I looked for them they were not in the list of services

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2024-09-02*

Hello,

Thank you for posting in Q&A forum.

I recommend that you use Group Policy to disable Xbox through AppLocker at the following path: Computer Configuration > Windows Settings > Security Settings > Application Control Policies > AppLocker > Packaged app Rules > Microsoft.XboxApp.

I hope the information above is helpful.

Best regards

Zunhui

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
