---
title: "Welcome — pages 401-440"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0401-0440
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0401-0440
family: sccm
documentKind: "doc"
abstract: "Task Detailed steps Tip: Capture network settings will ensure that our custom network settings are reapplied during deployment. Don't install updates or software, and then complete the wizard. Create a new device 1. Select the Assets and Compliance workspace. In the navigation p"
---

# Welcome — pages 401-440

<!-- p.401 -->

Task                  Detailed steps

                           Tip: Capture network settings will ensure that our custom network
                      settings are reapplied during deployment.

                      Don't install updates or software, and then complete the wizard.

Create a new device   1. Select the Assets and Compliance workspace. In the navigation pane,
collection            select Device Collections. Select Create Device Collection from the bar at
                      the top.

                      2. Name the collection as Windows 7 Enterprise x64.

<!-- p.402 -->

Task   Detailed steps

       3. Add our target computer (in this case GTRCM12XP1) as a direct member.

<!-- p.403 -->

Task                       Detailed steps

Distribute the task        1. Right-click your new collection, and then select Deploy > Task Sequence
sequence to this           from the shortcut menu. Click through the wizard, and then finish.
collection

Run the task sequence on   1. Log on to GTRCM12XP1, and then run the new task sequence to install
GTRCM12XP1 to install      your new operating system.
the operating system
image.

<!-- p.404 -->

 Task                        Detailed steps

OSD task sequences known issues
        You cannot stage a Windows PE 3.1 boot image to a Windows XP-based computer in
        Configuration Manager
        Task sequence fails in Configuration Manager if software updates require multiple restarts
        FIX: Task sequence to install an operating system doesn't run when you use custom port
        settings in System Center Configuration Manager 2012 SP1
        An update is available for the "Operating System Deployment" feature of Configuration
        Manager

The above and a number of other issues with task sequences are addressed in Description of
Cumulative Update 1 for System Center 2012 R2 Configuration Manager .

Last updated on 03/30/2026

<!-- p.405 -->

Error when managing boot images in
Configuration Manager
This article fixes an issue in which you can't manager boot images in Configuration Manager if
the WIMMount service is corrupted, misconfigured, or missing.

Original product version: Configuration Manager (current branch), Microsoft System Center
2012 R2 Configuration Manager, Microsoft System Center 2012 Configuration Manager
Original KB number: 4096324

Symptoms
In an environment that has Windows Assessment and Deployment Kit (ADK) installed and up-
to-date on the server that hosts the SMS Provider, you can't manage boot images by using
Configuration Manager. This includes the following actions:

     Update boot images on distribution points.
     Import new boot images.
     Create new boot images by using the Microsoft Deployment Toolkit (MDT) wizard.
     Modify boot images, such as to add drivers.

In this scenario, the following error is logged in the SMSProv.log file on the SMS Provider
server:

  SMS Provider ExecMethodAsync : SMS_BootImagePackage.PackageID="
  <Boot_Image_Package_ID>"::RefreshPkgSource~
  SMS Provider Requested class =SMS_BootImagePackage~
  SMS Provider Requested num keys =1~
  SMS Provider IExtClassManager::ValidateAuthenticationLevel...
  SMS Provider CExtProviderClassObject::DoExecuteMethod RefreshPkgSource~
  SMS Provider Loaded wimgapi.dll version 10.0.16299.15 from location 'C:\Program Files
  (x86)\Windows Kits\10\Assessment and Deployment Kit\Deployment
  Tools\amd64\DISM\wimgapi.dll'
  SMS Provider WIM index is 1.
  SMS Provider Image language ID 1033 and en-US~
  SMS Provider Loaded the image from \\<Boot_Image_Path>\boot.wim
  SMS Provider Temporary path for WIM file is C:\Windows\TEMP\BootImages\

<!-- p.406 -->

  {<Random_GUID>}\temp.
  SMS Provider Loaded the image index 1.
  SMS Provider ERROR> failed to mount wim file, err=-1052638943~
  SMS Provider ~*~*~..\sspbootimagepackage.cpp(5198) : Failed to inject OSD binaries into
  mounted WIM file (often happens if unsigned drivers are inserted into x64 boot
  image)~*~*~
  SMS Provider ~*~*~Failed to inject OSD binaries into mounted WIM file (often happens if
  unsigned drivers are inserted into x64 boot image) ~*~*~

When you manually run DISM.exe on the SMS Provider server, the following error is logged in
the DISM.log file:

  DISM DISM.EXE: Successfully registered commands for the provider: Compatibility
  Manager.
  [10780] [0x8007007b] OpenFilterPort:(408): The filename, directory name, or volume label
  syntax is incorrect.
  [10780] [0x8007007b] FltCommVerifyFilterPresent:(502): The filename, directory name, or
  volume label syntax is incorrect.
  [10780] [0x8007007b] WIMMountImageHandle:(1089): The filename, directory name, or
  volume label syntax is incorrect.
  [10780] [0x80070002] StateStoreRemoveMountedImage:(1030): The system cannot find the
  file specified.
  [10780] [0x80070002] WIMMountImageHandle:(1331): The system cannot find the file
  specified.

  DISM DISM WIM Provider: PID=10780 TID=1096 "Failed to mount the image." -
  CWimImageInfo::Mount(hr:0x8007007b)
  DISM DISM WIM Provider: PID=10780 TID=1096
  onecore\base\ntsetup\opktools\dism\providers\wimprovider\dll\wimmanager.cpp:2684 -
  CWimManager::InternalOpMount(hr:0x8007007b)
  DISM DISM WIM Provider: PID=10780 TID=1096
  onecore\base\ntsetup\opktools\dism\providers\wimprovider\dll\wimmanager.cpp:4028 -
  CWimManager::InternalCmdMount(hr:0x8007007b)
  DISM DISM WIM Provider: PID=10780 TID=1096 "Error executing command" -
  CWimManager::InternalExecuteCmd(hr:0x8007007b)
  DISM DISM WIM Provider: PID=10780 TID=1096
  onecore\base\ntsetup\opktools\dism\providers\wimprovider\dll\wimmanager.cpp:2201 -
  CWimManager::ExecuteCmdLine(hr:0x8007007b)

<!-- p.407 -->

  ７ Note

  Using Process Monitor when you manually run DISM can't identify which file or directory
  can't be found.

