---
title: "Problem in Domain Controller sync and transfer role"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1192361/problem-in-domain-controller-sync-and-transfer-rol
question_id: 1192361
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Problem in Domain Controller sync and transfer role

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1192361/problem-in-domain-controller-sync-and-transfer-rol (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, our environment has a DC and OS version is 2008R2, I created a new VM server and promote to DC, but this is very weird that both seem cannot connect, when one PC join the domain, only old DC (2008r2) can find its computer object, also, I tried to update the DNS record in new DC, the old DC doesn't sync anything, vice versa, but 5 roles PDC,RID and others are in new DC, how can I transfer the roles to old DC? Or any other alternative way to fix the problem? Here is the current Role state in old DC (2008R2)

And in new DC, the same name and shown cannot transfer

Running the "netdom query fsmo" in CMD and shows the result

Please give me any ideas... many thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-23*

Hello

Thank you for your question and reaching out. I can understand you are  having query\issues related  to DC sync and transfer.

It looks there is issues with AD replication health due to AD configuration are not synced.

-  At the command prompt, type the following commands, and then press ENTER

dcdiag /v /c /d /e /s: > c:\dcdiag.txt

repadmin /replsum

dcdiag /test:dns /s: /dnsbasic

repadmin /syncall /aped

-  Please verify DNS settings and its ip preferred DNS ip should be pointed to one of your working DC.

-   Disable any Antivirus program or Windows firewall you may have for temporary purpose.

-  Verify date and time should be correct and synced.

-  Run Active Directory Replication Status tool  to check overall health of AD Replication : from https://www.microsoft.com/en-us/download/details.aspx?id=30005

Reference :

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/troubleshoot/troubleshooting-active-directory-replication-problems

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/common-active-directory-replication-errors

--If the reply is helpful, please Upvote and Accept as answer--
