---
title: "Core infrastructure documentation — pages 2321-2360"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2321-2360
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2321-2360
family: sccm
documentKind: "doc"
abstract: "Surface device dashboard in Configuration Manager Article • 10/04/2022 Applies to: Configuration Manager (current branch) The Surface device dashboard gives you information about Surface devices found in your environment at a single glance. How to open To open the Surface device"
---

# Core infrastructure documentation — pages 2321-2360

<!-- p.2321 -->

Surface device dashboard in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Surface device dashboard gives you information about Surface devices found in
your environment at a single glance.

How to open
To open the Surface device dashboard, use the following steps:

   1. Open the Configuration Manager console.
   2. Select the Monitoring workspace.
   3. To load the dashboard, select the Surface Devices node.

Review information
The Surface device dashboard shows three graphs:

<!-- p.2322 -->

Percent of Surface devices: The percentage of Surface devices throughout your
environment.

Surface Models: The number of devices per Surface model. Hover over a graph
section to see the percentage of Surface devices for that model.

  Select a graph section to go through to a device list for that model.

<!-- p.2323 -->

     Top five firmware versions: The top five firmware models in your environment.
     Hover over a graph section to see the number of Surface devices with that
     firmware version. Select a graph section to go through to a device list.

Next steps
You can use Configuration Manager to deploy Surface firmware updates. For more
information, see Managing Surface driver updates.

For more information about Surface devices, see the Surface     website.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2324 -->

Removed and deprecated features for
Configuration Manager
Applies to: Configuration Manager (current branch)

This article lists the features that are deprecated or removed from support for Configuration
Manager. Deprecated features will be removed in a future update. These future changes might
affect your use of Configuration Manager.

This information is subject to change with future releases. It might not include each deprecated
Configuration Manager feature.

Deprecated features
The following features are deprecated. You can still use them now, but Microsoft plans to end
support in the future.

                                                                                         ﾉ   Expand table

 Feature                                                                   Deprecation       Planned end
                                                                           first             of support
                                                                           announced

 Microsoft Connected Cache (MCC) integration in Configuration Manager      June 2026         TBD
 will be deprecated in a future release of Configuration Manager. After
 deprecation, no further feature development or updates will be provided
 for Microsoft Connected Cache within Configuration Manager. Customers
 should begin transitioning to the standalone version of Microsoft
 Connected Cache to continue receiving ongoing improvements and
 support. For more information, see Microsoft Connected Cache.

 The MDT Integration with CM and Standalone is no longer supported         Dec 2024          The first
 with Configuration Manager. Customers should remove MDT TS steps,                           release after
 followed by removing MDT integration, to avoid TS corruption and                            Oct 10, 2025
 modification failures. More information on the MDT retirement here.

 Office 365 Client Management dashboard add-in support statement.          April 2024        The first
 For more information, see Office 365 Client Management dashboard.                           release after
                                                                                             April 1, 2025

 Windows Information Protection                                            July 2022         TBD

<!-- p.2325 -->

Feature                                                                    Deprecation     Planned end
                                                                           first           of support
                                                                           announced

The site system roles for on-premises MDM and macOS clients:               January 2022    Mar 31, 2024
enrollment proxy point and enrollment point.

The Microsoft Store for Business and Education. For more information,      November        The first
see Manage apps from the Microsoft Store for Business and Education        2021            release after
with Configuration Manager.                                                                March 1,
                                                                                           2023

Asset intelligence. For more information, see Asset intelligence           November        The first
deprecation.                                                               2021            release after
                                                                                           November 1,
                                                                                           2022

On-premises MDM. For more information, see On-premises MDM in              November        The first
Configuration Manager.                                                     2021            release after
                                                                                           November 1,
                                                                                           2022

Azure Active Directory (Azure AD) Graph API and Azure AD Authentication    July 2021       June 30, 2022
Library (ADAL), which is used by Configuration Manager for some cloud-
attached scenarios. If you use cloud-attached features such as co-
management, tenant attach, or Microsoft Entra discovery, starting June
30, 2022, these features may not work correctly in Configuration Manager
version 2107 or earlier. Stay current with Configuration Manager to make
sure these features continue to work. For more information, see CMG
FAQ.

The BitLocker management implementation for the recovery service has       March 2021      The first
changed. The legacy MBAM-based service is replaced by the messaging                        release after
processing engine on the management point.                                                 Mar 2025

Older style of console extensions that haven't been approved in the        April 2021      TBDNote 1
Console Extension node, will no longer be supported. For more
information about new console extensions, see Manage console
extensions.

The implementation for sharing content from Azure has changed. Use a       February 2019   The first
content-enabled cloud management gateway. Starting in version 2107,                        release after
you can't create a traditional cloud distribution point.                                   October 5,
                                                                                           2022

Cloud management gateway and cloud distribution point deployments          November        The first
with Azure Service Manager using a management certificate. For more        2018            release after
information, see Plan for CMG.                                                             October 5,
                                                                                           2022

<!-- p.2326 -->

Note 1: Support removed TBD
The specific timeframe is to be determined (TBD). Microsoft recommends that you change to the
new process or feature, but you can continue to use the deprecated process or feature for the
near future.

Unsupported and removed features
The following features are no longer supported. In some cases, they're no longer in the product.

                                                                                        ﾉ   Expand table

 Feature                                                              Deprecation    Support removed
                                                                      first
                                                                      announced

 System Center Update Publisher (SCUP) and integration with           October 2023   Jan 31, 2024
 ConfigMgr

 Sites that allow HTTP client communication. Configure the site for   March 2021     The first release
 HTTPS or Enhanced HTTP. For more information, see Enable the                        after April 1, 2024
 site for HTTPS-only or enhanced HTTP.

 Upgrade from any version of System Center 2012 Configuration         April 2022     Version 2303
 Manager to current branch. For more information, see Upgrade to
 Configuration Manager current branch

 The Configuration Manager client for macOS and Mac client            January 2022   December 31, 2022
 management. For more information, see Supported clients: Mac
 computers. Migrate management of macOS devices to Microsoft
 Intune. For more information, see Deployment guide: Manage
 macOS devices in Microsoft Intune.

 Community hub service and integration with ConfigMgr                 October 2022   The first release
                                                                                     after March 1, 2023

 The geographical view in the Site Hierarchy node of the              August 2020    The first release
 Monitoring workspace in the Configuration Manager console.                          after September
                                                                                     2023

 Desktop Analytics. For more information, see Windows                 November       November 30, 2022
 compatibility reports in Intune   .                                  2021

 The ability to deploy a cloud management gateway (CMG) as a          September      Version 2203
 cloud service (classic). All CMG deployments should use a virtual    2021
 machine scale set.

