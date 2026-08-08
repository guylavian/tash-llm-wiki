---
title: "Welcome — pages 441-480"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0441-0480
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0441-0480
family: sccm
documentKind: "doc"
abstract: "Output SMSProv.log PutInstanceAsync SMS_SCI_SysResUseSMS Provider04/09/2014 11:30:131552 (0x0610) CExtProviderClassObject::DoPutInstanceInstanceSMS Provider04/09/2014 11:30:131552 (0x0610) INFO: 'RemoteDp.contoso.com' is a valid FQDN.SMS Provider04/09/2014 11:30:131552 (0x0610)"
---

# Welcome — pages 441-480

<!-- p.441 -->

 Output

 SMSProv.log
 PutInstanceAsync SMS_SCI_SysResUseSMS Provider04/09/2014 11:30:131552 (0x0610)
 CExtProviderClassObject::DoPutInstanceInstanceSMS Provider04/09/2014 11:30:131552
 (0x0610)
 INFO: 'RemoteDp.contoso.com' is a valid FQDN.SMS Provider04/09/2014 11:30:131552
 (0x0610)

In the WMI namespace Root\SMS\Site_RR2 (where RR2 is the site code of the site), the
SMS_SCI_SYSResUse class contains all the site systems roles on the primary site server. You can

run the following query in WBEMTEST to identify all the DPs on that site server:

 SQL

 SELECT * FROM SMS_SCI_SysResUse WHERE rolename like 'SMS Distribution Point'

Changing the properties of these roles via the SDK alters the site control file and configure the
DP. The IsPXE property name is a member of the props property and is set to 1 when the DP is
PXE enabled.

The SMS Database Monitor component detects the change to the DPNotificaiton and
DistributionPoints tables and drops files in distmgr.box:

 Output

 Smsdbmon.log
 RCV:UPDATE on SiteControl for SiteControl_AddUpd_HMAN [RR2 ][19604]
 RCV: UPDATE on SiteControl for SiteControl_AddUpd_SiteCtrl [RR2 ][19605]
 SND: Dropped C:\Program Files\Microsoft Configuration
 Manager\inboxes\hman.box\RR2.SCU [19604]
 SND: Dropped C:\Program Files\Microsoft Configuration
 Manager\inboxes\sitectrl.box\RR2.CT0 [19605]
 RCV: UPDATE on Sites for Sites_Interop_Update_HMAN [RR2 ][19606]
 SND: Dropped C:\Program Files\Microsoft Configuration
 Manager\inboxes\hman.box\RR2.ITC [19606]
 RCV: UPDATE on DistributionPoints for DP_Properties_Upd [15 ][19607]
 RCV: INSERT on PkgNotification for PkgNotify_Add [RR200002 ][19608]
 RCV: INSERT on PkgNotification for PkgNotify_Add [RR200003 ][19609]
 RCV: INSERT on DPNotification for DPNotify_ADD [15 ][19610]
 RCV: UPDATE on SiteControlNotification for SiteCtrlNot_Add_DDM [RR2 ][19611]
 SND: Dropped C:\Program Files\Microsoft Configuration
 Manager\inboxes\distmgr.box\15.NOT [19607]
 SND: Dropped C:\Program Files\Microsoft Configuration
 Manager\inboxes\distmgr.box\RR200002.PKN [19608]
 SND: Dropped C:\Program Files\Microsoft Configuration
 Manager\inboxes\distmgr.box\RR200003.PKN [19609]
 SND: Dropped C:\Program Files\Microsoft Configuration

<!-- p.442 -->

 Manager\inboxes\distmgr.box\15.DPN [19610]
 Site Control Notification.

The Distribution Manager component on the primary site server then initiates the configuration
of the remote DP:

 Output

 ConfigureDPSMS_DISTRIBUTION_MANAGER04/09/2014 11:30:263776 (0x0EC0)
 IISPortsList in the SCF is "80".SMS_DISTRIBUTION_MANAGER04/09/2014 11:30:263776
 (0x0EC0)
 ISSSLPortsList in the SCF is "443".SMS_DISTRIBUTION_MANAGER04/09/2014 11:30:263776
 (0x0EC0)
 IISWebSiteName in the SCF is "".SMS_DISTRIBUTION_MANAGER04/09/2014 11:30:263776
 (0x0EC0)
 IISSSLState in the SCF is 448.SMS_DISTRIBUTION_MANAGER04/09/2014 11:30:263776
 (0x0EC0)
 DP registry settings have been successfully updated on RemoteDp.contoso.com
 SMS_DISTRIBUTION_MANAGER04/09/2014 11:30:263776 (0x0EC0)
 ConfigurePXESMS_DISTRIBUTION_MANAGER04/09/2014 11:30:263776 (0x0EC0)

In the SMS DP Provider log on the remote DP, we can see the following information about the
PXE installation, where initially the PxeInstalled registry key isn't found:

 Output

 Smsdpprov.log
 [66C][Thu 09/04/2014 11:30:28]:CcmInstallPXE
 [66C][Thu 09/04/2014 11:30:28]:RegQueryValueExW failed for
 Software\Microsoft\SMS\DP, PxeInstalled
 [66C][Thu 09/04/2014 11:30:28]:RegReadDWord failed; 0x80070002

The Visual C++ Redistributable is installed:

 Output

 Smsdpprov.log
 [66C][Thu 09/04/2014 11:30:28]:Running: C:\SMS_DP$\sms\bin\vcredist_x64.exe /q /log
 "C:\SMS_DP$\sms\bin\vcredist.log"
 [66C][Thu 09/04/2014 11:30:28]:Waiting for the completion of:
 C:\SMS_DP$\sms\bin\vcredist_x64.exe /q /log "C:\SMS_DP$\sms\bin\vcredist.log"
 [66C][Thu 09/04/2014 11:30:39]:Run completed for:
 C:\SMS_DP$\sms\bin\vcredist_x64.exe /q /log "C:\SMS_DP$\sms\bin\vcredist.log"

WDS is installed:

 Output

<!-- p.443 -->

 Smsdpprov.log
 [66C][Thu 09/04/2014 11:30:39]:Created the DP mutex key for WDS.
 [66C][Thu 09/04/2014 11:30:39]:Failed to open WDS service.
 [66C][Thu 09/04/2014 11:30:39]:WDS is NOT INSTALLED
 [66C][Thu 09/04/2014 11:30:39]:Installing WDS.
 [66C][Thu 09/04/2014 11:30:39]:Running: ServerManagerCmd.exe -i WDS -a
 [66C][Thu 09/04/2014 11:30:39]:Failed (2) to run: ServerManagerCmd.exe -i WDS -a
 [66C][Thu 09/04/2014 11:30:39]:Running: PowerShell.exe -Command Import-Module
 ServerManager; Get-WindowsFeature WDS; Add-WindowsFeature WDS
 [66C][Thu 09/04/2014 11:30:39]:Waiting for the completion of: PowerShell.exe -
 Command Import-Module ServerManager; Get-WindowsFeature WDS; Add-WindowsFeature WDS
 [66C][Thu 09/04/2014 11:31:35]:Run completed for: PowerShell.exe -Command Import-
 Module ServerManager; Get-WindowsFeature WDS; Add-WindowsFeature WDS
 [66C][Thu 09/04/2014 11:31:35]:Successfully installed WDS.

TFTP read filters are configured:

 Output

 Smsdpprov.log
 [66C][Thu 09/04/2014 11:31:35]:Setting TFTP config key as:
 System\CurrentControlSet\Services\WDSSERVER\Providers\WDSTFTP
 [66C][Thu 09/04/2014 11:31:35]:Configuring TFTP read filters
 [66C][Thu 09/04/2014 11:31:35]:SetupComplete is set to 0

