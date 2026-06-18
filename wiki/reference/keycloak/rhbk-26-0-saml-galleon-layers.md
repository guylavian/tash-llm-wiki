---
title: "Chapter 6. Red Hat build of Keycloak SAML Galleon feature pack for WildFly and EAP - Red Hat build of Keycloak 26.0 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-saml-galleon-layers
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/securing_applications_and_services_guide/saml-galleon-layers-
guide: securing_applications_and_services_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 6. Red Hat build of Keycloak SAML Galleon feature pack for WildFly and EAP - Red Hat build of Keycloak 26.0 Securing Applications and Services Guide

Chapter 6. Red Hat build of Keycloak SAML Galleon feature pack for WildFly and EAP
The SAML adapter is distributed as a Galleon feature pack for wildfly 29 or newer. More details about the subject in the WildFly documentation. The same option is provided for JBoss EAP 8 GA.
For an example about how to integrate Keycloak with JakartaEE applications running on latest Wildfly/EAP, take a look at the servlet-saml-service-provider
Jakarta folder in the Keycloak Quickstart GitHub Repository.
6.1. Installation
The provision of the feature pack is done using the wildfly-maven-plugin, wildfly-jar-maven-plugin or eap-maven-plugin respectively.
6.1.1. Example of provision using wildfly maven plugin
<plugin>
<groupId>org.wildfly.plugins</groupId>
<artifactId>wildfly-maven-plugin</artifactId>
<version>5.0.0.Final</version>
<configuration>
<feature-packs>
<feature-pack>
<location>wildfly@maven(org.jboss.universe:community-universe)#32.0.1.Final</location>
</feature-pack>
<feature-pack>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-saml-adapter-galleon-pack</artifactId>
<version>26.0.17</version>
</feature-pack>
</feature-packs>
<layers>
<layer>core-server</layer>
<layer>web-server</layer>
<layer>jaxrs-server</layer>
<layer>datasources-web-server</layer>
<layer>webservices</layer>
<layer>keycloak-saml</layer>
<layer>keycloak-client-saml</layer>
<layer>keycloak-client-saml-ejb</layer>
</layers>
</configuration>
<executions>
<execution>
<goals>
<goal>package</goal>
</goals>
</execution>
</executions>
</plugin>
6.1.2. Example of provision using wildfly jar maven plugin
<plugin>
<groupId>org.wildfly.plugins</groupId>
<artifactId>wildfly-jar-maven-plugin</artifactId>
<version>11.0.2.Final</version>
<configuration>
<feature-packs>
<feature-pack>
<location>wildfly@maven(org.jboss.universe:community-universe)#32.0.1.Final</location>
</feature-pack>
<feature-pack>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-saml-adapter-galleon-pack</artifactId>
<version>26.0.17</version>
</feature-pack>
</feature-packs>
<layers>
<layer>core-server</layer>
<layer>web-server</layer>
<layer>jaxrs-server</layer>
<layer>datasources-web-server</layer>
<layer>webservices</layer>
<layer>keycloak-saml</layer>
<layer>keycloak-client-saml</layer>
<layer>keycloak-client-saml-ejb</layer>
</layers>
</configuration>
<executions>
<execution>
<goals>
<goal>package</goal>
</goals>
</execution>
</executions>
</plugin>
6.1.3. Example of provision using EAP maven plugin
<plugin>
<groupId>org.jboss.eap.plugins</groupId>
<artifactId>eap-maven-plugin</artifactId>
<version>1.0.0.Final-redhat-00014</version>
<configuration>
<channels>
<channel>
<manifest>
<groupId>org.jboss.eap.channels</groupId>
<artifactId>eap-8.0</artifactId>
</manifest>
</channel>
</channels>
<feature-packs>
<feature-pack>
<location>org.keycloak:keycloak-saml-adapter-galleon-pack</location>
</feature-pack>
</feature-packs>
<layers>
<layer>core-server</layer>
<layer>web-server</layer>
<layer>jaxrs-server</layer>
<layer>datasources-web-server</layer>
<layer>webservices</layer>
<layer>keycloak-saml</layer>
<layer>keycloak-client-saml</layer>
<layer>keycloak-client-saml-ejb</layer>
</layers>
</configuration>
<executions>
<execution>
<goals>
<goal>package</goal>
</goals>
</execution>
</executions>
</plugin>
6.2. Configuration
The SAML client adapter is configured by a XML file /WEB-INF/keycloak-saml.xml
placed inside the WAR deployment. The configuration might look like the following:
<keycloak-saml-adapter xmlns="urn:keycloak:saml:adapter"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="urn:keycloak:saml:adapter https://www.keycloak.org/schema/keycloak_saml_adapter_1_10.xsd">
<SP entityID="http://localhost:8081/sales-post-sig/"
sslPolicy="EXTERNAL"
nameIDPolicyFormat="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"
logoutPage="/logout.jsp"
forceAuthentication="false"
isPassive="false"
turnOffChangeSessionIdOnLogin="false"
autodetectBearerOnly="false">
<Keys>
<Key signing="true" >
<KeyStore resource="/WEB-INF/keystore.jks" password="store123">
<PrivateKey alias="http://localhost:8080/sales-post-sig/" password="test123"/>
<Certificate alias="http://localhost:8080/sales-post-sig/"/>
</KeyStore>
</Key>
</Keys>
<PrincipalNameMapping policy="FROM_NAME_ID"/>
<RoleIdentifiers>
<Attribute name="Role"/>
</RoleIdentifiers>
<RoleMappingsProvider id="properties-based-role-mapper">
<Property name="properties.resource.location" value="/WEB-INF/role-mappings.properties"/>
</RoleMappingsProvider>
<IDP entityID="idp"
signaturesRequired="true">
<SingleSignOnService requestBinding="POST"
bindingUrl="http://localhost:8081/realms/demo/protocol/saml"
/>
<SingleLogoutService
requestBinding="POST"
responseBinding="POST"
postBindingUrl="http://localhost:8081/realms/demo/protocol/saml"
redirectBindingUrl="http://localhost:8081/realms/demo/protocol/saml"
/>
<Keys>
<Key signing="true">
<KeyStore resource="/WEB-INF/keystore.jks" password="store123">
<Certificate alias="demo"/>
</KeyStore>
</Key>
</Keys>
</IDP>
</SP>
</keycloak-saml-adapter>
You can use ${…}
enclosure as System property replacement. For example ${jboss.server.config.dir}
. To get detailed information of the different elements in the XML configuration file see Red Hat build of Keycloak SAML Galleon feature pack detailed configuration.
6.2.1. Securing a WAR
This section describes how to secure a WAR directly by adding config and editing files within your WAR package.
Once keycloak-saml.xml
is created and in the WEB-INF
directory of your WAR, you must set the auth-method
to KEYCLOAK-SAML
in web.xml
. You also have to use standard servlet security to specify role-base constraints on your URLs. Here’s an example web.xml file:
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee https://jakarta.ee/xml/ns/jakartaee/web-app_6_0.xsd"
version="6.0">
<module-name>customer-portal</module-name>
<security-constraint>
<web-resource-collection>
<web-resource-name>Admins</web-resource-name>
<url-pattern>/admin/*</url-pattern>
</web-resource-collection>
<auth-constraint>
<role-name>admin</role-name>
</auth-constraint>
<user-data-constraint>
<transport-guarantee>CONFIDENTIAL</transport-guarantee>
</user-data-constraint>
</security-constraint>
<security-constraint>
<web-resource-collection>
<web-resource-name>Customers</web-resource-name>
<url-pattern>/customers/*</url-pattern>
</web-resource-collection>
<auth-constraint>
<role-name>user</role-name>
</auth-constraint>
<user-data-constraint>
<transport-guarantee>CONFIDENTIAL</transport-guarantee>
</user-data-constraint>
</security-constraint>
<login-config>
<auth-method>KEYCLOAK-SAML</auth-method>
<realm-name>this is ignored currently</realm-name>
</login-config>
<security-role>
<role-name>admin</role-name>
</security-role>
<security-role>
<role-name>user</role-name>
</security-role>
</web-app>
All standard servlet settings except the auth-method
setting.
6.2.2. Securing WARs using the Red Hat build of Keycloak SAML Subsystem
You do not have to open a WAR to secure it with Red Hat build of Keycloak. Alternatively, you can externally secure it via the Red Hat build of Keycloak SAML Adapter Subsystem. While you don’t have to specify KEYCLOAK-SAML as an auth-method
, you still have to define the security-constraints
in web.xml
. You do not, however, have to create a WEB-INF/keycloak-saml.xml
file. This metadata is instead defined within the XML in your server’s domain.xml
or standalone.xml
subsystem configuration section.
<extensions>
<extension module="org.keycloak.keycloak-saml-adapter-subsystem"/>
</extensions>
<profile>
<subsystem xmlns="urn:jboss:domain:keycloak-saml:1.1">
<secure-deployment name="WAR MODULE NAME.war">
<SP entityID="APPLICATION URL">
...
</SP>
</secure-deployment>
</subsystem>
</profile>
The secure-deployment
name
attribute identifies the WAR you want to secure. Its value is the module-name
defined in web.xml
with .war
appended. The rest of the configuration uses the same XML syntax as keycloak-saml.xml
configuration defined in General Adapter Config.
An example configuration:
<subsystem xmlns="urn:jboss:domain:keycloak-saml:1.1">
<secure-deployment name="saml-post-encryption.war">
<SP entityID="http://localhost:8080/sales-post-enc/"
sslPolicy="EXTERNAL"
nameIDPolicyFormat="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"
logoutPage="/logout.jsp"
forceAuthentication="false">
<Keys>
<Key signing="true" encryption="true">
<KeyStore resource="/WEB-INF/keystore.jks" password="store123">
<PrivateKey alias="http://localhost:8080/sales-post-enc/" password="test123"/>
<Certificate alias="http://localhost:8080/sales-post-enc/"/>
</KeyStore>
</Key>
</Keys>
<PrincipalNameMapping policy="FROM_NAME_ID"/>
<RoleIdentifiers>
<Attribute name="Role"/>
</RoleIdentifiers>
<IDP entityID="idp">
<SingleSignOnService signRequest="true"
validateResponseSignature="true"
requestBinding="POST"
bindingUrl="http://localhost:8080/realms/saml-demo/protocol/saml"/>
<SingleLogoutService
validateRequestSignature="true"
validateResponseSignature="true"
signRequest="true"
signResponse="true"
requestBinding="POST"
responseBinding="POST"
postBindingUrl="http://localhost:8080/realms/saml-demo/protocol/saml"
redirectBindingUrl="http://localhost:8080/realms/saml-demo/protocol/saml"/>
<Keys>
<Key signing="true" >
<KeyStore resource="/WEB-INF/keystore.jks" password="store123">
<Certificate alias="saml-demo"/>
</KeyStore>
</Key>
</Keys>
</IDP>
</SP>
</secure-deployment>
</subsystem>
6.2.3. Setting SameSite value for JSESSIONID cookie
Browsers are planning to set the default value for the SameSite
attribute for cookies to Lax
. This setting means that cookies will be sent to applications only if the request originates in the same domain. This behavior can affect the SAML POST binding which may become non-functional. To preserve full functionality of the SAML adapter, we recommend setting the SameSite
value to None
for the JSESSIONID
cookie created by your container. Not doing so may result in resetting the container’s session with each request to Red Hat build of Keycloak.
To avoid setting the SameSite
attribute to None
, consider switching to the REDIRECT binding if it is acceptable, or to OIDC protocol where this workaround is not necessary.
To set the SameSite
value to None
for the JSESSIONID
cookie in Wildfly/EAP, add a file undertow-handlers.conf
with the following content to the WEB-INF
directory of your application.
samesite-cookie(mode=None, cookie-pattern=JSESSIONID)
The support for this configuration is available in Wildfly from version 19.1.0.
6.3. Registering with an Identity Provider
For each servlet-based adapter, the endpoint you register for the assert consumer service URL and single logout service must be the base URL of your servlet application with /saml
appended to it, that is, https://example.com/contextPath/saml
.
6.4. Logout
There are multiple ways you can log out from a web application. For Jakarta EE servlet containers, you can call HttpServletRequest.logout()
. For any other browser application, you can point the browser at any url of your web application that has a security constraint and pass in a query parameter GLO, i.e. http://myapp?GLO=true
. This will log you out if you have an SSO session with your browser.
6.4.1. Logout in clustered environment
Internally, the SAML adapter stores a mapping between the SAML session index, principal name (when known), and HTTP session ID. This mapping can be maintained in JBoss application server family (WildFly 10/11, EAP 6/7) across cluster for distributable applications. As a precondition, the HTTP sessions need to be distributed across cluster (i.e. application is marked with <distributable/>
tag in application’s web.xml
).
To enable the functionality, add the following section to your /WEB_INF/web.xml
file:
<context-param>
<param-name>keycloak.sessionIdMapperUpdater.classes</param-name>
<param-value>org.keycloak.adapters.saml.wildfly.infinispan.InfinispanSessionCacheIdMapperUpdater</param-value>
</context-param>
If the session cache of the deployment is named deployment-cache
, the cache used for SAML mapping will be named as deployment-cache.ssoCache
. The name of the cache can be overridden by a context parameter keycloak.sessionIdMapperUpdater.infinispan.cacheName
. The cache container containing the cache will be the same as the one containing the deployment session cache, but can be overridden by a context parameter keycloak.sessionIdMapperUpdater.infinispan.containerName
.
By default, the configuration of the SAML mapping cache will be derived from session cache. The configuration can be manually overridden in cache configuration section of the server just the same as other caches.
Currently, to provide reliable service, it is recommended to use replicated cache for the SAML session cache. Using distributed cache may lead to results where the SAML logout request would land to a node with no access to SAML session index to HTTP session mapping which would lead to unsuccessful logout.
6.4.2. Logout in cross-site scenario
Special handling is needed for handling sessions that span multiple data centers. Imagine the following scenario:
- Login requests are handled within cluster in data center 1.
- Admin issues logout request for a particular SAML session, the request lands in data center 2.
The data center 2 has to log out all sessions that are present in data center 1 (and all other data centers that share HTTP sessions).
To cover this case, the SAML session cache described above needs to be replicated not only within individual clusters but across all the data centers for example via standalone Infinispan/JDG server:
- A cache has to be added to the standalone Infinispan/JDG server.
- The cache from previous item has to be added as a remote store for the respective SAML session cache.
Once remote store is found to be present on SAML session cache during deployment, it is watched for changes and the local SAML session cache is updated accordingly.
6.5. Obtaining assertion attributes
After a successful SAML login, your application code may want to obtain attribute values passed with the SAML assertion. HttpServletRequest.getUserPrincipal()
returns a Principal
object that you can typecast into a Red Hat build of Keycloak specific class called org.keycloak.adapters.saml.SamlPrincipal
. This object allows you to look at the raw assertion and also has convenience functions to look up attribute values.
package org.keycloak.adapters.saml;
public class SamlPrincipal implements Serializable, Principal {
/**
* Get full saml assertion
*
* @return
*/
public AssertionType getAssertion() {
...
}
/**
* Get SAML subject sent in assertion
*
* @return
*/
public String getSamlSubject() {
...
}
/**
* Subject nameID format
*
* @return
*/
public String getNameIDFormat() {
...
}
@Override
public String getName() {
...
}
/**
* Convenience function that gets Attribute value by attribute name
*
* @param name
* @return
*/
public List<String> getAttributes(String name) {
...
}
/**
* Convenience function that gets Attribute value by attribute friendly name
*
* @param friendlyName
* @return
*/
public List<String> getFriendlyAttributes(String friendlyName) {
...
}
/**
* Convenience function that gets first value of an attribute by attribute name
*
* @param name
* @return
*/
public String getAttribute(String name) {
...
}
/**
* Convenience function that gets first value of an attribute by attribute name
*
*
* @param friendlyName
* @return
*/
public String getFriendlyAttribute(String friendlyName) {
...
}
/**
* Get set of all assertion attribute names
*
* @return
*/
public Set<String> getAttributeNames() {
...
}
/**
* Get set of all assertion friendly attribute names
*
* @return
*/
public Set<String> getFriendlyNames() {
...
}
}
6.6. Error Handling
Red Hat build of Keycloak has some error handling facilities for servlet based client adapters. When an error is encountered in authentication, the client adapter will call HttpServletResponse.sendError()
. You can set up an error-page
within your web.xml
file to handle the error however you want. The client adapter can throw 400, 401, 403, and 500 errors.
<error-page>
<error-code>403</error-code>
<location>/ErrorHandler</location>
</error-page>
The client adapter also sets an HttpServletRequest
attribute that you can retrieve. The attribute name is org.keycloak.adapters.spi.AuthenticationError
. Typecast this object to: org.keycloak.adapters.saml.SamlAuthenticationError
. This class can tell you exactly what happened. If this attribute is not set, then the adapter was not responsible for the error code.
public class SamlAuthenticationError implements AuthenticationError {
public static enum Reason {
EXTRACTION_FAILURE,
INVALID_SIGNATURE,
ERROR_STATUS
}
public Reason getReason() {
return reason;
}
public StatusResponseType getStatus() {
return status;
}
}
6.7. Troubleshooting
The best way to troubleshoot problems is to turn on debugging for SAML in both the client adapter and Red Hat build of Keycloak Server. Using your logging framework, set the log level to DEBUG
for the org.keycloak.saml
package. Turning this on allows you to see the SAML requests and response documents being sent to and from the server.
6.8. Multi Tenancy
SAML offers Multi Tenancy, meaning that a single target application (WAR) can be secured with multiple Red Hat build of Keycloak realms. The realms can be located on the same Red Hat build of Keycloak instance or on different instances.
To do this, the application must have multiple keycloak-saml.xml
adapter configuration files.
While you could have multiple instances of your WAR with different adapter configuration files deployed to different context-paths, this may be inconvenient and you may also want to select the realm based on something other than context-path.
Red Hat build of Keycloak makes it possible to have a custom config resolver, so you can choose which adapter config is used for each request. In SAML, the configuration is only interesting in the login processing; once the user is logged in, the session is authenticated and it does not matter if the keycloak-saml.xml
returned is different. For that reason, returning the same configuration for the same session is the correct way to go.
To achieve this, create an implementation of org.keycloak.adapters.saml.SamlConfigResolver
. The following example uses the Host
header to locate the proper configuration and load it and the associated elements from the applications' Java classpath:
package example;
import java.io.InputStream;
import org.keycloak.adapters.saml.SamlConfigResolver;
import org.keycloak.adapters.saml.SamlDeployment;
import org.keycloak.adapters.saml.config.parsers.DeploymentBuilder;
import org.keycloak.adapters.saml.config.parsers.ResourceLoader;
import org.keycloak.adapters.spi.HttpFacade;
import org.keycloak.saml.common.exceptions.ParsingException;
public class SamlMultiTenantResolver implements SamlConfigResolver {
@Override
public SamlDeployment resolve(HttpFacade.Request request) {
String host = request.getHeader("Host");
String realm = null;
if (host.contains("tenant1")) {
realm = "tenant1";
} else if (host.contains("tenant2")) {
realm = "tenant2";
} else {
throw new IllegalStateException("Not able to guess the keycloak-saml.xml to load");
}
InputStream is = getClass().getResourceAsStream("/" + realm + "-keycloak-saml.xml");
if (is == null) {
throw new IllegalStateException("Not able to find the file /" + realm + "-keycloak-saml.xml");
}
ResourceLoader loader = new ResourceLoader() {
@Override
public InputStream getResourceAsStream(String path) {
return getClass().getResourceAsStream(path);
}
};
try {
return new DeploymentBuilder().build(is, loader);
} catch (ParsingException e) {
throw new IllegalStateException("Cannot load SAML deployment", e);
}
}
}
You must also configure which SamlConfigResolver
implementation to use with the keycloak.config.resolver
context-param in your web.xml
:
<web-app>
...
<context-param>
<param-name>keycloak.config.resolver</param-name>
<param-value>example.SamlMultiTenantResolver</param-value>
</context-param>
</web-app>
6.9. Red Hat build of Keycloak specific errors
Red Hat build of Keycloak server can send an error to the client application in the SAML response, which may contain a SAML status such as:
<samlp:Status>
<samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Responder">
<samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:AuthnFailed"/>
</samlp:StatusCode>
<samlp:StatusMessage>authentication_expired</samlp:StatusMessage>
</samlp:Status>
Red Hat build of Keycloak sends this error when a user is authenticated and has an SSO session, but the authentication session expired in the current browser tab and hence Red Hat build of Keycloak server cannot automatically do SSO re-authentication of the user and redirect back to client with successful response. When a client application receives this type of error, it is ideal to retry authentication immediately and send a new SAML request to the Red Hat build of Keycloak server, which should typically always authenticate the user due to the SSO session and redirect back. The SAML adapter performs that retry automatically if the commented status is returned by the server. More details in the Server Administration Guide.
