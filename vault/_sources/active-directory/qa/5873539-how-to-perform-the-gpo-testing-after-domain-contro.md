---
title: "How to perform the GPO testing after domain controller migration from win2012 R2 to 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5873539/how-to-perform-the-gpo-testing-after-domain-contro
question_id: 5873539
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# How to perform the GPO testing after domain controller migration from win2012 R2 to 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5873539/how-to-perform-the-gpo-testing-after-domain-contro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How to perform the GPO testing after domain controller migration from win2012 R2 to 2022. Please advise the steps need to perform GPO health status and working fine after dc migration . Thanks.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-04-28*

Dear Aung Nyi Nyi Win,

After migrating domain controllers from 2012 R2 to 2022, the most reliable way to validate Group Policy health is to run `dcdiag /test:Advertising` and `dcdiag /test:DNS` on the new DCs, then confirm replication with `repadmin /replsummary`. Once replication is clean, use `gpresult /h report.html` on a test client joined to the domain to verify that policies are being applied as expected. You should also run `gpotool.exe` or `Get-GPOReport -All -ReportType HTML` from PowerShell to confirm consistency of GPOs across all DCs. Pay close attention to SYSVOL replication status by checking `\\<DCName>\SYSVOL` and ensuring DFSR is healthy, since mismatched SYSVOL contents are a common cause of GPO failures after migration. Finally, validate event logs under `Applications and Services Logs\Microsoft\Windows\GroupPolicy\Operational` on clients for any 1058 or 1030 errors. If all these checks pass without errors, you can be confident that GPOs are functioning correctly in the new 2022 domain controller environment.

If the above response helps answer your question, please hit "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

Domic V.
