---
title: "Chapter 2. Using OpenID Connect to secure applications and services - Red Hat Single Sign-On 7.6 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhsso-7-6-oidc
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html/securing_applications_and_services_guide/oidc
guide: securing_applications_and_services_guide
version: 7.6
family: rhsso
documentKind: "Documentation"
---

# Chapter 2. Using OpenID Connect to secure applications and services - Red Hat Single Sign-On 7.6 Securing Applications and Services Guide

Chapter 2. Using OpenID Connect to secure applications and services
This section describes how you can secure applications and services with OpenID Connect using either Red Hat Single Sign-On adapters or generic OpenID Connect Relying Party libraries.
2.1. Java adapters
Red Hat Single Sign-On comes with a range of different adapters for Java application. Selecting the correct adapter depends on the target platform.
All Java adapters share a set of common configuration options described in the Java Adapters Config chapter.
2.1.1. Java adapter configuration
Each Java adapter supported by Red Hat Single Sign-On can be configured by a simple JSON file. This is what one might look like:
{
"realm" : "demo",
"resource" : "customer-portal",
"realm-public-key" : "MIGfMA0GCSqGSIb3D...31LwIDAQAB",
"auth-server-url" : "https://localhost:8443/auth",
"ssl-required" : "external",
"use-resource-role-mappings" : false,
"enable-cors" : true,
"cors-max-age" : 1000,
"cors-allowed-methods" : "POST, PUT, DELETE, GET",
"cors-exposed-headers" : "WWW-Authenticate, My-custom-exposed-Header",
"bearer-only" : false,
"enable-basic-auth" : false,
"expose-token" : true,
"verify-token-audience" : true,
"credentials" : {
"secret" : "234234-234234-234234"
},
"connection-pool-size" : 20,
"socket-timeout-millis" : 5000,
"connection-timeout-millis" : 6000,
"connection-ttl-millis" : 500,
"disable-trust-manager" : false,
"allow-any-hostname" : false,
"truststore" : "path/to/truststore.jks",
"truststore-password" : "geheim",
"client-keystore" : "path/to/client-keystore.jks",
"client-keystore-password" : "geheim",
"client-key-password" : "geheim",
"token-minimum-time-to-live" : 10,
"min-time-between-jwks-requests" : 10,
"public-key-cache-ttl" : 86400,
"redirect-rewrite-rules" : {
"^/wsmaster/api/(.*)$" : "/api/$1"
}
}
You can use ${…}
enclosure for system property replacement. For example ${jboss.server.config.dir}
would be replaced by /path/to/Red Hat Single Sign-On
. Replacement of environment variables is also supported via the env
prefix, for example ${env.MY_ENVIRONMENT_VARIABLE}
.
The initial config file can be obtained from the admin console. This can be done by opening the admin console, select Clients
from the menu and clicking on the corresponding client. Once the page for the client is opened click on the Installation
tab and select Keycloak OIDC JSON
.
Here is a description of each configuration option:
- realm
- Name of the realm. This is REQUIRED.
- resource
- The client-id of the application. Each application has a client-id that is used to identify the application. This is REQUIRED.
- realm-public-key
- PEM format of the realm public key. You can obtain this from the Admin Console. This is OPTIONAL and it’s not recommended to set it. If not set, the adapter will download this from Red Hat Single Sign-On and it will always re-download it when needed (eg. Red Hat Single Sign-On rotates its keys). However if realm-public-key is set, then adapter will never download new keys from Red Hat Single Sign-On, so when Red Hat Single Sign-On rotate it’s keys, adapter will break.
- auth-server-url
-
The base URL of the Red Hat Single Sign-On server. All other Red Hat Single Sign-On pages and REST service endpoints are derived from this. It is usually of the form
https://host:port/auth
. This is REQUIRED. - ssl-required
-
Ensures that all communication to and from the Red Hat Single Sign-On server is over HTTPS. In production this should be set to
all
. This is OPTIONAL. The default value is external meaning that HTTPS is required by default for external requests. Valid values are 'all', 'external' and 'none'. - confidential-port
- The confidential port used by the Red Hat Single Sign-On server for secure connections over SSL/TLS. This is OPTIONAL. The default value is 8443.
- use-resource-role-mappings
- If set to true, the adapter will look inside the token for application level role mappings for the user. If false, it will look at the realm level for user role mappings. This is OPTIONAL. The default value is false.
- public-client
- If set to true, the adapter will not send credentials for the client to Red Hat Single Sign-On. This is OPTIONAL. The default value is false.
- enable-cors
- This enables CORS support. It will handle CORS preflight requests. It will also look into the access token to determine valid origins. This is OPTIONAL. The default value is false.
- cors-max-age
-
If CORS is enabled, this sets the value of the
Access-Control-Max-Age
header. This is OPTIONAL. If not set, this header is not returned in CORS responses. - cors-allowed-methods
-
If CORS is enabled, this sets the value of the
Access-Control-Allow-Methods
header. This should be a comma-separated string. This is OPTIONAL. If not set, this header is not returned in CORS responses. - cors-allowed-headers
-
If CORS is enabled, this sets the value of the
Access-Control-Allow-Headers
header. This should be a comma-separated string. This is OPTIONAL. If not set, this header is not returned in CORS responses. - cors-exposed-headers
-
If CORS is enabled, this sets the value of the
Access-Control-Expose-Headers
header. This should be a comma-separated string. This is OPTIONAL. If not set, this header is not returned in CORS responses. - bearer-only
- This should be set to true for services. If enabled the adapter will not attempt to authenticate users, but only verify bearer tokens. This is OPTIONAL. The default value is false.
- autodetect-bearer-only
-
This should be set to true if your application serves both a web application and web services (for example SOAP or REST). It allows you to redirect unauthenticated users of the web application to the Red Hat Single Sign-On login page, but send an HTTP
401
status code to unauthenticated SOAP or REST clients instead as they would not understand a redirect to the login page. Red Hat Single Sign-On auto-detects SOAP or REST clients based on typical headers likeX-Requested-With
,SOAPAction
orAccept
. The default value is false. - enable-basic-auth
- This tells the adapter to also support basic authentication. If this option is enabled, then secret must also be provided. This is OPTIONAL. The default value is false.
- expose-token
-
If
true
, an authenticated browser client (via a JavaScript HTTP invocation) can obtain the signed access token via the URLroot/k_query_bearer_token
. This is OPTIONAL. The default value is false. - credentials
- Specify the credentials of the application. This is an object notation where the key is the credential type and the value is the value of the credential type. Currently password and jwt is supported. This is REQUIRED only for clients with 'Confidential' access type.
- connection-pool-size
-
This config option defines how many connections to the Red Hat Single Sign-On server should be pooled. This is OPTIONAL. The default value is
20
. - socket-timeout-millis
-
Timeout for socket waiting for data after establishing the connection in milliseconds. Maximum time of inactivity between two data packets. A timeout value of zero is interpreted as an infinite timeout. A negative value is interpreted as undefined (system default if applicable). The default value is
-1
. This is OPTIONAL. - connection-timeout-millis
-
Timeout for establishing the connection with the remote host in milliseconds. A timeout value of zero is interpreted as an infinite timeout. A negative value is interpreted as undefined (system default if applicable). The default value is
-1
. This is OPTIONAL. - connection-ttl-millis
-
Connection time-to-live for client in milliseconds. A value less than or equal to zero is interpreted as an infinite value. The default value is
-1
. This is OPTIONAL. - disable-trust-manager
-
If the Red Hat Single Sign-On server requires HTTPS and this config option is set to
true
you do not have to specify a truststore. This setting should only be used during development and never in production as it will disable verification of SSL certificates. This is OPTIONAL. The default value isfalse
. - allow-any-hostname
-
If the Red Hat Single Sign-On server requires HTTPS and this config option is set to
true
the Red Hat Single Sign-On server’s certificate is validated via the truststore, but host name validation is not done. This setting should only be used during development and never in production as it will disable verification of SSL certificates. This seting may be useful in test environments This is OPTIONAL. The default value isfalse
. - proxy-url
- The URL for the HTTP proxy if one is used.
- truststore
-
The value is the file path to a truststore file. If you prefix the path with
classpath:
, then the truststore will be obtained from the deployment’s classpath instead. Used for outgoing HTTPS communications to the Red Hat Single Sign-On server. Client making HTTPS requests need a way to verify the host of the server they are talking to. This is what the trustore does. The keystore contains one or more trusted host certificates or certificate authorities. You can create this truststore by extracting the public certificate of the Red Hat Single Sign-On server’s SSL keystore. This is REQUIRED unlessssl-required
isnone
ordisable-trust-manager
istrue
. - truststore-password
-
Password for the truststore. This is REQUIRED if
truststore
is set and the truststore requires a password. - client-keystore
- This is the file path to a keystore file. This keystore contains client certificate for two-way SSL when the adapter makes HTTPS requests to the Red Hat Single Sign-On server. This is OPTIONAL.
- client-keystore-password
-
Password for the client keystore. This is REQUIRED if
client-keystore
is set. - client-key-password
-
Password for the client’s key. This is REQUIRED if
client-keystore
is set. - always-refresh-token
- If true, the adapter will refresh token in every request. Warning - when enabled this will result in a request to Red Hat Single Sign-On for every request to your application.
- register-node-at-startup
- If true, then adapter will send registration request to Red Hat Single Sign-On. It’s false by default and useful only when application is clustered. See Application Clustering for details
- register-node-period
- Period for re-registration adapter to Red Hat Single Sign-On. Useful when application is clustered. See Application Clustering for details
- token-store
- Possible values are session and cookie. Default is session, which means that adapter stores account info in HTTP Session. Alternative cookie means storage of info in cookie. See Application Clustering for details
- token-cookie-path
- When using a cookie store, this option sets the path of the cookie used to store account info. If it’s a relative path, then it is assumed that the application is running in a context root, and is interpreted relative to that context root. If it’s an absolute path, then the absolute path is used to set the cookie path. Defaults to use paths relative to the context root.
- principal-attribute
-
OpenID Connect ID Token attribute to populate the UserPrincipal name with. If token attribute is null, defaults to
sub
. Possible values aresub
,preferred_username
,email
,name
,nickname
,given_name
,family_name
. - turn-off-change-session-id-on-login
- The session id is changed by default on a successful login on some platforms to plug a security attack vector. Change this to true if you want to turn this off This is OPTIONAL. The default value is false.
- token-minimum-time-to-live
-
Amount of time, in seconds, to preemptively refresh an active access token with the Red Hat Single Sign-On server before it expires. This is especially useful when the access token is sent to another REST client where it could expire before being evaluated. This value should never exceed the realm’s access token lifespan. This is OPTIONAL. The default value is
0
seconds, so adapter will refresh access token just if it’s expired. - min-time-between-jwks-requests
-
Amount of time, in seconds, specifying minimum interval between two requests to Red Hat Single Sign-On to retrieve new public keys. It is 10 seconds by default. Adapter will always try to download new public key when it recognize token with unknown
kid
. However it won’t try it more than once per 10 seconds (by default). This is to avoid DoS when attacker sends lots of tokens with badkid
forcing adapter to send lots of requests to Red Hat Single Sign-On. - public-key-cache-ttl
-
Amount of time, in seconds, specifying maximum interval between two requests to Red Hat Single Sign-On to retrieve new public keys. It is 86400 seconds (1 day) by default. Adapter will always try to download new public key when it recognize token with unknown
kid
. If it recognize token with knownkid
, it will just use the public key downloaded previously. However at least once per this configured interval (1 day by default) will be new public key always downloaded even if thekid
of token is already known. - ignore-oauth-query-parameter
-
Defaults to
false
, if set totrue
will turn off processing of theaccess_token
query parameter for bearer token processing. Users will not be able to authenticate if they only pass in anaccess_token
- redirect-rewrite-rules
-
If needed, specify the Redirect URI rewrite rule. This is an object notation where the key is the regular expression to which the Redirect URI is to be matched and the value is the replacement String.
$
character can be used for backreferences in the replacement String. - verify-token-audience
-
If set to
true
, then during authentication with the bearer token, the adapter will verify whether the token contains this client name (resource) as an audience. The option is especially useful for services, which primarily serve requests authenticated by the bearer token. This is set tofalse
by default, however for improved security, it is recommended to enable this. See Audience Support for more details about audience support.
2.1.2. JBoss EAP adapter
You can install this adapter from a ZIP file or from an RPM.
2.1.3. Installing JBOSS EAP adapters from a ZIP file
To be able to secure WAR apps deployed on JBoss EAP, you must install and configure the Red Hat Single Sign-On adapter subsystem. You then have two options to secure your WARs.
- You can provide an adapter config file in your WAR and change the auth-method to KEYCLOAK within web.xml.
-
Alternatively, you do not have to modify your WAR at all and you can secure it via the Red Hat Single Sign-On adapter subsystem configuration in the configuration file, such as
standalone.xml
.
Both methods are described in this section.
Adapters are available as a separate archive depending on what server version you are using.
Procedure
Install the adapter that applies to your application server from the Sotware Downloads site.
Install on JBoss EAP 7:
$ cd $EAP_HOME $ unzip rh-sso-7.6.12-eap7-adapter.zip
This ZIP archive contains JBoss Modules specific to the Red Hat Single Sign-On adapter. It also contains JBoss CLI scripts to configure the adapter subsystem.
To configure the adapter subsystem, execute the appropriate command.
Install on JBoss EAP 7.1 or newer if the server is not running.
$ ./bin/jboss-cli.sh --file=bin/adapter-elytron-install-offline.cli
NoteThe offline script is not available for JBoss EAP 6.4
Install on JBoss EAP 7.1 or newer if the server is running.
$ ./bin/jboss-cli.sh -c --file=bin/adapter-elytron-install.cli
NoteIt is possible to use the legacy non-Elytron adapter on JBoss EAP 7.1 or newer as well, meaning you can use
adapter-install-offline.cli
NoteEAP supports OpenJDK 17 and Oracle JDK 17 since 7.4.CP7 and 7.4.CP8 respectively. Note that the new java version makes the elytron variant compulsory, so do not use the legacy adapter with JDK 17. Also, after running the adapter CLI file, execute the
enable-elytron-se17.cli
script provided by EAP. Both scripts are necessary to configure the elytron adapter and remove the incompatible EAP subsystems. For more details, see this Security Configuration Changes article.Install on JBoss EAP 6.4
$ ./bin/jboss-cli.sh -c --file=bin/adapter-install.cli
2.1.3.1. JBoss SSO
JBoss EAP has built-in support for single sign-on for web applications deployed to the same JBoss EAP instance. This should not be enabled when using Red Hat Single Sign-On.
2.1.3.2. Securing a WAR
This section describes how to secure a WAR directly by adding configuration and editing files within your WAR package.
Procedure
Create a
keycloak.json
adapter configuration file within theWEB-INF
directory of your WAR.The format of this configuration file is described in the Java adapter configuration section.
-
Set the
auth-method
toKEYCLOAK
inweb.xml
. Use standard servlet security to specify role-base constraints on your URLs.
Here’s an example:
<web-app xmlns="http://java.sun.com/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd" version="3.0"> <module-name>application</module-name> <security-constraint> <web-resource-collection> <web-resource-name>Admins</web-resource-name> <url-pattern>/admin/*</url-pattern> </web-resource-collection> <auth-constraint> <role-name>admin</role-name> </auth-constraint> <user-data-constraint> <transport-guarantee>CONFIDENTIAL</transport-guarantee> </user-data-constraint> </security-constraint> <security-constraint> <web-resource-collection> <web-resource-name>Customers</web-resource-name> <url-pattern>/customers/*</url-pattern> </web-resource-collection> <auth-constraint> <role-name>user</role-name> </auth-constraint> <user-data-constraint> <transport-guarantee>CONFIDENTIAL</transport-guarantee> </user-data-constraint> </security-constraint> <login-config> <auth-method>KEYCLOAK</auth-method> <realm-name>this is ignored currently</realm-name> </login-config> <security-role> <role-name>admin</role-name> </security-role> <security-role> <role-name>user</role-name> </security-role> </web-app>
2.1.3.3. Securing WARs via adapter subsystem
You do not have to modify your WAR to secure it with Red Hat Single Sign-On. Instead you can externally secure it via the Red Hat Single Sign-On Adapter Subsystem. While you don’t have to specify KEYCLOAK as an auth-method
, you still have to define the security-constraints
in web.xml
. You do not, however, have to create a WEB-INF/keycloak.json
file. The metadata is instead defined within server configuration (standalone.xml
) in the Red Hat Single Sign-On subsystem definition.
<extensions>
<extension module="org.keycloak.keycloak-adapter-subsystem"/>
</extensions>
<profile>
<subsystem xmlns="urn:jboss:domain:keycloak:1.1">
<secure-deployment name="WAR MODULE NAME.war">
<realm>demo</realm>
<auth-server-url>http://localhost:8081/auth</auth-server-url>
<ssl-required>external</ssl-required>
<resource>customer-portal</resource>
<credential name="secret">password</credential>
</secure-deployment>
</subsystem>
</profile>
The secure-deployment
name
attribute identifies the WAR you want to secure. Its value is the module-name
defined in web.xml
with .war
appended. The rest of the configuration corresponds pretty much one to one with the keycloak.json
configuration options defined in Java adapter configuration.
The exception is the credential
element.
To make it easier for you, you can go to the Red Hat Single Sign-On Admin Console and go to the Client/Installation tab of the application this WAR is aligned with. It provides an example XML file you can cut and paste.
If you have multiple deployments secured by the same realm you can share the realm configuration in a separate element. For example:
<subsystem xmlns="urn:jboss:domain:keycloak:1.1">
<realm name="demo">
<auth-server-url>http://localhost:8080/auth</auth-server-url>
<ssl-required>external</ssl-required>
</realm>
<secure-deployment name="customer-portal.war">
<realm>demo</realm>
<resource>customer-portal</resource>
<credential name="secret">password</credential>
</secure-deployment>
<secure-deployment name="product-portal.war">
<realm>demo</realm>
<resource>product-portal</resource>
<credential name="secret">password</credential>
</secure-deployment>
<secure-deployment name="database.war">
<realm>demo</realm>
<resource>database-service</resource>
<bearer-only>true</bearer-only>
</secure-deployment>
</subsystem>
2.1.3.4. Security domain
The security context is propagated to the EJB tier automatically.
2.1.4. Installing JBoss EAP 7 adapters from an RPM
With Red Hat Enterprise Linux 7, the term channel was replaced with the term repository. In these instructions only the term repository is used.
Prerequisites
You must subscribe to the JBoss EAP 7.4 repository before you can install the JBoss EAP 7 adapters from an RPM.
- Ensure that your Red Hat Enterprise Linux system is registered to your account using Red Hat Subscription Manager. For more information see the Red Hat Subscription Management documentation.
If you are already subscribed to another JBoss EAP repository, you must unsubscribe from that repository first.
For Red Hat Enterprise Linux 6, 7: Using Red Hat Subscription Manager, subscribe to the JBoss EAP 7.4 repository using the following command. Replace <RHEL_VERSION> with either 6 or 7 depending on your Red Hat Enterprise Linux version.
$ sudo subscription-manager repos --enable=jb-eap-7-for-rhel-<RHEL_VERSION>-server-rpms
For Red Hat Enterprise Linux 8: Using Red Hat Subscription Manager, subscribe to the JBoss EAP 7.4 repository using the following command:
$ sudo subscription-manager repos --enable=jb-eap-7.4-for-rhel-8-x86_64-rpms --enable=rhel-8-for-x86_64-baseos-rpms --enable=rhel-8-for-x86_64-appstream-rpms
Procedure
Install the JBoss EAP 7 adapters for OIDC based on your version of Red Hat Enterprise Linux.
Install on Red Hat Enterprise Linux 6, 7:
$ sudo yum install eap7-keycloak-adapter-sso7_6
Install on Red Hat Enterprise Linux 8:
$ sudo dnf install eap7-keycloak-adapter-sso7_6
NoteThe default EAP_HOME path for the RPM installation is /opt/rh/eap7/root/usr/share/wildfly.
Run the installation script for the OIDC module.
$ $EAP_HOME/bin/jboss-cli.sh -c --file=$EAP_HOME/bin/adapter-install.cli
Your installation is complete.
2.1.5. Installing JBoss EAP 6 adapters from an RPM
With Red Hat Enterprise Linux 7, the term channel was replaced with the term repository. In these instructions only the term repository is used.
You must subscribe to the JBoss EAP 6 repository before you can install the EAP 6 adapters from an RPM.
Prerequisites
- Ensure that your Red Hat Enterprise Linux system is registered to your account using Red Hat Subscription Manager. For more information see the Red Hat Subscription Management documentation.
If you are already subscribed to another JBoss EAP repository, you must unsubscribe from that repository first.
Using Red Hat Subscription Manager, subscribe to the JBoss EAP 6 repository using the following command. Replace <RHEL_VERSION> with either 6 or 7 depending on your Red Hat Enterprise Linux version.
$ sudo subscription-manager repos --enable=jb-eap-6-for-rhel-<RHEL_VERSION>-server-rpms
Procedure
Install the EAP 6 adapters for OIDC using the following command:
$ sudo yum install keycloak-adapter-sso7_6-eap6
NoteThe default EAP_HOME path for the RPM installation is /opt/rh/eap6/root/usr/share/wildfly.
Run the installation script for the OIDC module.
$ $EAP_HOME/bin/jboss-cli.sh -c --file=$EAP_HOME/bin/adapter-install.cli
Your installation is complete.
2.1.6. JBoss Fuse 6 adapter
Red Hat Single Sign-On supports securing your web applications running inside JBoss Fuse 6.
The only supported version of Fuse 6 is the latest release. If you use earlier versions of Fuse 6, it is possible that some functions will not work correctly. In particular, the Hawtio integration will not work with earlier versions of Fuse 6.
Security for the following items is supported for Fuse:
- Classic WAR applications deployed on Fuse with Pax Web War Extender
- Servlets deployed on Fuse as OSGI services with Pax Web Whiteboard Extender
- Apache Camel Jetty endpoints running with the Camel Jetty component
- Apache CXF endpoints running on their own separate Jetty engine
- Apache CXF endpoints running on the default engine provided by the CXF servlet
- SSH and JMX admin access
- Hawtio administration console
2.1.6.1. Securing your web applications inside Fuse 6
You must first install the Red Hat Single Sign-On Karaf feature. Next you will need to perform the steps according to the type of application you want to secure. All referenced web applications require injecting the Red Hat Single Sign-On Jetty authenticator into the underlying Jetty server. The steps to achieve this depend on the application type. The details are described below.
2.1.6.2. Installing the Keycloak feature
You must first install the keycloak
feature in the JBoss Fuse environment. The keycloak feature includes the Fuse adapter and all third-party dependencies. You can install it either from the Maven repository or from an archive.
2.1.6.2.1. Installing from the Maven repository
Prerequisites
- You must be online and have access to the Maven repository.
For Red Hat Single Sign-On, configure a proper Maven repository, so you can install the artifacts. For more information see the JBoss Enterprise Maven repository page.
Assuming the Maven repository is https://maven.repository.redhat.com/ga/, add the following to the
$FUSE_HOME/etc/org.ops4j.pax.url.mvn.cfg
file and add the repository to the list of supported repositories. For example:org.ops4j.pax.url.mvn.repositories= \ https://maven.repository.redhat.com/ga/@id=redhat.product.repo http://repo1.maven.org/maven2@id=maven.central.repo, \ ...
Procedure
- Start JBoss Fuse 6.3.0 Rollup 12
In the Karaf terminal type:
features:addurl mvn:org.keycloak/keycloak-osgi-features/18.0.19.redhat-00001/xml/features features:install keycloak
You might also need to install the Jetty 9 feature:
features:install keycloak-jetty9-adapter
Ensure that the features were installed:
features:list | grep keycloak
2.1.6.2.2. Installing from the ZIP bundle
This installation option is useful if you are offline or do not want to use Maven to obtain the JAR files and other artifacts.
Procedure
- Download the Red Hat Single Sign-On Fuse adapter ZIP archive from the Sotware Downloads site.
Unzip it into the root directory of JBoss Fuse. The dependencies are then installed under the
system
directory. You can overwrite all existing jar files.Use this for JBoss Fuse 6.3.0 Rollup 12:
cd /path-to-fuse/jboss-fuse-6.3.0.redhat-254 unzip -q /path-to-adapter-zip/rh-sso-7.6.12-fuse-adapter.zip
Start Fuse and run these commands in the fuse/karaf terminal:
features:addurl mvn:org.keycloak/keycloak-osgi-features/18.0.19.redhat-00001/xml/features features:install keycloak
-
Install the corresponding Jetty adapter. Since the artifacts are available directly in the JBoss Fuse
system
directory, you do not need to use the Maven repository.
2.1.6.3. Securing a Classic WAR application
Procedure
In the
/WEB-INF/web.xml
file, declare the necessary:- security constraints in the <security-constraint> element
- login configuration in the <login-config> element
security roles in the <security-role> element.
For example:
<?xml version="1.0" encoding="UTF-8"?> <web-app xmlns="http://java.sun.com/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd" version="3.0"> <module-name>customer-portal</module-name> <welcome-file-list> <welcome-file>index.html</welcome-file> </welcome-file-list> <security-constraint> <web-resource-collection> <web-resource-name>Customers</web-resource-name> <url-pattern>/customers/*</url-pattern> </web-resource-collection> <auth-constraint> <role-name>user</role-name> </auth-constraint> </security-constraint> <login-config> <auth-method>BASIC</auth-method> <realm-name>does-not-matter</realm-name> </login-config> <security-role> <role-name>admin</role-name> </security-role> <security-role> <role-name>user</role-name> </security-role> </web-app>
Add the
jetty-web.xml
file with the authenticator to the/WEB-INF/jetty-web.xml
file.For example:
<?xml version="1.0"?> <!DOCTYPE Configure PUBLIC "-//Mort Bay Consulting//DTD Configure//EN" "http://www.eclipse.org/jetty/configure_9_0.dtd"> <Configure class="org.eclipse.jetty.webapp.WebAppContext"> <Get name="securityHandler"> <Set name="authenticator"> <New class="org.keycloak.adapters.jetty.KeycloakJettyAuthenticator"> </New> </Set> </Get> </Configure>
-
Within the
/WEB-INF/
directory of your WAR, create a new file, keycloak.json. The format of this configuration file is described in the Java Adapters Config section. It is also possible to make this file available externally as described in Configuring the External Adapter. Ensure your WAR application imports
org.keycloak.adapters.jetty
and maybe some more packages in theMETA-INF/MANIFEST.MF
file, under theImport-Package
header. Usingmaven-bundle-plugin
in your project properly generates OSGI headers in manifest. Note that "*" resolution for the package does not import theorg.keycloak.adapters.jetty
package, since it is not used by the application or the Blueprint or Spring descriptor, but is rather used in thejetty-web.xml
file.The list of the packages to import might look like this:
org.keycloak.adapters.jetty;version="18.0.19.redhat-00001", org.keycloak.adapters;version="18.0.19.redhat-00001", org.keycloak.constants;version="18.0.19.redhat-00001", org.keycloak.util;version="18.0.19.redhat-00001", org.keycloak.*;version="18.0.19.redhat-00001", *;resolution:=optional
2.1.6.3.1. Configuring the External Adapter
If you do not want the keycloak.json
adapter configuration file to be bundled inside your WAR application, but instead made available externally and loaded based on naming conventions, use this configuration method.
To enable the functionality, add this section to your /WEB_INF/web.xml
file:
<context-param>
<param-name>keycloak.config.resolver</param-name>
<param-value>org.keycloak.adapters.osgi.PathBasedKeycloakConfigResolver</param-value>
</context-param>
That component uses keycloak.config
or karaf.etc
java properties to search for a base folder to locate the configuration. Then inside one of those folders it searches for a file called <your_web_context>-keycloak.json
.
So, for example, if your web application has context my-portal
, then your adapter configuration is loaded from the $FUSE_HOME/etc/my-portal-keycloak.json
file.
2.1.6.4. Securing a servlet deployed as an OSGI Service
You can use this method if you have a servlet class inside your OSGI bundled project that is not deployed as a classic WAR application. Fuse uses Pax Web Whiteboard Extender to deploy such servlets as web applications.
Procedure
Red Hat Single Sign-On provides
org.keycloak.adapters.osgi.undertow.PaxWebIntegrationService
, which allows injecting jetty-web.xml and configuring security constraints for your application. You need to declare such services in theOSGI-INF/blueprint/blueprint.xml
file inside your application. Note that your servlet needs to depend on it. An example configuration:<?xml version="1.0" encoding="UTF-8"?> <blueprint xmlns="http://www.osgi.org/xmlns/blueprint/v1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.osgi.org/xmlns/blueprint/v1.0.0 http://www.osgi.org/xmlns/blueprint/v1.0.0/blueprint.xsd"> <!-- Using jetty bean just for the compatibility with other fuse services --> <bean id="servletConstraintMapping" class="org.eclipse.jetty.security.ConstraintMapping"> <property name="constraint"> <bean class="org.eclipse.jetty.util.security.Constraint"> <property name="name" value="cst1"/> <property name="roles"> <list> <value>user</value> </list> </property> <property name="authenticate" value="true"/> <property name="dataConstraint" value="0"/> </bean> </property> <property name="pathSpec" value="/product-portal/*"/> </bean> <bean id="keycloakPaxWebIntegration" class="org.keycloak.adapters.osgi.PaxWebIntegrationService" init-method="start" destroy-method="stop"> <property name="jettyWebXmlLocation" value="/WEB-INF/jetty-web.xml" /> <property name="bundleContext" ref="blueprintBundleContext" /> <property name="constraintMappings"> <list> <ref component-id="servletConstraintMapping" /> </list> </property> </bean> <bean id="productServlet" class="org.keycloak.example.ProductPortalServlet" depends-on="keycloakPaxWebIntegration"> </bean> <service ref="productServlet" interface="javax.servlet.Servlet"> <service-properties> <entry key="alias" value="/product-portal" /> <entry key="servlet-name" value="ProductServlet" /> <entry key="keycloak.config.file" value="/keycloak.json" /> </service-properties> </service> </blueprint>
-
You might need to have the
WEB-INF
directory inside your project (even if your project is not a web application) and create the/WEB-INF/jetty-web.xml
and/WEB-INF/keycloak.json
files as in the Classic WAR application section. Note you don’t need theweb.xml
file as the security-constraints are declared in the blueprint configuration file.
-
You might need to have the
The
Import-Package
inMETA-INF/MANIFEST.MF
must contain at least these imports:org.keycloak.adapters.jetty;version="18.0.19.redhat-00001", org.keycloak.adapters;version="18.0.19.redhat-00001", org.keycloak.constants;version="18.0.19.redhat-00001", org.keycloak.util;version="18.0.19.redhat-00001", org.keycloak.*;version="18.0.19.redhat-00001", *;resolution:=optional
2.1.6.5. Securing an Apache Camel application
You can secure Apache Camel endpoints implemented with the camel-jetty component by adding the securityHandler with KeycloakJettyAuthenticator
and the proper security constraints injected. You can add the OSGI-INF/blueprint/blueprint.xml
file to your Camel application with a similar configuration as below. The roles, security constraint mappings, and Red Hat Single Sign-On adapter configuration might differ slightly depending on your environment and needs.
For example:
<?xml version="1.0" encoding="UTF-8"?>
<blueprint xmlns="http://www.osgi.org/xmlns/blueprint/v1.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:camel="http://camel.apache.org/schema/blueprint"
xsi:schemaLocation="
http://www.osgi.org/xmlns/blueprint/v1.0.0 http://www.osgi.org/xmlns/blueprint/v1.0.0/blueprint.xsd
http://camel.apache.org/schema/blueprint http://camel.apache.org/schema/blueprint/camel-blueprint.xsd">
<bean id="kcAdapterConfig" class="org.keycloak.representations.adapters.config.AdapterConfig">
<property name="realm" value="demo"/>
<property name="resource" value="admin-camel-endpoint"/>
<property name="bearerOnly" value="true"/>
<property name="authServerUrl" value="http://localhost:8080/auth" />
<property name="sslRequired" value="EXTERNAL"/>
</bean>
<bean id="keycloakAuthenticator" class="org.keycloak.adapters.jetty.KeycloakJettyAuthenticator">
<property name="adapterConfig" ref="kcAdapterConfig"/>
</bean>
<bean id="constraint" class="org.eclipse.jetty.util.security.Constraint">
<property name="name" value="Customers"/>
<property name="roles">
<list>
<value>admin</value>
</list>
</property>
<property name="authenticate" value="true"/>
<property name="dataConstraint" value="0"/>
</bean>
<bean id="constraintMapping" class="org.eclipse.jetty.security.ConstraintMapping">
<property name="constraint" ref="constraint"/>
<property name="pathSpec" value="/*"/>
</bean>
<bean id="securityHandler" class="org.eclipse.jetty.security.ConstraintSecurityHandler">
<property name="authenticator" ref="keycloakAuthenticator" />
<property name="constraintMappings">
<list>
<ref component-id="constraintMapping" />
</list>
</property>
<property name="authMethod" value="BASIC"/>
<property name="realmName" value="does-not-matter"/>
</bean>
<bean id="sessionHandler" class="org.keycloak.adapters.jetty.spi.WrappingSessionHandler">
<property name="handler" ref="securityHandler" />
</bean>
<bean id="helloProcessor" class="org.keycloak.example.CamelHelloProcessor" />
<camelContext id="blueprintContext"
trace="false"
xmlns="http://camel.apache.org/schema/blueprint">
<route id="httpBridge">
<from uri="jetty:http://0.0.0.0:8383/admin-camel-endpoint?handlers=sessionHandler&matchOnUriPrefix=true" />
<process ref="helloProcessor" />
<log message="The message from camel endpoint contains ${body}"/>
</route>
</camelContext>
</blueprint>
-
The
Import-Package
inMETA-INF/MANIFEST.MF
needs to contain these imports:
javax.servlet;version="[3,4)",
javax.servlet.http;version="[3,4)",
org.apache.camel.*,
org.apache.camel;version="[2.13,3)",
org.eclipse.jetty.security;version="[9,10)",
org.eclipse.jetty.server.nio;version="[9,10)",
org.eclipse.jetty.util.security;version="[9,10)",
org.keycloak.*;version="18.0.19.redhat-00001",
org.osgi.service.blueprint,
org.osgi.service.blueprint.container,
org.osgi.service.event,
2.1.6.6. Camel RestDSL
Camel RestDSL is a Camel feature used to define your REST endpoints in a fluent way. But you must still use specific implementation classes and provide instructions on how to integrate with Red Hat Single Sign-On.
The way to configure the integration mechanism depends on the Camel component for which you configure your RestDSL-defined routes.
The following example shows how to configure integration using the Jetty component, with references to some of the beans defined in previous Blueprint example.
<bean id="securityHandlerRest" class="org.eclipse.jetty.security.ConstraintSecurityHandler">
<property name="authenticator" ref="keycloakAuthenticator" />
<property name="constraintMappings">
<list>
<ref component-id="constraintMapping" />
</list>
</property>
<property name="authMethod" value="BASIC"/>
<property name="realmName" value="does-not-matter"/>
</bean>
<bean id="sessionHandlerRest" class="org.keycloak.adapters.jetty.spi.WrappingSessionHandler">
<property name="handler" ref="securityHandlerRest" />
</bean>
<camelContext id="blueprintContext"
trace="false"
xmlns="http://camel.apache.org/schema/blueprint">
<restConfiguration component="jetty" contextPath="/restdsl"
port="8484">
<!--the link with Keycloak security handlers happens here-->
<endpointProperty key="handlers" value="sessionHandlerRest"></endpointProperty>
<endpointProperty key="matchOnUriPrefix" value="true"></endpointProperty>
</restConfiguration>
<rest path="/hello" >
<description>Hello rest service</description>
<get uri="/{id}" outType="java.lang.String">
<description>Just an helllo</description>
<to uri="direct:justDirect" />
</get>
</rest>
<route id="justDirect">
<from uri="direct:justDirect"/>
<process ref="helloProcessor" />
<log message="RestDSL correctly invoked ${body}"/>
<setBody>
<constant>(__This second sentence is returned from a Camel RestDSL endpoint__)</constant>
</setBody>
</route>
</camelContext>
2.1.6.7. Securing an Apache CXF endpoint on a separate Jetty engine
Procedure
To run your CXF endpoints secured by Red Hat Single Sign-On on separate Jetty engines, perform the following procedure.
Add
META-INF/spring/beans.xml
to your application, and in it, declarehttpj:engine-factory
with Jetty SecurityHandler with injectedKeycloakJettyAuthenticator
. The configuration for a CFX JAX-WS application might resemble this one:<?xml version="1.0" encoding="UTF-8"?> <beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:jaxws="http://cxf.apache.org/jaxws" xmlns:httpj="http://cxf.apache.org/transports/http-jetty/configuration" xsi:schemaLocation=" http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://cxf.apache.org/jaxws http://cxf.apache.org/schemas/jaxws.xsd http://www.springframework.org/schema/osgi http://www.springframework.org/schema/osgi/spring-osgi.xsd http://cxf.apache.org/transports/http-jetty/configuration http://cxf.apache.org/schemas/configuration/http-jetty.xsd"> <import resource="classpath:META-INF/cxf/cxf.xml" /> <bean id="kcAdapterConfig" class="org.keycloak.representations.adapters.config.AdapterConfig"> <property name="realm" value="demo"/> <property name="resource" value="custom-cxf-endpoint"/> <property name="bearerOnly" value="true"/> <property name="authServerUrl" value="http://localhost:8080/auth" /> <property name="sslRequired" value="EXTERNAL"/> </bean> <bean id="keycloakAuthenticator" class="org.keycloak.adapters.jetty.KeycloakJettyAuthenticator"> <property name="adapterConfig"> <ref local="kcAdapterConfig" /> </property> </bean> <bean id="constraint" class="org.eclipse.jetty.util.security.Constraint"> <property name="name" value="Customers"/> <property name="roles"> <list> <value>user</value> </list> </property> <property name="authenticate" value="true"/> <property name="dataConstraint" value="0"/> </bean> <bean id="constraintMapping" class="org.eclipse.jetty.security.ConstraintMapping"> <property name="constraint" ref="constraint"/> <property name="pathSpec" value="/*"/> </bean> <bean id="securityHandler" class="org.eclipse.jetty.security.ConstraintSecurityHandler"> <property name="authenticator" ref="keycloakAuthenticator" /> <property name="constraintMappings"> <list> <ref local="constraintMapping" /> </list> </property> <property name="authMethod" value="BASIC"/> <property name="realmName" value="does-not-matter"/> </bean> <httpj:engine-factory bus="cxf" id="kc-cxf-endpoint"> <httpj:engine port="8282"> <httpj:handlers> <ref local="securityHandler" /> </httpj:handlers> <httpj:sessionSupport>true</httpj:sessionSupport> </httpj:engine> </httpj:engine-factory> <jaxws:endpoint implementor="org.keycloak.example.ws.ProductImpl" address="http://localhost:8282/ProductServiceCF" depends-on="kc-cxf-endpoint" /> </beans>
For the CXF JAX-RS application, the only difference might be in the configuration of the endpoint dependent on engine-factory:
<jaxrs:server serviceClass="org.keycloak.example.rs.CustomerService" address="http://localhost:8282/rest" depends-on="kc-cxf-endpoint"> <jaxrs:providers> <bean class="com.fasterxml.jackson.jaxrs.json.JacksonJsonProvider" /> </jaxrs:providers> </jaxrs:server>
-
The
Import-Package
inMETA-INF/MANIFEST.MF
must contain those imports:
META-INF.cxf;version="[2.7,3.2)",
META-INF.cxf.osgi;version="[2.7,3.2)";resolution:=optional,
org.apache.cxf.bus;version="[2.7,3.2)",
org.apache.cxf.bus.spring;version="[2.7,3.2)",
org.apache.cxf.bus.resource;version="[2.7,3.2)",
org.apache.cxf.transport.http;version="[2.7,3.2)",
org.apache.cxf.*;version="[2.7,3.2)",
org.springframework.beans.factory.config,
org.eclipse.jetty.security;version="[9,10)",
org.eclipse.jetty.util.security;version="[9,10)",
org.keycloak.*;version="18.0.19.redhat-00001"
2.1.6.8. Securing an Apache CXF endpoint on the default Jetty Engine
Some services automatically come with deployed servlets on startup. One such service is the CXF servlet running in the http://localhost:8181/cxf context. Securing such endpoints can be complicated. One approach, which Red Hat Single Sign-On is currently using, is ServletReregistrationService, which undeploys a built-in servlet at startup, enabling you to redeploy it on a context secured by Red Hat Single Sign-On.
The configuration file OSGI-INF/blueprint/blueprint.xml
inside your application might resemble the one below. Note that it adds the JAX-RS customerservice
endpoint, which is endpoint-specific to your application, but more importantly, secures the entire /cxf
context.
<?xml version="1.0" encoding="UTF-8"?>
<blueprint xmlns="http://www.osgi.org/xmlns/blueprint/v1.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:jaxrs="http://cxf.apache.org/blueprint/jaxrs"
xsi:schemaLocation="
http://www.osgi.org/xmlns/blueprint/v1.0.0 http://www.osgi.org/xmlns/blueprint/v1.0.0/blueprint.xsd
http://cxf.apache.org/blueprint/jaxrs http://cxf.apache.org/schemas/blueprint/jaxrs.xsd">
<!-- JAXRS Application -->
<bean id="customerBean" class="org.keycloak.example.rs.CxfCustomerService" />
<jaxrs:server id="cxfJaxrsServer" address="/customerservice">
<jaxrs:providers>
<bean class="com.fasterxml.jackson.jaxrs.json.JacksonJsonProvider" />
</jaxrs:providers>
<jaxrs:serviceBeans>
<ref component-id="customerBean" />
</jaxrs:serviceBeans>
</jaxrs:server>
<!-- Securing of whole /cxf context by unregister default cxf servlet from paxweb and re-register with applied security constraints -->
<bean id="cxfConstraintMapping" class="org.eclipse.jetty.security.ConstraintMapping">
<property name="constraint">
<bean class="org.eclipse.jetty.util.security.Constraint">
<property name="name" value="cst1"/>
<property name="roles">
<list>
<value>user</value>
</list>
</property>
<property name="authenticate" value="true"/>
<property name="dataConstraint" value="0"/>
</bean>
</property>
<property name="pathSpec" value="/cxf/*"/>
</bean>
<bean id="cxfKeycloakPaxWebIntegration" class="org.keycloak.adapters.osgi.PaxWebIntegrationService"
init-method="start" destroy-method="stop">
<property name="bundleContext" ref="blueprintBundleContext" />
<property name="jettyWebXmlLocation" value="/WEB-INF/jetty-web.xml" />
<property name="constraintMappings">
<list>
<ref component-id="cxfConstraintMapping" />
</list>
</property>
</bean>
<bean id="defaultCxfReregistration" class="org.keycloak.adapters.osgi.ServletReregistrationService" depends-on="cxfKeycloakPaxWebIntegration"
init-method="start" destroy-method="stop">
<property name="bundleContext" ref="blueprintBundleContext" />
<property name="managedServiceReference">
<reference interface="org.osgi.service.cm.ManagedService" filter="(service.pid=org.apache.cxf.osgi)" timeout="5000" />
</property>
</bean>
</blueprint>
As a result, all other CXF services running on the default CXF HTTP destination are also secured. Similarly, when the application is undeployed, the entire /cxf
context becomes unsecured as well. For this reason, using your own Jetty engine for your applications as described in Secure CXF Application on separate Jetty Engine then gives you more control over security for each individual application.
-
The
WEB-INF
directory might need to be inside your project (even if your project is not a web application). You might also need to edit the/WEB-INF/jetty-web.xml
and/WEB-INF/keycloak.json
files in a similar way as in Classic WAR application. Note that you do not need theweb.xml
file as the security constraints are declared in the blueprint configuration file. -
The
Import-Package
inMETA-INF/MANIFEST.MF
must contain these imports:
META-INF.cxf;version="[2.7,3.2)",
META-INF.cxf.osgi;version="[2.7,3.2)";resolution:=optional,
org.apache.cxf.transport.http;version="[2.7,3.2)",
org.apache.cxf.*;version="[2.7,3.2)",
com.fasterxml.jackson.jaxrs.json;version="[2.5,3)",
org.eclipse.jetty.security;version="[9,10)",
org.eclipse.jetty.util.security;version="[9,10)",
org.keycloak.*;version="18.0.19.redhat-00001",
org.keycloak.adapters.jetty;version="18.0.19.redhat-00001",
*;resolution:=optional
2.1.6.9. Securing Fuse Administration Services
2.1.6.9.1. Using SSH Authentication to Fuse Terminal
Red Hat Single Sign-On mainly addresses use cases for authentication of web applications; however, if your other web services and applications are protected with Red Hat Single Sign-On, protecting non-web administration services such as SSH with Red Hat Single Sign-On credentials is a best pracrice. You can do this using the JAAS login module, which allows remote connection to Red Hat Single Sign-On and verifies credentials based on Resource Owner Password Credentials.
To enable SSH authentication, perform the following procedure.
Procedure
-
In Red Hat Single Sign-On create a client (for example,
ssh-jmx-admin-client
), which will be used for SSH authentication. This client needs to haveDirect Access Grants Enabled
selected toOn
. In the
$FUSE_HOME/etc/org.apache.karaf.shell.cfg
file, update or specify this property:sshRealm=keycloak
Add the
$FUSE_HOME/etc/keycloak-direct-access.json
file with content similar to the following (based on your environment and Red Hat Single Sign-On client settings):{ "realm": "demo", "resource": "ssh-jmx-admin-client", "ssl-required" : "external", "auth-server-url" : "http://localhost:8080/auth", "credentials": { "secret": "password" } }
This file specifies the client application configuration, which is used by JAAS DirectAccessGrantsLoginModule from the
keycloak
JAAS realm for SSH authentication.Start Fuse and install the
keycloak
JAAS realm. The easiest way is to install thekeycloak-jaas
feature, which has the JAAS realm predefined. You can override the feature’s predefined realm by using your ownkeycloak
JAAS realm with higher ranking. For details see the JBoss Fuse documentation.Use these commands in the Fuse terminal:
features:addurl mvn:org.keycloak/keycloak-osgi-features/18.0.19.redhat-00001/xml/features features:install keycloak-jaas
Log in using SSH as
admin
user by typing the following in the terminal:ssh -o PubkeyAuthentication=no -p 8101 admin@localhost
-
Log in with password
password
.
On some later operating systems, you might also need to use the SSH command’s -o option -o HostKeyAlgorithms=+ssh-dss
because later SSH clients do not allow use of the ssh-dss
algorithm, by default. However, by default, it is currently used in JBoss Fuse 6.3.0 Rollup 12.
Note that the user needs to have realm role admin
to perform all operations or another role to perform a subset of operations (for example, the viewer role that restricts the user to run only read-only Karaf commands). The available roles are configured in $FUSE_HOME/etc/org.apache.karaf.shell.cfg
or $FUSE_HOME/etc/system.properties
.
2.1.6.9.2. Using JMX authentication
JMX authentication might be necessary if you want to use jconsole or another external tool to remotely connect to JMX through RMI. Otherwise it might be better to use hawt.io/jolokia, since the jolokia agent is installed in hawt.io by default. For more details see Hawtio Admin Console.
Procedure
In the
$FUSE_HOME/etc/org.apache.karaf.management.cfg
file, change the jmxRealm property to:jmxRealm=keycloak
-
Install the
keycloak-jaas
feature and configure the$FUSE_HOME/etc/keycloak-direct-access.json
file as described in the SSH section above. - In jconsole you can use a URL such as:
service:jmx:rmi://localhost:44444/jndi/rmi://localhost:1099/karaf-root
and credentials: admin/password (based on the user with admin privileges according to your environment).
2.1.6.10. Securing the Hawtio Administration Console
To secure the Hawtio Administration Console with Red Hat Single Sign-On, perform the following procedure.
Procedure
Add these properties to the
$FUSE_HOME/etc/system.properties
file:hawtio.keycloakEnabled=true hawtio.realm=keycloak hawtio.keycloakClientConfig=file://${karaf.base}/etc/keycloak-hawtio-client.json hawtio.rolePrincipalClasses=org.keycloak.adapters.jaas.RolePrincipal,org.apache.karaf.jaas.boot.principal.RolePrincipal
-
Create a client in the Red Hat Single Sign-On Admin Console in your realm. For example, in the Red Hat Single Sign-On
demo
realm, create a clienthawtio-client
, specifypublic
as the Access Type, and specify a redirect URI pointing to Hawtio: http://localhost:8181/hawtio/*. You must also have a corresponding Web Origin configured (in this case, http://localhost:8181). -
Create the
keycloak-hawtio-client.json
file in the$FUSE_HOME/etc
directory using content similar to that shown in the example below. Change therealm
,resource
, andauth-server-url
properties according to your Red Hat Single Sign-On environment. Theresource
property must point to the client created in the previous step. This file is used by the client (Hawtio JavaScript application) side.
{
"realm" : "demo",
"resource" : "hawtio-client",
"auth-server-url" : "http://localhost:8080/auth",
"ssl-required" : "external",
"public-client" : true
}
Create the
keycloak-hawtio.json
file in the$FUSE_HOME/etc
dicrectory using content similar to that shown in the example below. Change therealm
andauth-server-url
properties according to your Red Hat Single Sign-On environment. This file is used by the adapters on the server (JAAS Login module) side.{ "realm" : "demo", "resource" : "jaas", "bearer-only" : true, "auth-server-url" : "http://localhost:8080/auth", "ssl-required" : "external", "use-resource-role-mappings": false, "principal-attribute": "preferred_username" }
Start JBoss Fuse 6.3.0 Rollup 12 and install the keycloak feature if you have not already done so. The commands in Karaf terminal are similar to this example:
features:addurl mvn:org.keycloak/keycloak-osgi-features/18.0.19.redhat-00001/xml/features features:install keycloak
Go to http://localhost:8181/hawtio and log in as a user from your Red Hat Single Sign-On realm.
Note that the user needs to have the proper realm role to successfully authenticate to Hawtio. The available roles are configured in the
$FUSE_HOME/etc/system.properties
file inhawtio.roles
.
2.1.6.10.1. Securing Hawtio on JBoss EAP 6.4
Prerequisites
Set up Red Hat Single Sign-On as described in Securing the Hawtio Administration Console. It is assumed that:
-
you have a Red Hat Single Sign-On realm
demo
and clienthawtio-client
-
your Red Hat Single Sign-On is running on
localhost:8080
-
the JBoss EAP 6.4 server with deployed Hawtio will be running on
localhost:8181
. The directory with this server is referred in next steps as$EAP_HOME
.
Procedure
-
Copy the
hawtio-wildfly-1.4.0.redhat-630396.war
archive to the$EAP_HOME/standalone/configuration
directory. For more details about deploying Hawtio see the Fuse Hawtio documentation. -
Copy the
keycloak-hawtio.json
andkeycloak-hawtio-client.json
files with the above content to the$EAP_HOME/standalone/configuration
directory. - Install the Red Hat Single Sign-On adapter subsystem to your JBoss EAP 6.4 server as described in the JBoss adapter documentation.
In the
$EAP_HOME/standalone/configuration/standalone.xml
file configure the system properties as in this example:<extensions> ... </extensions> <system-properties> <property name="hawtio.authenticationEnabled" value="true" /> <property name="hawtio.realm" value="hawtio" /> <property name="hawtio.roles" value="admin,viewer" /> <property name="hawtio.rolePrincipalClasses" value="org.keycloak.adapters.jaas.RolePrincipal" /> <property name="hawtio.keycloakEnabled" value="true" /> <property name="hawtio.keycloakClientConfig" value="${jboss.server.config.dir}/keycloak-hawtio-client.json" /> <property name="hawtio.keycloakServerConfig" value="${jboss.server.config.dir}/keycloak-hawtio.json" /> </system-properties>
Add the Hawtio realm to the same file in the
security-domains
section:<security-domain name="hawtio" cache-type="default"> <authentication> <login-module code="org.keycloak.adapters.jaas.BearerTokenLoginModule" flag="required"> <module-option name="keycloak-config-file" value="${hawtio.keycloakServerConfig}"/> </login-module> </authentication> </security-domain>
Add the
secure-deployment
sectionhawtio
to the adapter subsystem. This ensures that the Hawtio WAR is able to find the JAAS login module classes.<subsystem xmlns="urn:jboss:domain:keycloak:1.1"> <secure-deployment name="hawtio-wildfly-1.4.0.redhat-630396.war" /> </subsystem>
Restart the JBoss EAP 6.4 server with Hawtio:
cd $EAP_HOME/bin ./standalone.sh -Djboss.socket.binding.port-offset=101
- Access Hawtio at http://localhost:8181/hawtio. It is secured by Red Hat Single Sign-On.
2.1.7. JBoss Fuse 7 Adapter
Red Hat Single Sign-On supports securing your web applications running inside JBoss Fuse 7.
JBoss Fuse 7 leverages Undertow adapter which is essentially the same as JBoss EAP 7 Adapter as JBoss Fuse 7.4.0 is bundled with the Undertow HTTP engine under the covers and Undertow is used for running various kinds of web applications.
The only supported version of Fuse 7 is the latest release. If you use earlier versions of Fuse 7, it is possible that some functions will not work correctly. In particular, integration will not work at all for versions of Fuse 7 lower than 7.12.0.
Security for the following items is supported for Fuse:
- Classic WAR applications deployed on Fuse with Pax Web War Extender
- Servlets deployed on Fuse as OSGI services with Pax Web Whiteboard Extender and additionally servlets registered through org.osgi.service.http.HttpService#registerServlet() which is standard OSGi Enterprise HTTP Service
- Apache Camel Undertow endpoints running with the Camel Undertow component
- Apache CXF endpoints running on their own separate Undertow engine
- Apache CXF endpoints running on the default engine provided by the CXF servlet
- SSH and JMX admin access
- Hawtio administration console
2.1.7.1. Securing your web applications inside Fuse 7
You must first install the Red Hat Single Sign-On Karaf feature. Next you will need to perform the steps according to the type of application you want to secure. All referenced web applications require injecting the Red Hat Single Sign-On Undertow authentication mechanism into the underlying web server. The steps to achieve this depend on the application type. The details are described below.
2.1.7.2. Installing the Keycloak feature
You must first install the keycloak-pax-http-undertow
and keycloak-jaas
features in the JBoss Fuse environment. The keycloak-pax-http-undertow
feature includes the Fuse adapter and all third-party dependencies. The keycloak-jaas
contains JAAS module used in realm for SSH and JMX authentication. You can install it either from the Maven repository or from an archive.
2.1.7.2.1. Installing from the Maven repository
Prerequisites
- You must be online and have access to the Maven repository.
- For Red Hat Single Sign-On, configure a proper Maven repository, so you can install the artifacts. For more information see the JBoss Enterprise Maven repository page.
Assuming the Maven repository is https://maven.repository.redhat.com/ga/, add the following to the
$FUSE_HOME/etc/org.ops4j.pax.url.mvn.cfg
file and add the repository to the list of supported repositories. For example:config:edit org.ops4j.pax.url.mvn config:property-append org.ops4j.pax.url.mvn.repositories ,https://maven.repository.redhat.com/ga/@id=redhat.product.repo config:update feature:repo-refresh
Procedure
- Start JBoss Fuse 7.4.0
In the Karaf terminal, type:
feature:repo-add mvn:org.keycloak/keycloak-osgi-features/18.0.19.redhat-00001/xml/features feature:install keycloak-pax-http-undertow keycloak-jaas
You might also need to install the Undertow feature:
feature:install pax-web-http-undertow
Ensure that the features were installed:
feature:list | grep keycloak
2.1.7.2.2. Installing from the ZIP bundle
This is useful if you are offline or do not want to use Maven to obtain the JAR files and other artifacts.
Procedure
- Download the Red Hat Single Sign-On Fuse adapter ZIP archive from the Sotware Downloads site.
Unzip it into the root directory of JBoss Fuse. The dependencies are then installed under the
system
directory. You can overwrite all existing jar files.Use this for JBoss Fuse 7.4.0:
cd /path-to-fuse/fuse-karaf-7.z unzip -q /path-to-adapter-zip/rh-sso-7.6.12-fuse-adapter.zip
Start Fuse and run these commands in the fuse/karaf terminal:
feature:repo-add mvn:org.keycloak/keycloak-osgi-features/18.0.19.redhat-00001/xml/features feature:install keycloak-pax-http-undertow keycloak-jaas
-
Install the corresponding Undertow adapter. Since the artifacts are available directly in the JBoss Fuse
system
directory, you do not need to use the Maven repository.
2.1.7.3. Securing a Classic WAR application
Procedure
In the
/WEB-INF/web.xml
file, declare the necessary:- security constraints in the <security-constraint> element
-
login configuration in the <login-config> element. Make sure that the
<auth-method>
isKEYCLOAK
. security roles in the <security-role> element
For example:
<?xml version="1.0" encoding="UTF-8"?> <web-app xmlns="http://java.sun.com/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd" version="3.0"> <module-name>customer-portal</module-name> <welcome-file-list> <welcome-file>index.html</welcome-file> </welcome-file-list> <security-constraint> <web-resource-collection> <web-resource-name>Customers</web-resource-name> <url-pattern>/customers/*</url-pattern> </web-resource-collection> <auth-constraint> <role-name>user</role-name> </auth-constraint> </security-constraint> <login-config> <auth-method>KEYCLOAK</auth-method> <realm-name>does-not-matter</realm-name> </login-config> <security-role> <role-name>admin</role-name> </security-role> <security-role> <role-name>user</role-name> </security-role> </web-app>
Within the
/WEB-INF/
directory of your WAR, create a new file, keycloak.json. The format of this configuration file is described in the Java Adapters Config section. It is also possible to make this file available externally as described in Configuring the External Adapter.For example:
{ "realm": "demo", "resource": "customer-portal", "auth-server-url": "http://localhost:8080/auth", "ssl-required" : "external", "credentials": { "secret": "password" } }
- Contrary to the Fuse 6 adapter, there are no special OSGi imports needed in MANIFEST.MF.
2.1.7.3.1. Configuration resolvers
The keycloak.json
adapter configuration file can be stored inside a bundle, which is default behaviour, or in a directory on a filesystem. To specify the actual source of the configuration file, set the keycloak.config.resolver
deployment parameter to the desired configuration resolver class. For example, in a classic WAR application, set the keycloak.config.resolver
context parameter in web.xml
file like this:
<context-param>
<param-name>keycloak.config.resolver</param-name>
<param-value>org.keycloak.adapters.osgi.PathBasedKeycloakConfigResolver</param-value>
</context-param>
The following resolvers are available for keycloak.config.resolver
:
- org.keycloak.adapters.osgi.BundleBasedKeycloakConfigResolver
-
This is the default resolver. The configuration file is expected inside the OSGi bundle that is being secured. By default, it loads file named
WEB-INF/keycloak.json
but this file name can be configured viaconfigLocation
property. - org.keycloak.adapters.osgi.PathBasedKeycloakConfigResolver
This resolver searches for a file called
<your_web_context>-keycloak.json
inside a folder that is specified bykeycloak.config
system property. Ifkeycloak.config
is not set,karaf.etc
system property is used instead.For example, if your web application is deployed into context
my-portal
, then your adapter configuration would be loaded either from the${keycloak.config}/my-portal-keycloak.json
file, or from${karaf.etc}/my-portal-keycloak.json
.- org.keycloak.adapters.osgi.HierarchicalPathBasedKeycloakConfigResolver
This resolver is similar to
PathBasedKeycloakConfigResolver
above, where for given URI path, configuration locations are checked from most to least specific.For example, for
/my/web-app/context
URI, the following configuration locations are searched for existence until the first one exists:-
${karaf.etc}/my-web-app-context-keycloak.json
-
${karaf.etc}/my-web-app-keycloak.json
-
${karaf.etc}/my-keycloak.json
-
${karaf.etc}/keycloak.json
-
2.1.7.4. Securing a servlet deployed as an OSGI Service
You can use this method if you have a servlet class inside your OSGI bundled project that is not deployed as a classic WAR application. Fuse uses Pax Web Whiteboard Extender to deploy such servlets as web applications.
Procedure
Red Hat Single Sign-On provides
org.keycloak.adapters.osgi.undertow.PaxWebIntegrationService
, which allows configuring authentication method and security constraints for your application. You need to declare such services in theOSGI-INF/blueprint/blueprint.xml
file inside your application. Note that your servlet needs to depend on it. An example configuration:<?xml version="1.0" encoding="UTF-8"?> <blueprint xmlns="http://www.osgi.org/xmlns/blueprint/v1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.osgi.org/xmlns/blueprint/v1.0.0 http://www.osgi.org/xmlns/blueprint/v1.0.0/blueprint.xsd"> <bean id="servletConstraintMapping" class="org.keycloak.adapters.osgi.PaxWebSecurityConstraintMapping"> <property name="roles"> <list> <value>user</value> </list> </property> <property name="authentication" value="true"/> <property name="url" value="/product-portal/*"/> </bean> <!-- This handles the integration and setting the login-config and security-constraints parameters --> <bean id="keycloakPaxWebIntegration" class="org.keycloak.adapters.osgi.undertow.PaxWebIntegrationService" init-method="start" destroy-method="stop"> <property name="bundleContext" ref="blueprintBundleContext" /> <property name="constraintMappings"> <list> <ref component-id="servletConstraintMapping" /> </list> </property> </bean> <bean id="productServlet" class="org.keycloak.example.ProductPortalServlet" depends-on="keycloakPaxWebIntegration" /> <service ref="productServlet" interface="javax.servlet.Servlet"> <service-properties> <entry key="alias" value="/product-portal" /> <entry key="servlet-name" value="ProductServlet" /> <entry key="keycloak.config.file" value="/keycloak.json" /> </service-properties> </service> </blueprint>
You might need to have the
WEB-INF
directory inside your project (even if your project is not a web application) and create the/WEB-INF/keycloak.json
file as described in the Classic WAR application section. Note you don’t need theweb.xml
file as the security-constraints are declared in the blueprint configuration file.- Contrary to the Fuse 6 adapter, there are no special OSGi imports needed in MANIFEST.MF.
2.1.7.5. Securing an Apache Camel application
You can secure Apache Camel endpoints implemented with the camel-undertow component by injecting the proper security constraints via blueprint and updating the used component to undertow-keycloak
. You have to add the OSGI-INF/blueprint/blueprint.xml
file to your Camel application with a similar configuration as below. The roles, security constraint mappings, and adapter configuration might differ slightly depending on your environment and needs.
Compared to the standard undertow
component, undertow-keycloak
component adds two new properties:
-
configResolver
is a resolver bean that supplies Red Hat Single Sign-On adapter configuration. Available resolvers are listed in Configuration Resolvers section. -
allowedRoles
is a comma-separated list of roles. User accessing the service has to have at least one role to be permitted the access.
For example:
<?xml version="1.0" encoding="UTF-8"?>
<blueprint xmlns="http://www.osgi.org/xmlns/blueprint/v1.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:camel="http://camel.apache.org/schema/blueprint"
xsi:schemaLocation="
http://www.osgi.org/xmlns/blueprint/v1.0.0 http://www.osgi.org/xmlns/blueprint/v1.0.0/blueprint.xsd
http://camel.apache.org/schema/blueprint http://camel.apache.org/schema/blueprint/camel-blueprint-2.17.1.xsd">
<bean id="keycloakConfigResolver" class="org.keycloak.adapters.osgi.BundleBasedKeycloakConfigResolver" >
<property name="bundleContext" ref="blueprintBundleContext" />
</bean>
<bean id="helloProcessor" class="org.keycloak.example.CamelHelloProcessor" />
<camelContext id="blueprintContext"
trace="false"
xmlns="http://camel.apache.org/schema/blueprint">
<route id="httpBridge">
<from uri="undertow-keycloak:http://0.0.0.0:8383/admin-camel-endpoint?matchOnUriPrefix=true&configResolver=#keycloakConfigResolver&allowedRoles=admin" />
<process ref="helloProcessor" />
<log message="The message from camel endpoint contains ${body}"/>
</route>
</camelContext>
</blueprint>
-
The
Import-Package
inMETA-INF/MANIFEST.MF
needs to contain these imports:
javax.servlet;version="[3,4)",
javax.servlet.http;version="[3,4)",
javax.net.ssl,
org.apache.camel.*,
org.apache.camel;version="[2.13,3)",
io.undertow.*,
org.keycloak.*;version="18.0.19.redhat-00001",
org.osgi.service.blueprint,
org.osgi.service.blueprint.container
2.1.7.6. Camel RestDSL
Camel RestDSL is a Camel feature used to define your REST endpoints in a fluent way. But you must still use specific implementation classes and provide instructions on how to integrate with Red Hat Single Sign-On.
The way to configure the integration mechanism depends on the Camel component for which you configure your RestDSL-defined routes.
The following example shows how to configure integration using the undertow-keycloak
component, with references to some of the beans defined in previous Blueprint example.
<camelContext id="blueprintContext"
trace="false"
xmlns="http://camel.apache.org/schema/blueprint">
<!--the link with Keycloak security handlers happens by using undertow-keycloak component -->
<restConfiguration apiComponent="undertow-keycloak" contextPath="/restdsl" port="8484">
<endpointProperty key="configResolver" value="#keycloakConfigResolver" />
<endpointProperty key="allowedRoles" value="admin,superadmin" />
</restConfiguration>
<rest path="/hello" >
<description>Hello rest service</description>
<get uri="/{id}" outType="java.lang.String">
<description>Just a hello</description>
<to uri="direct:justDirect" />
</get>
</rest>
<route id="justDirect">
<from uri="direct:justDirect"/>
<process ref="helloProcessor" />
<log message="RestDSL correctly invoked ${body}"/>
<setBody>
<constant>(__This second sentence is returned from a Camel RestDSL endpoint__)</constant>
</setBody>
</route>
</camelContext>
2.1.7.7. Securing an Apache CXF endpoint on a separate Undertow Engine
To run your CXF endpoints secured by Red Hat Single Sign-On on a separate Undertow engine, perform the following procedure.
Procedure
Add
OSGI-INF/blueprint/blueprint.xml
to your application, and in it, add the proper configuration resolver bean similarly to Camel configuration. In thehttpu:engine-factory
declareorg.keycloak.adapters.osgi.undertow.CxfKeycloakAuthHandler
handler using that camel configuration. The configuration for a CFX JAX-WS application might resemble this one:<?xml version="1.0" encoding="UTF-8"?> <blueprint xmlns="http://www.osgi.org/xmlns/blueprint/v1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:jaxws="http://cxf.apache.org/blueprint/jaxws" xmlns:cxf="http://cxf.apache.org/blueprint/core" xmlns:httpu="http://cxf.apache.org/transports/http-undertow/configuration". xsi:schemaLocation=" http://cxf.apache.org/transports/http-undertow/configuration http://cxf.apache.org/schemas/configuration/http-undertow.xsd http://cxf.apache.org/blueprint/core http://cxf.apache.org/schemas/blueprint/core.xsd http://cxf.apache.org/blueprint/jaxws http://cxf.apache.org/schemas/blueprint/jaxws.xsd"> <bean id="keycloakConfigResolver" class="org.keycloak.adapters.osgi.BundleBasedKeycloakConfigResolver" > <property name="bundleContext" ref="blueprintBundleContext" /> </bean> <httpu:engine-factory bus="cxf" id="kc-cxf-endpoint"> <httpu:engine port="8282"> <httpu:handlers> <bean class="org.keycloak.adapters.osgi.undertow.CxfKeycloakAuthHandler"> <property name="configResolver" ref="keycloakConfigResolver" /> </bean> </httpu:handlers> </httpu:engine> </httpu:engine-factory> <jaxws:endpoint implementor="org.keycloak.example.ws.ProductImpl" address="http://localhost:8282/ProductServiceCF" depends-on="kc-cxf-endpoint"/> </blueprint>
For the CXF JAX-RS application, the only difference might be in the configuration of the endpoint dependent on engine-factory:
<jaxrs:server serviceClass="org.keycloak.example.rs.CustomerService" address="http://localhost:8282/rest" depends-on="kc-cxf-endpoint"> <jaxrs:providers> <bean class="com.fasterxml.jackson.jaxrs.json.JacksonJsonProvider" /> </jaxrs:providers> </jaxrs:server>
-
The
Import-Package
inMETA-INF/MANIFEST.MF
must contain those imports:
META-INF.cxf;version="[2.7,3.3)",
META-INF.cxf.osgi;version="[2.7,3.3)";resolution:=optional,
org.apache.cxf.bus;version="[2.7,3.3)",
org.apache.cxf.bus.spring;version="[2.7,3.3)",
org.apache.cxf.bus.resource;version="[2.7,3.3)",
org.apache.cxf.transport.http;version="[2.7,3.3)",
org.apache.cxf.*;version="[2.7,3.3)",
org.springframework.beans.factory.config,
org.keycloak.*;version="18.0.19.redhat-00001"
2.1.7.8. Securing an Apache CXF endpoint on the default Undertow Engine
Some services automatically come with deployed servlets on startup. One such service is the CXF servlet running in the http://localhost:8181/cxf context. Fuse’s Pax Web supports altering existing contexts via configuration admin. This can be used to secure endpoints by Red Hat Single Sign-On.
The configuration file OSGI-INF/blueprint/blueprint.xml
inside your application might resemble the one below. Note that it adds the JAX-RS customerservice
endpoint, which is endpoint-specific to your application.
<?xml version="1.0" encoding="UTF-8"?>
<blueprint xmlns="http://www.osgi.org/xmlns/blueprint/v1.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:jaxrs="http://cxf.apache.org/blueprint/jaxrs"
xsi:schemaLocation="
http://www.osgi.org/xmlns/blueprint/v1.0.0 http://www.osgi.org/xmlns/blueprint/v1.0.0/blueprint.xsd
http://cxf.apache.org/blueprint/jaxrs http://cxf.apache.org/schemas/blueprint/jaxrs.xsd">
<!-- JAXRS Application -->
<bean id="customerBean" class="org.keycloak.example.rs.CxfCustomerService" />
<jaxrs:server id="cxfJaxrsServer" address="/customerservice">
<jaxrs:providers>
<bean class="com.fasterxml.jackson.jaxrs.json.JacksonJsonProvider" />
</jaxrs:providers>
<jaxrs:serviceBeans>
<ref component-id="customerBean" />
</jaxrs:serviceBeans>
</jaxrs:server>
</blueprint>
Furthermore, you have to create ${karaf.etc}/org.ops4j.pax.web.context-anyName.cfg file
. It will be treated as factory PID configuration that is tracked by pax-web-runtime
bundle. Such configuration may contain the following properties that correspond to some of the properties of standard web.xml
:
bundle.symbolicName = org.apache.cxf.cxf-rt-transports-http
context.id = default
context.param.keycloak.config.resolver = org.keycloak.adapters.osgi.HierarchicalPathBasedKeycloakConfigResolver
login.config.authMethod = KEYCLOAK
security.cxf.url = /cxf/customerservice/*
security.cxf.roles = admin, user
For full description of available properties in configuration admin file, please refer to Fuse documentation. The properties above have the following meaning:
bundle.symbolicName
andcontext.id
-
Identification of the bundle and its deployment context within
org.ops4j.pax.web.service.WebContainer
. context.param.keycloak.config.resolver
-
Provides value of
keycloak.config.resolver
context parameter to the bundle just the same as inweb.xml
for classic WARs. Available resolvers are described in Configuration Resolvers section. login.config.authMethod
-
Authentication method. Must be
KEYCLOAK
. security.anyName.url
andsecurity.anyName.roles
Values of properties of individual security constraints just as they would be set in
security-constraint/web-resource-collection/url-pattern
andsecurity-constraint/auth-constraint/role-name
inweb.xml
, respectively. Roles are separated by comma and whitespace around it. TheanyName
identifier can be arbitrary but must match for individual properties of the same security constraint.NoteSome Fuse versions contain a bug that requires roles to be separated by
", "
(comma and single space). Make sure you use precisely this notation for separating the roles.
The Import-Package
in META-INF/MANIFEST.MF
must contain at least these imports:
javax.ws.rs;version="[2,3)",
META-INF.cxf;version="[2.7,3.3)",
META-INF.cxf.osgi;version="[2.7,3.3)";resolution:=optional,
org.apache.cxf.transport.http;version="[2.7,3.3)",
org.apache.cxf.*;version="[2.7,3.3)",
com.fasterxml.jackson.jaxrs.json;version="${jackson.version}"
2.1.7.9. Securing Fuse Administration Services
2.1.7.9.1. Using SSH Authentication to Fuse Terminal
Red Hat Single Sign-On mainly addresses use cases for authentication of web applications; however, if your other web services and applications are protected with Red Hat Single Sign-On, protecting non-web administration services such as SSH with Red Hat Single Sign-On credentials is a best pracrice. You can do this using the JAAS login module, which allows remote connection to Red Hat Single Sign-On and verifies credentials based on Resource Owner Password Credentials.
To enable SSH authentication, perform the following procedure.
Procedure
-
In Red Hat Single Sign-On create a client (for example,
ssh-jmx-admin-client
), which will be used for SSH authentication. This client needs to haveDirect Access Grants Enabled
selected toOn
. In the
$FUSE_HOME/etc/org.apache.karaf.shell.cfg
file, update or specify this property:sshRealm=keycloak
Add the
$FUSE_HOME/etc/keycloak-direct-access.json
file with content similar to the following (based on your environment and Red Hat Single Sign-On client settings):{ "realm": "demo", "resource": "ssh-jmx-admin-client", "ssl-required" : "external", "auth-server-url" : "http://localhost:8080/auth", "credentials": { "secret": "password" } }
This file specifies the client application configuration, which is used by JAAS DirectAccessGrantsLoginModule from the
keycloak
JAAS realm for SSH authentication.Start Fuse and install the
keycloak
JAAS realm. The easiest way is to install thekeycloak-jaas
feature, which has the JAAS realm predefined. You can override the feature’s predefined realm by using your ownkeycloak
JAAS realm with higher ranking. For details see the JBoss Fuse documentation.Use these commands in the Fuse terminal:
features:addurl mvn:org.keycloak/keycloak-osgi-features/18.0.19.redhat-00001/xml/features features:install keycloak-jaas
Log in using SSH as
admin
user by typing the following in the terminal:ssh -o PubkeyAuthentication=no -p 8101 admin@localhost
-
Log in with password
password
.
On some later operating systems, you might also need to use the SSH command’s -o option -o HostKeyAlgorithms=+ssh-dss
because later SSH clients do not allow use of the ssh-dss
algorithm, by default. However, by default, it is currently used in JBoss Fuse 7.4.0.
Note that the user needs to have realm role admin
to perform all operations or another role to perform a subset of operations (for example, the viewer role that restricts the user to run only read-only Karaf commands). The available roles are configured in $FUSE_HOME/etc/org.apache.karaf.shell.cfg
or $FUSE_HOME/etc/system.properties
.
2.1.7.9.2. Using JMX authentication
JMX authentication might be necessary if you want to use jconsole or another external tool to remotely connect to JMX through RMI. Otherwise it might be better to use hawt.io/jolokia, since the jolokia agent is installed in hawt.io by default. For more details see Hawtio Admin Console.
To use JMX authentication, perform the following procedure.
Procedure
In the
$FUSE_HOME/etc/org.apache.karaf.management.cfg
file, change the jmxRealm property to:jmxRealm=keycloak
-
Install the
keycloak-jaas
feature and configure the$FUSE_HOME/etc/keycloak-direct-access.json
file as described in the SSH section above. - In jconsole you can use a URL such as:
service:jmx:rmi://localhost:44444/jndi/rmi://localhost:1099/karaf-root
and credentials: admin/password (based on the user with admin privileges according to your environment).
2.1.7.10. Securing the Hawtio Administration Console
To secure the Hawtio Administration Console with Red Hat Single Sign-On, perform the following procedure.
Procedure
-
Create a client in the Red Hat Single Sign-On Admin Console in your realm. For example, in the Red Hat Single Sign-On
demo
realm, create a clienthawtio-client
, specifypublic
as the Access Type, and specify a redirect URI pointing to Hawtio: http://localhost:8181/hawtio/*. Configure corresponding Web Origin (in this case, http://localhost:8181). Setup client scope mapping to include view-profile client role of account client in Scope tab inhawtio-client
client detail. Create the
keycloak-hawtio-client.json
file in the$FUSE_HOME/etc
directory using content similar to that shown in the example below. Change therealm
,resource
, andauth-server-url
properties according to your Red Hat Single Sign-On environment. Theresource
property must point to the client created in the previous step. This file is used by the client (Hawtio JavaScript application) side.{ "realm" : "demo", "clientId" : "hawtio-client", "url" : "http://localhost:8080/auth", "ssl-required" : "external", "public-client" : true }
Create the
keycloak-direct-access.json
file in the$FUSE_HOME/etc
directory using content similar to that shown in the example below. Change therealm
andurl
properties according to your Red Hat Single Sign-On environment. This file is used by JavaScript client.{ "realm" : "demo", "resource" : "ssh-jmx-admin-client", "auth-server-url" : "http://localhost:8080/auth", "ssl-required" : "external", "credentials": { "secret": "password" } }
Create the
keycloak-hawtio.json
file in the$FUSE_HOME/etc
dicrectory using content similar to that shown in the example below. Change therealm
andauth-server-url
properties according to your Red Hat Single Sign-On environment. This file is used by the adapters on the server (JAAS Login module) side.{ "realm" : "demo", "resource" : "jaas", "bearer-only" : true, "auth-server-url" : "http://localhost:8080/auth", "ssl-required" : "external", "use-resource-role-mappings": false, "principal-attribute": "preferred_username" }
Start JBoss Fuse 7.4.0, install the Keycloak feature. Then type in the Karaf terminal:
system:property -p hawtio.keycloakEnabled true system:property -p hawtio.realm keycloak system:property -p hawtio.keycloakClientConfig file://\${karaf.base}/etc/keycloak-hawtio-client.json system:property -p hawtio.rolePrincipalClasses org.keycloak.adapters.jaas.RolePrincipal,org.apache.karaf.jaas.boot.principal.RolePrincipal restart io.hawt.hawtio-war
Go to http://localhost:8181/hawtio and log in as a user from your Red Hat Single Sign-On realm.
Note that the user needs to have the proper realm role to successfully authenticate to Hawtio. The available roles are configured in the
$FUSE_HOME/etc/system.properties
file inhawtio.roles
.
2.1.8. Spring Boot adapter
The Spring Boot Adapter is deprecated and will not be included in the 8.0 and higher versions of RH-SSO. This adapter will be maintained during the lifecycle of RH-SSO 7.x. Users are urged to migrate to Spring Security to integrate their Spring Boot applications with RH-SSO.
2.1.8.1. Installing the Spring Boot adapter
To be able to secure Spring Boot apps you must add the Keycloak Spring Boot adapter JAR to your app. You then have to provide some extra configuration via normal Spring Boot configuration (application.properties
).
The Keycloak Spring Boot adapter takes advantage of Spring Boot’s autoconfiguration so all you need to do is add this adapter Keycloak Spring Boot starter to your project.
Procedure
To add the starter to your project using Maven, add the following to your dependencies:
<dependency> <groupId>org.keycloak</groupId> <artifactId>keycloak-spring-boot-starter</artifactId> </dependency>
Add the Adapter BOM dependency:
<dependencyManagement> <dependencies> <dependency> <groupId>org.keycloak.bom</groupId> <artifactId>keycloak-adapter-bom</artifactId> <version>18.0.19.redhat-00001</version> <type>pom</type> <scope>import</scope> </dependency> </dependencies> </dependencyManagement>
Currently the following embedded containers are supported and do not require any extra dependencies if using the Starter:
- Tomcat
- Undertow
- Jetty
2.1.8.2. Configuring the Spring Boot Adapter
Use the procedure to configure your Spring Boot app to use Red Hat Single Sign-On.
Procedure
Instead of a
keycloak.json
file, you configure the realm for the Spring Boot adapter via the normal Spring Boot configuration. For example:keycloak.realm = demorealm keycloak.auth-server-url = http://127.0.0.1:8080/auth keycloak.ssl-required = external keycloak.resource = demoapp keycloak.credentials.secret = 11111111-1111-1111-1111-111111111111 keycloak.use-resource-role-mappings = true
You can disable the Keycloak Spring Boot Adapter (for example in tests) by setting
keycloak.enabled = false
.-
To configure a Policy Enforcer, unlike keycloak.json, use
policy-enforcer-config
instead of justpolicy-enforcer
. Specify the Jakarta EE security config that would normally go in the
web.xml
.The Spring Boot Adapter will set the
login-method
toKEYCLOAK
and configure thesecurity-constraints
at startup time. Here’s an example configuration:keycloak.securityConstraints[0].authRoles[0] = admin keycloak.securityConstraints[0].authRoles[1] = user keycloak.securityConstraints[0].securityCollections[0].name = insecure stuff keycloak.securityConstraints[0].securityCollections[0].patterns[0] = /insecure keycloak.securityConstraints[1].authRoles[0] = admin keycloak.securityConstraints[1].securityCollections[0].name = admin stuff keycloak.securityConstraints[1].securityCollections[0].patterns[0] = /admin
If you plan to deploy your Spring Application as a WAR then you should not use the Spring Boot Adapter and use the dedicated adapter for the application server or servlet container you are using. Your Spring Boot should also contain a web.xml
file.
2.1.9. Java servlet filter adapter
If you are deploying your Java Servlet application on a platform where there is no Red Hat Single Sign-On adapter you opt to use the servlet filter adapter. This adapter works a bit differently than the other adapters. You do not define security constraints in web.xml. Instead you define a filter mapping using the Red Hat Single Sign-On servlet filter adapter to secure the url patterns you want to secure.
Backchannel logout works a bit differently than the standard adapters. Instead of invalidating the HTTP session it marks the session id as logged out. There’s no standard way to invalidate an HTTP session based on a session id.
<web-app xmlns="http://java.sun.com/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
version="3.0">
<module-name>application</module-name>
<filter>
<filter-name>Keycloak Filter</filter-name>
<filter-class>org.keycloak.adapters.servlet.KeycloakOIDCFilter</filter-class>
</filter>
<filter-mapping>
<filter-name>Keycloak Filter</filter-name>
<url-pattern>/keycloak/*</url-pattern>
<url-pattern>/protected/*</url-pattern>
</filter-mapping>
</web-app>
In the snippet above there are two url-patterns. /protected/* are the files we want protected, while the /keycloak/* url-pattern handles callbacks from the Red Hat Single Sign-On server.
If you need to exclude some paths beneath the configured url-patterns
you can use the Filter init-param keycloak.config.skipPattern
to configure a regular expression that describes a path-pattern for which the keycloak filter should immediately delegate to the filter-chain. By default no skipPattern is configured.
Patterns are matched against the requestURI
without the context-path
. Given the context-path /myapp
a request for /myapp/index.html
will be matched with /index.html
against the skip pattern.
<init-param>
<param-name>keycloak.config.skipPattern</param-name>
<param-value>^/(path1|path2|path3).*</param-value>
</init-param>
Note that you should configure your client in the Red Hat Single Sign-On Admin Console with an Admin URL that points to a secured section covered by the filter’s url-pattern.
The Admin URL will make callbacks to the Admin URL to do things like backchannel logout. So, the Admin URL in this example should be http[s]://hostname/{context-root}/keycloak
.
If you need to customize the session ID mapper, you can configure the fully qualified name of the class in the Filter init-param keycloak.config.idMapper. Session ID mapper is a mapper that is used to map user IDs and session IDs. By default org.keycloak.adapters.spi.InMemorySessionIdMapper is configured.
<init-param>
<param-name>keycloak.config.idMapper</param-name>
<param-value>org.keycloak.adapters.spi.InMemorySessionIdMapper</param-value>
</init-param>
The Red Hat Single Sign-On filter has the same configuration parameters as the other adapters except you must define them as filter init params instead of context params.
To use this filter, include this maven artifact in your WAR poms:
<dependency>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-servlet-filter-adapter</artifactId>
<version>18.0.19.redhat-00001</version>
</dependency>
2.1.10. Security Context
The KeycloakSecurityContext
interface is available if you need to access to the tokens directly. This could be useful if you want to retrieve additional details from the token (such as user profile information) or you want to invoke a RESTful service that is protected by Red Hat Single Sign-On.
In servlet environments it is available in secured invocations as an attribute in HttpServletRequest:
httpServletRequest
.getAttribute(KeycloakSecurityContext.class.getName());
Or, it is available in insecured requests in the HttpSession:
httpServletRequest.getSession()
.getAttribute(KeycloakSecurityContext.class.getName());
2.1.11. Error handling
Red Hat Single Sign-On has some error handling facilities for servlet based client adapters. When an error is encountered in authentication, Red Hat Single Sign-On will call HttpServletResponse.sendError()
. You can set up an error-page within your web.xml
file to handle the error however you want. Red Hat Single Sign-On can throw 400, 401, 403, and 500 errors.
<error-page>
<error-code>403</error-code>
<location>/ErrorHandler</location>
</error-page>
Red Hat Single Sign-On also sets a HttpServletRequest
attribute that you can retrieve. The attribute name is org.keycloak.adapters.spi.AuthenticationError
, which should be casted to org.keycloak.adapters.OIDCAuthenticationError
.
For example:
import org.keycloak.adapters.OIDCAuthenticationError;
import org.keycloak.adapters.OIDCAuthenticationError.Reason;
...
OIDCAuthenticationError error = (OIDCAuthenticationError) httpServletRequest
.getAttribute('org.keycloak.adapters.spi.AuthenticationError');
Reason reason = error.getReason();
System.out.println(reason.name());
2.1.12. Logout
You can log out of a web application in multiple ways. For Jakarta EE servlet containers, you can call HttpServletRequest.logout()
. For other browser applications, you can redirect the browser to http://auth-server/auth/realms/{realm-name}/protocol/openid-connect/logout
, which logs the user out if that user has an SSO session with his browser. The actual logout is done once the user confirms the logout. You can optionally include parameters such as id_token_hint
, post_logout_redirect_uri
, client_id
and others as described in the OpenID Connect RP-Initiated Logout. As a result, that logout does not need to be explicitly confirmed by the user if you include the id_token_hint
parameter. After logout, the user will be automatically redirected to the specified post_logout_redirect_uri
as long as it is provided. Note that you need to include either the client_id
or id_token_hint
parameter in case that post_logout_redirect_uri
is included.
If you want to avoid logging out of an external identity provider as part of the logout process, you can supply the parameter initiating_idp
, with the value being the identity (alias) of the identity provider in question. This parameter is useful when the logout endpoint is invoked as part of single logout initiated by the external identity provider. The parameter initiating_idp
is the supported parameter of the Red Hat Single Sign-On logout endpoint in addition to the parameters described in the RP-Initiated Logout specification.
When using the HttpServletRequest.logout()
option the adapter executes a back-channel POST call against the Red Hat Single Sign-On server passing the refresh token. If the method is executed from an unprotected page (a page that does not check for a valid token) the refresh token can be unavailable and, in that case, the adapter skips the call. For this reason, using a protected page to execute HttpServletRequest.logout()
is recommended so that current tokens are always taken into account and an interaction with the Red Hat Single Sign-On server is performed if needed.
2.1.13. Parameters forwarding
The Red Hat Single Sign-On initial authorization endpoint request has support for various parameters. Most of the parameters are described in OIDC specification. Some parameters are added automatically by the adapter based on the adapter configuration. However, there are also a few parameters that can be added on a per-invocation basis. When you open the secured application URI, the particular parameter will be forwarded to the Red Hat Single Sign-On authorization endpoint.
For example, if you request an offline token, then you can open the secured application URI with the scope
parameter like:
http://myappserver/mysecuredapp?scope=offline_access
and the parameter scope=offline_access
will be automatically forwarded to the Red Hat Single Sign-On authorization endpoint.
The supported parameters are:
-
scope - Use a space-delimited list of scopes. A space-delimited list typically references Client scopes defined on particular client. Note that the scope
openid
will be always be added to the list of scopes by the adapter. For example, if you enter the scope optionsaddress phone
, then the request to Red Hat Single Sign-On will contain the scope parameterscope=openid address phone
. prompt - Red Hat Single Sign-On supports these settings:
-
login
- SSO will be ignored and the Red Hat Single Sign-On login page will be always shown, even if the user is already authenticated -
consent
- Applicable only for the clients withConsent Required
. If it is used, the Consent page will always be displayed, even if the user previously granted consent to this client. -
none
- The login page will never be shown; instead the user will be redirected to the application, with an error if the user is not yet authenticated. This setting allows you to create a filter/interceptor on the application side and show a custom error page to the user. See more details in the specification.
-
-
max_age - Used only if a user is already authenticated. Specifies maximum permitted time for the authentication to persist, measured from when the user authenticated. If user is authenticated longer than
maxAge
, the SSO is ignored and he must re-authenticate. - login_hint - Used to pre-fill the username/email field on the login form.
- kc_idp_hint - Used to tell Red Hat Single Sign-On to skip showing login page and automatically redirect to specified identity provider instead. More info in the Identity Provider documentation.
Most of the parameters are described in the OIDC specification. The only exception is parameter kc_idp_hint
, which is specific to Red Hat Single Sign-On and contains the name of the identity provider to automatically use. For more information see the Identity Brokering
section in the Server Administration Guide.
If you open the URL using the attached parameters, the adapter will not redirect you to Red Hat Single Sign-On if you are already authenticated in the application. For example, opening http://myappserver/mysecuredapp?prompt=login will not automatically redirect you to the Red Hat Single Sign-On login page if you are already authenticated to the application mysecuredapp
. This behavior may be changed in the future.
2.1.14. Client authentication
When a confidential OIDC client needs to send a backchannel request (for example, to exchange code for the token, or to refresh the token) it needs to authenticate against the Red Hat Single Sign-On server. By default, there are three ways to authenticate the client: client ID and client secret, client authentication with signed JWT, or client authentication with signed JWT using client secret.
2.1.14.1. Client ID and Client Secret
This is the traditional method described in the OAuth2 specification. The client has a secret, which needs to be known to both the adapter (application) and the Red Hat Single Sign-On server. You can generate the secret for a particular client in the Red Hat Single Sign-On Admin Console, and then paste this secret into the keycloak.json
file on the application side:
"credentials": {
"secret": "19666a4f-32dd-4049-b082-684c74115f28"
}
2.1.14.2. Client authentication with Signed JWT
This is based on the RFC7523 specification. It works this way:
-
The client must have the private key and certificate. For Red Hat Single Sign-On this is available through the traditional
keystore
file, which is either available on the client application’s classpath or somewhere on the file system. - Once the client application is started, it allows to download its public key in JWKS format using a URL such as http://myhost.com/myapp/k_jwks, assuming that http://myhost.com/myapp is the base URL of your client application. This URL can be used by Red Hat Single Sign-On (see below).
-
During authentication, the client generates a JWT token and signs it with its private key and sends it to Red Hat Single Sign-On in the particular backchannel request (for example, code-to-token request) in the
client_assertion
parameter. Red Hat Single Sign-On must have the public key or certificate of the client so that it can verify the signature on JWT. In Red Hat Single Sign-On you need to configure client credentials for your client. First you need to choose
Signed JWT
as the method of authenticating your client in the tabCredentials
in the Admin Console. Then you can choose to either in the tabKeys
:-
Configure the JWKS URL where Red Hat Single Sign-On can download the client’s public keys. This can be a URL such as http://myhost.com/myapp/k_jwks (see details above). This option is the most flexible, since the client can rotate its keys anytime and Red Hat Single Sign-On then always downloads new keys when needed without needing to change the configuration. More accurately, Red Hat Single Sign-On downloads new keys when it sees the token signed by an unknown
kid
(Key ID). - Upload the client’s public key or certificate, either in PEM format, in JWK format, or from the keystore. With this option, the public key is hardcoded and must be changed when the client generates a new key pair. You can even generate your own keystore from the Red Hat Single Sign-On Admin Console if you don’t have your own available. For more details on how to set up the Red Hat Single Sign-On Admin Console, see the Server Administration Guide.
-
Configure the JWKS URL where Red Hat Single Sign-On can download the client’s public keys. This can be a URL such as http://myhost.com/myapp/k_jwks (see details above). This option is the most flexible, since the client can rotate its keys anytime and Red Hat Single Sign-On then always downloads new keys when needed without needing to change the configuration. More accurately, Red Hat Single Sign-On downloads new keys when it sees the token signed by an unknown
For set up on the adapter side you need to have something like this in your keycloak.json
file:
"credentials": {
"jwt": {
"client-keystore-file": "classpath:keystore-client.jks",
"client-keystore-type": "JKS",
"client-keystore-password": "storepass",
"client-key-password": "keypass",
"client-key-alias": "clientkey",
"algorithm": "RS256",
"token-expiration": 10
}
}
With this configuration, the keystore file keystore-client.jks
must be available on classpath in your WAR. If you do not use the prefix classpath:
you can point to any file on the file system where the client application is running.
The algorithm
field specifies the algorithm used for the Signed JWT and it defaults to RS256
. This field should be in sync with the key pair. For example, the RS256
algorithm needs a RSA key pair while the ES256
algorithm requires an EC key pair. Please refer to Cryptographic Algorithms for Digital Signatures and MACs for more information.
2.1.15. Multi Tenancy
Multi Tenancy, in our context, means that a single target application (WAR) can be secured with multiple Red Hat Single Sign-On realms. The realms can be located on the same Red Hat Single Sign-On instance or on different instances.
In practice, this means that the application needs to have multiple keycloak.json
adapter configuration files.
You could have multiple instances of your WAR with different adapter configuration files deployed to different context-paths. However, this may be inconvenient and you may also want to select the realm based on something else than context-path.
Red Hat Single Sign-On makes it possible to have a custom config resolver so you can choose what adapter config is used for each request.
To achieve this first you need to create an implementation of org.keycloak.adapters.KeycloakConfigResolver
. For example:
package example;
import org.keycloak.adapters.KeycloakConfigResolver;
import org.keycloak.adapters.KeycloakDeployment;
import org.keycloak.adapters.KeycloakDeploymentBuilder;
public class PathBasedKeycloakConfigResolver implements KeycloakConfigResolver {
@Override
public KeycloakDeployment resolve(OIDCHttpFacade.Request request) {
if (path.startsWith("alternative")) {
KeycloakDeployment deployment = cache.get(realm);
if (null == deployment) {
InputStream is = getClass().getResourceAsStream("/tenant1-keycloak.json");
return KeycloakDeploymentBuilder.build(is);
}
} else {
InputStream is = getClass().getResourceAsStream("/default-keycloak.json");
return KeycloakDeploymentBuilder.build(is);
}
}
}
You also need to configure which KeycloakConfigResolver
implementation to use with the keycloak.config.resolver
context-param in your web.xml
:
<web-app>
...
<context-param>
<param-name>keycloak.config.resolver</param-name>
<param-value>example.PathBasedKeycloakConfigResolver</param-value>
</context-param>
</web-app>
2.1.16. Application clustering
This chapter is related to supporting clustered applications deployed to JBoss EAP.
There are a few options available depending on whether your application is:
- Stateless or stateful
- Distributable (replicated http session) or non-distributable
- Relying on sticky sessions provided by load balancer
- Hosted on same domain as Red Hat Single Sign-On
Dealing with clustering is not quite as simple as for a regular application. Mainly due to the fact that both the browser and the server-side application sends requests to Red Hat Single Sign-On, so it’s not as simple as enabling sticky sessions on your load balancer.
2.1.16.1. Stateless token store
By default, the web application secured by Red Hat Single Sign-On uses the HTTP session to store security context. This means that you either have to enable sticky sessions or replicate the HTTP session.
As an alternative to storing the security context in the HTTP session the adapter can be configured to store this in a cookie instead. This is useful if you want to make your application stateless or if you don’t want to store the security context in the HTTP session.
To use the cookie store for saving the security context, edit your applications WEB-INF/keycloak.json
and add:
"token-store": "cookie"
The default value for token-store
is session
, which stores the security context in the HTTP session.
One limitation of using the cookie store is that the whole security context is passed in the cookie for every HTTP request. This may impact performance.
Another small limitation is limited support for Single-Sign Out. It works without issues if you init servlet logout (HttpServletRequest.logout) from the application itself as the adapter will delete the KEYCLOAK_ADAPTER_STATE cookie. However, back-channel logout initialized from a different application isn’t propagated by Red Hat Single Sign-On to applications using cookie store. Hence it’s recommended to use a short value for the access token timeout (for example 1 minute).
Some load balancers do not allow any configuration of the sticky session cookie name or contents, such as Amazon ALB. For these, it is recommended to set the shouldAttachRoute
option to false
.
2.1.16.2. Relative URI optimization
In deployment scenarios where Red Hat Single Sign-On and the application is hosted on the same domain (through a reverse proxy or load balancer) it can be convenient to use relative URI options in your client configuration.
With relative URIs the URI is resolved as relative to the URL used to access Red Hat Single Sign-On.
For example if the URL to your application is https://acme.org/myapp
and the URL to Red Hat Single Sign-On is https://acme.org/auth
, then you can use the redirect-uri /myapp
instead of https://acme.org/myapp
.
2.1.16.3. Admin URL configuration
Admin URL for a particular client can be configured in the Red Hat Single Sign-On Admin Console. It’s used by the Red Hat Single Sign-On server to send backend requests to the application for various tasks, like logout users or push revocation policies.
For example the way backchannel logout works is:
- User sends logout request from one application
- The application sends logout request to Red Hat Single Sign-On
- The Red Hat Single Sign-On server invalidates the user session
- The Red Hat Single Sign-On server then sends a backchannel request to application with an admin url that are associated with the session
- When an application receives the logout request it invalidates the corresponding HTTP session
If admin URL contains ${application.session.host}
it will be replaced with the URL to the node associated with the HTTP session.
2.1.16.4. Registration of application nodes
The previous section describes how Red Hat Single Sign-On can send logout request to node associated with a specific HTTP session. However, in some cases admin may want to propagate admin tasks to all registered cluster nodes, not just one of them. For example to push a new not before policy to the application or to logout all users from the application.
In this case Red Hat Single Sign-On needs to be aware of all application cluster nodes, so it can send the event to all of them. To achieve this, we support auto-discovery mechanism:
- When a new application node joins the cluster, it sends a registration request to the Red Hat Single Sign-On server
- The request may be re-sent to Red Hat Single Sign-On in configured periodic intervals
- If the Red Hat Single Sign-On server doesn’t receive a re-registration request within a specified timeout then it automatically unregisters the specific node
- The node is also unregistered in Red Hat Single Sign-On when it sends an unregistration request, which is usually during node shutdown or application undeployment. This may not work properly for forced shutdown when undeployment listeners are not invoked, which results in the need for automatic unregistration
Sending startup registrations and periodic re-registration is disabled by default as it’s only required for some clustered applications.
To enable the feature edit the WEB-INF/keycloak.json
file for your application and add:
"register-node-at-startup": true,
"register-node-period": 600,
This means the adapter will send the registration request on startup and re-register every 10 minutes.
In the Red Hat Single Sign-On Admin Console you can specify the maximum node re-registration timeout (should be larger than register-node-period from the adapter configuration). You can also manually add and remove cluster nodes in through the Admin Console, which is useful if you don’t want to rely on the automatic registration feature or if you want to remove stale application nodes in the event your not using the automatic unregistration feature.
2.1.16.5. Refresh token in each request
By default the application adapter will only refresh the access token when it’s expired. However, you can also configure the adapter to refresh the token on every request. This may have a performance impact as your application will send more requests to the Red Hat Single Sign-On server.
To enable the feature edit the WEB-INF/keycloak.json
file for your application and add:
"always-refresh-token": true
This may have a significant impact on performance. Only enable this feature if you can’t rely on backchannel messages to propagate logout and not before policies. Another thing to consider is that by default access tokens has a short expiration so even if logout is not propagated the token will expire within minutes of the logout.
2.2. JavaScript adapter
Red Hat Single Sign-On comes with a client-side JavaScript library that can be used to secure HTML5/JavaScript applications. The JavaScript adapter has built-in support for Cordova applications.
A good practice is to include the JavaScript adapter in your application using a package manager like NPM or Yarn. The keycloak-js
package is available on the following locations:
Alternatively, the library can be retrieved directly from the Red Hat Single Sign-On server at /auth/js/keycloak.js
and is also distributed as a ZIP archive.
One important thing to note about using client-side applications is that the client has to be a public client as there is no secure way to store client credentials in a client-side application. This makes it very important to make sure the redirect URIs you have configured for the client are correct and as specific as possible.
To use the JavaScript adapter you must first create a client for your application in the Red Hat Single Sign-On Admin Console. Make sure public
is selected for Access Type
. You achieve this in Capability config by turning OFF client authentication toggle.
You also need to configure Valid Redirect URIs
and Web Origins
. Be as specific as possible as failing to do so may result in a security vulnerability.
Once the client is created click on the Action
tab in the upper right corner and select Download adapter config
. Select Keycloak OIDC JSON
for Format Option
then click Download
. The downloaded keycloak.json
file should be hosted on your web server at the same location as your HTML pages.
Alternatively, you can skip the configuration file and manually configure the adapter.
The following example shows how to initialize the JavaScript adapter:
<html>
<head>
<script src="keycloak.js"></script>
<script>
function initKeycloak() {
const options = {};
const keycloak = new Keycloak();
keycloak.init(options)
.then(function(authenticated) {
console.log('keycloak:' + (authenticated ? 'authenticated' : 'not authenticated'));
}).catch(function(error) {
for (const property in error) {
console.error(`${property}: ${error[property]}`);
}
});
}
</script>
</head>
<body onload="initKeycloak()">
<!-- your page content goes here -->
</body>
</html>
If the keycloak.json
file is in a different location you can specify it:
const keycloak = new Keycloak('http://localhost:8080/myapp/keycloak.json');
Alternatively, you can pass in a JavaScript object with the required configuration instead:
const keycloak = new Keycloak({
url: 'http://keycloak-server$/auth',
realm: 'myrealm',
clientId: 'myapp'
});
By default to authenticate you need to call the login
function. However, there are two options available to make the adapter automatically authenticate. You can pass login-required
or check-sso
to the init function. login-required
will authenticate the client if the user is logged-in to Red Hat Single Sign-On or display the login page if not. check-sso
will only authenticate the client if the user is already logged-in, if the user is not logged-in the browser will be redirected back to the application and remain unauthenticated.
You can configure a silent check-sso
option. With this feature enabled, your browser won’t do a full redirect to the Red Hat Single Sign-On server and back to your application, but this action will be performed in a hidden iframe, so your application resources only need to be loaded and parsed once by the browser when the app is initialized and not again after the redirect back from Red Hat Single Sign-On to your app. This is particularly useful in case of SPAs (Single Page Applications).
To enable the silent check-sso
, you have to provide a silentCheckSsoRedirectUri
attribute in the init method. This URI needs to be a valid endpoint in the application (and of course it must be configured as a valid redirect for the client in the Red Hat Single Sign-On Admin Console):
keycloak.init({
onLoad: 'check-sso',
silentCheckSsoRedirectUri: window.location.origin + '/silent-check-sso.html'
})
The page at the silent check-sso redirect uri is loaded in the iframe after successfully checking your authentication state and retrieving the tokens from the Red Hat Single Sign-On server. It has no other task than sending the received tokens to the main application and should only look like this:
<html>
<body>
<script>
parent.postMessage(location.href, location.origin)
</script>
</body>
</html>
Please keep in mind that this page at the specified location must be provided by the application itself and is not part of the JavaScript adapter!
Silent check-sso
functionality is limited in some modern browsers. Please see the Modern Browsers with Tracking Protection Section.
To enable login-required
set onLoad
to login-required
and pass to the init method:
keycloak.init({
onLoad: 'login-required'
})
After the user is authenticated the application can make requests to RESTful services secured by Red Hat Single Sign-On by including the bearer token in the Authorization
header. For example:
const loadData = function () {
document.getElementById('username').innerText = keycloak.subject;
const url = 'http://localhost:8080/restful-service';
const req = new XMLHttpRequest();
req.open('GET', url, true);
req.setRequestHeader('Accept', 'application/json');
req.setRequestHeader('Authorization', 'Bearer ' + keycloak.token);
req.onreadystatechange = function () {
if (req.readyState == 4) {
if (req.status == 200) {
alert('Success');
} else if (req.status == 403) {
alert('Forbidden');
}
}
}
req.send();
};
One thing to keep in mind is that the access token by default has a short life expiration so you may need to refresh the access token prior to sending the request. You can do this by the updateToken
method. The updateToken
method returns a promise which makes it easy to invoke the service only if the token was successfully refreshed and display an error to the user if it wasn’t. For example:
keycloak.updateToken(30).then(function() {
loadData();
}).catch(function() {
alert('Failed to refresh token');
});
2.2.1. Session Status iframe
By default, the JavaScript adapter creates a hidden iframe that is used to detect if a Single-Sign Out has occurred. This does not require any network traffic, instead the status is retrieved by looking at a special status cookie. This feature can be disabled by setting checkLoginIframe: false
in the options passed to the init
method.
You should not rely on looking at this cookie directly. Its format can change and it’s also associated with the URL of the Red Hat Single Sign-On server, not your application.
Session Status iframe functionality is limited in some modern browsers. Please see Modern Browsers with Tracking Protection Section.
2.2.2. Implicit and hybrid flow
By default, the JavaScript adapter uses the Authorization Code flow.
With this flow the Red Hat Single Sign-On server returns an authorization code, not an authentication token, to the application. The JavaScript adapter exchanges the code
for an access token and a refresh token after the browser is redirected back to the application.
Red Hat Single Sign-On also supports the Implicit flow where an access token is sent immediately after successful authentication with Red Hat Single Sign-On. This may have better performance than standard flow, as there is no additional request to exchange the code for tokens, but it has implications when the access token expires.
However, sending the access token in the URL fragment can be a security vulnerability. For example the token could be leaked through web server logs and or browser history.
To enable implicit flow, you need to enable the Implicit Flow Enabled
flag for the client in the Red Hat Single Sign-On Admin Console. You also need to pass the parameter flow
with value implicit
to init
method:
keycloak.init({
flow: 'implicit'
})
One thing to note is that only an access token is provided and there is no refresh token. This means that once the access token has expired the application has to do the redirect to the Red Hat Single Sign-On again to obtain a new access token.
Red Hat Single Sign-On also supports the Hybrid flow.
This requires the client to have both the Standard Flow Enabled
and Implicit Flow Enabled
flags enabled in the admin console. The Red Hat Single Sign-On server will then send both the code and tokens to your application. The access token can be used immediately while the code can be exchanged for access and refresh tokens. Similar to the implicit flow, the hybrid flow is good for performance because the access token is available immediately. But, the token is still sent in the URL, and the security vulnerability mentioned earlier may still apply.
One advantage in the Hybrid flow is that the refresh token is made available to the application.
For the Hybrid flow, you need to pass the parameter flow
with value hybrid
to the init
method:
keycloak.init({
flow: 'hybrid'
})
2.2.3. Hybrid Apps with Cordova
Keycloak support hybrid mobile apps developed with Apache Cordova. The JavaScript adapter has two modes for this: cordova
and cordova-native
:
The default is cordova, which the adapter will automatically select if no adapter type has been configured and window.cordova is present. When logging in, it will open an InApp Browser that lets the user interact with Red Hat Single Sign-On and afterwards returns to the app by redirecting to http://localhost
. Because of this, you must whitelist this URL as a valid redirect-uri in the client configuration section of the Admin Console.
While this mode is easy to set up, it also has some disadvantages:
- The InApp-Browser is a browser embedded in the app and is not the phone’s default browser. Therefore it will have different settings and stored credentials will not be available.
- The InApp-Browser might also be slower, especially when rendering more complex themes.
- There are security concerns to consider, before using this mode, such as that it is possible for the app to gain access to the credentials of the user, as it has full control of the browser rendering the login page, so do not allow its use in apps you do not trust.
Use this example app to help you get started: https://github.com/keycloak/keycloak/tree/master/examples/cordova
The alternative mode cordova-native
takes a different approach. It opens the login page using the system’s browser. After the user has authenticated, the browser redirects back into the app using a special URL. From there, the Red Hat Single Sign-On adapter can finish the login by reading the code or token from the URL.
You can activate the native mode by passing the adapter type cordova-native
to the init
method:
keycloak.init({
adapter: 'cordova-native'
})
This adapter required two additional plugins:
- cordova-plugin-browsertab: allows the app to open webpages in the system’s browser
- cordova-plugin-deeplinks: allow the browser to redirect back to your app by special URLs
The technical details for linking to an app differ on each platform and special setup is needed. Please refer to the Android and iOS sections of the deeplinks plugin documentation for further instructions.
There are different kinds of links for opening apps: custom schemes (i.e. myapp://login
or android-app://com.example.myapp/https/example.com/login
) and Universal Links (iOS)) / Deep Links (Android). While the former are easier to set up and tend to work more reliably, the later offer extra security as they are unique and only the owner of a domain can register them. Custom-URLs are deprecated on iOS. We recommend that you use universal links, combined with a fallback site with a custom-url link on it for best reliability.
Furthermore, we recommend the following steps to improve compatibility with the Keycloak Adapter:
-
Universal Links on iOS seem to work more reliably with
response-mode
set toquery
-
To prevent Android from opening a new instance of your app on redirect add the following snippet to
config.xml
:
<preference name="AndroidLaunchMode" value="singleTask" />
There is an example app that shows how to use the native-mode: https://github.com/keycloak/keycloak/tree/master/examples/cordova-native
2.2.4. Custom Adapters
Sometimes it’s necessary to run the JavaScript client in environments that are not supported by default (such as Capacitor). To make it possible to use the JavasScript client in these kind of unknown environments is possible to pass a custom adapter. For example a 3rd party library could provide such an adapter to make it possible to run the JavaScript client without issues:
import Keycloak from 'keycloak-js';
import KeycloakCapacitorAdapter from 'keycloak-capacitor-adapter';
const keycloak = new Keycloak();
keycloak.init({
adapter: KeycloakCapacitorAdapter,
});
This specific package does not exist, but it gives a pretty good example of how such an adapter could be passed into the client.
It’s also possible to make your own adapter, to do so you will have to implement the methods described in the KeycloakAdapter
interface. For example the following TypeScript code ensures that all the methods are properly implemented:
import Keycloak, { KeycloakAdapter } from 'keycloak-js';
// Implement the 'KeycloakAdapter' interface so that all required methods are guaranteed to be present.
const MyCustomAdapter: KeycloakAdapter = {
login(options) {
// Write your own implementation here.
}
// The other methods go here...
};
const keycloak = new Keycloak();
keycloak.init({
adapter: MyCustomAdapter,
});
Naturally you can also do this without TypeScript by omitting the type information, but ensuring implementing the interface properly will then be left entirely up to you.
2.2.5. Earlier Browsers
The JavaScript adapter depends on Base64 (window.btoa and window.atob), HTML5 History API and optionally the Promise API. If you need to support browsers that do not have these available (for example, IE9) you need to add polyfillers.
Example polyfill libraries:
- Base64 - https://github.com/davidchambers/Base64.js
- HTML5 History - https://github.com/devote/HTML5-History-API
- Promise - https://github.com/stefanpenner/es6-promise
2.2.6. Modern Browsers with Tracking Protection
In the latest versions of some browsers various cookies policies are applied to prevent tracking of the users by third-parties, like SameSite in Chrome or completely blocked third-party cookies. It is expected that those policies will become even more restrictive and adopted by other browsers over time, eventually leading to cookies in third-party contexts to be completely unsupported and blocked by the browsers. The adapter features affected by this might get deprecated in the future.
Javascript adapter relies on third-party cookies for Session Status iframe, silent check-sso
and partially also for regular (non-silent) check-sso
. Those features have limited functionality or are completely disabled based on how the browser is restrictive regarding cookies. The adapter tries to detect this setting and reacts accordingly.
2.2.6.1. Browsers with "SameSite=Lax by Default" Policy
All features are supported if SSL / TLS connection is configured on the Red Hat Single Sign-On side as well as on the application side. Affected is for example Chrome starting with version 84.
2.2.6.2. Browsers with Blocked Third-Party Cookies
Session Status iframe is not supported and is automatically disabled if such browser behavior is detected by the JS adapter. This means the adapter cannot use session cookie for Single Sign-Out detection and have to rely purely on tokens. This implies that when user logs out in another window, the application using JavaScript adapter won’t be logged out until it tries to refresh the Access Token. Therefore, it is recommended to set Access Token Lifespan to relatively short time, so that the logout is detected rather sooner than later. Please see Session and Token Timeouts.
Silent check-sso
is not supported and falls back to regular (non-silent) check-sso
by default. This behaviour can be changed by setting silentCheckSsoFallback: false
in the options passed to the init
method. In this case, check-sso
will be completely disabled if restrictive browser behavior is detected.
Regular check-sso
is affected as well. Since Session Status iframe is unsupported, an additional redirect to Red Hat Single Sign-On has to be made when the adapter is initialized to check user’s login status. This is different from standard behavior when the iframe is used to tell whether the user is logged in, and the redirect is performed only when logged out.
An affected browser is for example Safari starting with version 13.1.
2.2.7. JavaScript Adapter Reference
2.2.7.1. Constructor
new Keycloak();
new Keycloak('http://localhost/keycloak.json');
new Keycloak({ url: 'http://localhost/auth', realm: 'myrealm', clientId: 'myApp' });
2.2.7.2. Properties
- authenticated
-
Is
true
if the user is authenticated,false
otherwise. - token
-
The base64 encoded token that can be sent in the
Authorization
header in requests to services. - tokenParsed
- The parsed token as a JavaScript object.
- subject
- The user id.
- idToken
- The base64 encoded ID token.
- idTokenParsed
- The parsed id token as a JavaScript object.
- realmAccess
- The realm roles associated with the token.
- resourceAccess
- The resource roles associated with the token.
- refreshToken
- The base64 encoded refresh token that can be used to retrieve a new token.
- refreshTokenParsed
- The parsed refresh token as a JavaScript object.
- timeSkew
- The estimated time difference between the browser time and the Red Hat Single Sign-On server in seconds. This value is just an estimation, but is accurate enough when determining if a token is expired or not.
- responseMode
- Response mode passed in init (default value is fragment).
- flow
- Flow passed in init.
- adapter
Allows you to override the way that redirects and other browser-related functions will be handled by the library. Available options:
- "default" - the library uses the browser api for redirects (this is the default)
- "cordova" - the library will try to use the InAppBrowser cordova plugin to load keycloak login/registration pages (this is used automatically when the library is working in a cordova ecosystem)
- "cordova-native" - the library tries to open the login and registration page using the phone’s system browser using the BrowserTabs cordova plugin. This requires extra setup for redirecting back to the app (see Section 2.2.3, “Hybrid Apps with Cordova”).
- "custom" - allows you to implement a custom adapter (only for advanced use cases)
- responseType
- Response type sent to Red Hat Single Sign-On with login requests. This is determined based on the flow value used during initialization, but can be overridden by setting this value.
2.2.7.3. Methods
init(options)
Called to initialize the adapter.
Options is an Object, where:
-
useNonce - Adds a cryptographic nonce to verify that the authentication response matches the request (default is
true
). -
onLoad - Specifies an action to do on load. Supported values are
login-required
orcheck-sso
. - silentCheckSsoRedirectUri - Set the redirect uri for silent authentication check if onLoad is set to 'check-sso'.
-
silentCheckSsoFallback - Enables fall back to regular
check-sso
when silentcheck-sso
is not supported by the browser (default istrue
). - token - Set an initial value for the token.
- refreshToken - Set an initial value for the refresh token.
- idToken - Set an initial value for the id token (only together with token or refreshToken).
-
scope - Set the default scope parameter to the Red Hat Single Sign-On login endpoint. Use a space-delimited list of scopes. Those typically reference Client scopes defined on a particular client. Note that the scope
openid
will always be added to the list of scopes by the adapter. For example, if you enter the scope optionsaddress phone
, then the request to Red Hat Single Sign-On will contain the scope parameterscope=openid address phone
. Note that the default scope specified here is overwritten if thelogin()
options specify scope explicitly. - timeSkew - Set an initial value for skew between local time and Red Hat Single Sign-On server in seconds (only together with token or refreshToken).
-
checkLoginIframe - Set to enable/disable monitoring login state (default is
true
). - checkLoginIframeInterval - Set the interval to check login state (default is 5 seconds).
-
responseMode - Set the OpenID Connect response mode send to Red Hat Single Sign-On server at login request. Valid values are
query
orfragment
. Default value isfragment
, which means that after successful authentication will Red Hat Single Sign-On redirect to JavaScript application with OpenID Connect parameters added in URL fragment. This is generally safer and recommended overquery
. -
flow - Set the OpenID Connect flow. Valid values are
standard
,implicit
orhybrid
. -
enableLogging - Enables logging messages from Keycloak to the console (default is
false
). pkceMethod - The method for Proof Key Code Exchange (PKCE) to use. Configuring this value enables the PKCE mechanism. Available options:
- "S256" - The SHA256 based PKCE method
- messageReceiveTimeout - Set a timeout in milliseconds for waiting for message responses from the Keycloak server. This is used, for example, when waiting for a message during 3rd party cookies check. The default value is 10000.
Returns a promise that resolves when initialization completes.
login(options)
Redirects to login form.
Options is an optional Object, where:
- redirectUri - Specifies the uri to redirect to after login.
-
prompt - This parameter allows to slightly customize the login flow on the Red Hat Single Sign-On server side. For example enforce displaying the login screen in case of value
login
. See Parameters Forwarding Section for the details and all the possible values of theprompt
parameter. -
maxAge - Used just if user is already authenticated. Specifies maximum time since the authentication of user happened. If user is already authenticated for longer time than
maxAge
, the SSO is ignored and he will need to re-authenticate again. - loginHint - Used to pre-fill the username/email field on the login form.
-
scope - Override the scope configured in
init
with a different value for this specific login. - idpHint - Used to tell Red Hat Single Sign-On to skip showing the login page and automatically redirect to the specified identity provider instead. More info in the Identity Provider documentation.
-
acr - Contains the information about
acr
claim, which will be sent insideclaims
parameter to the Red Hat Single Sign-On server. Typical usage is for step-up authentication. Example of use{ values: ["silver", "gold"], essential: true }
. See OpenID Connect specification and Step-up authentication documentation for more details. -
action - If value is
register
then user is redirected to registration page, if the value isUPDATE_PASSWORD
then the user will be redirected to the reset password page (if not authenticated will send user to login page first and redirect after authenticated), otherwise to login page. - locale - Sets the 'ui_locales' query param in compliance with section 3.1.2.1 of the OIDC 1.0 specification.
-
cordovaOptions - Specifies the arguments that are passed to the Cordova in-app-browser (if applicable). Options
hidden
andlocation
are not affected by these arguments. All available options are defined at https://cordova.apache.org/docs/en/latest/reference/cordova-plugin-inappbrowser/. Example of use:{ zoom: "no", hardwareback: "yes" }
;
createLoginUrl(options)
Returns the URL to login form.
Options is an optional Object, which supports same options as the function login
.
logout(options)
Redirects to logout.
Options is an Object, where:
- redirectUri - Specifies the uri to redirect to after logout.
createLogoutUrl(options)
Returns the URL to log out the user.
Options is an Object, where:
- redirectUri - Specifies the uri to redirect to after logout.
register(options)
Redirects to registration form. Shortcut for login with option action = 'register'
Options are same as for the login method but 'action' is set to 'register'
createRegisterUrl(options)
Returns the url to registration page. Shortcut for createLoginUrl with option action = 'register'
Options are same as for the createLoginUrl method but 'action' is set to 'register'
accountManagement()
Redirects to the Account Management Console.
createAccountUrl(options)
Returns the URL to the Account Management Console.
Options is an Object, where:
- redirectUri - Specifies the uri to redirect to when redirecting back to the application.
hasRealmRole(role)
Returns true if the token has the given realm role.
hasResourceRole(role, resource)
Returns true if the token has the given role for the resource (resource is optional, if not specified clientId is used).
loadUserProfile()
Loads the users profile.
Returns a promise that resolves with the profile.
For example:
keycloak.loadUserProfile()
.then(function(profile) {
alert(JSON.stringify(profile, null, " "))
}).catch(function() {
alert('Failed to load user profile');
});
isTokenExpired(minValidity)
Returns true if the token has less than minValidity seconds left before it expires (minValidity is optional, if not specified 0 is used).
updateToken(minValidity)
If the token expires within minValidity seconds (minValidity is optional, if not specified 5 is used) the token is refreshed. If -1 is passed as the minValidity, the token will be forcibly refreshed. If the session status iframe is enabled, the session status is also checked.
Returns a promise that resolves with a boolean indicating whether or not the token has been refreshed.
For example:
keycloak.updateToken(5)
.then(function(refreshed) {
if (refreshed) {
alert('Token was successfully refreshed');
} else {
alert('Token is still valid');
}
}).catch(function() {
alert('Failed to refresh the token, or the session has expired');
});
clearToken()
Clear authentication state, including tokens. This can be useful if application has detected the session was expired, for example if updating token fails.
Invoking this results in onAuthLogout callback listener being invoked.
2.2.7.4. Callback Events
The adapter supports setting callback listeners for certain events. Keep in mind that these have to be set before the call to the init
function.
For example:
keycloak.onAuthSuccess = function() { alert('authenticated'); }
The available events are:
- onReady(authenticated) - Called when the adapter is initialized.
- onAuthSuccess - Called when a user is successfully authenticated.
- onAuthError - Called if there was an error during authentication.
- onAuthRefreshSuccess - Called when the token is refreshed.
- onAuthRefreshError - Called if there was an error while trying to refresh the token.
- onAuthLogout - Called if the user is logged out (will only be called if the session status iframe is enabled, or in Cordova mode).
- onTokenExpired - Called when the access token is expired. If a refresh token is available the token can be refreshed with updateToken, or in cases where it is not (that is, with implicit flow) you can redirect to the login screen to obtain a new access token.
2.3. Node.js adapter
Red Hat Single Sign-On provides a Node.js adapter built on top of Connect to protect server-side JavaScript apps - the goal was to be flexible enough to integrate with frameworks like Express.js.
To use the Node.js adapter, first you must create a client for your application in the Red Hat Single Sign-On Admin Console. The adapter supports public, confidential, and bearer-only access type. Which one to choose depends on the use-case scenario.
Once the client is created click the Installation
tab, select Red Hat Single Sign-On OIDC JSON
for Format Option
, and then click Download
. The downloaded keycloak.json
file should be at the root folder of your project.
2.3.1. Installation
Assuming you’ve already installed Node.js, create a folder for your application:
mkdir myapp && cd myapp
Use npm init
command to create a package.json
for your application. Now add the Red Hat Single Sign-On connect adapter in the dependencies list:
"dependencies": {
"keycloak-connect": "file:keycloak-connect-18.0.7.tgz"
}
2.3.2. Usage
- Instantiate a Keycloak class
-
The
Keycloak
class provides a central point for configuration and integration with your application. The simplest creation involves no arguments.
In the root directory of your project create a file called server.js
and add the following code:
const session = require('express-session');
const Keycloak = require('keycloak-connect');
const memoryStore = new session.MemoryStore();
const keycloak = new Keycloak({ store: memoryStore });
Install the express-session
dependency:
npm install express-session
To start the server.js
script, add the following command in the 'scripts' section of the package.json
:
"scripts": {
"test": "echo \"Error: no test specified\" && exit 1",
"start" "node server.js"
},
Now we have the ability to run our server with following command:
npm run start
By default, this will locate a file named keycloak.json
alongside the main executable of your application, in our case on the root folder, to initialize keycloak-specific settings such as public key, realm name, various URLs.
In that case a Keycloak deployment is necessary to access Keycloak admin console.
Please visit links on how to deploy a Keycloak admin console with Podman or Docker
Now we are ready to obtain the keycloak.json
file by visiting the Red Hat Single Sign-On Admin Console
Paste the downloaded file on the root folder of our project.
Instantiation with this method results in all of the reasonable defaults being used. As alternative, it’s also possible to provide a configuration object, rather than the keycloak.json
file:
const kcConfig = {
clientId: 'myclient',
bearerOnly: true,
serverUrl: 'http://localhost:8080/auth',
realm: 'myrealm',
realmPublicKey: 'MIIBIjANB...'
};
const keycloak = new Keycloak({ store: memoryStore }, kcConfig);
Applications can also redirect users to their preferred identity provider by using:
const keycloak = new Keycloak({ store: memoryStore, idpHint: myIdP }, kcConfig);
- Configuring a web session store
-
If you want to use web sessions to manage server-side state for authentication, you need to initialize the
Keycloak(…)
with at least astore
parameter, passing in the actual session store thatexpress-session
is using.
const session = require('express-session');
const memoryStore = new session.MemoryStore();
// Configure session
app.use(
session({
secret: 'mySecret',
resave: false,
saveUninitialized: true,
store: memoryStore,
})
);
const keycloak = new Keycloak({ store: memoryStore });
- Passing a custom scope value
-
By default, the scope value
openid
is passed as a query parameter to Red Hat Single Sign-On’s login URL, but you can add an additional custom value:
const keycloak = new Keycloak({ scope: 'offline_access' });
2.3.3. Installing middleware
Once instantiated, install the middleware into your connect-capable app:
In order to do so, first we have to install Express:
npm install express
then require Express in our project as outlined below:
const express = require('express');
const app = express();
and configure Keycloak middleware in Express, by adding at the code below:
app.use( keycloak.middleware() );
Last but not least, let’s set up our server to listen for HTTP requests on port 3000 by adding the following code to main.js
:
app.listen(3000, function () {
console.log('App listening on port 3000');
});
2.3.4. Configuration for proxies
If the application is running behind a proxy that terminates an SSL connection Express must be configured per the express behind proxies guide. Using an incorrect proxy configuration can result in invalid redirect URIs being generated.
Example configuration:
const app = express();
app.set( 'trust proxy', true );
app.use( keycloak.middleware() );
2.3.5. Checking authentication
To check that a user is authenticated before accessing a resource, simply use keycloak.checkSso()
. It will only authenticate if the user is already logged-in. If the user is not logged-in, the browser will be redirected back to the originally-requested URL and remain unauthenticated:
app.get( '/check-sso', keycloak.checkSso(), checkSsoHandler );
2.3.6. Protecting resources
- Simple authentication
-
To enforce that a user must be authenticated before accessing a resource, simply use a no-argument version of
keycloak.protect()
:
app.get( '/complain', keycloak.protect(), complaintHandler );
- Role-based authorization
- To secure a resource with an application role for the current app:
app.get( '/special', keycloak.protect('special'), specialHandler );
To secure a resource with an application role for a different app:
app.get( '/extra-special', keycloak.protect('other-app:special'), extraSpecialHandler );
To secure a resource with a realm role:
app.get( '/admin', keycloak.protect( 'realm:admin' ), adminHandler );
- Resource-Based Authorization
-
Resource-Based Authorization allows you to protect resources, and their specific methods/actions,** based on a set of policies defined in Keycloak, thus externalizing authorization from your application. This is achieved by exposing a
keycloak.enforcer
method which you can use to protect resources.*
app.get('/apis/me', keycloak.enforcer('user:profile'), userProfileHandler);
The keycloak-enforcer
method operates in two modes, depending on the value of the response_mode
configuration option.
app.get('/apis/me', keycloak.enforcer('user:profile', {response_mode: 'token'}), userProfileHandler);
If response_mode
is set to token
, permissions are obtained from the server on behalf of the subject represented by the bearer token that was sent to your application. In this case, a new access token is issued by Keycloak with the permissions granted by the server. If the server did not respond with a token with the expected permissions, the request is denied. When using this mode, you should be able to obtain the token from the request as follows:
app.get('/apis/me', keycloak.enforcer('user:profile', {response_mode: 'token'}), function (req, res) {
const token = req.kauth.grant.access_token.content;
const permissions = token.authorization ? token.authorization.permissions : undefined;
// show user profile
});
Prefer this mode when your application is using sessions and you want to cache previous decisions from the server, as well automatically handle refresh tokens. This mode is especially useful for applications acting as a client and resource server.
If response_mode
is set to permissions
(default mode), the server only returns the list of granted permissions, without issuing a new access token. In addition to not issuing a new token, this method exposes the permissions granted by the server through the request
as follows:
app.get('/apis/me', keycloak.enforcer('user:profile', {response_mode: 'permissions'}), function (req, res) {
const permissions = req.permissions;
// show user profile
});
Regardless of the response_mode
in use, the keycloak.enforcer
method will first try to check the permissions within the bearer token that was sent to your application. If the bearer token already carries the expected permissions, there is no need to interact with the server to obtain a decision. This is specially useful when your clients are capable of obtaining access tokens from the server with the expected permissions before accessing a protected resource, so they can use some capabilities provided by Keycloak Authorization Services such as incremental authorization and avoid additional requests to the server when keycloak.enforcer
is enforcing access to the resource.
By default, the policy enforcer will use the client_id
defined to the application (for instance, via keycloak.json
) to reference a client in Keycloak that supports Keycloak Authorization Services. In this case, the client can not be public given that it is actually a resource server.
If your application is acting as both a public client(frontend) and resource server(backend), you can use the following configuration to reference a different client in Keycloak with the policies that you want to enforce:
keycloak.enforcer('user:profile', {resource_server_id: 'my-apiserver'})
It is recommended to use distinct clients in Keycloak to represent your frontend and backend.
If the application you are protecting is enabled with Keycloak authorization services and you have defined client credentials in keycloak.json
, you can push additional claims to the server and make them available to your policies in order to make decisions. For that, you can define a claims
configuration option which expects a function
that returns a JSON with the claims you want to push:
app.get('/protected/resource', keycloak.enforcer(['resource:view', 'resource:write'], {
claims: function(request) {
return {
"http.uri": ["/protected/resource"],
"user.agent": // get user agent from request
}
}
}), function (req, res) {
// access granted
For more details about how to configure Keycloak to protected your application resources, please take a look at the Authorization Services Guide.
- Advanced authorization
- To secure resources based on parts of the URL itself, assuming a role exists for each section:
function protectBySection(token, request) {
return token.hasRole( request.params.section );
}
app.get( '/:section/:page', keycloak.protect( protectBySection ), sectionHandler );
Advanced Login Configuration:
By default, all unauthorized requests will be redirected to the Red Hat Single Sign-On login page unless your client is bearer-only. However, a confidential or public client may host both browsable and API endpoints. To prevent redirects on unauthenticated API requests and instead return an HTTP 401, you can override the redirectToLogin function.
For example, this override checks if the URL contains /api/ and disables login redirects:
Keycloak.prototype.redirectToLogin = function(req) {
const apiReqMatcher = /\/api\//i;
return !apiReqMatcher.test(req.originalUrl || req.url);
};
2.3.7. Additional URLs
- Explicit user-triggered logout
-
By default, the middleware catches calls to
/logout
to send the user through a Red Hat Single Sign-On-centric logout workflow. This can be changed by specifying alogout
configuration parameter to themiddleware()
call:
app.use( keycloak.middleware( { logout: '/logoff' } ));
When the user-triggered logout is invoked a query parameter redirect_url
can be passed:
https://example.com/logoff?redirect_url=https%3A%2F%2Fexample.com%3A3000%2Flogged%2Fout
This parameter is then used as the redirect url of the OIDC logout endpoint and the user will be redirected to https://example.com/logged/out
.
- Red Hat Single Sign-On Admin Callbacks
-
Also, the middleware supports callbacks from the Red Hat Single Sign-On console to log out a single session or all sessions. By default, these type of admin callbacks occur relative to the root URL of
/
but can be changed by providing anadmin
parameter to themiddleware()
call:
app.use( keycloak.middleware( { admin: '/callbacks' } );
2.3.8. Complete example
A complete example using the Node.js adapter usage can be found in Keycloak quickstarts for Node.js
2.4. Other OpenID Connect libraries
Red Hat Single Sign-On can be secured by supplied adapters that are usually easier to use and provide better integration with Red Hat Single Sign-On. However, if an adapter is not available for your programming language, framework, or platform you might opt to use a generic OpenID Connect Relying Party (RP) library instead. This chapter describes details specific to Red Hat Single Sign-On and does not contain specific protocol details. For more information see the OpenID Connect specifications and OAuth2 specification.
2.4.1. Endpoints
The most important endpoint to understand is the well-known
configuration endpoint. It lists endpoints and other configuration options relevant to the OpenID Connect implementation in Red Hat Single Sign-On. The endpoint is:
/realms/{realm-name}/.well-known/openid-configuration
To obtain the full URL, add the base URL for Red Hat Single Sign-On and replace {realm-name}
with the name of your realm. For example:
http://localhost:8080/auth/realms/master/.well-known/openid-configuration
Some RP libraries retrieve all required endpoints from this endpoint, but for others you might need to list the endpoints individually.
2.4.1.1. Authorization endpoint
/realms/{realm-name}/protocol/openid-connect/auth
The authorization endpoint performs authentication of the end-user. This is done by redirecting the user agent to this endpoint.
For more details see the Authorization Endpoint section in the OpenID Connect specification.
2.4.1.2. Token endpoint
/realms/{realm-name}/protocol/openid-connect/token
The token endpoint is used to obtain tokens. Tokens can either be obtained by exchanging an authorization code or by supplying credentials directly depending on what flow is used. The token endpoint is also used to obtain new access tokens when they expire.
For more details see the Token Endpoint section in the OpenID Connect specification.
2.4.1.3. Userinfo endpoint
/realms/{realm-name}/protocol/openid-connect/userinfo
The userinfo endpoint returns standard claims about the authenticated user, and is protected by a bearer token.
For more details see the Userinfo Endpoint section in the OpenID Connect specification.
2.4.1.4. Logout endpoint
/realms/{realm-name}/protocol/openid-connect/logout
The logout endpoint logs out the authenticated user.
The user agent can be redirected to the endpoint, in which case the active user session is logged out. Afterward the user agent is redirected back to the application.
The endpoint can also be invoked directly by the application. To invoke this endpoint directly the refresh token needs to be included as well as the credentials required to authenticate the client.
2.4.1.5. Certificate endpoint
/realms/{realm-name}/protocol/openid-connect/certs
The certificate endpoint returns the public keys enabled by the realm, encoded as a JSON Web Key (JWK). Depending on the realm settings there can be one or more keys enabled for verifying tokens. For more information see the Server Administration Guide and the JSON Web Key specification.
2.4.1.6. Introspection endpoint
/realms/{realm-name}/protocol/openid-connect/token/introspect
The introspection endpoint is used to retrieve the active state of a token. In other words, you can use it to validate an access or refresh token. It can only be invoked by confidential clients.
For more details on how to invoke on this endpoint, see OAuth 2.0 Token Introspection specification.
2.4.1.7. Dynamic Client Registration endpoint
/realms/{realm-name}/clients-registrations/openid-connect
The dynamic client registration endpoint is used to dynamically register clients.
For more details see the Client Registration chapter and the OpenID Connect Dynamic Client Registration specification.
2.4.1.8. Token Revocation endpoint
/realms/{realm-name}/protocol/openid-connect/revoke
The token revocation endpoint is used to revoke tokens. Both refresh tokens and access tokens are supported by this endpoint.
For more details on how to invoke on this endpoint, see OAuth 2.0 Token Revocation specification.
2.4.1.9. Device Authorization endpoint
/realms/{realm-name}/protocol/openid-connect/auth/device
The device authorization endpoint is used to obtain a device code and a user code. It can be invoked by confidential or public clients.
For more details on how to invoke on this endpoint, see OAuth 2.0 Device Authorization Grant specification.
2.4.1.10. Backchannel Authentication endpoint
/realms/{realm-name}/protocol/openid-connect/ext/ciba/auth
The backchannel authentication endpoint is used to obtain an auth_req_id that identifies the authentication request made by the client. It can only be invoked by confidential clients.
For more details on how to invoke on this endpoint, see OpenID Connect Client Initiated Backchannel Authentication Flow specification.
Also please refer to other places of Red Hat Single Sign-On documentation like Client Initiated Backchannel Authentication Grant section of this guide and Client Initiated Backchannel Authentication Grant section of Server Administration Guide.
2.4.2. Validating access tokens
If you need to manually validate access tokens issued by Red Hat Single Sign-On you can invoke the Introspection Endpoint. The downside to this approach is that you have to make a network invocation to the Red Hat Single Sign-On server. This can be slow and possibly overload the server if you have too many validation requests going on at the same time. Red Hat Single Sign-On issued access tokens are JSON Web Tokens (JWT) digitally signed and encoded using JSON Web Signature (JWS). Because they are encoded in this way, this allows you to locally validate access tokens using the public key of the issuing realm. You can either hard code the realm’s public key in your validation code, or lookup and cache the public key using the certificate endpoint with the Key ID (KID) embedded within the JWS. Depending what language you code in, there are a multitude of third party libraries out there that can help you with JWS validation.
2.4.3. Flows
2.4.3.1. Authorization code
The Authorization Code flow redirects the user agent to Red Hat Single Sign-On. Once the user has successfully authenticated with Red Hat Single Sign-On an Authorization Code is created and the user agent is redirected back to the application. The application then uses the authorization code along with its credentials to obtain an Access Token, Refresh Token and ID Token from Red Hat Single Sign-On.
The flow is targeted towards web applications, but is also recommended for native applications, including mobile applications, where it is possible to embed a user agent.
For more details refer to the Authorization Code Flow in the OpenID Connect specification.
2.4.3.2. Implicit
The Implicit flow redirects works similarly to the Authorization Code flow, but instead of returning an Authorization Code the Access Token and ID Token is returned. This reduces the need for the extra invocation to exchange the Authorization Code for an Access Token. However, it does not include a Refresh Token. This results in the need to either permit Access Tokens with a long expiration, which is problematic as it’s very hard to invalidate these. Or requires a new redirect to obtain new Access Token once the initial Access Token has expired. The Implicit flow is useful if the application only wants to authenticate the user and deals with logout itself.
There’s also a Hybrid flow where both the Access Token and an Authorization Code is returned.
One thing to note is that both the Implicit flow and Hybrid flow has potential security risks as the Access Token may be leaked through web server logs and browser history. This is somewhat mitigated by using short expiration for Access Tokens.
For more details refer to the Implicit Flow in the OpenID Connect specification.
2.4.3.3. Resource Owner Password Credentials
Resource Owner Password Credentials, referred to as Direct Grant in Red Hat Single Sign-On, allows exchanging user credentials for tokens. It’s not recommended to use this flow unless you absolutely need to. Examples where this could be useful are legacy applications and command-line interfaces.
There are a number of limitations of using this flow, including:
- User credentials are exposed to the application
- Applications need login pages
- Application needs to be aware of the authentication scheme
- Changes to authentication flow requires changes to application
- No support for identity brokering or social login
- Flows are not supported (user self-registration, required actions, etc.)
For a client to be permitted to use the Resource Owner Password Credentials grant the client has to have the Direct Access Grants Enabled
option enabled.
This flow is not included in OpenID Connect, but is a part of the OAuth 2.0 specification.
For more details refer to the Resource Owner Password Credentials Grant chapter in the OAuth 2.0 specification.
2.4.3.3.1. Example using CURL
The following example shows how to obtain an access token for a user in the realm master
with username user
and password password
. The example is using the confidential client myclient
:
curl \
-d "client_id=myclient" \
-d "client_secret=40cc097b-2a57-4c17-b36a-8fdf3fc2d578" \
-d "username=user" \
-d "password=password" \
-d "grant_type=password" \
"http://localhost:8080/auth/realms/master/protocol/openid-connect/token"
2.4.3.4. Client credentials
Client Credentials is used when clients (applications and services) wants to obtain access on behalf of themselves rather than on behalf of a user. This can for example be useful for background services that applies changes to the system in general rather than for a specific user.
Red Hat Single Sign-On provides support for clients to authenticate either with a secret or with public/private keys.
This flow is not included in OpenID Connect, but is a part of the OAuth 2.0 specification.
For more details refer to the Client Credentials Grant chapter in the OAuth 2.0 specification.
2.4.3.5. Device Authorization Grant
Device Authorization Grant is used by clients running on internet-connected devices that have limited input capabilities or lack a suitable browser. The application requests Red Hat Single Sign-On a device code and a user code. Red Hat Single Sign-On creates a device code and a user code. Red Hat Single Sign-On returns a response including the device code and the user code to the application. Then the application provides the user with the user code and the verification URI. The user accesses a verification URI to be authenticated by using another browser. The application repeatedly polls Red Hat Single Sign-On until Red Hat Single Sign-On completes the user authorization. If user authentication is complete, the application obtains the device code. Then the application uses the device code along with its credentials to obtain an Access Token, Refresh Token and ID Token from Red Hat Single Sign-On.
For more details refer to the OAuth 2.0 Device Authorization Grant specification.
2.4.3.6. Client Initiated Backchannel Authentication Grant
Client Initiated Backchannel Authentication Grant is used by clients who want to initiate the authentication flow by communicating with the OpenID Provider directly without redirect through the user’s browser like OAuth 2.0’s authorization code grant.
The client requests Red Hat Single Sign-On an auth_req_id that identifies the authentication request made by the client. Red Hat Single Sign-On creates the auth_req_id.
After receiving this auth_req_id, this client repeatedly needs to poll Red Hat Single Sign-On to obtain an Access Token, Refresh Token and ID Token from Red Hat Single Sign-On in return for the auth_req_id until the user is authenticated.
In case that client uses ping
mode, it does not need to repeatedly poll the token endpoint, but it can wait for the notification sent by Red Hat Single Sign-On to the specified Client Notification Endpoint. The Client Notification Endpoint can be configured in the Red Hat Single Sign-On Admin Console. The details of the contract for Client Notification Endpoint are described in the CIBA specification.
For more details refer to OpenID Connect Client Initiated Backchannel Authentication Flow specification.
Also please refer to other places of Red Hat Single Sign-On documentation like Backchannel Authentication Endpoint of this guide and Client Initiated Backchannel Authentication Grant section of Server Administration Guide. For the details about FAPI CIBA compliance, please refer to the FAPI section of this guide.
2.4.4. Redirect URIs
When using the redirect based flows it’s important to use valid redirect uris for your clients. The redirect uris should be as specific as possible. This especially applies to client-side (public clients) applications. Failing to do so could result in:
- Open redirects - this can allow attackers to create spoof links that looks like they are coming from your domain
- Unauthorized entry - when users are already authenticated with Red Hat Single Sign-On an attacker can use a public client where redirect uris have not be configured correctly to gain access by redirecting the user without the users knowledge
In production for web applications always use https
for all redirect URIs. Do not allow redirects to http.
There’s also a few special redirect URIs:
http://localhost
- This redirect URI is useful for native applications and allows the native application to create a web server on a random port that can be used to obtain the authorization code. This redirect uri allows any port.
urn:ietf:wg:oauth:2.0:oob
-
If its not possible to start a web server in the client (or a browser is not available) it is possible to use the special
urn:ietf:wg:oauth:2.0:oob
redirect uri. When this redirect uri is used Red Hat Single Sign-On displays a page with the code in the title and in a box on the page. The application can either detect that the browser title has changed, or the user can copy/paste the code manually to the application. With this redirect uri it is also possible for a user to use a different device to obtain a code to paste back to the application.
2.5. Financial-grade API (FAPI) Support
Red Hat Single Sign-On makes it easier for administrators to make sure that their clients are compliant with these specifications:
This compliance means that the Red Hat Single Sign-On server will verify the requirements for the authorization server, which are mentioned in the specifications. Red Hat Single Sign-On adapters do not have any specific support for the FAPI, hence the required validations on the client (application) side may need to be still done manually or through some other third-party solutions.
2.5.1. FAPI client profiles
To make sure that your clients are FAPI compliant, you can configure Client Policies in your realm as described in the Server Administration Guide and link them to the global client profiles for FAPI support, which are automatically available in each realm. You can use either fapi-1-baseline
or fapi-1-advanced
profile based on which FAPI profile you need your clients to conform with.
In case you want to use Pushed Authorization Request (PAR), it is recommended that your client use both the fapi-1-baseline
profile and fapi-1-advanced
for PAR requests. Specifically, the fapi-1-baseline
profile contains pkce-enforcer
executor, which makes sure that client use PKCE with secured S256 algorithm. This is not required for FAPI Advanced clients unless they use PAR requests.
In case you want to use CIBA in a FAPI compliant way, make sure that your clients use both fapi-1-advanced
and fapi-ciba
client profiles. There is a need to use the fapi-1-advanced
profile, or other client profile containing the requested executors, as the fapi-ciba
profile contains just CIBA-specific executors. When enforcing the requirements of the FAPI CIBA specification, there is a need for more requirements, such as enforcement of confidential clients or certificate-bound access tokens.
2.5.2. Open Banking Brasil Financial-grade API Security Profile
Red Hat Single Sign-On is compliant with the Open Banking Brasil Financial-grade API Security Profile 1.0 Implementers Draft 2. This one is more strict in some requirements than the FAPI 1 Advanced specification and hence it may be needed to configure Client Policies in the more strict way to enforce some of the requirements. Especially:
-
If your client does not use PAR, make sure that it uses encrypted OIDC request objects. This can be achieved by using a client profile with the
secure-request-object
executor configured withEncryption Required
enabled. -
Make sure that for JWS, the client uses the
PS256
algorithm. For JWE, the client should use theRSA-OAEP
withA256GCM
. This may need to be set in all the Client Settings where these algorithms are applicable.
2.5.3. TLS considerations
As confidential information is being exchanged, all interactions shall be encrypted with TLS (HTTPS). Moreover, there are some requirements in the FAPI specification for the cipher suites and TLS protocol versions used. To match these requirements, you can consider configure allowed ciphers. This configuration can be done in the KEYCLOAK_HOME/standalone/configuration/standalone-*.xml
file in the Elytron subsystem. For example this element can be added under tls
server-ssl-contexts
<server-ssl-context name="kcSSLContext" want-client-auth="true" protocols="TLSv1.2" \
key-manager="kcKeyManager" trust-manager="kcTrustManager" \
cipher-suite-filter="TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_DHE_RSA_WITH_AES_128_GCM_SHA256,TLS_DHE_RSA_WITH_AES_256_GCM_SHA384" protocols="TLSv1.2" />
The references to kcKeyManager
and kcTrustManager
refers to the corresponding Keystore and Truststore. See the documentation of Wildfly Elytron subsystem for more details and also other parts of Red Hat Single Sign-On documentation such as Network Setup Section or X.509 Authentication Section.
