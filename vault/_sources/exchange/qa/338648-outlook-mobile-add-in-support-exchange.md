---
title: "Outlook Mobile Add-in Support - Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/338648/outlook-mobile-add-in-support-exchange
question_id: 338648
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-development-routing-development-other", "office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Outlook Mobile Add-in Support - Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/338648/outlook-mobile-add-in-support-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello there, I want to ask a question about Exchange Outlook Mobile Add-on support. I'm developing Phishing Reporter XML Add-in for Outlook. When I deployed the Add-in on Exchange Admin Center,  I've see the add-in my Outlook Desktop application and Exchange OWA. But I can not see Add-in on my Outlook IOS version. It is supported by Mobile devices, I tested with O365 account on IOS devices and works well. Is there a configuration setting for mobile support of add-ons on Exchange?    

Exchange account:    

    

Office 365 account:

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-07*

Hi @Sedat Özdemir   ,    

Thanks for sharing these information, I did a research about add-ins in Outlook mobile app, and I didn't found anything that could prove the add-ins could also working for Exchange on-prem mailboxes: Outlook mobile add-ins are supported on all Microsoft 365 business accounts, Outlook.com accounts, and support is coming soon to Gmail accounts.    

And the first snapshot you provided also proved this.    

Also I found a third-party article about Outlook add-ins: How To Use Outlook and OWA Add-ins    

Outlook on iOS/Android. Note: Add-ins on Outlook for mobile devices can only work if the mailbox hosted under Office 365 solution.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Outlook client support, then I would think it is expected that the add-ins of Outlook mobile app could not working for on-prem Exchange :(    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-06*

Thanks for your reply. I'm not using the Microsoft Report Phishing add-ins. I'm developing for my organization Phishing Reporter XML Add-in which basically sending the EML to specified email address. I tested with O365 account on IOS devices and works well, but I deployed add-in on-premise Exchange server, it didn't not work on Outlook mobile.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-01*

Hi @Sedat Özdemir   ,    

Are you using the Report Phishing add-ins?    

    

If so, I think it's expected because: The Report Phishing add-in is not available for shared mailboxes or mailboxes in on-premises Exchange organizations.    

See this article: Enable the Report Phishing add-in    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
