---
title: "Welcome — pages 801-840"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0801-0840
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0801-0840
family: sccm
documentKind: "doc"
abstract: "Unlike WCM and WSyncMgr, WSUS Control Manager (WSUSCtrl) resides on the software update point (SUP) itself. If SUP is remote, WSUSCtrl.log will be present on the SUP instead of on the site server. WSUS Control Manager periodically checks WSUS to make sure WSUS components are hea"
---

# Welcome — pages 801-840

<!-- p.801 -->

Unlike WCM and WSyncMgr, WSUS Control Manager (WSUSCtrl) resides on the software
update point (SUP) itself. If SUP is remote, WSUSCtrl.log will be present on the SUP instead of
on the site server. WSUS Control Manager periodically checks WSUS to make sure WSUS
components are healthy. If WSUS components are unhealthy, WCM and WSyncMgr can't
communicate with WSUS. In most cases, errors in WCM.log resemble the errors in
WsyncMgr.log. However, an exception could be when the SUP is remote from the site server. If
WSUS components are healthy, WSUSCtrl.log on the remote SUP doesn't report any errors.
However, if the site server can't connect to the WSUS server remotely, you'll see errors in
WCM.log and/or WSyncMgr.log even though WSUS itself is healthy.

To check whether WSUS is functioning as expected, run the following command on the WSUS
server. Then review the Application log in Event Viewer for errors:

 Console

 %ProgramFiles%\Update Services\Tools\wsusutil.exe checkhealth

Check connectivity from the site server to the WSUS server
If the WSUS server is remote from the site server, the WSUS Administration console must be
installed on the site server. The console installs the required APIs that are used by
Configuration Manager to connect to the WSUS server. To test whether Configuration Manager
can connect to the WSUS server, use the locally installed WSUS Administration console.

To connect to the remote WSUS server by using the WSUS Administration console, follow these
steps:

   1. Start the WSUS Administration console.
   2. Right-click Update Services in the tree view, and select Connect to Server.
   3. Specify the Server Name and Port Number of the remote WSUS server, and then select
     Connect. Make sure that you specify the FQDN of the WSUS server and the correct port
     number.

WSUS connection failures
For more information, see Troubleshoot WSUS connection failures.

More information

<!-- p.802 -->

     For more information about software update synchronization process, see Software
     updates synchronization.
     You can also post a question in our Configuration Manager support forum for security,
     updates, and compliance here       .
     Visit our blog     for all the latest news, information, and tech tips on Configuration
     Manager.

Last updated on 03/30/2026

<!-- p.803 -->

Troubleshoot software update scan failures
in Configuration Manager
This article describes how to troubleshoot software update scan failures in Configuration
Manager.

Original product version: Microsoft System Center 2012 Configuration Manager, Microsoft
System Center 2012 R2 Configuration Manager
Original KB number: 3090184

Summary
There are several reasons that a software update scan could fail. Most problems involve
communication or firewall issues between the client and the software update point computer.
We describe some of the most common error conditions and their associated resolutions and
troubleshooting tips here. For more information about Windows Update common errors, see
Windows Update common errors and mitigation.

For more information about software updates in Configuration Manager, see Software updates
introduction.

When you troubleshoot software update scan failures, focus on the WUAHandler.log and
WindowsUpdate.log files. WUAHandler just reports what the Windows Update Agent reported.
So the error in the WUAHandler.log file would be the same error that was reported by the
Windows Update Agent itself. Most information about the error will likely be found in the
WindowsUpdate.log file. For more information about how to read the WindowsUpdate.log file,
see Windows Update log files.

Scan failures due to missing or corrupted components
Errors 0x80245003, 0x80070514, 0x8DDD0018, 0x80246008, 0x80200013, 0x80004015,
0x800A0046, 0x800A01AD, 0x80070424, 0x800B0100, and 0x80248011 are caused by missing
or corrupted components.

Several issues can be caused by missing or corrupted files or registry keys, component
registrations, and so on. A good place to start is to run the Windows Update Troubleshooter
to detect and fix these issues automatically.

<!-- p.804 -->

It's also a good idea to make sure that you're running the latest version of the Windows
Update Agent .

If running the Windows Update Troubleshooter doesn't fix the problem, reset the Windows
Update Agent data store on the client by following these steps:

   1. Stop the Windows Update service by running the following command:

          Console

          net stop wuauserv

   2. Rename the C:\Windows\SoftwareDistribution folder to
      C:\Windows\SoftwareDistribution.old .

   3. Start the Windows Update service by running the following command:

          Console

          net start wuauserv

   4. Start a software update scan cycle.

Scan failures due to proxy-related issues
Errors 0x80244021, 0x8024401B, 0x80240030, and 0x8024402C are caused by proxy-related
issues.

Verify the proxy settings on the client, and make sure that they are configured correctly. The
Windows Update Agent uses WinHTTP to scan for available updates. When there's a proxy
server between the client and the WSUS computer, the proxy settings must be configured
correctly on the clients to enable them to communicate with WSUS by using the computer's
FQDN.

For proxy issues, WindowsUpdate.log may report errors that resemble the following ones:

  0x80244021 or HTTP Error 502 - Bad gateway

  0x8024401B or HTTP Error 407 - Proxy Authentication Required

  0x80240030 - The format of the proxy list was invalid

<!-- p.805 -->

  0x8024402C - The proxy server or target server name cannot be resolved

In most cases, you can bypass the proxy for local addresses because the WSUS computer is
located within the intranet. But if the client is connected to the Internet, you must make sure
that the proxy server is configured to enable that communication.

To view WinHTTP proxy settings, run one of the following commands:

     On Windows XP: proxycfg.exe
     On Windows Vista and later versions: netsh winhttp show proxy

Proxy settings that are configured in Internet Explorer are part of the WinINET proxy settings.
WinHTTP proxy settings aren't necessarily the same as the proxy settings that are configured in
Internet Explorer. However, if the proxy settings are set correctly in Internet Explorer, you can
import the proxy configuration from Internet Explorer. To import proxy configuration from
Internet Explorer, run one of the following commands:

     On Windows XP: proxycfg.exe -u
     On Windows Vista and later versions: netsh winhttp import proxy source =ie

For more information, see How the Windows Update client determines which proxy server to
use to connect to the Windows Update website.

Scan failures related to HTTP time-out or
authentication
Errors: 0x80072ee2, 0x8024401C, 0x80244023, or 0x80244017 (HTTP Status 401), 0x80244018
(HTTP Status 403)

Verify connectivity with the WSUS computer. During a scan, the Windows Update Agent must
communicate with the ClientWebService and SimpleAuthWebService virtual directories on the
WSUS computer to run a scan. If the client can't communicate with the WSUS computer, the
scan fails. This issue can occur for several reasons, including:

     port configuration
     proxy configuration
     firewall issues
     network connectivity

First, find the URL of the WSUS computer by checking the following registry key:

<!-- p.806 -->

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate

Try to access the URL to verify connectivity between the client and the WSUS computer. For
example, the URL you use should resemble the following URL:
http://SUPSERVER.CONTOSO.COM:8530/Selfupdate/wuident.cab

Then check whether the client can access the ClientWebService virtual directory. The URL
should resemble the following URL:
http://SUPSERVER.CONTOSO.COM:8530/ClientWebService/wusserverversion.xml

Finally, check whether the client can access the SimpleAuthWebService virtual directory. The URL
should resemble the following URL:
http://SUPSERVER.CONTOSO.COM:8530/SimpleAuthWebService/SimpleAuth.asmx

If these tests are successful, review the Internet Information Services (IIS) logs on the WSUS
computer to confirm that the HTTP errors are being returned from WSUS. If the WSUS
computer doesn't return the error, the issue is probably with an intermediate firewall or proxy.

If any of these tests fails, check for name resolution issues on the client. Verify that you can
resolve the FQDN of the WSUS computer.

