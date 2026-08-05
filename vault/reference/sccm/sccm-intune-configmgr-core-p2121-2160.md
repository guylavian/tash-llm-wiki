---
title: "Core infrastructure documentation — pages 2121-2160"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2121-2160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2121-2160
family: sccm
documentKind: "doc"
abstract: "Configuration Manager administrative users have the authority to block a client, and the action is taken in the Configuration Manager console. Client communication is rejected from the Configuration Manager hierarchy only. ７ Note The same client could register with a different C"
---

# Core infrastructure documentation — pages 2121-2160

<!-- p.2121 -->

  Configuration Manager administrative users have the authority to block a client,
  and the action is taken in the Configuration Manager console.

  Client communication is rejected from the Configuration Manager hierarchy only.

    ７ Note

    The same client could register with a different Configuration Manager
    hierarchy.

  The client is immediately blocked from the Configuration Manager site.

  Helps to protect site systems from potentially compromised computers and mobile
  devices.

Considerations for using certificate revocation
  This option is available for HTTPS Windows client connections if the public key
  infrastructure supports a certificate revocation list (CRL).

  Mac clients always perform CRL checking and this functionality cannot be disabled.

  Although mobile device clients do not use certificate revocation lists to check the
  certificates for site systems, their certificates can be revoked and checked by
  Configuration Manager.

  Public key infrastructure administrators have the authority to revoke a certificate,
  and the action is taken outside the Configuration Manager console.

  Client communication can be rejected from any computer or mobile device that
  requires this client certificate.

  There is likely to be a delay between revoking a certificate and site systems
  downloading the modified certificate revocation list (CRL).

  For many PKI deployments, this delay can be a day or longer. For example, in
  Active Directory Certificate Services, the default expiration period is one week for a
  full CRL, and one day for a delta CRL.

  Helps to protect site systems and clients from potentially compromised computers
  and mobile devices.

    ７ Note

<!-- p.2122 -->

        You can further protect site systems that run IIS from unknown clients by
        configuring a certificate trust list (CTL) in IIS.

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.2123 -->

Planning for client deployment to Mac
computers in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in January 2022, this feature of Configuration Manager is deprecated. For
  more information, see Mac computers.

You can install the Configuration Manager client on Mac computers that run macOS X
and use the following management capabilities:

      Hardware inventory

      You can use Configuration Manager hardware inventory to collect information
      about the hardware and installed applications on Mac computers. This information
      can then be viewed in Resource Explorer in the Configuration Manager console
      and used to create collections, queries and reports. For more information, see How
      to use Resource Explorer to view hardware inventory.

      Configuration Manager collects the following hardware information from Mac
      computers:

         Processor

         Computer System

         Disk Drive

         Disk Partition

         Network Adapter

         Operating System

         Service

         Process

         Installed Software

<!-- p.2124 -->

  Computer System Product

  USB Controller

  USB Device

  CDROM Drive

  Video Controller

  Desktop Monitor

  Portable Battery

  Physical Memory

  Printer

  ） Important

  You cannot extend the hardware information that is collected from Mac
  computers during hardware inventory.

Compliance settings

You can use Configuration Manager compliance settings to view the compliance of
and remediate macOS X preference (.plist) settings. For example, you could enforce
settings for the home page in the Safari web browser or ensure that the Apple
firewall is enabled. You can also use shell scripts to monitor and remediate settings
in macOS X.

Application management

Configuration Manager can deploy software to Mac computers. You can deploy
the following software formats to Mac computers:

  Apple disk image (.DMG)

  Meta package file (.MPKG)

  macOS X installer package (.PKG)

  macOS X application (.APP)

When you install the Configuration Manager client on Mac computers, you cannot
use the following management capabilities that are supported by the

<!-- p.2125 -->

     Configuration Manager client on Windows-based computers:

     Client push installation

     Operating system deployment

     Software updates

        ７ Note

        You can use Configuration Manager application management to deploy
        required macOS X software updates to Mac computers. In addition, you can
        use compliance settings to make sure that computers have any required
        software updates.

     Maintenance windows

     Remote control

     Power management

     Client status client check and remediation

     For more information about how to install and configure the Configuration
     Manager Mac client, see How to deploy clients to Macs.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2126 -->

Planning for client deployment to
Windows Embedded devices in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If your Windows Embedded device does not include the Configuration Manager client,
you can use any of the client installation methods if the device meets the required
dependencies. If the embedded device supports write filters, you must disable these
filters before you install the client, and then re-enable the filters again after the client is
installed and assigned to a site.

Note that when you disable the filters, you should not disable the filter drivers. Typically
these drivers are started automatically when the computer is started. Disabling the
drivers will either prevent installation of the client, or interfere with write filter
orchestration which will cause client operations to fail. These are the services associated
with each write filter type that must remain running:

                                                                                ﾉ   Expand table

 Write Filter      Driver    Type         Description
 Type

 EWF               ewf       Kernel       Implements sector-level I/O redirection on protected
                                          volumes.

 FBWF              fbwf      File         Implements file-level I/O redirection on protected
                             system       volumes.

 UWF               uwfreg    Kernel       UWF Registry Redirector

 UWF               uwfs      File         UWF File Redirector
                             System

 UWF               uwfvol    Kernel       UWF Volume Manager

Write filters control how the operating system on the embedded device is updated
when you make changes, such as when you install software. When write filters are
enabled, instead of making the changes directly to the operating system, these changes
are redirected to a temporary overlay. If the changes are only written to the overlay,
they are lost when the embedded device shuts downs. However, if the write filters are
temporarily disabled, the changes can be made permanent so that you do not have to

<!-- p.2127 -->

make the changes again (or reinstall software) every time that the embedded device
restarts. However, temporarily disabling and then re-enabling the write filters requires
one or more restarts, so that you typically want to control when this happens by
configuring maintenance windows so that restarts occur outside business hours.

You can configure options to automatically disable and re-enable the write filters when
you deploy software such as applications, task sequences, software updates, and the
Endpoint Protection client. The exception is for configuration baselines with
configuration items that use automatic remediation. In this scenario, the remediation
always occurs in the overlay so that it is available only until the device is restarted. The
remediation is applied again at the next evaluation cycle, but only to the overlay, which
is cleared at restart. To force Configuration Manager to commit the remediation
changes, you can deploy the configuration baseline and then another software
deployment that supports committing the change as soon as possible.

