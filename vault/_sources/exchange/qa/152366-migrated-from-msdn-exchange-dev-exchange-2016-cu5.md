---
title: "[Migrated from MSDN Exchange Dev] Exchange 2016 cu5 - cu18: seriously went wrong"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/152366/migrated-from-msdn-exchange-dev-exchange-2016-cu5
question_id: 152366
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Exchange 2016 cu5 - cu18: seriously went wrong

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/152366/migrated-from-msdn-exchange-dev-exchange-2016-cu5 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

It would be a very long story if I'll try to explain the whole situation. But I do it with some words.

1/ Situation: exchange 2016 cu5. Goal: update to cu18. 1 forest, 3 domains. It went totally wrong. We opened a case at Microsoft for 600€ but after 3 days (they claim to answer within 2 hours) and 9 calls from myself (they never called me back) I withdraw the case and asked the money back. They just didn't want to help (unbelievable). Money back=ok.  

So during the update we got some errors I can't remember but we restored a snapshot and the exchange 2016 is working again with some little minor issues.

That's the story, now the question.

2/ When we search for our system mailboxes with Set-ADServerSettings -ViewEntireForest $true; Get-Mailbox -Arbitration we get 4 of them: systemmailbox 1f05..., federationmailbox 4c1f4d8...... systemmailbox e0dc1c29...... migrationmailbox 8f3e7716....

So if I am correct for Exchange 2016 cu5 there have to be 5 of them. For cu18 there would be 7 required of them.

To recreate them I have to execute: setup.exe /iaccept..... /prepareAD. (executing with the setup finded in the cu18). But when doing that the system is saying:

a reboot from a previous installation is pending. Please restart and rerun setup.

After a restart everything stays the same. So it looks like a loop. Any executable tips? executable= the Exchange server is a production server. In normal circumstances I cannot reboot during working hours and after those hours I can only reboot during the night.

Source link: https://social.msdn.microsoft.com/Forums/office/en-US/d088fc96-d4f5-4137-b8a4-139a5ea8fee6/exchange-2016-cu5-cu18-seriously-went-wrong?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-05*

First, Exchange 2016 CU8 and later only have 5 system mailboxes : Recreate missing arbitration mailboxes    

    

Based on your description, the current problem is "a reboot from a previous installation is pending. Please restart and rerun setup."    

This issue is caused by previous installation doesn't applied, try to check the update of Windows server and restart computer three to four times. If this error still exists, you can follow this article to modify registry on your Exchange server and retry to install again.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
