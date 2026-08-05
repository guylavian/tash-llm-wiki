---
title: "outlook, exchange 2016 -The name cannot be matched to a name in the address list-can't create outlook profile"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/337442/outlook-exchange-2016-the-name-cannot-be-matched-t
question_id: 337442
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# outlook, exchange 2016 -The name cannot be matched to a name in the address list-can't create outlook profile

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/337442/outlook-exchange-2016-the-name-cannot-be-matched-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi experts,  

I can't create outlook profile for exchange 2016 users( 2 users).   

the error - The action cannot be completed. The name cannot be matched to a name in the address list", while at the step of logging on to the mail server.    

what I have tried so far are the follows:  

Remove the offending account from Windows Credentials, including the mailboxconnect.net server and the autodiscover should it be there. Within Generic Certificates, removing the offending account from there also. Close Windows Credential Manager.  

sign out from the office Excel,  run online repair of Office software.  

in the Exchange admin center, user mailbox properties.  Check the ""Hide from address lists"" option and click Save. still have the same issue. then I clear  the ""Hide from address lists"" option and click Save, tried but still not working.  

in Registry Editor , go to HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Identity  

and Delete the identity folder, restart. repair the Office application again. still not working.  

i tried use create the outlook profile using the manual settings, enter the exchange server name and login, but the error is "-  Log onto exchange ActiveSync mail server(EAS): The server cannon be found."  

what else can I try, any suggestion would be greatly appreciated.  

Thanks for your time.  

pingatwork

## Answers

_No answers on this thread._