Cause
This issue occurs if the WIMMount service is corrupted, misconfigured, or missing on the SMS
Provider server.

To verify, check the following registry entry on the server that hosts the SMS Provider:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WIMMount\ImagePath

The value of this entry should be the location of the Wimmount.sys file, which is under the
installation directory of Windows ADK.

  ７ Note

  The server that hosts the SMS provider may not be the central administration site or
  primary site server. If there are multiple servers that host the SMS Provider, make sure that
  you check this registry entry on all SMS Provider servers.

To find the servers that host the SMS Provider at a site, follow these steps:

   1. In the Configuration Manager console, go to Administration > Overview > Site
     Configuration > Sites.
   2. Right-click the site, and then select Properties.
   3. On the General tab, find the servers that are listed under SMS Provider location.

Resolution
To fix the issue, follow these steps to reinstall the WIMMount service:

   1. On the server that hosts the SMS Provider, go to the location where Windows ADK is
     installed. For example, the default path of Windows ADK 10 is C:\Program Files
     (x86)\Windows Kits\10\Assessment and Deployment Kit\Deployment Tools\amd64 .

   2. Go to the DISM folder, and then run the following command:

<!-- p.408 -->

       Console

       WimMountAdkSetupAmd64.exe /Install

Last updated on 03/30/2026

<!-- p.409 -->

Errors when capturing Windows 11 image
by using capture media in Configuration
Manager
This article provides solutions for some errors that occur when you capture a Windows 11
image by using capture media in Configuration Manager.

Applies to: Configuration Manager (current branch)

Symptoms
When you try to capture a Windows 11 image by using capture media in Configuration
Manager, you may experience one or more of the following errors:

     VCRUNTIME140_1.dll was not found
     Package <package name> was installed for a user, but not provisioned for all users
     An update or servicing operation may be using reserved storage
     Volume '\\?\Volume{GUID}' not found

See the following sections for error details, causes and solutions.

VCRUNTIME140_1.dll was not found
When you start the capture process by using TSMBAutoRun.exe, you receive the following error
message:

  OsdCaptureCD.exe – System Error
  The code execution cannot proceed because VCRUNTIME140_1.dll was not found.
  Reinstalling the program may fix this problem.

Default Visual C++ Runtime components are installed as a prerequisite during the
Configuration Manager Client Agent installation. If your reference installation is disconnected
from your Configuration Manager environment, these Visual C++ Runtime components will be
missing.

Solution: Install vcredist_x64.exe

<!-- p.410 -->

To resolve this issue, install vcredist_x64.exe, and make sure that the installed version matches
the version that's available in the \\<SCCM-Server>\<SMS_SiteCode>\Client\x64 share folder.

After vcredist_x64.exe is installed, restart the capture process.

Package <package name> was installed for a user, but
not provisioned for all users
Check the setupact.log file in the C:\Windows\System32\Sysprep\Panther folder. If some
applications are blocking the capture process, the "Package <Package name> was installed for
a user, but not provisioned for all users" error will be displayed in the setupact.log file like the
following output:

 Output

 02-07-2022 15:18:02.000 SYSPRP Entering SysprepGeneralizeValidate (Appx) -
 validating whether all apps are also provisioned.
 02-07-2022 15:18:03.000 SYSPRP Package
 Microsoft.OneDriveSync_21220.1024.5.0_neutral__8wekyb3d8bbwe was installed for a
 user, but not provisioned for all users. This package will not function properly in
 the sysprep image.
 02-07-2022 15:18:03.000 SYSPRP Failed to remove apps for the current user:
 0x80073cf2.
 02-07-2022 15:18:03.000 SYSPRP Exit code of RemoveAllApps thread was 0x3cf2.
 02-07-2022 15:18:03.000 SYSPRP ActionPlatform::LaunchModule: Failure occurred while
 executing 'SysprepGeneralizeValidate' from C:\Windows\System32\AppxSysprep.dll;
 dwRet = 0x3cf2
 02-07-2022 15:18:03.000 SYSPRP SysprepSession::Validate: Error in validating
 actions from C:\Windows\System32\Sysprep\ActionFiles\Generalize.xml; dwRet = 0x3cf2
 02-07-2022 15:18:03.000 SYSPRP RunPlatformActions:Failed while validating Sysprep
 session actions; dwRet = 0x3cf2
 02-07-2022 15:18:03.000 SYSPRP 983152 (0xf0070) RunDlls:An error occurred while
 running registry sysprep DLLs, halting sysprep execution. dwRet = 0x3cf2
 02-07-2022 15:18:03.000 SYSPRP 983256 (0xf00d8) WinMain:Hit failure while pre-
 validate sysprep generalize internal providers; hr = 0x80073cf2

Solution: Remove package for current user
To resolve this issue, remove the package by running the Remove-AppxPackage -Package
<package name> cmdlet as follows:

 PowerShell

 Remove-AppxPackage -Package
 Microsoft.OneDriveSync_21220.1024.5.0_neutral__8wekyb3d8bbwe

<!-- p.411 -->

After the package is removed, restart the capture process and monitor other packages in the
same situation.

An update or servicing operation may be using
reserved storage
Check the setupact.log file in the C:\Windows\System32\Sysprep\Panther folder. If some updates
are being installed on the computer, the "An update or servicing operation may be using
reserved storage" error is displayed in the setupact.log file like the following output:

 Output

 02-07-2022 14:24:15.000 SYSPRP Sysprep_Clean_Validate_Opk: Audit mode cannot be
 turned on if reserved storage is in use. An update or servicing operation may be
 using reserved storage.; hr = 0x800F0975
 02-07-2022 14:24:15.000 SYSPRP ActionPlatform::LaunchModule: Failure occurred while
 executing 'Sysprep_Clean_Validate_Opk' from C:\Windows\System32\spopk.dll; dwRet =
 0x975
 02-07-2022 14:24:15.000 SYSPRP SysprepSession::Validate: Error in validating
 actions from C:\Windows\System32\Sysprep\ActionFiles\Cleanup.xml; dwRet = 0x975
 02-07-2022 14:24:15.000 SYSPRP RunPlatformActions:Failed while validating Sysprep
 session actions; dwRet = 0x975
 02-07-2022 14:24:15.000 SYSPRP 983152 (0xf0070) RunDlls:An error occurred while
 running registry sysprep DLLs, halting sysprep execution. dwRet = 0x975
 02-07-2022 14:24:15.000 SYSPRP 983256 (0xf00d8) WinMain:Hit failure while pre-
 validate sysprep cleanup internal providers; hr = 0x80070975

