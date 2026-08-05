---
title: "Core infrastructure documentation — pages 2081-2120"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2081-2120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2081-2120
family: sccm
documentKind: "doc"
abstract: "Component Description Task Scheduler Required for client operations, such as regularly evaluating the health of the Configuration Manager client. Remote Differential Required to optimize data transmission over the network. Compression (RDC) SHA-2 code signing support Clients req"
---

# Core infrastructure documentation — pages 2081-2120

<!-- p.2081 -->

 Component                    Description

 Task Scheduler               Required for client operations, such as regularly evaluating the
                              health of the Configuration Manager client.

 Remote Differential          Required to optimize data transmission over the network.
 Compression (RDC)

 SHA-2 code signing support   Clients require support for the SHA-2 code signing algorithm. For
                              more information, see SHA-2 code signing support.

SHA-2 code signing support
Because of weaknesses in the SHA-1 algorithm and to align to industry standards,
Microsoft now only signs Configuration Manager binaries using the more secure SHA-2
algorithm. Legacy Windows OS versions require an update for SHA-2 code signing
support. For more information, see 2019 SHA-2 code signing support requirement for
Windows and WSUS .

If you don't update these OS versions, you can't install a supported version of the
Configuration Manager current branch client. This behavior applies to either a new client
install or updating it from a previous version.

If you need to manage a client on a version of Windows that's not updated, or older
than the versions listed above, use the Configuration Manager extended interoperability
client (EIC) version 1902. For more information, see Extended interoperability client.

   Tip

  If you don't use automatic client update, and update clients with another
  mechanism, make sure to update the version of ccmsetup. An older version of
  ccmsetup may not properly validate the new SHA-2 code signing certificate on
  client binaries. For example, if you copy ccmsetup.exe to a file share, or use
  ccmsetup.msi with group policy.

  The following client update mechanisms aren't affected:

        Client push installation: It uses the client package from the site.
        Software update-based installation: The site update republishes to WSUS.
        Intune MDM-managed Windows devices: The supported version for this
        mechanism already supports SHA-2 code signing, but it's still important to
        use the latest ccmsetup.msi.

<!-- p.2082 -->

Components automatically downloaded during
installation
The Configuration Manager client has external dependencies. These dependencies
depend on the OS version and the installed software on the client computer. If the client
requires these dependencies to complete the installation, it automatically installs them.

                                                                                ﾉ   Expand table

 Component                                                Description

 Microsoft Visual C++ 2015-2019 Redistributable version   (Version 2107 and later) Required to
 14.28.29914.0 ( vcredist_x*.exe )                        support client operations. When you
                                                          install this update on client computers,
                                                          it might require a restart to complete
                                                          the installation.

 Microsoft Visual C++ 2013 Redistributable version        (Version 2103 and earlier) Required to
 12.0.40660.0 ( vcredist_x*.exe )                         support client operations. When you
                                                          install this update on client computers,
                                                          it might require a restart to complete
                                                          the installation.

 Windows Imaging APIs 6.0.6001.18000 or later             Required to allow Configuration
 ( wimgapi.msi )                                          Manager to manage Windows image
                                                          (.wim) files.

 Microsoft Policy Platform 1.2.3514.0 or later            Required to allow clients to evaluate
 ( MicrosoftPolicyPlatformSetup.msi )                     compliance settings.

 Microsoft .NET Framework version 4.6.2 or later          Version 2107 and later: Required to
 ( NDP462-KB3151800-x86-x64-AllOS-ENU.exe )               support client operations.
                                                          Automatically installed on the
                                                          computer if it doesn't have this version
                                                          installed. For more information, see
                                                          More details about Microsoft .NET.

 Microsoft .NET Framework version 4.5.2 or later          Version 2103 and earlier: Required to
 ( NDP452-KB2901907-x86-x64-AllOS-ENU.exe )               support client operations.
                                                          Automatically installed on the
                                                          computer if it doesn't have this version
                                                          installed. For more information, see
                                                          More details about Microsoft .NET.

 Microsoft .NET Framework version 3.5                     Version 2309 and later: Required to
 ( dotNetFx35setup.exe )                                  support arm64 software update
                                                          deployment. Install on the computer if
                                                          it doesn't have this version installed.

<!-- p.2083 -->

 Component                                             Description

                                                       For more information, see More details
                                                       about Microsoft .NET.

 Microsoft Monitoring Agent version 10.20.18053.0      Installed as needed by devices that you
 ( MMASetup-*.exe )                                    onboard to Microsoft Defender for
                                                       Endpoint.

 Windows Firewall configuration                        Required for certain endpoint
 ( WindowsFirewallConfigurationProvider.msi )          protection policies.

 Microsoft WebView2                                    Installed as needed when you use
 ( Microsoft.WebView2.FixedVersionRuntime.x86.cab )    Software Center custom tabs.

  ７ Note

  Starting in version 2107, the Configuration Manager client no longer has an
  external dependency on Microsoft SQL Server Compact Edition (CE) 4.0 SP1. It now
  uses a built-in version of this component to store information related to client
  operations.

More details about Microsoft .NET

When you install or update the Configuration Manager client, if the device doesn't have
at least the required version of the .NET Framework, CCMSetup installs it. Starting in
version 2107, the minimum required version is 4.6.2.

Microsoft recommends that you install the latest version of .NET version 4.8 to get the
latest performance and security improvements. CCMSetup doesn't automatically install
.NET version 4.8. A later version of Configuration Manager will require .NET version 4.8.

  ７ Note

  .NET Framework version 4.6.2 is preinstalled with Windows Server 2016 and
  Windows 10 version 1607. Later versions of Windows are preinstalled with a later
  version of the .NET Framework.

  .NET Framework version 4.8 isn't supported on some OS versions, such as Windows
  10 2015 LTSB.

  .Net Framework version 3.5 isn't installed on arm64 versions.

  For more information, see .NET Framework system requirements.

<!-- p.2084 -->

Whether you update .NET before updating the Configuration Manager client, or
CCMSetup updates it, .NET may require a restart to complete its installation. CCMSetup
suppresses a restart if necessary. The user sees a Restart required notice in the Windows
notification area.

  ） Important

  When the Configuration Manager client updates to version 2111 or later, client
  notifications are dependent upon .NET 4.6.2 or later. Until you update .NET to
  version 4.6.2 or later, and restart the device, users won't see notifications from
  Configuration Manager. Other client-side functionality may be affected until the
  device is updated and restarted.

The following scenarios are common reasons why .NET requires the computer to restart:

     .NET applications or services are running on the computer.

     One or more software updates required for .NET installation are missing.

     The computer is pending a restart from prior installation of .NET framework
     software updates.

