---
title: "Chapter 2. Feature Overview - Red Hat Single Sign-On 7.1 Release Notes"
type: reference
domain: keycloak
slug: rhsso-7-1-feature-overview-1
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.1/html/release_notes/feature_overview-1
guide: release_notes
version: 7.1
family: rhsso
documentKind: "Documentation"
abstract: "2.1. OpenID Connect Certification The Keycloak version included in Red Hat Single Sign-On (RH-SSO) 7.1 conforms to the 5 OpenID Connect profiles: Basic, Implicit, Hybrid, Config, and Dynamic. Certification was achieved in Keycloak v2.3 (http://openid.net/certification/). Future RH-SSO 7.x versions will remain compatible with these profiles, unless documented otherwise. 2.2. Client adapter for Red …"
---

# Chapter 2. Feature Overview - Red Hat Single Sign-On 7.1 Release Notes

Chapter 2. Feature Overview
2.1. OpenID Connect Certification
The Keycloak version included in Red Hat Single Sign-On (RH-SSO) 7.1 conforms to the 5 OpenID Connect profiles: Basic, Implicit, Hybrid, Config, and Dynamic. Certification was achieved in Keycloak v2.3 (http://openid.net/certification/). Future RH-SSO 7.x versions will remain compatible with these profiles, unless documented otherwise.
2.2. Client adapter for Red Hat JBoss Fuse
RH-SSO 7.1 features a new client adapter for Red Hat JBoss Fuse, which enables securing of web application archives (WARs), servlets, Apache routes and Apache CXF endpoints deployed on JBoss Fuse, in both the Apache Karaf and Red Hat JBoss Enterprise Application Platform (JBoss EAP).
2.3. Node.js client adapter
RH-SSO 7.1 includes a new Node.js client adapter, which enables use of RH-SSO 7.1 Server for authentication and web single sign-on for Node.js applications.
2.4. Externalized authorization service
RH-SSO 7.1 introduces a new authorization service feature-set, based on the User Managed Access (UMA) specification. This enables RH-SSO 7.1 Server to act as a Policy Administration Point (PAP), Policy Decision Point (PDP), or Policy Information Point (PIP), separating the authorization logic from the application.
2.5. User Storage SPI
RH-SSO 7.1 features a new User Storage SPI that you can use to implement your own custom user storage federation provider, such as a relational or NoSQL database, to enable federation of users from any user store.
2.6. SSSD integration
RH-SSO 7.1 adds an integration with System Security Services Daemon (SSSD) in Red Hat Enterprise Linux (RHEL) 7.3. This enables use of SSSD as a user federation provider in front of a Microsoft Active Directory forest.
2.7. Client registration CLI
RH SSO 7.1 introduces a command-line interface (CLI) for developers to register client applications on RH-SSO Server.
2.8. RPM distribution
RH-SSO 7.1 introduces a new RPM distribution for Red Hat Enterprise Linux 6 and 7. The RH-SSO Server is provided in its own channel; the client adapters for JBoss EAP 6 and 7 are provided in their respective JBoss EAP x86_64 channels. The JBoss Fuse and Node.js client adapters are not available as RPMs.