Solution: Ensure computer is up to date
To resolve this issue, install updates on the computer until no updates are available.

After the computer is up to date and restarted, restart the capture process.

Volume '\\?\Volume{GUID}' not found
When you boot the computer into Windows PE (WinPE) and capture the Windows image
(.WIM) file, the "Volume '\\?\Volume{GUID}' not found" error is displayed in the SMSTS.log file
like the following output:

 Output

 02-07-2022 09:41:51.246 TSBootShell 1136 (0x470) RAM Disk Boot Path:
 MULTI(0)DISK(0)RDISK(0)PARTITION(3)\_SMSTASKSEQUENCE\WINPE\SOURCES\BOOT.WIM
 02-07-2022 09:41:51.246 TSBootShell 1136 (0x470) Volume '\\?\Volume{GUID}\' not
 found

<!-- p.412 -->

 02-07-2022 09:41:51.246 TSBootShell 1136 (0x470)
 GetVolumePathForVolumeName(szDeviceVolumeId, rsWin32Path), HRESULT=80070490
 (X:\bt\1204713\repo\src\Framework\TSCore\devicepath.cpp,167)
 02-07-2022 09:41:51.246 TSBootShell 1136 (0x470)
 DevicePath::DeviceNamespaceWin32Path(sDevicePath, rsWin32Path), HRESULT=80070490
 (X:\bt\1204713\repo\src\Framework\TSCore\devicepath.cpp,120)
 02-07-2022 09:41:51.246 TSBootShell 1136 (0x470)
 DevicePath::ArcToWin32Path(pszBootPath, rsLogicalPath), HRESULT=80070490
 (X:\bt\1204713\repo\src\Framework\TSCore\bootsystem.cpp,117)
 02-07-2022 09:41:51.246 TSBootShell 1136 (0x470) ConvertBootToLogicalPath failed to
 convert
 'MULTI(0)DISK(0)RDISK(0)PARTITION(3)\_SMSTASKSEQUENCE\WINPE\SOURCES\BOOT.WIM'
 (0x80070490). Retrying (0)...

This issue occurs because no drive letter is assigned to the operating system (OS) partition that
needs to be captured. This is because the No Default Drive Letter attribute is set to Yes for the
Windows 11 C drive. See the following screenshot for an example:

Solution: Allow automatic assignment of drive letters
To resolve this issue, restart the computer into Windows 11 original OS, and change the
partition attributes to reenable the automatic assignment by running the following commands:

 Windows Command Prompt

 diskpart
 Select Disk 0
 Select Partition 3

<!-- p.413 -->

 GPT attributes=0x0000000000000000
 Exit

To confirm that the automatic assignment is enabled and the drive letter is assigned to the
partition, use the detail partition command as follows:

 Windows Command Prompt

 diskpart
 Select Disk 0
 Select Partition 3
 detail partition

See the following screenshot for the correct partition attributes:

Partition 3 that's used in the command lines above is just an example. The selected partition

should match the partition index of your current installed OS. To determine the partition, run
the following commands:

 Windows Command Prompt

 diskpart
 Select Disk 0
 list partition

See the following screenshot for the command output. Use the partition that's marked as
Primary.

<!-- p.414 -->

After the assignment is completed, restart the capture process.

Last updated on 03/30/2026

<!-- p.415 -->

A PXE enabled distribution point that uses
a self-signed certificate generates many
files
This article provides a solution for the issue that a PXE enabled distribution point (DP)
generates many files if it uses a self-signed certificate in System Center 2012 Configuration
Manager.

Original product version: System Center 2012 Configuration Manager
Original KB number: 2713467

Symptoms
A PXE enabled DP will generate a number of files under
C:\ProgramData\Microsoft\Crypto\RSA\S-1-5-18 for each PXE request that it services on the

network. This issue occurs whether the device sending the PXE request has a task sequence
deployed to it or not. The generation of files will continue and may consume available hard
disk space.

Cause
This issue occurs whenever a self-signed certificate is used for the DP.

Resolution
To work around this problem, request a CA issued certificate for the PXE enabled DP and
specify the PFX file under the properties of the DP. Step-by-step instructions on how to do
create the PFX file are available in Deploying the Client Certificate for Distribution Points.

 Last updated on 03/30/2026

<!-- p.416 -->

Advanced troubleshooting for PXE boot
issues in Configuration Manager
This article provides advance troubleshooting techniques to help administrators diagnose and
resolve PXE boot failures in Configuration Manager.

Original product version: Configuration Manager (current branch)
Original KB number: 4491871

Introduction
For essential information about how PXE works, see the companion article Understand PXE
boot in ConfigMgr.

The solutions that are provided in Troubleshooting PXE boot issues in Configuration Manager
section can resolve most issues that affect PXE boot.

If you can't resolve your PXE boot issue by using IP Helpers or reinstalling PXE, try the following
troubleshooting steps.

Special consideration when co-hosting DHCP and
WDS on the same server
When Dynamic Host Configuration Protocol (DHCP) and WDS are co-hosted on the same
computer, WDS requires a special configuration to listen on a specific port. This configuration
is outlined in Windows Deployment Service and Dynamic Host Configuration Protocol (DHCP).
According to this article, you must complete the following actions if WDS and DHCP are co-
hosted on the same server:

   1. Set the UseDHCPPorts value to 0 in the following registry location:

      HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WDSServer\Providers\WDSPXE

   2. Run the following WDS command:

       Console

       WDSUTIL /Set-Server /UseDHCPPorts:No /DHCPOption60:Yes

<!-- p.417 -->

This recommendation requires that you configure WDS to run the WDSUTIL command. This
recommendation conflicts with the best practice not to configure WDS when you install a
ConfigMgr PXE-enabled DP. However, you can configure the two settings that are specified in
the WDSUTIL command ( UseDHCPPorts and DHCPOption60 ) by using alternative methods that
don't require the WDSUTIL command. This way you don't have to configure WDS.

