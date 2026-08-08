---
title: "Exchange 2010 delay problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/310088/exchange-2010-delay-problem
question_id: 310088
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2010 delay problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/310088/exchange-2010-delay-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Exchange 2010 SP3 Rollup Pack 22 and we have hybrid structure on servers. Some mails are too delay from outside customer. Example header in the link below. https://we.tl/t-Dei5e6P4Mg How can i solution? Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-15*

We solved the problem. https://www.nartac.com/Products/IISCrypto/ use the tool and change best practise TLS settings.  

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hi @DCS CUSTOMS   ，  

Do you mean that only email from specific senders will be delay? Or it happens randomly to all senders?  

Did you change any setting of Exchange server before this issue occurred?  

How long will the mail be delayed?  

I click the link you provided, and it will be redirected to a third-party website, I can’t get more information.

1.When you received the delay email, you could analyze the email headers through ExRCA, and the results will show the specific delays. We can see if the delay occurred before or after reaching Exchange.  

Message Header Analyzer: mha.azurewebsites.net  

  

2.You could run the following command to check the process and time of mail transmission in Exchange server.

```
Get-MessageTrackingLog -Start "<>" -End "<>" -Sender "<>" -MessageSubject <>
```

For more information: Get-MessageTrackingLog

In addition, Exchange Server 2010 reached its end of support on October 13, 2020. Please upgrade the Exchange server to a higher version as soon as possible.  

For more information: Exchange 2010 end of support roadmap

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