<!-- p.2327 -->

Feature                                                                 Deprecation    Support removed
                                                                        first
                                                                        announced

Cloud management gateway (CMG) as a cloud service (classic). All                       Version 2403
CMG deployments should use a virtual machine scale set.

The following compliance settings for Company resource access:          March 2021     Version 2203
Certificate profiles, VPN profiles, Wi-Fi profiles, Windows Hello for
Business settings, and email profiles. This deprecation includes the
co-management resource access workload. Use Microsoft Intune to
deploy resource access profiles. For more information, see
Frequently asked questions about resource access deprecation.

Desktop Analytics data for Windows 7, Windows 8, and earlier            July 2021      January 31, 2022
versions of Windows 10 that don't support the Windows diagnostic
data processor configuration.

Third-party add-ons that use Microsoft .NET Framework version           September      Version 2111
4.6.1 or earlier, and rely on Configuration Manager libraries. Such     2021
add-ons need to use .NET 4.6.2 or later. For more information, see
External dependencies require .NET 4.6.2.

Log Analytics connector for Azure Monitor. This feature is called       November       Version 2107
the OMS Connector in the Azure Services node.                           2020

Microsoft Edge legacy browser profiles. For more information, see       March 2021     April 2021
New Microsoft Edge to replace Microsoft Edge Legacy with April's
Windows 10 Update Tuesday release

The collection evaluation viewer, which was integrated in version       November       Version 2103
2010.                                                                   2020

Desktop Analytics tile and page for Security Updates                    December       March 2021
                                                                        2020

Desktop Analytics option to View recent data for device                 May 2020       July 2020
enrollment and security updates. For more information, see Data
latency.

Windows Analytics and Upgrade Readiness integration. For more           October 14,    January 31, 2020
information, see KB 4521815: Windows Analytics retirement on            2019
January 31, 2020   .

Device health attestation assessment for Conditional Access             July 3, 2019   Version 1910
compliance policies For more information, see What happened to
hybrid MDM.

The Configuration Manager Company Portal app                            May 21, 2019   Version 1910

The application catalog, including both site system roles: the          May 21, 2019   Version 1910
application catalog website point and web service point. For more

<!-- p.2328 -->

Feature                                                               Deprecation     Support removed
                                                                      first
                                                                      announced

information, see Remove the application catalog.

Certificate-based authentication with Windows Hello for Business      December        Version 1910
settings in Configuration Manager                                     2017
For more information, see Windows Hello for Business settings.

System Center Endpoint Protection for Mac and Linux                   October 2018    December 31, 2018
For more information, see End of support blog post .

On-premises Conditional Access                                        January 30,     September 1, 2019
For more information, see What happened to hybrid MDM.                2019

Hybrid mobile device management (MDM)                                 August 14,      September 1, 2019
For more information, see What happened to hybrid MDM.                2018

Starting with the 1902 Intune service release, expected at the end
of February 2019, new customers can't create a new hybrid
connection.

Security Content Automation Protocol (SCAP) extensions.               September       Version 1810
                                                                      2018

The Silverlight user experience for the application catalog website   August 11,      Version 1806
point is no longer supported. Users should use the new Software       2017
Center. For more information, see Configure Software Center.

The previous version of Software Center.                              December 13,    Version 1802
                                                                      2016
For more information about the new Software Center, see Plan for
and configure application management.

Management of Virtual Hard Disks (VHDs) with Configuration            January 6,      Version 1710
Manager.                                                              2017

This deprecation includes removal of options to create a new VHD
or manage a VHD using a task sequence, and the removal of the
Virtual Hard Disks node from the Configuration Manager console.

Existing VHDs are not deleted, but are no longer accessible from
within the Configuration Manager console.

Task sequences:                                                       November 18,    Version 1710
- Convert Disk to Dynamic                                             2016
- Install Deployment Tools

Upgrade Assessment Tool                                               September 12,   July 11, 2017
                                                                      2016
The Upgrade Assessment Tool depends on both Configuration

<!-- p.2329 -->

 Feature                                                                Deprecation     Support removed
                                                                        first
                                                                        announced

 Manager and the Application Compatibility Toolkit (ACT) 6.x. The
 final version of ACT was shipped in the Windows 10 v1511 ADK. As
 there are no further updates to ACT, support for the Upgrade
 Assessment Tool is discontinued. Deprecation notice was added to
 the download page for UAT on September 12, 2016.

 Software update points with a network load balancing (NLB) cluster     February 27,    Version 1702
                                                                        2016

 Task sequences:                                                        June 20, 2016   Version 1606
 - OSDPreserveDriveLetter

 During an operating system deployment, by default, Windows
 Setup now determines the best drive letter to use (typically C:). If
 you want to specify a different drive to use, you can change the
 location in the Apply Operating System task sequence step. Go to
 the Select the location where you want to apply this operating
 system setting. Select Specific logical drive letter and choose the
 drive that you want to use.

 Network Access Protection (NAP) - as found in System Center 2012       July 10, 2015   Version 1511
 Configuration Manager

 Out of Band Management - as found in System Center 2012                October 16,     Version 1511
 Configuration Manager                                                  2015

 System Center Configuration Manager Management Pack - for              October 16,     Version 1511
 System Center Operations Manager is not available for download         2015