To configure these settings without having WDS enabled, follow these guidelines:

     The UseDHCPPorts switch for WDSUTIL is actually the equivalent of setting the
     UseDHCPPorts registry key to a value of 0 in the following location:

     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WDSServer\Providers\WDSPXE

     Using the UseDHCPPorts switch isn't necessary if the registry key is manually set. If WDS
     wasn't installed, this registry key may not exist.

     The DHCPOption60 switch configures an option for the DHCP service, not for the WDS
     service. Instead of using WDSUTIL to set this DHCP option, you can use an equivalent
     DHCP command to set the same option. To do it, use the netsh command, as described
     in Configuring DHCP for Remote Boot Services.

     To configure the WDS options according to these guidelines, close any DHCP consoles
     that are open, and then run the following commands at an elevated command prompt:

       Console

       netsh dhcp server \\<DHCP_server_machine_name> add optiondef 60 PXEClient
       String 0 comment=PXE support

       Console

       netsh dhcp server \\<DHCP_server_machine_name> set optionvalue 60 STRING
       PXEClient

     These commands set up and enable DHCP Option 60 on a DHCP server. After you run
     these commands, if an option that is named Unknown is displayed instead of 060 PXE
     Client in the DHCP console, restart the server so that these settings can take effect. After

     the restart, the option should be displayed correctly. This issue usually occurs only if a
     DHCP console was left open when the two commands were run.

If DHCP is ever moved to another server and removed from the server that's hosting WDS,
these steps should be reversed. Follow these steps on the WDS server:

<!-- p.418 -->

   1. Run the following command at an elevated command prompt:

       Console

       REG ADD HKLM\SYSTEM\CurrentControlSet\services\WDSServer\Providers\WDSPXE /v
       UseDHCPPorts /t REG_DWORD /d 1 /f

   2. Run the following commands at an elevated command prompt:

       Console

       netsh dhcp server \\<DHCP_server_machine_name> delete optionvalue 60

       Console

       netsh dhcp server \\<DHCP_server_machine_name> delete optiondef 60 PXEClient

        ７ Note

        The first of these commands disables DHCP option 60. The second command
        removes DHCP option 60 completely.

Troubleshooting DHCP Discovery
Before you start to troubleshoot the initial DHCP discovery stage of the PXE booting process,
consider the following points:

     In SMSPXE.log, you should see the MAC address or the DHCPREQUEST of the device that
     you're trying to start. If you don't see that, a router configuration issue might exist
     between the client and the DP.
     Don't use DHCP options 60, 66, or 67. It isn't supported.
     Test whether the device can start when it's plugged into a switch on the same subnet as
     the PXE-enabled DP. If it can, the issue likely involves the router configuration.
     Make sure that the DHCP (67 and 68), TFTP (69), and BINL (4011) ports are open between
     the client computer, the DHCP server, and the PXE DP.

At this stage, there are no logs to refer to. A PXE error code is usually displayed if the PXE boot
process fails before WinPE starts. Here are examples of the error messages that you might see:

     PXE-E51: No DHCP or proxyDHCP offers were received.

<!-- p.419 -->

      PXE-E52: proxyDHCP offers were received. No DHCP offers were received.
      PXE-E53: No boot filename received.
      PXE-E55: proxyDHCP service did not reply to request on port 4011.
      PXE-E77 bad or missing discovery server list.
      PXE-E78: Could not locate boot server.

Although it helps narrow the focus of troubleshooting, you might still have to capture a
network trace of the issue by using a network monitoring tool, such as Netmon or
WireShark       . The network monitoring tool must be installed on both the PXE-enabled DP and
a computer that's connected to a mirrored port on the switch. For more information about how
to configure mirrored ports, refer to the manual provided by the manufacturer of the specific
switch or routing device.

The typical procedure is to start the network traces on both the DP and the computer that's
connected to the mirrored port. Try to start the device through PXE. Then, stop the trace, and
save it for further analysis.

Here is a sample trace of a DHCP conversation that was captured from the PXE-enabled DP:

You can see that the initial DHCPDISCOVER by the PXE client is followed by a DHCPOFFER
from the DHCP server and the PXE DP. The request from the client (0.0.0.0) is made and then
acknowledged by the DHCP server (10.238.0.14). After the PXE client has an IP address
(10.238.0.3), it sends a request to the PXE DP (10.238.0.2). That DP then acknowledges the
request by returning the network boot program details.

Capture a simultaneous network trace on the client and the DP to determine whether the
conversation is occurring as expected. Follow these guidelines:

      Make sure that the DHCP services are running and available.
      Verify that the WDS service is running on the DP.
      Make sure that no firewalls are blocking the DHCP ports between the server and the
      client.
      Verify that the client computer can start when it is on the same subnet as the DP.
      Make sure that IP Helpers are configured correctly if the client computer is starting from a
      different subnet than the one that the DP is in.

<!-- p.420 -->

Troubleshooting TFTP Transfer
If the error on PXE boot refers to TFTP, you may be unable to transfer the boot files. The
following are examples of the error messages that you may receive:

     PXE-E32: TFTP open timeout
     PXE-E35: TFTP read timeout
     PXE-E36: Error received from TFTP server
     PXE-E3F: TFTP packet size is invalid
     PXE-E3B: TFTP Error - File not Found
     PXE-T04: Access Violation

A good way to troubleshoot these errors is to monitor the network by using Netmon or
Wireshark. Below is an example of the data captured from a PXE client when a TFTP Open time-
out occurs.

Here the client is sending read requests for the Wdsnbp.com file, but it isn't receiving a
response. It indicates that something is preventing the acknowledgment from being received
by the client. Here's what the data should look like.

<!-- p.421 -->

In this situation, you can try the following troubleshooting methods:

     Reduce the block size on the PXE-enabled DP, see KB 975710 .

     Verify that the WDS service is started on the DP.

     Make sure that the TFTP port is open between the client computer and the DP.

     Verify that the permissions on the REMINST share and folder are correct.

     Check the WDS logs for other TFTP errors.

     Verify that the RemoteInstall\SMSBoot\x86 and RemoteInstall\SMSBoot\x64 folders contain
     the following files:

     Make sure that the fonts exist in SMSBoot\Fonts folder:

<!-- p.422 -->

     Make sure that the Boot.sdi file exists in the RemoteInstall\SMSBoot folder:

Windows PE startup issues - drivers
The most common issues that occur during this phase are driver-related. Overall, the latest
version of Windows PE (WinPE) contains most network and mass storage drivers. Sometimes a
required driver isn't included. So it must be imported into the boot WIM. The following
guidelines apply to this process:

     Import only the drivers that you need for the boot image.
     Consider adding only NIC or mass storage drivers. Other drivers aren't required.

The SMSTS.log file (located in <SystemDrive>:\Windows\temp\SMSTS) is the most useful
resource to troubleshoot these issues. (Remember to enable the command prompt during
startup so that you can examine this file.) If you don't see a log entry that has a valid IP address
and resembles the following entry, you're probably experiencing a driver issue:

 Output

 SMSTS.log
 Found network adapter "Intel 21140-Based PCI Fast Ethernet Adapter (Emulated)" with
 IP Address <IP address>

To verify this situation, press F8, and then run IPCONFIG at the command prompt to determine
whether the NIC is recognized and has a valid IP address.

WIM Files
Also make sure that both x86 and x64 boot images exist on the DP. You can see the WIMs in
the following directory, they'll also be in the content library:

<!-- p.423 -->

C:\RemoteInstall\SMSImages\<PackageID>

Make sure that Deploy this boot image from the PXE-enabled distribution point is set in the
properties of the boot images.

Configuration Manager Policy issues
Another common issue that affects PXE boot involves Task Sequence deployments. In the
following example, the Task Sequence is deployed to an unknown computer, but it's already in
the database. The first symptom is that the PXE boot is aborted.

Upon further investigation, you notice the following entry in the SMSPXE log:

 Output

 SMSPXE.log
 Client lookup reply: <ClientIDReply><Identification Unknown="0" ItemKey="16777299"
 ServerName=""><Machine><ClientID/><NetbiosName/></Machine></Identification>
 </ClientIDReply>
 MP_LookupDevice succeeded: 16777299 1 16777299 1 0
 00:15:5D:00:19:CA, 32E5B71A-B626-4A4B-902E-7F94AD38B5B3: device is in the database.
 Client boot action reply: <ClientIDReply><Identification Unknown="0"
 ItemKey="16777299" ServerName=""><Machine><ClientID/><NetbiosName/></Machine>
 </Identification><PXEBootAction LastPXEAdvertisementID=""
 LastPXEAdvertisementTime="" OfferID="" OfferIDTime="" PkgID="" PackageVersion=""
 packagePath="" BootImageID="" Mandatory=""/></ClientIDReply>
 Client Identity:
 00:15:5D:00:19:CA, 32E5B71A-B626-4A4B-902E-7F94AD38B5B3: SMSID= OfferID=,

<!-- p.424 -->

  PackageID=, PackageVersion=, BootImageID=, PackagePath=, Mandatory=0
  00:15:5D:00:19:CA, 32E5B71A-B626-4A4B-902E-7F94AD38B5B3: no advertisements found
  00:15:5D:00:19:CA, 32E5B71A-B626-4A4B-902E-7F94AD38B5B3: No boot action. Aborted.
  00:15:5D:00:19:CA, 32E5B71A-B626-4A4B-902E-7F94AD38B5B3: Not serviced.

You can see in this entry that when the NBS stored procedures ran, they found no available
policy. So the boot action was aborted. The reverse can also be true. That is, when a computer
is unknown but the Task Sequence is deployed to a collection of known computers.

You can try the following troubleshooting steps:

      Verify that the computer that you try to restart exists in a collection that's targeted for a
      Task Sequence deployment.
      Make sure that you've checked the Enable unknown computer support PXE setting on
      the DP.
      If you are deploying the Task Sequence to unknown computers, verify that the computers
      don't already exist in the database.

Need more help
For more help to resolve this issue, see our TechNet support forum        or contact Microsoft
Support     .

Third-party information disclaimer

The third-party products that this article discusses are manufactured by companies that are
independent of Microsoft. Microsoft makes no warranty, implied or otherwise, about the
performance or reliability of these products.

Third-party contact disclaimer

Microsoft provides third-party contact information to help you find additional information
about this topic. This contact information may change without notice. Microsoft does not
guarantee the accuracy of third-party contact information.

 Last updated on 03/30/2026

<!-- p.425 -->

How to boot from a PXE server that's on a
different network
This article describes how to boot from a PXE server on a different network.

Original product version: Configuration Manager
Original KB number: 4471003

PXE boot process
Generally, a client computer boots from the network by using the PXE protocol according to
the following process. It involves three parties, the DHCP server, the PXE server, and the client:

   1. The client computer broadcasts a DHCP packet that asks for the address of the DHCP and
     PXE servers.
   2. The DHCP server responds, sending a broadcast packet that tells the client it's an address
     server.
   3. The PXE server responds to the client and reports that it's a boot server.
   4. The client sends a request to the DHCP server to ask for the IP address.
   5. The DHCP server sends the IP address to the client.
   6. The client sends a request to the PXE server to ask for the path to the Network Boot
     Program (NBP).
   7. The PXE server responds, sending the NBP path.
   8. The client downloads and runs the NBP.

After this process, the basic PXE boot is completed, but there will be more interaction between
the client and the PXE server. It's controlled by the NBP implementation. For example, the
Windows Deployment Services (WDS) NBP implementation will require the path of a custom
boot file ( pxeboot.com or bootmgfw.efi ). The implementation will download and run the
custom boot file. Then, the Windows Imaging Format (WIM) file and other files that Windows
PE needs will be downloaded.

The eight steps mentioned earlier usually work if the client and the servers are on the same
network. When the client and servers are on different networks, the recommended method to
make sure the client can boot from the network without using DHCP options is to configure
the routers.

<!-- p.426 -->

Recommended method - IP helper
The routers must be able to route the client requests from the network of the client to the
network of the DHCP server. One such simple router rule is the IP helper. The helper just tells
the router to forward the DHCP requests to the known IP address of the DHP server.

For PXE requests, you just need to configure the routers to forward the client request to the
PXE server, just like you do with the DHCP server. Locate your router, find the DHCP IP helper
entry, and add another entry that looks exactly like the first one but uses the IP address of the
PXE server. For more information, see the blog post You want to PXE Boot? Don't use DHCP
options .

