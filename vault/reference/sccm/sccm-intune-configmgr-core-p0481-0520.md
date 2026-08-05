---
title: "Core infrastructure documentation — pages 481-520"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0481-0520
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0481-0520
family: sccm
documentKind: "doc"
abstract: "The fallback status point role is an exception. Because this site system role accepts unauthenticated data from clients, don't assign the fallback status point role to any other Configuration Manager site system role. Configure static IP addresses for site systems Static IP addr"
---

# Core infrastructure documentation — pages 481-520

<!-- p.481 -->

  The fallback status point role is an exception. Because this site system role accepts
  unauthenticated data from clients, don't assign the fallback status point role to any
  other Configuration Manager site system role.

Configure static IP addresses for site systems
Static IP addresses are easier to protect from name resolution attacks.

Static IP addresses also make the configuration of IPsec easier. Using IPsec is a security
best practice for securing communication between site systems in Configuration
Manager.

Don't install other applications on site system servers
When you install other applications on site system servers, you increase the attack
surface for Configuration Manager. You also risk incompatibility issues.

Require signing and enable encryption as a site option
Enable the signing and encryption options for the site. Ensure that all clients can support
the SHA-256 hash algorithm, and then enable the option to Require SHA-256.

Restrict and monitor administrative users
Grant administrative access to Configuration Manager only to users that you trust. Then
grant them minimum permissions by using the built-in security roles or by customizing
the security roles. Administrative users who can create, modify, and deploy software and
configurations can potentially control devices in the Configuration Manager hierarchy.

Periodically audit administrative user assignments and their authorization level to verify
required changes.

For more information, see Configure role-based administration.

Secure Configuration Manager backups
When you back up Configuration Manager, this information includes certificates and
other sensitive data that could be used by an attacker for impersonation.

Use SMB signing or IPsec when you transfer this data over the network, and secure the
backup location.

<!-- p.482 -->

Secure locations for exported objects
Whenever you export or import objects from the Configuration Manager console to a
network location, secure the location and secure the network channel.

Restrict who can access the network folder.

To prevent an attacker from tampering with the exported data, use SMB signing or IPsec
between the network location and the site server. Also secure the communication
between the computer that runs the Configuration Manager console and site server. Use
IPsec to encrypt the data on the network to prevent information disclosure.

Manually remove certificates from failed servers
If a site system isn't uninstalled properly, or stops functioning and can't be restored,
manually remove the Configuration Manager certificates for this server from other
Configuration Manager servers.

To remove the peer trust that was originally established with the site system and site
system roles, manually remove the Configuration Manager certificates for the failed
server in the Trusted People certificate store on other site system servers. This action is
important if you reuse the server without reformatting it.

For more information, see Cryptographic controls for server communication.

Don't configure internet-based site systems to bridge the
perimeter network
Don't configure site system servers to be multi-homed so that they connect to the
perimeter network and the intranet. Although this configuration allows internet-based
site systems to accept client connections from the internet and the intranet, it eliminates
a security boundary between the perimeter network and the intranet.

Configure the site server to initiate connections to
perimeter networks
If a site system is on an untrusted network, such as a perimeter network, configure the
site server to initiate connections to the site system.

By default, site systems initiate connections to the site server to transfer data. This
configuration can be a security risk when the connection initiation is from an untrusted
network to the trusted network. When site systems accept connections from the

<!-- p.483 -->

internet, or reside in an untrusted forest, configure the site system option to Require the
site server to initiate connections to this site system. After the installation of the site
system and any roles, all connections are initiated by the site server from the trusted
network.

Use SSL bridging and termination with authentication
If you use a web proxy server for internet-based client management, use SSL bridging to
SSL, by using termination with authentication.

When you configure SSL termination at the proxy web server, packets from the internet
are subject to inspection before they're forwarded to the internal network. The proxy
web server authenticates the connection from the client, terminates it, and then opens a
new authenticated connection to the internet-based site systems.

When Configuration Manager client computers use a proxy web server to connect to
internet-based site systems, the client identity (GUID) is securely contained within the
packet payload. Then the management point doesn't consider the proxy web server to
be the client.

If your proxy web server can't support the requirements for SSL bridging, SSL tunneling
is also supported. This option is less secure. The SSL packets from the internet are
forwarded to the site systems without termination. Then they can't be inspected for
malicious content.

  ２ Warning

  Mobile devices that are enrolled by Configuration Manager can't use SSL bridging.
  They must use SSL tunneling only.

Configurations to use if you configure the site to wake up
computers to install software
     If you use traditional wake-up packets, use unicast rather than subnet-directed
     broadcasts.

     If you must use subnet-directed broadcasts, configure routers to allow IP-directed
     broadcasts only from the site server and only on a non-default port number.

For more information about the different Wake On LAN technologies, see Planning how
to wake up clients.

<!-- p.484 -->

If you use email notification, configure authenticated
access to the SMTP mail server
Whenever possible, use a mail server that supports authenticated access. Use the
computer account of the site server for authentication. If you must specify a user
account for authentication, use an account that has the least privileges.

Enforce LDAP channel binding and LDAP signing
The security of Active Directory domain controllers can be improved by configuring the
server to reject Simple Authentication and Security Layer (SASL) LDAP binds that do not
request signing or to reject LDAP simple binds that are performed on a clear text
connection. Starting in version 1910, Configuration Manager supports enforcing LDAP
channel binding and LDAP signing. For more information, see 2020 LDAP channel
binding and LDAP signing requirements for Windows        .

Security guidance for the site server
Use the following guidance to help you secure the Configuration Manager site server.

  ２ Warning

  Network access account - Don't grant interactive sign-in rights to this account on
  SQL Servers. Don't grant this account the right to join computers to the domain. If
  you must join computers to the domain during a task sequence, use the Task
  sequence domain join account..

