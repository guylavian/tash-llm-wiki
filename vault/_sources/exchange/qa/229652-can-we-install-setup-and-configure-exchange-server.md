---
title: "Can we install, setup and configure Exchange Server 2019 at Microsoft Azure?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/229652/can-we-install-setup-and-configure-exchange-server
question_id: 229652
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Can we install, setup and configure Exchange Server 2019 at Microsoft Azure?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/229652/can-we-install-setup-and-configure-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

For installation, setup and configuration Exchange Server 2019; it is recommended to use member server.  

And because of various reasons, hardware specification of member server should be high.  

Therefore, we need two systems one for Active Directory-Domain Controller and another for member server.     

Please let me know, can I go for one of following options:  

Option1: AD-DC system is on-premises and member server is at Azure.  

Option2: both systems (AD-DC and member server) are at Azure.  

If I can go for either option1 or option2, I think there will be connectivity like below:  

For option1, premises to Azure’s one region.  

For option2, premises to Azure’s two regions, if AD-DC and member server are at different regions.  

Apart from connectivity between Azure’s region(s) and premises, please let me know, how deployment of Exchange Server 2019 at premises differs from deployment at Azure?  

Please elaborate and advise. In advance, thank you for giving your time.  

With Regards  

NndnG

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-14*

Hi @NndnG       

Yes, we can deploy Exchange server in Azure, make sure the AD-DC and member servers in the same network. And meet the requirements list in Exchange Server virtualization     

It is suggested to refer to the official document which gives a detailed introduction about Exchange dev/test environments in Azure    

In addition, here is the video series about Exchange 2019: Building an Exchange lab in Azure    

For more information about the connectivity between Azure and on-premise, contacting the azure froum will be a good idea, or we can add the Azure related tag in the original post above. They will give you more professional suggestions about this part.     

At last, you could also consider buying O365 subscription for your organization like this thread discussed: Exchange Server on Azure VM    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
