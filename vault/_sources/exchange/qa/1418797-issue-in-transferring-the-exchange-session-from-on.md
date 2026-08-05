---
title: "Issue in transferring the Exchange Session from one script to another."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1418797/issue-in-transferring-the-exchange-session-from-on
question_id: 1418797
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-online"]
---
# Issue in transferring the Exchange Session from one script to another.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1418797/issue-in-transferring-the-exchange-session-from-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm using Certificate based Authentication for Connecting to ExchangeOnline in an unattended Script. We have multiple scripts each perform a certain task but the authentication was happening in the one script and then the session will be transferred to other scripts. This was working when I was using basic authentication but now that I started using certificate based authentication the session is not being imported to the other scripts.   

Im using this command to connect.   

New Command :

```
Connect-ExchangeOnline -AppId $clientId -CertificateFilePath $certificatePath -Organization $domain -CertificatePassword (ConvertTo-SecureString -String $certPassword -AsPlainText -Force) -ExchangeEnvironmentName $exchangeEnv -PSSessionOption $sessionOptions
```

Old Command :

```
Connect-ExchangeOnline -Credential $credential -ExchangeEnvironmentName $exchangeEnv -PSSessionOption $sessionOptions -UseMultithreading $true
```

## Answers

_No answers on this thread._
