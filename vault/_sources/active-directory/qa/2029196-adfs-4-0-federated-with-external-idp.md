---
title: "ADFS 4.0, Federated with external IDP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2029196/adfs-4-0-federated-with-external-idp
question_id: 2029196
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS 4.0, Federated with external IDP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2029196/adfs-4-0-federated-with-external-idp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Scenario:

ADFS at Forest root domain Root.local

Federated with external IDP sending NameID to ADFS

at ADFS, claims Provider trust created and pass NameID

At child domain A.root.local we created shadow account to match with NameID sent from External IDP

A SAML2.0 app onboarded at ADFS but using security group as Role at child-domain A.Root.local (domain netbios A)

External IDP sucessfully send NameID to ADFS for login, question is how do I transform that NameID from external IDP to add A\NameID or ******@a.root.local so it will query the security group at child domain to send as role?

I am trying to add domain netbios name A to NameID in format A\NameID to the store and having another rule to look up security group at child domain to send as Role.

Thanks

## Answers

_No answers on this thread._
