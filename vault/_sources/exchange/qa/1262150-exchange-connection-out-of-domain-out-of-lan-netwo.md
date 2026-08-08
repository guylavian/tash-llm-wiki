---
title: "Exchange connection out of domain / out of lan networks"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1262150/exchange-connection-out-of-domain-out-of-lan-netwo
question_id: 1262150
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange connection out of domain / out of lan networks

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1262150/exchange-connection-out-of-domain-out-of-lan-netwo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning,

Here is the problem:

We have an Exchange 2013 solution and an Exchange 2007 (I don't know what it's for but it will be decommissioned soon, at the moment if I turn it off no more mail) on premise, recently, we have encountered the following incidents :

-  Shared ball that no longer goes back to the delegates

-  Impossible to configure an absence message via outlook, only from the OWA

-  Unable to use exchange outside domain or on a third-party domain on outlook 2013/2016/2019 --> Error message: Sorry.. Oulook could not configure your account because we encountered a problem. A link to: https://go.microsoft.com/fwlink/?linkid=858234 which doesn't explain much

And this for a month, before that everything was working perfectly.

Besides, my bal configuration test carried out successfully on:

-  iphone mail application (receiving and sending mail ok)

-  outlook mobile application (reception and sending of mail ok)

-  default mail application on win 10/11

No problem so far except on an workstation with outlook.

Microsoft connectivity test (https://testconnectivity.microsoft.com/tests/) completed successfully.

Check Outlook anywhere Ok

I dry no configuration parameter has been changed.

Thank you in advance for your clarifications.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-04-28*

Hi @droido  

Please run Test E-mail autoconfiguration via Outlook client, and check the results under the Log tag.

Example:

Would it fail? 

If yes please post a screenshot or in text of the details.

(Don't forget to hide your personal information in it, for example domain name)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
