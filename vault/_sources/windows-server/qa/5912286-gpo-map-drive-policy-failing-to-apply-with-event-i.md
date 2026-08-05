---
title: "GPO map drive policy failing to apply with Event ID 4098 - Error code 0x80070005 Access Denied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5912286/gpo-map-drive-policy-failing-to-apply-with-event-i
question_id: 5912286
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
answer_author_roles: ["Independent Advisor"]
---
# GPO map drive policy failing to apply with Event ID 4098 - Error code 0x80070005 Access Denied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5912286/gpo-map-drive-policy-failing-to-apply-with-event-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey sysadmins, I configured a Group Policy Preference to map a network share drive (Z:) for our accounting OU using Item-Level Targeting based on a security group. The policy hits the client machines, but the drive doesn't map. Event Viewer logs throw Event ID 4098 with error code 0x80070005 Access Denied. Users can manually navigate to the UNC path fine. What am I missing in the GPO context?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-05*

Hi David,

That access denied error happens because the drive map preference is running under the computer’s SYSTEM account instead of the user’s. In the preference item, open the Common tab and check “Run in logged-on user’s security context.” Make sure the GPO is linked to the OU with the user accounts, not just the computers, and that the Item-Level Targeting is scoped to the right security group. Once it runs in the user context, the mapping will succeed since users already have permissions to the UNC path.

Let me know if you need further clarification.

Harry.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-06-05*

The behavior matches a known limitation: certain Group Policy Preference items, including Scheduled Tasks and WMI/ILT-based items, do not run in the logged-on user’s security context even when configured that way, and instead run in the system context. When the preference (or its WMI/Item-Level Targeting) evaluates in the system context, access checks against user-scoped resources or permissions can fail with 0x80070005 (Access is denied), resulting in Event ID 4098 and the drive not being mapped.

In this scenario:

-  The GPP Drive Map is configured with Item-Level Targeting based on a security group.

-  The preference processing and/or its WMI/ILT evaluation runs in the system context.

-  The system context does not have the same group membership or access as the user, so the targeting or the drive mapping fails with Access Denied, even though the user can manually access the UNC path.

To resolve within the documented behavior:

-  Avoid relying on user-specific context for this GPP item when it is evaluated in the system context.

-  Adjust the targeting or security so that the system context does not encounter Access Denied (for example, by ensuring the required access is granted where the GPP item is evaluated), or redesign the mapping so it does not depend on conditions that only succeed in the user context.

-  Use Group Policy logging/tracing for the relevant Client Side Extension (CSE) to confirm that the failure is due to the system-context evaluation and 0x80070005, similar to the documented Scheduled Tasks GPP behavior.

References:

-  User GPP Scheduled Task item fails to apply and logs event ID: 4098 with 0x80070005 Access is denied

-  Scenario guide: GPO to map a network drive doesn't apply as expected

-  After you apply a WMI filter, the GPO does not take effect on a client computer that is running Windows 7 or Windows Server 2008 R2
