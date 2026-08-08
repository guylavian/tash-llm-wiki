---
title: "Adfs Upgrade - FBL raise giving ADFS config Database  Error Invalid colum name 'rowguid'"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/756872/adfs-upgrade-fbl-raise-giving-adfs-config-database
question_id: 756872
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Adfs Upgrade - FBL raise giving ADFS config Database  Error Invalid colum name 'rowguid'

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/756872/adfs-upgrade-fbl-raise-giving-adfs-config-database (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I am on the process of Upgrading our ADFS farm from 2012R2 to 2019 and using a SQL cluster for our database. While running the command $Credentials = Get-Credential    

Invoke-AdfsFarmBehaviorLevelRaise -Credential $Credentials i am getting the below error     

Invoke-AdfsFarmBehaviorLevelRaise : Database upgrade could not be performed on localhost. Error: An error occurred    

during an attempt to connect to the AD FS configuration database. Error: Invalid column name 'rowguid'.

## Answers

_No answers on this thread._
