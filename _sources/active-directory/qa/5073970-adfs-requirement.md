---
title: "ADFS Requirement"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5073970/adfs-requirement
question_id: 5073970
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# ADFS Requirement

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5073970/adfs-requirement (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day  

I hope someone will be able to give me some advice on the below.  

It is my very first time in my IT career attempting this, please bear with me.  

This my test setup we are testing and planning to deploy in production environment once all testing and lessons has been learned from the test environment experience.  

I have the following setup:  

Company A:  

* Windows Server 2016 Standard has been installed.  

* Server is a domain controller for Domain A.  

* Server is a Root CA for testing purposes.  

* Server has ADFS Role installed and configured.  

* ADFS multidomain has been configured.  

* There is no Proxy in the environment due to being used for testing only.  

* Server has AD Connect installed and configured with a Office365 Tenant A.  

* Has a bi-directional AD Trust with Company B  

* Has ADFS fully deployed and in working order.  

* Office365 Tenant A is isolated from Tenant B and completely seperate environments.  

* Company A when signing in on Office.com, I get redirect to ADFS and once login is completd I am redirected to Office 365 successfully, seems to be no problems on my primary tenant.  

Company B:  

* Windows Server 2016 Standard has been installed.  

* Server is a domain controller for Domain B.  

* Server has AD Connect installed and configured with a Office365 tenant B.  

* Has a bi-directional AD Trust with Company A.  

* Office365 Tenant B is isolated from Tenant A and completely seperate environments.  

What needs to be accomplished:  

-  Company A will be the ADFS role holder, no ADFS will reside in Company B.  

-  Federation trust between Company A and Company B.  

-  Company A Office365 environment will be used for development like Applications, SharePoint structure etc. Will this accomplish the environment I have laid out above?  

What I have tried already and failed:  

* I have performed the actions in this article, this is exactly what we want to accomplish, not sure if there were actual next steps or was that the only steps that had to be performed: https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-single-adfs-multitenant-federation  

* Company B when trying to sign into Office.com, I get a redirect to Company A ADFS login page, when login immediate error and stops. "An error occured. Contact your Administrator for more informatuon. Reyling party: Microsoft Office 365 Indetity Platform."
 Event Viewer gave me the below.  

Event ID 111   

Log Name:      AD FS/Admin  

Source:        AD FS  

Date:          2020/08/07 7:55:49 PM  

Event ID:      111  

Task Category: None  

Level:         Error  

Keywords:      AD FS  

User:          CompanyA\ADFS-Service  

Computer:      AD-DC01.Company.A  

Description:  

The Federation Service encountered an error while processing the WS-Trust request.

Request type: http://schemas.microsoft.com/idfx/requesttype/issue   

Additional Data   

Exception details:   

System.ArgumentOutOfRangeException: Not a valid Win32 FileTime.  

Parameter name: fileTime  

   at System.DateTime.FromFileTimeUtc(Int64 fileTime)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetPasswordExpiryDetails(SafeLsaReturnBufferHandle profileHandle, DateTime& nextPasswordChange, DateTime& lastPasswordChange)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)  

   at Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateTokenInternal(UsernameAuthenticationContext usernameAuthenticationContext, SecurityToken token)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.GetEffectivePrincipal(SecurityTokenElement securityTokenElement, SecurityToken deviceSecurityToken, SecurityTokenHandlerCollection securityTokenHandlerCollection)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.Issue(RequestSecurityToken request, IList`1& identityClaimSet, List`1 additionalClaims)  

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

  <System>  

    <Provider Name="AD FS" Guid="{2FFB687A-1571-4ACE-8550-47AB5CCAE2BC}" />  

    <EventID>111</EventID>  

    <Version>0</Version>  

    <Level>2</Level>  

    <Task>0</Task>  

    <Opcode>0</Opcode>  

    <Keywords>0x8000000000000001</Keywords>  

    <TimeCreated SystemTime="2020-08-07T17:55:49.755139100Z" />  

    <EventRecordID>274</EventRecordID>  

    <Correlation ActivityID="{694F8A6D-EA06-41C2-BE34-3F897C2E03E1}" />  

    <Execution ProcessID="3576" ThreadID="5156" />  

    <Channel>AD FS/Admin</Channel>  

    <Computer>AD-DC01.Company.A</Computer>  

    <Security UserID="S-1-5-21-2116166319-3450088182-1483477323-1111" />  

  </System>  

  <UserData>  

    <Event xmlns="http://schemas.microsoft.com/ActiveDirectoryFederationServices/2.0/Events">  

      <EventData>  

        <Data>http://schemas.microsoft.com/idfx/requesttype/issue</Data>  

        <Data>System.ArgumentOutOfRangeException: Not a valid Win32 FileTime.  

