---
title: "AD CS update to support sha256 KSP but my AD is not updating"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/542822/ad-cs-update-to-support-sha256-ksp-but-my-ad-is-no
question_id: 542822
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# AD CS update to support sha256 KSP but my AD is not updating

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/542822/ad-cs-update-to-support-sha256-ksp-but-my-ad-is-no (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

our AD CS are 2012 r2   

we recently updated to sha2 and the correct info is displayed when running   

certutil -getreg ca\csp\Provider shows KSP  

certutil -getreg ca\csp\cnghashAlgorithm shows 256  

we have an application requesting a cert from our Domain controller for auth and it returns a sha1 certificate and it provides the thumbprint value  

we can find that certificate on the DC and it is A sha1  do I just back up that cert on the DC then delete it and restart the server and hope it all works?  

will my end users get bumped   

we are a hospital so I would like to be 100% sure as we aren't as knowledgeable as we should be with certificates  

thanx in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-10*

well we backed up the cert and rebooted the domain controller and it pulled in a cert how do I verify that is the cert being used by AD

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-08*

the CA is correct  

the domain controller is still using the old cert   

I believe we have to delete that cert on the DC and restart it to pull the new sha2 cert   

just looking for confirmation if that is the process and what outages my endpoints might experience

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-08*

Hello @MikeO       

I believe you need to renew that certificate and restart CS services.    

Also , please have a look on below Microsoft article which may help you.    

https://social.technet.microsoft.com/wiki/contents/articles/31296.implementing-sha-2-in-active-directory-certificate-services.aspx    

If the reply was helpful, please don’t forget to upvote or accept as answer.
