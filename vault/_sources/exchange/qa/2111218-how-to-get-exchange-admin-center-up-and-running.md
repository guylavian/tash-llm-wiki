---
title: "How to get Exchange admin center up and running?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2111218/how-to-get-exchange-admin-center-up-and-running
question_id: 2111218
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to get Exchange admin center up and running?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2111218/how-to-get-exchange-admin-center-up-and-running (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I can run with or without ssl and the logon-screen opens properly with or without ssl. once I use non-proper credentials the logon-screen prints out a message and this loop continues until the credentials are right but instead of presenting the menu on the left column and on the top it simply shows: This page isn't working right now - from my perspective it would be more likely  an it never worked (on our infrastructure).  

Although in the past it worked but the old exchange-server isn't available to me (long story).  

So how can I fix this problem?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-28*

Hi,@Claus Frauenheim

Thanks for posting your question in the Microsoft Q&A forum.

Based on your description, you want to know if TLS 1.2 is active and enabled by Exchange.

 In the Exchange Server server, type `regedit` and press Enter to open the Registry Editor.

-  Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols`.

-  Under `TLS 1.2`, select the `Server` and `Client` keys respectively. Check to see if their status is Enable.

I need more information from you about whether Exchange is enabled for TLS 1.2:

1.What version of Exchange Server do you have?

2.Can you provide a screenshot of the reported error message?
