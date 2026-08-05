---
title: "Core infrastructure documentation — pages 1321-1360"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1321-1360
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1321-1360
family: sccm
documentKind: "doc"
abstract: "OS upgrade package: Expand Operating Systems, choose Operating system upgrade packages, and then select the OS upgrade package for which to manage access accounts. Boot image: Expand Operating Systems, choose Boot Images, and then select the boot image for which to manage access"
---

# Core infrastructure documentation — pages 1321-1360

<!-- p.1321 -->

           OS upgrade package: Expand Operating Systems, choose Operating system
           upgrade packages, and then select the OS upgrade package for which to
           manage access accounts.

           Boot image: Expand Operating Systems, choose Boot Images, and then
           select the boot image for which to manage access accounts.

   3. Right-click the selected object, and then choose Manage Access Accounts.

   4. In the Add Account dialog box, specify the account type that will be granted
     access to the content, and then specify the access rights associated with the
     account.

       ７ Note

       When you add a user name for the account, and Configuration Manager finds
       both a local user account and a domain user account with that name,
       Configuration Manager sets access rights for the domain user account.

Reporting services point account
SQL Server Reporting Services uses the Reporting services point account to retrieve the
data for Configuration Manager reports from the site database. The Windows user
account and password that you specify are encrypted and stored in the SQL Server
Reporting Services database.

  ７ Note

  The account you specify must have Log on locally permissions on the computer
  hosting the SQL Server Reporting Services database.

  The account is automatically granted all necessary rights by being added to the
  smsschm_users SQL Server Database Role on the Configuration Manager database.

For more information, see Introduction to reporting.

Remote tools permitted viewer accounts
The accounts that you specify as Permitted Viewers for remote control are a list of users
who are allowed to use remote tools functionality on clients.

<!-- p.1322 -->

For more information, see Introduction to remote control.

Site installation account
Use a domain user account to sign in to the server where you run Configuration
Manager setup and install a new site.

This account requires the following rights:

         Administrator on the following servers:
           The site server
           Each server that hosts the site database
           Each instance of the SMS Provider for the site

         Sysadmin on the instance of SQL Server that hosts the site database

Configuration Manager setup automatically adds this account to the SMS Admins
group.

After installation, this account is the only one with rights to the Configuration Manager
console. If you need to remove this account, make sure to add its rights to another user
first.

When expanding a standalone site to include a central administration site, this account
requires either Full Administrator or Infrastructure Administrator role-based
administration rights at the standalone primary site.

Site system installation account
The site server uses the Site system installation account to install, reinstall, uninstall,
and set up site systems. If you set up the site system to require the site server to initiate
connections to this site system, Configuration Manager also uses this account to pull
data from the site system after it installs the site system and any roles. Each site system
can have a different installation account, but you can set up only one installation
account to manage all roles on that site system.

This account requires local administrative permissions on the target site systems.
Additionally, this account must have Access this computer from the network in the
security policy on the target site systems.

   ） Important

<!-- p.1323 -->

  If you are specifying an account in a remote domain or forest, be sure to specify the
  domain FQDN before the user name and not just the domain NetBIOS name. For
  example, specify Corp.Contoso.com\UserName instead of just Corp\UserName. This
  allows Configuration Manager to use Kerberos when the account is used to
  authenticate to the remote site system. Using the FQDN often fixes authentication
  failures resulting from recent hardening changes around NTLM in Windows
  monthly updates.

   Tip

  If you have many domain controllers and these accounts are used across domains,
  before you set up the site system, check that Active Directory has replicated these
  accounts.

  When you specify a service account on each site system to be managed, this
  configuration is more secure. It limits the damage that attackers can do. However,
  domain accounts are easier to manage. Consider the trade-off between security
  and effective administration.

Site system proxy server account
The following site system roles use the Site system proxy server account to access the
internet via a proxy server or firewall that requires authenticated access:

     Asset Intelligence synchronization point
     Exchange Server connector
     Service connection point
     Software update point

  ） Important

  Specify an account that has the least possible permissions for the required proxy
  server or firewall.

For more information, see Proxy server support.

SMTP server connection account
The site server uses the SMTP server connection account to send email alerts when the
SMTP server requires authenticated access.

<!-- p.1324 -->

  ） Important

  Specify an account that has the least possible permissions to send emails.

For more information, see Configure alerts.

Software update point connection account
The site server uses the Software update point connection account for the following
two software update services:

     Windows Server Update Services (WSUS), which sets up settings like product
     definitions, classifications, and upstream settings.

     WSUS Synchronization Manager, which requests synchronization to an upstream
     WSUS server or Microsoft Update.

The site system installation account can install components for software updates, but it
can't do software update-specific functions on the software update point. If you can't
use the site server computer account for this functionality because the software update
point is in an untrusted forest, you must specify this account along with the site system
installation account.

This account must be a local administrator on the computer where you install WSUS. It
must also be part of the local WSUS Administrators group.

For more information, see Plan for software updates.

Source site account
The migration process uses the Source site account to access the SMS Provider of the
source site. This account requires Read permissions to site objects on the source site to
gather data for migration jobs.

If you have Configuration Manager 2007 distribution points or secondary sites with
colocated distribution points, when you upgrade them to Configuration Manager
(current branch) distribution points, this account must also have Delete permissions for
the Site class. This permission is to successfully remove the distribution point from the
Configuration Manager 2007 site during the upgrade.

  ７ Note

<!-- p.1325 -->

  Both the source site account and the source site database account are identified as
  Migration Manager in the Accounts node of the Administration workspace in the
  Configuration Manager console.

For more information, see Migrate data between hierarchies.

Source site database account
The migration process uses the Source site database account to access the SQL Server
database for the source site. To gather data from the SQL Server database of the source
site, the source site database account must have the Read and Execute permissions to
the source site's SQL Server database.

If you use the Configuration Manager (current branch) computer account, make sure
that all the following are true for this account:

     It's a member of the Distributed COM Users security group in the same domain as
     the Configuration Manager 2012 site.
     It's a member of the SMS Admins security group.
     It has the Read permission for all Configuration Manager 2012 objects.

  ７ Note

  Both the source site account and the source site database account are identified as
  Migration Manager in the Accounts node of the Administration workspace in the
  Configuration Manager console.