If the write filters are disabled, you can install software on Windows Embedded devices
by using Software Center. However, if the write filters are enabled, the installation fails
and Configuration Manager displays an error message that you have insufficient
permissions to install the application.

  ２ Warning

  Even if you do not select the Configuration Manager options to commit the
  changes, the changes might be committed if another software installation or
  change is made that commits changes. In this scenario, the original changes will be
  committed in addition to the new changes.

When Configuration Manager disables the write filters to make changes permanent,
only users who have local administrative rights can log on and use the embedded
device. During this period, low-rights users are locked out and see a message that the
computer is unavailable because it is being serviced. This helps protect the device while
it is in a state where changes can be permanently applied, and this servicing mode
lockout behavior is another reason to configure a maintenance window for a time when
users will not log on to these devices.

Configuration Manager supports managing the following types of write filters:

     File-Based Write Filter (FBWF) - For more information, see File-Based Write Filter.

     Enhanced Write Filter (EWF) RAM - For more information, see Enhanced Write
     Filter.

     Unified Write Filter (UWF) - For more information, see Unified Write Filter.

<!-- p.2128 -->

   Configuration Manager does not support write filter operations when the Windows
   Embedded device is in EWF RAM Reg mode.

） Important

If you have the choice, use File-Based Write Filters (FBWF) with Configuration
Manager for increased efficiency and higher scalability.

For devices that use FBWF only: Configure the following exceptions to persist
client state and inventory data between device restarts:

     CCMINSTALLDIR\*.sdf
         CCMINSTALLDIR\ServiceData
         HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\CCM\StateSystem

     Devices that run Windows Embedded 8.0 and later do not support exclusions
     that contain wildcard characters. On these devices, you must configure the
     following exclusions individually:

     All files in CCMINSTALLDIR with the extension .sdf, typically:
         UserAffinityStore.sdf
         InventoryStore.sdf
         CcmStore.sdf
         StateMessageStore.sdf
         CertEnrollmentStore.sdf
         CCMINSTALLDIR\ServiceData
         HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\CCM\StateSystem

For devices that use FBWF and UWF only: When clients in a workgroup use
certificates for authentication to management points, you must also exclude the
private key to ensure the client continues to communicate with the management
point. On these devices, configure the following exceptions:

     c:\Windows\System32\Microsoft\Protect
         c:\ProgramData\Microsoft\Crypto
         HKEY_LOCAL_MACHINE\Software\Microsoft\SystemCertificates\SMS\Certifi
         cates

７ Note

<!-- p.2129 -->

  No additional exceptions are needed by the Configuration Manager client other
  than those documented in the above Important box. Adding additional
  Configuration Manager or WMI (WBEM) related exceptions may lead to failures of
  the Configuration Manager including devices getting stuck in servicing mode or
  devices experiencing reboot loops. Unneeded exceptions include the Configuration
  Manager client directory, the CCMcache directory, the CCMSetup directory, the
  Task Sequence cache directory, the WBEM directory, and Configuration Manager
  related registry keys.

For an example scenario to deploy and manage write-filter-enabled Windows
Embedded devices in Configuration Manager see Example scenario for deploying and
managing Configuration Manager clients on Windows Embedded devices.

For more information about how to build images for Windows Embedded devices and
configure write filters, see your Windows Embedded documentation, or contact your
OEM.

  ７ Note

  When you select the applicable platforms for software deployments and
  configuration items, these display the Windows Embedded families rather than
  specific versions.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2130 -->

Example scenario for deploying and
managing Configuration Manager
clients on Windows Embedded devices
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This scenario demonstrates how you can manage write-filter-enabled Windows
Embedded devices with Configuration Manager.If your embedded devices do not
support write filters, they behave as standard Configuration Manager clients and these
procedures don't apply.

Coho Vineyard & Winery is opening a visitor center and needs kiosks that run Windows
Embedded to run interactive presentations. The building for the new visitor center is not
close to the IT department, so the kiosks must be managed remotely. In addition to the
software that runs the presentations, these devices must run up-to-date antimalware
protection software to comply with the company security policies. The kiosks must run 7
days a week, with no downtime while the visitor center is open.

Coho already runs Configuration Manager to manage devices on their network.
Configuration Manager is configured to run Endpoint Protection, and install software
updates and applications. However, because the IT team has not managed Windows
Embedded devices before, the Configuration Manager administrator runs a pilot to
manage two kiosks in the reception lobby.

To manage these Windows Embedded devices that are write-filter-enabled,
Configuration Manager administrator performs the following steps to install the
Configuration Manager client, protect the client by using Endpoint Protection, and
install the interactive presentation software.

   1. The Configuration Manager administrator (the Admin) reads how Windows
      Embedded devices uses write filters and how Configuration Manager can make this
      easier by automatically disabling and then re-enabling the writer filters to persist a
      software installation.

      For more information, see Planning for client deployment to Windows Embedded
      devices.

   2. Before the Admin installs the Configuration Manager client, the Admin creates a
      new query-based device collection for the Windows Embedded devices. Because
      the company uses standard naming formats to identify their computers, the Admin

<!-- p.2131 -->

  can uniquely identify Windows Embedded devices by the first six letters of the
  computer name: WEMDVC. The Admin uses the following WQL query to create
  this collection: select SMS_R_System.NetbiosName from SMS_R_System where
  SMS_R_System.NetbiosName like "WEMDVC%"

  This collection allows the Admin to manage the Windows Embedded devices with
  different configuration options from the other devices. The Admin will use this
  collection to control restarts, deploy Endpoint Protection with client settings, and
  deploy the interactive presentation application.

  See How to create collections.

3. The Admin configures the collection for a maintenance window to ensure that
  restarts that might be required for installing the presentation application and any
  upgrades do not occur during opening hours for the visitor center. Opening hours
  will be 09:00 through 18:00, Monday through Sunday. The Admin configures the
  maintenance window for every day, 18:30 through 06:00.

4. For more information, see How to use maintenance windows.

