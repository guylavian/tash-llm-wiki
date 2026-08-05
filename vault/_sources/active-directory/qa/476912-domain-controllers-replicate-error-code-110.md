---
title: "Domain Controllers replicate error code 110"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/476912/domain-controllers-replicate-error-code-110
question_id: 476912
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain Controllers replicate error code 110

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/476912/domain-controllers-replicate-error-code-110 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,     

I need some advice here, as the current environment contain Parent domain & 2 child domains. Due to some security policy RC4 has been disabled for all domain controllers. I noticed while doing health check or manual repadmin /replsum etc.     

Seem to getting AD health check is unhealthy.     

[DC2] DsBindWithSpnEx() failed with error 5,    

         Access is denied..  

         Warning: DC2 is the Schema Owner, but is not responding to DS RPC Bind.  

[DC1] DsBindWithSpnEx() failed with error 5,    

         Access is denied..  

         Warning: DC1 is the PDC Owner, but is not responding to DS RPC Bind  

Does it necessary to enable AES Encryption?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-07-23*

Hello @Anonymous   ,    

I read up some of the blog related to RC4 disabled.     

-  RC4 is disabled in registry & GPO is set to not defined. Necessary to enable AES in GPO?    

-  I noticed enterprise admin accounts, login to server need to run as different users to authenticate. In order to access dsa.msc or even     

     run cmd or powershell with privileges' access to perfrom repadmin /replsum  

-   RC4 is disabled. Does domain or service account need to enable AES?    

-  How to check on the logs if there is error on RC4 Kerberos or KDC ticket is expired?    

https://learn.microsoft.com/en-us/answers/questions/377020/if-we-disable-rc4-encryption-in-gpo-domain-level-i.html

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-07-21*

Hello @Anonymous      

Seem to be permission issues. Even with enterprise admin run cmd as administraor will show replicate 110 error same for above screenshot.     

If i launch those application, dsa.msc, cmd or domain trust etc - without prompt for authentication will get access denied.     

Some sort of permission issues.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-07-21*

Hello @Anonymous       

Below is the setting, does it mean RC4 & AES is enabled?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-19*

Hello @RussellAng-0425,    

Thank you for your confirmation.    

Does it necessary to enable AES Encryption?    

A: Because DC supports RC4, AES 128 and AES 256, if you disable RC4, please enable AES Encryption, then check if AD replication will work fine.    

    

Hope the information above is helpful to you.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-16*

Hello @RussellAng-0425,  

Thank you for posting here.  

To better understand your question, please confirm the following information at your convenience.  

1.Based on the description "Due to some security policy RC4 has been disabled for all domain controllers.   

", how did you disable RC4 for all DCs?  

2.Did you mean AD replication works fine before disabling RC4 for all DCs?  

3.Where did you see "Domain Controllers replicate error code 110", please provide the screenshot if possible.  

You can enable RC4 for all DCs if possible and then check if AD replication will become healthy again.  

Hope the information above is helpful to you.  

Should you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou  

============================================  

If the Answer is helpful, please click "Accept Answer" and upvote it.