For more information, see Migrate data between hierarchies.

Task sequence domain join account
Windows Setup uses the Task sequence domain join account to join a newly imaged
computer to a domain. This account is required by the Join Domain or Workgroup task
sequence step with the Join a domain option. This account can also be set up with the
Apply Network Settings step, but it isn't required.

This account requires the Domain Join right in the target domain.

   Tip

<!-- p.1326 -->

  Create one domain user account with the minimal permissions to join the domain,
  and use it for all task sequences.

  ） Important

  Don't assign interactive sign-in permissions to this account.

  Don't use the network access account for this account.

Task sequence network folder connection account
The task sequence engine uses the Task sequence network folder connection account
to connect to a shared folder on the network. This account is required by the Connect to
Network Folder task sequence step.

This account requires permissions to access the specified shared folder. It must be a
domain user account.

   Tip

  Create one domain user account with minimal permissions to access the required
  network resources, and use it for all task sequences.

  ） Important

  Don't assign interactive sign-in permissions to this account.

  Don't use the network access account for this account.

Task sequence run as account
The task sequence engine uses the Task sequence run as account to run command lines
or PowerShell Scripts with credentials other than the Local System account. This account
is required by the Run Command Line and Run PowerShell Script task sequence steps
with the option Run this step as the following account chosen.

Set up the account to have the minimum permissions required to run the command line
that you specify in the task sequence. The account requires interactive sign-in rights. It

<!-- p.1327 -->

usually requires the ability to install software and access network resources. For the Run
PowerShell Script task, this account requires local administrator permissions.

  ） Important

  Don't use the network access account for this account.

  Never make the account a domain admin.

  Never set up roaming profiles for this account. When the task sequence runs, it
  downloads the roaming profile for the account. This leaves the profile vulnerable to
  access on the local computer.

  Limit the scope of the account. For example, create different task sequences that
  run as accounts for each task sequence. Then, if one account is compromised, only
  the client computers to which that account has access are compromised.

  If the command line requires administrative access on the computer, consider
  creating a local administrator account solely for this account on all computers that
  run the task sequence. Delete the account once you no longer need it.

User objects that Configuration Manager uses
in SQL Server
Configuration Manager automatically creates and maintains the following user objects
in SQL. These objects are located within the Configuration Manager database under
Security/Users.

  ） Important

  Modifying or removing these objects may cause drastic issues within a
  Configuration Manager environment. We recommend that you don't make any
  changes to these objects.

smsdbuser_ReadOnly
This object is used to run queries under the read-only context. This object is used with
several stored procedures.

smsdbuser_ReadWrite

<!-- p.1328 -->

This object is used to provide permissions for dynamic SQL statements.

smsdbuser_ReportSchema
This object is used to run SQL Server Reporting Executions. The following stored
procedure is used with this function: spSRExecQuery .

Database roles that Configuration Manager
uses in SQL
Configuration Manager automatically creates and maintains the following role objects in
SQL. These roles provide access to specific stored procedures, tables, views, and
functions. These roles either get or add data to the Configuration Manager database.
These objects are located within the Configuration Manager database under
Security/Roles/Database Roles.

  ） Important

  Modifying or removing these objects may cause drastic issues within a
  Configuration Manager environment. Don't change these objects. The following list
  is for information purposes only.

smsdbrole_AITool
Configuration Manager grants this permission to administrative user accounts based on
role-based access to import volume license information for Asset Intelligence. This
account could be added by a Full Administrator, Operations Administrator or, Asset
Manager role, or any role with 'Manage Asset Intelligence' permission.

smsdbrole_AIUS
Configuration Manager grants the computer account that hosts the Asset Intelligence
synchronization point account access to get Asset Intelligence proxy data and to view
pending AI data for upload.

smsdbrole_CRP
Configuration Manager grants permission to the computer account of the site system
that supports the certificate registration point for Simple Certificate Enrollment Protocol

<!-- p.1329 -->

(SCEP) support for certificate signing and renewal.

smsdbrole_CRPPfx
Configuration Manager grants permission to the computer account of the site system
that supports the certificate registration point configured for PFX support for signing
and renewal.

smsdbrole_DMP
Configuration Manager grants this permission to computer account for a management
point that has the option Allow mobile devices and Mac computers to uses this
management point, the ability to provide support for MDM enrolled devices.

smsdbrole_DmpConnector
Configuration Manager grants this permission to the computer account that hosts the
service connection point to retrieve and provide diagnostic data, manage cloud services,
and retrieve service updates.

smsdbrole_DViewAccess
Configuration Manager grants this permission to the computer account of the primary
site servers on the CAS when the SQL Server distributed views option is selected in the
replication link properties.

smsdbrole_DWSS
Configuration Manager grants this permission to the computer account that hosts the
data warehouse role.

smsdbrole_EnrollSvr
Configuration Manager grants this permission to the computer account that hosts the
enrollment point to allow for device enrollment via MDM.

smsdbrole_extract
Provides access to all the extended schema views.

<!-- p.1330 -->

smsdbrole_HMSUser
For the hierarchy manager service. Configuration Manager grants permissions this
account to manage failover state messages and SQL Server Broker transactions between
sites within a hierarchy.

  ７ Note

  The smdbrole_WebPortal role is a member of this role by default.

smsdbrole_MCS
Configuration Manager grants this permission to the computer account of the
distribution point that supports multicast.

smsdbrole_MP
Configuration Manager grants this permission to the computer account that hosts the
management point role to provide support for the Configuration Manager clients.

smsdbrole_MPMBAM
Configuration Manager grants this permission to the computer account that hosts the
management point that manages BitLocker for an environment.

smsdbrole_MPUserSvc
Configuration Manager grants this permission to the computer account that hosts the
management point to support user-based application requests.

smsdbrole_siteprovider
Configuration Manager grants this permission to the computer account that hosts an
SMS Provider role.

smsdbrole_siteserver
Configuration Manager grants this permission to the computer account that hosts the
primary site or CAS.

<!-- p.1331 -->

smsdbrole_SUP
Configuration Manager grants this permission to the computer account that hosts the
software update point for working with third-party updates.

