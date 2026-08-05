---
title: "Remove-CalendarEvents cmdlet on Exchange Online throws exception: \"String was not recognized as a valid DateTime\"!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/347484/remove-calendarevents-cmdlet-on-exchange-online-th
question_id: 347484
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-ms-graph", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Remove-CalendarEvents cmdlet on Exchange Online throws exception: "String was not recognized as a valid DateTime"!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/347484/remove-calendarevents-cmdlet-on-exchange-online-th (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Seems that problem appears only for Remove-CalendarEvents cmdlet when we set its QueryStartDate parameter.  

We have tested Set-Mailbox with StartDateForRetentionHold and EndDateForRetentionHold parameters and Set-MailboxAutoReplyConfiguration with -StartTime and -EndTime and these cmdlets worked just fine. For all cmdlets we have specified dates as object of DateTime type but error appears only for Remove-CalendarEvents.  

Problem happens on different time formats, we have tested United Kingdom(dd/MM/yyyy) and Unkrainian(dd.MM.yyyy) date formats that specified in system settings and it seems that problem appears when day part is in the first place. Everything is ok when we using United Sates(M/d/yyyy) format in system settings.  

We tried creating dates in different ways:  

$date = Get-Date -Date "27.08.2020"  

$date = [System.DateTime]::Parse("27.08.2020")  

We even tried to specify the kind of days created, but that didn't change anything.  

Full error:  

Error on proxy command 'Remove-CalendarEvents -Identity:'' -CancelOrganizedMeetings:$True  

-Confirm:$False -QueryStartDate:'27/08/2020 00:00:00' -QueryWindowInDays:'1825'' to server  

VI1PR06MB5152.eurprd06.prod.outlook.com: Server version 15.20.3999.0000, Proxy method PSWS:  

Cmdlet error with following error message:  

System.Management.Automation.ParentContainsErrorRecordException: Cannot process argument transformation on parameter  

'QueryStartDate'. Cannot convert value "27/08/2020 00:00:00" to type "Microsoft.Exchange.ExchangeSystem.ExDateTime". Error:  

"String was not recognized as a valid DateTime.".  

Environment:  

PSVersion: 5.1.17763.1490  

PSEdition: Desktop  

PSCompatibleVersions: {1.0, 2.0, 3.0, 4.0...}  

BuildVersion: 10.0.17763.1490  

CLRVersion: 4.0.30319.42000  

WSManStackVersion: 3.0  

PSRemotingProtocolVersion: 2.3  

SerializationVersion: 1.1.0.1

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-07*

Hi，    

Try '08/27/2020 00:00:00' or '2020/08/27 00:00:00' instead of '27/08/2020 00:00:00'. Or you can call the ParseExact method    

```
$date = [DateTime]::ParseExact('27/08/2020 00:00:00','dd/MM/yyyy hh:mm:ss',[Globalization.CultureInfo]::CreateSpecificCulture('en-GB'))
```

Best Regards,    

Ian Xue    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
