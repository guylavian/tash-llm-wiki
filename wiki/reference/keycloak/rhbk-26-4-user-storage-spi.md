---
title: "Chapter 5. User Storage SPI - Red Hat build of Keycloak 26.4 Server Developer Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-user-storage-spi
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_developer_guide/user-storage-spi
guide: server_developer_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
---

# Chapter 5. User Storage SPI - Red Hat build of Keycloak 26.4 Server Developer Guide

Chapter 5. User Storage SPI
You can use the User Storage SPI to write extensions to Red Hat build of Keycloak to connect to external user databases and credential stores. The built-in LDAP and ActiveDirectory support is an implementation of this SPI in action. Out of the box, Red Hat build of Keycloak uses its local database to create, update, and look up users and validate credentials. Often though, organizations have existing external proprietary user databases that they cannot migrate to Red Hat build of Keycloak’s data model. For those situations, application developers can write implementations of the User Storage SPI to bridge the external user store and the internal user object model that Red Hat build of Keycloak uses to log in users and manage them.
When the Red Hat build of Keycloak runtime needs to look up a user, such as when a user is logging in, it performs a number of steps to locate the user. It first looks to see if the user is in the user cache; if the user is found it uses that in-memory representation. Then it looks for the user within the Red Hat build of Keycloak local database. If the user is not found, it then loops through User Storage SPI provider implementations to perform the user query until one of them returns the user the runtime is looking for. The provider queries the external user store for the user and maps the external data representation of the user to Red Hat build of Keycloak’s user metamodel.
User Storage SPI provider implementations can also perform complex criteria queries, perform CRUD operations on users, validate and manage credentials, or perform bulk updates of many users at once. It depends on the capabilities of the external store.
User Storage SPI provider implementations are packaged and deployed similarly to (and often are) Jakarta EE components. They are not enabled by default, but instead must be enabled and configured per realm under the User Federation
tab in the administration console.
If your user provider implementation is using some user attributes as the metadata attributes for linking/establishing the user identity, then please make sure that users are not able to edit the attributes and the corresponding attributes are read-only. The example is the LDAP_ID
attribute, which the built-in Red Hat build of Keycloak LDAP provider is using for to store the ID of the user on the LDAP server side. See the details in the Threat model mitigation chapter.
There are two sample projects in Red Hat build of Keycloak Quickstarts Repository. Each quickstart has a README
file with instructions on how to build, deploy, and test the sample project. The following table provides a brief description of the available User Storage SPI quickstarts:
| Name | Description |
|---|---|
| Demonstrates implementing a user storage provider using JPA. | |
| Demonstrates implementing a user storage provider using a simple properties file that contains username/password key pairs. |
In order to connect to the external database, you should use the Red Hat build of Keycloak properties for the additional datasources described in the Configure multiple datasources guide.
5.1. Accessing the new entity manager
In order to simply access your data in your Red Hat build of Keycloak extension, you can obtain the EntityManager for the additional datasources used in these quickstarts. It helps you to interact with entities specified for your datasource, as it provides some kind of bridge between your JPA entities and the database.
You can use the new entity manager (for the user-store
datasource) as follows:
EntityManager em = session.getProvider(JpaConnectionProvider.class, "user-store").getEntityManager();
var user = em.find(org.your.extension.UserEntity.class, 123L);
5.2. Provider interfaces
When building an implementation of the User Storage SPI you have to define a provider class and a provider factory. Provider class instances are created per transaction by provider factories. Provider classes do all the heavy lifting of user lookup and other user operations. They must implement the org.keycloak.storage.UserStorageProvider
interface.
package org.keycloak.storage;
public interface UserStorageProvider extends Provider {
/**
* Callback when a realm is removed. Implement this if, for example, you want to do some
* cleanup in your user storage when a realm is removed
*
* @param realm
*/
default
void preRemove(RealmModel realm) {
}
/**
* Callback when a group is removed. Allows you to do things like remove a user
* group mapping in your external store if appropriate
*
* @param realm
* @param group
*/
default
void preRemove(RealmModel realm, GroupModel group) {
}
/**
* Callback when a role is removed. Allows you to do things like remove a user
* role mapping in your external store if appropriate
* @param realm
* @param role
*/
default
void preRemove(RealmModel realm, RoleModel role) {
}
}
You may be thinking that the UserStorageProvider
interface is pretty sparse? You’ll see later in this chapter that there are other mix-in interfaces your provider class may implement to support the meat of user integration.
UserStorageProvider
instances are created once per transaction. When the transaction is complete, the UserStorageProvider.close()
method is invoked and the instance is then garbage collected. Instances are created by provider factories. Provider factories implement the org.keycloak.storage.UserStorageProviderFactory
interface.
package org.keycloak.storage;
/**
* @author <a href="mailto:bill@burkecentral.com">Bill Burke</a>
* @version $Revision: 1 $
*/
public interface UserStorageProviderFactory<T extends UserStorageProvider> extends ComponentFactory<T, UserStorageProvider> {
/**
* This is the name of the provider and will be shown in the admin console as an option.
*
* @return
*/
@Override
String getId();
/**
* called per Keycloak transaction.
*
* @param session
* @param model
* @return
*/
T create(KeycloakSession session, ComponentModel model);
...
}
Provider factory classes must specify the concrete provider class as a template parameter when implementing the UserStorageProviderFactory
. This is a must as the runtime will introspect this class to scan for its capabilities (the other interfaces it implements). So for example, if your provider class is named FileProvider
, then the factory class should look like this:
public class FileProviderFactory implements UserStorageProviderFactory<FileProvider> {
public String getId() { return "file-provider"; }
public FileProvider create(KeycloakSession session, ComponentModel model) {
...
}
The getId()
method returns the name of the User Storage provider. This id will be displayed in the admin console’s User Federation page when you want to enable the provider for a specific realm.
The create()
method is responsible for allocating an instance of the provider class. It takes a org.keycloak.models.KeycloakSession
parameter. This object can be used to look up other information and metadata as well as provide access to various other components within the runtime. The ComponentModel
parameter represents how the provider was enabled and configured within a specific realm. It contains the instance id of the enabled provider as well as any configuration you may have specified for it when you enabled through the admin console.
The UserStorageProviderFactory
has other capabilities as well which we will go over later in this chapter.
5.3. Provider capability interfaces
If you have examined the UserStorageProvider
interface closely you might notice that it does not define any methods for locating or managing users. These methods are actually defined in other capability interfaces depending on what scope of capabilities your external user store can provide and execute on. For example, some external stores are read-only and can only do simple queries and credential validation. You will only be required to implement the capability interfaces for the features you are able to. You can implement these interfaces:
| SPI | Description |
|---|---|
|
| This interface is required if you want to be able to log in with users from this external store. Most (all?) providers implement this interface. |
|
| Defines complex queries that are used to locate one or more users. You must implement this interface if you want to view and manage users from the administration console. |
|
| Implement this interface if your provider supports count queries. |
|
|
This interface is combined capability of |
|
| Implement this interface if your provider supports adding and removing users. |
|
| Implement this interface if your provider supports bulk update of a set of users. |
|
| Implement this interface if your provider can validate one or more different credential types (for example, if your provider can validate a password). |
|
| Implement this interface if your provider supports updating one or more different credential types. |
5.4. Model interfaces
Most of the methods defined in the capability interfaces either return or are passed in representations of a user. These representations are defined by the org.keycloak.models.UserModel
interface. App developers are required to implement this interface. It provides a mapping between the external user store and the user metamodel that Red Hat build of Keycloak uses.
package org.keycloak.models;
public interface UserModel extends RoleMapperModel {
String getId();
String getUsername();
void setUsername(String username);
String getFirstName();
void setFirstName(String firstName);
String getLastName();
void setLastName(String lastName);
String getEmail();
void setEmail(String email);
...
}
UserModel
implementations provide access to read and update metadata about the user including things like username, name, email, role and group mappings, as well as other arbitrary attributes.
There are other model classes within the org.keycloak.models
package that represent other parts of the Red Hat build of Keycloak metamodel: RealmModel
, RoleModel
, GroupModel
, and ClientModel
.
5.4.1. Storage Ids
One important method of UserModel
is the getId()
method. When implementing UserModel
developers must be aware of the user id format. The format must be:
"f:" + component id + ":" + external id
The Red Hat build of Keycloak runtime often has to look up users by their user id. The user id contains enough information so that the runtime does not have to query every single UserStorageProvider
in the system to find the user.
The component id is the id returned from ComponentModel.getId()
. The ComponentModel
is passed in as a parameter when creating the provider class so you can get it from there. The external id is information your provider class needs to find the user in the external store. This is often a username or a uid. For example, it might look something like this:
f:332a234e31234:wburke
When the runtime does a lookup by id, the id is parsed to obtain the component id. The component id is used to locate the UserStorageProvider
that was originally used to load the user. That provider is then passed the id. The provider again parses the id to obtain the external id and it will use to locate the user in external user storage.
This format has the drawback that it can generate long IDs for the external storage users. This is specially important when combined with the WebAuthn authentication, which limits the user handle ID to 64 bytes. For that reason, if the storage users are going to use WebAuthn authentication, it is important to limit the full storage ID to 64 characters. The method validateConfiguration
can be used to assign a short ID for the provider component on creation, giving some space to the user IDs within the 64 byte limitation.
@Override
void validateConfiguration(KeycloakSession session, RealmModel realm, ComponentModel model)
throws ComponentValidationException
{
// ...
if (model.getId() == null) {
// On creation use short UUID of 22 chars, 40 chars left for the user ID
model.setId(KeycloakModelUtils.generateShortId());
}
}
5.5. Packaging and deployment
In order for Red Hat build of Keycloak to recognize the provider, you need to add a file to the JAR: META-INF/services/org.keycloak.storage.UserStorageProviderFactory
. This file must contain a line-separated list of fully qualified classnames of the UserStorageProviderFactory
implementations:
org.keycloak.examples.federation.properties.ClasspathPropertiesStorageFactory
org.keycloak.examples.federation.properties.FilePropertiesStorageFactory
To deploy this jar, copy it to the providers/
directory, then run bin/kc.[sh|bat] build
.
5.6. Simple read-only, lookup example
To illustrate the basics of implementing the User Storage SPI let’s walk through a simple example. In this chapter you’ll see the implementation of a simple UserStorageProvider
that looks up users in a simple property file. The property file contains username and password definitions and is hardcoded to a specific location on the classpath. The provider will be able to look up the user by ID and username and also be able to validate passwords. Users that originate from this provider will be read-only.
5.6.1. Provider class
The first thing we will walk through is the UserStorageProvider
class.
public class PropertyFileUserStorageProvider implements
UserStorageProvider,
UserLookupProvider,
CredentialInputValidator,
CredentialInputUpdater
{
...
}
Our provider class, PropertyFileUserStorageProvider
, implements many interfaces. It implements the UserStorageProvider
as that is a base requirement of the SPI. It implements the UserLookupProvider
interface because we want to be able to log in with users stored by this provider. It implements the CredentialInputValidator
interface because we want to be able to validate passwords entered in using the login screen. Our property file is read-only. We implement the CredentialInputUpdater
because we want to post an error condition when the user attempts to update his password.
protected KeycloakSession session;
protected Properties properties;
protected ComponentModel model;
// map of loaded users in this transaction
protected Map<String, UserModel> loadedUsers = new HashMap<>();
public PropertyFileUserStorageProvider(KeycloakSession session, ComponentModel model, Properties properties) {
this.session = session;
this.model = model;
this.properties = properties;
}
The constructor for this provider class is going to store the reference to the KeycloakSession
, ComponentModel
, and property file. We’ll use all of these later. Also notice that there is a map of loaded users. Whenever we find a user we will store it in this map so that we avoid re-creating it again within the same transaction. This is a good practice to follow as many providers will need to do this (that is, any provider that integrates with JPA). Remember also that provider class instances are created once per transaction and are closed after the transaction completes.
5.6.1.1. UserLookupProvider implementation
@Override
public UserModel getUserByUsername(RealmModel realm, String username) {
UserModel adapter = loadedUsers.get(username);
if (adapter == null) {
String password = properties.getProperty(username);
if (password != null) {
adapter = createAdapter(realm, username);
loadedUsers.put(username, adapter);
}
}
return adapter;
}
protected UserModel createAdapter(RealmModel realm, String username) {
return new AbstractUserAdapter(session, realm, model) {
@Override
public String getUsername() {
return username;
}
};
}
@Override
public UserModel getUserById(RealmModel realm, String id) {
StorageId storageId = new StorageId(id);
String username = storageId.getExternalId();
return getUserByUsername(realm, username);
}
@Override
public UserModel getUserByEmail(RealmModel realm, String email) {
return null;
}
The getUserByUsername()
method is invoked by the Red Hat build of Keycloak login page when a user logs in. In our implementation we first check the loadedUsers
map to see if the user has already been loaded within this transaction. If it hasn’t been loaded we look in the property file for the username. If it exists we create an implementation of UserModel
, store it in loadedUsers
for future reference, and return this instance.
The createAdapter()
method uses the helper class org.keycloak.storage.adapter.AbstractUserAdapter
. This provides a base implementation for UserModel
. It automatically generates a user id based on the required storage id format using the username of the user as the external id.
"f:" + component id + ":" + username
Every get method of AbstractUserAdapter
either returns null or empty collections. However, methods that return role and group mappings will return the default roles and groups configured for the realm for every user. Every set method of AbstractUserAdapter
will throw a org.keycloak.storage.ReadOnlyException
. So if you attempt to modify the user in the Admin Console, you will get an error.
The getUserById()
method parses the id
parameter using the org.keycloak.storage.StorageId
helper class. The StorageId.getExternalId()
method is invoked to obtain the username embedded in the id
parameter. The method then delegates to getUserByUsername()
.
Emails are not stored, so the getUserByEmail()
method returns null.
5.6.1.2. CredentialInputValidator implementation
Next let’s look at the method implementations for CredentialInputValidator
.
@Override
public boolean isConfiguredFor(RealmModel realm, UserModel user, String credentialType) {
String password = properties.getProperty(user.getUsername());
return credentialType.equals(PasswordCredentialModel.TYPE) && password != null;
}
@Override
public boolean supportsCredentialType(String credentialType) {
return credentialType.equals(PasswordCredentialModel.TYPE);
}
@Override
public boolean isValid(RealmModel realm, UserModel user, CredentialInput input) {
if (!supportsCredentialType(input.getType())) return false;
String password = properties.getProperty(user.getUsername());
if (password == null) return false;
return password.equals(input.getChallengeResponse());
}
The isConfiguredFor()
method is called by the runtime to determine if a specific credential type is configured for the user. This method checks to see that the password is set for the user.
The supportsCredentialType()
method returns whether validation is supported for a specific credential type. We check to see if the credential type is password
.
The isValid()
method is responsible for validating passwords. The CredentialInput
parameter is really just an abstract interface for all credential types. We make sure that we support the credential type and also that it is an instance of UserCredentialModel
. When a user logs in through the login page, the plain text of the password input is put into an instance of UserCredentialModel
. The isValid()
method checks this value against the plain text password stored in the properties file. A return value of true
means the password is valid.
5.6.1.3. CredentialInputUpdater implementation
As noted before, the only reason we implement the CredentialInputUpdater
interface in this example is to forbid modifications of user passwords. The reason we have to do this is because otherwise the runtime would allow the password to be overridden in Red Hat build of Keycloak local storage. We’ll talk more about this later in this chapter.
@Override
public boolean updateCredential(RealmModel realm, UserModel user, CredentialInput input) {
if (input.getType().equals(PasswordCredentialModel.TYPE)) throw new ReadOnlyException("user is read only for this update");
return false;
}
@Override
public void disableCredentialType(RealmModel realm, UserModel user, String credentialType) {
}
@Override
public Stream<String> getDisableableCredentialTypesStream(RealmModel realm, UserModel user) {
return Stream.empty();
}
The updateCredential()
method just checks to see if the credential type is password. If it is, a ReadOnlyException
is thrown.
5.6.2. Provider factory implementation
Now that the provider class is complete, we now turn our attention to the provider factory class.
public class PropertyFileUserStorageProviderFactory
implements UserStorageProviderFactory<PropertyFileUserStorageProvider> {
public static final String PROVIDER_NAME = "readonly-property-file";
@Override
public String getId() {
return PROVIDER_NAME;
}
First thing to notice is that when implementing the UserStorageProviderFactory
class, you must pass in the concrete provider class implementation as a template parameter. Here we specify the provider class we defined before: PropertyFileUserStorageProvider
.
If you do not specify the template parameter, your provider will not function. The runtime does class introspection to determine the capability interfaces that the provider implements.
The getId()
method identifies the factory in the runtime and will also be the string shown in the admin console when you want to enable a user storage provider for the realm.
5.6.2.1. Initialization
private static final Logger logger = Logger.getLogger(PropertyFileUserStorageProviderFactory.class);
protected Properties properties = new Properties();
@Override
public void init(Config.Scope config) {
InputStream is = getClass().getClassLoader().getResourceAsStream("/users.properties");
if (is == null) {
logger.warn("Could not find users.properties in classpath");
} else {
try {
properties.load(is);
} catch (IOException ex) {
logger.error("Failed to load users.properties file", ex);
}
}
}
@Override
public PropertyFileUserStorageProvider create(KeycloakSession session, ComponentModel model) {
return new PropertyFileUserStorageProvider(session, model, properties);
}
The UserStorageProviderFactory
interface has an optional init()
method you can implement. When Red Hat build of Keycloak boots up, only one instance of each provider factory is created. Also at boot time, the init()
method is called on each of these factory instances. There’s also a postInit()
method you can implement as well. After each factory’s init()
method is invoked, their postInit()
methods are called.
In our init()
method implementation, we find the property file containing our user declarations from the classpath. We then load the properties
field with the username and password combinations stored there.
The Config.Scope
parameter is factory configuration that configured through server configuration.
For example, by running the server with the following argument:
kc.[sh|bat] start --spi-storage--readonly-property-file--path=/other-users.properties
We can specify the classpath of the user property file instead of hardcoding it. Then you can retrieve the configuration in the PropertyFileUserStorageProviderFactory.init()
:
public void init(Config.Scope config) {
String path = config.get("path");
InputStream is = getClass().getClassLoader().getResourceAsStream(path);
...
}
5.6.2.2. Create method
Our last step in creating the provider factory is the create()
method.
@Override
public PropertyFileUserStorageProvider create(KeycloakSession session, ComponentModel model) {
return new PropertyFileUserStorageProvider(session, model, properties);
}
We simply allocate the PropertyFileUserStorageProvider
class. This create method will be called once per transaction.
5.6.3. Packaging and deployment
The class files for our provider implementation should be placed in a jar. You also have to declare the provider factory class within the META-INF/services/org.keycloak.storage.UserStorageProviderFactory
file.
org.keycloak.examples.federation.properties.FilePropertiesStorageFactory
To deploy this jar, copy it to the providers/
directory, then run bin/kc.[sh|bat] build
.
5.6.4. Enabling the provider in the Admin Console
You enable user storage providers per realm within the User Federation page in the Admin Console.
User Federation
Procedure
Select the provider we just created from the list:
readonly-property-file
.The configuration page for our provider displays.
Click Save because we have nothing to configure.
Configured Provider
Return to the main User Federation page
You now see your provider listed.
User Federation
You will now be able to log in with a user declared in the users.properties
file. This user will only be able to view the account page after logging in.
5.7. Configuration techniques
Our PropertyFileUserStorageProvider
example is a bit contrived. It is hardcoded to a property file that is embedded in the jar of the provider, which is not terribly useful. We might want to make the location of this file configurable per instance of the provider. In other words, we might want to reuse this provider multiple times in multiple different realms and point to completely different user property files. We’ll also want to perform this configuration within the Admin Console UI.
The UserStorageProviderFactory
has additional methods you can implement that handle provider configuration. You describe the variables you want to configure per provider and the Admin Console automatically renders a generic input page to gather this configuration. When implemented, callback methods also validate the configuration before it is saved, when a provider is created for the first time, and when it is updated. UserStorageProviderFactory
inherits these methods from the org.keycloak.component.ComponentFactory
interface.
List<ProviderConfigProperty> getConfigProperties();
default
void validateConfiguration(KeycloakSession session, RealmModel realm, ComponentModel model)
throws ComponentValidationException
{
}
default
void onCreate(KeycloakSession session, RealmModel realm, ComponentModel model) {
}
default
void onUpdate(KeycloakSession session, RealmModel realm, ComponentModel model) {
}
The ComponentFactory.getConfigProperties()
method returns a list of org.keycloak.provider.ProviderConfigProperty
instances. These instances declare metadata that is needed to render and store each configuration variable of the provider.
5.7.1. Configuration example
Let’s expand our PropertyFileUserStorageProviderFactory
example to allow you to point a provider instance to a specific file on disk.
PropertyFileUserStorageProviderFactory
public class PropertyFileUserStorageProviderFactory
implements UserStorageProviderFactory<PropertyFileUserStorageProvider> {
protected static final List<ProviderConfigProperty> configMetadata;
static {
configMetadata = ProviderConfigurationBuilder.create()
.property().name("path")
.type(ProviderConfigProperty.STRING_TYPE)
.label("Path")
.defaultValue("${jboss.server.config.dir}/example-users.properties")
.helpText("File path to properties file")
.add().build();
}
@Override
public List<ProviderConfigProperty> getConfigProperties() {
return configMetadata;
}
The ProviderConfigurationBuilder
class is a great helper class to create a list of configuration properties. Here we specify a variable named path
that is a String type. On the Admin Console configuration page for this provider, this configuration variable is labeled as Path
and has a default value of ${jboss.server.config.dir}/example-users.properties
. When you hover over the tooltip of this configuration option, it displays the help text, File path to properties file
.
The next thing we want to do is to verify that this file exists on disk. We do not want to enable an instance of this provider in the realm unless it points to a valid user property file. To do this, we implement the validateConfiguration()
method.
@Override
public void validateConfiguration(KeycloakSession session, RealmModel realm, ComponentModel config)
throws ComponentValidationException {
String fp = config.getConfig().getFirst("path");
if (fp == null) throw new ComponentValidationException("user property file does not exist");
fp = EnvUtil.replace(fp);
File file = new File(fp);
if (!file.exists()) {
throw new ComponentValidationException("user property file does not exist");
}
}
The validateConfiguration()
method provides the configuration variable from the ComponentModel
to verify if that file exists on disk. Notice that the use of the org.keycloak.common.util.EnvUtil.replace()
method. With this method any string that includes ${}
will replace that value with a system property value. The ${jboss.server.config.dir}
string corresponds to the conf/
directory of our server and is really useful for this example.
Next thing we have to do is remove the old init()
method. We do this because user property files are going to be unique per provider instance. We move this logic to the create()
method.
@Override
public PropertyFileUserStorageProvider create(KeycloakSession session, ComponentModel model) {
String path = model.getConfig().getFirst("path");
Properties props = new Properties();
try {
InputStream is = new FileInputStream(path);
props.load(is);
is.close();
} catch (IOException e) {
throw new RuntimeException(e);
}
return new PropertyFileUserStorageProvider(session, model, props);
}
This logic is, of course, inefficient as every transaction reads the entire user property file from disk, but hopefully this illustrates, in a simple way, how to hook in configuration variables.
5.7.2. Configuring the provider in the Admin Console
Now that the configuration is enabled, you can set the path
variable when you configure the provider in the Admin Console.
5.8. Add/Remove user and query capability interfaces
One thing we have not done with our example is allow it to add and remove users or change passwords. Users defined in our example are also not queryable or viewable in the Admin Console. To add these enhancements, our example provider must implement the UserQueryMethodsProvider
(or UserQueryProvider
) and UserRegistrationProvider
interfaces.
5.8.1. Implementing UserRegistrationProvider
Use this procedure to implement adding and removing users from the particular store, we first have to be able to save our properties file to disk.
PropertyFileUserStorageProvider
public void save() {
String path = model.getConfig().getFirst("path");
path = EnvUtil.replace(path);
try {
FileOutputStream fos = new FileOutputStream(path);
properties.store(fos, "");
fos.close();
} catch (IOException e) {
throw new RuntimeException(e);
}
}
Then, the implementation of the addUser()
and removeUser()
methods becomes simple.
PropertyFileUserStorageProvider
public static final String UNSET_PASSWORD="#$!-UNSET-PASSWORD";
@Override
public UserModel addUser(RealmModel realm, String username) {
synchronized (properties) {
properties.setProperty(username, UNSET_PASSWORD);
save();
}
return createAdapter(realm, username);
}
@Override
public boolean removeUser(RealmModel realm, UserModel user) {
synchronized (properties) {
if (properties.remove(user.getUsername()) == null) return false;
save();
return true;
}
}
Notice that when adding a user we set the password value of the property map to be UNSET_PASSWORD
. We do this as we can’t have null values for a property in the property value. We also have to modify the CredentialInputValidator
methods to reflect this.
The addUser()
method will be called if the provider implements the UserRegistrationProvider
interface. If your provider has a configuration switch to turn off adding a user, returning null
from this method will skip the provider and call the next one.
PropertyFileUserStorageProvider
@Override
public boolean isValid(RealmModel realm, UserModel user, CredentialInput input) {
if (!supportsCredentialType(input.getType()) || !(input instanceof UserCredentialModel)) return false;
UserCredentialModel cred = (UserCredentialModel)input;
String password = properties.getProperty(user.getUsername());
if (password == null || UNSET_PASSWORD.equals(password)) return false;
return password.equals(cred.getValue());
}
Since we can now save our property file, it also makes sense to allow password updates.
PropertyFileUserStorageProvider
@Override
public boolean updateCredential(RealmModel realm, UserModel user, CredentialInput input) {
if (!(input instanceof UserCredentialModel)) return false;
if (!input.getType().equals(PasswordCredentialModel.TYPE)) return false;
UserCredentialModel cred = (UserCredentialModel)input;
synchronized (properties) {
properties.setProperty(user.getUsername(), cred.getValue());
save();
}
return true;
}
We can now also implement disabling a password.
PropertyFileUserStorageProvider
@Override
public void disableCredentialType(RealmModel realm, UserModel user, String credentialType) {
if (!credentialType.equals(PasswordCredentialModel.TYPE)) return;
synchronized (properties) {
properties.setProperty(user.getUsername(), UNSET_PASSWORD);
save();
}
}
private static final Set<String> disableableTypes = new HashSet<>();
static {
disableableTypes.add(PasswordCredentialModel.TYPE);
}
@Override
public Stream<String> getDisableableCredentialTypes(RealmModel realm, UserModel user) {
return disableableTypes.stream();
}
With these methods implemented, you’ll now be able to change and disable the password for the user in the Admin Console.
5.8.2. Implementing UserQueryProvider
UserQueryProvider
is combination of UserQueryMethodsProvider
and UserCountMethodsProvider
. Without implementing UserQueryMethodsProvider
the Admin Console would not be able to view and manage users that were loaded by our example provider. Let’s look at implementing this interface.
PropertyFileUserStorageProvider
@Override
public int getUsersCount(RealmModel realm) {
return properties.size();
}
@Override
public Stream<UserModel> searchForUserStream(RealmModel realm, String search, Integer firstResult, Integer maxResults) {
Predicate<String> predicate = "*".equals(search) ? username -> true : username -> username.contains(search);
return properties.keySet().stream()
.map(String.class::cast)
.filter(predicate)
.skip(firstResult)
.map(username -> getUserByUsername(realm, username))
.limit(maxResults);
}
The first declaration of searchForUserStream()
takes a String
parameter. In this example, the parameter represents a username that you want to search by. This string can be a substring, which explains the choice of the String.contains()
method when doing the search. Notice the use of *
to indicate to request a list of all users. The method iterates over the key set of the property file, delegating to getUserByUsername()
to load a user. Notice that we are indexing this call based on the firstResult
and maxResults
parameter. If your external store does not support pagination, you will have to do similar logic.
PropertyFileUserStorageProvider
@Override
public Stream<UserModel> searchForUserStream(RealmModel realm, Map<String, String> params, Integer firstResult, Integer maxResults) {
// only support searching by username
String usernameSearchString = params.get("username");
if (usernameSearchString != null)
return searchForUserStream(realm, usernameSearchString, firstResult, maxResults);
// if we are not searching by username, return all users
return searchForUserStream(realm, "*", firstResult, maxResults);
}
The searchForUserStream()
method that takes a Map
parameter can search for a user based on first, last name, username, and email. Only usernames are stored, so the search is based only on usernames except when the Map
parameter does not contain the username
attribute. In this case, all users are returned. In that situation, the searchForUserStream(realm, search, firstResult, maxResults)
is used.
PropertyFileUserStorageProvider
@Override
public Stream<UserModel> getGroupMembersStream(RealmModel realm, GroupModel group, Integer firstResult, Integer maxResults) {
return Stream.empty();
}
@Override
public Stream<UserModel> searchForUserByUserAttributeStream(RealmModel realm, String attrName, String attrValue) {
return Stream.empty();
}
Groups or attributes are not stored, so the other methods return an empty stream.
5.9. Augmenting external storage
The PropertyFileUserStorageProvider
example is really limited. While we will be able to log in with users stored in a property file, we won’t be able to do much else. If users loaded by this provider need special role or group mappings to fully access particular applications there is no way for us to add additional role mappings to these users. You also can’t modify or add additional important attributes like email, first and last name.
For these types of situations, Red Hat build of Keycloak allows you to augment your external store by storing extra information in Red Hat build of Keycloak’s database. This is called federated user storage and is encapsulated within the org.keycloak.storage.federated.UserFederatedStorageProvider
class.
UserFederatedStorageProvider
package org.keycloak.storage.federated;
public interface UserFederatedStorageProvider extends Provider,
UserAttributeFederatedStorage,
UserBrokerLinkFederatedStorage,
UserConsentFederatedStorage,
UserNotBeforeFederatedStorage,
UserGroupMembershipFederatedStorage,
UserRequiredActionsFederatedStorage,
UserRoleMappingsFederatedStorage,
UserFederatedUserCredentialStore {
...
}
The UserFederatedStorageProvider
instance is available on the UserStorageUtil.userFederatedStorage(KeycloakSession)
method. It has all different kinds of methods for storing attributes, group and role mappings, different credential types, and required actions. If your external store’s datamodel cannot support the full Red Hat build of Keycloak feature set, then this service can fill in the gaps.
Red Hat build of Keycloak comes with a helper class org.keycloak.storage.adapter.AbstractUserAdapterFederatedStorage
that will delegate every single UserModel
method except get/set of username to user federated storage. Override the methods you need to override to delegate to your external storage representations. It is strongly suggested you read the javadoc of this class as it has smaller protected methods you may want to override. Specifically surrounding group membership and role mappings.
5.9.1. Augmentation example
In our PropertyFileUserStorageProvider
example, we just need a simple change to our provider to use the AbstractUserAdapterFederatedStorage
.
PropertyFileUserStorageProvider
protected UserModel createAdapter(RealmModel realm, String username) {
return new AbstractUserAdapterFederatedStorage(session, realm, model) {
@Override
public String getUsername() {
return username;
}
@Override
public void setUsername(String username) {
String pw = (String)properties.remove(username);
if (pw != null) {
properties.put(username, pw);
save();
}
}
};
}
We instead define an anonymous class implementation of AbstractUserAdapterFederatedStorage
. The setUsername()
method makes changes to the properties file and saves it.
5.10. Import implementation strategy
When implementing a user storage provider, there’s another strategy you can take. Instead of using user federated storage, you can create a user locally in the Red Hat build of Keycloak built-in user database and copy attributes from your external store into this local copy. There are many advantages to this approach.
- Red Hat build of Keycloak basically becomes a persistence user cache for your external store. Once the user is imported you’ll no longer hit the external store thus taking load off of it.
- If you are moving to Red Hat build of Keycloak as your official user store and deprecating the old external store, you can slowly migrate applications to use Red Hat build of Keycloak. When all applications have been migrated, unlink the imported user, and retire the old legacy external store.
There are some obvious disadvantages though to using an import strategy:
- Looking up a user for the first time will require multiple updates to Red Hat build of Keycloak database. This can be a big performance loss under load and put a lot of strain on the Red Hat build of Keycloak database. The user federated storage approach will only store extra data as needed and may never be used depending on the capabilities of your external store.
- With the import approach, you have to keep local Red Hat build of Keycloak storage and external storage in sync. The User Storage SPI has capability interfaces that you can implement to support synchronization, but this can quickly become painful and messy.
To implement the import strategy you simply check to see first if the user has been imported locally. If so return the local user, if not create the user locally and import data from the external store. You can also proxy the local user so that most changes are automatically synchronized.
This will be a bit contrived, but we can extend our PropertyFileUserStorageProvider
to take this approach. We begin first by modifying the createAdapter()
method.
PropertyFileUserStorageProvider
protected UserModel createAdapter(RealmModel realm, String username) {
UserProvider userProvider = session.getProvider(UserProvider.class);
UserModel local = userProvider.getUserByUsername(realm, username);
if (local == null) {
local = userProvider.addUser(realm, username);
local.setFederationLink(model.getId());
}
return new UserModelDelegate(local) {
@Override
public void setUsername(String username) {
String pw = (String)properties.remove(username);
if (pw != null) {
properties.put(username, pw);
save();
}
super.setUsername(username);
}
};
}
In this method we call session.getProvider(UserProvider.class)
to obtain a reference to local Red Hat build of Keycloak user storage. We see if the user is stored locally, if not, we add it locally. Do not set the id
of the local user. Let Red Hat build of Keycloak automatically generate the id
. Also note that we call UserModel.setFederationLink()
and pass in the ID of the ComponentModel
of our provider. This sets a link between the provider and the imported user.
When a user storage provider is removed, any user imported by it will also be removed. This is one of the purposes of calling UserModel.setFederationLink()
.
Another thing to note is that if a local user is linked, your storage provider will still be delegated to for methods that it implements from the CredentialInputValidator
and CredentialInputUpdater
interfaces. Returning false
from a validation or update will just result in Red Hat build of Keycloak seeing if it can validate or update using local storage.
Also notice that we are proxying the local user using the org.keycloak.models.utils.UserModelDelegate
class. This class is an implementation of UserModel
. Every method just delegates to the UserModel
it was instantiated with. We override the setUsername()
method of this delegate class to synchronize automatically with the property file. For your providers, you can use this to intercept other methods on the local UserModel
to perform synchronization with your external store. For example, get methods could make sure that the local store is in sync. Set methods keep the external store in sync with the local one. One thing to note is that the getId()
method should always return the id that was auto generated when you created the user locally. You should not return a federated id as shown in the other non-import examples.
If your provider is implementing the UserRegistrationProvider
interface, your removeUser()
method does not need to remove the user from local storage. The runtime will automatically perform this operation. Also note that removeUser()
will be invoked before it is removed from local storage.
5.10.1. ImportedUserValidation interface
If you remember earlier in this chapter, we discussed how querying for a user worked. Local storage is queried first, if the user is found there, then the query ends. This is a problem for our above implementation as we want to proxy the local UserModel
so that we can keep usernames in sync. The User Storage SPI has a callback for whenever a linked local user is loaded from the local database.
package org.keycloak.storage.user;
public interface ImportedUserValidation {
/**
* If this method returns null, then the user in local storage will be removed
*
* @param realm
* @param user
* @return null if user no longer valid
*/
UserModel validate(RealmModel realm, UserModel user);
}
Whenever a linked local user is loaded, if the user storage provider class implements this interface, then the validate()
method is called. Here you can proxy the local user passed in as a parameter and return it. That new UserModel
will be used. You can also optionally do a check to see if the user still exists in the external store. If validate()
returns null
, then the local user will be removed from the database.
5.10.2. ImportSynchronization interface
With the import strategy you can see that it is possible for the local user copy to get out of sync with external storage. For example, maybe a user has been removed from the external store. The User Storage SPI has an additional interface you can implement to deal with this, org.keycloak.storage.user.ImportSynchronization
:
package org.keycloak.storage.user;
public interface ImportSynchronization {
SynchronizationResult sync(KeycloakSessionFactory sessionFactory, String realmId, UserStorageProviderModel model);
SynchronizationResult syncSince(Date lastSync, KeycloakSessionFactory sessionFactory, String realmId, UserStorageProviderModel model);
}
This interface is implemented by the provider factory. Once this interface is implemented by the provider factory, the administration console management page for the provider shows additional options. You can manually force a synchronization by clicking a button. This invokes the ImportSynchronization.sync()
method. Also, additional configuration options are displayed that allow you to automatically schedule a synchronization. Automatic synchronizations invoke the syncSince()
method.
5.11. User caches
When a user object is loaded by ID, username, or email queries it is cached. When a user object is being cached, it iterates through the entire UserModel
interface and pulls this information to a local in-memory-only cache. In a cluster, this cache is still local, but it becomes an invalidation cache. When a user object is modified, it is evicted. This eviction event is propagated to the entire cluster so that the other nodes' user cache is also invalidated.
5.11.1. Managing the user cache
You can access the user cache by calling KeycloakSession.getProvider(UserCache.class)
.
/**
* All these methods effect an entire cluster of Keycloak instances.
*
* @author <a href="mailto:bill@burkecentral.com">Bill Burke</a>
* @version $Revision: 1 $
*/
public interface UserCache extends UserProvider {
/**
* Evict user from cache.
*
* @param user
*/
void evict(RealmModel realm, UserModel user);
/**
* Evict users of a specific realm
*
* @param realm
*/
void evict(RealmModel realm);
/**
* Clear cache entirely.
*
*/
void clear();
}
There are methods for evicting specific users, users contained in a specific realm, or the entire cache.
5.11.2. OnUserCache callback interface
You might want to cache additional information that is specific to your provider implementation. The User Storage SPI has a callback whenever a user is cached: org.keycloak.models.cache.OnUserCache
.
public interface OnUserCache {
void onCache(RealmModel realm, CachedUserModel user, UserModel delegate);
}
Your provider class should implement this interface if it wants this callback. The UserModel
delegate parameter is the UserModel
instance returned by your provider. The CachedUserModel
is an expanded UserModel
interface. This is the instance that is cached locally in local storage.
public interface CachedUserModel extends UserModel {
/**
* Invalidates the cache for this user and returns a delegate that represents the actual data provider
*
* @return
*/
UserModel getDelegateForUpdate();
boolean isMarkedForEviction();
/**
* Invalidate the cache for this model
*
*/
void invalidate();
/**
* When was the model was loaded from database.
*
* @return
*/
long getCacheTimestamp();
/**
* Returns a map that contains custom things that are cached along with this model. You can write to this map.
*
* @return
*/
ConcurrentHashMap getCachedWith();
}
This CachedUserModel
interface allows you to evict the user from the cache and get the provider UserModel
instance. The getCachedWith()
method returns a map that allows you to cache additional information pertaining to the user. For example, credentials are not part of the UserModel
interface. If you wanted to cache credentials in memory, you would implement OnUserCache
and cache your user’s credentials using the getCachedWith()
method.
5.11.3. Cache policies
On the administration console management page for your user storage provider, you can specify a unique cache policy.
5.12. Leveraging Jakarta EE
Since version 20, Keycloak relies only on Quarkus. Unlike WildFly, Quarkus is not an Application Server.
Therefore, the User Storage Providers cannot be packaged within any Jakarta EE component or make it an EJB as was the case when Keycloak ran over WildFly in previous versions.
Providers implementations are required to be plain java objects which implement the suitable User Storage SPI interfaces, as was explained in the previous sections. They must be packaged and deployed as stated in the Migration Guide. See Migrating custom providers.
You can still implement your custom UserStorageProvider
class, which is able to integrate an external database by JPA Entity Manager, as shown in this example:
CDI is not supported.
5.13. REST management API
You can create, remove, and update your user storage provider deployments through the administrator REST API. The User Storage SPI is built on top of a generic component interface so you will be using that generic API to manage your providers.
The REST Component API lives under your realm admin resource.
/admin/realms/{realm-name}/components
We will only show this REST API interaction with the Java client. Hopefully you can extract how to do this from curl
from this API.
public interface ComponentsResource {
@GET
@Produces(MediaType.APPLICATION_JSON)
public List<ComponentRepresentation> query();
@GET
@Produces(MediaType.APPLICATION_JSON)
public List<ComponentRepresentation> query(@QueryParam("parent") String parent);
@GET
@Produces(MediaType.APPLICATION_JSON)
public List<ComponentRepresentation> query(@QueryParam("parent") String parent, @QueryParam("type") String type);
@GET
@Produces(MediaType.APPLICATION_JSON)
public List<ComponentRepresentation> query(@QueryParam("parent") String parent,
@QueryParam("type") String type,
@QueryParam("name") String name);
@POST
@Consumes(MediaType.APPLICATION_JSON)
Response add(ComponentRepresentation rep);
@Path("{id}")
ComponentResource component(@PathParam("id") String id);
}
public interface ComponentResource {
@GET
public ComponentRepresentation toRepresentation();
@PUT
@Consumes(MediaType.APPLICATION_JSON)
public void update(ComponentRepresentation rep);
@DELETE
public void remove();
}
To create a user storage provider, you must specify the provider id, a provider type of the string org.keycloak.storage.UserStorageProvider
, as well as the configuration.
import org.keycloak.admin.client.Keycloak;
import org.keycloak.representations.idm.RealmRepresentation;
...
Keycloak keycloak = Keycloak.getInstance(
"http://localhost:8080",
"master",
"admin",
"password",
"admin-cli");
RealmResource realmResource = keycloak.realm("master");
RealmRepresentation realm = realmResource.toRepresentation();
ComponentRepresentation component = new ComponentRepresentation();
component.setName("home");
component.setProviderId("readonly-property-file");
component.setProviderType("org.keycloak.storage.UserStorageProvider");
component.setParentId(realm.getId());
component.setConfig(new MultivaluedHashMap());
component.getConfig().putSingle("path", "~/users.properties");
realmResource.components().add(component);
// retrieve a component
List<ComponentRepresentation> components = realmResource.components().query(realm.getId(),
"org.keycloak.storage.UserStorageProvider",
"home");
component = components.get(0);
// Update a component
component.getConfig().putSingle("path", "~/my-users.properties");
realmResource.components().component(component.getId()).update(component);
// Remove a component
realmREsource.components().component(component.getId()).remove();
5.14. Migrating from an earlier user federation SPI
This chapter is only applicable if you have implemented a provider using the earlier (and now removed) User Federation SPI.
In Keycloak version 2.4.0 and earlier there was a User Federation SPI. Red Hat Single Sign-On version 7.0, although unsupported, had this earlier SPI available as well. This earlier User Federation SPI has been removed from Keycloak version 2.5.0 and Red Hat Single Sign-On version 7.1. However, if you have written a provider with this earlier SPI, this chapter discusses some strategies you can use to port it.
5.14.1. Import versus non-import
The earlier User Federation SPI required you to create a local copy of a user in the Red Hat build of Keycloak’s database and import information from your external store to the local copy. However, this is no longer a requirement. You can still port your earlier provider as-is, but you should consider whether a non-import strategy might be a better approach.
Advantages of the import strategy:
- Red Hat build of Keycloak basically becomes a persistence user cache for your external store. Once the user is imported you’ll no longer hit the external store, thus taking load off of it.
- If you are moving to Red Hat build of Keycloak as your official user store and deprecating the earlier external store, you can slowly migrate applications to use Red Hat build of Keycloak. When all applications have been migrated, unlink the imported user, and retire the earlier legacy external store.
There are some obvious disadvantages though to using an import strategy:
- Looking up a user for the first time will require multiple updates to Red Hat build of Keycloak database. This can be a big performance loss under load and put a lot of strain on the Red Hat build of Keycloak database. The user federated storage approach will only store extra data as needed and might never be used depending on the capabilities of your external store.
- With the import approach, you have to keep local Red Hat build of Keycloak storage and external storage in sync. The User Storage SPI has capability interfaces that you can implement to support synchronization, but this can quickly become painful and messy.
5.14.2. UserFederationProvider versus UserStorageProvider
The first thing to notice is that UserFederationProvider
was a complete interface. You implemented every method in this interface. However, UserStorageProvider
has instead broken up this interface into multiple capability interfaces that you implement as needed.
UserFederationProvider.getUserByUsername()
and getUserByEmail()
have exact equivalents in the new SPI. The difference between the two is how you import. If you are going to continue with an import strategy, you no longer call KeycloakSession.userStorage().addUser()
to create the user locally. Instead you call KeycloakSession.userLocalStorage().addUser()
. The userStorage()
method no longer exists.
The UserFederationProvider.validateAndProxy()
method has been moved to an optional capability interface, ImportedUserValidation
. You want to implement this interface if you are porting your earlier provider as-is. Also note that in the earlier SPI, this method was called every time the user was accessed, even if the local user is in the cache. In the later SPI, this method is only called when the local user is loaded from local storage. If the local user is cached, then the ImportedUserValidation.validate()
method is not called at all.
The UserFederationProvider.isValid()
method no longer exists in the later SPI.
The UserFederationProvider
methods synchronizeRegistrations()
, registerUser()
, and removeUser()
have been moved to the UserRegistrationProvider
capability interface. This new interface is optional to implement so if your provider does not support creating and removing users, you don’t have to implement it. If your earlier provider had switch to toggle support for registering new users, this is supported in the new SPI, returning null
from UserRegistrationProvider.addUser()
if the provider doesn’t support adding users.
The earlier UserFederationProvider
methods centered around credentials are now encapsulated in the CredentialInputValidator
and CredentialInputUpdater
interfaces, which are also optional to implement depending on if you support validating or updating credentials. Credential management used to exist in UserModel
methods. These also have been moved to the CredentialInputValidator
and CredentialInputUpdater
interfaces. One thing to note that if you do not implement the CredentialInputUpdater
interface, then any credentials provided by your provider can be overridden locally in Red Hat build of Keycloak storage. So if you want your credentials to be read-only, implement the CredentialInputUpdater.updateCredential()
method and return a ReadOnlyException
.
The UserFederationProvider
query methods such as searchByAttributes()
and getGroupMembers()
are now encapsulated in an optional interface UserQueryProvider
. If you do not implement this interface, then users will not be viewable in the admin console. You’ll still be able to log in though.
5.14.3. UserFederationProviderFactory versus UserStorageProviderFactory
The synchronization methods in the earlier SPI are now encapsulated within an optional ImportSynchronization
interface. If you have implemented synchronization logic, then have your new UserStorageProviderFactory
implement the ImportSynchronization
interface.
5.14.4. Upgrading to a new model
The User Storage SPI instances are stored in a different set of relational tables. Red Hat build of Keycloak automatically runs a migration script. If any earlier User Federation providers are deployed for a realm, they are converted to the later storage model as is, including the id
of the data. This migration will only happen if a User Storage provider exists with the same provider ID (i.e., "ldap", "kerberos") as the earlier User Federation provider.
So, knowing this there are different approaches you can take.
- You can remove the earlier provider in your earlier Red Hat build of Keycloak deployment. This will remove the local linked copies of all users you imported. Then, when you upgrade Red Hat build of Keycloak, just deploy and configure your new provider for your realm.
-
The second option is to write your new provider making sure it has the same provider ID:
UserStorageProviderFactory.getId()
. Make sure this provider is deployed to the server. Boot the server, and have the built-in migration script convert from the earlier data model to the later data model. In this case all your earlier linked imported users will work and be the same.
If you have decided to get rid of the import strategy and rewrite your User Storage provider, we suggest that you remove the earlier provider before upgrading Red Hat build of Keycloak. This will remove linked local imported copies of any user you imported.
5.15. Stream-based interfaces
Many of the user storage interfaces in Red Hat build of Keycloak contain query methods that can return potentially large sets of objects, which might lead to significant impacts in terms of memory consumption and processing time. This is especially true when only a small subset of the objects' internal state is used in the query method’s logic.
To provide developers with a more efficient alternative to process large data sets in these query methods, a Streams
sub-interface has been added to user storage interfaces. These Streams
sub-interfaces replace the original collection-based methods in the super-interfaces with stream-based variants, making the collection-based methods default. The default implementation of a collection-based query method invokes its Stream
counterpart and collects the result into the proper collection type.
The Streams
sub-interfaces allow for implementations to focus on the stream-based approach for processing sets of data and benefit from the potential memory and performance optimizations of that approach. The interfaces that offer a Streams
sub-interface to be implemented include a few capability interfaces, all interfaces in the org.keycloak.storage.federated
package and a few others that might be implemented depending on the scope of the custom storage implementation.
See this list of the interfaces that offer a Streams
sub-interface to developers.
| Package | Classes |
|
|
|
|
|
|
|
| All interfaces |
|
|
|
(*) indicates the interface is a capability interface
Custom user storage implementation that want to benefit from the streams approach should simply implement the Streams
sub-interfaces instead of the original interfaces. For example, the following code uses the Streams
variant of the UserQueryProvider
interface:
public class CustomQueryProvider extends UserQueryProvider.Streams {
...
@Override
Stream<UserModel> getUsersStream(RealmModel realm, Integer firstResult, Integer maxResults) {
// custom logic here
}
@Override
Stream<UserModel> searchForUserStream(String search, RealmModel realm) {
// custom logic here
}
...
}