Also verify the proxy settings on the client to make sure that they are configured correctly. For
more information, see the Scan failures due to proxy-related issues section.

Finally, verify that the WSUS ports can be accessed. WSUS can be configured to use any of the
following ports:

     80
     443
     8530
     8531

For clients to communicate with the WSUS computer, the appropriate ports must be enabled
on any firewall between the client and the WSUS computer.

Determine the port settings used by WSUS and the software
update point
Port settings are configured when the software update point site system role is created. These
port settings must be the same as the port settings that are used by the WSUS website.
Otherwise, WSUS Synchronization Manager won't connect to the WSUS computer that's

<!-- p.807 -->

running on the software update point to request synchronization. The following procedures
show how to verify the port settings that are used by WSUS and the software update point.

Determine the WSUS port settings in IIS 6.0

   1. On the WSUS server, open Internet Information Services (IIS) Manager.
   2. Expand Web Sites, right-click the website for the WSUS server, and then select
     Properties.
   3. Select the Web Site tab.
   4. The HTTP port setting is displayed in TCP port, and the HTTPS port setting is displayed in
     SSL port.

Determine the WSUS port settings in IIS 7.0 and later versions

   1. On the WSUS server, open Internet Information Services (IIS) Manager.
   2. Expand Sites, right-click the website for the WSUS server, and then select Edit Bindings.
   3. In the Site Bindings dialog box, the HTTP and HTTPS port values are displayed in the Port
     column.

Verify and configure ports for the software update point

   1. In the Configuration Manager console, go to Administration > Site Configuration >
     Servers and Site System Roles, and then select <SiteSystemName> in the right pane.
   2. In the bottom pane, right-click Software Update Point and then click Properties.
   3. On the General tab, specify or verify the WSUS configuration port numbers.

After the ports are verified and configured correctly, you should check port connectivity from
the client by running the following command:

 Console

 telnet SUPSERVER.CONTOSO.COM <PortNumber>

If the port is inaccessible, telnet returns an error that resembles the following.

  Could not open connection to the host, on port <PortNumber>

This error suggests that firewall rules must be configured to enable communication for the
WSUS Server ports.

<!-- p.808 -->

Scan fails with error 0x80072f0c
Error 0x80072f0c translates to A certificate is required to complete client authentication. This
error should occur only if the WSUS computer is configured to use SSL. As part of the SSL
configuration, WSUS virtual directories must be configured to use SSL, and they must be set to
ignore client certificates. If the WSUS website or any of the virtual directories that were
mentioned previously are configured incorrectly to Accept or Require client certificates, you
receive this error.

Check SSL configuration
When the site is configured in HTTPS only mode, the software update point is automatically
configured to use SSL. When the site is in HTTPS or HTTP mode, you can choose whether to
configure the software update point to use SSL. When the software update point is configured
to use SSL, the WSUS computer must also be explicitly configured to use SSL. Before you
configure SSL, you should review the certificate requirements. And make sure that a server
authentication certificate is installed on the software update point server.

Verify that the software update point is configured for SSL

   1. On the Configuration Manager console, go to Administration > Site Configuration >
     Servers and Site System Roles, and then select <SiteSystemName> in the right pane.
   2. In the bottom pane, right-click Software Update Point, and then select Properties.
   3. On the General tab, verify that the following option is enabled:
     Require SSL communication to the WSUS Server

Verify that the WSUS computer is configured for SSL

   1. Open the WSUS console on the software update point for the site.
   2. In the console tree pane, select Options.
   3. In the display pane, select Update Source and Proxy Server.
   4. Verify that the Use SSL when synchronizing update information option is selected.

Add the server authentication certificate to the WSUS Administration
website

   1. On the WSUS computer, start Internet Information Services (IIS) Manager.
   2. Expand Sites, right-click Default Web Site or the WSUS Administration website if WSUS is
     configured to use a custom website, and then select Edit Bindings.

<!-- p.809 -->

   3. Select the HTTPS entry, and then select Edit.
   4. In the Edit Site Binding dialog box, select the server authentication certificate, and then
     select OK.
   5. In the Edit Site Binding dialog box, select OK, and then select Close.
   6. Exit IIS Manager.

  ） Important

  Make sure that the FQDN that is specified in the Site System properties matches the
  FQDN that is specified in the certificate. If the software update point accepts connections
  from the intranet only, the Subject Name or Subject Alternative Name must contain the
  intranet FQDN. When the software update point accepts client connections from the
  Internet only, the certificate must still contain both the Internet FQDN and the intranet
  FQDN, because WCM and WSyncMgr still use the intranet FQDN to connect to the
  software update point. If the software update point accepts connections from both the
  Internet and the intranet, both the Internet FQDN and the intranet FQDN must be
  specified by using the ampersand (&) symbol delimiter between the two names.

Verify that SSL is configured on the WSUS computer

For more information, see Configure SSL on the WSUS server.

  ） Important

  You cannot configure the whole WSUS website to require SSL, because then all traffic to
  the WSUS site would have to be encrypted. WSUS encrypts update metadata only. If a
  computer tries to retrieve update files on the HTTPS port, the transfer will fail.

Group Policy overrides the correct WSUS
configuration information
The Software Updates feature automatically configures a local Group Policy setting for the
Configuration Manager client, so that it's configured to use the software update point source
location and port number. Both the server name and the port number are required for the
client to find the software update point.

<!-- p.810 -->

If an Active Directory Group Policy setting is applied to computers for software update point
client installation, it overrides the local Group Policy setting. Unless the value of the setting
that's defined in Group Policy is identical to the one that's being set by Configuration Manager
(server name and port), the Configuration Manager software update scan will fail on the client.
In this case, the WUAHandler.log file shows the following entry:

 Output

 Group policy settings were overwritten by a higher authority (Domain Controller)
 to: Server http://server and Policy ENABLED

To fix this issue, the software update point for client installation and software updates must be
the same server. And it must be specified in the Active Directory Group Policy setting by using
the correct name format and port information. For example, if the software update point was
using the default website, the software update point would be http://server1.contoso.com:80 .

Clients can't find the WSUS server location
   1. To understand how clients obtain the WSUS server location, see WSUS server location.
     And review the client and management point logs.
   2. Enable verbose and debug logging on the client and management point.
   3. Verify that there are no communication errors in CcmMessaging.log on the client.
   4. If the management point returns an empty WSUS location response, there may be a
     mismatch in the Content Version of WSUS. It could be a result of failed synchronization.
     To find the Content Version of the software update point, in Configuration Manager
     console, select Monitoring > Software Update Point Synchronization Status.
   5. Review the data in CI_UpdateSources , WSUSServerLocations and Update_SyncStatus tables,
     verify that the Update Source Unique ID and Content Version match across these tables.

Compliance results unknown
   1. Review the PolicyAgent.log file on the client to verify that the client is receiving policies.
   2. Verify that software update synchronization is successful on the software update point. If
     synchronization fails, troubleshoot synchronization issues.
   3. If the WUAHandler.log file doesn't exist and isn't created after you start a scan cycle, the
     issue most likely occurs because of one of the following reasons:

           The software update scan policy isn't available
           Clients can't find the WSUS server location

<!-- p.811 -->

  4. Verify that there are no communication errors in the CcmMessaging.log file on the client.
  5. If the scan is successful, the client should send state messages to the management point
     to indicate the update status. To understand how state messages processing works, see
     state message processing flow.

Other issues
For more information, see Troubleshoot client software update scanning.

Last updated on 03/30/2026

<!-- p.812 -->

Troubleshoot software update
deployments in Configuration Manager
This article describes how to troubleshoot software update deployments that don't run
successfully.

Original product version: Microsoft System Center 2012 Configuration Manager, Microsoft
System Center 2012 R2 Configuration Manager
Original KB number: 3090264

