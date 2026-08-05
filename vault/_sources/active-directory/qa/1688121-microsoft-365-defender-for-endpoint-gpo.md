---
title: "Microsoft 365 Defender for endpoint GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1688121/microsoft-365-defender-for-endpoint-gpo
question_id: 1688121
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Microsoft 365 Defender for endpoint GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1688121/microsoft-365-defender-for-endpoint-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

We are in phase of implementing Microsoft 365 defender for endpoint and we are not going to use Intune for deployment. We are using service similar to intune for mobile device management.

My question is how can we use GPO for defender config? Where to download gpo extension and how to configure it.?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-28*

Hi Neuvi,

Do we need to import admx and adml into GPO to be able to use defender settings or we can use default one which already are present in gpo? Will it work with Microsoft 365 defender of endpoint?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-28*

Hi Troops,

Thank you for posting in the Q&A Forums.

Configuring Windows Defender through Group Policy Objects (GPOs) is an efficient way to centrally manage Windows Defender settings.

 

In the Group Policy Management tool, create a new Edit Group Policy and navigate to the following path:

Computer Configuration -> Administrative Templates -> Windows Components

Under it, you can find Windows Defender related folders, such as “Microsoft Defender Antivirus”, which you can configure.

Best regards

NeuviJ

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-28*

Hi Troops,

Thank you for posting in the Q&A Forums.

Configuring Windows Defender through a Group Policy Object (GPO) is an efficient way to centrally manage Windows Defender settings.

In the Group Policy Management tool, create a new Edit Group Policy and navigate to the following path:

Computer Configuration -> Administrative Templates -> Windows Components

Under it, you can find Windows Defender related folders, such as “Microsoft Defender Antivirus”, which you can configure.

Best regards

NeuviJ

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-27*

Follow https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
