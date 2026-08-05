---
title: "Exchange 2019 OWA/ECP ADFS gives hmac-sha1 errors in FIPS mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/519366/exchange-2019-owa-ecp-adfs-gives-hmac-sha1-errors
question_id: 519366
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management"]
---
# Exchange 2019 OWA/ECP ADFS gives hmac-sha1 errors in FIPS mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/519366/exchange-2019-owa-ecp-adfs-gives-hmac-sha1-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have successfully configured WAP and ADFS for claims based authentication to the ECP and OWA directories. I am able to successfully log in until I enable "System cryptography: Use FIPS compliant algorithms for encryption, hashing and signing." in the mailserver's group policy. FIPS mode is enabled on the WAP and ADFS servers, but when I enable it on the CAS/Mailbox servers, the connection fails.

I receive two errors as follows:

MSExchange Front End HTTP Proxy

EventID 1003

[Ecp] An internal server error occurred. The unhandled exception was: System.ArgumentException: ID6037: Cannot create algorithm with name 'http://www.w3.org/2000/09/xmldsig#hmac-sha1'.  

Parameter name: algorithm  

at Microsoft.IdentityModel.CryptoUtil.Algorithms.NewDefaultEncryption()  

at Microsoft.IdentityModel.Web.RsaEncryptionCookieTransform.Encode(Byte[] value)  

at Microsoft.IdentityModel.Tokens.SessionSecurityTokenHandler.ApplyTransforms(Byte[] cookie, Boolean outbound)  

at Microsoft.Exchange.Security.Authentication.AdfsSessionSecurityTokenHandler.ApplyTransforms(Byte[] cookie, Boolean outbound)  

at Microsoft.IdentityModel.Tokens.SessionSecurityTokenHandler.WriteToken(XmlWriter writer, SecurityToken token)  

at Microsoft.IdentityModel.Tokens.SessionSecurityTokenHandler.WriteToken(SessionSecurityToken sessionToken)  

at Microsoft.IdentityModel.Web.SessionAuthenticationModule.WriteSessionTokenToCookie(SessionSecurityToken sessionToken)  

at Microsoft.IdentityModel.Web.SessionAuthenticationModule.AuthenticateSessionSecurityToken(SessionSecurityToken sessionToken, Boolean writeCookie)  

at Microsoft.IdentityModel.Web.WSFederationAuthenticationModule.SignInWithResponseMessage(HttpRequest request)  

at Microsoft.IdentityModel.Web.WSFederationAuthenticationModule.OnAuthenticateRequest(Object sender, EventArgs args)  

at Microsoft.Exchange.Security.Authentication.AdfsFederationAuthModule.InternalOnAuthenticateRequest(Object sender, EventArgs eventArgs)  

at System.Web.HttpApplication.SyncEventExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()  

at System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)  

at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

ASP.NET 4.0.30319.0

EventID 1309

Event code: 3005  

Event message: An unhandled exception has occurred.  

Event time: 8/18/2021 5:45:48 PM  

Event time (UTC): 8/18/2021 9:45:48 PM  

Event ID: 714e4414463e446580a2b76abc9ed4b1  

Event sequence: 4  

Event occurrence: 1  

Event detail code: 0

Application information:  

Application domain: /LM/W3SVC/1/ROOT/ecp-1-132737966456709170  

Trust level: Full  

Application Virtual Path: /ecp  

Application Path: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp\  

Machine name: EPMX1

Process information:  

Process ID: 22544  

Process name: w3wp.exe  

Account name: NT AUTHORITY\SYSTEM

Exception information:  

Exception type: ArgumentException  

Exception message: ID6037: Cannot create algorithm with name 'http://www.w3.org/2000/09/xmldsig#hmac-sha1'.  

Parameter name: algorithm  

at Microsoft.IdentityModel.CryptoUtil.Algorithms.NewDefaultEncryption()  

at Microsoft.IdentityModel.Web.RsaEncryptionCookieTransform.Encode(Byte[] value)  

