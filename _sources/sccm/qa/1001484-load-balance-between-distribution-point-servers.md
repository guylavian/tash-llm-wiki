---
title: "Load Balance between Distribution Point Servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1001484/load-balance-between-distribution-point-servers
question_id: 1001484
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Load Balance between Distribution Point Servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1001484/load-balance-between-distribution-point-servers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

Do we have a query/report showing the usage/number of clients for a distribution point?    

Showing all clients using each distribution points?    

Thanks,    

Dom

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-12*

Hi,    

1,The build-in executable named smsdpusage.exe (default location C:\Program Files\Microsoft Configuration Manager\bin\i386\smsdpusage.exe) provides you the information about the usage of your distribution points. This executable starts the distribution point usage process. When this process starts, it evaluates the IIS logs, of the previous day, and generates a report of distribution point usage. That report is sent to the management point for processing into the database. Refer to:    

What is smsdpusage.exe?    

2,Similar thread for your reference:    

Query to find clients connecting to a DP    

SCCM Report - Client count with Boundary and Distribution point    

Thanks for your time.    

Best regards,    

Simon    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.    

email-notifications.html
