---
title: "Welcome — pages 841-880"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0841-0880
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0841-0880
family: sccm
documentKind: "doc"
abstract: "Error name Error code Description BG_E_MISSING_FILE_SIZE 0x80200011 When BITS sends a HEAD request and the server/proxy doesn't return Content-Length header in the response, BITS puts the job in ERROR state with this error. Check the proxy server and WSUS server to ensure that t"
---

# Welcome — pages 841-880

<!-- p.841 -->

 Error name                              Error code    Description

 BG_E_MISSING_FILE_SIZE                  0x80200011    When BITS sends a HEAD request and the
                                                       server/proxy doesn't return Content-Length
                                                       header in the response, BITS puts the job in
                                                       ERROR state with this error. Check the proxy
                                                       server and WSUS server to ensure that they
                                                       are configured correctly. Some versions of
                                                       the Apache 2.0 proxy server are known to
                                                       exhibit this behavior.

 BG_E_HTTP_ERROR_403                     0x80190193    When the server returns HTTP 403 response
                                                       in any of the requests, BITS puts the job in
                                                       ERROR state with this error code. HTTP 403
                                                       corresponds to Forbidden: Access is denied.
                                                       Check access permissions for the account
                                                       running the job.

 ERROR_NOT_LOGGED_ON                     0x800704dd    The SENS service isn't receiving user logon
                                                       notifications. BITS (version 2.0 and later)
                                                       depends on logon notifications from Service
                                                       Control Manager, which in turn depends on
                                                       the SENS service. Ensure that the SENS
                                                       service is started and running correctly.

Repair a corrupted BITS configuration
To repair corrupted BITS service configuration, you can enter the BITS service configuration
manually.

  ７ Note

  This action should only be taken in circumstances where all other troubleshooting
  attempts have failed. You must be an administrator to modify the BITS configuration.

To repair a corrupted BITS configuration, follow these steps:

   1. Open a Command Prompt.

   2. Enter the following commands, press ENTER after you type each command:

       Console

       sc config bits binpath= "%systemroot%\system32\svchost.exe –k netsvcs"
       sc config bits depend= RpcSs/EventSystem
       sc config bits start= delayed-auto
       sc config bits type= interact type=own
       sc config bits error= normal
       sc config bits obj= LocalSystem
       sc privs bits privileges=
       SeCreateGlobalPrivilege/SeImpersonatePrivilege/SeTcbPrivilege/SeAssignPrimaryT
       okenPrivilege/SeIncreateQuotaPrivilege
       sc sidtype bits unrestricted
       sc failure bits reset= 86400 actions=restart/60000/restart/120000

<!-- p.842 -->

   3. Stop and restart BITS.

Issues with the WSUS agent service
Make sure that the Windows Update service can start successfully.

To view the current status of the Windows Update service, open a Command Prompt and run
the following command:

 Console

 sc query wuauserv

If WUAUSERV is running, you should see the following output:

 Output

 SERVICE_NAME: wuauserv
 TYPE: 20 WIN32_SHARE_PROCESS
 STATE: 4 RUNNING

If WUAUSERV isn't running, you see the following output:

 Output

 SERVICE_NAME: wuauserv
 TYPE: 20 WIN32_SHARE_PROCESS
 STATE: 1 STOPPED

Verify that you can start the WUAUSERV service successfully. You must be logged on as a local
administrator to stop and restart WUAUSERV.

To start the WUAUSERV service, run the following commands from a Command Prompt:

 Console

 sc start wuauserv

If the client agent fails to start and run properly, check the Windows Update Agent version. If
the agent isn't up to date, update the Windows Update Agent to the latest version .

You can also reset Windows Update components.

After you run the fix or update the agent, run wuauclt /detectnow . Check windowsupdate.log
to make sure there's no issues.

Make sure the WSUS server is reachable from the
client

<!-- p.843 -->

Make sure that you can access the URL http://<WSUSSERVER:port>/iuident.cab and download
the file without errors.

If the WSUS server is unreachable from the client, the most likely causes include:

     There's a name resolution issue on the client.
     There's a network-related issue, such as a proxy configuration issue.

Use standard troubleshooting procedures to verify name resolution is working on the network.
If name resolution is working, the next step is to check for proxy issues. Check
windowsupdate.log (C:\windows) to see if there are any proxy related errors. You can run the
proxycfg command to check the WinHTTP proxy settings.

If there are proxy errors, go to Internet Explorer > Tools > Connections > LAN Settings,
configure the correct proxy, and then make sure you can access the WSUS URL specified.

Once done, you can copy these user proxy settings to the WinHTTP proxy settings by using the
proxycfg -u command. After the proxy settings are specified, run wuauclt /detectnow from a

Command Prompt and check windowsupdate.log for errors.

Rebuild the Automatic Update Agent Store
When there are issues downloading updates and there are errors relating to the software
distribution store, complete the following steps on the client:

     Stop the Automatic Updates service by running sc stop wuauserv from a Command
     Prompt.
     Rename the software distribution folder (for example, C:\Windows\SoftwareDistribution).
     Restart the Automatic Update service by running sc start wuauserv from a Command
     Prompt.
     From a Command Prompt, run wuauclt /resetauthorization /detectnow .
     From a Command Prompt, run wuauclt /reportnow .

Check for clients with the same SUSclient ID
You may experience an issue where only one WSUS client appears in the console. Or you may
notice that out of a group of clients, only one appears in the console at a time but the exact
one that does appear may change over time. This issue can happen when systems are imaged
and the clients end up having the same SUSclientID .

For those clients that aren't working properly because of the same SUSclientID , complete the
following steps:

     Stop the Automatic Updates service by running sc stop wuauserv from a Command
     Prompt.

     Delete the SUSclientID registry key from the following location:

<!-- p.844 -->

     HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\WindowsUpdate

     Restart the Automatic Update service by running sc start wuauserv from a Command
     Prompt.

     From a Command Prompt, run wuauclt /resetauthorization /detectnow .

     From a Command Prompt, run wuauclt /reportnow .

Last updated on 03/30/2026

<!-- p.845 -->

How to troubleshoot WSUS connection
failures
This article introduces several procedures for troubleshooting Windows Server Update Service
(WSUS) connection failures.

  ７ Note

  Home users: This article is intended only for technical support agents and IT professionals.
  If you're looking for help with a problem, ask the Microsoft Community      .

Original product version: Configuration Manager (current branch)
Original KB number: 4025764

