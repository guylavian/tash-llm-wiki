---
title: "Customize Only Local Admin Profile Through GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1415894/customize-only-local-admin-profile-through-gpo
question_id: 1415894
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# Customize Only Local Admin Profile Through GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1415894/customize-only-local-admin-profile-through-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Is it possible to customize the Local Administrator Profile of Windows 10,11 domain PCs through a GPO, like skipping the customization screens on the first login of the admin account?

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-17*

Hello
Yes, it is possible to customize the Local Administrator Profile of Windows 10,11 domain PCs through a Group Policy Object (GPO). You can manage local administrators on your domain PCs through GPO.
 
To skip the customization screens on the first login of the admin account, you can disable the first sign-in animation using the Windows Registry or Group Policy Object. Here are the steps to disable the first sign-in animation:
 
Open the Windows Group Policy Editor. To open it, launch the ‘Run’ dialog box, type gpedit.msc and hit Enter key.
Go to Local Computer Policy > Computer Configuration > Administrative Templates > System > Logon.
Within Logon, on the right side, you’ll notice an option reading Show first sign-in animation. Double-click on this policy to open its Configuration box.
Set it to Disabled.
 
This policy setting allows you to control whether users see the first sign-in animation when signing in to the computer for the first time. This applies to both the first user of the computer who completes the initial setup and users who are added to the computer later. It also controls if Microsoft account users will be offered the opt-in prompt for services during their first sign-in.
 
Please note that these steps require administrative privileges. If you do not have administrative access, you may need to request it from your system administrator.
 
Best Regards,
Wesley Li

If the Answer is helpful, please click "Accept Answer" and upvote it.
