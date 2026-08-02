---
title: "Error when running Active Directory schema commands for Exchange 2016 installation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1667920/error-when-running-active-directory-schema-command
question_id: 1667920
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Error when running Active Directory schema commands for Exchange 2016 installation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1667920/error-when-running-active-directory-schema-command (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Exchange Community, 

I am in the process of installing an Exchange 2016 server in our environment, which currently hosts Exchange 2010. However, I encountered an error while attempting to execute Active Directory schema commands. The error message reads: 'The parameter 'iacceptexchangeserverlicenseterms_diagnosticdataoff' is not a recognized option.'

The new server is domain-joined, and the account used belongs to both the Schema Admins and Enterprise Admins security groups. Despite this, I am uncertain about the cause of this error.

Any assistance would be highly appreciated,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-16*

Hi @Jabulani Motloung,

Welcome to the Microsoft Forum for technical support.

Based on your description, I noticed that the version you are installing is Exchange Sever2016 CU12. To prepare schema for this version, you should use the command in the format:

Setup.EXE /m:upgrade /IAcceptExchangeServerLicenseTerms

For detailed information you can refer to this document: Setup fails for unattended installation of Exchange Server 2019 CU11 or 2016 CU22 or later - Microsoft Support

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