5. The Admin then configures a custom device client setting to install the Endpoint
  Protection client by selecting Yes for the following settings, and then deploys this
  custom client setting to the Windows Embedded device collection:

       Install Endpoint Protection client on client computers

       For Windows Embedded devices with write filters, commit Endpoint
       Protection client installation (requires restart)

       Allow Endpoint Protection client installation and restart to be performed
       outside maintenance windows

       When the Configuration Manager client is installed, these settings install the
       Endpoint Protection client and ensure that it is persisted in the operating
       system as part of the installation, rather than written to the overlay only. The
       company security policies require that the antimalware software is always
       installed and the Admin does not want to run the risk of the kiosks being
       unprotected for even a short period of time if they restart.

    ７ Note

    The restarts that are required to install the Endpoint Protection client are a
    one-time occurrence, which happen during the setup period for the devices
    and before the visitor center is operational. Unlike the periodic deployment of

<!-- p.2132 -->

    applications or software definition updates, the next time the Endpoint
    Protection client is installed on the same device will probably be when the
    company upgrades to the next version of Configuration Manager.

  For more information, see Configuring Endpoint Protection.

6. With the configuration settings for the client now in place, the Admin prepares to
  install the Configuration Manager clients. Before the Admin can install the clients,
  they must manually disable the write filter on the Windows Embedded devices. The
  Admin reads the OEM documentation that accompanies the kiosks and follows
  their instructions to disable the write filters.

  The Admin renames the device so it uses the company standard naming format,
  and then installs the client manually by running CCMSetup with the following
  command from a mapped drive that holds the client source files: CCMSetup.exe
  /MP:mpserver.cohovineyardandwinery.com SMSSITECODE=CO1

  This command installs the client, assigns the client to the management point that
  has the intranet FQDN of mpserver.cohovineyardandwinery.com, and assigns the
  client to the primary site named CO1.

  The Admin knows that it always takes a while for clients to install and send back
  their status to the site. So the Admin waits before they confirm that the clients
  successfully install, assign to the site, and appear as clients in the collection that
  they created for Windows Embedded devices.

  As additional confirmation, the Admin checks the properties of Configuration
  Manager in Control Panel on the devices and compares them to standard Windows
  computers that are managed by the site. For example, on the Components tab, the
  Hardware Inventory Agent displays Enabled, and on the Actions tab, there are 11
  available actions, which include Application Deployment Evaluation Cycle and
  Discovery Data Collection Cycle.

  Confident that the clients are successfully installed, assigned, and receiving client
  policy from the management point, the Admin then manually enables the write
  filters by following the instructions from the OEM.

  For more information, see:

       How to deploy clients to Windows computers

       How to assign clients to a site

<!-- p.2133 -->

7. Now that the Configuration Manager client is installed on the Windows Embedded
  devices, the Admin confirms that they can manage them in the same way as they
  manage the standard Windows clients. For example, from the Configuration
  Manager console, the Admin can remotely manage them by using remote control,
  initiate client policy for them, and view client properties and hardware inventory.

  Because these devices are joined to an Active Directory domain, the Admin does
  not have to manually approve them as trusted clients and confirms from the
  Configuration Manager console that they are approved.

  For more information, see How to manage clients.

8. To install the interactive presentation software, the Admin runs the Deploy
  Software Wizard and configures a required application. On the User Experience
  page of the wizard, in the Write filter handling for Windows Embedded devices
  section, they accept the default option that selects Commit changes at deadline
  or during a maintenance window (requires restarts).

  The Admin keeps this default option for write filters to ensure that the application
  persists after a restart, so that it is always available to the visitors using the kiosks.
  The daily maintenance window provides a safe period during which the restarts for
  installation and any updates can occur.

  The Admin deploys the application to the Windows Embedded devices collection.

  For more information, see How to deploy applications with Configuration
  Manager.

9. To configure definition updates for Endpoint Protection, the Admin uses software
  updates and runs the Create Automatic Deployment Rule Wizard. They select the
  Definition Updates template to prepopulate the wizard with settings that are
  appropriate for Endpoint Protection.

  These settings include the following on the User Experience page of the wizard:

       Deadline behavior: The Software Installation check box is not selected.

       Write filter handling for Windows Embedded devices: The Commit changes
       at deadline or during a maintenance window (requires restarts) check box is
       not selected.

       The Admin keeps these default settings. Together, these two options with this
       configuration allow any software update definitions for Endpoint Protection
       to be installed in the overlay during the day and not wait to be installed and
       committed during the maintenance window. This configuration best meets

<!-- p.2134 -->

        the company security policy for computers to run up-to-date antimalware
        protection.

           ７ Note

           Unlike software installations for applications, software update definitions
           for Endpoint Protection can occur very frequently, even multiple times a
           day. They are often small files. For these types of security-related
           deployments, it can often be beneficial to always install to the overlay
           rather than wait until the maintenance window. The Configuration
           Manager client will quickly re-install the software definition updates if
           the device restarts because this action initiates an evaluation check and
           does not wait until the next scheduled evaluation.

        The Admin selects the Windows Embedded devices collection for the
        automatic deployment rule.

        For more information, see
        Step 3: Configure Configuration Manager Software Updates to Deliver
        Definition Updates to Client Computers in Configuring Endpoint Protection

10. The Admin decides to configure a maintenance task that periodically commits all
   changes on the overlay. This task is to support the software update definitions
   deployment, to reduce the number of updates that accumulate and must be
   installed again, each time the device restarts. In the Admin's experience, this helps
   the antimalware programs run more efficiently.

     ７ Note

     These software update definitions would be automatically committed to the
     image if the embedded devices ran another management task that supported
     committing the changes. For example, installing a new version of the
     interactive presentation software would also commit the changes for software
     update definitions. Or, installing standard software updates every month that
     install during the maintenance window could also commit the changes for
     software update definitions. However, in this scenario, where standard
     software updates do not run and the interactive presentation software is
     unlikely to be updated very often, it might be months before the software
     definition updates are automatically committed to the image.

