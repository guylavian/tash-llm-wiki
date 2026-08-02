---
title: "Exchange 2016 on-premise Search wont work on shared mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1428675/exchange-2016-on-premise-search-wont-work-on-share
question_id: 1428675
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 on-premise Search wont work on shared mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1428675/exchange-2016-on-premise-search-wont-work-on-share (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Does anyone have similar issue? If we tried to search with option all mailboxes then we get what we search for and when we change to current folder we get nothing. is this how it should work or is there any fix for this?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-20*

Hello Nenad Milanovic,

According to your description, I would like to confirm with you the detailed version of  Exchange CU and Outlook.

In addition, searches may be affected by how you add a shared mailbox in Outlook, so how do you add a shared mailbox? Was it added as an additional email account or auto-mapping?

Besides, you can try to disable FAST search either by applying Group Policy or by implementing the DisableServerAssistedSearch and DisableServerAssistedSuggestions user registry values.  

Group Policy registry path:  

HKEY_CURRENT_USER\software\policies\Microsoft\office\16.0\outlook\search  

DWORD: DisableServerAssistedSearch  

Value: 1

Reference: How Outlook 2016 utilizes Exchange Server 2016 FAST Search

If the issue persists, it’s suggested to try turning off cache mode for shared folders:

File tab -> Account Settings -> Double-click the account name -> More Settings -> Advanced tab -> Clear the check mark from download shared folders.

Hope the above information is helpful to you.   

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
