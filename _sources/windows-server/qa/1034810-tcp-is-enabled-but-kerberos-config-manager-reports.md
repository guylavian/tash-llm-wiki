---
title: "TCP is enabled but Kerberos Config Manager reports it as disabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1034810/tcp-is-enabled-but-kerberos-config-manager-reports
question_id: 1034810
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# TCP is enabled but Kerberos Config Manager reports it as disabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1034810/tcp-is-enabled-but-kerberos-config-manager-reports (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm running SQL Server 2016 and increased network security to refuse NTLM connections throughout the domain. Every time I check the authentication of the SQL database it reports as NTLM. I initially had an issue with the SPN but was able to resolve that. I ran Kerberos Configuration Manager and it reports that TCP must be enabled. When I review SQL Configuration Manager TCP is enabled will all ports set to 1433. I confirmed firewall is off on the SQL box. Is there another setting I'm missing? Everything I read about the error from Kerberos Config Manager just tells me to enable TCP but it already is.

## Answers

_No answers on this thread._
