---
title: "Software update management documentation — pages 81-120"
type: reference
domain: sccm
slug: sccm-intune-configmgr-sum-p0081-0120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-sum-p0081-0120
family: sccm
documentKind: "doc"
abstract: "2. Select the central administration site or the stand-alone primary site. 3. On the Home tab, in the Settings group, click Configure Site Components, and then click Software Update Point. 4. On the Products tab, make sure the following products are selected for synchronization:"
---

# Software update management documentation — pages 81-120

<!-- p.81 -->

   2. Select the central administration site or the stand-alone primary site.
   3. On the Home tab, in the Settings group, click Configure Site Components, and
     then click Software Update Point.
   4. On the Products tab, make sure the following products are selected for
     synchronization:

           Windows Insider Pre-Release
           Windows 10, version 1903 and later

   5. On the Classifications tab, make sure the following classifications are selected for
     synchronization:

           Upgrades
           Security Updates
           Updates (optional)

   6. Click OK to close the Software Update Point Component Properties.

Upgrading Windows Insider devices
Once the upgrades for Windows Insiders are synchronized, you can see them from
Software Library > Windows Servicing > All Windows Feature Updates.

Deploy Feature Updates for Windows Insider to your target collection just like any other
upgrade. However, you'll want to keep the following items in mind when you're
deploying these Feature Updates:

     These upgrades will be applicable to all Windows 10 clients 1903 or earlier, with
     matching architecture, edition, and language.
     There are license terms, your deployment must accept the terms in order to install.
     Consider using the thread priority in client settings.
     Dynamic Update automatically installs critical updates, including the latest
     Cumulative Update, directly from Microsoft Update. This behavior started with
     Feature Updates for Windows 10 version 1903.
        You can explicitly disable Dynamic Update in client settings or with a
        setupconfig.ini file.
        For more information, see the Windows 10 Dynamic Update           blog post.

For more information on how to deploy upgrades, see Manage Windows as a service.

<!-- p.82 -->

Keeping Insider devices up-to-date
Cumulative Updates for Windows Insider will be available for WSUS and by extension for
Configuration Manager. These Cumulative Updates will be released at a frequency
similar to Windows Cumulative Updates. The Windows Insider Cumulative updates are in
the Windows Insider Pre-Release product category and classified as either Security
Updates or Updates. You can deploy the Cumulative Updates for Windows Insider using
your regular software update process like using automatic deployment rules or phased
deployments.

Extended Security Updates and Configuration
Manager
The Extended Security Updates (ESU)     program is a last resort option for customers
who need to run certain legacy Microsoft products past the end of support. It includes
Critical and/or Important security updates (as defined by the Microsoft Security
Response Center (MSRC)     ) for a maximum of three years after the product's End of
Extended Support date.

Products that are beyond their support lifecycle aren't supported for use with
Configuration Manager. This includes any products that are covered under the ESU
program. For example, Windows 7. Security updates released under the ESU program
will be published to Windows Server Update Services (WSUS). These updates will appear
in the Configuration Manager console. While products that are covered under the ESU
program are no longer supported for use with Configuration Manager, the latest
released version of Configuration Manager current branch can be used to deploy and
install Windows security updates released under the program.

Client management features not related to Windows software update management or
OS deployment will no longer be tested on the operating systems covered under the
ESU program and we don't guarantee that they'll continue to function. It's highly
recommended to upgrade or migrate to a current version of the operating systems as
soon as possible to receive client management support.

   Tip

  Starting in Configuration Manager 2010, you'll be notified in-console about devices
  with operating systems that are past the end of support date and that are no
  longer eligible to receive security updates. For more information, see Console
  notifications. This information is provided for your convenience and only for use
  internally within your company. You should not solely rely on this information to

<!-- p.83 -->

  confirm update or license compliance. Be sure to verify the accuracy of the
  information provided to you.

Next steps
Start software updates synchronization to retrieve software updates based on the new
criteria. For more information, see Synchronize software updates.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.84 -->

Manage settings for software updates
Applies to: Configuration Manager (current branch)

After you synchronize software updates in Configuration Manager, configure and verify the
settings in the following sections.

Client settings for software updates
After you install the software update point, software updates is enabled on clients by default.
The settings on the Software Updates page in client settings have default values. The client
settings are used site-wide. They affect when software updates are scanned for compliance,
and how & when software updates are installed on client computers. Before you deploy
software updates, verify that the client settings are appropriate for software updates at your
site.

   ） Important

          The Enable software updates on clients setting is enabled by default. If you clear
          this setting, Configuration Manager removes the existing deployment policies from
          the client under certain conditions.

        Starting with the September 2020 cumulative update, HTTP-based Windows Server
        Update Services (WSUS) servers are secure by default. A client scanning for updates
        against an HTTP-based WSUS isn't allowed to leverage a user proxy by default. If you still
        require a user proxy despite the security trade-offs, a new software updates client setting
        is available to allow these connections. For more information about the changes for
        scanning WSUS, see September 2020 changes to improve security for Windows devices
        scanning WSUS     . So the best security protocols are in place, Microsoft recommends that
        you use the TLS/SSL protocol to help secure your software update infrastructure.

For information about how to configure client settings, see How to configure client settings.

For more information about the client settings, see About client settings.

Software Updates Best Practices

Conflicting donfigurations

<!-- p.85 -->

The Configuration Manager client sets local group policies to control the software update
workflow and scan for update compliance. When domain group policy objects (GPO) are used
for Windows Updates, it overrides the equivalent setting used by our client. The client expects
specific registry values to remain in place without any other platform changing the settings.
Domain GPO's can cause the component to go into an error state, even if the setting is
perceived to be the same.

For example, if a domain group policy sets the WSUS Server, Configuration Manager can't
configure or access the setting and might not operate properly. This behavior causes clients to
have scan failures and issues reporting compliance back to the site.

Remove older deployments and software update groups
To optimize site performance and improve compliance accuracy, remove older deployments
and software update groups. Since updates are cumulative, there's no need to keep older
updates deployed. Keeping old deployments negatively affects your environment.

Remove any unnecessary Products & Categories in the
Software Update Properties
Selecting too many products & categories for sync can cause negative performance.
Remember, devices have to scan every update in the SUSDB, whether it's deployed or not. So,
only select products that are relevant and necessary.

