---
title: "Chapter 6. Service Provider Interfaces (SPI) - Red Hat Single Sign-On 7.6 Server Developer Guide"
type: reference
domain: keycloak
slug: rhsso-7-6-providers
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html/server_developer_guide/providers
guide: server_developer_guide
version: 7.6
family: rhsso
documentKind: "Documentation"
---

# Chapter 6. Service Provider Interfaces (SPI) - Red Hat Single Sign-On 7.6 Server Developer Guide

Chapter 6. Service Provider Interfaces (SPI)
Red Hat Single Sign-On is designed to cover most use-cases without requiring custom code, but we also want it to be customizable. To achieve this Red Hat Single Sign-On has a number of Service Provider Interfaces (SPI) for which you can implement your own providers.
6.1. Implementing an SPI
To implement an SPI you need to implement its ProviderFactory and Provider interfaces. You also need to create a service configuration file.
For example, to implement the Theme Selector SPI you need to implement ThemeSelectorProviderFactory and ThemeSelectorProvider and also provide the file META-INF/services/org.keycloak.theme.ThemeSelectorProviderFactory
.
Example ThemeSelectorProviderFactory:
package org.acme.provider;
import ...
public class MyThemeSelectorProviderFactory implements ThemeSelectorProviderFactory {
@Override
public ThemeSelectorProvider create(KeycloakSession session) {
return new MyThemeSelectorProvider(session);
}
@Override
public void init(Config.Scope config) {
}
@Override
public void postInit(KeycloakSessionFactory factory) {
}
@Override
public void close() {
}
@Override
public String getId() {
return "myThemeSelector";
}
}
Red Hat Single Sign-On creates a single instance of provider factories which makes it possible to store state for multiple requests. Provider instances are created by calling create on the factory for each request so these should be light-weight object.
Example ThemeSelectorProvider:
package org.acme.provider;
import ...
public class MyThemeSelectorProvider implements ThemeSelectorProvider {
public MyThemeSelectorProvider(KeycloakSession session) {
}
@Override
public String getThemeName(Theme.Type type) {
return "my-theme";
}
@Override
public void close() {
}
}
Example service configuration file (META-INF/services/org.keycloak.theme.ThemeSelectorProviderFactory
):
org.acme.provider.MyThemeSelectorProviderFactory
You can configure your provider through standalone.xml
, standalone-ha.xml
, or domain.xml
.
For example by adding the following to standalone.xml
:
<spi name="themeSelector">
<provider name="myThemeSelector" enabled="true">
<properties>
<property name="theme" value="my-theme"/>
</properties>
</provider>
</spi>
Then you can retrieve the config in the ProviderFactory
init method:
public void init(Config.Scope config) {
String themeName = config.get("theme");
}
Your provider can also lookup other providers if needed. For example:
public class MyThemeSelectorProvider implements ThemeSelectorProvider {
private KeycloakSession session;
public MyThemeSelectorProvider(KeycloakSession session) {
this.session = session;
}
@Override
public String getThemeName(Theme.Type type) {
return session.getContext().getRealm().getLoginTheme();
}
}
6.1.1. Show info from your SPI implementation in the Admin Console
Sometimes it is useful to show additional info about your Provider to a Red Hat Single Sign-On administrator. You can show provider build time information (for example, version of custom provider currently installed), current configuration of the provider (eg. url of remote system your provider talks to) or some operational info (average time of response from remote system your provider talks to). Red Hat Single Sign-On Admin Console provides Server Info page to show this kind of information.
To show info from your provider it is enough to implement org.keycloak.provider.ServerInfoAwareProviderFactory
interface in your ProviderFactory
.
Example implementation for MyThemeSelectorProviderFactory
from previous example:
package org.acme.provider;
import ...
public class MyThemeSelectorProviderFactory implements ThemeSelectorProviderFactory, ServerInfoAwareProviderFactory {
...
@Override
public Map<String, String> getOperationalInfo() {
Map<String, String> ret = new LinkedHashMap<>();
ret.put("theme-name", "my-theme");
return ret;
}
}
6.2. Use available providers
In your provider implementation, you can use other providers available in Red Hat Single Sign-On. The existing providers can be typically retrieved with the usage of the KeycloakSession
, which is available to your provider as described in the section Implementing an SPI.
Red Hat Single Sign-On has two provider types:
Single-implementation provider types - There can be only a single active implementation of the particular provider type in Red Hat Single Sign-On runtime.
For example
HostnameProvider
specifies the hostname to be used by Red Hat Single Sign-On and that is shared for the whole Red Hat Single Sign-On server. Hence there can be only single implementation of this provider active for the Red Hat Single Sign-On server. If there are multiple provider implementations available to the server runtime, one of them needs to be specified as the default one.
For example such as:
<spi name="hostname">
<default-provider>default</default-provider>
...
</spi>
The value default
used as the value of default-provider
must match the ID returned by the ProviderFactory.getId()
of the particular provider factory implementation. In the code, you can obtain the provider such as keycloakSession.getProvider(HostnameProvider.class)
Multiple implementation provider types - Those are provider types, that allow multiple implementations available and working together in the Red Hat Single Sign-On runtime.
For example
EventListener
provider allows to have multiple implementations available and registered, which means that particular event can be sent to all the listeners (jboss-logging, sysout etc). In the code, you can obtain a specified instance of the provider for example such assession.getProvider(EventListener.class, "jboss-logging")
. You need to specifyprovider_id
of the provider as the second argument as there can be multiple instances of this provider type as described above.The provider ID must match the ID returned by the
ProviderFactory.getId()
of the particular provider factory implementation. Some provider types can be retrieved with the usage ofComponentModel
as the second argument and some (for exampleAuthenticator
) even need to be retrieved with the usage ofKeycloakSessionFactory
. It is not recommended to implement your own providers this way as it may be deprecated in the future.
6.3. Registering provider implementations
There are two ways to register provider implementations. In most cases the simplest way is to use the Red Hat Single Sign-On deployer approach as this handles a number of dependencies automatically for you. It also supports hot deployment as well as re-deployment.
The alternative approach is to deploy as a module.
If you are creating a custom SPI you will need to deploy it as a module, otherwise we recommend using the Red Hat Single Sign-On deployer approach.
6.3.1. Using the Red Hat Single Sign-On deployer
If you copy your provider jar to the Red Hat Single Sign-On standalone/deployments/
directory, your provider will automatically be deployed. Hot deployment works too. Additionally, your provider jar works similarly to other components deployed in a JBoss EAP environment in that they can use facilities like the jboss-deployment-structure.xml
file. This file allows you to set up dependencies on other components and load third-party jars and modules.
Provider jars can also be contained within other deployable units like EARs and WARs. Deploying with a EAR actually makes it really easy to use third party jars as you can just put these libraries in the EAR’s lib/
directory.
6.3.2. Register a provider using Modules
Procedure
Create a module using the jboss-cli script or manually create a folder.
For example, to add the event listener sysout example provider using the
jboss-cli
script, execute:KEYCLOAK_HOME/bin/jboss-cli.sh --command="module add --name=org.acme.provider --resources=target/provider.jar --dependencies=org.keycloak.keycloak-core,org.keycloak.keycloak-server-spi"
Alternatively, you can manually create the module inside
KEYCLOAK_HOME/modules
and add your jar and amodule.xml
.For example, create the folder
KEYCLOAK_HOME/modules/org/acme/provider/main
. Then copyprovider.jar
to this folder and createmodule.xml
with the following content:<?xml version="1.0" encoding="UTF-8"?> <module xmlns="urn:jboss:module:1.3" name="org.acme.provider"> <resources> <resource-root path="provider.jar"/> </resources> <dependencies> <module name="org.keycloak.keycloak-core"/> <module name="org.keycloak.keycloak-server-spi"/> </dependencies> </module>
Register this module with Red Hat Single Sign-On by editing the keycloak-server subsystem section of
standalone.xml
,standalone-ha.xml
, ordomain.xml
, and adding it to the providers:<subsystem xmlns="urn:jboss:domain:keycloak-server:1.2"> <web-context>auth</web-context> <providers> <provider>module:org.keycloak.examples.event-sysout</provider> </providers> ...
6.3.3. Disabling a provider
You can disable a provider by setting the enabled attribute for the provider to false in standalone.xml
, standalone-ha.xml
, or domain.xml
. For example to disable the Infinispan user cache provider add:
<spi name="userCache">
<provider name="infinispan" enabled="false"/>
</spi>
6.4. Leveraging Jakarta EE
The service providers can be packaged within any Jakarta EE component so long as you set up the META-INF/services
file correctly to point to your providers. For example, if your provider needs to use third party libraries, you can package up your provider within an ear and store these third party libraries in the ear’s lib/
directory. Also note that provider jars can make use of the jboss-deployment-structure.xml
file that EJBs, WARS, and EARs can use in a JBoss EAP environment. See the JBoss EAP documentation for more details on this file. It allows you to pull in external dependencies among other fine grain actions.
ProviderFactory
implementations are required to be plain java objects. But, we also currently support implementing provider classes as Stateful EJBs. This is how you would do it:
@Stateful
@Local(EjbExampleUserStorageProvider.class)
public class EjbExampleUserStorageProvider implements UserStorageProvider,
UserLookupProvider,
UserRegistrationProvider,
UserQueryProvider,
CredentialInputUpdater,
CredentialInputValidator,
OnUserCache
{
@PersistenceContext
protected EntityManager em;
protected ComponentModel model;
protected KeycloakSession session;
public void setModel(ComponentModel model) {
this.model = model;
}
public void setSession(KeycloakSession session) {
this.session = session;
}
@Remove
@Override
public void close() {
}
...
}
You define the @Local
annotation and specify your provider class there. If you don’t do this, EJB will not proxy the provider instance correctly and your provider won’t work.
You put the @Remove
annotation on the close()
method of your provider. If you don’t, the stateful bean will never be cleaned up and you may eventually see error messages.
Ixmplementations of ProviderFactory
are required to be plain java objects. Your factory class would perform a JNDI lookup of the Stateful EJB in its create()
method.
public class EjbExampleUserStorageProviderFactory
implements UserStorageProviderFactory<EjbExampleUserStorageProvider> {
@Override
public EjbExampleUserStorageProvider create(KeycloakSession session, ComponentModel model) {
try {
InitialContext ctx = new InitialContext();
EjbExampleUserStorageProvider provider = (EjbExampleUserStorageProvider)ctx.lookup(
"java:global/user-storage-jpa-example/" + EjbExampleUserStorageProvider.class.getSimpleName());
provider.setModel(model);
provider.setSession(session);
return provider;
} catch (Exception e) {
throw new RuntimeException(e);
}
}
6.5. JavaScript providers
Red Hat Single Sign-On has the ability to execute scripts during runtime in order to allow administrators to customize specific functionalities:
- Authenticator
- JavaScript Policy
- OpenID Connect Protocol Mapper
- SAML Protocol Mapper
6.5.1. Authenticator
Authentication scripts must provide at least one of the following functions: authenticate(..)
, which is called from Authenticator#authenticate(AuthenticationFlowContext)
action(..)
, which is called from Authenticator#action(AuthenticationFlowContext)
Custom Authenticator
should at least provide the authenticate(..)
function. You can use the javax.script.Bindings
script within the code.
script
-
the
ScriptModel
to access script metadata realm
-
the
RealmModel
user
-
the current
UserModel
session
-
the active
KeycloakSession
authenticationSession
-
the current
AuthenticationSessionModel
httpRequest
-
the current
org.jboss.resteasy.spi.HttpRequest
LOG
-
a
org.jboss.logging.Logger
scoped toScriptBasedAuthenticator
You can extract additional context information from the context
argument passed to the authenticate(context)
action(context)
function.
AuthenticationFlowError = Java.type("org.keycloak.authentication.AuthenticationFlowError");
function authenticate(context) {
LOG.info(script.name + " --> trace auth for: " + user.username);
if ( user.username === "tester"
&& user.getAttribute("someAttribute")
&& user.getAttribute("someAttribute").contains("someValue")) {
context.failure(AuthenticationFlowError.INVALID_USER);
return;
}
context.success();
}
6.5.2. Create a JAR with the scripts to deploy
JAR files are regular ZIP files with a .jar
extension.
In order to make your scripts available to Red Hat Single Sign-On you need to deploy them to the server. For that, you should create a JAR
file with the following structure:
META-INF/keycloak-scripts.json
my-script-authenticator.js
my-script-policy.js
my-script-mapper.js
The META-INF/keycloak-scripts.json
is a file descriptor that provides metadata information about the scripts you want to deploy. It is a JSON file with the following structure:
{
"authenticators": [
{
"name": "My Authenticator",
"fileName": "my-script-authenticator.js",
"description": "My Authenticator from a JS file"
}
],
"policies": [
{
"name": "My Policy",
"fileName": "my-script-policy.js",
"description": "My Policy from a JS file"
}
],
"mappers": [
{
"name": "My Mapper",
"fileName": "my-script-mapper.js",
"description": "My Mapper from a JS file"
}
],
"saml-mappers": [
{
"name": "My Mapper",
"fileName": "my-script-mapper.js",
"description": "My Mapper from a JS file"
}
]
}
This file should reference the different types of script providers that you want to deploy:
authenticators
For OpenID Connect Script Authenticators. You can have one or multiple authenticators in the same JAR file
policies
For JavaScript Policies when using Red Hat Single Sign-On Authorization Services. You can have one or multiple policies in the same JAR file
mappers
For OpenID Connect Script Protocol Mappers. You can have one or multiple mappers in the same JAR file
saml-mappers
For SAML Script Protocol Mappers. You can have one or multiple mappers in the same JAR file
For each script file in your JAR
file, you need a corresponding entry in META-INF/keycloak-scripts.json
that maps your scripts files to a specific provider type. For that you should provide the following properties for each entry:
name
A friendly name that will be used to show the scripts through the Red Hat Single Sign-On Administration Console. If not provided, the name of the script file will be used instead
description
An optional text that better describes the intend of the script file
fileName
The name of the script file. This property is mandatory and should map to a file within the JAR.
6.5.3. Deploy the script JAR
Once you have a JAR file with a descriptor and the scripts you want to deploy, you just need to copy the JAR to the Red Hat Single Sign-On standalone/deployments/
directory.
6.5.3.1. Deploy the script engine on Java 15 and later
To run the scripts, JavaScript providers require that a JavaScript engine is available in your Java application. Java 14 and lower versions include the Nashorn JavaScript Engine. It is automatically available as part of the Java itself and JavaScript providers are able to use this script engine by default. However, for Java 15 or higher versions, the script engine is not part of the Java itself. It needs to be added to your server because Red Hat Single Sign-On does not have any script engine by default. Java 15 and higher versions require an extra step when deploying script providers - adding the script engine of your choice to your distribution.
You can use any script engine. However, we only test with the Nashorn JavaScript Engine. The following steps assume that this engine is used:
You can install the script engine by adding the new module nashorn-core to your Red Hat Single Sign-On. After the server starts, you can run commands similar to these in the KEYCLOAK_HOME/bin
directory:
export NASHORN_VERSION=15.3
wget https://repo1.maven.org/maven2/org/openjdk/nashorn/nashorn-core/$NASHORN_VERSION/nashorn-core-$NASHORN_VERSION.jar
./jboss-cli.sh -c --command="module add --module-root-dir=../modules/system/layers/keycloak/ --name=org.openjdk.nashorn.nashorn-core --resources=./nashorn-core-$NASHORN_VERSION.jar --dependencies=asm.asm,jdk.dynalink"
rm nashorn-core-$NASHORN_VERSION.jar
In case you want to install your provider into the different module, you can use configuration property script-engine-module
of the default scripting provider. For example, you can use something such as this in your KEYCLOAK_HOME/standalone/configuration/standalone-*.xml
file:
<spi name="scripting">
<provider name="default" enabled="true">
<properties>
<property name="script-engine-module" value="org.graalvm.js.js-scriptengine"/>
</properties>
</provider>
</spi>
6.6. Available SPIs
If you want to see list of all available SPIs at runtime, you can check Server Info
page in Admin Console as described in Admin Console section.