smsschm_users
Configuration Manager grants access to the account used for the reporting services
point account to allow access to the SMS reporting views to display the Configuration
Manager reporting data. The data is further restricted with the use of role-based access.

Elevated permissions
Configuration Manager requires some accounts to have elevated permissions for
ongoing operations. For example, see Prerequisites for installing a primary site. The
following list summarizes these permissions and the reasons why they're needed.

     The computer account of the primary site server and central administration site
     server requires:

        Local Administrator rights on all site system servers. This permission is to
        manage, install, and remove system services. The site server also updates local
        groups on the site system when you add or remove roles.

        Sysadmin access to the SQL Server instance for the site database. This
        permission is to configure and manage SQL Server for the site. Configuration
        Manager tightly integrates with SQL, it's not just a database.

     User accounts in the Full Administrator role require:

        Local Administrator rights on all site servers. This permission is to view, edit,
        remove, and install system services, registry keys and values, and WMI objects.

        Sysadmin access to the SQL Server instance for the site database. This
        permission is to install and update the database during setup or recovery. It's
        also required for SQL Server maintenance and operations. For example,
        reindexing and updating statistics.

          ７ Note

          Some organizations may choose to remove sysadmin access and only grant
          it when it is required. This behavior is sometimes referred to as "just-in-
          time (JIT) access." In this case, users with the Full Administrator role should

<!-- p.1332 -->

           still have access to read, update, and execute stored procedures on the
           Configuration Manager database. These permissions allow them to
           troubleshoot most issues without full sysadmin access.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1333 -->

Communications between endpoints in
Configuration Manager
ﾃ   Summarize this article for me

Applies to: Configuration Manager (current branch)

This article describes how Configuration Manager site systems and clients communicate across
your network. It includes the following sections:

     Communications between site systems in a site
        Site server to distribution point

     Communications from clients to site systems and services
        Client to management point communication
        Client to distribution point communication
        Considerations for client communications from the internet or an untrusted forest

     Communications across Active Directory forests
        Support domain computers in a forest that's not trusted by your site server's forest
        Support computers in a workgroup
        Scenarios to support a site or hierarchy that spans multiple domains and forests

Communications between site systems in a site
When Configuration Manager site systems or components communicate across the network to
other site systems or components in the site, they use one of the following protocols,
depending on how you configure the site:

     Server message block (SMB)

     HTTP

     HTTPS

With the exception of communication from the site server to a distribution point, server-to-
server communications in a site can occur at any time. These communications don't use
mechanisms to control the network bandwidth. Because you can't control the communication
between site systems, make sure that you install site system servers in locations that have fast
and well-connected networks.

Site server to distribution point

<!-- p.1334 -->

To help you manage the transfer of content from the site server to distribution points, use the
following strategies:

     Configure the distribution point for network bandwidth control and scheduling. These
     controls resemble the configurations that are used by intersite addresses. Use this
     configuration instead of installing another Configuration Manager site when the transfer
     of content to remote network locations is your main bandwidth consideration.

     You can install a distribution point as a prestaged distribution point. A prestaged
     distribution point lets you use content that is manually put on the distribution point
     server and removes the requirement to transfer content files across the network.

For more information, see Manage network bandwidth for content management.

Communications from clients to site systems and
services
Clients initiate communication to site system roles, Active Directory Domain Services, and
online services. To enable these communications, firewalls must allow the network traffic
between clients and the endpoint of their communications. For more information about ports
and protocols used by clients when they communicate to these endpoints, see Ports used in
Configuration Manager.

Before a client can communicate with a site system role, the client uses service location to find
a role that supports the client's protocol (HTTP or HTTPS). By default, clients use the most
secure method that's available to them. For more information, see Understand how clients find
site resources and services.

To help secure the communication between Configuration Manager clients and site servers,
configure one of the following options:

     Use a public key infrastructure (PKI) and install PKI certificates on clients and servers.
     Enable site systems to communicate with clients over HTTPS. For information about how
     to use certificates, see PKI certificate requirements.

     Configure the site to Use Configuration Manager-generated certificates for HTTP site
     systems. For more information, see Enhanced HTTP.

When you deploy a site system role that uses Internet Information Services (IIS) and supports
communication from clients, you must specify whether clients connect to the site system by
using HTTP or HTTPS. If you use HTTP, you must also consider signing and encryption choices.
For more information, see Planning for signing and encryption.

<!-- p.1335 -->

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP client
  communication are deprecated. Configure the site for HTTPS or Enhanced HTTP. For more
  information, see Enable the site for HTTPS-only or enhanced HTTP.

  ２ Warning

  Configuration Manager doesn't support HTTP Strict Transport Security (HSTS)
  configuration in IIS. Configuration Manager clients don’t honor HSTS headers, however
  the mandatory redirection to HTTPS isn’t compatible with HTTP or Enhanced HTTP site
  system role configuration. For more information on IIS configuration, see HSTS Settings
  for a Web Site.

  Enabling HSTS breaks site system roles that rely on HTTP, in particular:

           Fallback Status Point (FSP) is HTTP-only by design and stops functioning if HTTPS
           redirection is enforced.
           Software Update Point (SUP) uses Windows Server Update Services (WSUS). WSUS
           encrypts update metadata over HTTPS but always delivers update payloads over
           HTTP. Enabling HTTPS redirection on WSUS Web Site blocks the payload downloads
           and breaks update functionality.

Client to management point communication
There are two stages when a client communicates with a management point: authentication
(transport) and authorization (message). This process varies depending upon the following
factors:

     Site configuration: HTTPS only, allows HTTP or HTTPS, or allows HTTP or HTTPS with
     enhanced HTTP enabled
     Management point configuration: HTTPS or HTTP
     Device identity for device-centric scenarios
     User identity for user-centric scenarios

Use the following table to understand how this process works:

                                                                                 ﾉ   Expand table

<!-- p.1336 -->

 MP       Client authentication             Client authorization             Client authorization
 type                                       Device identity                  User identity

 HTTP     Anonymous                         Location request:                For user-centric scenarios,
          With Enhanced HTTP, the site      Anonymous                        using one of the following
          verifies the Microsoft Entra ID   Client package: Anonymous        methods to prove user
          user or device token.             Registration, using one of       identity:
                                            the following methods to         - Windows-integrated
                                            prove device identity:           authentication
                                            - Anonymous (manual              - Microsoft Entra ID user token
                                            approval)                        (Enhanced HTTP)
                                            - Windows-integrated
                                            authentication
                                            - Microsoft Entra ID device
                                            token (Enhanced HTTP)
                                            After registration, the client
                                            uses message signing to
                                            prove device identity

 HTTPS    Using one of the following        Location request:                For user-centric scenarios,
          methods:                          Anonymous                        using one of the following
          - PKI certificate                 Client package: Anonymous        methods to prove user
          - Windows-integrated              Registration, using one of       identity:
          authentication                    the following methods to         - Windows-integrated
          - Microsoft Entra ID user or      prove device identity:           authentication
          device token                      - Anonymous (manual              - Microsoft Entra ID user token
                                            approval)
                                            - Windows-integrated
                                            authentication
                                            - PKI certificate
                                            - Microsoft Entra ID user or
                                            device token
                                            After registration, the client
                                            uses message signing to
                                            prove device identity

   Tip

  For more information on the configuration of the management point for different device
  identity types and with the cloud management gateway, see Enable management point
  for HTTPS.

Client to distribution point communication
When a client communicates with a distribution point, it only needs to authenticate before
downloading the content. Use the following table to understand how this process works:

<!-- p.1337 -->

                                                                                     ﾉ   Expand table

 DP type    Client authentication

 HTTP       - Anonymous, if allowed
            - Windows-integrated authentication with computer account or network access account
            - Content access token (Enhanced HTTP)

 HTTPS      - PKI certificate
            - Windows-integrated authentication with computer account or network access account
            - Content access token

Considerations for client communications from the internet or
an untrusted forest
For more information, see the following articles:

     Overview of cloud management gateway

     Plan for internet-based client management

Communications across Active Directory forests
Configuration Manager supports sites and hierarchies that span Active Directory forests. It also
supports domain computers that aren't in the same Active Directory forest as the site server,
and computers that are in workgroups.

Support domain computers in a forest that's not trusted by
your site server's forest
     Install site system roles in that untrusted forest, with the option to publish site
     information to that Active Directory forest

     Manage these computers as if they're workgroup computers

When you install site system servers in an untrusted Active Directory forest, the client-to-server
communication from clients in that forest is kept within that forest, and Configuration Manager
can authenticate the computer by using Kerberos. When you publish site information to the
client's forest, clients benefit from retrieving site information, such as a list of available
management points, from their Active Directory forest, rather than downloading this
information from their assigned management point.

<!-- p.1338 -->

  ７ Note

  If you want to manage devices that are on the internet, you can install internet-based site
  system roles in your perimeter network when the site system servers are in an Active
  Directory forest. This scenario doesn't require two-way trust between the perimeter
  network and the site server's forest.

Support computers in a workgroup
     Manually approve workgroup computers when they use HTTP client connections to site
     system roles. Configuration Manager can't authenticate these computers by using
     Kerberos.

     Configure workgroup clients to use the Network Access Account so that these computers
     can retrieve content from distribution points.

     Provide an alternative mechanism for workgroup clients to find management points. Use
     DNS publishing or directly assign a management point. These clients can't retrieve site
     information from Active Directory Domain Services.

For more information, see the following articles:

     Manage conflicting records

     Network access account

     How to install Configuration Manager clients on workgroup computers

Scenarios to support a site or hierarchy that spans multiple
domains and forests

Scenario 1: Communication between sites in a hierarchy that spans
forests

This scenario requires a two-way forest trust that supports Kerberos authentication. If you don't
have a two-way forest trust that supports Kerberos authentication, then Configuration
Manager doesn't support a child site in the remote forest.

Configuration Manager supports installing a child site in a remote forest that has the required
two-way trust with the forest of the parent site. For example, you can place a secondary site in
a different forest from its primary parent site as long as the required trust exists.

<!-- p.1339 -->

  ７ Note

  A child site can be a primary site (where the central administration site is the parent site)
  or a secondary site.

Intersite communication in Configuration Manager uses database replication and file-based
transfers. When you install a site, you must specify an account with which to install the site on
the designated server. This account also establishes and maintains communication between
sites. After the site successfully installs and initiates file-based transfers and database
replication, you don't have to configure anything else for communication to the site.

When a two-way forest trust exists, Configuration Manager doesn't require any additional
configuration steps.

By default, when you install a new child site, Configuration Manager configures the following
components:

     An intersite file-based replication route at each site that uses the site server computer
     account. Configuration Manager adds the computer account of each computer to the
     SMS_SiteToSiteConnection_<sitecode> group on the destination computer.

     Database replication between the SQL Servers at each site.

Also set the following configurations:

     Intervening firewalls and network devices must allow the network packets that
     Configuration Manager requires.

     Name resolution must work between the forests.

     To install a site or site system role, you must specify an account that has local
     administrator permissions on the specified computer.

Scenario 2: Communication in a site that spans forests

This scenario doesn't require a two-way forest trust.

Primary sites support the installation of site system roles on computers in remote forests.

     When a site system role accepts connections from the internet, as a security best practice,
     install the site system roles in a location where the forest boundary provides protection
     for the site server (for example, in a perimeter network).

To install a site system role on a computer in an untrusted forest:

<!-- p.1340 -->

     Specify a Site System Installation Account, which the site uses to install the site system
     role. (This account must have local administrative credentials to connect to.) Then install
     site system roles on the specified computer.

     Select the site system option Require the site server to initiate connections to this site
     system. This setting requires the site server to establish connections to the site system
     server to transfer data. This configuration prevents the computer in the untrusted location
     from initiating contact with the site server that's inside your trusted network. These
     connections use the Site System Installation Account.

To use a site system role that was installed in an untrusted forest, firewalls must allow the
network traffic even when the site server initiates the transfer of data.

Additionally, the following site system roles require direct access to the site database.
Therefore, firewalls must allow applicable traffic from the untrusted forest to the site's SQL
Server:

     Asset Intelligence synchronization point

     Endpoint Protection point

     Enrollment point

     Management point

     Reporting service point

     State migration point

For more information, see Ports used in Configuration Manager.

You might need to configure the management point and enrollment point access to the site
database.

     By default, when you install these roles, Configuration Manager configures the computer
     account of the new site system server as the connection account for the site system role.
     It then adds the account to the appropriate SQL Server database role.

     When you install these site system roles in an untrusted domain, configure the site system
     role connection account to enable the site system role to obtain information from the
     database.

If you configure a domain user account to be the connection account for these site system
roles, make sure that the domain user account has appropriate access to the SQL Server
database at that site:

<!-- p.1341 -->

      Management point: Management Point Database Connection Account

      Enrollment point: Enrollment Point Connection Account

Consider the following additional information when you plan for site system roles in other
forests:

      If you run Windows Firewall, configure the applicable firewall profiles to pass
      communications between the site database server and computers that are installed with
      remote site system roles.

      When the internet-based management point trusts the forest that contains the user
      accounts, user policies are supported. When no trust exists, only computer policies are
      supported.

Scenario 3: Communication between clients and site system roles when
the clients aren't in the same Active Directory forest as their site server

Configuration Manager supports the following scenarios for clients that aren't in the same
forest as their site's site server:

      There's a two-way forest trust between the forest of the client and the forest of the site
      server.

      The site system role server is located in the same forest as the client.

      The client is on a domain computer that doesn't have a two-way forest trust with the site
      server, and site system roles aren't installed in the client's forest.

      The client is on a workgroup computer.

Clients on a domain-joined computer can use Active Directory Domain Services for service
location when their site is published to their Active Directory forest.

To publish site information to another Active Directory forest:

      Specify the forest and then enable publishing to that forest in the Active Directory
      Forests node of the Administration workspace.

      Configure each site to publish its data to Active Directory Domain Services. This
      configuration enables clients in that forest to retrieve site information and find
      management points. For clients that can't use Active Directory Domain Services for
      service location, you can use DNS or the client's assigned management point.

<!-- p.1342 -->

Scenario 4: Put the Exchange Server connector in a remote forest
To support this scenario, make sure that name resolution works between the forests. For
example, configure DNS forwards. When you configure the Exchange Server connector, specify
the intranet FQDN of the Exchange Server. For more information, see Manage mobile devices
with Configuration Manager and Exchange.

See also
     Plan for security

     Security and privacy for Configuration Manager clients

Last updated on 02/13/2026

<!-- p.1343 -->

Enhanced HTTP
Article • 11/16/2023

Applies to: Configuration Manager (current branch)

Microsoft recommends using HTTPS communication for all Configuration Manager
communication paths, but it's challenging for some customers because of the overhead
of managing PKI certificates. With enhanced HTTP, Configuration Manager can provide
secure communication by issuing self-signed certificates to specific site systems.

There are two primary goals for this configuration:

      You can secure sensitive client communication without the need for PKI server
      authentication certificates.

      Clients can securely access content from distribution points without the need for a
      network access account, client PKI certificate, or Windows authentication.

All other client communication is over HTTP. Enhanced HTTP isn't the same as enabling
HTTPS for client communication or a site system.

  ７ Note

  PKI certificates are still a valid option for customers with the following
  requirements:

        All client communication is over HTTPS
        Advanced control of the signing infrastructure

  If you're already using PKI, site systems use the PKI certificate bound in IIS even if
  you enable enhanced HTTP.

Scenarios
The following scenarios benefit from enhanced HTTP:

Scenario 1: Client to management point
Microsoft Entra joined devices and devices with a Configuration Manager issued token
can communicate with a management point configured for HTTP if you enable

<!-- p.1344 -->

enhanced HTTP for the site. With enhanced HTTP enabled, the site server generates a
certificate for the management point allowing it to communicate via a secure channel.

  ７ Note

  This scenario doesn't require using an HTTPS-enabled management point, but it's
  supported as an alternative to using enhanced HTTP. For more information on
  using an HTTPS-enabled management point, see Enable management point for
  HTTPS.

Scenario 2: Client to distribution point
A workgroup or Microsoft Entra joined client can authenticate and download content
over a secure channel from a distribution point configured for HTTP. These types of
devices can also authenticate and download content from a distribution point
configured for HTTPS without requiring a PKI certificate on the client. It's challenging to
add a client authentication certificate to a workgroup or Microsoft Entra joined client.

This behavior includes OS deployment scenarios with a task sequence running from
boot media, PXE, or Software Center. For more information, see Network access account.

Scenario 3: Microsoft Entra device identity
A Microsoft Entra joined or hybrid Microsoft Entra device without a Microsoft Entra user
signed in can securely communicate with its assigned site. The cloud-based device
identity is now sufficient to authenticate with the CMG and management point for
device-centric scenarios. (A user token is still required for user-centric scenarios.)

Features
The following Configuration Manager features support or require enhanced HTTP:

     Cloud management gateway
     OS deployment without a network access account
     Enable co-management for new internet-based Windows devices
     App approvals via email
     Administration service
     View recently connected consoles
     BitLocker management key recovery (version 2103 and later)
     Software Center user-available applications (version 2107 and later)

<!-- p.1345 -->

     Company Portal on co-managed devices (version 2107 and later)

  ７ Note

  The software update point and related scenarios have always supported secure
  HTTP traffic with clients as well as the cloud management gateway. It uses a
  mechanism with the management point that's different from certificate- or token-
  based authentication.

Unsupported scenarios
Enhanced HTTP doesn't currently secure all communication in Configuration Manager.
The following list summarizes some key functionality that's still HTTP.

     Client peer-to-peer communication for content
     State migration point
     Remote tools
     Reporting services point

  ７ Note

  This list isn't exhaustive.

Prerequisites
     A management point configured for HTTP client connections. Set this option on
     the General tab of the management point role properties.

     A distribution point configured for HTTP client connections. Set this option on the
     Communication tab of the distribution point role properties. Don't enable the
     option to Allow clients to connect anonymously.

     For scenarios that require Microsoft Entra authentication, onboard the site to
     Microsoft Entra ID for cloud management. If you don't onboard the site to
     Microsoft Entra ID, you can still enable enhanced HTTP.

     For Scenario 3 only: A client running a supported version of Windows 10 or later
     and joined to Microsoft Entra ID. The client requires this configuration for
     Microsoft Entra device authentication.

<!-- p.1346 -->

  ７ Note

  There are no OS version requirements, other than what the Configuration Manager
  client supports.

Configure the site
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node. Select the site and choose
     Properties in the ribbon.

   2. Switch to the Communication Security tab. Select the option for HTTPS or HTTP.
     Then enable the option to Use Configuration Manager-generated certificates for
     HTTP site systems.

   Tip

  Wait up to 30 minutes for the management point to receive and configure the new
  certificate from the site.

You can also enable enhanced HTTP for the central administration site (CAS). Use this
same process, and open the properties of the CAS. This action only enables enhanced
HTTP for the SMS Provider role at the CAS. It's not a global setting that applies to all
sites in the hierarchy.

For more information on how the client communicates with the management point and
distribution point with this configuration, see Communications from clients to site
systems and services.

Validate the certificate
You can see these certificates in the Configuration Manager console. Go to the
Administration workspace, expand Security, and select the Certificates node. Look for
the SMS Issuing root certificate and the site server role certificates issued by the SMS
Issuing root.

When you enable enhanced HTTP, the site server generates a self-signed certificate
named SMS Role SSL Certificate. This certificate is issued by the root SMS Issuing
certificate. The management point adds this certificate to the IIS default web site bound
to port 443.

<!-- p.1347 -->

To see the status of the configuration, review mpcontrol.log.

Conceptual diagram
This diagram summarizes and visualizes some of the main aspects of the enhanced
HTTP functionality in Configuration Manager.

     The connection with Microsoft Entra ID is recommended but optional. It enables
     scenarios that require Microsoft Entra authentication.

     When you enable the site option for enhanced HTTP, the site issues self-signed
     certificates to site systems such as the management point and distribution point
     roles.

     With the site systems still configured for HTTP connections, clients communicate
     with them over HTTPS.

Frequently asked questions

What are the benefits of enhanced HTTP?

<!-- p.1348 -->

The main benefit is to reduce the usage of pure HTTP, which is an insecure protocol.
Configuration Manager tries to be secure by default, and Microsoft wants to make it
easy for you to keep your devices secure. Enabling PKI-based HTTPS is a more secure
configuration, but that can be complex for many customers. If you can't do HTTPS, then
enable enhanced HTTP. Microsoft recommends this configuration, even if your
environment doesn't currently use any of the features that support it.

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP client
  communication are deprecated. Configure the site for HTTPS or Enhanced HTTP.
  For more information, see Enable the site for HTTPS-only or enhanced HTTP.

Do I need to use Microsoft Entra ID to enable enhanced
HTTP?
No. Many of the scenarios and features that benefit from enhanced HTTP rely on
Microsoft Entra authentication. You can enable enhanced HTTP without onboarding the
site to Microsoft Entra ID. It then supports features like the administration service and
the reduced need for the network access account. You only need Microsoft Entra ID
when one of the supporting features requires it.

  ７ Note

  Even if you don't directly use the administration service REST API, some
  Configuration Manager features natively use it, including parts of the Configuration
  Manager console.

How do clients communicate with site systems?
When you enable enhanced HTTP, the site issues certificates to site systems. For
example, the management point and the distribution point. Then these site systems can
support secure communication in currently supported scenarios.

From a client perspective, the management point issues each client a token. The client
uses this token to secure communication with the site systems. That behavior is OS
version agnostic, other than what the Configuration Manager client supports.

<!-- p.1349 -->

If some site systems are already HTTPS, can I enable
enhanced HTTP?
Yes. Site systems always prefer a PKI certificate. For example, one management point
already has a PKI certificate, but others don't. When you enable enhanced HTTP for the
site, the HTTPS management point continues to use the PKI certificate. The other
management points use the site-issued certificate for enhanced HTTP.

Next steps
     Plan for security

     Security and privacy for Configuration Manager clients

     Configure security

     Communication between endpoints

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1350 -->

Hierarchy maintenance tool (Preinst.exe)
for Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The hierarchy maintenance tool (Preinst.exe) passes commands to the Configuration
Manager Hierarchy Manager while the Hierarchy Manager service is running. The
hierarchy maintenance tool is automatically installed when you install a Configuration
Manager site. You can find Preinst.exe in the \bin\X64\00000409 folder on the site server.

Use the hierarchy maintenance tool in the following scenarios:

      When secure key exchange is required, there are situations where you need to
      manually do the initial public key exchange between sites. For more information,
      see Manually exchange public keys between sites.

      Remove active jobs for a destination site that's no longer available.

      Delete a site server from the Configuration Manager console when you can't
      uninstall it with setup. For example, if you physically remove a Configuration
      Manager site without first running setup to uninstall the site. The site information
      will still exist in the parent site's database, and the parent site will continue to
      attempt to communicate with the child site. To resolve this issue, run the hierarchy
      maintenance tool and manually delete the child site from the parent site's
      database.

      Stop all Configuration Manager services at a site without having to stop services
      individually.

      When you recover a site, use the CHILDKEYS option to distribute the public keys
      from multiple child sites to the recovering site.

To run the hierarchy maintenance tool, the current user needs administrative privileges
on the local computer. Also, the user must explicitly have the Administer security right
for the Site class. It's not sufficient that the user inherits this right by being a member of
a group that has that permission.

Hierarchy maintenance tool command-line
options

<!-- p.1351 -->

