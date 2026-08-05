---
title: "Exchange Online Forwarding: Loss of Per-Recipient Context for Multi-Bcc Emails When Relaying via External Connector"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2261609/exchange-online-forwarding-loss-of-per-recipient-c
question_id: 2261609
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online Forwarding: Loss of Per-Recipient Context for Multi-Bcc Emails When Relaying via External Connector

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2261609/exchange-online-forwarding-loss-of-per-recipient-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are forwarding all incoming emails from Exchange Online to an external server for DLP scanning, and then relaying the emails back to Exchange for final delivery to recipients.

For To and Cc recipients, Exchange forwards a single copy of the email, with all intended recipients correctly visible in the headers.

For single Bcc recipients, Exchange also forwards a single copy, and the intended Bcc recipient can still be identified via headers (such as To, Bcc, or other available metadata).

However, when there are multiple Bcc recipients, Exchange sends only a single shared copy, and in this case, there is no header or envelope information available to identify individual Bcc recipients on our external server.

We have already configured connectors, mail flow rules, and external routing successfully. Everything works correctly except for emails with multiple Bcc recipients because:

-  No separate copy is generated per Bcc recipient.

-  No header (such as X-Original-To, X-GM-Original-To, or equivalent) is available to help identify the original Bcc recipient.

-  As a result, we cannot correctly determine the intended individual recipient for multi-Bcc emails after scanning.  

Please advise : 

-  Is there a way to enforce separate copies for each Bcc recipient during forwarding (similar to how Gmail handles it)?

-  Alternatively, is there a way to add a header (for example, X-Original-To or similar) containing the original recipient address for each Bcc recipient during forwarding?

-  Are there any available settings (e.g., via Purview, Journaling, or Transport Rules) to preserve original recipient information in multi-Bcc scenarios?

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-28*

Hi Anish,

Thank you for posting your question in the Microsoft Q&A forum.

Based on my research, it’s by designed that and we cannot find or add any message header to see BCC addresses.

You could try to create a message trace and generate extended report to check message processing for each stage, you may find all BCC recipients from the extended report.

Please can check this article for more information about Extended report:

Extended reports

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