Install Configuration Manager on a member server
instead of a domain controller
The Configuration Manager site server and site systems don't require installation on a
domain controller. Domain controllers don't have a local Security Accounts
Management (SAM) database other than the domain database. When you install
Configuration Manager on a member server, you can maintain Configuration Manager
accounts in the local SAM database rather than in the domain database.

This practice also lowers the attack surface on your domain controllers.

<!-- p.485 -->

Install secondary sites without copying the files over the
network
When you run setup and create a secondary site, don't select the option to copy the
files from the parent site to the secondary site. Also don't use a network source location.
When you copy files over the network, a skilled attacker could hijack the secondary site
installation package and tamper with the files before they're installed. Timing this attack
would be difficult. This attack can be mitigated by using IPsec or SMB when you transfer
the files.

Instead of copying the files over the network, on the secondary site server, copy the
source files from media folder to a local folder. Then, when you run setup to create a
secondary site, on the Installation Source Files page, select Use the source files at the
following location on the secondary site computer (most secure), and specify this
folder.

For more information, see Install a secondary site.

Site role installation inherits permissions from drive root
Make sure to properly configure the system drive permissions before you install the first
site system role to any server. For example, C:\SMS_CCM inherits permissions from C:\ . If
the root of the drive isn't properly secured, then low rights users may be able to access
or modify content in the Configuration Manager folder.

Security guidance for SQL Server
Configuration Manager uses SQL Server as the back-end database. If the database is
compromised, attackers could bypass Configuration Manager. If they access SQL Server
directly, they can launch attacks through Configuration Manager. Consider attacks
against SQL Server to be high risk and mitigate appropriately.

Use the following security guidance to help you secure SQL Server for Configuration
Manager.

Don't use the Configuration Manager site database server
to run other SQL Server applications
When you increase the access to the Configuration Manager site database server, this
action increases the risk to your Configuration Manager data. If the Configuration

<!-- p.486 -->

Manager site database is compromised, other applications on the same SQL Server
computer are then also put at risk.

Configure SQL Server to use Windows authentication
Although Configuration Manager accesses the site database by using a Windows
account and Windows authentication, it's still possible to configure SQL Server to use
SQL Server mixed mode. SQL Server mixed mode allows additional SQL Server sign-ins
to access the database. This configuration isn't required and increases the attack surface.

Update SQL Server Express at secondary sites
When you install a primary site, Configuration Manager downloads SQL Server Express
from the Microsoft Download Center. It then copies the files to the primary site server.
When you install a secondary site and select the option that installs SQL Server Express,
Configuration Manager installs the previously downloaded version. It doesn't check
whether new versions are available. To make sure that the secondary site has the latest
versions, do one of the following tasks:

     After you install the secondary site, run Windows Update on the secondary site
     server.

     Before you install the secondary site, manually install SQL Server Express on the
     secondary site server. Make sure that you install the latest version and any
     software updates. Then install the secondary site, and select the option to use an
     existing SQL Server instance.

Periodically run Windows Update for all installed versions of SQL Server. This practice
makes sure that they have the latest software updates.

Follow general guidance for SQL Server
Identify and follow the general guidance for your version of SQL Server. However, take
into consideration the following requirements for Configuration Manager:

     The computer account of the site server must be a member of the Administrators
     group on the computer that runs SQL Server. If you follow the SQL Server
     recommendation of "provision administrator principals explicitly", the account that
     you use to run setup on the site server must be a member of the SQL Server Users
     group.

<!-- p.487 -->

     If you install SQL Server by using a domain user account, make sure that the site
     server computer account is configured for a Service Principal Name (SPN) that's
     published to Active Directory Domain Services. Without the SPN, Kerberos
     authentication fails and Configuration Manager setup fails.

Security guidance for site systems that run IIS
Several site system roles in Configuration Manager require IIS. The process of securing
IIS enables Configuration Manager to operate correctly and reduces the risk of security
attacks. When practical, minimize the number of servers that require IIS. For example,
run only the number of management points that you require to support your client
base, taking into consideration high availability and network isolation for internet-based
client management.

Use the following guidance to help you secure the site systems that run IIS.

Disable IIS functions that you don't require
Install only the minimum IIS features for the site system role that you install. For more
information, see Site and site system prerequisites.

Configure the site system roles to require HTTPS
When clients connect to a site system by using HTTP rather than by using HTTPS, they
use Windows authentication. This behavior might fall back to using NTLM
authentication rather than Kerberos authentication. When NTLM authentication is used,
clients might connect to a rogue server.

The exception to this guidance might be distribution points. Package access accounts
don't work when the distribution point is configured for HTTPS. Package access
accounts provide authorization to the content, so that you can restrict which users can
access the content. For more information, see Security guidance for content
management.

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP client
  communication are deprecated. Configure the site for HTTPS or Enhanced HTTP.
  For more information, see Enable the site for HTTPS-only or enhanced HTTP.

<!-- p.488 -->

Configure a certificate trust list (CTL) in IIS for site system
roles
Site system roles:

     A distribution point that you configure for HTTPS

     A management point that you configure for HTTPS and enable to support mobile
     devices

A CTL is a defined list of trusted root certification authorities (CAs). When you use a CTL
with group policy and a public key infrastructure (PKI) deployment, a CTL enables you to
supplement the existing trusted root CAs that are configured on your network. For
example, CAs that are automatically installed with Microsoft Windows or added through
Windows enterprise root CAs. When a CTL is configured in IIS, it defines a subset of
those trusted root CAs.

This subset provides you with more control over security. The CTL restricts the client
certificates that are accepted to only those certificates that are issued from the list of
CAs in the CTL. For example, Windows comes with a number of well-known, third-party
CA certificates.