<!-- p.2135 -->

   The Admin first creates a custom task sequence that has no settings other than the
   name. They run the Create Task Sequence Wizard:

    a. On the Create a New Task Sequence page, the Admin selects Create a new
      custom task sequence, and then clicks Next.

    b. On the Task Sequence Information page, the Admin enters Maintenance task
      to commit changes on embedded devices for the task sequence name, and
      then clicks Next.

    c. On the Summary page, the Admin selects Next, and completes the wizard.

      The Admin then deploys this custom task sequence to the Windows Embedded
      devices collection, and configures the schedule to run every month. As part of
      the deployment settings, they select the Commit changes at deadline or during
      a maintenance window (requires restarts) check box to persist the changes
      after a restart. To configure this deployment, the Admin selects the custom task
      sequence that they just created, and then on the Home tab, in the Deployment
      group, they click Deploy to start the Deploy Software Wizard:

    d. On the General page, the Admin selects the Windows Embedded devices
      collection, and then clicks Next.

    e. On the Deployment Settings page, the Admin selects the Purpose of Required,
      and then clicks Next.

    f. On the Scheduling page, the Admin clicks New to specify a weekly schedule
      during the maintenance window, and then clicks Next.

    g. The Admin completes the wizard without any further changes.

      For more information, see
      Manage task sequences to automate tasks.

11. For the kiosks to run automatically, the Admin writes a script to configure the
   devices for the following settings:

         Automatically log on, using a guest account that has no password.

         Automatically run the interactive presentation software on startup.

         The Admin uses packages and programs to deploy this script to the Windows
         Embedded devices collection. When the Admin runs the Deploy Software
         Wizard, they again select the Commit changes at deadline or during a

<!-- p.2136 -->

        maintenance window (requires restarts) check box to persist the changes
        after a restart.

        For more information, see Packages and programs.

12. The following morning, the Admin checks the Windows Embedded devices. They
   confirm the following:

        The kiosk is automatically logged on by using the guest account.

        The interactive presentation software is running.

        The Endpoint Protection client is installed and has the latest software update
        definitions.

        That the device restarted during the maintenance window.

        For more information, see:

        How to monitor Endpoint Protection

        Monitor applications with Configuration Manager

13. The Admin monitors the kiosks and reports the successful management of them to
   their manager. As a result, 20 kiosks are ordered for the visitor center.

   To avoid the manual installation of the Configuration Manager client, which
   requires manually disabling and then enabling the write filters, the Admin ensures
   that the order includes a customized image that already includes the installation
   and site assignment of the Configuration Manager client. In addition, the devices
   are named according to the company naming format.

   The kiosks are delivered to the visitor center a week before it opens. During this
   time, the kiosks are connected to the network, all device management for them is
   automatic, and no local administrator is required. The Admin confirms that the
   kiosks are functioning as required:

        The clients on the kiosks complete site assignment and download the trusted
        root key from Active Directory Domain Services.

        The clients on the kiosks are automatically added to the Windows Embedded
        devices collection and configured with the maintenance window.

        The Endpoint Protection client is installed and has the latest software update
        definitions for antimalware protection.

<!-- p.2137 -->

           The interactive presentation software is installed and runs automatically,
           ready for visitors.

 14. After this initial setup, any restarts that might be required for updates occur only
     when the visitor center is closed.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2138 -->

Plan how to wake up clients in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager supports traditional wake-up packets to wake up computers in
sleep mode when you want to install required software, such as software updates and
applications.

  ７ Note

  This article describes how an older version of Wake on LAN functions. This
  functionality still exists in Configuration Manager version 1810, which also includes
  a newer version of Wake on LAN too. Both versions of Wake on LAN can, and in
  many cases will, be enabled simultaneously. For more information about how the
  new version of Wake on LAN functions starting in 1810 and enabling either or both
  versions, see How to configure Wake on LAN.

How to wake up clients in Configuration
Manager
Configuration Manager supports traditional wake-up packets to wake up computers in
sleep mode when you want to install required software, such as software updates and
applications.

You can supplement the traditional wake-up packet method by using the wake-up proxy
client settings. Wake-up proxy uses a peer-to-peer protocol and elected computers to
check whether other computers on the subnet are awake, and to wake them if
necessary. When the site is configured for Wake On LAN and clients are configured for
wake-up proxy, the process works as follows:

   1. Computers with the Configuration Manager client installed and that aren't asleep
      on the subnet check whether other computers on the subnet are awake. They do
      this check by sending each other a TCP/IP ping command every five seconds.

   2. If there's no response from other computers, they're assumed to be asleep. The
      computers that are awake become manager computer for the subnet.

<!-- p.2139 -->

  Because it's possible that a computer might not respond because of a reason other
  than it's asleep (for example, it's turned off, removed from the network, or the
  proxy wake-up client setting is no longer applied), the computers are sent a wake-
  up packet every day at 2 P.M. local time. Computers that don't respond will no
  longer be assumed to be asleep and will not be woken up by wake-up proxy.

  To support wake-up proxy, at least three computers must be awake for each
  subnet. To achieve this requirement, three computers are non-deterministically
  chosen to be guardian computers for the subnet. This state means that they stay
  awake, despite any configured power policy to sleep or hibernate after a period of
  inactivity. Guardian computers honor shutdown or restart commands, for example,
  as a result of maintenance tasks. If this action happens, the remaining guardian
  computers wake up another computer on the subnet so that the subnet continues
  to have three guardian computers.

3. Manager computers ask the network switch to redirect network traffic for the
  sleeping computers to themselves.

  The redirection is achieved by the manager computer broadcasting an Ethernet
  frame that uses the sleeping computer's MAC address as the source address. This
  behavior makes the network switch behave as if the sleeping computer has moved
  to the same port that the manager computer is on. The manager computer also
  sends ARP packets for the sleeping computers to keep the entry fresh in the ARP
  cache. The manager computer also responds to ARP requests on behalf of the
  sleeping computer and replies with the MAC address of the sleeping computer.

    ２ Warning

    During this process, the IP-to-MAC mapping for the sleeping computer
    remains the same. Wake-up proxy works by informing the network switch that
    a different network adapter is using the port that was registered by another
    network adapter. However, this behavior is known as a MAC flap and is
    unusual for standard network operation. Some network monitoring tools look
    for this behavior and can assume that something is wrong. Consequently,
    these monitoring tools can generate alerts or shut down ports when you use
    wake-up proxy.

    Do not use wake-up proxy if your network monitoring tools and services do
    not allow MAC flaps.

