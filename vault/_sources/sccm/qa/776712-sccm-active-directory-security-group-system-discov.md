---
title: "SCCM - ACTIVE DIRECTORY (SECURITY GROUP/SYSTEM) DISCOVERY AGENT FAILED TO BIND TO CONTAINER"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/776712/sccm-active-directory-security-group-system-discov
question_id: 776712
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
---
# SCCM - ACTIVE DIRECTORY (SECURITY GROUP/SYSTEM) DISCOVERY AGENT FAILED TO BIND TO CONTAINER

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/776712/sccm-active-directory-security-group-system-discov (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Guys  

We have an untrusted domain, where the System and Group discovery worked very well untill the 01-2022 CU patch got installed on the SCCM Site server (Server 2016).  

The log is giving me the following error:  

Active Directory Security Group Discovery Agent failed to bind to container LDAP://domain.com/OU=ou,OU=ou2,DC=domain,dc=com  

Error: The user name or password is incorrect.  

Possible cause: The AD container specified earlier might be invalid now. The Domain Controller is inaccessible.  

Solution: Please verify that the AD container paths specified are valid. Confirm accessibility of the site server to the Domain Controller to be que**ried.  

We use a Service account from the DMZ domain to do the discovery: (dmz\service-account).  

If I remove the CU from the Site Server, the discovery works well again.  

I hope someone can point me in the right direction with this problem.  

/Andy

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-21*

Haven't heard from you for some time, is Jason's answer helpful to you? If it is helpful, please accept answer. It will make someone who has the similar issue easily find the answer.    

If you have any other issues, please don't hesitate to let us know.    

Thanks and have a nice day.    

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
