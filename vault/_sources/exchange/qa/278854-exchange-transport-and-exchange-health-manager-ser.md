---
title: "Exchange Transport and Exchange Health Manager service stuck in a starting state"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/278854/exchange-transport-and-exchange-health-manager-ser
question_id: 278854
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Transport and Exchange Health Manager service stuck in a starting state

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/278854/exchange-transport-and-exchange-health-manager-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello We seem to be getting a issue where once we patched one of our Windows Server 2016 Exchange 2016 CU19 exchange servers yesterday with the latest Windows Updates, the Exchange Transport and Exchange Health Manager services are now stuck in a starting state and never go into the running state. We have restarted the server many times, restarted the domain controller in the same site, uninstalled a couple of the updates on the exchange server however this has not helped! See attached pictures of the updates installed, a couple of events we get when we force stop and start the transport service and a picture of the starting state of the transport service. Thanks Charlei[69634-pic1.png][1]![69651-pic2.png][2]![69558-pic3.png][3]![69559-pic4.png][4] [1]: /api/attachments/69634-pic1.png?platform=QnA [2]: /api/attachments/69651-pic2.png?platform=QnA [3]: /api/attachments/69558-pic3.png?platform=QnA [4]: /api/attachments/69559-pic4.png?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-19*

Hi @CharlieRix   ,    

Did you try to manually stop the MS Exchange transport and Exchange health manager service and start it again?    

I noted that you has been uninstall a couple of updates, it’s include the latest Windows Updates?    

According to the error information, it’s could cause by service startup time is too long resulting in timeout, You can try to editing or creating the ServicesPipeTimeout DWORD value, the Service Control Manager timeout period can be overridden, thereby giving the service more time to start up and report ready to the Service. But it should be noted that if you modify the registry incorrectly, it will have a serious impact, so it is recommended that you back up in advance.    

-  Go to Start > Run > and type regedit    

-  Navigate to: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control    

-  With the control folder selected, right click in the pane on the right and select new DWORD Value    

-  Name the new DWORD: ServicesPipeTimeout    

-  Right-click ServicesPipeTimeout, and then click Modify    

-  Click Decimal, type '180000', and then click OK    

-  Restart the computer    

Please refer to:  How to back up and restore the registry in Windows    

In addition, if running a third-party anti-virus and anti-spam software, if possible, try to temporarily turn it off.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
