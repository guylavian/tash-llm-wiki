---
title: "Domain Controller Upgrade from Windows Server 2012 R2 to Windows Server 2019:  In-Place or Side-by-Side, Can Evaluation License be Used?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188973/domain-controller-upgrade-from-windows-server-2012
question_id: 2188973
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: []
---
# Domain Controller Upgrade from Windows Server 2012 R2 to Windows Server 2019:  In-Place or Side-by-Side, Can Evaluation License be Used?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188973/domain-controller-upgrade-from-windows-server-2012 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm doing work for a small business that has a single server running Windows Server 2012 R2.  It is the domain controller and runs DHCP, DNS, and is their file server.  I have purchased the 2019 license and CALs, and we are ready to upgrade.  However, Microsoft documents state that a side-by-side upgrade is preferred for domain controllers.  This process would require a second Windows server that I would promote to a DC, but I don't have one.  My thought is that I could install 2019 on a desktop using an evaluation license, promote it to a DC, migrate all the FSMO roles to it, upgrade the 2012 R2 server, migrate the FSMO roles back, demote the desktop, then re-image it with Windows 10/11.  This entire process could be done within a few days.  The only problem is, I'm not sure it's possible and/or legal to do so.  Does anyone have any insight on this scenario?

Thanks for any assistance!

## Answer (community) — community member

*upvotes: 1 · updated: 2023-10-09*

Hello Mike Frazer,  

Thank you for posting in Microsoft Community forum.  

The recommended method is adding new 2019 server to domain and promoting this 2019 server to Domain Controller, we do not recommend to perform in-place upgrade OS from 2012 R2 to 2019.  

Prerequisites 

1.Review Windows Server 2019 release notes and system requirements.  

2.Register, then download and install. (Note: This evaluation edition expires in 180 days.)  

3.Receive emails with resources to guide you through your evaluation.  

Installation Guidelines 

After installation, install the latest servicing package.  

1.Go to: Microsoft update catalog and search for "Windows Server 2019”.  

2.Evaluation versions of Windows Server must activate over the internet in the first 10 days to avoid automatic shutdown.   

For more information about Evaluation versions of Windows Server 2019, please view link below.  

Windows Server 2019 | Microsoft Evaluation Center  

Please note:   

You may encounter any issue during the upgrade of 2012 R2 server, please had better back up all the data about domain controller (using built-in Windows backup role to back up), DHCP, DNS, and file server on this 2012 R2 server.  

Meanwhile, here is a thread about best way to upgrade windows server 2012 r2 domain controllers to 2019 domain controllers, step by step.  

What is the best way to upgrade windows server 2012 r2 domain - Microsoft Community  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