WINS
Windows Internet Name Service (WINS) is a legacy computer name registration and resolution
service. It's a deprecated service. You should replace WINS with Domain Name System (DNS). For
more information, see Windows Internet Name Service (WINS).

Out of Band Management
With Configuration Manager, native support for AMT-based computers from within the
Configuration Manager console has been removed.

     AMT-based computers remain fully managed when you use the Intel SCS Add-on for
     Configuration Manager . The add-on provides you access to the latest capabilities to

<!-- p.2330 -->

     manage AMT, while removing limitations introduced until Configuration Manager could
     incorporate those changes.

     Out of Band Management in System Center 2012 Configuration Manager is not affected by
     this change.

Network Access Protection
Configuration Manager has removed support for Network Access Protection. The feature has
been deprecated in Windows Server 2012 R2, and is removed from Windows 10.

For network access protection alternatives, see the Deprecated functionality section of Network
Policy and Access Services Overview.

See also
     Removed and deprecated
     Microsoft Support Lifecycle
     Support for current branch versions of Configuration Manager

Last updated on 06/11/2026

<!-- p.2331 -->

How to manage clients in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When the Configuration Manager client installs on a device and successfully assigns to a
site, you see the device in the Assets and Compliance workspace in the Devices node,
and in one or more collections in the Device Collections node. Select the device or a
collection, and then run management operations. However, there are other ways to
manage the client, which might involve other workspaces in the console, or tasks
outside of the console.

  ７ Note

  If you install the Configuration Manager client, but it hasn't yet successfully
  assigned to a site, it might not display in the console. After the client assigns to a
  site, update collection membership, and then refresh the console view.

  A device can also display in the console when the Configuration Manager client
  isn't installed. This behavior happens if the site discovers a device but the client
  isn't installed and assigned.

  Mobile devices managed with the Exchange Server connector or on-premises
  MDM don't install the Configuration Manager client.

  To manage a device from the console, use the Client column in the Devices node to
  determine whether the client is installed.

Manage clients from the Devices node
Depending on the device type, some of these options might not be available.

   1. In the Configuration Manager console, go to the Assets and Compliance
      workspace, and select the Devices node.

   2. Select one or more devices, and then select one of these client management tasks
      from the ribbon. You can also right-click the device.

Import user device affinity

<!-- p.2332 -->

Configure the associations between users and devices, so you can efficiently deploy
software to users.

For more information, see Link users and devices with user device affinity.

Import computer information
Launch the Import Computer Information Wizard to import new computer information
into the Configuration Manager database. You can import multiple computers using a
file, or specify information for a single computer.

Add selected items
Provides the following options:

        Add selected items to existing device collection: Opens the Select Collection
        dialog box. Select the collection to which you want to add this device. The device is
        included in this collection by using a Direct membership rule.

        Add selected items to new device collection: Opens the Create Device Collection
        Wizard where you can create a new collection. The selected collection is included
        in this collection by using a Direct membership rule.

For more information, see How to create collections.

Install client
Opens the Install Client Wizard. This wizard uses client push installation to install or
reinstall the Configuration Manager client on the selected device.

   Tip

  There are many different ways to install the Configuration Manager client. Although
  the Client Push wizard offers a convenient client installation method from the
  console, this method has many dependencies and isn't suitable for all
  environments. For more information about the dependencies, see Prerequisites for
  deploying clients to Windows computers. For more information about the other
  client installation methods, see Client installation methods.

For more information, see How to install Configuration Manager clients by using client
push.

<!-- p.2333 -->

Run script
Opens the Run Script wizard to run a PowerShell script on the selected device.

For more information, see Create and run PowerShell scripts.

Install application
Install an application to a device in real time. This feature can help reduce the need for
separate collections for every application.

Starting in version 2111, select the Install Application Group action for an app group.

For more information, see Install applications for a device.

Reassign site
Reassign one or more clients, including managed mobile devices, to another primary
site in the hierarchy. You can individually reassign clients or select more than one to
reassign them in bulk.

Client settings - Resultant client settings
When you deploy multiple client settings to the same device, the prioritization and
combination of settings is complex. Use this option to view the resultant set of client
settings deployed to this device.

For more information, see How to configure client settings.

Start
     Run Resource Explorer to see the hardware and software inventory information
     from a Windows client. For more information, see the following articles:

        How to use Resource Explorer to view hardware inventory

        How to use Resource Explorer to view software inventory

     Remotely administer the device by using Remote Control, Remote Assistance, or
     Remote Desktop Client. For more information, see How to remotely administer a
     Windows client computer.

Approve

<!-- p.2334 -->

When the client communicates with site systems using HTTP and a self-signed
certificate, you must approve these clients to identify them as trusted computers. By
default, the site configuration automatically approves clients from the same Active
Directory forest, trusted forests, and connected Microsoft Entra tenants. This default
behavior means that you don't have to manually approve each client. Manually approve
workgroup computers or clients from an untrusted forest that you trust, and any other
unapproved computers that you trust.

  ） Important

  Although some management functions might work for unapproved clients, this is
  an unsupported scenario for Configuration Manager.

You don't have to approve clients that always communicate to site systems using HTTPS,
or clients that use a PKI certificate when they communicate to site systems using HTTP.
These clients establish trust by using the PKI certificates.

Block or unblock
Block a client that you no longer trust. Blocking prevents the client from receiving policy,
and prevents site systems from communicating with the client.

  ） Important

  Blocking a client only prevents communication from the client to Configuration
  Manager site systems. It doesn't prevent communication to other devices. When
  the client communicates to site systems by using HTTP instead of HTTPS, there are
  some security limitations.

You can also unblock a client that is blocked.

For more information, see Determine whether to block clients.

Clear required PXE deployments
You can redeploy a required PXE deployment by clearing the status of the last PXE
deployment assigned to a Configuration Manager collection or a computer. This action
resets the status of that deployment and reinstalls the most recent required
deployments.

For more information, see Use PXE to deploy Windows over the network.

<!-- p.2335 -->

Client notification
For more information, see Client notifications.

Endpoint Protection
For more information, see Client notifications.