Summary
When you deploy software updates in Configuration Manager, you typically add the updates to
a software update group. Then deploy the software update group to clients. When you create
the deployment, the update policy is sent to client computers. The update content files are
downloaded from a distribution point to the local cache on the client computer. The updates
are then available for installation on the client. Normally this process is completed successfully
with little effort. However, issues may sometimes arise that cause update deployment to fail.
We cover the two most common failure scenarios and provide troubleshooting suggestions for
each.

For more information about software updates in Configuration Manager, see Software updates
introduction.

When software update deployment fails, the problem generally falls into one of two categories:

        Updates fail to download.
        You experience unexpected reboots, or updates are installed outside a maintenance
        window.

Updates fail to download
   1. When updates don't get downloaded to the client, first check the CAS.log,
        ContentTransferManager.log, and DataTransferService.log files for errors. To learn about
        how updates are downloaded, see Track the software update deployment process in
        Configuration Manager

<!-- p.813 -->

   2. Verify that the client is in the appropriate boundary associated with the boundary group
     for the distribution point. For more information about boundary groups, see Configuring
     boundaries and boundary groups in Configuration Manager.

   3. Check the Software Update Package status and verify that the updates are downloaded
     and installed on the distribution points. If the content isn't installed on the distribution
     point that's associated with the client's boundary group, check whether fallback for
     content location must be enabled. For more information, see What is fallback and what
     does it mean?.

   4. If the client receives the download location but fails to download content, try to
     download the content manually by accessing the URL for the content. You can find the
     URL by reviewing DataTransferServices.log.

Installation, supersedence, or detection issues with
specific updates
   1. Check to see whether the scan failed during the deployment evaluation. For more
     information about scan failures, see Troubleshoot software update scan failures in
     Configuration Manager.
   2. Review WUAHandler.log and WindowsUpdate.log to find the errors received during
     update installation.
   3. To rule out an installation issue with the update itself, manually install the update or
     install it from Microsoft Update (if possible). See whether the update installation is
     successful.
   4. Most .NET Framework update failures are caused by corrupted .NET Framework
     installations. In these cases, try to manually install the update. If the installation process
     fails, see Fix Windows Update errors     .

For more information, see Installation, supersedence, or detection issues with specific updates.

You experience unexpected reboots, or updates are
installed outside a maintenance window
If possible, enable verbose and debug logging if the issue can be reproduced.

   1. Review the ServiceWindowManager.log file on the client, and identify the service windows
     that are available.

<!-- p.814 -->

ServiceWindowManager.log contains information about maintenance windows and their
start and end time. This information can be very useful when you troubleshoot issues
related to software update installation on clients.

To find a list of available maintenance windows (service windows) on a client, open
ServiceWindowManager.log, and search for the Refreshing Service Windows string.
Immediately following this line, you'll see a list of the applicable service windows on the
computer, as in the following example:

 Output

 Refreshing Service Windows..... ServiceWindowManager
 Populating instance of ServiceWindow with ID=7cb56688-692f-4fae-b398-
 0e3ff4413adb,
 ScheduleString=02C159C0381A200002C159C0381B200002C159C0381C200002C159C0381D200
 002C159C0381E2000, Type=6 ServiceWindowManager
 This is a one shot Service Window that has already finished.
 ServiceWindowManager
 Duration for the Service Window is Total days: 0, hours: 00, mins: 00, secs:
 00 ServiceWindowManager
 Populating instance of ServiceWindow with ID=90a5f436-364c-48c7-8dc7-
 c5014abcbea8, ScheduleString=00084AC028592000, Type=6 ServiceWindowManager
 StartTime is 02/09/14 00:00:00 ServiceWindowManager
 Duration for the Service Window is Total days: 1, hours: 05, mins: 00, secs:
 00 ServiceWindowManager
 Populating instance of ServiceWindow with ID=45dca355-3249-4845-b8aa-
 72d0e604548e, ScheduleString=02C24AC0381C2000, Type=6 ServiceWindowManager
 StartTime is 02/12/14 22:00:00 ServiceWindowManager
 Duration for the Service Window is Total days: 0, hours: 07, mins: 00, secs:
 00 ServiceWindowManager
 Populating instance of ServiceWindow with ID=87e4759c-2884-45e6-9261-
 c33ba53f596c, ScheduleString=02C24AC0381D2000, Type=6 ServiceWindowManager
 StartTime is 02/13/14 22:00:00 ServiceWindowManager
 Duration for the Service Window is Total days: 0, hours: 07, mins: 00, secs:
 00 ServiceWindowManager
 Populating instance of ServiceWindow with ID={1E957DDD-0A26-434C-952A-
 586F3E31E319}, ScheduleString=00302B0018192000, Type=1 ServiceWindowManager
 StartTime is 02/16/14 01:00:00 ServiceWindowManager
 Duration for the Service Window is Total days: 0, hours: 03, mins: 00, secs:
 00 ServiceWindowManager
 Populating instance of ServiceWindow with ID=36da6950-3d1e-4027-be0e-
 7b16a4daee7e, ScheduleString=02C24AC0101E2000, Type=6 ServiceWindowManager
 StartTime is 02/14/14 22:00:00 ServiceWindowManager
 Duration for the Service Window is Total days: 0, hours: 02, mins: 00, secs:
 00 ServiceWindowManager
 Populating instance of ServiceWindow with ID=028bfbc0-7120-4081-a268-
 0e664a92ac4a, ScheduleString=00074AC0005F2000, Type=6 ServiceWindowManager
 StartTime is 02/15/14 00:00:00 ServiceWindowManager
 Duration for the Service Window is Total days: 1, hours: 00, mins: 00, secs:
 00 ServiceWindowManager
 Populating instance of ServiceWindow with ID=49fd80be-ac4b-4877-974d-

<!-- p.815 -->

    ecd09958926d, ScheduleString=02C24AC0381B2000, Type=6 ServiceWindowManager
    StartTime is 02/11/14 22:00:00 ServiceWindowManager
    Duration for the Service Window is Total days: 0, hours: 07, mins: 00, secs:
    00 ServiceWindowManager
    Populating instance of ServiceWindow with ID=ad27b0ca-8c74-43c7-8200-
    1f601880bd75, ScheduleString=02C24AC0381A2000, Type=6 ServiceWindowManager
    StartTime is 02/10/14 22:00:00 ServiceWindowManager
    Duration for the Service Window is Total days: 0, hours: 07, mins: 00, secs:
    00 ServiceWindowManager

  Generally, service windows with IDs containing all lowercase alpha-numeric characters are
  non-business hour (NBH) maintenance windows. They're based on business hours
  configured in Software Center. However, service windows with IDs containing all
  uppercase alpha-numeric characters are maintenance windows defined for the collection
  in the Configuration Manager console. In the example, all service windows are non-
  business hour windows, except the one with ID 1E957DDD-0A26-434C-952A-
  586F3E31E319. This window is a maintenance window defined for the collection that
  holds the client.

2. Review the UpdatesDeployment.log file. Locate the following line to check whether the
  deployment was set to ignore the maintenance window:

    Output

    Notify reboot with deadline = Sunday, Feb 09, 2014. - 21:30:17, Ignore reboot
    Window = True, NotifyUI = True

3. Review the MaintenanceCoordinator.log file. Locate the following line to check whether
  the deployment was set to ignore the maintenance window. A value of 1 for swoverride
  means that the ignore maintenance window setting is enabled.

    Output

    RequestPersistence(id=Update download job, persist=1, swoverride=1, swType=4,
    pendingWFDisable=0, deadline=1)

4. Review the SCNotify.log file, and look for the following lines to check whether the user
  clicked the restart notification to initiate a restart:

    Output

    ConfirmRestartDialog: User chose to restart/logoff.
    (Microsoft.SoftwareCenter.Client.Pages.ConfirmRestartDialog at
    ButtonRestart_Click)
    ConfirmRestartDialog: user is allowed to restart