After .NET Framework is installed, it may require other updates. These updates may also
require the computer to restart.

If you need to manage the device restarts before you update the Configuration
Manager client, use the following recommended process:

   1. Install the latest baseline .NET version. For example, starting in version 2107, install
     .NET version 4.8.
   2. Restart the device.
   3. Scan for software updates and install the latest .NET cumulative update.
   4. Restart the device.
   5. Install the latest Configuration Manager client version.

Known issue with .NET version 4.6.2 on Windows Server 2008 SP2

The release of .NET version 4.6.2 that Configuration Manager redistributes doesn't install
on Windows Server 2008 SP2. This version of the OS is covered under the Extended
Security Updates (ESU) program. While products under this program are no longer
supported for use with Configuration Manager, you can use the latest released version of
Configuration Manager current branch to deploy and install Windows security updates
released under the ESU program.

<!-- p.2085 -->

Microsoft recommends updating the OS to a later version that's fully supported. If your
business requirements necessitate use of this OS version, download the latest release of
.NET version 4.6.2 published on 6/23/2021 or later. For more information, see The .NET
Framework 4.6.2 offline installer for Windows         . This .NET release does install on Server
2008 SP2. Manually update .NET on devices with this OS version before you update the
Configuration Manager client to version 2107.

Configuration Manager dependencies
For more information, see Determine the site system roles for clients.

                                                                                  ﾉ    Expand table

 Component         Description

 Management        To deploy the Configuration Manager client, you don't require a management
 point             point. Clients require a management point to transfer information with the site.
                   Without a management point, you can't manage client computers.

 Distribution      The distribution point is an optional, but recommended site system role for
 point             client deployment and management. All distribution points host the client
                   source files. Clients find the nearest distribution point from which to download
                   the source files during client deployment or update. If the site doesn't have a
                   distribution point, computers download the client source files from their
                   management point.

 Fallback status   The fallback status point is an optional, but recommended site system role for
 point             client deployment. The fallback status point tracks client deployment and
                   enables computers in the Configuration Manager site to send state messages
                   when they can't communicate with a management point.

 Reporting         The reporting services point is an optional, but recommended site system role. It
 services point    displays reports related to client deployment and management. For more
                   information, see Introduction to reporting.

Installation method dependencies
The following prerequisites are specific to the various methods of client installation.

Client push installation
     The site uses client push installation accounts to connect to computers to install
     the client. Specify these accounts on the Accounts tab of the Client Push

<!-- p.2086 -->

     Installation Properties. The account must be a member of the local Administrators
     group on the destination computer.

     If you don't specify a client push installation account, the site server uses its
     computer account.

     The site needs to discover the computer on which you're installing the client. At
     least one Configuration Manager discovery method is needed.

     The computer has an ADMIN$ share.

     To automatically push the Configuration Manager client to discovered resources,
     select the option to Enable client push installation to assigned resources in the
     Client Push Installation Properties.

     The client computer needs to communicate with a distribution point or a
     management point to download the source files.

     When you require Kerberos mutual authentication, clients must be in a trusted
     Active Directory forest. Kerberos in Windows relies upon Active Directory for
     mutual authentication.

To use client push, you need the following security permissions:

     To configure the client push installation account: Modify and Read permission for
     the Site object.

     To use client push to install the client to collections, devices and queries: Modify
     Resource and Read permission for the Collection object.

The Infrastructure Administrator default security role includes the required permissions
to manage client push installations.

Software update point-based installation
     If you haven't extended the Active Directory schema, or you're installing clients
     from another forest, use group policy to provision installation parameters for
     CCMSetup.exe. For more information, see How to provision client installation
     properties.

     Publish the Configuration Manager client to the software update point.

     To download the source files, the client computer needs to communicate with a
     distribution point or a management point.

<!-- p.2087 -->

For the security permissions required to manage Configuration Manager software
updates, see Prerequisites for software updates.

Group policy-based installation
     If you haven't extended the Active Directory schema, or you're installing clients
     from another forest, use group policy to provision installation parameters for
     CCMSetup.exe. For more information, see How to provision client installation
     properties.

     To download the source files, the client computer needs to communicate with a
     distribution point or a management point.

Logon script-based installation
To download the source files, the client computer needs to communicate with a
distribution point or a management point. Unless you specified CCMSetup.exe with the
following command-line parameter: ccmsetup /source

Manual installation
To download the source files, the client computer needs to communicate with a
distribution point or a management point. Unless you specified CCMSetup.exe with the
following command-line parameter: ccmsetup /source

Microsoft Intune MDM installation
     Requires a Microsoft Intune subscription and appropriate licenses.

     Requires the device has internet access, even if it isn't internet-based.

     Depending upon the use case, you may also require one or both of the following
     technologies:

        Microsoft Entra ID

        Cloud management gateway

Workgroup computer installation
To access resources in the Configuration Manager site server's domain, configure a
network access account for the site.

<!-- p.2088 -->

For more information about how to configure the network access account, see the
Fundamental concepts for content management.

Software distribution-based installation (for upgrades
only)
      If you haven't extended the Active Directory schema, or you're installing clients
      from another forest, use group policy to provision installation parameters for
      CCMSetup.exe. For more information, see How to provision client installation
      properties.

      To download the source files, the client computer needs to communicate with a
      distribution point or a management point.

For the security permissions required to upgrade the Configuration Manager client
using application management, see Security and privacy for application management.

Automatic client upgrades
You must be a member of the Full Administrator security role to configure automatic
client upgrades.

Firewall requirements
If there's a firewall between the site system servers and the computers onto which you
want to install the Configuration Manager client, see Windows Firewall and port settings
for clients.

Next steps
Windows firewall and port settings for clients

Prerequisites for deploying clients to mobile devices

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2089 -->

Prerequisites for deploying clients to
mobile devices in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  On-premises MDM and the Configuration Manager client for macOS are both
  deprecated.

  Migrate management of macOS and mobile devices to Microsoft Intune. For more
  information, see Supported clients and devices.

Deploying Configuration Manager clients in your environment has the following external
dependencies and dependencies within the product.

For more information on the minimum hardware and OS requirements for the
Configuration Manager client, see Supported configurations.

  ７ Note

  The software version numbers shown in this article only list the minimum version
  numbers required.

When you install the Configuration Manager client on mobile devices and enroll them,
use this information to determine the prerequisites.

Dependencies external to Configuration
Manager
      A Microsoft enterprise certification authority (CA) with certificate templates to
      deploy and manage the certificates required for mobile devices.

      The issuing CA must automatically approve certificate requests from the mobile
      device users during the enrollment process.

