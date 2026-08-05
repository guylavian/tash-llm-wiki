---
title: "Chapter 1. Planning for securing applications and services - Red Hat build of Keycloak 26.4 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-overview-3
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/securing_applications_and_services_guide/overview-
guide: securing_applications_and_services_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
abstract: "Understand basic concepts for securing applications. As an OAuth2, OpenID Connect and SAML compliant server, Red Hat build of Keycloak can secure any application and service as long as the technology stack they are using supports any of these protocols. For more details about the security protocols supported by Red Hat build of Keycloak, consider looking at Server Administration Guide. Most of the…"
---

# Chapter 1. Planning for securing applications and services - Red Hat build of Keycloak 26.4 Securing Applications and Services Guide

Chapter 1. Planning for securing applications and services
Understand basic concepts for securing applications.
As an OAuth2, OpenID Connect and SAML compliant server, Red Hat build of Keycloak can secure any application and service as long as the technology stack they are using supports any of these protocols. For more details about the security protocols supported by Red Hat build of Keycloak, consider looking at Server Administration Guide.
Most of the support for some of these protocols is already available from the programming language, framework, or reverse proxy they are using. Leveraging the support already available from the application ecosystem is a key aspect to make your application fully compliant with security standards and best practices, so that you avoid vendor lock-in.
For some programming languages, Red Hat build of Keycloak provides libraries that try to fill the gap for the lack of support of a particular security protocol or to provide a more rich and tightly coupled integration with the server. These libraries are known by Keycloak Client Adapters, and they should be used as a last resort if you cannot rely on what is available from the application ecosystem.
1.1. Basic steps to secure applications and services
These are the basic steps for securing an application or a service in Red Hat build of Keycloak.
Register a client to a realm using one of these options:
- The Red Hat build of Keycloak Admin Console
- The client registration service
- The CLI
Enable OpenID Connect or SAML protocols in your application using one these options:
- Leveraging existing OpenID Connect and SAML support from the application ecosystem
- Using a Red Hat build of Keycloak Adapter
This guide provides the detailed instructions for these steps. You can find more details in the Server Administration Guide about how to register a client to Red Hat build of Keycloak through the administration console.
1.2. Getting Started
The Red Hat build of Keycloak Quickstarts Repository provides examples about how to secure applications and services using different programming languages and frameworks. By going through their documentation and codebase, you will understand the bare minimum changes required in your application and service in order to secure it with Red Hat build of Keycloak.
Also, see the following sections for recommendations for trusted and well-known client-side implementations for both OpenID Connect and SAML protocols.
1.2.1. OpenID Connect
1.2.1.1. JavaScript (client-side)
1.2.1.2. Node.js (server-side)
1.2.2. SAML
1.2.2.1. Java
1.3. Terminology
These terms are used in this guide:
-
Clients
are entities that interact with Red Hat build of Keycloak to authenticate users and obtain tokens. Most often, clients are applications and services acting on behalf of users that provide a single sign-on experience to their users and access other services using the tokens issued by the server. Clients can also be entities only interested in obtaining tokens and acting on their own behalf for accessing other services. -
Applications
include a wide range of applications that work for specific platforms for each protocol -
Client adapters
are libraries that make it easy to secure applications and services with Red Hat build of Keycloak. They provide a tight integration to the underlying platform and framework. -
Creating a client
andregistering a client
are the same action.Creating a Client
is the term used to create a client by using the Admin Console.Registering a client
is the term used to register a client by using the Red Hat build of Keycloak Client Registration Service. -
A service account
is a type of client that is able to obtain tokens on its own behalf.
