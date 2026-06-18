---
title: "Chapter 1. Planning for securing applications and services - Red Hat Single Sign-On 7.6 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhsso-7-6-planning-for-securing-applications-and-services
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html/securing_applications_and_services_guide/planning_for_securing_applications_and_services
guide: securing_applications_and_services_guide
version: 7.6
family: rhsso
documentKind: "Documentation"
---

# Chapter 1. Planning for securing applications and services - Red Hat Single Sign-On 7.6 Securing Applications and Services Guide

Chapter 1. Planning for securing applications and services
Red Hat Single Sign-On supports both OpenID Connect (an extension to OAuth 2.0) and SAML 2.0. When securing clients and services the first thing you need to decide is which of the two you are going to use. If you want you can also choose to secure some with OpenID Connect and others with SAML.
To secure clients and services you are also going to need an adapter or library for the protocol you’ve selected. Red Hat Single Sign-On comes with its own adapters for selected platforms, but it is also possible to use generic OpenID Connect Relying Party and SAML Service Provider libraries.
1.1. Client adapters
Red Hat Single Sign-On client adapters are libraries that make it very easy to secure applications and services with Red Hat Single Sign-On. We call them adapters rather than libraries as they provide a tight integration to the underlying platform and framework. This makes our adapters easy to use and they require less boilerplate code than what is typically required by a library.
1.2. Supported Platforms
Red Hat Single Sign-On enables you to protect applications running on different platforms and using different technology stacks using OpenID Connect and SAML protocols.
1.2.1. OpenID Connect
1.2.1.1. Java
1.2.1.2. JavaScript (client-side)
1.2.1.3. Node.js (server-side)
1.2.2. SAML
1.2.2.1. Java
1.2.2.2. Apache HTTP Server
1.3. Supported Protocols
Red Hat Single Sign-On supports both OpenID Connect and SAML protocols.
1.3.1. OpenID Connect
OpenID Connect (OIDC) is an authentication protocol that is an extension of OAuth 2.0. While OAuth 2.0 is only a framework for building authorization protocols and is mainly incomplete, OIDC is a full-fledged authentication and authorization protocol. OIDC also makes heavy use of the Json Web Token (JWT) set of standards. These standards define an identity token JSON format and ways to digitally sign and encrypt that data in a compact and web-friendly way.
There are really two types of use cases when using OIDC. The first is an application that asks the Red Hat Single Sign-On server to authenticate a user for them. After a successful login, the application will receive an identity token and an access token. The identity token contains information about the user such as username, email, and other profile information. The access token is digitally signed by the realm and contains access information (like user role mappings) that the application can use to determine what resources the user is allowed to access on the application.
The second type of use cases is that of a client that wants to gain access to remote services. In this case, the client asks Red Hat Single Sign-On to obtain an access token it can use to invoke on other remote services on behalf of the user. Red Hat Single Sign-On authenticates the user then asks the user for consent to grant access to the client requesting it. The client then receives the access token. This access token is digitally signed by the realm. The client can make REST invocations on remote services using this access token. The REST service extracts the access token, verifies the signature of the token, then decides based on access information within the token whether or not to process the request.
1.3.2. SAML 2.0
SAML 2.0 is a similar specification to OIDC but a lot older and more mature. It has its roots in SOAP and the plethora of WS-* specifications so it tends to be a bit more verbose than OIDC. SAML 2.0 is primarily an authentication protocol that works by exchanging XML documents between the authentication server and the application. XML signatures and encryption are used to verify requests and responses.
In Red Hat Single Sign-On SAML serves two types of use cases: browser applications and REST invocations.
There are really two types of use cases when using SAML. The first is an application that asks the Red Hat Single Sign-On server to authenticate a user for them. After a successful login, the application will receive an XML document that contains something called a SAML assertion that specifies various attributes about the user. This XML document is digitally signed by the realm and contains access information (like user role mappings) that the application can use to determine what resources the user is allowed to access on the application.
The second type of use cases is that of a client that wants to gain access to remote services. In this case, the client asks Red Hat Single Sign-On to obtain a SAML assertion it can use to invoke on other remote services on behalf of the user.
1.3.3. OpenID Connect vs. SAML
Choosing between OpenID Connect and SAML is not just a matter of using a newer protocol (OIDC) instead of the older more mature protocol (SAML).
In most cases Red Hat Single Sign-On recommends using OIDC.
SAML tends to be a bit more verbose than OIDC.
Beyond verbosity of exchanged data, if you compare the specifications you’ll find that OIDC was designed to work with the web while SAML was retrofitted to work on top of the web. For example, OIDC is also more suited for HTML5/JavaScript applications because it is easier to implement on the client side than SAML. As tokens are in the JSON format, they are easier to consume by JavaScript. You will also find several nice features that make implementing security in your web applications easier. For example, check out the iframe trick that the specification uses to easily determine if a user is still logged in or not.
SAML has its uses though. As you see the OIDC specifications evolve you see they implement more and more features that SAML has had for years. What we often see is that people pick SAML over OIDC because of the perception that it is more mature and also because they already have existing applications that are secured with it.
1.4. Terminology
These terms are used in this guide:
-
Clients
are entities that interact with Red Hat Single Sign-On to authenticate users and obtain tokens. Most often, clients are applications and services acting on behalf of users that provide a single sign-on experience to their users and access other services using the tokens issued by the server. Clients can also be entities only interested in obtaining tokens and acting on their own behalf for accessing other services. -
Applications
include a wide range of applications that work for specific platforms for each protocol -
Client adapters
are libraries that make it easy to secure applications and services with Red Hat Single Sign-On. They provide a tight integration to the underlying platform and framework. -
Creating a client
andregistering a client
are the same action.Creating a Client
is the term used to create a client by using the Admin Console.Registering a client
is the term used to register a client by using the Red Hat Single Sign-On Client Registration Service. -
A service account
is a type of client that is able to obtain tokens on its own behalf.
1.5. Basic steps to secure applications and services
These are the basic steps for securing an application or a service in Red Hat Single Sign-On.
Configure a client using one of these options:
- A Red Hat Single Sign-On adapter
- A generic OpenID connect or SAML library
Register a client using one of these options:
- The Red Hat Single Sign-On Admin Console
- The client registration service
- The CLI
