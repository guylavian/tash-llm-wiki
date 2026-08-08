---
title: "Exchange 2019 - EML Viewer for e-discovery"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/128225/exchange-2019-eml-viewer-for-e-discovery
question_id: 128225
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Exchange 2019 - EML Viewer for e-discovery

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/128225/exchange-2019-eml-viewer-for-e-discovery (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,    

We are running an on premise Exchange 2019 environment.    

The Security officer requires to view the messages discovered using E-Discovery on the ECP itself rather than downloading it and viewing it separately which is quite a task as they do for a number of emails..    

 We can download the EML Files and can view it successfully. No issues in that way of working    

The issue is that the results are shown previewable as to the mail subject etc. But when we click on the mail to view, it ends up with 404 PAGE NOT FOUND.     

Been trying to find a solution, but reaching no-where. What is needed so that I can enable the mail preview on the ECP itself rather than downloading and why do I get this 404 page not found ?    

Any leads, solution would be highly appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-16*

Hi @PD   ，  

You means that could create a eDiscovery and download the result and view it. Also could open the Preview search results but open the mail failed. Please correct me if I understand wrong.  

What’s your Exchange version is? If it is not the latest version, try to upgrade.  

Could you log in to the OWA of the user who created this eDiscovery normally?  

According to the error information, It may be caused by OWA authentication failure. Please following the steps and see if the issue is resolved.  

1.Please try to change the another browser.

2.Please make sure that the authentication is set to Basic Authentication and Forms Authentication is disabled on OWA and ECP virtual directly in IIS. After the above settings, please restart IIS by running IISReset /noforce command.  

3.Please run the following command to check settings of OWA virtual directory. Screenshot below is the default settings in my lab environment.

```
Get-OwaVirtualDirectory | fl server,*url*,*auth*
```

  

For more information: View or configure Outlook on the web virtual directories in Exchange Server

4.Please try to run the following command to reenabling the forms based authentication for OWA virtual directory and restart IIS by running IISReset /noforce command. Then you also could recycle the app pools for OWA in application pool in IIS. Try to view the mail again.

```
Set-OWAVirtualDirectory -Identity "<> (Default Web Site)" -FormsAuthentication $False -BasicAuthentication $True  
Set-OWAVirtualDirectory -Identity "<> (Default Web Site)" -FormsAuthentication $true -BasicAuthentication $True
```

5.Please run UpdateCas.ps1 and UpdateConfigFiles.ps1 from the exchange bin directory C:\Program Files\Microsoft\Exchange Server\V15\Bin. And please run the IISRESET in CMD start as administrator to restart IIS.

6.You could run the following command to remove and re-create the OWA virtual directory.

```
Remove-OWAVirtualDirectory  
New-OWAVirtualDirectory
```

For more information：New-OwaVirtualDirectory

In addition, please try to reproduce the problem and check whether there are related error logs in the event viewer. If it exists, please share it with us. It should be noted that it covers your personal information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