<!-- p.2090 -->

     For more information about the certificate requirements, see Security and privacy
     for certificate profiles.

     A security group that contains the users that can enroll their mobile devices.

     This security group is used to configure the certificate template that is used during
     mobile device enrollment.

     Optional but recommended: a DNS alias (CNAME record) named ConfigMgrEnroll.
     Configure this alias for the server name of the enrollment proxy point.

     This DNS alias is required to support automatic discovery for the enrollment
     service. If you don't configure this DNS record, users must manually specify the
     name of the enrollment proxy point as part of the enrollment process.

     Site system role dependencies for the computers that run the enrollment point and
     the enrollment proxy point.

     For more information, see Supported operating systems for site system servers.

Configuration Manager dependencies
For more information, see Determine the site system roles for clients.

     Management point configurations:
        HTTPS client connections
        Enabled for mobile devices
        An internet FQDN
        Accept client connections from the internet

     Enrollment point and enrollment proxy point

     An enrollment proxy point manages enrollment requests from mobile devices and
     the enrollment point completes the enrollment process. The enrollment point must
     be in the same Active Directory forest as the site server, but the enrollment proxy
     point can be in another forest.

     Client settings for mobile device enrollment

     Configure client settings to allow users to enroll mobile devices and configure at
     least one enrollment profile.

     Reporting services point

<!-- p.2091 -->

     The reporting services point is an optional, but recommended site system role. It
     can display reports related to mobile device enrollment and client management.
     For more information, see Introduction to reporting.

     To configure enrollment for mobile devices, your account needs the following
     security permissions:

        To add, modify, and delete the enrollment site system roles: Modify permission
        for the Site object.

        To configure client settings for enrollment: Default client settings require
        Modify permission for the Site object, and custom client settings require Client
        agent permissions.

     The Full Administrator default security role includes the required permissions to
     configure the enrollment site system roles.

     To manage enrolled mobile devices, your account needs the following security
     permissions:

        To wipe or retire a mobile device: Delete resource for the Collection object.

        To cancel a wipe or retire command: Delete resource for the Collection object.

        To allow and block mobile devices: Modify resource for the Collection object.

        To remote lock, or reset the passcode on a mobile device: Modify resource for
        the Collection object.

     The Operations Administrator default security role includes the required
     permissions to manage mobile devices.

For more information about how to configure security permissions, see Fundamentals of
role-based administration and Configure role-based administration.

Firewall requirements
Intervening network devices such as routers and firewalls, and Windows Firewall if
applicable, must allow the traffic associated with mobile device enrollment.

     Between mobile devices and the enrollment proxy point: HTTPS (by default, TCP
     443)

     Between the enrollment proxy point and the enrollment point: HTTPS (by default,
     TCP 443)

<!-- p.2092 -->

If you use a proxy web server, configure it for SSL tunneling. SSL bridging isn't
supported for mobile devices.

Next steps
Windows firewall and port settings for clients

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2093 -->

Windows Firewall and port settings for
clients in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Client computers in Configuration Manager that run Windows Firewall often require you
to configure exceptions to allow communication with their site. The exceptions that you
must configure depend on the management features that you use with the
Configuration Manager client.

Use the following sections to identify these management features and for more
information about how to configure Windows Firewall for these exceptions.

Modifying the Ports and Programs Permitted
by Windows Firewall
Use the following procedure to modify the ports and programs on Windows Firewall for
the Configuration Manager client.

To modify the ports and programs permitted by Windows Firewall

   1. On the computer that runs Windows Firewall, open Control Panel.

   2. Right-click Windows Firewall, and then click Open.

   3. Configure any required exceptions and any custom programs and ports that you
      require.

Programs and Ports that Configuration
Manager Requires
The following Configuration Manager features require exceptions on the Windows
Firewall:

Queries
If you run the Configuration Manager console on a computer that runs Windows
Firewall, queries fail the first time that they are run and the operating system displays a

<!-- p.2094 -->

dialog box asking if you want to unblock statview.exe. If you unblock statview.exe, future
queries will run without errors. You can also manually add Statview.exe to the list of
programs and services on the Exceptions tab of the Windows Firewall before you run a
query.

Client Push Installation
To use client push to install the Configuration Manager client, add the following as
exceptions to the Windows Firewall:

     Outbound and inbound: File and Printer Sharing

     Inbound: Windows Management Instrumentation (WMI)

Client Installation by Using Group Policy
To use Group Policy to install the Configuration Manager client, add File and Printer
Sharing as an exception to the Windows Firewall.

Client Requests
For client computers to communicate with Configuration Manager site systems, add the
following as exceptions to the Windows Firewall:

Outbound: TCP Port 80 (for HTTP communication)

Outbound: TCP Port 443 (for HTTPS communication)

  ） Important

  These are default port numbers that can be changed in Configuration Manager. For
  more information, see How to How to configure client communication ports. If
  these ports have been changed from the default values, you must also configure
  matching exceptions on the Windows Firewall.

Client Notification
For the management point to notify client computers about an action that it must take
when an administrative user selects a client action in the Configuration Manager
console, such as download computer policy or initiate a malware scan, add the following
as an exception to the Windows Firewall:

<!-- p.2095 -->

Outbound: TCP Port 10123

If this communication does not succeed, Configuration Manager automatically falls back
to using the existing client-to-management point communication port of HTTP, or
HTTPS:

Outbound: TCP Port 80 (for HTTP communication)

Outbound: TCP Port 443 (for HTTPS communication)

  ） Important

  These are default port numbers that can be changed in Configuration Manager. For
  more information, see How to configure client communication ports. If these
  ports have been changed from the default values, you must also configure
  matching exceptions on the Windows Firewall.

Remote Control
To use Configuration Manager remote control, allow the following port:

     Inbound: TCP Port 2701

Remote Assistance and Remote Desktop
To initiate Remote Assistance from the Configuration Manager console, add the custom
program Helpsvc.exe and the inbound custom port TCP 135 to the list of permitted
programs and services in Windows Firewall on the client computer. You must also
permit Remote Assistance and Remote Desktop. If you initiate Remote Assistance from
the client computer, Windows Firewall automatically configures and permits Remote
Assistance and Remote Desktop.

Wake-Up Proxy
If you enable the wake-up proxy client setting, a new service named ConfigMgr Wake-
up Proxy uses a peer-to-peer protocol to check whether other computers are awake on
the subnet and to wake them up if necessary. This communication uses the following
ports:

Outbound: UDP Port 25536