Besides, you can add an IP helper entry for each PXE server. In a load-balancing scenario
(multiple PXE servers), PXE servers can be up or down in a group, and you don't have to do any
extra configuration. In diverse environments (Windows, Linux, and Router PXE servers all
coexisting), the different PXE servers can selectively respond to the clients that they recognize.

Problematic scenarios
To configure the DHCP server to respond to PXE requests, you might try to add PXE options to
the DHCP replies. It results in the client always downloading the network boot file (as specified
in the DHCP reply) and running it.

It's problematic in some UEFI setting scenarios. The client may not try to boot from the hard
drive after the client was configured to start from a network boot. But the network boot failed,
for example, there's no task sequence deployment for the client. It's also problematic for
mixed-OS environments. Your Linux computer would be instructed by the DHCP server to
download and run the Windows network boot program.

So, letting the DHCP server masquerade as a PXE server doesn't work as expected in some
scenarios. The true PXE server decides whether it will respond and serve a network boot file. In
the Configuration Manager case, the server will only respond if there's a task sequence
deployed to the client.

 Last updated on 03/30/2026

<!-- p.427 -->

Certificate isn't updated on a PXE-enabled
distribution point and multiple error
entries are logged
This article provides a solution for the Failed to get the encrypted PXE password error
message in Distmgr.log after you update the certificate of a distribution point (DP) that's used
for PXE boot.

Original product version: Configuration Manager (current branch)
Original KB number: 4511618

Symptoms
After you update the certificate of a DP that's used for PXE boot, the updated certificate
doesn't seem to be used. When you restart Windows Deployment Services (WDS) on the PXE-
enabled DP, the following error entries are logged in the SMSPXE.log file:

  Begin validation of Certificate [Thumbprint <Old_Cert_Thumbprint>] issued to '<DP
  Server>'
  Certificate [<Old_Cert_Thumbprint>] issued to '<DP_Server>' has expired.
  Completed validation of Certificate [<Old_Cert_Thumbprint>] issued to '<DP Server>'
  reply has no message header marker
  Failed to send status message (80004005)
  Unsuccessful in sending status message. 80004005.
  PXE::MP_ReportStatus failed; 0x80070490
  Certificate not valid.
  A required certificate is not within its validity period when verifying against the current
  system clock or the timestamp in the signed file. (Error: 800B0101; Source: Windows)
  Failed to validate PXEClientKey certificate.
  PXE Provider failed to read configuration parameters.
  A required certificate is not within its validity period when verifying against the current
  system clock or the timestamp in the signed file. (Error: 800B0101; Source: Windows)

  ７ Note

<!-- p.428 -->

  The certificate thumbprint in SMSPXE.log belongs to the previous certificate that has
  expired. To check a certificate thumbprint, double-click the certificate, select the Details
  tab, and then check the value of the Thumbprint field.

Additionally, the following entry is not logged in the Distmgr.log file on the parent site server:

  DP registry settings have been successfully updated on <DP_Server>

  ７ Note

  This log entry would indicate that the new certificate is updated in the registry of the DP.

Instead, the following error entry is logged in Distmgr.log:

  Failed to get the encrypted PXE password

In this scenario, you observe the following conditions:

     The certificate is updated on the General tab in the DP Properties dialog box.

     The following entry is logged in the Hman.log file on the parent site server:

        DP cert query: EXEC spUpdateDPCert N'<DP_Server>', N'<data>', 0x,
        <Cert_Info_Blob>

        ７ Note

        This entry indicates that the spUpdateDPCert SQL Server stored procedure has run
        to update the certificate in the database.

     The certificate is updated in the database.

     In the Configuration Manager console, the new certificate is displayed under
     Administration > Overview > Security > Certificates.

Cause

<!-- p.429 -->

In most cases, this issue occurs if a PXE password is specified in the properties of the DP, and
the parent site is moved to another server or is recovered from a backup on a rebuilt server.

In this case, the machine keys have changed between the old instance of the site and the new
instance of the site. The machine keys from the original site are required to correctly decrypt
the PXE password. Because the machine keys from the original site are no longer available, the
PXE password can't be decrypted and set. If a PXE password is specified, the PXE password
must be reset before the new certificate can be set in the registry of the DP.

For more information, see Post-recovery tasks.

Resolution
To fix this issue, follow these steps:

   1. Temporarily disable the PXE password on the affected DP.

      In the DP Properties dialog box, select the PXE tab, and then clear the Require a
      password when computers use PXE check box.

   2. Verify that the certificate is updated. To do this, check whether the following entry is
      logged in Distmgr.log

        DP registry settings have been successfully updated on <DP_Server>

   3. Restart WDS on the DP, verify that the certificate thumbprint in SMSPXE.log belongs to
      the updated certificate, and that no error entry is logged in SMSPXE.log.

   4. Re-enable the PXE password on the DP.

      In the DP Properties dialog box, select the PXE tab, select the Require a password when
      computers use PXE check box, and then enter the password.

After you follow these steps, the new machine keys on the site server will be used to encrypt
the PXE password, and you won't see the following error entry in Distmgr.log:

  Failed to get the encrypted PXE password

 Last updated on 03/30/2026

<!-- p.430 -->

PXE boot doesn't work because a self-
signed certificate isn't created
This article helps you fix an issue in which the Preboot Execution Environment (PXE) boot
doesn't work in Configuration Manager if a self-signed certificate isn't created.

Original product version: Microsoft System Center 2012 Configuration Manager, Microsoft
System Center 2012 R2 Configuration Manager, Configuration Manager (current branch)
Original KB number: 4469580

Symptoms
When you try to start a computer through the PXE boot by using Configuration Manager, the
PXE boot process doesn't work.

When this problem occurs, the following error entry is logged in the SMSPXE log on the PXE-
enabled distribution point (DP) when you start Windows Deployment Services (WDS):

  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE PXE::MP_GetList failed; 0x80092002
  SMSPXE PXE::MP_ReportStatus failed; 0x80092002
  SMSPXE PXE::CPolicyProvider::InitializePerformanceCounters failed; 0x80070002
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE PXE::MP_GetList failed; 0x80092002
  SMSPXE PXE::MP_LookupDevice failed; 0x80092002
  SMSPXE PXE Provider failed to initialize MP connection.

