---
title: "Exchange 2019 - Unable to add DAG member"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/353861/exchange-2019-unable-to-add-dag-member
question_id: 353861
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 - Unable to add DAG member

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/353861/exchange-2019-unable-to-add-dag-member (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

I have an Exchange 2019 environment. I'm trying to add second node to the DAG but getting the below error. Exchange 2019 CU7 both servers. IP less DAG.  

A server-side database availability group administrative operation failed. Error The operation failed. CreateCluster errors may result from incorrectly configured static addresses. Error: An error occurred while attempting a cluster operation. Error: Cluster API failed: "CreateCluster() failed with 0x42a. Error: The service has returned a service-specific error code". [Server:]

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-04-13*

Hi @Bargavi Nagarajan  ,    

To add to what AshokM mentioned, it's also suggested to have a check at the Group Policy settings for any deny policy on the local logins,      

Computer Configuration/ windows settings / Local Policies / User Rigths Assignment / Deny Log on Locally    

Here's a similar thread which was finally found out to be related to the GPOs:    

Can't add Exchange Server 2019 server to a DAG Error:CreateCluster() failed with 0x42a    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-13*

Thank you all for your suggestions. Issue has been resolved after uninstalling & re-installing the FailoverClustering role.
