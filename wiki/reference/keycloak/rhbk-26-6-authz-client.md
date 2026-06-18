---
title: "Chapter 19. Red Hat build of Keycloak authorization client - Red Hat build of Keycloak 26.6 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-authz-client
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/securing_applications_and_services_guide/authz-client-
guide: securing_applications_and_services_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 19. Red Hat build of Keycloak authorization client - Red Hat build of Keycloak 26.6 Securing Applications and Services Guide

Chapter 19. Red Hat build of Keycloak authorization client
Using the Red Hat build of Keycloak authz client administer and check permissions.
Depending on your requirements, a resource server should be able to manage resources remotely or even check for permissions programmatically. If you are using Java, you can access the Red Hat build of Keycloak Authorization Services using the Authorization Client API.
It is targeted for resource servers that want to access the different endpoints provided by the server such as the Token Endpoint, Resource, and Permission management endpoints.
19.1. Maven dependency
<dependencies>
<dependency>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-authz-client</artifactId>
<version>999.0.0-SNAPSHOT</version>
</dependency>
</dependencies>
19.2. Configuration
The client configuration is defined in a keycloak.json
file as follows:
{
"realm": "hello-world-authz",
"auth-server-url" : "http://localhost:8080",
"resource" : "hello-world-authz-service",
"credentials": {
"secret": "secret"
}
}
realm (required)
The name of the realm.
auth-server-url (required)
The base URL of the Red Hat build of Keycloak server. All other Red Hat build of Keycloak pages and REST service endpoints are derived from this. It is usually in the form https://host:port.
resource (required)
The client-id of the application. Each application has a client-id that is used to identify the application.
credentials (required)
Specifies the credentials of the application. This is an object notation where the key is the credential type and the value is the value of the credential type. The details are in the dedicated section.
The configuration file is usually located in your application’s classpath, the default location from where the client is going to try to find a
file.
keycloak.json
19.3. Creating the authorization client
Considering you have a
file in your classpath, you can create a new keycloak.json
instance as follows:
AuthzClient
// create a new instance based on the configuration defined in a keycloak.json located in your classpath
AuthzClient authzClient = AuthzClient.create();
19.4. Obtaining user entitlements
Here is an example illustrating how to obtain user entitlements:
// create a new instance based on the configuration defined in keycloak.json
AuthzClient authzClient = AuthzClient.create();
// create an authorization request
AuthorizationRequest request = new AuthorizationRequest();
// send the entitlement request to the server in order to
// obtain an RPT with all permissions granted to the user
AuthorizationResponse response = authzClient.authorization("alice", "alice").authorize(request);
String rpt = response.getToken();
System.out.println("You got an RPT: " + rpt);
// now you can use the RPT to access protected resources on the resource server
Here is an example illustrating how to obtain user entitlements for a set of one or more resources:
// create a new instance based on the configuration defined in keycloak.json
AuthzClient authzClient = AuthzClient.create();
// create an authorization request
AuthorizationRequest request = new AuthorizationRequest();
// add permissions to the request based on the resources and scopes you want to check access
request.addPermission("Default Resource");
// send the entitlement request to the server in order to
// obtain an RPT with permissions for a single resource
AuthorizationResponse response = authzClient.authorization("alice", "alice").authorize(request);
String rpt = response.getToken();
System.out.println("You got an RPT: " + rpt);
// now you can use the RPT to access protected resources on the resource server
19.5. Creating a resource using the protection API
// create a new instance based on the configuration defined in keycloak.json
AuthzClient authzClient = AuthzClient.create();
// create a new resource representation with the information we want
ResourceRepresentation newResource = new ResourceRepresentation();
newResource.setName("New Resource");
newResource.setType("urn:hello-world-authz:resources:example");
newResource.addScope(new ScopeRepresentation("urn:hello-world-authz:scopes:view"));
ProtectedResource resourceClient = authzClient.protection().resource();
ResourceRepresentation existingResource = resourceClient.findByName(newResource.getName());
if (existingResource != null) {
resourceClient.delete(existingResource.getId());
}
// create the resource on the server
ResourceRepresentation response = resourceClient.create(newResource);
String resourceId = response.getId();
// query the resource using its newly generated id
ResourceRepresentation resource = resourceClient.findById(resourceId);
System.out.println(resource);
19.6. Introspecting an RPT
// create a new instance based on the configuration defined in keycloak.json
AuthzClient authzClient = AuthzClient.create();
// send the authorization request to the server in order to
// obtain an RPT with all permissions granted to the user
AuthorizationResponse response = authzClient.authorization("alice", "alice").authorize();
String rpt = response.getToken();
// introspect the token
TokenIntrospectionResponse requestingPartyToken = authzClient.protection().introspectRequestingPartyToken(rpt);
System.out.println("Token status is: " + requestingPartyToken.getActive());
System.out.println("Permissions granted by the server: ");
for (Permission granted : requestingPartyToken.getPermissions()) {
System.out.println(granted);
}
19.7. Client authentication
When an authorization client needs to send a backchannel request, it needs to authenticate against the Red Hat build of Keycloak server. By default, there are three ways to authenticate the client: client ID and client secret, client authentication with signed JWT, or client authentication with signed JWT using client secret.
19.7.1. Client ID and Client Secret
This is the traditional method described in the OAuth2 specification. The client has a secret, which needs to be known to both the client and the Red Hat build of Keycloak server. You can generate the secret for a particular client in the Red Hat build of Keycloak Admin Console, and then paste this secret into the keycloak.json
file on the application side:
"credentials": {
"secret": "19666a4f-32dd-4049-b082-684c74115f28"
}
19.7.2. Client authentication with Signed JWT
This is based on the RFC7523 specification. It works this way:
-
The client must have the private key and certificate. For authorization client, this is available through the traditional
keystore
file, which is either available on the client application’s classpath or somewhere on the file system. -
During authentication, the client generates a JWT token and signs it with its private key and sends it to Red Hat build of Keycloak in the particular request in the
client_assertion
parameter. Red Hat build of Keycloak must have the public key or certificate of the client so that it can verify the signature on JWT. In Red Hat build of Keycloak, you configure client credentials for your client. First, you choose
Signed JWT
as the method of authenticating your client in the tabCredentials
in the Admin Console. Then you can choose one of these methods in theKeys
tab:-
Configure the JWKS URL where Red Hat build of Keycloak can download the client’s public keys. This option is the most flexible, since the client can rotate its keys anytime and Red Hat build of Keycloak always downloads new keys as needed without changing the configuration. In other words, Red Hat build of Keycloak downloads new keys when it sees the token signed by an unknown
kid
(Key ID). However, you will need to care of exposing the public key somewhere in JWKS format to be available to the server. - Upload the client’s public key or certificate, either in PEM format, in JWK format, or from the keystore. With this option, the public key is hardcoded and must be changed when the client generates a new key pair. You can even generate your own keystore from the Red Hat build of Keycloak Admin Console if you do not have your own keystore available. This option is the easiest when using authorization client.
-
Configure the JWKS URL where Red Hat build of Keycloak can download the client’s public keys. This option is the most flexible, since the client can rotate its keys anytime and Red Hat build of Keycloak always downloads new keys as needed without changing the configuration. In other words, Red Hat build of Keycloak downloads new keys when it sees the token signed by an unknown
To set up for this method, you need to code something such as the following in your keycloak.json
file:
"credentials": {
"jwt": {
"client-keystore-file": "classpath:keystore-client.jks",
"client-keystore-type": "JKS",
"client-keystore-password": "storepass",
"client-key-password": "keypass",
"client-key-alias": "clientkey",
"token-expiration": 10
}
}
With this configuration, the keystore file keystore-client.jks
must be available on classpath of the application, which uses authorization client. If you do not use the prefix classpath:
you can point to any file on the file system where the client application is running.
19.7.3. Client authentication with Signed JWT using client secret
This is the same as Client Authentication with Signed JWT except for using the client secret instead of the private key and certificate.
The client has a secret, which needs to be known to both the application using authorization client and the Red Hat build of Keycloak server. You choose Signed JWT with Client Secret
as the method of authenticating your client in the Credentials
tab in the Admin Console, and then paste this secret into the keycloak.json
file on the application side:
"credentials": {
"secret-jwt": {
"secret": "19666a4f-32dd-4049-b082-684c74115f28",
"algorithm": "HS512"
}
}
The "algorithm" field specifies the algorithm for the Signed JWT using Client Secret. It needs to be one of the following values : HS256, HS384, and HS512. For details, see JSON Web Algorithms (JWA).
This "algorithm" field is optional; HS256 is applied automatically if the "algorithm" field does not exist on the keycloak.json
file.
19.7.4. Add your own client authentication method
You can add your own client authentication method as well. You will need to implement both client-side and server-side providers. For more details see the Authentication SPI
section in Server Developer Guide.
