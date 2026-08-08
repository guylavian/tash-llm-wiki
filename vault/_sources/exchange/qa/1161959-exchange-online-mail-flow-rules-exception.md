---
title: "Exchange online mail flow rules exception"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161959/exchange-online-mail-flow-rules-exception
question_id: 1161959
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange online mail flow rules exception

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161959/exchange-online-mail-flow-rules-exception (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I have setup a mail flow rule to add a banner to emails for external email addresses to remind staff this is external and be careful about attachments and links. 

this works fine however I would like to exclude emails sent to our support address as this goes into a 3rd party system that has it own security and rules but I have not managed to find a way of doing this. 

at the moment I have a list of domains that are excluded from the rule and that works fine, I have also added an exception that says if the recipient contains any of these words then exclude and added the support address but that has not worked. 

does anyone know if that is possible?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-19*

unfortunately the address in question is a distribution group so it will not let me do that. 

the question now does that needs to be a distribution group as there is only one member, so all it does it redirect the email to a different address. 

is there a better way to forward emails sent to the support address to an external address?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-19*

Hi @Mark Dagley  ，

The “Includes these words” parameter need include exactly the specified word in the email address, and identify words with spaces.

According to your needs, you can refer to the screenshot below to set exceptions：

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-18*

here is the rule 

Rule description

Apply this rule if Is received from 'Outside the organization 

Do the following Prepend the message with the disclaimer HTML for the disclaimer banner 

If the disclaimer can't be applied, attach the message to a new disclaimer message. and set message header 'External' with the value 'external'

Except if

 Includes these words in the recipient's address '******@ourdomainname.co.uk'

or 

Includes these words in the sender's address 'Microsoft.com' or 'linkedin.com' ....
