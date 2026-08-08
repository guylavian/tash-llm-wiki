---
title: "ADFS 4.0 - Third Relying Party restrict acces by OU"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/366211/adfs-4-0-third-relying-party-restrict-acces-by-ou
question_id: 366211
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS 4.0 - Third Relying Party restrict acces by OU

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/366211/adfs-4-0-third-relying-party-restrict-acces-by-ou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I want to restrict access to an application depending on what organizational unit the user is located in.  

Attempted to create the following Issuance Authorization Rules;  

1- The first, to get the distinguished name  

c: [Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  

 => add (store = "Active Directory", types = ("temp: / claim / dn"), query = "; distinguishedName; {0}", param = c.Value);  

2- The second to allow only one specific OU:  

c: [Type == "temp: / Claim / dn", Value = ~ "^. * (? i) (OU = Staff, OU = Users, DC = contoso, DC = com) $"]  

 => issue (Type = "http://schemas.microsoft.com/authorization/claims/permit", Value = "PermitUsersWithClaim");  

I have the claim rules configured to pass the fields: name, surname, email address  

Do you know what is failing me?  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-22*

Exception details:   

Microsoft.IdentityServer.Service.IssuancePipeline.CallerAuthorizationException: MSIS5007: The caller authorization failed for caller identity domain\DFernandez for relying party trust http://www.externalapplication.com.  

   at Microsoft.IdentityModel.Threading.AsyncResult.End(IAsyncResult result)  

   at Microsoft.IdentityModel.Threading.TypedAsyncResult`1.End(IAsyncResult result)      at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.Issue(RequestSecurityToken request, IList`1& identityClaimSet, List`1 additionalClaims)      at Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.Issue(RequestSecurityToken request, List`1 additionalClaims)  

   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolManager.Issue(HttpSamlRequestMessage httpSamlRequestMessage, SecurityTokenElement onBehalfOf, String sessionState, String relayState, String& newSamlSession, String& samlpAuthenticationProvider, Boolean isUrlTranslationNeeded, WrappedHttpListenerContext context, Boolean isKmsiRequested)  

   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.RequestBearerToken(WrappedHttpListenerContext context, HttpSamlRequestMessage httpSamlRequest, SecurityTokenElement onBehalfOf, String relyingPartyIdentifier, Boolean isKmsiRequested, Boolean isApplicationProxyTokenRequired, String& samlpSessionState, String& samlpAuthenticationProvider)  

   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.BuildSignInResponseCoreWithSerializedToken(HttpSamlRequestMessage httpSamlRequest, WrappedHttpListenerContext context, String relyingPartyIdentifier, SecurityTokenElement signOnTokenElement, Boolean isKmsiRequested, Boolean isApplicationProxyTokenRequired)  

   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.BuildSignInResponseCoreWithSecurityToken(SamlSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.Process(ProtocolContext context)  

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.ProcessProtocolRequest(ProtocolContext protocolContext, PassiveProtocolHandler protocolHandler)  

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-22*

No,  

I tried adding these 2 rules in the issuance rules and deleting the default permit all rule, but when we attempt to login this causes a sso error
