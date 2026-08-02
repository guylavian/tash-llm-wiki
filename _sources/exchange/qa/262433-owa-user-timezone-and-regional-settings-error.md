---
title: "OWA  user timezone and regional settings error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/262433/owa-user-timezone-and-regional-settings-error
question_id: 262433
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# OWA  user timezone and regional settings error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/262433/owa-user-timezone-and-regional-settings-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

after cumulative update When trying to log into OWA for some user, it asks you to set your timezone and regional settings as expected.   

However, when trying to save the settings, the following error occurs  

"This method or property is not supported after HttpRequest.Form, Files, InputStream, or BinaryRead has been invoked."

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-17*

How about accessing OWA locally on the Exchange server via https://localhost/owa  

I am temporarily solving this issue by locally accessing owa and log in with the user credential. When we enter localhost owa it prompts for regional setting and after that the user not getting any error while login to the web access.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-15*

We couldn't find the below entry in applicationHost.Config file and we tried the second link shared by Ashokan already. Is there any other way to fix this issue  

<add name="TransportModule" type="System.Web.TransportClient.TransportHandlerModule, System.Web.TransportClient, Version=1.0.0.0, Culture=neutral, PublicKeyToken=9cbc39238c01012f" />  

Please find the answer for your question  

What's the version of your Exchange server and which CU are you using?  

Version 15.1 ‎(Build 2106.2)‎  

Have you tried to access OWA in different browsers and see if the issue persists? Also how about in Private mode?  

Issue persists  

Any relevant error in Event Viewer?  

i don't know in event viewer where to check the error

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-08*

Hi @Muhammed Shehim  ,    

What's the version of your Exchange server and which CU are you using?    

Have you tried to access OWA in different browsers and see if the issue persists? Also how about in Private mode?    

Any relevant error in Event Viewer?    

Based on my previous experience, this error could be related to the a previous loaded module System.Web.TransportClient.TransportHandlerModule. Please try following the steps below and see if it can resolve your issue:    

-  On all mailbox servers(or all client access servers supposing you are running earlier versions of Exchange), navigate to the path below and locate the applicationHost.Config file:        C:\Windows\System32\inetsrv\config  

    

-  Make a backup of the applicationHost.Config file.    

-  Search and removed the part below:        <add name="TransportModule" type="System.Web.TransportClient.TransportHandlerModule, System.Web.TransportClient, Version=1.0.0.0, Culture=neutral, PublicKeyToken=9cbc39238c01012f" />  

-  Restart IIS.    

-  Check if the OWA user can set their timezone and region settings properly.     

If the method above doesn't work, please remember to restore the applicationHost.Config file using the backup created in step2 and you could provide more information as mentioned earlier for further troubleshooting. Meanwhile, before the issue gets finally resolved, you may refer to the second link shared by AshokM to set the timezone and region for users using Exchange powershell as a temporary workaround.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-07*

Hi,  

I found a reference for the similar issue, please check if that is helpful.  

https://social.technet.microsoft.com/Forums/en-US/dc741f39-74fb-4396-801c-891351ef8ff8/exchange-2013-on-premise-verthis-method-or-property-is-not-supported-after-httprequestform-files?forum=exchangesvradmin  

https://support.secureauth.com/hc/en-us/articles/360019647772-OWA-new-user-timezone-and-regional-settings-error  

If the above suggestion helps, please click on “Accept Answer” and upvote it.
