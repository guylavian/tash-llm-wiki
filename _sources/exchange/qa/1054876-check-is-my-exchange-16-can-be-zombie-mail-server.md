---
title: "Check is my Exchange 16 can be zombie mail server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1054876/check-is-my-exchange-16-can-be-zombie-mail-server
question_id: 1054876
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Check is my Exchange 16 can be zombie mail server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1054876/check-is-my-exchange-16-can-be-zombie-mail-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

From time to time I look on mail logs of my Exchange 2016. Today I looked to smtp send logs and start thinking is my server is enough protected because I found that in my logs:

Software: Microsoft Exchange Server

Version: 15.0.0.0

Log-type: SMTP Send Protocol Log

Date: 2022-10-19T08:44:41.856Z

Fields: date-time,connector-id,session-id,sequence-number,local-endpoint,remote-endpoint,event,data,context

2022-10-19T08:44:32.784Z,My.Mail.Server.com,08DAB13335961996,0,,50.7.176.26:25,,SendRoutingHeaders,Set Session Permissions  

2022-10-19T08:44:32.784Z,My.Mail.Server.com,08DAB13335961996,1,,50.7.176.26:25,,,attempting to connect  

2022-10-19T08:44:32.910Z,My.Mail.Server.com,08DAB13335961996,2,InternalIPOfMyMailServer:10437,50.7.176.26:25,+,,  

2022-10-19T08:44:33.035Z,My.Mail.Server.com,08DAB13335961996,3,InternalIPOfMyMailServer:10437,50.7.176.26:25,<,220 0dsblqs2.hispanicliving.shop ESMTP Postfix,  

2022-10-19T08:44:33.036Z,My.Mail.Server.com,08DAB13335961996,4,InternalIPOfMyMailServer:10437,50.7.176.26:25,>,EHLO My.Mail.Server.com,  

2022-10-19T08:44:33.159Z,My.Mail.Server.com,08DAB13335961996,5,InternalIPOfMyMailServer:10437,50.7.176.26:25,<,250 0dsblqs2.hispanicliving.shop Hello My.Mail.Server.com [ExternalIPOfMyMailServer] SIZE 1000000 HELP ENHANCEDSTATUSCODES OK,  

2022-10-19T08:44:33.159Z,My.Mail.Server.com,08DAB13335961996,6,InternalIPOfMyMailServer:10437,50.7.176.26:25,*,,sending message with RecordId 167503004549 and InternetMessageId <fed061de-3411-44fe-b5cb-d85762c10d2e@Testta  .MyDomain.com>  

2022-10-19T08:44:33.159Z,My.Mail.Server.com,08DAB13335961996,7,InternalIPOfMyMailServer:10437,50.7.176.26:25,>,MAIL FROM:<> SIZE=18019,  

2022-10-19T08:44:33.281Z,My.Mail.Server.com,08DAB13335961996,8,InternalIPOfMyMailServer:10437,50.7.176.26:25,<,250 2.1.0 Ok,  

2022-10-19T08:44:33.281Z,My.Mail.Server.com,08DAB13335961996,9,InternalIPOfMyMailServer:10437,50.7.176.26:25,>,RCPT TO:<****@hispanicliving.shop**>,  

2022-10-19T08:44:33.421Z,My.Mail.Server.com,08DAB13335961996,10,InternalIPOfMyMailServer:10437,50.7.176.26:25,<,250 2.1.5 Ok,  

2022-10-19T08:44:33.421Z,My.Mail.Server.com,08DAB13335961996,11,InternalIPOfMyMailServer:10437,50.7.176.26:25,>,DATA,  

2022-10-19T08:44:33.544Z,My.Mail.Server.com,08DAB13335961996,12,InternalIPOfMyMailServer:10437,50.7.176.26:25,<,354 End data with <CR><LF>.<CR><LF>,  

2022-10-19T08:44:33.720Z,My.Mail.Server.com,08DAB13335961996,13,InternalIPOfMyMailServer:10437,50.7.176.26:25,<,250 ok 1666169082 30910,  

2022-10-19T08:44:33.722Z,My.Mail.Server.com,08DAB13335961996,14,InternalIPOfMyMailServer:10437,50.7.176.26:25,>,QUIT,  

2022-10-19T08:44:33.722Z,My.Mail.Server.com,08DAB13335961996,15,InternalIPOfMyMailServer:10437,50.7.176.26:25,-,,Remote

252084-smtp-send-log.txt

I search in other date smtp send logs and there are more lines like that.

So main main question is - what should I check to protect my mail server from send mails by not auth users (outside my domain)?  

I undestand this logs like my server is allowing send mail from "no-sender" --> MAIL FROM:<>

## Answers

_No answers on this thread._