4. When a manager computer sees a new TCP connection request for a sleeping
  computer and the request is to a port that the sleeping computer was listening on

<!-- p.2140 -->

   before it went to sleep, the manager computer sends a wake-up packet to the
   sleeping computer, and then stops redirecting traffic for this computer.

5. The sleeping computer receives the wake-up packet and wakes up. The sending
   computer automatically retries the connection and this time, the computer is
   awake and can respond.

   Wake-up proxy has the following prerequisites and limitations:

） Important

If you have a separate team that is responsible for the network infrastructure and
network services, notify and include this team during your evaluation and testing
period. For example, on a network that uses 802.1X network access control, wake-
up proxy will not work and can disrupt the network service. In addition, wake-up
proxy could cause some network monitoring tools to generate alerts when the
tools detect the traffic to wake-up other computers.

   All Windows operating systems listed as supported clients in Supported operating
   systems for clients and devices are supported for Wake On LAN.

   Guest operating systems that run on a virtual machine are not supported.

   Clients must be enabled for wake-up proxy by using client settings. Although
   wake-up proxy operation does not depend on hardware inventory, clients do not
   report the installation of the wake-up proxy service unless they are enabled for
   hardware inventory and submitted at least one hardware inventory.

   Network adapters (and possibly the BIOS) must be enabled and configured for
   wake-up packets. If the network adapter is not configured for wake-up packets or
   this setting is disabled, Configuration Manager will automatically configure and
   enable it for a computer when it receives the client setting to enable wake-up
   proxy.

   If a computer has more than one network adapter, you cannot configure which
   adapter to use for wake-up proxy; the choice is non-deterministic. However, the
   adapter chosen is recorded in the SleepAgent_<DOMAIN>@SYSTEM_0.log file.

   The network must allow ICMP echo requests (at least within the subnet). You
   cannot configure the five-second interval that is used to send the ICMP ping
   commands.

   Communication is unencrypted and unauthenticated, and IPsec is not supported.

<!-- p.2141 -->

     The following network configurations are not supported:

           802.1X with port authentication

           Wireless networks

           Network switches that bind MAC addresses to specific ports

           IPv6-only networks

           DHCP lease durations less than 24 hours

If you want to wake up computers for scheduled software installation, you must
configure each primary site to use wake-up packets.

To use wake-up proxy, you must deploy Power Management wake-up proxy client
settings in addition to configuring the primary site.

Decide whether to use subnet-directed broadcast packets, or unicast packets, and what
UDP port number to use. By default, traditional wake-up packets are transmitted by
using UDP port 9, but to help increase security, you can select an alternative port for the
site if this alternative port is supported by intervening routers and firewalls.

Choose Between Unicast and Subnet-Directed
Broadcast for Wake-on-LAN
If you chose to wake up computers by sending traditional wake-up packets, you must
decide whether to transmit unicast packets or subnet-direct broadcast packets. If you
use wake-up proxy, you must use unicast packets. Otherwise, use the following table to
help you determine which transmission method to choose.

                                                                              ﾉ    Expand table

 Transmission      Advantage                     Disadvantage
 method

 Unicast           More secure solution than     Wake-up packets do not find destination
                   subnet-directed broadcasts    computers that have changed their subnet
                   because the packet is sent    address after the last hardware inventory
                   directly to a computer        schedule.
                   instead of to all computers
                   on a subnet.                  Switches might have to be configured to
                                                 forward UDP packets.
                   Might not require
                   reconfiguration of routers    Some network adapters might not respond to

<!-- p.2142 -->

Transmission   Advantage                       Disadvantage
method

               (you might have to configure    wake-up packets in all sleep states when they
               the ARP cache).                 use unicast as the transmission method.

               Consumes less network
               bandwidth than subnet-
               directed broadcast
               transmissions.

               Supported with IPv4 and IPv6.

Subnet-        Higher success rate than        Less secure solution than using unicast because
Directed       unicast if you have computers   an attacker could send continuous streams of
Broadcast      that frequently change their    ICMP echo requests from a falsified source
               IP address in the same          address to the directed broadcast address. This
               subnet.                         causes all of the hosts to reply to that source
                                               address. If routers are configured to allow
               No switch reconfiguration is    subnet-directed broadcasts, the additional
               required.                       configuration is recommended for security
                                               reasons:
               High compatibility rate with
               computer adapters for all       - Configure routers to allow only IP-directed
               sleep states, because subnet-   broadcasts from the Configuration Manager
               directed broadcasts were the    site server, by using a specified UDP port
               original transmission method    number.
               for sending wake-up packets.    - Configure Configuration Manager to use the
                                               specified non-default port number.

                                               Might require reconfiguration of all intervening
                                               routers to enable subnet-directed broadcasts.

                                               Consumes more network bandwidth than
                                               unicast transmissions.

                                               Supported with IPv4 only; IPv6 is not supported.

 ２ Warning

 There are security risks associated with subnet-directed broadcasts: An attacker
 could send continuous streams of Internet Control Message Protocol (ICMP) echo
 requests from a falsified source address to the directed broadcast address, which
 cause all the hosts to reply to that source address. This type of denial of service
 attack is commonly called a smurf attack and is typically mitigated by not enabling
 subnet-directed broadcasts.

<!-- p.2143 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2144 -->

Manage Configuration Manager clients
in a virtual desktop infrastructure (VDI)
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager supports installing the Configuration Manager client on the
following virtual desktop infrastructure (VDI) scenarios:

      Personal virtual machines: The virtual machine (VM) maintains user data and
      settings between sessions.

      Remote Desktop Services sessions: Host multiple, concurrent client sessions on a
      centralized server. Users connect to a session and run applications on that server.

      Pooled virtual machines/Non-Persistent: The VM doesn't persist between
      sessions. When a user closes a session, the virtual environment discards all data
      and settings. Pooled virtual machines are useful when you can't use Remote
      Desktop Services. For example, if a required application can't run on the Windows
      Server that hosts the client sessions.

      Azure Virtual Desktop: A desktop and app virtualization service that runs on
      Microsoft Azure. Starting in version 1906, use Configuration Manager to manage
      these virtual devices running Windows in Azure.

