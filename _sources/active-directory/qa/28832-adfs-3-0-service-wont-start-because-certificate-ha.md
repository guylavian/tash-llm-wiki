---
title: "ADFS 3.0 Service won't start because certificate has expired"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/28832/adfs-3-0-service-wont-start-because-certificate-ha
question_id: 28832
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS 3.0 Service won't start because certificate has expired

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/28832/adfs-3-0-service-wont-start-because-certificate-ha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have a fairly urgent issue with ADFS service not starting.  

The infrastructure is all Server 2019 and the service account password had expired so the ADFS could not auto renew the token signing and decrypting certificate.  I know, I should have set the service account password to never expire.  My fault.  

Right now the service will not start (because the certificate has expired) and powershell commands come up with a communication error:  

get-adfsproperties : The communication object, System.ServiceModel.Channels.ServiceChannel, cannot be used for communication because it is in the Faulted state.  

I have tried the command "Update-AdfsCertificate -CertificateType Token-Decrypting -Urgent" but that comes up with the same error.  As the service will not start I cannot get into the console.  

Please help.

## Answer (community) — community member

*upvotes: 2 · updated: 2022-07-28*

I just encountered this issue in Server 2019.  The easiest solution was to just set the clock back to a day when the certificates weren't expired and start the service.   Then you can generate the new certificates. I found that the computer clock could only be adjusted via Control Panel "Date and Time" app.  This issue is very likely the result of setting the Automatic Renew option to disabled and never manually generating certificates before they expire.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-05-22*

can you try to start the service with a different service account?    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/manually-configure-a-service-account-for-a-federation-server-farm
