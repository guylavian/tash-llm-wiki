---
title: "exchange 2016 graceful shutdown"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/306026/exchange-2016-graceful-shutdown
question_id: 306026
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange 2016 graceful shutdown

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/306026/exchange-2016-graceful-shutdown (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello  

what is the correct way to shut down a exchange server (not dag) so that the mail queue get emptied?  

thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-10*

Hi @Efff dd   ,    

If you only want to clean the queue, you can use Remove-Message command.    

Or if you want to reboot the server, I think you can shutdown directly and restart, but it will cause a short break for sure.    

Also you could post more details to help me know your questions better.    

Thanks for your understanding & Have a good day!    

Best regards,    

Zhengqi Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