<!-- p.431 -->

  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE PXE::MP_GetList failed; 0x80092002
  SMSPXE PXE::MP_ReportStatus failed; 0x80092002
  SMSPXE PXE::CPolicyProvider::InitializeMPConnection failed; 0x80092002

Additionally, the SMSPXE.log file includes the following error entries when you try to run a PXE
boot:

  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE PXE::MP_GetList failed; 0x80092002
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE PXE::MP_LookupDevice failed; 0x80092002
  SMSPXE PXE::MP_GetList failed; 0x80092002
  SMSPXE PXE::MP_LookupDevice failed; 0x80092002
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided

<!-- p.432 -->

  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE PXE::MP_GetList failed; 0x80092002
  SMSPXE PXE::MP_ReportStatus failed; 0x80092002
  SMSPXE Failed to create certificate store from encoded certificate. Verify the provided
  Certificate was provisioned correctly. .
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE PXE Provider failed to process message.
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)
  SMSPXE PXE::MP_GetList failed; 0x80092002
  SMSPXE PXE::MP_ReportStatus failed; 0x80092002
  SMSPXE PXE Provider failed to process message.
  An error occurred during encode or decode operation. (Error: 80092002; Source: Windows)

If you try to fix the problem by re-creating the self-signed certificate in the properties of the DP
by changing the date or time of the self-signed certificate, the certificate isn't re-created.

  ７ Note

  You can view certificates for the DP in the Configuration Manager console under
  Administration > Security > Certificates.

When you re-create the self-signed certificate for a DP, the Start Date value should be
approximately the time when the date and time values were changed for the certificate in the
DP properties.

When this problem occurs, the CertMgr.log file includes the following error entries:

  SMS_CERTIFICATE_MANAGER ~Found notification file C:\Program Files\Microsoft
  Configuration Manager\inboxes\certmgr.box\5_<DP_FQDN>.CMN
  SMS_CERTIFICATE_MANAGER Successfully made a network connection to \\
  <DP_FQDN>\ADMIN$.~
  SMS_CERTIFICATE_MANAGER Successfully made a network connection to \\
  <DP_FQDN>\ADMIN$.~
  SMS_CERTIFICATE_MANAGER Cannot get copy of security registry key on server
  (<DP_FQDN>) (0x80070005)
  SMS_CERTIFICATE_MANAGER Failed to get the copy of Security registry key on server
  <DP_FQDN> (0x80070005)

<!-- p.433 -->

  SMS_CERTIFICATE_MANAGER Cancelling network connection to \\<DP_FQDN>\ADMIN$.
  SMS_CERTIFICATE_MANAGER Cancelling network connection to \\<DP_FQDN>\ADMIN$.

Cause
This issue occurs if the IssuingCertificateList registry key is missing from the following
registry subkey on the DP:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Security

  ７ Note

  The registry key value could also be missing on the management point.

Resolution
To fix the issue, copy the IssuingCertificateList registry key value from the following registry
subkey on the management point:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Security

Then, copy this value to the same registry key on the DP. To do this, you can run the following
command at an elevated command prompt on the DP:

 Console

 REG.exe ADD "HKLM\SOFTWARE\Microsoft\SMS\Security" /v IssuingCertificateList /t
 REG_MULTI_SZ /d <Value_From_MP> /f

  ７ Note

  In this command, replace <Value_From_MP> with the value that you got from the
  management point (without the angle brackets).

If the registry key value is also missing on the management point, open SQL Server
Management Studio on the primary site, and then run the following query against the primary
site database:

 SQL

<!-- p.434 -->

 SELECT SD.SiteCode, SC.ComponentName, SCP.Name, SCP.Value1, SCP.Value2, SCP.Value3
 FROM SC_Component SC
 JOIN SC_SiteDefinition SD ON SD.SiteNumber = SC.SiteNumber
 JOIN SC_Component_Property SCP ON SCP.ComponentID = SC.ID
 WHERE SCP.Name = 'IssuingCertificateList'

  ） Important

  The value in the Value1 column must be copied to the registry on both the DP and the
  management point.

Copy the value in the Value1 column, and then run the following command at an elevated
command prompt on both the DP and management point:

 Console

 REG.exe ADD "HKLM\SOFTWARE\Microsoft\SMS\Security" /v IssuingCertificateList /t
 REG_MULTI_SZ /d <Value_from_DB> /f

  ７ Note

  In this command, replace <Value_from_DB> with the value that you copied from the
  primary site database (without the angle brackets).

You may want to check the CertMgr.log file to see whether additional DPs are affected. If they
are, run the REG.exe command on the additional DPs.

Last updated on 03/30/2026

<!-- p.435 -->

Troubleshooting PXE boot issues in
Configuration Manager
This article helps administrators diagnose and resolve PXE boot failures in Configuration
Manager.

  ） Important

  For home users: This article is only intended for technical support agents and IT
  professionals. If you're looking for help with a problem, please ask the Microsoft
  Community      .

Original product version: Configuration Manager (current branch), Microsoft System Center
2012 Configuration Manager, Microsoft System Center 2012 R2 Configuration Manager
Original KB number: 4468612

Introduction
For essential information about how PXE works, see the companion article Understand PXE
boot in ConfigMgr.

  ７ Note

  If you require PXE or multicast support, you need an on-premises distribution point to
  respond to these boot requests.

Before you start to troubleshoot on the PXE Service Point, we recommend that you try the
following solutions. If solution 1 works for you, you don't need to go to solution 2. These
solutions resolve most problems that affect PXE boot.

Solution 1: Verify IP Helpers
IP Helpers aren't required if all of the following components are on the same subnet or VLAN:

     The DHCP server
     The client computer

<!-- p.436 -->

     The ConfigMgr server that's running Windows Deployment Services (WDS)
     The PXE-enabled Distribution Point (DP)

IP Helpers must be configured on the routers if any of the components listed above are on
separate subnets or VLANs. It's usually the case in most environments.

This process varies and depends on the router hardware manufacturer. For a general overview
of the process, see Configuring Your Router to Forward Broadcasts. For more information
about how to correctly configure IP Helpers on your routers, contact the manufacturer of the
router.

