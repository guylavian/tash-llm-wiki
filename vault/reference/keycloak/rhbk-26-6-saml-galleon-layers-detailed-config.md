---
title: "Chapter 7. Red Hat build of Keycloak SAML Galleon feature pack detailed configuration - Red Hat build of Keycloak 26.6 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-saml-galleon-layers-detailed-config
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/securing_applications_and_services_guide/saml-galleon-layers-detailed-config-
guide: securing_applications_and_services_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Review this detailed list of elements for the `keycloak-saml.xml` configuration file. This chapter contains the detailed list of elements for the keycloak-saml.xml configuration file used by the Red Hat build of Keycloak SAML Galleon feature pack. 7.1. SP element Here is the explanation of the SP element attributes: ... entityID This is the identifier for this client. The IdP needs this value to d…"
---

# Chapter 7. Red Hat build of Keycloak SAML Galleon feature pack detailed configuration - Red Hat build of Keycloak 26.6 Securing Applications and Services Guide

Chapter 7. Red Hat build of Keycloak SAML Galleon feature pack detailed configuration
Review this detailed list of elements for the `keycloak-saml.xml` configuration file.
This chapter contains the detailed list of elements for the keycloak-saml.xml
configuration file used by the Red Hat build of Keycloak SAML Galleon feature pack.
7.1. SP element
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
This should be set to true if your application serves both a web application and web services (for example SOAP or REST). It allows you to redirect unauthenticated users of the web application to the Red Hat build of Keycloak login page, but send an HTTP
401
status code to unauthenticated SOAP or REST clients instead as they would not understand a redirect to the login page. Red Hat build of Keycloak auto-detects SOAP or REST clients based on typical headers likeX-Requested-With
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
inside the principal. This is specially useful when re-playing a signed assertion. The returned document is the one that was generated parsing the SAML response received by the Red Hat build of Keycloak server. This setting is OPTIONAL and its default value is false (the document is not saved inside the principal).
7.2. Service Provider keys and key elements
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
7.2.1. KeyStore element
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
7.2.2. Key PEMS
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
7.3. SP PrincipalNameMapping element
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
7.4. RoleIdentifiers element
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
7.5. RoleMappingsProvider element
The RoleMappingsProvider
is an optional element that allows for the specification of the id and configuration of the org.keycloak.adapters.saml.RoleMappingsProvider
SPI implementation that is to be used by the SAML adapter.
When Red Hat build of Keycloak is used as the IDP, it is possible to use the built-in role mappers to map any roles before adding them to the SAML assertion. However, the SAML adapters can be used to send SAML requests to third party IDPs and in this case it might be necessary to map the roles extracted from the assertion into a different set of roles as required by the SP. The RoleMappingsProvider
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
7.5.1. Properties Based role mappings provider
Red Hat build of Keycloak includes a RoleMappingsProvider
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
file can contain both roles and principals as keys, and a list of zero or more roles separated by comma as values. When invoked, the implementation iterates through the set of roles that were extracted from the assertion and checks, for each role, if a mapping exists. If the role maps to an empty role, it is discarded. If it maps to a set of one or more different roles, then these roles are set in the result set. If no mapping is found for the role then it is included as is in the result set.
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
7.6. IDP Element
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
. Note thatSHA1
based algorithms are deprecated and can be removed in the future. We recommend the use of some more secure algorithm instead of*_SHA1
. Also, with*_SHA1
algorithms, verifying signatures do not work if the SAML server (usually Red Hat build of Keycloak) runs on Java 17 or higher. - signatureCanonicalizationMethod
-
This is the signature canonicalization method that the IDP expects signed documents to use. This setting is OPTIONAL. The default value is
http://www.w3.org/2001/10/xml-exc-c14n#
and should be good for most IDPs. - metadataUrl
- The URL used to retrieve the IDP metadata, currently this is only used to pick up signing and encryption keys periodically which allow cycling of these keys on the IDP without manual changes on the SP side.
7.7. IDP AllowedClockSkew sub element
The AllowedClockSkew
optional sub element defines the allowed clock skew between IDP and SP. The default value is 0.
<AllowedClockSkew unit="MILLISECONDS">3500</AllowedClockSkew>
- unit
-
It is possible to define the time unit attached to the value for this element. Allowed values are MICROSECONDS, MILLISECONDS, MINUTES, NANOSECONDS and SECONDS. This is OPTIONAL. The default value is
SECONDS
.
7.8. IDP SingleSignOnService sub element
The SingleSignOnService
sub element defines the login SAML endpoint of the IDP. The client adapter will send requests to the IDP formatted via the settings within this element when it wants to log in.
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
Should the client expect the IDP to sign the assertion response document sent back from an authn request? This setting OPTIONAL. Defaults to whatever the IDP
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
7.9. IDP SingleLogoutService sub element
The SingleLogoutService
sub element defines the logout SAML endpoint of the IDP. The client adapter will send requests to the IDP formatted via the settings within this element when it wants to log out.
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
7.10. IDP Keys sub element
The Keys sub element of IDP is only used to define the certificate or public key to use to verify documents signed by the IDP. It is defined in the same way as the SP’s Keys element. But again, you only have to define one certificate or public key reference. Note that, if both IDP and SP are realized by Red Hat build of Keycloak server and adapter, respectively, there is no need to specify the keys for signature validation, see below.
It is possible to configure SP to obtain public keys for IDP signature validation from published certificates automatically, provided both SP and IDP are implemented by Red Hat build of Keycloak. This is done by removing all declarations of signature validation keys in Keys sub element. If the Keys sub element would then remain empty, it can be omitted completely. The keys are then automatically obtained by SP from SAML descriptor, location of which is derived from SAML endpoint URL specified in the IDP SingleSignOnService sub element. Settings of the HTTP client that is used for SAML descriptor retrieval usually needs no additional configuration, however it can be configured in the IDP HttpClient sub element.
It is also possible to specify multiple keys for signature verification. This is done by declaring multiple Key elements within Keys sub element that have signing
attribute set to true
. This is useful for example in situation when the IDP signing keys are rotated: There is usually a transition period when new SAML protocol messages and assertions are signed with the new key but those signed by previous key should still be accepted.
It is not possible to configure Red Hat build of Keycloak to both obtain the keys for signature verification automatically and define additional static signature verification keys.
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
7.11. IDP HttpClient sub element
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
This config option defines how many connections to the Red Hat build of Keycloak server should be pooled. This is OPTIONAL. The default value is
10
. - disableTrustManager
-
If the Red Hat build of Keycloak server requires HTTPS and this config option is set to
true
you do not have to specify a truststore. This setting should only be used during development and never in production as it will disable verification of SSL certificates. This is OPTIONAL. The default value isfalse
. - allowAnyHostname
-
If the Red Hat build of Keycloak server requires HTTPS and this config option is set to
true
the Red Hat build of Keycloak server’s certificate is validated via the truststore, but host name validation is not done. This setting should only be used during development and never in production as it will partly disable verification of SSL certificates. This setting may be useful in test environments. This is OPTIONAL. The default value isfalse
. - truststore
-
The value is the file path to a truststore file. If you prefix the path with
classpath:
, then the truststore will be obtained from the deployment’s classpath instead. Used for outgoing HTTPS communications to the Red Hat build of Keycloak server. Client making HTTPS requests need a way to verify the host of the server they are talking to. This is what the truststore does. The keystore contains one or more trusted host certificates or certificate authorities. You can create this truststore by extracting the public certificate of the Red Hat build of Keycloak server’s SSL keystore. This is REQUIRED unlessdisableTrustManager
istrue
. - truststorePassword
-
Password for the truststore. This is REQUIRED if
truststore
is set and the truststore requires a password. - clientKeystore
- This is the file path to a keystore file. This keystore contains client certificate for two-way SSL when the adapter makes HTTPS requests to the Red Hat build of Keycloak server. This is OPTIONAL.
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
