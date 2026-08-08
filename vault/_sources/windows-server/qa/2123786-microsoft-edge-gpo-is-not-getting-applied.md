---
title: "Microsoft Edge GPO is not getting applied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2123786/microsoft-edge-gpo-is-not-getting-applied
question_id: 2123786
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-licensing-and-activation-itpro-server", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Microsoft Edge GPO is not getting applied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2123786/microsoft-edge-gpo-is-not-getting-applied (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a GPO that enables the browser to allow 11 extensions, which are already configured in the policy.

Please note that the same GPO works perfectly with other browsers, like Chrome.

However, after testing in edge://policy, the IDs do not appear as expected.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-11-27*

1-Ensure Microsoft Edge GPOs are Available

Download the templates from https://www.microsoft.com/edge/business/download

2-Verify GPO Configuration

Computer Configuration > Policies > Administrative Templates > Microsoft Edge

User Configuration > Policies > Administrative Templates > Microsoft Edge

3-Check GPO Link and Scope

4-Force Group Policy Update

CMD> gpupdate /force

5-Check Group Policy Results

CMD> gpresult /r

6-Verify Permissions

7-Check Edge Version Compatibility

8-Review Event Logs

Application and Service Logs > Microsoft > EdgeUpdate for Edge-specific logs.

Windows Logs > System for GPO-related logs.

9-Network Connectivity and DNS

10-Check for Local Policies Overriding GPOs

gpedit.msc

11-Clear the Group Policy Cache

C:\Windows\System32\GroupPolicy\

CMD> gpupdate /force

12-Ensure Edge Policies are Supported on the OS Version

By using these step-by-step, you should be able to identify the root cause of why your Microsoft Edge GPO is not being applied. If none of these steps work, you might want to test applying a simple GPO to ensure that GPO application itself works on the machine.