By default, the computer that runs IIS trusts certificates that chain to these well-known
CAs. When you don't configure IIS with a CTL for the listed site system roles, the site
accepts as a valid client any device that has a certificate issued from these CAs. If you
configure IIS with a CTL that didn't include these CAs, the site refuses client connections,
if the certificate chains to these CAs. For Configuration Manager clients to be accepted
for the listed site system roles, you must configure IIS with a CTL that specifies the CAs
that are used by Configuration Manager clients.

  ７ Note

  Only the listed site system roles require you to configure a CTL in IIS. The certificate
  issuers list that Configuration Manager uses for management points provides the
  same functionality for client computers when they connect to HTTPS management
  points.

For more information about how to configure a list of trusted CAs in IIS, see the IIS
documentation.

Don't put the site server on a computer with IIS

<!-- p.489 -->

Role separation helps to reduce the attack profile and improve recoverability. The
computer account of the site server typically has administrative privileges on all site
system roles. It may also have these privileges on Configuration Manager clients, if you
use client push installation.

Use dedicated IIS servers for Configuration Manager
Although you can host multiple web-based applications on the IIS servers that are also
used by Configuration Manager, this practice can significantly increase your attack
surface. A poorly configured application could allow an attacker to gain control of a
Configuration Manager site system. This breach could allow an attacker to gain control
of the hierarchy.

If you must run other web-based applications on Configuration Manager site systems,
create a custom web site for Configuration Manager site systems.

Use a custom website
For site systems that run IIS, configure Configuration Manager to use a custom website
instead of the default website. If you have to run other web applications on the site
system, you must use a custom website. This setting is a site-wide setting rather than a
setting for a specific site system.

When you use custom websites, remove the default
virtual directories
When you change from using the default website to using a custom website,
Configuration Manager doesn't remove the old virtual directories. Remove the virtual
directories that Configuration Manager originally created under the default website.

For example, remove the following virtual directories for a distribution point:

     SMS_DP_SMSPKG$

     SMS_DP_SMSSIG$

     NOCERT_SMS_DP_SMSPKG$

     NOCERT_SMS_DP_SMSSIG$

Follow IIS Server security guidance

<!-- p.490 -->

Identify and follow the general guidance for your version of IIS Server. Take into
consideration any requirements that Configuration Manager has for specific site system
roles. For more information, see Site and site system prerequisites.

Configure IIS custom headers
Configure the following custom headers to disable MIME sniffing:

x-content-type-options: nosniff

For more information, see Custom Headers.

If other services use the same IIS instance, make sure these custom headers are
compatible.

Security guidance for the management point
Management points are the primary interface between devices and Configuration
Manager. Consider attacks against the management point and the server that it runs on
to be high risk, and mitigate appropriately. Apply all appropriate security guidance and
monitor for unusual activity.

Use the following guidance to help secure a management point in Configuration
Manager.

Assign the client on a management point to the same site
Avoid the scenario where you assign the Configuration Manager client that's on a
management point to a site other than the management point's site.

If you migrate from an earlier version to Configuration Manager current branch, migrate
the client on the management point to the new site as soon as possible.

Security guidance for the fallback status point
If you install a fallback status point in Configuration Manager, use the following security
guidance:

For more information about the security considerations when you install a fallback
status point, see Determine whether you require a fallback status point.

<!-- p.491 -->

Don't run any other roles on the same site system
The fallback status point is designed to accept unauthenticated communication from
any computer. If you run this site system role with other roles or a domain controller,
the risk to that server greatly increases.

Install the fallback status point before you install clients
with PKI certificates
If Configuration Manager site systems don't accept HTTP client communication, you
might not know that clients are unmanaged because of PKI-related certificate issues. If
you assign clients to a fallback status point, they report these certificate issues through
the fallback status point.

For security reasons, you can't assign a fallback status point to clients after they're
installed. You can only assign this role during client installation.

Avoid using the fallback status point in the perimeter
network
By design, the fallback status point accepts data from any client. Although a fallback
status point in the perimeter network could help you to troubleshoot internet-based
clients, balance the troubleshooting benefits with the risk of a site system that accepts
unauthenticated data in a publicly accessible network.

If you do install the fallback status point in the perimeter network or any untrusted
network, configure the site server to initiate data transfers. Don't use the default setting
that allows the fallback status point to initiate a connection to the site server.

Security issues for site administration
Review the following security issues for Configuration Manager:

     Configuration Manager has no defense against an authorized administrative user
     who uses Configuration Manager to attack the network. Unauthorized
     administrative users are a high security risk. They could launch many attacks, which
     include the following strategies:

        Use software deployment to automatically install and run malicious software on
        every Configuration Manager client computer in the organization.

        Remotely control a Configuration Manager client without client permission.

<!-- p.492 -->

   Configure rapid polling intervals and extreme amounts of inventory. This action
   creates denial of service attacks against the clients and servers.

   Use one site in the hierarchy to write data to another site's Active Directory
   data.

The site hierarchy is the security boundary. Consider sites to be management
boundaries only.

Audit all administrative user activity and routinely review the audit logs. Require all
Configuration Manager administrative users to undergo a background check
before they're hired. Require periodic rechecks as a condition of employment.

If the enrollment point is compromised, an attacker could obtain certificates for
authentication. They could steal the credentials of users who enroll their mobile
devices.

The enrollment point communicates with a CA. It can create, modify, and delete
Active Directory objects. Never install the enrollment point in the perimeter
network. Always monitor for unusual activity.

If you allow user policies for internet-based client management, you increase your
attack profile.

In addition to using PKI certificates for client-to-server connections, these
configurations require Windows authentication. They might fall back to using
NTLM authentication rather than Kerberos. NTLM authentication is vulnerable to
impersonation and replay attacks. To successfully authenticate a user on the
internet, you need to allow a connection from the internet-based site system to a
domain controller.

The Admin$ share is required on site system servers.

The Configuration Manager site server uses the Admin$ share to connect to and
do service operations on site systems. Don't disable or remove this share.

