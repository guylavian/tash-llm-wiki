---
title: "Removing On-Premises Exchange Servers after Migrating to Office 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1807345/removing-on-premises-exchange-servers-after-migrat
question_id: 1807345
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Removing On-Premises Exchange Servers after Migrating to Office 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1807345/removing-on-premises-exchange-servers-after-migrat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Microsoft experts.  

I have a concern like the article here https://practical365.com/removing-premises-exchange-servers-migrating-office-365/, but I don't know if Microsoft has a solution so far for decommissioning on-premises Exchange but still keeping on-premises AD syncing users to M365?

My plan is after migrating all mailboxes to M365 I would like to completely decommission on-premise Exchange Server but still retain the on-premises Active Directory for other requirements, directory synchronization and password hash sync so that users have a single set of credentials to remember for authenticating to Office 365 cloud services.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-17*

If you are looking for a migration between On-premises Exchange server and Office 365, then I would suggest you use a professional solution named Weeom Exchange to Office 365 Migration (Weeom Exchange Server Suite) Software.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-15*

I think you are talking about Exchange Hybrid Configuration between your on-premises Exchange Server and Office 365.

After migrating all mailboxes to Office 365 you can completely decommission on-premises Exchange Server but still retain the on-premises Active Directory for other requirements.

Once you have migrated all mailboxes to Office 365, remove all mail flow connectors and uninstall Exchange Server.

With the help of Azure AD Connect, keep the on-premises AD synchronized with Azure AD.

After this, by Office 365 admin center or through EMS, you can manage all mail-related tasks.
