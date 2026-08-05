---
title: "Exchange 2016 CU19 - Server error on '/ecp' Application"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/247455/exchange-2016-cu19-server-error-on-ecp-application
question_id: 247455
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2016 CU19 - Server error on '/ecp' Application

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/247455/exchange-2016-cu19-server-error-on-ecp-application (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have install Exchange Server 2016 CU19 on new Windows Server 2016. OWA is working properly but ECP gives me a "Server error on '/ecp' Application" after the login.    

Any advise?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-28*

Hi Yuki Sun-MSFT,    

Thanks for your reply.    

Before to open this topic I've re-create OWA & ECP directories and I've run the *.ps1 scripts. Unfortunately without success.    

When I open ecp via IE it gives me the following after ecp login.    

I've clean the ASP.NET Temp sub folder & files, reboot the server, unfortunately without success again.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-28*

Hi @Dimitrios Kourlas  ,    

Have you checked if there's any relevant events recorded in the Event Viewer when the error occurs?    

Are you able to access ECP via https://localhost/ecp on the Exchange server?    

Please try to remove and recreate the ECP virtual directory and see if it can be fixed.    

If it doesn't work, It's suggested to run the "UpdateCAS.ps1" and “UpdateConfigFiles.ps1” script from the Exchange install directory scripts subfolder:    

-  C:\Program Files\Microsoft\Exchange Server\V15\Bin>.\UpdateCas.ps1    

-  C:\Program Files\Microsoft\Exchange Server\V15\Bin>.\UpdateConfigFiles.ps1    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
