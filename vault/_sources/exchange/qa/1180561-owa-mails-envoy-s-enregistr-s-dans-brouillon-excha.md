---
title: "OWA, mails envoyés enregistrés dans brouillon Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180561/owa-mails-envoy-s-enregistr-s-dans-brouillon-excha
question_id: 1180561
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# OWA, mails envoyés enregistrés dans brouillon Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180561/owa-mails-envoy-s-enregistr-s-dans-brouillon-excha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Bonjour , 

une fois envoye un email , toujour apres l'envoi , l'email enregiste sur brouillon

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-15*

Hi @Lahcen Idder  ,

Welcome to Microsoft Q&A forum.

Please note that currently Microsoft Q&A only support posting in English.

Could you please edit your question into English?  Then we can better understand the question and help you with this issue, thanks for your understanding.

The following is my understanding of your question and some suggestions.If I misunderstood your question, please feel free to correct me.

Have you confirmed with the recipient that recipient has received the email?

Does this issue affect all users in your organization, regardless of whether the email is sent to internal or external recipients?

 

In my experience, when sending a message in OWA, the message is first in the queue waiting to be sent, and it is normal for the message to be temporarily stored in the draft box.

If you confirm that the message was sent successfully, please run the get-messagetrackinglog command below for a problematic message and see if any clues can be found. 

You can share the output here for further investigation, but do remember to remove any personal information involved for privacy concerns.

```
Get-MessageTrackingLog -MessageSubject  -Sender  -Recipients  |select timestamp,EventID, Source,ConnectorID |sort-object Timestamp
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
