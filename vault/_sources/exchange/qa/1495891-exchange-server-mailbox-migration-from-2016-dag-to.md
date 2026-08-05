---
title: "Exchange Server Mailbox Migration from 2016 DAG to 2019 DAG."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1495891/exchange-server-mailbox-migration-from-2016-dag-to
question_id: 1495891
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server Mailbox Migration from 2016 DAG to 2019 DAG.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1495891/exchange-server-mailbox-migration-from-2016-dag-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
We are doing migration of mailboxes from Exchange 2016 DAG to 2019 DAG, Have notice that C: drive is significantly increasing the size, however we dont have any DB mounted in this drive, also IIS and Transport logs are located in D Drive.
Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-17*

Check this: Cleanup Exchange logs.
Pick a retention period for your logs and then set this as a scheduled task to run as often as possible.
I also recommend using something like WindirStat to confirm the actual location of what is taking up your disk space.

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-16*

Hello @IT Engineer    

From what I've found, this seems to be related to transaction logs. Large transaction logs are generated when mailboxes are moved.  

In addition, the transaction logs should be automatically deleted when the migration or backup is completed. If the current disk is not full, you can temporarily ignore it and observe. If it affects usage, you may consider enabling circular logging.  

Reference：
Large transaction logs are generated  

https://learn.microsoft.com/en-us/answers/questions/307696/exchange-transaction-logs  

Enable circular logging in Exchange Server

(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

Regards
SF
