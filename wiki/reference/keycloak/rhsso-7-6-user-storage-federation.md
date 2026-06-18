---
title: "Chapter 4. Using external storage - Red Hat Single Sign-On 7.6 Server Administration Guide"
type: reference
domain: keycloak
slug: rhsso-7-6-user-storage-federation
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html/server_administration_guide/user-storage-federation
guide: server_administration_guide
version: 7.6
family: rhsso
documentKind: "Documentation"
---

# Chapter 4. Using external storage - Red Hat Single Sign-On 7.6 Server Administration Guide

Chapter 4. Using external storage
Organizations can have databases containing information, passwords, and other credentials. Typically, you cannot migrate existing data storage to a Red Hat Single Sign-On deployment so Red Hat Single Sign-On can federate existing external user databases. Red Hat Single Sign-On supports LDAP and Active Directory, but you can also code extensions for any custom user database by using the Red Hat Single Sign-On User Storage SPI.
When a user attempts to log in, Red Hat Single Sign-On examines that user’s storage to find that user. If Red Hat Single Sign-On does not find the user, Red Hat Single Sign-On iterates over each User Storage provider for the realm until it finds a match. Data from the external data storage then maps into a standard user model the Red Hat Single Sign-On runtime consumes. This user model then maps to OIDC token claims and SAML assertion attributes.
External user databases rarely have the data necessary to support all the features of Red Hat Single Sign-On, so the User Storage Provider can opt to store items locally in Red Hat Single Sign-On user data storage. Providers can import users locally and sync periodically with external data storage. This approach depends on the capabilities of the provider and the configuration of the provider. For example, your external user data storage may not support OTP. The OTP can be handled and stored by Red Hat Single Sign-On, depending on the provider.
4.1. Adding a provider
To add a storage provider, perform the following procedure:
Procedure
Click User Federation in the menu.
User federation
- Select the provider type from the Add Provider list. Red Hat Single Sign-On brings you to that provider’s configuration page.
4.2. Dealing with provider failures
If a User Storage Provider fails, you may not be able to log in and view users in the Admin Console. Red Hat Single Sign-On does not detect failures when using a Storage Provider to look up a user, so it cancels the invocation. If you have a Storage Provider with a high priority that fails during user lookup, the login or user query fails with an exception and will not fail over to the next configured provider.
Red Hat Single Sign-On searches the local Red Hat Single Sign-On user database first to resolve users before any LDAP or custom User Storage Provider. Consider creating an administrator account stored in the local Red Hat Single Sign-On user database in case of problems connecting to your LDAP and back ends.
Each LDAP and custom User Storage Provider has an enable
toggle on its Admin Console page. Disabling the User Storage Provider skips the provider when performing queries, so you can view and log in with user accounts in a different provider with lower priority. If your provider uses an import
strategy and is disabled, imported users are still available for lookup in read-only mode.
When a Storage Provider lookup fails, Red Hat Single Sign-On does not fail over because user databases often have duplicate usernames or duplicate emails between them. Duplicate usernames and emails can cause problems because the user loads from one external data store when the admin expects them to load from another data store.
4.3. Lightweight Directory Access Protocol (LDAP) and Active Directory
Red Hat Single Sign-On includes an LDAP/AD provider. You can federate multiple different LDAP servers in one Red Hat Single Sign-On realm and map LDAP user attributes into the Red Hat Single Sign-On common user model.
By default, Red Hat Single Sign-On maps the username, email, first name, and last name of the user account, but you can also configure additional mappings. Red Hat Single Sign-On’s LDAP/AD provider supports password validation using LDAP/AD protocols and storage, edit, and synchronization modes.
4.3.1. Configuring federated LDAP storage
Procedure
Click User Federation in the menu.
User federation
- Select ldap from the Add Provider list. Red Hat Single Sign-On brings you to the LDAP configuration page.
4.3.2. Storage mode
Red Hat Single Sign-On imports users from LDAP into the local Red Hat Single Sign-On user database. This copy of the user database synchronizes on-demand or through a periodic background task. An exception exists for synchronizing passwords. Red Hat Single Sign-On never imports passwords. Password validation always occurs on the LDAP server.
The advantage of synchronization is that all Red Hat Single Sign-On features work efficiently because any required extra per-user data is stored locally. The disadvantage is that each time Red Hat Single Sign-On queries a specific user for the first time, Red Hat Single Sign-On performs a corresponding database insert.
You can synchronize the import with your LDAP server. Import synchronization is unnecessary when LDAP mappers always read particular attributes from the LDAP rather than the database.
You can use LDAP with Red Hat Single Sign-On without importing users into the Red Hat Single Sign-On user database. The LDAP server backs up the common user model that the Red Hat Single Sign-On runtime uses. If LDAP does not support data that a Red Hat Single Sign-On feature requires, that feature will not work. The advantage of this approach is that you do not have the resource usage of importing and synchronizing copies of LDAP users into the Red Hat Single Sign-On user database.
The Import Users switch on the LDAP configuration page controls this storage mode. To import users, toggle this switch to ON.
If you disable Import Users, you cannot save user profile attributes into the Red Hat Single Sign-On database. Also, you cannot save metadata except for user profile metadata mapped to the LDAP. This metadata can include role mappings, group mappings, and other metadata based on the LDAP mappers' configuration.
When you attempt to change the non-LDAP mapped user data, the user update is not possible. For example, you cannot disable the LDAP mapped user unless the user’s enabled
flag maps to an LDAP attribute.
4.3.3. Edit mode
Users and admins can modify user metadata, users through the Account Console, and administrators through the Admin Console. The Edit Mode
configuration on the LDAP configuration page defines the user’s LDAP update privileges.
- READONLY
- You cannot change the username, email, first name, last name, and other mapped attributes. Red Hat Single Sign-On shows an error anytime a user attempts to update these fields. Password updates are not supported.
- WRITABLE
- You can change the username, email, first name, last name, and other mapped attributes and passwords and synchronize them automatically with the LDAP store.
- UNSYNCED
- Red Hat Single Sign-On stores changes to the username, email, first name, last name, and passwords in Red Hat Single Sign-On local storage, so the administrator must synchronize this data back to LDAP. In this mode, Red Hat Single Sign-On deployments can update user metadata on read-only LDAP servers. This option also applies when importing users from LDAP into the local Red Hat Single Sign-On user database.
When Red Hat Single Sign-On creates the LDAP provider, Red Hat Single Sign-On also creates a set of initial LDAP mappers. Red Hat Single Sign-On configures these mappers based on a combination of the Vendor, Edit Mode, and Import Users switches. For example, when edit mode is UNSYNCED, Red Hat Single Sign-On configures the mappers to read a particular user attribute from the database and not from the LDAP server. However, if you later change the edit mode, the mapper’s configuration does not change because it is impossible to detect if the configuration changes changed in UNSYNCED mode. Decide the Edit Mode when creating the LDAP provider. This note applies to Import Users switch also.
4.3.4. Other configuration options
- Console Display Name
- The name of the provider to display in the admin console.
- Priority
- The priority of the provider when looking up users or adding a user.
- Sync Registrations
- Toggle this switch to ON if you want new users created by Red Hat Single Sign-On added to LDAP.
- Allow Kerberos authentication
- Enable Kerberos/SPNEGO authentication in the realm with user data provisioned from LDAP. For more information, see the Kerberos section.
- Other options
- Hover the mouse pointer over the tooltips in the Admin Console to see more details about these options.
4.3.5. Connecting to LDAP over SSL
When you configure a secure connection URL to your LDAP store (for example,ldaps://myhost.com:636
), Red Hat Single Sign-On uses SSL to communicate with the LDAP server. Configure a truststore on the Red Hat Single Sign-On server side so that Red Hat Single Sign-On can trust the SSL connection to LDAP.
Configure the global truststore for Red Hat Single Sign-On with the Truststore SPI. For more information about configuring the global truststore, see the Server Installation and Configuration Guide. If you do not configure the Truststore SPI, the truststore falls back to the default mechanism provided by Java, which can be the file supplied by the javax.net.ssl.trustStore
system property or the cacerts file from the JDK if the system property is unset.
The Use Truststore SPI
configuration property, in the LDAP federation provider configuration, controls the truststore SPI. By default, Red Hat Single Sign-On sets the property to Only for ldaps
, which is adequate for most deployments. Red Hat Single Sign-On uses the Truststore SPI if the connection URL to LDAP starts with ldaps
only.
4.3.6. Synchronizing LDAP users to Red Hat Single Sign-On
If you set the Import Users option, the LDAP Provider handles importing LDAP users into the Red Hat Single Sign-On local database. The first time a user logs in, the LDAP provider imports the LDAP user into the Red Hat Single Sign-On database and validates the LDAP password. This first time a user logs in is the only time Red Hat Single Sign-On imports the user. If you click the Users menu in the Admin Console and click the View all users button, you only see the LDAP users authenticated at least once by Red Hat Single Sign-On. Red Hat Single Sign-On imports users this way, so this operation does not trigger an import of the entire LDAP user database.
If you want to sync all LDAP users into the Red Hat Single Sign-On database, configure and enable the Sync Settings on the LDAP provider configuration page.
Two types of synchronization exist:
- Periodic Full sync
- This type synchronizes all LDAP users into the Red Hat Single Sign-On database. The LDAP users already in Red Hat Single Sign-On, but different in LDAP, directly update in the Red Hat Single Sign-On database.
- Periodic Changed users sync
- When synchronizing, Red Hat Single Sign-On creates or updates users created or updated after the last sync only.
The best way to synchronize is to click Synchronize all users when you first create the LDAP provider, then set up periodic synchronization of changed users.
4.3.7. LDAP mappers
LDAP mappers are listeners
triggered by the LDAP Provider. They provide another extension point to LDAP integration. LDAP mappers are triggered when:
- Users log in by using LDAP.
- Users initially register.
- The Admin Console queries a user.
When you create an LDAP Federation provider, Red Hat Single Sign-On automatically provides a set of mappers
for this provider. This set is changeable by users, who can also develop mappers or update/delete existing ones.
- User Attribute Mapper
-
This mapper specifies which LDAP attribute maps to the attribute of the Red Hat Single Sign-On user. For example, you can configure the
mail
LDAP attribute to theemail
attribute in the Red Hat Single Sign-On database. For this mapper implementation, a one-to-one mapping always exists. - FullName Mapper
-
This mapper specifies the full name of the user. Red Hat Single Sign-On saves the name in an LDAP attribute (usually
cn
) and maps the name to thefirstName
andlastname
attributes in the Red Hat Single Sign-On database. Havingcn
to contain the full name of the user is common for LDAP deployments.
When you register new users in Red Hat Single Sign-On and Sync Registrations
is ON for the LDAP provider, the fullName mapper permits falling back to the username. This fallback is useful when using Microsoft Active Directory (MSAD). The common setup for MSAD is to configure the cn
LDAP attribute as fullName and, at the same time, use the cn
LDAP attribute as the RDN LDAP Attribute
in the LDAP provider configuration. With this setup, Red Hat Single Sign-On falls back to the username. For example, if you create Red Hat Single Sign-On user "john123" and leave firstName and lastName empty, then the fullname mapper saves "john123" as the value of the cn
in LDAP. When you enter "John Doe" for firstName and lastName later, the fullname mapper updates LDAP cn
to the "John Doe" value as falling back to the username is unnecessary.
- Hardcoded Attribute Mapper
-
This mapper adds a hardcoded attribute value to each Red Hat Single Sign-On user linked with LDAP. This mapper can also force values for the
enabled
oremailVerified
user properties. - Role Mapper
-
This mapper configures role mappings from LDAP into Red Hat Single Sign-On role mappings. A single role mapper can map LDAP roles (usually groups from a particular branch of the LDAP tree) into roles corresponding to a specified client’s realm roles or client roles. You can configure more Role mappers for the same LDAP provider. For example, you can specify that role mappings from groups under
ou=main,dc=example,dc=org
map to realm role mappings, and role mappings from groups underou=finance,dc=example,dc=org
map to client role mappings of clientfinance
. - Hardcoded Role Mapper
- This mapper grants a specified Red Hat Single Sign-On role to each Red Hat Single Sign-On user from the LDAP provider.
- Group Mapper
- This mapper maps LDAP groups from a branch of an LDAP tree into groups within Red Hat Single Sign-On. This mapper also propagates user-group mappings from LDAP into user-group mappings in Red Hat Single Sign-On.
- MSAD User Account Mapper
-
This mapper is specific to Microsoft Active Directory (MSAD). It can integrate the MSAD user account state into the Red Hat Single Sign-On account state, such as enabled account or expired password. This mapper uses the
userAccountControl
, andpwdLastSet
LDAP attributes, specific to MSAD and are not the LDAP standard. For example, if the value ofpwdLastSet
is0
, the Red Hat Single Sign-On user must update their password. The result is an UPDATE_PASSWORD required action added to the user. If the value ofuserAccountControl
is514
(disabled account), the Red Hat Single Sign-On user is disabled. - Certificate Mapper
-
This mapper maps X.509 certificates. Red Hat Single Sign-On uses it in conjunction with X.509 authentication and
Full certificate in PEM format
as an identity source. This mapper behaves similarly to theUser Attribute Mapper
, but Red Hat Single Sign-On can filter for an LDAP attribute storing a PEM or DER format certificate. EnableAlways Read Value From LDAP
with this mapper.
User Attribute mappers that map basic Red Hat Single Sign-On user attributes, such as username, firstname, lastname, and email, to corresponding LDAP attributes. You can extend these and provide your own additional attribute mappings. The Admin Console provides tooltips to help with configuring the corresponding mappers.
4.3.8. Password hashing
When Red Hat Single Sign-On updates a password, Red Hat Single Sign-On sends the password in plain-text format. This action is different from updating the password in the built-in Red Hat Single Sign-On database, where Red Hat Single Sign-On hashes and salts the password before sending it to the database. For LDAP, Red Hat Single Sign-On relies on the LDAP server to hash and salt the password.
By default, LDAP servers such as MSAD, RHDS, or FreeIPA hash and salt passwords. Other LDAP servers such as OpenLDAP or ApacheDS store the passwords in plain-text unless you use the LDAPv3 Password Modify Extended Operation as described in RFC3062. Enable the LDAPv3 Password Modify Extended Operation in the LDAP configuration page. See the documentation of your LDAP server for more details.
Always verify that user passwords are properly hashed and not stored as plaintext by inspecting a changed directory entry using ldapsearch
and base64 decode the userPassword
attribute value.
4.3.9. Troubleshooting
It is useful to increase the logging level to TRACE for the category org.keycloak.storage.ldap
. With this setting, many logging messages are sent to the server log in the TRACE
level, including the logging for all queries to the LDAP server and the parameters, which were used to send the queries. When you are creating any LDAP question on user forum or JIRA, consider attaching the server log with enabled TRACE logging. If it is too big, the good alternative is to include just the snippet from server log with the messages, which were added to the log during the operation, which causes the issues to you.
When you create LDAP provider, message appear in the server log in the INFO level starting with:
When you create LDAP provider, message appear in the server log in the INFO level starting with:
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
Connection Pool Debug Level
of
For tracking the performance or connection pooling issues, consider setting the value of property Connection Pool Debug Level
of the LDAP provider to value all
. This will add lots of additional messages to server log with the included logging for the LDAP connection pooling. This can be used to track the issues related to connection pooling or performance.
After changing the configuration of connection pooling, you may need to restart the Keycloak server to enforce re-initialization of the LDAP provider connection.
If no more messages appear for connection pooling even after server restart, it can indicate that connection pooling does not work with your LDAP server.
-
For the case of reporting LDAP issue, you may consider to attach some part of your LDAP tree with the target data, which causes issues in your environment. For example if login of some user takes lot of time, you can consider attach his LDAP entry showing count of
member
attributes of various "group" entries. In this case, it might be useful to add if those group entries are mapped to some Group LDAP mapper (or Role LDAP Mapper) in Red Hat Single Sign-On etc.
For the case of reporting LDAP issue, you may consider to attach some part of your LDAP tree with the target data, which causes issues in your environment. For example if login of some user takes lot of time, you can consider attach his LDAP entry showing count of member
attributes of various "group" entries. In this case, it might be useful to add if those group entries are mapped to some Group LDAP mapper (or Role LDAP Mapper) in Red Hat Single Sign-On and so on.
4.4. SSSD and FreeIPA Identity Management integration
Red Hat Single Sign-On includes the System Security Services Daemon (SSSD) plugin. SSSD is part of the Fedora and Red Hat Enterprise Linux (RHEL), and it provides access to multiple identities and authentication providers. SSSD also provides benefits such as failover and offline support. For more information, see the Red Hat Enterprise Linux Identity Management documentation.
SSSD integrates with the FreeIPA identity management (IdM) server, providing authentication and access control. With this integration, Red Hat Single Sign-On can authenticate against privileged access management (PAM) services and retrieve user data from SSSD. For more information about using Red Hat Identity Management in Linux environments, see the Red Hat Enterprise Linux Identity Management documentation.
Red Hat Single Sign-On and SSSD communicate through read-only D-Bus interfaces. For this reason, the way to provision and update users is to use the FreeIPA/IdM administration interface. By default, the interface imports the username, email, first name, and last name.
Red Hat Single Sign-On registers groups and roles automatically but does not synchronize them. Any changes made by the Red Hat Single Sign-On administrator in Red Hat Single Sign-On do not synchronize with SSSD.
4.4.1. FreeIPA/IdM server
The FreeIPA Docker image is available in Docker Hub. To set up the FreeIPA server, see the FreeIPA documentation.
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
Use the following command to enroll your Linux server in the IPA domain so that the SSSD federation provider starts and runs on Red Hat Single Sign-On:
ipa-client-install --mkhomedir -p admin -w password
Run the following command on the client to verify the installation is working:
kinit admin
- Enter your password.
Add users to the IPA server using this command:
$ ipa user-add <username> --first=<first name> --last=<surname> --email=<email address> --phone=<telephoneNumber> --street=<street> \ --city=<city> --state=<state> --postalcode=<postal code> --password
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
This script makes the following changes to
/etc/sssd/sssd.conf
:[domain/your-hostname.local] ... ldap_user_extra_attrs = mail:mail, sn:sn, givenname:givenname, telephoneNumber:telephoneNumber ... [sssd] services = nss, sudo, pam, ssh, ifp ... [ifp] allowed_uids = root, yourOSUsername user_attributes = +mail, +telephoneNumber, +givenname, +sn
Run
dbus-send
to ensure the setup is successful.sudo dbus-send --print-reply --system --dest=org.freedesktop.sssd.infopipe /org/freedesktop/sssd/infopipe org.freedesktop.sssd.infopipe.GetUserGroups string:john
If the setup is successful, you see the user’s group. If this command returns a timeout or an error, the federation provider running on Red Hat Single Sign-On cannot retrieve any data. This error usually happens because the server is not enrolled in the FreeIPA IdM server, or does not have permission to access the SSSD service.
If you do not have permission to access the SSSD service, ensure that the user running the Red Hat Single Sign-On server is in the
/etc/sssd/sssd.conf
file in the following section:[ifp] allowed_uids = root, your_username
4.4.3. Enabling the SSSD federation provider
Red Hat Single Sign-On uses DBus-Java to communicate at a low level with D-Bus. D-Bus depends on the Unix Sockets Library.
Before enabling the SSSD Federation provider, install the RPM for this library:
$ sudo yum install rh-sso7-libunix-dbus-java
Red Hat Single Sign-On uses JNA to authenticate with PAM. Ensure you have the JAN package installed.
$ sudo yum install jna
Use the sssctl user-checks
command to validate your setup:
$ sudo sssctl user-checks admin -s keycloak
4.5. Configuring a federated SSSD store
After the installation, configure a federated SSSD store.
Procedure
- Click User Federation in the menu.
- From the Add Provider list select sssd. Red Hat Single Sign-On brings you to the sssd configuration page.
- Click Save.
You can now authenticate against Red Hat Single Sign-On using FreeIPA/IdM credentials.
4.6. Custom providers
Red Hat Single Sign-On does have a Service Provider Interface (SPI) for User Storage Federation to develop custom providers. You can find documentation on developing customer providers in the Server Developer Guide.
