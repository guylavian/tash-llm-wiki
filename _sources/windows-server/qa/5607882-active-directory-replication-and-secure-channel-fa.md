---
title: "Active Directory replication and secure channel failure – suspected link to recent KB updates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5607882/active-directory-replication-and-secure-channel-fa
question_id: 5607882
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
answer_author_roles: ["Independent Advisor", "Q&A User"]
---
# Active Directory replication and secure channel failure – suspected link to recent KB updates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5607882/active-directory-replication-and-secure-channel-fa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Subject: Active Directory replication and secure channel failure – suspected link to recent KB updates

Hello,

I’m reporting a critical issue affecting our Active Directory infrastructure, which has occurred multiple times following cumulative updates on our two Windows Server 2025 Datacenter domain controllers (version 24H2): SERDC and SERDC2.

🔹 Environment:

-  Simple setup: AD + DNS + DHCP + GPO

-  No Exchange or additional services

-  Fewer than 300 users

🔹 Symptoms:

-  AD replication failure (repadmin /replsummary: 5/5 errors)

-  Secure channel broken (Test-ComputerSecureChannel fails)

-  Netlogon 5719, RPC error 1727

-  GPOs not applied, login failures

-  DFS-R frozen, SYSVOL not replicating

🔹 Timeline:

-  The issue first appeared after Windows Server updates in October 2025.

-  We noticed KB5067360 and KB5070881 were installed, but we cannot confirm with certainty that these KBs are the direct cause.

-  KB5067360 is non-removable (message: “This update is required by your computer”).

-  KB5070881 was manually uninstalled, which temporarily resolved the issue.

-  We restored a post-rejoin snapshot to return to a healthy state.

-  Despite disabling updates, they were automatically re-enabled, and the issue reappeared on November 3rd.

🔹 Actions taken:

-  Clean rejoin of SERDC2

-  Snapshot restoration

-  Update blocking via GPO and disabling wuauserv

-  Temporary shutdown of SERDC2 to stabilize the domain

🔹 Request:

We would like to know if this behavior is known, if a fix or official workaround exists, and whether the mentioned KBs could be involved.

We’ve included technical logs in the ZIP:

-  repadmin /replsummary, showrepl, syncall

-  netlogon.log

-  AD and system event logs

-  Installed KB list

Thank you in advance for your assistance.

Best regards, Jean-Sébastien

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-11-20*

Hello, we are experiencing the exact same problem: after installing the October 2025 security updates, one of our Active Directory servers crashed. The server was completely reinstalled, and the other was not updated. Then we installed the November 2025 security updates, and the same problem occurred. We have three domain controllers: two running Windows Server 2022 and one running Windows Server 2025. Have you found a solution?

Thank you very much.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-11-03*

Hi Jean Sébastien, 

Based on your description, the replication failures, secure channel errors, and SYSVOL/DFS-R issues are consistent with some known cases following certain cumulative updates on Windows Server 2025 (24H2). However, the exact root cause is often environment- or configuration-specific.

Specifically:

-  KB5067360 is a mandatory servicing stack update and generally does not directly cause AD replication failures.

-  KB5070881 has been reported in some cases to impact Netlogon and secure channel stability, particularly in smaller AD environments. Your observation that uninstalling KB5070881 temporarily resolved the issue aligns with these reports.

From the logs you provided, the replication errors are consistent with secure channel and RPC connectivity issues between the DCs. A few recommended steps:

-  Verify that the computer account passwords for both DCs are synchronized. Running Test-ComputerSecureChannel -Repair -Credential (Get-Credential) on both DCs can help reestablish trust.

-  Ensure DFS-R and SYSVOL permissions are correct; restoring snapshots can sometimes introduce inconsistencies.

-  Temporarily disable KB5070881 while monitoring replication stability. You’ve observed that this helps, which is consistent with known behavior.

-  Microsoft has documented some registry/workaround options for KB5070881 in combination with certain AD topologies; I can provide detailed guidance if needed.

At this stage, this behavior is known but not widespread. Careful update management is key to preventing recurrence. I recommend testing these repair steps in a lab environment before deploying in production.

I hope this information is useful.. If it is, don't forget to "Accept the answer" so that others could benefit too. Thank you :)