Outbound: UDP Port 9

<!-- p.2096 -->

These are the default port numbers that can be changed in Configuration Manager by
using the Power Management clients settings of Wake-up proxy port number (UDP)
and Wake On LAN port number (UDP). If you specify the Power Management:
Windows Firewall exception for wake-up proxy client setting, these ports are
automatically configured in Windows Firewall for clients. However, if clients run a
different firewall, you must manually configure the exceptions for these port numbers.

In addition to these ports, wake-up proxy also uses Internet Control Message Protocol
(ICMP) echo request messages from one client computer to another client computer.
This communication is used to confirm whether the other client computer is awake on
the network. ICMP is sometimes referred to as TCP/IP ping commands.

For more information about wake-up proxy, see Plan how to wake up clients.

Windows Event Viewer, Windows Performance Monitor,
and Windows Diagnostics
To access Windows Event Viewer, Windows Performance Monitor, and Windows
Diagnostics from the Configuration Manager console, enable File and Printer Sharing as
an exception on the Windows Firewall.

Ports Used During Configuration Manager
Client Deployment
The following tables list the ports that are used during the client installation process.

  ） Important

  If there is a firewall between the site system servers and the client computer,
  confirm whether the firewall permits traffic for the ports that are required for the
  client installation method that you choose. For example, firewalls often prevent
  client push installation from succeeding because they block Server Message Block
  (SMB) and Remote Procedure Calls (RPC). In this scenario, use a different client
  installation method, such as manual installation (running CCMSetup.exe) or Group
  Policy-based client installation. These alternative client installation methods do not
  require SMB or RPC.

For information about how to configure Windows Firewall on the client computer, see
Modifying the Ports and Programs Permitted by Windows Firewall.

<!-- p.2097 -->

Ports that are used for all installation methods

                                                                                      ﾉ   Expand table

Description                                                            UDP      TCP

Hypertext Transfer Protocol (HTTP) from the client computer to a       --       80 (See note 1,
fallback status point, when a fallback status point is assigned to              Alternate Port
the client.                                                                     Available)

Ports that are used with client push installation

                                                                                      ﾉ   Expand table

Description                                                           UDP     TCP

Server Message Block (SMB) between the site server and client         --      445
computer.

RPC endpoint mapper between the site server and the client            135     135
computer.

RPC dynamic ports between the site server and the client              --      DYNAMIC
computer.

Hypertext Transfer Protocol (HTTP) from the client computer to        --      80 (See note 1,
a management point when the connection is over HTTP.                          Alternate Port
                                                                              Available)

Secure Hypertext Transfer Protocol (HTTPS) from the client            --      443 (See note 1,
computer to a management point when the connection is over                    Alternate Port
HTTPS.                                                                        Available)

Ports that are used with software update point-based
installation

                                                                                      ﾉ   Expand table

Description                                                      UDP        TCP

Hypertext Transfer Protocol (HTTP) from the client computer      --         80 or 8530 (See note 2,
to the software update point.                                               Windows Server Update
                                                                            Services)

Secure Hypertext Transfer Protocol (HTTPS) from the client       --         443 or 8531 (See note 2,
computer to the software update point.                                      Windows Server Update

<!-- p.2098 -->

Description                                                      UDP        TCP

                                                                            Services)

Server Message Block (SMB) between the source server and         --         445
the client computer when you specify the CCMSetup
command-line property /source:<Path>.

Ports that are used with Group Policy-based installation

                                                                                        ﾉ   Expand table

Description                                                            UDP        TCP

Hypertext Transfer Protocol (HTTP) from the client computer to a       --         80 (See note 1,
management point when the connection is over HTTP.                                Alternate Port
                                                                                  Available)

Secure Hypertext Transfer Protocol (HTTPS) from the client             --         443 (See note 1,
computer to a management point when the connection is over                        Alternate Port
HTTPS.                                                                            Available)

Server Message Block (SMB) between the source server and the           --         445
client computer when you specify the CCMSetup command-line
property /source:<Path>.

Ports that are used with manual installation and logon
script-based installation

                                                                                        ﾉ   Expand table

Description                                                                       UDP       TCP

Server Message Block (SMB) between the client computer and a network              --        445
share from which you run CCMSetup.exe.

When you install Configuration Manager, the client installation source
files are copied and automatically shared from the
<InstallationPath>\Client folder on management points. However, you
can copy these files and create a new share on any computer on the
network. Alternatively, you can eliminate this network traffic by running
CCMSetup.exe locally, for example, by using removable media.

Hypertext Transfer Protocol (HTTP) from the client computer to a                  --        80 (See note
management point when the connection is over HTTP, and you do not                           1, Alternate
specify the CCMSetup command-line property /source:<Path>.

<!-- p.2099 -->

 Description                                                                   UDP      TCP

                                                                                        Port
                                                                                        Available)

 Secure Hypertext Transfer Protocol (HTTPS) from the client computer to a      --       443 (See note
 management point when the connection is over HTTPS, and you do not                     1, Alternate
 specify the CCMSetup command-line property /source:<Path>.                             Port
                                                                                        Available)

 Server Message Block (SMB) between the source server and the client           --       445
 computer when you specify the CCMSetup command-line property
 /source:<Path>.

Ports that are used with software distribution-based
installation

                                                                                    ﾉ   Expand table

 Description                                                       UDP   TCP

 Server Message Block (SMB) between the distribution point         --    445
 and the client computer.

 Hypertext Transfer Protocol (HTTP) from the client to a           --    80 (See note 1, Alternate
 distribution point when the connection is over HTTP.                    Port Available)

 Secure Hypertext Transfer Protocol (HTTPS) from the client to a   --    443 (See note 1,
 distribution point when the connection is over HTTPS.                   Alternate Port Available)

Notes
1 Alternate Port Available In Configuration Manager, you can define an alternate port
for this value. If a custom port has been defined, substitute that custom port when you
define the IP filter information for IPsec policies or for configuring firewalls.

2 Windows Server Update Services You can install Windows Server Update Service
(WSUS) either on the default Web site (port 80) or a custom Web site (port 8530).

After installation, you can change the port. You do not have to use the same port
number throughout the site hierarchy.

If the HTTP port is 80, the HTTPS port must be 443.

If the HTTP port is anything else, the HTTPS port must be 1 higher. For example, 8530
and 8531.

<!-- p.2100 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2101 -->

Determine the site system roles for
Configuration Manager clients
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article can help you determine the site system roles that you need to deploy
Configuration Manager clients.

For more information about where to install these roles in the hierarchy, see Design a
hierarchy of sites.

