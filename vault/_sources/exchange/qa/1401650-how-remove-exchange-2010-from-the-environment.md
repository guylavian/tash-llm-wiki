---
title: "How remove Exchange 2010 from the environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1401650/how-remove-exchange-2010-from-the-environment
question_id: 1401650
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How remove Exchange 2010 from the environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1401650/how-remove-exchange-2010-from-the-environment (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange Server 2010: We recently completed migrating Exchange 2010 to Exchange 2016. Exchange 2010 servers were removed from the domain without properly uninstalling Mailbox and Hub transport.  How do I remove the mailbox and Hub transport roles from the environment when the old severs have been removed from the domain and there is no way to login them to properly remove them from the control panel

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-24*

Hello @Odong, Vincent,

According to your description, the best approach is to try to recover Exchange 2010 first, and then uninstall it according to the normal process. To recover exchange 2010, please refer to Recover an Exchange Server: Exchange 2010 Help | Microsoft Learn. After that, it is recommended that you try to remove Exchange 2010 according to the official recommended practices. For details, you could refer to this blog: Best practices when decommissioning Exchange 2010 - Microsoft Community Hub.

Certainly, if you really do not have the corresponding conditions to recover first, it is recommended that you refer to the "Remove Exchange from Active Directory" section of this document to delete it from AD. (Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