Edit primary users
View users of this device in the last 90 days, or specify the primary users of this device.

For more information, see Link users and devices with user device affinity.

Wipe a mobile device
You can wipe mobile devices that support the wipe command. This action permanently
removes all data on the mobile device, including personal settings and personal data.
Typically, this action resets the mobile device back to factory defaults. Wipe a mobile
device when it's no longer trusted. For example, if the device is lost or stolen.

   Tip

  Check the manufacturer's documentation for more information about how the
  mobile device processes a remote wipe command.

There's often a delay until the mobile device receives the wipe command:

     If the mobile device is enrolled by Configuration Manager, the client receives the
     command when it downloads its client policy.

     If the mobile device is managed by the Exchange Server connector, it receives the
     command when it synchronizes with Exchange.

To monitor when the device receives the wipe command, use the Wipe Status column.
Until the device sends a wipe acknowledgment to Configuration Manager, you can
cancel the wipe command.

Retire a mobile device
The Retire option is supported only by mobile devices enrolled by on-premises MDM.

<!-- p.2336 -->

For more information, see Help protect your data with remote wipe, remote lock, or
passcode reset.

Change ownership
If a device isn't domain-joined and doesn't have the Configuration Manager client
installed, use this option to change the ownership to Company or Personal.

You can use this value in application requirements to control deployments, and to
control how much inventory is collected from users' devices.

You may need to add the Device Owner column to the view by right-clicking any
column heading and choosing it.

Delete

  ２ Warning

  Don't delete a client if you want to uninstall the Configuration Manager client or
  remove it from a collection.

The Delete action manually removes the client record from the Configuration Manager
database. Only use this action to troubleshoot a problem. If you delete the object, but
the client is still installed and communicating with the site, Heartbeat Discovery
recreates the client record. It reappears in the Configuration Manager console, although
the client history and any previous associations are lost.

  ７ Note

  When you delete a mobile device client that was enrolled by Configuration
  Manager, this action also revokes the issued PKI certificate. This certificate is then
  rejected by the management point, even if IIS doesn't check the certificate
  revocation list (CRL).

  Certificates on mobile device legacy clients are not revoked when you delete these
  clients.

To uninstall the client, see Uninstall the Configuration Manager client.

To assign the client to a new primary site, see How to assign clients to a site.

<!-- p.2337 -->

To remove the client from a collection, reconfigure the collection properties. For more
information, see How to manage collections.

Refresh
Refresh the console view with the latest data in the database. For example, if a device
appears in the list from discovery, but doesn't show as installed. After you install the
client and make sure it's assigned to the site, select Refresh.

Properties
View the discovery data and deployments targeted for the client.

Switch to the Variables tab to configure variables that task sequences use to deploy an
OS to the device. For more information, see Create task sequence variables for devices
and collections.

Starting in version 2111, switch to the Custom properties tab to manually set custom
properties on the device for reporting or to create collections. For more information, see
Custom properties for devices.

Manage clients from the Device Collections
node
Many of the tasks that are available for devices in the Devices node are also available on
collections. The console automatically applies the operation to all eligible devices in the
collection. This action on an entire collection generates more network packets and
increases CPU usage on the site server.

Consider the following questions before you run collection-level tasks. Once started, you
can't stop the task from the console.

     How many devices are in the collection?
     Are the devices connected by low-bandwidth network connections?
     How much time does this task need to complete for all the devices?

For more information, see How to manage collections.

Restart clients

<!-- p.2338 -->

Use the Configuration Manager console to identify clients that require a restart. Then
use a client notification action to restart them.

   Tip

  Enable automatic client upgrade to keep your clients up-to-date with less effort.
  For more information, see About automatic client upgrade.

To identify devices that are pending a restart, go to the Assets and Compliance
workspace in the Configuration Manager console and select the Devices node. Then
view the status for each device in the details pane in a new column named Pending
Restart. Each device has one or more of the following values:

     No: there's no pending restart
     Configuration Manager: this value comes from the client reboot coordinator
     component (RebootCoordinator.log)
     File rename: this value comes from Windows reporting a pending file rename
     operation ( HKLM\SYSTEM\CurrentControlSet\Control\Session Manager,
     PendingFileRenameOperations )

     Windows Update: this value comes from the Windows Update Agent reporting a
     pending restart is required for one or more updates
     ( HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto
     Update\RebootRequired )

     Add or remove feature: this value comes from the Windows component-based
     servicing reporting the addition or removal of a Windows feature requires a restart
     ( HKLM\Software\Microsoft\Windows\CurrentVersion\Component Based
     Servicing\Reboot Pending )

Create the client notification to restart a device
   1. Select the device you want to restart within a collection in the Device Collections
     node of the console.
   2. In the ribbon, select Client Notification, and then select Restart. An information
     window opens about the restart. Select OK to confirm the restart request.

When the notification is received by a client, a Software Center notification window
opens to inform the user about the restart. By default, the restart occurs after 90
minutes. You can modify the restart time by configuring client settings. Settings for the
restart behavior are found on the Computer restart tab of the default settings.

<!-- p.2339 -->

Configure the client content cache
The client cache stores temporary files for when clients install applications and
programs. Software updates also use the client cache, but always attempt to download
to the cache whatever the size setting. Configure the cache settings, such as size and
location, when you manually install the client, when you use client push installation, or
after installation.

For more information, see Configure the client content cache.

Uninstall the client
You can uninstall the Configuration Manager client software from a computer by using
CCMSetup.exe with the /Uninstall property. Run CCMSetup.exe on an individual
computer from the command prompt, or deploy a package to uninstall the client for a
collection of computers.

  ７ Note

  You can't uninstall the Configuration Manager client from a mobile device. If you
  must remove the Configuration Manager client from a mobile device, you must
  wipe the device, which deletes all data on the mobile device.

   1. Open a Windows command prompt as an administrator. Change the folder to the
      location in which CCMSetup.exe is located, for example: cd %windir%\ccmsetup

   2. Run the following command: CCMSetup.exe /uninstall

   Tip

  The uninstall process displays no results on the screen. To verify that the client
  successfully uninstalls, see the following log file:
   %windir%\ccmsetup\logs\CCMSetup.log

  If you need to wait for the uninstall process to complete before doing something
  else, run Wait-Process CCMSetup in PowerShell. This command can pause a script
  until the CCMSetup process completes.

