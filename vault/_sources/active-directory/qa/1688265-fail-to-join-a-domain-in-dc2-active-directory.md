---
title: "Fail to join a domain in DC2 Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1688265/fail-to-join-a-domain-in-dc2-active-directory
question_id: 1688265
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Fail to join a domain in DC2 Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1688265/fail-to-join-a-domain-in-dc2-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I've completed 1st DC1 active directory setup as follow

When I try to jon a domain in DC2 [20.136.20.252], it prompt this  

[An error occurred when DNS was queried for the service location (SRV) resource record used to locate an Active Directory Domain Controller (AD DC) for domain "ad.5gcjumphostkpg.com".

The error was: "No records found for given DNS query."

(error code 0x0000251D DNS_INFO_NO_RECORDS)

The query was for the SRV record for _ldap._tcp.dc._msdcs.ad.5gcjumphostkpg.com]

However Im able to ping and lookup DC1 server [20.136.20.250]

Skipping Joining domain in DC2,  When try to promote this DC, entered the domain with correct credential, it prompt this error

## Answers

_No answers on this thread._
