---
title: "exchange 2019 unable to send / receive email after shutdown exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1352093/exchange-2019-unable-to-send-receive-email-after-s
question_id: 1352093
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange 2019 unable to send / receive email after shutdown exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1352093/exchange-2019-unable-to-send-receive-email-after-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

As part of our migration plan, we have been operating both an Exchange 2019 server and an Exchange 2013 server in coexistence mode. We successfully migrated all user mailboxes to the Exchange 2019 server, marking a significant milestone in our migration process.

To ensure a smooth transition and eventual decommissioning of the Exchange 2013 server, we conducted through testing. However, during the testing phase, we encountered an unexpected issue. When we are shutting down the Exchange 2013 server, we noticed that all users were unable to send and receive emails from internal and external.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-13*

This is similar issue with someone posted in the forum.

Please refer the link below, hope this will help you

https://community.spiceworks.com/topic/2246424-exchange-2013-to-exchange-2016-upgrade-not-sending-e-mail

## Answer (community) — community member

*upvotes: 0 · updated: 2023-08-29*

we are using default exch1.domain.com for exchange server 2013 and exch2.domain.com for exchange server 2019 but this issue happen to webmail also escalate to microsoft support already the issue still haven't resolved yet.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-08-28*

Check your mail.domain.com internal DNS record. See if the mail.domain.com is still pointing to the old server or not.

Ensure the Exchange 2019 server does not act as a backup server for the Exchange 2013 server.

For more insight - Decommission Exchange Server after Migration

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-08-28*

Hi @AhWei  

Is the DNS pointing correctly? Did you reconfigure the connector? I see this in best practice:  

Best Practices for Migrating from Exchange Server 2013 to Exchange Server 2019

Also, you could check the other steps in the best practice to see if you missed something.

By the way, is this a question you posted earlier?

https://learn.microsoft.com/en-us/answers/questions/1305974/all-users-unable-to-send-and-receive-email-after-s

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
