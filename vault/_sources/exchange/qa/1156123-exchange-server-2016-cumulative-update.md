---
title: "Exchange Server 2016 Cumulative Update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1156123/exchange-server-2016-cumulative-update
question_id: 1156123
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2016 Cumulative Update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1156123/exchange-server-2016-cumulative-update (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

I am planning to migrate our current Exchange server 2016 CU19 (Hybrid Setup with MS365) to Exchange server 2019. Do I still need to install CU11 on the current exchange server 2016? Thank you.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-10*

Hi @Juan Dela Cruz  ,    

The requirement to upgrade Exchange Hybrid Server 2016 to 2019 is to upgrade Exchange Server 2016 to the latest cumulative updates.    

Then setup an Exchange 2019 Server on a new VM or physical server for migration.    

Here is a guide on how to upgrade Exchange : How to Upgrade Exchange Hybrid Server 2016 to 2019? (linkedin.com)    

Hope this helps!    

(Note:Microsoft provides third-party contact information to help you find additional information about this topic. This contact information may change without notice. Microsoft does not guarantee the accuracy of third-party contact information.)    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-09*

Follow the Migration Assistant to move between versions once everything has been migrated to 2019.    

To reduce the current client's effect, install a new Exchange 2019 server on a new network side, then configure all services (including SCP, all VD's URL, Outlook Anywhere, and MAPI over HTTP) and install the certificate.
