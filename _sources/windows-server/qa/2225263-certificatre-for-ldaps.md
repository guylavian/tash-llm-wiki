---
title: "Certificatre for LDAPS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2225263/certificatre-for-ldaps
question_id: 2225263
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Certificatre for LDAPS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2225263/certificatre-for-ldaps (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The client needs to connect to our LDAP over SSL from a Linux server not from our domain. We have our internal corporate Microsoft certification center. I created a certificate from the Kerberos template, which implies Server Authentication and Client Authentication. I successfully installed this certificate on the domain controller. I gave the client a regular certificate from our CA, just like I do for those who connect to Web services. As a result, the client successfully connected via LDAP over SSL. I am interested in such questions.

-  Do I need to pass another certificate to the client? I heard somewhere that the client needs to pass the certificate of the domain controller and the corporate CA.

-  If we did not have an internal CA, is it possible to use a self-signed certificate on the domain controller for LDAPS and pass it to the client?

-  How to detect such a self-signed certificate on the domain controller using Powershell or at least in the certificates snap-in?

## Answers

_No answers on this thread._
