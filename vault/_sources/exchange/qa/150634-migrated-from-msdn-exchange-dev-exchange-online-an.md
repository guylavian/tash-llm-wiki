---
title: "[Migrated from MSDN Exchange Dev] Exchange Online and adding Exchange on-premise - Hybrid deployment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/150634/migrated-from-msdn-exchange-dev-exchange-online-an
question_id: 150634
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Exchange Online and adding Exchange on-premise - Hybrid deployment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/150634/migrated-from-msdn-exchange-dev-exchange-online-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.    

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/0190be6e-f778-4812-976d-430b61369a96/exchange-online-and-adding-exchange-onpremise-hybrid-deployment?forum=exchangesvrdevelopment     

Hello,    

we have from few years Exchange Online(we have added a few domain). We have too Azure AD with is synchronization with our local AD. We are preparing to deploy hybrid exchange configuration but before running the hybrid configuration wizard I want to make sure I haven't missed anything.     

I. Our Exchange Online configuration:    

aaa.org (AD domain)    

bbb.com (domain)(default domain on Exchange Online)    

ccc.com (domain)    

Two connector to external mail server:     

-  first connector applies to the domain bbb.com    

-  second connector applies to the domain ccc.com    

II. Our local AD (aaa.org domain)    

The Schema AD for Exchange on-premise was extended and Exchange On Premise 2019 (as mailbox server) was installed. I installed certificate for aaa.org on Exchange server (certificate has ISS service now), and our server (for example OWA) is available from external network.     

And now i have a few question:    

1 . If i run the hybrid wizard may this affect to my current connectors to external server ?    

2 . I have read : https://learn.microsoft.com/en-us/exchange/hybrid-deployment-prerequisites, and i have question about:    

Autodiscover DNS records:    

on my Exchange On-Premise server i have set autodiscover as https://exchangeserver.aaa.org/Autodiscover/Autodiscover.xml. On my DNS i created one rekord A which is ponting to public IP Address of my exchange on premise server. Do i have to add anything else?    

3 . How i Can add additional domain to my exchange on-premise server ? In this moment a have added only ma Active Directory Domain.    

Thank you in advance for your help,    

Tom

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-04*

Why do you want to deploy the hybrid?  

Do you have any mailboxes on on-premises Exchange?

For your questions:  

-  Are these two connectors created on Exchange Online, and used to send emails from different SMTP address?  

HCW helps to create connectors for mail flow between on-premises Exchange and Exchange Online. If your connectors are created on Exchange Online and no on-premises mailboxes use bbb.com or ccc.com, your connectors won't be affected.

2) The url you provided "https://exchangeserver.aaa.org/Autodiscover/Autodiscover.xml" looks like the SCP record, am I right?  

If you have on-premises mailboxes, yes, you should make autodiscover.aaa.org pointed to the public IP of your on-premises Exchange server.  

If you don't have on-premises mailboxes, you should create the CNAME record to make autodiscover.aaa.org points to autodiscover.outlook.com. Also, you should set the SCP to $null.

3) Do you mean you want to add bbb.com and ccc.com to on-premises Exchange? Why do you want to add them to on-premise organization?  

To add additional domains, you have to add accepted domains. For your reference: Accepted domains in Exchange Server.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