When you use the hierarchy maintenance tool, you must run it locally on the central
administration site (CAS), primary site, or secondary site server. Use the following syntax:
preinst.exe /<option> . The following command-line options are available:

      /DELJOB <SiteCode> : Delete all jobs or commands from the current site to the

     specified destination site.

      /DELSITE <ChildSiteCodeToRemove> : Use this option at a parent site to delete the

     data for child sites from the site database of the parent site. Typically, you use this
     option if a site server computer is decommissioned before you uninstall the site
     from it.

        ７ Note

        The /DELSITE option doesn't uninstall the site on the computer specified by
        the ChildSiteCodeToRemove parameter. This option only removes the site
        information from the Configuration Manager site database.

      /DUMP <SiteCode> : Use this option on the local site server to write site control

     images to the root folder of the drive on which the site is installed. You can write a
     specific site control image to the folder or write all site control files in the
     hierarchy.

        /DUMP <SiteCode> writes the site control image only for the specified site.

        /DUMP writes the site control files for all sites.

     An image is a binary representation of the site control file, which is stored in the
     Configuration Manager site database. The dumped site control file image is a sum
     of the base image plus the pending delta images.

     After dumping a site control file image with the hierarchy maintenance tool, the
     file name is in the format sitectrl_<SiteCode>.ct0 .

      /STOPSITE : Use this option on the local site server to start a shutdown cycle for the

     Configuration Manager Site Component Manager service, which partially resets the
     site. When you start this shutdown cycle, it stops some Configuration Manager
     services on a site server and its remote site systems. It also flags these services for
     reinstallation. As a result of this shutdown cycle, some passwords are automatically
     changed when the services are reinstalled.

        ７ Note

<!-- p.1352 -->

  If you want to see a record of shutdown, reinstallation, and password changes
  for Site Component Manager, enable logging for this component before
  using this command-line option.

After the shutdown cycle is started, it proceeds automatically, skipping any non-
responding components or computers. However, if the Site Component Manager
service can't access a remote site system during the shutdown cycle, the
components that are installed on the remote site system are reinstalled when the
Site Component Manager service is restarted. When it's restarted, the Site
Component Manager service repeatedly attempts reinstallation of all services that
are flagged for reinstallation until it's successful.

You can restart the Site Component Manager service using Service Manager. After
it restarts, all affected services are uninstalled, reinstalled, and restarted. After you
use the /STOPSITE option to start the shutdown cycle, you can't avoid the
reinstallation cycles after the Site Component Manager service is restarted.

/KEYFORPARENT : Distribute the site's public key to a parent site.

The /KEYFORPARENT option places the public key of the site in the file
<SiteCode>.CT4 at the root of the program files drive. After you run preinst.exe

with this option, manually copy this file to the parent site's \Inboxes\hman.box
folder (not hman.box\pubkey ).

/KEYFORCHILD : Distribute the site's public key to a child site.

The /KEYFORCHILD option places the public key of the site in the file
<SiteCode>.CT5 at the root of the program files drive. After you run preinst.exe

with this option, manually copy this file to the child site's \Inboxes\hman.box folder
(not hman.box\pubkey ).

/CHILDKEYS : Use this option on the child sites of a site that you're recovering. It

distributes public keys from multiple child sites to the recovering site.

The /CHILDKEYS option places the key from the site where you run the option and
all of that sites child sites public keys into the file <SiteCode>.CT6 . After you run
preinst.exe with this option, manually copy this file to the recovering site's
\Inboxes\hman.box folder (not hman.box\pubkey ).

/PARENTKEYS : Use this option on the parent site of a site that you're recovering. It

distributes public keys from all parent sites to the recovering site.

<!-- p.1353 -->

     The /PARENTKEYS option places the key from the site where you run the option and
     the keys from each parent site above that site into the file <SiteCode>.CT7 . After
     you run preinst.exe with this option, manually copy this file to the recovering site's
      \Inboxes\hman.box folder (not hman.box\pubkey ).

Manually exchange public keys between sites
By default, the Require secure key exchange option is enabled for Configuration
Manager sites. When secure key exchange is required, there are two situations when you
need to manually do the initial key exchange between sites:

     If you haven't extended the Active Directory schema for Configuration Manager

     Configuration Manager sites aren't publishing site data to Active Directory

You can use the hierarchy maintenance tool to export the public keys for each site. Once
exported, then manually exchange the keys between the sites.

  ７ Note

  After the public keys are manually exchanged, review the hman.log log file on the
  parent site server. This log file records site configuration changes and site
  information publication to Active Directory. You can make sure that the primary site
  has processed the new public key.

How to manually transfer the child site public key to the
parent site
   1. Sign in to the child site server, open a command prompt, and navigate to the
     location of Preinst.exe.

   2. Type the following command to export the child site's public key: Preinst
     /keyforparent

The /keyforparent option places the public key of the child site in the <SiteCode>.CT4
file located at the root of the system drive.

   1. Move the <SiteCode>.CT4 file to the parent site's \inboxes\hman.box folder in the
     Configuration Manager installation directory.

<!-- p.1354 -->

How to manually transfer the parent site public key to the
child site
   1. Sign in to the parent site server, open a command prompt, and navigate to the
     location of Preinst.exe.

   2. Type the following command to export the parent site's public key: Preinst
     /keyforchild

The /keyforchild option places the public key of the parent site in the <SiteCode>.CT5
file located at the root of the system drive.

   1. Move the <SiteCode>.CT5 file to the child site's \inboxes\hman.box folder in the
     Configuration Manager installation directory.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1355 -->

International support in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The following sections provide technical details to help you make Configuration
Manager compliant with specific international requirements.

GB18030 Requirements
Configuration Manager meets the standards that are defined in GB18030 so that you
can use Configuration Manager in China. A Configuration Manager deployment must
have the following configurations to meet the GB18030 requirements:

      Each site server computer and SQL Server computer that you use with
      Configuration Manager must use a Chinese operating system.

      Each site database and each instance of SQL Server in the hierarchy must use the
      same collation, and must be one of the following:

         Chinese_Simplified_Pinyin_100_CI_AI

         Chinese_Simplified_Stroke_Order_100_CI_AI

        ７ Note

        These database collations are an exception to the requirements that are noted
        in Support for SQL Server versions for Configuration Manager.

      You must place a file with the name GB18030.SMS in the root folder of the system
      volume of each site server computer in the hierarchy. This file does not contain any
      data and can be an empty text file that is named to meet this requirement.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1356 -->

Interoperability between different
versions of Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can install and operate multiple, independent hierarchies of Configuration Manager
on the same network. However, because different hierarchies of Configuration Manager
don't interoperate outside of the migration process, each hierarchy requires
configurations to prevent conflicts between them. Additionally, you can create certain
configurations to help resources that you manage interact with the site systems from
the correct hierarchy.

