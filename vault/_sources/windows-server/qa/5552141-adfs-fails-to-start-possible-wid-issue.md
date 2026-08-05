---
title: "ADFS fails to start. Possible WID issue."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5552141/adfs-fails-to-start-possible-wid-issue
question_id: 5552141
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-performance-app-tech-compatibility"]
answer_author_roles: ["Independent Advisor"]
---
# ADFS fails to start. Possible WID issue.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5552141/adfs-fails-to-start-possible-wid-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

ADFS fails to start after reboots occasionally. I have found an issue in the WID logs here: 

Failed to verify Authenticode signature on DLL 'C:\Windows\WID\Binn\DBVerify\adfsconfigDbVerify.dll'.

The Service Broker endpoint is in disabled or stopped state.

The Database Mirroring endpoint is in disabled or stopped state.

Error: 3605, Severity: 16, State: 1.

Schema verification failed for database 'AdfsConfiguration'.

We have SentinelOne installed. We've removed Defender. We've set ADFS to a delayed start. 

ADFS is also dependent on WID. 

SentinelOne support asked that we get with MS to see if we could enable debug logging for ADFS/WID. We haven't been able to get this information from MS.

Has anyone else ran into this? Does anyone have a fix?

Thank you!

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-09-11*

Dear Cameron Gregory,

The error referencing the Authenticode signature on `adfsconfigDbVerify.dll` and the disabled Service Broker and Database Mirroring endpoints suggests a possible integrity or trust issue with the Windows Internal Database (WID) components. This may be further complicated by third-party security software such as SentinelOne, which can interfere with DLL validation or service startup timing.

Setting ADFS to delayed start is a good step, but we recommend also verifying that the WID service is fully initialized before ADFS attempts to load. You may consider implementing a startup dependency script or using Task Scheduler to delay ADFS further. Additionally, enabling debug logging for ADFS and WID can provide deeper insight—this can be configured via PowerShell using `Set-AdfsProperties` and by modifying SQL Server trace flags for WID.

Warm regards,

Domic Vo
