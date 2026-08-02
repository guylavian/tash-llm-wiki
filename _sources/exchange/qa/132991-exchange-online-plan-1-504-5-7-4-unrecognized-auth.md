---
title: "Exchange online plan 1 504 5.7.4 Unrecognized authentication type"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/132991/exchange-online-plan-1-504-5-7-4-unrecognized-auth
question_id: 132991
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange online plan 1 504 5.7.4 Unrecognized authentication type

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/132991/exchange-online-plan-1-504-5-7-4-unrecognized-auth (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently changed my email hosting to Microsoft Exchange online (plan 1).  I have a windows desktop application and a scanner that I need to send emails from using SMTP.  When I setup my account on the scanner device and software, I get the error "504 5.7.4 Unrecognized authentication type".  How do I fix this error?    

I have followed the directions:    

How to set up a multifunction device or application to send email using Microsoft 365 or Office 365, Option 1    

https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365    

Outlook on the web works, logon with username and password, send and receive emails.    

Multifactor Authentication is disabled.    

I have tried using the following host information, all returning the same error:    

<mydomain>.mail.protection.outlook.com, port 25    

smtp.office365.com, port 25    

smtp.office365.com, port 587    

My account is licensed: Exchange Online (Plan 1)    

In Microsoft 365 admin center, active users, my user, manage email apps: (all are checked)    

Outlook on the web - checked    

Outlook desktop (MAPI) - checked    

Exchange web services - checked    

Mobile (Exchange ActiveSync) - checked    

IMAP - checked    

Pop - checked    

Authenticated SMTP - checked    

In Exchange properies for account:    

Outlook on the web - enabled    

Outlook desktop (MAPI) - enabled    

Exchange web services - enabled    

Mobile (Exchange ActiveSync) - enabled    

IMAP - enabled    

Pop - enabled    

Using SMTP Diag tool, I get the following log trying to send an email:    

Connecting to mail server.    

Connected.    

220 <isthisprivate>.outlook.office365.com Microsoft ESMTP MAIL Service ready at Tue, 20 Oct 2020 18:02:19 +0000    

EHLO MYHOST    

250-<isthisprivate>.outlook.office365.com Hello [1.2.3.4]    

250-SIZE 157286400    

250-PIPELINING    

250-DSN    

250-ENHANCEDSTATUSCODES    

250-STARTTLS    

250-8BITMIME    

250-BINARYMIME    

250-CHUNKING    

250 SMTPUTF8    

AUTH LOGIN    

504 5.7.4 Unrecognized authentication type [<isthisprivate>.CANPRD01.PROD.OUTLOOK.COM]    

Forcing disconnection from SMTP server.    

QUIT    

221 2.0.0 Service closing transmission channel    

Disconnected.    

Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-01*

I really wish @FTINC   had provided a better answer.  I'm really stuck on this and they've perfectly described everything I've also tried to get our scanner to send with SMTP AUTH unsuccessfully.  I still haven't figured out what I'm doing wrong.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-21*

@FTINC      

Yes, you found the correct article to configure Exchange Online Relay Email for your application. However, we don't know how your application works. We recommend that you use this article to confirm with your application provider to check which option your application supports. Then, try to use the correct, the option 1 and 2 aren't supported by all application/device.    

You can also try to use the option 3 to create a dedicated SMTP relay connector to relay email from your application.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
