---
title: "GPO to let standard user run applications that need elevated privileges"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185655/gpo-to-let-standard-user-run-applications-that-nee
question_id: 1185655
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# GPO to let standard user run applications that need elevated privileges

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185655/gpo-to-let-standard-user-run-applications-that-nee (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have some apps that needs to be used on our LAN, on the clients PCs. But some of those apps needs "elevated privileges" to run, that means, the user must belong to the administrators group. That would be a hole for our workstation security, so, how can solve this?. Is there any GPo that can help the users to run some apps with "administrator privileges"?, without knowing the admin password, of course. 

Please, help

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-02*

Hello.

Yes is possible....create a GPO with this 2 settings.

-  Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options.

-  User Account Control: Run all administrators in Admin Approval Mode

-  Enabled

-  Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options.

-  User Account Control: Behavior of the elevation prompt for administrators in Admin Approval Mode

-  Elevate without prompting

These settings will allow non-administrative users to run certain applications with elevated privileges

I hope this helps

Regards
