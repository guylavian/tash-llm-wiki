---
title: "how to get rid of the response from Exchange when password is invalid and catch error message instead?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2079277/how-to-get-rid-of-the-response-from-exchange-when
question_id: 2079277
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# how to get rid of the response from Exchange when password is invalid and catch error message instead?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2079277/how-to-get-rid-of-the-response-from-exchange-when (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have the following command:

```
$null = Connect-ExchangeOnline -Credential $cred -PSSessionOption $proxyOptions -ShowBanner:$false -ErrorAction Stop
SilentlyContinue -WarningAction SilentlyContinue -InformationAction SilentlyContinue -ErrorVariable authError 2> $null
```

if there is a credential error it prints me:  

Error Acquiring Token:

AADSTS50126: Error validating credentials due to invalid username or password. Trace ID:   

I want to get rid of this message from the screen as later I return some JSON output from this script and it ruins it. I've checked chatgpt and copilot for answers but without success so far.  

I am using:

```
Import-Module -Name ExchangeOnlineManagement -RequiredVersion 3.1.0
```

Is there any way to do it?

## Answers

_No answers on this thread._
