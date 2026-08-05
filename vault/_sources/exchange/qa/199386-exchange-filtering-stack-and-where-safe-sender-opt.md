---
title: "Exchange filtering stack and where safe sender options are processed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/199386/exchange-filtering-stack-and-where-safe-sender-opt
question_id: 199386
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange filtering stack and where safe sender options are processed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/199386/exchange-filtering-stack-and-where-safe-sender-opt (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In the article https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/create-safe-sender-lists-in-office-365, different methods of creating safe senders are described:    

-  Mail flow rules    

-  Outlook Safe Senders    

-  IP Allow List (connection filtering)    

-  Allowed sender lists or allowed domain lists (anti-spam policies)    

The details for each of these methods suggest that different parts of the Exchange filtering stack are bypassed depending on each method. It is not clear which parts of the stack are bypassed, however, and this has made it difficult to troubleshoot messages that are not making it to our users' inbox.    

Is there a diagram, like this one from Nakivo https://www.nakivo.com/blog/wp-content/uploads/2020/05/The-working-principle-of-Exchange-Online-Protection.png, that includes where each safe sender method is processed?    

To be more specific to the problem I'm working on, a customer's vendor uses Sendgrid to send critical email notifications. Unfortunately these messages send from shared IP addresses and one of them is on a spam list and gets blocked at the Connection Filtering level (the block action don't show up in Mail Trace). I've added the sender's email address to allowed senders list in EOP spam policies but am still receiving reports that messages are not being received. Does this not bypass connection filtering?    

Thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

Hi @spencer   ,    

-  According to the Microsoft article, through "IP Block List" you can block all emails from this IP address, all incoming messages are rejected, are not marked as spam, and no additional filtering occurs. So when it's not possible to use one of the other options to block a sender, only then should you use the IP Block List in the connection filter policy.    

-  For the working flow of Exchange Online Protection, you can refer to the screenshot below, any message that passes all of these protection layers successfully is delivered to the recipient.    

For the working principle of each part, you can refer to: Exchange Online Protection overview    

    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-15*

It does not. Connection filtering will block the IP before any other processing and it wont be ever seen by those other methods    

https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/configure-the-connection-filter-policy?view=o365-worldwide
