---
title: "Asking about creating a local user with a GPO in Windows Server 2019."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5553606/asking-about-creating-a-local-user-with-a-gpo-in-w
question_id: 5553606
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Asking about creating a local user with a GPO in Windows Server 2019.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5553606/asking-about-creating-a-local-user-with-a-gpo-in-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears,  

I need to ask about creating a local user with a GPO in Windows Server 2019 for unifying the local admin on the PC with a specified password.

Navigate to Computer Configuration > Preferences > Control Panel Settings > Local Users and Groups.

When I choose to create, all options are hidden.

If there is any other way, kindly guide me.

## Answer (community) — Independent Advisor

*upvotes: 1 · updated: 2025-09-13*

Hello Mohamed,

This behavior often occurs when the Group Policy Management Console (GPMC) is being run on a system that doesn’t match the target architecture or OS version. To resolve this, please ensure you're editing the GPO from a Windows Server 2019 machine or a Windows 10/11 client with the RSAT: Group Policy Management Tools installed and fully updated.

Additionally, confirm that you're using the 64-bit version of the GPMC if your clients are 64-bit. In some cases, launching GPMC with elevated privileges (Run as Administrator) can also restore visibility to the configuration fields.

Once the interface is functioning properly, you can proceed to:

Set Action to “Update” (recommended for modifying existing accounts)

Specify the username (e.g., Administrator)

Set the desired password

Configure options like “Password never expires” or “User cannot change password” as needed

Make sure the GPO is linked to the correct OU and that the target machines have permission to apply it. You can verify GPO application using `gpresult /h` or the Group Policy Event Log.

=====

I hope this helps you move forward with your deployment. If this guidance clears things up, feel free to hit “Accept Answer”—always great to know when the solution lands well 😊

T&B, Harry.
