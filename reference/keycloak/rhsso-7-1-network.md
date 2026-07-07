---
title: "Chapter 7. Network Setup - Red Hat Single Sign-On 7.1 Server Installation and Configuration Guide"
type: reference
domain: keycloak
slug: rhsso-7-1-network
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.1/html/server_installation_and_configuration_guide/network
guide: server_installation_and_configuration_guide
version: 7.1
family: rhsso
documentKind: "Documentation"
abstract: "Red Hat Single Sign-On can run out of the box with some networking limitations. For one, all network endpoints bind to localhost so the auth server is really only usable on one local machine. For HTTP based connections, it does not use default ports like 80 and 443. HTTPS/SSL is not configured out of the box and without it, Red Hat Single Sign-On has many security vulnerabilities. Finally, Red Hat…"
---

# Chapter 7. Network Setup - Red Hat Single Sign-On 7.1 Server Installation and Configuration Guide

Chapter 7. Network Setup
Red Hat Single Sign-On can run out of the box with some networking limitations. For one, all network endpoints bind to localhost
so the auth server is really only usable on one local machine. For HTTP based connections, it does not use default ports like 80 and 443. HTTPS/SSL is not configured out of the box and without it, Red Hat Single Sign-On has many security vulnerabilities. Finally, Red Hat Single Sign-On may often need to make secure SSL and HTTPS connections to external servers and thus need a trust store set up so that endpoints can be validated correctly. This chapter discusses all of these things.
7.1. Bind Addresses
By default Red Hat Single Sign-On binds to the localhost loopback address 127.0.0.1
. That’s not a very useful default if you want the authentication server available on your network. Generally, what we recommend is that you deploy a reverse proxy or load balancer on a public network and route traffic to individual Red Hat Single Sign-On server instances on a private network. In either case though, you still need to set up your network interfaces to bind to something other than localhost
.
Setting the bind address is quite easy and can be done on the command line with either the standalone.sh or domain.sh boot scripts discussed in the Choosing an Operating Mode chapter.
$ standalone.sh -b 192.168.0.5
The -b
switch sets the IP bind address for any public interfaces.
Alternatively, if you don’t want to set the bind address at the command line, you can edit the profile configuration of your deployment. Open up the profile configuration file (standalone.xml or domain.xml depending on your operating mode) and look for the interfaces
XML block.
<interfaces>
<interface name="management">
<inet-address value="${jboss.bind.address.management:127.0.0.1}"/>
</interface>
<interface name="public">
<inet-address value="${jboss.bind.address:127.0.0.1}"/>
</interface>
</interfaces>
The public
interface corresponds to subsystems creating sockets that are available publicly. An example of one of these subsystems is the web layer which serves up the authentication endpoints of Red Hat Single Sign-On. The management
interface corresponds to sockets opened up by the management layer of the JBoss EAP. Specifically the sockets which allow you to use the jboss-cli.sh
command line interface and the JBoss EAP web console.
In looking at the public
interface you see that it has a special string ${jboss.bind.address:127.0.0.1}
. This string denotes a value 127.0.0.1
that can be overriden on the command line by setting a Java system property, i.e.:
$ domain.sh -Djboss.bind.address=192.168.0.5
The -b
is just a shorthand notation for this command. So, you can either change the bind address value directly in the profile config, or change it on the command line when you boot up.
There are many more options available when setting up interface
definitions. For more information, see the network interface in the JBoss EAP Configuration Guide.
7.2. Socket Port Bindings
The ports opened for each socket have a pre-defined default that can be overriden at the command line or within configuration. To illustrate this configuration, let’s pretend you are running in standalone mode and open up the …/standalone/configuration/standalone.xml. Search for socket-binding-group
.
<socket-binding-group name="standard-sockets" default-interface="public" port-offset="${jboss.socket.binding.port-offset:0}">
<socket-binding name="management-http" interface="management" port="${jboss.management.http.port:9990}"/>
<socket-binding name="management-https" interface="management" port="${jboss.management.https.port:9993}"/>
<socket-binding name="ajp" port="${jboss.ajp.port:8009}"/>
<socket-binding name="http" port="${jboss.http.port:8080}"/>
<socket-binding name="https" port="${jboss.https.port:8443}"/>
<socket-binding name="txn-recovery-environment" port="4712"/>
<socket-binding name="txn-status-manager" port="4713"/>
<outbound-socket-binding name="mail-smtp">
<remote-destination host="localhost" port="25"/>
</outbound-socket-binding>
</socket-binding-group>
socket-bindings
define socket connections that will be opened by the server. These bindings specify the interface
(bind address) they use as well as what port number they will open. The ones you will be most interested in are:
- http
- Defines the port used for Red Hat Single Sign-On HTTP connections
- https
- Defines the port used for Red Hat Single Sign-On HTTPS connections
- ajp
-
This socket binding defines the port used for the AJP protocol. This protocol is used by Apache HTTPD server in conjunction
mod-cluster
when you are using Apache HTTPD as a load balancer. - management-http
- Defines the HTTP connection used by JBoss EAP CLI and web console.
When running in domain mode setting the socket configurations is a bit trickier as the example domain.xml file has multiple socket-binding-groups
defined. If you scroll down to the server-group
definitions you can see what socket-binding-group
is used for each server-group
.
domain socket bindings
<server-groups>
<server-group name="load-balancer-group" profile="load-balancer">
...
<socket-binding-group ref="load-balancer-sockets"/>
</server-group>
<server-group name="auth-server-group" profile="auth-server-clustered">
...
<socket-binding-group ref="ha-sockets"/>
</server-group>
</server-groups>
There are many more options available when setting up socket-binding-group
definitions. For more information, see the socket binding group in the JBoss EAP Configuration Guide.
7.3. Setting up HTTPS/SSL
Red Hat Single Sign-On is not set up by default to handle SSL/HTTPS. It is highly recommended that you either enable SSL on the Red Hat Single Sign-On server itself or on a reverse proxy in front of the Red Hat Single Sign-On server.
This default behavior is defined by the SSL/HTTPS mode of each Red Hat Single Sign-On realm. This is discussed in more detail in the Server Administration Guide, but let’s give some context and a brief overview of these modes.
- external requests
-
Red Hat Single Sign-On can run out of the box without SSL so long as you stick to private IP addresses like
localhost
,127.0.0.1
,10.0.x.x
,192.168.x.x
, and172..16.x.x
. If you don’t have SSL/HTTPS configured on the server or you try to access Red Hat Single Sign-On over HTTP from a non-private IP adress you will get an error. - none
- Red Hat Single Sign-On does not require SSL. This should really only be used in development when you are playing around with things.
- all requests
- Red Hat Single Sign-On requires SSL for all IP addresses.
The SSL mode for each realm can be configured in the Red Hat Single Sign-On admin console.
7.3.1. Enabling SSL/HTTPS for the Red Hat Single Sign-On Server
If you are not using a reverse proxy or load balancer to handle HTTPS traffic for you, you’ll need to enable HTTPS for the Red Hat Single Sign-On server. This involves
- Obtaining or generating a keystore that contains the private key and certificate for SSL/HTTP traffic
- Configuring the Red Hat Single Sign-On server to use this keypair and certificate.
7.3.1.1. Creating the Certificate and Java Keystore
In order to allow HTTPS connections, you need to obtain a self signed or third-party signed certificate and import it into a Java keystore before you can enable HTTPS in the web container you are deploying the Red Hat Single Sign-On Server to.
7.3.1.1.1. Self Signed Certificate
In development, you will probably not have a third party signed certificate available to test a Red Hat Single Sign-On deployment so you’ll need to generate a self-signed one using the keytool
utility that comes with the Java JDK.
$ keytool -genkey -alias localhost -keyalg RSA -keystore keycloak.jks -validity 10950
Enter keystore password: secret
Re-enter new password: secret
What is your first and last name?
[Unknown]: localhost
What is the name of your organizational unit?
[Unknown]: Keycloak
What is the name of your organization?
[Unknown]: Red Hat
What is the name of your City or Locality?
[Unknown]: Westford
What is the name of your State or Province?
[Unknown]: MA
What is the two-letter country code for this unit?
[Unknown]: US
Is CN=localhost, OU=Keycloak, O=Test, L=Westford, ST=MA, C=US correct?
[no]: yes
You should answer What is your first and last name ?
question with the DNS name of the machine you’re installing the server on. For testing purposes, localhost
should be used. After executing this command, the keycloak.jks
file will be generated in the same directory as you executed the keytool
command in.
If you want a third-party signed certificate, but don’t have one, you can obtain one for free at cacert.org. You’ll have to do a little set up first before doing this though.
The first thing to do is generate a Certificate Request:
$ keytool -certreq -alias yourdomain -keystore keycloak.jks > keycloak.careq
Where yourdomain
is a DNS name for which this certificate is generated for. Keytool generates the request:
-----BEGIN NEW CERTIFICATE REQUEST-----
MIIC2jCCAcICAQAwZTELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAk1BMREwDwYDVQQHEwhXZXN0Zm9y
ZDEQMA4GA1UEChMHUmVkIEhhdDEQMA4GA1UECxMHUmVkIEhhdDESMBAGA1UEAxMJbG9jYWxob3N0
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr7kck2TaavlEOGbcpi9c0rncY4HhdzmY
Ax2nZfq1eZEaIPqI5aTxwQZzzLDK9qbeAd8Ji79HzSqnRDxNYaZu7mAYhFKHgixsolE3o5Yfzbw1
29RvyeUVe+WZxv5oo9wolVVpdSINIMEL2LaFhtX/c1dqiqYVpfnvFshZQaIg2nL8juzZcBjj4as
H98gIS7khql/dkZKsw9NLvyxgJvp7PaXurX29fNf3ihG+oFrL22oFyV54BWWxXCKU/GPn61EGZGw
Ft2qSIGLdctpMD1aJR2bcnlhEjZKDksjQZoQ5YMXaAGkcYkG6QkgrocDE2YXDbi7GIdf9MegVJ35
2DQMpwIDAQABoDAwLgYJKoZIhvcNAQkOMSEwHzAdBgNVHQ4EFgQUQwlZJBA+fjiDdiVzaO9vrE/i
n2swDQYJKoZIhvcNAQELBQADggEBAC5FRvMkhal3q86tHPBYWBuTtmcSjs4qUm6V6f63frhveWHf
PzRrI1xH272XUIeBk0gtzWo0nNZnf0mMCtUBbHhhDcG82xolikfqibZijoQZCiGiedVjHJFtniDQ
9bMDUOXEMQ7gHZg5q6mJfNG9MbMpQaUVEEFvfGEQQxbiFK7hRWU8S23/d80e8nExgQxdJWJ6vd0X
MzzFK6j4Dj55bJVuM7GFmfdNC52pNOD5vYe47Aqh8oajHX9XTycVtPXl45rrWAH33ftbrS8SrZ2S
vqIFQeuLL3BaHwpl3t7j2lMWcK1p80laAxEASib/fAwrRHpLHBXRcq6uALUOZl4Alt8=
-----END NEW CERTIFICATE REQUEST-----
Send this ca request to your CA. The CA will issue you a signed certificate and send it to you. Before you import your new cert, you must obtain and import the root certificate of the CA. You can download the cert from CA (ie.: root.crt) and import as follows:
$ keytool -import -keystore keycloak.jks -file root.crt -alias root
Last step is to import your new CA generated certificate to your keystore:
$ keytool -import -alias yourdomain -keystore keycloak.jks -file your-certificate.cer
7.3.1.2. Configure Red Hat Single Sign-On to Use the Keystore
Now that you have a Java keystore with the appropriate certificates, you need to configure your Red Hat Single Sign-On installation to use it. First step is to move the keystore file to the configuration/ directory of your deployment and to edit the standalone.xml, standalone-ha.xml or domain.xml file to use the keystore and enable HTTPS. (See operating mode).
In the standalone or domain configuration file, search for the security-realms
element and add:
<security-realm name="UndertowRealm">
<server-identities>
<ssl>
<keystore path="keycloak.jks" relative-to="jboss.server.config.dir" keystore-password="secret" />
</ssl>
</server-identities>
</security-realm>
Find the element server name="default-server"
(it’s a child element of subsystem xmlns="urn:jboss:domain:undertow:3.1"
) and add:
<subsystem xmlns="urn:jboss:domain:undertow:3.1">
<buffer-cache name="default"/>
<server name="default-server">
<https-listener name="https" socket-binding="https" security-realm="UndertowRealm"/>
...
</subsystem>
7.4. Outgoing HTTP Requests
The Red Hat Single Sign-On server often needs to make non-browser HTTP requests to the applications and services it secures. The auth server manages these outgoing connections by maintaining an HTTP client connection pool. There are some things you’ll need to configure in standalone.xml
, standalone-ha.xml
, or domain.xml
. The location of this file depends on your operating mode.
HTTP client Config example
<spi name="connectionsHttpClient">
<provider name="default" enabled="true">
<properties>
<property name="connection-pool-size" value="256"/>
</properties>
</provider>
</spi>
Possible configuration options are:
- establish-connection-timeout-millis
- Timeout for establishing a socket connection.
- socket-timeout-millis
- If an outgoing request does not receive data for this amount of time, timeout the connection.
- connection-pool-size
- How many connections can be in the pool (128 by default).
- max-pooled-per-route
- How many connections can be pooled per host (64 by default).
- connection-ttl-millis
- Maximum connection time to live in milliseconds. Not set by default.
- max-connection-idle-time-millis
-
Maximum time the connection might stay idle in the connection pool (900 seconds by default). Will start background cleaner thread of Apache HTTP client. Set to -
1
to disable this checking and the background thread. - disable-cookies
-
true
by default. When set to true, this will disable any cookie caching. - client-keystore
- This is the file path to a Java keystore file. This keystore contains client certificate for two-way SSL.
- client-keystore-password
-
Password for the client keystore. This is REQUIRED if
client-keystore
is set. - client-key-password
-
Password for the client’s key. This is REQUIRED if
client-keystore
is set.
7.4.1. Outgoing HTTPS Request Truststore
When Red Hat Single Sign-On invokes on remote HTTPS endpoints, it has to validate the remote server’s certificate in order to ensure it is connecting to a trusted server. This is necessary in order to prevent man-in-the-middle attacks. The certificates of these remote server’s or the CA that signed these certificates must be put in a truststore. This truststore is managed by the Red Hat Single Sign-On server.
The truststore is used when connecting securely to identity brokers, LDAP identity providers, when sending emails, and for backchannel communication with client applications.
By default, a truststore provider is not configured, and any https connections fall back to standard java truststore configuration as described in Java’s JSSE Reference Guide. If there is no trust establised, then these outgoing HTTPS requests will fail.
You can use keytool to create a new truststore file or add trusted host certificates to an existing one:
$ keytool -import -alias HOSTDOMAIN -keystore truststore.jks -file host-certificate.cer
The truststore is configured within the standalone.xml
, standalone-ha.xml
, or domain.xml
file in your distribution. The location of this file depends on your operating mode. You can add your truststore configuration by using the following template:
<spi name="truststore">
<provider name="file" enabled="true">
<properties>
<property name="file" value="path to your .jks file containing public certificates"/>
<property name="password" value="password"/>
<property name="hostname-verification-policy" value="WILDCARD"/>
<property name="disabled" value="false"/>
</properties>
</provider>
</spi>
Possible configuration options for this setting are:
- file
-
The path to a Java keystore file. HTTPS requests need a way to verify the host of the server they are talking to. This is what the trustore does. The keystore contains one or more trusted host certificates or certificate authorities. This truststore file should only contain public certificates of your secured hosts. This is REQUIRED if
disabled
is not true. - password
-
Password for the truststore. This is REQUIRED if
disabled
is not true. - hostname-verification-policy
-
WILDCARD
by default. For HTTPS requests, this verifies the hostname of the server’s certificate.ANY
means that the hostname is not verified.WILDCARD
Allows wildcards in subdomain names i.e. *.foo.com.STRICT
CN must match hostname exactly. - disabled
-
If true (default value), truststore configuration will be ignored, and certificate checking will fall back to JSSE configuration as described. If set to false, you must configure
file
, andpassword
for the truststore.
