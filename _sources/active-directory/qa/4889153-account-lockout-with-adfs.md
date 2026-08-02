---
title: "Account lockout with ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4889153/account-lockout-with-adfs
question_id: 4889153
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 5
qa_tags: []
---
# Account lockout with ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4889153/account-lockout-with-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day,

We have had a user that is locked out a few times a day.  The domain controller logs show the account tries to authenticate 5 times and then locks out.  Through the day, the account is authenticated unsuccessfully and most of the time does not reach 5 attempts
 before the 30 minute counter resets.  The 4740 MS Windows Security logs on the domain controller point to our ADFS server as the Caller Computer Name.

-
System

-
Provider
<br>
---
---
<br><br><br><br>
[ Name]
Microsoft-Windows-Security-Auditing
<br>
---
---
<br><br><br><br><br>
[ Guid]
{GUIDREDACTED}
<br>
---
---

EventID
4740
<br>
---
---
---

Version
0
<br>
---
---
---

Level
0
<br>
---
---
---

Task
13824
<br>
---
---
---

Opcode
0
<br>
---
---
---

Keywords
0x8020000000000000
<br>
---
---
---

-
TimeCreated
<br>
---
---
<br><br><br><br>
[ SystemTime]
2016-01-15T20:15:58.282955400Z
<br>
---
---

EventRecordID
31847
<br>
---
---
---

Correlation
<br>
---
---

-
Execution
<br>
---
---
<br><br><br><br>
[ ProcessID]
476
<br>
---
---
<br><br><br><br><br>
[ ThreadID]
1124
<br>
---
---

Channel
Security
<br>
---
---
---

Computer
DC.CORP.PRI
<br>
---
---
---

Security
<br>
---
---

-
EventData

TargetUserName
BILLYBOB

TargetDomainName
ADFSSERVER1

TargetSid
S-1-5-21-496199920-1230739820-379940124-1132

SubjectUserSid
S-1-5-18

SubjectUserName
DOMAINCONTROLLER1$

SubjectDomainName
CORP

SubjectLogonId
0x3e7

## Answer (community) — community member

*upvotes: 0 · updated: 2016-01-26*

We are still having lock out issues after enabled extranet, so it looks like a combination of internal and external sources are causing the issue.  I am going to open up a case with AD FS as you suggested.

## Answer (community) — community member

*upvotes: 0 · updated: 2016-01-25*

We don't currently have the extranet feature enabled, but are planning to do this now.  I was more or so looking for the root cause of the lockouts, but this tool should prevent them all together and make our environment safer from attacks.

## Answer (community) — community member

*upvotes: 0 · updated: 2016-01-23*

Hi Jim,  

Do you mean you have enabled the ADFS Extranet Lockout Protection as described in the article below?  

Enabling ADFS 2012 R2 Extranet Lockout Protection  

If yes, I’d like to explain that this feature is completely related to the on-premises ADFS configurations, but our community forum mainly focuses on the integration between on-premises ADFS and Office 365 online services. In order to provide you with the most
 dedicated assistance, I suggest you raise this question in the ADFS Support Forum. Thanks for your understanding.  

And if it’s not about what I mentioned above, please feel free to let me know with a more detailed description on how you configured the lockout deployment.  

Regards,  

Allen

## Answer (community) — community member

*upvotes: 0 · updated: 2016-01-22*

More information 

When we check the ADFS servers security logs we see the following log but have no idea what is actually trying to authenticate to the ADFS server with a bad password.  We enabled Failed Auditing on the ADFS server as well.  Here is the security logs from
 the ADFS server.

System 

 - Provider 

  [ Name]  AD FS Auditing 

 - EventID 411 

  [ Qualifiers]  0 

  Level 0 

  Task 3 

  Keywords 0x8090000000000000 

 - TimeCreated 

  [ SystemTime]  2016-01-22T23:22:39.002009500Z 

  EventRecordID 76101 

  Channel Security 

  Computer ADFSSERVER.CORP.PRI

 - Security 

  [ UserID]  S-1-GUID