Starting in version 2111, when you uninstall the client it also removes the client
bootstrap, ccmsetup.msi, if it exists.

<!-- p.2340 -->

Manage conflicting records
Configuration Manager uses the hardware identifier to attempt to identify clients that
might be duplicates and alert you to the conflicting records. For example, if you reinstall
a computer, the hardware identifier would be the same but the GUID used by
Configuration Manager might be changed.

Configuration Manager automatically resolves conflicts by using Windows
authentication of the computer account or a PKI certificate from a trusted source. When
Configuration Manager can't resolve the conflict of duplicate hardware identifiers, a
hierarchy setting determines the behavior.

Change the hierarchy setting for managing conflicting
records
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. In the ribbon, select Hierarchy Settings.

   3. Switch to the Client Approval and Conflicting Records tab, and select one of the
     following options:

           Automatically resolve conflicting records
           Manually resolve conflicting records

Manually resolve conflicting records
   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     System Status, and select the Conflicting Records node.

   2. Select one or more conflicting records, and then choose Conflicting Record.

   3. Select one of the following options:

           Merge: Combine the newly detected record with the existing client record.

           New: Create a new record for the conflicting client record.

           Block: Create a new record for the conflicting client record, but mark it as
           blocked.

Manage duplicate hardware identifiers

<!-- p.2341 -->

You can provide a list of hardware identifiers that Configuration Manager ignores for
PXE boot and client registration. This list helps to address two common issues:

   1. Many new devices don't include an onboard Ethernet port. Technicians use a USB-
     to-Ethernet adapter to establish a wired connection for purposes of OS
     deployment. These adapters are often shared because of cost and general
     usability. The site uses the MAC address of this adapter to identify the device. So
     reusing the adapter becomes problematic without other administrator actions
     between each deployment. To reuse the adapter in this scenario, exclude its MAC
     address.

   2. While the SMBIOS attribute should be unique, some specialty hardware devices
     have duplicate identifiers. Exclude this duplicate identifier and rely on the unique
     MAC address of each device.

Use the following process to add hardware identifiers for Configuration Manager to
ignore:

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. On the Home tab of the ribbon, in the Sites group, choose Hierarchy Settings.

   3. Switch to the Client Approval and Conflicting Records tab. To add new hardware
     identifiers, choose Add in the Duplicate hardware identifiers section.

PowerShell for duplicate hardware IDs
You can use the following PowerShell cmdlets to automate the management of
duplicate hardware identifiers:

     Get-CMDuplicateHardwareIdGuid
     New-CMDuplicateHardwareIdGuid
     Remove-CMDuplicateHardwareIdGuid
     Get-CMDuplicateHardwareIdMacAddress
     New-CMDuplicateHardwareIdMacAddress
     Remove-CMDuplicateHardwareIdMacAddress

Start policy retrieval
A Configuration Manager client downloads its client policy on a schedule that you
configure as a client setting. You can also start on-demand policy retrieval from the
client. For example, for troubleshooting or testing situations.

<!-- p.2342 -->

     Client notification
     The client control panel
     Support Center
     A script

Start client policy retrieval with client notification
   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select Devices.

   2. Select the device that you want to download policy. On the Home tab of the
     ribbon, in the Device group, select Client Notification, and then choose Download
     Computer Policy.

       ７ Note

       You can also use client notification to start policy retrieval for all devices in a
       collection.

Start client policy retrieval from the Configuration
Manager client control panel
   1. Open the Configuration Manager control panel on the computer.

   2. Switch to the Actions tab. Select Machine Policy Retrieval & Evaluation Cycle to
     start the computer policy, and then select Run Now.

   3. Select OK to confirm the prompt.

   4. Repeat the previous steps for any other actions. For example, User Policy Retrieval
     & Evaluation Cycle for user client settings.

Start client policy retrieval with Support Center Client
Tools
Use Support Center Client Tools to request and view client policy. For more information,
see Support Center reference.

Start client policy retrieval by script
   1. Open a script editor, such as Notepad or Windows PowerShell ISE.

<!-- p.2343 -->

   2. Copy and insert the following sample PowerShell code into the file:

        PowerShell

        $trigger = "{00000000-0000-0000-0000-000000000021}"
        Invoke-WmiMethod -Namespace root\ccm -Class sms_client -Name
        TriggerSchedule $trigger

         Tip

        For more information about the schedule IDs, see Message IDs.

   3. Save the file with a .ps1 extension.

   4. Run the script on the client.

Next steps
Configure the content cache for clients

Client notification

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2344 -->

Configure the content cache for
Configuration Manager clients
Article • 12/16/2024

Applies to: Configuration Manager (current branch)

The client cache stores temporary files for when clients install applications and
programs. Software updates also use the client cache, but always attempt to download
to the cache whatever of the size setting. Configure the cache settings, such as size and
location, when you manually install the client, when you use client push installation, or
after installation.

You can specify the cache folder size using client settings in the Configuration Manager
console. For more information, see Client cache settings.

The default location for the Configuration Manager client cache is %windir%\ccmcache
and the default disk space is 5120 MB.

  ） Important

  Don't encrypt the folder used for the client cache. Configuration Manager can't
  download content to an encrypted folder.

About
The Configuration Manager client downloads the content for required software soon
after the deployment's available time but waits to run it until the deployment's
scheduled time. At the scheduled time, the Configuration Manager client checks to see
whether the content is available in the cache. If content is in the cache and it's the
correct version, the client uses the cached content. When the required version of the
content changes, or if the client deletes the content to make room for another package,
the client downloads the content to the cache again.

If the client attempts to download content for a program or application that's greater
than the size of the cache, the deployment fails because of insufficient cache size. The
client generates status message 10050 for insufficient cache size. If you increase the
cache size later, the result is:

      For a required program: The client doesn't automatically retry to download the
      content. Redeploy the package and program to the client.

