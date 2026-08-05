---
title: "Chapter 14. User Storage Federation - Red Hat Single Sign-On 7.2 Server Administration Guide"
type: reference
domain: keycloak
slug: rhsso-7-2-user-storage-federation
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.2/html/server_administration_guide/user-storage-federation
guide: server_administration_guide
version: 7.2
family: rhsso
documentKind: "Documentation"
abstract: "Many companies have existing user databases that hold information about users and their passwords or other credentials. In may cases, it is just not possible to migrate off of those existing stores to a pure Red Hat Single Sign-On deployment. Red Hat Single Sign-On can federate existing external user databases. Out of the box we have support for LDAP and Active Directory. You can also code your ow…"
---

# Chapter 14. User Storage Federation - Red Hat Single Sign-On 7.2 Server Administration Guide

Chapter 14. User Storage Federation
Many companies have existing user databases that hold information about users and their passwords or other credentials. In may cases, it is just not possible to migrate off of those existing stores to a pure Red Hat Single Sign-On deployment. Red Hat Single Sign-On can federate existing external user databases. Out of the box we have support for LDAP and Active Directory. You can also code your own extension for any custom user databases you might have using our User Storage SPI.
The way it works is that when a user logs in, Red Hat Single Sign-On will look into its own internal user store to find the user. If it can’t find it there it will iterate over every User Storage provider you have configured for the realm until it finds a match. Data from the external store is mapped into a common user model that is consumed by the Red Hat Single Sign-On runtime. This common user model can then be mapped to OIDC token claims and SAML assertion attributes.
External user databases rarely have every piece of data need to support all the features that Red Hat Single Sign-On has. In this case, the User Storage Provider can opt to store some things locally in the Red Hat Single Sign-On user store. Some providers even import the user locally and sync periodically with the external store. All this depends on the capabilities of the provider and how its configured. For example, your external user store may not support OTP. Depending on the provider, this OTP support can be handled and stored by Red Hat Single Sign-On
14.1. Adding a Provider
To add a storage provider go to the User Federation
left menu item in the Admin Console.
User Federation
On the right side, there is an Add Provider
list box. Choose the provider type you want to add and you will be brought to the configuration page of that provider.
14.2. Dealing with Provider Failures
If a User Storage Provider fails, that is, if your LDAP server is down, you may have trouble logging in and may not be able to view users in the admin console. Red Hat Single Sign-On does not catch failures when using a Storage Provider to lookup a user. It will abort the invocation. So, if you have a Storage Provider with a higher priority that fails during user lookup, the login or user query will fail entirely with an exception and abort. It will not fail over to the next configured provider.
The local Red Hat Single Sign-On user database is always searched first to resolve users before any LDAP or custom User Storage Provider. You may want to consider creating an admin account that is stored in the local Red Hat Single Sign-On user database just in case any problems come up in connecting to your LDAP and custom back ends.
Each LDAP and custom User Storage Provider has an enable
switch on its admin console page. Disabling the User Storage Provider will skip the provider when doing user queries so that you can view and login with users that might be stored in a different provider with lower priority. If your provider is using an import
strategy and you disable it, imported users are still available for lookup, but only in read only mode. You will not be able to modify these users until you re-enable the provider.
The reason why Red Hat Single Sign-On does not fail over if a Storage Provider lookup fails is that user databases often have duplicate usernames or duplicate emails between them. This can cause security issues and unforeseen problems as the user may be loaded from one external store when the admin is expecting the user to be loaded from another.
14.3. LDAP and Active Directory
Red Hat Single Sign-On comes with a built-in LDAP/AD provider. It is possible to federate multiple different LDAP servers in the same Red Hat Single Sign-On realm. You can map LDAP user attributes into the Red Hat Single Sign-On common user model. By default, it maps username, email, first name, and last name, but you are free to configure additional mappings. The LDAP provider also supports password validation via LDAP/AD protocols and different storage, edit, and synchronization modes.
To configure a federated LDAP store go to the Admin Console. Click on the User Federation
left menu option. When you get to this page there is an Add Provider
select box. You should see ldap within this list. Selecting ldap will bring you to the LDAP configuration page.
14.3.1. Storage Mode
By default, Red Hat Single Sign-On will import users from LDAP into the local Red Hat Single Sign-On user database. This copy of the user is either synchronized on demand, or through a periodic background task. The one exception to this is passwords. Passwords are not imported and password validation is delegated to the LDAP server. The benefits to this approach is that all Red Hat Single Sign-On features will work as any extra per-user data that is needed can be stored locally. This approach also reduces load on the LDAP server as uncached users are loaded from the Red Hat Single Sign-On database the 2nd time they are accessed. The only load your LDAP server will have is password validation. The downside to this approach is that when a user is first queried, this will require a Red Hat Single Sign-On database insert. The import will also have to be synchronized with your LDAP server as needed.
Alternatively, you can choose not to import users into the Red Hat Single Sign-On user database. In this case, the common user model that the Red Hat Single Sign-On runtime uses is backed only by the LDAP server. This means that if LDAP doesn’t support a piece of data that a Red Hat Single Sign-On feature needs that feature will not work. The benefit to this approach is that you do not have the overhead of importing and synchronizing a copy of the LDAP user into the Red Hat Single Sign-On user database.
This storage mode is controled by the Import Enabled
switch. Set to On
to import users.
14.3.2. Edit Mode
Users, through the User Account Service, and admins through the Admin Console have the ability to modify user metadata. Depending on your setup you may or may not have LDAP update privileges. The Edit Mode
configuration option defines the edit policy you have with your LDAP store.
- READONLY
- Username, email, first name, last name, and other mapped attributes will be unchangeable. Red Hat Single Sign-On will show an error anytime anybody tries to update these fields. Also, password updates will not be supported.
- WRITABLE
- Username, email, first name, last name, and other mapped attributes and passwords can all be updated and will be synchronized automatically with your LDAP store.
- UNSYNCED
- Any changes to username, email, first name, last name, and passwords will be stored in Red Hat Single Sign-On local storage. It is up to you to figure out how to synchronize back to LDAP. This allows Red Hat Single Sign-On deployments to support updates of user metadata on a read-only LDAP server. This option only applies when you are importing users from LDAP into the local Red Hat Single Sign-On user database.
14.3.3. Other config options
- Console Display Name
- Name used when this provider is referenced in the admin console
- Priority
- The priority of this provider when looking up users or for adding registrations.
- Sync Registrations
- Does your LDAP support adding new users? Click this switch if you want new users created by Red Hat Single Sign-On in the admin console or the registration page to be added to LDAP.
- Allow Kerberos authentication
- Enable Kerberos/SPNEGO authentication in realm with users data provisioned from LDAP. More info in Kerberos section.
- Other options
- The rest of the configuration options should be self explanatory. You can mouseover the tooltips in Admin Console to see some more details about them.
14.3.4. Connect to LDAP over SSL
When you configure a secured connection URL to your LDAP store(for example ldaps://myhost.com:636
), Red Hat Single Sign-On will use SSL for the communication with LDAP server. The important thing is to properly configure a truststore on the Red Hat Single Sign-On server side, otherwise Red Hat Single Sign-On can’t trust the SSL connection to LDAP.
The global truststore for the Red Hat Single Sign-On can be configured with the Truststore SPI. Please check out the Server Installation and Configuration Guide for more detail. If you don’t configure the truststore SPI, the truststore will fallback to the default mechanism provided by Java (either the file provided by system property javax.net.ssl.trustStore
or the cacerts file from the JDK if the system property is not set).
There is a configuration property Use Truststore SPI
in the LDAP federation provider configuration, where you can choose whether the Truststore SPI is used. By default, the value is Only for ldaps
, which is fine for most deployments. The Truststore SPI will only be used if the connection to LDAP starts with ldaps
.
14.3.5. Sync of LDAP users to Red Hat Single Sign-On
If you have import enabled, the LDAP Provider will automatically take care of synchronization (import) of needed LDAP users into the Red Hat Single Sign-On local database. As users log in, the LDAP provider will import the LDAP user into the Red Hat Single Sign-On database and then authenticate against the LDAP password. This is the only time users will be imported. If you go to the Users
left menu item in the Admin Console and click the View all users
button, you will only see those LDAP users that have been authenticated at least once by Red Hat Single Sign-On. It is implemented this way so that admins don’t accidentally try to import a huge LDAP DB of users.
If you want to sync all LDAP users into the Red Hat Single Sign-On database, you may configure and enable the Sync Settings
of the LDAP provider you configured. There are 2 types of synchronization:
- Periodic Full sync
-
This will synchronize all LDAP users into Red Hat Single Sign-On DB. Those LDAP users, which already exist in Red Hat Single Sign-On and were changed in LDAP directly will be updated in Red Hat Single Sign-On DB (For example if user
Mary Kelly
was changed in LDAP toMary Smith
). - Periodic Changed users sync
- When syncing occurs, only those users that were created or updated after the last sync will be updated and/or imported.
The best way to handle syncing is to click the Synchronize all users
button when you first create the LDAP provider, then set up a periodic sync of changed users. The configuration page for your LDAP Provider has several options to support you.
14.3.6. LDAP Mappers
LDAP mappers are listeners
, which are triggered by the LDAP Provider at various points, provide another extension point to LDAP integration. They are triggered when a user logs in via LDAP and needs to be imported, during Red Hat Single Sign-On initiated registration, or when a user is queried from the Admin Console. When you create an LDAP Federation provider, Red Hat Single Sign-On will automatically provide set of built-in mappers
for this provider. You are free to change this set and create a new mapper or update/delete existing ones.
- User Attribute Mapper
-
This allows you to specify which LDAP attribute is mapped to which attribute of Red Hat Single Sign-On user. So, for example, you can configure that LDAP attribute
mail
to the attributeemail
in the Red Hat Single Sign-On database. For this mapper implementation, there is always a one-to-one mapping (one LDAP attribute is mapped to one Red Hat Single Sign-On attribute) - FullName Mapper
-
This allows you to specify that the full name of the user, which is saved in some LDAP attribute (usually
cn
) will be mapped tofirstName
andlastname
attributes in the Red Hat Single Sign-On database. Havingcn
to contain full name of user is a common case for some LDAP deployments. - Role Mapper
-
This allows you to configure role mappings from LDAP into Red Hat Single Sign-On role mappings. One Role mapper can be used to map LDAP roles (usually groups from a particular branch of LDAP tree) into roles corresponding to either realm roles or client roles of a specified client. It’s not a problem to configure more Role mappers for the same LDAP provider. So for example you can specify that role mappings from groups under
ou=main,dc=example,dc=org
will be mapped to realm role mappings and role mappings from groups underou=finance,dc=example,dc=org
will be mapped to client role mappings of clientfinance
. - Hardcoded Role Mapper
- This mapper will grant a specified Red Hat Single Sign-On role to each Red Hat Single Sign-On user linked with LDAP.
- Group Mapper
- This allows you to configure group mappings from LDAP into Red Hat Single Sign-On group mappings. Group mapper can be used to map LDAP groups from a particular branch of an LDAP tree into groups in Red Hat Single Sign-On. It will also propagate user-group mappings from LDAP into user-group mappings in Red Hat Single Sign-On.
- MSAD User Account Mapper
-
This mapper is specific to Microsoft Active Directory (MSAD). It’s able to tightly integrate the MSAD user account state into the Red Hat Single Sign-On account state (account enabled, password is expired etc). It’s using the
userAccountControl
andpwdLastSet
LDAP attributes. (both are specific to MSAD and are not LDAP standard). For example ifpwdLastSet
is0
, the Red Hat Single Sign-On user is required to update their password and there will be an UPDATE_PASSWORD required action added to the user. IfuserAccountControl
is514
(disabled account) the Red Hat Single Sign-On user is disabled as well.
By default, there are User Attribute mappers that map basic Red Hat Single Sign-On user attributes like username, firstname, lastname, and email to corresponding LDAP attributes. You are free to extend these and provide additional attribute mappings. Admin console provides tooltips, which should help with configuring the corresponding mappers.
14.4. SSSD and FreeIPA Identity Management Integration
Red Hat Single Sign-On also comes with a built-in SSSD (System Security Services Daemon) plugin. SSSD is part of the latest Fedora or Red Hat Enterprise Linux and provides access to multiple identity and authentication providers. It provides benefits such as failover and offline support. To see configuration options and for more information see the Red Hat Enterprise Linux Identity Management documentation.
SSSD also integrates with the FreeIPA identity management (IdM) server, providing authentication and access control. For Red Hat Single Sign-On, we benefit from this integration authenticating against PAM services and retrieving user data from SSSD. For more information about using Red Hat Identity Management in Linux environments, see the Red Hat Enterprise Linux Identity Management documentation.
Most of the communication between Red Hat Single Sign-On and SSSD occurs through read-only D-Bus interfaces. For this reason, the only way to provision and update users is to use the FreeIPA/IdM administration interface. By default, like the LDAP federation provider, it is set up only to import username, email, first name, and last name.
Groups and roles are automatically registered, but not synchronized, so any changes made by the Red Hat Single Sign-On administrator directly in Red Hat Single Sign-On is not synchronized with SSSD.
Information on how to configure the FreeIPA/IdM server follows.
14.4.1. FreeIPA/IdM Server
As a matter of simplicity, a FreeIPA Docker image already available is used. To set up a server, see the FreeIPA documentation.
Running a FreeIPA server with Docker requires this command:
docker run --name freeipa-server-container -it \
-h server.freeipa.local -e PASSWORD=YOUR_PASSWORD \
-v /sys/fs/cgroup:/sys/fs/cgroup:ro \
-v /var/lib/ipa-data:/data:Z freeipa/freeipa-server
The parameter -h
with server.freeipa.local
represents the FreeIPA/IdM server hostname. Be sure to change YOUR_PASSWORD
to a password of your choosing.
After the container starts, change /etc/hosts
to:
x.x.x.x server.freeipa.local
If you do not make this change, you must set up a DNS server.
So that the SSSD federation provider is started and running on Red Hat Single Sign-On you must enroll your Linux machine in the IPA domain:
ipa-client-install --mkhomedir -p admin -w password
To ensure that everything is working as expected, on the client machine, run:
kinit admin
You should be prompted for the password. After that, you can add users to the IPA server using this command:
$ ipa user-add john --first=John --last=Smith --email=john@smith.com --phone=042424242 --street="Testing street" \ --city="Testing city" --state="Testing State" --postalcode=0000000000
14.4.2. SSSD and D-Bus
As mentioned previously, the federation provider obtains the data from SSSD using D-BUS and authentication occurs using PAM.
First, you have to install the sssd-dbus RPM, which allows information from SSSD to be transmitted over the system bus.
$ sudo yum install sssd-dbus
You must run this provisioning script:
$ .../bin/federation-sssd-setup.sh
This script makes the necessary changes to /etc/sssd/sssd.conf
:
[domain/your-hostname.local]
...
ldap_user_extra_attrs = mail:mail, sn:sn, givenname:givenname, telephoneNumber:telephoneNumber
...
[sssd]
services = nss, sudo, pam, ssh, ifp
...
[ifp]
allowed_uids = root, yourOSUsername
user_attributes = +mail, +telephoneNumber, +givenname, +sn
Also, a keycloak
file is included under /etc/pam.d/
:
auth required pam_sss.so
account required pam_sss.so
Ensure everything is working as expected by running dbus-send
:
sudo dbus-send --print-reply --system --dest=org.freedesktop.sssd.infopipe /org/freedesktop/sssd/infopipe org.freedesktop.sssd.infopipe.GetUserGroups string:john
You should be able to see the user’s group. If this command returns a timeout or an error, it means that the federation provider will also not be able to retrieve anything on Red Hat Single Sign-On.
Most of the time this occurs because the machine was not enrolled in the FreeIPA IdM server or you do not have permission to access the SSSD service.
If you do not have permission, ensure that the user running Red Hat Single Sign-On is included in the /etc/sssd/sssd.conf
file in the following section:
[ifp]
allowed_uids = root, your_username
14.4.3. Enabling the SSSD Federation Provider
Red Hat Single Sign-On uses DBus-Java to communicate at a low level with D-Bus, which depends on the Unix Sockets Library.
Before enabling the SSSD Federation provider, you must install the RPM for this library:
$ sudo yum install rh-sso7-libunix-dbus-java
For authentication with PAM Red Hat Single Sign-On uses JNA. Be sure you have this package installed:
$ sudo yum install jna
Use sssctl user-checks
command to validate your setup:
$ sudo sssctl user-checks admin -s keycloak
14.5. Configuring a Federated SSSD Store
After installation, you need to configure a federated SSSD store.
To configure a federated SSSD store, complete the following steps:
- Navigate to the Administration Console.
- From the left menu, select User Federation.
- From the Add Provider dropdown list, select sssd. The sssd configuration page opens.
- Click Save.
Now you can authenticate against Red Hat Single Sign-On using FreeIPA/IdM credentials.
14.6. Custom Providers
Red Hat Single Sign-On does have an SPI for User Storage Federation that you can use to write your own custom providers. You can find documentation for this in our Server Developer Guide.
