---
title: "how to disable xbox at startup via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197315/how-to-disable-xbox-at-startup-via-gpo
question_id: 2197315
fetched: 2026-07-25
answer_count: 10
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# how to disable xbox at startup via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197315/how-to-disable-xbox-at-startup-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

how to disable xbox at startup via GPO

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-21*

no you didn't get my point , maybe my problem

now i have Windows server 2012R2 AD and i have laptops running windows 11 and Xbox appears on the Apps so i want to disable/remove so i want to perform that via Gany Group Policy on the AD to be centralized.

i tried your first comment way but still xbox exist so any other suggestions .

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-21*

Windows Server is primarily designed for enterprise and server environments, so it doesn't include Xbox apps, online gaming services, or drivers related to Xbox, let alone auto-starting Xbox.

Why did you think about disabling Xbox on Windows Server?

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-20*

thanks for reply Yuhao but now i have AD windows server 2012R2 and i can't find Microsoft.XboxApp package at the menu so please can you help in that ?

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-20*

thanks for reply Yuhao but now i have AD windows server 2012R2 and i can't find Microsoft.XboxApp package at the menu so please can you help in that ?

Regards ,Ahmed

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-17*

Hello, Ahmed Shaban

Welcome to Microsoft Community.

To disable the Xbox app at startup via Group Policy (GPO), you can follow these steps:

-  Open Group Policy Management:

-  Press `Windows + R` to open the Run dialog box.

-  Type `gpedit.msc` and press Enter to open the Group Policy Editor.

-  Navigate to AppLocker:

-  Go to `Computer Configuration` > `Windows Settings` > `Security Settings` > `Application Control Policies` > `AppLocker `> `Packaged app Rules`.

-  Create a New Rule:

-  Right-click on the blank pane and select `Create New Rule`.

-  Follow the wizard to create a rule that blocks the `Microsoft.XboxApp` package.

Yuhao L

Microsoft Community Technical Support
