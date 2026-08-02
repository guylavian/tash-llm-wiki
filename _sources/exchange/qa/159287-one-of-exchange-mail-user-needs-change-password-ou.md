---
title: "One of Exchange mail user needs change password out of office network, what is the issue ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/159287/one-of-exchange-mail-user-needs-change-password-ou
question_id: 159287
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# One of Exchange mail user needs change password out of office network, what is the issue ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/159287/one-of-exchange-mail-user-needs-change-password-ou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Once of exchange mailbox user can login his mailbox from office but when works from home asked password change, seem like one user has this issue still, is there any solution for this ?

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-12*

@DM Kosala Randika Paranathala       

Does the user set to remember the credential and use the same computer in the office and at home?    

You can post the screenshot of the alert here, and don't forget to cover the personal information.    

Please also check, if the issue can be reproduced when login to the mailbox with OWA.    

Did the user try to change the password? Does it still ask to change the password even after changing the password?    

Please check the settings for Account options from ADUC.     

You can try to select "Password never expires", then check if the issue still occurs.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