Configuration Manager uses name resolution services to connect to other
computers. These services are hard to secure against the following security attacks:
   Spoofing
   Tampering
   Repudiation
   Information disclosure
   Denial of service
   Elevation of privilege

<!-- p.493 -->

     Identify and follow any security guidance for the version of DNS that you use for
     name resolution.

Privacy information for discovery
Discovery creates records for network resources and stores them in the Configuration
Manager database. Discovery data records contain computer information such as IP
addresses, OS versions, and computer names. You can also configure Active Directory
discovery methods to return any information that your organization stores in Active
Directory Domain Services.

The only discovery method that Configuration Manager enables by default is Heartbeat
Discovery. This method only discovers computers that already have the Configuration
Manager client software installed.

Discovery information isn't directly sent to Microsoft. It's stored in the Configuration
Manager database. Configuration Manager retains information in the database until it
deletes the data. This process happens every 90 days by the site maintenance task
Delete Aged Discovery Data.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.494 -->

Network infrastructure considerations
for Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To prepare your network to support Configuration Manager, you may need to configure
some infrastructure components. For example, open firewall ports to pass the
communications used by Configuration Manager.

Ports and protocols
Different Configuration Manager features use different network ports. Some ports are
required, and some you can customize.

Most Configuration Manager communications use common ports like port 80 for HTTP
or 443 for HTTPS. Some site system roles support the use of custom websites and
custom ports. For more information, see Websites for site system servers.

Before you deploy Configuration Manager, identify the ports that you plan to use, and
set up firewalls as needed.

After you install Configuration Manager, if you need to change a port, don't forget to
update firewalls on devices and the network. Also change the configuration of the port
in Configuration Manager.

For more information, see the following articles:

      How to configure client communication ports
      Ports used in Configuration Manager

Internet access requirements
Some Configuration Manager features rely on internet connectivity for full functionality.
If your organization restricts network communication with the internet using a firewall or
proxy device, make sure to allow the necessary endpoints.

For more information, see Internet access requirements

Proxy servers

<!-- p.495 -->

You can specify separate proxy servers for different site system servers and clients. You
make these configurations when you install a site system role or client, or change them
later as needed.

For more information, see Proxy server support.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.496 -->

Ports used in Configuration Manager
Applies to: Configuration Manager (current branch)

This article lists the network ports that Configuration Manager uses. Some connections use
ports that aren't configurable, and some support custom ports that you specify. If you use any
port filtering technology, verify that the required ports are available. These port filtering
technologies include firewalls, routers, proxy servers, or IPsec.

  ７ Note

  If you support internet-based clients by using SSL bridging, in addition to port
  requirements, you might also have to allow some HTTP verbs and headers to traverse your
  firewall.

Ports you can configure
Configuration Manager enables you to configure the ports for the following types of
communication:

     Enrollment proxy point to enrollment point

     Client-to-site systems that run IIS

     Client to internet (as proxy server settings)

     Software update point to internet (as proxy server settings)

     Software update point to WSUS server

     Site server to site database server

     Site server to WSUS database server

     Reporting services points

        ７ Note

        You configure the ports for the reporting services point in SQL Server Reporting
        Services. Configuration Manager then uses these ports during communications to
        the reporting services point. Be sure to review these ports that define the IP filter
        information for IPsec policies or for configuring firewalls.

<!-- p.497 -->

By default, the HTTP port that's used for client-to-site system communication is port 80, and
443 for HTTPS. You can change these ports during setup or in the site properties.

Non-configurable ports
Configuration Manager doesn't allow you to configure ports for the following types of
communication:

     Site to site

     Site server to site system

     Configuration Manager console to SMS Provider

     Configuration Manager console to the internet

     Connections to cloud services, such as Microsoft Azure

Ports used by clients and site systems
The following sections detail the ports that are used for communication in Configuration
Manager. The arrows in the section title show the direction of the communication:

     --> Indicates that one computer starts communication and the other computer always

     responds

     <--> Indicates that either computer can start communication

Asset Intelligence synchronization point --> Microsoft

                                                                                       ﾉ   Expand table

 Description                                          UDP                        TCP

 HTTPS                                                --                         443

Asset Intelligence synchronization point --> SQL Server

                                                                                       ﾉ   Expand table

 Description                  UDP         TCP

 SQL over TCP                 --          1433 Note 2 Alternate port available

<!-- p.498 -->

Client --> Client
Wake-up proxy also uses ICMP echo request messages from one client to another client.
Clients use this communication to confirm whether the other client is awake on the network.
ICMP is sometimes referred to as ping commands. ICMP doesn't have a UDP or TCP protocol
number, and so it isn't listed in the below table. However, any host-based firewalls on these
client computers or intervening network devices within the subnet must permit ICMP traffic for
wake-up proxy communication to succeed.

                                                                                               ﾉ   Expand table

 Description                                     UDP                                                    TCP

 Wake On LAN                                     9 Note 2 Alternate port available                      --

 Wake-up proxy                                   25536 Note 2 Alternate port available                  --

 Windows PE Peer cache broadcast                 8004                                                   --

 Windows PE Peer cache download                  --                                                     8003

For more information, see Windows PE Peer Cache.

Client --> Configuration Manager Network Device Enrollment
Service (NDES) policy module

                                                                                               ﾉ   Expand table

 Description                                          UDP                                TCP

 HTTP                                                                                    80

 HTTPS                                                --                                 443

Client --> Cloud distribution point

                                                                                               ﾉ   Expand table

 Description                                          UDP                                TCP

 HTTPS                                                --                                 443

For more information, see Ports and data flow.

<!-- p.499 -->

Client --> Cloud management gateway (CMG)

                                                                                         ﾉ   Expand table

 Description                                        UDP                            TCP

 HTTPS                                              --                             443

For more information, see CMG data flow.

Client --> Distribution point, both standard and pull

                                                                                         ﾉ   Expand table

 Description                    UDP         TCP

 HTTP                           --          80 Note 2 Alternate port available

 HTTPS                          --          443 Note 2 Alternate port available

 Express updates                --          8005 Note 2 Alternate port available

  ７ Note

  Use client settings to configure the alternate port for express updates. For more
  information, see Port that clients use to receive requests for delta content.

Client --> Distribution point configured for multicast, both
standard and pull

                                                                                         ﾉ   Expand table

 Description                                                 UDP                               TCP

 Server Message Block (SMB)                                  --                                445

 Multicast protocol                                          63000-64000                       --

Client --> Distribution point configured for PXE, both
standard and pull

<!-- p.500 -->

                                                                                               ﾉ     Expand table

 Description                                                                      UDP                    TCP

 DHCP                                                                             67 and 68              --

 TFTP                                                                             69 Note 4              --

 Boot Information Negotiation Layer (BINL)                                        4011                   --

 DHCPv6 for PXE responder without WDS                                             547                    --

  ） Important

  If you enable a host-based firewall, make sure that the rules allow the server to send and
  receive on these ports. When you enable a distribution point for PXE, Configuration
  Manager can enable the inbound (receive) rules on the Windows Firewall. It doesn't
  configure the outbound (send) rules.

Client --> Fallback status point

                                                                                               ﾉ     Expand table

 Description                   UDP           TCP

 HTTP                          --            80 Note 2 Alternate port available

Client --> Global catalog domain controller
A Configuration Manager client doesn't contact a global catalog server when it's a workgroup
computer or when it's configured for internet-only communication.

                                                                                               ﾉ     Expand table

 Description                                                         UDP                      TCP

 Global catalog LDAP                                                 --                       3268

Client --> Management point

                                                                                               ﾉ     Expand table

<!-- p.501 -->

 Description                                                                  UDP        TCP

 Client notification (default communication before falling back to HTTP       --         10123 Note 2 Alternate port
 or HTTPS)                                                                               available

 HTTP                                                                         --         80 Note 2 Alternate port
                                                                                         available

 HTTPS                                                                        --         443 Note 2 Alternate port
                                                                                         available

Client --> Software update point

                                                                                                     ﾉ   Expand table

 Description                           UDP               TCP

 HTTP                                  --                80 or 8530 Note 3

 HTTPS                                 --                443 or 8531 Note 3

Client --> State migration point

                                                                                                     ﾉ   Expand table

 Description                                      UDP          TCP

 HTTP                                             --           80 Note 2 Alternate port available

 HTTPS                                            --           443 Note 2 Alternate port available

 Server Message Block (SMB)                       --           445

CMG connection point --> CMG virtual machine scale set
Configuration Manager uses these connections to build the CMG channel. For more
information, see CMG data flow.

                                                                                                     ﾉ   Expand table

 Description                                                 UDP                   TCP

 HTTPS (one VM)                                              --                    443

 HTTPS (two or more VMs)                                     --                    10124-10139

<!-- p.502 -->

CMG connection point --> CMG classic cloud service
Configuration Manager uses these connections to build the CMG channel. For more
information, see CMG data flow.

                                                                                 ﾉ   Expand table

 Description                                                UDP           TCP

 TCP-TLS (preferred)                                        --            10140-10155

 HTTPS (fallback with one VM)                               --            443

 HTTPS (fallback with two or more VMs)                      --            10124-10139

CMG connection point --> Management point

                                                                                 ﾉ   Expand table

 Description                                     UDP                       TCP

 HTTPS                                           --                        443

 HTTP                                            --                        80

The specific port required depends upon the management point configuration. For more
information, see CMG data flow.

CMG connection point --> Software update point
The specific port depends upon the software update point configuration.

                                                                                 ﾉ   Expand table

 Description                               UDP               TCP

 HTTPS                                     --                443/8531

 HTTP                                      --                80/8530

For more information, see CMG data flow.

Configuration Manager console --> Client

<!-- p.503 -->

                                                                                                ﾉ    Expand table

 Description                                                                        UDP              TCP

 Remote Control (control)                                                           --               2701

 Remote Assistance (RDP and RTC)                                                    --               3389

Configuration Manager console --> internet

                                                                                                ﾉ    Expand table

 Description                                              UDP                             TCP

 HTTP                                                     --                              80

 HTTPS                                                    --                              443

The Configuration Manager console uses internet access for the following actions:

     Downloading software updates from Microsoft Update for deployment packages.
     The Feedback item in the ribbon.
     Links to documentation within the console.
     Downloading items from Community hub

Configuration Manager console --> Reporting services point

                                                                                                ﾉ    Expand table

 Description                   UDP            TCP

 HTTP                          --             80 Note 2 Alternate port available

 HTTPS                         --             443 Note 2 Alternate port available

Configuration Manager console --> Site server

                                                                                                ﾉ    Expand table

 Description                                                                                    UDP         TCP

 RPC (initial connection to WMI to locate provider system)                                      --          135

<!-- p.504 -->

Configuration Manager console --> SMS Provider

                                                                                         ﾉ   Expand table

 Description                                        UDP                 TCP

 RPC Endpoint Mapper                                135                 135

 RPC                                                --                  DYNAMIC Note 6

 HTTPS                                              --                  443 *Note

Note for administration service
Any device that makes a call to the administration service on the SMS Provider uses HTTPS
port 443. For more information, see What is the administration service?

Configuration Manager Network Device Enrollment Service
(NDES) policy module --> Certificate registration point

                                                                                         ﾉ   Expand table

 Description                 UDP           TCP

 HTTPS                       --            443 Note 2 Alternate port available

Data warehouse service point --> SQL Server

                                                                                         ﾉ   Expand table

 Description                  UDP          TCP

 SQL over TCP                 --           1433 Note 2 Alternate port available

