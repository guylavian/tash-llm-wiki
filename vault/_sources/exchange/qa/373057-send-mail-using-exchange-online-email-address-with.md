---
title: "Send mail using exchange online email address without storing message"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/373057/send-mail-using-exchange-online-email-address-with
question_id: 373057
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Send mail using exchange online email address without storing message

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/373057/send-mail-using-exchange-online-email-address-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible to send an email using exchange online without keeping the sent message?   

No matter what settings I do with the exchange online management shell, the message is always stored in the sent emails -folder. Please, note that I tested using this code. Send emails may potentially contain sensitive information; thus, they should not exist on the server.  

$username = "mailboxOrUser@mydomain"  

$password = "password"  

$sstr = ConvertTo-SecureString -string $password -AsPlainText -Force  

$cred = New-Object System.Management.Automation.PSCredential -argumentlist $username, $sstr  

$body = "Hello"  

Send-MailMessage -To "x.x@mydomain" -from "x.x@mydomain" -Subject 'Hello.' -Body $body -BodyAsHtml -smtpserver smtp.office365.com -usessl -Credential $cred -Port 587  

]

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-28*

Thanks. Works perfectly!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-28*

@Tolppa       

Have you run the above command to disable "MessageCopyForSMTPClientSubmission"? I tested it in my lab, it could work after waiting about 30 minute.    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
