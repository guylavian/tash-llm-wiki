---
title: "ADFS - ADFS doesn't seem to adhere to the SAML2.0 specification with regards to AssertionConsumerServiceURL (MSIS3200)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/107001/adfs-adfs-doesnt-seem-to-adhere-to-the-saml2-0-spe
question_id: 107001
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
---
# ADFS - ADFS doesn't seem to adhere to the SAML2.0 specification with regards to AssertionConsumerServiceURL (MSIS3200)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/107001/adfs-adfs-doesnt-seem-to-adhere-to-the-saml2-0-spe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have successfully installed and configured the ADFS service on Windows 2012 R2. I've also setup a relying party trust and logging in with SSO works perfectly. However according to the SAML2.0 specification the AuthRequest may optionally contain a AssertionConsumerServiceURL attibute which may or may not point to a different location as to the URL configured in the relying party trust. Please refer to the SAML Core Specification.   

What I am trying to achieve is to have the ADFS send the SAML Response, containing the assertion, back to different locations based on who sent the AuthRequest in the first place. I have multiple service providers but don't want to have to configure a relying party trust for every SP. The reason for that is mainly because the service providers (e.g. IOT edges) are added and removed dynamically and there are potentially lots of them.  

I expected ADFS to send the assertion to the URL stated in the AssertionConsumerServiceURL attribute but it seems not to from my tests. At least ADFS should do so when the AuthRequest is signed as stated here. What I am getting is the following error(MSIS3200):  

```
Exception details: 
Microsoft.IdentityServer.Service.Policy.PolicyServer.Engine.AssertionConsumerServiceUrlDoesNotMatchPolicyException: MSIS3200: No AssertionConsumerService is configured on the relying party trust 'https://mytesturl.com/saml/metadata' that is a prefix match of the AssertionConsumerService URL 'https://mytesturl.com:7000/saml/?acs' specified by the request.
   at Microsoft.IdentityServer.Service.SamlProtocol.EndpointResolver.LookupAssertionConsumerServiceByUrl(Collection`1 assertionConsumerServices, Uri requestedAssertionConsumerServiceUrl, String scopeIdentity)
   at Microsoft.IdentityServer.Service.SamlProtocol.EndpointResolver.FindSamlResponseEndpointForAuthenticationRequest(Boolean artifactEnabled, AuthenticationRequest request, ScopeDescription scopeDescription)
   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolManager.GetResponseEndpointFromRequest(SamlRequest request, Boolean isUrlTranslationNeeded, ScopeDescription scope)
   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolManager.Issue(HttpSamlRequestMessage httpSamlRequestMessage, SecurityTokenElement onBehalfOf, String sessionState, String relayState, String& newSamlSession, String& samlpAuthenticationProvider, Boolean isUrlTranslationNeeded, WrappedHttpListenerContext context, Boolean isKmsiRequested)
   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.RequestBearerToken(WrappedHttpListenerContext context, HttpSamlRequestMessage httpSamlRequest, SecurityTokenElement onBehalfOf, String relyingPartyIdentifier, Boolean isKmsiRequested, Boolean isApplicationProxyTokenRequired, String& samlpSessionState, String& samlpAuthenticationProvider)
   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.BuildSignInResponseCoreWithSerializedToken(HttpSamlRequestMessage httpSamlRequest, WrappedHttpListenerContext context, String relyingPartyIdentifier, SecurityTokenElement signOnTokenElement, Boolean isKmsiRequested, Boolean isApplicationProxyTokenRequired)
   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.BuildSignInResponseCoreWithSecurityToken(SamlSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)
   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.Process(ProtocolContext context)
   at Microsoft.IdentityServer.Web.PassiveProtocolListener.ProcessProtocolRequest(ProtocolContext protocolContext, PassiveProtocolHandler protocolHandler)
   at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)
```

which basically states that the configured URL for the assertion consumer (https://mytesturl.com/saml/?acs) is different from the one sent in the AuthRequest (https://mytesturl.com:7000/saml/?acs). Indeed the two URL's do not match but that is the whole point in stating the AssertionConsumerServiceURL in the AuthRequest to begin with. I am certain that I have signed the AuthRequest, I have verified that in SAML-tracer as well as in my SP code.  

I hope someone can shed some light on this matter. Are my assumptions incorrect or have I failed to test ADFS properly, perhaps overlooked a configuration parameter on ADFS?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-06*

Hi,  

thank you for your reply.  

I had already figured out that adding multiple assertion consumer URLs to the relying party configuration works but that is not an option for me as it would require an explicit action from an IT administrator for each and every node in the system. I understand ADFS does not support what I'm trying to achieve but I'm still curious why ADFS considers the AssertionConsumerServiceURL untrusted if the AuthnRequest is signed. Signing the request should be sufficient for trusting the source and hence the URL.  

That being said I have gone a different route for my solution seeing I cannot trust ADFS or any other IdP supporting my initial solution. For the curious ones, the idea is to only maintain a single service provider for the complete system and route all SAML traffic through that SP regardless of the initial receiver of the authentication request. This will allow configuration of a relying party with a single SP (consumer URL) on the IdP side. Not as clean solution as my first idea but it does have some advantages.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-06*

What you're trying to achieve is not possible without having one Relying Party per Service Provider, or at least having the endpoint that is being sent on the SAML Request as the AssertionConsumerServiceURL on the Relying Party settings. We cannot consider the request as coming from known source if that is not happening. Also, if you're setting up new AD FS farm, AD FS 2019 should be considered