Many products and categories shown in the list are only for WSUS. Configuration Manager
can't deploy them. So, don't select these items. Some examples include:

     Dynamic Updates
     Servicing Drivers
     Silverlight
     Legacy operating systems that are no longer supported, like Windows 7, Windows 8, etc.
     'Rollups' category, 'Feature Packs' category, 'Service Packs' category, etc.

Software Updates Scan Cycle and Deployment Cycle
When the scan cycle or deployment cycle client settings are less than the default of once per 7
days, it can have have negative performance effect because of excessive scanning. In general,
it's not necessary to scan more than once a week. Devices already have a built-in mechanism to
scan for updates when they receive a deployment.

Self Update

<!-- p.86 -->

When Automatic Updates is enabled on client computers, the Windows Update Agent (WUA)
automatically performs a self-update when a newer version becomes available or when there
are problems with a WUA component. When Automatic Updates isn't configured or is disabled,
and client computers have an earlier version of the WUA, the client computers must run the
WUA installation file.

Software updates properties
The software update properties provide information about software updates and associated
content. You can also use these properties to configure settings for software updates. When
you open the properties for multiple software updates, only the Maximum Run Time and
Custom Severity tabs are displayed.

Use the following procedure to open software update properties.

To open software update properties

   1. In the Configuration Manager console, click Software Library.

   2. In the Software Library workspace, expand Software Updates, and click All Software
     Updates.

   3. Select one or more software updates, and then, on the Home tab, click Properties in the
     Properties group.

        ７ Note

        On the All Software Updates node, Configuration Manager displays only the
        software updates that have a Critical and Security classification, and that have been
        released in the last 30 days.

Review software updates information
In software update properties, you can review detailed information about a software update.
The detailed information isn't shown when you select more than one software update. The
following sections describe the information that is available for a selected software update.

Software update details
In the Update Details tab, you can view the following summary information about the selected
software update:

<!-- p.87 -->

     Bulletin ID: Specifies the bulletin ID that is associated with security software updates. You
     can find security bulletin details by searching on the bulletin ID on the Microsoft Security
     Response Center     Web page.

  ７ Note

  The way Microsoft documents security updates is changing. The previous model used
  security bulletin webpages and included security bulletin ID numbers (e.g. MS16-XXX) as a
  pivot point. This form of security update documentation, including bulletin ID numbers, is
  being retired and replaced with the Security Update Guide. Instead of bulletin IDs, the new
  guide pivots on vulnerability ID numbers and KB Article ID numbers. For more
  information, see the Security Update Guide FAQs       .

     Article ID: Specifies the article ID for the software update. The referenced article provides
     more detailed information about the software update and the issue that the software
     update fixes or improves.

     Date revised: Specifies the date that the software update was last modified.

     Maximum severity rating: Specifies the vendor-defined severity rating for the software
     update.

     Description: Provides an overview of what condition the software update fixes or
     improves.

     Applicable languages: Lists the languages for which the software update is applicable.

     Affected products: Lists the products for which the software update is applicable.

Content information
In the Content Information tab, review the following information about the content that is
associated with the selected software update:

     Content ID: Specifies the content ID for the software update.

     Downloaded: Indicates whether Configuration Manager has downloaded the software
     update files.

     Language: Specifies the languages for the software update.

     Source Path: Specifies the path to the software update source files.

     Size (MB): Specifies the size of the software update source files.

<!-- p.88 -->

Custom bundle information
In the Custom Bundle Information tab, review the custom bundle information for the software
update. When the selected software update contains bundled software updates that are
contained in the software update file, they are displayed in the Bundle information section.
This tab doesn't show bundled software updates that are displayed in the Content Information
tab, such as update files for different languages.

Supersedence information

On the Supersedence Information tab, you can view the following information about the
supersedence of the software update:

        This update has been superseded by the following updates: Specifies the software
        updates that supersede this update, which means that the updates listed are newer. In
        most cases, you deploy one of the software updates that supersedes the software update.
        The software updates that are displayed in the list contain hyperlinks to webpages that
        provide more information about the software updates. When this update isn't
        superseded, None is displayed.

        This update supersedes the following updates: Specifies the software updates that are
        superseded by this software update, which means this software update is newer. In most
        cases, you deploy this software update to replace the superseded software updates. The
        software updates that are displayed in the list contain hyperlinks to web pages that
        provide more information about the software updates. When this update doesn't
        supersede any other update, None is displayed.

Configure software updates settings
In the properties, you can configure software update settings for one or more software
updates. You can configure most software update settings only at the central administration
site or stand-alone primary site. The following sections help you to configure settings for
software updates.

Set maximum run time
In the Maximum Run Time tab, set the maximum amount of time a software update is allotted
to complete on client computers. If the update takes longer than the maximum run-time value,
Configuration Manager creates a status message and stops the software updates installation.
You can configure this setting only on the central administration site or a stand-alone primary
site.

<!-- p.89 -->

Configuration Manager also uses this setting to determine whether to initiate the software
update installation within a configured maintenance window. If the maximum run-time value is
greater than the available remaining time in the maintenance window, the software updates
installation is postponed until the start of the next maintenance window. When there are
multiple software updates to be installed on a client computer with a configured maintenance
window (timeframe), the software update with the lowest maximum run time installs first. Then,
the software update with the next lowest maximum run time installs next, and so on. Before it
installs each software update, the client verifies that the available maintenance window
provides enough time to install the software update. After a software update starts installing, it
continues to install, even if the installation goes beyond the end of the maintenance window.
For more information about maintenance windows, see the How to use maintenance windows.

On the Maximum Run Time tab, you can view and configure the following settings:

     Maximum run time: Specifies the maximum number of minutes allotted for a software
     update installation to complete before Configuration Manager stops the installation. This
     setting also determines if there's enough available time remaining to install the update
     before the end of a maintenance window. For service packs, the default setting is 60
     minutes. For other software update types, if you did a fresh install of Configuration
     Manager version 1511 or higher, the default is 10 minutes. It's 5 minutes when you
     upgraded from a previous version. Values can range from 5 to 9999 minutes.

  ） Important

  Be sure to set the maximum run time value smaller than the configured maintenance
  window time. Or, increase the maintenance window time to a value greater than the
  maximum run time. Otherwise, the software update installation won't initiate.

