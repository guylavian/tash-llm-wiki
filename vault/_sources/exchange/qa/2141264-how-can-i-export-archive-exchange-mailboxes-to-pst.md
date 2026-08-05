---
title: "How can I Export Archive Exchange Mailboxes to PST?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2141264/how-can-i-export-archive-exchange-mailboxes-to-pst
question_id: 2141264
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How can I Export Archive Exchange Mailboxes to PST?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2141264/how-can-i-export-archive-exchange-mailboxes-to-pst (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I had previously archived a few mailboxes on the Exchange server to store as a backup. Now I want to export all the mailboxes on the server (including the archived ones) to PST. I know I can use the PowerShell cmdlets to do so. But I am looking for a more straightforward method.

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2025-01-07*

Prerequisites:1. Ensure you have Exchange Organization Management role permissions

-  Configure the Mailbox Import Export role if not already done

Here's the step-by-step process:

-  Enable Mailbox Export Feature (one-time setup):

-  Open Exchange Management Shell (PowerShell)

-  Run this command:Prerequisites:

-  New-ManagementRoleAssignment -Role "Mailbox Import Export" -User "your_admin_account"

-  Export via Exchange Admin Center:

-  Log into Exchange Admin Center (EAC)

-  Go to Recipients > Mailboxes

-  Select the mailboxes you want to export

-  Click "..." (More options) > Export to PST

-  Choose export options:

-  Include archived mailboxes

-  Select specific folders or entire mailbox

-  Choose export location

-  Start the export

-  Alternative Method - eDiscovery:

-  Go to Compliance Admin Center

-  Create new eDiscovery case

-  Add the mailboxes to export

-  Create and run search

-  Export results as PST

-  Export via Exchange Admin Center:

-  Log into Exchange Admin Center (EAC)

-  Go to Recipients > Mailboxes

-  Select the mailboxes you want to export

-  Click "..." (More options) > Export to PST

-  Choose export options: 

-  Include archived mailboxes

-  Select specific folders or entire mailbox

-  Choose export location

-  Start the export

-  Alternative Method - eDiscovery:

-  Go to Compliance Admin Center

-  Create new eDiscovery case

-  Add the mailboxes to export

-  Create and run search

-  Export results as PST
