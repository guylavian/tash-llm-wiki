---
title: "Chapter 9. Policy enforcers - Red Hat build of Keycloak 26.6 Authorization Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-enforcer-overview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/authorization_services_guide/enforcer_overview
guide: authorization_services_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Policy Enforcement Point (PEP) is a design pattern and as such you can implement it in different ways. Red Hat build of Keycloak provides all the necessary means to implement PEPs for different platforms, environments, and programming languages. Red Hat build of Keycloak Authorization Services presents a RESTful API and leverages OAuth2 authorization capabilities for fine-grained authorization usi…"
---

# Chapter 9. Policy enforcers - Red Hat build of Keycloak 26.6 Authorization Services Guide

Chapter 9. Policy enforcers
Policy Enforcement Point (PEP) is a design pattern and as such you can implement it in different ways. Red Hat build of Keycloak provides all the necessary means to implement PEPs for different platforms, environments, and programming languages. Red Hat build of Keycloak Authorization Services presents a RESTful API and leverages OAuth2 authorization capabilities for fine-grained authorization using a centralized authorization server.
The Policy enforcers available by Red Hat build of Keycloak are:
- Java Policy enforcer - useful to be used in the Java client applications
- Javascript Policy enforcer - useful to be used in the applications secured by Red Hat build of Keycloak Javascript adapter
9.1. JavaScript integration for Policy Enforcer
The Red Hat build of Keycloak Server comes with a JavaScript library you can use to interact with a resource server protected by a policy enforcer. This library is based on the Red Hat build of Keycloak JavaScript adapter, which can be integrated to allow your client to obtain permissions from a Red Hat build of Keycloak Server.
You can obtain this library by installing it from NPM:
npm install keycloak-js
Next, you can create a KeycloakAuthorization
instance as follows:
import Keycloak from "keycloak-js";
import KeycloakAuthorization from "keycloak-js/authz";
const keycloak = new Keycloak({
url: "http://keycloak-server",
realm: "my-realm",
clientId: "my-app"
});
const authorization = new KeycloakAuthorization(keycloak);
await keycloak.init();
// Now you can use the authorization object to interact with the server.
The keycloak-js/authz
library provides two main features:
- Obtain permissions from the server using a permission ticket, if you are accessing a UMA protected resource server.
- Obtain permissions from the server by sending the resources and scopes the application wants to access.
In both cases, the library allows you to easily interact with both resource server and Red Hat build of Keycloak Authorization Services to obtain tokens with permissions your client can use as bearer tokens to access the protected resources on a resource server.
9.1.1. Handling authorization responses from a UMA-Protected resource server
If a resource server is protected by a policy enforcer, it responds to client requests based on the permissions carried along with a bearer token. Typically, when you try to access a resource server with a bearer token that is lacking permissions to access a protected resource, the resource server responds with a 401 status code and a WWW-Authenticate
header.
HTTP/1.1 401 Unauthorized
WWW-Authenticate: UMA realm="${realm-name}",
as_uri="https://${host}:${port}/realms/${realm-name}",
ticket="016f84e8-f9b9-11e0-bd6f-0021cc6004de"
See UMA Authorization Process for more information.
What your client needs to do is extract the permission ticket from the
header returned by the resource server and use the library to send an authorization request as follows:
WWW-Authenticate
// prepare a authorization request with the permission ticket
const authorizationRequest = { ticket };
// send the authorization request, if successful retry the request
authorization.authorize(authorizationRequest).then((rpt) => {
// onGrant
}, () => {
// onDeny
}, () => {
// onError
});
The authorize
function is completely asynchronous and supports a few callback functions to receive notifications from the server:
-
onGrant
: The first argument of the function. If authorization succeeds and the server returns an RPT with the requested permissions, the callback receives the RPT. -
onDeny
: The second argument of the function. Only called if the server has denied the authorization request. -
onError
: The third argument of the function. Only called if the server responds unexpectedly.
Most applications should use the onGrant
callback to retry a request after a 401 response. Subsequent requests should include the RPT as a bearer token for retries.
9.1.2. Obtaining entitlements
The keycloak-js/authz
library provides an entitlement
function that you can use to obtain an RPT from the server by providing the resources and scopes your client wants to access.
Example about how to obtain an RPT with permissions for all resources and scopes the user can access
authorization.entitlement("my-resource-server-id").then((rpt) => {
// onGrant callback function.
// If authorization was successful you'll receive an RPT
// with the necessary permissions to access the resource server
});
Example about how to obtain an RPT with permissions for specific resources and scopes
authorization.entitlement("my-resource-server", {
permissions: [
{
id: "Some Resource"
}
]
}).then((rpt) => {
// onGrant
});
When using the entitlement
function, you must provide the client_id of the resource server you want to access.
The entitlement
function is completely asynchronous and supports a few callback functions to receive notifications from the server:
-
onGrant
: The first argument of the function. If authorization succeeds and the server returns an RPT with the requested permissions, the callback receives the RPT. -
onDeny
: The second argument of the function. Only called if the server has denied the authorization request. -
onError
: The third argument of the function. Only called if the server responds unexpectedly.
9.1.3. Authorization request
Both authorize
and entitlement
functions accept an authorization request object. This object can be set with the following properties:
permissions
An array of objects representing the resource and scopes. For instance:
const authorizationRequest = { permissions: [ { id: "Some Resource", scopes: ["view", "edit"] } ] }
metadata
An object where its properties define how the authorization request should be processed by the server.
response_include_resource_name
A boolean value indicating to the server if resource names should be included in the RPT’s permissions. If false, only the resource identifier is included.
response_permissions_limit
An integer N that defines a limit for the amount of permissions an RPT can have. When used together with
rpt
parameter, only the last N requested permissions will be kept in the RPT
submit_request
A boolean value indicating whether the server should create permission requests to the resources and scopes referenced by a permission ticket. This parameter will only take effect when used together with the
ticket
parameter as part of a UMA authorization process.
9.1.4. Obtaining the RPT
If you have already obtained an RPT using any of the authorization functions provided by the library, you can always obtain the RPT as follows from the authorization object (assuming that it has been initialized by one of the techniques shown earlier):
const rpt = authorization.rpt;
