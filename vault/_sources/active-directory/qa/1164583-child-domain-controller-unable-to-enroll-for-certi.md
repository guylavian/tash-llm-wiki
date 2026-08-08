---
title: "Child domain controller unable to enroll for certificate in parent domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164583/child-domain-controller-unable-to-enroll-for-certi
question_id: 1164583
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Child domain controller unable to enroll for certificate in parent domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164583/child-domain-controller-unable-to-enroll-for-certi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I set up a quick lab with a couple of Windows Server 2022 hosts. The first host was promoted to a domain controller (dc-0.example.com) and a domain certificate authority was installed. That domain controller automatically enrolled itself for a certificate.

I then promoted the second host to a domain controller and configured it as a child domain in the above forest (dc-1.child.example.com).

However, the child domain controller is failing to auto-enroll for a certificate, with event id 53 from source CertificationAuthority.

Any idea why the parent domain controller thinks the child domain controller is in another forest?

```
Active Directory Certificate Services denied request 3 because A referral was returned from the server. 0x8007202b (WIN32: 8235 ERROR_DS_REFERRAL).
The request was for CHILD\DC-1$.
Additional information: Denied by Policy Module  0x8007202b, The requester's Active Directory object is not in the current forest.
Cross forest enrollment is not enabled.  CN=DC-1,OU=Domain Controllers,DC=child,DC=example,DC=com  ldap: 0xa: LDAP_REFERRAL: 0000202B: RefErr: DSID-0310079D, data 0, 1 access points
	ref 1: 'child.example.com'
```

## Answers

_No answers on this thread._
