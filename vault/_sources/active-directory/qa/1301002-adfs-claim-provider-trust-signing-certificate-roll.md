---
title: "ADFS claim provider trust signing certificate rollover"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1301002/adfs-claim-provider-trust-signing-certificate-roll
question_id: 1301002
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS claim provider trust signing certificate rollover

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1301002/adfs-claim-provider-trust-signing-certificate-roll (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We recently had a SSO user that changed their signing certificate. They provided us with the new certificate in before the intervention so we could add it in the signing certificate section of this claim provider in ADFS.

We did it, keeping the old one in place, that way, when they'll do the rollover there would be no impact because we would already trust the new certificate.

But the day of the rollover the SSO stopped working because of signature verificaton failure (see full error below). To get it to work again we did nothing more than removing the old certificate that was no more in use.

I don't get why ADFS was only validating the signature against the old certifcate. Isn't it exactly the point of supporting multiple signing certificates that our clients would be able to do a rollover without causing any interruption of service ? Or is it something that I don't get about how it works ? 

Thanks for your help.

```
Exception details: 
Microsoft.IdentityServer.Protocols.Saml.SamlProtocolException: MSIS1022: Cannot process SAML Response from ''.
Inner exception: ID6013: The signature verification failed.
   at Microsoft.IdentityServer.Service.Tokens.SamlMessageSecurityTokenHandler.ReadToken(XmlReader reader)
   at Microsoft.IdentityModel.Tokens.SecurityTokenHandlerCollection.ReadToken(XmlReader reader)
   at Microsoft.IdentityModel.Tokens.SecurityTokenElement.ReadSecurityToken(XmlElement securityTokenXml, SecurityTokenHandlerCollection securityTokenHandlers)
   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolManager.Issue(HttpSamlRequestMessage httpSamlRequestMessage, SecurityTokenElement onBehalfOf, String sessionState, String relayState, String& newSamlSession, String& samlpAuthenticationProvider, Boolean isUrlTranslationNeeded, WrappedHttpListenerContext context, Boolean isKmsiRequested)
   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.RequestBearerToken(WrappedHttpListenerContext context, HttpSamlRequestMessage httpSamlRequest, SecurityTokenElement onBehalfOf, String relyingPartyIdentifier, Boolean isKmsiRequested, Boolean isApplicationProxyTokenRequired, String& samlpSessionState, String& samlpAuthenticationProvider)
   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.BuildSignInResponseCoreWithSerializedToken(HttpSamlRequestMessage httpSamlRequest, WrappedHttpListenerContext context, String relyingPartyIdentifier, SecurityTokenElement signOnTokenElement, Boolean isKmsiRequested, Boolean isApplicationProxyTokenRequired)
   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.SendSignInResponseForSecurityToken(GenericProtocolRequest originalRequest, SecurityTokenElement requestedTokenElement, ProtocolContext context)
   at Microsoft.IdentityServer.Web.PassiveProtocolListener.ProcessProtocolRequest(ProtocolContext protocolContext, PassiveProtocolHandler protocolHandler)
   at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)
```

## Answers

_No answers on this thread._
