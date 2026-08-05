---
title: "Exchange 2016 Autodiscover: some Outlook 2019 users get 503 error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/291861/exchange-2016-autodiscover-some-outlook-2019-users
question_id: 291861
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 Autodiscover: some Outlook 2019 users get 503 error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/291861/exchange-2016-autodiscover-some-outlook-2019-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

-Test Email Autoconfiguration-  

We have Exchange on premise with 2010 and 2016 servers.  Autodiscover appears to not work for some users   

test-outlookwebservices          autodiscover: Outlook provider SUCCESS  but another user has failure  

                          service endpoint:         exchangeserver2   (same for both users)

If I go to the webpage in a browser  

https://exchangeserver2.company.local/Autodiscover/Autodiscover.xml for me it returns status 600 which Microsoft says is normal  

On another computer it returns 503.    All computers are connected to the domain.  

How can I go about troubleshooting this?   Are their some logs that I can look at for more information?  

Thanks,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-01*

Hi @J Hankins   ,    

Will the Test Email Autoconfiguration give a error message? What's the result for Ex 2010 and Ex 2016 users?     

The cmdlet Test-OultookWebServices could only work in Ex 2010.     

    

Also please check the SCP in ADSIEDIT:    

Connect to Configuration partition -> Servers -> Microsoft Exchange -> DomainName -> Administrative Groups -> Exchange Administrative Groups -> Servers -> ServerName(You may have two servers here, check both of them) -> Protocols -> Autodiscover -> ServerName -> right click and choose properties -> check the serviceBindingInformation, they should be https://FQDN/Autodiscover/Autodiscover.xml ( different for the two server)    

    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
