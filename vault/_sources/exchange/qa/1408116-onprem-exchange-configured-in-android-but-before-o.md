---
title: "Onprem exchange configured in android but before one month no mail is not showing & archive folder is not showing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1408116/onprem-exchange-configured-in-android-but-before-o
question_id: 1408116
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Onprem exchange configured in android but before one month no mail is not showing & archive folder is not showing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1408116/onprem-exchange-configured-in-android-but-before-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Mail configured in Android but before one month no mail is not showing & archive folder is not showing.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-30*

Hello Md Nasir Uddin,

According to your description, in order to better understand and solve the problem, I would like to confirm the following issues:

-  Could "Before one month" be understood to mean that one month ago was normal, or does it mean something else?

-  When you mentioned "no mail is not showing" what do you mean?

-  What client are you using now? Outlook for Android or the mail app that comes with Android? Is there the problem with both?

-  whether this problem occurs in a single user or multiple users?

Please log in to OWA and see if everything is working there.

Besides, if the problem occurs with just one user, it is recommended that you reconfigure the account. Try deleting and re-adding your account to see if it works. If the issue is affecting all users, run Exchange Remote Connection Analyzer to test ActiveSync and see if it has any errors.

If there is any misunderstanding, please correct me.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
