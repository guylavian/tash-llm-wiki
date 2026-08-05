---
title: "Exchange 2016 HMA - Unable to sign into outlook for iOS/Android"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1659944/exchange-2016-hma-unable-to-sign-into-outlook-for
question_id: 1659944
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 HMA - Unable to sign into outlook for iOS/Android

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1659944/exchange-2016-hma-unable-to-sign-into-outlook-for (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, 

My organization is using Exchange Server 2016 CU23 Apr24HU. We have established a hybrid configuration with our GCC tenant. Recently we are no longer able to log on-premises users into the outlook mobile application. They authenticate successfully and then are prompted saying no mailbox was found for this user in the gov community cloud, would you like to add as an exchange account? 

If I click add as exchange account, I am then prompted to sign in using basic authentication. I have tried with multiple accounts and multiple different devices both iOS/Android. Our exchange server is updated to the latest available version. I have verified all necessary ports have been opened. 

Outlook mobile previously worked with HMA. I have approximately 25 users who have successfully used HMA to sign into the on-prem exchange mailbox with outlook mobile.  These 25 users who previously setup outlook mobile is able to still authenticate and connect to their mailbox. New users who have not previously setup outlook mobile are unable to add their mailbox due to the error previously provided. 

HMA is functioning as intended for desktop client users, only mobile users seem to be affected at this time.

Thanks for any help you can send my way! This has been an issue for about 2 months. The only change I can thing of in my environment is related to Exchange Extended Protection.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-25*

Hi @Michael Herman,

According to your description, I suggest you check whether the user's email address/SMTP and login address/UPN match. Based on my experience, if the two do not match, it will cause login problems：

-  Check email address/SMTP:   · In the EAC, navigate to Mailbox under Recipient Configuration.   · Find and select the corresponding user mailbox, select "edit".   · In the "Email Address" tab, you can see a list of all the user's email addresses, including the primary SMTP address, which is usually shown in bold and preceded by the "SMTP:" prefix.   

-  Check the user login address/UPN:   · In Active Directory Users and Computers (ADUC), find the corresponding user account, right-click and select "Properties".   · In the "Account" tab, you can see the user's login name and domain, which is the user's UPN. A UPN is usually in a format like an email address, such as "[******@domain.com]".

If you have any questions, please feel free to contact me.
