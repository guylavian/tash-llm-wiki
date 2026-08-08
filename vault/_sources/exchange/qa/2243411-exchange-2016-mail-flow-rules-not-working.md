---
title: "Exchange 2016 Mail flow rules not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2243411/exchange-2016-mail-flow-rules-not-working
question_id: 2243411
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange 2016 Mail flow rules not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2243411/exchange-2016-mail-flow-rules-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Mail Flow rule "If the message is from ******@xxx.com"  "set message header 'Sensitivity' with the value 'company-confidential'"

Rule Stopped working. Created new rule, it works when sending from Outlook client. It does not work when email is generated from an application. Message header does not get "set" per the rule.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-03*

Hi @Andre Inge  ,

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, the issue you are experiencing is Mail Flow Rules are working when sent from the Outlook client, but not when generated from the application.

There are a few suggestions below that I hope will help you.

-  Please check the sender of the email generated from the application. The sender address used by the application to send emails may not be exactly the same as the one set in the rule. Please check if the sender in MessageTrackingLog matches the one in the rule. This can be obtained using the Get- MessageTrackingLog command. More details can be found in the documentation: Get-MessageTrackingLog (ExchangePowerShell) | Microsoft Learn

-  Some special message types may not be able to apply the rule, check the type of email generated from the application. Refer to the documentation for more details: Mail flow rules in Exchange Server | Microsoft Learn

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-04-02*

use instead:

The sender address includes any of these words "******@xxx.com", then set the message header...
