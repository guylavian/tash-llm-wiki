---
title: "Exchange 2019 CU12 generate CSR GUI is missing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198225/exchange-2019-cu12-generate-csr-gui-is-missing
question_id: 2198225
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Exchange 2019 CU12 generate CSR GUI is missing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198225/exchange-2019-cu12-generate-csr-gui-is-missing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All, 

```
Would like to seek for your help on exchange 2019 CU12, the generate CSR GUI is missing, and found out its GUI has been removed since CU12 due to security concern, just wonder any guide i can follow on how to generate CSR CUI via powershell ? any help would be appreicated, Thanks
```

Keith

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-25*

Hi keith li_1210,

Thank you for posting in the Microsoft Community Forums.

In the absence of a GUI, you can use the Exchange Command Line Manager (EMS) to generate CSRs.EMS is a powerful tool for Exchange Server that allows you to perform a variety of administrative tasks, including certificate management, from the command line.

The exact steps may vary depending on the version and configuration of Exchange Server; the following is a general guide:

Open EMS.

Generate a CSR using the appropriate commands.This usually involves specifying parameters such as the name of the certificate, key length, hash algorithm, and so on. Note that Exchange Server itself does not directly provide commands for generating CSRs, but you can use a Windows certificate management tool (such as certreq.exe) or a third-party tool to generate CSRs and configure certificates in Exchange.

Submit the generated CSR file to a certificate authority (CA) to obtain a signed certificate.

Install the signed certificate in Exchange Server.

 Exchange Server documentation | Microsoft Learn

Best regards

Neuvi Jiang
