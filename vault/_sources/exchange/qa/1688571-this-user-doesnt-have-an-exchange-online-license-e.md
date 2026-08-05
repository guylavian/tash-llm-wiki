---
title: "This user doesn't have an Exchange Online license error for Office 365 apps for Enterprise (E3)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1688571/this-user-doesnt-have-an-exchange-online-license-e
question_id: 1688571
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# This user doesn't have an Exchange Online license error for Office 365 apps for Enterprise (E3)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1688571/this-user-doesnt-have-an-exchange-online-license-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Sole user of Office 365 apps for Enterprise (E3) started having issues in Outlook over the weekend.   Outlook is getting no new messages and send attempts end in error 0x80040115. Further investigation shows that the user's mailbox has gone astray (I'm sure that its still there but inaccessible). 

What would cause a user to loose their mailbox connection and how would I correct the problem.   My current workaround is to switch to a Business apps - Standard license, which is not a good long term solution because the user needs to use Access.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-29*

Hi,

Welcome to the Microsoft forum.

According to your description , may I please know if this issue only occurs in Outlook? If you use OWA, will it occur?

1.

If the issue does not occur in OWA, we could consider that the mailbox is working fine and it may be something wrong with Outlook, you can try to do the following:

-  Open Outlook in safe mode and troubleshoot add-ins,more details you can refer to : Fix Microsoft Outlook Error 0x80040115 in Windows 11/10 (thewindowsclub.com)

-  Try to use SARA to fix the problem,download it in this link: Download Microsoft Support and Recovery Assistant from Official Microsoft Download Center

- 

If the issue also occurs in OWA, you may need to check the status of your E3 license. For example, if the license has expired, you will not be able to use all the features under the license including access to Exchange mailboxes.

Access to the Microsoft 365 admin Center,select Billing->Your products:

Check if the status of the E3 license has expired.

I hope this helps.Please feel free to contact me for any updates.
