---
title: "Chapter 8. Authorization Services - Red Hat Single Sign-On 7.2 Authorization Services Guide"
type: reference
domain: keycloak
slug: rhsso-7-2-service-overview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.2/html/authorization_services_guide/service_overview
guide: authorization_services_guide
version: 7.2
family: rhsso
documentKind: "Documentation"
abstract: "Red Hat Single Sign-On Authorization Services are based on OAuth2’s User-Managed Access (UMA) Profile. This section describes the different RESTful endpoints that you can interact with to enable fine-grained authorization for your applications and services. 8.1. Protection API The Protection API provides a UMA-compliant set of endpoints providing: Resource Registration With this endpoint, resource…"
---

# Chapter 8. Authorization Services - Red Hat Single Sign-On 7.2 Authorization Services Guide

Chapter 8. Authorization Services
Red Hat Single Sign-On Authorization Services are based on OAuth2’s User-Managed Access (UMA) Profile.
This section describes the different RESTful endpoints that you can interact with to enable fine-grained authorization for your applications and services.
8.1. Protection API
The Protection API provides a UMA-compliant set of endpoints providing:
Resource Registration
With this endpoint, resource servers can manage their resources remotely and enable policy enforcers to query the server for the resources that need protection.
Permission Registration
In the UMA protocol, resource servers access this endpoint, which issues permission tickets.
An important requirement for this API is that only resource servers are allowed to access its endpoints using a special OAuth2 access token called a protection API token (PAT). In UMA, a PAT is a token with the scope uma_protection.
8.1.1. What is a PAT and How to Obtain It
A protection API token (PAT) is a special OAuth2 access token with a scope defined as uma_protection. When you create a resource server, Red Hat Single Sign-On automatically creates a role, uma_protection, for the corresponding client application and associates it with the client’s service account.
Service Account granted with uma_protection role
Resource servers can obtain a PAT from Red Hat Single Sign-On like any other OAuth2 access token. For example, using curl:
curl -X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
-d 'grant_type=client_credentials&client_id=${client_id}&client_secret=${client_secret}' \
"http://localhost:8080/auth/realms/${realm_name}/protocol/openid-connect/token"
The example above is using the client_credentials grant type to obtain a PAT from the server. As a result, the server returns a response similar to the following:
{
"access_token": ${PAT},
"expires_in": 300,
"refresh_expires_in": 1800,
"refresh_token": ${refresh_token},
"token_type": "bearer",
"id_token": ${id_token},
"not-before-policy": 0,
"session_state": "ccea4a55-9aec-4024-b11c-44f6f168439e"
}
Red Hat Single Sign-On can authenticate your client application in different ways. For simplicity, the client_credentials grant type is used here, which requires a client_id and a client_secret. You can choose to use any supported authentication method.
8.1.2. Managing Resources
Resource servers can manage their resources remotely using a UMA-compliant endpoint.
http://${host}:${port}/auth/realms/${realm_name}/authz/protection/resource_set
This endpoint provides registration operations outlined as follows (entire path omitted for clarity):
- Create resource set description: POST /resource_set
- Read resource set description: GET /resource_set/{_id}
- Update resource set description: PUT /resource_set/{_id}
- Delete resource set description: DELETE /resource_set/{_id}
- List resource set descriptions: GET /resource_set
- List resource set descriptions using a filter: GET /resource_set?filter=${filter}
For more information about the contract for each of these operations, see UMA Resource Set Registration.
8.1.3. Managing Permission Requests
Resource servers using the UMA protocol can use a specific endpoint to manage permission requests. This endpoint provides a UMA-compliant flow for registering permission requests and obtaining a permission ticket.
http://${host}:${port}/auth/realms/${realm_name}/authz/protection/permission
A permission ticket is a special security token type representing a permission request. Per the UMA specification, a permission ticket is:
A correlation handle that is conveyed from an authorization server to a resource server, from a resource server to a client, and ultimately from a client back to an authorization server, to enable the authorization server to assess the correct policies to apply to a request for authorization data.
Permission ticket support is limited. In the full UMA protocol, resource servers can register permission requests in the server to support authorization flows where a resource owner (the user that owns a resource being requested) can approve access to his resources by third parties, among other ways. This represents one of the main features of the UMA specification: resource owners can control their own resources and the policies that govern them. Currently Red Hat Single Sign-On UMA implementation support is very limited in this regard. For example, the system does not store permission tickets on the server and we are essentially using UMA to provide API security and base our authorization offerings. In the future, full support of UMA and other use cases is planned.
In most cases, you won’t need to deal with this endpoint directly. Red Hat Single Sign-On provides a policy enforcer that enables UMA for your resource server so it can obtain a permission ticket from the authorization server, return this ticket to client application, and enforce authorization decisions based on a final requesting party token (RPT).
The process of obtaining permission tickets from Red Hat Single Sign-On is performed by resource servers and not regular client applications, where permission tickets are obtained when a client tries to access a protected resource without the necessary grants to access the resource. The issuance of permission tickets is an important aspects when using UMA as it allows resource servers to:
- Abstract from clients the data associated with the resources protected by the resource server
- Register in the Red Hat Single Sign-On authorization requests which in turn can be used later in workflows to grant access based on the resource’s owner consent
- Decouple resource servers from authorization servers and allow them to protect and manage their resources using different authorization servers
Client wise, a permission ticket has also important aspects that its worthy to highlight:
- Clients don’t need to know about how authorization data is associated with protected resources. A permission ticket is completely opaque to clients.
- Clients can have access to resources on different resource servers and protected by different authorization servers
These are just some of the benefits brought by UMA where other aspects of UMA are strongly based on permission tickets, specially regarding privacy and user controlled access to their resources.
8.2. Authorization API
The Authorization API provides a UMA-compliant endpoint for obtaining authorization data from the server, where the authorization data represents the result of the evaluation of all permissions and authorization policies associated with the resources being requested.
Unlike the Protection API, any client application can access the Authorization API endpoint, which requires a special OAuth2 access token called an authorization API token (AAT). In UMA, an AAT is a token with the scope uma_authorization.
8.2.1. What is an AAT and How to Obtain It
An authorization API token (AAT) is a special OAuth2 access token with the scope uma_authorization. When you create a user, Red Hat Single Sign-On automatically assigns the role uma_authorization to the user. The uma_authorization role is a default realm role.
Default Role uma_authorization
An AAT enables a client application to query the server for user permissions.
Client applications can obtain an AAT from Red Hat Single Sign-On like any other OAuth2 access token. Usually, client applications obtain AATs after the user is successfully authenticated in Red Hat Single Sign-On. By default, the authorization_code grant type is used to authenticate users, and the server will issue an OAuth2 access token to the client application acting on their behalf.
The example below uses the Resource Owner Password Credentials Grant Type to request an AAT:
curl -X POST \
-H "Authorization: Basic aGVsbG8td29ybGQtYXV0aHotc2VydmljZTpwYXNzd29yZA==" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d 'username=${username}&password=${user_password}&grant_type=password' \
"http://localhost:8080/auth/realms/${realm_name}/protocol/openid-connect/token"
As a result, the server response is:
{
"access_token": ${AAT},
"expires_in": 300,
"refresh_expires_in": 1800,
"refresh_token": ${refresh_token},
"token_type": "bearer",
"id_token": ${id_token},
"not-before-policy": 0,
"session_state": "3cad2afc-855b-47b7-8e4d-a21c66e312fb"
}
8.2.2. Requesting Authorization Data and Token
Client applications using the UMA protocol can use a specific endpoint to obtain a special security token called a Requesting Party Token (RPT). This token consists of all the permissions granted to a user as a result of the evaluation of the permissions and authorization policies associated with the resources being requested. With an RPT, client applications can gain access to protected resources at the resource server.
UMA compliant Authorization API Endpoint
http://${host}:${port}/auth/realms/${realm_name}/authz/authorize
When requesting an RPT, you need to provide two things:
- A permission ticket representing the resources you want to access
- The Authorization API token (AAT) (as a bearer token) representing a user’s identity and his consent to access authorization data on his behalf.
The permission ticket is added to an HTTP request as a parameter whether the AAT is included in a
header in order to authenticate the request using the AAT as a bearer token.
Authorization
curl -X POST
-H "Authorization: Bearer ${AAT}" -d '{
"ticket" : ${PERMISSION_TICKET}
}' "http://localhost:8080/auth/realms/hello-world-authz/authz/authorize"
As a result, the server response is:
{"rpt":"${RPT}"}
8.3. Entitlement API
The Entitlement API provides a 1-legged protocol for obtaining authorization data from the server, where the authorization data represents the result of the evaluation of all permissions and authorization policies associated with the resources being requested.
Unlike the Authorization API, the Entitlement API is not UMA-compliant and does not require permission tickets.
The purpose of this API is provide a more lightweight API for obtaining authorization data, where a client in possession of a valid OAuth2 access token is able to obtain the necessary authorization data on behalf of its users.
8.3.1. Requesting Entitlements
Client applications can use a specific endpoint to obtain a special security token called a Requesting Party Token (RPT). This token consists of all the entitlements (or permissions) for a user as a result of the evaluation of the permissions and authorization policies associated with the resources being requested. With an RPT, client applications can gain access to protected resources at the resource server.
Entitlement API Endpoint
http://${host}:${port}/auth/realms/${realm_name}/authz/entitlement/{client_id}
The client_id parameter above must be provided in order to identify the client application acting as a resource server in Red Hat Single Sign-On. You must provide the client identifier in order to restrict the scope of the evaluation to the resources, scopes and permissions managed by a specific resource server.
The Entitlement API comes in two flavors:
- Using HTTP GET in order to obtain all entitlements based on the resources owned by a specific user or/and general resources owned and managed by the resource server itself.
- Using HTTP POST in order to obtain entitlements based on a set of one or more resources and scopes sent along with an entitlement request.
Using one or another depends on your use case and how much resources you have registered in Red Hat Single Sign-On. Although the GET variant provides an easy way to obtain entitlements from the server, it might not be appropriate in case you have too much resources associated with an user. In this case, the POST method is recommended.
Regardless of the HTTP method you decide to use, the Entitlement API endpoint expects an access token in the request representing a user’s identity and his consent to access authorization data on his behalf. The access token must be sent as a bearer token using an HTTP
header.
Authorization
After successfully invoking the Entitlement API endpoint, you will get a RPT with all permissions granted by the server.
8.3.1.1. Obtaining Entitlements
The easiest way to obtain entitlements for a specific user is using an HTTP GET request. For example, using curl:
curl -X GET \
-H "Authorization: Bearer ${access_token}" \
"http://${host}:${port}/auth/realms/${realm_name}/authz/entitlement/{client_id}"
As a result, the server response is:
{
"rpt": ${RPT}
}
Using this method to obtain entitlements, the server responds to the requesting client with all entitlements for a user, based on the evaluation of the permissions and authorization policies associated with the resources owned by the user or the resource server itself. For instance, suppose you have permissions defined in Red Hat Single Sign-On for the following resources:
- Main Page
- Alice Bank Account
- Bob Bank Account
Main Page is a common resource in your application and owned by the resource server itself, it represents a landing or main page in your application. On the other hand, Alice Bank Account is a resource where user alice is the owner. The same goes for Bob Bank Account which is owned by a different user, bob.
When obtaining entitlements for user alice, the server is going to evaluate all permissions associated with resources Main Page and Alice Bank Account. Giving you back a RPT (if permissions were actually granted) with a set of permissions representing these resources.
8.3.1.2. Obtaining Entitlements for a Specific Set of Resources
You can also use the entitlements endpoint to obtain a user’s entitlements for a set of one or more resources. For example, using curl:
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ${access_token}" -d '{
"permissions" : [
{
"resource_set_name" : "Alice Bank Account"
}
]
}' "http://${host}:${port}/auth/realms/${realm_name}/authz/entitlement/{client_id}"
As a result, the server response is:
{
"rpt": ${RPT}
}
Unlike the GET version, the server responds with an RPT holding the permissions granted during the evaluation of the permissions and authorization policies associated with the resources being requested.
You can also specify the scopes you want to access. For example, using curl:
curl -X POST -H "Authorization: Bearer ${access_token}" -d '{
"permissions" : [
{
"resource_set_name" : "Alice Bank Account",
"scopes" : [
"withdraw"
]
}
]
}' "http://${host}:${port}/auth/realms/${realm_name}/authz/entitlement/{client_id}"
8.3.2. Entitlement Request Metadata
When requesting entitlements client applications are allowed to associate metadata information to the request and define how they expect to obtain the permissions.
curl -X POST -H "Authorization: Bearer ${access_token}" -d '{
"metadata" : {
"include_resource_name" : false
},
"permissions" : [
...
]
}' "http://${host}:${port}/auth/realms/${realm_name}/authz/entitlement/{client_id}"
The Entitlement API endpoint only allows passing metadata along an entitlement request when using HTTP POST.
The following sections will explain how and when you can use the different information you can include in an entitlement request as a metadata.
8.3.3. Decide whether or not resource’s name should be included the response
include_resource_name
curl -X POST -H "Authorization: Bearer ${access_token}" -d '{
"metadata" : {
"include_resource_name" : false
},
"permissions" : [
...
]
}' "http://${host}:${port}/auth/realms/${realm_name}/authz/entitlement/{client_id}"
Clients can use
to decide whether or not resource`s name should be included on each permission granted by the server. This option can be used to reduce the size of RPTs and optimize client-server communication.
include_resource_name
By default, permissions in a RPT contain both the id and name of the resource that was granted by every single permission. This option is specially useful when the resource server is capable of map their resources only based on the resource`s id.
8.3.4. Limiting the number of permissions within a RPT
limit
curl -X POST -H "Authorization: Bearer ${access_token}" -d '{
"metadata" : {
"limit" : 10
},
"permissions" : [
...
]
}' "http://${host}:${port}/auth/realms/${realm_name}/authz/entitlement/{client_id}"
Clients can use
to specify how many permissions they expected within a RPT returned by the server. The limit option works as follows:
limit
-
If a request is sent without a previously issued RPT, only
permissions will be returned based on the resources/scopes from thelimit
claim.permissions
-
If a request is sent with a previously issued RPT, the permissions associated with the resources/scopes from the
claim take precedence where the permissions from the previously issued RPT are only included ifpermissions
is not reached. In case there is enough room for permissions from a previously issued RPT, the server will include the first permissions defined there.limit
This option allows clients to control the size of RPTs and keep only last permissions granted by the server. It usually makes sense only in cases your client is capable of sending previously issued RPTs while asking for new permissions (a.k.a.: incremental authorization).
8.4. Requesting Party Token
A requesting party token (RPT) is a JSON web token (JWT) digitally signed using JSON web signature (JWS). The token is built based on the OAuth2 access token previously issued by Red Hat Single Sign-On to a specific client acting on behalf of an user or on its own behalf.
When you decode an RPT, you see a payload similar to the following:
{
"authorization": {
"permissions": [
{
"resource_set_id": "d2fe9843-6462-4bfc-baba-b5787bb6e0e7",
"resource_set_name": "Hello World Resource"
}
]
},
"jti": "d6109a09-78fd-4998-bf89-95730dfd0892-1464906679405",
"exp": 1464906971,
"nbf": 0,
"iat": 1464906671,
"sub": "f1888f4d-5172-4359-be0c-af338505d86c",
"typ": "kc_ett",
"azp": "hello-world-authz-service"
}
From this token you can obtain all permissions granted by the server from the permissions claim.
Also note that permissions are directly related with the resources/scopes you are protecting and complete decoupled from the access control methods that were used to actually grant and issue these same permissions.
8.4.1. Introspecting a Requesting Party Token
Sometimes you might want to introspect a requesting party token (RPT) to check its validity or obtain the permissions within the token to enforce authorization decisions on the resource server side.
There are two main use cases where token introspection can help you:
- When client applications need to query the token validity to obtain a new one with the same or additional permissions
- When enforcing authorization decisions at the resource server side, especially when none of the built-in policy enforcers fits your application
8.4.2. Obtaining Information about an RPT
The token introspection is essentially a OAuth2 token introspection-compliant endpoint from which you can obtain information about an RPT.
http://${host}:${port}/auth/realms/${realm_name}/protocol/openid-connect/token/introspect
To introspect an RPT using this endpoint, you can send a request to the server as follows:
curl -X POST \
-H "Authorization: Basic aGVsbG8td29ybGQtYXV0aHotc2VydmljZTpzZWNyZXQ=" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d 'token_type_hint=requesting_party_token&token=${RPT}' \
"http://localhost:8080/auth/realms/hello-world-authz/protocol/openid-connect/token/introspect"
The request above is using HTTP BASIC and passing the client’s credentials (client ID and secret) to authenticate the client attempting to introspect the token, but you can use any other client authentication method supported by Red Hat Single Sign-On.
The introspection endpoint expects two parameters:
token_type_hint
Use requesting_party_token as the value for this parameter, which indicates that you want to introspect an RPT.
token
Use the token string as it was returned by the server during the authorization process as the value for this parameter.
As a result, the server response is:
{
"permissions": [
{
"resource_set_id": "90ccc6fc-b296-4cd1-881e-089e1ee15957",
"resource_set_name": "Hello World Resource"
}
],
"exp": 1465314139,
"nbf": 0,
"iat": 1465313839,
"aud": "hello-world-authz-service",
"active": true
}
If the RPT is not active, this response is returned instead:
{
"active": false
}
8.4.3. Do I Need to Invoke the Server Every Time I Want to Introspect an RPT?
No. Both Entitlement APIs use the JSON web token (JWT) specification as the default format for RPTs.
If you want to validate these tokens without a call to the remote introspection endpoint, you can decode the RPT and query for its validity locally. Once you decode the token, you can also use the permissions within the token to enforce authorization decisions.
This is essentially what the policy enforcers do. Be sure to:
- Validate the signature of the RPT (based on the realm’s public key)
- Query for token validity based on its exp, iat, and aud claims
8.5. Authorization Client Java API
Depending on your requirements, a resource server should be able to manage resources remotely or even check for permissions programmatically. If you are using Java, you can access the Red Hat Single Sign-On Authorization Services using the Authorization Client API.
It is targeted for resource servers that want to access the different APIs provided by the server such as the Protection, Authorization and Entitlement APIs.
8.5.1. Maven Dependency
<dependencies>
<dependency>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-authz-client</artifactId>
<version>${KEYCLOAK_VERSION}</version>
</dependency>
</dependencies>
8.5.2. Configuration
The client configuration is defined in a keycloak.json
file as follows:
{
"realm": "hello-world-authz",
"auth-server-url" : "http://localhost:8080/auth",
"resource" : "hello-world-authz-service",
"credentials": {
"secret": "secret"
}
}
realm (required)
The name of the realm.
auth-server-url (required)
The base URL of the Red Hat Single Sign-On server. All other Red Hat Single Sign-On pages and REST service endpoints are derived from this. It is usually in the form https://host:port/auth.
resource (required)
The client-id of the application. Each application has a client-id that is used to identify the application.
credentials (required)
Specifies the credentials of the application. This is an object notation where the key is the credential type and the value is the value of the credential type.
The configuration file is usually located in your application’s classpath, the default location from where the client is going to try to find a
file.
keycloak.json
8.5.3. Creating the Authorization Client
Considering you have a
file in your classpath, you can create a new keycloak.json
instance as follows:
AuthzClient
// create a new instance based on the configuration defined in a keycloak.json located in your classpath
AuthzClient authzClient = AuthzClient.create();
8.5.4. Obtaining User Entitlements
Here is an example illustrating how to obtain user entitlements:
// create a new instance based on the configuration defined in keycloak-authz.json
AuthzClient authzClient = AuthzClient.create();
// obtain an Entitlement API Token to get access to the Entitlement API.
// this token is an access token issued to a client on behalf of an user
// with a uma_authorization scope
String eat = getEntitlementAPIToken(authzClient);
// send the entitlement request to the server to
// obtain an RPT with all permissions granted to the user
EntitlementResponse response = authzClient.entitlement(eat).getAll("hello-world-authz-service");
String rpt = response.getRpt();
// now you can use the RPT to access protected resources on the resource server
Here is an example illustrating how to obtain user entitlements for a set of one or more resources:
// create a new instance based on the configuration defined in keycloak-authz.json
AuthzClient authzClient = AuthzClient.create();
// obtain an Entitlement API Token to get access to the Entitlement API.
// this token is an access token issued to a client on behalf of an user
// with a uma_authorization scope
String eat = getEntitlementAPIToken(authzClient);
// create an entitlement request
EntitlementRequest request = new EntitlementRequest();
PermissionRequest permission = new PermissionRequest();
permission.setResourceSetName("Hello World Resource");
request.addPermission(permission);
// send the entitlement request to the server to obtain an RPT
// with all permissions granted to the user
EntitlementResponse response = authzClient.entitlement(eat).get("hello-world-authz-service", request);
String rpt = response.getRpt();
// now you can use the RPT to access protected resources on the resource server
8.5.5. Creating a Resource Using the Protection API
// create a new instance based on the configuration defined in keycloak-authz.json
AuthzClient authzClient = AuthzClient.create();
// create a new resource representation with the information we want
ResourceRepresentation newResource = new ResourceRepresentation();
newResource.setName("New Resource");
newResource.setType("urn:hello-world-authz:resources:example");
newResource.addScope(new ScopeRepresentation("urn:hello-world-authz:scopes:view"));
ProtectedResource resourceClient = authzClient.protection().resource();
Set<String> existingResource = resourceClient.findByFilter("name=" + newResource.getName());
if (!existingResource.isEmpty()) {
resourceClient.delete(existingResource.iterator().next());
}
// create the resource on the server
RegistrationResponse response = resourceClient.create(newResource);
String resourceId = response.getId();
// query the resource using its newly generated id
ResourceRepresentation resource = resourceClient.findById(resourceId).getResourceDescription();
8.5.6. Introspecting a RPT
AuthzClient authzClient = AuthzClient.create();
String rpt = getRequestingPartyToken(authzClient);
TokenIntrospectionResponse requestingPartyToken = authzClient.protection().introspectRequestingPartyToken(rpt);
if (requestingPartyToken.getActive()) {
for (Permission granted : requestingPartyToken.getPermissions()) {
// iterate over the granted permissions
}
}
