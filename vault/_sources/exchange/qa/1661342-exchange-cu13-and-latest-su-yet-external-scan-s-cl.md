---
title: "Exchange CU13 and latest SU, yet external scan(s) claim CVE-2022-41040 CVE-2022-41082 vulnerability."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1661342/exchange-cu13-and-latest-su-yet-external-scan-s-cl
question_id: 1661342
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange CU13 and latest SU, yet external scan(s) claim CVE-2022-41040 CVE-2022-41082 vulnerability.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1661342/exchange-cu13-and-latest-su-yet-external-scan-s-cl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Per Exchange Health Checker version 24.03.12.1700 this is my Exchange version.

Build Number: 15.02.1258.032

Exchange IU or Security Hotfix Detected: Security Update for Exchange Server 2019 Cumulative Update 13 (KB5036402)

We always run one CU behind the latest, and we pay for external vulnerability scans. So when CU12 went end of life we upgraded to CU13, and then our SOC began telling us that our Microsoft Exchange Server OWA has (KB5019758, ProxyNotShell) CVE-2022-41040: Server-Side Request Forgery (SSRF) and CVE-2022-41082: Remote code execution (RCE) vulnerabilities.

So I do my own external vulnerability scan using NMAP and the following scripts, which too claim the server is vulnerable.

https://github.com/Diverto/nse-exchange CVE-2022-1040_checker

https://github.com/Diverto/nse-exchange http-vuln-cve2022-41082.nse

Yet, we were, and are, patched to the point that these vulnerabilities should not exist. Also the Exchange Heath Checker Script should tell me if we're vulnerable, yet it does not. Even the EOMTv2.ps1 script used to make URL rewrite rules to mitigate this attack in the first place now says: VERBOSE: Checking if EOMTv2 is up to date with https://aka.ms/EOMTv2-VersionsUri VERBOSE: Starting EOMTv2.ps1 version 23.11.21.1852 on MAIL VERBOSE: EOMTv2 preCheck complete on MAIL NOTICE: CVE-2022-41040 vulnerability has been fixed for the Exchange build running on this computer - mitigation will not be applied.

So here's the question(s)/assumption; When Microsoft released CU13 and the SU's to fix those CVE's, and we went from CU12 to CU13, wiping away those URL rewrite kludges, was my SOC, and those NMAP scripts, now supposed to be fooled into thinking the Exchange server has this vulnerability?

Is there an external vulnerability scan I can try, other than what I already have, that I can be sure is telling me the truth?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-04-29*

I always go by what the Exchange Health Checker says. Not sure what that external scanning is going by honestly. 
BTW, if you are on CU13, you are really two builds behind. Hopefully you have Extended Protection Enabled! 

https://learn.microsoft.com/en-us/exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019
