---
title: "Minimum of the Exchange hybrid configuration for Teams calendar sharing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1803060/minimum-of-the-exchange-hybrid-configuration-for-t
question_id: 1803060
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-teams-teams-business-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Minimum of the Exchange hybrid configuration for Teams calendar sharing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1803060/minimum-of-the-exchange-hybrid-configuration-for-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The company has recently deployed Microsoft Teams, but we prefer to keep everything else on-premises (mailboxes, mail flow in/out to the Internet).

We have a requirement to share calendar free/busy information between Microsoft Teams (in Microsoft 365) and our on-premises mailboxes. However, we do not want to configure any additional mail flow between Exchange on-premises and Exchange Online, and we want to avoid exposing our on-premises mailbox servers to Internet traffic. Additionally, since all mobile clients connect through a permanent VPN and use internal autodiscovery DNS, we prefer not to publish the autodiscovery record in the public domain.

Q1: Is it possible to achieve this with the mentioned restrictions?

Q2: Can we avoid running the Hybrid Configuration Wizard (HCW) and instead perform a minimal manual configuration?

What else, except listed below, do I need to have in place to get it working as expected?

-  Azure AD Connect: Configured and synchronizing user identities to Azure AD (completed) 

-  Federation Trust: create and configure a federation trust 

-  Is there any port/traffic that I need to unblock from the Internet to on-prem to a specific server to get it working?

-  Organization Relationship: create an organization relationship both on-premises and in Exchange Online 

-  Is there any port/traffic that I need to unblock from the Internet to on-prem to a specific server to get it working?

-  Do I need to publish an autodiscovery DNS record on the public domain?

-  Anything else?

We are concerned about the security implications of exposing the autodiscover service. Is there a safer alternative, such as utilizing the Edge Transport server to handle autodiscover requests?

Any tips highly appreciated.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-10*

Hi，@Michal Ziemba

Here is a detailed introduction of HCW: Introducing the Microsoft Office 365 Hybrid Configuration Wizard - Microsoft Community Hub

Previously, HCW didn’t allow skipping any configurations, which sometimes led to a bad Exchange Server hybrid configuration state. However, now you can use the newly introduced Choose Exchange Hybrid Configuration feature to skip unnecessary steps for existing hybrid configurations.

You can refer to this link: HCW Choose Exchange Hybrid Configuration feature | Microsoft Learn

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.
