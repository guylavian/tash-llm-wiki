---
title: "Office 365 Exchange Online Exchange.Manage scope cannot add to Graph API scopes in OAuth Link"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1406270/office-365-exchange-online-exchange-manage-scope-c
question_id: 1406270
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Office 365 Exchange Online Exchange.Manage scope cannot add to Graph API scopes in OAuth Link

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1406270/office-365-exchange-online-exchange-manage-scope-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In the OAuth link using authorization code flow, unable to pass any permissions from Office 365 Exchange Online API or for that matter any other permission that doesn't belong to Microsoft Graph API in the scopes parameter of the OAuth link.

For example, this is the OAuth link :-

login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=XXXXXXXXXX&response_type=code&redirect_uri=https%3A//google.com&response_mode=query&state=12345&prompt=consent&scope=offline_access%20AuditLog.Read.All%20Policy.Read.All%20Directory.Read.All%20IdentityProvider.Read.All%20Securityevents.Read.All%20ThreatIndicators.Read.All%20SecurityActions.Read.All%20User.Read.All%20UserAuthenticationMethod.Read.All%20MailboxSettings.Read%20DeviceManagementManagedDevices.Read.All%20DeviceManagementApps.Read.All%20UserAuthenticationMethod.ReadWrite.All%20DeviceManagementServiceConfig.Read.All%20DeviceManagementConfiguration.Read.All%20Organization.Read.All%20Exchange.Manage

 

It throws the following error

error=invalid_client&error_description=AADSTS650053%3A+The+application+%27AZTest%27+asked+for+scope+%27Exchange.Manage%27+that+doesn%27t+exist+on+the+resource+%2700000003-0000-0000-c000-000000000000%27.+Contact+the+app+vendor.%0D%0ATrace+ID%3A+02c24508-4948-4e3d-a79f-e19341c0ca00%0D%0ACorrelation+ID%3A+057133e4-9566-4263-87aa-a4328fbdedd8%0D%0ATimestamp%3A+2023-10-25+10%3A12%3A28Z&state=12345

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-10-27*

Exchange.Manage is a scope for the Exchange Online API (with resource ID of 00000002-0000-0ff1-ce00-000000000000, https://outlook.office.com), not the Graph API (00000003-0000-0000-c000-000000000000). So that's the expected behavior. 

To resolve the error, update your resource value. Do note that you cannot use a single request to obtain access tokens for multiple resources, one request per resource will do.
