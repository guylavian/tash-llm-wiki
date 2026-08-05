---
title: "Exchange New federation trust not working : an underlaying connection was closed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2182977/exchange-new-federation-trust-not-working-an-under
question_id: 2182977
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange New federation trust not working : an underlaying connection was closed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2182977/exchange-new-federation-trust-not-working-an-under (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

Quick summary of my issue : I need to set up an Organizational Relatioship Between two of my exchange organization to share some of my user calendar (both are on premise servers with no hybrid activated). I set it up on one of them with no issue but the other one won't event create a New-FederationTrust.

The only log i have after doing the command (or activating it via ecp) is : "Can't access federation metadata file from federation partner. More informations : "An underlaying connection was closed : an unexpected error occured during send."."

 

I tried multiple solutions :

-  Enabling TLS1.2 and disabling TLS1.0, 1.1, 1.3

-  Tried accessing federation urls from explorer with System/Exchange account :

-  https://login.microsoftonline.com/extSTS.srf

-  https://nexus.microsoftonline-p.com/federationmetadata/2006-12/federationmetadata.xml

-  https://domains.live.com/service/managedelegation2.asmx

-  I checked with adsiedit if any remnant of old federation-trust existed and there was nothing

-  I tried the command Test-Federation-Trust and it answered "no federation trust present" (as it should)

On my firewall all i see are accept and server-rst logs to/from Azure Ips. 

Please help me resolve this issue,

Thanks in advance,

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-27*

Hi @，

Thank you for posting your question in the Microsoft Q&A forum.

As per your description, your issue is that you are unable to create a federation trust between two exchange organizations. Is it convenient for you please clarify/provide the following information so that we can check further:

-  what is your exchange version?

2.What is the difference in configuration between your two exchange organizations?

Based on the information so far I have the following suggestions which I hope will help you:

-  make sure the Exchange server and Windows server are fully compliant with the latest updates and patches. Older versions can sometimes cause problems with authentication trust.

-  please check that federated sharing is enabled for your exchange organization using the Get-FederatedOrganizationIdentifier command.

-  Please check your version of the .NET Framework to ensure that it supports TLS 1.2. You can refer to the following link for detailed instructions on how to determine the .NET version and how to install the update. How to enable Transport Layer Security (TLS) 1.2 on clients - Configuration Manager | Microsoft Learn

-  Use the Get-ExchangeCertificate command to check that your certificate associated with the IIS service is not expired and is available. If it is not available, you can regenerate it using the New-ExchangeCertificate command.

-  Check your prerequisites and configuration process for errors in conjunction with this document. For example: The domain used for establishing a federation trust should be resolvable from the Internet; Both Exchange organizations in a federated sharing relationship must use the same Microsoft Entra authentication system for their federation trusts, and so on. Configure a federation trust: Exchange 2013 Help | Microsoft Learn

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.
