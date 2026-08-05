---
title: "Auditing Transport Rules 2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2152821/auditing-transport-rules-2
question_id: 2152821
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Auditing Transport Rules 2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2152821/auditing-transport-rules-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

I've already asked the question on auditing tansport rules but I still don' understand the following:

Suppose there's a rule that appends the signature when the mail is being sent from IT department:

..and my goal is to find WHICH MESSAGES THIS RULE HAS BEEN APPLIED TO.

The method described in the previous post - 

(Get-TransportService | Get-MessageTrackingLog -MessageSubject "TestEmail" -Start "04/01/2022 09:00:00" -End "04/08/2022 18:00:00" -Source Agent).EventData.value | where{$_ -like "RuleID" -and $_ -like "Action="}

...answers another question:  HAS ANY RULE BEEN APPLIED TO THIS PARICLAR MESSAGE?

Here's my test: I send two messages for which the rule must be fired:

The rule does really fire up and I want to find those messages in the logs:

[PS] C:\Windows\system32>(Get-TransportService | Get-MessageTrackingLog -Start "01/27/2024 09:00:00" -End "01/28/2025 21:00:00" -Source Agent).EventData.value | where{$_ -like "f94242a7-ebe6-46f4-9612-ec4745b26353**and $_ -like "Action="}

There're two issues here:

-  each message has 3 or 2 lines in the command's otput so it's not clear how many mssages were procssed by the rule

-  there're no message ID or subject to identify th message

Is there a way to solve these problems?

Regards,

Michael

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-26*

P.S. one more test to illustrate the strangeness of the rules:

I created a new rule that fires up for messages sent to SharedMB @ contoso1.net...

 

...and sent the single message to that address. Nevertheless, three messages were returned by the following commands:

$startDate = "02/26/2025 09:00:00"

$endDate = "02/26/2025 21:00:00"

$ruleID = "7366001e-f754-4330-9211-1bb412b6b159"

Get-TransportService | Get-MessageTrackingLog -Start $startDate -End $endDate -Source Agent |

Where-Object { $_.EventData -like "Action=" } |Select-Object MessageId, MessageSubject, EventData

 For some reason two messages with daily reports - sent from EntAdmin @ Contoso1.net to Michael.Firsov @ contoso1.net were also subject to that rule (the two messages that were sent after the new rule had been created).

The log does really contain the newly-created rule for the messages that were NOT destined to SharedMB @ contoso1.net:

"2025-02-26T15:00:23.023Z,,EXCH1,,,CatContentConversion,,AGENT,AGENTINFO,58639188492289,******@EXCH1.Contoso1.net,4d444fe5-aa74-4e25-a8c5-08dd567649c5,@contoso1.net,,5718,1,,,TestENTERPRISE: Daily EXCHANGE Server Report from EXCH2!,entadmin @ contoso1.net,@Contoso1.net,,Originating,,10.0.0.62,10.0.0.211,"S:AMA=SUM|v=0|action=|error=|atch=2;S:AMA=EV|engine=M|v=0|sig=1.413.283.0|name=|file=;S:TRA=ETRP|ruleId=ff116ef4-402d-4dff-90cb-c3d772b3179a|st=2023-05-12T07:55:40.0000000Z|ExecW=4|ExecC=0|Conditions=GTOEP,M.MAS,1;S:TRA=ETRP|ruleId=f94242a7-ebe6-46f4-9612-ec4745b26353|st=2025-02-07T14:54:33.0000000Z|ExecW=1|ExecC=0|Conditions=ISUP,M.F,1;S:TRA=ETRP|ruleId=7366001e-f754-4330-9211-1bb412b6b159|"

???

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-26*

P.S. one more test to illustrate the strangeness of the rules: 

I created a new rule that fires up for messages sent to ******@contoso1.net...

...and sent the single message to that address. Nevertheless, three messages were returned by the following commands:

$startDate = "02/26/2025 09:00:00"

$endDate = "02/26/2025 21:00:00"

$ruleID = "7366001e-f754-4330-9211-1bb412b6b159"

Get-TransportService | Get-MessageTrackingLog -Start $startDate -End $endDate -Source Agent |

Where-Object { $_.EventData -like "Action=" } |Select-Object MessageId, MessageSubject, EventData

For some reason two messages with daily reports - sent from ******@Contoso1.net to ******@contoso1.net were also subject to that rule (the two messages that were sent after the new rule had been created).

The log does really contain the newly-created rule for the messages that were NOT destined to ******@contoso1.net:

"2025-02-26T15:00:23.023Z,,EXCH1,,,CatContentConversion,,AGENT,AGENTINFO,58639188492289,******@EXCH1.Contoso1.net,4d444fe5-aa74-4e25-a8c5-08dd567649c5,@contoso1.net,,5718,1,,,TestENTERPRISE: Daily EXCHANGE Server Report from EXCH2!,@contoso1.net,******@Contoso1.net,,Originating,,10.0.0.62,10.0.0.211,"S:AMA=SUM|v=0|action=|error=|atch=2;S:AMA=EV|engine=M|v=0|sig=1.413.283.0|name=|file=;S:TRA=ETRP|ruleId=ff116ef4-402d-4dff-90cb-c3d772b3179a|st=2023-05-12T07:55:40.0000000Z|ExecW=4|ExecC=0|Conditions=GTOEP,M.MAS,1;S:TRA=ETRP|ruleId=f94242a7-ebe6-46f4-9612-ec4745b26353|st=2025-02-07T14:54:33.0000000Z|ExecW=1|ExecC=0|Conditions=ISUP,M.F,1;S:TRA=ETRP|ruleId=7366001e-f754-4330-9211-1bb412b6b159|"

???

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-07*

P.S. ..just to illustrate the strangeness of the log:

I've modifed the rule to apply the signature to the messages sent ony from Micael Firsov (instead of the distribution group) and sent one more test email (Signature Test...):

The result: the rule was applied but

-  I still don't understand why does the message with the signature added (meaning the rule had been really applied) have two instances of the RuleID in the log?

-  why does this time the Ation field = AHD instead of "ApplyHTMLDisclaimer" as it should be and as it was in the previouse test (see he pictue above)?

-  if the log contains the same RuleID - the single instance! -  for all other messages then what does it mean? Those messages does not have the signature applied - why in this case there's the Signature RuleID in the log for all other mesages?

Regards,  

Michael Firsov

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-07*

Hi Jake Zhang,

I must apologize - seems the problem in the log itself:  all messages do really get logged as the ones for which the rule has been applied - I don't know why for now - but the most interesting fact is this: out of all messages only two of them - the last two - have the rule with the id =f94242a7-ebe6-46f4-9612-ec4745b26353 logged twice, with the Action =ApplyHtmlDisclaimer, so the main question is why do some messages has only one occurence of the  RuleID =f94242a7-ebe6-46f4-9612-ec4745b26353 in the log while some of them get logged twice in the same log but it's not the question I originally posted so... 

Thank you so much for your help!

Regards,  

Michael Firsov
