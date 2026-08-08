---
title: "Unable to Generate \"Active Directory Diagnostics\" Report in Performance Monitor on Windows Server 2025"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2243281/unable-to-generate-active-directory-diagnostics-re
question_id: 2243281
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-performance-system-performance"]
answer_author_roles: ["Independent Advisor"]
---
# Unable to Generate "Active Directory Diagnostics" Report in Performance Monitor on Windows Server 2025

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2243281/unable-to-generate-active-directory-diagnostics-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On a domain controller running Windows Server 2025, I am unable to generate the system defined Active Directory Diagnostics report in Performance Monitor.

It is defined as normal and I can start collection. It then collects data for 300 seconds, but afterwards it has not generated the report. It can only show a bunch of performance counters.  

In the view menu the Report option is greyed out.

I found this: https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/report-generation-process-stops-responding

Tried to add more memory, but it didn't solve it.

Tried to run tracerpt manually, and got a report created but it did not show information about AD - Searches, LDAP etc.

Shouldn't this work on Windows Server 2025?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-05-11*

Hi, I am Henry and I'd like to help.

It looks like you're encountering an issue where Active Directory Diagnostics in Performance Monitor on Windows Server 2025 is failing to generate a report. Since you've already tried increasing memory and running tracerpt manually, here are some additional troubleshooting steps:

Possible Solutions

1. Check Data Collector Set Configuration

-  Instead of using the built-in System Data Collector Set, try creating a User Defined Data Collector Set:

-  Open Performance Monitor → Data Collector Sets → User Defined.

-  Right-click User Defined → New > Data Collector Set.

-  Select Active Directory Diagnostics as the template.

-  Ensure Enable data management and report generation is checked.

2. Verify Stop Condition Settings

-  The report generation process only triggers when the Data Collector Set stops.

-  Right-click the Data Collector Set → Properties → Stop Condition tab.

-  Ensure Overall Duration is set to a reasonable time (e.g., 5 minutes).

3. Manually Generate the Report

-  If the automatic report generation fails, try running:

`tracerpt C:\PerfLogs\Admin\ActiveDirectory.etl -o C:\PerfLogs\Admin\AD_Report.xml`

-  Open the XML file in Performance Monitor to check for missing AD-related data.

4. Update Windows Server 2025

Ensure your system is fully updated, as patches may resolve Performance Monitor issues.
