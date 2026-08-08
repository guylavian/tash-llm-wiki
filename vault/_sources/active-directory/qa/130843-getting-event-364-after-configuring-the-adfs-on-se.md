---
title: "Getting Event 364 After Configuring the ADFS on Server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/130843/getting-event-364-after-configuring-the-adfs-on-se
question_id: 130843
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Getting Event 364 After Configuring the ADFS on Server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/130843/getting-event-364-after-configuring-the-adfs-on-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI Team,  

After configuring the ADFS I am trying to login into ADFS then I am getting the windows even ID 364 in ADFS --> Admin logs.  

I am creating this for Lab purpose ,here is the below error message.  

```
Log Name: AD FS/Admin Source: AD FS Date: 10/16/2020 10:17:50 AM Event ID: 364 Task Category: None Level: Error Keywords: AD FS User: VIRTUSAINFORLN\abc Computer: AMULNPRACTICE02.virtusainforln.com Description: Encountered error during federation passive request. Additional Data Protocol Name: Relying Party: Exception details: Microsoft.IdentityServer.RequestFailedException: MSIS7065: There are no registered protocol handlers on path /adfs/ls/idpinitatedsignon to process the incoming request. at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context) Event Xml:    364 0 2 0 0 0x8000000000000001  1574   AD FS/Admin AMULNPRACTICE02.virtusainforln.com          Microsoft.IdentityServer.RequestFailedException: MSIS7065: There are no registered protocol handlers on path /adfs/ls/idpinitatedsignon to process the incoming request. at 
Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)     
```

Can anyone help me on that.

## Answers

_No answers on this thread._