Parameter name: fileTime  

   at System.DateTime.FromFileTimeUtc(Int64 fileTime)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetPasswordExpiryDetails(SafeLsaReturnBufferHandle profileHandle, DateTime& nextPasswordChange, DateTime& lastPasswordChange)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)  

   at Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateTokenInternal(UsernameAuthenticationContext usernameAuthenticationContext, SecurityToken token)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.GetEffectivePrincipal(SecurityTokenElement securityTokenElement, SecurityToken deviceSecurityToken, SecurityTokenHandlerCollection securityTokenHandlerCollection)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.Issue(RequestSecurityToken request, IList`1&amp; identityClaimSet, List`1 additionalClaims)</Data>  

      </EventData>  

    </Event>  

  </UserData>  

</Event>  

Event ID 1000   

Log Name:      AD FS/Admin  

Source:        AD FS  

Date:          2020/08/07 7:55:49 PM  

Event ID:      1000  

Task Category: None  

Level:         Warning  

Keywords:      AD FS  

User:          CompanyA\ADFS-Service  

Computer:      AD-DC01.Company.A  

Description:  

An error occurred during processing of a token request. The data in this event may have the identity of the caller (application) that made this request. The data includes an Activity ID that you can cross-reference to error or warning events to help diagnose
 the problem that caused this error.    

Additional Data   

Caller:  

OnBehalfOf user:  

ActAs user:  

Target Relying Party:  

 http://adfs.companya.co.za/adfs/services/trust   

Device identity:  

User action:   

Use the Activity ID data in this message to search and correlate the data to events in the Event log using Event Viewer. This Activity ID will also be shown as additional information in the error page when an error occurs in the federation passive Web application.  

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

  <System>  

    <Provider Name="AD FS" Guid="{2FFB687A-1571-4ACE-8550-47AB5CCAE2BC}" />  

    <EventID>1000</EventID>  

    <Version>0</Version>  

    <Level>3</Level>  

    <Task>0</Task>  

    <Opcode>0</Opcode>  

    <Keywords>0x8000000000000001</Keywords>  

    <TimeCreated SystemTime="2020-08-07T17:55:49.755156000Z" />  

    <EventRecordID>275</EventRecordID>  

    <Correlation ActivityID="{694F8A6D-EA06-41C2-BE34-3F897C2E03E1}" />  

    <Execution ProcessID="3576" ThreadID="5156" />  

    <Channel>AD FS/Admin</Channel>  

    <Computer>AD-DC01.Company.A</Computer>  

    <Security UserID="S-1-5-21-2116166319-3450088182-1483477323-1111" />  

  </System>  

  <UserData>  

    <Event xmlns="http://schemas.microsoft.com/ActiveDirectoryFederationServices/2.0/Events">  

      <EventData>  

        <Data>  

        </Data>  

        <Data>  

        </Data>  

        <Data>  

        </Data>  

        <Data>http://adfs.companya.co.za/adfs/services/trust</Data>  

        <Data>  

        </Data>  

      </EventData>  

    </Event>  

  </UserData>  

</Event>  

Event ID 364:  

Log Name:      AD FS/Admin  

Source:        AD FS  

Date:          2020/08/07 7:55:49 PM  

Event ID:      364  

Task Category: None  

Level:         Error  

Keywords:      AD FS  

User:          CompanyA\ADFS-Service  

Computer:      AD-DC01.Company.A  

Description:  

Encountered error during federation passive request.   

Additional Data   

Protocol Name:   

wsfed   

Relying Party:   

urn:federation:MicrosoftOnline   

Exception details:   

Microsoft.IdentityServer.RequestFailedException: MSIS7012: An error occurred while processing the request. Contact your administrator for details. ---> System.ArgumentOutOfRangeException: Not a valid Win32 FileTime.  