Set custom severity
In the properties for a software update, you can use the Custom Severity tab to configure
custom severity values for the software updates. This feature can be necessary if the predefined
severity values don't meet your needs. The custom values are listed in the Custom Severity
column in the Configuration Manager console. You can sort the software updates by the
defined custom severity values and can also create queries & reports that can filter on these
values. You can configure this setting only on the central administration site or stand-alone
primary site.

You can configure the following settings on the Custom Severity tab.

<!-- p.90 -->

      Custom severity: Sets a custom severity value for the software updates. Select Critical,
      Important, Moderate, or Low from the list. By default, the custom severity value is empty.

CRL checking for software updates
By default, the certificate revocation list (CRL) isn't checked when verifying the signature on
Configuration Manager software updates. Checking the CRL each time a certificate is used
offers more security against using a certificate that has been revoked. But, it introduces a
connection delay and incurs additional processing on the computer performing the CRL check.

If used, CRL checking must be enabled on the Configuration Manager consoles that process
software updates.

To enable CRL checking

On the computer performing the CRL check, from the product DVD, run the following
command from a command prompt:

 Windows Command Prompt
 \SMSSETUP\BIN\X64\\**<*language*>**\UpdDwnldCfg.exe /checkrevocation

For example, for English (US) run \SMSSETUP\BIN\X64\00000409\UpdDwnldCfg.exe
/checkrevocation .

 Last updated on 12/08/2025

<!-- p.91 -->

Tutorial: Configure a software update
point to use TLS/SSL with a PKI
certificate
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuring Windows Server Update Services (WSUS) servers and their corresponding
software update points (SUP) to use TLS/SSL may reduce the ability of a potential
attacker to remotely compromise a client and elevate privileges. To ensure that the best
security protocols are in place, we highly recommend that you use the TLS/SSL protocol
to help secure your software update infrastructure. This article walks you through the
steps required to configure each of your WSUS servers and the software update point to
use HTTPS. For more information about securing WSUS, see the Secure WSUS with the
Secure Sockets Layer Protocol article in the WSUS documentation.

In this tutorial, you will:

 ＂ Obtain a PKI certificate, if needed
 ＂ Bind the certificate to the WSUS Administration website
 ＂ Configure the WSUS web services to require SSL
 ＂ Configure the WSUS application to use SSL
 ＂ Verify the WSUS console connection can use SSL
 ＂ Configure the software update point to require SSL communication to the WSUS
     server
 ＂ Verify functionality with Configuration Manager

Considerations and limitations
WSUS uses TLS/SSL to authenticate client computers and downstream WSUS servers to
the upstream WSUS server. WSUS also uses TLS/SSL to encrypt update metadata. WSUS
doesn't use TLS/SSL for an update's content files. The content files are signed and the
hash of the file is included in the update's metadata. Before the files are downloaded
and installed by the client, both the digital signature and hash are checked. If either
check fails, the update won't be installed.

Consider the following limitations when you use TLS/SSL to secure a WSUS deployment:

      Using TLS/SSL increases the server workload. You should expect a small
      performance loss from encrypting all the metadata that is sent over the network.

<!-- p.92 -->

     If you use WSUS with a remote SQL Server database, the connection between the
     WSUS server and the database server isn't secured by TLS/SSL. If the database
     connection must be secured, consider the following recommendations:
           Move the WSUS database to the WSUS server.
           Move the remote database server and the WSUS server to a private network.
           Deploy Internet Protocol security (IPsec) to help secure network traffic.

When configuring WSUS servers and their software update points to use TLS/SSL, you
may want to phase in the changes for large Configuration Manager hierarchies. If you
choose to phase in these changes, start at the bottom of the hierarchy and move
upwards ending with the central administration site.

Prerequisites
This tutorial covers the most common method to obtain a certificate for use with
Internet Information Services (IIS). Whichever method your organization uses, ensure
that the certificate meets the PKI certificate requirements for a Configuration Manager
software update point. As with any certificate, the certificate authority must be trusted
by devices communicating with the WSUS server.

     A WSUS server with the software update point role installed
     Verify you've followed best practices on disabling recycling and configuring
     memory limits for WSUS before enabling TLS/SSL.
     One of the two following options:
           An appropriate PKI certificate already in the WSUS server's Personal certificate
           store.
           The ability to request and obtain an appropriate PKI certificate for the WSUS
           server from your Enterprise root certificate authority (CA).
              By default, most certificate templates including the WebServer certificate
              template will only issue to Domain Admins. If the logged in user isn't a
              domain admin, their user account will need to be granted the Enroll
              permission on the certificate template.

Obtain the certificate from the CA if needed
If you already have an appropriate certificate in the WSUS server's Personal certificate
store, skip this section and start with the Bind the certificate section. To send a certificate
request to your internal CA to install a new certificate, follow the instructions in this
section.

<!-- p.93 -->

1. From the WSUS server, open an administrative command prompt and run
  certlm.msc . Your user account needs to be a local administrator to manage

  certificates for the local computer.

  The Certificate Manager tool for the local device appears.

2. Expand Personal, then right-click on Certificates.

3. Select All Tasks then Request New Certificate.

4. Choose Next to begin certificate enrollment.

5. Choose the type of certificate to enroll. The certificate purpose is Server
  Authentication and the Microsoft certificate template to use is Web Server or a
  custom template that has Server Authentication specified as Enhanced Key
  Usage. You may be prompted for additional information to enroll the certificate.
  Typically, you'll specify the following information at minimum:

        Common name: Found on the Subject tab, set the value to the WSUS server's
        FQDN.
        Friendly name: Found on the General tab, set the value to a descriptive name
        to help you identify the certificate later.

6. Select Enroll then Finish to complete the enrollment.

<!-- p.94 -->

   7. Open the certificate if you want to see details about it such as the certificate's
     thumbprint.

   Tip

  If your WSUS server is internet facing, you'll need the external FQDN in the Subject
  or Subject Alternative Name (SAN) in your certificate.

