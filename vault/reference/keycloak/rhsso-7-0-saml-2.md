---
title: "Chapter 3. SAML - Red Hat Single Sign-On 7.0 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhsso-7-0-saml-2
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.0/html/securing_applications_and_services_guide/saml_2
guide: securing_applications_and_services_guide
version: 7.0
family: rhsso
documentKind: "Documentation"
abstract: "This section describes how you can secure applications and services with SAML using either Red Hat Single Sign-On client adapters or generic SAML provider libraries. 3.1. Java Adapters Red Hat Single Sign-On comes with a range of different adapters for Java application. Selecting the correct adapter depends on the target platform. 3.1.1. General Adapter Config Each SAML client adapter supported by…"
---

# Chapter 3. SAML - Red Hat Single Sign-On 7.0 Securing Applications and Services Guide

Chapter 3. SAML
This section describes how you can secure applications and services with SAML using either Red Hat Single Sign-On client adapters or generic SAML provider libraries.
3.1. Java Adapters
Red Hat Single Sign-On comes with a range of different adapters for Java application. Selecting the correct adapter depends on the target platform.
3.1.1. General Adapter Config
Each SAML client adapter supported by Red Hat Single Sign-On can be configured by a simple XML text file. This is what one might look like:
<keycloak-saml-adapter>
<SP entityID="http://localhost:8081/sales-post-sig/"
sslPolicy="EXTERNAL"
nameIDPolicyFormat="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"
logoutPage="/logout.jsp"
forceAuthentication="false"
isPassive="false"
turnOffChangeSessionIdOnLogin="false">
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
<IDP entityID="idp"
signaturesRequired="true">
<SingleSignOnService requestBinding="POST"
bindingUrl="http://localhost:8081/auth/realms/demo/protocol/saml"
/>
<SingleLogoutService
requestBinding="POST"
responseBinding="POST"
postBindingUrl="http://localhost:8081/auth/realms/demo/protocol/saml"
redirectBindingUrl="http://localhost:8081/auth/realms/demo/protocol/saml"
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
Some of these configuration switches may be adapter specific and some are common across all adapters. For Java adapters you can use $\{…}
enclosure as System property replacement. For example $\{jboss.server.config.dir}
.
3.1.1.1. SP Element
Here is the explanation of the SP element attributes
<SP entityID="sp"
sslPolicy="ssl"
nameIDPolicyFormat="format"
forceAuthentication="true"
isPassive="false">
...
</SP>
- entityID
- This is the identifier for this client. The IDP needs this value to determine who the client is that is communicating with it. This setting is REQUIRED.
- sslPolicy
-
This is the SSL policy the adapter will enforce. Valid values are:
ALL
,EXTERNAL
, andNONE
. ForALL
, all requests must come in via HTTPS. ForEXTERNAL
, only non-private IP addresses must come over the wire via HTTPS. ForNONE
, no requests are required to come over via HTTPS. This settings is OPTIONAL. Default value isEXTERNAL
. - nameIDPolicyFormat
-
SAML clients can request a specific NameID Subject format. Fill in this value if you want a specific format. It must be a standard SAML format identifier, i.e.
urn:oasis:names:tc:SAML:2.0:nameid-format:transient
. This setting is OPTIONAL. By default, no special format is requested. - forceAuthentication
-
SAML clients can request that a user is re-authenticated even if they are already logged in at the IDP. Set this to
true
to enable. This setting is OPTIONAL. Default value isfalse
. - isPassive
-
SAML clients can request that a user is never asked to authenticate even if they are not logged in at the IDP. Set this to
true
if you want this. Do not use together withforceAuthentication
as they are opposite. This setting is OPTIONAL. Default value isfalse
. - turnOffChangeSessionIdOnLogin
-
The session id is changed by default on a successful login on some platforms to plug a security attack vector. Change this to
true
to disable this. It is recommended you do not turn it off. Default value isfalse
.
3.1.1.2. SP Keys and Key elements
If the IDP requires that the client application (SP) sign all of its requests and/or if the IDP will encrypt assertions, you must define the keys used to do this. For client signed documents you must define both the private and public key or certificate that will be used to sign documents. For encryption, you only have to define the private key that will be used to decrypt.
There are two ways to describe your keys. They can be stored within a Java KeyStore or you can copy/paste the keys directly within keycloak-saml.xml
in the PEM format.
<Keys>
<Key signing="true" >
...
</Key>
</Keys>
The Key
element has two optional attributes signing
and encryption
. When set to true these tell the adapter what the key will be used for. If both attributes are set to true, then the key will be used for both signing documents and decrypting encrypted assertions. You must set at least one of these attributes to true.
3.1.1.2.1. KeyStore element
Within the Key
element you can load your keys and certificates from a Java Keystore. This is declared within a KeyStore
element.
<Keys>
<Key signing="true" >
<KeyStore resource="/WEB-INF/keystore.jks" password="store123">
<PrivateKey alias="myPrivate" password="test123"/>
<Certificate alias="myCertAlias"/>
</KeyStore>
</Key>
</Keys>
Here are the XML config attributes that are defined with the KeyStore
element.
- file
- File path to the key store. This option is OPTIONAL. The file or resource attribute must be set.
- resource
- WAR resource path to the KeyStore. This is a path used in method call to ServletContext.getResourceAsStream(). This option is OPTIONAL. The file or resource attribute must be set.
- password
- The password of the KeyStore. This option is REQUIRED.
If you are defining keys that the SP will use to sign document, you must also specify references to your private keys and certificates within the Java KeyStore. The PrivateKey
and Certificate
elements in the above example define an alias
that points to the key or cert within the keystore. Keystores require an additional password to access private keys. In the PrivateKey
element you must define this password within a password
attribute.
3.1.1.2.2. Key PEMS
Within the Key
element you declare your keys and certificates directly using the sub elements PrivateKeyPem
, PublicKeyPem
, and CertificatePem
. The values contained in these elements must conform to the PEM key format. You usually use this option if you are generating keys using openssl
or similar command line tool.
<Keys>
<Key signing="true>
<PrivateKeyPem>
2341251234AB31234==231BB998311222423522334
</PrivateKeyPem>
<CertificatePem>
211111341251234AB31234==231BB998311222423522334
</CertificatePem>
</Key>
</Keys>
3.1.1.3. SP PrincipalNameMapping element
This element is optional. When creating a Java Principal object that you obtain from methods like HttpServletRequest.getUserPrincipal()
, you can define what name that is returned by the Principal.getName()
method.
<SP ...>
<PrincipalNameMapping policy="FROM_NAME_ID"/>
</SP>
<SP ...>
<PrincipalNameMapping policy="FROM_ATTRIBUTE" attribute="email" />
</SP>
The policy
attribute defines the policy used to populate this value. The possible values for this attribute are:
- FROM_NAME_ID
- This policy just uses whatever the SAML subject value is. This is the default setting
- FROM_ATTRIBUTE
-
This will pull the value from one of the attributes declared in the SAML assertion received from the server. You’ll need to specify the name of the SAML assertion attribute to use within the
attribute
XML attribute.
3.1.1.4. RoleIdentifiers element
The RoleIdentifiers
element defines what SAML attributes within the assertion received from the user should be used as role identifiers within the Java EE Security Context for the user.
<RoleIdentifiers>
<Attribute name="Role"/>
<Attribute name="member"/>
<Attribute name="memberOf"/>
</RoleIdentifiers>
By default Role
attribute values are converted to Java EE roles. Some IDPs send roles via a member
or memberOf
attribute assertion. You can define one or more Attribute
elements to specify which SAML attributes must be converted into roles.
3.1.1.5. IDP Element
Everything in the IDP element describes the settings for the identity provider (authentication server) the SP is communicating with.
<IDP entityID="idp"
signaturesRequired="true"
signatureAlgorithm="RSA_SHA1"
signatureCanonicalizationMethod="http://www.w3.org/2001/10/xml-exc-c14n#">
...
</IDP>
Here are the attribute config options you can specify within the IDP
element declaration.
- entityID
- This is the issuer ID of the IDP. This setting is REQUIRED.
- signaturesRequired
-
If set to
true
, the client adapter will sign every document it sends to the IDP. Also, the client will expect that the IDP will be signing any documents sent to it. This switch sets the default for all request and response types, but you will see later that you have some fine grain control over this. This setting is OPTIONAL and will default tofalse
. - signatureAlgorithm
-
This is the signature algorithm that the IDP expects signed documents to use. Allowed values are:
RSA_SHA1
,RSA_SHA256
,RSA_SHA512
, andDSA_SHA1
. This setting is OPTIONAL and defaults toRSA_SHA256
. - signatureCanonicalizationMethod
-
This is the signature canonicalization method that the IDP expects signed documents to use. This setting is OPTIONAL. The default value is
http://www.w3.org/2001/10/xml-exc-c14n#
and should be good for most IDPs.
3.1.1.6. IDP SingleSignOnService sub element
The SingleSignOnService
sub element defines the login SAML endpoint of the IDP. The client adapter will send requests to the IDP formatted via the settings within this element when it wants to login.
<SingleSignOnService signRequest="true"
validateResponseSignature="true"
requestBinding="post"
bindingUrl="url"/>
Here are the config attributes you can define on this element:
- signRequest
-
Should the client sign authn requests? This setting is OPTIONAL. Defaults to whatever the IDP
signaturesRequired
element value is. - validateResponseSignature
-
Should the client expect the IDP to sign the assertion response document sent back from an auhtn request? This setting OPTIONAL. Defaults to whatever the IDP
signaturesRequired
element value is. - requestBinding
-
This is the SAML binding type used for communicating with the IDP. This setting is OPTIONAL. The default value is
POST
, but you can set it toREDIRECT
as well. - responseBinding
-
SAML allows the client to request what binding type it wants authn responses to use. The values of this can be
POST
orREDIRECT
. This setting is OPTIONAL. The default is that the client will not request a specific binding type for responses. - bindingUrl
- This is the URL for the IDP login service that the client will send requests to. This setting is REQUIRED.
3.1.1.7. IDP SingleLogoutService sub element
The SingleLogoutService
sub element defines the logout SAML endpoint of the IDP. The client adapter will send requests to the IDP formatted via the settings within this element when it wants to logout.
<SingleLogoutService validateRequestSignature="true"
validateResponseSignature="true"
signRequest="true"
signResponse="true"
requestBinding="redirect"
responseBinding="post"
postBindingUrl="posturl"
redirectBindingUrl="redirecturl">
- signRequest
-
Should the client sign logout requests it makes to the IDP? This setting is OPTIONAL. Defaults to whatever the IDP
signaturesRequired
element value is. - signResponse
-
Should the client sign logout responses it sends to the IDP requests? This setting is OPTIONAL. Defaults to whatever the IDP
signaturesRequired
element value is. - validateRequestSignature
-
Should the client expect signed logout request documents from the IDP? This setting is OPTIONAL. Defaults to whatever the IDP
signaturesRequired
element value is. - validateResponseSignature
-
Should the client expect signed logout response documents from the IDP? This setting is OPTIONAL. Defaults to whatever the IDP
signaturesRequired
element value is. - requestBinding
-
This is the SAML binding type used for communicating SAML requests to the IDP. This setting is OPTIONAL. The default value is
POST
, but you can set it to REDIRECT as well. - responseBinding
-
This is the SAML binding type used for communicating SAML responses to the IDP. The values of this can be
POST
orREDIRECT
. This setting is OPTIONAL. The default value isPOST
, but you can set it toREDIRECT
as well. - postBindingUrl
-
This is the URL for the IDP’s logout service when using the POST binding. This setting is REQUIRED if using the
POST
binding. - redirectBindingUrl
- This is the URL for the IDP’s logout service when using the REDIRECT binding. This setting is REQUIRED if using the REDIRECT binding.
3.1.1.8. IDP Keys subelement
The Keys sub element of IDP is only used to define the certificate or public key to use to verify documents signed by the IDP. It is defined in the same way as the SP’s Key’s element. But again, you only have to define one certificate or public key reference.
<IDP entityID="idp">
...
<Keys>
<Key signing="true">
<KeyStore resource="/WEB-INF/keystore.jks" password="store123">
<Certificate alias="demo"/>
</KeyStore>
</Key>
</Keys>
</IDP>
3.1.2. JBoss EAP Adapter
To be able to secure WAR apps deployed on JBoss EAP, you must install and configure the Red Hat Single Sign-On SAML Adapter Subsystem.
You then provide a keycloak config, /WEB-INF/keycloak-saml.xml
file in your WAR and change the auth-method to KEYCLOAK-SAML within web.xml. Both methods are described in this section.
3.1.2.1. Adapter Installation
Each adapter is a separate download on the Red Hat Single Sign-On download site.
Install on JBoss EAP 6.x:
$ cd $JBOSS_HOME
$ unzip rh-sso-saml-eap6-adapter.zip
Install on JBoss EAP 7.x:
$ cd $JBOSS_HOME
$ unzip rh-sso-saml-eap7-adapter.zip
These zip files create new JBoss Modules specific to the Wildfly/JBoss EAP SAML Adapter within your Wildfly or JBoss EAP distro.
After adding the modules, you must then enable the Red Hat Single Sign-On SAML Subsystem within your app server’s server configuration: domain.xml
or standalone.xml
.
There is a CLI script that will help you modify your server configuration. Start the server and run the script from the server’s bin directory:
$ cd $JBOSS_HOME/bin
$ jboss-cli.sh -c --file=adapter-install-saml.cli
The script will add the extension, subsystem, and optional security-domain as described below.
<server xmlns="urn:jboss:domain:1.4">
<extensions>
<extension module="org.keycloak.keycloak-saml-adapter-subsystem"/>
...
</extensions>
<profile>
<subsystem xmlns="urn:jboss:domain:keycloak-saml:1.1"/>
...
</profile>
The keycloak
security domain should be used with EJBs and other components when you need the security context created in the secured web tier to be propagated to the EJBs (other EE component) you are invoking. Otherwise this configuration is optional.
<server xmlns="urn:jboss:domain:1.4">
<subsystem xmlns="urn:jboss:domain:security:1.2">
<security-domains>
...
<security-domain name="keycloak">
<authentication>
<login-module code="org.keycloak.adapters.jboss.KeycloakLoginModule"
flag="required"/>
</authentication>
</security-domain>
</security-domains>
For example, if you have a JAX-RS service that is an EJB within your WEB-INF/classes directory, you’ll want to annotate it with the @SecurityDomain
annotation as follows:
import org.jboss.ejb3.annotation.SecurityDomain;
import org.jboss.resteasy.annotations.cache.NoCache;
import javax.annotation.security.RolesAllowed;
import javax.ejb.EJB;
import javax.ejb.Stateless;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import java.util.ArrayList;
import java.util.List;
@Path("customers")
@Stateless
@SecurityDomain("keycloak")
public class CustomerService {
@EJB
CustomerDB db;
@GET
@Produces("application/json")
@NoCache
@RolesAllowed("db_user")
public List<String> getCustomers() {
return db.getCustomers();
}
}
We hope to improve our integration in the future so that you don’t have to specify the @SecurityDomain
annotation when you want to propagate a keycloak security context to the EJB tier.
3.1.2.2. Per WAR Configuration
This section describes how to secure a WAR directly by adding config and editing files within your WAR package.
The first thing you must do is create a keycloak-saml.xml
adapter config file within the WEB-INF
directory of your WAR. The format of this config file is described in the General Adapter Config section.
Next you must set the auth-method
to KEYCLOAK-SAML
in web.xml
. You also have to use standard servlet security to specify role-base constraints on your URLs. Here’s an example web.xml file:
<web-app xmlns="http://java.sun.com/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
version="3.0">
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
3.1.2.3. Securing WARs via Red Hat Single Sign-On SAML Subsystem
You do not have to crack open a WAR to secure it with Red Hat Single Sign-On. Alternatively, you can externally secure it via the Red Hat Single Sign-On SAML Adapter Subsystem. While you don’t have to specify KEYCLOAK-SAML as an auth-method
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
bindingUrl="http://localhost:8080/auth/realms/saml-demo/protocol/saml"/>
<SingleLogoutService
validateRequestSignature="true"
validateResponseSignature="true"
signRequest="true"
signResponse="true"
requestBinding="POST"
responseBinding="POST"
postBindingUrl="http://localhost:8080/auth/realms/saml-demo/protocol/saml"
redirectBindingUrl="http://localhost:8080/auth/realms/saml-demo/protocol/saml"/>
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
3.1.3. Registering with an IDP
For each servlet based adapter, the endpoint you register for the assert consumer service url and and single logout service must be the base url of your servlet application with /saml
appended to it i.e. https://example.com/contextPath/saml
3.1.4. Logout
There are multiple ways you can logout from a web application. For Java EE servlet containers, you can call HttpServletRequest.logout()
. For any other browser application, you can point the browser at any url of your web application that has a security constraint and pass in a query parameter GLO, i.e. http://myapp?GLO=true
. This will log you out if you have an SSO session with your browser.
3.1.5. Obtaining Assertion Attributes
After a successful SAML login, your application code may want to obtain attribute values passed with the SAML assertion. HttpServletRequest.getUserPrincipal()
returns a Principal
object that you can typecast into a Red Hat Single Sign-On specific class called org.keycloak.adapters.saml.SamlPrincipal
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
3.1.6. Error Handling
Red Hat Single Sign-On has some error handling facilities for servlet based client adapters. When an error is encountered in authentication, the client adapter will call HttpServletResponse.sendError()
. You can set up an error-page
within your web.xml
file to handle the error however you want. The client adapter may throw 400, 401, 403, and 500 errors.
<error-page>
<error-code>404</error-code>
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
3.1.7. Troubleshooting
The best way to troubleshoot some problems is to turn on debugging for saml in both the client adapter and the Red Hat Single Sign-On server. To do this turn on debugging int the org.keycloak.saml
package to debug
in your log4j or other logging framework. Turning this on allows you to see the SAML requests and response documents being sent to and from the server.
3.2. mod_auth_mellon Apache HTTPD Module
The mod_auth_mellon is an Apache HTTPD plugin for SAML. If your language/environment supports using Apache HTTPD as a proxy, then you can use mod_auth_mellon to secure your web application with SAML. Configuration of this adapter is beyond the scope of this document. Please see the mod_auth_mellon Github repo for more details on configuration.
To configure mod_auth_mellon you’ll need
- IDP entity descriptor XML file. This describes the connection to Red Hat Single Sign-On or another SAML IDP
- SP entity descriptor XML file. This describes the SAML connections and config for the application you are securing.
- Private key PEM file. This is a text file that defines the private key the application will use to sign documents. It is in the PEM format
- Certificate PEM file. This is a text file that defines the certificate for your application.
- mod_auth_mellon specific Apache HTTPD module config.
If you have already defined and registered the client application within a realm on the Red Hat Single Sign-On application server, Red Hat Single Sign-On can generate all the files you need except the Apache HTTPD module config. Go to the Installation
tab of your SAML client and select the Mod Auth Mellon files
option.
mod_auth_mellon config download
Click the Download
button and you will download a zip file that contains the XML descriptor and pem files you need.