Verify the prerequisites
     If you are using WSUS 3.0 SP2 on Windows Server 2008 R2, you must have update
     4039929     or a later-version update package installed on the WSUS server.

     To verify the server version, follow these steps:

        1. Open the WSUS console.
        2. Click the server name.
        3. Locate the version number under Overview > Connection > Server Version.
        4. Check whether the version is 3.2.7600.283 or a later version.

     If you are using WSUS on Windows Server 2012 or a later version, you must have one of
     the following Security Quality Monthly Rollups or a later-version rollup installed on the
     WSUS server:
        Windows Server 2012 - KB4039873
        Windows Server 2012 R2 - KB4039871
        Windows Server 2016 - KB4039396

  ７ Note

  If you're using Configuration Manager and the software update point is installed on a
  remote site system server, the WSUS Administration Console must be installed on the site

<!-- p.846 -->

  server. For WSUS 3.0 SP2, KB 4039929               or a later update must also be installed on the
  WSUS Administration console. After you install 4039929                     (remotely or locally), a server
  restart is required. After the restart, check whether the issue persists.

Troubleshoot connection failures
To troubleshoot connection failures, follow these steps:

   1. Verify that the Update Services service and the World Wide Web Publishing Service are
       running on the WSUS server.
   2. Verify that the Default website or WSUS Administration website is running on the WSUS
       server.
   3. Review the IIS logs for the WSUS Administration website ( c:\inetpub\logfiles ), and
       check for errors.

Code definitions
The following table defines common error codes. For more information about HTTP status
code in IIS, see The HTTP status code in IIS 7 and later versions               .

                                                                                               ﾉ   Expand table

 ID     Explanation

 200    Success

 206    Continuation: OK

 401    Authorization: OK if followed by 200

 403    Access failure: Certificate issues or incorrect IIS configuration.

 404    Not found: Missing Virtual directory or IIS configuration

 500    Service not available

 503    Busy: This can be caused by a WSUS application pool memory issue or just too many client
        connections. To fix the issue, increase the WSUS Application Pool Private memory limit to 4-8 GB.
        Some environments may require more than 8 GB; adjust this setting as needed. See Configure an
        Application Pool to Recycle after Reaching Maximum Used Memory (IIS 7).

  ７ Note

<!-- p.847 -->

  Accessing most WSUS URLs in a browser will return a 403 error.

503 errors in IIS may be accompanied by xxxx2ee2 errors in the c:\windows\windowsupdate.log
file on clients.

To resolve 503 IIS errors, a client time-out, or a large number of roundtrip errors, see The
complete guide to WSUS and Configuration Manager SUP maintenance.

If a client's IP address doesn't appear in the IIS logs, verify that the client is set to connect to
the correct WSUS server. This situation may also occur because of network blocking or because
the server logs a special error.

      On the WSUS server, check the C:\windows\system32\logfiles\httperr logs for errors.

      On the client, check the following registry subkey to determine whether the correct FQDN
      of the WSUS server is set:

      Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate

  ７ Note

  For Configuration Manager clients, check the ccm\logs\locationservices.log file for a
  WSUS entry to verify that the client is getting the correct server URL. You may have to
  force the Configuration Manager client to run another scan by using the Software Updates
  Scan Cycle from the agent in order for the service to log this entry.

 Last updated on 03/30/2026

<!-- p.848 -->

Troubleshoot high CPU usage on a WSUS
server
This article introduces several procedures for troubleshooting high CPU usage in Windows
Server Update Service (WSUS).

  ７ Note

  Home users: This article is intended only for technical support agents and IT professionals.
  If you're looking for help with a problem, ask the Microsoft Community         .

Original product version: Configuration Manager (current branch)
Original KB number: 4489045

High CPU usage can occur if the WSUS database (SUSDB) is not clean. After the server runs for
a while, there can be too many updates for the WSUS server to provide to the clients.

In this situation, if a failure occurs or a new WSUS server is installed or an unrelated issue
prevents clients from scanning for a few days, all the clients might start scanning and continue
to scan constantly and never actually complete a scan or install updates.

To fix the issue, you have to clean up the WSUS server and decline superseded updates. Follow
the steps in the order below as a monthly cleanup routine. However, if you are troubleshooting
high CPU issues, we recommend that you do step 4 first and then step 3. You should defer
steps 1 and 2 until the CPU usage level decreases.

Step 1: Back up the WSUS database
Backing up the WSUS database can improve the performance slightly.

Step 2: Run the WSUS Server Cleanup Wizard
Running the WSUS Server Cleanup Wizard can improve database performance. However, it
does not reduce the number of updates that the clients are scanning. Additionally, it can take
many hours or days for the wizard to run without necessarily resolving the issue.

Step 3: Reindex the WSUS database

<!-- p.849 -->

Reindexing the WSUS database can improve database performance if it's fragmented. To do
this, run the following commands.

   1. Update the statistics by using the FULLSCAN option.

       SQL

       Use <dbname>
       Go
       Exec sp_msforeachtable 'update statistics ? with fullscan'
       Go

   2. Rebuild the indexes.

       SQL

       Use <dbname>
       Go
       Exec sp_msforeachtable 'DBCC DBREINDEX (''?'')'
       Go

Step 4: Decline superseded updates
Declining superseded updates immediately reduces the number of updates that are being
scanned.

To decline superseded updates or perform any WSUS actions in a situation where the WSUS
application pool recycles too quickly, you can first stop the clients from connecting to the
WSUS application pool. To do this, connect to the WSUS server by using the WSUS console,
and then synchronize the WSUS server with the upstream server and with Configuration
Manager (if it is used). If you are using Configuration Manager, it's important to synchronize to
the latest version of the update in the Configuration Manager console so that clients will see
that WSUS has current and valid updates.

To disconnect the clients, use one of the following methods.

Method 1: Create a test application pool
   1. Right-click Application pools in the Internet Information Services (IIS) Manager area,
     and then select Add Application Pool to create a test application pool.

   2. Select Client web service > Manage application > Advanced settings, and then change
     the application pool to the test application pool that you created.

<!-- p.850 -->

Method 2: Change the port for the WSUS website
   1. Select WSUS Administration Web Site > Edit Bindings.

   2. Change the WSUS console to connect to the new port, run the script, and synchronize
     with USS.

        ７ Note

        This method will cause syncing with Configuration Manager to fail.

Method 3: Use Firewall rules to block all client IP addresses or
allow only USS and site server incoming connections
After the clients are disconnected from the WSUS server, you can run the PowerShell script by
using the -skipdecline (and -exclusion period, if necessary) parameters to determine the
total number of superseded updates that can be declined. Then, run the script again by using -
skipdecline to actually decline the updates.

