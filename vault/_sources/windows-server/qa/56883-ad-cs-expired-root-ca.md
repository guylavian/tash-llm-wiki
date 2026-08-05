---
title: "AD CS Expired Root CA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/56883/ad-cs-expired-root-ca
question_id: 56883
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# AD CS Expired Root CA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/56883/ad-cs-expired-root-ca (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a 2 tier PKI environment. Every time i add  a server in the domain 2 expired  Root certificate appears in the Intermediate CA store of new server.      

one is  certificate template  cross certification authority template and other is Root Certification template which are both expired  

We previously have a cross certification to other PKI but its already decommission.  

I would like to know how to stop new computers on getting that certificate and is there a way to cleanup the prod server who has that expired certificate?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-03*

Hello,    

Thank you so much for posting here.    

According to our description, every time when we add a server to the domain, there will be 2 expired certificates appearing in the Intermediate CA store. For example:     

    

As mentioned, the expired certificates are Cross CA and Root CA.     

    

Firstly, we need to figure out how the computers get the certificates. If automatically, we could have a check by running “gpresult /h” to get a detailed group policy result report, then check if there is any GPO for the computers to get the certificates.    

Besides, we could have a check of the expired certificate and make sure that they are not Root CA certificate and Intermediate CA certificate. What I mean here is that the expired certificates could be issued by Root CA and Intermediate CA.     

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong
