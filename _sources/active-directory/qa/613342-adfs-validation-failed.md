---
title: "adfs validation failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/613342/adfs-validation-failed
question_id: 613342
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# adfs validation failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/613342/adfs-validation-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm getting token validation failed to need to know how to fix this issue. What is causing this issue?  

Data  

The user name or password is incorrect  

Data  

System.IdentityModel.Tokens.SecurityTokenValidationException: iws.com\dhudson ---> System.ComponentModel.Win32Exception: The user name or password is incorrect at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserHandle(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, SafeCloseHandle& tokenHandle, SafeLsaReturnBufferHandle& profileHandle) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUser(UserNameSecurityToken token, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName) at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateTokenInternal(SecurityToken token) --- End of inner exception stack trace --- at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateTokenInternal(SecurityToken token) at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateToken(SecurityToken token) System.ComponentModel.Win32Exception (0x80004005): The user name or password is incorrect at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserHandle(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, SafeCloseHandle& tokenHandle, SafeLsaReturnBufferHandle& profileHandle) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName) at Microsoft.IdentityServer.Service.Tokens.LsaLogonUserHelper.GetLsaLogonUser(UserNameSecurityToken token, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName) at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateTokenInternal(SecurityToken token

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-04*

I was looking at this log that you wanted. The user name and password are correct. 100%. So what is cause it not recognizing the username and password.  

An account failed to log on.

Subject:  

Security ID: IWS\adfsservice  

Account Name: adfsservice  

Account Domain: IWS  

Logon ID: 0x20B329FE

Logon Type: 3

Account For Which Logon Failed:  

Security ID: NULL SID  

Account Name:  

Account Domain:

Failure Information:  

Failure Reason: Unknown user name or bad password.  

Status: 0xC000006D  

Sub Status: 0xC000006A

Process Information:  

Caller Process ID: 0x88c  

Caller Process Name: C:\Windows\ADFS\Microsoft.IdentityServer.ServiceHost.exe

Network Information:  

Workstation Name: IWS03ADFS  

Source Network Address: -  

Source Port: -

Detailed Authentication Information:  

Logon Process: W  

Authentication Package: Negotiate  

Transited Services: -  

Package Name (NTLM only): -  

Key Length: 0

This event is generated when a logon request fails. It is generated on the computer where access was attempted.

The Subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.

The Logon Type field indicates the kind of logon that was requested. The most common types are 2 (interactive) and 3 (network).

The Process Information fields indicate which account and process on the system requested the logon.

The Network Information fields indicate where a remote logon request originated. Workstation name is not always available and may be left blank in some cases.

The authentication information fields provide detailed information about this specific logon request.  

-  Transited services indicate which intermediate services have participated in this logon request.  

-  Package name indicates which sub-protocol was used among the NTLM protocols.  

-  Key length indicates the length of the generated session key. This will be 0 if no session key was requested.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-04*

The user name or password is incorrect.  

So you are sure that's not the problem?  

Can you show us the event 4625 generated at that time on the Security event log?
