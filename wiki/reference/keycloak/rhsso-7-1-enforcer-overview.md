---
title: "Chapter 9. Policy Enforcers - Red Hat Single Sign-On 7.1 Authorization Services Guide"
type: reference
domain: keycloak
slug: rhsso-7-1-enforcer-overview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.1/html/authorization_services_guide/enforcer_overview
guide: authorization_services_guide
version: 7.1
family: rhsso
documentKind: "Documentation"
---

# Chapter 9. Policy Enforcers - Red Hat Single Sign-On 7.1 Authorization Services Guide

Chapter 9. Policy Enforcers
Policy Enforcement Point (PEP) is a design pattern and as such you can implement it in different ways. Red Hat Single Sign-On provides all the necessary means to implement PEPs for different platforms, environments, and programming languages. Red Hat Single Sign-On Authorization Services presents a RESTful API, and leverages OAuth2 authorization capabilities for fine-grained authorization using a centralized authorization server.
9.1. Red Hat Single Sign-On Adapter Policy Enforcer
You can enforce authorization decisions for your applications if you are using Red Hat Single Sign-On OIDC adapters.
When you enable policy enforcement for your Red Hat Single Sign-On application, the corresponding adapter intercepts all requests to your application and enforces the authorization decisions obtained from the server.
Policy enforcement is strongly linked to your application’s paths and the resources you created for a resource server using the Red Hat Single Sign-On Administration Console. By default, when you create a resource server, Red Hat Single Sign-On creates a default configuration for your resource server so you can enable policy enforcement quickly.
The default configuration allows access for all resources in your application provided the authenticated user belongs to the same realm as the resource server being protected.
9.1.1. Policy Enforcement Configuration
To enable policy enforcement for your application, add the following property to your keycloak.json file:
keycloak.json
{
"policy-enforcer": {}
}
Or a little more verbose if you want to manually define the resources being protected:
{
"policy-enforcer": {
"user-managed-access" : {},
"enforcement-mode" : "ENFORCING"
"paths": [
{
"path" : "/someUri/*",
"methods" : [
{
"method": "GET",
"scopes" : ["urn:app.com:scopes:view"]
},
{
"method": "POST",
"scopes" : ["urn:app.com:scopes:create"]
}
]
},
{
"name" : "Some Resource",
"path" : "/usingPattern/{id}",
"methods" : [
{
"method": "DELETE",
"scopes" : ["urn:app.com:scopes:delete"]
}
]
},
{
"path" : "/exactMatch"
},
{
"name" : "Admin Resources",
"path" : "/usingWildCards/*"
}
]
}
}
Here is a description of each configuration option:
policy-enforcer
Specifies the configuration options that define how policies are actually enforced and optionally the paths you want to protect. If not specified, the policy enforcer queries the server for all resources associated with the resource server being protected. In this case, you need to ensure the resources are properly configured with a URI property that matches the paths you want to protect.
user-managed-access
Specifies that the adapter uses the UMA protocol. If specified, the adapter queries the server for permission tickets and return them to clients according to the UMA specification. If not specified, the adapter relies on the requesting party token (RPT) sent to the server to enforce permissions.
enforcement-mode
Specifies how policies are enforced.
ENFORCING
(default mode) Requests are denied by default even when there is no policy associated with a given resource.
PERMISSIVE
Requests are allowed even when there is no policy associated with a given resource.
DISABLED
Completely disables the evaluation of policies and allows access to any resource.
on-deny-redirect-to
Defines a URL where a client request is redirected when an "access denied" message is obtained from the server. By default, the adapter responds with a 403 HTTP status code.
paths
Specifies the paths to protect.
name
The name of a resource on the server that is to be associated with a given path. When used in conjunction with a path, the policy enforcer ignores the resource’s URI property and uses the path you provided instead.
path
(required) A URI relative to the application’s context path. If this option is specified, the policy enforcer queries the server for a resource with a URI with the same value. Currently a very basic logic for path matching is supported. Examples of valid paths are:
-
Wildcards:
/*
-
Suffix:
/*.html
-
Sub-paths:
/path/*
- Path parameters: /resource/{id}
- Exact match: /resource
-
Wildcards:
methods The HTTP methods (for example, GET, POST, PATCH) to protect and how they are associated with the scopes for a given resource in the server. +[/'']
method
The name of the HTTP method.
scopes
An array of strings with the scopes associated with the method. When you associate scopes with a specific method, the client trying to access a protected resource (or path) must provide an RPT that grants permission to all scopes specified in the list. For example, if you define a method POST with a scope create, the RPT must contain a permission granting access to the create scope when performing a POST to the path.
enforcement-mode
Specifies how policies are enforced.
ENFORCING
(default mode) Requests are denied by default even when there is no policy associated with a given resource.
DISABLED
Disables the evaluation of policies for a path
9.1.2. Protecting a Stateless Service Using a Bearer Token
If the adapter is configured with the bearer-only
configuration option, the policy enforcer decides whether a request to access a protected resource is allowed or denied based on the permissions of the bearer token.
- HTTP GET example passing an RPT as a bearer token
GET /my-resource-server/my-protected-resource HTTP/1.1
Host: host.com
Authorization: Bearer ${RPT}
...
In this example, a keycloak.json file in your application is similar to the following:
Example of WEB-INF/keycloak.json with the bearer-only configuration option
...
"bearer-only" : true,
...
9.1.2.1. Authorization Response
When a client tries to access a resource server with a bearer token that is lacking permissions to access a protected resource, the resource server responds with a 401 status code and a WWW-Authenticate
header. The value of the WWW-Authenticate
header depends on the authorization protocol in use by the resource server.
Here is an example of a response from a resource server that is using UMA as the authorization protocol:
HTTP/1.1 401 Unauthorized
WWW-Authenticate: UMA realm="photoz-restful-api",as_uri="http://localhost:8080/auth/realms/photoz/authz/authorize",ticket="${PERMISSION_TICKET}"
And another example when the resource server is using the Entitlement protocol:
HTTP/1.1 401 Unauthorized
WWW-Authenticate: KC_ETT realm="photoz-restful-api",as_uri="http://localhost:8080/auth/realms/photoz/authz/entitlement"
Once a client receives a response from the server, it examines the status code and WWW-Authenticate
header to obtain an RPT from the Red Hat Single Sign-On Server.
9.1.3. Obtaining the Authorization Context
When policy enforcement is enabled, the permissions obtained from the server are available through org.keycloak.AuthorizationContext
. This class provides several methods you can use to obtain permissions and ascertain whether a permission was granted for a particular resource or scope.
Obtaining the Authorization Context in a Servlet Container
HttpServletRequest request = ... // obtain javax.servlet.http.HttpServletRequest
KeycloakSecurityContext keycloakSecurityContext =
(KeycloakSecurityContext) request
.getAttribute(KeycloakSecurityContext.class.getName());
AuthorizationContext authzContext =
keycloakSecurityContext.getAuthorizationContext();
For more details about how you can obtain a KeycloakSecurityContext
consult the adapter configuration. The example above should be sufficient to obtain the context when running an application using any of the servlet containers supported by Red Hat Single Sign-On.
The authorization context helps give you more control over the decisions made and returned by the server. For example, you can use it to build a dynamic menu where items are hidden or shown depending on the permissions associated with a resource or scope.
if (authzContext.hasResourcePermission("Project Resource")) {
// user can access the Project Resource
}
if (authzContext.hasResourcePermission("Admin Resource")) {
// user can access administration resources
}
if (authzContext.hasScopePermission("urn:project.com:project:create")) {
// user can create new projects
}
The AuthorizationContext
represents one of the main capabilities of Red Hat Single Sign-On Authorization Services. From the examples above, you can see that the protected resource is not directly associated with the policies that govern them.
Consider some similar code using role-based access control (RBAC):
if (User.hasRole('user')) {
// user can access the Project Resource
}
if (User.hasRole('admin')) {
// user can access administration resources
}
if (User.hasRole('project-manager')) {
// user can create new projects
}
Although both examples address the same requirements, they do so in different ways. In RBAC, roles only implicitly define access for their resources. With Red Hat Single Sign-On you gain the capability to create more manageable code that focuses directly on your resources whether you are using RBAC, attribute-based access control (ABAC), or any other BAC variant. Either you have the permission for a given resource or scope, or you don’t.
Now, suppose your security requirements have changed and in addition to project managers, PMOs can also create new projects.
Security requirements change, but with Red Hat Single Sign-On there is no need to change your application code to address the new requirements. Once your application is based on the resource and scope identifier, you need only change the configuration of the permissions or policies associated with a particular resource in the authorization server. In this case, the permissions and policies associated with the Project Resource
and/or the scope urn:project.com:project:create
would be changed.
9.1.4. JavaScript Integration
The Red Hat Single Sign-On Server comes with a JavaScript library you can use to interact with a resource server protected by a policy enforcer. This library is based on the Red Hat Single Sign-On JavaScript adapter, which can be integrated to allow your client to obtain permissions from a Red Hat Single Sign-On Server.
You can obtain this library from a running a Red Hat Single Sign-On Server instance by including the following script
tag in your web page:
<script src="http://.../auth/js/keycloak-authz.js"></script>
Once you do that, you can create a KeycloakAuthorization
instance as follows:
var keycloak = ... // obtain a Keycloak instance from keycloak.js library
var authorization = new KeycloakAuthorization(keycloak);
The keycloak-authz.js library provides two main features:
Handle responses from a resource server protected by a Red Hat Single Sign-On Policy Enforcer and obtain a requesting party token (RPT) with the necessary permissions to gain access to the protected resources on the resource server.
- In this case, the library can handle whatever authorization protocol the resource server is using: Entitlements.
- Obtain permissions from a Red Hat Single Sign-On Server using the Entitlement API.
In both cases, the library allows you to easily interact with both resource server and Red Hat Single Sign-On Authorization Services to obtain tokens with permissions your client can use as bearer tokens to access the protected resources on a resource server.
9.1.4.1. Handling Authorization Responses from a Resource Server
If a resource server is protected by a policy enforcer, it responds to client requests based on the permissions carried along with a bearer token. Typically, when you try to access a resource server with a bearer token that is lacking permissions to access a protected resource, the resource server responds with a 401 status code and a WWW-Authenticate
header.
The value of the WWW-Authenticate
header depends on the authorization protocol in use by the resource server. Whatever protocol is in use, you can use a KeycloakAuthorization
instance to handle responses as follows:
var wwwAuthenticateHeader = ... // extract WWW-Authenticate Header from the response in case of a 401 status code
authorization.authorize(wwwAuthenticateHeader).then(function (rpt) {
// onGrant callback function.
// If authorization was successful you'll receive an RPT
// with the necessary permissions to access the resource server
}, function () {
// onDeny callback function.
// Called when the authorization request is denied by the server
}, function () {
// onError callback function. Called when the server responds unexpectedly
});
The authorize
function is completely asynchronous and supports a few callback functions to receive notifications from the server:
-
onGrant
: The first argument of the function. If authorization was successful and the server returned an RPT with the requested permissions, the callback receives the RPT. -
onDeny
: The second argument of the function. Only called if the server has denied the authorization request. -
onError
: The third argument of the function. Only called if the server responds unexpectedly.
Most applications should use the onGrant
callback to retry a request after a 401 response. Subsequent requests should include the RPT as a bearer token for retries.
9.1.4.2. Obtaining Entitlements
The keycloak-authz.js library provides an entitlement
function that you can use to obtain an RPT from the server using the Entitlement API.
authorization.entitlement('my-resource-server-id').then(function (rpt) {
// onGrant callback function.
// If authorization was successful you'll receive an RPT
// with the necessary permissions to access the resource server
});
When using the entitlement
function, you must provide the client_id of the resource server you want to access.
The entitlement
function is completely asynchronous and supports a few callback functions to receive notifications from the server:
-
onGrant
: The first argument of the function. If authorization was successful and the server returned an RPT with the requested permissions, the callback receives the RPT. -
onDeny
: The second argument of the function. Only called if the server has denied the authorization request. -
onError
: The third argument of the function. Only called if the server responds unexpectedly.
9.1.4.3. Obtaining the RPT
If you have already obtained an RPT using any of the authorization functions provided by the library, you can always obtain the RPT as follows from the authorization object (assuming that it has been initialized by one of the techniques shown earlier):
var rpt = authorization.rpt;
9.1.5. Setting Up TLS/HTTPS
When the server is using HTTPS, ensure your adapter is configured as follows:
keycloak.json
{
"truststore": "path_to_your_trust_store",
"truststore-password": "trust_store_password"
}
The configuration above enables TLS/HTTPS to the Authorization Client, making possible to access a Red Hat Single Sign-On Server remotely using the HTTPS scheme.
It is strongly recommended that you enable TLS/HTTPS when accessing the Red Hat Single Sign-On Server endpoints.
