---
title: "exchange 2016 ecp - office 365 tab error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2069678/exchange-2016-ecp-office-365-tab-error
question_id: 2069678
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange 2016 ecp - office 365 tab error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2069678/exchange-2016-ecp-office-365-tab-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have installed AZ AD Connect, ran the Hybrid wizard and selected full not minimal. I have synced users. When I Log into my Exchange 2016 admin center and click the Office 365 tab I receive:

This page isn’t working

outlook.office365.com is currently unable to handle this request.

HTTP ERROR 500

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-16*

Hi @Chuck Yucuis,

Welcome to the Microsoft Q&A platform!

Based on your description, you're encountering an HTTP 500 error when trying to access the Office 365 tab in the Exchange 2016 admin center. This error is usually a server-side issue. Here are a few steps you can take to troubleshoot and resolve the issue:

-  Look at the Event Viewer on your Exchange server for any warnings or errors around the time you tried to access the Office 365 tab. This might give you more specific information about what is causing the error.

-  Ensure that all necessary Exchange services are running properly. You can check this by opening the Services console (`services.msc`) and verifying the status of related Exchange services.

-  Verify that OAuth is correctly configured for hybrid deployments. This is essential for the proper functioning of hybrid features. You can use the following command in Exchange Management Shell to verify OAuth configuration:

```
Test-OAuthConnectivity -Service EWS -TargetUri https://outlook.office365.com/ews/exchange.asmx -Mailbox  -Verbose
```

-  Ensure that your Exchange server is up to date with the latest cumulative updates and patches.

-  Sometimes, browser cache can cause issues. Try clearing the cache or using a different browser.

-  If none of the above steps resolve the issue, consider re-running the Hybrid Configuration Wizard to ensure that no steps were missed or misconfigured.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