Personal VMs
Configuration Manager treats personal VMs the same as a physical computer. You can
preinstall the Configuration Manager client on the VM image or after you provision it.

For more information, see Support for virtualization environments.

Remote Desktop Services
You don't install the Configuration Manager client for individual Remote Desktop
sessions. Install it once on the server that hosts Remote Desktop Services. You can use
all Configuration Manager client features on the Remote Desktop Services server.

For more information, see Welcome to Remote Desktop Services.

<!-- p.2145 -->

Pooled VMs/Non-Persistent
When you decommission a pooled virtual machine, any changes made by Configuration
Manager are lost.

Because the VM might only be operational for a short length of time, some
Configuration Manager features may not return relevant data. For example, hardware
inventory, software inventory, and software metering. Consider excluding pooled VM
from inventory tasks.

Azure Virtual Desktop
For more information, see Supported operating systems for clients and devices.

Other considerations
Because virtualization supports running multiple Configuration Manager clients on the
same physical computer, many client operations have a built-in randomized delay for
scheduled actions. For example, hardware and software inventory, antimalware scans,
software installations, and software update scans. This delay helps distribute the CPU
processing and data transfer for a server that has multiple VMs that run the
Configuration Manager client.

Except for Windows Embedded clients in servicing mode, Configuration Manager clients
not in virtualized environments also use this randomized delay. This behavior helps
avoid peaks in network bandwidth. It also reduces the CPU processing on site systems,
such as the management point and site server. The delay interval varies according to the
Configuration Manager capability. For example, see About client settings - Disable
deadline randomization.

To help with Configuration Manager client performance in virtual environments that
support multiple user sessions, it disables user policy by default. Starting in version
1910, you can enable user policy in this scenario. For more information, see About client
settings - Enable user policy for multiple user sessions.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2146 -->

How to configure client communication
ports in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can change the request port numbers that Configuration Manager clients use to
communicate with site systems that use HTTP and HTTPS for communication. Although
HTTP or HTTPS is more likely to be already configured for firewalls, client notification
that uses HTTP or HTTPS requires more CPU usage and memory on the management
point computer than if you use a custom port number. You can also specify the site port
number to use if you wake up clients by using traditional wake-up packets.

When you specify HTTP and HTTPS request ports, you can specify both a default port
number and an alternative port number. If communication fails with the default port,
clients automatically try the alternative port. You can specify port settings for HTTP and
HTTPS data communication.

The default values for client request ports are 80 for HTTP traffic and 443 for HTTPS
traffic. Change them only if you don't want to use these default values. A typical
scenario for using custom ports is when you use a custom website in IIS rather than the
default website. If you change the default port numbers for the default website in IIS,
and other applications also use the default website, they're likely to fail.

  ） Important

  Don't change the port numbers in Configuration Manager without understanding
  the consequences. For example:

        If you change the port numbers for the client request services as a site
        configuration, and existing clients aren't reconfigured to use the new port
        numbers, these clients will be unmanaged.
        Before you configure a non-default port number, make sure that firewalls and
        all intervening network devices support this configuration. If you will manage
        clients on the internet, and change the default HTTPS port number of 443,
        routers and firewalls on the internet might block this communication.

To make sure that clients don't become unmanaged after you change the request port
numbers, configure clients to use the new request port numbers. When you change the

<!-- p.2147 -->

request ports on a primary site, any attached secondary sites automatically inherit the
same port configuration.

How clients get the port configuration
When the Configuration Manager site is published to Active Directory Domain Services,
new and existing clients that can access this information will automatically be configured
with their site port settings. You don't need to take further action.

Clients that can't access this information published to Active Directory include:

     Workgroup clients
     Clients from another Active Directory forest
     Clients that are configured for internet-only
     Clients that are currently on the internet.

If you change the default port numbers after you install these clients, reinstall them.

Install any new clients by using one of the following methods:

     Reinstall the clients by using the Client Push Installation Wizard. Client push
     installation automatically configures clients with the current site port configuration.
     For more information, see How to install Configuration Manager clients with client
     push.

     Reinstall the clients by using CCMSetup.exe and the client.msi installation
     properties of CCMHTTPPORT and CCMHTTPSPORT. For more information, see
     About client installation properties.

     Reinstall the clients by using a method that searches Active Directory Domain
     Services for Configuration Manager client installation properties. For more
     information, see About client installation properties published to Active Directory
     Domain Services.

To reconfigure the port numbers for existing clients, you can also use the script
Portswitch.vbs. Find this script on the installation media in the
SMSSETUP\Tools\PortConfiguration folder.

  ） Important

  For existing and new clients that are currently on the internet, configure the non-
  default port numbers by using the CCMSetup.exe client.msi properties of
  CCMHTTPPORT and CCMHTTPSPORT.

<!-- p.2148 -->

After changing the request ports on the site, when you install new clients with the site-
wide client push installation method, they're automatically configured with the current
port numbers for the site.

Configure ports for a site
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. Select the primary site to configure.

   3. On the Home tab of the ribbon, select Properties.

   4. Switch to the Ports tab.

   5. Select a service, and then select the Properties icon to open the Port Detail
     window.

<!-- p.2149 -->

   6. Specify the port number and description for the item, and then select OK.

   7. If you want to use the custom website SMSWeb for site systems that run IIS, select
     Use custom web site. For more information, see Websites for site system servers.

   8. Select OK to save the configuration and close the site properties window.

Repeat this procedure for all primary sites in the hierarchy.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2150 -->

Configure client computers to find
management points by using DNS
publishing
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Clients in Configuration Manager must locate a management point to complete site
assignment and as an on-going process to remain managed. Active Directory Domain
Services provides the most secure method for clients on the intranet to find
management points. However, if clients cannot use this service location method (for
example, you have not extended the Active Directory schema, or clients are from a
workgroup), use DNS publishing as the preferred alternative service location method.

Before you use DNS publishing for management points, make sure that DNS servers on
the intranet have service location resource records (SRV RR) and corresponding host (A
or AAA) resource records for the site's management points. The service location
resource records can be created automatically by Configuration Manager or manually,
by the DNS administrator who creates the records in DNS.

