---
title: "Exchange 2019 windows server core patch install confirmation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297128/exchange-2019-windows-server-core-patch-install-co
question_id: 297128
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 windows server core patch install confirmation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297128/exchange-2019-windows-server-core-patch-install-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Friends, Is anyone running Exchange 2019, CU 8 on Windows server Core 2019? If so, have you attempted to apply KB5000871 (zero-day patch) to your servers? How were you able to confirm the patch was installed successfully? I've attempted to verify using systeminfo, get-hotfix -id KB5000871, Dism.exe /Online /get-packages | findstr KB5000871 and Dism.exe /Online /get-packages and wmic qfe list. So far, I have not been able to confirm the KB was installed but received no error nor was I prompted to reboot. Has anyone else been able to confirm successful installation of this KB? Thanks Phillip

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-04*

I have the same question. For now I use the HealthChecker.ps1 script   

From MS mail:  

Q: Is there a method I can use to determine which of my Exchange servers can install the security updates directly, and which will need to have a supported Update Rollup (UR) or Cumulative Update (CU) installed first?    

A: Yes. You can use the Exchange Server Health Checker script, which can be downloaded from GitHub (use the latest release). Running this script will tell you if you are behind on your on-premises Exchange Server updates.    

https://github.com/dpaulson45/HealthChecker#download  

It also shows if patch is installed in the txt file under Exchange Information
