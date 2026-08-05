---
title: "ADFS-Event id 111 and ADFS Proxy- Event ID 364"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4189558/adfs-event-id-111-and-adfs-proxy-event-id-364
question_id: 4189558
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# ADFS-Event id 111 and ADFS Proxy- Event ID 364

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4189558/adfs-event-id-111-and-adfs-proxy-event-id-364 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello TechNet,

We encountered user authentication issue and was able to find event ID 133 and other event IDs related to database communication, we were able to resolved the authentication issue by re-establishing communication between the ADFS and ADFS proxy server (removed
 the configured proxy from the ADFS server then re-initiate the ADFS Proxy configuration Wizard). 

However, we have observed that there was a continuous Event ID 364 logged on AD FS Proxy and Event ID 111 on the AD FS 2.0 server. These was logged before and after users are encountering issue with authentication.

As of now, users are able to authenticate but Event ID 364 and Event ID 111 are still appearing on the event logs. Please help us on this as we are afraid this might bring back the issue on the users authentication any time.

Thank you.

ADFS Proxy Event ID 364 Details:

Encountered error during federation passive request. 

Additional Data 

Exception details: 

Microsoft.IdentityServer.Web.AuthenticationFailedException: MSIS8108: Authentication failed.

   at Microsoft.IdentityServer.Web.FederationPassiveAuthentication.SubmitRequest(MSISRequestSecurityToken request)

   at Microsoft.IdentityServer.Web.FederationPassiveAuthentication.RequestBearerToken(MSISSignInRequestMessage signInRequest, SecurityTokenElement onBehalfOf, SecurityToken primaryAuthToken, String desiredTokenType, UInt32 lifetime, Uri& replyTo)

   at Microsoft.IdentityServer.Web.FederationPassiveAuthentication.RequestBearerToken(MSISSignInRequestMessage signInRequest, SecurityTokenElement onBehalfOf, SecurityToken primaryAuthToken, String desiredTokenType, Uri& replyTo)

   at Microsoft.IdentityServer.Web.FederationPassiveAuthentication.BuildSingleSignOnToken(SecurityToken securityToken, String issuer, FederationPassiveContext federationPassiveContext, String& signature)

   at Microsoft.IdentityServer.Web.FederationPassiveAuthentication.SignIn(SecurityToken securityToken)

ADFS Event ID 111 Details:

The Federation Service encountered an error while processing the WS-Trust request. 

Request type: http://schemas.xmlsoap.org/ws/2005/02/trust/RST/Issue 

Additional Data 

Exception details: 

Microsoft.IdentityServer.Framework.SecurityTokenService.FailedAuthenticationException: MSIS3019: Authentication failed. ---> System.IdentityModel.Tokens.SecurityTokenValidationException: ID4063: LogonUser failed for the '--------' user. Ensure that the user
 has a valid Windows account. ---> System.ComponentModel.Win32Exception: The password for this account has expired

   --- End of inner exception stack trace ---

   at System.IdentityModel.Tokens.WindowsUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)

   at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)

   at Microsoft.IdentityServer.Service.SecurityTokenService.MSISSecurityTokenService.GetOnBehalfOfPrincipal(RequestSecurityToken request, ClaimsPrincipal callerPrincipal)

   --- End of inner exception stack trace ---

   at Microsoft.IdentityServer.Service.SecurityTokenService.MSISSecurityTokenService.GetOnBehalfOfPrincipal(RequestSecurityToken request, ClaimsPrincipal callerPrincipal)

   at Microsoft.IdentityServer.Service.SecurityTokenService.MSISSecurityTokenService.BeginGetScope(ClaimsPrincipal principal, RequestSecurityToken request, AsyncCallback callback, Object state)

   at System.IdentityModel.SecurityTokenService.BeginIssue(ClaimsPrincipal principal, RequestSecurityToken request, AsyncCallback callback, Object state)

   at System.ServiceModel.Security.WSTrustServiceContract.DispatchRequestAsyncResult..ctor(DispatchContext dispatchContext, AsyncCallback asyncCallback, Object asyncState)

   at System.ServiceModel.Security.WSTrustServiceContract.BeginDispatchRequest(DispatchContext dispatchContext, AsyncCallback asyncCallback, Object asyncState)

   at System.ServiceModel.Security.WSTrustServiceContract.BeginProcessCore(Message requestMessage, WSTrustRequestSerializer requestSerializer, WSTrustResponseSerializer responseSerializer, String requestAction, String responseAction, String trustNamespace,
 AsyncCallback callback, Object state)

System.IdentityModel.Tokens.SecurityTokenValidationException: ID4063: LogonUser failed for the '-----' user. Ensure that the user has a valid Windows account. ---> System.ComponentModel.Win32Exception: The password for this account has expired

   --- End of inner exception stack trace ---

   at System.IdentityModel.Tokens.WindowsUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)

   at Microsoft.IdentityServer.Service.Tokens.MSISWindowsUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)

   at Microsoft.IdentityServer.Service.SecurityTokenService.MSISSecurityTokenService.GetOnBehalfOfPrincipal(RequestSecurityToken request, ClaimsPrincipal callerPrincipal)

System.ComponentModel.Win32Exception (0x80004005): The password for this account has expired

## Answers

_No answers on this thread._