Bind the certificate to the WSUS Administration
site
Once you have the certificate in the WSUS server's personal certificate store, bind it to
the WSUS Administration site in IIS.

   1. On the WSUS server, open Internet Information Services (IIS) Manager.

   2. Go to Sites > WSUS Administration.

   3. Select Bindings from either the action menu or by right-clicking on the site.

   4. In the Site Bindings window, select the line for https, then select Edit....

           Don't remove the HTTP site binding. WSUS uses HTTP for the update content
           files.

   5. Under the SSL certificate option, choose the certificate to bind to the WSUS
     Administration site. The certificate's friendly name is shown in the drop-down
     menu. If a friendly name wasn't specified, then the certificate's IssuedTo field is
     shown. If you're not sure which certificate to use, select View and verify the
     thumbprint matches the one you obtained.

<!-- p.95 -->

   6. Select OK when you're done, then Close to exit the site bindings. Keep Internet
     Information Services (IIS) Manager open for the next steps.

Configure the WSUS web services to require
SSL
   1. In IIS Manager on the WSUS server, go to Sites > WSUS Administration.

   2. Expand the WSUS Administration site so you see the list of web services and virtual
     directories for WSUS.

   3. For each of the below WSUS web services:

           ApiRemoting30
           ClientWebService
           DSSAuthWebService
           ServerSyncWebService
           SimpleAuthWebService

     Make the following changes:
      a. Select SSL Settings.
     b. Enable the Require SSL option.
      c. Verify the Client certificates option is set to Ignore.
     d. Select Apply.

Don't set the SSL settings at the top-level WSUS Administration site since certain
functions, such as content, need to use HTTP.

Configure the WSUS application to use SSL
Once the web services are set to require SSL, the WSUS application needs to be notified
so it can do some additional configuration to support the change.

   1. Open an admin command prompt on the WSUS server. The user account running
     this command must be a member of either the WSUS Administrators group or the
     local Administrators group.

   2. Change directory to the tools folder for WSUS:

     cd "c:\Program Files\Update Services\Tools"

   3. Configure WSUS to use SSL with the following command:

<!-- p.96 -->

     WsusUtil.exe configuressl server.contoso.com

     Where server.contoso.com is the FQDN of the WSUS server.

   4. WsusUtil returns the URL of the WSUS server with the port number specified at the
     end. The port will be either 8531 (default) or 443. Verify the URL returned is what
     you expected. If something was mistyped, you can run the command again.

   Tip

  If your WSUS server is internet facing, specify the external FQDN when running
  WsusUtil.exe configuressl .

Verify the WSUS console can connect using SSL
The WSUS console uses the ApiRemoting30 web service for connection. The
Configuration Manager software update point (SUP) also uses this same web service to
direct WSUS to take certain actions such as:

     Initiating a software update synchronization
     Setting the proper upstream server for WSUS, which is dependent on where the
     SUP's site resides in your Configuration Manager hierarchy
     Adding or removing products and classifications for synchronization from the
     hierarchy's top-level WSUS server.
     Removing expired updates

Open the WSUS console to verify you can use an SSL connection to the WSUS server's
ApiRemoting30 web service. We'll test some of the other web services later.

   1. Open the WSUS console and select Action > Connect to Server.

   2. Enter the FQDN of the WSUS server for the Server name option.

   3. Choose the Port number returned in the URL from WSUSutil.

<!-- p.97 -->

   4. The Use Secure Sockets Layer (SSL) to connect to this server option automatically
     enables when either 8531 (default) or 443 are chosen.

   5. If your Configuration Manager site server is remote from the software update
     point, launch the WSUS console from the site server and verify the WSUS console
     can connect over SSL.

           If the remote WSUS console can't connect, it likely indicates a problem with
           either trusting the certificate, name resolution, or the port being blocked.

Configure the software update point to require
SSL communication to the WSUS server
Once WSUS is set up to use TLS/SSL, you'll need to update the corresponding
Configuration Manager software update point to require SSL too. When you make this
change, Configuration Manager will:

     Verify it can configure the WSUS server for the software update point
     Direct clients to use the SSL port when they're told to scan against this WSUS
     server.

To configure the software update point to require SSL communication to the WSUS
server, do the following steps:

   1. Open the Configuration Manager console and connect to either your central
     administration site or the primary site server for the software update point you
     need to edit.

   2. Go to Administration > Overview > Site Configuration > Servers and Site System
     Roles.

   3. Select the site system server where WSUS is installed, then select the software
     update point site system role.

<!-- p.98 -->

  4. From the ribbon, choose Properties.

  5. Enable the Require SSL communication to the WSUS server option.

  6. In the WCM.log for the site, you'll see the following entries when you apply the
     change:

       SCF change notification triggered.
       Populating config from SCF
       Setting new configuration state to 1 (WSUS_CONFIG_PENDING)
       ...
       Attempting connection to local WSUS server
       Successfully connected to local WSUS server
       ...
       Setting new configuration state to 2 (WSUS_CONFIG_SUCCESS)

Log file examples have been edited to remove unneeded information for this scenario.

Verify functionality with Configuration
Manager

Verify the site server can sync updates
  1. Connect the Configuration Manager console to the top-level site.

<!-- p.99 -->

   2. Go to Software Library > Overview > Software Updates > All Software Updates.

   3. From the ribbon, select Synchronize Software Updates.

   4. Select Yes to the notification asking if you want to initiate a site-wide
     synchronization for software updates.

           Since the WSUS configuration changed, a full software updates
           synchronization will occur rather than a delta synchronization.

   5. Open the wsyncmgr.log for the site. If you're monitoring a child site, you'll need to
     wait for the parent site to finish synchronization first. Verify that the server syncs
     successfully by reviewing the log for entries similar to the following:

        Starting Sync
        ...
        Full sync required due to changes in main WSUS server location.
        ...
        Found active SUP SERVER.CONTOSO.COM from SCF File.
        ...
        https://SERVER.CONTOSO.COM:8531
        ...
        Done synchronizing WSUS Server SERVER.CONTOSO.COM
        ...
        sync: Starting SMS database synchronization
        ...
        Done synchronizing SMS with WSUS Server SERVER.CONTOSO.COM

Verify a client can scan for updates
When you change the software update point to require SSL, Configuration Manager
clients receive the updated WSUS URL when it makes a location request for a software
update point. By testing a client, we can:

     Determine if the client trusts the WSUS server's certificate.
     If the SimpleAuthWebService and the ClientWebService for WSUS are functional.
     That the WSUS content virtual directory is functional, if the client happened to get
     a EULA during the scan

   1. Identify a client that scans against the software update point recently changed to
     use TLS/SSL. Use Run scripts with the below PowerShell script if you need help with
     identifying a client:

        PowerShell

