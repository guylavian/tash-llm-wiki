---
title: "cannot login to EAC or Exchange powerShell after restoring Exchange 2016 Server from backup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/319853/cannot-login-to-eac-or-exchange-powershell-after-r
question_id: 319853
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# cannot login to EAC or Exchange powerShell after restoring Exchange 2016 Server from backup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/319853/cannot-login-to-eac-or-exchange-powershell-after-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

getting HTTP 500 error   

and redirect to URTL  https://localhost/owa/auth.owa when trying to login to EAC  

I also cannot open PowerShell getting access denied   

this is happening after we restored the Exchange server from Veeam backup .   

IS there a something I need to do to get this going ? Looks like all Exchange Services are running .

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-24*

Hello it turned out that Trend Micro AV was blocking the access.   

Once I whitelisted the internal Exchange URL's it started working .

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-19*

Hi, @dirkdigs       

Did you make some changes to the active directory before you restore the server?    

For example, modify the members of the groups in ADUC (Active Directory Users and Computers).    

Please check if there are some error events like Event ID 4 generated in the Event Viewer>Application Log on the server.    

If you can find Event ID 4 in the application log, the problem may be caused by incorrect permission settings of the server.    

Please refer to this document to troubleshot the problem:    

Error occurs in EMS, EAC, ECP, OWA, or Outlook on the web in Exchange Server 2013 or Exchange Server 2016    

In addition, please note that the supported method to backup Exchange server is using Windows Server Backup.     

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