In extreme cases in which the PowerShell script can't run because of timeouts, you can add the
supersedence column to the WSUS console when all updates are displayed, and then decline
the updates manually by following these steps:

   1. Open the Windows Update Services Microsoft Management Console (MMC).
   2. Select the All Updates view. To do it, set the display to show the Approval status of Any
     except Declined with a status of Any, and then click Refresh.
   3. Right-click the column headers, and then select Supersedence.
   4. Left-click the Supersedence column to sort by supersedence.
   5. Select and decline the superseded updates.

The performance issue can normally be resolved after the valid update is reduced to fewer than
7,000 connections (but fewer than 5,000 is preferred). You might have to restrict connections to
the WSUS administration website for a few days to let the clients complete all scans. We also
recommend that you reindex the database after you decline superseded updates. If you're
using Configuration Manager, also perform a sync between WSUS and Configuration Manager
while the clients are not connecting.

After you complete these steps, you should limit connections if the CPU usage is still too high.
To do this, follow these steps:

<!-- p.851 -->

   1. Open Internet Information Services (IIS) Manager > WSUS Administration Web Site >
      Manage web site > Advanced settings > Limits > Maximum concurrent connections.

   2. Set the value to 50 or 100.

   3. Monitor the W3Wp process in Task Manager and the total CPU on the server.

   4. Open Task Manager > Resource Monitor, and note the PID for the WSUS application
      pool. If you are unsure which w3wp process is running the WSUS application pool, you
      can use Appcmd (Method 2) to identify the PID easily.

By default, the PID should change only one time every 29 hours. If it changes more often, your
connection limit may be too high for the current CPU and memory setting for the WSUS
application pool.

Monitor for stable w3wp memory and stable overall CPU use of less than 90 percent. As the
steady state CPU and memory use decrease, you can slowly increase connection limits to the
WSUS administration website. Depending on what kind of situation you are in, the memory
usage may take several days to return to a stable state. Increasing the connection limits might
need to occur in small increments and over the course of several days.

Reference
High CPU/High Memory in WSUS following Update Tuesdays

 Last updated on 03/30/2026

<!-- p.852 -->

Troubleshoot WSUS synchronization and
import issues
Applies to: Windows Server Update Services

Starting in July 2020, users have experienced WSUS synchronization and import problems with
the Windows Update (WU) or Microsoft Update (MU) endpoints.

This article describes how to troubleshoot some common problems. You can use some of these
troubleshooting techniques (such as network captures) for many other issues, too.

Endpoints
Currently WSUS uses the following endpoints to synchronize metadata:

     https://sws.update.microsoft.com

     Most WSUS servers should synchronize with this new endpoint. Starting from July 2020,
     this endpoint accepts only Transport Layer Security (TLS) 1.2 connections. And some
     ciphers were disabled.

     https://sws1.update.microsoft.com

     This old endpoint will be decommissioned eventually. For more information, see End of
     synchronization for WSUS 3.0 SP2 . This endpoint supports TLS 1.2, TLS 1.1, and TLS 1.0
     connections.

     https://fe2.update.microsoft.com

     This old endpoint is decommissioned as a WSUS synchronization endpoint, and
     connections to it will fail. However, Windows Update clients configured to synchronize
     with Microsoft Update may continue to use this endpoint.

When you experience WSUS synchronization or manual import problems, first check which
endpoint you're synchronizing with:

   1. Open an elevated PowerShell Command Prompt window on the WSUS server.

   2. To find the current synchronization endpoint, run the following PowerShell script:

<!-- p.853 -->

       PowerShell

       $server = Get-WsusServer
       $config = $server.GetConfiguration()
       # Check current settings before you change them
       $config.MUUrl

Windows Server 2012 and later versions should be configured to use the
https://sws.update.microsoft.com endpoint. If you're still using

https://sws1.update.microsoft.com or https://fe2.update.microsoft.com , change to the new

endpoint by following the steps in WSUS synchronization fails with SoapException. If necessary,
troubleshoot connection issues with the https://sws.update.microsoft.com endpoint.

Issue 1: Manual import fails, but synchronization
succeeds
Many users import updates into WSUS manually, and some updates must be imported
manually. For example, preview updates that are released in the third and fourth weeks of the
month must be manually imported. Starting at the end of July 2020, you might have found you
can't manually import updates.

However, some WSUS servers can still import updates successfully. And the usual
synchronization with WU and MU continues to work.

This issue occurs on WSUS servers that are running Windows Server 2012, Windows Server
2012 R2, Windows Server 2016, or Windows Server 2019.

Troubleshoot issue 1
   1. Run the PowerShell script in Endpoints to determine which endpoints the WSUS servers
     use. You'll probably find that working servers are communicating with

<!-- p.854 -->

     https://fe2.update.microsoft.com or https://sws1.update.microsoft.com , and failing

     servers are communicating with https://sws.update.microsoft.com .

   2. Check the %Program Files%\Update Services\LogFiles\SoftwareDistribution.log file for
     errors when you manually import updates. Look for errors that resemble the following
     example:

       Output

       ProcessWebServiceProxyException found Exception was WebException. Action:
       Retry. Exception Details: System.Net.WebException: The underlying connection
       was closed: An unexpected error occurred on a send. --->
       System.IO.IOException: Unable to read data from the transport connection: An
       existing connection was forcibly closed by the remote host. --->
       System.Net.Sockets.SocketException: An existing connection was forcibly closed
       by the remote host
          at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32
       size)
          -- End of inner exception stack trace ---
          ...
          at System.Net.TlsStream.ProcessAuthentication(LazyAsyncResult result)
          at System.Net.TlsStream.Write(Byte[] buffer, Int32 offset, Int32 size)
          at System.Net.PooledStream.Write(Byte[] buffer, Int32 offset, Int32 size)
          at System.Net.ConnectStream.WriteHeaders(Boolean async)

The following message in the error indicates that the WSUS server tried to connect with
WU/MU by using TLS, but WU/MU closed the connection:

  An existing connection was forcibly closed by the remote host.

The following screenshot shows a network capture of the connection attempt.

                                                                                           

In the network capture, frame 874 is the Client Hello packet that uses TLS 1.0. Frame 877 is the
server response. The response includes the ACK (A) and RST (R) flags. Because the

<!-- p.855 -->

https://sws.update.microsoft.com endpoint supports only TLS 1.2 connections, it denies the

connection, and issues a reset response.

Resolution for issue 1
This issue occurs because WSUS import functionality can't use TLS 1.2.

