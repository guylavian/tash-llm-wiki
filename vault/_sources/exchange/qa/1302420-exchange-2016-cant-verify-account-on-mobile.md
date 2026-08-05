---
title: "exchange 2016 can't verify account on mobile."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1302420/exchange-2016-cant-verify-account-on-mobile
question_id: 1302420
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange 2016 can't verify account on mobile.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1302420/exchange-2016-cant-verify-account-on-mobile (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently I have the problem that we are using exchange online, recently we migrated some of those users to exchange onprem. Initially they can use mail on normal mobile, recently those users do not receive mail on mobile anymore. reinstalling exchange on mobile, exchange failed to authenticate user, please help me.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-06-12*

Hi @Pham Tien Dung  ,

According to your description, please clarify some question to help us narrow down the issue.

1.Please try to log on OWA and see if there is still showing mobile devices? 

2.Have you change the password of those accounts recently?

3.Is the mobile device connected to internal WiFi? If so, try using mobile data.

Below are some suggestions:

1.Confirm that ActiveSync is enabled for the user in EAC. Mobile device can't connect via ActiveSync - Exchange | Microsoft Learn

2.Confirm that the user's mobile device isn't in the list of quarantined devices.

3.Check the permissions of the account in ADUC, compare the permissions of the problematic account with other normal accounts, make sure enable inheritance, then login your account on the mobile device again to check whether the issue still exists:

4.Change the password and reconfigure the mobile account.

Hope the above can help.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
