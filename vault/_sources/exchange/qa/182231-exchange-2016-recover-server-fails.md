---
title: "Exchange 2016 Recover Server Fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/182231/exchange-2016-recover-server-fails
question_id: 182231
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 Recover Server Fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/182231/exchange-2016-recover-server-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.    

We are trying to recover an Exchange 2016 server that failed during a CU update. However, when running setup /m:recoverserver the process fails the prereq check. Its not clear exactly why, but the last error in the setup logs is:    

[12/01/2020 14:49:36.0416] [0] Calling ADSession.GetSharedConfigDC()    

Failed to determine hostname for the DC. Hostname: null    

The server is named identically to the old server, and /preparead and /preparedomains have been run on the DC with the FSMO roles (it is in another site). I have tried both CU15 and CU18 installers but get the same error.    

I've attached the full (redacted) setup logs.44057-exchangesetuplog.txt    

Thoughts?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-02*

Do you have a GC in the site of new server?    

Try specifying the DC name in the /mode:recoverserver command:    

-  <Virtual DVD drive letter>:\Setup.exe /IAcceptExchangeServerLicenseTerms /Mode:RecoverServer [/TargetDir:<Path>] [/DomainController:<ServerNameOrFQDN>] [/DoNotStartTransport] [/EnableErrorReporting]    

Also, make sure:    

-  Install the same Windows Server operating system and service pack level on the server    

-  Configure your storage volumes to use the same drive letters as the previous server    

-  Join the server to the domain (note that you will first need to reset the computer account that already exists in Active Directory)    

-  Pre-Requisites:https://practical365.com/exchange-server/exchange-server-2016-pre-requisites/    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
