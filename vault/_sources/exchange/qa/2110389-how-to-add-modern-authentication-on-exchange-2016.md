---
title: "How to add modern authentication on Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2110389/how-to-add-modern-authentication-on-exchange-2016
question_id: 2110389
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to add modern authentication on Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2110389/how-to-add-modern-authentication-on-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Cannot add email accounts created by exchange 2016 on mobile outlook app (both iOS & Android)

How to fix this issue?

Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-25*

Selected Exchange to enter the email account information. After entering all details, outlook showed an error message as attached.

From the EAC, Under Mobile Device Details showed my Mobile record as below

From virtual directories, 

I can add my Exchange account in the mail app (both Android & iOS) which doesn’t have issue.

Thank you.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-25*

Hello, @CC,

Welcome to the Microsoft Q&A platform!

Based on your description, I understand that you want to know how to add modern authentication on Exchange 2016 due to failing to add email accounts created by exchange 2016 on mobile outlook app (both iOS & Android).

To enable modern authentication on Exchange 2016, please follow the steps below.

-  Enable Modern Authentication on Exchange 2016: Open the Exchange Management Shell and run the following command to enable OAuth authentication.

```
Set-OrganizationConfig -OAuth2ClientProfileEnabled $true
```

-  Configure Hybrid Modern Authentication (HMA): If you have a hybrid setup, you need to configure Hybrid Modern Authentication with the help of Configure Exchange Server to use Hybrid Modern Auth - Microsoft 365 Enterprise | Microsoft Learn.

-  Verify Configuration: Run the following command to verify OAuth is enabled.

```
Get-OrganizationConfig | Format-List OAuth*
```

By following these steps, you should be able to enable modern authentication on Exchange 2016. For more information, you can click on Enable Modern Auth in Exchange Server on-premises | Microsoft Learn for reference.

About your failure to add email accounts created by exchange 2016 on mobile outlook app (both iOS & Android), please make sure the Outlook app on both iOS and Android is updated to the latest version and try to remove and re-add the email accounts on the Outlook mobile app.

If it does not work, we have a dedicated supported channel to help you fix the issue. You can easily access help topics and contact the built-in support right form your device. Here is an article for your reference: Get in-app help for Outlook for iOS and Android - Microsoft Support.

If you still cannot solve your problem, to better understand your situation, can you provide the following information?

1.The screenshot of the error message.

2.The detailed steps about how you add your Exchange account to the mail app. Some screenshots would be highly appreciated.

3.Check if the you can add your Exchange account in the mail app which doesn’t have issue. This can help us to determine whether the issue is related to the Exchange accounts or the mail app.

4.The OS version of the problematic phone.

5.Is the Exchange account from Office 365 Exchange Online or Exchange on-premises?

6.Let the administrators check if the problematic uses’ Exchange ActiveSync feature is enabled.

If the answer is helpful please click on ACCEPT ANSWER as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