Parameter name: fileTime  

   at System.DateTime.FromFileTimeUtc(Int64 fileTime)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetPasswordExpiryDetails(SafeLsaReturnBufferHandle profileHandle, DateTime& nextPasswordChange, DateTime& lastPasswordChange)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)  

   at Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateTokenInternal(UsernameAuthenticationContext usernameAuthenticationContext, SecurityToken token)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.GetEffectivePrincipal(SecurityTokenElement securityTokenElement, SecurityToken deviceSecurityToken, SecurityTokenHandlerCollection securityTokenHandlerCollection)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.Issue(RequestSecurityToken request, IList`1& identityClaimSet, List`1 additionalClaims)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.SubmitRequest(MSISRequestSecurityToken request, IList`1& identityClaimCollection)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.RequestBearerToken(MSISRequestSecurityToken signInRequest, Uri& replyTo, IList`1& identityClaimCollection)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.RequestSingleSignOnToken(ProtocolContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSsoSecurityToken(WSFederationSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken, SecurityToken& ssoSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponseCoreWithSecurityToken(WSFederationSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponse(WSFederationSignInContext federationPassiveContext, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   --- End of inner exception stack trace ---  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponse(WSFederationSignInContext federationPassiveContext, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.Process(ProtocolContext context)  

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.ProcessProtocolRequest(ProtocolContext protocolContext, PassiveProtocolHandler protocolHandler)  

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)  

System.ArgumentOutOfRangeException: Not a valid Win32 FileTime.  

Parameter name: fileTime  

   at System.DateTime.FromFileTimeUtc(Int64 fileTime)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetPasswordExpiryDetails(SafeLsaReturnBufferHandle profileHandle, DateTime& nextPasswordChange, DateTime& lastPasswordChange)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)  

   at Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateTokenInternal(UsernameAuthenticationContext usernameAuthenticationContext, SecurityToken token)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.GetEffectivePrincipal(SecurityTokenElement securityTokenElement, SecurityToken deviceSecurityToken, SecurityTokenHandlerCollection securityTokenHandlerCollection)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.Issue(RequestSecurityToken request, IList`1& identityClaimSet, List`1 additionalClaims)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.SubmitRequest(MSISRequestSecurityToken request, IList`1& identityClaimCollection)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.RequestBearerToken(MSISRequestSecurityToken signInRequest, Uri& replyTo, IList`1& identityClaimCollection)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.RequestSingleSignOnToken(ProtocolContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSsoSecurityToken(WSFederationSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken, SecurityToken& ssoSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponseCoreWithSecurityToken(WSFederationSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponse(WSFederationSignInContext federationPassiveContext, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

  <System>  

    <Provider Name="AD FS" Guid="{2FFB687A-1571-4ACE-8550-47AB5CCAE2BC}" />  

    <EventID>364</EventID>  

    <Version>0</Version>  

    <Level>2</Level>  

    <Task>0</Task>  

    <Opcode>0</Opcode>  

    <Keywords>0x8000000000000001</Keywords>  

    <TimeCreated SystemTime="2020-08-07T17:55:49.755839500Z" />  

    <EventRecordID>276</EventRecordID>  

    <Correlation ActivityID="{694F8A6D-EA06-41C2-BE34-3F897C2E03E1}" />  

    <Execution ProcessID="3576" ThreadID="5156" />  

    <Channel>AD FS/Admin</Channel>  

    <Computer>AD-DC01.Company.A</Computer>  

    <Security UserID="S-1-5-21-2116166319-3450088182-1483477323-1111" />  

  </System>  

  <UserData>  

    <Event xmlns="http://schemas.microsoft.com/ActiveDirectoryFederationServices/2.0/Events">  

      <EventData>  

        <Data>wsfed</Data>  

        <Data>urn:federation:MicrosoftOnline</Data>  

        <Data>Microsoft.IdentityServer.RequestFailedException: MSIS7012: An error occurred while processing the request. Contact your administrator for details. ---> System.ArgumentOutOfRangeException: Not a valid Win32 FileTime.  

Parameter name: fileTime  

   at System.DateTime.FromFileTimeUtc(Int64 fileTime)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetPasswordExpiryDetails(SafeLsaReturnBufferHandle profileHandle, DateTime& nextPasswordChange, DateTime& lastPasswordChange)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)  

   at Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateTokenInternal(UsernameAuthenticationContext usernameAuthenticationContext, SecurityToken token)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.GetEffectivePrincipal(SecurityTokenElement securityTokenElement, SecurityToken deviceSecurityToken, SecurityTokenHandlerCollection securityTokenHandlerCollection)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.Issue(RequestSecurityToken request, IList`1&amp; identityClaimSet, List`1 additionalClaims)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.SubmitRequest(MSISRequestSecurityToken request, IList`1& identityClaimCollection)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.RequestBearerToken(MSISRequestSecurityToken signInRequest, Uri& replyTo, IList`1& identityClaimCollection)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.RequestSingleSignOnToken(ProtocolContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSsoSecurityToken(WSFederationSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken, SecurityToken& ssoSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponseCoreWithSecurityToken(WSFederationSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponse(WSFederationSignInContext federationPassiveContext, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   --- End of inner exception stack trace ---  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponse(WSFederationSignInContext federationPassiveContext, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.Process(ProtocolContext context)  

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.ProcessProtocolRequest(ProtocolContext protocolContext, PassiveProtocolHandler protocolHandler)  

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)  

System.ArgumentOutOfRangeException: Not a valid Win32 FileTime.  

Parameter name: fileTime  

   at System.DateTime.FromFileTimeUtc(Int64 fileTime)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetPasswordExpiryDetails(SafeLsaReturnBufferHandle profileHandle, DateTime& nextPasswordChange, DateTime& lastPasswordChange)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)  

   at Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)  

   at Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateTokenInternal(UsernameAuthenticationContext usernameAuthenticationContext, SecurityToken token)  

   at Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.GetEffectivePrincipal(SecurityTokenElement securityTokenElement, SecurityToken deviceSecurityToken, SecurityTokenHandlerCollection securityTokenHandlerCollection)  

   at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.Issue(RequestSecurityToken request, IList`1&amp; identityClaimSet, List`1 additionalClaims)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.SubmitRequest(MSISRequestSecurityToken request, IList`1& identityClaimCollection)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.RequestBearerToken(MSISRequestSecurityToken signInRequest, Uri& replyTo, IList`1& identityClaimCollection)  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.RequestSingleSignOnToken(ProtocolContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSsoSecurityToken(WSFederationSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken, SecurityToken& ssoSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponseCoreWithSecurityToken(WSFederationSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponse(WSFederationSignInContext federationPassiveContext, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

</Data>  

      </EventData>  

    </Event>  

  </UserData>  

</Event>  

* Reading about the errors it seems more to be in line with Token authentication not working, I have no idea how to resolve this if you can point me in the right direction I will really appreciate the assistance.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-13*

Hello rduplessis,

Thanks for your feedback and apologize for the inconvenience caused by this problem.

Based on the error you shared, may I double confirm if you directly access the forum from your ADFS server?  From the error you shared, it is more likely that you cannot directly open the forum link from your server.
  Generally this is a public forum, it is recommended that please try to access the forum from an Internet device ( better not related to your ADFS intranet) to see if it make any difference, thanks.  By the way, the link in your error is different from the
 link I shared in the first reply above. If conveneint, please copy the link https://docs.microsoft.com/en-us/answers/topics/adfs.html  from my first reply and then try to access it from a device which can directly access Internet to see the results, thanks.

Please feel free to share with me if you got any further updates, thanks.

Best Regards,

Oliver

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-13*

Hi Oliver

I tried your suggestions to no avail.

I then tried to post in the Q&A for some reason I am not allowed to.

How do I apply for access, this is the first time in my IT career of 12 years I need to ask for help on a Microsoft Forum.

Access Denied

You don't have permission to access "http://docs.microsoft.com/answers/questions/ask.html" on this server.

Reference #18.7088655f.1597322688.211b2bf

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-13*

Hi Oliver

Thanks so much for the reply.

I will have a look at the information you provided, if I do not come right will go to the ADFS Q&A forum.

When I do have a solution, I will update this tread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-12*

Hello rduplessis,

Based on the link which you tried above, I did a lot of research on it, as far as I know you want to deploy one ADFS server with multiple Azure AD tenant ( two tenants) scenario for authentication.  Also I checked the ADFS event log you shared above and
 did a lot of more research on the errors in the log.

According to the event log above, there are different errors with generated Event ID in it.  Event ID 364 " An error occurred while processing the request. Contact your administrator for details."  Activity ID ="{694F8A6D-EA06-41C2-BE34-3F897C2E03E1}" etc.
  I did a lot of more research on these errors, as far as I know generally the Event ID 365 error may caused by the different reasons in the passive request, it can also occur during single sign on (SSO) or logout for both SAML and WS-Federation sceanrios etc.
  For more details, you can refer to https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff641688(v=ws.10)?redirectedfrom=MSDN >
 Event ID 364.   And some other troubleshooting article for your reference https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/troubleshooting/ad-fs-tshoot-logging.

On another hand, since the ADFS working fine with the company A, and based on my research on this issue with error, it is more likely related to the misconfiugration for ADFS with another forest.  However, I can find limited Microsoft Official resource on
 this kind of issue to help troubleshooting the problem.  If you cannot resolve this issue with the link above, as Microsoft has a dedicated ADFS Q&A Forum,
 the dedicated support engineers there are more experience with ADFS related scenarios. it is recommended that please post a new thread there to get further professional assistance regarding your current problem, thanks.   By the way, if you got any further
 updates there, please feel free to share with us, thanks.

Your understanding and patience will be highly appreciated.

Best Regards,

Oliver
