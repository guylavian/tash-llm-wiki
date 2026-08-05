---
title: "ADFS OWA Cookie expiration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/277347/adfs-owa-cookie-expiration
question_id: 277347
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS OWA Cookie expiration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/277347/adfs-owa-cookie-expiration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I publish OWA (exchange 2019) via ADFS (Windows 2016) and WAP. Frr some users I have errors (users conno't logon)

On WAP

Web Application Proxy received a request with an expired access cookie.  

The access cookie expired at: ‎2021‎-‎02‎-‎17T10:17:21.000000000Z.

Details:  

Transaction ID: {6f27eb28-01e4-0029-9b19-2a6fe401d701}  

Session ID: {6f27eb28-01e4-0019-80b6-2a6fe401d701}  

Published Application Name: *********  

Published Application ID: 38DC6AB9-40EE-B2DF-E94C-24AEEB4BBF9B  

Published Application External URL: https://*********  

Published Backend URL: https://*********  

User: <Unknown>  

User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36  

Device ID: <Not Applicable>  

Token State: NotFound  

Cookie State: Expired  

Client Request URL: https://*********/owa/ev.owa2?ns=PendingRequest&ev=FinishNotificationRequest&UA=0&cid=88f07396-574a-4929-a583-9888b8ab10d1  

Backend Request URL: <Not Applicable>  

Preauthentication Flow: <Not Applicable>  

Backend Server Authentication Mode:  

State Machine State: Idle  

Response Code to Client: <Not Applicable>  

Response Message to Client: <Not Applicable>  

Client Certificate Issuer: <Not Found>  

Response Code from Backend: <Not Applicable>  

Frontend Response Location Header: <Not Applicable>  

Backend Response Location Header: <Not Applicable>  

Backend Request Http Verb: <Not Applicable>  

Client Request Http Verb: POST

On ADFS  

Encountered error during federation passive request.

Additional Data

Protocol Name:

Relying Party:

Exception details:  

Microsoft.IdentityServer.Web.InvalidRequestException: Duplicate post parameter \"Res\".

## Answers

_No answers on this thread._
