---
title: "Chapter 4. Using external storage - Red Hat build of Keycloak 26.4 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-user-storage-federation
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_administration_guide/user-storage-federation
guide: server_administration_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Organizations can have databases containing information, passwords, and other credentials. Typically, you cannot migrate existing data storage to a Red Hat build of Keycloak deployment so Red Hat build of Keycloak can federate existing external user databases. Red Hat build of Keycloak supports LDAP and Active Directory, but you can also code extensions for any custom user database by using the Re…"
---

# Chapter 4. Using external storage - Red Hat build of Keycloak 26.4 Server Administration Guide

Chapter 4. Using external storage
Organizations can have databases containing information, passwords, and other credentials. Typically, you cannot migrate existing data storage to a Red Hat build of Keycloak deployment so Red Hat build of Keycloak can federate existing external user databases. Red Hat build of Keycloak supports LDAP and Active Directory, but you can also code extensions for any custom user database by using the Red Hat build of Keycloak User Storage SPI.
When a user attempts to log in, Red Hat build of Keycloak examines that user’s storage to find that user. If Red Hat build of Keycloak does not find the user, Red Hat build of Keycloak iterates over each User Storage provider for the realm until it finds a match. Data from the external data storage then maps into a standard user model the Red Hat build of Keycloak runtime consumes. This user model then maps to OIDC token claims and SAML assertion attributes.
External user databases rarely have the data necessary to support all the features of Red Hat build of Keycloak, so the User Storage Provider can opt to store items locally in Red Hat build of Keycloak user data storage. Providers can import users locally and sync periodically with external data storage. This approach depends on the capabilities of the provider and the configuration of the provider. For example, your external user data storage may not support OTP. The OTP can be handled and stored by Red Hat build of Keycloak, depending on the provider.
4.1. Adding a provider
To add a storage provider, perform the following procedure:
Procedure
Click User Federation in the menu.
User federation
Choose to add a Kerberos or LDAP provider
Red Hat build of Keycloak brings you to that provider’s configuration page.
4.2. Dealing with provider failures
If a User Storage Provider fails, you may not be able to log in and view users in the Admin Console. Red Hat build of Keycloak does not detect failures when using a Storage Provider to look up a user, so it cancels the invocation. If you have a Storage Provider with a high priority that fails during user lookup, the login or user query fails with an exception and will not fail over to the next configured provider.
Red Hat build of Keycloak searches the local Red Hat build of Keycloak user database first to resolve users before any LDAP or custom User Storage Provider. Consider creating an administrator account stored in the local Red Hat build of Keycloak user database in case of problems connecting to your LDAP and back ends.
Each LDAP and custom User Storage Provider has an enable
toggle on its Admin Console page. Disabling the User Storage Provider skips the provider when performing queries, so you can view and log in with user accounts in a different provider with lower priority. If your provider uses an import
strategy and is disabled, imported users are still available for lookup in read-only mode.
When a Storage Provider lookup fails, Red Hat build of Keycloak does not fail over because user databases often have duplicate usernames or duplicate emails between them. Duplicate usernames and emails can cause problems because the user loads from one external data store when the admin expects them to load from another data store.
4.3. Lightweight Directory Access Protocol (LDAP) and Active Directory
Red Hat build of Keycloak includes an LDAP/AD provider. You can federate multiple different LDAP servers in one Red Hat build of Keycloak realm and map LDAP user attributes into the Red Hat build of Keycloak common user model.
By default, Red Hat build of Keycloak maps the username, email, first name, and last name of the user account, but you can also configure additional mappings. Red Hat build of Keycloak’s LDAP/AD provider supports password validation using LDAP/AD protocols and storage, edit, and synchronization modes.
4.3.1. Configuring federated LDAP storage
Procedure
Click User Federation in the menu.
User federation
Click Add LDAP providers.
Red Hat build of Keycloak brings you to the LDAP configuration page.
Add LDAP provider
4.3.2. Storage mode
Red Hat build of Keycloak imports users from LDAP into the local Red Hat build of Keycloak user database. This copy of the user database synchronizes on-demand or through a periodic background task. An exception exists for synchronizing passwords. Red Hat build of Keycloak never imports passwords. Password validation always occurs on the LDAP server.
The advantage of synchronization is that all Red Hat build of Keycloak features work efficiently because any required extra per-user data is stored locally. The disadvantage is that each time Red Hat build of Keycloak queries a specific user for the first time, Red Hat build of Keycloak performs a corresponding database insert. Also, when imported users are returned as part of a search operation, a corresponding LDAP search is performed for each one to check if the user still exists in LDAP and do some basic validation.
You can synchronize the import with your LDAP server. Import synchronization is unnecessary when LDAP mappers always read particular attributes from the LDAP rather than the database.
You can use LDAP with Red Hat build of Keycloak without importing users into the Red Hat build of Keycloak user database. The LDAP server backs up the common user model that the Red Hat build of Keycloak runtime uses. If LDAP does not support data that a Red Hat build of Keycloak feature requires, that feature will not work. The advantage of this approach is that you do not have the resource usage of importing and synchronizing copies of LDAP users into the Red Hat build of Keycloak user database.
The Import Users switch on the LDAP configuration page controls this storage mode. To import users, toggle this switch to ON.
If you disable Import Users, you cannot save user profile attributes into the Red Hat build of Keycloak database. Also, you cannot save metadata except for user profile metadata mapped to the LDAP. This metadata can include role mappings, group mappings, and other metadata based on the LDAP mappers' configuration.
When you attempt to change the non-LDAP mapped user data, the user update is not possible. For example, you cannot disable the LDAP mapped user unless the user’s enabled
flag maps to an LDAP attribute.
When working with imported users, Red Hat build of Keycloak performs a LDAP search when the user is queried to validate the user and decorate it so that the configured mappers work properly. This means that extra care must be taken when performing unfiltered user searches that may fetch a big number of users as a LDAP search will be issued for every imported user that is found, possibly affecting the performance in a negative way.
Operations that fetch a single user (for example during login) are usually cached and should not be impacted by this extra LDAP search that is performed when the user is fetched for the first time.
4.3.3. Edit mode
Users and admins can modify user metadata, users through the Account Console, and administrators through the Admin Console. The Edit Mode
configuration on the LDAP configuration page defines the user’s LDAP update privileges.
- READONLY
- You cannot change the username, email, first name, last name, and other mapped attributes. Red Hat build of Keycloak shows an error anytime a user attempts to update these fields. Password updates are not supported.
- WRITABLE
- You can change the username, email, first name, last name, and other mapped attributes and passwords and synchronize them automatically with the LDAP store.
- UNSYNCED
- Red Hat build of Keycloak stores changes to the username, email, first name, last name, and passwords in Red Hat build of Keycloak local storage, so the administrator must synchronize this data back to LDAP. In this mode, Red Hat build of Keycloak deployments can update user metadata on read-only LDAP servers. This option also applies when importing users from LDAP into the local Red Hat build of Keycloak user database.
When Red Hat build of Keycloak creates the LDAP provider, Red Hat build of Keycloak also creates a set of initial LDAP mappers. Red Hat build of Keycloak configures these mappers based on a combination of the Vendor, Edit Mode, and Import Users switches. For example, when edit mode is UNSYNCED, Red Hat build of Keycloak configures the mappers to read a particular user attribute from the database and not from the LDAP server. However, if you later change the edit mode, the mapper’s configuration does not change because it is impossible to detect if the configuration changes changed in UNSYNCED mode. Decide the Edit Mode when creating the LDAP provider. This note applies to Import Users switch also.
4.3.4. Other configuration options
- Console Display Name
- The name of the provider to display in the admin console.
- Priority
- The priority of the provider when looking up users or adding a user.
- Sync Registrations
- Toggle this switch to ON if you want new users created by Red Hat build of Keycloak added to LDAP.
- Allow Kerberos authentication
- Enable Kerberos/SPNEGO authentication in the realm with user data provisioned from LDAP. For more information, see the Kerberos section.
- Remove invalid users during searches
-
Remove users from the local database if they are not available from the user storage when executing searches. If this is true, users no longer available from their corresponding user storage will be deleted from the local database whenever trying to look up users. If false, then users previously imported from the user storage will be kept in the local database, as read-only and disabled, even if that user is no longer available from the user storage. For example, user was deleted directly from LDAP or the
Users DN
is invalid. Note that this behavior will only happen when the user is not yet cached. - Relative User Creation DN
-
Relative DN from the
Users DN
where new users will be created. This allows users to be created in a sub-DN of the parentUsers DN
when using asubtree
search scope. For example, if theUsers DN
is set toou=people,dc=myorg,dc=com
and theRelative User Creation DN
is set toou=engineering
, users will be fetched from theUsers DN
and all sub-DNs, but new users will be stored inou=engineering,ou=people,dc=myorg,dc=com
. In other words, Red Hat build of Keycloak concatenates theRelative User Creation DN
with theUsers DN
(a comma is added automatically when concatenating the DNs) and uses this resulting DN to store users
A similar property is also available in the group and role mappers, allowing groups and roles to be added to a sub-DN of the base DN that is used to search for the groups/roles.
- Other options
- Hover the mouse pointer over the tooltips in the Admin Console to see more details about these options.
4.3.5. Connecting to LDAP over SSL
When you configure a secure connection URL to your LDAP store (for example,ldaps://myhost.com:636
), Red Hat build of Keycloak uses SSL to communicate with the LDAP server. Configure a truststore on the Red Hat build of Keycloak server side so that Red Hat build of Keycloak can trust the SSL connection to LDAP - see Configuring a Truststore chapter.
The Use Truststore SPI
configuration property is deprecated. It should normally be left as Always
.
4.3.6. Synchronizing LDAP users to Red Hat build of Keycloak
If you set the Import Users option, the LDAP Provider handles importing LDAP users into the Red Hat build of Keycloak local database. The first time a user logs in or is returned as part of a user query (e.g. using the search field in the admin console), the LDAP provider imports the LDAP user into the Red Hat build of Keycloak database. During authentication, the LDAP password is validated.
By default, Red Hat build of Keycloak does not support the username and email attributes with case-sensitive values when storing users to the local database. The value for these attributes will be stored in lower-case in the local database. However, if the Import Users option is disabled, Red Hat build of Keycloak will not lower-case the username and email attributes when querying users from LDAP. This behavior allows you to use case-sensitive usernames and emails when Import Users is disabled. Note that this behavior applies only to username and email attributes. Other attributes remain case-sensitive.
It is recommended to not use case-sensitive usernames and emails when using LDAP with Red Hat build of Keycloak, as some features in Red Hat build of Keycloak may not work correctly with case-sensitive usernames and emails.
If you want to sync all LDAP users into the Red Hat build of Keycloak database, configure and enable the Sync Settings on the LDAP provider configuration page.
Two types of synchronization exist:
- Periodic Full sync
- This type synchronizes all LDAP users into the Red Hat build of Keycloak database. The LDAP users already in Red Hat build of Keycloak, but different in LDAP, directly update in the Red Hat build of Keycloak database.
- Periodic Changed users sync
- When synchronizing, Red Hat build of Keycloak creates or updates users created or updated after the last sync only.
The best way to synchronize is to click Synchronize all users when you first create the LDAP provider, then set up periodic synchronization of changed users.
4.3.7. LDAP mappers
LDAP mappers are listeners
triggered by the LDAP Provider. They provide another extension point to LDAP integration. LDAP mappers are triggered when:
- Users log in by using LDAP.
- Users initially register.
- The Admin Console queries a user.
When you create an LDAP Federation provider, Red Hat build of Keycloak automatically provides a set of mappers
for this provider. This set is changeable by users, who can also develop mappers or update/delete existing ones.
- User Attribute Mapper
-
This mapper specifies which LDAP attribute maps to the attribute of the Red Hat build of Keycloak user. For example, you can configure the
mail
LDAP attribute to theemail
attribute in the Red Hat build of Keycloak database. For this mapper implementation, a one-to-one mapping always exists. - FullName Mapper
-
This mapper specifies the full name of the user. Red Hat build of Keycloak saves the name in an LDAP attribute (usually
cn
) and maps the name to thefirstName
andlastname
attributes in the Red Hat build of Keycloak database. Havingcn
to contain the full name of the user is common for LDAP deployments.
When you register new users in Red Hat build of Keycloak and Sync Registrations
is ON for the LDAP provider, the fullName mapper permits falling back to the username. This fallback is useful when using Microsoft Active Directory (MSAD). The common setup for MSAD is to configure the cn
LDAP attribute as fullName and, at the same time, use the cn
LDAP attribute as the RDN LDAP Attribute
in the LDAP provider configuration. With this setup, Red Hat build of Keycloak falls back to the username. For example, if you create Red Hat build of Keycloak user "john123" and leave firstName and lastName empty, then the fullname mapper saves "john123" as the value of the cn
in LDAP. When you enter "John Doe" for firstName and lastName later, the fullname mapper updates LDAP cn
to the "John Doe" value as falling back to the username is unnecessary.
- Hardcoded Attribute Mapper
-
This mapper adds a hardcoded attribute value to each Red Hat build of Keycloak user linked with LDAP. This mapper can also force values for the
enabled
oremailVerified
user properties. - Role Mapper
-
This mapper configures role mappings from LDAP into Red Hat build of Keycloak role mappings. A single role mapper can map LDAP roles (usually groups from a particular branch of the LDAP tree) into roles corresponding to a specified client’s realm roles or client roles. You can configure more Role mappers for the same LDAP provider. For example, you can specify that role mappings from groups under
ou=main,dc=example,dc=org
map to realm role mappings, and role mappings from groups underou=finance,dc=example,dc=org
map to client role mappings of clientfinance
. - Hardcoded Role Mapper
- This mapper grants a specified Red Hat build of Keycloak role to each Red Hat build of Keycloak user from the LDAP provider.
- Group Mapper
- This mapper maps LDAP groups from a branch of an LDAP tree into groups within Red Hat build of Keycloak. This mapper also propagates user-group mappings from LDAP into user-group mappings in Red Hat build of Keycloak.
- MSAD User Account Mapper
-
This mapper is specific to Microsoft Active Directory (MSAD). It can integrate the MSAD user account state into the Red Hat build of Keycloak account state, such as enabled account or expired password. This mapper uses the
userAccountControl
, andpwdLastSet
LDAP attributes, specific to MSAD and are not the LDAP standard. For example, if the value ofpwdLastSet
is0
, the Red Hat build of Keycloak user must update their password. The result is an UPDATE_PASSWORD required action added to the user. If the value ofuserAccountControl
is514
(disabled account), the Red Hat build of Keycloak user is disabled. - Certificate Mapper
-
This mapper maps X.509 certificates. Red Hat build of Keycloak uses it in conjunction with X.509 authentication and
Full certificate in PEM format
as an identity source. This mapper behaves similarly to theUser Attribute Mapper
, but Red Hat build of Keycloak can filter for an LDAP attribute storing a PEM or DER format certificate. EnableAlways Read Value From LDAP
with this mapper.
User Attribute mappers that map basic Red Hat build of Keycloak user attributes, such as username, firstname, lastname, and email, to corresponding LDAP attributes. You can extend these and provide your own additional attribute mappings. The Admin Console provides tooltips to help with configuring the corresponding mappers.
4.3.8. Password hashing
When Red Hat build of Keycloak updates a password, Red Hat build of Keycloak sends the password in plain-text format. This action is different from updating the password in the built-in Red Hat build of Keycloak database, where Red Hat build of Keycloak hashes and salts the password before sending it to the database. For LDAP, Red Hat build of Keycloak relies on the LDAP server to hash and salt the password.
By default, LDAP servers such as MSAD, RHDS, or FreeIPA hash and salt passwords. Other LDAP servers such as OpenLDAP store the passwords in plain-text unless you use the LDAPv3 Password Modify Extended Operation as described in RFC3062. Enable the LDAPv3 Password Modify Extended Operation in the LDAP configuration page. See the documentation of your LDAP server for more details. Configure ApacheDS to hash and salt passwords automatically by enabling the passwordHashing interceptor.
Always verify that user passwords are properly hashed and not stored as plaintext by inspecting a changed directory entry using ldapsearch
and base64 decode the userPassword
attribute value.
4.3.9. Configuring the connection pool
For more efficiency when managing LDAP connections and to improve performance when handling multiple connections, you can enable connection pooling. By doing that, when a connection is closed, it will be returned to the pool for future use therefore reducing the cost of creating new connections all the time.
The LDAP connection pool configuration is configured using the following system properties:
| Name | Description |
|---|---|
|
| A list of space-separated authentication types of connections that may be pooled. Valid types are "none", "simple", and "DIGEST-MD5" |
|
| The string representation of an integer that represents the number of connections per connection identity to create when initially creating a connection for the identity |
|
|
The string representation of an integer that represents the maximum number of connections per connection identity that can be maintained concurrently. Note setting this value too low may cause contention in obtaining LDAP connections. See also |
|
| The string representation of an integer that represents the preferred number of connections per connection identity that should be maintained concurrently |
|
| The string representation of an integer that represents the number of milliseconds that an idle connection may remain in the pool without being closed and removed from the pool |
|
| A list of space-separated protocol types of connections that may be pooled. Valid types are "plain" and "ssl" |
|
| A string that indicates the level of debug output to produce. Valid values are "fine" (trace connection creation and removal) and "all" (all debugging information) |
|
| The string representation of an integer that represents how long in milliseconds obtaining a connection should take. This is also applicable to wait times due to connection pool contention. Effectively defaults to 5000. |
By default, connection pooling is enabled for both plain
and ssl
protocols.
For more details, see the Java LDAP Connection Pooling Configuration documentation.
To set any of these properties, you can set the JAVA_OPTS_APPEND
environment variable:
export JAVA_OPTS_APPEND=-Dcom.sun.jndi.ldap.connect.pool.initsize=10 -Dcom.sun.jndi.ldap.connect.pool.maxsize=50
4.3.10. Troubleshooting
It is useful to increase the logging level to TRACE for the category org.keycloak.storage.ldap
. With this setting, many logging messages are sent to the server log in the TRACE
level, including the logging for all queries to the LDAP server and the parameters, which were used to send the queries. When you are creating any LDAP question on user forum or JIRA, consider attaching the server log with enabled TRACE logging. If it is too big, the good alternative is to include just the snippet from server log with the messages, which were added to the log during the operation, which causes the issues to you.
- When you create an LDAP provider, a message appears in the server log in the INFO level starting with:
Creating new LDAP Store for the LDAP storage provider: ...
It shows the configuration of your LDAP provider. Before you are asking the questions or reporting bugs, it will be nice to include this message to show your LDAP configuration. Eventually feel free to replace some config changes, which you do not want to include, with some placeholder values. One example is bindDn=some-placeholder
. For connectionUrl
, feel free to replace it as well, but it is generally useful to include at least the protocol, which was used (ldap
vs ldaps
)`. Similarly it can be useful to include the details for configuration of your LDAP mappers, which are displayed with the message like this at the DEBUG level:
Mapper for provider: XXX, Mapper name: YYY, Provider: ZZZ ...
Note those messages are displayed just with the enabled DEBUG logging.
-
For tracking the performance or connection pooling issues, consider setting the value of property
com.sun.jndi.ldap.connect.pool.debug
toall
. This change adds many additional messages to the server log with the included logging for the LDAP connection pooling. As a result, you can track the issues related to connection pooling or performance. For more details, see Configuring the connection pool.
After changing the configuration of connection pooling, you may need to restart the Red Hat build of Keycloak server to enforce re-initialization of the LDAP provider connection.
If no more messages appear for connection pooling even after server restart, it can indicate that connection pooling does not work with your LDAP server.
-
For the case of reporting LDAP issue, you may consider to attach some part of your LDAP tree with the target data, which causes issues in your environment. For example if login of some user takes lot of time, you can consider attach his LDAP entry showing count of
member
attributes of various "group" entries. In this case, it might be useful to add if those group entries are mapped to some Group LDAP mapper (or Role LDAP Mapper) in Red Hat build of Keycloak and so on.
4.4. SSSD and FreeIPA Identity Management integration
Red Hat build of Keycloak includes the System Security Services Daemon (SSSD) plugin. SSSD is part of the Fedora and Red Hat Enterprise Linux (RHEL), and it provides access to multiple identities and authentication providers. SSSD also provides benefits such as failover and offline support. For more information, see the Red Hat Enterprise Linux Identity Management documentation.
SSSD integrates with the FreeIPA identity management (IdM) server, providing authentication and access control. With this integration, Red Hat build of Keycloak can authenticate against privileged access management (PAM) services and retrieve user data from SSSD. For more information about using Red Hat Identity Management in Linux environments, see the Red Hat Enterprise Linux Identity Management documentation.
Red Hat build of Keycloak and SSSD communicate through read-only D-Bus interfaces. For this reason, the way to provision and update users is to use the FreeIPA/IdM administration interface. By default, the interface imports the username, email, first name, and last name.
Red Hat build of Keycloak registers groups and roles automatically but does not synchronize them. The groups are imported from SSSD the first time the user is accessed and then they are managed entirely inside Red Hat build of Keycloak. Any changes made by the administrator in Red Hat build of Keycloak do not synchronize with SSSD or vice-versa.
4.4.1. FreeIPA/IdM server
The FreeIPA Container image is available at Quay.io. To set up the FreeIPA server, see the FreeIPA documentation.
Procedure
Run your FreeIPA server using this command:
docker run --name freeipa-server-container -it \ -h server.freeipa.local -e PASSWORD=YOUR_PASSWORD \ -v /sys/fs/cgroup:/sys/fs/cgroup:ro \ -v /var/lib/ipa-data:/data:Z freeipa/freeipa-server
The parameter
-h
withserver.freeipa.local
represents the FreeIPA/IdM server hostname. ChangeYOUR_PASSWORD
to a password of your own.After the container starts, change the
/etc/hosts
file to include:x.x.x.x server.freeipa.local
If you do not make this change, you must set up a DNS server.
Use the following command to enroll your Linux server in the IPA domain so that the SSSD federation provider starts and runs on Red Hat build of Keycloak:
ipa-client-install --mkhomedir -p admin -w password
Run the following command on the client to verify the installation is working:
kinit admin
- Enter your password.
Add users to the IPA server using this command:
$ ipa user-add <username> --first=<first name> --last=<surname> --email=<email address> --phone=<telephoneNumber> --street=<street> --city=<city> --state=<state> --postalcode=<postal code> --password
Force set the user’s password using kinit.
kinit <username>
Enter the following to restore normal IPA operation:
kdestroy -A kinit admin
4.4.2. SSSD and D-Bus
The federation provider obtains the data from SSSD using D-BUS. It authenticates the data using PAM.
Procedure
Install the sssd-dbus RPM.
$ sudo yum install sssd-dbus
Run the following provisioning script:
$ bin/federation-sssd-setup.sh
The script can also be used as a guide to configure SSSD and PAM for Red Hat build of Keycloak. It makes the following changes to
/etc/sssd/sssd.conf
:[domain/your-hostname.local] ... ldap_user_extra_attrs = mail:mail, sn:sn, givenname:givenname, telephoneNumber:telephoneNumber ... [sssd] services = nss, sudo, pam, ssh, ifp ... [ifp] allowed_uids = root, yourOSUsername user_attributes = +mail, +telephoneNumber, +givenname, +sn
The
ifp
service is added to SSSD and configured to allow the OS user to interrogate the IPA server through this interface.The script also creates a new PAM service
/etc/pam.d/keycloak
to authenticate users via SSSD:auth required pam_sss.so account required pam_sss.so
Run
dbus-send
to ensure the setup is successful.dbus-send --print-reply --system --dest=org.freedesktop.sssd.infopipe /org/freedesktop/sssd/infopipe org.freedesktop.sssd.infopipe.GetUserAttr string:<username> array:string:mail,givenname,sn,telephoneNumber dbus-send --print-reply --system --dest=org.freedesktop.sssd.infopipe /org/freedesktop/sssd/infopipe org.freedesktop.sssd.infopipe.GetUserGroups string:<username>
If the setup is successful, each command displays the user’s attributes and groups respectively. If there is a timeout or an error, the federation provider running on Red Hat build of Keycloak cannot retrieve any data. This error usually happens because the server is not enrolled in the FreeIPA IdM server, or does not have permission to access the SSSD service.
If you do not have permission to access the SSSD service, ensure that the user running the Red Hat build of Keycloak server is in the
/etc/sssd/sssd.conf
file in the following section:[ifp] allowed_uids = root, yourOSUsername
And the
ipaapi
system user is created inside the host. This user is necessary for theifp
service. Check the user is created in the system.grep ipaapi /etc/passwd ipaapi:x:992:988:IPA Framework User:/:/sbin/nologin
4.4.3. Enabling the SSSD federation provider
Red Hat build of Keycloak uses DBus-Java project to communicate at a low level with D-Bus and JNA to authenticate via Operating System Pluggable Authentication Modules (PAM).
Although now Red Hat build of Keycloak contains all the needed libraries to run the SSSD
provider, JDK version 21 is needed. Therefore the SSSD
provider will only be displayed when the host configuration is correct and JDK 21 is used to run Red Hat build of Keycloak.
4.4.4. Configuring a federated SSSD store
After the installation, configure a federated SSSD store.
Procedure
- Click User Federation in the menu.
- If everything is setup successfully the Add Sssd providers button will be displayed in the page. Click on it.
- Assign a name to the new provider.
- Click Save.
You can now authenticate against Red Hat build of Keycloak using a FreeIPA/IdM user and credentials.
4.5. Custom providers
Red Hat build of Keycloak does have a Service Provider Interface (SPI) for User Storage Federation to develop custom providers. You can find documentation on developing customer providers in the Server Developer Guide.
