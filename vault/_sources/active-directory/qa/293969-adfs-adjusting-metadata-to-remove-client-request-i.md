---
title: "ADFS Adjusting MetaData to remove client-request-id"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/293969/adfs-adjusting-metadata-to-remove-client-request-i
question_id: 293969
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Adjusting MetaData to remove client-request-id

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/293969/adfs-adjusting-metadata-to-remove-client-request-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

Have an ADFS server setup for various connections. All SAML configs work while connecting directly to ADFS. We are trying to set up a WAP to secure our network a bit more and to force Forms Based Authentication to external users.  

During testing, there is 1 SAML trust that does not work through the WAP and came to the conclusion with the vendor that the issue is when going through the WAP the SAML POST adds an extra parameter called "client-request-id" which the SP doesn't accept and therefore fails.  

They are saying that the fix needs to be applied from the ADFS side, but I am unable to find anything that is public knowledge that will allow this change?  

Lastly, they are deploying a code fix in the future that will accept the client-request-id but at this time no ETA. Also for knowledge, the vendor is Cisco :D, and the issue is with VPN ( AnyConnect ) through ASA.  

Thank you,  

Daniel

## Answers

_No answers on this thread._
