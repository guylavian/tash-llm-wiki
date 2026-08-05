---
title: "unable to connect to exchangeOnline with credential in powershell script"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1037332/unable-to-connect-to-exchangeonline-with-credentia
question_id: 1037332
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# unable to connect to exchangeOnline with credential in powershell script

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1037332/unable-to-connect-to-exchangeonline-with-credentia (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

I'm working on powershell scripts which should interact with exchange online.    

I managed to do it in my laptop, with the following command:    

    `Connect-ExchangeOnline -Credential  $UserCredential -ShowBanner:$False -Verbose -EnableErrorReporting -LogDirectoryPath $logDirPath -LogLevel` All  

and got the following reporting info:    

Successfully acquired token based on Credential flow;Successfully got a token from AAD;SessionPrefixName:ExchangeOnlineInternalSession    

Now, when I deploy my scripts in the test vm which has the same configuration, they failed to connect:    

3.0.0      ExchangeOnlineManagement     

1.1.183.66 MSOnline    

I get the following report:    

,CorrelationID: - Could not acquire token silently  need UI authentication. No account or login hint was passed to the AcquireTokenSilent call    

Do you know how it s possible and how to solve it?    

regards    

Mat

## Answers

_No answers on this thread._
