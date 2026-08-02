---
title: "exchange 2013 EOMT.ps1 iis mitigation non applied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/318759/exchange-2013-eomt-ps1-iis-mitigation-non-applied
question_id: 318759
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# exchange 2013 EOMT.ps1 iis mitigation non applied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/318759/exchange-2013-eomt-ps1-iis-mitigation-non-applied (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an exchange 2013. Sunday 14 mar 2021 I've applied the kb5000871 that was downloaded wia windowsupdate. Today I've downloaded EOMT.ps1 to check if the server is secured by the last CVE-2021-26855. The script finish wtiting that server is patched and no mitigation need. It also tell to check web.config for the presence of section: <rewrite> <rules> <rule name="X-AnonResource-Backend Abort - inbound"> <match url=".*" /> ... that is MISSING on mine. So I've downloaded and installed the rewrite module 2.0 and run again. It always finish without appliyng any. My question is: is the section <rewrite> on web config necessary? Or it is just for exchange >2013? This because the script only chek if kb5000871 is installed, not if the web.config <rewrite> session is present. Thanks' a lot in advance

## Answers

_No answers on this thread._
