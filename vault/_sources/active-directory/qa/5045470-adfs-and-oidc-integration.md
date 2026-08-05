---
title: "ADFS and OIDC integration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5045470/adfs-and-oidc-integration
question_id: 5045470
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 17
qa_tags: []
---
# ADFS and OIDC integration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5045470/adfs-and-oidc-integration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning community,

i'm implementing an integration with ADFS for implementing user authentication between my application and ADFS.

So i registered successfully my application on ADFS and retrieved the client-id and secret-id and setup the redirect URL.  

After that i imported the ADFS certificate into my app and performed the OpenID configuration successfully using these parameters:

-  Discovery URL: https://ADFS-hostname/adfs/.well-known/openid-configuration

-  Authorization URL: https://ADFS-hostname/adfs/oauth2/authorize/

-  Token URL: https://ADFS-hostname/adfs/oauth2/token/

-  JWT URL: https://ADFS-hostname/adfs/discovery/keys

-  Scope:vpn_cert  aza  email  logon_cert  user_impersonation  openid  profile

-  Client ID

-  Client Secret

Then i created the Relying Party into ADFS with the following information:

-  Relying Party identifiers: https://ADFS-hostname/adfs/oauth2/authorize/

-  Access Control Policy: Permit Everyone.

But when i try to login then i'm redirect correctly from my App to ADFS but i receive the following error:

Encountered error during federation passive request.   

Additional Data   

Event ID 364  

Protocol Name:   

OAuthAuthorizationProtocol   

Relying Party:   

Exception details:   

Microsoft.IdentityServer.Web.Protocols.OAuth.Exceptions.OAuthUnauthorizedClientException: MSIS9321: Received invalid OAuth request. The client 'ClientID Number' is forbidden to access the resource 'http://schemas.microsoft.com/ws/2009/12/identityserver/selfscope'.  

at Microsoft.IdentityServer.Web.Protocols.OAuth.OAuthAuthorization.OAuthTokenBrokerAuthorizationRequestContext.ValidateBroker()  

at Microsoft.IdentityServer.Web.Protocols.OAuth.OAuthAuthorization.OAuthTokenBrokerAuthorizationRequestContext.ValidateCore()  

at Microsoft.IdentityServer.Web.Protocols.ProtocolContext.Validate()  

at Microsoft.IdentityServer.Web.Protocols.OAuth.OAuthAuthorization.OAuthAuthorizationProtocolHandler.PreAuthenticationProcess(ProtocolContext context)  

at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)  

Any hints or suggestions will be appriciated.

Regards

Mario

## Answer (community) — community member

*upvotes: 0 · updated: 2020-05-06*

Thank you Oliver,

I did already what you suggested.  

It's not working.  

So i'll post on the correct forum.  

Thanks again.  

Regards

Mario

## Answer (community) — community member

*upvotes: 0 · updated: 2020-05-06*

Hello Mario,

Based on the error message you provided above, I did a lot of research on it,  it is more likely that the problem is related to the ADFS access control policy. Since you mentioned that you have policy " Permite Everyone", please double checl if you have
 configured the correct policy to allow you access your resourece. And in the Rekying party Trust section, please check if you have applied your policies there.  For more details, please refer to https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/create-a-rule-to-permit-or-deny-users-based-on-an-incoming-claim?redirectedfrom=MSDN&f=255&MSPPError=-2147217396.

On another hand, as we are focusing on Office 365 Exchange Online Support, we are not experts for on-premise ADFS related problem. I'd like to help you do more research on it, however I can find limited Offcial documentation on it. However Microsoft has
 a dedicated TechNet Forum, the support engineers there are focusing on ADFS related problems. If your issue persists, it is recommended that please post a new
 thread there to get further professional assistance regarding your problem, thanks. By the way, if you need any other help from Office 365 Exchange Online, please feel free to share with me, and I'd like to help you, thanks.

Your understanding and patience will be highly appreciated.

Best Regards,

Oliver
