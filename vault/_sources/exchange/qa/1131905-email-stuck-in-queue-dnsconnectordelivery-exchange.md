---
title: "Email Stuck in Queue DnsConnectorDelivery Exchange Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1131905/email-stuck-in-queue-dnsconnectordelivery-exchange
question_id: 1131905
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Email Stuck in Queue DnsConnectorDelivery Exchange Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1131905/email-stuck-in-queue-dnsconnectordelivery-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

We have an exchange server 2016 that we have configured hybrid. originally all mail flows were running normally, but we have a newly occurring issue where emails are stuck in the queue DnsConnectorDelivery. Here's capture for the details:    

    

    

Really appreciate for your answer!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-29*

Hi @Arief Hardiansyah   ，    

Sorry for the late reply.    

Please refer to the steps in the follow link to check if your server's IP address is blacklisted. If so, remove it and then adding it to the whitelist in Exchange online.     

https://alittleofnothing.wordpress.com/2014/09/22/exchange-online-office-365-hybrid-configuration-connectivity-problems-must-issue-a-starttls-command-first/    

(Note:Microsoft provides third-party contact information to help you find additional information about this topic. This contact information may change without notice. Microsoft does not guarantee the accuracy of third-party contact information.)    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
