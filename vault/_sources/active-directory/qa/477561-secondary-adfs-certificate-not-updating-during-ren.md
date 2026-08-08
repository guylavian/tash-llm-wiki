---
title: "Secondary ADFS certificate not updating during renewal"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/477561/secondary-adfs-certificate-not-updating-during-ren
question_id: 477561
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Secondary ADFS certificate not updating during renewal

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/477561/secondary-adfs-certificate-not-updating-during-ren (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I am hoping someone could lead me to resolve this issue.  

I have renewed the SSL certificate (service communication) on the primary ADFS server but the secondary is not updating and is still showing the old certificate thumbprint.  

Both servers (Win 2016) have the certificate and private key in their respective personal store. One thing I noticed is that the virtual account adfssrv does not have the read permission on the private key on the secondary but has the permission on the primary server. I am not sure if it is related.  

Thank you for your help.

## Answers

_No answers on this thread._
