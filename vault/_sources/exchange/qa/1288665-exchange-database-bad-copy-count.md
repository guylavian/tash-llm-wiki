---
title: "Exchange Database Bad Copy Count"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1288665/exchange-database-bad-copy-count
question_id: 1288665
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1", "windows-business-windows-server-high-availability-clustering-high-availability"]
---
# Exchange Database Bad Copy Count

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1288665/exchange-database-bad-copy-count (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have been facing an issue for last 5 days. I have four mailbox servers. Two in DC site and another two in DR site.

One mailbox server in my DC site getting unexpected reboot for last four months. I raised a ticket to Microsoft two months ago and they still can't provide any solution. But I have been facing a new issue for last 5 days. When my server got reboot, my databases showing bad copy 2. It shows that full DC site is disconnected. I searched a lot of article where I found the same solution get-mailboxdatabasecopystatus * and AD replication.

My active directory replication is totally ok from DC to DR and vice-versa. Also I checked 64327, 3343, 135 ports. These ports are also okay. I also checked dynamic port range. Even I opened all the ports from DC to DR but the issue still same.

I got the event ID 4113 error also.

When I ran test-replicationhealth command, I found the following error:

So please suggest me how to I resolve it. It's a big issue now and also sorry to say that last two months I didn't get any good support from Microsoft which I expected. Even earlier I posted about the reboot issue in technet but no one replied to me. 

```
Passive database copy 'MBXDB07\NCCBEXMBX2001' has an
                                                      unhealthy status 'DisconnectedAndResynchronizing' for duration
                                                      13:28:12.9520096. [SuspendComment: None specified.]
                                                      [ErrorMessage: The Microsoft Exchange Replication service was
                                                      unable to perform an incremental reseed of database copy
                                                      'MBXDB07\NCCBEXMBX2001' due to a network error. The database
                                                      copy status will be set to Disconnected. Error
                                                      Microsoft.Exchange.Cluster.Replay.NetworkTimeoutException: A
                                                      timeout occurred while communicating with server 'nccexmbx1999'.
                                                      Error: "A connection could not be completed within 5 seconds."
                                                         at Microsoft.Exchange.Cluster.Replay.NetworkManager.OpenConnec
                                                      tion(NetworkPath& actualPath, Int32 timeoutInMsec, Boolean
                                                      ignoreNodeDown)
                                                         at Microsoft.Exchange.Cluster.Replay.LogCopyClient.OpenChannel
                                                      (Boolean useScavenge)
                                                         at
                                                      Microsoft.Exchange.Cluster.Replay.LogCopyClient.QueryEndOfLog()
                                                         at Microsoft.Exchange.Cluster.Replay.FailoverPerformanceTracke
                                                      rBase`1.RunTimedOperation(TOpCode opCode, Action operation)
                                                         at Microsoft.Exchange.Cluster.Replay.IncrementalReseeder.IsInc
                                                      rementalReseedRequired(Action checkAbortRequested, Int64&
                                                      highestLogGenCompared, Boolean& e00IsEndOfLogStream)
                                                      ].
```

```
Passive database copy 'MBXDB07\NCCBEXMBX2001' has an
                                                      unhealthy status 'DisconnectedAndResynchronizing' for duration
                                                      13:28:12.9520096. [SuspendComment: None specified.]
                                                      [ErrorMessage: The Microsoft Exchange Replication service was
                                                      unable to perform an incremental reseed of database copy
                                                      'MBXDB07\NCCBEXMBX2001' due to a network error. The database
                                                      copy status will be set to Disconnected. Error
                                                      Microsoft.Exchange.Cluster.Replay.NetworkTimeoutException: A
                                                      timeout occurred while communicating with server 'nccexmbx1999'.
                                                      Error: "A connection could not be completed within 5 seconds."
                                                         at Microsoft.Exchange.Cluster.Replay.NetworkManager.OpenConnec
                                                      tion(NetworkPath& actualPath, Int32 timeoutInMsec, Boolean
                                                      ignoreNodeDown)
                                                         at Microsoft.Exchange.Cluster.Replay.LogCopyClient.OpenChannel
                                                      (Boolean useScavenge)
                                                         at
                                                      Microsoft.Exchange.Cluster.Replay.LogCopyClient.QueryEndOfLog()
                                                         at Microsoft.Exchange.Cluster.Replay.FailoverPerformanceTracke
                                                      rBase`1.RunTimedOperation(TOpCode opCode, Action operation)
                                                         at Microsoft.Exchange.Cluster.Replay.IncrementalReseeder.IsInc
                                                      rementalReseedRequired(Action checkAbortRequested, Int64&
                                                      highestLogGenCompared, Boolean& e00IsEndOfLogStream)
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-26*

Hi @Md. Rubiat Haque

Great to know that the issue has already been resolved and thanks for sharing the solution so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that The question author cannot accept their own answer. They can only accept answers by others.%22)

I'll repost your solution in case you'd like to "[Accept] the answer : )

There was network issue between DC to DR. They have something called zone protection between DC to DR. That's why the communication wasn't established properly between these two sites.

Best Regards,
Dezhi

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-22*

Hello,

Thank you for your question and for reaching out with your question today.

In order to stop the error, you need to modify the CheckDatabaseRedundancy.ps1 script. Please refer to the following thread fior information on how to do this:

http://social.technet.microsoft.com/Forums/en-US/exchangesvravailabilityandisasterrecovery/thread/23752d4d-2225-4bf2-850a-83c1d9f4f9be

If the reply was helpful, please don’t forget to upvote or accept as answer.

Best regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-22*

Hi Md. Rubiat Haque,

Does your problem appear during the reboot process of the exchange server or within a short time after reboot?

Does the same problem occur after waiting?

If the server keeps rebooting the connection timeout is normal.

Please also check your disk status to see if there is any damage.

This link can also help you troubleshoot errors.

https://social.technet.microsoft.com/Forums/en-US/49d624bd-dbda-4be6-adb3-0485508e4e01/database-copy-is-failed-and-suspended?forum=exchangesvradmin

Best Regards,

Dezhi

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation](https://aka.ms/msftqanotifications)"https://aka.ms/msftqanotifications)") to enable e-mail notifications if you want to receive the related email notification for this thread.
