---
title: "Messages to optusnet and bigpond could not be delivered"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5729390/messages-to-optusnet-and-bigpond-could-not-be-deli
question_id: 5729390
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Messages to optusnet and bigpond could not be delivered

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5729390/messages-to-optusnet-and-bigpond-could-not-be-deli (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Emails to optusnet and bigpond have been rejected even when replying an email from them. 

Original Message Headers

```
ARC-Seal: i=1; a=rsa-sha256; s=arcselector10001; d=microsoft.com; cv=none;
```

Error:550 5.7.1 Policy-DT510: Rejected content policy violationError:*550 5.7.1 Policy-DT52 Not going to happen - not now - not ever!***Error:**550 5.7.1 Policy-DT52 Not going to happen - not now - not ever!

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 1 · updated: 2026-01-21*

Hi @Shirley-0199

Thank you for posting your question in Microsoft Q&A. 

Based on my research, it appears that the NDR code 550 5.7.1 indicates that the recipient’s mail server has rejected your email due to its security or policy settings, meaning the message is not permitted to enter their system. 

To troubleshoot this, you should contact the recipient or their email administrator so they can review and correct the configuration on their side. Please reach out to the recipient (via phone, in person, etc.) and ask them to inform their email admin about the delivery issue. Their email administrator may need to adjust the mailbox or server settings to allow email from your address or domain. 

You can refer via: Fix NDR error 550 5.7.1 in Exchange Online - Exchange | Microsoft Learn 

I hope this helps.

Please understand that our initial reply may not always immediately resolve the issue. However, with your help and more detailed information, we can work together to find a solution.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