For more information about how to install and configure these roles, see Install site
system roles.

Management point
By default, all Windows client computers use a distribution point to install the
Configuration Manager client. They can fall back to a management point when a
distribution point is unavailable. However, you can install Windows clients on computers
from an alternative source when you use the CCMSetup command-line property
/source:<Path> . For example, you might do this action if you install clients on the
internet. Another scenario is when you want to avoid sending network packets between
the computer and the management point during client installation. This scenario is
because a firewall blocks the required ports or because you have a low-bandwidth
connection. However, all clients must communicate with a management point to assign
to a site and to be managed by Configuration Manager.

For more information about client command-line properties, see About client
installation properties.

When you install more than one management point in the hierarchy, clients
automatically connect to one point based on their forest membership and network
location. You can't install more than one management point in a secondary site.

Mac computer clients and mobile device clients that you enroll with Configuration
Manager always require a management point for client installation. This management
point must be in a primary site, must be configured to support mobile devices, and must
accept client connections from the Internet. These clients can't use management points
in secondary sites or connect to management points in other primary sites.

<!-- p.2102 -->

Distribution point
You don't need a distribution point to install Configuration Manager clients on Windows
computers. By default, Configuration Manager uses a distribution point to install the
client source files on Windows computers. It can fall back to downloading these files
from a management point. Distribution points aren't used to install mobile device clients
that are enrolled by Configuration Manager, but are used if you install the mobile device
legacy client. If you install the Configuration Manager client as part of an OS
deployment, the OS image is stored and retrieved from a distribution point.

Although you might not need distribution points to install most Configuration Manager
clients, you'll need them to install software such as applications and software updates
on the clients.

Fallback status point
You can use a fallback status point to monitor client deployment for Windows
computers. You can also identify the Windows computer clients that are unmanaged
because they can't communicate with a management point.

The following client types don't use a fallback status point:

     Mac computers
     Mobile devices that are enrolled by Configuration Manager
     Mobile devices that are managed by using the Exchange Server connector

A fallback status point isn't required to monitor client activity and client health.

The fallback status point always communicates with clients over HTTP, which uses
unauthenticated connections and sends data in clear text. This behavior makes the
fallback status point vulnerable to attack, particularly when it's used with internet-based
client management. To help reduce the attack surface, always dedicate a server to
running the fallback status point. Don't install other site system roles on the same server
in a production environment.

Install a fallback status point if all the following conditions apply:

     You want client communication errors from Windows computers to be sent to the
     site, even if these client computers can't communicate with a management point.

     You want to use the Configuration Manager client deployment reports, which
     display the data that's sent by the fallback status point.

<!-- p.2103 -->

     You have a dedicated server for this site system role and have additional security
     measures to help protect the server from attack.

     The benefits of using a fallback status point outweigh any security risks associated
     with unauthenticated connections and clear text transfers over HTTP traffic.

Don't install a fallback status point if the security risks of running a website with
unauthenticated connections and clear text transfers outweigh the benefits of
identifying client communication problems.

Reporting services point
Configuration Manager provides many reports to help you monitor the installation,
assignment, and management of clients in the Configuration Manager console. Some of
the client deployment reports require that clients are assigned to a fallback status point.

The reports aren't needed to deploy clients. You can see some deployment information
in the Configuration Manager console or use the client log files for detailed information.
However, the client reports provide valuable information to help monitor and
troubleshoot client deployment.

Enrollment point and enrollment proxy point

  ） Important

  With the deprecation of on-premises MDM and the Configuration Manager client
  for macOS, these site system roles are also deprecated. For more information, see
  Removed and deprecated features for Configuration Manager.

Configuration Manager requires the enrollment point and the enrollment proxy point to
enroll mobile devices and to enroll certificates for Mac computers. You don't need these
site system roles in the following situations:

     You plan to manage mobile devices by using the Exchange Server connector
     You install the mobile device legacy client
     You request and install the client certificate on Mac computers independently from
     Configuration Manager

Cloud management gateway connector point

<!-- p.2104 -->

You need a cloud management gateway connector point if you're setting up a cloud
management gateway to manage clients on the internet.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2105 -->

Security and privacy for Configuration
Manager clients
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article describes security and privacy information for Configuration Manager clients.
It also includes information for mobile devices that are managed by the Exchange Server
connector.

Security guidance for clients
The Configuration Manager site accepts data from devices that run the Configuration
Manager client. This behavior introduces the risk that the clients could attack the site.
For example, they could send malformed inventory, or attempt to overload the site
systems. Deploy the Configuration Manager client only to devices that you trust.

Use the following security guidance to help protect the site from rogue or compromised
devices.

Use public key infrastructure (PKI) certificates for client
communications with site systems that run IIS
      As a site property, configure Site system settings for HTTPS only. For more
      information, see Configure security.

      Install clients with the UsePKICert CCMSetup property.

      Use a certificate revocation list (CRL). Make sure that clients and communicating
      servers can always access it.

Mobile device clients and some internet-based clients require these certificates.
Microsoft recommends these certificates for all client connections on the intranet.

For more information on the use of certificates in Configuration Manager, see Plan for
certificates.

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP client
  communication are deprecated. Configure the site for HTTPS or Enhanced HTTP.

<!-- p.2106 -->

  For more information, see Enable the site for HTTPS-only or enhanced HTTP.

Automatically approve client computers from trusted
domains and manually check and approve other
computers
When you can't use PKI authentication, approval identifies a computer that you trust to
be managed by Configuration Manager. The hierarchy has the following options to
configure client approval:

     Manual
     Automatic for computers in trusted domains
     Automatic for all computers

The most secure approval method is to automatically approve clients that are members
of trusted domains. This option includes cloud-domain joined clients from connected
Microsoft Entra tenants. Then manually check and approve all other computers.
Automatically approving all clients isn't recommended, unless you have other access
controls to prevent untrustworthy computers from accessing your network.

For more information about how to manually approve computers, see Manage clients
from the devices node.

Don't rely on blocking to prevent clients from accessing
the Configuration Manager hierarchy
Blocked clients are rejected by the Configuration Manager infrastructure. If clients are
blocked, they can't communicate with site systems to download policy, upload inventory
data, or send state or status messages.

Blocking is designed for the following scenarios:

     To block lost or compromised boot media when you deploy an OS to clients
     When all site systems accept HTTPS client connections

When site systems accept HTTP client connections, don't rely on blocking to protect the
Configuration Manager hierarchy from untrusted computers. In this scenario, a blocked
client could rejoin the site with a new self-signed certificate and hardware ID.

