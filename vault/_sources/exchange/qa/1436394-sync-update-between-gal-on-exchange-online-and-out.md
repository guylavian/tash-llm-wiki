---
title: "Sync update between GAL on Exchange online and Outlook app on computer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1436394/sync-update-between-gal-on-exchange-online-and-out
question_id: 1436394
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator"]
---
# Sync update between GAL on Exchange online and Outlook app on computer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1436394/sync-update-between-gal-on-exchange-online-and-out (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How often GAL sync between Online Exchange and Outlook application on phone or PC please?

Is it possible to amend the sync period or increase?

Is it possible to reduce the sync time?

Is there a way to do via PowerShell or I have to do on the Exchange online website?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-24*

Hi @IT  ,

How often GAL sync between Online Exchange and Outlook application on phone or PC please?

The Global Address List (GAL) is a direct view of the current mail objects and it's usually updated automatically across devices right after the change occurs. 

Is it possible to amend the sync period or increase?  

Is it possible to reduce the sync time?  

Is there a way to do via PowerShell or I have to do on the Exchange online website?

NO. We have no control over the update of address lists in Exchange Online (The Update-AddressList cmdlet or Update-GlobalAddressList isn't available in Exchange Online PowerShell), so it's not possible to modify the "sync time" by either PowerShell or via EAC. 

In case you encounter issues that recipients that should appear in an address list do not, you would need to change the required property value for those users to a temporary value, and then back to the value that's required by the address list. For more details, you can refer to: 

Use Exchange Online PowerShell to update address lists

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