<!-- p.100 -->

    $Last = (Get-CIMInstance -Namespace "root\CCM\Scanagent" -Class
    "CCM_SUPLocationList").LastSuccessScanPath
    $Current= Write-Output (Get-CIMInstance -Namespace "root\CCM\Scanagent"
    -Class "CCM_SUPLocationList").CurrentScanPath
    Write-Host "LastGoodSUP- $last"
    Write-Host "CurrentSUP- $current"

     Tip

    Open this script in community hub. For more information, see Direct links to
    community hub items.

2. Run a software update scan cycle on your test client. You can force a scan with the
  following PowerShell script:

    PowerShell

    Invoke-WMIMethod -Namespace root\ccm -Class SMS_CLIENT -Name
    TriggerSchedule "{00000000-0000-0000-0000-000000000113}"

     Tip

    Open this script in community hub. For more information, see Direct links to
    community hub items.

3. Review the client's ScanAgent.log to verify the message to scan against the
  software update point was received.

    Message received: '<?xml version='1.0' ?>
    <UpdateSourceMessage MessageType='ScanByUpdateSource'>
       <ForceScan>TRUE</ForceScan>
       <UpdateSourceIDs>
            <ID>{A1B2C3D4-1234-1234-A1B2-A1B2C3D41234}</ID>
       </UpdateSourceIDs>
     </UpdateSourceMessage>'

4. Review the LocationServices.log to verify that the client sees the correct WSUS
  URL. LocationServices.log

<!-- p.101 -->

        WSUSLocationReply : <WSUSLocationReply SchemaVersion="1
        ...
        <LocationRecord WSUSURL="https://SERVER.CONTOSO.COM:8531"
        ServerName="SERVER.CONTOSO.COM"
        ...
        </WSUSLocationReply>

   5. Review the WUAHandler.log to verify that the client can successfully scan.

        Enabling WUA Managed server policy to use server:
        https://SERVER.CONTOSO.COM:8531
        ...
        Successfully completed scan.

TLS certificate pinning for devices scanning
HTTPS-configured WSUS servers
(Introduced in 2103)

Starting in Configuration Manager 2103, you can further increase the security of HTTPS
scans against WSUS by enforcing certificate pinning. To fully enable this behavior, add
certificates for your WSUS servers to the new WindowsServerUpdateServices certificate
store on your clients and ensure certificate pinning is enabled through Client Settings.
For more information about the changes to the Windows Update Agent, see Scan
changes and certificates add security for Windows devices using WSUS for updates -
Microsoft Tech Community     .

Prerequisites for enforcing TLS certificate pinning for
Windows Update client
     Configuration Manager version 2103
     Ensure your WSUS servers and software update points are configured to use
     TLS/SSL
     Add the certificates for your WSUS servers to the new
     WindowsServerUpdateServices certificate store on your clients

        When using certificate pinning with a cloud management gateway (CMG), the
        WindowsServerUpdateServices store needs the CMG certificate. If clients switch

        from internet to VPN both the CMG and WSUS server certificates are needed in
        the WindowsServerUpdateServices store.

<!-- p.102 -->

  ７ Note

  Software update scans for devices will continue to run successfully using the
  default value of Yes for the Enforce TLS certificate pinning for Windows Update
  client for detecting updates client setting. This includes scans over both HTTP and
  HTTPS. The certificate pinning doesn't take effect until a certificate is in the client's
   WindowsServerUpdateServices store and the WSUS server is configured to use

  TLS/SSL.

Enable or disable TLS certificate pinning for devices
scanning HTTPS-configured WSUS servers
   1. From the Configuration Manager console, go to Administration > Client Settings.
   2. Choose the Default Client Settings or a custom set of client settings, then select
     Properties from the ribbon.
   3. Select the Software Updates tab in the Client settings
   4. Choose one of the following options for the Enforce TLS certificate pinning for
     Windows Update client for detecting updates setting:

             No: Don't enable enforcement of TLS certificate pinning for WSUS scanning
             Yes: Enables enforcement of TLS certificate pinning for devices during WSUS
             scanning (default)

   5. Verify clients can scan for updates.

Next steps
Deploy software updates

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.103 -->

Synchronize software updates from a
disconnected software update point
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When the software update point at the top-level site is disconnected from the Internet,
you must use the export and import functions of the WSUSUtil tool to synchronize
software updates metadata. You can choose an existing WSUS server not in your
Configuration Manager hierarchy as the synchronization source. This article provides
information about how to use the export and import functions of the WSUSUtil tool.

To export and import software updates metadata, you must export software updates
metadata from the WSUS database on a specified export server, then copy the locally
stored license terms files to the disconnected software update point, and then import
the software updates metadata to the WSUS database on the disconnected software
update point.

Use the following table to identify the export server in which to export the software
updates metadata.

                                                                                ﾉ   Expand table

 Software              Upstream update        Export server for a disconnected software update
 update point          source for connected   point
                       software update
                       points

 Central               Microsoft Update       Choose a WSUS server that is synchronized with
 administration        (Internet)             Microsoft Update by using the software update
 site                                         classifications, products, and languages that you
                       Existing WSUS server   need in your Configuration Manager environment.

 Stand-alone           Microsoft Update       Choose a WSUS server that is synchronized with
 primary site          (Internet)             Microsoft Update by using the software update
                                              classifications, products, and languages that you
                       Existing WSUS server   need in your Configuration Manager environment.

Before you start the export process, verify that software updates synchronization is
completed on the selected export server to ensure that the most recent software
updates metadata is synchronized. To verify that software updates synchronization has
completed successfully, use the following procedure.

<!-- p.104 -->

To verify that software updates synchronization has completed
successfully on the export server

   1. Open the WSUS Administration console and connect to the WSUS database on the
     export server.

   2. In the WSUS Administration console, click Synchronizations. A list of the software
     updates synchronization attempts are displayed in the results pane.

   3. In the results pane, find the latest software updates synchronization attempt and
     verify that it completed successfully.

  ） Important

       The WSUSUtil tool must be run locally on the export server to export the
       software updates metadata, and it also must be run on the disconnected
       software update point server to import the software updates metadata. In
       addition, the user that runs the WSUSUtil tool must be a member of the local
       Administrators group on each server.
       If you are using Windows Server 2012, ensure KB2819484         is installed on the
       WSUS servers.

