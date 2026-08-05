---
title: "Windows LAPS not rotating local admin passwords automatically"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5876156/windows-laps-not-rotating-local-admin-passwords-au
question_id: 5876156
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Windows LAPS not rotating local admin passwords automatically

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5876156/windows-laps-not-rotating-local-admin-passwords-au (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We recently migrated to the built-in Windows LAPS for Entra ID. The initial password generates and saves to the cloud perfectly. But the auto-rotation after 30 days just... isn't happening. I can manually force a rotation from the portal, but it refuses to do it on schedule. Anyone seen this behavior before?

## Answer (community) — community member

*upvotes: 1 · updated: 2026-04-30*

Automatic rotation depends entirely on the password expiration time that Windows LAPS has stored in Microsoft Entra ID and on the device processing LAPS policy successfully. When that expiration time is reached, the device rotates the password and writes the new password and new expiration back to Entra ID.

From the documented behavior:

-  After the initial password is generated, Windows LAPS computes and stores a password expiration time based on the policy’s password age setting (for example, 30 days).

-  The device then automatically rotates the password when that stored expiration time is reached, and again stores a new password and a new expiration time in Entra ID.

-  Passwords stored in Entra ID are protected by role-based access control, but Entra ID does not support “forcing” expiration by editing the expiration timestamp in the directory; the device itself must decide the password is expired and rotate it.

For early/manual rotation and verification on Entra-joined devices:

-  Use `Reset-LapsPassword` on the device to force a rotation, then `Get-LapsAADPassword -DeviceIds <deviceId> -IncludePasswords -AsPlainText` to confirm the new password and that the rotation path is working end to end.

-  Intune can also trigger a manual rotation via the Rotate local admin password device action. This requires the device to be online at the time of the request and to have successfully backed up its LAPS data; otherwise the rotation fails.

-  Each manual rotation resets the “PasswordAgeDays” timer. For example, if PasswordAgeDays is 10 and a manual rotation is done on March 5, the next scheduled rotation is 10 days from March 5, not from the original policy date.

Given that manual rotation works in the portal but scheduled rotation does not, focus on these checks:

-  Confirm that the LAPS policy is actually applied and not in conflict on the device (for example, only one effective policy, with the expected PasswordAgeDays value).

-  Confirm that the device is successfully backing up its password and expiration to Entra ID (since devices that haven’t successfully backed up their data cannot complete rotations).

-  Use `Reset-LapsPassword` once and then wait beyond the configured PasswordAgeDays interval to see if automatic rotation occurs, verifying with `Get-LapsAADPassword`.

-  Avoid trying to “force” expiration by editing timestamps in Entra ID; this is not supported and will not trigger rotation.

If these checks show that policy is applied, backups are succeeding, and a single `Reset-LapsPassword` correctly updates the password and expiration in Entra ID, automatic rotation should follow the configured PasswordAgeDays schedule.

References:

-  Get started with Windows LAPS and Microsoft Entra ID

-  Key concepts in Windows LAPS

-  Microsoft Intune support for Windows LAPS

-  Deploy Windows LAPS policy with Microsoft Intune

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-04-30*

HI Luyng,

Yes, this is a known issue with Windows LAPS in Entra ID when relying solely on the scheduled rotation policy. The rotation interval is enforced by the LAPS client service on the device, not by Entra ID itself, and it requires that the policy setting `PasswordAgeDays` is correctly applied via Intune or Group Policy. If the device doesn’t receive or honor that policy, the password will never auto‑rotate. Check under `HKLM\SOFTWARE\Microsoft\Policies\LAPS` that `PasswordAgeDays` is set to 30 and confirm the device has the latest cumulative update (LAPS fixes were included in KB5035857 and later). Also verify that the scheduled task `\Microsoft\Windows\LAPS\PasswordExpiration` exists and is not disabled. If all of that looks correct but rotation still doesn’t trigger, it’s typically a bug in the current LAPS client build, and Microsoft has acknowledged it in recent release notes. In that case, the only reliable workaround is manual rotation until the next servicing update resolves the scheduler issue.

If the above response helps answer your question, please hit "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

Domic V.