<!-- p.816 -->

       (Microsoft.SoftwareCenter.Client.Pages.ConfirmRestartDialog at
       ButtonRestart_Click)
       The user is allowed to restart the computer. Initiating restart.
       (Microsoft.SoftwareCenter.Client.Data.WmiDataConnector at RestartComputer)

  5. View the deployment properties in the Configuration Manager console to check whether
     the deployment is set to override maintenance windows. If the deployment isn't set to
     override maintenance windows, but the client logs suggest that the deployment did
     override maintenance windows, review the audit status messages to check whether the
     deployment was modified by someone.

     To review audit status messages, navigate to Configuration Manager console >
     Monitoring > System Status > Status Message Queries. Right-click All Status Messages,
     click Show Messages, select the timeframe, and then click OK.

     In the Configuration Manager Status Message Viewer window, navigate to View > Filter,
     and then filter for Message ID = 30197. If the deployment was modified, you'll see a
     status message that resembles the following one:

       Output

       Severity Type Site code Date / Time System Component Message ID Description
       Information Audit PR1 2/9/2014 11:57:49 PM PR1SITE.CONTOSO.COM
       Microsoft.ConfigurationManagement.exe 30197 User "DOMAIN\User" modified
       updates assignment 4 ({BAFB1BDB-7A6C-4DCF-9866-6C22DF92346A}).

Last updated on 03/30/2026

<!-- p.817 -->

PowerShell script to decline superseded
updates in WSUS
If you are using standalone Windows Server Update Services (WSUS) servers or an older
version of Configuration Manager, you can manually decline superseded updates by using the
WSUS console. Or you can run the following PowerShell script. For common questions about
WSUS maintenance for Configuration Manager environments, see the complete guide to WSUS
and Configuration Manager SUP maintenance.

 PowerShell

 <#
     .SYNOPSIS
         Script to decline superseeded updates in WSUS. It's recommended to run the
 script with the -SkipDecline switch to see how many superseded updates
         are in WSUS and to TAKE A BACKUP OF THE SUSDB before declining the updates.

      .PARAMETER UpdateServer
          Specify WSUS Server Name

      .PARAMETER Port
          WSUS Server Port

      .PARAMETER UseSSL
          Specifies whether WSUS Server is configured to use SSL

      .PARAMETER SkipDecline
          Runs decline script in audit mode

     .PARAMETER DeclineLastLevelOnly
         Whether to decline all superseded updates or only last level superseded
 updates

         Supersedence chain could have multiple updates. For example, Update1
 supersedes Update2. Update2 supersedes Update3. In this scenario,
         the Last Level in the supersedence chain is Update3. To decline only the
 last level updates in the supersedence chain, specify the DeclineLastLevelOnly
 switch

     .PARAMETER ExclusionPeriod
         The number of days between today and the release date for which the
 superseded updates must not be declined.

     .EXAMPLE
         # To do a test run against WSUS Server without SSL
         Decline-SupersededUpdates.ps1 -UpdateServer SERVERNAME -Port 8530 -
 SkipDecline

<!-- p.818 -->

    .EXAMPLE
        # To do a test run against WSUS Server using SSL
        Decline-SupersededUpdates.ps1 -UpdateServer SERVERNAME -UseSSL -Port 8531 -
SkipDecline

      .EXAMPLE
          # To decline all superseded updates on the WSUS Server using SSL
          Decline-SupersededUpdates.ps1 -UpdateServer SERVERNAME -UseSSL -Port 8531

      .EXAMPLE
          # To decline only Last Level superseded updates on the WSUS Server using
SSL
        Decline-SupersededUpdates.ps1 -UpdateServer SERVERNAME -UseSSL -Port 8531 -
DeclineLastLevelOnly

    .EXAMPLE
        # To decline all superseded updates on the WSUS Server using SSL but keep
superseded updates published within the last 2 months (60 days)
        Decline-SupersededUpdates.ps1 -UpdateServer SERVERNAME -UseSSL -Port 8531 -
ExclusionPeriod 60
#>
[CmdletBinding()]
param
(
    [Parameter(Mandatory = $true, Position = 1)]
    [string]
    $UpdateServer,

      [Parameter(Mandatory = $true, Position = 2)]
      [int]
      $Port,

      [Parameter()]
      [switch]
      $UseSSL,

      [Parameter()]
      [switch]
      $SkipDecline,

      [Parameter()]
      [switch]
      $DeclineLastLevelOnly,

      [Parameter()]
      [int]
      $ExclusionPeriod = 0
)

if (-not (Test-Path -Path "$PSScriptRoot\WsusDeclineLogs"))
{
    New-Item -Path $PSScriptRoot -Name 'WsusDeclineLogs' -ItemType Directory -Force
}

<!-- p.819 -->

$file =
"$PSScriptRoot\WsusDeclineLogs\WSUS_Decline_Superseded_{0:MMddyyyy_HHmm}.log" -f
(Get-Date)

Start-Transcript -Path $file

if ($SkipDecline -and $DeclineLastLevelOnly)
{
    Write-Output -InputObject 'Using SkipDecline and DeclineLastLevelOnly switches
together is not allowed.'
    Write-Output -InputObject ''
    return
}

$outSupersededList = Join-Path -Path "$PSScriptRoot\WsusDeclineLogs" -ChildPath
'SupersededUpdates.csv'
$outSupersededListBackup = Join-Path -Path "$PSScriptRoot\WsusDeclineLogs" -
ChildPath 'SupersededUpdatesBackup.csv'

Set-Content -Value 'UpdateID, RevisionNumber, Title, KBArticle, SecurityBulletin,
LastLevel' -Path $outSupersededList

try
{
    if ($UseSSL)
    {
        Write-Output -InputObject "Connecting to WSUS server $UpdateServer on Port
$Port using SSL... "
    }
    else
    {
        Write-Output -InputObject "Connecting to WSUS server $UpdateServer on Port
$Port... "
    }

[reflection.assembly]::LoadWithPartialName('Microsoft.UpdateServices.Administration
') | Out-Null
    $wsus =
[Microsoft.UpdateServices.Administration.AdminProxy]::GetUpdateServer($UpdateServer
, $UseSSL, $Port);
}
catch [System.Exception]
{
    Write-Output -InputObject 'Failed to connect.'
    Write-Output -InputObject "Error: $($_.Exception.Message)"
    Write-Output -InputObject 'Please make sure that WSUS Admin Console is
installed on this machine'
    Write-Output -InputObject ''
    $wsus = $null
}

if ($null -eq $wsus)
{
    return

<!-- p.820 -->

}

Write-Output -InputObject 'Connected.'

$UpdateScope = New-Object Microsoft.UpdateServices.Administration.UpdateScope

(Get-Date).AddMonths(-6)
$UpdateScope.FromArrivalDate = (Get-Date).AddMonths(-6)
$UpdateScope.ToArrivalDate = (Get-Date)

$countAllUpdates = 0
$countSupersededAll = 0
$countSupersededLastLevel = 0
$countSupersededExclusionPeriod = 0
$countSupersededLastLevelExclusionPeriod = 0
$countDeclined = 0

Write-Output -InputObject 'Getting a list of all updates... '

try
{
    $allUpdates = $wsus.GetUpdates($UpdateScope)
}
catch [System.Exception]
{
    Write-Output -InputObject 'Failed to get updates.'
    Write-Output -InputObject "Error: $($_.Exception.Message)"
    Write-Output -InputObject 'If this operation timed out, please decline the
superseded updates from the WSUS Console manually.'
    Write-Output -InputObject ''
    return
}

Write-Output -InputObject 'Done'

Write-Output -InputObject 'Parsing the list of updates... '
foreach ($update in $allUpdates)
{
    $countAllUpdates++

      if ($update.IsDeclined)
      {
          $countDeclined++
      }

      if (-not $update.IsDeclined -and $update.IsSuperseded)
      {
          $countSupersededAll++

         if (-not $update.HasSupersededUpdates)
         {
             $countSupersededLastLevel++
         }

         if ($update.CreationDate -lt (Get-Date).AddDays(-$ExclusionPeriod))

<!-- p.821 -->

       {
            $countSupersededExclusionPeriod++
            if (-not $update.HasSupersededUpdates)
            {
                $countSupersededLastLevelExclusionPeriod++
            }
       }

        "$($update.Id.UpdateId.Guid), $($update.Id.RevisionNumber),
$($update.Title), $($update.KnowledgeBaseArticles), $($update.SecurityBulletins),
$($update.HasSupersededUpdates)" | Out-File $outSupersededList -Append
    }
}

Write-Output -InputObject 'Done.'
Write-Output -InputObject "List of superseded updates: $outSupersededList"

Write-Output -InputObject ''
Write-Output -InputObject 'Summary:'
Write-Output -InputObject '========'

Write-Output -InputObject "All Updates = $countAllUpdates"
$AnyExceptDeclined = $countAllUpdates - $countDeclined
Write-Output -InputObject "Any except Declined = $AnyExceptDeclined"
Write-Output -InputObject "All Superseded Updates = $countSupersededAll"
$SuperseededAllOutput = $countSupersededAll - $countSupersededLastLevel
Write-Output -InputObject "    Superseded Updates (Intermediate) =
$SuperseededAllOutput"
Write-Output -InputObject "    Superseded Updates (Last Level) =
$countSupersededLastLevel"
Write-Output -InputObject "    Superseded Updates (Older than $ExclusionPeriod
days) = $countSupersededExclusionPeriod"
Write-Output -InputObject "    Superseded Updates (Last Level Older than
$ExclusionPeriod days) = $countSupersededLastLevelExclusionPeriod"