at Microsoft.IdentityModel.Tokens.SessionSecurityTokenHandler.ApplyTransforms(Byte[] cookie, Boolean outbound)  

at Microsoft.Exchange.Security.Authentication.AdfsSessionSecurityTokenHandler.ApplyTransforms(Byte[] cookie, Boolean outbound)  

at Microsoft.IdentityModel.Tokens.SessionSecurityTokenHandler.WriteToken(XmlWriter writer, SecurityToken token)  

at Microsoft.IdentityModel.Tokens.SessionSecurityTokenHandler.WriteToken(SessionSecurityToken sessionToken)  

at Microsoft.IdentityModel.Web.SessionAuthenticationModule.WriteSessionTokenToCookie(SessionSecurityToken sessionToken)  

at Microsoft.IdentityModel.Web.SessionAuthenticationModule.AuthenticateSessionSecurityToken(SessionSecurityToken sessionToken, Boolean writeCookie)  

at Microsoft.IdentityModel.Web.WSFederationAuthenticationModule.SignInWithResponseMessage(HttpRequest request)  

at Microsoft.IdentityModel.Web.WSFederationAuthenticationModule.OnAuthenticateRequest(Object sender, EventArgs args)  

at Microsoft.Exchange.Security.Authentication.AdfsFederationAuthModule.InternalOnAuthenticateRequest(Object sender, EventArgs eventArgs)  

at System.Web.HttpApplication.SyncEventExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()  

at System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)  

at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

Request information:  

Request URL: https://mail.---.com:443/ecp/  

Request path: /ecp/  

User host address: ---  

User: ---  

Is authenticated: True  

Authentication Type: ADFS  

Thread account name: NT AUTHORITY\SYSTEM

Thread information:  

Thread ID: 17  

Thread account name: NT AUTHORITY\SYSTEM  

Is impersonating: False  

Stack trace: at Microsoft.IdentityModel.CryptoUtil.Algorithms.NewDefaultEncryption()  

at Microsoft.IdentityModel.Web.RsaEncryptionCookieTransform.Encode(Byte[] value)  

at Microsoft.IdentityModel.Tokens.SessionSecurityTokenHandler.ApplyTransforms(Byte[] cookie, Boolean outbound)  

at Microsoft.Exchange.Security.Authentication.AdfsSessionSecurityTokenHandler.ApplyTransforms(Byte[] cookie, Boolean outbound)  

at Microsoft.IdentityModel.Tokens.SessionSecurityTokenHandler.WriteToken(XmlWriter writer, SecurityToken token)  

at Microsoft.IdentityModel.Tokens.SessionSecurityTokenHandler.WriteToken(SessionSecurityToken sessionToken)  

at Microsoft.IdentityModel.Web.SessionAuthenticationModule.WriteSessionTokenToCookie(SessionSecurityToken sessionToken)  

at Microsoft.IdentityModel.Web.SessionAuthenticationModule.AuthenticateSessionSecurityToken(SessionSecurityToken sessionToken, Boolean writeCookie)  

at Microsoft.IdentityModel.Web.WSFederationAuthenticationModule.SignInWithResponseMessage(HttpRequest request)  

at Microsoft.IdentityModel.Web.WSFederationAuthenticationModule.OnAuthenticateRequest(Object sender, EventArgs args)  

at Microsoft.Exchange.Security.Authentication.AdfsFederationAuthModule.InternalOnAuthenticateRequest(Object sender, EventArgs eventArgs)  

at System.Web.HttpApplication.SyncEventExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()  

at System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)  

at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

Custom event details:

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-14*

@Anonymous   , did you ever find an answer?    

If you revert back to Forms based Auth in Exchange, it works in FIPS mode.  But when I set Exchange to use ADFS, I get the same error you got.  ADFS is already in FIPS mode.    

I wonder if it's something with DotNet and FIPs?    

MS, any ideas?    

Steve
