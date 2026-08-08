---
title: "One outlook email account in Exchange online doesnt get verification email"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2261959/one-outlook-email-account-in-exchange-online-doesn
question_id: 2261959
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# One outlook email account in Exchange online doesnt get verification email

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2261959/one-outlook-email-account-in-exchange-online-doesn (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

why is one outlook user not receiving email verifications.  They are receiving internal as well as external emails but cannot get email verifications.  The emails show in the applications as leaving their servers but a message trace in Exchange Admin Center shows the verification emails as never arriving,  not in quarantine or spam or anywhere.  How can they possibly get lost like this?  We verified on backscatterer.org that neither our ip address nor her email is listed in on backscatterer.org

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-29*

Hi @Anonymous  ,

Thank you for posting your question in the Microsoft Q&A forum.

Do other user mailboxes have the same issue that cannot receive this kind of verification email?  

In general, it may need to wait for some time to generate message trace logs. If you still cannot get any message trace logs for this specific verification email even after several hours, it seems that this email is not received by O365.

If so, you may contact the application side for further investigation:

-  Please help to confirm if the verification email could be sent to any gateway or any third-party scan server, before sending to O365.

-  If the email generated from application will be sent to O365 directly, please check if any SMTP logs from application side to confirm the application side has setup SMTP session with EOP and transfer email data successfully.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