Export process for software updates
The export process for software updates consists of two main steps: to copy the locally
stored license terms files to the disconnected software update point, and to export
software updates metadata from the WSUS database on the export server.

Use the following procedure to copy the local license terms metadata to the
disconnected software update point.

To copy local files from the export server to the disconnected
software update point server
   1. On the export server, navigate to the folder where software updates and the
     license terms for software updates are stored. By default, the WSUS server stores
     the files at <WSUSInstallationDrive>\WSUS\WSUSContent\, where
     WSUSInstallationDrive is the drive on which WSUS is installed.

<!-- p.105 -->

  2. Copy all files and folders from this location to the WSUSContent folder on the
    disconnected software update point server.

    Use the following procedure to export the software updates metadata from the
    WSUS database on the export server.

To export software updates metadata from the WSUS database on
the export server
  1. At the command prompt on the export server, navigate to the folder that contains
    WSUSutil.exe. By default, the tool is located at %ProgramFiles%\Update
    Services\Tools. For example, if the tool is located in the default location, type cd
    %ProgramFiles%\Update Services\Tools.

  2. Type the following to export the software updates metadata to a package file:

    wsusutil.exe export packagename logfile

    For example:

    wsusutil.exe export export.xml.gz export.log

    The format can be summarized as follows: WSUSutil.exe is followed by the export
    option, the name of the export .xml.gz file that is created during the export
    operation, and the name of a log file. WSUSutil.exe exports the metadata from the
    export server and creates a log file of the operation.

      ７ Note

      The package (.xml.gz file) and the log file name must be unique in the current
      folder.

  3. Move the export package to the folder that contains WSUSutil.exe on the import
    WSUS server.

      ７ Note

      If you move the package to this folder, the import experience can be easier.
      You can move the package to any location that is accessible to the import
      server, and then specify the location when you run WSUSutil.exe.

<!-- p.106 -->

Import software updates metadata
Use the following procedure to import software updates metadata from the export
server to the disconnected software update point.

  ） Important

  Never import any exported data from a source that you do not trust. If you import
  content from a source that you do not trust, it might compromise the security of
  your WSUS server.

To import metadata to the database of the import server

   1. At the command prompt on the import WSUS server, navigate to the folder that
     contains WSUSutil.exe. By default, the tool is located at %ProgramFiles%\Update
     Services\Tools.

   2. Type the following:

     wsusutil.exe import packagename logfile

     For example:

     wsusutil.exe import export.xml.gz import.log

     The format can be summarized as follows: WSUSutil.exe is followed by the import
     command, the name of package file (.xml.gz) that is created during the export
     operation, the path to the package file if it is in a different folder, and the name of
     a log file. WSUSutil.exe imports the metadata from the export server and creates a
     log file of the operation.

Next steps
After you synchronize software updates for the first time, or after there are new
classifications or products available, you must configure the new classifications and
products to synchronize software updates with the new criteria.

After you synchronize software updates with the criteria that you need, manage settings
for software updates.

<!-- p.107 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.108 -->

Synchronize Microsoft 365 Apps
updates from a disconnected software
update point
Article • 06/20/2024

Applies to: Configuration Manager (current branch)

Starting in Configuration Manager version 2002, you can use a tool to import Microsoft
365 Apps updates from an internet connected WSUS server into a disconnected
Configuration Manager environment. Previously when you exported and imported
metadata for software updated in disconnected environments, you were unable to
deploy Microsoft 365 Apps updates. Microsoft 365 Apps updates require additional
metadata downloaded from an Office API and the Office CDN, which isn't possible for
disconnected environments.

  ７ Note

  Starting on April 21, 2020, Office 365 ProPlus is being renamed to Microsoft 365
  Apps for enterprise. For more information, see Name change for Office 365
  ProPlus. You may still see references to the old name in the Configuration Manager
  console and supporting documentation while the console is being updated.

Prerequisites
      An internet connected WSUS server running a currently supported version of
      Windows Server.

      The WSUS server needs connectivity to these internet endpoints:
         officecdn.microsoft.com
         config.office.com

         clients.config.office.net
         go.microsoft.com

      Copy the OfflineUpdateExporter tool and its dependencies to the internet
      connected WSUS server.
         The tool and its dependencies are in the
         <ConfigMgrInstallDir>/tools/OfflineUpdateExporter directory.

<!-- p.109 -->

   The user running the tool must be part of the WSUS Administrators group.

   The directory created to store the Microsoft 365 Apps update metadata and
   content should have appropriate access control lists (ACLs) to secure the files.
      This directory must also be empty.

   Data being moved from the online WSUS server to the disconnected environment
   should be moved securely.

 ） Important

 Content will be downloaded for all Microsoft 365 Apps languages. Each update can
 have approximately 10 GB of content.

Synchronize then decline unneeded Microsoft
365 Apps updates
 1. On your internet connected WSUS, open the WSUS console.
 2. Select Options then Products and Classifications.
 3. In the Products tab, select Office 365 Client and select Updates in the
   Classifications tab.

                                                                                      

 4. Go to Synchronizations and select Synchronize Now to get the Microsoft 365
   Apps updates into WSUS.
 5. When the synchronization completes, decline any Microsoft 365 Apps updates that
   you don't want to deploy with Configuration Manager. You don't need to approve
   Microsoft 365 Apps updates in order for them to be downloaded.

<!-- p.110 -->

         Declining unwanted Microsoft 365 Apps updates in WSUS doesn't stop them
         from being exported during a WsusUtil.exe export, but it does stop the
         OfflineUpdateExporter tool from downloading the content for them.
         The OfflineUpdateExporter tool does the download of Microsoft 365 Apps
         updates for you. Other products will still need to be approved for download if
         you're exporting updates for them.
           Create a new update view in WSUS to easily see and decline unneeded
           Microsoft 365 Apps updates in WSUS.
 6. If you're approving other product updates for download and export, wait for the
   content download to complete before running WsusUtil.exe export and copying
   the contents of the WSUSContent folder. For more information, see Synchronize
   software updates from a disconnected software update point

