---
title: "Error in servidor Exchange 2016 / ECP CU19"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/328037/error-in-servidor-exchange-2016-ecp-cu19
question_id: 328037
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Error in servidor Exchange 2016 / ECP CU19

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/328037/error-in-servidor-exchange-2016-ecp-cu19 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi dear,   

I have a problem on my Servers Exchange 2016, after the installation of CU19 made available by Microsoft I am no longer able to access the virtual ecp, presents the message below An exception occurred processing while your request. Additionally, another exception occurred while executing the custom error page for the first exception. The request has been terminated. I performed the analysis for OwaVirtualDirectory and EcpVirtualDirectory and the auth options are identical. I can access OWA in browser but the ECP does not. I would very much like the support of Mr(a)s. Thank you

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-25*

Hi @Alex Vieira  ,    

Thanks for the response.     

May I know if you have also applied the latest security update(KB5000871) after upgrading to CU19? If yes, how did you install the patch?     

Considering that as stated in the known issues section in the link earlier, OWA or ECP might stop working if the SU is installed by directly double-clicking it, so if that is your case, it's recommended to try reinstalling the SU using elevated permissions and see the result.    

If issue persists, please check the IIS Settings for ECP Virtual Directories Path using the steps below:    

 1.Start IIS Manager on the server. Navigate to Exchange Backend website > ECP Virtual directory, select Application settings > BinsearchFolder.     

 2.If the directory paths resemble the following:    

```
%ExchangeInstallDir%bin;%ExchangeInstallDir%bin\CmdletExtensionAgents;%ExchangeInstallDir%ClientAccess\Owa\bin
```

Please replace them with the paths below and then restart IIS to check the result:    

Note: The paths must point to where Exchange Server is installed. The following examples assume that the program is installed on drive C. If it is installed on a different drive on your server,then you would need to use the path that's appropriate for your installation.    

```
C:\Program Files\Microsoft\Exchange Server\V15\bin;C:\Program Files\Microsoft\Exchange Server\V15\bin\CmdletExtensionAgents;C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\Owa\bin
```

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