$i = 0
if (-not $SkipDecline)
{

    Write-Output -InputObject "SkipDecline flag is set to $SkipDecline. Continuing
with declining updates"
    $updatesDeclined = 0

    if ($DeclineLastLevelOnly)
    {
        Write-Output -InputObject ' DeclineLastLevel is set to True. Only
declining last level superseded updates.'

       foreach ($update in $allUpdates)
       {

            if (-not $update.IsDeclined -and $update.IsSuperseded -and -not
$update.HasSupersededUpdates)
            {
                if ($update.CreationDate -lt (Get-Date).AddDays(-$ExclusionPeriod))

<!-- p.822 -->

               {
                    $i++
                    $percentComplete = "{0:N2}" -f (($updatesDeclined /
$countSupersededLastLevelExclusionPeriod) * 100)
                    Write-Progress -Activity "Declining Updates" -Status "Declining
update #$i/$countSupersededLastLevelExclusionPeriod - $($update.Id.UpdateId.Guid)"
-PercentComplete $percentComplete -CurrentOperation "$($percentComplete)% complete"

                   try
                   {
                         $update.Decline()
                         $updatesDeclined++
                    }
                    catch [System.Exception]
                    {
                         Write-Output -InputObject "Failed to decline update
$($update.Id.UpdateId.Guid). Error:" $_.Exception.Message
                    }
                }
            }
        }
    }
    else
    {
        Write-Output -InputObject ' DeclineLastLevel is set to False. Declining
all superseded updates.'

       foreach ($update in $allUpdates)
       {

            if (-not $update.IsDeclined -and $update.IsSuperseded)
            {
                if ($update.CreationDate -lt (Get-Date).AddDays(-$ExclusionPeriod))
                {

                    $i++
                    $percentComplete = "{0:N2}" -f (($updatesDeclined /
$countSupersededAll) * 100)
                    Write-Progress -Activity "Declining Updates" -Status "Declining
update #$i/$countSupersededAll - $($update.Id.UpdateId.Guid)" -PercentComplete
$percentComplete -CurrentOperation "$($percentComplete)% complete"
                    try
                    {
                        $update.Decline()
                        $updatesDeclined++
                    }
                    catch [System.Exception]
                    {
                        Write-Output -InputObject "Failed to decline update
$($update.Id.UpdateId.Guid). Error:" $_.Exception.Message
                    }
                }
            }
        }
    }

<!-- p.823 -->

      Write-Output -InputObject "   Declined $updatesDeclined updates."

      if ($updatesDeclined -ne 0)
      {
          Copy-Item -Path $outSupersededList -Destination $outSupersededListBackup -
 Force
          Write-Output -InputObject " Backed up list of superseded updates to
 $outSupersededListBackup"
      }
 }
 else
 {
      Write-Output -InputObject "SkipDecline flag is set to $SkipDecline. Skipped
 declining updates"
 }

 Write-Output -InputObject ''
 Write-Output -InputObject 'Done'
 Write-Output -InputObject ''

 Stop-Transcript

Last updated on 03/30/2026

<!-- p.824 -->

Use WSUS to deploy definition updates to
computers that are running Windows
Defender
This article describes how to use Microsoft Windows Server Update Services (WSUS) to deploy
definition updates to computers that are running Microsoft Windows Defender.

Original product version: Windows Server Update Services
Original KB number: 919772

Deploy Windows Defender definition updates
To do this, follow these steps:

   1. Open the WSUS Administrator console, and then select Options at the bottom of the
     console tree.

   2. Select Products and Classifications and verify that the Windows Defender check box is
     selected under the Products tab.

   3. Verify that the Definition Updates check box is selected under the Classifications tab, and
     then select OK.

   4. Optional: approve the updates by using an automatic approval rule. To do this, follow
     these steps:
      a. At the bottom of the console tree, select Options.
      b. Select Automatic Approvals.
      c. Under step 1, select New Rule..., and then select the When an update is in a specific
        classification check box and the When an update is in a specific product check box.
      d. Under step 2, select Any classification > Definition Updates, then click OK.
      e. Next, select Any product and clear the All Products check box, then scroll down and
        select Windows Defender, afterward select OK.

   5. At the bottom of the console tree, select Synchronizations.

   6. On the action pane on the left, select Synchronize now.

   7. At the top of the console tree, select Updates.

<!-- p.825 -->

  8. Approve any Windows Defender updates that WSUS should deploy.

Last updated on 03/30/2026

<!-- p.826 -->

Error 80244007 when a WSUS client scans
for updates
Original product version: Windows Server 2019, Windows Server 2016, Windows Server 2012
R2, Windows Server 2012
Original KB number: 4096317

Summary
When Windows Server Update Services (WSUS) clients scan for updates, they might fail with
error [80244007] SyncUpdates_WithRecovery failed . This error occurs when the number of
updates to be synchronized exceeds the default maximum number of installed prerequisites
that a client can pass to the SyncUpdates method.

This article describes how to identify and resolve this issue by adjusting WSUS server
configuration settings.

Symptom
You use WSUS to deploy software updates to computers in your organization. When a WSUS
client computer scans for updates on the WSUS server, you see the following error message in
the WindowsUpdate.log file on the client computer:

 Output

 WS error: <detail><ErrorCode>InvalidParameters</ErrorCode>
 <Message>parameters.InstalledNonLeafUpdateIDs</Message><ID>GUID</ID><Method>
 http://www.microsoft.com/SoftwareDistribution/Server/ClientWebService/SyncUpdates"
 </Method></detail>"

 *FAILED\* [80244007] SyncUpdates_WithRecovery failed

Additionally, the following exception is logged in the SoftwareDistribution.log file on the WSUS
server:

 Output

 ThrowException: actor = http://WSUSServerName:8530/ClientWebService/client.asmxs,
 ID=GUID, ErrorCode=InvalidParameters, Message=parameters.InstalledNonLeafUpdateIDs,

<!-- p.827 -->

  Client=Client_ID

