---
title: "Exchange2019 mailbox move failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1403642/exchange2019-mailbox-move-failed
question_id: 1403642
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange2019 mailbox move failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1403642/exchange2019-mailbox-move-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I hope to move the mailbox from Exchange 2013 to Exchange 2019. Currently, my small mailbox (several hundred KB) can be moved normally, but the mailbox move of the large mailbox (1.xG) always fails, prompting me Resource 'MdbReplication(linzjtestdb)' is unhealthy and shouldn't be accessed.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-27*

Several factors, such as database corruption, disk errors, or insufficient resources, can cause this.

To fix this error, you need to identify and resolve the underlying issue causing the database to be unhealthy. Once the database is healthy, you can move Exchange 2013 mailboxes to Exchange 2019 without problems.

Check the Exchange 2013 server logs for any errors.

Run the Eseutil utility to scan the database for corruption. 

Check the disk space on the drive where the database is located. 

Check the memory and CPU usage on the Exchange 2013 server.

Also, make sure you check and remove all past move requests:

`Get-MoveRequest`

and

`Get-MoveRequest | Remove-MoveRequest -Confirm:$false`

Then, Run a repair on the problematic mailbox.

Validate that the destination mailbox database is correctly configured to accept the mailbox size.

Now, Try migrating the mailbox again.

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-26*

Hi @镇军 林  ,

but the mailbox move of the large mailbox (1.xG) always fails, prompting me Resource 'MdbReplication(linzjtestdb)' is unhealthy and shouldn't be accessed.

Does this issue only occur to this particular mailbox, or all large mailboxes are affected?  

Is the mailbox database (linzjtestdb) the source database or it's the target db?

Based on my research, mailbox move issues involving "MdbReplication" might be related to the transaction logs. So, if the aforementioned database is the target database, it's recommended to temporarily enabling the circular logging on the target database so that it will not generate the transaction logs during the migration. You can also refer to the blog below for other best practices when moving mailboxes:  

Mailbox migration best practices  

(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

If the issue persists, please run the command below and see if there's more information in the output:

```
Get-MoveRequestStatistics  -IncludeReport | FL
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
