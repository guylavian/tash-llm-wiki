---
title: "SCCM, failed to get the software upates package with the specific ID"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1008406/sccm-failed-to-get-the-software-upates-package-wit
question_id: 1008406
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-updates"]
---
# SCCM, failed to get the software upates package with the specific ID

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1008406/sccm-failed-to-get-the-software-upates-package-wit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

I have problem with my ADR it's error as attached picture.    

Anyone have any ideas?    

Thanks in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-19*

Hi @Keaphearun SOEUNG  ,

Thanks for your reply.

Please create a new deployment package. For example:  

-  Create a new folder.  

2) Create a new deployment package.  

3) After that the deployment package will be applied

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-16*

Hi @Keaphearun SOEUNG  ,

Failed to get the software updates package with ID “HQ100025”

1, Please help check the deployment package, does it exist? For example:

1) Check the deployment packages which is used in the rule.  

Path: Software Library>Automatic Deployment Rules> Right-click the rule>Properties> Deployment Packages  

2) Check the deployment packages and package source.  

Path: Software Library>Deployment Packages>Right-click the Package>Properties>General  

3) Make sure the deployment package exists.  

2, If the deployment package exists, please try to create a new deployment package.
