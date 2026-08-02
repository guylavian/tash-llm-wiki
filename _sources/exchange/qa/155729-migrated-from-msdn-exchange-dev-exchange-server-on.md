---
title: "[Migrated from MSDN Exchange Dev] Exchange server on win 2012 r2 server application gui icon dissapears after windows server essentials instalation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/155729/migrated-from-msdn-exchange-dev-exchange-server-on
question_id: 155729
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] Exchange server on win 2012 r2 server application gui icon dissapears after windows server essentials instalation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/155729/migrated-from-msdn-exchange-dev-exchange-server-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange have been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link] Exchange server on win 2012 r2 server application gui icon dissapears after windows server essentials instalation  

[Original post]  

Hello all,  

I have a win 2012 r2 server running exchange 2013. all was working fine. I put windows server essentials on it and my exchange account in outlook began prompting for a password and i couldn't get it to stop.  

Then I noticed that the icon on the server to manage exchange was gone. Looking at the running services all the exchange services seem to still be installed and running but I cannot connect to the exchange server with outlook when i try to setup a exchange account I get the message " an encrypted connection to your mail server is not available. Click next to try an unencrypted connection. After that it fails and says "having trouble connecting to your account  

I uninstalled the windows server essentials from the server but the exchange management icon still is gone. verify settings and make changes if necessary.  

Any ideas how to get the exchange management icon back sh  

Thanks for any ideas  

Mac

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-09*

Hi Marc,    

According to this official article, "Microsoft does not support installing Exchange Server on a server that is running Windows Server Essentials." So if you would like to deploy Exchange server on a Windows Server Essentials network, it's recommended to have them installed on separate severs.    

As per the the current issue, may I know if you are referring to the EMS icon by "exchange management icon"? If this is the case, have you checked the Start screen > Apps list to see if the icon is visible there? It yes, you can right-click the icon and pin it to the Start screen or taskbar if you like.      

In case the icon is not visible in the Start screen, please verify that the ConnectFunctions.ps1 , RemoteExchange.ps1 and CommonConnectFunctions.ps1 files are present in the%ExchangeInstallPath%\bin directory. If they are not there, you can copy the files from the Exchange Server 2013 installation media (\setup\serverroles\common) to the %ExchangeInstallPath%\bin directory.      

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
