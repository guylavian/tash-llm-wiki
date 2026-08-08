---
title: "Chapter 1. Using OpenID Connect (OIDC) and Keycloak to centralize authorization - Red Hat build of Quarkus 3.27 Keycloak authorization"
type: reference
domain: keycloak
slug: doc-security-keycloak-authorization-3
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_quarkus/3.27/html/keycloak_authorization/security-keycloak-authorization
guide: keycloak_authorization
documentKind: "Documentation"
abstract: "Learn how to enable bearer token authorization in your Quarkus application by using Keycloak Authorization Services for secure access to protected resources. 1.1. Overview The Keycloak Authorization extension, quarkus-keycloak-authorization, extends the OpenID Connect extension, quarkus-oidc, to provide advanced authorization capabilities. It features a policy enforcer that dynamically manages acc…"
---

# Chapter 1. Using OpenID Connect (OIDC) and Keycloak to centralize authorization - Red Hat build of Quarkus 3.27 Keycloak authorization

Chapter 1. Using OpenID Connect (OIDC) and Keycloak to centralize authorization
Learn how to enable bearer token authorization in your Quarkus application by using Keycloak Authorization Services for secure access to protected resources.
1.1. Overview
The Keycloak Authorization extension, quarkus-keycloak-authorization
, extends the OpenID Connect extension, quarkus-oidc
, to provide advanced authorization capabilities. It features a policy enforcer that dynamically manages access to secured resources. Access is governed by permissions defined in Keycloak, supporting flexible and dynamic Resource-Based Access Control (RBAC).
Use the quarkus-keycloak-authorization
extension only if you are using Keycloak and the Keycloak Authorization Services feature is enabled in your environment to handle authorization decisions.
If you are not using Keycloak, or if Keycloak is configured without the Keycloak Authorization Services feature, use the quarkus-oidc
extension instead.
How it works
The quarkus-keycloak-authorization
extension centralizes authorization responsibilities in Keycloak, enhancing security and simplifying application maintenance:
-
It uses the
quarkus-oidc
extension to verify bearer tokens. - It sends verified tokens to Keycloak Authorization Services.
- It allows Keycloak to evaluate resource-based permissions dynamically by using attributes such as resource name, identifier, or URI.
By externalizing authorization decisions, you can:
- Implement diverse access control strategies without modifying application code.
- Reduce redeployment needs as security requirements evolve.
Compatibility
This extension is compatible only with Quarkus OIDC service applications. It complements explicit mechanisms such as role-based access control with dynamic authorization policies.
Key Features
- Centralized Management: Delegate authorization decisions to Keycloak for consistent security policies across applications.
- Dynamic Permissions: Define access control dynamically by using resource attributes.
- Simplified Maintenance: Reduce the need to update and redeploy applications when access policies change.
Setting Up
Before using this extension, ensure the following:
- Keycloak Authorization Services feature is enabled in your Keycloak instance.
-
Your Quarkus application includes the
quarkus-keycloak-authorization
extension.
For detailed steps, see the OIDC Bearer Token Authentication guide.
Additional resources
To learn more about Keycloak Authorization Services and the policy enforcer, visit the official documentation: Keycloak Authorization Services Documentation.
1.2. Prerequisites
To complete this guide, you need:
- Roughly 15 minutes
- An IDE
-
JDK 17+ installed with
JAVA_HOME
configured appropriately - Apache Maven 3.8.6 or later
- A working container runtime (Docker or Podman)
- Optionally the Quarkus CLI if you want to use it
- Optionally Mandrel or GraalVM installed and configured appropriately if you want to build a native executable (or Docker if you use a native container build)
- jq tool
- Keycloak
1.3. Architecture
This example demonstrates a simple microservice setup with two protected endpoints:
-
/api/users/me
-
/api/admin
Token-based access control
Access to these endpoints is controlled by using bearer tokens. To gain access, the following conditions must be met:
- Valid token: The token must have a correct signature, a valid expiration date, and the appropriate audience.
- Trust: The microservice must trust the issuing Keycloak server.
The bearer tokens issued by the Keycloak server serve as:
- User identifiers: Indicating the subject (user) for whom the token was issued.
- Client references: Identifying the client application acting on behalf of the user, per OAuth 2.0 Authorization Server standards.
Endpoints and access policies
For /api/users/me
:
-
Access policy: Open to users with a valid bearer token and the
user
role. Response: Returns user details as a JSON object derived from the token.
Example response
{ "user": { "id": "1234", "username": "johndoe", "email": "johndoe@example.com" } }
For /api/admin
:
-
Access policy: Restricted to users with a valid bearer token and the
admin
role.
Decoupled authorization
This example highlights the use of role-based access control (RBAC) policies to protect resources. Key points include:
- Policy flexibility: Keycloak supports various policy types, such as attribute-based and custom policies, enabling fine-grained control.
- Decoupled application logic: Authorization policies are managed entirely by Keycloak, allowing your application to focus on its core functionality.
1.4. Solution
We recommend that you follow the instructions in the next sections and create the application step by step. However, you can go right to the completed example.
Clone the Git repository: git clone https://github.com/quarkusio/quarkus-quickstarts.git -b 3.27
, or download an archive.
The solution is in the security-keycloak-authorization-quickstart
directory.
1.5. Creating the project
To get started, create a new project by using the following command:
Using the Quarkus CLI:
quarkus create app org.acme:security-keycloak-authorization-quickstart \ --extension='oidc,keycloak-authorization,rest-jackson' \ --no-code cd security-keycloak-authorization-quickstart
To create a Gradle project, add the
--gradle
or--gradle-kotlin-dsl
option.For more information about how to install and use the Quarkus CLI, see the Quarkus CLI guide.
Using Maven:
mvn com.redhat.quarkus.platform:quarkus-maven-plugin:3.27.3.SP2-redhat-00001:create \ -DprojectGroupId=org.acme \ -DprojectArtifactId=security-keycloak-authorization-quickstart \ -Dextensions='oidc,keycloak-authorization,rest-jackson' \ -DnoCode cd security-keycloak-authorization-quickstart
To create a Gradle project, add the
-DbuildTool=gradle
or-DbuildTool=gradle-kotlin-dsl
option.
For Windows users:
-
If using cmd, (don’t use backward slash
\
and put everything on the same line) -
If using Powershell, wrap
-D
parameters in double quotes e.g."-DprojectArtifactId=security-keycloak-authorization-quickstart"
This command generates a new project with the keycloak-authorization
extension. The extension integrates a Keycloak Adapter into your Quarkus application, providing the necessary capabilities to interact with a Keycloak server and perform bearer token authorization.
Adding extensions to an existing project
If you already have an existing Quarkus project, you can add the oidc
and keycloak-authorization
extensions by running the following command in your project’s base directory:
Using the Quarkus CLI:
quarkus extension add oidc,keycloak-authorization
Using Maven:
./mvnw quarkus:add-extension -Dextensions='oidc,keycloak-authorization'
Using Gradle:
./gradlew addExtension --extensions='oidc,keycloak-authorization'
This command adds the following dependencies to your build file:
Using Maven:
<dependency> <groupId>io.quarkus</groupId> <artifactId>quarkus-oidc</artifactId> </dependency> <dependency> <groupId>io.quarkus</groupId> <artifactId>quarkus-keycloak-authorization</artifactId> </dependency>
Using Gradle:
implementation("io.quarkus:quarkus-oidc") implementation("io.quarkus:quarkus-keycloak-authorization")
Implementing the /api/users/me
endpoint
Start by implementing the /api/users/me
endpoint. The following code defines a Jakarta REST resource that provides user details:
package org.acme.security.keycloak.authorization;
import jakarta.inject.Inject;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import org.jboss.resteasy.reactive.NoCache;
import io.quarkus.security.identity.SecurityIdentity;
@Path("/api/users")
public class UsersResource {
@Inject
SecurityIdentity identity;
@GET
@Path("/me")
@NoCache
public User me() {
return new User(identity);
}
public static class User {
private final String userName;
User(SecurityIdentity identity) {
this.userName = identity.getPrincipal().getName();
}
public String getUserName() {
return userName;
}
}
}
Implementing the /api/admin
endpoint
Next, define the /api/admin
endpoint. The following code represents a simple Jakarta REST resource protected with authentication:
package org.acme.security.keycloak.authorization;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import io.quarkus.security.Authenticated;
@Path("/api/admin")
@Authenticated
public class AdminResource {
@GET
@Produces(MediaType.TEXT_PLAIN)
public String admin() {
return "granted";
}
}
Role-based access control with Keycloak
Notice that explicit annotations such as @RolesAllowed
are not defined to enforce access control for the resources. Instead, the keycloak-authorization
extension dynamically maps the URIs of protected resources in Keycloak.
Access control is managed as follows:
- Keycloak evaluates permissions for each request based on its configured policies.
- The extension enforces these permissions, granting or denying access based on the roles or policies defined in Keycloak.
This decouples access control logic from the application code, making it easier to manage and update access policies directly in Keycloak.
1.6. Configuring the application
You can use the OpenID Connect extension to configure the adapter settings through the application.properties
file, typically located in the src/main/resources
directory. For example:
# OIDC Configuration
%prod.quarkus.oidc.auth-server-url=https://localhost:8543/realms/quarkus
quarkus.oidc.client-id=backend-service
quarkus.oidc.credentials.secret=secret
quarkus.oidc.tls.verification=none
# Enable Policy Enforcement
quarkus.keycloak.policy-enforcer.enable=true
# Import the realm file with Dev Services for Keycloak
# Note: This property is effective only in dev mode, not in JVM or native modes
quarkus.keycloak.devservices.realm-path=quarkus-realm.json
- 1
- Specifies the URL of the Keycloak server and the realm used for authentication.
- 2
- Identifies the client application within the Keycloak realm.
- 3
- Defines the client secret for authentication with the Keycloak server.
- 4
- Disables TLS verification for development purposes, not recommended for production.
- 5
- Enables the Keycloak policy enforcer to manage access control based on defined permissions.
- 6
- Configures Dev Services to import a specified realm file, effective only in dev mode and not in JVM or native modes.
Adding the %prod.
profile prefix to quarkus.oidc.auth-server-url
ensures that Dev Services for Keycloak automatically launches a container in development mode. For more details, see the Running the application in Dev mode section.
By default, applications using the quarkus-oidc
extension are treated as service
type applications. However, the extension also supports web-app
type applications under the following conditions:
-
The access token returned during the authorization code grant flow must be the source of roles (
quarkus.oidc.roles.source=accesstoken
). -
Note: For
web-app
type applications, ID token roles are checked by default.
1.7. Starting and configuring the Keycloak server
Do not start the Keycloak server when you run the application in dev mode. Dev Services for Keycloak launches a container. For more information, see the Running the application in Dev mode section.
To start a Keycloak server, use the following Docker command:
docker run --name keycloak \
-e KC_BOOTSTRAP_ADMIN_USERNAME=admin \
-e KC_BOOTSTRAP_ADMIN_PASSWORD=admin \
-p 8543:8443 \
-v "$(pwd)"/config/keycloak-keystore.jks:/etc/keycloak-keystore.jks \
quay.io/keycloak/keycloak:{keycloak.version} \
start --hostname-strict=false --https-key-store-file=/etc/keycloak-keystore.jks
- 1
- For
keycloak.version
, ensure the version is26.3.4
or later. - 2
- For Keycloak keystore, use the
keycloak-keystore.jks
file located at quarkus-quickstarts/security-keycloak-authorization-quickstart/config.
Accessing the Keycloak server
- Open your browser and navigate to https://localhost:8543.
Log in to the Keycloak Administration Console by using the following credentials:
-
Username:
admin
-
Password:
admin
-
Username:
Importing the realm configuration
To create a new realm, import the realm configuration file. For detailed steps on creating realms, refer to the Keycloak documentation: Create a new realm.
After importing the realm, go to Clients, choose the backend-service
client, and select the Authorization and Resources tab for this client. You can now review the resource permissions:
Role of Keycloak in resource permissions
The resource access permissions are configured directly in Keycloak, which eliminates the need for @RolesAllowed
annotations in your application code. This approach centralizes access control management within Keycloak, simplifying application maintenance and security updates.
1.8. Running the application in dev mode
To run the application in development mode, use the following command:
Using the Quarkus CLI:
quarkus dev
Using Maven:
./mvnw quarkus:dev
Using Gradle:
./gradlew --console=plain quarkusDev
Dev Services for Keycloak starts a Keycloak container and imports the quarkus-realm.json
configuration file.
Open a Dev UI available at /q/dev-ui and click a Provider: Keycloak link on an OpenID Connect card in the Dev UI.
Interacting with Dev UI
Testing user permissions
When prompted to log in to a Single Page Application
provided by OpenID Connect Dev UI
, do the following:
Log in as
alice
(password:alice
), who only has aUser Permission
to access the/api/users/me
resource:-
Access
/api/admin
, which returns403
. -
Access
/api/users/me
, which returns200
.
-
Access
Log out and log in as
admin
(password:admin
), who has bothAdmin Permission
to access the/api/admin
resource andUser Permission
to access the/api/users/me
resource:-
Access
/api/admin
, which returns200
. -
Access
/api/users/me
, which returns200
.
-
Access
Customizing the Keycloak realm
If you started Dev Services for Keycloak without importing a realm file such as quarkus-realm.json, create a default quarkus
realm without Keycloak authorization policies:
- Select the Keycloak Admin link from the OpenID Connect card in the Dev UI.
-
Log in to the Keycloak admin console. The username and password are both
admin
. -
Follow the instructions at Keycloak Authorization Services documentation to enable authorization policies in the
quarkus
realm.
The Keycloak Admin link is easy to find in Dev UI:
Adding custom JavaScript policies
If your application uses Keycloak authorization configured with JavaScript policies that are deployed in a JAR archive, Dev Services for Keycloak can transfer this archive to the Keycloak container. Use the following properties in application.properties
to configure the transfer:
# Alias the policies archive
quarkus.keycloak.devservices.resource-aliases.policies=/policies.jar
# Map the policies archive to a specific location in the container
quarkus.keycloak.devservices.resource-mappings.policies=/opt/keycloak/providers/policies.jar
1.9. Running the application in JVM mode
After exploring the application in dev mode, you can run it as a standard Java application in JVM mode.
Compile the application:
Using the Quarkus CLI:
quarkus build
Using Maven:
./mvnw install
Using Gradle:
./gradlew build
Run the application:
java -jar target/quarkus-app/quarkus-run.jar
1.10. Running the application in native mode
You can compile this demo into native code; no modifications are required.
Native compilation eliminates the need for a JVM in the production environment because the produced binary includes the runtime and is optimized for minimal resource usage.
Compilation takes longer and is disabled by default. To build the application, enable the native
profile.
Build the native binary:
Using the Quarkus CLI:
quarkus build --native
Using Maven:
./mvnw install -Dnative
Using Gradle:
./gradlew build -Dquarkus.native.enabled=true
After a while, run the native binary:
./target/security-keycloak-authorization-quickstart-1.0.0-SNAPSHOT-runner
1.11. Testing the application
See the preceding Running the application in Dev mode section for instructions on testing your application in development mode.
You can test the application running in JVM or native modes by using curl
.
Obtaining an access token
The application uses bearer token authorization. To access its resources, first obtain an access token from the Keycloak server:
export access_token=$(\
curl --insecure -X POST https://localhost:8543/realms/quarkus/protocol/openid-connect/token \
--user backend-service:secret \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'username=alice&password=alice&grant_type=password' | jq --raw-output '.access_token' \
)
If the quarkus.oidc.authentication.user-info-required
property is set to true
, the application requires that an access token is used to request UserInfo
. In that case, you must add the scope=openid
query parameter to the token grant request; for example:
export access_token=$(\
curl --insecure -X POST http://localhost:8180/realms/quarkus/protocol/openid-connect/token \
--user backend-service:secret \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'username=alice&password=alice&grant_type=password&scope=openid' | jq --raw-output '.access_token' \
)
The preceding example obtains an access token for the user alice
.
Accessing the /api/users/me
endpoint
Any user with a valid access token can access the http://localhost:8080/api/users/me
endpoint, which returns a JSON payload with user details:
curl -v -X GET \
http://localhost:8080/api/users/me \
-H "Authorization: Bearer "$access_token
Accessing the /api/admin
endpoint
The http://localhost:8080/api/admin
endpoint is restricted to users with the admin
role. If you try to access this endpoint with the previously issued access token, the server returns a 403 Forbidden
response:
curl -v -X GET \
http://localhost:8080/api/admin \
-H "Authorization: Bearer "$access_token
Getting an admin access token
To access the admin endpoint, get an access token for the admin
user:
export access_token=$(\
curl --insecure -X POST https://localhost:8543/realms/quarkus/protocol/openid-connect/token \
--user backend-service:secret \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'username=admin&password=admin&grant_type=password' | jq --raw-output '.access_token' \
)
1.12. Injecting the authorization client
You can use the Keycloak Authorization Client Java API for advanced tasks, such as managing resources and getting permissions directly from Keycloak. To enable this functionality, inject an AuthzClient
instance into your beans:
public class ProtectedResource {
@Inject
AuthzClient authzClient;
}
To use the AuthzClient
directly, set quarkus.keycloak.policy-enforcer.enable=true
. Otherwise, no bean is available for injection.
1.13. Mapping protected resources
By default, the extension uses lazy loading to fetch resources from Keycloak on demand. It uses the request URI to identify and map application resources that require protection.
To disable lazy loading and instead pre-load all resources at startup, configure the following property:
quarkus.keycloak.policy-enforcer.lazy-load-paths=false
The time required to pre-load resources from Keycloak during startup depends on the number of resources, which might impact your application’s initial load time.
1.14. More about configuring protected resources
In the default configuration, Keycloak manages the roles and decides who can access which routes.
To configure the protected routes by using the @RolesAllowed
annotation or the application.properties
file, check the OpenID Connect (OIDC) Bearer token authentication and Authorization of web endpoints guides. For more details, check the Quarkus Security overview.
1.15. Access to public resources
To allow access to a public resource without applying quarkus-keycloak-authorization
policies, define a permit
HTTP policy in the application.properties
file. For more information, see the Authorization of web endpoints guide.
You do not need to disable policy checks for a Keycloak Authorization Policy when using configurations like the following:
quarkus.keycloak.policy-enforcer.paths.1.paths=/api/public
quarkus.keycloak.policy-enforcer.paths.1.enforcement-mode=DISABLED
To restrict access to public resources for anonymous users, define an enforcing Keycloak Authorization Policy:
quarkus.keycloak.policy-enforcer.paths.1.paths=/api/public-enforcing
quarkus.keycloak.policy-enforcer.paths.1.enforcement-mode=ENFORCING
Only the default tenant configuration applies when controlling anonymous access to the public resource is required.
1.16. Checking permission scopes programmatically
In addition to resource permissions, you can define method scopes. A scope typically represents an action performed on a resource. You can create an enforcing Keycloak Authorization Policy with a method scope. For example:
# path policy with enforced scope 'read' for method 'GET'
quarkus.keycloak.policy-enforcer.paths.1.name=Scope Permission Resource
quarkus.keycloak.policy-enforcer.paths.1.paths=/api/protected/standard-way
quarkus.keycloak.policy-enforcer.paths.1.methods.get.method=GET
quarkus.keycloak.policy-enforcer.paths.1.methods.get.scopes=read
# path policies without scope
quarkus.keycloak.policy-enforcer.paths.2.name=Scope Permission Resource
quarkus.keycloak.policy-enforcer.paths.2.paths=/api/protected/programmatic-way,/api/protected/annotation-way
- 1
- User must have resource permission
Scope Permission Resource
and scoperead
The Keycloak Policy Enforcer secures the /api/protected/standard-way
request path, removing the need for annotations such as @RolesAllowed
. However, in some scenarios, you may need to perform a programmatic check.
You can achieve this by injecting a SecurityIdentity
instance into your beans, as shown in the following example. Or, you can get the same result by annotating the resource method with @PermissionsAllowed
. The following example demonstrates three resource methods, each requiring the same read
scope:
import java.security.BasicPermission;
import java.util.List;
import jakarta.inject.Inject;
import jakarta.ws.rs.ForbiddenException;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import org.keycloak.representations.idm.authorization.Permission;
import io.quarkus.security.PermissionsAllowed;
import io.quarkus.security.identity.SecurityIdentity;
import io.smallrye.mutiny.Uni;
@Path("/api/protected")
public class ProtectedResource {
@Inject
SecurityIdentity identity;
@GET
@Path("/standard-way")
public Uni<List<Permission>> standardWay() {
return Uni.createFrom().item(identity.<List<Permission>> getAttribute("permissions"));
}
@GET
@Path("/programmatic-way")
public Uni<List<Permission>> programmaticWay() {
var requiredPermission = new BasicPermission("Scope Permission Resource") {
@Override
public String getActions() {
return "read";
}
};
return identity.checkPermission(requiredPermission).onItem()
.transform(granted -> {
if (granted) {
return identity.getAttribute("permissions");
}
throw new ForbiddenException();
});
}
@PermissionsAllowed("Scope Permission Resource:read")
@GET
@Path("/annotation-way")
public Uni<List<Permission>> annotationWay() {
return Uni.createFrom().item(identity.<List<Permission>> getAttribute("permissions"));
}
}
- 1
- The
/standard-way
sub-path requires both the resource permission and theread
scope, based on the configuration set in theapplication.properties
file. - 2
- The
/programmatic-way
sub-path checks only for theScope Permission Resource
permission by default. However, you can enforce additional constraints, such as scope requirements, by usingSecurityIdentity#checkPermission
. - 3
- The
@PermissionsAllowed
annotation at/annotation-way
restricts access to requests that have theScope Permission Resource
permission along with theread
scope. For more information, see the section Authorization using annotations of the Authorization of web endpoints guide.
1.17. Multi-tenancy
You can set up policy enforcer configurations for each tenant, similar to how it is done with OpenID Connect (OIDC) multi-tenancy. For example:
quarkus.keycloak.policy-enforcer.enable=true
# Default Tenant
quarkus.oidc.auth-server-url=${keycloak.url:replaced-by-test-resource}/realms/quarkus
quarkus.oidc.client-id=quarkus-app
quarkus.oidc.credentials.secret=secret
quarkus.keycloak.policy-enforcer.enforcement-mode=PERMISSIVE
quarkus.keycloak.policy-enforcer.paths.1.name=Permission Resource
quarkus.keycloak.policy-enforcer.paths.1.paths=/api/permission
quarkus.keycloak.policy-enforcer.paths.1.claim-information-point.claims.static-claim=static-claim
# Service Tenant
quarkus.oidc.service-tenant.auth-server-url=${keycloak.url:replaced-by-test-resource}/realms/quarkus
quarkus.oidc.service-tenant.client-id=quarkus-app
quarkus.oidc.service-tenant.credentials.secret=secret
quarkus.keycloak.service-tenant.policy-enforcer.enforcement-mode=PERMISSIVE
quarkus.keycloak.service-tenant.policy-enforcer.paths.1.name=Permission Resource Service
quarkus.keycloak.service-tenant.policy-enforcer.paths.1.paths=/api/permission
quarkus.keycloak.service-tenant.policy-enforcer.paths.1.claim-information-point.claims.static-claim=static-claim
# WebApp Tenant
quarkus.oidc.webapp-tenant.auth-server-url=${keycloak.url:replaced-by-test-resource}/realms/quarkus
quarkus.oidc.webapp-tenant.client-id=quarkus-app
quarkus.oidc.webapp-tenant.credentials.secret=secret
quarkus.oidc.webapp-tenant.application-type=web-app
quarkus.oidc.webapp-tenant.roles.source=accesstoken
quarkus.keycloak.webapp-tenant.policy-enforcer.enforcement-mode=PERMISSIVE
quarkus.keycloak.webapp-tenant.policy-enforcer.paths.1.name=Permission Resource WebApp
quarkus.keycloak.webapp-tenant.policy-enforcer.paths.1.paths=/api/permission
quarkus.keycloak.webapp-tenant.policy-enforcer.paths.1.claim-information-point.claims.static-claim=static-claim
1.18. Dynamic tenant configuration resolution
To create configurations for multiple tenants while avoiding excessive entries in your configuration file, you can use the io.quarkus.keycloak.pep.TenantPolicyConfigResolver
interface to define them programmatically at runtime.
package org.acme.security.keycloak.authorization;
import java.util.Map;
import jakarta.enterprise.context.ApplicationScoped;
import io.quarkus.keycloak.pep.TenantPolicyConfigResolver;
import io.quarkus.keycloak.pep.runtime.KeycloakPolicyEnforcerConfig;
import io.quarkus.keycloak.pep.runtime.KeycloakPolicyEnforcerTenantConfig;
import io.quarkus.oidc.OidcRequestContext;
import io.quarkus.oidc.OidcTenantConfig;
import io.smallrye.mutiny.Uni;
import io.vertx.ext.web.RoutingContext;
@ApplicationScoped
public class CustomTenantPolicyConfigResolver implements TenantPolicyConfigResolver {
private final KeycloakPolicyEnforcerTenantConfig enhancedTenantConfig;
private final KeycloakPolicyEnforcerTenantConfig newTenantConfig;
public CustomTenantPolicyConfigResolver(KeycloakPolicyEnforcerConfig enforcerConfig) {
this.enhancedTenantConfig = KeycloakPolicyEnforcerTenantConfig.builder(enforcerConfig.defaultTenant())
.paths("/enhanced-config")
.permissionName("Permission Name")
.get("read-scope")
.build();
this.newTenantConfig = KeycloakPolicyEnforcerTenantConfig.builder()
.paths("/new-config")
.claimInformationPoint(Map.of("claims", Map.of("grant", "{request.parameter['grant']}")))
.build();
}
@Override
public Uni<KeycloakPolicyEnforcerTenantConfig> resolve(RoutingContext routingContext, OidcTenantConfig tenantConfig,
OidcRequestContext<KeycloakPolicyEnforcerTenantConfig> requestContext) {
String path = routingContext.normalizedPath();
String tenantId = tenantConfig.tenantId().orElse(null);
if ("enhanced-config-tenant".equals(tenantId) && path.equals("/enhanced-config")) {
return Uni.createFrom().item(enhancedTenantConfig);
} else if ("new-config-tenant".equals(tenantId) && path.equals("/new-config")) {
return Uni.createFrom().item(newTenantConfig);
}
return Uni.createFrom().nullItem();
}
}
- 1
- Define or update the
/enhanced-config
path in the default tenant configuration. - 2
- Add the
/new-config
path to the tenant configuration, including custom claims and values that are populated programmatically. - 3
- Fallback to the default static tenant configuration resolution defined in the
application.properties
file or other SmallRye Config sources.
1.19. Configuration reference
This configuration adheres to the official Keycloak Policy Enforcer Configuration guidelines. For detailed insights into various configuration options, see the following documentation:
🔒 Fixed at build time: Configuration property fixed at build time - All other configuration properties are overridable at runtime
| Configuration property | Type | Default |
|
🔒 Fixed at build time Enables policy enforcement.
Environment variable: | boolean |
|
|
Adapters will make separate HTTP invocations to the Keycloak server to turn an access code into an access token. This config option defines how many connections to the Keycloak server should be pooled
Environment variable: | int |
|
|
Specifies how policies are enforced.
Environment variable: |
|
|
|
Defines the limit of entries that should be kept in the cache
Environment variable: | int |
|
|
Defines the time in milliseconds when the entry should be expired
Environment variable: | long |
|
|
Specifies how the adapter should fetch the server for resources associated with paths in your application. If true, the policy enforcer is going to fetch resources on-demand accordingly with the path being requested
Environment variable: | boolean |
|
|
Complex config.
Environment variable: | Map<String,Map<String,Map<String,String>>> | |
|
Simple config.
Environment variable: | Map<String,Map<String,String>> | |
|
Specifies how scopes should be mapped to HTTP methods. If set to true, the policy enforcer will use the HTTP method from the current request to check whether access should be granted
Environment variable: | boolean |
|
|
The name of a resource on the server that is to be associated with a given path
Environment variable: | string | |
|
HTTP request paths that should be protected by the policy enforcer
Environment variable: | list of string | |
|
The name of the HTTP method
Environment variable: | string | required ⚠️ Required |
|
An array of strings with the scopes associated with the method
Environment variable: | list of string | required ⚠️ Required |
|
A string referencing the enforcement mode for the scopes associated with a method
Environment variable: |
|
|
|
Specifies how policies are enforced
Environment variable: |
|
|
|
Complex config.
Environment variable: | Map<String,Map<String,Map<String,String>>> | |
|
Simple config.
Environment variable: | Map<String,Map<String,String>> | |
| Type | Default | |
|
Adapters will make separate HTTP invocations to the Keycloak server to turn an access code into an access token. This config option defines how many connections to the Keycloak server should be pooled
Environment variable: | int |
|
|
Specifies how policies are enforced.
Environment variable: |
|
|
|
The name of a resource on the server that is to be associated with a given path
Environment variable: | string | |
|
HTTP request paths that should be protected by the policy enforcer
Environment variable: | list of string | |
|
The name of the HTTP method
Environment variable: | string | required ⚠️ Required |
|
An array of strings with the scopes associated with the method
Environment variable: | list of string | required ⚠️ Required |
|
A string referencing the enforcement mode for the scopes associated with a method
Environment variable: |
|
|
|
Specifies how policies are enforced
Environment variable: |
|
|
|
Complex config.
Environment variable: | Map<String,Map<String,Map<String,String>>> | |
|
Simple config.
Environment variable: | Map<String,Map<String,String>> | |
|
Defines the limit of entries that should be kept in the cache
Environment variable: | int |
|
|
Defines the time in milliseconds when the entry should be expired
Environment variable: | long |
|
|
Specifies how the adapter should fetch the server for resources associated with paths in your application. If true, the policy enforcer is going to fetch resources on-demand accordingly with the path being requested
Environment variable: | boolean |
|
|
Complex config.
Environment variable: | Map<String,Map<String,Map<String,String>>> | |
|
Simple config.
Environment variable: | Map<String,Map<String,String>> | |
|
Specifies how scopes should be mapped to HTTP methods. If set to true, the policy enforcer will use the HTTP method from the current request to check whether access should be granted
Environment variable: | boolean |
|
