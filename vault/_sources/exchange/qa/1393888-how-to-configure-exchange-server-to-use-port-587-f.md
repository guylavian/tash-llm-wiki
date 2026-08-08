---
title: "How to configure Exchange Server to use port 587 for outbound mail"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1393888/how-to-configure-exchange-server-to-use-port-587-f
question_id: 1393888
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# How to configure Exchange Server to use port 587 for outbound mail

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1393888/how-to-configure-exchange-server-to-use-port-587-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've just set up an Exchange Server 2019 on my own test server running Windows Server 2022. Everything works fine when port 25 is open.

But my VPS provider, where I'm planning to set up a mail server, blocks port 25 due to spam issues. Is it possible to configure Exchange Server to use port 587 for outbound mail? 

As I understand for now - I need to configure Send connectors to proxy outbound mail. And I've tried to do so - just selected "Proxy through client access server" in Send connector. And it's still using port 25 ... I've tried to change port for Send connector, I’ve tried to change port for Outbound Proxy Frontend connector. Nothing helps.

Is it even possible to use port 587 to send email to other servers? Or the only way is to use smart host?

## Answers

_No answers on this thread._