Cause
This issue occurs when the number of updates to be synchronized exceeds the maximum
number of installed prerequisites that a WSUS client can pass to SyncUpdates .

Resolution
To fix the issue, follow these steps on the WSUS server:

   1. Open an elevated Command Prompt window, and then go to %programfiles%\Update
      Services\WebServices\ClientWebService.

   2. Type the following commands, and press Enter after each command:

        Console

        takeown /f web.config
        icacls web.config /grant administrator:(F)
        notepad.exe web.config

   3. In web.config, locate the following entries, and then update their values as indicated:

        XML

        <add key="maxInstalledPrerequisites" value="800"/>
        <add key="maxCachedUpdates" value="44000"/>

      This change increases maxInstalledPrerequisites from 400 to 800 and
      maxCachedUpdates from 22,000 to 44,000.

   4. Save the web.config file.

   5. Run IISReset .

 Last updated on 02/05/2026

<!-- p.828 -->

General guidance on optimizing WSUS
client performance
This article provides general guidelines for optimizing Microsoft Windows Server Update
Services (WSUS) client performance.

Original product version: Windows Server Update Services
Original KB number: 2517455

Summary
After deploying a WSUS server, you may experience the following performance issues on
clients:

      You may experience prolonged high CPU utilization when you scan for updates or when
      you install updates.
      The scans fail.

This article provides general guidelines for optimizing the performance of the clients and for
fixing the issue if the scans ultimately fail. However, keep in mind that a scan is still a CPU-
intensive operation. The Svchost.exe process contains the Automatic Updates service. When
you perform a scan, the Svchost.exe process can cause CPU usage to reach 100 percent for a
certain period of time. For example, Microsoft Office updates use Windows Installer, and when
Microsoft Office updates are detected, these updates can contribute to 100 percent CPU
utilization for a short period of time.

Read this article entirety before attempting any procedure contained here.

Run the WSUS Server Cleanup Wizard
Update scan performance can also be affected by the number of updates the client needs to
evaluate. The WSUS Server Cleanup Wizard will help to remove redundant updates and
optimize the performance for both the WSUS server and the clients. To run the WSUS Server
Cleanup Wizard, follow the steps below:

   1. In the WSUS administration console, select Options > Server Cleanup Wizard.
   2. By default, this wizard will remove unneeded content and any computers that have not
      contacted the server for 30 days or more. Select all possible options, and then select

<!-- p.829 -->

     Next.
   3. The wizard will begin the cleanup process and will present a summary of its work when
     it's finished. Select Finish to complete the process.

For more information, see Using the Server Cleanup Wizard.

Check custom WSUS admin scripts
If you are using a script to approve updates, be cautious that you don't approve expired and
declined updates. These updates are set to be expired by Microsoft and are never approved for
install. Reactivating these updates may cause update scan failures on the clients.

We recommend avoid using Any for approval state when enumerating updates. Instead, use a
combination of other ApprovedState values. For example, the following PowerShell code will
restrict the update search result to updates that are approved with the latest revision and not
approved updates, which are safe to approve:

  PowerShell

  $updateScope.ApprovedStates =
  [Microsoft.UpdateServices.Administration.ApprovedStates]::LatestRevisionApproved -
  bor [Microsoft.UpdateServices.Administration.ApprovedStates]::NotApproved
  foreach($update in $wsus.GetUpdates($updateScope)) { #Approve the update
  $update.Approve($updateaction,$targetgroup) }

For more details, check following WSUS SDK documentation:

     UpdateScope.ApprovedStates Property
     ApprovedStates Enumeration

Reset Windows Update components
If the performance issue happens on only a few of clients, you can try resetting the Windows
Update component on these clients and see if the problem is resolved. Refer to the following
article for details steps and tools:

Windows Update - additional resources

  ７ Note

  Aggressive mode of the script (or step 4 of the above article) should only be run as the
  last possible resort. Performing that step or running the script in Aggressive mode will

<!-- p.830 -->

  wipe the datastore on the local computer, completely erasing all of the user's settings,
  update history, and local cache. This can prove to be very troublesome especially for a
  system administrator, since there is no way to know what updates were previously
  installed on the machine after wiping the datastore.

If the client computer is running Windows 7, it's recommended that you run the built-in
troubleshooter instead of following the steps outlined in the above article. This troubleshooter
performs steps similar to the above article, but is non-destructive and might be a bit more
effective.

To run this troubleshooter, follow the steps below:

   1. Open the Windows Update troubleshooter by selecting the Start > Control Panel.
   2. Select Find and fix problems.
   3. Under System and Security, select Fix problems with Windows Update.

If you're prompted for an administrator password or confirmation, type the password or
provide confirmation, then allow the troubleshooter to complete.

 Last updated on 03/30/2026

<!-- p.831 -->

Reindex the WSUS database
The performance of large WSUS deployments will degrade over time if the WSUS database
isn't maintained properly. The T-SQL script in this article can be run by SQL Server
administrators to reindex and defragment WSUS databases. It shouldn't be used on WSUS 2.0
databases.

T-SQL script
This script does basic maintenance tasks on SUSDB:

     Identifies indexes that are fragmented, and defragments them. For certain tables, a fill
     factor is set to improve insert performance.
     Updates potentially out-of-date table statistics.

 SQL

 USE SUSDB;
 GO
 SET NOCOUNT ON;

 -- Rebuild or reorganize indexes based on their fragmentation levels
 DECLARE @work_to_do TABLE (
     objectid int
     , indexid int
     , pagedensity float
     , fragmentation float
     , numrows int
 )

 DECLARE @objectid int;
 DECLARE @indexid int;
 DECLARE @schemaname nvarchar(130);
 DECLARE @objectname nvarchar(130);
 DECLARE @indexname nvarchar(130);
 DECLARE @numrows int
 DECLARE @density float;
 DECLARE @fragmentation float;
 DECLARE @command nvarchar(4000);
 DECLARE @fillfactorset bit
 DECLARE @numpages int

 -- Select indexes that need to be defragmented based on the following
 -- * Page density is low
 -- * External fragmentation is high in relation to index size
 PRINT 'Estimating fragmentation: Begin. ' + convert(nvarchar, getdate(), 121)

<!-- p.832 -->

INSERT @work_to_do
SELECT
     f.object_id
     , index_id
     , avg_page_space_used_in_percent
     , avg_fragmentation_in_percent
     , record_count
FROM
     sys.dm_db_index_physical_stats (DB_ID(), NULL, NULL , NULL, 'SAMPLED') AS f
WHERE
     (f.avg_page_space_used_in_percent < 85.0 and
f.avg_page_space_used_in_percent/100.0 * page_count < page_count - 1)
     or (f.page_count > 50 and f.avg_fragmentation_in_percent > 15.0)
     or (f.page_count > 10 and f.avg_fragmentation_in_percent > 80.0)

PRINT 'Number of indexes to rebuild: ' + cast(@@ROWCOUNT as nvarchar(20))

PRINT 'Estimating fragmentation: End. ' + convert(nvarchar, getdate(), 121)

SELECT @numpages = sum(ps.used_page_count)
FROM
     @work_to_do AS fi
     INNER JOIN sys.indexes AS i ON fi.objectid = i.object_id and fi.indexid =
i.index_id
     INNER JOIN sys.dm_db_partition_stats AS ps on i.object_id = ps.object_id and
i.index_id = ps.index_id

-- Declare the cursor for the list of indexes to be processed.
DECLARE curIndexes CURSOR FOR SELECT * FROM @work_to_do

-- Open the cursor.
OPEN curIndexes

