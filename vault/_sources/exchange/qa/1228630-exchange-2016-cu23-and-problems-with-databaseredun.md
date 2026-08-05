---
title: "Exchange 2016 CU23 and problems with DatabaseRedundancy and DatabaseAvailability"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1228630/exchange-2016-cu23-and-problems-with-databaseredun
question_id: 1228630
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Exchange 2016 CU23 and problems with DatabaseRedundancy and DatabaseAvailability

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1228630/exchange-2016-cu23-and-problems-with-databaseredun (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
I have a standalone exchange server 2016 with CU 23 and I have problems. Sending e-mails takes a very long time, even several dozen minutes.
A few days ago exchange start having problems with this:

When I look at errors I've got this for DatabaseRedundancy :

And for DatabaseAvailability:

Any ideas for it?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-14*

Hi @drClays ,  

As Amit Singh said, if you don’t set up a database availability group, you could ignore the errors safely.   

I tested my Exchange lab without DAG, it returns the same result.

For slow mail sending, you can check the mail queue for stuck mail.
Open Exchange Toolbox and select Queue Viewer. View email details through the "Queue Viewer".
In the list of messages in the queue, you can view detailed information about each email, including its status, recent events, and error characters.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
