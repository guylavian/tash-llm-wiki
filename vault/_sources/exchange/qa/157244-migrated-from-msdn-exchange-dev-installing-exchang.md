---
title: "[Migrated from MSDN Exchange Dev]Installing Exchange 2013 in an additional server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/157244/migrated-from-msdn-exchange-dev-installing-exchang
question_id: 157244
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Installing Exchange 2013 in an additional server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/157244/migrated-from-msdn-exchange-dev-installing-exchang (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Hi Team,  

A simple query, we have already exchange 2013 infrastructure in place. We are building new Exchange 2013 servers in a new DC in the same forest/AD. My query is, while installing new Exchange servers, do i need to still run prepareschema, preparead commands from set up? As it is just an additional exchange server and necessary schema, domain and AD preparation is done already. Or should i just straight away run pre-requisites and install exchange?  

Regards BM

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-10*

Hi ,    

Yes, you still need to prepare Schema/AD/AD domain.    

Please run the following command to prepare Schema/AD/AD domain.    

```
Setup.exe /PrepareSchema /IAcceptExchangeServerLicenseTerms  
Setup.exe /PrepareAD /OrganizationName:"" /IAcceptExchangeServerLicenseTerms  
Setup.exe /PrepareAllDomains /IAcceptExchangeServerLicenseTerms
```

Then you can check whether the preparation is successful in ADSI.    

1）In the Schema naming context, verify that the rangeUpper property on ms-Exch-Schema-Verision-Pt is set to the value shown for your version of Exchange 2013 in the Exchange 2013 Active Directory versions table.    

2）In the Configuration naming context, verify that the objectVersion property in the CN=<your organization>,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=<domain> container is set to the value shown for your version of Exchange 2013 in the Exchange 2013 Active Directory versions table.    

3）In the Default naming context, verify that the objectVersion property in the Microsoft Exchange System Objects container under DC=<root domain is set to the value shown for your version of Exchange 2013 in the Exchange 2013 Active Directory versions table.    

For more information you could refer to:Prepare Active Directory and domains    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
