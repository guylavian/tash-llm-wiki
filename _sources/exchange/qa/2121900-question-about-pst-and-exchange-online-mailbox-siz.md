---
title: "Question about PST and Exchange Online mailbox sizes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2121900/question-about-pst-and-exchange-online-mailbox-siz
question_id: 2121900
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Question about PST and Exchange Online mailbox sizes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2121900/question-about-pst-and-exchange-online-mailbox-siz (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

Pre-history: a mailbox is backed up by 3rd-party cloud backup and was exported to a PST file.

The size if the original mailbox is 19.65GB.

The size of the PST file exported from the mailbox snapshot is 18.4GB. 

I created a shared mailbox in Exchange Online and copied Inbox \deleted items and Sent Items from the PST file to the new shared mailbox. 

The size of the shared mailbox is only 5.59GB i.e. more 3 times less than original mailbox and PST file.

Is it possible taking into account that everything was copied (not a single item from Inbox \ Sent Items \ Deleted Items was missed)?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2024-11-22*

Hi,@X-Box-11-2021

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, when importing a PST file into a shared mailbox, the mailbox size appears smaller than the original mailbox.

There may be several reasons for this phenomenon:

1.The PST file exported by the third-party cloud backup you are using may contain metadata such as views, rules, categories, and indexes. It is recommended that you use Outlook to export the PST file and then check the size of the PST file.

2.If a PST file contains a mailbox item that is larger than 150 MB, the item will be skipped and not imported during the import process.You can refer to this link:https://learn.microsoft.com/en-us/purview/importing-pst-files-to-office-365#is-there-a-message-size-limit-when-importing-pst-files-using-drive-shipping

We recommend that you check your mailbox for lost emails, if there are no lost emails or import error message alerts, then there is no need to worry.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
