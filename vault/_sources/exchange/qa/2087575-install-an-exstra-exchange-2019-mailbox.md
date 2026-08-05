---
title: "Install an exstra Exchange 2019 Mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2087575/install-an-exstra-exchange-2019-mailbox
question_id: 2087575
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Install an exstra Exchange 2019 Mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2087575/install-an-exstra-exchange-2019-mailbox (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am in the process of upgrading my Exchange 2019 host's operating system from Windows 2019 to 2022 through a new virtual Windows 2022.

I have installed a new Windows 2022 virtual server, updated it and installed all prerequisites for Exchange 2019

I have followed your article:

https://www.alitajran.com/install-second-exchange-server-in-domain/

but receives the following error “The Mailbox server role is already installed on this computer”:

I need a hint :-)

Thanks in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-08*

I have solved the problem and would like to close the case :-) Thank you for your comments

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-07*

Hi,

Welcome to Microsoft Q&A community!

Ensure that you have prepared the Active Directory schema, AD, and domains before running the setup. You can do this by running the following commands:

```
Setup.exe /PrepareSchema /IAcceptExchangeServerLicenseTerms
Setup.exe /PrepareAD /IAcceptExchangeServerLicenseTerms
Setup.exe /PrepareDomains /IAcceptExchangeServerLicenseTerms
```

You can refer to:https://learn.microsoft.com/en-us/Exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019

Check FSMO Roles: Verify that the Domain Controller (DC) in the same site as the Exchange server is the schema master. If not, you may need to run the preparation commands in the site where the schema master resides or move the FSMO roles to the DC in the same site as the Exchange server.

Let me know if you need further assistance or if there's anything else I can help with!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-10-04*

If you are doing an in place upgrade of the operating system on an Exchange Server, that is not supported.
