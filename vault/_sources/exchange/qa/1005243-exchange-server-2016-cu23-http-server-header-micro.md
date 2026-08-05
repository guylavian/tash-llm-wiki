---
title: "Exchange Server 2016(CU23) \"http-server-header: Microsoft-IIS/8.5 – Only available on Microsoft Serveur 2012 R2 Last CVE is 2014 on IIS 8.5 Exploitation of recent CVE (ex : CVE 10-05-2022 with 9.0 CVE Score On Microsoft Serveur 2012 R2) \""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1005243/exchange-server-2016-cu23-http-server-header-micro
question_id: 1005243
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2016(CU23) "http-server-header: Microsoft-IIS/8.5 – Only available on Microsoft Serveur 2012 R2 Last CVE is 2014 on IIS 8.5 Exploitation of recent CVE (ex : CVE 10-05-2022 with 9.0 CVE Score On Microsoft Serveur 2012 R2) "

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1005243/exchange-server-2016-cu23-http-server-header-micro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All    

My Current Infra    

1-Primary Domain Controller    

1-Secondary Domain Controller + File Server    

2-RODC    

-  UK-RODC    

2 Child Domain    

1 Exchange Server 2016 (CU23) Standard Version (Standalone Server)    

Note from the pentest:    

"http-server-header: Microsoft-IIS/8.5 – Only available on Microsoft Serveur 2012 R2 Last CVE is 2014 on IIS 8.5    

Exploitation of recent CVE (ex : CVE 10-05-2022 with 9.0 CVE Score On Microsoft Serveur 2012    

R2) "    

https://stackoverflow.com/questions/67584329/how-to-hide-asp-net-technologies-from-wappalyzer-hosted-on-iis    

From above the link.    

I can able to see 1st point    

To stop this, able to remove the header:    

Open the IIS Manager.    

In the Connections tree, select the website that SS is running under.    

Click the HTTP Response Headers button on the right. The HTTP Response Headers panel appears.    

Click to select the X-Powered-By HTTP header.    

Click the Remove button in the Actions panel. The header disappears.    

-----------------------------------------------------------------------------------------------------------------------------------------    

    

2nd Point. i  don;t understand the changes what exactly to be done.  i don;t see any The HTTP header “X-ASPNET-VERSION"    

Hide the ASP.NET version. The HTTP header “X-ASPNET-VERSION” reveals the version of ASP.NET being used by the SS application pool. To stop this, remove the header:    

Open the web.config file, which is located in the root directory for the website.    

Inside the <system.web> tag, add the tag .    

Save the file.    

--------------------------------------------------------------------------------------------------------------------------------------------    

    

3rd Point. i don;t see in the registry DisableServerHeader it means need to be add this DisableServerHeader    

Hide the server type. The HTTP header line Server: Microsoft-HTTPAPI/2.0 is added to the header by the .NET framework. To remove that information, you must update the Windows registry:    

Open the Windows Registry Editor.    

Navigate to Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\HTTP\Parameters.    

Change the DisableServerHeader (REG_DWORD type) registry key from 0 to 1.    

Please advise without any impact Exchange Server

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-14*

Hi  @Sathishkumar Singh   ,    

"http-server-header: Microsoft-IIS/8.5 – Only available on Microsoft Serveur 2012 R2 Last CVE is 2014 on IIS 8.5    

Exploitation of recent CVE (ex : CVE 10-05-2022 with 9.0 CVE Score On Microsoft Serveur 2012    

R2) "    

I wonder where you got this error from ? Since different testing methods focus on different directions, it is recommended that you could use  healthchecker.ps1 to check that there are security vulnerabilities in your environment.    

In addition, I have referred to the method you provided and operated it in my lab. I got the same result as you . I also didn't find the HTTP header " X-ASPNET-VERSION" . Since this link is not officially provided by Microsoft, we cannot guarantee the accuracy and security of this method .    

I would suggest  that you could refer to the following link to update the Exchange Server Security Updates to the latest version to protect your environment.    

Released: August 2022 Exchange Server Security Updates - Microsoft Tech Community    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