Certificate revocation is the primary line of defense against potentially compromised
certificates. A certificate revocation list (CRL) is only available from a supported public

<!-- p.2107 -->

key infrastructure (PKI). Blocking clients in Configuration Manager offers a second line of
defense to protect your hierarchy.

For more information, see Determine whether to block clients.

Use the most secure client installation methods that are
practical for your environment
     For domain computers, group policy client installation and software update-based
     client installation methods are more secure than client push installation.

     If you apply access controls and change controls, use imaging and manual
     installation methods.

     Use Kerberos mutual authentication with client push installation.

Of all the client installation methods, client push installation is the least secure because
of the many dependencies it has. These dependencies include local administrative
permissions, the Admin$ share, and firewall exceptions. The number and type of these
dependencies increase your attack surface.

When using client push, the site can require Kerberos mutual authentication by not
allowing fallback to NTLM before establishing the connection. This enhancement helps
to secure the communication between the server and the client. For more information,
see How to install clients with client push.

For more information about the different client installation methods, see Client
installation methods.

Wherever possible, select a client installation method that requires the least security
permissions in Configuration Manager. Restrict the administrative users that are
assigned security roles with permissions that can be used for purposes other than client
deployment. For example, configuring automatic client upgrade requires the Full
Administrator security role, which grants an administrative user all security permissions.

For more information about the dependencies and security permissions required for
each client installation method, see Prerequisites for computer clients.

If you must use client push installation, secure the client
push installation account
The client push installation account must be a member of the local Administrators
group on each computer that installs the Configuration Manager client. Never add the

<!-- p.2108 -->

client push installation account to the Domain Admins group. Instead, create a global
group, and then add that global group to the local Administrators group on your
clients. Create a group policy object to add a Restricted Group setting to add the client
push installation account to the local Administrators group.

For greater security, create multiple client push installation accounts, each with
administrative access to a limited number of computers. If one account is compromised,
only the client computers to which that account has access are compromised.

Remove certificates before imaging clients
When you deploy clients by using OS images, always remove certificates before
capturing the image. These certificates include PKI certificates for client authentication,
and self-signed certificates. If you don't remove these certificates, clients might
impersonate each other. You can't verify the data for each client.

For more information, see Create a task sequence to capture an OS.

Make sure that Configuration Manager client gets an
authorized copy of certificates

The Configuration Manager trusted root key certificate
When both of the following statements are true, clients rely on the Configuration
Manager trusted root key to authenticate valid management points:

     You haven't extended the Active Directory schema for Configuration Manager
     Clients don't use PKI certificates when they communicate with management points

In this scenario, clients have no way to verify that the management point is trusted for
the hierarchy unless they use the trusted root key. Without the trusted root key, a skilled
attacker could direct clients to a rogue management point.

When clients don't use PKI certificates and can't download the trusted root key from the
Active Directory global catalog, pre-provision the clients with the trusted root key. This
action makes sure that they can't be directed to a rogue management point. For more
information, see Planning for the trusted root key.

The site server signing certificate
Clients use the site server signing certificate to verify that the site server signed the
policy downloaded from a management point. This certificate is self-signed by the site

<!-- p.2109 -->

server and published to Active Directory Domain Services.

When clients can't download this certificate from the Active Directory global catalog, by
default they download it from the management point. If the management point is
exposed to an untrusted network like the internet, manually install the site server
signing certificate on clients. This action makes sure that they can't download tampered
client policies from a compromised management point.

To manually install the site server signing certificate, use the CCMSetup client.msi
property SMSSIGNCERT.

If the client downloads the trusted root key from the first
management point it contacts, don't use automatic site
assignment
To avoid the risk of a new client downloading the trusted root key from a rogue
management point, only use automatic site assignment in the following scenarios:

     The client can access Configuration Manager site information that's published to
     Active Directory Domain Services.

     You pre-provision the client with the trusted root key.

     You use PKI certificates from an enterprise certification authority to establish trust
     between the client and the management point.

For more information about the trusted root key, see Planning for the trusted root key.

Make sure that maintenance windows are large enough
to deploy critical software updates
Maintenance windows for device collections restrict the times that Configuration
Manager can install software on these devices. If you configure the maintenance
window to be too small, the client may not install critical software updates. This behavior
leaves the client vulnerable to any attack that the software update mitigates.

Take security precautions to reduce the attack surface on
Windows Embedded devices with write filters
When you enable write filters on Windows Embedded devices, any software installations
or changes are only made to the overlay. These changes don't persist after the device
restarts. If you use Configuration Manager to disable the write filters, during this period

<!-- p.2110 -->

the embedded device is vulnerable to changes to all volumes. These volumes include
shared folders.

Configuration Manager locks the computer during this period so that only local
administrators can sign in. Whenever possible, take other security precautions to help
protect the computer. For example, enable restrictions on the firewall.

If you use maintenance windows to persist changes, plan these windows carefully.
Minimize the time that write filters are disabled, but make them long enough to allow
software installations and restarts to complete.

Use the latest client version with software update-based
client installation
If you use software update-based client installation, and install a later version of the
client on the site, update the published software update. Then clients receive the latest
version from the software update point.

When you update the site, the software update for client deployment that's published to
the software update point isn't automatically updated. Republish the Configuration
Manager client to the software update point and update the version number.

For more information, see How to install Configuration Manager clients by using
software update-based installation.

Only suspend BitLocker PIN entry on trusted and
restricted-access devices
Only configure the client setting to Suspend BitLocker PIN entry on restart to Always
for computers that you trust and that have restricted physical access.

When you set this client setting to Always, Configuration Manager can complete the
installation of software. This behavior helps install critical software updates and resume
services. If an attacker intercepts the restart process, they could take control of the
computer. Use this setting only when you trust the computer, and when physical access
to the computer is restricted. For example, this setting might be appropriate for servers
in a data center.

For more information on this client setting, see About client settings.

Don't bypass PowerShell execution policy

<!-- p.2111 -->

If you configure the Configuration Manager client setting for PowerShell execution
policy to Bypass, then Windows allows unsigned PowerShell scripts to run. This behavior
could allow malware to run on client computers. When your organization requires this
option, use a custom client setting. Assign it to only the client computers that must run
unsigned PowerShell scripts.

For more information on this client setting, see About client settings.

Security guidance for mobile devices

Install the enrollment proxy point in a perimeter network
and the enrollment point in the intranet
For internet-based mobile devices that you enroll with Configuration Manager, install
the enrollment proxy point in a perimeter network and the enrollment point in the
intranet. This role separation helps to protect the enrollment point from attack. If an
attacker compromises the enrollment point, they could obtain certificates for
authentication. They can also steal the credentials of users who enroll their mobile
devices.