To fix this issue, use one of the following methods:

     Configure .NET Framework to use TLS 1.2 by using registry keys.

     To set the registry keys, see Configure for strong cryptography. Restart the server after
     you set the registry keys.

     Create or update the w3wp.exe.config file to enable TLS 1.2.

        ７ Note

        This change will apply to all w3wp.exe instances that are created, regardless of
        whether they are for WSUS. W3wp.exe uses TLS 1.2 if the remote side supports this
        version. If TLS 1.1 and TLS 1.0 are enabled, W3wp.exe negotiates these protocols if
        the target site doesn't support TLS 1.2.

     If the %SystemRoot%\system32\inetsrv\w3wp.exe.config file doesn't exist, follow these
     steps:

        1. Create a new file that's named W3wp.exe.config in the
              %SystemRoot%\system32\inetsrv folder.

        2. Open the file in a text editor, such as Notepad.

        3. Add the following lines to the file, and then save the file:

               XML

               <?xml version="1.0" encoding="utf-8"?>
               <configuration>
                  <runtime>
                     <AppContextSwitchOverrides
               value="Switch.System.Net.DontEnableSystemDefaultTlsVersions=false"/>
                  </runtime>
               </configuration>

<!-- p.856 -->

     If the %SystemRoot%\system32\inetsrv\w3wp.exe.config file already exists, follow these
     steps:

        1. Open the file in Notepad, or another text editor.

        2. Add the following lines immediately under the <configuration> element, and then
           save the file:

              XML

              <runtime>
                 <AppContextSwitchOverrides
              value="Switch.System.Net.DontEnableSystemDefaultTlsVersions=false"/>
              </runtime>

     After you create or update the W3wp.exe.config file, open an elevated Command Prompt
     window, and then run iisreset to restart all worker processes. Test whether manual
     import now works.

Issue 2: Manual import fails after you disable TLS 1.1
or TLS 1.0
TLS 1.1 and TLS 1.0 are being phased out because they're considered insecure. After you
disable these protocols, you can no longer import updates. However, synchronization
continues to work.

This issue occurs on WSUS servers that are running Windows Server 2012, Windows Server
2012 R2, Windows Server 2016, or Windows Server 2019.

Troubleshoot issue 2
WSUS logs which SSL/TLS versions are enabled when it starts. To determine the SSL/TLS
versions, follow these steps:

   1. Restart the WSUS service.

   2. Run iisreset at an elevated command prompt to force WSUS to go through the startup
     sequence.

   3. Open the WSUS console, and connect to the server.

<!-- p.857 -->

   4. Open %Program Files%\Update Services\LogFiles\SoftwareDistribution.log , look for
     entries that start at SCHANNEL Protocol. You should see entries that resemble the
     following example:

       Output

       SCHANNEL Protocol 'TLS 1.0' disabled
       SCHANNEL Protocol 'TLS 1.1' disabled
       SCHANNEL Protocols subkey for 'TLS 1.2' not found. Protocol is enabled

     These entries show that TLS 1.1 and TLS 1.0 are disabled, and TLS 1.2 is enabled.

If the import process fails, SoftwareDistribution.log logs the following error entry:

 Output

 ProcessWebServiceProxyException found Exception was WebException. Action: Retry.
 Exception Details: System.Net.WebException: The underlying connection was closed:
 An unexpected error occurred on a receive. --->
 System.ComponentModel.Win32Exception: The client and server cannot communicate,
 because they do not possess a common algorithm

The following screenshot shows a network capture of the connection attempt.

                                                                                               

In the network capture, frames 1518-1520 show the three-way handshake (SYN, SYN ACK, ACK)
between the client and server. Frame 1536 is an ACK FIN packet from the WSUS server.

WSUS closes the connection, because all protocols it knows how to use for import (SSL3, TLS
1.0, TLS 1.1) are disabled and it can't use TLS 1.2.

Resolution for issue 2
This issue is similar to issue 1, in which WSUS import can't use TLS 1.2. To fix this issue, use
Resolution for issue 1.

Issue 3: Synchronization fails on Windows Server 2012
and Windows Server 2012 R2 WSUS servers that apply
only security-only updates

<!-- p.858 -->

Windows Server 2012 and Windows Server 2012 R2 servicing contain the following update
tracks:

      A security-only update, which isn't cumulative. It contains only security fixes. For example,
      June 9, 2020—KB4561673 (Security-only update) .
      A Monthly Rollup, which is cumulative. It contains all security fixes from the security-only
      update, and also contains non-security fixes. For example, June 9, 2020—KB4561666
      (Monthly Rollup)     .

WSUS on Windows Server 2012 and Windows Server 2012 R2 can't use TLS 1.2 for
synchronization unless one of the following Monthly Rollups or a later Monthly Rollup is
installed:

      June 27, 2017—KB4022721 (Preview of Monthly Rollup)         for Windows Server 2012
      June 27, 2017—KB4022720 (Preview of Monthly Rollup)         for Windows Server 2012 R2

The change that enables WSUS to use TLS 1.2 is a non-security fix, it's included only in the
Monthly Rollups.

Some users opt to install only the security-only updates and never install the Monthly Rollups.
Therefore, their WSUS servers don't have the update that enables TLS 1.2 installed. After the
https://sws.update.microsoft.com endpoint is changed to accept only TLS 1.2 connections,

these WSUS servers can no longer synchronize with the endpoint. This issue also occurs on a
freshly installed Windows Server 2012 or Windows Server 2012 R2 WSUS server that hasn't
installed any Monthly Rollups.

Troubleshoot issue 3
If the WSUS server has the correct updates installed, WSUS will log which SSL/TLS versions are
enabled when it starts. Follow these steps on the WSUS server:

   1. Restart the WSUS service.

   2. Run iisreset from an elevated command prompt to force WSUS to go through the
      startup sequence.

   3. Open the WSUS console, and connect to the server.

   4. Open %Program Files%\Update Services\LogFiles\SoftwareDistribution.log , search for
      entries that start with SCHANNEL Protocol. You should see entries that resemble the
      following example:

<!-- p.859 -->

       Output

       SCHANNEL Protocol 'TLS 1.0' disabled
       SCHANNEL Protocol 'TLS 1.1' disabled
       SCHANNEL Protocols subkey for 'TLS 1.2' not found. Protocol is enabled

     If you can't find these entries, it means the update that enables TLS 1.2 isn't installed.

When synchronization fails, SoftwareDistribution.log logs the following error message:

 Output

 WebServiceCommunicationHelper.ProcessWebServiceProxyException
 ProcessWebServiceProxyException found Exception was WebException. Action: Retry.
 Exception Details: System.Net.WebException: The underlying connection was closed:
 An unexpected error occurred on a send. ---> System.IO.IOException: Unable to read
 data from the transport connection: An existing connection was forcibly closed by
 the remote host. ---> System.Net.Sockets.SocketException: An existing connection
 was forcibly closed by the remote host   at
 System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)

