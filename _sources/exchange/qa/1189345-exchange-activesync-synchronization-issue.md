---
title: "Exchange Activesync synchronization issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189345/exchange-activesync-synchronization-issue
question_id: 1189345
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
---
# Exchange Activesync synchronization issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189345/exchange-activesync-synchronization-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am currently experiencing a synchronization problem with the Exchange Activesync protocol that I did not encounter with the IMAP protocol.

I use the mail solution "Hostpoint.ch" that I synchronize locally on my PC with Outlook via the Exchange Activesync protocol. Since I use this protocol, the mails contained in my folders keep moving between the folders on my Outlook application whereas on my original mailbox (Hostpoint.ch), the mails are stored in the right folders...

When I put a mail in a folder in Outlook, there is no synchronization issue, it goes in the right folder in my original online mailbox.

However, when accessing previously stored mail, that's where Outlook goes "off the rails" and I see empty folders, and folders with mails from other folders.

I don't have this problem at all with the IMAP protocol and I'm struggling to understand why I have it with EAS.

Thanks in advance for your precious help!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-15*

Hi @Pierre ,

The EAS protocol provides access to data in Exchange mailboxes to various devices and other clients. Outlook supports the use of EAS to connect to other services that support the EAS protocol. Because an EAS connection doesn't provide all the features of a standard connection to Exchange, Outlook doesn't support this method to connect to Exchange.

You could refer to: https://learn.microsoft.com/en-us/outlook/troubleshoot/profiles-and-accounts/outlook-cannot-use-activesync-connect-exchange

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
