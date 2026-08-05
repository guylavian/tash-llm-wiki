---
title: "adfs certificate time does not take effect after modification"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/381433/adfs-certificate-time-does-not-take-effect-after-m
question_id: 381433
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# adfs certificate time does not take effect after modification

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/381433/adfs-certificate-time-does-not-take-effect-after-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Thank you for your answer    

```
PS C:\Users\administrator.TESTYUNWEI> Set-AdfsProperties -CertificateDuration 3650  
PS C:\Users\administrator.TESTYUNWEI> get-AdfsProperties |fl CertificateDuration  
  
CertificateDuration : 3650
```

I set the certificate time    

But my certificate Token Encryption Certificate 、 Service Communication Certificate The end time has not changed    

There is no automatic replacement of the new certificate    

How can I replace the certificate with a new certificate after the time I set

## Answers

_No answers on this thread._
