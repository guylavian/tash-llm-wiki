---
title: "Chapter 3. Using SAML to secure applications and services - Red Hat Single Sign-On 7.6 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhsso-7-6-using-saml-to-secure-applications-and-services
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html/securing_applications_and_services_guide/using_saml_to_secure_applications_and_services
guide: securing_applications_and_services_guide
version: 7.6
family: rhsso
documentKind: "Documentation"
abstract: "This section describes how you can secure applications and services with SAML using either Red Hat Single Sign-On client adapters or generic SAML provider libraries. 3.1. Java adapters Red Hat Single Sign-On comes with a range of different adapters for Java application. Selecting the correct adapter depends on the target platform. 3.1.1. General Adapter Config Each SAML client adapter supported by…"
---

# Chapter 3. Using SAML to secure applications and services - Red Hat Single Sign-On 7.6 Securing Applications and Services Guide

Chapter 3. Using SAML to secure applications and services
This section describes how you can secure applications and services with SAML using either Red Hat Single Sign-On client adapters or generic SAML provider libraries.
3.1. Java adapters
Red Hat Single Sign-On comes with a range of different adapters for Java application. Selecting the correct adapter depends on the target platform.
3.1.1. General Adapter Config
Each SAML client adapter supported by Red Hat Single Sign-On can be configured by a simple XML text file. This is what one might look like:
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
Some of these configuration switches may be adapter specific and some are common across all adapters. For Java adapters you can use ${…}
enclosure as System property replacement. For example ${jboss.server.config.dir}
.
3.1.1.1. SP element
Here is the explanation of the SP element attributes:
<SP entityID="sp"
sslPolicy="ssl"
nameIDPolicyFormat="format"
forceAuthentication="true"
isPassive="false"
keepDOMAssertion="true"
autodetectBearerOnly="false">
...
</SP>
- entityID
- This is the identifier for this client. The IdP needs this value to determine who the client is that is communicating with it. This setting is REQUIRED.
- sslPolicy
-
This is the SSL policy the adapter will enforce. Valid values are:
ALL
,EXTERNAL
, andNONE
. ForALL
, all requests must come in via HTTPS. ForEXTERNAL
, only non-private IP addresses must come over the wire via HTTPS. ForNONE
, no requests are required to come over via HTTPS. This setting is OPTIONAL. Default value isEXTERNAL
. - nameIDPolicyFormat
-
SAML clients can request a specific NameID Subject format. Fill in this value if you want a specific format. It must be a standard SAML format identifier:
urn:oasis:names:tc:SAML:2.0:nameid-format:transient
. This setting is OPTIONAL. By default, no special format is requested. - forceAuthentication
-
SAML clients can request that a user is re-authenticated even if they are already logged in at the IdP. Set this to
true
to enable. This setting is OPTIONAL. Default value isfalse
. - isPassive
-
SAML clients can request that a user is never asked to authenticate even if they are not logged in at the IdP. Set this to
true
if you want this. Do not use together withforceAuthentication
as they are opposite. This setting is OPTIONAL. Default value isfalse
. - turnOffChangeSessionIdOnLogin
-
The session ID is changed by default on a successful login on some platforms to plug a security attack vector. Change this to
true
to disable this. It is recommended you do not turn it off. Default value isfalse
. - autodetectBearerOnly
-
This should be set to true if your application serves both a web application and web services (for example SOAP or REST). It allows you to redirect unauthenticated users of the web application to the Red Hat Single Sign-On login page, but send an HTTP
401
status code to unauthenticated SOAP or REST clients instead as they would not understand a redirect to the login page. Red Hat Single Sign-On auto-detects SOAP or REST clients based on typical headers likeX-Requested-With
,SOAPAction
orAccept
. The default value is false. - logoutPage
-
This sets the page to display after logout. If the page is a full URL, such as
http://web.example.com/logout.html
, the user is redirected after logout to that page using the HTTP302
status code. If a link without scheme part is specified, such as/logout.jsp
, the page is displayed after logout, regardless of whether it lies in a protected area according tosecurity-constraint
declarations in web.xml, and the page is resolved relative to the deployment context root. - keepDOMAssertion
-
This attribute should be set to true to make the adapter store the DOM representation of the assertion in its original form inside the
SamlPrincipal
associated to the request. The assertion document can be retrieved using the methodgetAssertionDocument
inside the principal. This is specially useful when re-playing a signed assertion. The returned document is the one that was generated parsing the SAML response received by the Red Hat Single Sign-On server. This setting is OPTIONAL and its default value is false (the document is not saved inside the principal).
3.1.1.2. Service Provider keys and key elements
If the IdP requires that the client application (or SP) sign all of its requests and/or if the IdP will encrypt assertions, you must define the keys used to do this. For client-signed documents you must define both the private and public key or certificate that is used to sign documents. For encryption, you only have to define the private key that is used to decrypt it.
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
<Key signing="true">
<PrivateKeyPem>
2341251234AB31234==231BB998311222423522334
</PrivateKeyPem>
<CertificatePem>
211111341251234AB31234==231BB998311222423522334
</CertificatePem>
</Key>
</Keys>
3.1.1.3. SP PrincipalNameMapping element
This element is optional. When creating a Java Principal object that you obtain from methods such as HttpServletRequest.getUserPrincipal()
, you can define what name is returned by the Principal.getName()
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
element defines what SAML attributes within the assertion received from the user should be used as role identifiers within the Jakarta EE Security Context for the user.
<RoleIdentifiers>
<Attribute name="Role"/>
<Attribute name="member"/>
<Attribute name="memberOf"/>
</RoleIdentifiers>
By default Role
attribute values are converted to Jakarta EE roles. Some IdPs send roles using a member
or memberOf
attribute assertion. You can define one or more Attribute
elements to specify which SAML attributes must be converted into roles.
3.1.1.5. RoleMappingsProvider element
The RoleMappingsProvider
is an optional element that allows for the specification of the id and configuration of the org.keycloak.adapters.saml.RoleMappingsProvider
SPI implementation that is to be used by the SAML adapter.
When Red Hat Single Sign-On is used as the IDP, it is possible to use the built in role mappers to map any roles before adding them to the SAML assertion. However, the SAML adapters can be used to send SAML requests to third party IDPs and in this case it might be necessary to map the roles extracted from the assertion into a different set of roles as required by the SP. The RoleMappingsProvider
SPI allows for the configuration of pluggable role mappers that can be used to perform the necessary mappings.
The configuration of the provider looks as follows:
...
<RoleIdentifiers>
...
</RoleIdentifiers>
<RoleMappingsProvider id="properties-based-role-mapper">
<Property name="properties.resource.location" value="/WEB-INF/role-mappings.properties"/>
</RoleMappingsProvider>
<IDP>
...
</IDP>
The id
attribute identifies which of the installed providers is to be used. The Property
sub-element can be used multiple times to specify configuration properties for the provider.
3.1.1.5.1. Properties Based role mappings provider
Red Hat Single Sign-On includes a RoleMappingsProvider
implementation that performs the role mappings using a properties
file. This provider is identified by the id properties-based-role-mapper
and is implemented by the org.keycloak.adapters.saml.PropertiesBasedRoleMapper
class.
This provider relies on two configuration properties that can be used to specify the location of the properties
file that will be used. First, it checks if the properties.file.location
property has been specified, using the configured value to locate the properties
file in the filesystem. If the configured file is not located, the provider throws a RuntimeException
. The following snippet shows an example of provider using the properties.file.configuration
option to load the roles.properties
file from the /opt/mappers/
directory in the filesystem:
<RoleMappingsProvider id="properties-based-role-mapper">
<Property name="properties.file.location" value="/opt/mappers/roles.properties"/>
</RoleMappingsProvider>
If the properties.file.location
configuration has not been set, the provider checks the properties.resource.location
property, using the configured value to load the properties
file from the WAR
resource. If this configuration property is also not present, the provider attempts to load the file from /WEB-INF/role-mappings.properties
by default. Failure to load the file from the resource will result in the provider throwing a RuntimeException
. The following snippet shows an example of provider using the properties.resource.location
to load the roles.properties
file from the application’s /WEB-INF/conf/
directory:
<RoleMappingsProvider id="properties-based-role-mapper">
<Property name="properties.resource.location" value="/WEB-INF/conf/roles.properties"/>
</RoleMappingsProvider>
The properties
file can contain both roles and principals as keys, and a list of zero or more roles separated by comma as values. When invoked, the implementation iterates through the set of roles that were extracted from the assertion and checks, for each role, if a mapping exists. If the role maps to an empty role, it is discarded. If it maps to a set of one ore more different roles, then these roles are set in the result set. If no mapping is found for the role then it is included as is in the result set.
Once the roles have been processed, the implementation checks if the principal extracted from the assertion contains an entry properties
file. If a mapping for the principal exists, any roles listed as value are added to the result set. This allows the assignment of extra roles to a principal.
As an example, let’s assume the provider has been configured with the following properties file:
roleA=roleX,roleY
roleB=
kc_user=roleZ
If the principal kc_user
is extracted from the assertion with roles roleA
, roleB
and roleC
, the final set of roles assigned to the principal will be roleC
, roleX
, roleY
and roleZ
because roleA
is being mapped into both roleX
and roleY
, roleB
was mapped into an empty role - thus being discarded, roleC
is used as is and finally an additional role was added to the kc_user
principal (roleZ
).
Note: to use spaces in role names for mappings, use unicode replacements for space. For example, incoming 'role A' would appear as:
role\u0020A=roleX,roleY
3.1.1.5.2. Adding your own role mappings provider
To add a custom role mappings provider one simply needs to implement the org.keycloak.adapters.saml.RoleMappingsProvider
SPI. For more details see the SAML Role Mappings SPI
section in Server Developer Guide.
3.1.1.6. IDP Element
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
and should be good for most IDPs. - metadataUrl
- The URL used to retrieve the IDP metadata, currently this is only used to pick up signing and encryption keys periodically which allow cycling of these keys on the IDP without manual changes on the SP side.
3.1.1.7. IDP AllowedClockSkew sub element
The AllowedClockSkew
optional sub element defines the allowed clock skew between IDP and SP. The default value is 0.
<AllowedClockSkew unit="MILLISECONDS">3500</AllowedClockSkew>
- unit
-
It is possible to define the time unit attached to the value for this element. Allowed values are MICROSECONDS, MILLISECONDS, MINUTES, NANOSECONDS and SECONDS. This is OPTIONAL. The default value is
SECONDS
.
3.1.1.8. IDP SingleSignOnService sub element
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
. This setting is OPTIONAL. The default is that the client will not request a specific binding type for responses. - assertionConsumerServiceUrl
-
URL of the assertion consumer service (ACS) where the IDP login service should send responses to. This setting is OPTIONAL. By default it is unset, relying on the configuration in the IdP. When set, it must end in
/saml
, for examplehttp://sp.domain.com/my/endpoint/for/saml
. The value of this property is sent inAssertionConsumerServiceURL
attribute of SAMLAuthnRequest
message. This property is typically accompanied by theresponseBinding
attribute. - bindingUrl
- This is the URL for the IDP login service that the client will send requests to. This setting is REQUIRED.
3.1.1.9. IDP SingleLogoutService sub element
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
3.1.1.10. IDP Keys sub element
The Keys sub element of IDP is only used to define the certificate or public key to use to verify documents signed by the IDP. It is defined in the same way as the SP’s Keys element. But again, you only have to define one certificate or public key reference. Note that, if both IDP and SP are realized by Red Hat Single Sign-On server and adapter, respectively, there is no need to specify the keys for signature validation, see below.
It is possible to configure SP to obtain public keys for IDP signature validation from published certificates automatically, provided both SP and IDP are implemented by Red Hat Single Sign-On. This is done by removing all declarations of signature validation keys in Keys sub element. If the Keys sub element would then remain empty, it can be omitted completely. The keys are then automatically obtained by SP from SAML descriptor, location of which is derived from SAML endpoint URL specified in the IDP SingleSignOnService sub element. Settings of the HTTP client that is used for SAML descriptor retrieval usually needs no additional configuration, however it can be configured in the IDP HttpClient sub element.
It is also possible to specify multiple keys for signature verification. This is done by declaring multiple Key elements within Keys sub element that have signing
attribute set to true
. This is useful for example in situation when the IDP signing keys are rotated: There is usually a transition period when new SAML protocol messages and assertions are signed with the new key but those signed by previous key should still be accepted.
It is not possible to configure Red Hat Single Sign-On to both obtain the keys for signature verification automatically and define additional static signature verification keys.
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
3.1.1.11. IDP HttpClient sub element
The HttpClient
optional sub element defines the properties of HTTP client used for automatic obtaining of certificates containing public keys for IDP signature verification via SAML descriptor of the IDP when enabled.
<HttpClient connectionPoolSize="10"
disableTrustManager="false"
allowAnyHostname="false"
clientKeystore="classpath:keystore.jks"
clientKeystorePassword="pwd"
truststore="classpath:truststore.jks"
truststorePassword="pwd"
proxyUrl="http://proxy/"
socketTimeout="5000"
connectionTimeout="6000"
connectionTtl="500" />
- connectionPoolSize
-
This config option defines how many connections to the Red Hat Single Sign-On server should be pooled. This is OPTIONAL. The default value is
10
. - disableTrustManager
-
If the Red Hat Single Sign-On server requires HTTPS and this config option is set to
true
you do not have to specify a truststore. This setting should only be used during development and never in production as it will disable verification of SSL certificates. This is OPTIONAL. The default value isfalse
. - allowAnyHostname
-
If the Red Hat Single Sign-On server requires HTTPS and this config option is set to
true
the Red Hat Single Sign-On server’s certificate is validated via the truststore, but host name validation is not done. This setting should only be used during development and never in production as it will partly disable verification of SSL certificates. This seting may be useful in test environments. This is OPTIONAL. The default value isfalse
. - truststore
-
The value is the file path to a truststore file. If you prefix the path with
classpath:
, then the truststore will be obtained from the deployment’s classpath instead. Used for outgoing HTTPS communications to the Red Hat Single Sign-On server. Client making HTTPS requests need a way to verify the host of the server they are talking to. This is what the trustore does. The keystore contains one or more trusted host certificates or certificate authorities. You can create this truststore by extracting the public certificate of the Red Hat Single Sign-On server’s SSL keystore. This is REQUIRED unlessdisableTrustManager
istrue
. - truststorePassword
-
Password for the truststore. This is REQUIRED if
truststore
is set and the truststore requires a password. - clientKeystore
- This is the file path to a keystore file. This keystore contains client certificate for two-way SSL when the adapter makes HTTPS requests to the Red Hat Single Sign-On server. This is OPTIONAL.
- clientKeystorePassword
-
Password for the client keystore and for the client’s key. This is REQUIRED if
clientKeystore
is set. - proxyUrl
- URL to HTTP proxy to use for HTTP connections. This is OPTIONAL.
- socketTimeout
-
Timeout for socket waiting for data after establishing the connection in milliseconds. Maximum time of inactivity between two data packets. A timeout value of zero is interpreted as an infinite timeout. A negative value is interpreted as undefined (system default if applicable). The default value is
-1
. This is OPTIONAL. - connectionTimeout
-
Timeout for establishing the connection with the remote host in milliseconds. A timeout value of zero is interpreted as an infinite timeout. A negative value is interpreted as undefined (system default if applicable). The default value is
-1
. This is OPTIONAL. - connectionTtl
-
Connection time-to-live for client in milliseconds. A value less than or equal to zero is interpreted as an infinite value. The default value is
-1
. This is OPTIONAL.
3.1.2. JBoss EAP adapter
To be able to secure WAR apps deployed on JBoss EAP, you must install and configure the Red Hat Single Sign-On SAML Adapter Subsystem.
You then provide a keycloak config, /WEB-INF/keycloak-saml.xml
file in your WAR and change the auth-method to KEYCLOAK-SAML within web.xml.
You install the adapters by using a ZIP file or an RPM.
3.1.3. Installing adapters from a ZIP file
Each adapter is a separate download on the Red Hat Single Sign-On download site.
Procedure
Install the adapter that applies to your application server from the Downloads site.
Install on JBoss EAP 7.x:
$ cd $EAP_HOME $ unzip rh-sso-saml-eap7-adapter.zip
Install on JBoss EAP 6.x:
$ cd $EAP_HOME $ unzip rh-sso-saml-eap6-adapter.zip
These ZIP files create new JBoss Modules specific to the JBoss EAP SAML Adapter within your JBoss EAP distribution.
Use a CLI script to enable the Red Hat Single Sign-On SAML Subsystem within your app server’s server configuration:
domain.xml
orstandalone.xml
.Start the server and run the script that applies to your application server.
Use this command for JBoss EAP 7.1 or newer
$ cd $JBOSS_HOME $ ./bin/jboss-cli.sh -c --file=bin/adapter-elytron-install-saml.cli
NoteEAP supports OpenJDK 17 and Oracle JDK 17 since 7.4.CP7 and 7.4.CP8 respectively. Note that the new java version makes the elytron variant compulsory, so do not use the legacy adapter with JDK 17. Also, after running the adapter CLI file, execute the
enable-elytron-se17.cli
script provided by EAP. Both scripts are necessary to configure the elytron adapter and remove the incompatible EAP subsystems. For more details, see this Security Configuration Changes article.Use this command for JBoss EAP 7.0 and EAP 6.4
$ cd $JBOSS_HOME $ ./bin/jboss-cli.sh -c --file=bin/adapter-install-saml.cli
NoteIt is possible to use the legacy non-Elytron adapter on JBoss EAP 7.1 or newer as well, meaning you can use
adapter-install-saml.cli
even on those versions. However, we recommend to use the newer Elytron adapter.The script will add the extension, subsystem, and optional security-domain as described below.
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
The security context is propagated to the EJB tier automatically.
3.1.3.1. JBoss SSO
JBoss EAP has built-in support for single sign-on for web applications deployed to the same JBoss EAP instance. This should not be enabled when using Red Hat Single Sign-On.
3.1.3.2. Setting SameSite value for JSESSIONID cookie
Browsers are planning to set the default value for the SameSite
attribute for cookies to Lax
. This setting means that cookies will be sent to applications only if the request originates in the same domain. This behavior can affect the SAML POST binding which may become non-functional. To preserve full functionality of the SAML adapter, we recommend setting the SameSite
value to None
for the JSESSIONID
cookie created by your container. Not doing so may result in resetting the container’s session with each request to Red Hat Single Sign-On.
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
3.1.4. Installing JBoss EAP 7 Adapters from an RPM
With Red Hat Enterprise Linux 7, the term channel was replaced with the term repository. In these instructions only the term repository is used.
Prerequisites
You must subscribe to the JBoss EAP 7 repository before you can install the EAP 7 adapters from an RPM.
- Ensure that your Red Hat Enterprise Linux system is registered to your account using Red Hat Subscription Manager. For more information see the Red Hat Subscription Management documentation.
If you are already subscribed to another JBoss EAP repository, you must unsubscribe from that repository first.
For Red Hat Enterprise Linux 6, 7: Using Red Hat Subscription Manager, subscribe to the JBoss EAP 7.4 repository using the following command. Replace <RHEL_VERSION> with either 6 or 7 depending on your Red Hat Enterprise Linux version.
$ sudo subscription-manager repos --enable=jb-eap-7-for-rhel-<RHEL_VERSION>-server-rpms
For Red Hat Enterprise Linux 8: Using Red Hat Subscription Manager, subscribe to the JBoss EAP 7.4 repository using the following command:
$ sudo subscription-manager repos --enable=jb-eap-7.4-for-rhel-8-x86_64-rpms --enable=rhel-8-for-x86_64-baseos-rpms --enable=rhel-8-for-x86_64-appstream-rpms
Procedure
Install the EAP 7 adapters for SAML based on your version of Red Hat Enterprise Linux.
Install on Red Hat Linux 7:
$ sudo yum install eap7-keycloak-saml-adapter-sso7_6
Install on Red Hat Enterprise Linux 8:
$ sudo dnf install eap7-keycloak-adapter-sso7_6
NoteThe default EAP_HOME path for the RPM installation is /opt/rh/eap7/root/usr/share/wildfly.
Run the installation script for the SAML module:
$ $EAP_HOME/bin/jboss-cli.sh -c --file=$EAP_HOME/bin/adapter-install-saml.cli
Your installation is complete.
3.1.5. Installing JBoss EAP 6 Adapters from an RPM
With Red Hat Enterprise Linux 7, the term channel was replaced with the term repository. In these instructions only the term repository is used.
Prerequisites
You must subscribe to the JBoss EAP 6 repository before you can install the EAP 6 adapters from an RPM.
- Ensure that your Red Hat Enterprise Linux system is registered to your account using Red Hat Subscription Manager. For more information see the Red Hat Subscription Management documentation.
- If you are already subscribed to another JBoss EAP repository, you must unsubscribe from that repository first.
Using Red Hat Subscription Manager, subscribe to the JBoss EAP 6 repository using the following command. Replace <RHEL_VERSION> with either 6 or 7 depending on your Red Hat Enterprise Linux version.
$ sudo subscription-manager repos --enable=jb-eap-6-for-rhel-<RHEL_VERSION>-server-rpms
Procedure
Install the EAP 6 adapters for SAML using the following command:
$ sudo yum install keycloak-saml-adapter-sso7_6-eap6
NoteThe default EAP_HOME path for the RPM installation is /opt/rh/eap6/root/usr/share/wildfly.
Run the installation script for the SAML module:
$ $EAP_HOME/bin/jboss-cli.sh -c --file=$EAP_HOME/bin/adapter-install-saml.cli
Your installation is complete.
3.1.5.1. Securing a WAR
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
3.1.5.2. Securing WARs using the Red Hat Single Sign-On SAML Subsystem
You do not have to open a WAR to secure it with Red Hat Single Sign-On. Alternatively, you can externally secure it via the Red Hat Single Sign-On SAML Adapter Subsystem. While you don’t have to specify KEYCLOAK-SAML as an auth-method
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
3.1.6. Java Servlet filter adapter
If you want to use SAML with a Java servlet application that doesn’t have an adapter for that servlet platform, you can opt to use the servlet filter adapter that Red Hat Single Sign-On has. This adapter works a little differently than the other adapters. You still have to specify a /WEB-INF/keycloak-saml.xml
file as defined in the General Adapter Config section, but you do not define security constraints in web.xml. Instead you define a filter mapping using the Red Hat Single Sign-On servlet filter adapter to secure the url patterns you want to secure.
Backchannel logout works a bit differently than the standard adapters. Instead of invalidating the http session it instead marks the session ID as logged out. There’s just no way of arbitrarily invalidating an http session based on a session ID.
Backchannel logout does not currently work when you have a clustered application that uses the SAML filter.
<web-app xmlns="http://java.sun.com/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
version="3.0">
<module-name>customer-portal</module-name>
<filter>
<filter-name>Keycloak Filter</filter-name>
<filter-class>org.keycloak.adapters.saml.servlet.SamlFilter</filter-class>
</filter>
<filter-mapping>
<filter-name>Keycloak Filter</filter-name>
<url-pattern>/*</url-pattern>
</filter-mapping>
</web-app>
The Red Hat Single Sign-On filter has the same configuration parameters available as the other adapters except you must define them as filter init params instead of context params.
You can define multiple filter mappings if you have various different secure and unsecure url patterns.
You must have a filter mapping that covers /saml
. This mapping covers all server callbacks.
When registering SPs with an IdP, you must register http[s]://hostname/{context-root}/saml
as your Assert Consumer Service URL and Single Logout Service URL.
To use this filter, include this maven artifact in your WAR poms:
<dependency>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-saml-servlet-filter-adapter</artifactId>
<version>18.0.19.redhat-00001</version>
</dependency>
In order to use Multi Tenancy the keycloak.config.resolver
parameter should be passed as a filter parameter.
<filter>
<filter-name>Keycloak Filter</filter-name>
<filter-class>org.keycloak.adapters.saml.servlet.SamlFilter</filter-class>
<init-param>
<param-name>keycloak.config.resolver</param-name>
<param-value>example.SamlMultiTenantResolver</param-value>
</init-param>
</filter>
3.1.7. Registering with an Identity Provider
For each servlet-based adapter, the endpoint you register for the assert consumer service URL and single logout service must be the base URL of your servlet application with /saml
appended to it, that is, https://example.com/contextPath/saml
.
3.1.8. Logout
There are multiple ways you can logout from a web application. For Jakarta EE servlet containers, you can call HttpServletRequest.logout()
. For any other browser application, you can point the browser at any url of your web application that has a security constraint and pass in a query parameter GLO, i.e. http://myapp?GLO=true
. This will log you out if you have an SSO session with your browser.
3.1.8.1. Logout in clustered environment
Internally, the SAML adapter stores a mapping between the SAML session index, principal name (when known), and HTTP session ID. This mapping can be maintained in JBoss application server family (WildFly 10/11, EAP 6/7) across cluster for distributable applications. As a precondition, the HTTP sessions need to be distributed across cluster (i.e. application is marked with <distributable/>
tag in application’s web.xml
).
To enable the functionality, add the following section to your /WEB_INF/web.xml
file:
For EAP 7, WildFly 10/11:
<context-param>
<param-name>keycloak.sessionIdMapperUpdater.classes</param-name>
<param-value>org.keycloak.adapters.saml.wildfly.infinispan.InfinispanSessionCacheIdMapperUpdater</param-value>
</context-param>
For EAP 6:
<context-param>
<param-name>keycloak.sessionIdMapperUpdater.classes</param-name>
<param-value>org.keycloak.adapters.saml.jbossweb.infinispan.InfinispanSessionCacheIdMapperUpdater</param-value>
</context-param>
If the session cache of the deployment is named deployment-cache
, the cache used for SAML mapping will be named as deployment-cache.ssoCache
. The name of the cache can be overridden by a context parameter keycloak.sessionIdMapperUpdater.infinispan.cacheName
. The cache container containing the cache will be the same as the one containing the deployment session cache, but can be overridden by a context parameter keycloak.sessionIdMapperUpdater.infinispan.containerName
.
By default, the configuration of the SAML mapping cache will be derived from session cache. The configuration can be manually overridden in cache configuration section of the server just the same as other caches.
Currently, to provide reliable service, it is recommended to use replicated cache for the SAML session cache. Using distributed cache may lead to results where the SAML logout request would land to a node with no access to SAML session index to HTTP session mapping which would lead to unsuccessful logout.
3.1.8.2. Logout in cross-site scenario
The cross-site scenario only applies to WildFly 10 and higher, and EAP 7 and higher.
Special handling is needed for handling sessions that span multiple data centers. Imagine the following scenario:
- Login requests are handled within cluster in data center 1.
- Admin issues logout request for a particular SAML session, the request lands in data center 2.
The data center 2 has to log out all sessions that are present in data center 1 (and all other data centers that share HTTP sessions).
To cover this case, the SAML session cache described above needs to be replicated not only within individual clusters but across all the data centers for example via standalone Infinispan/JDG server:
- A cache has to be added to the standalone Infinispan/JDG server.
- The cache from previous item has to be added as a remote store for the respective SAML session cache.
Once remote store is found to be present on SAML session cache during deployment, it is watched for changes and the local SAML session cache is updated accordingly.
3.1.9. Obtaining assertion attributes
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
3.1.10. Error Handling
Red Hat Single Sign-On has some error handling facilities for servlet based client adapters. When an error is encountered in authentication, the client adapter will call HttpServletResponse.sendError()
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
3.1.11. Troubleshooting
The best way to troubleshoot problems is to turn on debugging for SAML in both the client adapter and Red Hat Single Sign-On Server. Using your logging framework, set the log level to DEBUG
for the org.keycloak.saml
package. Turning this on allows you to see the SAML requests and response documents being sent to and from the server.
3.1.12. Multi Tenancy
SAML offers the same functionality as OIDC for Multi Tenancy, meaning that a single target application (WAR) can be secured with multiple Red Hat Single Sign-On realms. The realms can be located on the same Red Hat Single Sign-On instance or on different instances.
To do this, the application must have multiple keycloak-saml.xml
adapter configuration files.
While you could have multiple instances of your WAR with different adapter configuration files deployed to different context-paths, this may be inconvenient and you may also want to select the realm based on something other than context-path.
Red Hat Single Sign-On makes it possible to have a custom config resolver, so you can choose which adapter config is used for each request. In SAML, the configuration is only interesting in the login processing; once the user is logged in, the session is authenticated and it does not matter if the keycloak-saml.xml
returned is different. For that reason, returning the same configuration for the same session is the correct way to go.
To achieve this, create an implementation of org.keycloak.adapters.saml.SamlConfigResolver
. The following example uses the Host
header to locate the proper configuration and load it and the associated elements from the applications’s Java classpath:
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
3.2. mod_auth_mellon Apache HTTPD Module
The mod_auth_mellon module is an Apache HTTPD plugin for SAML. If your language/environment supports using Apache HTTPD as a proxy, then you can use mod_auth_mellon to secure your web application with SAML. For more details on this module see the mod_auth_mellon GitHub repo.
To configure mod_auth_mellon you need:
- An Identity Provider (IdP) entity descriptor XML file, which describes the connection to Red Hat Single Sign-On or another SAML IdP
- An SP entity descriptor XML file, which describes the SAML connections and configuration for the application you are securing.
- A private key PEM file, which is a text file in the PEM format that defines the private key the application uses to sign documents.
- A certificate PEM file, which is a text file that defines the certificate for your application.
- mod_auth_mellon-specific Apache HTTPD module configuration.
3.2.1. Configuring mod_auth_mellon with Red Hat Single Sign-On
There are two hosts involved:
- The host on which Red Hat Single Sign-On is running, which will be referred to as $idp_host because Red Hat Single Sign-On is a SAML identity provider (IdP).
- The host on which the web application is running, which will be referred to as $sp_host. In SAML an application using an IdP is called a service provider (SP).
All of the following steps need to performed on $sp_host with root privileges.
3.2.1.1. Installing the packages
To install the necessary packages, you will need:
- Apache Web Server (httpd)
- Mellon SAML SP add-on module for Apache
- Tools to create X509 certificates
To install the necessary packages, run this command:
yum install httpd mod_auth_mellon mod_ssl openssl
3.2.1.2. Creating a configuration directory for Apache SAML
It is advisable to keep configuration files related to Apache’s use of SAML in one location.
Create a new directory named saml2 located under the Apache configuration root /etc/httpd:
mkdir /etc/httpd/saml2
3.2.1.3. Configuring the Mellon Service Provider
Configuration files for Apache add-on modules are located in the /etc/httpd/conf.d directory and have a file name extension of .conf. You need to create the /etc/httpd/conf.d/mellon.conf file and place Mellon’s configuration directives in it.
Mellon’s configuration directives can roughly be broken down into two classes of information:
- Which URLs to protect with SAML authentication
- What SAML parameters will be used when a protected URL is referenced.
Apache configuration directives typically follow a hierarchical tree structure in the URL space, which are known as locations. You need to specify one or more URL locations for Mellon to protect. You have flexibility in how you add the configuration parameters that apply to each location. You can either add all the necessary parameters to the location block or you can add Mellon parameters to a common location high up in the URL location hierarchy that specific protected locations inherit (or some combination of the two). Since it is common for an SP to operate in the same way no matter which location triggers SAML actions, the example configuration used here places common Mellon configuration directives in the root of the hierarchy and then specific locations to be protected by Mellon can be defined with minimal directives. This strategy avoids duplicating the same parameters for each protected location.
This example has just one protected location: https://$sp_host/private.
To configure the Mellon service provider, perform the following procedure.
Procedure
- Create the file /etc/httpd/conf.d/mellon.conf with this content:
<Location / >
MellonEnable info
MellonEndpointPath /mellon/
MellonSPMetadataFile /etc/httpd/saml2/mellon_metadata.xml
MellonSPPrivateKeyFile /etc/httpd/saml2/mellon.key
MellonSPCertFile /etc/httpd/saml2/mellon.crt
MellonIdPMetadataFile /etc/httpd/saml2/idp_metadata.xml
</Location>
<Location /private >
AuthType Mellon
MellonEnable auth
Require valid-user
</Location>
Some of the files referenced in the code above are created in later steps.
3.2.2. Setting the SameSite value for the cookie used by mod_auth_mellon
Browsers are planning to set the default value for the SameSite
attribute for cookies to Lax
. This setting means that cookies will be sent to applications only if the request originates in the same domain. This behavior can affect the SAML POST binding which may become non-functional. To preserve full functionality of the mod_auth_mellon module, we recommend setting the SameSite
value to None
for the cookie created by mod_auth_mellon. Not doing so may result in an inability to login using Red Hat Single Sign-On.
To set the SameSite
value to None
, add the following configuration to <Location / >
tag within your mellon.conf
file.
MellonSecureCookie On
MellonCookieSameSite none
The support for this configuration is available in the mod_auth_mellon module from version 0.16.0.
3.2.2.1. Creating the Service Provider metadata
In SAML IdPs and SPs exchange SAML metadata, which is in XML format. The schema for the metadata is a standard, thus assuring participating SAML entities can consume each other’s metadata. You need:
- Metadata for the IdP that the SP utilizes
- Metadata describing the SP provided to the IdP
One of the components of SAML metadata is X509 certificates. These certificates are used for two purposes:
- Sign SAML messages so the receiving end can prove the message originated from the expected party.
- Encrypt the message during transport (seldom used because SAML messages typically occur on TLS-protected transports)
You can use your own certificates if you already have a Certificate Authority (CA) or you can generate a self-signed certificate. For simplicity in this example a self-signed certificate is used.
Because Mellon’s SP metadata must reflect the capabilities of the installed version of mod_auth_mellon, must be valid SP metadata XML, and must contain an X509 certificate (whose creation can be obtuse unless you are familiar with X509 certificate generation) the most expedient way to produce the SP metadata is to use a tool included in the mod_auth_mellon package (mellon_create_metadata.sh). The generated metadata can always be edited later because it is a text file. The tool also creates your X509 key and certificate.
SAML IdPs and SPs identify themselves using a unique name known as an EntityID. To use the Mellon metadata creation tool you need:
- The EntityID, which is typically the URL of the SP, and often the URL of the SP where the SP metadata can be retrieved
- The URL where SAML messages for the SP will be consumed, which Mellon calls the MellonEndPointPath.
To create the SP metadata, perform the following procedure.
Procedure
Create a few helper shell variables:
fqdn=`hostname` mellon_endpoint_url="https://${fqdn}/mellon" mellon_entity_id="${mellon_endpoint_url}/metadata" file_prefix="$(echo "$mellon_entity_id" | sed 's/[^A-Za-z.]/_/g' | sed 's/__*/_/g')"
Invoke the Mellon metadata creation tool by running this command:
/usr/libexec/mod_auth_mellon/mellon_create_metadata.sh $mellon_entity_id $mellon_endpoint_url
Move the generated files to their destination (referenced in the /etc/httpd/conf.d/mellon.conf file created above):
mv ${file_prefix}.cert /etc/httpd/saml2/mellon.crt mv ${file_prefix}.key /etc/httpd/saml2/mellon.key mv ${file_prefix}.xml /etc/httpd/saml2/mellon_metadata.xml
3.2.2.2. Adding the Mellon Service Provider to the Red Hat Single Sign-On Identity Provider
Assumption: The Red Hat Single Sign-On IdP has already been installed on the $idp_host.
Red Hat Single Sign-On supports multiple tenancy where all users, clients, and so on are grouped in what is called a realm. Each realm is independent of other realms. You can use an existing realm in your Red Hat Single Sign-On, but this example shows how to create a new realm called test_realm and use that realm.
All these operations are performed using the Red Hat Single Sign-On Admin Console. You must have the admin username and password for $idp_host to perform the following procedure.
Procedure
Open the Admin Console and log on by entering the admin username and password.
After logging into the Admin Console, there will be an existing realm. When Red Hat Single Sign-On is first set up a root realm, master, is created by default. Any previously created realms are listed in the upper left corner of the Admin Console in a drop-down list.
- From the realm drop-down list select Add realm.
-
In the Name field type
test_realm
and click Create.
3.2.2.2.1. Adding the Mellon Service Provider as a client of the realm
In Red Hat Single Sign-On SAML SPs are known as clients. To add the SP we must be in the Clients section of the realm.
- Click the Clients menu item on the left and click Create in the upper right corner to create a new client.
3.2.2.2.2. Adding the Mellon SP client
To add the Mellon SP client, perform the following procedure.
Procedure
- Set the client protocol to SAML.
- From the Client Protocol drop down list, select saml.
Provide the Mellon SP metadata file created above (/etc/httpd/saml2/mellon_metadata.xml).
Depending on where your browser is running you might have to copy the SP metadata from $sp_host to the machine on which your browser is running so the browser can find the file.
- Click Save.
3.2.2.2.3. Editing the Mellon SP client
Use this procedure to set important client configuration parameters.
Procedure
- Ensure "Force POST Binding" is On.
- Add paosResponse to the Valid Redirect URIs list:
- Copy the postResponse URL in "Valid Redirect URIs" and paste it into the empty add text fields just below the "+".
- Change "postResponse" to "paosResponse". (The paosResponse URL is needed for SAML ECP.)
- Click Save at the bottom.
Many SAML SPs determine authorization based on a user’s membership in a group. The Red Hat Single Sign-On IdP can manage user group information but it does not supply the user’s groups unless the IdP is configured to supply it as a SAML attribute.
Perform the following procedure to configure the IdP to supply the user’s groups as as a SAML attribute.
Procedure
- Click the Mappers tab of the client.
- In the upper right corner of the Mappers page, click Create.
- From the Mapper Type drop-down list select Group list.
- Set Name to "group list".
- Set the SAML attribute name to "groups".
- Click Save.
The remaining steps are performed on $sp_host.
3.2.2.2.4. Retrieving the Identity Provider metadata
Now that you have created the realm on the IdP you need to retrieve the IdP metadata associated with it so the Mellon SP recognizes it. In the /etc/httpd/conf.d/mellon.conf file created previously, the MellonIdPMetadataFile is specified as /etc/httpd/saml2/idp_metadata.xml but until now that file has not existed on $sp_host.
Use this procedure to retrieve that file from the IdP.
Procedure
Use this command, substituting with the correct value for $idp_host:
curl -k -o /etc/httpd/saml2/idp_metadata.xml \ https://$idp_host/auth/realms/test_realm/protocol/saml/descriptor
Mellon is now fully configured.
To run a syntax check for Apache configuration files, use this command:
apachectl configtest
NoteConfigtest is equivalent to the -t argument to apachectl. If the configuration test shows any errors, correct them before proceeding.
Restart the Apache server:
systemctl restart httpd.service
You have now set up both Red Hat Single Sign-On as a SAML IdP in the test_realm and mod_auth_mellon as SAML SP protecting the URL $sp_host/protected (and everything beneath it) by authenticating against the $idp_host
IdP.