-  EventData 

  00000000-0000-0000-0000-000000000000 

  schemas.microsoft.com/.../UserName 

  *** Email address is removed for privacy *** user name or password is incorrect 

  System.IdentityModel.Tokens.SecurityTokenValidationException: *** Email address is removed for privacy *** ---> System.ComponentModel.Win32Exception: The user name or password is incorrect at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserHandle(SafeHGlobalHandle
 pLogonInfo, Int32 logonInfoSize, SafeCloseHandle& tokenHandle, SafeLsaReturnBufferHandle& profileHandle) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange,
 DateTime& lastPasswordChange, String authenticationType, String issuerName) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUser(UserNameSecurityToken token, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)
 at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateTokenInternal(SecurityToken token) --- End of inner exception stack trace --- at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateTokenInternal(SecurityToken
 token) at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateToken(SecurityToken token) System.ComponentModel.Win32Exception (0x80004005): The user name or password is incorrect at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserHandle(SafeHGlobalHandle
 pLogonInfo, Int32 logonInfoSize, SafeCloseHandle& tokenHandle, SafeLsaReturnBufferHandle& profileHandle) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange,
 DateTime& lastPasswordChange, String authenticationType, String issuerName) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUser(UserNameSecurityToken token, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)
 at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateTokenInternal(SecurityToken token)

```
ADFS Applications and Servers Log

System 

 - Provider 

  [ Name]  AD FS 

  [ Guid]  {2FFB687A-1571-4ACE-8550-47AB5CCAE2BC} 

  EventID 342 

  Version 0 

  Level 2 

  Task 0 

  Opcode 0 

  Keywords 0x8000000000000001 

 - TimeCreated 

  [ SystemTime]  2016-01-22T23:31:56.873607700Z 

  EventRecordID 1058899 

  Correlation 

 - Execution 

  [ ProcessID]  3592 

  [ ThreadID]  4608 

  Channel AD FS/Admin 

  Computer ADFSSERVER.COMPANY.PRI

 - Security 

  [ UserID]  S-1-5GUID 

- UserData 

 - Event 

 - EventData 

  Data [schemas.microsoft.com/.../UserName](http://schemas.microsoft.com/ws/2006/05/identitymodel/tokens/UserName) 

  Data \*\*\* Email address is removed for privacy \*\*\* user name or password is incorrect 

  Data System.IdentityModel.Tokens.SecurityTokenValidationException \*\*\* Email address is removed for privacy \*\*\* ---> System.ComponentModel.Win32Exception: The user name or password is incorrect at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserHandle(SafeHGlobalHandle
 pLogonInfo, Int32 logonInfoSize, SafeCloseHandle& tokenHandle, SafeLsaReturnBufferHandle& profileHandle) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange,
 DateTime& lastPasswordChange, String authenticationType, String issuerName) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUser(UserNameSecurityToken token, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)
 at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateTokenInternal(SecurityToken token) --- End of inner exception stack trace --- at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateTokenInternal(SecurityToken
 token) at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateToken(SecurityToken token) System.ComponentModel.Win32Exception (0x80004005): The user name or password is incorrect at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserHandle(SafeHGlobalHandle
 pLogonInfo, Int32 logonInfoSize, SafeCloseHandle& tokenHandle, SafeLsaReturnBufferHandle& profileHandle) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange,
 DateTime& lastPasswordChange, String authenticationType, String issuerName) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUser(UserNameSecurityToken token, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)
 at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateTokenInternal(SecurityToken token)
```

We turned on AD FS Tracing Debug, but we are not seeing any good information here either.

AD FS Tracing Debug logs

-  System 

 - Provider 

  [ Name]  AD FS Tracing 

  [ Guid]  {0457a490-4d4d-4a5b-b639-35382f1b6709} 

  EventID 52 

  Version 0 

  Level 2 

  Task 0 

  Opcode 0 

  Keywords 0x8000000000000400 

 - TimeCreated 

  [ SystemTime]  2016-01-22T23:14:23.444506200Z 

  EventRecordID 3030 

  Correlation 

 - Execution 

  [ ProcessID]  3592 

  [ ThreadID]  5040 

  [ ProcessorID]  0 

  [ KernelTime]  0 

  [ UserTime]  1 

  Channel AD FS Tracing/Debug 

  Computer ADFSSERVER.CORP.PRI

 - Security 

  [ UserID]  S-GUID1234

-  UserData 

 - Event 

  EventData MSIS3144: MSISWindowsUserNameSecurityTokenHandler.ValidateToken: Incoming security token failed validation. *** Email address is removed for privacy *** user name or password is incorrect

I am at a loss on why this is happening.  I see that there are other users that are getting the same errors in the logs but not often enough to lock the accounts out.   We would really like to trace the device that is causing the lock outs so we can look
 in to the other bad password attempts with ADFS as well.

Thank you

Jim Webb
