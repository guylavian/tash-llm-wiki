---
title: "Exchange 2016 - Migrate mailbox data from one mailbox to another mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/409810/exchange-2016-migrate-mailbox-data-from-one-mailbo
question_id: 409810
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 - Migrate mailbox data from one mailbox to another mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/409810/exchange-2016-migrate-mailbox-data-from-one-mailbo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

Many thanks in advance, I am looking for how can we migrate mailbox data from one user mailbox to another mailbox, where both mailboxes are in Exchange 2016.  

I could see an option in Shell: Connect-Mailbox  

But, for this command to work, it looks like the expectation is target to be just a mail-enabled user, and not actually a mailbox. So, looking for whather I am correct about this, in first case. If yes, then what are the ways to proceed with this?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-27*

Hi Eric & Ashok,  

Thanks for your help, yes we finally moved on with export & import approach.   

However, I feel that Microsoft should introduce restore-mailbox feature to Exchange On-prem architecture

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-27*

Hi,    

The best choice is exporting the mailbox to pst and importing it to target mailbox, steps for your refference: Export Exchange mailbox to PST with PowerShell    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
