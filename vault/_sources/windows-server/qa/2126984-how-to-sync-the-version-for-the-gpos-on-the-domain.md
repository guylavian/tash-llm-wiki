---
title: "How to sync the version for the GPOs on the Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2126984/how-to-sync-the-version-for-the-gpos-on-the-domain
question_id: 2126984
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# How to sync the version for the GPOs on the Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2126984/how-to-sync-the-version-for-the-gpos-on-the-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am experiencing an issue where the Group Policy Objects (GPOs) are not synchronizing with the domain controller. "The version number for one or more GPOs on this domain controller are not in sync with the versions for the GPOs on the Baseline domain controller"

This is message from de SysVol GPO Version

What can I do to resolve this?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-06*

Hello,

Here are some steps you can take to resolve this:

Check Replication Status:

Use the repadmin /showrepl command to check the replication status between your domain controllers. This will help identify any replication issues.

Force Replication:

You can force replication using the repadmin /syncall command. This ensures that all domain controllers are synchronized.

Verify SYSVOL and Netlogon Shares:

Ensure that the SYSVOL and Netlogon shares are available and properly replicated. You can use the dfsrdiag command to check the status of DFS Replication.

Check GPO Version Numbers:

Open the Group Policy Management Console (GPMC) and check the version numbers of the GPOs. If there is a mismatch, you may need to manually update the GPOs.

Use ADSI Edit:

If the issue persists, you can use ADSI Edit to manually update the msDFSR-Enabled and msDFSR-Options attributes. This involves stopping the DFSR service, making the necessary changes, and then restarting the service.

Run GPUpdate:

On the affected machines, run gpupdate /force to force a Group Policy update.

Check Event Logs:

Look at the Event Viewer logs on your domain controllers for any errors related to Group Policy or DFS Replication. This can provide more insight into what might be causing the issue.
