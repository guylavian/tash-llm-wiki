---
title: "ACtive directory Web Services unable to start"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/341044/active-directory-web-services-unable-to-start
question_id: 341044
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# ACtive directory Web Services unable to start

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/341044/active-directory-web-services-unable-to-start (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone  

After reboot there is a problem with ADWS service. It always starting with error :  

A timeout was reached (60000 milliseconds) while waiting for the Active Directory Web Services service to connect.  

There are no any events in Active Directory Web Services - Application and Services Logs  

Tried to turn on additional logs - no event at all  

https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/active-directory-web-services-event-1202/ba-p/1514401  

Checked:  

-  Certificate is valid and can be enrolled  

-  dism checkhealth and sfc /scannow  

-  Procmon - no access denied or some other error, except   

Microsoft.ActiveDirectory.WebServices.exe Operation - TCP Reconnect take too much time and ended with TCP Disconnect  

What else can i do ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-07*

Hello Daisy,  

-  After updates unstallation and reboot  

-  All last installed patches were removed. There where no any other changes  

kind regard  

Kirill

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-06*

Hello Daisy,  

I've tried to increase time to 120 seconds and restart computer Already, it doesn't help.  

Service fall in 20 seconds  

kind regard  

Kirill

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-06*

Hello @Courtenay  ,    

For event ID 7000, we can refer to the link below.    

A slow service does not start due to time-out error in Windows    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/service-not-start-events-7000-7011-time-out-error    

Then check if the issue persists.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-02*

Hello Daisy,

Thank for response

1) Yes, ADWS service can not be started on one Domain Controller. Others work well. Btw, DC is Windows Server 2012 R2  

2) Errors always the same

The Active Directory Web Services service failed to start due to the following error:  

The service did not respond to the start or control request in a timely fashion.

A timeout was reached (60000 milliseconds) while waiting for the Active Directory Web Services service to connect.  

3) There are no any events at all on Active Directory Web Services Logs after it stop to working. Even after computer restart.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-02*

Hello @Courtenay  ,

Thank you for posting here.

After my view, I can see "Active Directory Web Services---This service provides a Web Service interface to instances of the directory service (AD DS and AD LDS) that are running locally on this server. If this service is stopped or disabled, client applications, such as Active Directory PowerShell, will not be able to access or manage any directory service instances that are running locally on this server."

1.Based on the description, do you mean the ADWS service on one Domain Controller can not be started?  

2.If so, if you try to start ADWS service on this Domain Controller, what error message do you receive? Please provide the screenshot if possible.  

3.After we try to start ADWS service on this Domain Controller (maybe the service can not be started), please check if there is any event logged in Event Viewer as below?  

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