Distribution point, both standard and pull --> Management
point
A distribution point communicates to the management point in the following scenarios:

       To report the status of prestaged content

       To report usage summary data

<!-- p.505 -->

    To report content validation

    To report the status of package downloads, only for pull-distribution points

                                                                                     ﾉ   Expand table

Description                UDP          TCP

HTTP                       --           80 Note 2 Alternate port available

HTTPS                      --           443 Note 2 Alternate port available

Endpoint Protection point --> internet

                                                                                     ﾉ   Expand table

Description                                         UDP                        TCP

HTTP                                                --                         80

Endpoint Protection point --> SQL Server

                                                                                     ﾉ   Expand table

Description                 UDP         TCP

SQL over TCP                --          1433 Note 2 Alternate port available

Enrollment proxy point --> Enrollment point

                                                                                     ﾉ   Expand table

Description                UDP          TCP

HTTPS                      --           443 Note 2 Alternate port available

Enrollment point --> SQL Server

                                                                                     ﾉ   Expand table

<!-- p.506 -->

Description                    UDP             TCP

SQL over TCP                   --              1433 Note 2 Alternate port available

Exchange Server Connector --> Exchange Online

                                                                                             ﾉ   Expand table

Description                                                                           UDP          TCP

Windows Remote Management over HTTPS                                                  --           5986

Exchange Server Connector --> On-premises Exchange Server

                                                                                             ﾉ   Expand table

Description                                                                           UDP          TCP

Windows Remote Management over HTTP                                                   --           5985

Mac computer --> Enrollment proxy point

                                                                                             ﾉ   Expand table

Description                                                UDP                         TCP

HTTPS                                                      --                          443

Management point --> Domain controller

                                                                                             ﾉ   Expand table

Description                                                                  UDP      TCP

Lightweight Directory Access Protocol (LDAP)                                 389      389

Secure LDAP (LDAPS, for signing and binding)                                 636      636

Global catalog LDAP                                                          --       3268

RPC Endpoint Mapper                                                          --       135

RPC                                                                          --       DYNAMIC Note 6

<!-- p.507 -->

Management point <--> Site server
Note 5

                                                                                          ﾉ   Expand table

 Description                                              UDP              TCP

 RPC Endpoint mapper                                      --               135

 RPC                                                      --               DYNAMIC Note 6

 Server Message Block (SMB)                               --               445

Management point --> SQL Server

                                                                                          ﾉ   Expand table

 Description                  UDP        TCP

 SQL over TCP                 --         1433 Note 2 Alternate port available

Mobile device --> Enrollment proxy point

                                                                                          ﾉ   Expand table

 Description                                         UDP                            TCP

 HTTPS                                               --                             443

Pull-Distribution point --> Distribution point configured as
source

                                                                                          ﾉ   Expand table

 Description                       UDP      TCP

 HTTP                              --       80 Note 2 Alternate port available

 HTTPS                             --       443 Note 2 Alternate port available

 Express updates                   --       8005 Note 2 Alternate port available

<!-- p.508 -->

Reporting Services point --> SQL Server

                                                                                            ﾉ   Expand table

 Description                       UDP    TCP

 SQL over TCP                      --     1433 Note 2 Alternate port available

Service connection point --> Azure (CMG)

                                                                                            ﾉ   Expand table

 Description                                                                          UDP         TCP

 HTTPS for CMG service deployment                                                     --          443

For more information, see CMG data flow.

Service connection point --> Azure Logic App

                                                                                            ﾉ   Expand table

 Description                                                                     UDP            TCP

 HTTPS for external notification                                                 --             443

For more information, see External notifications.

Service connection point --> SQL Server

                                                                                            ﾉ   Expand table

 Description                       UDP    TCP

 SQL over TCP                      --     1433 Note 2 Alternate port available

Site server <--> Asset Intelligence synchronization point

                                                                                            ﾉ   Expand table

<!-- p.509 -->

 Description                                                   UDP   TCP

 Server Message Block (SMB)                                    --    445

 RPC Endpoint Mapper                                           135   135

 RPC                                                           --    DYNAMIC Note 6

Site server --> Client

                                                                                    ﾉ   Expand table

 Description                    UDP                                                      TCP

 Wake On LAN                    9 Note 2 Alternate port available                        --

Site server --> Cloud distribution point

                                                                                    ﾉ   Expand table

 Description                                              UDP                 TCP

 HTTPS                                                    --                  443

For more information, see Ports and data flow.

Site server --> Distribution point, both standard and pull
Note 5

                                                                                    ﾉ   Expand table

 Description                                                   UDP   TCP

 Server Message Block (SMB)                                    --    445

 RPC Endpoint Mapper                                           135   135

 RPC                                                           --    DYNAMIC Note 6

Site server --> Domain controller

                                                                                    ﾉ   Expand table

<!-- p.510 -->

Description                                          UDP         TCP

Lightweight Directory Access Protocol (LDAP)         389         389

Secure LDAP (LDAPS, for signing and binding)         636         636

Global catalog LDAP                                  --          3268

RPC Endpoint Mapper                                  --          135

RPC                                                  --          DYNAMIC Note 6

Site server <--> Certificate registration point

                                                                        ﾉ   Expand table

Description                                    UDP        TCP

Server Message Block (SMB)                     --         445

RPC Endpoint Mapper                            135        135

RPC                                            --         DYNAMIC Note 6

Site server <--> CMG connection point

                                                                        ﾉ   Expand table

Description                                    UDP        TCP

Server Message Block (SMB)                     --         445

RPC Endpoint Mapper                            135        135

RPC                                            --         DYNAMIC Note 6

Site server <--> Endpoint Protection point

                                                                        ﾉ   Expand table

Description                                    UDP        TCP

Server Message Block (SMB)                     --         445

RPC Endpoint Mapper                            135        135

