---
title: "ADFS MSIS7065: There are no Registered protocol handlers on path /adfs/ls/idpinitialtedSignon.aspx"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2125160/adfs-msis7065-there-are-no-registered-protocol-han
question_id: 2125160
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS MSIS7065: There are no Registered protocol handlers on path /adfs/ls/idpinitialtedSignon.aspx

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2125160/adfs-msis7065-there-are-no-registered-protocol-han (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can anyone suggest what causing this issue and a fix?

-  The OS is Windows server 2022, hosted on VM workstation 16.5 configuring the ADFS service, I get the following message when accessing https://adfs.ldlt.com/adfs/ls/idpinitiatedSignon.aspx on the workplace VM?

Microsoft.IdentityServer.RequestFailedException: MSIS7065: There are no registered protocol handlers on path /adfs/ls/idpinitialtedSignon.aspx to process the incoming request. at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)

Event ID 364

I tried setting Set-AdfsProperties –EnableIdpInitiatedSignonPage $True, this do not work.

Performing the same steps on the home VM workstation 17.6 (hardware setting 16.5), I can access the the sign on page? I am stumped, what causing it and how to fix the issue?

## Answers

_No answers on this thread._
