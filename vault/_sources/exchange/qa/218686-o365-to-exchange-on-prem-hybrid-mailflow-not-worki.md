---
title: "O365 to Exchange On prem Hybrid Mailflow not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/218686/o365-to-exchange-on-prem-hybrid-mailflow-not-worki
question_id: 218686
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# O365 to Exchange On prem Hybrid Mailflow not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/218686/o365-to-exchange-on-prem-hybrid-mailflow-not-worki (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,  

We have an exchange migration project going on where from one site (Datacenter) to another site (Datacenter) migration is happening. So we built new Exchange servers in new site in the same forest, configured the same. Mailboxes have been migrated to the new servers too.  Hybrid configuration wizard has been run adding new set of servers to Hybrid configuration. Now old Load balancer settings have been replicated to the new site's LB. Now when we are removing old exchange servers and keeeping only new, mail from O365 to On premise not working. Mail trace shows on O365 below error:  

'[{LED=450 4.4.316 Connection refused};{MSG=Socket error code 10061};{Last attempted server name=Hybrid.ourdomain.com}  

Doing a bit google, it says that it could be firewall issue. But as per N/w all ports are opened. Old servers working when put behind Load balancer but not with the new servers.   

Is there anything from Exchange server's standpoint we are missing? We are thinking to use one of the OLD server IP addresses in the new server to eliminate the network issue if there are any.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-08*

Hi @GoodResource   ,    

Can this new Exchange server receive other external mail?    

-  Did any error messages appear when you configured HCW? You can verify the success of the hybrid deployment through the methods in this article    

-  For newly created Exchange server, is it a new DNS record added? If so, ensure that the DNS records are correct as mentioned above.    

-  In order to better solve the issue, if possible, please provide the complete NDR, which will provide more information. But it should be noted that covering the personal information.    

-  For whether the mail can reach the on-premises Exchange organization, you can first get it from the NDR and check "Generating server", If it shows the on-premises Exchange server, it means that the mail cannot be delivered after reaching the on-premises Exchange. If you want to understand the entire transport process of emails, I think you need to communicate with the network team to grab the network packets for viewing.    

-  As to whether the problem must be caused by the firewall, we can only judge by the error message. If we want to confirm,  still need to check the firewall log and related settings.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-06*

Hi @GoodResource   ,  

Could the mail from on-premises Exchange to Exchange online working?  

1.According to search the information you provided, as you know, error 10061 indicates that the connection was refused, so it is very likely that the firewall caused the issue. Please check the firewall settings to make sure connections from Exchange Online IP addresses are not blocked to your on-premises organization. If possible, please check the firewall log to see if there are any related records about the refused connection.  

For a list of the Microsoft 365 IP addresses, you could refer to: Office 365 URLs and IP address ranges

2.Please make sure that publish the correct DNS records.  

3.If you are running a third-party antivirus software, if possible, please turn it off temporarily.  

4.Please make sure that the certificate used to encrypt the communication between Exchange online and on-premises Exchange is valid.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
