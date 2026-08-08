---
title: "Exchange Server 2003 Exchange Services stopped working."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2640171/exchange-server-2003-exchange-services-stopped-wor
question_id: 2640171
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 7
qa_tags: []
---
# Exchange Server 2003 Exchange Services stopped working.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2640171/exchange-server-2003-exchange-services-stopped-wor (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

I have a Windows SBS (2003), which is my Domain Controller & Exchange Server (2003) installed. Arrived on site this morning only to find out that Outlook wasn't opening. Checked the Small Business Server and
 it was up and running; however, most of the Exchange Services had stopped running:

I tried to restart the services but they kept failing. I even rebooted a couple of times hoping that I'll get lucky but luck wasn't on my side. Below is the error message and System's log I got during the failure:

Windows could not start the Microsoft Exchange Information Store on Local Computer. For more information, review the System Event Log. If this is a non-Microsoft service, contact the service vendor, and refer to service-specific error code 0.

Event System's Log:

Source: Service Control Manager

Category: None

Event ID: 7024

Description: 
The Microsoft Exchange Information Store service terminated with service-specific error 0 (0x0).

I also have a couple of Event Application's Log:

Source: MSExchangeIS

Category: General

Event ID: 5000

Description: Unable to initialize the Microsoft Exchange Information Store service. Failed to initialize Security - Error 0x80004005.

Source: MSExchangeSA

Category: Monitoring

Event ID: 9098

Description: The MAD Monitoring thread was unable to read its configuration from the DS, error '0x8007007e'

I have tried uninstalling and re-installing SMTP but it didn't help. I have also looked at a couple of threads but they seem not directly related to my issue.

When I tried to start the STMP's service, this is the error message I get: Could not start the Simple Mail Transfer Protocol (SMTP) service on Local Computer. Error 126: The specified module could not be found.

This is from the System Log:

Source: Service Control Manager

Category: None

Event ID: 7023

Description: 
The Simple Mail Transfer Protocol (SMTP) service terminated with the following error: The specified module could not be found.

The server worked great the days before and there were nothing done to the server that I can remembered that will trigger such. 

I do have TrendMicro Worry Free Business installed on the server but I also file/folders exclusion for the Exchange folder(s)/file(s). Had this setting for the past few years and nothing has changed. No update
 or anything was done since the last time it was running.

Although I have only included one or two errors, I did get messages and logs for all of the failed services.

Help!

## Answers

_No answers on this thread._
