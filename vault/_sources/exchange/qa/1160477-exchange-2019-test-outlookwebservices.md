---
title: "Exchange 2019 test-outlookwebservices失败"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160477/exchange-2019-test-outlookwebservices
question_id: 1160477
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 test-outlookwebservices失败

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160477/exchange-2019-test-outlookwebservices (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

运行test-outlookwebservices时，自动发现失败，如图。

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-13*

Hi,

Welcome to Microsoft Q&A! 

Currently in Microsoft Q&A we only support English, could you please edit your question into English so that more community members can help to solve your issues? Thanks for your understanding.

Then based on my understanding, you ran the Test-OutlookWebServices cmdlet in Exchange 2019 and got a failure result for Autodiscover service, right? If this is the case, you can just ignore the result as although this cmdlet can be run in Exchange 2019, it's functional only in Exchange Server 2010.  

Reference: Test-OutlookWebServices  

I tried runing it in my Exchange 2019 lab environment and got the same output as yours. But as mentioned above, the output doesn't make sense at all in Exchange 2019. 

With the above being said, if you are attempting to check the autodiscover service within your environment, you can take advantage of the built-in Outlook client tool Test E-mail AutoConfiguration. For detailed instructions, you can refer to: Mailboxes - Test E-mail AutoConfiguration

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
