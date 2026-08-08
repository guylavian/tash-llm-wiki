---
title: "Active directory and domain controller upgrade from Version 2008R2 to Version 2016 / 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/802115/active-directory-and-domain-controller-upgrade-fro
question_id: 802115
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-high-availability-clustering-high-availability"]
---
# Active directory and domain controller upgrade from Version 2008R2 to Version 2016 / 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/802115/active-directory-and-domain-controller-upgrade-fro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Sir,  

```
Customer has an environment with Windows 2008R2 active directory, they want to upgrade active directory and domain controller to Version 2016 / version 2019.
```

May I have information whether it is possible and any issue in the application and client after Active directory and all domain controller upgrade?  

Existing environment has:  

1、Exchange 2013 cu23 DAG (Withness service in DC)  

2、Sharepoint 2013  

3、Microsoft Dynamic Ax 2012 R3  

4、Windows Failover Cluster (Working on Windows 2012 R2)  

```
All PC are running Windows version 10.

 I understand that Exchange 2013 has scheme which can support up to active directory 2016 only. For others, I doesn't find information related on Active directory.
```

May I have information or related document link?  

Joe Tam

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-06*

Hello @JOE TAM   ,    

Welcome to Q&A Forum!     

Currently, SharePoint 2013 does not support Windows 2019 Domain Controller.    

Upgrading Active Directory  from 2008 R2 to 2016 will not have any impact on the SharePoint 2013 environment.    

---------------------------------------------------    

Microsoft Supported Reply    

We can confirm that SharePoint On-Premise version 2010 and 2013 are compatible with Active Directory On-Premise version 2016    

We can confirm that after AD upgrade successfully to version 2016 there won’t be any issue or impact to SharePoint On-Premise version 2010 and 2013    

Please note, the SharePoint On-Premise version 2010 and 2013 means Out-of-Box features/functions in SharePoint On-Premise version 2010 and 2013    

-  Custom solutions/developments in SharePoint On-Premise version 2010 and 2013 are not included in this statement. We cannot ensure custom solutions/developments work correct after upgraded AD to version 2016.    

-  Features/Functions used in SharePoint On-Premise version 2010 and 2013 provided by other applications are not included in this statement. Such as send email feature in SharePoint On-Premise version 2010 and 2013 is based on mail system. SharePoint only call the APIs from the mail system to proceed the send email actions. However we cannot ensure mail system can work correct with Active Directory On-Premise version 2016. That is why the features/functions provided by other applications are not included in this statement.    

Therefore, we recommended to proceed a test in UAT environment firstly to ensure everything works fine with Active Directory On-Premise version 2016"    

Here are similar cases for your reference:    

-  Upgrading AD from 2008 R2 to 2016. Does it have any impact on SharePoint 2013 environment.    

-  SharePoint Foundation 2013 with 2016/2019 Domain Controllers?    

Thanks,    

Echo Du    

=============================================    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
