---
title: "Exporting Sent and received count for exchange online users through powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2123744/exporting-sent-and-received-count-for-exchange-onl
question_id: 2123744
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exporting Sent and received count for exchange online users through powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2123744/exporting-sent-and-received-count-for-exchange-onl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

is it possible to generate a report from Office 365 using PowerShell that details the total number of emails sent and received by each user over the past 30 days, specifically for users with a license containing "faculty"

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-11-27*

There's a built-in report for that: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/email-activity-ww?view=o365-worldwide

You can simply use the Export functionality in the portal, then filter the report in Excel. Or you can get the report data via PowerShell and the `Get-MgReportEmailActivityUserDetail` cmdlet. No server-side filtering is supported, so as with the portal, you will have to apply the filter client-side.
