---
title: "How to Disable Exchange 2016(CU19) ECP External Access (Without breaking OWA)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/309389/how-to-disable-exchange-2016-cu19-ecp-external-acc
question_id: 309389
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# How to Disable Exchange 2016(CU19) ECP External Access (Without breaking OWA)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/309389/how-to-disable-exchange-2016-cu19-ecp-external-acc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support  

My Current infra  

1-Primary AD  

1-Secondary AD  

2-Child Domain   

2-RODC  

1-Standalone Exchange Server 2016(CU19)  

How to Disable Exchange 2016(CU19) ECP External Access (Without breaking OWA)   

it should be able to access internally ECP with same as External.  

Please share me step by step guide to avoid impact during Disabling EAC  

Also i read article says that it may break OWA during Disabling EAC  

Please advice

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-09-25*

FWIW i did it with a simple URL Rewrite Rule. I edited the web.config file by adding this rule and it works perfectly for my environment. No access to ECP from anywhere at all except from the Exchange Server itself. If you need to add additional IP addresses (maybe from a LAN PC) that you want to allow to have access to it, you can add  them after this line: <add input="{REMOTE_ADDR}" pattern="^127.0.0.1$" negate="true" />

```

        

        

            

            

        

        

    
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

@Sathishkumar Singh      

Here are step by step to disable EAC from accessed from external of your organization, you still could access it from the internal of your organization. It doesn't effect the using of OWA: Turn off access to the Exchange admin center    

You can also install an Exchange 2019，then using Exchange 2019 as the Internet facing server, the new function "Client Access Rules" is more easier to control the access of EAC.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
