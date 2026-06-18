---
title: "Chapter 9. Policy enforcers - Red Hat Single Sign-On 7.5 Authorization Services Guide"
type: reference
domain: keycloak
slug: rhsso-7-5-enforcer-overview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.5/html/authorization_services_guide/enforcer_overview
guide: authorization_services_guide
version: 7.5
family: rhsso
documentKind: "Documentation"
---

# Chapter 9. Policy enforcers - Red Hat Single Sign-On 7.5 Authorization Services Guide

Chapter 9. Policy enforcers
Policy Enforcement Point (PEP) is a design pattern and as such you can implement it in different ways. Red Hat Single Sign-On provides all the necessary means to implement PEPs for different platforms, environments, and programming languages. Red Hat Single Sign-On Authorization Services presents a RESTful API, and leverages OAuth2 authorization capabilities for fine-grained authorization using a centralized authorization server.
A PEP is responsible for enforcing access decisions from the Red Hat Single Sign-On server where these decisions are taken by evaluating the policies associated with a protected resource. It acts as a filter or interceptor in your application in order to check whether or not a particular request to a protected resource can be fulfilled based on the permissions granted by these decisions.
Permissions are enforced depending on the protocol you are using. When using UMA, the policy enforcer always expects an RPT as a bearer token in order to decide whether or not a request can be served. That means clients should first obtain an RPT from Red Hat Single Sign-On before sending requests to the resource server.
However, if you are not using UMA, you can also send regular access tokens to the resource server. In this case, the policy enforcer will try to obtain permissions directly from the server.
If you are using any of the Red Hat Single Sign-On OIDC adapters, you can easily enable the policy enforcer by adding the following property to your keycloak.json file:
keycloak.json
{
"policy-enforcer": {}
}
When you enable the policy enforcer all requests sent your application are intercepted and access to protected resources will be granted depending on the permissions granted by Red Hat Single Sign-On to the identity making the request.
Policy enforcement is strongly linked to your application’s paths and the resources you created for a resource server using the Red Hat Single Sign-On Administration Console. By default, when you create a resource server, Red Hat Single Sign-On creates a default configuration for your resource server so you can enable policy enforcement quickly.
9.1. Configuration
To enable policy enforcement for your application, add the following property to your keycloak.json file:
keycloak.json
{
"policy-enforcer": {}
}
Or a little more verbose if you want to manually define the resources being protected:
{
"policy-enforcer": {
"user-managed-access" : {},
"enforcement-mode" : "ENFORCING",
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
Specifies the configuration options that define how policies are actually enforced and optionally the paths you want to protect. If not specified, the policy enforcer queries the server for all resources associated with the resource server being protected. In this case, you need to ensure the resources are properly configured with a URIS property that matches the paths you want to protect.
user-managed-access
Specifies that the adapter uses the UMA protocol. If specified, the adapter queries the server for permission tickets and returns them to clients according to the UMA specification. If not specified, the policy enforcer will be able to enforce permissions based on regular access tokens or RPTs. In this case, before denying access to the resource when the token lacks permission, the policy enforcer will try to obtain permissions directly from the server.
enforcement-mode
Specifies how policies are enforced.
ENFORCING
(default mode) Requests are denied by default even when there is no policy associated with a given resource.
PERMISSIVE
Requests are allowed even when there is no policy associated with a given resource.
DISABLED
Completely disables the evaluation of policies and allows access to any resource. When
enforcement-mode
isDISABLED
applications are still able to obtain all permissions granted by Red Hat Single Sign-On through the Authorization Context
on-deny-redirect-to
Defines a URL where a client request is redirected when an "access denied" message is obtained from the server. By default, the adapter responds with a 403 HTTP status code.
path-cache
Defines how the policy enforcer should track associations between paths in your application and resources defined in Red Hat Single Sign-On. The cache is needed to avoid unnecessary requests to a Red Hat Single Sign-On server by caching associations between paths and protected resources.
lifespan
Defines the time in milliseconds when the entry should be expired. If not provided, default value is 30000. A value equal to 0 can be set to completely disable the cache. A value equal to -1 can be set to disable the expiry of the cache.
max-entries
Defines the limit of entries that should be kept in the cache. If not provided, default value is 1000.
paths
Specifies the paths to protect. This configuration is optional. If not defined, the policy enforcer will discover all paths by fetching the resources you defined to your application in Red Hat Single Sign-On, where these resources are defined with
URIS
representing some paths in your application.name
The name of a resource on the server that is to be associated with a given path. When used in conjunction with a path, the policy enforcer ignores the resource’s URIS property and uses the path you provided instead.
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
- Patterns: /{version}/resource, /api/{version}/resource, /api/{version}/resource/*
-
Wildcards:
methods
The HTTP methods (for example, GET, POST, PATCH) to protect and how they are associated with the scopes for a given resource in the server.
method
The name of the HTTP method.
scopes
An array of strings with the scopes associated with the method. When you associate scopes with a specific method, the client trying to access a protected resource (or path) must provide an RPT that grants permission to all scopes specified in the list. For example, if you define a method POST with a scope create, the RPT must contain a permission granting access to the create scope when performing a POST to the path.
scopes-enforcement-mode
A string referencing the enforcement mode for the scopes associated with a method. Values can be ALL or ANY. If ALL, all defined scopes must be granted in order to access the resource using that method. If ANY, at least one scope should be granted in order to gain access to the resource using that method. By default, enforcement mode is set to ALL.
enforcement-mode
Specifies how policies are enforced.
ENFORCING
(default mode) Requests are denied by default even when there is no policy associated with a given resource.
- DISABLED
claim-information-point
Defines a set of one or more claims that must be resolved and pushed to the Red Hat Single Sign-On server in order to make these claims available to policies. See Claim Information Point for more details.
lazy-load-paths
Specifies how the adapter should fetch the server for resources associated with paths in your application. If true, the policy enforcer is going to fetch resources on-demand accordingly with the path being requested. This configuration is specially useful when you don’t want to fetch all resources from the server during deployment (in case you have provided no
paths
) or in case you have defined only a sub set ofpaths
and want to fetch others on-demand.http-method-as-scope
Specifies how scopes should be mapped to HTTP methods. If set to true, the policy enforcer will use the HTTP method from the current request to check whether or not access should be granted. When enabled, make sure your resources in Red Hat Single Sign-On are associated with scopes representing each HTTP method you are protecting.
claim-information-point
Defines a set of one or more global claims that must be resolved and pushed to the Red Hat Single Sign-On server in order to make these claims available to policies. See Claim Information Point for more details.
9.2. Claim Information Point
A Claim Information Point (CIP) is responsible for resolving claims and pushing these claims to the Red Hat Single Sign-On server in order to provide more information about the access context to policies. They can be defined as a configuration option to the policy-enforcer in order to resolve claims from different sources, such as:
- HTTP Request (parameters, headers, body, etc)
- External HTTP Service
- Static values defined in configuration
- Any other source by implementing the Claim Information Provider SPI
When pushing claims to the Red Hat Single Sign-On server, policies can base decisions not only on who a user is but also by taking context and contents into account, based on who, what, why, when, where, and which for a given transaction. It is all about Contextual-based Authorization and how to use runtime information in order to support fine-grained authorization decisions.
9.2.1. Obtaining information from the HTTP request
Here are several examples showing how you can extract claims from an HTTP request:
keycloak.json
"policy-enforcer": {
"paths": [
{
"path": "/protected/resource",
"claim-information-point": {
"claims": {
"claim-from-request-parameter": "{request.parameter['a']}",
"claim-from-header": "{request.header['b']}",
"claim-from-cookie": "{request.cookie['c']}",
"claim-from-remoteAddr": "{request.remoteAddr}",
"claim-from-method": "{request.method}",
"claim-from-uri": "{request.uri}",
"claim-from-relativePath": "{request.relativePath}",
"claim-from-secure": "{request.secure}",
"claim-from-json-body-object": "{request.body['/a/b/c']}",
"claim-from-json-body-array": "{request.body['/d/1']}",
"claim-from-body": "{request.body}",
"claim-from-static-value": "static value",
"claim-from-multiple-static-value": ["static", "value"],
"param-replace-multiple-placeholder": "Test {keycloak.access_token['/custom_claim/0']} and {request.parameter['a']} "
}
}
}
]
}
9.2.2. Obtaining information from an external HTTP service
Here are several examples showing how you can extract claims from an external HTTP Service:
keycloak.json
"policy-enforcer": {
"paths": [
{
"path": "/protected/resource",
"claim-information-point": {
"http": {
"claims": {
"claim-a": "/a",
"claim-d": "/d",
"claim-d0": "/d/0",
"claim-d-all": ["/d/0", "/d/1"]
},
"url": "http://mycompany/claim-provider",
"method": "POST",
"headers": {
"Content-Type": "application/x-www-form-urlencoded",
"header-b": ["header-b-value1", "header-b-value2"],
"Authorization": "Bearer {keycloak.access_token}"
},
"parameters": {
"param-a": ["param-a-value1", "param-a-value2"],
"param-subject": "{keycloak.access_token['/sub']}",
"param-user-name": "{keycloak.access_token['/preferred_username']}",
"param-other-claims": "{keycloak.access_token['/custom_claim']}"
}
}
}
}
]
}
9.2.3. Static claims
keycloak.json
"policy-enforcer": {
"paths": [
{
"path": "/protected/resource",
"claim-information-point": {
"claims": {
"claim-from-static-value": "static value",
"claim-from-multiple-static-value": ["static", "value"],
}
}
}
]
}
9.2.4. Claim information provider SPI
The Claim Information Provider SPI can be used by developers to support different claim information points in case none of the built-ins providers are enough to address their requirements.
For example, to implement a new CIP provider you need to implement org.keycloak.adapters.authorization.ClaimInformationPointProviderFactory
and ClaimInformationPointProvider
and also provide the file META-INF/services/org.keycloak.adapters.authorization.ClaimInformationPointProviderFactory
in your application`s classpath.
Example of org.keycloak.adapters.authorization.ClaimInformationPointProviderFactory
:
public class MyClaimInformationPointProviderFactory implements ClaimInformationPointProviderFactory<MyClaimInformationPointProvider> {
@Override
public String getName() {
return "my-claims";
}
@Override
public void init(PolicyEnforcer policyEnforcer) {
}
@Override
public MyClaimInformationPointProvider create(Map<String, Object> config) {
return new MyClaimInformationPointProvider(config);
}
}
Every CIP provider must be associated with a name, as defined above in the MyClaimInformationPointProviderFactory.getName
method. The name will be used to map the configuration from the claim-information-point
section in the policy-enforcer
configuration to the implementation.
When processing requests, the policy enforcer will call the MyClaimInformationPointProviderFactory.create method in order to obtain an instance of MyClaimInformationPointProvider. When called, any configuration defined for this particular CIP provider (via claim-information-point) is passed as a map.
Example of ClaimInformationPointProvider
:
public class MyClaimInformationPointProvider implements ClaimInformationPointProvider {
private final Map<String, Object> config;
public ClaimsInformationPointProvider(Map<String, Object> config) {
this.config = config;
}
@Override
public Map<String, List<String>> resolve(HttpFacade httpFacade) {
Map<String, List<String>> claims = new HashMap<>();
// put whatever claim you want into the map
return claims;
}
}
9.3. Obtaining the authorization context
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
9.4. Using the AuthorizationContext to obtain an Authorization Client Instance
The
can also be used to obtain a reference to the Authorization Client API configured to your application:
AuthorizationContext
ClientAuthorizationContext clientContext = ClientAuthorizationContext.class.cast(authzContext);
AuthzClient authzClient = clientContext.getClient();
In some cases, resource servers protected by the policy enforcer need to access the APIs provided by the authorization server. With an
instance in hands, resource servers can interact with the server in order to create resources or check for specific permissions programmatically.
AuthzClient
9.5. JavaScript integration
The Red Hat Single Sign-On Server comes with a JavaScript library you can use to interact with a resource server protected by a policy enforcer. This library is based on the Red Hat Single Sign-On JavaScript adapter, which can be integrated to allow your client to obtain permissions from a Red Hat Single Sign-On Server.
You can obtain this library from a running a Red Hat Single Sign-On Server instance by including the following script
tag in your web page:
<script src="http://.../auth/js/keycloak-authz.js"></script>
Once you do that, you can create a KeycloakAuthorization
instance as follows:
var keycloak = ... // obtain a Keycloak instance from keycloak.js library
var authorization = new KeycloakAuthorization(keycloak);
The keycloak-authz.js library provides two main features:
- Obtain permissions from the server using a permission ticket, if you are accessing a UMA protected resource server.
- Obtain permissions from the server by sending the resources and scopes the application wants to access.
In both cases, the library allows you to easily interact with both resource server and Red Hat Single Sign-On Authorization Services to obtain tokens with permissions your client can use as bearer tokens to access the protected resources on a resource server.
9.5.1. Handling authorization responses from a UMA-Protected resource server
If a resource server is protected by a policy enforcer, it responds to client requests based on the permissions carried along with a bearer token. Typically, when you try to access a resource server with a bearer token that is lacking permissions to access a protected resource, the resource server responds with a 401 status code and a WWW-Authenticate
header.
HTTP/1.1 401 Unauthorized
WWW-Authenticate: UMA realm="${realm}",
as_uri="https://${host}:${port}/auth/realms/${realm}",
ticket="016f84e8-f9b9-11e0-bd6f-0021cc6004de"
See UMA Authorization Process for more information.
What your client needs to do is extract the permission ticket from the
header returned by the resource server and use the library to send an authorization request as follows:
WWW-Authenticate
// prepare a authorization request with the permission ticket
var authorizationRequest = {};
authorizationRequest.ticket = ticket;
// send the authorization request, if successful retry the request
Identity.authorization.authorize(authorizationRequest).then(function (rpt) {
// onGrant
}, function () {
// onDeny
}, function () {
// onError
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
9.5.2. Obtaining entitlements
The
library provides an keycloak-authz.js
entitlement
function that you can use to obtain an RPT from the server by providing the resources and scopes your client wants to access.
Example about how to obtain an RPT with permissions for all resources and scopes the user can access
authorization.entitlement('my-resource-server-id').then(function (rpt) {
// onGrant callback function.
// If authorization was successful you'll receive an RPT
// with the necessary permissions to access the resource server
});
Example about how to obtain an RPT with permissions for specific resources and scopes
authorization.entitlement('my-resource-server', {
"permissions": [
{
"id" : "Some Resource"
}
]
}).then(function (rpt) {
// onGrant
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
9.5.3. Authorization request
Both
and authorize
functions accept an authorization request object. This object can be set with the following properties:
entitlement
permissions
An array of objects representing the resource and scopes. For instance:
var authorizationRequest = { "permissions": [ { "id" : "Some Resource", "scopes" : ["view", "edit"] } ] }
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
9.5.4. Obtaining the RPT
If you have already obtained an RPT using any of the authorization functions provided by the library, you can always obtain the RPT as follows from the authorization object (assuming that it has been initialized by one of the techniques shown earlier):
var rpt = authorization.rpt;
9.6. Configuring TLS/HTTPS
When the server is using HTTPS, ensure your adapter is configured as follows:
keycloak.json
{
"truststore": "path_to_your_trust_store",
"truststore-password": "trust_store_password"
}
The configuration above enables TLS/HTTPS to the Authorization Client, making possible to access a Red Hat Single Sign-On Server remotely using the HTTPS scheme.
It is strongly recommended that you enable TLS/HTTPS when accessing the Red Hat Single Sign-On Server endpoints.
