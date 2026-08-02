---
title: "ExchangeService.findItems call fails outlook.office365.com:443 failed to respond"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1658976/exchangeservice-finditems-call-fails-outlook-offic
question_id: 1658976
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# ExchangeService.findItems call fails outlook.office365.com:443 failed to respond

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1658976/exchangeservice-finditems-call-fails-outlook-offic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,

We have integrated to exchange server (using EWS ews-java-api-2.0) in our java app.

Our customer facing issue in production env when our app try to connect to exchange server and read incoming mail.

Customer account ******@telesur.sr is authenticating to exchange server successfully but then fails with below error when performs ExchangeService.findItems call. 

UNHANDLED EXCEPTION: microsoft.exchange.webservices.data.core.excep tion.service.remote.ServiceRequestException: The request failed. The request failed. outlook.office365.com:443 failed to respond ****: microsoft.exchange.webservices .data.core.exception.service.remote.ServiceRequestException: The request failed. The request failed. outlook.office365.com:443 failed to respond at microsoft.exchange.webservices.data.core.request.SimpleServiceRequestBase.internalExecute(SimpleServiceRequestBase.java:74) [ews-java-api-2.0.jar:] at microsoft.exchange.webservices.data.core.request.MultiResponseServiceRequest.execute(MultiResponseServiceRequest.java:158) [ews-java-api-2.0.jar:] at microsoft.exchange.webservices.data.core.ExchangeService.findItems(ExchangeService.java:985) [ews-java-api-2.0.jar:] at microsoft.exchange.webservices.data.core.ExchangeService.findItems(ExchangeService.java:1049) [ews-java-api-2.0.jar:]

 

Kindly note that behavior is inconsistent. The error occurs once and in next attempt it works fine then again fails in next attempt.

 

Could you please assist what's going wrong here? We could have thought of anything wrong with configuration but sometimes it works too.

 

Thank you,

Amit Udiya

+91-7795145836

## Answers

_No answers on this thread._
