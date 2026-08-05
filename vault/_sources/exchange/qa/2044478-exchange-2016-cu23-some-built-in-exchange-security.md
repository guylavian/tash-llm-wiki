---
title: "Exchange 2016 CU23: Some Built-in Exchange Security groups have been deleted. How do I restore them?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2044478/exchange-2016-cu23-some-built-in-exchange-security
question_id: 2044478
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 CU23: Some Built-in Exchange Security groups have been deleted. How do I restore them?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2044478/exchange-2016-cu23-some-built-in-exchange-security (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I currently have Exchange 2016 CU23 running on Windows 2016 Server.  One of my colleagues deleted a few of the built-in Exchange security groups that were created during the installation of Exchange.  Some of these groups are needed for RBAC permissions, as well as viewing receive connectors within the ECP.  They have been deleted for over a year now and we don't have any backups to restore them.  What's the easiest way to recreate/restore them?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-09*

Hi,

Welcome to the Microsoft Q&A forum!

Based on my experience, there are two ways to deal with this situation.

The first method is creating new role group in EA. You can customize the permissions you need for the new group. For details you can refer to part Work with role groups of this article：Exchange Server permissions

The second way is to use the `Setup.exe` command with the `/PrepareAD` switch to recreate the default security groups. This command will reinitialize the default RBAC roles and groups. Here is the command you can run:

```
Setup.exe /PrepareAD /IAcceptExchangeServerLicenseTerms
```

More information about prepare AD:Prepare Active Directory and domains for Exchange Server
