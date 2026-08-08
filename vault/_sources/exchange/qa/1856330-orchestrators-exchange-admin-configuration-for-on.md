---
title: "Orchestrator's Exchange Admin configuration for on-premises Exchange produces Azure error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1856330/orchestrators-exchange-admin-configuration-for-on
question_id: 1856330
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["msc-orchestrator", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Orchestrator's Exchange Admin configuration for on-premises Exchange produces Azure error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1856330/orchestrators-exchange-admin-configuration-for-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are in a hybrid, Azure AD Connect integrated environment, where local AD syncs to Azure.  This configuration requires that new Exchange mailboxes be initiated on-premises, created as Remote Mailboxes.

In SCO 2022, the Exchange Admin activities ceased working where they were working fine in SCO 2019.

Now, the attempt to use the Exchange Powershell activity produces an error like it's trying to connect with Azure, instead of local AD.  There is no "Azure AD application" for an on-prem SCO runbook server to connect to on-prem AD, or on-prem Exchange.  Has anyone seen this, and/or know what will fix it?

(Additional note, for activities that connect to Exchange Online work fine, once the mailboxes are created.  It's just the Integration Pack failing to work with on-prem.)

The configuration for this activity must specify a valid Azure AD application (client) ID.

`Exception: InvalidActivityException`

Target site: ExchangeGatewayFactory.ValidateConfigurationForExchangeOnline

`Stack trace:`

`   at SystemCenter.IntegrationPack.ExchangeAdmin.Domain.ExchangeGatewayFactory.ValidateConfigurationForExchangeOnline(ExchangeConfiguration configuration)`

   at SystemCenter.IntegrationPack.ExchangeAdmin.Activity.RunPowerShellCommandActivity.Execute(IActivityRequest request, IActivityResponse response)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-08-07*

Hi,

The error message you’re encountering, `InvalidActivityException`, indicates that the Exchange Admin Integration Pack is trying to validate the configuration for Exchange Online instead of your on-premises Exchange environment. This is likely due to a misconfiguration or a bug in the integration pack.

Here are some steps to help resolve this issue:

-  Verify Configuration: Double-check the configuration settings for the Exchange Admin Integration Pack. Ensure that it is explicitly set to connect to your on-premises Exchange server and not to Azure AD or Exchange Online.

-  Update Integration Pack: Look for any updates or patches for the Exchange Admin Integration Pack. Sometimes, updates can fix bugs or compatibility issues.

-  PowerShell Modules: Ensure that the correct PowerShell modules for on-premises Exchange are installed and up to date on the Orchestrator server. This includes verifying that the necessary modules and permissions are in place.

-  Service Account Permissions: Confirm that the service account used by SCO has the necessary permissions to create and manage mailboxes in the on-premises Exchange environment. This might involve adjusting roles and permissions in both AD and Exchange.

-  Hybrid Configuration Wizard: Make sure the Hybrid Configuration Wizard (HCW) has been run and configured correctly. This tool helps to set up and manage hybrid deployments between on-premises Exchange and Exchange Online.

-  Logs and Diagnostics: Review the logs and diagnostic information from both SCO and Exchange. This can provide more detailed error messages and clues about where the configuration might be going wrong.
