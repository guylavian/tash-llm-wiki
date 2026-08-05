---
title: "How to add custom MIME header in email in Exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2148002/how-to-add-custom-mime-header-in-email-in-exchange
question_id: 2148002
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to add custom MIME header in email in Exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2148002/how-to-add-custom-mime-header-in-email-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, We want to know if we can add a custom MIME header in email in Exchange online messages so if we receive the email in Bcc we can redirect that email to a specific mailbox. It is to use SAP application with EXO. SAP has suggested the following article but we can not update the configuration file as we can do in exchange servers. Any suggestion would be valuable.

https://community.sap.com/t5/crm-and-cx-blogs-by-sap/how-to-set-up-a-custom-mime-header-for-your-email-server/ba-p/13579042

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-17*

Hi, @Mohd Ajaz Khan  

As mentioned in the article you provided, in Exchange Online this may involve creating mail flow rules. To do this, you need to go to the Exchange Admin Center as an administrator, navigate to Mail Flow, and modify your mail flow rules as shown below. 

Unfortunately, in Exchange Online, mail flow rules can't detect Bcc recipients directly. This is because the Bcc recipient's information is hidden during the mail transmission process and cannot be accessed by the mail flow rules. 

Maybe that's what you're looking for. Configure S/MIME in Exchange Online | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
