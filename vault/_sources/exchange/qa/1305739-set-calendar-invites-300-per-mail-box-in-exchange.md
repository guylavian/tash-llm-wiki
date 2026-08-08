---
title: "Set calendar invites 300 per mail box in exchange server 2019 using script"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1305739/set-calendar-invites-300-per-mail-box-in-exchange
question_id: 1305739
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-powershell"]
---
# Set calendar invites 300 per mail box in exchange server 2019 using script

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1305739/set-calendar-invites-300-per-mail-box-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team. I want to Set calendar invites, 300 per mailbox in exchange server 2019 by using script only. I think we can do this by using a Powershell script, or is there any other way to do this using script only? Please help me out as soon as possible…If possible then please help to provide the script!!!  

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-15*

Hello there,

Use the Set-MailboxCalendarConfiguration cmdlet to modify mailbox calendar settings for Outlook on the web. This affects how the user's calendar looks and how reminders work in Outlook on the web.

 $ol = New-Object -ComObject Outlook.Application

$meeting = $ol.CreateItem('olAppointmentItem')

$meeting.Subject = 'Test # 4'

$meeting.Body = 'Let''s have a meeting'

$meeting.Location = 'Virtual'

$meeting.ReminderSet = $true

$meeting.Importance = 1

$meeting.MeetingStatus = [Microsoft.Office.Interop.Outlook.OlMeetingStatus]::olMeeting

$meeting.Recipients.Add('******@contoso.net')

$meeting.Recipients.Add('******@contoso.net')

$meeting.ReminderMinutesBeforeStart = 15

$meeting.Start = [datetime]::Today.Adddays(1)

$meeting.Duration = 30

$meeting.Send()  

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer--
