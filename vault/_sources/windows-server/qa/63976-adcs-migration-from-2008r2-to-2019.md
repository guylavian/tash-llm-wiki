---
title: "ADCS Migration from 2008R2 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/63976/adcs-migration-from-2008r2-to-2019
question_id: 63976
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# ADCS Migration from 2008R2 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/63976/adcs-migration-from-2008r2-to-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi experts,  

I would like to ask the following on the topic migrating ADCS from 2008R2 to 2019. I have run couple of articles like the one as below:-  

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-migrating-the-active-directory-certificate-service/ba-p/697674  

Let me briefly explain on the current structure in the environment of ours  

-  1 Root CA which is not joined domain - Windows 2008R2  

-  4 Issuing suboordinate CA - Windows 2008R2  

The final result of the ADCS structure will be as below:-  

-  Root CA and the issuing subordinate CA will be migrated to Windows 2019  

-  Since they are many clients are relying to the certificates which was rolled out. Are we able to migrate all the servers from Windows 2008 R2 to Windows 2019 without the need to reissue the cert to the clients? As there are tons of web apps and services which are relying on the certificates.  

I would like to have this deployment in order so that there will not issues of certificate where the chains will be broken. The objectives are as below:-  

-  CA name will be the same  

-  IP address of the CA server will be different  

-  Hostname of the CA server will be different.   

I was advised to perform the root CA migration first then followed by the 4 suboordinate issuing CA. Is that a good idea?  

Another question is since the root CA server name and the IP address will be different, how are we going to tell the issuing CA that the root CA server name and IP address is being changed? Also when we migrate the  subordinate issuing CA, how are we going to tell the other suboordinate CA and root CA that this issuing CA server name and ip address is being changed. What are the configuration that is to take place  

Thank you  

Peter

## Answers

_No answers on this thread._
