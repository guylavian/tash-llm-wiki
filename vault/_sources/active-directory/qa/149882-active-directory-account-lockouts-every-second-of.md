---
title: "Active Directory Account Lockouts Every Second of the Day"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/149882/active-directory-account-lockouts-every-second-of
question_id: 149882
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory Account Lockouts Every Second of the Day

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/149882/active-directory-account-lockouts-every-second-of (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,  

Since last week ago I’m struggling with my Active Directory Account Lockouts  

I have read all the possible answers on MWG Forums, Tech Support, Sys Admin and Microsoft Forms also.  

 Till now I find myself in the middle of nowhere. So I decided to post here once again the question if anyone has experienced this before and how it has been solved  

 Note: In all the previous questions marked as solutions I could not find anything useful  

 So below I will describe my situations:  

```
Last week ago I changed my windows AD credentials due to expiry date
Since that moment I keep getting locked every second !
If I want to be unlocked the sys admin should be on the phone with me. They need to click on OK and unlock my user and me at the same time I should click OK in order to login !
```

Without this synchronization it is not possible since my user is getting locked two frequently  

```
I have changed the password four time but no result
From the logs of AD, on event 4740 I can see only that the caller computer name is MWG ( which is our proxy web gateway server )
Our Proxy ( MWG ) is joined into domain ( using NTLM2 method )
I have tried to enable on MWG the bad password logs but nothing useful can be found from there
I keep getting the popup from proxy (MWG)
I keep getting locked
I have logged on every possible server with rdp and sign out from there from my user
I have check all the possible logs from AD but the only thing that I keep looking is: Caller computer name MWG
```

%NICWIN-4-Security_4776_Microsoft-Windows-Security-Auditing: Security,rn=506628954 cid=9316 eid=728,Mon Nov 02 12:28:46 2020,4776,Microsoft-Windows-Security-Auditing,,Audit Failure,Credential Validation,The computer attempted to validate the credentials for an account. Authentication Package: MICROSOFT_AUTHENTICATION_PACKAGE_V1_0 Logon Account: UserName Source Workstation: McAfeeNew Error Code: 0xC0000234  

```
Tech Support of MWG is saying that is not MWG which is looking my AD credentials but another computer
I believe the opposite:  maybe on another workstations where the pop up of MWG has appeared I may have inputed my AD credentials
I have checked on all servers and my workstation for Windows Credentials ( like everyone) is suggesting but nothing is shown there.
I have used Netwrix_Account_Lockout_Examiner on our Domain Controller but I could find nothing
```

I found some task scheduler on my PC with my UserName wich I have disabled but it is not working  

Since Netwrix_Account_Lockout_Examiner is using event viewer logs I find it useless  

Please could you help me ?  

Has anyone faced this before ? Maybe it is better to close my UserName but I find it not a good solution  

Thank Youuuu

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-11*

Hello, yes I found it finally :) :) :)   

It was inserted on one of our system in order to authenticate against the proxy server  

I found it by accident :)

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-04*

Hello,    

Thank you so much for posting here.    

This event 4776 generates every time that a credential validation occurs using NTLM authentication. It shows successful and unsuccessful credential validation attempts. The error code 0xC0000234 means "Account logon with account locked."    

Through the 4776 event log, we can obtain the address of the Source workstation (McAfeeNew), log in to the computer and refer to the following steps to check:    

• Check the credential management to see if there are cached user’s old credentials    

• Check whether there is a wrong password to mount the network disk    

• Check whether the user has used the wrong password to start services, run scheduled tasks, etc.    

• Are there other third-party programs that cache the user's wrong password    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
