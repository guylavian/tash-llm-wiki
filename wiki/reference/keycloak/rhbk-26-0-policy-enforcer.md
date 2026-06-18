---
title: "Chapter 15. Red Hat build of Keycloak policy enforcer - Red Hat build of Keycloak 26.0 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-policy-enforcer
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/securing_applications_and_services_guide/policy-enforcer-
guide: securing_applications_and_services_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 15. Red Hat build of Keycloak policy enforcer - Red Hat build of Keycloak 26.0 Securing Applications and Services Guide

Chapter 15. Red Hat build of Keycloak policy enforcer
Policy Enforcement Point (PEP) is a design pattern and as such you can implement it in different ways. Red Hat build of Keycloak provides all the necessary means to implement PEPs for different platforms, environments, and programming languages. Red Hat build of Keycloak Authorization Services presents a RESTful API, and leverages OAuth2 authorization capabilities for fine-grained authorization using a centralized authorization server.
A PEP is responsible for enforcing access decisions from the Red Hat build of Keycloak server where these decisions are taken by evaluating the policies associated with a protected resource. It acts as a filter or interceptor in your application in order to check whether or not a particular request to a protected resource can be fulfilled based on the permissions granted by these decisions.
Red Hat build of Keycloak provides built-in support for enabling the Red Hat build of Keycloak Policy Enforcer to Java applications with built-in support to secure JakartaEE-compliant frameworks and web containers. If you are using Maven, you should configure the following dependency to your project:
<dependency>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-policy-enforcer</artifactId>
<version>999.0.0-SNAPSHOT</version>
</dependency>
When you enable the policy enforcer all requests sent to your application are intercepted and access to protected resources will be granted depending on the permissions granted by Red Hat build of Keycloak to the identity making the request.
Policy enforcement is strongly linked to your application’s paths and the resources you created for a resource server using the Red Hat build of Keycloak Administration Console. By default, when you create a resource server, Red Hat build of Keycloak creates a default configuration for your resource server so you can enable policy enforcement quickly.
15.1. Configuration
The policy enforcer configuration uses a JSON format and most of the time you don’t need to set anything if you want to automatically resolve the protected paths based on the resources available from your resource server.
If you want to manually define the resources being protected, you can use a slightly more verbose format:
{
"enforcement-mode" : "ENFORCING",
"paths": [
{
"path" : "/users/*",
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
}
]
}
The following is a description of each configuration option:
enforcement-mode
Specifies how policies are enforced.
ENFORCING
(default mode) Requests are denied by default even when no policy is associated with a given resource.
PERMISSIVE
Requests are allowed even when no policy is associated with a given resource.
DISABLED
Completely disables the evaluation of policies and allows access to any resource. When
enforcement-mode
isDISABLED
, applications are still able to obtain all permissions granted by Red Hat build of Keycloak through the Authorization Context
on-deny-redirect-to
Defines a URL where a client request is redirected when an "access denied" message is obtained from the server. By default, the adapter responds with a 403 HTTP status code.
path-cache
Defines how the policy enforcer should track associations between paths in your application and resources defined in Red Hat build of Keycloak. The cache is needed to avoid unnecessary requests to a Red Hat build of Keycloak server by caching associations between paths and protected resources.
lifespan
Defines the time in milliseconds when the entry should be expired. If not provided, default value is 30000. A value equal to 0 can be set to completely disable the cache. A value equal to -1 can be set to disable the expiry of the cache.
max-entries
Defines the limit of entries that should be kept in the cache. If not provided, default value is 1000.
paths
Specifies the paths to protect. This configuration is optional. If not defined, the policy enforcer discovers all paths by fetching the resources you defined to your application in Red Hat build of Keycloak, where these resources are defined with
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
Defines a set of one or more claims that must be resolved and pushed to the Red Hat build of Keycloak server in order to make these claims available to policies. See Claim Information Point for more details.
lazy-load-paths
Specifies how the adapter should fetch the server for resources associated with paths in your application. If true, the policy enforcer is going to fetch resources on-demand accordingly with the path being requested. This configuration is specially useful when you do not want to fetch all resources from the server during deployment (in case you have provided no
paths
) or in case you have defined only a sub set ofpaths
and want to fetch others on-demand.http-method-as-scope
Specifies how scopes should be mapped to HTTP methods. If set to true, the policy enforcer will use the HTTP method from the current request to check whether or not access should be granted. When enabled, make sure your resources in Red Hat build of Keycloak are associated with scopes representing each HTTP method you are protecting.
claim-information-point
Defines a set of one or more global claims that must be resolved and pushed to the Red Hat build of Keycloak server in order to make these claims available to policies. See Claim Information Point for more details.
15.2. Claim Information Point
A Claim Information Point (CIP) is responsible for resolving claims and pushing these claims to the Red Hat build of Keycloak server in order to provide more information about the access context to policies. They can be defined as a configuration option to the policy-enforcer in order to resolve claims from different sources, such as:
- HTTP Request (parameters, headers, body, etc)
- External HTTP Service
- Static values defined in configuration
- Any other source by implementing the Claim Information Provider SPI
When pushing claims to the Red Hat build of Keycloak server, policies can base decisions not only on who a user is but also by taking context and contents into account, based on who, what, why, when, where, and which for a given transaction. It is all about Contextual-based Authorization and how to use runtime information in order to support fine-grained authorization decisions.
15.2.1. Obtaining information from the HTTP request
Here are several examples showing how you can extract claims from an HTTP request:
keycloak.json
{
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
"param-replace-multiple-placeholder": "Test {keycloak.access_token['/custom_claim/0']} and {request.parameter['a']}"
}
}
}
]
}
15.2.2. Obtaining information from an external HTTP service
Here are several examples showing how you can extract claims from an external HTTP Service:
keycloak.json
{
"paths": [
{
"path": "/protected/resource",
"claim-information-point": {
"http": {
"claims": {
"claim-a": "/a",
"claim-d": "/d",
"claim-d0": "/d/0",
"claim-d-all": [
"/d/0",
"/d/1"
]
},
"url": "http://mycompany/claim-provider",
"method": "POST",
"headers": {
"Content-Type": "application/x-www-form-urlencoded",
"header-b": [
"header-b-value1",
"header-b-value2"
],
"Authorization": "Bearer {keycloak.access_token}"
},
"parameters": {
"param-a": [
"param-a-value1",
"param-a-value2"
],
"param-subject": "{keycloak.access_token['/sub']}",
"param-user-name": "{keycloak.access_token['/preferred_username']}",
"param-other-claims": "{keycloak.access_token['/custom_claim']}"
}
}
}
}
]
}
15.2.3. Static claims
keycloak.json
{
"paths": [
{
"path": "/protected/resource",
"claim-information-point": {
"claims": {
"claim-from-static-value": "static value",
"claim-from-multiple-static-value": ["static", "value"]
}
}
}
]
}
15.2.4. Claim information provider SPI
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
public MyClaimInformationPointProvider(Map<String, Object> config) {
this.config = config;
}
@Override
public Map<String, List<String>> resolve(HttpFacade httpFacade) {
Map<String, List<String>> claims = new HashMap<>();
// put whatever claim you want into the map
return claims;
}
}
15.3. Obtaining the authorization context
When policy enforcement is enabled, the permissions obtained from the server are available through org.keycloak.AuthorizationContext
. This class provides several methods you can use to obtain permissions and ascertain whether a permission was granted for a particular resource or scope.
Obtaining the Authorization Context in a Servlet Container
HttpServletRequest request = // obtain javax.servlet.http.HttpServletRequest
AuthorizationContext authzContext = (AuthorizationContext) request.getAttribute(AuthorizationContext.class.getName());
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
represents one of the main capabilities of Red Hat build of Keycloak Authorization Services. From the examples above, you can see that the protected resource is not directly associated with the policies that govern them.
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
Although both examples address the same requirements, they do so in different ways. In RBAC, roles only implicitly define access for their resources. With Red Hat build of Keycloak, you gain the capability to create more manageable code that focuses directly on your resources whether you are using RBAC, attribute-based access control (ABAC), or any other BAC variant. Either you have the permission for a given resource or scope, or you do not have that permission.
Now, suppose your security requirements have changed and in addition to project managers, PMOs can also create new projects.
Security requirements change, but with Red Hat build of Keycloak there is no need to change your application code to address the new requirements. Once your application is based on the resource and scope identifier, you need only change the configuration of the permissions or policies associated with a particular resource in the authorization server. In this case, the permissions and policies associated with the Project Resource
and/or the scope urn:project.com:project:create
would be changed.
15.4. Using the AuthorizationContext to obtain an Authorization Client Instance
The
can also be used to obtain a reference to the Red Hat build of Keycloak authorization client configured to your application:
AuthorizationContext
ClientAuthorizationContext clientContext = ClientAuthorizationContext.class.cast(authzContext);
AuthzClient authzClient = clientContext.getClient();
In some cases, resource servers protected by the policy enforcer need to access the APIs provided by the authorization server. With an AuthzClient
instance in hands, resource servers can interact with the server in order to create resources or check for specific permissions programmatically.
15.5. Configuring TLS/HTTPS
When the server is using HTTPS, ensure your policy enforcer is configured as follows:
{
"truststore": "path_to_your_trust_store",
"truststore-password": "trust_store_password"
}
The configuration above enables TLS/HTTPS to the Authorization Client, making possible to access a Red Hat build of Keycloak Server remotely using the HTTPS scheme.
It is strongly recommended that you enable TLS/HTTPS when accessing the Red Hat build of Keycloak Server endpoints.
