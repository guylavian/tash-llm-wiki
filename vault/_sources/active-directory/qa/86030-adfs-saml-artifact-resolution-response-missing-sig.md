---
title: "ADFS SAML Artifact Resolution Response Missing Signature"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/86030/adfs-saml-artifact-resolution-response-missing-sig
question_id: 86030
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS SAML Artifact Resolution Response Missing Signature

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/86030/adfs-saml-artifact-resolution-response-missing-sig (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to integrate ADFS with our Service Provider (SP). I've enabled the Artifact Resolution (SOAP) mechanism in ADFS and ADFS does response to an ArtifactRequest message with an ArtifactResponse message, but the ArtifactResponse is missing a ds:Signature element (signature on the ArtifactResponse). It does include a signature inside the Response, but the SAML protocol specification (e.g. http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0-cd-02.html#5.1.2.SP-Initiated%20SSO:%20%20Redirect/POST%20Bindings|outline) says that the ArtifactResponse should look like:

<samlp:ArtifactResponsexmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="identifier_3"

InResponseTo="identifier_2"

Version="2.0"

IssueInstant="2004-12-05T09:22:05Z">

<!-- an ArtifactResponse message SHOULD be signed -->

<ds:Signature

xmlns:ds="http://www.w3.org/2000/09/xmldsig#">...</ds:Signature>

<samlp:Status>

<samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/></samlp:Status>

<samlp:Responsexmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ... > ...</samlp:Response>

</samlp:ArtifactResponse>

The response from ADFS is missing the ds:Signature element here. Consequently, the SAML library in our SP is rejecting the ArtifactResponse as "unauthenticated".

Is there some setting in ADFS required to provide the required signature? I haven't been able to find one.

Thanks.

## Answers

_No answers on this thread._
