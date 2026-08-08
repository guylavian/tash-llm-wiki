---
title: "HTTP ERROR 500 in Hybrid Exchange ECP/EAC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1291767/http-error-500-in-hybrid-exchange-ecp-eac
question_id: 1291767
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# HTTP ERROR 500 in Hybrid Exchange ECP/EAC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1291767/http-error-500-in-hybrid-exchange-ecp-eac (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I need assistance opening my Exchange Hybrid (Microsoft Exchange Server 2013 Cumulative Update 23) ECP browser. I get an error "The website cannot display the page This error (HTTP 500 Internal Server Error) means that the website you are visiting had a server problem that prevented the webpage from displaying. For more information about HTTP errors, see Help." My path is https://<server name>/ecp/ExchClientVer=15 .  I've turned on all the Microsoft Exchange services.  My EMS is working and only the ECP is not.  I also tried a different browser like Google and had the same result "This page isn't working, <server name> is currently unable to handle this request HTTP ERROR 500." Exchange Hybrid is running on Windows Server 2012 R2 (VM) and also has IIS.  

Finally, (Separate question) is it possible to use Exchange Management Shell on a Local Machine remotely? For example, install EMS on my Windows 10 machine and work from there instead of logging on directly to the Exchange Hybrid to open the EMS. Is there an EMS tool that I can download and install in my local machine? 

Your input is greatly appreciated.  Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-26*

Have you tried:

https://docs.microsoft.com/en-us/exchange/troubleshoot/administration/cannot-access-owa-or-ecp-if-oauth-expired#resolution

Or if the bindings on the exchange backend are correct?

https://docs.microsoft.com/en-us/answers/questions/203118/error-500-exchange-2016.html

Also, check this article - https://www.stellarinfo.com/blog/exchange-server-http-500-error-ecp/

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-26*

Hi @A_Lop  ,

Colud you please tell me if your owa can access normally?

-  When accessing ecp fails, please check the application log for Event ID 1309. This issue occurs if SharedWebConfig.config is missing from either of the following locations:C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxyC:\Program Files\Microsoft\Exchange Server\V15\ClientAccess.Event ID 1309 and you can't access OWA and ECP after you install Exchange Server 2016 or Exchange Server 2013 - Exchange | Microsoft Learn

-  You can try to check whether the path under BinsearchFolder of ECP Virtual directory is correct in IIS Manager. If not, please modify it and use the UpdateConfigFiles.ps1 and UpdateCAS.ps15 PowerShell scripts to update the server configuration.OWA or ECP stops working after you install a security update - Exchange | Microsoft Learn

-  Finally you can try to re-create/reset the IIS virtual directories.

https://theitbros.com/recreate-owa-ecp-virtual-directories-exchange-server-2016/

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

You can install Exchange 2013 management tools on other devices, but there is no win10 among the supported operating systems.

https://learn.microsoft.com/en-us/exchange/install-the-exchange-2013-management-tools-exchange-2013-help,

https://learn.microsoft.com/en-us/exchange/exchange-2013-system-requirements-exchange-2013-help#supported-operating-systems-for-exchange-2013

On win10 you can use power shell to connect to Exchange servers and run Exchange commands.

https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-servers-using-remote-powershell?view=exchange-ps

Best Regards,

Dezhi

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation](https://aka.ms/msftqanotifications)"https://aka.ms/msftqanotifications)") to enable e-mail notifications if you want to receive the related email notification for this thread.
