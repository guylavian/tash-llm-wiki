---
title: "Intermittent Outlook login prompt after Exchange 2013CU23 > Exchange 2019 migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/329267/intermittent-outlook-login-prompt-after-exchange-2
question_id: 329267
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Intermittent Outlook login prompt after Exchange 2013CU23 > Exchange 2019 migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/329267/intermittent-outlook-login-prompt-after-exchange-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello fellow IT-guys,  

we recently spun up a new Exchange 2019 server, moved mailboxes to new databases on the EX2019 from our old EX2013CU23 server.  

After that, we swapped DNS and uninstalled Exchange 2013 via control panel from old server and turned it off.  

So far so good, but I'm having one weird issue:  

Outlook (Various versions from Outlook 2013 to Outlook 365) sometimes, usually after starting it the first time for the day (After having it shut down for a while, like end of workday) will prompt for login.  

If you close Outlook and open it again, it won't prompt and all is well in the world.  

If you do not enter credentials and open Outlook, it will complain that it cannot reach the information store.  

Entering credentials will successfully open Outlook.  

I am sure there's some reference on the old server somewhere, but I don't know exactly where to start troubleshooting. I cannot find a log entry in the Event Viewer either on client or server that I can correlate to this.  

So I'd like to have some assistance in where to start troubleshooting this.  

Old artifacts in AD? Certificate missmatches? Some configuration in EX2019 I've missed?  

Anything is of help!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-25*

Hi @Emil Gustafsson  ,    

Outlook (Various versions from Outlook 2013 to Outlook 365) sometimes, usually after starting it the first time for the day (After having it shut down for a while, like end of workday) will prompt for login.    

Does it affect some particulat users only or all users are affected?    

Are the users connecting to Exchange server via Outlook Anywhere or MAPI over HTTP?     

Any difference if the machine is outside the organization's network?    

If the login prompt issue can be reproduced on a machine every day when opening Outlook the first time for the day, it's suggested to try launching Outlook in safe mode(Press Win+R, type "outlook /safe", press Enter.) next time and see how it goes. This helps narrow down if the issue is due to any third-party add-ins on the client side. If possible, it's also recommended to test on a clean machine by configuring a problematic user account and see if it can be reproduced.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-24*

Have you checked the credential manager?   

Any add-ins causing this issue?  

Try adding ExcludeExplicitO365Endpoint registry key and see if that helps.  

-  Open regedit  

-  Navigate to HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Outlook\AutoDiscover   

-  Add a new DWORD entry  

-  Enter the name of ExcludeExplicitO365Endpoint and value of 1.  

Please note: Export/backup of registry before making changes.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-24*

Hi @Emil Gustafsson   ,    

Run Test Email autoconfiguration, to do this outlook system tray -> right click -> Test Email autoconfiguration    

Type the email address and uncheck "use guessmart" & "secure guessmart authentication" and click on "Test"    

If the test is success and the result has the necessary URL's.     

Check the authentication for Autodiscover, MAPI, OAB, EWS virtual directories    

https://learn.microsoft.com/en-us/exchange/clients/default-virtual-directory-settings?view=exchserver-2019    

If the above suggestion helps, please click on "Accept Answer" and upvote it. Thanks for understanding.
