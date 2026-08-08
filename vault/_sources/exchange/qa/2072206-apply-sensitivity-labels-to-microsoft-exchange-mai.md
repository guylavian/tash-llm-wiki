---
title: "Apply Sensitivity Labels to Microsoft Exchange Mail via .NET core code."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2072206/apply-sensitivity-labels-to-microsoft-exchange-mai
question_id: 2072206
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Apply Sensitivity Labels to Microsoft Exchange Mail via .NET core code.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2072206/apply-sensitivity-labels-to-microsoft-exchange-mai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I would like to apply sensitivity labels to emails programmatically. I have successfully obtained the email ID (message ID) and sensitivity label ID using Graph API in .NET Core Application C#. 

However, I cannot find an endpoint within the Microsoft Graph API or any other way via code that allows me to apply the sensitivity label directly to the email.

I have necessary APP Permission and App details like tenant id, client id etc.

I don't want to download email file and apply sensitivity label like any other file. Just like graph API support updating content and subject of exchange email. Can we apply labels as well.

Thank you in advance for your help.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-19*

Hi @Amit Singh Rawat

You can apply sensitivity labels to messages by creating single-value properties. Sensitivity labels can be assigned by extending the PidTagSensitivity attribute, but the label values can only be values for three sensitivity levels. See this article for details.

To set extended properties, see Endpoints.

Hope this helps.

If the reply is helpful, please click Accept Answer and kindly upvote it. If you have additional questions about this answer, please click Comment.
