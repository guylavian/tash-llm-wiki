---
title: "exchange owa error: error: Your request can't be completed right now. Please try again in a few moments."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/117900/exchange-owa-error-error-your-request-cant-be-comp
question_id: 117900
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# exchange owa error: error: Your request can't be completed right now. Please try again in a few moments.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/117900/exchange-owa-error-error-your-request-cant-be-comp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dears,

i have 4 exchange 2016 servers. OWA is published externally using adfs and wap.  

recently, the following is happening on owa externally: ****error: Your request can't be completed right now. Please try again in a few moments.****  

whenever i open inbox items, this issue happens.  

and when i try to search in the address book or send an email: it is giving make sure that your device is connected to the internet.  

however, mail flow internally on owa is working. then issue is just externally.

any idea?

best regards

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-26*

able to provide more information on how to resolve?  

i am having same issues, but only on chromium browsers

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-12*

issue was related to security configuration on the firewall.  

best regards,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-07*

hey,  

.If you install or upgrade Exchange server recently, please make suer already prepare Schema/AD/AD domains. do i have to run this if im just upgrading from cu to cu on the same exchange server version?  

Please try to change another browser to access OWA.: same issue  

Please run the following command in the Windows Powershell to check whether the Windows components required by Exchange are complete: this is valid  

Check Windows and Anonymous authentication are enabled on OWA virtual directory on exchange back end web site, if not, change them and reset iis.: this is set too  

all the users are facing it too  

the issue isnt on the mail flow, its just i cant open messages nor compose emails:   

best regards

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-07*

Hi @eg1995   ,  

What is your Exchange server version?  

Only one user have this issue or all users have?  

Did you change any settings before this issue occurred?  

Please following the steps and see if the issue is resolved:  

1.Please try to change another browser to access OWA.  

2.If you install or upgrade Exchange server recently, please make suer already prepare Schema/AD/AD domains, and please check if there have Event ID 4999 error log in the Windows Application log. If so, follow the steps in the link below to fix it.  

For more information: Error in Outlook Web App after an upgrade to Exchange Server 2013 CU 11 or later: Your request cannot be completed right now  

3.Please run the following command in the Windows Powershell to check whether the Windows components required by Exchange are complete:

```
Get-WindowsFeature
```

For more information :Install the required Windows components  

4.Considering that there is a problem with the external OWA, please try to temporarily turn off the firewall and log in to OWA again. In addition, if there is a third-party antivirus software, please turn it off temporarily.  

5.Check Windows and Anonymous authentication are enabled on OWA virtual directory on exchange back end web site, if not, change them and reset iis.  

6.Please try to run the following command to check the external url setting of OWA virtual directory. You also could run the following commands to remove and re-create the OWA virtual directory.

```
Get-OWAVirtualdirectory | fl  
Remove-OWAVirtualdirectory  
New-OWAVirtualdirectory
```

In addition, please check when you login OWA if there have any related error log in Event Viewer and IIS log.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
