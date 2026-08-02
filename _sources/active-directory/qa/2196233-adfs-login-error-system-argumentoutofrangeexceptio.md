---
title: "ADFS Login error System.ArgumentOutOfRangeException: Not a valid Win32 FileTime."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196233/adfs-login-error-system-argumentoutofrangeexceptio
question_id: 2196233
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# ADFS Login error System.ArgumentOutOfRangeException: Not a valid Win32 FileTime.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196233/adfs-login-error-system-argumentoutofrangeexceptio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Dynamics CRM application hosted in Domain A with ADFS and Users are available in Domain A and Domain B. One Way Forest Trust with Selective Authentication is configured between the forests. 

As Selective Authentication is enabled, we provided 'Allowed to Authenticate' permissions for the Domain B Domain users group on the Domain A Computer accounts where the application is hosted.

We are able to login to the Dynamics CRM application with users from Domain A. However, we get the below error message when we try to access the application with users in Domain B.

```
ServiceHostManager.LogFailedAuthenticationInfo: Token of type 'http://schemas.microsoft.com/ws/2006/05/identitymodel/tokens/UserName' validation failed with following exception details:System.ArgumentOutOfRangeException: Not a valid Win32 FileTime.Parameter name: fileTime   at System.DateTime.FromFileTimeUtc(Int64 fileTime)   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetPasswordExpiryDetails(SafeLsaReturnBufferHandle profileHandle, DateTime& nextPasswordChange, DateTime& lastPasswordChange)   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)   at Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateTokenInternal(UsernameAuthenticationContext usernameAuthenticationContext, SecurityToken token)   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-02*

Hello Manoj.Batchu,  

Thank you for posting in Microsoft Community forum.  

  ****From the description above, I understand your question is related to ADFS.  ****

Since there are no engineers dedicated to ADFS in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and select "Active Directory Federation Services" tag or any other tag related to your products.  

  ****I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