-- Loop through the indexes
WHILE (1=1)
BEGIN
    FETCH NEXT FROM curIndexes
    INTO @objectid, @indexid, @density, @fragmentation, @numrows;
    IF @@FETCH_STATUS < 0 BREAK;

    SELECT
        @objectname = QUOTENAME(o.name)
        , @schemaname = QUOTENAME(s.name)
    FROM
        sys.objects AS o
        INNER JOIN sys.schemas as s ON s.schema_id = o.schema_id
    WHERE
        o.object_id = @objectid;

    SELECT
        @indexname = QUOTENAME(name)
        , @fillfactorset = CASE fill_factor WHEN 0 THEN 0 ELSE 1 END
    FROM
        sys.indexes
    WHERE

<!-- p.833 -->

           object_id = @objectid AND index_id = @indexid;

     IF ((@density BETWEEN 75.0 AND 85.0) AND @fillfactorset = 1) OR (@fragmentation
 < 30.0)
         SET @command = N'ALTER INDEX ' + @indexname + N' ON ' + @schemaname + N'.'
 + @objectname + N' REORGANIZE';
     ELSE IF @numrows >= 5000 AND @fillfactorset = 0
         SET @command = N'ALTER INDEX ' + @indexname + N' ON ' + @schemaname + N'.'
 + @objectname + N' REBUILD WITH (FILLFACTOR = 90)';
     ELSE
         SET @command = N'ALTER INDEX ' + @indexname + N' ON ' + @schemaname + N'.'
 + @objectname + N' REBUILD';
     PRINT convert(nvarchar, getdate(), 121) + N' Executing: ' + @command;
     EXEC (@command);
     PRINT convert(nvarchar, getdate(), 121) + N' Done.';
 END

 -- Close and deallocate the cursor.
 CLOSE curIndexes;
 DEALLOCATE curIndexes;

 IF EXISTS (SELECT * FROM @work_to_do)
 BEGIN
     PRINT 'Estimated number of pages in fragmented indexes: ' + cast(@numpages as
 nvarchar(20))
     SELECT @numpages = @numpages - sum(ps.used_page_count)
     FROM
         @work_to_do AS fi
         INNER JOIN sys.indexes AS i ON fi.objectid = i.object_id and fi.indexid =
 i.index_id
         INNER JOIN sys.dm_db_partition_stats AS ps on i.object_id = ps.object_id
 and i.index_id = ps.index_id

       PRINT 'Estimated number of pages freed: ' + cast(@numpages as nvarchar(20))
 END
 GO

 --Update all statistics
 PRINT 'Updating all statistics.' + convert(nvarchar, getdate(), 121)
 EXEC sp_updatestats
 PRINT 'Done updating statistics.' + convert(nvarchar, getdate(), 121)
 GO

Last updated on 03/30/2026

<!-- p.834 -->

The spDeleteUpdate stored procedure runs
slowly
When the spDeleteUpdate stored procedure runs, it may take tens of seconds for it to delete a
single update. When you use spDeleteUpdate to delete hundreds or thousands of updates
during Windows Server Update Services (WSUS) maintenance, it may take days to finish.

Cause
The slow performance occurs because a primary key isn't set on a temporary table that's
created by spDeleteUpdate .

