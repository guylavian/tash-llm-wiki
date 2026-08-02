---
title: "Windows 11 DCDIAG"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1221083/windows-11-dcdiag
question_id: 1221083
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Windows 11 DCDIAG

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1221083/windows-11-dcdiag (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I just installed Windows 11 and i am getting an error message with DCDiag on my Windows 11 box, this error message does not appear on my Windows 10 box.   Is DCDiag not supported on Windows 11?
Again...this error message only appears on my Windows 11 box
Invalid service type: DNSCACHE on DC02, current value WIN32_SHARE_PROCESS, expected value WIN32_OWN_PROCESS

```
Cdcdiag /test:dns /dnsbasic /s:dc02

Directory Server Diagnosis

Performing initial setup:
   * Identified AD Forest.
   Done gathering initial info.

Doing initial required tests

   Testing server: Site\DC02
      Starting test: Connectivity
         ......................... DC02 passed test Connectivity

Doing primary tests

   Testing server: Site\DC02

      Starting test: DNS

         DNS Tests are running and not hung. Please wait a few minutes...
         Invalid service type: DNSCACHE on DC02, current value WIN32_SHARE_PROCESS, expected value
         WIN32_OWN_PROCESS
         ......................... DC02 passed test DNS

   Running partition tests on : ForestDnsZones

   Running partition tests on : DomainDnsZones

   Running partition tests on : Schema

   Running partition tests on : Configuration

   Running partition tests on : domain

   Running enterprise tests on : domain.com
      Starting test: DNS
         Test results for domain controllers:

            DC: DC02.domain.com
            Domain: domain.com

               TEST: Basic (Basc)
                  Error: DNSCACHE service is not running

         Summary of DNS test results:

                                            Auth Basc Forw Del  Dyn  RReg Ext
            _________________________________________________________________
            Domain: domain.com
               DC02                    PASS FAIL n/a  n/a  n/a  n/a  n/a

         ......................... domain.com failed test DNS
```

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-04-11*

dcdiag is available if you have the Active Directory Domain Services (AD DS) or Active Directory Lightweight Directory Services (AD LDS) server role installed which wouldn't be the case on a desktop operating system.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
