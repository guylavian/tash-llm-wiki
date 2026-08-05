---
title: "Change fonts in Exchange disclaimer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2285014/change-fonts-in-exchange-disclaimer
question_id: 2285014
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Change fonts in Exchange disclaimer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2285014/change-fonts-in-exchange-disclaimer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Need to change font and bold it for part of the disclaimer

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-06-18*

Hi @Belle Fiederer  

Thank you for reaching out regarding updating the font and bold formatting in your Exchange disclaimer. I'm happy to guide you through the steps to achieve this using mail flow rules in the Exchange Admin Center. 

Follow these steps to set up and format your disclaimer in the Exchange Admin Center: 

To edit an existing rule and customize your disclaimer: 

-  Log into the Exchange Admin Center with an account that has Exchange Administrator or Global Administrator permissions: https://admin.exchange.microsoft.com 

-  Navigate to Mail flow > Rules, find your existing disclaimer rule, and click Edit. 

-  Locate the action that applies the disclaimer (e.g., “Apply a disclaimer to the message”). 

-  Update the disclaimer text using HTML tags to set the font and bold formatting. For example: 

```
This email contains confidential information. Do not share it.
```

-  Save the changes and test by sending an email to verify the formatting. 

To create a new rule if you don’t have one yet: 

-  Log into the Exchange Admin Center. 

-  Go to Mail flow > Rules and click +Add a rule then select Apply disclaimers. 

-  Set conditions such as Sender is inside the organization and Recipient is outside the organization. 

-  Under Do the following, choose Append the disclaimer (to add it to the end of emails) or Prepend the disclaimer (to add it to the beginning). 

-  Click the Enter text... link to input your disclaimer with HTML formatting. For example, if your disclaimer is:   

This email and any attachments are confidential. Unauthorized use is strictly prohibited.   

and you want “Unauthorized use is strictly prohibited.” to be bold and in Times New Roman font size 10pt, enter: 

```
This email and any attachments are confidential. Unauthorized use is strictly prohibited.
```

Choose a Fallback Option: 

After entering your HTML, click "Select one..." for the fallback action. This determines what happens if the disclaimer can't be added (e.g., if the original email is encrypted).  

-  Wrap: recommended — adds the original message as an attachment with the disclaimer 

-  Ignore: sends the message without the disclaimer 

-  Reject: prevents sending and notifies the sender 

Review and Finalize Rule Settings: 

-  Review and finalize the rule settings (priority, audit, mode). Set the mode to Enforce to activate immediately or start with test modes if preferred. 

-  Click Next and then Finish to create the rule. 

After that, send a test email from an internal account to an external recipient and confirm the disclaimer appears as intended, including formatting. Because email clients can display HTML differently, thorough testing is important. 

Should you encounter any difficulties or if the disclaimer isn't displaying correctly after you've made these changes, please don't hesitate to reply to this email. Providing the exact text of your desired disclaimer and a description of how you'd like it to look can help me craft the precise HTML code for you. 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
