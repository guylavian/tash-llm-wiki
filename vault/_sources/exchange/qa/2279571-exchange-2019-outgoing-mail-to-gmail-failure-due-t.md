---
title: "Exchange 2019 Outgoing mail to gmail failure due to SPF record error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2279571/exchange-2019-outgoing-mail-to-gmail-failure-due-t
question_id: 2279571
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# Exchange 2019 Outgoing mail to gmail failure due to SPF record error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2279571/exchange-2019-outgoing-mail-to-gmail-failure-due-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Sir,

```
Customer has an Exchange 2019 organization with 2 Exchange servers (Server name: Ex1 & Ex2) in 1 organization. Email has only 1 domain: domain1.com.
```

They encountered an SPF return error message when the send out email outgoing from ex2 server only to Gmail. It is fine when the outgoing email to Gmail is from ex1.

Current server setting is:

Server EX1 IP: 1.2.3.4

Server EX2 IP: 5.6.7.8

In nslookup:

Set type=mx

domain1.com

MX: record:

domain1.com   MX Preference=0, mail exchanger=mail.domain1.com

domain2.com   MX preference=20, mail exchanger=mail2.domain1.com

mail.domain1.com   internet address=1.2.3.4

mail2.domain1.com  internet address=5.6.7.8

set type=ptr

1.2.3.4

Server:  8.8.8.8

Address:  8.8.8.8

Non-authoritative answer:

4.3.2.1.in-addr.arpa     name = mail.domain1.com

5.6.7.8

Non-authoritative answer:

8.7.6.5.in-addr.arpa     name = mail.domain1.com

set type=txt

domain1.com

Server:  8.8.8.8

Address:  8.8.8.8

Non-authoritative answer:

domain1.com   text =

```
"v=spf1 a mx a:mail.domain1.com a:mail2.domain1.com ip4:1.2.3.4 ip4:5.6.7.8 include:azurance.com ~all
```

===============================================================

May I know the SPF record failure due to the PTR record of 5.6.7.8 ?  It should be pointing to mail2.domain1.com ? Please suggest.

Joe Tam

## Answers

_No answers on this thread._