The following screenshot shows a network capture of the connection attempt.

                                                                                              

In the network capture, frame 95 is the Client Hello packet that uses TLS 1.0. Frame 96 is the
RST packet from https://sws.update.microsoft.com . Because the endpoint supports only TLS
1.2 connections, it denies the connection, and then issues a reset response. The WSUS server
will try several times before it gives up. Therefore, this sequence is repeated.

Resolution for issue 3
To fix this issue, install the latest Monthly Rollup for Windows Server 2012 or Windows Server
2012 R2. Also apply Resolution for issue 1 to prevent the manual import failure.

<!-- p.860 -->

Issue 4: Synchronization fails after July 2020 if WSUS
is integrated with Configuration Manager
Many WSUS installations are integrated with Microsoft Endpoint Configuration Manager
software update points (SUPs). After July 2020, you may experience synchronization failures if
Configuration Manager is configured to synchronize Surface drivers.

This issue occurs on WSUS servers that are running Windows Server 2012, Windows Server
2012 R2, Windows Server 2016, or Windows Server 2019.

Troubleshoot issue 4
When this issue occurs, entries that resemble the following example are logged in
Wsyncmgr.log:

  Output

  Calling ImportUpdateFromCatalogSite for driver update GUIDs
  Generic exception : ImportUpdateFromCatalogSite failed. Arg = 001d4517-c586-4bb1-
  9e66-ed6ff8e8d34f. Error =The underlying connection was closed: An unexpected error
  occurred on a receive.
  Generic exception : ImportUpdateFromCatalogSite failed. Arg = 0037641d-bb9b-4530-
  9568-11e413223106. Error =The underlying connection was closed: An unexpected error
  occurred on a receive.

Also, the %Program Files\Update Services\LogFiles\SoftwareDistribution.log file logs the
following errors:

  Output

  ProcessWebServiceProxyException found Exception was WebException. Action: Retry.
  Exception Details: System.Net.WebException: The underlying connection was closed:
  An unexpected error occurred on a receive. --->
  System.ComponentModel.Win32Exception: The client and server cannot communicate,
  because they do not possess a common algorithm

These errors indicate that the connection was closed. This issue occurs because Configuration
Manager uses the WSUS import functionality. Therefore, it has the same limitations.

Resolution for issue 4
To fix this issue, use Resolution for issue 1.

<!-- p.861 -->

Issue 5: Synchronization fails after July 2020 because
of limited ciphers
You may disable various ciphers to secure TLS connections. Starting from July 2020, your WSUS
servers can no longer synchronize with WU/MU. Also, when https://sws.update.microsoft.com
is changed to accept only TLS 1.2 connections, some ciphers are removed.

This issue occurs on WSUS servers that are running Windows Server 2012, Windows Server
2012 R2, Windows Server 2016, or Windows Server 2019.

Troubleshoot issue 5
The %Program Files\Update Services\LogFiles\SoftwareDistribution.log file logs the following
errors when synchronizing:

 Output

 ProcessWebServiceProxyException found Exception was WebException. Action: Retry.
 Exception Details: System.Net.WebException: The underlying connection was closed:
 An unexpected error occurred on a send. ---> System.IO.IOException: Unable to read
 data from the transport connection: An existing connection was forcibly closed by
 the remote host. ---> System.Net.Sockets.SocketException: An existing connection
 was forcibly closed by the remote host

However, these entries aren't useful to determine whether you have a cipher problem.

In this situation, use a network capture, or check the applied Group Policy Objects (GPOs). To
check the applied GPOs, run the following command at an elevated command prompt:

 Console

 gpresult /scope computer /h GPReport.html

Open GPReport.html in a browser.

                                                                                            

Search for SSL Cipher Suite Order, and the SSL Cipher Suites setting. Usually this setting isn't
configured. If it's configured, the issue may occur because there's no common cipher with
WU/MU.

<!-- p.862 -->

As of August 2020, https://sws.update.microsoft.com supports the following ciphers:

         TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
         TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
         TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
         TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256

   ７ Note

   This list will change over time because ciphers will gradually grow weaker as technology
   improves.

If the GPO is applied, and it doesn't specify one of these ciphers, communication with WU/MU
fails.

The following screenshot shows a network capture.

                                                                                           

In the network capture, frame 400 is the Client Hello packet that uses TLS 1.2. The frame detail
shows which ciphers were sent by the client. Frame 404 is the RST packet from

<!-- p.863 -->

https://sws.update.microsoft.com . Because there's no common cipher, the synchronization

fails.

Resolution for issue 5
To fix this issue, follow these steps:

    1. Use the output of gpresult to determine the GPO that specifies the SSL Cipher Suite
         Order, and then remove the GPO. Or change it to include ciphers that are supported by
         https://sws.update.microsoft.com .

         For Windows Server 2016 and Windows Server 2019, include one of the following ciphers:

              TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
              TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
              TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
              TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256

         For Windows Server 2012 and 2012 R2, include one of the following ciphers:

              TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_P256
              TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_P384
              TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256_P256
              TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256_P384

    2. If the ciphers aren't set by GPO, locate the following registry subkey:

         HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Cryptography\Configuration\SSL\000100

         02

         Add one of the required ciphers to the Functions value of the registry key.

    3. Restart the WSUS server.

To prevent manual import failures, also apply Resolution for issue 1.

A successful connection
The following screenshots show a successful connection when a Windows Server 2016 WSUS
server synchronizes updates.

<!-- p.864 -->

                                                                                           

                                                                                           

In the network capture, frame 191 is the Client Hello packet that uses TLS 1.2. The frame detail
shows which ciphers were sent by the client. Frame 195 is the Server Hello packet from the

<!-- p.865 -->

endpoint. The TLSCipherSuite that's chosen by WU is
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384. The server certificate is also sent in the Server
Hello packet.

Additional connection setup occurs in frames 196-203. The data transfer by the application
(WSUS) and the https://sws.update.microsoft.com endpoint then begins in frame 207.

A note about proxy servers
If you use a proxy server, the network capture will look different. The WSUS server connects to
the proxy, and you may see a CONNECT request with the destination
https://sws.update.microsoft.com , https://sws1.update.microsoft.com , or

https://fe2.update.microsoft.com . WSUS will issue a Client Hello packet with the ciphers it

supports. If the connection isn't successful because of wrong TLS version, or if there is no
common cipher, you may or may not see an RST packet. Proxies tend to return an FIN to the
client to indicate the end of the connection. But this might not be true for every proxy server.
Some proxy servers send an RST packet, or something else.

