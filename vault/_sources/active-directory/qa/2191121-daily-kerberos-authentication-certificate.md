---
title: "Daily Kerberos Authentication Certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191121/daily-kerberos-authentication-certificate
question_id: 2191121
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 6
qa_tags: []
---
# Daily Kerberos Authentication Certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191121/daily-kerberos-authentication-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello MS Community, 

Not sure if this question is appropriate for this forum. I need some expert's advice with Certificate Authority (CA) certificates deployments in our Domain Controllers (DC). We recently created a new Intermediate (Issuing) CA in our environment due to old OS version on our old CA and to conform with best practice to secure Root CA. Followed procedures and everything is working as it should. However, I have an odd issue where our DCs are requesting and enrolling a new Kerberos Authentication certificate on a daily basis. We're not experiencing any issue at this time, but this doesn't look to be a normal behavior. We have 100s of Kerberos Authentication certificates in the certificate stores, all have a year expiration period. Our concerns is that the DC will keep on acquiring multiple certificates which will cause an issue in the future for all of our DCs.

Any assistance or procedures to mitigate this anomaly is greatly appreciated.

v/r

Mark

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-15*

Hello Mark, 

Thank you for contacting us. It is not normal for domain controllers to request and register new Kerberos authentication certificates every day. This behavior may be caused by a configuration error or a problem with the certification authority. 

To resolve this issue, you can try the following steps: 

-  Check the event log on the domain controller for any errors related to certificate registration. 

-  Verify that the domain controller is configured to use the correct certification authority for certificate registration. 

-  Check the certification authority log for any errors or warnings related to certificate registration. 

-  Verify that the domain controller has the correct permissions to register the certificate from the certification authority. 

-  Check the certificate template on the certification authority to make sure it is configured correctly. 

Best regards

Qiuyang
