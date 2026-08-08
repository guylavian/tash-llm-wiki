---
title: "Getting 500 from EWS API"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1400137/getting-500-from-ews-api
question_id: 1400137
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# Getting 500 from EWS API

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1400137/getting-500-from-ews-api (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to connect to exchange web server APIs from java. I want to configure the mail flow rules. This is the code I am using - 

```
exchangeService = new ExchangeService(ExchangeVersion.Exchange2010_SP2);
exchangeService.setUrl(new URI("https://outlook.office365.com/EWS/exchange.asmx"));
ExchangeCredentials credentials = new TokenCredentials(accessToken);
this.exchangeService.setCredentials(credentials);
exchangeService.getInboxRules();
```

The account I'm trying to connect to is a trial account with a domain like - `

## Answers

_No answers on this thread._