Resolution
To fix the issue, run the following SQL script against the WSUS database (SUSDB) on every
affected WSUS server. This script sets a primary key on the @revisionList temporary table.

 SQL

 USE [SUSDB]
 GO

 /****** Object: StoredProcedure [dbo].[spDeleteUpdate]          Script Date: 11/2/2020
 8:55:02 AM ******/
 SET ANSI_NULLS ON
 GO

 SET QUOTED_IDENTIFIER ON
 GO

 ALTER PROCEDURE [dbo].[spDeleteUpdate]
     @localUpdateID int
 AS
 SET NOCOUNT ON
 BEGIN TRANSACTION
 SAVE TRANSACTION DeleteUpdate
 DECLARE @retcode INT
 DECLARE @revisionID INT
 DECLARE @revisionList TABLE(RevisionID INT PRIMARY KEY)
 INSERT INTO @revisionList (RevisionID)
     SELECT r.RevisionID FROM dbo.tbRevision r
         WHERE r.LocalUpdateID = @localUpdateID
 IF EXISTS (SELECT b.RevisionID FROM dbo.tbBundleDependency b WHERE

<!-- p.835 -->

b.BundledRevisionID IN (SELECT RevisionID FROM @revisionList))
    OR EXISTS (SELECT p.RevisionID FROM dbo.tbPrerequisiteDependency p WHERE
p.PrerequisiteRevisionID IN (SELECT RevisionID FROM @revisionList))
BEGIN
     RAISERROR('spDeleteUpdate got error: cannot delete update as it is still
referenced by other update(s)', 16, -1)
     ROLLBACK TRANSACTION DeleteUpdate
     COMMIT TRANSACTION
     RETURN(1)
END
INSERT INTO @revisionList (RevisionID)
     SELECT DISTINCT b.BundledRevisionID FROM dbo.tbBundleDependency b
          INNER JOIN dbo.tbRevision r ON r.RevisionID = b.RevisionID
          INNER JOIN dbo.tbProperty p ON p.RevisionID = b.BundledRevisionID
          WHERE r.LocalUpdateID = @localUpdateID
              AND p.ExplicitlyDeployable = 0
IF EXISTS (SELECT IsLocallyPublished FROM dbo.tbUpdate WHERE LocalUpdateID =
@localUpdateID AND IsLocallyPublished = 1)
BEGIN
     INSERT INTO @revisionList (RevisionID)
          SELECT DISTINCT pd.PrerequisiteRevisionID FROM dbo.tbPrerequisiteDependency
pd
              INNER JOIN dbo.tbUpdate u ON pd.PrerequisiteLocalUpdateID =
u.LocalUpdateID
              INNER JOIN dbo.tbProperty p ON pd.PrerequisiteRevisionID = p.RevisionID
              WHERE u.IsLocallyPublished = 1 AND p.UpdateType = 'Category'
END
DECLARE #cur CURSOR LOCAL FAST_FORWARD FOR
     SELECT t.RevisionID FROM @revisionList t ORDER BY t.RevisionID DESC
OPEN #cur
FETCH #cur INTO @revisionID
WHILE (@@ERROR=0 AND @@FETCH_STATUS=0)
BEGIN
     IF EXISTS (SELECT b.RevisionID FROM dbo.tbBundleDependency b WHERE
b.BundledRevisionID = @revisionID
                     AND b.RevisionID NOT IN (SELECT RevisionID FROM @revisionList))
         OR EXISTS (SELECT p.RevisionID FROM dbo.tbPrerequisiteDependency p WHERE
p.PrerequisiteRevisionID = @revisionID
                        AND p.RevisionID NOT IN (SELECT RevisionID FROM
@revisionList))
     BEGIN
          DELETE FROM @revisionList WHERE RevisionID = @revisionID
          IF (@@ERROR <> 0)
          BEGIN
              RAISERROR('Deleting disqualified revision from temp table failed', 16,
-1)
              GOTO Error
          END
     END
     FETCH NEXT FROM #cur INTO @revisionID
END
IF (@@ERROR <> 0)
BEGIN
     RAISERROR('Fetching a cursor to value a revision', 16, -1)
     GOTO Error

<!-- p.836 -->

 END
 CLOSE #cur
 DEALLOCATE #cur
 DECLARE #cur CURSOR LOCAL FAST_FORWARD FOR
     SELECT t.RevisionID FROM @revisionList t ORDER BY t.RevisionID DESC
 OPEN #cur
 FETCH #cur INTO @revisionID
 WHILE (@@ERROR=0 AND @@FETCH_STATUS=0)
 BEGIN
     EXEC @retcode = dbo.spDeleteRevision @revisionID
     IF @@ERROR <> 0 OR @retcode <> 0
     BEGIN
         RAISERROR('spDeleteUpdate got error from spDeleteRevision', 16, -1)
         GOTO Error
     END
     FETCH NEXT FROM #cur INTO @revisionID
 END
 IF (@@ERROR <> 0)
 BEGIN
     RAISERROR('Fetching a cursor to delete a revision', 16, -1)
     GOTO Error
 END
 CLOSE #cur
 DEALLOCATE #cur
 COMMIT TRANSACTION
 RETURN(0)
 Error:
     CLOSE #cur
     DEALLOCATE #cur
     IF (@@TRANCOUNT > 0)
     BEGIN
         ROLLBACK TRANSACTION DeleteUpdate
         COMMIT TRANSACTION
     END
     RETURN(1)
 GO

Last updated on 03/30/2026

<!-- p.837 -->

Troubleshoot issues with WSUS client
agents
This article helps you diagnose and resolve issues with the Windows Server Update Services
(WSUS) client agents.

Original product version: Windows Server Update Services
Original KB number: 10132

When you experience issues with the WSUS client agents, they can manifest themselves in
many ways. Some common problems are listed here:

     It could be an issue with the client settings for Group Policy.
     It could be an issue with BITS.
     It could be an issue with the WSUS agent service.
     It could be related to a network issue that prevents the client from reaching the server.
     It could be an issue with the Automatic Update Agent Store.
     It could be an issue in which clients have duplicate WSUS client IDs caused by disk
     cloning.

Verify that the client is configured correctly
When you troubleshoot issues with a WSUS client agent, first make sure the client is properly
configured. Make sure the proper Active Directory Group Policy is being received by the client,
and the details of the WSUS server are present. You can do so by running the following
command:

 Console

 GPRESULT /V > GPRESULT.TXT

Open the text file in Notepad and find the name of your WSUS policy. For example, if your
WSUS policy is named WSUS, you can find it in the GPRESULT.TXT file within the Computer
Settings section under the Applied Group Policy Objects heading. Below is an example:

 Output

 Applied Group Policy Objects
 -----------------------------
 Default Domain Policy
 WSUS
 Local Group Policy

If the WSUS settings aren't present, possible causes include:

     The system doesn't have the Group Policy from the domain.

<!-- p.838 -->

     The Group Policy isn't targeted to the client system.

To fix this issue, ensure that the Group Policy is successfully updated on each client, and that
the WSUS setting is properly configured.

To update the Group Policy on the client, run GPUpdate /force from a Command Prompt.

For more information about configuring Group Policy for WSUS clients, see Configure
Automatic Updates by Using Group Policy.

Check for issues relating to BITS

  ７ Note

  Windows Update Delivery Optimization allows clients to download updates from
  Microsoft Update or a WSUS server for Windows 10, Windows 11, and server operating
  systems newer than Windows Server 2016. For more information, see common issues with
  Delivery Optimization and a comprehensive list of all Delivery Optimization settings.

Background Intelligent Transfer Service (BITS) is the service used by WSUS to download
updates from Microsoft Update to the main WSUS server, and from WSUS servers to their
clients. Some download issues may be caused by problems with BITS on the server or client
computers. When you troubleshoot download problems, you should ensure that BITS is
running properly on all affected computers.

The BITS service must run under the LocalSystem account by default. To configure the service
to run under the correct account, follow these steps:

   1. Open a Command Prompt and run the following command:

       Console

       sc config bits obj= LocalSystem

     A space must occur between obj= and LocalSystem. If successful, you should receive the
     following output:

       Output

       [SC] ChangeServiceConfig SUCCESS

   2. Stop and restart BITS.

To view the BITS service status, open a Command Prompt and run the following command:

 Console

 sc query bits

<!-- p.839 -->

If BITS is running, you should see the following output:

 Output

 SERVICE_NAME: bits
 TYPE: 20 WIN32_SHARE_PROCESS
 STATE: 4 RUNNING

If BITS isn't running, you'll see the following output:

 Output

 SERVICE_NAME: bits
 TYPE: 20 WIN32_SHARE_PROCESS
 STATE: 1 STOPPED

Usually it's possible to resolve BITS issues by stopping the service and restarting it. To stop and
restart the BITS service, run the following commands from a Command Prompt:

 Console

 sc stop bits
 sc start bits

  ７ Note

  You must be logged on as a local administrator to stop and restart BITS.

BITS fails to start
If the BITS service fails to start, look in the event log for any BITS-related error. You can use the
following table to diagnose the cause of these errors.

                                                                                         ﾉ   Expand table

 Error name                               Error code      Description

 ERROR_SERVICE_DOES_NOT_EXIST             0x80070424      See the section on repairing the BITS configuration below.

 ERROR_SERVICE_NOT_IN_EXE                 0x8007043B      BITS isn't listed as one of the services in the netsvcs svchost gro

 ERROR_SERVICE_DISABLED                   0x80070422      BITS has been disabled. Enable the BITS service.

 ERROR_SERVICE_DEPENDENCY_DELETED         0x80070433,     A service appearing in the BITS service dependency list cannot
 ERROR_SERVICE_DEPENDENCY_FAIL            0x8007042c      started. Make sure the dependency list for the BITS service is co
                                                          Windows Vista: RpcSs, EventSystem (also http.sys and
                                                          LanManWorkstation when peer caching is enabled)
                                                          Windows Server 2003: Rpcss, EventSystem
                                                          Windows XP: Rpcss
                                                          Windows 2000: Rpcss, SENS, Wmi

 ERROR_PATH_NOT_FOUND                     0x80070003      Pre-Windows Vista: %ALLUSERSPROFILE%\Microsoft\Network d
                                                          exist

<!-- p.840 -->

 Error name                              Error code     Description

 ERROR_FILE_NOT_FOUND                    0x80070002     The Parameters key is missing. Ensure that the following keys a
                                                        values exist:
                                                        HKLM\SYSTEM\CurrentControlSet\Services\BITS\Parameters\Serv
                                                        %SystemRoot%\System32\qmgr.dll

 REGDB_E_CLASSNOTREG,                    0x80040154,    BITS for Windows 2000 is dependent on SENS and EventSystem
 EVENT_E_INTERNALERROR                   0x80040206     services. If the COM+ catalog is corrupted, BITS may fail with th
                                                        code.

BITS jobs are failing
If the client is properly configured to receive updates, BITS is configured correctly, and BITS
appears to start and run properly, you may be experiencing an issue where BITS jobs
themselves are failing. To verify it, look in the event log for any BITS-related errors. You can use
the following table to diagnose the cause of these errors.

                                                                                       ﾉ   Expand table

 Error name                                Error code    Description

 E_INVALIDARG                              0x80070057    An incorrect proxy server name was specified
                                                         in the user's Internet Explorer proxy settings.
                                                         This error is also seen when credentials are
                                                         supplied for authentication schemes that
                                                         aren't NTLM/Negotiate, but the user name or
                                                         password is null. Change the user's Internet
                                                         Explorer proxy settings to be a valid proxy
                                                         server. Or change the credentials not to be
                                                         NULL user name/password for schemes other
                                                         than NTLM/Negotiate.

 ERROR_WINHTTP_NAME_NOT_RESOLVED           0x80072ee7    The server/proxy could not be resolved by
                                                         BITS. Internet Explorer on the same machine
                                                         in the context of the job owner would see the
                                                         same problem. Try downloading the same file
                                                         via the web browser using the context of the
                                                         job owner.

 ERROR_HTTP_INVALID_SERVER_RESPONSE        0x80072f78    It's a transient error and the job will continue
                                                         downloading.

 BG_E_INSUFFICIENT_RANGE_SUPPORT           0x80200013    BITS uses range headers in HTTP requests to
                                                         request parts of a file. If the server or proxy
                                                         server doesn't understand range requests
                                                         and returns the full file instead of the
                                                         requested range, BITS puts the job into the
                                                         ERROR state with this error. Capture the
                                                         network traffic during the error and examine
                                                         if HTTP GET requests with Range header are
                                                         getting valid responses. Check proxy servers
                                                         to ensure that they are configured correctly
                                                         to support Range requests.
