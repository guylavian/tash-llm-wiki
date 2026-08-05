---
title: "How to enable Office 365 Exchange Online API permissions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1852335/how-to-enable-office-365-exchange-online-api-permi
question_id: 1852335
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to enable Office 365 Exchange Online API permissions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1852335/how-to-enable-office-365-exchange-online-api-permi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

I need to read emails from my personal Outlook account with a Python service via IMAP. Since it is a service, I need to access the emails without user authentication via an UI. In the docs I found, I should register an app in Azure with IMAP access or ReadEmail permissions in the Office 365 Exchange Online API. However, this API does not appear for me in the Microsoft APIs screen, nor in the APIs screen that my organization uses. How do I activate this Office 365 Exchange Online API in Application Permissions? Do I need a specific license? Or is there an easier way to read emails from a personal account, using Application Permissions, now that Microsoft has deprecated basic authentication?

Thanks!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-02*

Hi, @Pierre Tavolo

Welcome to the Microsoft Q&A platform!

By your description, it is right to register your app in Azure, you can try the following again.

1.Register an App in Azure:

    Go to the Azure portal and navigate to "Azure Active Directory" > "App registrations" > "New     registration".

    Fill in the required details and register the app.

2.Assign API Permissions:

    On the app's Overview page, select "API permissions" from the "Manage" section.

    Click on "Add a permission" and select "APIs my organization uses".

    Start typing "Office 365 Exchange Online" in the search box and select it from the results.

    Choose "Application permissions" and expand the "Exchange" section.

    Select the necessary permissions such as Exchange.ManageAsApp and Exchange.Manage.

3.Grant Admin Consent:

    After adding the permissions, you need to grant admin consent for the permissions to take effect. This can be done by clicking on the "Grant admin consent" button on the API permissions page.

More information can be found Get started with Office 365 Management APIs | Microsoft Learn

If you are still unable to find the permissions, you can try using the Microsoft Graph API as an alternative. The Microsoft Graph API provides a unified endpoint for accessing various Microsoft services, including Outlook.

If the answer is helpful please click on ACCEPT ANSWER as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions. Thank you for your support and understanding.
