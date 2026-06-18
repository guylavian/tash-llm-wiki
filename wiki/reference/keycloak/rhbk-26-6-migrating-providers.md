---
title: "Chapter 6. Migrating custom providers - Red Hat build of Keycloak 26.6 Migration Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-migrating-providers
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/migration_guide/migrating-providers
guide: migration_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 6. Migrating custom providers - Red Hat build of Keycloak 26.6 Migration Guide

Chapter 6. Migrating custom providers
Similarly to the Red Hat Single Sign-On 7.6, custom providers are deployed to the Red Hat build of Keycloak by copying them to a deployment directory. In the Red Hat build of Keycloak, copy your providers to the providers
directory instead of standalone/deployments
, which no longer exists. Additional dependencies should also be copied to the providers
directory.
Red Hat build of Keycloak does not use a separate classpath for custom providers, so you may need to be more careful with additional dependencies that you include. In addition, the EAR
and WAR
packaging formats, and jboss-deployment-structure.xml
files, are no longer supported.
While Red Hat Single Sign-On 7.6 automatically discovered custom providers, and even supported the ability to hot-deploy custom providers while Keycloak is running, this behavior is no longer supported. Also, after you make a change to the providers or dependencies in the providers
directory, you have to do a build or restart the server with the auto build feature.
Depending on what APIs your providers use you may also need to make some changes to the providers. See the following sections for details.
6.1. Transition from Java EE to Jakarta EE
Keycloak migrated its codebase from Java EE (Enterprise Edition) to Jakarta EE, which brought various changes. We have upgraded all Jakarta EE specifications in order to support Jakarta EE 10, such as:
- Jakarta Persistence 3.1
- Jakarta RESTful Web Services 3.1
- Jakarta Mail API 2.1
- Jakarta Servlet 6.0
- Jakarta Activation 2.1
Jakarta EE 10 provides a modernized, simplified, lightweight approach to building cloud-native Java applications. The main changes provided within this initiative are changing the namespace from javax.*
to jakarta.*
. This change does not apply for javax.*
packages provided directly in the JDK, such as javax.security
, javax.net
, javax.crypto
, etc.
In addition, Jakarta EE APIs like session/stateless beans are no longer supported.
6.2. Removed third party dependencies
Some dependencies were removed in Red Hat build of Keycloak including
-
openshift-rest-client
-
okio-jvm
-
okhttp
-
commons-lang
-
commons-compress
-
jboss-dmr
-
kotlin-stdlib
Also, since Red Hat build of Keycloak is no longer based on EAP, most of the EAP dependencies were removed. This change means that if you use any of these libraries as dependencies of your own providers deployed to the Red Hat build of Keycloak, you may also need to copy those JAR files explicitly to the Keycloak distribution providers
directory.
6.3. Context and dependency injection are no longer enabled for JAX-RS Resources
To provide a better runtime and leverage as much as possible the underlying stack, all injection points for contextual data using the javax.ws.rs.core.Context
annotation were removed. The expected improvement in performance involves no longer creating proxies instances multiple times during the request lifecycle, and drastically reducing the amount of reflection code at runtime.
If you need access to the current request and response objects, you can now obtain their instances directly from the KeycloakSession
:
@Context
org.jboss.resteasy.spi.HttpRequest request;
@Context
org.jboss.resteasy.spi.HttpResponse response;
was replaced by:
KeycloakSession session = // obtain the session, which is usually available when creating a custom provider from a factory
KeycloakContext context = session.getContext();
HttpRequest request = context.getHttpRequest();
HttpResponse response = context.getHttpResponse();
Additional contextual data can be obtained from the runtime through the KeycloakContext
instance:
KeycloakSession session = // obtain the session
KeycloakContext context = session.getContext();
MyContextualObject myContextualObject = context.getContextObject(MyContextualObject.class);
6.4. Deprecated methods from data providers and models
Some previously deprecated methods are now removed in Red Hat build of Keycloak:
-
RealmModel#searchForGroupByNameStream(String, Integer, Integer)
-
UserProvider#getUsersStream(RealmModel, boolean)
-
UserSessionPersisterProvider#loadUserSessions(int, int, boolean, int, String)
-
Interfaces added for Streamification work, such as
RoleMapperModel.Streams
and similar -
KeycloakModelUtils#getClientScopeMappings
-
Deprecated methods from
KeycloakSession
-
UserQueryProvider#getUsersStream
methods
Also, these other changes were made:
-
Some methods from
UserSessionProvider
were moved toUserLoginFailureProvider
. -
Streams
interfaces in federated storage provider classes were deprecated. Streamification - interfaces now contain only Stream-based methods.
For example in
GroupProvider
interface@Deprecated List<GroupModel> getGroups(RealmModel realm);
was replaced by
Stream<GroupModel> getGroupsStream(RealmModel realm);
Consistent parameter ordering - methods now have strict parameter ordering where
RealmModel
is always the first parameter.For example in
UserLookupProvider
interface:@Deprecated UserModel getUserById(String id, RealmModel realm);
was replaced by
UserModel getUserById(RealmModel realm, String id)
6.4.1. List of changed interfaces
(o.k.
stands for org.keycloak.
package)
server-spi
module-
o.k.credential.CredentialInputUpdater
-
o.k.credential.UserCredentialStore
-
o.k.models.ClientProvider
-
o.k.models.ClientSessionContext
-
o.k.models.GroupModel
-
o.k.models.GroupProvider
-
o.k.models.KeyManager
-
o.k.models.KeycloakSessionFactory
-
o.k.models.ProtocolMapperContainerModel
-
o.k.models.RealmModel
-
o.k.models.RealmProvider
-
o.k.models.RoleContainerModel
-
o.k.models.RoleMapperModel
-
o.k.models.RoleModel
-
o.k.models.RoleProvider
-
o.k.models.ScopeContainerModel
-
o.k.models.UserCredentialManager
-
o.k.models.UserModel
-
o.k.models.UserProvider
-
o.k.models.UserSessionProvider
-
o.k.models.utils.RoleUtils
-
o.k.sessions.AuthenticationSessionProvider
-
o.k.storage.client.ClientLookupProvider
-
o.k.storage.group.GroupLookupProvider
-
o.k.storage.user.UserLookupProvider
-
o.k.storage.user.UserQueryProvider
-
server-spi-private
module-
o.k.events.EventQuery
-
o.k.events.admin.AdminEventQuery
-
o.k.keys.KeyProvider
-
6.4.2. Refactorings in the storage layer
Red Hat build of Keycloak undergoes a large refactoring to simplify the API usage, which impacts existing code. Some of these changes require updates to existing code. The following sections provide more detail.
6.4.2.1. Changes in the module structure
Several public APIs around storage functionality in KeycloakSession
have been consolidated, and some have been moved, deprecated, or removed. Three new modules have been introduced, and data-oriented code from server-spi
, server-spi-private
, and services
modules have been moved there:
org.keycloak:keycloak-model-storage
- Contains all public facing APIs from the storage store, such as the User Storage API.
org.keycloak:keycloak-model-storage-private
-
Contains private implementations that relate to user storage management, such as storage
*Manager
classes. org.keycloak:keycloak-model-storage-services
- Contains all REST endpoints that directly operate on the storage store.
If you are using for example in your custom user storage provider implementation the classes which have been moved to the new modules, you need to update your dependencies to include the new modules listed above.
6.4.2.2. Changes in KeycloakSession
KeycloakSession
has been simplified. Several methods have been removed in KeycloakSession
.
KeycloakSession
session contained several methods for obtaining a provider for a particular object type, such as for a UserProvider
there are users()
, userLocalStorage()
, userCache()
, userStorageManager()
, and userFederatedStorage()
. This situation may be confusing for the developer who has to understand the exact meaning of each method.
For those reasons, only the users()
method is kept in KeycloakSession
, and should replace all other calls listed above. The rest of the methods have been removed. The same pattern of depreciation applies to methods of other object areas, such as clients()
or groups()
. All methods ending in *StorageManager()
and *LocalStorage()
have been removed. The next section describes how to migrate those calls to the new API or use the storage API.
6.4.3. Migrating existing providers
The existing providers need no migration if they do not call a removed method, which should be the case for most providers.
If the provider uses removed methods, but does not rely on local versus non-local storage, changing a call from the now removed userLocalStorage()
to the method users()
is the best option. Be aware that the semantics change here as the new method involves a cache if that has been enabled in the local setup.
This before migration example shows how accessing a removed API does not compile.
session.userLocalStorage();
This post migration example shows accessing the new API when the caller does not depend on the storage API.
session.users();
In the rare case when a custom provider needs to distinguish between the mode of a particular provider, access to the deprecated objects is provided by using the StoreManagers
data store provider. This might be the case if the provider accesses the local storage directly or wants to skip the cache. This option will be available only if the storage modules are part of the deployment.
This before migration example shows accessing a removed API.
session.userLocalStorage();
This post migration example shows accessing the new functionality by the StoreManagers API.
((DatastoreProvider) session.getProvider(DatastoreProvider.class)).userLocalStorage();
Some user storage related APIs have been wrapped in org.keycloak.storage.UserStorageUtil
for convenience.
6.4.4. Changes to RealmModel
The methods getUserStorageProviders
, getUserStorageProvidersStream
, getClientStorageProviders
, getClientStorageProvidersStream
, getRoleStorageProviders
and getRoleStorageProvidersStream
have been removed. Code which depends on these methods should cast the instance as follows:
This before migration code example will not compile due to the changed API.
realm.getClientStorageProvidersStream()...;
This post migration example casts the instance to the legacy interface.
((LegacyRealmModel) realm).getClientStorageProvidersStream()...;
Similarly, code that used to implement the interface RealmModel
and wants to provide these methods should implement the new interface LegacyRealmModel
. This interface is a sub-interface of RealmModel
and includes the old methods:
This before migration code example implements the old interface.
public class MyClass extends RealmModel {
/* might not compile due to @Override annotations for methods no longer present
in the interface RealmModel. / / ... */
}
This post migration code example implements the new interface.
public class MyClass extends LegacyRealmModel {
/* ... */
}
6.4.5. Interface UserCache moved to the legacy module
As the caching status of objects will be transparent to services, the interface UserCache
has been moved to the module keycloak-storage-legacy
.
Code that depends on the legacy implementation should access the UserCache
directly.
This before migration code example will not compile.
session.userCache().evict(realm, user);
This post migration example shows using the API directly.
UserStorageUitl.userCache(session);
To trigger the invalidation of a realm, instead of using the UserCache
API, consider triggering an event:
This before migration code example uses the cache API.
UserCache cache = session.getProvider(UserCache.class);
if (cache != null) cache.evict(realm)();
- This post migration example shows using the invalidation API.*
session.invalidate(InvalidationHandler.ObjectType.REALM, realm.getId());
6.4.6. Credential management for users
Credentials for users were previously managed using session.userCredentialManager().method(realm, user, ...)
. The new way is to leverage user.credentialManager().method(...)
. This form gets the credential functionality closer to the API of users, and does not rely on prior knowledge of the user credential’s location in regard to realm and storage.
The old APIs have been removed.
Before migration: accessing a removed API.
session.userCredentialManager().createCredential(realm, user, credentialModel)
This post migration example shows accessing the new API.
user.credentialManager().createStoredCredential(credentialModel)
For a custom UserStorageProvider
, there is a new method credentialManager()
that needs to be implemented when returning a UserModel
. Those must return an instance of the UserCredentialManager
:
This before migration code example will not compile due to the new method credentialManager()
required by UserModel
.
public class MyUserStorageProvider implements UserLookupProvider, ... {
/* ... */
protected UserModel createAdapter(RealmModel realm, String username) {
return new AbstractUserAdapter(session, realm, model) {
@Override
public String getUsername() {
return username;
}
};
}
}
This post migration example shows the implementation of the API UserModel.credentialManager()
for the store.
public class MyUserStorageProvider implements UserLookupProvider, ... {
/* ... */
protected UserModel createAdapter(RealmModel realm, String username) {
return new AbstractUserAdapter(session, realm, model) {
@Override
public String getUsername() {
return username;
}
@Override
public SubjectCredentialManager credentialManager() {
return new LegacyUserCredentialManager(session, realm, this);
}
};
}
}
