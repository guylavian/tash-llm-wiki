---
title: "Upgrade to ADFS 2019 from 2012R2 with SQL dB"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/608325/upgrade-to-adfs-2019-from-2012r2-with-sql-db
question_id: 608325
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Upgrade to ADFS 2019 from 2012R2 with SQL dB

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/608325/upgrade-to-adfs-2019-from-2012r2-with-sql-db (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I was able to join new 2019 ADFS and web proxy and remove old 2012r2 server successfully. Although with   

PS C:\Windows\system32> Invoke-AdfsFarmBehaviorLevelRaise -Credential $Cred  

I get the following error: An AD FS configuration database with the same name already exists; specify that  

the existing database is to be overwritten.  

I am using an account that is admin rights on all ADFS and Web proxy servers and has 'sa' rights to the SQL server where dB is located. Any suggestions? Not sure how to overwrite the dB

## Answers

_No answers on this thread._
