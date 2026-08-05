---
title: "Outlook 2021 issues connecting to on Prem Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1689860/outlook-2021-issues-connecting-to-on-prem-exchange
question_id: 1689860
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Outlook 2021 issues connecting to on Prem Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1689860/outlook-2021-issues-connecting-to-on-prem-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 1 desktop client that currently has Office 2021 Home and Business installed but cannot connect to their mailbox hosted on an on premises Exchange 2019 CU14 server. Pings from the client PC to the autodiscover.domain.com DNS record return the correct IP address. We've tried Office 2007, Office 365 and now Office 2021. Login to OWA for this user works fine.

Have created an dword registry value to skip Office365 autodiscover priority and the problem persists.

What do we need to do to allow Outlook 2021 to connect to exchange 2019?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-03*

Hi @Shaughn Belmore  ,

Thank you for posting to Microsoft Community.

Based on your description, I know there is an issue with Outlook connect to account in Exchange Server.

Could you kindly offer the error or screenshot when you cannot connect with me for further assistance?

However,  please double check you have configured Internal and External URL in Exchange Server correctly. Ensure all your URIs are updated.

You could refer to Internal and External URL part of Configure mail flow and client access on Exchange servers | Microsoft Learn.

Please check Autodiscover connection for a user by use cmdlet below.

Test-OutlookWebServices -identity: xxxx@example.com –MailboxCredential (Get-Credential)

The cmdlet first checks if it can connect to Autodiscover service and specifies its URL. Then it checks connectivity with all services defined by Autodiscover xml records.

Hope it helps, if there are anything else I could help with, please feel free to contact me.
