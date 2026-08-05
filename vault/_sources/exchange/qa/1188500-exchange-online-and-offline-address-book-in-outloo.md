---
title: "Exchange Online and offline address book in Outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1188500/exchange-online-and-offline-address-book-in-outloo
question_id: 1188500
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online and offline address book in Outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1188500/exchange-online-and-offline-address-book-in-outloo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

For some reason, I have several Outlook 2016 cache mode clients not seeing random users in the offline address book. We are using O365 Exchange online and AD on-premise, syncing to Azure. All users are visible in the normal global address book.

What I tried:

-  Delete offline address book from C:\Users\user\AppData\Local\Microsoft\Outlook

-  rename offline address book from C:\Users\userAppData\Local\Microsoft\Outlook

-  re-create outlook profile.

-  article

anything high level on the O365 Tenant to check?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-13*

Hi  @ Virtual Tech ,

Are these users who do not appear in the OAB newly added?

If so, please check back in 24 hours to see if the OAB has been updated. Because the GAL can take 24 to 48 hours to update the OAB.

Here is a troubleshooting guide about not being able to view M365 users in OAB:

Cannot find user in offline address book - Exchange | Microsoft Learn

Hope this helps!

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