<!-- p.511 -->

 Description                        UDP   TCP

 RPC                                --    DYNAMIC Note 6

Site server <--> Enrollment point

                                                       ﾉ   Expand table

 Description                        UDP   TCP

 Server Message Block (SMB)         --    445

 RPC Endpoint Mapper                135   135

 RPC                                --    DYNAMIC Note 6

Site server <--> Enrollment proxy point

                                                       ﾉ   Expand table

 Description                        UDP   TCP

 Server Message Block (SMB)         --    445

 RPC Endpoint Mapper                135   135

 RPC                                --    DYNAMIC Note 6

Site server <--> Fallback status point
Note 5

                                                       ﾉ   Expand table

 Description                        UDP   TCP

 Server Message Block (SMB)         --    445

 RPC Endpoint Mapper                135   135

 RPC                                --    DYNAMIC Note 6

Site server --> internet

<!-- p.512 -->

                                                                                    ﾉ   Expand table

 Description                                   UDP                      TCP

 HTTP                                          --                       80 Note 1

 HTTPS                                         --                       443

Site server <--> Issuing certification authority (CA)
This communication is used when you deploy certificate profiles by using the certificate
registration point. The communication isn't used for every site server in the hierarchy. Instead,
it's used only for the site server at the top of the hierarchy.

                                                                                    ﾉ   Expand table

 Description                                        UDP           TCP

 RPC Endpoint Mapper                                135           135

 RPC (DCOM)                                         --            DYNAMIC Note 6

Site server --> Server hosting remote content library share
You can move the content library to another storage location to free up hard drive space on
your central administration or primary site servers. For more information, see Configure a
remote content library for the site server.

                                                                                    ﾉ   Expand table

 Description                                                             UDP            TCP

 Server Message Block (SMB)                                              --             445

Site server <--> Service connection point

                                                                                    ﾉ   Expand table

 Description                                              UDP           TCP

 Server Message Block (SMB)                               --            445

 RPC Endpoint Mapper                                      135           135

<!-- p.513 -->

 Description                                              UDP              TCP

 RPC                                                      --               DYNAMIC Note 6

Site server <--> Reporting services point
Note 5

                                                                                        ﾉ   Expand table

 Description                                              UDP              TCP

 Server Message Block (SMB)                               --               445

 RPC Endpoint Mapper                                      135              135

 RPC                                                      --               DYNAMIC Note 6

Site server <--> Site server

                                                                                        ﾉ   Expand table

 Description                                                                 UDP            TCP

 Server Message Block (SMB)                                                  --             445

Site server --> SQL Server

                                                                                        ﾉ   Expand table

 Description                  UDP         TCP

 SQL over TCP                 --          1433 Note 2 Alternate port available

During the installation of a site that uses a remote SQL Server to host the site database, open
the following ports between the site server and the SQL Server:

                                                                                        ﾉ   Expand table

 Description                                              UDP              TCP

 Server Message Block (SMB)                               --               445

 RPC Endpoint Mapper                                      135              135

<!-- p.514 -->

 Description                                          UDP            TCP

 RPC                                                  --             DYNAMIC Note 6

Site server --> SQL Server for WSUS

                                                                                      ﾉ   Expand table

 Description                  UDP   TCP

 SQL over TCP                 --    1433 Note 3 Alternate port available

Site server --> SMS Provider

                                                                                      ﾉ   Expand table

 Description                                          UDP            TCP

 Server Message Block (SMB)                           --             445

 RPC Endpoint Mapper                                  135            135

 RPC                                                  --             DYNAMIC Note 6

Site server <--> Software update point
Note 5

                                                                                      ﾉ   Expand table

 Description                                     UDP              TCP

 Server Message Block (SMB)                      --               445

 RPC Endpoint Mapper                             135              135

 RPC                                             --               DYNAMIC Note 6

 HTTP                                            --               80 or 8530 Note 3

 HTTPS                                           --               443 or 8531 Note 3

Site server <--> State migration point

<!-- p.515 -->

Note 5

                                                                                           ﾉ   Expand table

 Description                                                                     UDP           TCP

 Server Message Block (SMB)                                                      --            445

 RPC Endpoint Mapper                                                             135           135

SMS Provider --> SQL Server

                                                                                           ﾉ   Expand table

 Description                   UDP            TCP

 SQL over TCP                  --             1433 Note 2 Alternate port available

Software update point --> internet

                                                                                           ﾉ   Expand table

 Description                                     UDP                           TCP

 HTTP                                            --                            80 Note 1

Software update point --> Upstream WSUS server

                                                                                           ﾉ   Expand table

 Description                         UDP                  TCP

 HTTP                                --                   80 or 8530 Note 3

 HTTPS                               --                   443 or 8531 Note 3

SQL Server --> SQL Server
Intersite database replication requires the SQL Server at one site to communicate directly with
the SQL Server at its parent or child site.

                                                                                           ﾉ   Expand table

<!-- p.516 -->

 Description                               UDP           TCP

 SQL Server service                        --            1433 Note 2 Alternate port available

 SQL Server Service Broker                 --            4022 Note 2 Alternate port available

 SQL Server Browser                        --            1434

   Tip

  Configuration Manager requires the SQL Browser service when using a named instance
  and non-default SQL port.

State migration point --> SQL Server

                                                                                                ﾉ   Expand table

 Description                  UDP          TCP

 SQL over TCP                 --           1433 Note 2 Alternate port available

Notes for ports used by clients and site systems

Note 1: Proxy server port

This port can't be configured but can be routed through a configured proxy server.

Note 2: Alternate port available
You can define an alternate port in Configuration Manager for this value. If you define a
custom port, use that custom port in the IP filter information for IPsec policies or to configure
firewalls.

Note 3: Windows Server Update Services (WSUS)
Since Windows Server 2012, by default WSUS uses port 8530 for HTTP and port 8531 for
HTTPS.

