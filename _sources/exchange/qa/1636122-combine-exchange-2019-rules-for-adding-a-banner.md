---
title: "Combine Exchange 2019 rules for adding a banner"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1636122/combine-exchange-2019-rules-for-adding-a-banner
question_id: 1636122
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Combine Exchange 2019 rules for adding a banner

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1636122/combine-exchange-2019-rules-for-adding-a-banner (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

All,

To add a banner to our incoming email from out of our organization we use a rule with HTML code in it.

So far so good, this works.

What we also want to do is make exceptions for incoming email that's multipart-signed and/or multipart encrypted.

For both i can only create separate rules and not combine them.

The problem is, that when i create seperate rules, the second rule makes that the banner is placed twice within the email message.

Anyone have an idea how i can solve this or how to combine both rules into one?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-29*

I couldn't combine the 2 because as an exception i can only choose for Encrypted or Signed as the message type.

So i had to make 2 separate rules.

For management purposes i would only like to use one as you can imagine.

I added screenshots of one of the rules. The other is the same except for the message type

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-29*

Hello @Bakker, Ron, 

Based on your problem description, I would like to ask if your two rules are set up according to 1. Add a banner if the sender is from an external organization. 2. Add a banner if the sender is from an external organization, except for incoming emails with multipart signatures and/or multipart encryption . If the rules are set up in this way, then the rules for adding a banner will indeed be duplicated, and your requirements will only need to be set up in accordance with the second rule, as shown in the screenshot. If not, please provide how it was configured and I will advise you!
