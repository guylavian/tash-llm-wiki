---
title: "Exchange Server 2013 Server Error in '/ecp' Application."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/172363/exchange-server-2013-server-error-in-ecp-applicati
question_id: 172363
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange Server 2013 Server Error in '/ecp' Application.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/172363/exchange-server-2013-server-error-in-ecp-applicati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I am having a problem with ECP with this error  

I have 2 Mail servers and 2 Client access servers.  

The 2 mail server have the back end configured, and the 2 client access the front end on IIS  

OWA works perfectly except for ECP  

Have tried updatecas on the 4 servers, have tried recreating ECP directories, the paths are correctly on the application pools.  

Can anyone help me with this problem?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-24*

Hi @luan gashi  ,    

Please try running the "UpdateCAS.ps1" and “UpdateConfigFiles.ps1” script from the Exchange install directory scripts subfolder and check the result:    

Run Exchange Management Shell or Powershell as an administrator:    

```
cd "C:\Program Files\Microsoft\Exchange Server\V15\Bin"  
UpdateCAS.ps1  
UpdateConfigFiles.ps1
```

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-23*

Hi,  

Could you please share the exact error message while accessing https://localhost/ecp on the servers?   

Check if you are getting the login page. Error appears before or after the credentials.  

Please remove personal information while sharing the details.  

Check the authentication on the ECP virtual directory which should be identical to OWA.
