---
title: "Help with Creating Transport Rule for Calendar Invites"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2238450/help-with-creating-transport-rule-for-calendar-inv
question_id: 2238450
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Help with Creating Transport Rule for Calendar Invites

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2238450/help-with-creating-transport-rule-for-calendar-inv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Assistance is needed in setting up a transport rule to apply a specific disclaimer for outgoing calendar invites, similar to the one shown in the attached image. A transport rule has been created in Exchange Online, but it does not display the intended disclaimer when sending calendar invites. Additionally, the goal is to implement this disclaimer for Teams invites as well. Currently, there is a default disclaimer for every email being sent, and the new disclaimer appears below the default one, causing them to mix. 

It's important that this disclaimer is only applied to outgoing invites, not for regular email messages.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-25*

Hi @Mohana Reddy  ,

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, you are experiencing an issue with two disclaimers in the email after adding a disclaimer to a calendar invitation.

-  If you want the disclaimer to apply only to outgoing invitations. Please select Calendaring as the message type when setting up your transfer rules. 

 

-  You are currently seeing two disclaimers because you have two transfer rules applied to your email at the same time. You can set the default disclaimer rule as below in the except if of the default disclaimer rule. Or adjust it appropriately according to your actual needs.

 

Here is my test flow. (The same is available in teams, so I won't repeat it here)

-  create a transmission rule for calendar invitation. 

 

-  Create a transfer rule for regular emails. 

 

-  Send the calendar invitation with the following result.

-  The result of sending a regular email is as follows.

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.