When you use a proxy, you have to know the IP address of the internal interface of the proxy
server, because WSUS isn't communicating directly with the WU endpoints. If you can't get the
IP address of the proxy server, search the network capture for CONNECT requests, and search
for the URL of the Windows Update endpoint.

References
      WSUS Synchronization fails with SoapException
      How to enable TLS 1.2 on the site servers and remote site systems
      TLS registry settings

 Last updated on 03/30/2026

<!-- p.866 -->

[SDP3][721e15b6-76f5-43d0-a435-
191d3474a359] Windows Server Update
Services and Windows Update Agent
diagnostics
This diagnostic package is designed to collect information used to troubleshoot most Windows
Update issues.

Original product version: Windows Server Update Services
Original KB number: 2793732

Custom uploads
                                                                                         ﾉ    Expand table

 Description                                                    File name

 Compressed copy of file specified by user                      {ComputerName}_filename.zip

General information
                                                                                         ﾉ    Expand table

 Description                                                 File name

 Summary of information gathered about the operating         {ComputerName}__OS_Summary.txt
 system

 List of running tasks                                       {ComputerName}_OS_TaskList.txt

 Basic system information including machine name,            resultreport.xml
 service pack, computer model, and processor name and
 speed

 Environment variables                                       {ComputerName}_OS_EnvironmentVariables.txt

 Event logs for last 14 days (Application, System, and       {ComputerName}_OS_EventLogs.zip
 Security)

 List of installed certificates (Computer and User stores)   {ComputerName}_OS_Certificates.txt

 List of installed services                                  {ComputerName}_OS_Services.txt

 List of installed updates and hotfixes installed            {ComputerName}_Hotfixes.*

 List of user rights (privileges) using showpriv.exe tool    {ComputerName}_UserRights.txt

 Reboot pending flag from Windows Update, CBS,               {ComputerName}_OS_RebootPending.txt
 ConfigMgr Client, and so on

<!-- p.867 -->

Description                                               File name

Resultant set of Group Policies                           {ComputerName}_OS_GPResult.*

System information                                        {ComputerName}_OS_MSInfo.nfo

SystemInfo output                                         {ComputerName}_OS_SysInfo.txt

WMI quota configuration and loaded providers.             {ComputerName}_OS_WMIProviderConfig.txt

IIS information
                                                                                        ﾉ   Expand table

Description                                           File name

IIS configuration information                         {ComputerName}_IISConfiguration.zip

IIS logs (last 5 days)                                {ComputerName}_Logs_IIS.zip

Virtual directory list and configuration              {ComputerName}_IIS_VDirInfo.txt

Networking basic information
                                                                                        ﾉ   Expand table

Description                                                File name

Summary of networking information collected                {ComputerName}__NET_Summary.txt

Active BITS jobs                                           {ComputerName}_OS_BITSTransfers.txt

Basic SMB configuration information, such as output of     {ComputerName}_OS_SMB-Info.txt
net.exe subcommands, such as net share , net sessions ,
net use , net accounts , net config

Basic TCP/IP and networking configuration information,     {ComputerName}_OS_TCPIP-Info.txt
such as TCP/IP registry key and outputs from ipconfig ,
netstat , nbtstat , and netsh commands

Enabled Windows Firewall rules                             {ComputerName}_OS_EnabledFirewallRules.txt

Proxy configuration                                        {ComputerName}_OS_ProxyInfo.txt

Registry keys
                                                                                        ﾉ   Expand table

Description                                                                         File name

HKEY_CURRENT_USER\Software\Policies                                                 {ComputerName}_RegistryKey_HKCUP

HKEY_LOCAL_MACHINE\Software\Microsoft\CCM                                           {ComputerName}_RegistryKey_CCM.tx

HKEY_LOCAL_MACHINE\Software\Microsoft\OLE                                           {ComputerName}_RegistryKey_DCOM.

<!-- p.868 -->

Description                                                                            File name

HKEY_LOCAL_MACHINE\Software\Microsoft\SMS                                              {ComputerName}_RegistryKey_SMS.txt

HKEY_LOCAL_MACHINE\Software\Microsoft\Update Services                                  {ComputerName}_RegistryKey_WSUS.t

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall                 {ComputerName}_RegistryKey_Uninsta

HKEY_LOCAL_MACHINE\Software\Policies                                                   {ComputerName}_RegistryKey_HKLMP

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services                                   {ComputerName}_RegistryKey_Service

Robust Office inventory scan output
                                                                                           ﾉ   Expand table

Description                                                                    File name

File containing a list of all installed applications of the supported Office   {ComputerName}_ROIScan.log
families.

File containing a list of all installed applications of the supported Office   {ComputerName}_ROIScan.zip
families.

Server manager and server roles information
                                                                                           ﾉ   Expand table

Description                                                                                 File name

List of roles and features installed on server media (Windows Server 2008 R2 and later      resultreport.xml
versions)

Windows Update Agent information
                                                                                           ﾉ   Expand table

Description                                                            File name

Windows Update Agent version, service security descriptors,            {ComputerName}__WUA_Summary.txt
and registry settings.

File list in SoftwareDistribution directory                            {ComputerName}_WUA_FileList.txt

File version of Windows Update Agent related EXE/DLL files             {ComputerName}_WUA_FileVersions.txt

WSUS database information
                                                                                           ﾉ   Expand table

Description                                             File name

Database version and security information               {ComputerName}_SQL_Basic.txt

<!-- p.869 -->

 Description                                                File name

 Dead deployments                                           {ComputerName}_SQL_DeadDeployments.txt

 Output of tbConfiguration tables                           {ComputerName}_SQL_SUSDBConfig.txt

 Output of tbSchema tables                                  {ComputerName}_SQL_SUSDBSchema.txt

WSUS server information
                                                                                             ﾉ   Expand table

 Description                                                     File name

 Summary of WSUS server information collected.                   {ComputerName}__WSUS_Summary.txt

 File list of WSUS content directory (only collected with        {ComputerName}_WSUS_FileList_ContentDir.txt
 WSUS diagnostics)

 File list of WSUS installation directory (only collected        {ComputerName}_WSUS_FileList_InstallDir.txt
 with WSUS Diagnostics)

 File versions of EXE/DLL files in WSUS installation             {ComputerName}_WSUS_FileVersions.txt
 directory (only collected with WSUS diagnostics)

 List of approved updates (Not collected for WSUS 4.0)           {ComputerName}_WSUS_ApprovedUpdates.xml

 WSUS basic information                                          {ComputerName}_WSUS_BasicInfo.txt

 WSUS logs                                                       {ComputerName}_Logs_WSUS.zip

 WSUS setup logs (if available)                                  {ComputerName}_Logs_WSUSSetup.zip

