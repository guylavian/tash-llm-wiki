---
title: "Exchange - Free space on local disk."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/430813/exchange-free-space-on-local-disk
question_id: 430813
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange - Free space on local disk.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/430813/exchange-free-space-on-local-disk (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, How much free disk space should there be for mail to arrive correctly? I noticed that if 20gb remains on the local C drive, then mail arrives with great delays.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-11*

Hi @Андрей Михалевский   ,    

As Andy said, you could check the Event logs to see if there are any related logs with Back Pressure.    

In addition, I think you should check the folder size of your Exchange server to see if the Exchange log size or some other files are too large. If so, you could delete some of them.    

Or you could enable circular logging to delete the database logs. Configure circular logging for a mailbox database    

Then, as for the message delay issue, please try restarting the MS Exchange Transport service and check if the messages were stuck in Queue.     

And you can use the Delivery Reports or message header to analyze the process.     

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
