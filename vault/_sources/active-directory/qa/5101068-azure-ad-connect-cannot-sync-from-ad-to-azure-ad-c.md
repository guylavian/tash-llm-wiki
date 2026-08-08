---
title: "Azure AD Connect cannot sync from AD to Azure AD Cloud"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5101068/azure-ad-connect-cannot-sync-from-ad-to-azure-ad-c
question_id: 5101068
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Azure AD Connect cannot sync from AD to Azure AD Cloud

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5101068/azure-ad-connect-cannot-sync-from-ad-to-azure-ad-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I would like to ask everyone that I have encountered a problem with Azure AD connect service.

Using Azure AD Connect application, I select an individual user or OU or Distribution Group to sync from our on-prem AD to Azure AD, but it doesn't sync.

When I select an option button "Sync all domains and OUs", then Azure AD can sync to Azure AD and we can see from portal. But in portal, there are duplicate users records when I select this option.

I would like to sync only specific user and OU only.

Please advise asap.

Thanks & Best Regards,

Susan

<To protect your privacy, your PII has been removed by moderator>

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hi Susan,

Good day to you.

Generally, the admin can run AAD connect tool to select the specific OU or user to sync with Azure AD like the page you post. Based on your description, it looks like there is the failure during syncing user or OU or Distribution Group. May I know if there is error message about this issue when you syncing them, or just they can't be synced? Besides, you first can run the troubleshooting task in the wizard to check if it is workable, please perform the following steps:

-  Open a new Windows PowerShell session on your Azure AD Connect server with the Run as Administrator option.

-  Run `Set-ExecutionPolicy RemoteSigned` or `Set-ExecutionPolicy Unrestricted`.

-  Start the Azure AD Connect wizard.

-  Navigate to the Additional Tasks page, select Troubleshoot, and click Next.

-  On the Troubleshooting page, click Launch to start the troubleshooting menu in PowerShell.

-  In the main menu, select Troubleshoot Object Synchronization.

Looking forward to your feedback and we'll always be here for you.

Regards,

Joey