The REMINST share is created and WDS is configured:

 Output

 Smsdpprov.log
 [66C][Thu 09/04/2014 11:31:35]:RegQueryValueExW failed for
 Software\Microsoft\Windows\CurrentVersion\Setup, REMINST
 [66C][Thu 09/04/2014 11:31:35]:RegReadDWord failed; 0x80070002
 [66C][Thu 09/04/2014 11:31:35]:REMINST not set in WDS
 [66C][Thu 09/04/2014 11:31:35]:WDS is NOT Configured
 [66C][Thu 09/04/2014 11:31:35]:Share (REMINST) does not exist. (NetNameNotFound)
 (0x00000906)
 [66C][Thu 09/04/2014 11:31:35]:GetFileSharePath failed; 0x80070906
 [66C][Thu 09/04/2014 11:31:35]:REMINST share does not exist. Need to create it.
 [66C][Thu 09/04/2014 11:31:35]:Enumerating drives A through Z for the NTFS drive
 with the most free space.
 [66C][Thu 09/04/2014 11:31:37]:Drive 'C:\' is the best drive for the SMS
 installation directory.
 [66C][Thu 09/04/2014 11:31:37]:Creating REMINST share to point to: C:\RemoteInstall
 [66C][Thu 09/04/2014 11:31:37]:Succesfully created share REMINST
 [66C][Thu 09/04/2014 11:31:37]:Removing existing PXE related directories
 [66C][Thu 09/04/2014 11:31:37]:Registering WDS provider: SourceDir:
 C:\SMS_DP$\sms\bin
 [66C][Thu 09/04/2014 11:31:37]:Registering WDS provider: ProviderPath:
 C:\SMS_DP$\sms\bin\smspxe.dll
 [66C][Thu 09/04/2014 11:31:37]:DoPxeProviderRegister

<!-- p.444 -->

 [66C][Thu 09/04/2014 11:31:37]:PxeLoadWdsPxe
 [66C][Thu 09/04/2014 11:31:37]:Loading wdspxe.dll from
 C:\Windows\system32\wdspxe.dll
 [66C][Thu 09/04/2014 11:31:37]:wdspxe.dll is loaded
 [66C][Thu 09/04/2014 11:31:37]:PxeProviderRegister has suceeded (0x00000000)
 [66C][Thu 09/04/2014 11:31:37]:Disabling WDS/RIS functionality
 [66C][Thu 09/04/2014 11:31:39]:WDSServer status is 1
 [66C][Thu 09/04/2014 11:31:39]:WDSServer is NOT STARTED
 [66C][Thu 09/04/2014 11:31:39]:Running: WDSUTIL.exe /Initialize-Server
 /REMINST:"C:\RemoteInstall"
 [66C][Thu 09/04/2014 11:31:39]:Waiting for the completion of: WDSUTIL.exe
 /Initialize-Server /REMINST:"C:\RemoteInstall"
 [66C][Thu 09/04/2014 11:31:50]:Run completed for: WDSUTIL.exe /Initialize-Server
 /REMINST:"C:\RemoteInstall"
 [66C][Thu 09/04/2014 11:31:50]:CcmInstallPXE: Deleting the DP mutex key for WDS.
 [66C][Thu 09/04/2014 11:31:50]:Installed PXE
 [66C][Thu 09/04/2014 11:32:03]:CcmInstallPXE
 [66C][Thu 09/04/2014 11:32:03]:PXE provider is already installed.
 [66C][Thu 09/04/2014 11:32:03]:Installed PXE

On the remote DP, we can now see the following values added in
HKEY_LOCAL_MACHINE\Software\Microsoft\SMS\DP :

  ７ Note

  PxeInstalled and IsPXE are set to 1.

If we look at the remote DP's file system, there's a new login C:\SMS_DP$\sms\logs :

 Output

 SMSPXE.log
 Machine is running Windows Longhorn. (NTVersion=0X602, ServicePack=0)
 Cannot read the registry value of MACIgnoreListFile (00000000)
 MAC Ignore List Filename in registry is empty
 Begin validation of Certificate [Thumbprint
 AA11BB22CC33DD44EE55FF66AA77BB88CC99DD00] issued to 'e728f6ce-29a6-4ac3-974e-
 ba3dc855d9a4'
 Completed validation of Certificate [Thumbprint
 AA11BB22CC33DD44EE55FF66AA77BB88CC99DD00] issued to 'e728f6ce-29a6-4ac3-974e-
 ba3dc855d9a4'

The Distribution Point should now be PXE-enabled and ready to accept incoming requests.

<!-- p.445 -->

Add boot images to a PXE-enabled DP
Whenever a new PXE-enabled distribution point is configured, there are more steps that need
to be completed to enable full functionality. One of these is that you must distribute the x86
and x64 boot images to the new PXE-enabled DP.

To do this, navigate to Software Library > Operating Systems > Boot Images > Boot Image
(x86), and then right-click and select Distribute Content > Add the Boot Image to the PXE
enabled DP. Repeat this process for Boot Image (x64).