Configure the password settings to help protect mobile
devices from unauthorized access
For mobile devices that are enrolled by Configuration Manager: Use a mobile device
configuration item to configure the password complexity as the PIN. Specify at least the
default minimum password length.

For mobile devices that don't have the Configuration Manager client installed but are
managed by the Exchange Server connector: Configure the Password Settings for the
Exchange Server connector such that the password complexity is the PIN. Specify at
least the default minimum password length.

Only allow applications to run that are signed by
companies that you trust
Help prevent tampering of inventory information and status information by allowing
applications to run only when they're signed by companies that you trust. Don't allow
devices to install unsigned files.

<!-- p.2112 -->

For mobile devices that are enrolled by Configuration Manager: Use a mobile device
configuration item to configure the security setting Unsigned applications as
Prohibited. Configure Unsigned file installations to be a trusted source.

For mobile devices that don't have the Configuration Manager client installed but are
managed by the Exchange Server connector: Configure the Application Settings for the
Exchange Server connector such that Unsigned file installation and Unsigned
applications are Prohibited.

Lock mobile devices when not in use
Help prevent elevation of privilege attacks by locking the mobile device when it isn't
used.

For mobile devices that are enrolled by Configuration Manager: Use a mobile device
configuration item to configure the password setting Idle time in minutes before
mobile device is locked.

For mobile devices that don't have the Configuration Manager client installed but are
managed by the Exchange Server connector: Configure the Password Settings for the
Exchange Server connector to set the Idle time in minutes before mobile device is
locked.

Restrict the users who can enroll their mobile devices
Help prevent elevation of privileges by restricting the users who can enroll their mobile
devices. Use a custom client setting rather than default client settings to allow only
authorized users to enroll their mobile devices.

User device affinity guidance for mobile devices
Don't deploy applications to users who have mobile devices enrolled by Configuration
Manager in the following scenarios:

        The mobile device is used by more than one person.

        The device is enrolled by an administrator on behalf of a user.

        The device is transferred to another person without retiring and then re-enrolling
        the device.

Device enrollment creates a user device affinity relationship. This relationship maps the
user who does enrollment to the mobile device. If another user uses the mobile device,

<!-- p.2113 -->

they can run the applications deployed to the original user, which might result in an
elevation of privileges. Similarly, if an administrator enrolls the mobile device for a user,
applications deployed to the user aren't installed on the mobile device. Instead,
applications deployed to the administrator might be installed.

Protect the connection between the Configuration
Manager site server and the Exchange Server
If the Exchange Server is on-premises, use IPsec. Hosted Exchange automatically secures
the connection with HTTPS.

Use the principle of least privileges for the Exchange
connector
For a list of the minimum cmdlets that the Exchange Server connector requires, see
Manage mobile devices with Configuration Manager and Exchange.

Security guidance for macOS devices

Store and access the client source files from a secured
location
Before installing or enrolling the client on a macOS computer, Configuration Manager
doesn't verify whether these client source files have been tampered with. Download
these files from a trustworthy source. Securely store and access them.

Monitor and track the validity period of the certificate
Monitor and track the validity period of the certificates that you use for macOS
computers. Configuration Manager doesn't support automatic renewal of this certificate,
or warn you that the certificate is about to expire. A typical validity period is one year.

For more information about how to renew the certificate, see Renewing the macOS
client certificate manually.

Configure the trusted root certificate for SSL only
To help protect against elevation of privileges, configure the certificate for the trusted
root certificate authority so that it's only trusted for the SSL protocol.

<!-- p.2114 -->

When you enroll Mac computers, a user certificate to manage the Configuration
Manager client is automatically installed. This user certificate includes the trusted root
certificates in its trust chain. To restrict the trust of this root certificate to the SSL
protocol only, use the following procedure:

   1. On the Mac computer, open a terminal window.

   2. Enter the following command: sudo /Applications/Utilities/Keychain\
      Access.app/Contents/MacOS/Keychain\ Access

   3. In the Keychain Access dialog box, in the Keychains section, select System. Then in
      the Category section, select Certificates.

   4. Locate and open the root CA certificate for the Mac client certificate.

   5. In the dialog box for the root CA certificate, expand the Trust section, and then
      make the following changes:

      a. When using this certificate: Change the Always Trust setting to Use System
         Defaults.

      b. Secure Sockets Layer (SSL): Change no value specified to Always Trust.

   6. Close the dialog box. When prompted, enter the administrator's password, and
      then select Update Settings.

After you complete this procedure, the root certificate is only trusted to validate the SSL
protocol. Other protocols that are now untrusted with this root certificate include Secure
Mail (S/MIME), Extensible Authentication (EAP), or code signing.

  ７ Note

  Also use this procedure if you installed the client certificate independently from
  Configuration Manager.

Security issues for clients
The following security issues have no mitigation:

Status messages aren't authenticated
The management point doesn't authenticate status messages. When a management
point accepts HTTP client connections, any device can send status messages to the

<!-- p.2115 -->

management point. If the management point accepts HTTPS client connections only, a
device must have a valid client authentication certificate, but could also send any status
message. The management point discards any invalid status message received from a
client.

There are a few potential attacks against this vulnerability:

      An attacker could send a bogus status message to gain membership in a collection
      that's based on status message queries.
      Any client could launch a denial of service against the management point by
      flooding it with status messages.
      If status messages are triggering actions in status message filter rules, an attacker
      could trigger the status message filter rule.
      An attacker could send status message that would render reporting information
      inaccurate.

Policies can be retargeted to non-targeted clients
There are several methods that attackers could use to make a policy targeted to one
client apply to an entirely different client. For example, an attacker at a trusted client
could send false inventory or discovery information to have the computer added to a
collection to which it shouldn't belong. That client then receives all the deployments to
that collection.

Controls exist to help prevent attackers from directly modifying policy. However,
attackers could take an existing policy that reformats and redeploys an OS and send it
to a different computer. This redirected policy could create a denial of service. These
types of attacks would require precise timing and extensive knowledge of the
Configuration Manager infrastructure.

Client logs allow user access
All the client log files allow the Users group with Read access, and the special
Interactive user with access to write data. If you enable verbose logging, attackers might
read the log files to look for information about compliance or system vulnerabilities.
Processes such as software that the client installs in a user's context must write to logs
with a low-rights user account. This behavior means an attacker could also write to the
logs with a low-rights account.

The most serious risk is that an attacker could remove information in the log files. An
administrator might need this information for auditing and intrusion detection.

<!-- p.2116 -->