After installation, you can change the port. You don't have to use the same port number
throughout the site hierarchy.

<!-- p.517 -->

      If the HTTP port is 80, the HTTPS port must be 443.

      If the HTTP port is anything else, the HTTPS port must be 1 or higher, for example, 8530
      and 8531.

        ７ Note

        When you configure the software update point to use HTTPS, the HTTP port must
        also be open. Unencrypted data, such as the EULA for specific updates, uses the
        HTTP port.

      The site server makes a connection to the SQL Server hosting the SUSDB when you
      enable the following options for WSUS cleanup:
         Add non-clustered indexes to the WSUS database to improve WSUS cleanup
         performance
         Remove obsolete updates from the WSUS database

If you change the default SQL Server port to an alternate port with SQL Server Configuration
Manager, make sure the site server can connect using the defined port. Configuration Manager
doesn't support dynamic ports. By default, SQL Server named instances use dynamic ports for
connections to the database engine. When you use a named instance, manually configure the
static port.

Note 4: Trivial FTP (TFTP) Daemon

The Trivial FTP (TFTP) Daemon system service doesn't require a user name or password and is
an integral part of Windows Deployment Services (WDS). The Trivial FTP Daemon service
implements support for the TFTP protocol that's defined by the following RFCs:

      RFC 1350: TFTP

      RFC 2347: Option extension

      RFC 2348: Block size option

      RFC 2349: Time-out interval and transfer size options

TFTP is designed to support diskless boot environments. TFTP Daemons listen on UDP port 69
but respond from a dynamically allocated high port. If you enable this port, the TFTP service
can receive incoming TFTP requests, but the selected server can't respond to those requests.
You can't enable the selected server to respond to inbound TFTP requests unless you configure
the TFTP server to respond from port 69.

<!-- p.518 -->

The PXE-enabled distribution point and the client in Windows PE select dynamically allocated
high ports for TFTP transfers. These ports are defined by Microsoft between 49152 and 65535.
For more information, see Service overview and network port requirements for Windows.

However, during the actual PXE boot, the network card on the device selects the dynamically
allocated high port it uses during the TFTP transfer. The network card on the device isn't bound
to the dynamically allocated high ports defined by Microsoft. It's only bound to the ports
defined in RFC 1350. This port can be any from 0 to 65535. For more information about what
dynamically allocated high ports the network card uses, contact the device hardware
manufacturer.

Note 5: Communication between the site server and site systems

By default, communication between the site server and site systems is bi-directional. The site
server starts communication to configure the site system, and then most site systems connect
back to the site server to send status information. Reporting service points and distribution
points don't send status information. If you select Require the site server to initiate
connections to this site system on the site system properties after the site system has been
installed, the site system won't start communication with the site server. Instead, the site server
starts the communication. It uses the site system installation account for authentication to the
site system server.

Note 6: Dynamic ports
Dynamic ports use a range of port numbers that's defined by the OS version. These ports are
also known as ephemeral ports. For more information about the default port ranges, see
Service overview and network port requirements for Windows.

Other ports
The following sections provide more information about ports that Configuration Manager uses.

Client to server shares
Clients use Server Message Block (SMB) whenever they connect to UNC shares. For example:

     Manual client installation that specifies the CCMSetup.exe /source: command-line
     property

     Endpoint Protection clients that download definition files from a UNC path

<!-- p.519 -->

                                                                                ﾉ   Expand table

 Description                                                       UDP              TCP

 Server Message Block (SMB)                                        --               445

Connections to SQL Server
For communication to the SQL Server database engine and for intersite replication, you can use
the default SQL Server port or specify custom ports:

     Intersite communications use:

        SQL Server Service Broker, which defaults to port TCP 4022.

        SQL Server service, which defaults to port TCP 1433.

     Intrasite communication between the SQL Server database engine and various
     Configuration Manager site system roles defaults to port TCP 1433.

     Configuration Manager uses the same ports and protocols to communicate with each
     SQL Server Always On availability group replica that hosts the site database as if the
     replica was a standalone SQL Server instance.

When you use Azure and the site database is behind an internal or external load balancer,
configure the following components:

     Firewall exceptions on each replica
     Load-balancing rules

Configure the following ports:

     SQL over TCP: TCP 1433
     SQL Server Service Broker: TCP 4022
     Server Message Block (SMB): TCP 445
     RPC Endpoint Mapper: TCP 135

  ２ Warning

  Configuration Manager doesn't support dynamic ports. By default, SQL Server named
  instances use dynamic ports for connections to the database engine. When you use a
  named instance, manually configure the static port for intrasite communication.

The following site system roles communicate directly with the SQL Server database:

<!-- p.520 -->

     Certificate registration point role

     Enrollment point role

     Management point

     Site server

     Reporting Services point

     SMS Provider

     SQL Server --> SQL Server

When a SQL Server hosts a database from more than one site, each database must use a
separate instance of SQL Server. Configure each instance with a unique set of ports.

If you enable a host-based firewall on the SQL Server, configure it to allow the correct ports.
Also configure network firewalls in between computers that communicate with the SQL Server.

For an example of how to configure SQL Server to use a specific port, see Configure a server to
listen on a specific TCP port.

Discovery and publishing
Configuration Manager uses the following ports for the discovery and publishing of site
information:

     Lightweight Directory Access Protocol (LDAP): 389
     Secure LDAP (LDAPS, for signing and binding): 636
     Global catalog LDAP: 3268
     RPC Endpoint Mapper: 135
     RPC: Dynamically allocated high TCP ports
     TCP: 1024: 5000
     TCP: 49152: 65535

External connections made by Configuration Manager
On-premises Configuration Manager clients or site systems can make the following external
connections:

     Asset Intelligence synchronization point --> Microsoft

     Endpoint Protection point --> internet
