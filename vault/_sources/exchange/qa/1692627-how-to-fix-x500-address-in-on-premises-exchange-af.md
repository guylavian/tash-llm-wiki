---
title: "How to fix x500 address in on-premises exchange after the migration?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1692627/how-to-fix-x500-address-in-on-premises-exchange-af
question_id: 1692627
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to fix x500 address in on-premises exchange after the migration?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1692627/how-to-fix-x500-address-in-on-premises-exchange-af (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have hybrid exchange setup. After the migration, the new accounts created have different x500 address format which has caused issue using printer services.

The emails are bouncing back with error:

Remote server returned '554 5.4.1 <ML1PEPF00011309.mail.protection.outlook.com #5.4.1 smtp;550 5.4.1 Recipient address rejected: Access denied. [ML1PEPF00011309.ausprd01.prod.outlook.com 2024-06-05T01:29:56.833Z 08DC84E0261C2B13]>

No issue with the migrated user though.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-07*

Hi @Suman Shrestha,

Thank you for posting to Microsoft Community.

Based on your description, I know there are an issue you got a 5.4.1 error when you send email via the account created after migrated.

The reason why the issue occurred usually is the email server don't accept email from the sender's domain or DNS misconfiguration.

 Please check the status of the domain in the Exchange admin center (EAC) by following these steps:

-  In the Microsoft 365 admin center, click Admin > Exchange.

-  Click Mail flow > Accepted domains.

-  Verify that your domain is listed and verify the Domain Type value for the domain. Typically, the value should be Authoritative. However, if you have properly configured a shared domain, the value might be Internal Relay.

For more information, you could refer to Fix NDR error code 550 5.4.1 in Exchange Online - Exchange | Microsoft Learn.

Also, please ensure DBEB (Directory Based Edge Blocking) is disable for your domain.

Hope it helps and if there is anything else I could help with, please let me know.
