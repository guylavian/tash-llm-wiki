---
title: "ADCA and kerberos?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/518655/adca-and-kerberos
question_id: 518655
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# ADCA and kerberos?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/518655/adca-and-kerberos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!  

I was following this guide to mitigate the petitoam issue.  

https://support.microsoft.com/en-us/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429  

But under additional mitigation it says the following:  

Disable NTLM for Internet Information Services (IIS) on AD CS Servers in your domain running the "Certificate Authority Web Enrollment" or "Certificate Enrollment Web Service" services.  

To do so open IIS Manager UI, set Windows authentication to Negotiate:Kerberos:   

If I do that the IIS manager gives an error "kernel mode authentication cannot be used with negotiable 2 providers" So it seems that enabling kernel mode authenticaiton stops the option to have negotiate Kerberos?  

Info:  

Server 2012 R2

## Answers

_No answers on this thread._
