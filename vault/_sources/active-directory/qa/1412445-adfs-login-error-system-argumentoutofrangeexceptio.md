---
title: "ADFS Login error System.ArgumentOutOfRangeException: Not a valid Win32 FileTime."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1412445/adfs-login-error-system-argumentoutofrangeexceptio
question_id: 1412445
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# ADFS Login error System.ArgumentOutOfRangeException: Not a valid Win32 FileTime.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1412445/adfs-login-error-system-argumentoutofrangeexceptio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Dynamics CRM application hosted in Domain A with ADFS and Users are available in Domain A and Domain B. One Way Forest Trust with Selective Authentication is configured between the forests.

As Selective Authentication is enabled, we provided 'Allowed to Authenticate' permissions for the Domain B Domain users group on the Domain A Computer accounts where the application is hosted.

We are able to login to the Dynamics CRM application with users from Domain A. However, we get the below error message when we try to access the application with users in Domain B.

```
ServiceHostManager.LogFailedAuthenticationInfo: Token of type 'http://schemas.microsoft.com/ws/2006/05/identitymodel/tokens/UserName' validation failed with following exception details:System.ArgumentOutOfRangeException: Not a valid Win32 FileTime.Parameter name: fileTime   at System.DateTime.FromFileTimeUtc(Int64 fileTime)   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetPasswordExpiryDetails(SafeLsaReturnBufferHandle profileHandle, DateTime& nextPasswordChange, DateTime& lastPasswordChange)   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)   at Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateTokenInternal(UsernameAuthenticationContext usernameAuthenticationContext, SecurityToken token)   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)
```

## Answers

_No answers on this thread._