For more information about DNS publishing as a service location method for
Configuration Manager clients, see Understand how clients find site resources and
services for Configuration Manager.

By default, clients search DNS for management points in their DNS domain. However, if
there are no management points published in the clients' domain, you must manually
configure clients with a management point DNS suffix. You can configure this DNS suffix
on clients either during or after client installation:

      To configure clients for a management point suffix during client installation,
      configure the CCMSetup Client.msi properties.

      To configure clients for a management point suffix after client installation, in
      Control Panel, configure the Configuration Manager Properties.

To configure clients for a management point suffix during client
installation

      Install the client with the following CCMSetup Client.msi property:

         DNSSUFFIX= <management point domain>

<!-- p.2151 -->

        If the site has more than one management point and they are in more than one
        domain, specify just one domain. When clients connect to a management point
        in this domain, they download a list of available management points, which will
        include the management points from the other domains.

        For more information about the CCMSetup command-line properties, see About
        client installation properties.

To configure clients for a management point suffix after client
installation

   1. In Control Panel of the client computer, navigate to Configuration Manager, and
     then double-click Properties.

   2. On the Site tab, specify the DNS suffix of a management point, and then click OK.

     If the site has more than one management point and they are in more than one
     domain, specify just one domain. When clients connect to a management point in
     this domain, they download a list of available management points, which will
     include the management points from the other domains.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2152 -->

How to configure client settings in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You manage all client settings in Configuration Manager from the Client Settings node
of the Administration workspace in the console. When you want to configure settings
for all users and devices in the hierarchy, modify the default settings. If you want to
apply different settings to just some users or devices, create custom settings and deploy
to collections. Custom client settings override the default settings.

For information about each client setting, see About client settings.

  ７ Note

  You can also use configuration items to manage clients to assess, track, and
  remediate the configuration compliance of devices. For more information, see
  Ensure device compliance.

Configure default client settings
   1. In the Configuration Manager console, go to the Administration workspace, and
      select the Client Settings node.

   2. Select Default Client Settings. On the Home tab of the ribbon, select Properties.

   3. View and configure the client settings for each group of settings in the navigation
      pane.

   Tip

  Configuration Manager configures clients with these settings when they next
  download policy. To start policy retrieval for a single client, see Start policy retrieval
  for a Configuration Manager client.

Create and deploy custom client settings

<!-- p.2153 -->

When you deploy these custom settings, they override the default client settings. Before
you begin this procedure, make sure that you have a collection the deployment. The
collection should contain the users or devices that require these custom client settings.

   1. In the Configuration Manager console, go to the Administration workspace, and
     select the Client Settings node.

   2. On the Home tab of the ribbon, in the Create group, select Create Custom Client
     Settings. Then choose either Create Custom Client Device Settings or Create
     Custom Client User Settings.

      a. Specify a unique name and optional description.

     b. Select one or more of the settings groups.

      c. Select each group of settings from the navigation pane, configure the available
        settings, and then select OK to save the settings.

   3. Select the custom client setting that you created. On the Home tab of the ribbon,
     in the Client Settings group, choose Deploy.

   4. In the Select Collection window, select the appropriate collection, and then choose
     OK. To verify the targeted collection, switch to the Deployments tab in the details
     pane of the Client Settings node.

   5. View the order of the custom client setting that you created. When you have
     multiple custom client settings, they're applied according to their order number. If
     there are any conflicts between settings, the setting that has the lowest order
     number overrides the other settings. To change the order number, on the Home
     tab of the ribbon, in the Client Settings group, choose Move Item Up or Move
     Item Down.

   Tip

  Configuration Manage configures clients with these settings when they next
  download policy. To start policy retrieval for a single client, see Start policy retrieval
  for a Configuration Manager client.

View client settings
When you deploy multiple client settings to the same device, user, or user group, the
prioritization and combination of settings is complex.

<!-- p.2154 -->

   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select either the Devices or Users node.

   2. Select a device or user, and in the Client Settings group of the ribbon, select
     Resultant Client Settings.

   3. Select a client setting from the left pane, and it displays the settings. In this view,
     the settings are read-only.

        ７ Note

        To view the client settings, your account needs Read access to client settings.

Automate with PowerShell
Optionally, you can use the Configuration Manager PowerShell cmdlets to automate
client settings. For more information, see the following articles in the PowerShell
documentation:

     Get-CMClientSetting: Get an existing client settings object.

     New-CMClientSetting: Create a new client settings object.

     Remove-CMClientSetting: Remove a client settings object.

Use the following cmdlets to configure client settings for the specific group:

     Set-CMClientSettingBackgroundIntelligentTransfer
     Set-CMClientSettingClientCache
     Set-CMClientSettingClientPolicy
     Set-CMClientSettingCloudService
     Set-CMClientSettingComplianceSetting
     Set-CMClientSettingComputerAgent
     Set-CMClientSettingComputerRestart
     Set-CMClientSettingDeliveryOptimization
     Set-CMClientSettingEndpointProtection
     Set-CMClientSettingEnrollment
     Set-CMClientSettingGeneral
     Set-CMClientSettingHardwareInventory
     Set-CMClientSettingMeteredInternetConnection
     Set-CMClientSettingPowerManagement
     Set-CMClientSettingRemoteTool

<!-- p.2155 -->

     Set-CMClientSettingSoftwareCenter
     Set-CMClientSettingSoftwareDeployment
     Set-CMClientSettingSoftwareInventory
     Set-CMClientSettingSoftwareMetering
     Set-CMClientSettingSoftwareUpdate
     Set-CMClientSettingStateMessaging
     Set-CMClientSettingUserAndDeviceAffinity

Use the following cmdlets to manage deployments of custom client settings:

     New-CMClientSettingDeployment
     Remove-CMClientSettingDeployment

Next steps
About client settings

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2156 -->

About client settings in Configuration
Manager
Applies to: Configuration Manager (current branch)

Manage all client settings in the Configuration Manager console from the Client Settings node
in the Administration workspace. Configuration Manager comes with a set of default settings.
When you change the default client settings, these settings are applied to all clients in the
hierarchy. You can also configure custom client settings, which override the default client
settings when you assign them to collections. For more information, see How to configure
client settings.