<!-- p.2345 -->

      For a required application: The client automatically retries to download the content
      when it downloads its client policy.

If the client attempts to download content that's less than the size of the cache, but the
cache is full, all required deployments keep retrying until:

      The cache space is available
      The download times out
      The retry count reaches its limit

If you later increase the cache size, the client attempts to download the content again
during the next retry interval. The client tries to download the content every four hours
until it tries 18 times.

Cached content isn't automatically deleted and is only removed if new content requires
its disk space. It remains in the cache for the configured number of minutes after the
client uses that content. If you configure the content with the option to persist content
in the client cache, the client doesn't automatically delete it. If the cache space is used
by content that was downloaded within the configured number of minutes, and the
client must download new content, either increase the cache size or choose the option
to delete persisted cache content. For more information, see About client settings.

  ） Important

  Don't manually delete files from the client cache folder using Windows Explorer or
  the command line. This action can cause issues with the Configuration Manager
  client. The client manages the cache and tracks the content apart from the file
  system. Always use a supported method to delete files in the cache.

For applications only, if the content for a related deployment currently exists in the
cache, then the client downloads only new or changed files. Related deployments
include those deployments for older revisions of the same deployment type and
superseded applications.

Configure
Use the following procedures to configure the client cache during manual client
installation or after you install the client.

Configure the cache during manual client installation

<!-- p.2346 -->

Run the CCMSetup.exe command from the install source location and specify the
following properties that you require, and separated by spaces:

     DISABLECACHEOPT

     SMSCACHEDIR

     SMSCACHEFLAGS

  ７ Note

  Use the cache size settings available in Client Settings in the Configuration
  Manager console instead of SMSCACHESIZE. For more information, see Client
  cache settings.

For more information about how to use these command-line properties for
CCMSetup.exe, see About client installation properties.

Configure the cache during client push installation
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. Select the appropriate site. On the Home tab of the ribbon, in the Settings group,
     select Client Installation Settings, and choose Client Push Installation. Switch to
     the Installation Properties tab.

   3. Specify the following properties, separated by spaces:

           DISABLECACHEOPT

           SMSCACHEDIR

           SMSCACHEFLAGS

       ７ Note

       Use the cache size settings available in Client Settings in the Configuration
       Manager console instead of SMSCACHESIZE. For more information, see Client
       cache settings.

For more information about how to use these command-line properties for
CCMSetup.exe, see About client installation properties.

<!-- p.2347 -->

Configure the cache on the client computer
   1. On the client computer, open the Configuration Manager control panel.

   2. Switch to the Cache tab. Set the space and location properties. The default location
     is %windir%\ccmcache .

   3. To delete the files in the cache folder, choose Delete Files.

        ） Important

        Don't manually delete files from the ccmcache folder using Windows Explorer
        or the command line. This action can cause issues with the Configuration
        Manager client. The client manages the cache and tracks the content apart
        from the file system. Always use a supported method to delete files in the
        cache. For example, the Delete Files option on the control panel.

Configure client cache size in Client Settings
Adjust the size of the client cache without having to reinstall the client. Use the cache
size settings available in Client Settings in the Configuration Manager console. For more
information, see Client cache settings.

Next steps
Client notification

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2348 -->

Client notification in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To take immediate action on remote clients, send a client notification action from the
Configuration Manager console. Start these actions on an individual device or on a
collection of devices.

Actions
The following actions are on the ribbon in the Device or Collection group of the Home
tab.

Install client
Opens the Install Client Wizard. This wizard uses client push installation to install a
Configuration Manager client. For more information, see Client push installation.

Permissions - Install client
This action requires the Modify Resource and Read permissions on the Collection
object.

The following built-in roles have these permissions by default:

       Application Administrator
       Full Administrator
       Infrastructure Administrator
       Operations Administrator
       OS Deployment Manager

Add these permissions to any custom roles that need to push the client.

Run script
Opens the Run Script wizard to run a PowerShell script on all of the clients in the
collection. For more information, see Create and run PowerShell scripts.

<!-- p.2349 -->

Permissions - Run script
This action requires the Run Script permission on the Collection object.

The following built-in roles have this permission by default:

     Full Administrator
     Infrastructure Administrator
     Operations Administrator

Add this permission to any custom roles that need to run scripts.

Start CMPivot
Starts CMPivot, which runs real-time queries against the targeted devices. For more
information, see CMPivot.

Permissions - Start CMPivot

This action requires the Run CMPivot permission on the Collection object.

Client notification
These actions are under the Client notification menu, on the ribbon in the Device or
Collection group of the Home tab. You can start a Client Notification from the Devices
node or within a collection membership view.

  ７ Note

  Starting in version 2203, you can perform client notification actions, including Run
  Scripts, from the Deployment Status view. Use the right-click menu on either a
  group of clients in a Category or a single client in the Asset details pane to display
  the client notification actions.

Permissions - Client notification

Client notification actions require the Notify Resource permission on the Collection
object. This permission applies to all actions under the Client notification menu.

The following built-in roles have this permission by default:

     Full Administrator

<!-- p.2350 -->

     Operations Administrator

Add this permission to any custom roles that need to use client notification actions.

Download computer policy
Refresh the device policy. For more information, see Initiate policy retrieval for a
Configuration Manager client.

Download user policy
Refresh the user policy.

Collect discovery data
Trigger clients to send a discovery data record (DDR). For more information, see
Heartbeat discovery.

Collect software inventory
Trigger clients to run a software inventory cycle. For more information, see Introduction
to software inventory.

Collect hardware inventory
Trigger clients to run a hardware inventory cycle. For more information, see Introduction
to hardware inventory.

Evaluate application deployments
Trigger clients to run an application deployment evaluation cycle. For more information,
see Schedule re-evaluation for deployments.

Evaluate software update deployments
Trigger clients to run a software updates deployment evaluation cycle. For more
information, see Introduction to software updates.

Switch to the next software update point

