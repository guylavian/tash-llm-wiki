---
title: "Hello, my Exchange 2013 server does not load the edit setting page"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1275649/hello-my-exchange-2013-server-does-not-load-the-ed
question_id: 1275649
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Hello, my Exchange 2013 server does not load the edit setting page

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1275649/hello-my-exchange-2013-server-does-not-load-the-ed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When i want to modify group in my Exchange 2013 server, the edit page stays blank and after a time display's time out error. All other blades are opening in edit mode, just the groups one is affected.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-04*

Hi @miroslav atanasov  ,

To narrow down the issue, please clarify some questions and provide more information. Below are my suggestions:

 

1.Whether the account logged into the EAC has the correct admin role. What are the results of using another user to sign in?

 

2.If you use the command Get-DistributionGroup in the Exchange Management shell, what happens and whether it is displayed as follows: 

![A screen shot of a computer program

Description automatically generated with low confidence](/api/attachments/5bc76088-9a9c-4bf6-8145-712d842f3292?platform=QnA)

3.Open IIS Manager, find the Bingdings information of the Exchange back end, and check if the SSL certificate is correct for MS Exchange.

![A screenshot of a computer

Description automatically generated](/api/attachments/a4516f69-d969-4849-a7d1-90b7fc899a35?platform=QnA)

4.Finally, it is recommended to restart Exchange related services.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-04*

It might be that there is an SSL Certificate Binding Issue.