After this is done, Distribution Manager starts processing the request and initiate the
distribution to the remote DP:

 Output

 DistMgr.log
 Found notification for package 'RR200004'Used 0 out of 30 allowed processing
 threads.
 Starting package processing thread, thread ID = 0x152C (5420)
 Start adding package to server ["Display=\\RemoteDp.contoso.com\"]MSWNET:
 ["SMS_SITE=RR2"]\\RemoteDp.contoso.com\...
 Attempting to add or update a package on a distribution point.
 Successfully made a network connection to \\RemoteDp.contoso.com\ADMIN$.
 CreateSignatureShare, connecting to DP
 Signature share exists on distribution point path \\RemoteDp.contoso.com\SMSSIG$
 Share SMSPKGC$ exists on distribution point \\RemoteDp.contoso.com\SMSPKGC$
 Checking configuration of IIS virtual directories on DP
 ["Display=\\RemoteDp.contoso.com\"]MSWNET:["SMS_SITE=RR2"]\\RemoteDp.contoso.com\
 Creating, reading or updating IIS registry key for a distribution point.
 Virtual Directory SMS_DP_SMSSIG$ for the physical path C:\SMSSIG$ already exists.
 Created package transfer job to send package RR200004 to distribution point
 ["Display=\\RemoteDp.contoso.com\"]MSWNET:["SMS_SITE=RR2"]\\RemoteDp.contoso.com\.
 StoredPkgVersion (9) of package RR200004. StoredPkgVersion in database is 9.
 SourceVersion (9) of package RR200004. SourceVersion in database is 9.

Package Transfer Manager (the DP is remote) then initiates sending of the content:

 Output

 PkgXferMgr.log
 DeleteJobNotificationFiles deleted 1 *.PKN file(s) this cycle.
 Found send request with ID: 105, Package: RR200004, Version:9, Priority: 2,
 Destination: REMOTEDP.CONTOSO.COM, DPPriority: 200
 Created sending thread (Thread ID = 0x1140)
 Sending thread starting for Job: 105, package: RR200004, Version: 9, Priority: 2,
 server: REMOTEDP.CONTOSO.COM, DPPriority: 200
 Sending legacy content RR200004.9 for package RR200004
 Finished sending SWD package RR200004 version 9 to distribution point

<!-- p.446 -->

 REMOTEDP.CONTOSO.COM
 Sent status to the distribution manager for pkg RR200004, version 9, status 3 and
 distribution point ["Display=\\RemoteDp.contoso.com\"]MSWNET:
 ["SMS_SITE=RR2"]\\RemoteDp.contoso.com\
 StateTable::CState::Handle - (8210:1 2014-09-10 13:19:12.087+00:00) >> (8203:3
 2013-11-26 15:43:48.108+00:00)
 Successfully send state change notification 7F6041B0-3EE2-427F-AB72-B89610A6331C
 Sending thread complete

SMS Distribution Point Provider then deploys the WIM to the remote install directory:

 Output

 Smsdpprov.log
 [468][Wed 09/10/2014 14:09:59]:A DP usage gathering task has been registered
 successfully
 [99C][Wed 09/10/2014 14:19:07]:Content 'RR200004.9' for package 'RR200004' has been
 added to content library successfully
 [99C][Wed 09/10/2014 14:19:07]:Expanding
 C:\SCCMContentLib\FileLib\E8A1\E8A136A1348B4CFE97334D0F65934845F2B4675D0B7D925AB830
 378F4ECF39B9 from package RR200004
 [99C][Wed 09/10/2014 14:19:07]:Finding Wimgapi.Dll
 [99C][Wed 09/10/2014 14:19:07]:Found C:\Windows\system32\wimgapi.dll
 [99C][Wed 09/10/2014 14:19:07]:Expanding RR200004 to C:\RemoteInstall\SMSImages

SMSPXE discovers the new image:

 Output

 SMSPXE.log
 Found new image RR200004
 PXE::CBootImageManager::QueryWIMInfo
 Loaded C:\Windows\system32\wimgapi.dll
 Opening image file C:\RemoteInstall\SMSImages\RR200004\boot.RR200004.wim
 Found Image file: C:\RemoteInstall\SMSImages\RR200004\boot.RR200004.wim
 PackageID: RR200004
 ProductName: Microsoft&reg; Windows&reg; Operating System
 Architecture: 0
 Description: Microsoft Windows PE (x86)
 Version:
 Creator:
 SystemDir: WINDOWS
 Closing image file C:\RemoteInstall\SMSImages\RR200004\boot.RR200004.wim
 PXE::CBootImageManager::InstallBootFilesForImage
 Temporary path to copy extract files from:
 C:\RemoteInstall\SMSTempBootFiles\RR200004.

Make sure that these boot images are configured to deploy from the PXE-enabled DP. Right-
click the boot image and select Properties > Data Source, and then select Deploy this boot
image from the PXE-enabled distribution point.

<!-- p.447 -->

The PXE boot process
The example boot process described here involves three machines: The DHCP server, the PXE-
enabled DP, and the client (an x64 BIOS computer). All are located on the same subnet.

  ７ Note

  You must make sure that the DHCP (67 and 68), TFTP (69), and BINL (4011) ports are open
  between the client computer, the DHCP server, and the PXE enabled DP.

In the PXE boot process, the client must first acquire TCP/IP parameters and the location of the
TFTP boot server. Once a device is powered on and completes the POST, it begins the PXE boot
process (prompted via the boot selection menu).

   1. The first thing the PXE firmware does is sending a DHCPDISCOVER (a UDP packet)
     broadcast to get TCP/IP details. This includes a list of parameter requests, and the
     following example is a sample network trace with the parameter list from a
     DHCPDISCOVER packet:

     The PXE client then identifies the vendor and machine-specific information so that it can
     request the location and file name of the appropriate boot image file.

<!-- p.448 -->

2. The DHCP server and the PXE-enabled DP then send a DHCPOFFER to the client
  containing all of the relevant TCP/IP parameters.

  In the following example DHCP offer, it doesn't contain the server name or boot file
  information because this is the offer from the DHCP server rather than the PXE enabled
  DP.

3. The client then replies with a DHCPREQUEST once it has selected a DHCPOFFER. This
  contains the IP address from the offer that was selected.

4. The DHCP server responds to the DHCPREQUEST with a DHCPACK that contains the
  same details as the DHCPOFFER. The server host name and the boot file name aren't
  provided here:

<!-- p.449 -->

5. At this point, we still don't have the boot file information. However now the client has an
  IP address. Next, the PXE client sends a new DHCPREQUEST to the PXE-enabled DP after
  receiving a DHCPOFFER from the earlier DHCPDISCOVER broadcast.

6. The PXE-enabled DP sends a DHCPACK that contains the BootFileName location and the
  WDS network boot program (NBP).

<!-- p.450 -->

Downloading the boot files
 1. After the DHCP conversation completes, the client will start the TFTP session with a read
   request:

   The server responds with the tsize and then the blksize. The client then transfers the file
   from the server.

     ７ Note

     The size of these blocks is the blksize, and in this case it's set to 1456 bytes. The
     blksize is configurable on Windows Server 2008 and later versions. See Operating
     system deployment over a network by using WDS fails in Windows Server 2008
     and in Windows Server 2008 R2 .

   Here we can see the end of the DHCP conversation and the start of the TFTP transfer:

<!-- p.451 -->

When the WDS network boot program (NBP) has been transferred to the client computer,
it runs. In our example, it starts by downloading wdsnbp.com . The NBP dictates whether
the client can boot from the network, whether the client must press F12 to initiate the
boot and which boot image the client receives.

NBPs are both architecture and firmware specific (BIOS or UEFI). On BIOS computers, the
NBP is a 16-bit real-mode application, therefore it's possible to use the same NBP for
both x86-based and x64-based operating systems.

In our case (an x64 BIOS machine), the NBP is located in the following directory on the
PXE enabled DP: \\remotedp\c$\RemoteInstall\SMSBoot\x64

The files perform the following functions:

     PXEboot.com - x86 and x64 BIOS: Requires the end user to press F12 for PXE boot to

     continue (this is the default NBP).

     PXEboot.n12 - x86 and x64 BIOS: Immediately begins PXE boot (doesn't require

     pressing F12 on the client).

     AbortPXE.com - x86 and x64 BIOS: Allows the device to immediately begin booting

     by using the next boot device specified in the BIOS. This allows for devices that
     shouldn't be booting using PXE to immediately begin their secondary boot process
     without waiting for a timeout.

<!-- p.452 -->

           Bootmgfw.efi - x64 UEFI and IA64 UEFI: The EFI version of PXEboot.com or

           PXEboot.n12 (in EFI, the choice of whether or not to PXE boot is handled within the

          EFI shell and not by the NBP). Bootmgfw.efi is the equivalent of combining the
          functionality of PXEboot.com , PXEboot.n12 , abortpxe.com , and bootmgr.exe .

           wdsnbp.com - x86 and x64 BIOS: A special NBP developed for use by Windows

          Deployment Services that serves the following general purposes:
             Architecture detection
             Pending devices scenarios

           Wdsmgfw.efi - x64 UEFI and IA64 UEFI: A special NBP developed for use by Windows

          Deployment Services that serves the following general purposes:
             Handles prompting the user to press a key to continue PXE boot
             Pending devices scenarios

   2. The NBP downloads the operating system loader and the boot files via TFTP, which
     include the following:

           smsboot\x64\pxeboot.com

           smsboot\x64\bootmgr.exe

           \SMSBoot\Fonts\wgl4_boot.ttf

           \SMSBoot\boot.sdi

           \SMSImages\RR200004\boot.RR200004.wim

   3. A RAMDISK is created using these files and the WinPE WIM file in memory.

   4. The client boots from the RAMDISK.

WinPE boot
After WinPE boots, the TS boot shell initiates from the SMS folder that's included in the WinPE
image (this folder is injected into the boot WIM when it's imported into Configuration
Manager). You can see this process logged in SMSTS.log that's located under
X:\Windows\Temp\SMSTSLog\ .

<!-- p.453 -->

   Tip

  To access this login WinPE, enable the command prompt on the boot image. To do this,
  right-click Boot Image > Properties > Customization, and then check Enable command
  support (testing only). You can then access the command prompt by pressing F8 in
  WinPE.

Here's the initial TS boot shell process:

 Output

 SMSTS.log
 ========================[ TSBootShell.exe ]========================
 Succeeded loading resource DLL 'X:\sms\bin\i386\1033\TSRES.DLL'
 Debug shell is enabled
 Waiting for PNP initialization...
 RAM Disk Boot Path: NET(0)\SMSIMAGES\RR200004\BOOT.RR200004.WIM
 Booted from network (PXE)
 Network(PXE) path: X:\sms\data\
 Found config path X:\sms\data\
 This is not a fixed non usb disk
 Booting from removable media, not restoring bootloaders on hard drive
 X:\sms\data\WinPE does not exist.
 X:\_SmsTsWinPE\WinPE does not exist.
 Executing command line: wpeinit.exe -winpe
 The command completed successfully.
 Starting DNS client service.
 Executing command line: X:\sms\bin\i386\TsmBootstrap.exe /env:WinPE
 /configpath:X:\sms\data\
 The command completed successfully.

Followed by the Task Sequence Manager boot strap:

 Output

 SMSTS.log
 ========================[ TSMBootStrap.exe ]========================
 Command line: X:\sms\bin\i386\TsmBootstrap.exe /env:WinPE /configpath:X:\sms\data\
 Succeeded loading resource DLL 'X:\sms\bin\i386\1033\TSRES.DLL'
 Succeeded loading resource DLL 'X:\sms\bin\i386\TSRESNLC.DLL'
 Current OS version is 6.2.9200.0
 Adding SMS bin folder "X:\sms\bin\i386" to the system environment PATH
 PXE Boot with Root = X:\
 Executing from PXE in WinPE
 Loading TsPxe.dll from X:\sms\bin\i386\TsPxe.dll

Once TSPXE is loaded, it downloads the TS variables using TFTP:

<!-- p.454 -->

 Output

 SMSTS.log
 TsPxe.dll loaded
 Device has PXE booted
 Variable Path: \SMSTemp\2014.09.05.18.20.31.0001.{0C616323-A027-41B0-A215-
 057AF4F1E361}.boot.var
 Succesfully added firewall rule for Tftp
 Executing: X:\sms\bin\i386\smstftp.exe -i 10.238.0.2 get
 \SMSTemp\2014.09.05.18.20.31.0001.{0C616323-A027-41B0-A215-057AF4F1E361}.boot.var
 X:\sms\data\variables.dat
 Executing command line: "X:\sms\bin\i386\smstftp.exe" -i 10.238.0.2 get
 \SMSTemp\2014.09.05.18.20.31.0001.{0C616323-A027-41B0-A215-057AF4F1E361}.boot.var
 X:\sms\data\variables.dat
 Process completed with exit code 0
 Succesfully removed firewall rule for Tftp
 Successfully downloaded pxe variable file.

 Loading Media Variables from "X:\sms\data\variables.dat"
 Loading Media Variables from "X:\sms\data\variables.dat"
 Found network adapter "Intel 21140-Based PCI Fast Ethernet Adapter (Emulated)" with
 IP Address 10.238.0.3.
 Loading Media Variables from "X:\sms\data\variables.dat"
 Loading variables from the Task Sequencing Removable Media.
 Loading Media Variables from "X:\sms\data\variables.dat"
 Succeeded loading resource DLL "X:\sms\bin\i386\1033\TSRES.DLL"

 Setting SMSTSMP TS environment variable
 Setting _SMSMediaGuid TS environment variable
 Setting _SMSTSBootMediaPackageID TS environment variable
 Setting _SMSTSHTTPPort TS environment variable
 Setting _SMSTSHTTPSPort TS environment variable
 Setting _SMSTSIISSSLState TS environment variable
 Setting _SMSTSLaunchMode TS environment variable
 Setting _SMSTSMediaPFX TS environment variable
 Setting _SMSTSPublicRootKey TS environment variable
 Setting _SMSTSRootCACerts TS environment variable
 Setting _SMSTSSiteCode TS environment variable
 Setting _SMSTSSiteSigningCertificate TS environment variable
 Setting _SMSTSUseFirstCert TS environment variable
 Setting _SMSTSx64UnknownMachineGUID TS environment variable
 Setting _SMSTSx86UnknownMachineGUID TS environment variable

At this point, TSPXE locates the Management Point (MP) and downloads policy before
presenting the user interface for the user to select the optional Task Sequence:

 Output

 SMSTS.log
 site=RR2, MP=<http://ConfigMgrR2.CONTOSO.COM>, ports: http=80,https=443
 certificates are received from MP.
 CLibSMSMessageWinHttpTransport::Send: URL: ConfigMgrR2.CONTOSO.COM:80 CCM_POST

<!-- p.455 -->

  /ccm_system/request
  Request was successful.
  Downloading policy from <http://ConfigMgrR2.CONTOSO.COM>.
  Retrieving Policy Assignments:
  Processing Policy Assignment {7898f153-a6de-43e9-98c3-ca5cc61483b0}.
  Processing Policy Assignment {fba19677-0e9b-490d-b601-07e247979bd4}.
  Processing Policy Assignment {6306ca4c-e7ed-4cf5-8419-af9b1695a909}.
  Processing Policy Assignment {05a027ff-e9cf-4fa1-8bd8-4565481061e2}.
  Processing Policy Assignment {b3c991f6-9f83-43c3-875c-f60c4492d278}.
  ...
  Successfully read 152 policy assignments.

Lastly, the collection and machine variables are downloaded and the Welcome Page is
activated:

  Output

  SMSTS.log
  Retrieving collection variable policy.
  Found 0 collection variables.
  Retrieving machine variable policy.
  Downloading policy body {01000053}-{RR2}.
  Response ID: {01000053}-{RR2}
  Reading Policy Body.
  Parsing Policy Body.
  Found 0 machine variables.
  Setting collection variables in the task sequencing environment.
  Setting machine variables in the task sequencing environment.
  Running Wizard in Interactive mode
  Loading Media Variables from "X:\sms\data\variables.dat"
  Activating Welcome Page.
  Loading bitmap

More information
For more information about troubleshooting PXE boot issues, see the following articles:

      Troubleshooting PXE boot issues
      Advanced troubleshooting for PXE boot issues in Configuration Manager.

 Last updated on 03/30/2026

<!-- p.456 -->

Configuration Manager PXE boot causes
Windows Deployment Services to crash
This article provides workarounds to solve the Windows Deployment Services (WDS) crash that
is caused by Pre-Boot Execution Environment (PXE) boot in a Configuration Manager
environment.

Original product version: Microsoft System Center 2012 Configuration Manager, Microsoft
System Center 2012 R2 Configuration Manager
Original KB number: 3046055

Symptoms
You use a Pre-Boot Execution Environment (PXE) distribution point to perform PXE boots. In
this situation, the operation first appears to work successfully, but then the process stops
running. When you examine the server on which the PXE distribution point and WDS are
installed, you discover that WDS has crashed.

Restarting WDS on the server doesn't resolve the issue. When you restart both the Windows
Management Instrumentation and WDS, or when you restart the server itself, it may
temporarily resolve the problem. However, the issue eventually recurs, and WDS crashes again.

If you try to reproduce the issue by continuing to perform PXE boots, you discover that
although the issue may occur frequently, it cannot be reproduced on a consistent basis. The
crash behavior occurs randomly.

Cause
This issue may occur in environments where there are redundant backup routers. If IP Helpers
for PXE (DHCP relays) are positioned on both the primary and backup routers, it may cause a
situation where two duplicate PXE request packets are sent to WDS: the original PXE request by
the primary router and a duplicate PXE request by the backup, redundant router.

If the timing is just right, the duplicate PXE request may overwrite some of the information in
WDS from the original PXE request. This issue causes information in WDS for the PXE request
to become corrupted, and then WDS crashes.

<!-- p.457 -->

Workaround
To work around the issue, use one of these methods:

     Disable the PXE IP Helpers in the backup, redundant router so that duplicate PXE requests
     are not sent. For more information about PXE IP Helpers, see Configuring your router to
     forward broadcasts.

     Configure the Configuration Manager WDS provider to be single-threaded instead of
     multithreaded. This configuration will limit WDS processing of PXE requests to one at a
     time and will prevent the second, duplicate PXE request from conflicting with the original
     request. To configure the Configuration Manager WDS provider for single-threading,
     create the NumberOfThreads registry key with a DWORD value of 1 in the following
     location:

     Configuration Manager 2012 DP/WDS server:
     HKEY_LOCAL_MACHINE\Software\Microsoft\SMS\DP

     Doing this configuration does not typically affect server performance for PXE requests
     except in environments where a large number of PXE requests are performed on a
     consistent basis. In these environments, we recommend that you use the first
     workaround.

Last updated on 03/30/2026

<!-- p.458 -->

WDS doesn't start on a PXE enabled
remote distribution point in Configuration
Manager
This article fixes an issue in which Windows Deployment Services (WDS) doesn't start on a PXE
enabled remote distribution point in Configuration Manager.

Original product version: System Center 2012 Configuration Manager
Original KB number: 2712387

Symptoms
After enabling the PXE feature of a remote Configuration Manager distribution point (DP),
Windows Deployment Services (WDS) and PXE install correctly, however WDS never starts.
Attempting to manually start WDS via the Services console results in the following error
message:

  Windows could not start the Windows Deployment Services Server on Local Computer. For
  more information, review the System Event Log. If this is a non-Microsoft service, contact
  the service vendor, or refer to service-specific error code -1056505588.

Looking at the Application System event log on a 64-bit server reveals the following error
messages:

  Log Name:      Application
  Source:     SideBySide
  Date:       <Date><Time>
  Event ID:   33
  Task Category: None
  Level:      Error
  Keywords: Classic
  User:       N/A
  Computer: <Remote_DP_Server>
  Description:
  Activation context generation failed for "C:\SMS_DP$\sms\bin\smspxe.dll". Dependent

<!-- p.459 -->

Assembly
Microsoft.VC90.CRT,processorArchitecture="amd64",publicKeyToken="1fc8b3b9a1e18e3b",
type="win32",version="9.0.30729.4148" could not be found. Please use sxstrace.exe for
detailed diagnosis.

Log Name: Application
Source:        WDSPXE
Date:       <Date><Time>
Event ID:      259
Task Category: WDSPXE
Level:      Error
Keywords: Classic
User:       N/A
Computer:      <Remote_DP_Server>
Description:
An error occurred while trying to load the module from C:\SMS_DP$\sms\bin\smspxe.dll
for provider SMSPXE. If the provider is marked as critical, the Windows Deployment
Services server will be shutdown.

Log Name: Application
Source:        WDSPXE
Date:       <Date><Time>
Event ID:      264
Task Category: WDSPXE
Level:      Error
Keywords: Classic
User:       N/A
Computer: <Remote_DP_Server>
Description:
An error occurred while trying to initialize provider SMSPXE. Since the provider isn't
marked as critical, the Windows Deployment Services server will remain started.

Error Information: 0x36B1

Log Name: Application
Source:        WDSPXE
Date:       <Date><Time>

<!-- p.460 -->

Event ID:      268
Task Category: WDSPXE
Level:      Error
Keywords: Classic
User:       N/A
Computer: <Remote_DP_Server>
Description:
All registered providers failed to initialize. Please review the Event Log for specific error
messages for each provider. Windows Deployment Server will be shutdown.

Log Name: Application
Source:        WDSServer
Date:       <Date><Time>
Event ID:      513
Task Category: WDSServer
Level:      Error
Keywords: Classic
User:       N/A
Computer: <Remote_DP_Server>
Description:
An error occurred while trying to initialize provider WDSPXE from
C:\Windows\system32\wdspxe.dll. Windows Deployment Services server will be shutdown.

Error Information: 0xC107010C

Log Name: Application
Source:        WDSServer
Date:       <Date><Time>
Event ID:      257
Task Category: WDSServer
Level:      Error
Keywords: Classic
User:       N/A
Computer: <Remote_DP_Server>
Description:
An error occurred while trying to start the Windows Deployment Services server.

Error Information: 0xC107010C

<!-- p.461 -->

Cause
This issue can occur when a dependent component, Microsoft.VC90.CRT , is not available. This
component is normally available via a DLL installed by Microsoft Visual C++ 2008
Redistributable. Microsoft Visual C++ 2008 Redistributable is normally installed during the
Configuration Manager client install via the install file vcredist_x86.exe or vcredist_x64.exe. If
the Configuration Manager client has not been installed on the server hosting the PXE enabled
remote DP, the Microsoft Visual C++ 2008 Redistributable will also not have been installed and
Microsoft.VC90.CRT will not be available.

  ７ Note

  Microsoft Visual C++ 2008 Redistributable is a common install for many different software
  install packages. It may be installed on the server even if the Configuration Manager client
  is not installed on the server.

Resolution
To resolve the problem, install the Configuration Manager client on the server hosting the PXE
enabled remote DP.

If the PXE enabled remote DP server is not going to also be a Configuration Manager client
and therefore the Configuration Manager client install is not desired, Microsoft Visual C++
2008 Redistributable can be installed separately on the server by manually running either
vcredist_x86.exe (32-bit Windows) or vcredist_x64.exe (64-bit Windows) from the
Configuration Manager client install files. These install files can be found in the client install
directory on the parent primary site server under the following paths:

      vcredist_x86.exe: <Configuration Manager_2012_Install_Directory>\Client\i386
      vcredist_x64.exe: <Configuration Manager_2012_Install_Directory>\Client\x64

Once the Microsoft Visual C++ 2008 Redistributable has been installed via the Configuration
Manager client install or a manual install, manually start WDS via the Services console. WDS
should subsequently be able to start automatically.

 Last updated on 03/30/2026

<!-- p.462 -->

A client computer can steal the
Configuration Manager GUID of an
Unknown Computer object during imaging
This article provides the information to solve the issue that the Configuration Manager Unique
Identifier (GUID) of an Unknown Computer object is taken by a client computer that's being
imaged.

Original product version: Configuration Manager (current branch)
Original KB number: 4471061

Symptoms
Configuration Manager current branch version 1702 included a new feature that lets you use
the Previous button to retry a failed task sequence in the Task Sequence Wizard when it runs
on Microsoft Windows Preinstallation Environment (Windows PE).

For more information about this feature, see Return to previous page when a task sequence
fails.

This feature introduced the following issue:

When the Previous button is selected, the client PC that's being imaged can steal the
Configuration Manager Unique Identifier (GUID) of the Unknown Computer object that's being
used (either the x64 Unknown Computer or the x86 Unknown Computer).

This issue was fixed in Update rollup for Configuration Manager current branch, version
1702     .

This issue is also fixed in all subsequent versions of Configuration Manager current branch.

However, starting in Configuration Manager current branch version 1702, unknown computers
that are started from media or preboot execution environment (PXE) may not find task
sequences that are targeted to them. In this scenario, the following error message is logged in
the SMSTS.log:

   There are no task sequences available to this computer. Please ensure you have at least
   one task sequence advertised to this computer.

<!-- p.463 -->

  Unspecified error (Error: 80004005; Source: Windows)

This issue may occur if the Previous button on the Select a task sequence to run page is
selected on the unknown computer.

This issue is also fixed in all subsequent versions of Configuration Manager current branch.

Despite applying the update rollup in Configuration Manager current branch version 1702 or
upgrading to a later version of Configuration Manager, the issue still occurs.

Cause
This issue may continue to occur because the fix in the update rollup for Configuration
Manager current branch version 1702 and later Configuration Manager current branch versions
prevents the issue from occurring only going forward. It doesn't fix the issue if the issue
currently exists in the environment.

Therefore, the issue can continue to occur in Configuration Manager current branch version
1702 or newer even after the version 1702 update rollup or a later version is applied. This is
true unless the following steps are taken:

     Update the boot images on distribution points.
     Recreate the boot media by using the updated images.
     Correctly clean the client PC that stole the GUID.

Resolution

  ２ Warning

  Do not try to fix this issue by recreating the Unknown Computer objects. This doesn't
  correctly fix the issue, and it doesn't prevent the issue from reoccurring going forward.
  Additionally, there are known issues that occur in environments that have multiple
  Unknown Computer objects for a single site. If you have previously tried to resolve this
  issue by recreating the Unknown Computer objects, see Remove duplicate Unknown
  Computer objects.

To resolve this issue and prevent it from returning in the environment, follow these steps:

<!-- p.464 -->

   1. Update all boot images in the environment. To do this, right-click the images in the
     Configuration Manager console, and then select Update Distribution Points. This puts the
     updated Configuration Manager binaries that contain the fix into the boot image. For
     more information, see Update distribution points with the boot image.

   2. If you use media in the environment, recreate all media in the environment after you
     update all boot images on the distribution points. This makes sure that the updated boot
     images that have the fix are in the media that's being used in the environment.

     To prevent media that has old boot images from being used, the certificates for those
     boot images can be blocked in the Configuration Manager console under the
     Administration > Security > Certificates node. To make sure that the issue doesn't recur,
     we recommend that you block all certificates for all media created before the boot
     images were updated in step 1. The date on which the media was created is displayed in
     the Start Date column.

     For more information about how to create media, see Create task sequence media.

   3. The client computer that stole the GUID must be cleaned correctly.

To correctly clean the client that stole the GUID, follow these steps:

   1. Identify the computer that acquired the GUID. To do this, examine the properties of the
     Unknown Computer object (usually x64 Unknown Computer), note the value of
     Configuration Manager Unique Identifier, and then run a query in the Configuration
     Manager console to identify the computer object that has the same GUID. You can do all
     these steps from the console. You do not have to go into the SQL Server database to do
     this.

   2. After you identify the computer that acquired the stolen GUID, remotely connect to that
     computer, and then completely clean the Configuration Manager client. This involves
     more than simply uninstalling the client. Instead, you must follow steps 3-7.

   3. On the client computer, under C:\Windows\CCMSetup , run the CCMSetup.exe /uninstall
     command at an elevated command prompt.

   4. Monitor Task Manager until CCMSetup finishes running. Double-check the ccmsetup.log
     file to make sure that the client was uninstalled correctly.

   5. On the client computer, delete the following directories:

             C:\Windows\CCM

<!-- p.465 -->

        C:\Windows\CCMSetup

     ７ Note

     To fully delete these directories, you may have to restart the computer.

6. On the client computer, delete the following registry keys (if they exist):

        HKEY_LOCAL_MACHINE\Software\Microsoft\CCM

        HKEY_LOCAL_MACHINE\Software\Microsoft\CCMSetup

        HKEY_LOCAL_MACHINE\Software\Microsoft\SMS

7. On the client computer, delete the C:\Windows\SMSCFG.ini file.

8. On the client computer, delete all certificates under the SMS > Certificates node in the
  Certificates console for the Computer account. To do this, follow these steps:

   a. Run MMC.exe at an elevated command prompt.

  b. On the File menu, select Add/Remove Snap-in.

   c. Select Certificates, and then select Add.

  d. Select Computer account and then select Next.

   e. Select Local computer and then select Finish.

   f. Select OK.

  g. Navigate to Certificates > SMS > Certificates.

  h. In the results pane, right-click each certificate listed under the Certificates > SMS >
     Certificates node, and then select Delete. Repeat this step until all certificates are
     deleted.

   i. Close the Certificates console.

9. Delete the record of the offending computer from the Configuration Manager console.
  Again, you do not have to go into the SQL Server database to do this. You can delete the
  record from the Configuration Manager console. Make sure that you do this after you
  complete steps 1-8. Doing this first may cause the record to be recreated if the client
  reports are backed up before they are fully cleaned.

<!-- p.466 -->

 10. Reinstall the Configuration Manager client on the offending client computer.

Remove duplicate Unknown Computer objects
If the Unknown Computer objects have been recreated at the site when you tried to fix the
problem, the extra Unknown Computer objects should be deleted. To accomplish this, all of the
current Unknown Computer objects should be deleted for the affected site followed by
creating a brand new set of Unknown Computer objects for the site. Deleting Unknown
Computer objects can be completed only from the SQL Server database. It cannot be done
from the Configuration Manager console.

  ７ Note

  It's acceptable to have multiple Unknown Computer objects if there are multiple primary
  sites. However, each site should have only one Unknown Computer object per
  architecture. For example, there should be only one x64 object that's labeled x64
  Unknown Computer and only one x86 object that's labeled x86 Unknown Computer.

To delete the extra Unknown Computer objects, follow these steps:

   1. Make sure you have a current and valid backup of the Configuration Manager site by
     using the built-in Backup maintenance task.

   2. Open the Configuration Manager console. If there are multiple primary sites, we
     recommend that you open a Configuration Manager console that's connected to the
     central administration site.

   3. In the Configuration Manager console, go to Assets and Compliance > Overview >
     Device Collections.

   4. Double-click the All Unknown Computers collection.

   5. In the results pane, sort the objects in the All Unknown Computers collection by
     selecting the Site Code column.

   6. Note whether there are multiple x64 Unknown Computer objects or x86 Unknown
     Computer objects for any individual site.

   7. If there are multiple x64 Unknown Computer objects or x86 Unknown Computer objects
     for any individual site, right-click the columns in the results pane, and add Resource ID to

<!-- p.467 -->

   the list of columns.

 8. Determine the Resource ID value for each x64 Unknown Computer object and each x86
   Unknown Computer object for any one site. Make sure to note the resource ID for all of
   the Unknown Computer objects even if only one of the Unknown Computer objects is
   duplicated.

 9. After you determine the Resource IDs of the Unknown Computer objects for a site, the
   x64 Unknown Computer objects and the x86 Unknown Computer objects for the site
   can be deleted.

10. Open SQL Server Management Studio, and then connect to the database for the site that
   hosts the extra Unknown Computer objects.

11. Expand the Databases node, and select the Configuration Manager database (usually
   CM_Site_Code).

12. On the toolbar, select New Query.

13. Make sure that the correct database is selected in the drop-down menu to the left of the
   Execute button on the toolbar.

14. In the query pane, run the following SQL query:

     SQL

     SELECT C.CollectionID, C.SiteID, C.CollectionName, CM.MachineID, CM.Name FROM
     Collections C JOIN CollectionMembers CM ON C.SiteID = CM.SiteID JOIN
     UnknownSystem_DISC USD ON USD.ItemKey = CM.MachineID

   This query displays all the collections that all the Unknown Computer objects belong to.
   Use this query to determine which collections the Unknown Computer objects are
   members of. Make a note of this information so that when the new set of Unknown
   Computer objects are created, they can be added back to the appropriate collections. The
   Resource ID is listed in the MachineID column.

15. In the query pane, run the following SQL query:

     SQL

     SELECT * FROM UnknownSystem_DISC WHERE ItemKey IN
     ('Resource_ID_1','Resource_ID_2', 'Resource_ID_3')

<!-- p.468 -->

   In this query, Resource_ID_x is the Resource ID of each of the Unknown Computer objects
   for the site, as determined in step 9. For example, if the Resource IDs are 2046820354
   and 2046820355, the query would be as follows:

     SQL

     SELECT * FROM UnknownSystem_DISC WHERE ItemKey IN ('2046820354','2046820355')

16. Verify that the records that are returned by the query in step 15 are correct. If they are,
   then run the following query to delete the records:

     SQL

     DELETE FROM UnknownSystem_DISC WHERE ItemKey IN
     ('Resource_ID_1','Resource_ID_2', 'Resource_ID_3')

   In this query, Resource_ID_x is the Resource ID of each of the Unknown Computer objects
   for the site, as determined in step 9. For example, if the Resource IDs are 2046820354
   and 2046820355, the delete query would be as follows:

     SQL

     DELETE FROM UnknownSystem_DISC WHERE ItemKey IN ('2046820354', '2046820355')

      ７ Note

      Remember to delete all of the Unknown Computer objects for the affected site, both
      x64 and x86, even if only one of them was duplicated.

17. Follow the section Recreate Unknown Computer objects in case of accidental deletion to
   create new Unknown Computer objects for the affected site.

18. Return to the Configuration Manager console, and then go to Assets and Compliance >
   Overview > Device Collections.

19. Right-click the All Unknown Computers collection, and then select Update Membership.

20. Wait a few minutes, and then select Refresh. Verify that only one x64 Unknown
   Computer object or x86 Unknown Computer object exists for each site. If the objects do
   not display, wait a few more minutes and try again.

<!-- p.469 -->

 21. Once the new Unknown Computer objects appear, add them back to the appropriate
     collections as determined in step 14.

 22. Repeat steps 10-21 for all additional primary sites, as necessary.

Recreate Unknown Computer objects in case of
accidental deletion
If, for whatever reason, all Unknown Computer objects are accidentally deleted for any one site
that uses this process, they can be recreated by using the following steps. These steps should
be taken only if there are no Unknown Computer objects for a site. If only one of the two
Unknown Computer objects exists at a site, delete the one remaining Unknown Computer
object by using the steps in the Remove duplicate Unknown Computer objects section of this
article, and then follow these steps:

   1. Sign in to the primary site server that the Unknown Computer objects are missing from.

   2. At an elevated command prompt, run the following command:

       Console

       REG.exe ADD
       "HKLM\SOFTWARE\Microsoft\SMS\COMPONENTS\SMS_DISCOVERY_DATA_MANAGER" /v
       CreatedUnknownDDR /t REG_DWORD /d 0 /f

After this registry key value is updated, the Unknown Computer objects should be
automatically recreated soon afterward. You can check the progress of the creation of the
Unknown Computer objects in the DDM.log file on the primary site server.

To speed up the recreation of the Unknown Computer records, restart the
SMS_DISCOVERY_DATA_MANAGER thread by following these steps:

   1. Open the Configuration Manager console on the primary site from which the Unknown
     Computer objects are missing, and then go to Monitoring > Overview > System Status >
     Component Status.

   2. On the toolbar, select Start > Configuration Manager Service Manager.

   3. In Configuration Manager Service Manager, expand the node under the site code and
     then select Components.

<!-- p.470 -->

   4. In the results pane, right-click SMS_DISCOVERY_DATA_MANAGER and select Query. The
      thread should display as Running.

   5. Right-click SMS_DISCOVERY_DATA_MANAGER, and then click Stop.

   6. Right-click SMS_DISCOVERY_DATA_MANAGER, and then click Query.

         ７ Note

         The thread should display as Stopped.

   7. Right-click SMS_DISCOVERY_DATA_MANAGER, and then click Start.

   8. Right-click SMS_DISCOVERY_DATA_MANAGER, and then click Query.

         ７ Note

         The thread should display as Running.

   9. Close the Configuration Manager Service Manager window.

The Unknown Computer objects should be automatically recreated soon. You can check the
progress of this process in the DDM.log file on the primary site server.

 Last updated on 03/30/2026

<!-- p.471 -->

An error occurred when loading the task
sequence when you create an MDT task
sequence
This article helps you fix an issue where you receive the An error occurred when loading the
task sequence error when you create a Microsoft Deployment Toolkit (MDT) task sequence in
Configuration Manager.

Original product version: Configuration Manager
Original KB number: 2468097

Symptoms
After selecting the Finish button when attempting to create an MDT task sequence, the task
sequence may fail to create with the following error:

  An error occurred when loading the task sequence

The TaskSequenceProvider.log file may also show errors similar to the following:

  Failed to load class properties and qualifiers for class BDD_UsePackage in task sequence.
  0x80041002 (2147749890) TaskSequenceProvider
  Failed to load node Use Toolkit Package from XML into WMI 0x80041002 (2147749890)
  TaskSequenceProvider
  Failed to load children steps for node "Execute Task Sequence" from XML 0x80041002
  (2147749890) TaskSequenceProvider
  Failed to load children steps for node "" from XML 0x80041002 (2147749890)
  TaskSequenceProvider
  Failed to load XML for the task sequence into WMI 0x80041002 (2147749890)
  TaskSequenceProvider

Cause
This error can occur if the MDT Windows Management Instrumentation (WMI) classes are not
properly registered.

<!-- p.472 -->

Resolution
To resolve this issue, follow the steps below:

   1. Close all of your remote and local Configuration Manager admin console sessions.
   2. Log on to your Configuration Manager server, in Microsoft Deployment Toolkit, select
      Configure ConfigMgr Integration.
   3. In the Configure ConfigMgr Integration wizard, select Remove the MDT console
      extensions for System Center Configuration Manager, click Next, then click Finish.
   4. Rerun Configure ConfigMgr Integration, select Install the MDT extensions for
      Configuration Manager, click Next, then click Finish.

Once you do the steps, try creating the task sequence again. It should now complete
successfully.

More information
This error occurs because the BDD_* WMI classes have not been correctly registered under the
\root\SMS\site_<sitecode> namespace in WMI.

 Last updated on 03/30/2026

<!-- p.473 -->

Can't create bootable media with errors
80004005 and 0x8004101d
Article • 05/20/2025

Applies to: Configuration Manager (current branch, version 2409)

Symptoms
In Microsoft Configuration Manager (current branch, version 2409), you can't create bootable
media when selecting a cloud management gateway for a management point.

The following error is logged in the SMSProv.log file:

  Output

  Failed to get MP installation directory path
  ~*~*~D:\dbs\sh\cmgm\1213_044837_0\cmd\1b\src\SiteServer\SDK_Provider\SMSProv\sspts
  package.cpp(3101) : GetTSMediaAdditionalInfo failed due to error 80004005
  ~*~*~GetTSMediaAdditionalInfo failed due to error 80004005

Additionally, the following error is logged in the CreateTSMedia.log file:

  Output

  Error invoking WMI method SMS_TaskSequencePackage.GetTSMediaAdditionalInfo
  (0x8004101d)
  StageCertificate::RetrieveTokenForMediaCert() failed. 0x8004101d

Cause
This issue occurs because the SMS provider isn't in the same location as the management
point. In Configuration Manager (current branch, version 2409), the system checks the location
of the management point and attempts to use the DLLs available in that location.

Workaround
Since a management point can't be hosted on a central administration site, you need to create
the bootable media on a primary site. Additionally, ensure that all Configuration Manager
providers are in the same location as the management point.

<!-- p.474 -->

Status
Microsoft is working on a resolution and will update this article when it's available.

<!-- p.475 -->

Computer hangs at the Just a moment
screen in a debug deployment of an OSD
task sequence
This article fixes an issue in which a computer appears to hang during an OSD task sequence
running in debug mode.

Original product version: Configuration Manager (current branch)
Original KB number: 4517137

Symptoms
You run a debug deployment of an Operating System Deployment (OSD) task sequence that
deploys Windows 10 in Configuration Manager. After the task sequence restarts out of WinPE
and into the full OS, the device hangs for a long time at the Just a moment screen during
Windows Setup.

Cause
This issue typically occurs if the Step option of the task sequence debugger is used from the
Setup Windows and ConfigMgr task or if a break point is set after the Setup Windows and
ConfigMgr task.

After Windows Setup is completed, the OSD task sequence is restarted by using the
SetupComplete.cmd script. Current versions of Windows 10 hide programs and do not
interactively display them when they are started through the SetupComplete.cmd script. This
behavior causes anything that the task sequence tries to display to be hidden instead. This
includes the task sequence debugger and any task sequence progress bars.

In this situation, the task sequence does continue, and the debugger does start. However, the
debugger is hidden and cannot be seen. Only the Just a moment screen is visible. This makes it
appear as though Windows Setup is still running.

After the first restart after SetupComplete.cmd initially runs, programs are shown interactively
and are no longer hidden. At this point, the task sequence debugger and progress bars are visibly
displayed.

<!-- p.476 -->

Resolution
To resolve the issue, follow these steps:

   1. Add a Restart Computer task immediately after the Setup Windows and ConfigMgr task.
      Make sure that the Restart Computer task is set to the The currently installed default
      operating system option.

   2. Set any necessary break points by following these guidelines:

            Do not set a break point on the Restart Computer task that you added in step 1.
            Instead, set break points after the Restart Computer task, as appropriate.
            Do not use the Step option in the task sequence debugger at the Setup Windows and
            ConfigMgr task. Instead, set a break point to the task after the Restart Computer task,
            and then select the Run option when you're ready to continue.

References
For more information about the task sequence debugger, see Debug a task sequence. For more
information about the SetupComplete.cmd script file, see Add a Custom Script to Windows
Setup.

 Last updated on 06/25/2026

<!-- p.477 -->

Dynamic Media can't get management
point locations when Task Sequence
Wizard runs in Windows PE
This article fixes an issue in which Dynamic Media in Configuration Manager cannot get
management point locations when the Task Sequence Wizard runs in Microsoft Windows
Preinstallation Environment (Windows PE).

Original product version: Configuration Manager (current branch), Microsoft System Center
2012 R2 Configuration Manager
Original KB number: 4471115

Symptoms
You use Dynamic Media in Configuration Manager. When the Task Sequence Wizard first starts
in Windows PE, the initial communication to the management point to sync the time settings is
successful, as shown in the following SMSTS.log entry:

  TSMBootstrap Getting MP time information
  TSMBootstrap Set authenticator in transport
  TSMBootstrap Requesting client identity
  TSMBootstrap Setting message signatures.
  TSMBootstrap Setting the authenticator.
  TSMBootstrap CLibSMSMessageWinHttpTransport::Send: URL:MP_ServerCCM_POST
  /ccm_system/request
  TSMBootstrap Request was successful.

However, the later request to the management point to get location information fails, as shown
in the following SMSTS.log entry:

  TSMBootstrap IP: 192.168.0.100 192.168.0.0
  TSMBootstrap CLibSMSMessageWinHttpTransport::Send: URL: MP_Server GET
  /SMS_MP/.sms_aut?MPLOCATION&ir=192.168.0.100&ip=192.168.0.0
  TSMBootstrap Error. Status code 500 returned
  TSMBootstrap XML parsing error at line 1 char 11: DTD is prohibited.

<!-- p.478 -->

  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
  TSMBootstrap bSuccess == ((VARIANT_BOOL)-1), HRESULT=80004005
  (e:\CM1706_RTM\sms\common\inc\ccmxml.h,1151)
  TSMBootstrap oXMLDoc.loadFromXML( sReply.c_str()), HRESULT=80004005
  (e:\cm1706_rtm\sms\framework\osdmessaging\libsmsmessaging.cpp,5767)
  TSMBootstrap Error loading from XML
  TSMBootstrap CCM::SMSMessaging::CLibSMSMPLocation::RequestMPLocation failed;
  0x80004005
  TSMBootstrap MPLocation.RequestMPLocation (szTrustedRootKey, sIPSubnets.c_str(),
  sIPAddresses.c_str(), httpS, http), HRESULT=80004005
  (e:\cm1706_rtm\sms\framework\osdmessaging\libsmsmessaging.cpp,10164)
  TSMBootstrap CCM::SMSMessaging::GetMPLocations failed; 0x80004005
  TSMBootstrap Failed to query MP_Server for MP location

  ７ Note

  The IP addresses in the first line of this log entry are the IP addresses of the client
  computer and its subnet.

If multiple management points are defined in the Dynamic Media, the same failure occurs
regardless of which management point Configuration Manager tries to communicate with. If
you try to use the same URL in a browser, as in the following example, this also causes a 500
error:

http://MP_Server/SMS_MP/.sms_aut?MPLOCATION&ir=192.168.15.100&ip=192.168.0.0

The Internet Information Services (IIS) logs on the management point do not reveal a matching
500 error entry. Instead, a 200 success entry is displayed. If you enable Failed Request Tracing
in IIS for the 500 error message, you find the following error message:

  CALL_ISAPI_EXTENSION DllName="MP_Install_Directory\getauth.dll"
  MODULE_SET_RESPONSE_ERROR_STATUS
  Warning ModuleName="IsapiModule", Notification="EXECUTE_REQUEST_HANDLER",
  HttpStatus="500", HttpReason="Internal Server Error", HttpSubStatus="0", ErrorCode="The
  operation completed successfully.
  (0x0)", ConfigExceptionInfo=""

<!-- p.479 -->

For more information about how to enable failed request tracing in IIS for 500 error messages,
see the Troubleshooting Failed Requests Using Tracing in IIS 8.5.

The MP_GetAuth.log file on the management point shows the following error entry that was
logged when the client made the request that's recorded in the SMSTS.log:

  MP_GetAuth_ISAPI MP GA Number of MPs in the Site = <Number_Of_MPs_At_Site>
  MP_GetAuth_ISAPI MP GA: Actual Auth Reply Body :
  <MPList><XML_List_Of_MPs_At_Site></MPList>
  MP_GetAuth_ISAPI MP GA: GetAuthSendResponseHeaders: Sending response 200 OK
  MP_GetAuth_ISAPI MP GA: GetAuthDoneWithSession: ServerSupportFunction() returned
  0x0
  MP_GetAuth_ISAPI MP GA: HttpExtensionProc:GetAuthProcessRequest() returned 1
  MP_GetAuth_ISAPI MP GA: Query String Before Decode : MPLOCATION&ir=
  192.168.0.100&ip=192.168.0.0
  MP_GetAuth_ISAPI MP GA: Query String After Decode : MPLOCATION&ir=
  192.168.0.100&ip=192.168.0.0
  MP_GetAuth_ISAPI MP GA: Auth Request Type is MPLOCATION&ir=
  192.168.0.100&ip=192.168.0.0
  MP_GetAuth_ISAPI No more rows.
  MP_GetAuth_ISAPI No more rows.
  MP_GetAuth_ISAPI Formatted string exceeded max buffer size. Result is truncated.
  MP_GetAuth_ISAPI m_docReply.LoadFromString (String (bstrMPLocationXML), false),
  HRESULT=8000ffff (e:\nts_sccm_release\sms\mp\isapi\getauth\getauth.cpp,994)
  MP_GetAuth_ISAPI hr, HRESULT=8000ffff
  (e:\nts_sccm_release\sms\mp\isapi\getauth\getauth.cpp,2124)
  MP_GetAuth_ISAPI AuthRequest.ProcessGETRequest(), HRESULT=8000ffff
  (e:\nts_sccm_release\sms\mp\isapi\getauth\getauth.cpp,98)
  MP_GetAuth_ISAPI MP GA: GetAuthSendResponseHeaders: Sending response 500 Internal
  Server Error
  MP_GetAuth_ISAPI MP GA: GetAuthDoneWithSession: ServerSupportFunction() returned
  0x0
  MP_GetAuth_ISAPI MP GA: HttpExtensionProc:GetAuthProcessRequest() returned 4

The issue doesn't occur for site-based media or the Preboot Execution Environment (PXE)
through Configuration Manager. However, the issue can occur if you use third-party PXE
solutions that can use Dynamic Media.

<!-- p.480 -->

Cause
This issue occurs because there are multiple Unknown Computer objects for a specific website,
and that site has several management points. This causes many results to be returned when
MPLOCATION is called and the GetMPLocationForIPSubnet stored procedure runs.

To run GetMPLocationForIPSubnet manually on the server that's running SQL Server through
SQL Management Studio, run the following query:

 SQL

 exec GetMPLocationForIPSubnet N'192.168.0.0'

In this scenario. this command returns several hundred rows. This large number of rows
exceeds the maximum buffer size. This, in turn, causes the 500 error message and also causes
MPLOCATION to fail.

Resolution
All sites should have only one Unknown Computer object per architecture. For example, there
should be only one x64 object that's labeled x64 Unknown Computer and only one x86 object
that's labeled x86 Unknown Computer. If a site has more than one Unknown Computer object
per architecture, the extra Unknown Computer objects should be deleted. Deleting extra
Unknown Computer objects can be done only from the SQL Server database. It cannot be done
from the Configuration Manager console.

  ７ Note

  Creating extra Unknown Computer objects to prevent the client computers from stealing
  the GUID of the Unknown Computer objects is not the correct method to fix this issue. For
  the correct method, see A client computer can steal the Configuration Manager GUID of
  an Unknown Computer object during imaging.

To delete the extra Unknown Computer objects, follow these steps:

   1. Make sure you have a current and valid backup of the Configuration Manager site by
     using the built-in Backup maintenance task.

   2. Open the Configuration Manager console. If there are multiple primary sites, we
     recommend that you open a Configuration Manager console that's connected to the
