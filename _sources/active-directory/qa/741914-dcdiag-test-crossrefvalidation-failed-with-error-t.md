---
title: "dcdiag test \"CrossRefValidation\" failed with error \"This cross-ref has a non-standard dNSRoot attribute.\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/741914/dcdiag-test-crossrefvalidation-failed-with-error-t
question_id: 741914
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# dcdiag test "CrossRefValidation" failed with error "This cross-ref has a non-standard dNSRoot attribute."

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/741914/dcdiag-test-crossrefvalidation-failed-with-error-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

I'm relatively new to Active Directory and i'm currently trying to set up a Domain and a Subdomain with two DCs each. I've already configured the Active Directory and DNS and according to my tests with nslookup every DC can resolve every name. Replication in each Domain works as well.

I then tested the Master DC (DC1) with dcdiag. Almost every test has passed except for "FrsEvent" and "CrossRefValidation".  

CrossRefValidation says:

```
Starting test: CrossRefValidation
     This cross-ref has a non-standard dNSRoot attribute.
      Cross-ref DN: CN=a79c523d-37df-4232-91bc-d812b8e6aafe,CN=Partitions,CN=Configuration,DC=Domain,DC=com
      nCName attribute (Partition name): DC=DomainDnsZones,DC=sub,DC=domain,DC=com
      Bad dNSRoot attribute: DC4-Sub.sub.domain.com
      Check with your network administrator to make sure this dNSRoot attribute is correct, and if not please change the attribute to the
     value below.
       dNSRoot should be: DomainDnsZones.sub.domain.com
        It appears this partition (DC=DomainDnsZones,DC=sub,DC=domain,DC=com) failed to get completely created.  This cross-ref
        (CN=a79c523d-37df-4232-91bc-d812b8e6aafe,CN=Partitions,CN=Configuration,DC=domain,DC=com) is dead and should be removed from the
        directory.
     ......................... DomainDnsZones failed test CrossRefValidation
```

I've googled the error, but i have not found any articles that explains the error in such a way, that a newbie like me could understand.

What does this error mean? What is CrossRefValidation?

Your help is greatly appreciated.

## Answers

_No answers on this thread._
