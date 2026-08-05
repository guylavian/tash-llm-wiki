---
title: "The Kerberos protocol encountered an error while validating the KDC certificate during smartcard logon."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4272571/the-kerberos-protocol-encountered-an-error-while-v
question_id: 4272571
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 140
qa_tags: []
---
# The Kerberos protocol encountered an error while validating the KDC certificate during smartcard logon.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4272571/the-kerberos-protocol-encountered-an-error-while-v (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have an issuing CA, an offline root CA, and another (legacy, shouldn't be used anymore) online root CA. I am utilizing the new CA infrastructure to provide smartcard logon options for MFA. And it's working great for on-site devices and domain-joined devices over VPN. However, the issue I'm encountering happens when anyone tries to logon to a remote computer via RDP from a non-domain joined device. The error I receive is:  

The Kerberos protocol encountered an error while validating the KDC certificate during smartcard logon.

I have looked at certutil -dcinfo and verify, but all comes back clean (as it should, since remoting from domain-joined devices works great.) I have also tried turning off the old root CA service to no avail.

Due to limitations of virtualization hardware, we had to deploy the issuing CA on one of our DCs. I thought that maybe this issue was due to the DC's certificate not being provisioned from the new offline root CA, but it isn't working on any remote server or device. Any guidance is appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-16*

Hello Brandon

My name is Fred.

This forum is focused on home users In your case I recommend you to post in the IT support forum here:

https://techcommunity.microsoft.com/t5/windows-...

Or here:

https://learn.microsoft.com/en-us/answers/produ...

Sorry for this inconvenience.

Best Regards,

Fred