<!-- p.2351 -->

Trigger clients to switch to the next available software update point. For more
information, see Software update point switching.

Evaluate device health attestation
Trigger Windows 10 or later clients to check and send their latest device health state. For
more information, see Health attestation.

Check conditional access compliance
Trigger clients to check compliance for conditional access policies. For more information,
see Conditional access.

Wake Up
Trigger devices configured to support Wake-on-LAN to wake up using other devices on
the same subnet to send the Wake-on-LAN package. For more information, see How to
configure Wake on LAN.

Restart
Trigger the selected devices to restart. For more information, see Restart clients.

Client diagnostics
Use the following actions to help troubleshoot clients:

     Enable verbose logging: Change the global log level for the CCM component to
     verbose, and enable debug logging.

     Disable verbose logging: Change the global log level to default, and disable
     debug logging.

     Collect Client Logs: The site sends a client notification message to the selected
     clients to gather the CCM logs. The client sends the logs to the management point
     using the same channel as software inventory file collection. You don't need to
     enable software inventory in client settings.
        The size limit for the compressed client logs is 100 MB.
        Use Resource Explorer manage and view these files.

<!-- p.2352 -->

                                                                               

  ） Important

        These actions only change the log verbosity, not the size or history. More
        verbose logging can generate more log content.
        The management point role also uses the CCM component. If the targeted
        device is also a management point, this action also applies to that role.

For more information about these settings, see About log files.

Track the status of the task in the diagnostics.log on the client. When client logs are
collected, additional information is logged in MP_SinvCollFile.log on the management
point and sinvproc.log on the site server.

  ７ Note

  Starting in version 2107, you can inventory client log file settings such as log levels
  and size. Enable the hardware inventory class, Client Diagnostics
  (CCM_ClientDiagnostics). For more information, see Enable or disable existing
  hardware inventory classes.

Prerequisites - Client diagnostics
     Update the target client to the latest version.

     Your Configuration Manager administrative user needs the Notify resource
     permission.

     The following built-in roles have this permission by default:
        Full Administrator
        Infrastructure Administrator

     Add this permission to any custom roles that need to use client notification
     actions.

Cleanup aged client diagnostic files

<!-- p.2353 -->

Collected client logs are stored according to the software inventory file collection
settings. The files are stored on the site server in the Inboxes\sinv.box\FileCol directory.
There's no defined limit to the number of versions.

The maintenance task to delete aged diagnostic files varies depending on your
Configuration Manager version:

     Version 2010 and later uses the Delete Aged Collected Diagnostic Files site
     maintenance task to delete diagnostic files.
     Version 2006 and earlier uses the Delete Aged Collected Files site maintenance
     task to delete diagnostic files.

For more information, see Reference for maintenance tasks in Configuration Manager.

Endpoint Protection
The following actions are under the Endpoint Protection menu. This menu is on the
ribbon in the Collection group of the Home tab. When you select one or more devices,
these actions are on the Selected Object tab of the ribbon.

For more information, see Endpoint Protection in Configuration Manager.

Permissions - Endpoint Protection
This action requires the Enforce Security permission on the Collection object.

The following built-in roles have this permission by default:

     Full Administrator
     Endpoint Protection Manager
     Operations Administrator

Add this permission to any custom roles that need to trigger Endpoint Protection
actions.

Full Scan
Trigger Endpoint Protection or Windows Defender to run a full antimalware scan.

Quick Scan
Trigger Endpoint Protection or Windows Defender to run a quick antimalware scan.

<!-- p.2354 -->

Download Definition
Trigger Endpoint Protection or Windows Defender to download the latest antimalware
definitions.

Monitor client operations
Monitor the operations sent to clients by using the Client Operations node under the
Monitoring workspace. For some instances, you can cancel the operation by using the
Cancel option in the ribbon. Use the Delete option to remove the operation from the
console's view.

                                                                                 

Next steps
     How to manage clients

     How to manage collections

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2355 -->

Maintain Mac clients
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in January 2022, this feature of Configuration Manager is deprecated. For
  more information, see Mac computers.

Here are procedures for uninstalling Mac clients and for renewing their certificates.

Uninstalling the Mac client
   1. On a Mac computer, open a terminal window and navigate to the folder containing
      macclient.dmg.

   2. Navigate to the Tools folder and enter the following command-line:

      ./CMUninstall -c

        ７ Note

        The -c property instructs the client uninstall to also remove client crash logs
        and log files. We recommend this to avoid confusion if you later reinstall the
        client.

   3. If required, manually remove the client authentication certificate that Configuration
      Manager was using, or revoke it. CMUnistall doesn't remove or revoke this
      certificate.

Renewing the Mac client certificate
Use one of the following methods to renew the Mac client certificate:

      Renew certificate wizard

      Renew certificate manually

Renew certificate wizard

<!-- p.2356 -->

1. Configure the following values as strings in the ccmclient.plist file that controls
  when the Renew Certificate Wizard opens:

        RenewalPeriod1 - Specifies, in seconds, the first renewal period in which users
        can renew the certificate. The default value is 3,888,000 seconds (45 days).
        Don't configure a value less than 300, as the period will revert to the default.

        RenewalPeriod2 - Specifies, in seconds, the second renewal period in which
        users can renew the certificate. The default value is 259,200 seconds (3 days).
        If this value is configured and is greater than or equal to 300 seconds and is
        less than or equal to RenewalPeriod1, the value will be used. If
        RenewalPeriod1 is greater than 3 days, a value of 3 days will be used for
        RenewalPeriod2. If RenewalPeriod1 is less than 3 days, then RenewalPeriod2
        is set to the same value as RenewalPeriod1.

        RenewalReminderInterval1 - Specifies, in seconds, the frequency at which the
        Renew Certificate Wizard will be displayed to users during the first renewal
        period. The default value is 86,400 seconds (1 day). If
        RenewalReminderInterval1 is greater than 300 seconds and less than the
        value configured for RenewalPeriod1, then the configured value will be used.
        Otherwise, the default value of 1 day will be used.

        RenewalReminderInterval2 - Specifies, in seconds the frequency at which the
        Renew Certificate Wizard will be displayed to users during the second
        renewal period. The default value is 28,800 seconds (8 hours). If
        RenewalReminderInterval2 is greater than 300 seconds, less than or equal to
        RenewalReminderInterval1 and less than or equal to RenewalPeriod2, then
        the configured value will be used. Otherwise, a value of 8 hours will be used.

        Example: If the values are left as their defaults, 45 days before the certificate
        expires, the wizard will open every 24 hours. Within 3 days of the certificate
        expiring, the wizard will open every 8 hours.

        Example: Use the following command line, or a script, to set the first renewal
        period to 20 days.

        sudo defaults write com.microsoft.ccmclient RenewalPeriod1 1728000

