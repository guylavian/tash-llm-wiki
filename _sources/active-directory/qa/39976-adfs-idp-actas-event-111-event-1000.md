---
title: "ADFS IDP /ActAs Event 111 & Event 1000"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/39976/adfs-idp-actas-event-111-event-1000
question_id: 39976
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS IDP /ActAs Event 111 & Event 1000

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/39976/adfs-idp-actas-event-111-event-1000 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Experiencing an issue with ADFS 4 (Server 2016) , when we pass a IDP Saml request from the SP to the IDP  with the ActAs permission passed  

if we omit the ActAs Element in the  request, the ADFS server responds with the token (no claims) , but we cannot get the get request working  where it send a security token and claims (when stipulating ActAs)  

We have added the necessary Delegation Authorization Rules for the specified ActAS Service Account to the relying party   

ADFS Event Logs reports   

Event ID 111 (Error)  

The Federation Service encountered an error while processing the WS-Trust request.   

Request type: http://docs.oasis-open.org/ws-sx/ws-trust/200512/RST/Issue   

Additional Data   

Exception details:   

System.Xml.XmlException: ID4125: An error occurred reading XML data. ---> System.InvalidOperationException: No corresponding start element is open.  

   at System.Xml.XmlBaseReader.ReadEndElement()  

   at Microsoft.IdentityModel.Protocols.XmlSignature.SignedInfo.ReadFrom(XmlDictionaryReader reader, TransformFactory transformFactory)  

   at Microsoft.IdentityModel.Protocols.XmlSignature.Signature.ReadFrom(XmlDictionaryReader reader)  

   at Microsoft.IdentityModel.Protocols.XmlSignature.EnvelopedSignatureReader.ReadSignature()  

   at Microsoft.IdentityModel.Protocols.XmlSignature.EnvelopedSignatureReader.TryReadSignature()  

   at Microsoft.IdentityModel.Tokens.Saml2.Saml2SecurityTokenHandler.ReadAssertion(XmlReader reader)  

   --- End of inner exception stack trace ---  

   at Microsoft.IdentityModel.Tokens.Saml2.Saml2SecurityTokenHandler.ReadAssertion(XmlReader reader)  

   at Microsoft.IdentityModel.Tokens.Saml2.Saml2SecurityTokenHandler.ReadToken(XmlReader reader)  

   at Microsoft.IdentityModel.Tokens.SecurityTokenHandlerCollection.ReadToken(XmlReader reader)  

   at Microsoft.IdentityModel.Tokens.SecurityTokenElement.ReadSecurityToken(XmlElement securityTokenXml, SecurityTokenHandlerCollection securityTokenHandlers)  

   at Microsoft.IdentityModel.Tokens.SecurityTokenElement.CreateSubject(XmlElement securityTokenXml, SecurityTokenHandlerCollection securityTokenHandlers)  

   at Microsoft.IdentityServer.Service.SecurityTokenService.MSISSecurityTokenService.BeginGetScope(IClaimsPrincipal principal, RequestSecurityToken request, AsyncCallback callback, Object state)  

   at Microsoft.IdentityModel.SecurityTokenService.SecurityTokenService.BeginIssue(IClaimsPrincipal principal, RequestSecurityToken request, AsyncCallback callback, Object state)  

   at Microsoft.IdentityModel.Protocols.WSTrust.WSTrustServiceContract.DispatchRequestAsyncResult..ctor(DispatchContext dispatchContext, AsyncCallback asyncCallback, Object asyncState)  

   at Microsoft.IdentityModel.Protocols.WSTrust.WSTrustServiceContract.BeginDispatchRequest(DispatchContext dispatchContext, AsyncCallback asyncCallback, Object asyncState)  

   at Microsoft.IdentityModel.Protocols.WSTrust.WSTrustServiceContract.BeginProcessCore(Message requestMessage, WSTrustRequestSerializer requestSerializer, WSTrustResponseSerializer responseSerializer, String requestAction, String responseAction, String trustNamespace, AsyncCallback callback, Object state)  

System.InvalidOperationException: No corresponding start element is open.  

   at System.Xml.XmlBaseReader.ReadEndElement()  

   at Microsoft.IdentityModel.Protocols.XmlSignature.SignedInfo.ReadFrom(XmlDictionaryReader reader, TransformFactory transformFactory)  

   at Microsoft.IdentityModel.Protocols.XmlSignature.Signature.ReadFrom(XmlDictionaryReader reader)  

   at Microsoft.IdentityModel.Protocols.XmlSignature.EnvelopedSignatureReader.ReadSignature()  

   at Microsoft.IdentityModel.Protocols.XmlSignature.EnvelopedSignatureReader.TryReadSignature()  

Followed by a   Event ID  1000 (Warning)  

Additional Data   

Caller:  

DOMAIN\xxx_someAD account  

OnBehalfOf user:  

ActAs user:  

Target Relying Party:  

xxx.xxx.xxxx  

Seems we are missing a element when passing the XM soap request from the SP to IDP, However I cannot ascertain which element it is expecting.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-11*

In the context of ADFS and WS-Trust requests, the XML structure must adhere to the WS-Trust standard, which defines how security tokens are requested, issued, and validated in a federated authentication scenario.
