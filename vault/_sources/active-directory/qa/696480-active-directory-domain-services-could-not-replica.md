---
title: "Active Directory Domain Services could not replicate the directory partition CN=Configuration,DC=xxxx,DC=LOCAL from the remote Active Directory Domain Controller xxx.xxxx.LOCAL.    \"Replication access was denied.\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/696480/active-directory-domain-services-could-not-replica
question_id: 696480
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory Domain Services could not replicate the directory partition CN=Configuration,DC=xxxx,DC=LOCAL from the remote Active Directory Domain Controller xxx.xxxx.LOCAL.    "Replication access was denied."

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/696480/active-directory-domain-services-could-not-replica (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I face an issue while promoting new Domain Controller (Additional Domain Controller); this domain controller must be the 7th DC in the forset/domain, the promotion is failed each time with the Following error:  

 The operation failed because:    

Active Directory Domain Services could not replicate the directory partition CN=Configuration,DC=xxxx,DC=LOCAL from the remote Active Directory Domain Controller xxx.xxxx.LOCAL.    

"Replication access was denied."  

The user account I used for promotion is member of: Enterprise Admins, Schema Admins, Domain Admins, Administrators, also I set it in Domain Controllers Group, with full controll/permission on Configuration Partition (Adsi Edit)  

I am able to promote Read Only Domain Controller (RODC) but the issue appreaes only during promoting new Writable DC, which lead to failed promotion process.  

appreciate Any help.

## Answer (community) — Q&A User

*upvotes: 4 · updated: 2022-01-17*

Thankfully I am able to solve this issue, it was due to Deny permission on “Replicating Directory Changes All” role for Administrators group on configuration partition at “ADSIEdit”, when I changed it to allow the issue resolved successfully.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-15*

You can work through this one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/replication-error-8453    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-15*

Hello,  

Have you run repadmin to verify that bi-directional replication is healthy on all other DC's?  

Check that DNS role is installed and it may help to make sure server is a domain member   

Miguel Fra  

https://www.falconitservices.com
