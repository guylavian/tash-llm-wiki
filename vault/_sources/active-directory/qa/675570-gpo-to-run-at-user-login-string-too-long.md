---
title: "GPO to Run at User Login - String too long"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/675570/gpo-to-run-at-user-login-string-too-long
question_id: 675570
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# GPO to Run at User Login - String too long

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/675570/gpo-to-run-at-user-login-string-too-long (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Any ideas on an alternate method of creating a browser instance at user login with a HTTP URL parameter?   

Here are the details of my solution that almost works:  

- 	Set a working WMI filter for the requested subnets provided:    

Select * FROM Win32_IP4RouteTable  

WHERE (Mask='255.255.255.255'  

AND (Destination Like '191.168.4.%' OR Destination Like '191.168.5.%' OR Destination Like '191.168.33.%' OR Destination Like '191.168.38.%'))  

- 	Created Computer targeted GPO to execute a program at user logon:  

Computer Configuration > Policies > Admin Templates >   

System > Logon  

In the policy item "Run these programs at user logon"   

We specified to run a Chrome instance using the parameter "C:\Program Files\Google\Chrome\Application\chrome.exe" https://apps.powerapps.com/play/06b194ae-27c2- <cut off>  

However, the item gets cut off due to a character limit – the URL https://apps.powerapps.com/play/06b194ae-27c2-4c28-9634-a82baa6d8023?tenantId=0141856a-3155-40cc-8e14-  

Is too long.  

This is unfortunate because the command does work if you test a “Start Run ->>>  to Edge or Chrome with the below commands.  

"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://apps.powerapps.com/play/06b194ae-27c2-4c28-9634-a82baa6d8023?tenantId=0141856a-3155-40cc-8e14-  

"C:\Program Files\Google\Chrome\Application\chrome.exe" https://apps.powerapps.com/play/06b194ae-27c2-4c28-9634-a82baa6d8023?tenantId=0141856a-3155-40cc-8e14-

## Answers

_No answers on this thread._