IP Helpers are necessary because the PXE request generated by the client computer is a
broadcast that doesn't travel outside the local subnet or VLAN. If the DHCP server or the
WDS/PXE-enabled DP isn't on the same subnet or VLAN as the client computer, they won't see
or hear the PXE request broadcast from the client. Therefore, the servers won't respond to the
PXE request. To have the PXE request broadcast travel between subnets or VLANs, the PXE
request broadcast must be forwarded by the router to DHCP and WDS/PXE Service Point
servers so that they can correctly respond to the client's PXE request.

Using DHCP options isn't recommended
DHCP options can be problematic and might not work reliably or consistently. Also, using
DHCP options to control PXE requests in Configuration Manager is not supported by
Microsoft.

The recommended and supported method for PXE booting client computers on remote
subnets is to use IP Helpers.

For more information about DHCP options that aren't recommended or supported, see the
following articles:

     You want to PXE Boot? Don't use DHCP Options
     Configure at least one distribution point to accept PXE requests

Verify that DHCP options 60, 66, and 67 aren't configured

  ） Important

  Before you continue, it's imperative that you verify both the following conditions:

          The routers have IP Helpers configured.

<!-- p.437 -->

        The DHCP server does not have DHCP Options 60, 66, or 67 configured.

If both these criteria aren't met, the PXE Service Point will experience problems. When you
check DHCP options, make sure that you check the options at both the server and scope levels.

In certain instances, configuring DHCP options 60, 66, and 67 may make the PXE boot process
appear to proceed further along than it did before these options were configured. However, in
most cases, the process is actually proceeding along an incorrect path.

  ） Important

  The only exception in which a DHCP option must be used is if DHCP and WDS reside on
  the same server. In this situation, only DHCP Option 60 has to be set. DHCP Options 66
  and 67 should still not be set in this scenario. For more information, see Advanced
  troubleshooting for PXE boot issues in Configuration Manager.

Solution 2: Reinstall PXE (use only if Solution 1 didn't
resolve the issue)
In many cases, errors that occur during installation or configuration are the cause of PXE boot
issues. They can be difficult and time-consuming to pinpoint. In many cases, reinstalling PXE
and starting over can be the most effective and least time-consuming solution. To do it, follow
these steps:

   1. On the DP, clear the Enable PXE checkbox. When you're prompted to remove the
     Windows Deployment service, select Yes.

   2. Verify that PXE was uninstalled. Use Distmgr.log for DPs on site servers. Use
     Smsdpprov.log for a standalone DP.

        ） Important

        Do not proceed until you verify that PXE is fully uninstalled.

   3. In Server Manager, verify that WDS is uninstalled. If WDS is uninstalled, there should be a
     pending restart.

   4. Restart the server.

<!-- p.438 -->

   5. Locate and delete the RemoteInstall folder.

   6. Change the date on the self-signed certificate in the properties of PXE DP. Wait for the
     new certificate to be created. It isn't applicable if the DP is HTTPS.

   7. Add the PXE point again by selecting the check box in DP properties. Monitor through
     Distrmgr.log if the DP is on the site server. Or monitor through Smsdpprov.log for a
     standalone DP. Verify that the DP was installed.

   8. Verify that a new RemoteInstall folder was created.

   9. Verify that at least one x64 boot image and one x86 boot image is distributed to the DP.
     For each boot image that's distributed to the PXE DP and that will be used for PXE boot,
     make sure that the PXE option is enabled for each boot image. BIOS PCs or UEFI PCs in
     Legacy mode require an x86 boot image even if all PCs in the environment are x64.

 10. Verify that the WDS service was started.

 11. Navigate to the RemoteInstall folder, and verify the following SMS folders were created:

          SMSBoot
          SMSImages
          SMSTemp
          SMSTEmpBootFiles

 12. Navigate to the SMSImages folder, and verify that all the boot images that were
     distributed to the PXE DP are listed here. Boot images are listed by Package ID.

 13. Navigate to the SMSBoot folder, and verify that both the x86 and x64 folders are
     populated with files.

 14. Try a PXE boot.

Need more help
For more help with troubleshooting PXE boot issues, see Advanced troubleshooting for PXE
boot issues in Configuration Manager.

For more help to resolve this issue, see our TechNet support forum       or contact Microsoft
Support   .

Third-party information disclaimer

<!-- p.439 -->

The third-party products that this article discusses are manufactured by companies that are
independent of Microsoft. Microsoft makes no warranty, implied or otherwise, about the
performance or reliability of these products.

Third-party contact disclaimer

Microsoft provides third-party contact information to help you find additional information
about this topic. This contact information may change without notice. Microsoft does not
guarantee the accuracy of third-party contact information.

 Last updated on 03/30/2026

<!-- p.440 -->

Understand PXE boot in Configuration
Manager
This article describes basic processes of Preboot Execution Environment (PXE) boot in
Configuration Manager, how they work, and how they interoperate with each other.

Original product version: Configuration Manager (current branch), Microsoft System Center
2012 R2 Configuration Manager, Microsoft System Center 2012 Configuration Manager
Original KB number: 4468601

Introduction
Preboot Execution Environment (PXE) boot in System Center 2012 Configuration Manager
(ConfigMgr 2012 or ConfigMgr 2012 R2) and later versions enables administrators to easily
access the Windows Preinstallation Environment (WinPE) across the network via PXE. PXE is an
industry standard created by Intel that provides pre-boot services within the devices firmware
that enables devices to download network boot programs to client computers.

Configuration Manager relies on the Windows Deployment Services (WDS) server role via the
WDS PXE provider. In ConfigMgr 2012 and later versions, the SMS PXE provider (SMSPXE)
registers with the WDS service and supplies the logic for the PXE client requests.

Before troubleshooting PXE-related problems in Configuration Manager, it's important to
understand the basic processes involved, how they work and how they interoperate with each
other.

In all instances in this document, we're using System Center 2012 Configuration Manager R2
Cumulative Update 2 (ConfigMgr 2012 R2 CU2) and a remote site system installed on Windows
Server 2012 with the Distribution Point (DP) role installed.

PXE service point installation
We'll first look at the processes involved in the installation of the SMSPXE provider.

Installation is initiated by selecting the Enable PXE support for clients option on the PXE tab in
Distribution point properties. When PXE support is enabled, an instance of SMS_SCI_SysResUse
class is created.
