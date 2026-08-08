---
title: "Installation of Exchaneg 2016 in Exchange 2010 Enviornment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/198584/installation-of-exchaneg-2016-in-exchange-2010-env
question_id: 198584
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Installation of Exchaneg 2016 in Exchange 2010 Enviornment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/198584/installation-of-exchaneg-2016-in-exchange-2010-env (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts,  

I am trying to install Exchange 2016 in co-exist environment of Exchange 2010. I have a hybrid environment with Office 365 and I wanted to build Exchange 2016 and decommission Exchange 2010 servers. However I try to install Exchange 2016, I got a message that you have one Exchange 2007 legacy server that must be upgraded to remove in order to install Exchange 2016.  

I have DAG and CAS load balancing servers but I removed DAG and also deleted CAS Loan balancer but still having the same message. I found cluster virtual server in AD and manually deleted that but still receiving the same error message.   

I have run ASDI edit utility and found the cluster server still exist. I can delete the cluster server name and continue the installation but I seek your advise regarding the entire scenario.  

I will appreciate any advise and help in this respect.  

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-28*

Hi Kyle,  

Thanks again for your reply but I need to understand why you are asking me to stop AAD connect, then rebuild the local domain ? I have been using AAD connect prior to Hybrid setup as we are using office 365 other Apps.  

Can you please also explain why does rebuilt the local domain require ?  

Thx  

NAV

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

anonymous user     

Based on your description, I think you may not uninstall the Exchange 2007 server in the correct way before(Uninstall from Control Panel). So, there still exist residual information in AD.     

In this way, you can only to remove Exchange 2007 from ADSI(Isn't suggested and supported), this article may be help to you. About removing Windows cluster from your organization, you may need to confirm with the Windows server teams.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Here may be a workaround may be useful to you:    

-  Move all mailboxes to Exchange online.    

-  Remove hybrid configuration from Exchange 2010 and remove local Exchange and AD.    

-  Rebuild a local AD and install Exchange 2016.    

-  Hybrid with Office 365 and writeback AD account to local AD.    

This suggestion may be more complicated, but it can completely delete the remaining information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