The following sections describe settings and options in further detail.

Background Intelligent Transfer Service (BITS)

Limit the maximum network bandwidth for BITS background
transfers
When this option is Yes, clients use BITS bandwidth throttling. To configure the other settings
in this group, you must enable this setting.

Throttling window start time
Specify the local start time for the BITS throttling window.

Throttling window end time
Specify the local end time for the BITS throttling window. If the end time is equal to the
Throttling window start time, BITS throttling is always enabled.

Maximum transfer rate during throttling window (Kbps)
Specify the maximum transfer rate that clients can use during the window.

Allow BITS downloads outside the throttling window
Allow clients to use separate BITS settings outside the specified window.

<!-- p.2157 -->

Maximum transfer rate outside the throttling window (Kbps)
Specify the maximum transfer rate that clients can use outside the BITS throttling window.

Client cache settings

Configure BranchCache
Set up the client computer for Windows BranchCache. To allow BranchCache caching on the
client, set Enable BranchCache to Yes.

     Enable BranchCache: Enables BranchCache on client computers.

     Maximum BranchCache cache size (percentage of disk): The percentage of the disk that
     you allow BranchCache to use.

   Tip

  If you set Configure BranchCache to No, then Configuration Manager doesn't configure
  any BranchCache settings.

  To disable BranchCache, set Configure BranchCache to Yes, and then set Enable
  BranchCache to No.

Configure client cache size
The Configuration Manager client cache on Windows computers stores temporary files used to
install applications and programs. If this option is set to No, the default size is 5,120 MB.

If you choose Yes, then specify:

     Maximum cache size (MB)
     Maximum cache size (percentage of disk): The client cache size expands to the
     maximum size in megabytes (MB), or the percentage of the disk, whichever is less.

Enable as peer cache source
Enables peer cache for Configuration Manager clients. Choose Yes, and then specify the port
through which the client communicates with the peer computer.

<!-- p.2158 -->

     Port for initial network broadcast (default UDP 8004): Configuration Manager uses this
     port in Windows PE or the full Windows OS. The task sequence engine in Windows PE
     sends the broadcast to get content locations before it starts the task sequence.

     Port for content download from peer (default TCP 8003): Configuration Manager
     automatically configures Windows Firewall rules to allow this traffic. If you use a different
     firewall, you must manually configure rules to allow this traffic.

     For more information, see Ports used for connections.

  ７ Note

  We configure the port to download content from peer as (default TCP 8003) which binds
  to self-signed cert even in an environment where PKI certificate is enabled.

Minimum duration before cached content can be removed
(minutes)
Specify the minimum time for the Configuration Manager client to keep cached content. This
client setting defines the minimum amount of time Configuration Manager agent should wait
before it can remove content from the cache in case more space is needed.

By default this value is 1,440 minutes (24 hours). The maximum value for this setting is 10,080
minutes (one week).

This setting gives you greater control over the client cache on different types of devices. You
might reduce the value on clients that have small hard drives and don't need to keep existing
content before another deployment runs.

Client policy

Client policy polling interval (minutes)
Specifies how frequently the following Configuration Manager clients download client policy:

     Windows computers (for example, desktops, servers, laptops)
     Mobile devices that Configuration Manager enrolls
     Mac computers

This value is 60 minutes by default. Reducing this value causes clients to poll the site more
frequently. With many clients, this behavior can have a negative impact on the site

<!-- p.2159 -->

performance. The size and scale guidance is based on the default value. Increasing this value
causes clients to poll the site less often. Any changes to client policies, including new
deployments, take longer for clients to download and process.

Enable user policy on clients
When you set this option to Yes, and use user discovery, then clients receive applications and
programs targeted to the signed-in user.

If this setting is No, users don't receive required applications that you deploy to users. Users
also don't receive any other management tasks in user policies.

This setting applies to users when their computer is on either the intranet or the internet. It
must be Yes if you also want to enable user policies on the internet.

Enable user policy requests from internet clients
Set this option to Yes for users to receive the user policy on internet-based computers. The
following requirements also apply:

     The client and site are configured for internet-based client management or a cloud
     management gateway.

     The Enable user policy on clients setting is Yes.

     The internet-based management point successfully authenticates the user by using
     Windows authentication (Kerberos or NTLM). For more information, see Considerations
     for client communications from the internet.

     The cloud management gateway successfully authenticates the user by using Microsoft
     Entra ID. For more information, see Prerequisites to deploy user-available applications.

If you set this option to No, or any of the previous requirements aren't met, then a computer
on the internet only receives computer policies. If this setting is No, but Enable user policy on
clients is Yes, users don't receive user policies until the computer is connected to the intranet.

  ７ Note

  For internet-based client management, application approval requests from users don't
  require user policies or user authentication. The cloud management gateway doesn't
  support application approval requests.

<!-- p.2160 -->

Enable user policy for multiple user sessions
By default, this setting is disabled. Even if you enable user policies, the client disables them by
default on any device that allows multiple concurrent active user sessions. For example,
terminal servers or Windows Enterprise multi-session in Azure Virtual Desktop.

The client only disables user policy when it detects this type of device during a new installation.
For an existing client of this type that you update to a later client version, the previous behavior
persists. On an existing device, it configures the user policy setting even if it detects that the
device allows multiple user sessions.

If you require user policy in this scenario, and accept any potential performance impact, enable
this client setting.

Cloud services

Allow access to cloud distribution point
Set this option to Yes for clients to obtain content from a content-enabled CMG. This setting
doesn't require the device to be internet-based.

Automatically register new Windows 10 or later domain joined
devices with Microsoft Entra ID
When you configure Microsoft Entra ID to support hybrid join, Configuration Manager
configures Windows 10 or later devices for this functionality. For more information, see How to
configure Microsoft Entra hybrid joined devices.

Enable clients to use a cloud management gateway
By default, all internet-roaming clients use any available cloud management gateway. An
example of when to configure this setting to No is to scope usage of the service, such as
during a pilot project or to save costs.

Compliance settings

Enable compliance evaluation on clients
Set this option to Yes to configure the other settings in this group.
