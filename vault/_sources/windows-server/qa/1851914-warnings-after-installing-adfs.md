---
title: "Warnings after installing ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1851914/warnings-after-installing-adfs
question_id: 1851914
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Warnings after installing ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1851914/warnings-after-installing-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. I installed ADFS and got warnings. How critical are they? Which services does it interact with?

The first warning is to restart the server - OK, I'll do it.

The second warning. My wildcard certificate was issued using the Active Directory Certificate Service*.LAB.COM

Did I understand correctly that I have to run a powershell commandlet to fix it?https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/ad-fs-support-for-alternate-hostname-binding-for-certificate-authentication

Set-AdfsAlternateTlsClientBinding -Member ADFS.lab.com -Thumbprint '<thumbprint of cert>' ?

The third warning:An error occurred during an attempt to set the SPN for the specified service account. Set the SPN for the service account manually.  For more information about setting the SPN of the service account manually, see the AD FS Deployment Guide.  Error message: The SPN required for this Federation Service is already set on another Active Directory account.  Choose a different Federation Service name and try again.

## Answers

_No answers on this thread._
