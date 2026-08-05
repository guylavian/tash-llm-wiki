---
title: "Exchange Hybrid minimal config to manage mailboxes that are already in the cloud."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2241033/exchange-hybrid-minimal-config-to-manage-mailboxes
question_id: 2241033
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Hybrid minimal config to manage mailboxes that are already in the cloud.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2241033/exchange-hybrid-minimal-config-to-manage-mailboxes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I have a customer that previously had Exchange 2010 installed. They then onboarded their mailboxes to the cloud and decided to remove the Exchange server.

Accounts are still synced from AD via Entra connect so they now that want to manage their mailboxes using an on-prem Exchange management server.

I have installed Exchange 2019 CU15.

What pre-requisites need to be in place to run the HCW with Minimal configuration for Recipient management only? I don't need all the config for migrating mailboxes and managing on-prem mailboxes or managing co-existence.

I am specifically looking for info around the type of SSL, Internal and External DNS, Virtual Directories and anything else that is relevant.

Thanks

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-31*

Hi @Arend Dieperink,

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, you would like to know the type of SSL, internal and external DNS, virtual directories, and other information required to run a minimally configured HCW.

-  In Exchange services, certificates issued by trusted third-party CAs are used to help protect Secure Socket Layer (SSL) communications between Exchange servers and clients. Services that use certificates include Outlook Web Edition, Exchange ActiveSync, Outlook Anywhere, and Secure Mail Transfer. To help protect recipients in local and Exchange Online organizations, and to help ensure that messages sent between organizations are not intercepted and read, the transport between local organizations and the EOP is configured to use mandatory TLS. Secure Mail Transfer uses TLS/SSL certificates provided by a trusted third-party certificate authority (CA). Mail between EOP and Exchange Online organizations also uses TLS. For more detailed information, refer to the document: Transport options in Exchange hybrid deployments | Microsoft Learn

-  This document discusses routing options for inbound mail from the Internet and outbound mail to the Internet, which can be determined by using DNS records for the MX records. Email routing in Exchange hybrid deployments | Microsoft Learn

-  You can use the Get-AutodiscoverVirtualDirectory, Get-WebServicesVirtualDirectory commands to obtain information about virtual directories. Make sure that the URL of the virtual directory for EWS, Autodiscover, etc. is correct and matches the certificate.

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.