2. When the Renew Certificate Wizard opens, the User name and Server name fields
  will typically be pre-populated and the user can just enter a password to renew the
  certificate.

     ７ Note

<!-- p.2357 -->

        If the wizard does not open, or if you accidentally close the wizard, click
        Renew from the Configuration Manager preference page to open the wizard.

Renew certificate manually
A typical validity period for the Mac client certificate is 1 year. Configuration Manager
doesn't automatically renew the user certificate that it requests during enrollment, so
you must use the following procedure to renew the certificate manually.

  ） Important

  If the certificate expires, you must uninstall, reinstall and then re-enroll the Mac
  client.

This procedure removes the SMSID, which is required to request a new certificate for the
same Mac computer. When you remove and replace the client SMSID, any stored client
history such as inventory is deleted after you delete the client from the Configuration
Manager console.

   1. Create and populate a device collection for the Mac computers that must renew
     the user certificates.

        ２ Warning

        Configuration Manager does not monitor the validity period of the certificate
        that it enrolls for Mac computers. You must monitor this independently from
        Configuration Manager to identify the Mac computers to add to this
        collection.

   2. In the Assets and Compliance workspace, start the Create Configuration Item
     Wizard.

   3. On the General page, specify the following information:

            Name:Remove SMSID for Mac

            Type:Mac OS X

   4. On the Supported Platforms page, ensure that all macOS X versions are selected.

   5. On the Settings page, choose New and then, in the Create Setting dialog box,
     specify the following information:

<!-- p.2358 -->

         Name:Remove SMSID for Mac

         Setting type:Script

         Data type:String

 6. In the Create Setting dialog box, for Discovery script, choose Add script to specify
   a script that discovers Mac computers with an SMSID configured.

 7. In the Edit Discovery Script dialog box, enter the following Shell Script:

      Shell

      defaults read com.microsoft.ccmclient SMSID

 8. Choose OK to close the Edit Discovery Script dialog box.

 9. In the Create Setting dialog box, for Remediation script (optional), choose Add
   script to specify a script that removes the SMSID when it's found on Mac
   computers.

10. In the Create Remediation Script dialog box, enter the following Shell Script:

      Shell

      defaults delete com.microsoft.ccmclient SMSID

11. Choose OK to close the Create Remediation Script dialog box.

12. On the Compliance Rules page of the wizard, click New, and then in the Create
   Rule dialog box, specify the following information:

         Name:Remove SMSID for Mac

         Selected setting: Choose Browse and then select the discovery script that
         you specified previously.

         In the following values field, enter The domain/default pair of
         (com.microsoft.ccmclient, SMSID) does not exist.

         Enable the option Run the specified remediation script when this setting is
         noncompliant.

13. Complete the Create Configuration Item Wizard.

<!-- p.2359 -->

 14. Create a configuration baseline that contains the configuration item that you have
     just created and deploy it to the device collection that you created in step 1.

     For more information about how to create and deploy configuration baselines, see
     How to create configuration baselines and How to deploy configuration baselines.

 15. On Mac computers that have the SMSID removed, run the following command to
     install a new certificate:

        Shell

        sudo ./CMEnroll -s <enrollment_proxy_server_name> -
        ignorecertchainvalidation -u <'user name'>

     When prompted, provide the password for the super user account to run the
     command and then the password for the Active Directory user account.

 16. To limit the enrolled certificate to Configuration Manager, on the Mac computer,
     open a terminal window and make the following changes:

     a. Enter the command sudo /Applications/Utilities/Keychain\
     Access.app/Contents/MacOS/Keychain\ Access

     b. In the Keychain Access dialog, in the Keychains section, choose System, and
     then, in the Category section, choose Keys.

     c. Expand the keys to view the client certificates. When you have identified the
     certificate with a private key that you have just installed, double-click the key.

     d. On the Access Control tab, choose Confirm before allowing access.

     e. Browse to /Library/Application Support/Microsoft/CCM, select CCMClient, and
     then choose Add.

     f. Choose Save Changes and close the Keychain Access dialog box.

 17. Restart the Mac computer.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2360 -->

Introduction to collections in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Collections help you organize resources into manageable units. You can create
collections to match your client management needs, and to perform operations on
multiple resources at one time.

Most management tasks rely on or require using one or more collections. Although you
can use the built-in collection of All Systems, using it for management tasks is not a best
practice. Create custom collections to more specifically identify the devices or users for a
task.

Built-in and custom collections appear in the User Collections and Device Collections
nodes in the Assets and Compliance workspace in the Configuration Manager console.

Collections that you have recently viewed appear in the Users node and in the Devices
node in the Assets and Compliance workspace.

Here are some examples of collection use:

                                                                                    ﾉ   Expand table

 Operation             Example

 Grouping              You can create collections that group resources based on your organization's
 resources             hierarchy.

                       For example, you could create a collection of all computers in the "London
                       Headquarters" Active Directory Organizational Unit (OU). For more
                       information about how to create this type of collection, see How to create
                       collections.

                       You could use this collection for operations such as configuring Endpoint
                       Protection settings, configuring device power management settings, or
                       installing the Configuration Manager client.

 Application           You can create a collection of all computers that do not have Microsoft
 deployment            Microsoft 365 Apps installed and then deploy it to all computers in that
                       collection.
