---
title: "Exchange EWS RecurringMaster Recreate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/426251/exchange-ews-recurringmaster-recreate
question_id: 426251
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Exchange EWS RecurringMaster Recreate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/426251/exchange-ews-recurringmaster-recreate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello People.  

I am trying to get data from RecurringMaster and recreate it anywhere else.  

I got a problem with the AppointmentType of RecurringMaster.  

On the list of DeletedOccurrence and ModifiedOccurrence there no index in the series of the Appointment.  

there only "OriginalStartTime",  

When I try to do a filter appointment where OriginalStart is the same, the EWS return Error cannot filter by this Param.  

because these items are virtual (their master and the occurrences are virtuals)  

I must find a way to search the Virtual appointment with the OriginalStart, or if there any Appointment Index (the Occurrence index anything)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-09*

You could try using Export/Import of the master instance https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/exporting-and-importing-items-by-using-ews-in-exchange which would be a simple way of maintaining an exact duplicate. Otherwise for more complex sync using the recurrence blob is going to give you the most flexibility.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-09*

>When I try to do a filter appointment where OriginalStart is the same, the EWS return Error cannot filter by this Param.

What does you code look like ? . You can't use a SearchFilter restriction in conjunction with a CalendarView and the only way you would get Recurring meeting expansion to happen is if you use a CalendarView, so property what you doing isn't going to work the way your trying.

You can try paring the recurrence blob yourself to extract that detail https://learn.microsoft.com/en-us/office/client-developer/outlook/mapi/how-to-read-and-parse-a-recurrence-pattern