Exporting the Microsoft 365 Apps updates
 1. Copy the OfflineUpdateExporter folder from Configuration Manager to the internet
   connected WSUS server.

         The tool and its dependencies are in the
         <ConfigMgrInstallDir>/tools/OfflineUpdateExporter directory.

 2. From a command prompt on the internet connected WSUS server, run the tool
   with the following usage: OfflineUpdateExporter.exe -O -D <destination path>

                                                                            ﾉ   Expand table

    OfflineUpdateExporter         Description
    Parameter

    -O                            -Office. Specifies product for updates export is Office 365
                                  or Microsoft 365 Apps

    -D                            -Destination. Destination is a required parameter and the
                                  entire path to the destination folder is needed.

         The OfflineUpdateExporter tool does the following:
           Connects to WSUS
           Reads the Microsoft 365 Apps update metadata in WSUS
           Downloads the content and any additional metadata needed by the
           Microsoft 365 Apps updates to the destination folder

 3. At the command prompt on the internet connected WSUS server, navigate to the
   folder that contains WsusUtil.exe. By default, the tool is located in

<!-- p.111 -->

   %ProgramFiles%\Update Services\Tools. For example, if the tool is located in the
   default location, type cd %ProgramFiles%\Update Services\Tools.

        The user that runs the WsusUtil tool must be a member of the local
        Administrators group on the server.

 4. Type the following to export the software updates metadata to a GZIP file:

   WsusUtil.exe export packagename logfile

   For example:

   WsusUtil.exe export export.xml.gz export.log

 5. Copy the export.xml.gz file to the top-level WSUS server on the disconnected
   network.

 6. If you approved updates for other products, copy the contents of the
   WSUSContent folder to the top-level disconnected WSUS server's WSUSContent
   folder.

 7. Copy the destination folder used for the OfflineUpdateExporter to the top-level
   Configuration Manager site server on the disconnected network.

Import the Microsoft 365 Apps updates
 1. On the disconnected top-level WSUS server, import the update metadata from the
   export.xml.gz you generated on the internet connected WSUS server.

   For example:

   WsusUtil.exe import export.xml.gz import.log

   By default, the WsusUtil.exe tool is located in %ProgramFiles%\Update
   Services\Tools.

 2. Once the import is complete, you'll need to configure a site control property on
   the disconnected top-level Configuration Manager site server. This configuration
   change points Configuration Manager to the content for Microsoft 365 Apps. To
   change the property's configuration:
   a. Copy the O365OflBaseUrlConfigured PowerShell script to the top-level
      disconnected Configuration Manager site server.
   b. Change "D:\Office365updates\content" to the full path of the copied directory
      containing the Microsoft 365 Apps content and metadata generated by
      OfflineUpdateExporter.

<!-- p.112 -->

          ） Important

          Only local paths work for the O365OflBaseUrlConfigured property.

     c. Save the script as O365OflBaseUrlConfigured.ps1
    d. From an elevated PowerShell window on the disconnected top-level
       Configuration Manager site server, run .\O365OflBaseUrlConfigured.ps1 .
     e. Restart the SMS_Executive service on the site server.

 3. In the Configuration Manager console, navigate to Administration > Site
    Configuration > Sites.

 4. Right-click on your top-level site, then select Configure Site Components >
    Software Update Point.

 5. In the Classifications tab, select Updates. In the Products tab, select Office 365
    Client.

 6. Synchronize software updates for Configuration Manager

 7. When the synchronization completes, use your normal process to deploy Microsoft
    365 Apps updates.

Proxy configuration
    Proxy configuration isn't natively built into the tool. If proxy is set in the Internet
    Options on the server where the tool is running, in theory it will be used and
    should function properly.
       From a command prompt, run netsh winhttp show proxy to see the configured
       proxy.

Modify O365OflBaseUrlConfigured property
 PowerShell

 # Name: O365OflBaseUrlConfigured.ps1
 #
 # Description: This sample sets the O365OflBaseUrlConfigured property for
 the SMS_WSUS_CONFIGURATION_MANAGER component on the top-level site.
 # This script must be run on the disconnected top-level Configuration
 Manager site server
 #
 # Replace "D:\Office365updates\content" with the full path to the copied
 directory containing all the Office metadata and content generated by the

<!-- p.113 -->

  OfflineUpdateExporter tool.
  # Only local paths work for the O365OflBaseUrlConfigured property.

  $PropertyValue = "D:\Office365updates\content"

  # Don't change any of the lines below
  $PropertyName = "O365OflBaseUrlConfigured"

  # Get provider instance
  $providerMachine = Get-WmiObject -namespace "root\sms" -class
  "SMS_ProviderLocation"

  if($providerMachine -is [system.array])
  {
      $providerMachine=$providerMachine[0]
  }

  $SiteCode = $providerMachine.SiteCode

  $component = gwmi -ComputerName $providerMachine.Machine -namespace
  root\sms\site_$SiteCode -query 'select comp.* from sms_sci_component comp
  join SMS_SCI_SiteDefinition sdef on sdef.SiteCode=comp.SiteCode where
  sdef.ParentSiteCode="" and
  comp.componentname="SMS_WSUS_CONFIGURATION_MANAGER"'
  $properties = $component.props

  Write-host "Updating $PropertyName property for site " $SiteCode

  foreach ($property in $properties)
  {
    if ($property.propertyname -eq $PropertyName)
    {
      Write-host "Current value for $PropertyName is $($property.value2)"
      $property.value2 = $PropertyValue
      Write-host "Updating value for $PropertyName to $($property.value2)"
      break
    }
  }

  $component.props = $properties
  $component.put()

Next steps
Add software updates to an update group

Feedback

<!-- p.114 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.115 -->

Download software updates
Article • 04/11/2023

Applies to: Configuration Manager (current branch)

There are several methods available to you for downloading software updates in
Configuration Manager. When you create an automatic deployment rule (ADR) or
manually deploy software updates, the software updates are downloaded to the content
library on the site server. Then, the software updates are copied to the content library on
the distribution points that are associated with the configured deployment package. If
you want to download the software updates before you deploy them, you can use the
Download Updates Wizard. Doing this will enable you to verify that the software
updates are available on distribution points before you deploy the software updates to
client computers.

  ７ Note

        Starting March 28, 2023, on-premises Windows 11, version 22H2 devices will
        receive quality updates via the Unified Update Platform (UUP). On-premises
        update management with Unified Update Platform (UUP) requires an
        additional 10 GB of space per Windows version and processor architecture for
        each version. For more information, see the UUP considerations section
        For information about monitoring content status, see the Content status
        monitoring.

