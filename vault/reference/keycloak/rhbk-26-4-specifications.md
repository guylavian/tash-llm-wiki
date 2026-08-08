---
title: "Chapter 13. Specifications implemented - Red Hat build of Keycloak 26.4 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-specifications
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/securing_applications_and_services_guide/specifications-
guide: securing_applications_and_services_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
abstract: "List of specifications and standards implemented by Red Hat build of Keycloak. This chapter presents a list of specifications and standards that Red Hat build of Keycloak currently implements. The standards are separated in different sections and, in each one, a table is shown with the following four columns: Specification: The standard or specification that Red Hat build of Keycloak implements. S…"
---

# Chapter 13. Specifications implemented - Red Hat build of Keycloak 26.4 Securing Applications and Services Guide

Chapter 13. Specifications implemented
List of specifications and standards implemented by Red Hat build of Keycloak.
This chapter presents a list of specifications and standards that Red Hat build of Keycloak currently implements. The standards are separated in different sections and, in each one, a table is shown with the following four columns:
- Specification: The standard or specification that Red Hat build of Keycloak implements.
- Status: The current status of the implementation inside Red Hat build of Keycloak (supported, preview, experimental,…). See Enabling and disabling features for more information.
Conformity: Assurance of conformity of the implementation.
- Certified (version): The specification provides conformance tests that Red Hat build of Keycloak executes periodically and for each new version. The version in brackets is the last version of Red Hat build of Keycloak certified by the authority.
- Passed: There are conformance tests provided by the authority that Red Hat build of Keycloak passes, but no version is certified yet.
- Partial: There are conformance tests but Red Hat build of Keycloak is not yet fully passing them.
- If this column is empty means that Red Hat build of Keycloak does not pass any external conformance tests for the spec. Only common project integration tests are executed. Maybe the authority does not provide a conformance tests suite or Red Hat build of Keycloak is not interested in passing them.
- Comments: A generic column that can contain details of the implementation or the status. For example parts that are not covered yet or specific behaviors out of the spec.
13.1. OpenID Connect
| Specification | Status | Conformity | Comments |
|---|---|---|---|
| Supported | Certified (18.0.0) | ||
| Supported | Certified (18.0.0) | ||
| Supported | Certified (18.0.0) | ||
| Supported | Certified (18.0.0) | ||
| Supported | Certified (18.0.0) | ||
| Supported | Certified (18.0.0) | ||
| Supported | Certified (18.0.0) | ||
| OpenID Connect Client-Initiated Backchannel Authentication Flow | Supported | Certified (18.0.0) | |
| Supported | Certified (18.0.0) | ||
| Supported | Certified (18.0.0) | ||
| Supported | |||
| Experimental |
13.2. OAuth
13.3. Financial-grade API (FAPI)
| Specification | Status | Conformity | Comments |
|---|---|---|---|
| Supported | Certified (15.0.2) | ||
| Supported | Certified (15.0.2) | ||
| Financial-grade API: JWT Secured Authorization Response Mode for OAuth 2.0 (JARM) | Supported | Certified (15.0.2) | |
| Financial-grade API: Client Initiated Backchannel Authentication Profile (Draft) | Supported | Certified (15.0.2) | |
| Supported | Passed | ||
| Supported | Passed |
13.4. Security Assertion Markup Language (SAML)
| Specification | Status | Conformity | Comments |
|---|---|---|---|
| Supported | This standard covers multiple bindings and contexts. Red Hat build of Keycloak implements a full range of them but there are missing parts for sure. |
13.5. User Managed Access (UMA)
| Specification | Status | Conformity | Comments |
|---|---|---|---|
| User-Managed Access (UMA) 2.0 Grant for OAuth 2.0 Authorization | Supported | ||
| Supported |
13.6. JSON Web
| Specification | Status | Conformity | Comments |
|---|---|---|---|
| Supported | |||
| Supported | |||
| Supported | |||
| Supported | |||
| Supported | |||
| Supported |
13.7. Misc
| Specification | Status | Conformity | Comments |
|---|---|---|---|
| Security Requirements for Cryptographic Modules (FIPS 140-2) | Supported | Certified | Red Hat build of Keycloak uses Bouncy Castle (BC) FIPS libraries to provide FIPS 140-2. BC is indeed a certified FIPS 140-3 implementation, but also needs a certified stack (Operative system and Java VM). See FIPS 140-2 support for more information. |
| Web Authentication: An API for accessing Public Key Credentials Level 2 | Supported | This specification has conformance tests but Red Hat build of Keycloak is not using them. Red Hat build of Keycloak acts as a WebAuthn’s Relying Party (RP) for this specification. |
