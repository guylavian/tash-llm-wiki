---
title: "ADFS Extranet Smart Lockout - Users cannot be unlocked with powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/192958/adfs-extranet-smart-lockout-users-cannot-be-unlock
question_id: 192958
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Extranet Smart Lockout - Users cannot be unlocked with powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/192958/adfs-extranet-smart-lockout-users-cannot-be-unlock (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are using ADFS on Windows Server 2019. External login to O365 will authenticate via this ADFS server instead of Azure AD.    

Recently we have been trying on the Extranet Smart Lockout feature.    

In order to see how it would work, we have set the lockout mode to enforce.    

```
set the ExtranetLockoutMode to 
```

Things seems to work as expected, except for one issue - when a user got locked, we cannot unlock the account via powershell.    

Here's the scenario.    

-  We intentionally logging in an account with false password to trigger a lockout.     

```
PS C:\Users\administrator.contoso> Get-AdfsAccountActivity -Identity ******@contoso.com  

Identifier             : contoso\Extest01  
BadPwdCountFamiliar    : 6  
BadPwdCountUnknown     : 0  
LastFailedAuthFamiliar : 12/5/2020 5:18:11 PM  
LastFailedAuthUnknown  : 12/5/2020 4:51:56 PM  
FamiliarLockout        : True  
UnknownLockout         : False  
FamiliarIps            : {202.xxx.xxx.109}
```

-  Then we try to unlock it by the following script. (As it is a FamiliarLockout, we added the parameter -Location Familiar)    

```
PS C:\Users\administrator.contoso> Reset-AdfsAccountLockout ******@contoso.com -Location Familiar
```

-  It is verified that the account has been unlocked using powershell.    

```
PS C:\Users\administrator.contoso> Get-AdfsAccountActivity -Identity ******@contoso.com  

Identifier             : contoso\Extest01  
BadPwdCountFamiliar    : 0  
BadPwdCountUnknown     : 0  
LastFailedAuthFamiliar : 12/5/2020 5:18:11 PM  
LastFailedAuthUnknown  : 12/5/2020 4:51:56 PM  
FamiliarLockout        : False  
UnknownLockout         : False  
FamiliarIps            : {202.xxx.xxx.109}
```

-  However, we try logging in again with the correct password, it is still not able to login.    

-  We also tried logging from internal network, it worked. So the account is not locked in AD.    

Please help to see if there is anything missing here. Thanks in advanced.    

Additional information.    

We have set the ESL via the following powershell:    

```
Set-AdfsProperties -EnableExtranetLockout $true -ExtranetLockoutThreshold 3 -ExtranetObservationWindow (new-timespan -Minutes 10) -ExtranetLockoutRequirePDC $false
```

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-11*

Anyone has an idea?
