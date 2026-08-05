---
title: "ADFS idpinitiatedsignon SAML assertion not signed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/12295/adfs-idpinitiatedsignon-saml-assertion-not-signed
question_id: 12295
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS idpinitiatedsignon SAML assertion not signed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/12295/adfs-idpinitiatedsignon-saml-assertion-not-signed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to extract SAMLResponse assertion via https://<adfs_domain>/adfs/ls/idpinitiatedsignon using a webview. The problem is that the SAMLResponse assertion is not signed and the signature is not included inside the assertion.    

As a result I cannot validate the SAML assertion. We have configured ADFS with an ADFS signing cert since it is an IDP initiated flow.    

Also we set the following property in ADFS: SamlResponseSignature = AssertionOnly    

See attached for SAMLResponse.xml

## Answers

_No answers on this thread._