References
Microsoft Support Diagnostic Tool resources

Last updated on 03/30/2026

<!-- p.870 -->

WSUS client computers restart
automatically without any notification
when updates are installed on the client
computers
This article provides a solution to an issue in which Windows Server Update Services (WSUS)
client computers restart automatically without any notification when updates are installed on
the client computers.

Original product version: Windows Server Update Services
Original KB number: 931265

Symptoms
Consider the following scenario:

     You use a Microsoft Windows Server Update Services server to deploy updates on WSUS
     client computers.
     A time deadline is set on the WSUS server for the updates to be installed on the WSUS
     client computers.
     The updates are installed on the WSUS client computers when the time deadline expires
     that is set on the WSUS server.

In this scenario, the WSUS client computers restart automatically without any notification even
though the WSUS client computers are configured not to restart automatically without a
notification.

Cause
This issue occurs because the updates that are deployed on the WSUS client computers require
that Windows Installer 3.1 is present on the WSUS client computers.

If Windows Installer 3.1 is not present on the WSUS client computers, Windows Installer 3.1 is
downloaded from the WSUS server and installed on the WSUS client computers, regardless of
the WSUS server approval status.

<!-- p.871 -->

Installation of Windows Installer 3.1 on the WSUS client computers causes the WSUS client
computers to restart because a restart is required for Windows Installer 3.1 to function
correctly.

Resolution

  ２ Warning

  Serious problems might occur if you modify the registry incorrectly by using Registry
  Editor or by using another method. Make sure that you back up the registry       before you
  modify it. These problems might require that you reinstall the operating system. Microsoft
  cannot guarantee that these problems can be solved. Modify the registry at your own risk.

To resolve this issue, follow these steps on the WSUS client computers:

   1. Select Start, select Run, type regedit , and then select OK.

   2. Locate and then select the following registry subkey:

      HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU

   3. In the details pane, right-click NoAutoRebootWithLoggedOnUsers, and then select
      Modify.

   4. Type 1 in the Value data box, and then select OK.

   5. Exit Registry Editor.

   6. Restart the WSUS client computers.

 Last updated on 03/30/2026

<!-- p.872 -->

A WSUS client takes longer than expected
to finish an update scan
This article helps you fix an issue where a Microsoft Windows Server Update Services (WSUS)
client computer takes longer than expected to finish a scan to determine whether an update
applies to the client computer.

Original product version: Configuration Manager
Original KB number: 938947

Symptoms
Consider the following scenario:

     A WSUS client computer is connected to a WSUS or Configuration Manager Software
     Update Services (SUP) server.
     The WSUS client computer runs a scan to determine whether an update applies to the
     client computer.

In this scenario, the WSUS client computer takes longer than expected to finish the scan. For
example, the scan may take hours or days to finish. Additionally, you experience the following
problems on the WSUS client computer:

     Task Manager indicates high CPU usage for the Svchost.exe process.
     You cannot stop the Svchost.exe process.

Cause
This problem occurs if you don't decline expired definition updates or expired malicious
software (also known as malware) updates on the WSUS or SUP server.

Resolution
To resolve this problem, set the option to approve update revisions on the WSUS or SUP server
automatically. Also, set the option to decline expired updates on the server.

   1. In the WSUS administration console, click Options, and then click Automatic Approvals.

<!-- p.873 -->

   2. On the Advanced tab, make sure that both Automatically approve new revisions of
     approved updates and Automatically decline updates when a new revision causes them
     to expire are selected.
   3. Click OK.

More information
By default, the Automatically approve new revisions of approved updates and Automatically
decline updates when a new revision causes them to expire options are selected. If you
decide not to approve the update revisions automatically, the WSUS server will use the older
update revision. In this case, you must manually approve the update revision.

  ７ Note

  A revision is an update version that has changed. For example, the update version may
  have expired or the update version may have applicability rules that have updated.

The default settings for the Automatically approve new revisions of approved updates and
Automatically decline updates when a new revision causes them to expire options let you
maintain good performance on the WSUS network. If you don't want expired updates to be
automatically declined, you can manually decline them. However, make sure that you do this
periodically.

It's recommended that you run the server clean-up wizard regularly. For more information, see
General guidance on optimizing WSUS client performance.

Troubleshoot stuck client computers
To resolve an issue in which a client computer stops responding during an update scan, follow
these steps:

   1. On the affected client computer, set the startup type for the Automatic Updates service
     (Wuauserv) to Disabled.
   2. Restart the computer.
   3. Delete the %Windir%\SoftwareDistribution folder.
   4. Set the startup type for the Automatic Updates service to Automatic, and then start the
     Automatic Updates service.

<!-- p.874 -->

Last updated on 03/30/2026

<!-- p.875 -->

The Windows Server Update Services
console crashes when browsing for updates
This article helps you fix an issue where the Windows Server Update Services (WSUS) console
crashes because of the corrupted application cache.

Original product version: Windows Server Update Services
Original KB number: 2761925

Symptoms
The WSUS console crashes when browsing for updates and displays the following error
message:

  An unexpected error occurred.
  click reset server node to try to connect to the server again

  Event Type: Error
  Event Source: Windows Server Update Services
  Event Category: None
  Event ID: 7053
  Date:
  Time:
  User: N/A
  Computer:
  Description: The WSUS administration console has encountered an unexpected error. This
  may be a transient error; try restarting the administration console.

Cause
This can occur if the application cache is corrupted.

Resolution
To resolve this issue, delete the WSUS application cache from the location below:

<!-- p.876 -->

C:\Users\<user profile>\AppData\Roaming\Microsoft\MMC

where <user profile> is the currently logged in user profile.

 Last updated on 03/30/2026

<!-- p.877 -->

Maintain the Windows Server Update
Services (WSUS) database manually
or automatically
Routine maintenance of the WSUS database (SUSDB) is important to ensure the application's
health and optimal performance. This article describes concise steps and scripts to maintain
SUSDB manually or automatically.

For more information, see The complete guide to WSUS and Configuration Manager SUP
maintenance.

How long does the maintenance take?
The maintenance duration might vary depending on the machine's resources, including CPU,
memory, and disk capacity. Factors affecting the maintenance duration include the time since the
last maintenance, the number of selected products and classifications, and the volume of updates
that need to be cleaned up.

In a small environment, with minimal products and classifications and recent maintenance on
SUSDB, the automatic scripts with the RA option might take less than one minute to run.
However, in some cases, it might take several days to complete. If it takes longer than expected
and you can't complete the maintenance successfully, you need to create a new SUSDB.

