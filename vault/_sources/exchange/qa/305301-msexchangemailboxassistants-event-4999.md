---
title: "MSExchangeMailboxAssistants event 4999"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/305301/msexchangemailboxassistants-event-4999
question_id: 305301
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# MSExchangeMailboxAssistants event 4999

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/305301/msexchangemailboxassistants-event-4999 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

MS Windows 2019, MS Exchange 2019 CU7   

MS Windows and MS Exchange are installed with Russian. An attempt was made to switch the Windows interface to English, after which the MSExchangeMailboxAssistants service starts with an error and stops. I tried to return the Windows interface language back to Russian, but the service error remained.  

Thanks for any help.  

Error text:  

Watson report about to be sent for process id: 26956, with parameters: E12IIS, c-RTL-AMD64, 15.02.0721.008, MSExchangeMailboxAssistants, M.Exchange.Assistants, M.E.A.AssistantsRpcServer.RegisterAssistant, System.ArgumentException, 503a-dumptidset, 15.02.0721.008.  

ErrorReportingEnabled: False

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-10*

Hi @Максим Хирьянов   ,  

Are there any Exchange functions that are not working properly?  

Does any specific error pop up when you start the MS Exchange Mailbox Assistant service?  

Do you try to restart the Exchange server and MSExchange Mailbox Assistants service? If not, please try.  

1.1.Please run the following command to make sure that all required service are running:

```
Test-ServiceHealth
```

2.According to the error information, we could only know that Microsoft Exchange Assistants service failed. It may not be possible to know the root cause of the error, so please check if there are any related errors in the event log, or if there are any errors in Exchange. Please share the information with us, but please pay attention to covering your personal information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
