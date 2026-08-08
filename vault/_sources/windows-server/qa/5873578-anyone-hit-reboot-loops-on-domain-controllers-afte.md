---
title: "Anyone hit reboot loops on domain controllers after recent patches?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5873578/anyone-hit-reboot-loops-on-domain-controllers-afte
question_id: 5873578
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-install-windows-updates-features-roles"]
answer_author_roles: ["Independent Advisor"]
---
# Anyone hit reboot loops on domain controllers after recent patches?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5873578/anyone-hit-reboot-loops-on-domain-controllers-afte (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I’ve been seeing reports about domain controllers getting stuck in reboot loops after recent updates, which is honestly pretty concerning. Has anyone experienced this in production? What’s your process for validating updates on critical servers before rollout?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-04-28*

Hi Yuso Faisyahhhhh,

If you are hit by this, Microsoft has released Out-Of-Band (OOB) emergency fixes. You need to manually grab them from the Microsoft Update Catalog:

For Windows Server 2025: Install KB5091157

For Windows Server 2022: Install KB5091575

Regarding your question about validating updates on critical servers, don't overcomplicate it. Here is the standard IT survival guide for patching DCs:

The N-14 Rule: Never auto-patch DCs on Patch Tuesday. Delay your DC patching schedule by at least 7 to 14 days so the community can find the landmines for you.

Ring Deployment: Always patch a secondary, non-FSMO role DC first. Let it bake for 48 hours.

Targeted Log Checking: After the test DC reboots, don't just look for "Online" status. Explicitly filter your Event Viewer for LSASS, Kerberos, and Netlogon errors. If those are clean, then you roll out to the rest.

I hope this helps you dodge the reboot loop! If this answers your question, please click "Accept Answer".

Tracy.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-04-28*

Yes, there is a documented issue where domain controllers can enter repeated reboot loops after specific recent security updates, and it has been seen in production.

From the context:

-  After installing the April 2026 security updates on Windows Server domain controllers in multi-domain forests using Privileged Access Management (PAM), LSASS can crash during startup, causing DCs to restart repeatedly and making the domain unavailable.

-  Windows Server 2025: issue introduced by KB5082063 and resolved by out-of-band (OOB) updates KB5091157 (standard) or KB5091470 (hotpatch for enrolled servers).

-  Windows Server 2022: issue introduced by KB5082142 and resolved by OOB updates KB5091575 (standard) or KB5091576 (hotpatch).

-  A similar LSASS-related DC reboot issue was previously seen with KB5009543 and resolved by OOB update KB5010793.

For environments already affected:

-  Identify affected DC OS versions and originating KBs (for example, KB5082063 on Server 2025, KB5082142 on Server 2022).

-  Apply the corresponding OOB fix on DCs:

-  Server 2025: install KB5091157 from the Microsoft Update Catalog, or KB5091470 if using hotpatching.

-  Server 2022: install KB5091575 from the Microsoft Update Catalog, or KB5091576 if using hotpatching.

-  Reboot DCs as required (standard OOB) and verify LSASS stability and normal authentication/replication.

A practical validation process for critical servers (such as DCs) based on these incidents:

-  Staging and ring-based rollout

-  Maintain a non-production environment (or at least a subset of DCs) that mirrors production roles and PAM/ESAE/PIM configurations.

-  Apply Patch Tuesday updates first to lab or secondary DCs, monitor for at least several days before touching core DCs.

-  Targeted scenario testing before broad rollout

-  Explicitly test:

-  DC reboots and LSASS stability after updates.

-  Authentication (user logons, Kerberos tickets, smart card if used).

-  AD replication health.

-  For environments using PAM/ESAE/PIM or shadow principals, treat any LSASS-related changes as high risk and extend validation time.

-  Health and rollback readiness

-  Ensure multiple healthy DCs per domain and sites so that if one DC fails after patching, others can still service authentication.

-  Take recent system state backups of DCs before patching.

-  Patch DCs in small batches, never all at once.

-  Monitor known issues and OOB releases

-  Review Windows Server release health pages for the specific OS version before and after each Patch Tuesday to catch:

-  Known issues affecting DCs (LSASS crashes, memory leaks, Kerberos changes, etc.).

-  Availability of OOB fixes like KB5091157, KB5091575, or earlier KB5010793.

-  Delay rollout of problematic updates on core DCs until a documented resolution or OOB fix is available.

-  Post-update verification

-  After installing updates on DCs, immediately:

-  Reboot and confirm they remain stable (no repeated LSASS crashes or unexpected restarts).

-  Check Event Viewer for LSASS, Kerberos, and AD DS errors.

-  Validate logons and key application authentication paths.

This combination of staged deployment, explicit DC-focused testing, and monitoring of release health/OOB updates helps avoid production reboot loops on domain controllers.

References:

-  Windows Server 2025 known issues and notifications

-  Windows Server 2022

-  Windows 10, version 1607 and Windows Server 2016 known issues and notifications

-  Resolved issues in Windows Server 2025

-  Resolved issues in Windows Server 2022

-  January 11, 2022—KB5009543 (OS Builds 19042.1466, 19043.1466, and 19044.1466)

-  November 8, 2022—KB5020019 (Monthly Rollup)