Query to obtain the update count
An excessive number of superseded, declined, and obsolete updates often cause poor health of
SUSDB. To obtain the update count, run the following SQL query. If the counts in the last three
columns of the query result exceed a few hundred, maintenance should be performed.

 SQL

 use SUSDB;

 DECLARE @numberOfMatch INT
 DECLARE @tmpTable TABLE (
     name VARCHAR(25)
 )
 INSERT INTO @tmpTable
 EXEC spGetObsoleteUpdatesToCleanup

<!-- p.878 -->

 SELECT @numberOfMatch = @@ROWCOUNT
 select
 (Select count (*) from vwMinimalUpdate ) 'Total Updates',
 (Select count (*) from vwMinimalUpdate where declined=0) as 'Live Updates',
 (Select count (*) from vwMinimalUpdate where IsSuperseded =1) as 'Superseded',
 (Select count (*) from vwMinimalUpdate where IsSuperseded =1 and declined=0) as
 'Superseded but not declined',
 (Select count (*) from vwMinimalUpdate where declined=1) as 'Declined',
 (Select count (*) from vwMinimalUpdate where IsSuperseded =1 and declined=1)
 'Superseded & Declined',
 (select Count(*) From @tmpTable ) 'Obsolete Updates Needed to be cleaned'

Maintain the WSUS database (SUSDB) manually

  ） Important

       Run the steps on each WSUS server in the hierarchy. When performing a cleanup and
       removing items from WSUS servers, start at the lowest level of the hierarchy.
       Ensure that any scheduled synchronizations are disabled, either in Configuration
       Manager (if used) or on standalone WSUS servers.

The following steps can resolve many issues with scanning and synchronization. If there are a
large number of declined updates, you might need to repeat steps 9 through 12 multiple times.
After each run, execute the SQL query to confirm that the update count is decreasing. Steps 8
and 9 might result in errors each time, which is expected. Therefore, you need to repeat steps 9
through 12 multiple times. Some steps (especially step 9) might take several hours to complete.

   1. Run the SQL script described in Slow performance of the spDeleteUpdate procedure.

   2. Shrink the SUSDB files.

   3. Shrink the SUSDB database.

   4. Reindex and update statistics on SUSDB.

      a. To reindex SUSDB, run the following SQL script:

          SQL

          EXEC sp_MSforeachtable @command1="SET QUOTED_IDENTIFIER ON;ALTER INDEX ALL ON
          ? REBUILD;"

     b. To update statistics, run the following SQL script:

<!-- p.879 -->

       SQL

       Exec sp_msforeachtable "UPDATE STATISTICS ? WITH FULLSCAN, COLUMNS"

5. Perform a cleanup of the synchronization history.

    ７ Note

    If there are a large number of synchronizations, the WSUS console may crash.

    SQL

    USE SUSDB
    GO
    DELETE FROM tbEventInstance WHERE EventNamespaceID = '2' AND EVENTID IN ('381',
    '382', '384', '386', '387', '389')

6. Perform a cleanup of superseded updates older than 30 days or according to your specific
  configuration.

    ７ Note

          The value of 30 in the first line indicates the number of days between today and
          the release date, during which superseded updates shouldn't be marked as
          declined.
          In Configuration Manager, this value should align with the supersedence rules
          configured in the software update point (SUP) component properties.
          On standalone WSUS servers, specify the number of days you want to retain
          superseded updates. For instance, set the value to 60 instead of 30 to keep two
          months of superseded updates. Any updates older than this period will be
          marked as declined and subsequently cleaned up.

    SQL

    DECLARE @thresholdDays INT = 30   -- Specify the number of days between today and
    the release date during which superseded updates should not be marked as
    declined. If Configuration Manager is being used with WSUS, this value should
    match the configuration of supersedence rules in the software update point (SUP)
    component properties.
    DECLARE @testRun BIT = 0          -- Set this value to 1 to test without
    declining anything.
    -- There shouldn't be any need to modify anything after this line.

<!-- p.880 -->

    DECLARE @uid UNIQUEIDENTIFIER
    DECLARE @title NVARCHAR(500)
    DECLARE @date DATETIME
    DECLARE @userName NVARCHAR(100) = SYSTEM_USER
    DECLARE @count INT = 0
    DECLARE DU CURSOR FOR
            SELECT MU.UpdateID, U.DefaultTitle, U.CreationDate FROM vwMinimalUpdate MU
            JOIN PUBLIC_VIEWS.vUpdate U ON MU.UpdateID = U.UpdateId
            WHERE MU.IsSuperseded = 1 AND MU.Declined = 0 AND MU.IsLatestRevision = 1
            AND MU.CreationDate < DATEADD(dd,-@thresholdDays,GETDATE())
            ORDER BY MU.CreationDate
    PRINT 'Declining superseded updates older than ' + CONVERT(NVARCHAR(5),
    @thresholdDays) + ' days.' + CHAR(10)
    OPEN DU
    FETCH NEXT FROM DU INTO @uid, @title, @date
    WHILE (@@FETCH_STATUS > - 1)
    BEGIN
            SET @count = @count + 1
            PRINT 'Declining update ' + CONVERT(NVARCHAR(50), @uid) + ' (Creation Date
    ' + CONVERT(NVARCHAR(50), @date) + ') - ' + @title + ' ...'
            IF @testRun = 0
                   EXEC spDeclineUpdate @updateID = @uid, @adminName = @userName,
    @failIfReplica = 1
            FETCH NEXT FROM DU INTO @uid, @title, @date
    END
    CLOSE DU
    DEALLOCATE DU
    PRINT CHAR(10) + 'Attempted to decline ' + CONVERT(NVARCHAR(10), @count) + '
    updates.'

7. Perform a cleanup of obsolete updates.

    SQL

    DECLARE @var1 INT
    DECLARE @msg nvarchar(100)
    CREATE TABLE #results (Col1 INT)
            INSERT INTO #results(Col1) EXEC spGetObsoleteUpdatesToCleanup
    DECLARE WC Cursor
            FOR
            SELECT Col1 FROM #results
    OPEN WC
            FETCH NEXT FROM WC
            INTO @var1
            WHILE (@@FETCH_STATUS > -1)
            BEGIN SET @msg = 'Deleting' + CONVERT(varchar(10), @var1)
            RAISERROR(@msg,0,1) WITH NOWAIT EXEC spDeleteUpdate @localUpdateID=@var1
            FETCH NEXT FROM WC INTO @var1 END
    CLOSE WC
            DEALLOCATE WC

            DROP TABLE #results
