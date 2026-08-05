---
title: "[Migrated from MSDN Exchange Dev] Warning on Exchange server 2010"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/138427/migrated-from-msdn-exchange-dev-warning-on-exchang
question_id: 138427
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] Warning on Exchange server 2010

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/138427/migrated-from-msdn-exchange-dev-warning-on-exchang (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] Warning on Exchange server 2010  

[Original post]  

Hi,   

We are getting the below warning when clicking Hub Transport option under Server Configuration in Exchange 2010. Could you please share some suggestions to resolve it?  

Warnings  

Get-ReceiveConnector  

Completed  

Warning:  

The object Ex2013\Default Frontend Ex2013 has been corrupted, and it's in an inconsistent state. The following validation errors happened:  

Warning:  

Could not convert property TlsDomainCapabilities to type SmtpReceiveDomainCapabilities.  

Error while converting string 'mail.protection.outlook.com:512:<I>CN=MSIT Machine Auth CA 2, DC=redmond, DC=corp, DC=microsoft,  

DC=com<S>CN=mail.protection.outlook.com, OU=Forefront Online Protection for Exchange, O=Microsoft, L=Redmond, S=WA, C=US'  

to result type Microsoft.Exchange.Data.SmtpReceiveDomainCapabilities: "mail.protection.outlook.com:512:<I>CN=MSIT Machine Auth CA 2,  

DC=redmond, DC=corp, DC=microsoft, DC=com<S>CN=mail.protection.outlook.com, OU=Forefront Online Protection for Exchange, O=Microsoft, L=Redmond, S=WA, C=US"  

isn't a valid list of SMTP Receive domain capabilities.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-26*

Hi,  

From your description and the warning message you shared, is the Exchange 2010 server coexistent with Exchange 2013? If this is the case, according to my research, this could be an expected behavior as  Ex2013\Default Frontend Ex2013 is only available in Exchange 2013 and may not be handled in Exchange 2010.   

Given this, normally this warning message can be safely ignored. And it's suggested to use the Exchange 2013 management tools instead.    

Here is a thread which discuss a similar warning for your reference: Exchange 2013 Hybrid Wizard  

By the way, please be aware that Exchange 2010 has end its support lifecycle, it's highly recommended to complete the migration to newer versions of Exchange and decommission Exchange 2010 as soon as possible.  

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