Use the following procedure to download software updates by using the Download
Software Updates Wizard.

To download software updates

   1. In the Configuration Manager console, go to the Software Library workspace, and
      select the Software Updates node.

   2. Choose the software update to download by using one of the following methods:

            Select one or more software update groups from the Software Update
            Groups node. Then click Download in the ribbon.

            Select one or more software updates from All Software Updates node. Then
            click Download in the ribbon.

<!-- p.116 -->

         ７ Note

         In the All Software Updates node, Configuration Manager displays only
         software updates with a Critical and Security classification that have
         been released in the last 30 days.

          Tip

         Click Add Criteria to filter the software updates that are displayed in the
         All Software Updates node. Save search criteria that you often use, and
         then manage saved searches on the Search tab.

3. On the Deployment Package page of the Download Software Updates Wizard,
  configure the following settings:

       Select deployment package: Choose this setting to select an existing
       deployment package for the software updates that are in the deployment.

         ７ Note

         Software updates that the site has already downloaded to the selected
         deployment package won't be downloaded again.

       Create a new deployment package: Select this setting to create a new
       deployment package for the software updates in the deployment. Configure
       the following settings:

          Name: Specifies the name of the deployment package. The package must
          have a unique name that briefly describes the package content. It's limited
          to 50 characters.

          Description: Specify a description that provides information about the
          deployment package. The optional description is limited to 127 characters.

          Package source: Specifies the location of the software update source files.
          Type a network path for the source location, for example,
          \\server\sharename\path , or click Browse to find the network location.

          Create the shared folder for the deployment package source files before
          you proceed to the next page.

<!-- p.117 -->

             You can't use the specified location as the source of another software
             deployment package.

             You can change the package source location in the deployment
             package properties after Configuration Manager creates the
             deployment package. If you do, first copy the content from the original
             package source to the new package source location.

             The computer account of the SMS Provider and the user that's running
             the wizard to download the software updates must both have Write
             permissions to the download location. Restrict access to the download
             location. This restriction reduces the risk of attackers tampering with the
             software update source files.

          Enable binary differential replication: Enable this setting to minimize
          network traffic between sites. Binary differential replication (BDR) only
          updates the content that has changed in the package, instead of updating
          the entire package contents. For more information, see Binary differential
          replication.

4. On the Distribution Points page, specify the distribution points or distribution
  point groups to host the software update files. For more information about
  distribution points, see Distribution point configurations. This page is available
  only when you create a new software update deployment package.

5. The Distribution Settings page is available only when you create a new software
  update deployment package. Specify the following settings:

       Distribution priority: Use this setting to specify the distribution priority for
       the deployment package. The distribution priority applies when the
       deployment package is sent to distribution points at child sites. Deployment
       packages are sent in priority order: high, medium, or low. Packages with
       identical priorities are sent in the order in which they were created. If there's
       no backlog, the package processes immediately regardless of its priority. By
       default, the site sends packages with Medium priority.

       Enable for on-demand distribution: Use this setting to enable on-demand
       content distribution to distribution points configured for this feature and in
       the client's current boundary group. When you enable this setting, the
       management point creates a trigger for the distribution manager to
       distribute the content to all such distribution points when a client requests
       the content for the package and the content isn't available. For more
       information, see On-demand content distribution.

<!-- p.118 -->

       Prestaged distribution point settings: Use this setting to specify how you
       want to distribute content to prestaged distribution points. Choose one of
       the following options:

             Automatically download content when packages are assigned to
             distribution points: Use this setting to ignore the prestage settings and
             distribute content to the distribution point.

             Download only content changes to the distribution point: Use this
             setting to prestage the initial content to the distribution point, and then
             distribute content changes to the distribution point.

             Manually copy the content in this package to the distribution point: Use
             this setting to always prestage content on the distribution point. This
             option is the default.

       For more information about prestaging content to distribution points, see
       Use Prestaged content.

6. On the Download Location page, specify the location that Configuration Manager
  uses to download the software update source files. Use one of the following
  options:

       Download software updates from the Internet: Select this setting to
       download the software updates from the location on the internet. This option
       is the default.

       Download software updates from a location on my network: Select this
       setting to download the software updates from a local directory or shared
       folder. This setting is useful when the computer that runs the wizard doesn't
       have internet access. Any computer with internet access can preliminarily
       download the software updates. Then store them in a location on the local
       network that's accessible from the computer that runs the wizard.

7. On the Language Selection page, select the languages for which the site
  downloads the selected software updates. The site only downloads these updates
  if they're available in the selected languages. Software updates that aren't
  language-specific are always downloaded. By default, the wizard selects the
  languages that you've configured in the software update point properties. At least
  one language must be selected before proceeding to the next page. When you
  select only languages that a software update doesn't support, the download fails
  for the update.

<!-- p.119 -->

   8. On the Summary page, verify the settings that you selected in the wizard, and then
     click Next to download the software updates.

   9. On the Completion page, verify that the software updates were successfully
     downloaded, and then click Close.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.120 -->

Add software updates to an update
group
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Software update groups provide you with an effective method to organize software
updates in your environment. You can manually add software updates to a software
update group or automatically add software updates to a software update group by
using an ADR. You can also deploy a software update group manually or deploy the
group automatically by using an ADR. After you deploy a software update group, you
can add new software updates to the group and Configuration Manager will
automatically deploy them. Use the following procedures to add software updates to a
new or existing software update group.

   Tip

        Starting in version 2203, you can organize software update groups and
        packages by using folders. This change allows for better categorization and
        management of software updates. For more information, see Deploy software
        updates.
        Devices running an unsupported operating systems will display as compliant
        since there aren't applicable updates to the operating system any longer.

Add software updates to a new software
update group
   1. In the Configuration Manager console, select Software Library.

   2. In the Software Library workspace, expand Software Updates, and then select All
      Software Updates.

   3. Select the software updates to be added to the new software update group.

   4. On the Home tab, in the Update group, select Create Software Update Group.

   5. Specify the name for the software update group and optionally provide a
      description. Use a name and description that provide enough information for you
