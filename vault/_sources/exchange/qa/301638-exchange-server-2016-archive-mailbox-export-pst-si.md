---
title: "Exchange server 2016 archive mailbox export PST size showing 3 times of archive mailbox size"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/301638/exchange-server-2016-archive-mailbox-export-pst-si
question_id: 301638
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange server 2016 archive mailbox export PST size showing 3 times of archive mailbox size

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/301638/exchange-server-2016-archive-mailbox-export-pst-si (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team,  

We have exported the Exchange server 2016 archive mailbox PST. The PST size is showing 3 times huge on archive mailbox size.  

Checked deleted item also but unable to find why PST is taking too much size.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-08*

Hi anonymous user,    

Based on my experience, it's common for the exported PST file to be much larger than the mailbox size. This is because Exchange Server mailboxes store email more efficiently than Outlook uses in a *.pst or *.ost.     

For more information, hopefully you can find the following article helpful:    

Comparing Mailbox and PST File Size    

By the way, I've seen several similar threads which also mentioned that the PST size is around 3 times huge on archive mailbox size, I'll leave the links below for your reference:    

Online Archiving into PST took too much space    

his online archive mailbox size is 48 GB but while I go to downloading his mailbox into .pst, it's .pst is more than 150 GB    

Mailbox size much smaller than PST size    

For those that still run their own Exchange, I usually see an average of 2-3x the size of PST vs actual mailbox in a stand alone user    

(Please Note: Since some of the web sites above are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.)    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
