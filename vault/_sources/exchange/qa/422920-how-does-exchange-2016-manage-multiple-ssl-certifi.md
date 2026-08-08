---
title: "How does Exchange 2016 manage multiple SSL certificates and services?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/422920/how-does-exchange-2016-manage-multiple-ssl-certifi
question_id: 422920
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# How does Exchange 2016 manage multiple SSL certificates and services?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/422920/how-does-exchange-2016-manage-multiple-ssl-certifi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 installation has 5 certificates installed, 3 default (one self-signed), one cert from the onsite CA, and one SSL from an 3rd party CA. One default cert has no services assigned to it. The certificate from the onsite CA and the default EX self-signed certs have IIS,POP,IMAP and SMTP assigned. The cert from the external CA has only IMAP,POP and SMTP... but i need to put IIS on there for OWA and ActiveSync.  

I'm not clear on how EXCH manages the certificates and the services assigned to them. My concern is that in the event there is an error with the namespace scheme on the 3rd party certificate or with the split DNS, and i assign the IIS to it, it will start spewing security errors with the OWA, outlook client and mobile devices. IIS is already assigned to 2 other certs as well, so how does it handle which one to use? Or does it reference all of them?  

Historically, when the certificate from the onsite AD CA gets renewed, all the remote mobile devices indicate that there is a certificate error because they can't resolve back to the local site, which would indicate it's using the certificate from the local AD CA, not the EX self-signed one. So how does it determine which one to use if the same services are applied across multiple certs?

## Answers

_No answers on this thread._
