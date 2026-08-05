---
title: "Exchange 2013 / MS 365 Apps for Business - Pop Up"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189542/exchange-2013-ms-365-apps-for-business-pop-up
question_id: 1189542
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2013 / MS 365 Apps for Business - Pop Up

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189542/exchange-2013-ms-365-apps-for-business-pop-up (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone, 

Need some help ... I have a user who keeps getting the pop up in Outlook that is asking for his username and password for the exchange server .. I have done the following 

-  reset users password 

-  redid users outlook profile 

-  took user out of cache mode in outlook 

-  Reg edits so outlook will look for the exchange server and not exchange 365 

I don't know what else to try short of nuking the user and redoing his whole profile or wiping the computer and reinstalling everything from starch .. 

Any thoughts ? or ideas ? 

Thanks ..

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-15*

Hi @Josh Hallett  ,

 

Outlook password prompt issues could be caused by various reasons. So before going on, I need to confirm the following questions with you:

 

-  Please confirm that only the current user account has the problem, and other users work with Ex13+Outlook for M365 app are fine?

-  When does the password prompt appear, when the user opens Outlook or when doing some operations? Can Outlook work normally after entering credentials? Can you provide a screenshot of the pop-up frame? (Be careful to erase personal information)

-  Which protocol is the user using, Outlook Anywhere or MAPI/HTTP? If possible, please provide a screenshot of Outlook Connection Status as shown below, be sure to remove all privacy information involved:

- 

-  `Reg edits so outlook will look for the exchange server and not exchange 365`       Notice that you modified the registry, in order to check if the Outlook client is still trying to connect to Exchange365, please run Test E-Mail Autoconfiguration to check the logs tab. If it's still trying to connect to Exchange Online, sometimes you need to add the registry "DisableAutodiscoverv2Service" as well.

 

Additionally, below are some other possible solutions based on my experience for reference:

1.Please try logging in with a different user's account to see if the problem persists. This helps narrow down if the issue is related to the configuration on this specific client. If the issue can be reproduced, you can try adding the following registry keys and check the result:

HKEY_CURRENT_USER\Software\Microsoft\Exchange\AlwaysUseMSOAuthForAutoDiscover REG_DWORD 1
HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Identity\EnableADAL REG_DWORD 1
HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Identity\Version REG_DWORD 1

Related thread please refer to: Re: Outlook keeps asking for password - Page 2 - Microsoft Community Hub

Important: Follow the steps in this section carefully. Serious problems might occur if you modify the registry incorrectly. Before you modify it, back up the registry for restoration in case problems occur.

 

-  Open Credential Manager. Locate the set of Windows credentials, remove credentials that contain Outlook names.

3. Shared calendars can impact the user credentials, this issue may also occur if you have shared calendars opened in Outlook. You can try to unselect the shared calendar to check the result.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
