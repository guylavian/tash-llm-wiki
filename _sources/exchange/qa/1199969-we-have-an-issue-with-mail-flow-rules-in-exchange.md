---
title: "We have an issue with Mail Flow rules in Exchange On-line."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1199969/we-have-an-issue-with-mail-flow-rules-in-exchange
question_id: 1199969
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# We have an issue with Mail Flow rules in Exchange On-line.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1199969/we-have-an-issue-with-mail-flow-rules-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,
We have an issue with Mail Flow rules in Exchange On-line. When we use the condition "Any Recipient" it works like we used the condition "The recipient". The condition defined in the rule is Any recipient > address includes any of these words and action is Delete the message without notifying anyone .
The rule works only for the recipient which has the defined word in the condition but other recipients gets the email delivered. Ideally this should delete the message for all the recipients as per the article. There is no other transport rule created. 
https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/conditions-and-exceptions#recipients
Check the screenshot

.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-12*

Hi，  

Sorry for the late reply.

In my repeated testing, there are two scenarios to prevent all recipients from receiving this message by matching the specified characters in the recipient's address:  

1.Check the message headers ，delete the message if 'To' message header matches the string 'mak'：  

2.Check the recipient address, if there is an address that matches 'mak', add a specified mailbox in the To box as a condition of the next rule：

Then delete the message based on the email address in the previous rule:  

   

Hope the above is helpful to you!

--  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-07*

Hi @ Ajaz Khan ,  

Can I understand that if a message contains a specified recipient, delete the message and prevent other recipients from receiving the message?

If this is the case, you can use "The To or CC Box Contains This person" as the condition. For example:  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