A computer could be used to obtain a certificate that's
designed for mobile device enrollment
When Configuration Manager processes an enrollment request, it can't verify the
request originated from a mobile device rather than from a computer. If the request is
from a computer, it can install a PKI certificate that then allows it to register with
Configuration Manager.

To help prevent an elevation of privilege attack in this scenario, only allow trusted users
to enroll their mobile devices. Carefully monitor device enrollment activities in the site.

A blocked client can still send messages to the
management point
When you block a client that you no longer trust, but it established a network
connection for client notification, Configuration Manager doesn't disconnect the
session. The blocked client can continue to send packets to its management point until
the client disconnects from the network. These packets are only small, keep-alive
packets. This client can't be managed by Configuration Manager until it's unblocked.

Automatic client upgrade doesn't verify the management
point
When you use automatic client upgrade, the client can be directed to a management
point to download the client source files. In this scenario, the client doesn't verify the
management point as a trusted source.

When users first enroll macOS computers, they're at risk
from DNS spoofing
When the macOS computer connects to the enrollment proxy point during enrollment,
it's unlikely that the macOS computer already has the trusted root CA certificate. At this
point, the macOS computer doesn't trust the server, and prompts the user to continue.
If a rogue DNS server resolves the fully qualified domain name (FQDN) of the
enrollment proxy point, it could direct the macOS computer to a rogue enrollment
proxy point to install certificates from an untrusted source. To help reduce this risk,
follow DNS guidance to avoid spoofing in your environment.

macOS enrollment doesn't limit certificate requests

<!-- p.2117 -->

Users can re-enroll their macOS computers, each time requesting a new client
certificate. Configuration Manager doesn't check for multiple requests or limit the
number of certificates requested from a single computer. A rogue user could run a script
that repeats the command-line enrollment request. This attack could cause a denial of
service on the network or on the issuing certificate authority (CA). To help reduce this
risk, carefully monitor the issuing CA for this type of suspicious behavior. Immediately
block from the Configuration Manager hierarchy any computer that shows this pattern
of behavior.

A wipe acknowledgment doesn't verify that the device
has been successfully wiped
When you start a wipe action for a mobile device, and Configuration Manager
acknowledges the wipe, the verification is that Configuration Manager successfully sent
the message. It doesn't verify that the device acted on the request.

For mobile devices managed by the Exchange Server connector, a wipe
acknowledgment verifies that the command was received by Exchange, not by the
device.

If you use the options to commit changes on Windows
Embedded devices, accounts might be locked out sooner
than expected
If the Windows Embedded device is running an OS version earlier than Windows 7, and
a user attempts to sign in while the write filters are disabled by Configuration Manager,
Windows allows only half of the configured number of incorrect attempts before the
account is locked out.

For example, you configure the domain policy for Account lockout threshold to six
attempts. A user mistypes their password three times, and the account is locked out.
This behavior effectively creates a denial of service. If users must sign in to embedded
devices in this scenario, caution them about the potential for a reduced lockout
threshold.

Privacy information for clients
When you deploy the Configuration Manager client, you enable client settings for
Configuration Manager features. The settings that you use to configure the features can
apply to all clients in the Configuration Manager hierarchy. This behavior is the same

<!-- p.2118 -->

whether they're directly connected to the internal network, connected through a remote
session, or connected to the internet.

Client information is stored in the Configuration Manager site database in your SQL
Server, and isn't sent to Microsoft. Information is kept in the database until it's deleted
by the site maintenance task Delete Aged Discovery Data every 90 days. You can
configure the deletion interval.

Some summarized or aggregate diagnostics and usage data is sent to Microsoft. For
more information, see Diagnostics and usage data.

You can learn more about Microsoft's data collection and use in the Microsoft Privacy
Statement    .

Client status
Configuration Manager monitors the activity of clients. It periodically evaluates the
Configuration Manager client and can remediate issues with the client and its
dependencies. Client status is enabled by default. It uses server-side metrics for the
client activity checks. Client status uses client-side actions for self-checks, remediation,
and for sending client status information to the site. The client runs the self-checks
according to a schedule that you configure. The client sends the results of the checks to
the Configuration Manager site. This information is encrypted during transfer.

Client status information is stored in the Configuration Manager database in your SQL
Server, and isn't sent to Microsoft. The information isn't stored in encrypted format in
the site database. This information is kept in the database until it's deleted according to
the value configured for the Retain client status history for the following number of
days client status setting. The default value for this setting is every 31 days.

Privacy information for the Exchange Server
Connector
The Exchange Server Connector finds and manages devices that connect to an on-
premises or hosted Exchange Server by using the ActiveSync protocol. The records
found by the Exchange Server Connector are stored in the Configuration Manager
database in your SQL Server. The information is collected from the Exchange Server. It
doesn't contain any additional information from what the mobile devices send to
Exchange Server.

The mobile device information isn't sent to Microsoft. The mobile device information is
stored in the Configuration Manager database in your SQL Server. Information is kept in

<!-- p.2119 -->

the database until it's deleted by the site maintenance task Delete Aged Discovery Data
every 90 days. You configure the deletion interval.

You can learn more about Microsoft's data collection and use in the Microsoft Privacy
Statement    .

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2120 -->

Determine whether to block clients in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If a client computer or client mobile device is no longer trusted, you can block the client
in the System Center 2012 Configuration Manager console. Blocked clients are rejected
by the Configuration Manager infrastructure so that they cannot communicate with site
systems to download policy, upload inventory data, or send state or status messages.

You must block and unblock a client from its assigned site rather than from a secondary
site or a central administration site.

  ） Important

  Although blocking in Configuration Manager can help to secure the Configuration
  Manager site, do not rely on this feature to protect the site from untrusted
  computers or mobile devices if you allow clients to communicate with site systems
  by using HTTP, because a blocked client could rejoin the site with a new self-signed
  certificate and hardware ID. Instead, use the blocking feature to block lost or
  compromised boot media that you use to deploy operating systems, and when site
  systems accept HTTPS client connections.

Clients that access the site by using the ISV Proxy certificate cannot be blocked. For
more information about the ISV Proxy certificate, see the Configuration Manager
Software Development Kit (SDK).

If your site systems accept HTTPS client connections and your public key infrastructure
(PKI) supports a certificate revocation list (CRL), always consider certificate revocation to
be the primary line of defense against potentially compromised certificates. Blocking
clients in Configuration Manager offers a second line of defense to protect your
hierarchy.

Considerations for blocking clients
      This option is available for HTTP and HTTPS client connections, but has limited
      security when clients connect to site systems by using HTTP.
