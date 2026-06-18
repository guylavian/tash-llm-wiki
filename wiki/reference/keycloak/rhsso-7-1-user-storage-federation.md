---
title: "Chapter 14. User Storage Federation - Red Hat Single Sign-On 7.1 Server Administration Guide"
type: reference
domain: keycloak
slug: rhsso-7-1-user-storage-federation
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.1/html/server_administration_guide/user-storage-federation
guide: server_administration_guide
version: 7.1
family: rhsso
documentKind: "Documentation"
abstract: "Red Hat Single Sign-On can federate external user databases. Out of the box we have support for LDAP and Active Directory. Before you dive into this, you should understand how Red Hat Single Sign-On does federation. Red Hat Single Sign-On performs federation a bit differently than other products/projects. The vision of Red Hat Single Sign-On is that it is an out of the box solution that should pro…"
---

# Chapter 14. User Storage Federation - Red Hat Single Sign-On 7.1 Server Administration Guide

Chapter 14. User Storage Federation
Red Hat Single Sign-On can federate external user databases. Out of the box we have support for LDAP and Active Directory. Before you dive into this, you should understand how Red Hat Single Sign-On does federation.
Red Hat Single Sign-On performs federation a bit differently than other products/projects. The vision of Red Hat Single Sign-On is that it is an out of the box solution that should provide a core set of features regardless of the backend user storage you want to use. Because of this requirement/vision, Red Hat Single Sign-On has a set data model that all of its services use. Most of the time when you want to federate an external user store, much of the metadata that would be needed to provide this complete feature set does not exist in that external store. For example your LDAP server may only provide password validation, but not support TOTP or user role mappings. The Red Hat Single Sign-On User Federation SPI was written to support these completely variable configurations.
The way user federation works is that Red Hat Single Sign-On will import your federated users on demand to its local storage. How much metadata is imported depends on the underlying federation plugin and how that plugin is configured. Some federation plugins may only import the username into Red Hat Single Sign-On storage. Others might import everything from name, address, and phone number, to user role mappings. Some plugins might want to import credentials directly into Red Hat Single Sign-On storage and let Red Hat Single Sign-On handle credential validation. Others might want to handle credential validation themselves. The goal of the User Storage Federation SPI is to support all of these scenarios.
14.1. Adding a Provider
To add a storage provider go to the User Federation
left menu item in the Admin Console.
User Federation
On the right side, there is an Add Provider
list box. Choose the provider you want to add and you will be brought to the configuration page of that provider.
14.2. LDAP and Active Directory
Red Hat Single Sign-On comes with a built-in LDAP/AD provider. It is possible to federate multiple different LDAP servers in the same Red Hat Single Sign-On realm. You can map LDAP user attributes into the Red Hat Single Sign-On common user model. By default, it maps username, email, first name, and last name, but you are free to configure additional mappings. The LDAP provider also supports password validation via LDAP/AD protocols and different storage, edit, and synchronization modes.
To configure a federated LDAP store go to the Admin Console. Click on the User Federation
left menu option. When you get to this page there is an Add Provider
select box. You should see ldap within this list. Selecting ldap will bring you to the ldap configuration page.
14.2.1. Edit Mode
Users, through the User Account Service, and admins through the Admin Console have the ability to modify user metadata. Depending on your setup you may or may not have LDAP update privileges. The Edit Mode
configuration option defines the edit policy you have with your LDAP store.
- READONLY
- Username, email, first name, last name, and other mapped attributes will be unchangeable. Red Hat Single Sign-On will show an error anytime anybody tries to update these fields. Also, password updates will not be supported.
- WRITABLE
- Username, email, first name, last name, and other mapped attributes and passwords can all be updated and will be synchronized automatically with your LDAP store.
- UNSYNCED
- Any changes to username, email, first name, last name, and passwords will be stored in Red Hat Single Sign-On local storage. It is up to you to figure out how to synchronize back to LDAP. This allows Red Hat Single Sign-On deployments to support updates of user metadata on a read-only LDAP server.
14.2.2. Other config options
- Console Display Name
- Name used when this provider is referenced in the admin console
- Priority
- The priority of this provider when looking up users or for adding registrations.
- Sync Registrations
- If a new user is added through a registration page or admin console, should the user be eligible to be synchronized to this provider?
- Allow Kerberos authentication
- Enable Kerberos/SPNEGO authentication in realm with users data provisioned from LDAP. More info in Kerberos section.
- Other options
- The rest of the configuration options should be self explanatory. You can mouseover the tooltips in Admin Console to see some more details about them.
14.2.3. Connect to LDAP over SSL
When you configure a secured connection URL to your LDAP store(for example ldaps://myhost.com:636
), Red Hat Single Sign-On will use SSL for the communication with LDAP server. The important thing is to properly configure a truststore on the Red Hat Single Sign-On server side, otherwise Red Hat Single Sign-On can’t trust the SSL connection to LDAP.
The global truststore for the Red Hat Single Sign-On can be configured with the Truststore SPI. Please check out the Server Installation and Configuration Guide for more detail. If you don’t configure the truststore SPI, the truststore will fallback to the default mechanism provided by Java (either the file provided by system property javax.net.ssl.trustStore
or the cacerts file from the JDK if the system property is not set).
There is a configuration property Use Truststore SPI
in the LDAP federation provider configuration, where you can choose whether the Truststore SPI is used. By default, the value is Only for ldaps
, which is fine for most deployments. The Truststore SPI will only be used if the connection to LDAP starts with ldaps
.
14.2.4. Sync of LDAP users to Red Hat Single Sign-On
LDAP Federation Provider will automatically take care of synchronization (import) of needed LDAP users into the Red Hat Single Sign-On local database. As users log in, the LDAP Federation provider will import the LDAP user into the Red Hat Single Sign-On database and then authenticate against the LDAP password. This is the only time users will be imported. If you go to the Users
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
14.2.5. LDAP/Federation mappers
LDAP mappers are listeners
, which are triggered by the LDAP Federation provider at various points, provide another extension point to LDAP integration. They are triggered when a user logs in via LDAP and needs to be imported, during Red Hat Single Sign-On initiated registration, or when a user is queried from the Admin Console. When you create an LDAP Federation provider, Red Hat Single Sign-On will automatically provide set of built-in mappers
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
By default, there is set of User Attribute mappers that map basic Red Hat Single Sign-On user attributes like username, first name, lastname, and email to corresponding LDAP attributes. You are free to extend these and provide additional attribute mappings. Admin console provides tooltips, which should help with configuring the corresponding mappers.
14.3. SSSD and FreeIPA Identity Management Integration
Red Hat Single Sign-On also comes with a built-in SSSD (System Security Services Daemon) plugin. SSSD is part of the latest Fedora or Red Hat Enterprise Linux and provides access to multiple identity and authentication providers. It provides benefits such as failover and offline support. To see configuration options and for more information see the Red Hat Enterprise Linux Identity Management documentation.
SSSD also integrates with the FreeIPA identity management (IdM) server, providing authentication and access control. For Red Hat Single Sign-On, we benefit from this integration authenticating against PAM services and retrieving user data from SSSD. For more information about using Red Hat Identity Management in Linux environments, see the Red Hat Enterprise Linux Identity Management documentation.
Most of the communication between Red Hat Single Sign-On and SSSD occurs through read-only D-Bus interfaces. For this reason, the only way to provision and update users is to use the FreeIPA/IdM administration interface. By default, like the LDAP federation provider, it is set up only to import username, email, first name, and last name.
Groups and roles are automatically registered, but not synchronized, so any changes made by the Red Hat Single Sign-On administrator directly in Red Hat Single Sign-On is not synchronized with SSSD.
Information on how to configure the FreeIPA/IdM server follows.
14.3.1. FreeIPA/IdM Server
As a matter of simplicity, a FreeIPA Docker image already available is used. To set up a server, see the FreeIPA documentation.
Running a FreeIPA server with Docker requires this command:
docker run --name freeipa-server-container -it \
-h server.freeipa.local -e PASSWORD=YOUR_PASSWORD \
-v /sys/fs/cgroup:/sys/fs/cgroup:ro \
-v /var/lib/ipa-data:/data:Z adelton/freeipa-server
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
14.3.2. SSSD and D-Bus
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
14.3.3. Enabling the SSSD Federation Provider
Red Hat Single Sign-On uses DBus-Java to communicate at a low level with D-Bus, which depends on the Unix Sockets Library.
Before enabling the SSSD Federation provider, you must install the RPM for this library:
$ sudo yum install rh-sso7-libunix-dbus-java.x86_64.rpm
For authentication with PAM Red Hat Single Sign-On uses JNA. Be sure you have this package installed:
$ sudo yum install jna
14.4. Configuring a Federated SSSD Store
After installation, you need to configure a federated SSSD store.
To configure a federated SSSD store, complete the following steps:
- Navigate to the Administration Console.
- From the left menu, select User Federation.
- From the Add Provider dropdown list, select sssd. The sssd configuration page opens.
- Click Save.
Now you can authenticate against Red Hat Single Sign-On using FreeIPA/IdM credentials.
14.5. Custom Providers
Red Hat Single Sign-On does have a private SPI for User Storage Federation that you can use to write your own custom providers. There is no commercial support for this yet. You can find some documentation for this in our community documentation. This SPI is slated for a major rewrite before commercial support will be provided.
