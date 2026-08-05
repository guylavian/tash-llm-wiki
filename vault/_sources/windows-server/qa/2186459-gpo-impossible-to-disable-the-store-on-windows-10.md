---
title: "GPO - Impossible to disable the store on Windows 10/11 Pro"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186459/gpo-impossible-to-disable-the-store-on-windows-10
question_id: 2186459
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 7
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# GPO - Impossible to disable the store on Windows 10/11 Pro

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186459/gpo-impossible-to-disable-the-store-on-windows-10 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Following this article, I noticed that we need Enterprise/Education OS version to disable the Microsoft Store :  https://learn.microsoft.com/en-us/troubleshoot/windows-client/group-policy/cannot-disable-microsoft-store

There is also an alternative which consists in blocking C:\Program Files\WindowsApps but it is not "Microsoft officiaI" and I don't wish to apply such a solution.

Is there another way to disable Microsoft Store or at least some of the application types such as games,...?

Thanks for your feedback.

## Answer (community) — community member

*upvotes: 3 · updated: 2025-01-09*

Hello,

I confirm.

The only solution we found was to activate this feature in the GPO : Only display the private store within the Microsoft Store.

(it is redirecting the store to "nothing" and blocking the Microsoft Store in our case)

## Answer (community) — community member

*upvotes: 1 · updated: 2025-01-09*

So just to be clear, there is a policy to disable the MS Store. But Windows 11Pro is designed for not applying this policy. Does this sound right to you?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-29*

Hi Yann M98800,

Can't disable Microsoft Store via Group Policy - Windows Client | Microsoft Learn  

The link has already said that it is not possible to make relevant settings for Win110 Pro via GPO, this is so designed on the system side and we are not able to make changes to the system design. 

Best regards

Neuvi Jiang

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-29*

I have a lot of computers and the purpose is a GPO.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-29*

Hi Yann M98800,

Thank you for posting in the Microsoft Community Forums.

You can use the local security policy feature of your operating system. The following are the steps that can be used to enable or disable the Microsoft Store application.

-  Click the Windows Search or Start Menu button, and then type Local Security Policy in it to turn it on.

-  Locate the Software Restriction Policies folder and right-click on it.

-  Select “New Software Restriction Policies” to create a new one.

-  On the right hand side, under Object Types, you will see a folder icon with the text “Additional Rules”. Right-click on it and select “New Path Rule...”.    

-  To disable the Microsoft Store, type in the path where the App Store app is installed on Windows 10.

-  Select level- Disallowed and click the Apply button.    

Best regards

Neuvi Jiang