Current branch and earlier versions
Sites of different versions can't coexist in the same Configuration Manager hierarchy.
The only exceptions are during the process of the following upgrade scenarios:

      From System Center 2012 Configuration Manager to Configuration Manager
      current branch
      From one Configuration Manager current branch version to a newer version using
      in-console updates

You can deploy a Configuration Manager current branch site and hierarchy side by side
with an existing System Center 2012 Configuration Manager site or hierarchy. Plan to
prevent clients from either version from trying to join a site from the other version.

For example, if two or more Configuration Manager hierarchies have overlapping
boundaries that include the same network locations, assign each new client to a specific
site instead of using automatic site assignment. For more information, see How to
assign clients to a site.

Additionally, you can't install a client from System Center 2012 Configuration Manager
on a computer that hosts a site system role from Configuration Manager current branch.
You also can't you install a Configuration Manager current branch client on a computer
that hosts a site system role from System Center 2012 Configuration Manager.

The following clients and connections aren't supported:

      Any System Center 2012 Configuration Manager or earlier computer client version

<!-- p.1357 -->

          Any System Center 2012 Configuration Manager or earlier device management
          client

          Windows CE Platform Builder device management client (any version)

          System Center Mobile Device Manager VPN connection

Client site assignment considerations
Configuration Manager clients can be assigned to only a single primary site. You can't
predict the actual site assignment of a client when all of the following conditions are
true:

          You use automatic site assignment to assign clients to a site during client
          installation
          More than one boundary group includes the same boundary
          The boundary groups have different assigned sites

If boundaries overlap across multiple Configuration Manager sites and hierarchies,
clients might not be assigned to the site you expect, or might not get assigned to a site
at all.

Configuration Manager current branch clients check the version of the site before they
complete site assignment. If site boundaries overlap, you can't assign clients to a site
with a previous version. However, earlier System Center 2012 Configuration Manager
clients might incorrectly be assigned to a later Configuration Manager current branch
site.

To prevent clients from unintentionally being assigned to the wrong site when two
hierarchies have overlapping boundaries, configure client installation parameters to
assign clients to a specific site.

Limitations in a mixed-version hierarchy
When you upgrade a Configuration Manager current branch hierarchy, there are times
when different sites will have different versions. For example, first you upgrade the
central administration site. Because of site maintenance windows, you don't upgrade the
primary sites until a later time and date.

When different sites in a single hierarchy run different versions, some functionality isn't
available. This behavior can affect how you manage Configuration Manager objects in
the Configuration Manager console, and which functionality is available to clients.

<!-- p.1358 -->

Typically, functionality from the newer version of Configuration Manager isn't accessible
at sites or to clients that run a lower service pack version.

Network access account
You upgrade the central administration site to Configuration Manager current branch.
You view the network access account details from a Configuration Manager console
that's connected to this updated site. It doesn't display account details from sites that
still run System Center 2012 Configuration Manager.

After you upgrade the primary site to the same version as the central administration site,
the account details are visible in the console.

The same behavior applies when you update between versions of Configuration
Manager.

Boot images for OS deployment

When upgrading from System Center 2012 Configuration Manager
to Configuration Manager current branch

When the top-level site of a hierarchy upgrades to Configuration Manager current
branch, it automatically updates the default boot images to use the Windows
Assessment and Deployment Kit (ADK) version 10. Use these boot images only for
deployments to clients at Configuration Manager current branch sites. For more
information, see Planning for OS deployment interoperability.

When upgrading between Configuration Manager current branch
versions

As long as new versions of Configuration Manager don't update the version of Windows
ADK that's in use, there's no effect on boot images.

New task sequence steps
When you create a task sequence with a step introduced in one version of Configuration
Manager that's not available in an earlier version, you might have the following issues:

     An error occurs when you try to edit the task sequence from a site that's running a
     previous version of Configuration Manager.

<!-- p.1359 -->

     The task sequence doesn't run on a computer that runs a previous version of the
     Configuration Manager client.

Client to down-level management point communications
A Configuration Manager client that communicates with a management point from a
site that runs a lower version than the client can only use functionality that the down-
level version of Configuration Manager supports. For example, if you deploy content
from a Configuration Manager current branch site that was recently upgraded to a client
that communicates with a management point that hasn't yet upgraded to that version,
that client can't use new functionality from the latest version.

Package and task sequence deployments to legacy clients
You can't deploy a package or task sequence to a client version 5.7730 or earlier. To
work around this limitation, upgrade the client to a later version.

Orchestration groups
Orchestration groups can't be used in a mixed-version hierarchy.

Assign site systems as clients to the same site
If you install the Configuration Manager client on site systems, assign them to the same
site. Roles like the management point and distribution point have shared binary files
between the role and the client. These collocated clients should always be the same
version as the site system role.

For example, for a management point in site XYZ, assign the client installed on this site
system server to site XYZ.

Configuration Manager console
This section contains information about the use of the Configuration Manager console
in an environment that has a mix of Configuration Manager versions.

An environment with both System Center 2012
Configuration Manager and Configuration Manager
current branch

<!-- p.1360 -->

To manage a Configuration Manager site, both the console and the site the console
connects to must run the same version of Configuration Manager. For example, you
can't use a System Center 2012 Configuration Manager console to manage a
Configuration Manager current branch site, or the other way around.

It's not supported to install both the System Center 2012 Configuration Manager
console and the Configuration Manager current branch console on the same computer.

An environment with multiple versions of Configuration
Manager
Configuration Manager current branch doesn't support installing more than a single
Configuration Manager console on a computer. To use multiple consoles that are
specific to different versions of Configuration Manager, install the different consoles on
separate computers.

During the process of updating sites in a hierarchy to a new version, you can connect a
console to a site that runs a newer version and view information about other sites in that
hierarchy. However, this configuration isn't recommended. It's possible that differences
between the console version and Configuration Manager site version can result in data
issues. Some features that are available in the latest product version won't be available
in the console.

It's not supported to manage a site when using a console with a version that doesn't
match the site version. Doing so might cause loss of data and can put your site at risk.
For example, it's not supported to use a console from version 2103 to manage a site
that runs version 2010.

Next steps
Use the Configuration Manager client software for extended interoperability with future
versions of a Current Branch site

Feedback
Was this page helpful?      Yes     No

Provide product feedback
