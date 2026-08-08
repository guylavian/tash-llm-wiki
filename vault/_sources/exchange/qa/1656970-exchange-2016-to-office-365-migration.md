---
title: "Exchange 2016 to  Office 365 Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1656970/exchange-2016-to-office-365-migration
question_id: 1656970
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-online-server", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 to  Office 365 Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1656970/exchange-2016-to-office-365-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What would you say I’d the best method for 80 odd users the plan is to decom the on prem server post migration does that rule oit remote move migration I know it used to at least I think it did.

The last few large scale migrations I have done were all remote move migrations in hybrid environments for large user base.

The last time I did one for a small company years ago I used the cutover method as it all just went over in a weekend with minimal user Impact anyway any advise would be appreciated

Thanks in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-17*

For a migration of around 80 users with the plan to decommission the on-premises server post-migration, a remote move migration might not be the most suitable option, especially if you're planning to decommission the server immediately after the migration. Remote move migration is typically used in hybrid scenarios where you maintain both on-premises and cloud-based resources.

Here are a couple of methods you could consider:

-  Cutover Migration: This method is suitable for smaller organizations and can be completed over a weekend, as you mentioned. It involves moving all mailboxes, users, and email data from an on-premises Exchange server to Office 365 and is generally straightforward. However, it requires careful planning to ensure minimal user impact.

-  Staged Migration: If you're looking to spread out the migration process over a longer period, a staged migration allows you to move batches of mailboxes to Office 365. This can help manage the load and ensure a smoother transition for users.

-  IMAP Migration: If you're only moving mailboxes and don't require calendar or contact migration, an IMAP migration could be a viable option. It's relatively simple but has limitations compared to other methods.

A version of cutover could look something like this:  

-  Verify that your Exchange 2016 environment is up to date.

-  Ensure that all user mailboxes are on Exchange 2016.

-  Configure Outlook Anywhere on your on-premises Exchange server.

-  Check that you have the necessary licenses for Microsoft 365.

-  Domain Setup:    Add and verify your domain in Microsoft 365.    Decide on a domain type (authoritative or internal relay).

-  User Communication:    Inform users about the upcoming migration and any actions they may need to take.

-  Migration Endpoint:    Create a migration endpoint in Microsoft 365 to connect to your on-premises server.

-  Pilot Migration:    Perform a pilot migration with a small number of users to validate the process.

-  Full Migration:    Schedule and perform the cutover migration for all users.    Monitor the migration process and troubleshoot any issues that arise.

-  Post-Migration:    Update DNS records to point to Microsoft 365.    Decommission on-premises Exchange servers if they are no longer needed.    Provide support to users for any post-migration issues.

-  Final Checks:    Ensure all data has been migrated successfully.    Confirm that users can access their mailboxes and that mail flow is working correctly.

Regarding tooling - we use Sharegate internally for everything and it works flawlessly.
