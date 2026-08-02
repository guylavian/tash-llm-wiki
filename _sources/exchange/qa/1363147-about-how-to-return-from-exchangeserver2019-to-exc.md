---
title: "About how to return from ExchangeServer2019 to ExchangeServer2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1363147/about-how-to-return-from-exchangeserver2019-to-exc
question_id: 1363147
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
---
# About how to return from ExchangeServer2019 to ExchangeServer2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1363147/about-how-to-return-from-exchangeserver2019-to-exc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Thank you.

*The content written in Japanese was converted to English using a translation app, so we apologize if there are any mistranslations.

Since support for Exchange Server 2013 has ended, we are planning to switch to Exchange Server 2019.

I have created a procedure to move mailboxes from Exchange 2013 and switch to Exchange 2019.

I was able to confirm that the switch was successful in the test environment, but in case something goes wrong,

You need to create a procedure to get back to the original state.

*According to company rules, work permission will not be granted unless there is a procedure to return to the original state(´ཀ`)

Please let me know if there is a way to return to the original Exchange 2013 from the situation shown in the example below.

　　・Exchange2013(cu23) is WindowsServer2012R2, Exchange2019(cu12) is WindowsServer2019

　　・Moved all mailboxes from Exchange 2013 to Exchange 2019

　　・Exchange Server 2019 and Exchange Server 2013 need to use the same host name, so after moving the mailbox, uninstall Exchange 2013, exit from Active Directory, and shut down.

　　・Exchange2013 is backed up daily using Windows Server Backup.

I thought it would be possible to restore Exchange 2013 from Windows Server backup after uninstalling all Exchange from Active Directory, but it didn't work so I posted.

Thank you.

## Answers

_No answers on this thread._
