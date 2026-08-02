---
title: "Exchange Online Mailbox soft-deleted grace period"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1379889/exchange-online-mailbox-soft-deleted-grace-period
question_id: 1379889
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Online Mailbox soft-deleted grace period

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1379889/exchange-online-mailbox-soft-deleted-grace-period (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Have below question, appreciate someone could answers these:

-  If i remove exchange license from user, their mailbox data will be retained for 30 days grace period. But what if after 10 days I assign the license back to user and mailbox got recovered, then I unassign their license again. Will the grace period restart from 30 days or it will continue from the initial grace period?

-  I'm doing a migration from 3rd party mail hosting to EOP. Now domain (Company A) is verified in M365 tenant and both locations have mailboxes with same email address. I can't cutover MX record yet because of some reasons. And now my M365 tenant there is other users (Company B) with different domains as well and they are using the EOP services already. When users of Company B is sending emails to Company A (Company A have both email address in EOP and 3rd party hosting, MX points to 3rd party hosting), the emails just stay internally within M365 organization and won't go externally to look for actual MX record. I've tried to search through the internet and tried with connectors method, all just won't work. So I ended up unassign their exchange license to remove the mailbox, would like to know is there any other alternatives that I can do now before I perform the MX cutover? I need to keep both email address for continuous sync before I proceed with the MX cutover.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-03*

Hi @Marcus Wong  

Will the grace period restart from 30 days or it will continue from the initial grace period?

It should restart from 30 days.

If the purpose is to keep the mailbox data, you can consider converting it to a shared mailbox, which does not require a license and have a storage quota of 50 GB.

Now domain (Company A) is verified in M365 tenant and both locations have mailboxes with same email address.

If the email addresses are exactly the same, it may not be possible to deliver emails to third-party.

If possible I would suggest using different email addresses, then use mail flow rules or Outlook inbox rules in Exchange Online to forward or redirect the messages to third-party.

To archive this, you may also need to first configure this domain (Company A) as internal relay domain in Exchange Online, then create a send connector to send messages to recipients in the third-party host.

For more details, please refer to:

Manage accepted domains in Exchange Online (Internal relay part)

Set up connectors to route mail between Microsoft 365 or Office 365 and your own email servers

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
