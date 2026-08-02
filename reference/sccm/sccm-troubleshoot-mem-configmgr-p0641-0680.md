---
title: "Welcome — pages 641-680"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0641-0680
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0641-0680
family: sccm
documentKind: "doc"
abstract: "example: Output Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xd0007, IsComplete=1, Progress=1, Applicable=1) INFO: Waiting for CONFIGURATION_MANAGER_SERVICE to be ready to apply update: 3B7D84FA-ECCC-4EA0-B8AB-ABBDA1E88E0E CMUpdate upgrades itself to"
---

# Welcome — pages 641-680

<!-- p.641 -->

example:

 Output

 Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xd0007,
 IsComplete=1, Progress=1, Applicable=1)
 INFO: Waiting for CONFIGURATION_MANAGER_SERVICE to be ready to apply update:
 3B7D84FA-ECCC-4EA0-B8AB-ABBDA1E88E0E

CMUpdate upgrades itself to the new version, and logs entries that resemble the following
example:

 Output

 CONFIGURATION_MANAGER_UPDATE service is stopping...
 ...
 CONFIGURATION_MANAGER_UPDATE service is starting...
 Microsoft Microsoft Configuration Manager v5.00 (Build 9132)

CMUpdate looks for the service window that's configured for the site, and logs entries that
resemble the following example:

 Output

 There is no service window defined for the site server to apply the CM server
 updates.

Process step 2: CMUpdate verifies the state of the
update and redist content
CMUpdate verifies that the CMUStaging content is intact, and then reads the Update.map file.
It logs entries that resemble the following example:

 Output

 Checking if the CMU Staging folder already has the content extracted.
 Creating hash for algorithm 32780
 Staging folder has hash =
 6C3C912C1C79E3958A0D8EE7F306470A87058E5DC6936F3438BF812D367F976F
 Content is already found at the staging folder
 ...
 Successfully read file \\?\E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-
 ABBDA1E88E0E\SMSSetup\update.map
 Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xd0005,
 IsComplete=2, Progress=100, Applicable=1)

CMUpdate processes the redists, and creates an in-memory list of files to be copied. It logs
entries that resemble the following example:

 Output

 Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xd0006,
 IsComplete=1, Progress=1, Applicable=1)
 Found redist manifest E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-
 ABBDA1E88E0E\redist\ConfigMgr.Manifest.cab and set redist folder to
 E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-ABBDA1E88E0E\redist.
 INFO: Extracted file C:\Windows\TEMP\ConfigMgr.Manifest.xml
 INFO: Processing file group "Dot_Net_Framework"
 INFO: Processing file "NDP462-KB3151800-x86-x64-AllOS-ENU.exe"
 INFO: File will be downloaded from https://go.microsoft.com/fwlink/?LinkID=2171070.
 INFO: File for NDP462-KB3151800-x86-x64-AllOS-ENU.exe [.NET Framework Extended
 4.6.2 RTM] will be copied with file name: NDP462-KB3151800-x86-x64-AllOS-ENU.exe.
 ...
 Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xd0006,
 IsComplete=2, Progress=100, Applicable=1)

Process step 3: CMUpdate installs the update
At this point, the actual update starts. CMUpdate follows these steps:

<!-- p.642 -->

   1. Unpack and run the pre-upgrade SQL scripts from the \CMUStaging\<Update
     GUID>\redist\ConfigMgr.AutoUpgradeScripts.cab folder.
   2. Turn off SQL Server Service Broker.
   3. Stop the Configuration Manager services.
   4. Unload the WMI providers.
   5. Delete the SMSDBMON triggers.
   6. Save the site control settings.
   7. Update the Configuration Manager database.
   8. Update the SQL registry entries.
   9. Update the RCM registry entries.
 10. Install files, language packs, components, and controls.
 11. Update the site control settings.
 12. Configure SQL Server Service Broker.
 13. Start WMI, and then install services.
 14. Update the site table.
 15. Update the Admin console binaries.
 16. Turn on SQL Server Service Broker.

During this process, CMUpdate also copies the redists from the \CMUStaging\<Update
GUID>\redist` folder. CMUpdate uses the copied files to replace 0-byte placeholder files in the
\CMUStaging\<Update GUID>\SMSSetup\* folders.

CMUpdate logs entries that resemble the following example:

 Output

 INFO: Checking media: E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-
 ABBDA1E88E0E\SMSSetup\bin\x64\NDP462-KB3151800-X86-X64-ALLOS-ENU.EXE
 INFO: Verifying hash for file 'E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-
 ABBDA1E88E0E\SMSSetup\bin\x64\NDP462-KB3151800-X86-X64-ALLOS-ENU.EXE'
 Expected hash:B4CBB4BC9A3983EC3BE9F80447E0D619D15256A9CE66FF414AE6E3856705E237,
 Actual hash:E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855
 WARNING: File hash mismatch for E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-
 ABBDA1E88E0E\SMSSetup\bin\x64\NDP462-KB3151800-X86-X64-ALLOS-ENU.EXE
 INFO: Checking alternate path: E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-
 ABBDA1E88E0E\redist\NDP462-KB3151800-X86-X64-ALLOS-ENU.EXE
 INFO: Verifying hash for file 'E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-
 ABBDA1E88E0E\redist\NDP462-KB3151800-X86-X64-ALLOS-ENU.EXE'
 INFO: Verifying signature for file 'E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-
 B8AB-ABBDA1E88E0E\redist\NDP462-KB3151800-X86-X64-ALLOS-ENU.EXE'
 INFO: Found valid source in folder: 'E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-
 B8AB-ABBDA1E88E0E\redist\'
 INFO: Found valid source for external dependency file 'NDP462-KB3151800-X86-X64-
 ALLOS-ENU.EXE' at 'E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-
 ABBDA1E88E0E\redist\'
 This file E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-
 ABBDA1E88E0E\redist\NDP462-KB3151800-X86-X64-ALLOS-ENU.EXE will be copied from
 redist.
 e:\configmgr\bin\x64\ndp462-kb3151800-x86-x64-allos-enu.exe file version is up to
 date (4.6.1590.0).
 same version detected, and this file is flagged to compare signing timestamp.
 Per digital signature signing time E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-
 ABBDA1E88E0E\redist\NDP462-KB3151800-X86-X64-ALLOS-ENU.EXE file version is up to
 date per signing timestamp.
 File E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-B8AB-ABBDA1E88E0E\redist\NDP462-
 KB3151800-X86-X64-ALLOS-ENU.EXE has newer modification time than
 (e:\configmgr\bin\x64\ndp462-kb3151800-x86-x64-allos-enu.exe) but they have the
 same hash. It will be skipped.

Process step 4: CMUpdate updates the OSD
packages
After CMUpdate installs the files, it updates the OSD packages, and logs entries that resemble
the following example:

 Output

<!-- p.643 -->

 INFO: Adding default USMT package ...
 INFO: USMT package path is C:\Program Files (x86)\Windows Kits\10\Assessment and
 Deployment Kit\User State Migration Tool
 INFO: Adding Boot Image Packages, this may take some time...
 INFO: Attempting to export x86 boot image from ADK installation source
 INFO: Attempting to export x64 boot image from ADK installation source
 INFO: Attempting to export arm64 boot image from ADK installation source
 Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xd001a,
 IsComplete=3, Progress=100, Applicable=1)

Then, CMUpdate asynchronously waits for multiple processes (including SiteComp) to finish. It
logs entries that resemble the following example:

 Output

 ~      Starting ConfigMgr Update post installation monitor thread...

You can review other entries regarding component reinstallation in the SiteComp.log file.

Process step 5: CMUpdate updates CD.Latest
CMUpdate updates the CD.Latest file to reflect the new version of Configuration Manager. It
logs entries that resemble the following example:

 Output

 Creating cd backup location at E:\ConfigMgr\cd.latest
 Copying contents of update package from E:\ConfigMgr\CMUStaging\3B7D84FA-ECCC-4EA0-
 B8AB-ABBDA1E88E0E to E:\ConfigMgr\cd.latest
 ...
 successfully updated setup registry to have new external files stored at
 E:\ConfigMgr\cd.latest\redist

Finally, CMUpdate creates a notification file for HMAN that's named 196612.esc, and then
starts the post-installation tasks. It logs entries that resemble the following example:

 Output

 INFO: Successfully dropped update pack installed notification to HMAN CFD box.

Process step 6: Post installation tasks
CMUpdate performs the following post-installation tasks:

     1. Verify that the SMS_Executive service is installed.
     2. Verify that the SMSDBMon component is installed.
     3. Verify that the HMAN component is installed.
     4. Verify that the RCM component is installed.
     5. Monitor the start of replication.
     6. Update the Configuration Manager client preproduction package.
     7. Update the client folder on the site server.

HMAN performs the following post-installation tasks:

     1. Update the Configuration Manager client package.
     2. Turn on features that are specified in the upgrade or update wizard. Then, reopen the
       console to display the features.

  ７ Note

          Update.map contains the list of updates and files to be replaced and added. To
          review the list of files, open Update.map in Notepad.
          Install.map contains the list of steps that the installation process runs. It serves as a
          workflow for CMUpdate.exe that provides the steps and parameters to run in order.

<!-- p.644 -->

        For minor updates, check CMUpdate.log for details.

HMAN logs entries that resemble the following example:

 Output

 INFO: 196612.ESC file was found. Updating client packages. InteropMode = 0
 WARN: The current update package's state (196611) is not set to installed yet. Will
 retry in next cycle.
 ...
 INFO: 196612.ESC file was found. Updating client packages. InteropMode = 0
 Loaded client upgrade settings from DB successfully. FullClientPackageID=CS100004,
 StagingClientPackageID=CS100008, ClientUpgradePackageID=CS100005,
 PilotingUpgradePackageID=CS100009, ClientUpgradeAdvertisementID=CS120000,
 ClientPilotingAdvertisementID=(null)
 Client piloting is not enabled.
 Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xe0007,
 IsComplete=1, Progress=1, Applicable=1)
 ~Directory \\?\E:\ConfigMgr\StagingClient\i386 exists
 Copying ccmsetup from 'E:\ConfigMgr\CMUClient\CcmSetup.exe' to
 'E:\ConfigMgr\PilotingUpgrade\CcmSetup.exe'...
 ...
 Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xe0007,
 IsComplete=2, Progress=100, Applicable=1)
 ...
 Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xe0009,
 IsComplete=1, Progress=1, Applicable=1)
 Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xe0008,
 IsComplete=1, Progress=1, Applicable=1)
 Copying client binaries from 'E:\ConfigMgr\CMUClient' to 'E:\ConfigMgr\Client'...
 Copying ccmsetup from 'E:\ConfigMgr\CMUClient\ccmsetup.exe' to
 'E:\ConfigMgr\ClientUpgrade\ccmsetup.exe'...
 Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xe0009,
 IsComplete=2, Progress=100, Applicable=1)
 Successfully reported ConfigMgr update status (SiteCode=CS1, SubStageID=0xe0008,
 IsComplete=2, Progress=100, Applicable=1)

Results of the Installation stage
The console labels the update package as Installed. In the CM_UpdatePackages table, the state
value for the update package is 196612 .

  ７ Note

  Because of the Applicability checks, the console typically hides older update packages.

Troubleshoot the Installation stage
To review the status of the Installation stage, in the console, go to Administration > Overview
> Updates and Servicing. Alternatively, you can use the following SQL query to fetch update
package states for each a site:

 SQL

 -- Use Update GUID parameter for monitoring status query
 DECLARE @UpdateGUID UNIQUEIDENTIFIER = '<PACKAGE GUID>';

 select ServerData.SiteCode, cmupss.* from CM_UpdatePackageSiteStatus cmupss
 Left join serverdata on cmupss.SiteNumber=ServerData.ID
 where cmupss.PackageGUID = @UpdateGUID and cmupss.state<>196612

If the Installation stage is stuck in the Installing state or fails completely, go to Monitoring >
Overview > Updates and Servicing Status to review the update package state. You should be
able to identify the site that has an issue.

Use the following flow chart to help identify the issue.

<!-- p.645 -->

                                                                                               

The following issues can cause an update package to appear to be stuck during the Installation
stage:

     Installation is actually progressing. To review the current progress, see the CMUpdate.log
     file.
     The update content didn't finish replicating, or didn't replicate correctly. For assistance,
     see Troubleshoot the Replication stage earlier in this article.
     One of the sites is waiting for a service window. Make sure that the service window exists
     and is configured correctly.
     CMUpdate stopped. Therefore, the installation process can't continue.
     The update package content can't replicate between the CAS and the primary sites
     because of a Database Replication Service (DRS) issue.

Failures can occur at any step of the Installation stage. CMUpdate.log is the primary log to use
for investigating installation issues. However, if the failure occurs at any of the post-installation
steps, review the SiteComp.log file for information about component reinstallations and the
SMSExec.log file for information about component startup.

Case studies of Installation stage issues
Issue 1: "Error in verifying the trust of file
\\?...\CMUStaging\79FB5420-BB10-44FF-81BA-
7BB53D4EE22F\SMSSetup\update.map.cab"

In CMUpdate.log, you find an error entry that resembles the following example:

 Output

 update package content 79FB5420-BB10-44FF-81BA-7BB53D4EE22F has been expanded to
 folder \\?\...\CMUStaging\79FB5420-BB10-44FF-81BA-7BB53D4EE22F\
 Error in verifying the trust of file \\?\...\CMUStaging\79FB5420-BB10-44FF-81BA-
 7BB53D4EE22F\SMSSetup\update.map.cab.

This issue occurs because the files aren't downloaded correctly. To fix this issue, follow these
steps:

<!-- p.646 -->

   1. Verify the contents of EasySetupPayload folder: both Payload and Redists should have
        valid signatures. If it's necessary, switch the SCP to Offline mode.
   2. Run the RetryContentReplication WMI method. This method forces the Easy Setup
        Package to update. Wait for replication to finish.
   3. Try again to install the update.

Issue 2: Update installs on the CAS and primary sites, but console
still displays "Installing"

A specific global replication group, CMUpdates, replicates the installation completion
information one time per minute. If the replication process isn't working correctly, the console
continues to display Installing even if the update installed successfully on all sites.

In the console, go to Monitoring > Overview > Database Replication. For each link for the
CMUpdates replication group states, review the Initialization and Replication tabs. If you find
an issue, see Troubleshoot database replication service issues in Configuration Manager for
help.

Issue 3: CONFIGURATION_MANAGER_UPDATE service keeps
restarting

The CMUpdate process is the main driver of update package installation. It hosts the
CONFIGURATION_MANAGER_UPDATE service. If CMUpdate fails, the installation stops
responding at a specific stage, and CMUpdate.log might repeatedly record the same activity.
To investigate this issue, open Event Viewer, and review the Windows Application log for Event
ID 1000 (Process crash).

Security software can also cause this behavior by preventing the updated CMUpdate binary
from running, or by stopping the process. To investigate this issue, turn off the security
software, and then try again to update. If the issue persists, use the ProcDump tool to collect a
process memory dump file. Download and unpack the tool, and then run the following
command at a command prompt:

 Console

 procdump -ma -e cmupdate.exe

Create a support ticket, attach the dump file, and then submit it to Microsoft Support.

Issue 4: CMUpdate doesn't update the database objects

If this issue occurs, look for the following typical causes:

        Third-party objects in the Configuration Manager SQL Server database. Remove the third-
        party objects, and then install the update again.
        Third-party software that accesses the Configuration Manager SQL Server database, and
        locks first-party database objects. For example, an external Configuration Manager
        database might behave in this manner. Make sure that other software doesn't lock
        database objects while CMUpdate works in the database.

Reference
Relevant folders for installing Configuration
Manager updates
                                                                                             ﾉ    Expand table

 Folder                Location   Description

 \EasySetupPayload     SCP        This shared folder contains the actual installation files for an update.
                                  There's no Setup.exe file. Instead, an Install.map file is used for installing.

<!-- p.647 -->

 Folder               Location   Description

 \CMUStaging          Site       This folder contains unpacked Configuration Manager manifest CAB file
                      server     that HMAN downloaded and extracted to perform applicability checks.
                                 The installation files are temporarily stored in this folder while the
                                 update installs.

 \CMUClient           Site       This folder contains the latest client installation files. The files are copied
                      server     directly from the EasySetupPayload folder.

 \PilotingUpgrade     Site       This folder contains the source content for the Client Piloting Package.
                      server

 \ClientUpgrade       Site       This folder contains the source content for the Client Upgrade Package.
                      server

 \cd.latest           Site       This folder contains the latest version of the Configuration Manager
                      server     client installation files.

State codes and flags for update packages
The following table lists the state codes and the states that they represent.

                                                                                             ﾉ   Expand table

 State                                                                                      Value

 UNKNOWN                                                                                    0

 ENABLED                                                                                    2

 DOWNLOAD_IN_PROGRESS                                                                       262145

 DOWNLOAD_SUCCESS                                                                           262146

 DOWNLOAD_FAILED                                                                            327679

 APPLICABILITY_CHECKING                                                                     327681

 APPLICABILITY_SUCCESS                                                                      327682

 APPLICABILITY_HIDE                                                                         393213

 APPLICABILITY_NA                                                                           393214

 APPLICABILITY_FAILED                                                                       393215

 CONTENT_REPLICATING                                                                        65537

 CONTENT_REPLICATION_SUCCESS                                                                65538

 CONTENT_REPLICATION_FAILED                                                                 131071

 PREREQ_IN_PROGRESS                                                                         131073

 PREREQ_SUCCESS                                                                             131074

 PREREQ_WARNING                                                                             131075

 PREREQ_ERROR                                                                               196607

 INSTALL_IN_PROGRESS                                                                        196609

 INSTALL_WAITING_SERVICE_WINDOW                                                             196610

 INSTALL_WAITING_PARENT                                                                     196611

 INSTALL_SUCCESS                                                                            196612

 INSTALL_PENDING_REBOOT                                                                     196613

 INSTALL_FAILED                                                                             262143

 INSTALL_CMU_VALIDATING                                                                     196614

 INSTALL_CMU_STOPPED                                                                        196615

 INSTALL_CMU_INSTALLFILES                                                                   196616

<!-- p.648 -->

 State                                               Value

 INSTALL_CMU_STARTED                                 196617

 INSTALL_CMU_SUCCESS                                 196618

 INSTALL_WAITING_CMU                                 196619

 INSTALL_CMU_FAILED                                  262142

 INSTALL_INSTALLFILES                                196620

 INSTALL_UPGRADESITECTRLIMAGE                        196621

 INSTALL_CONFIGURESERVICEBROKER                      196622

 INSTALL_INSTALLSYSTEM                               196623

 INSTALL_CONSOLE                                     196624

 INSTALL_INSTALLBASESERVICES                         196625

 INSTALL_UPDATE_SITES                                196626

 INSTALL_SSB_ACTIVATION_ON                           196627

 INSTALL_UPGRADEDATABASE                             196628

 INSTALL_UPDATEADMINCONSOLE                          196629

The following table lists the available flags.

                                                         ﾉ   Expand table

 Flag                                            Value

 Normal installation                             0

 Prerequisite check only                         1

 Ignore warnings                                 2

 Last updated on 03/30/2026

<!-- p.649 -->

Configuration Manager clients don't get
software updates
This article fixes an issue in which Configuration Manager clients can't get updates from the
software update point.

Original product version: Configuration Manager (current branch - version 1702)
Original KB number: 4041012

Symptom
After installing Configuration Manager current branch version 1702, you may see the following
symptoms:

     Newly installed clients are unable to get updates from the software update point. This can
     also occur if the software update point is moved to a different server after installation of
     version 1702. With verbose client logging enabled, the LocationServices.log file contains
     an empty value for the WSUSLocationReply entry.
     Some computers show in the console as Unknown State.

Cause
Beginning with Configuration Manager current branch version 1702, clients use boundary
groups to find a new software update point, and to fallback and find a new software update
point if their current one is no longer accessible. If you install a new site that runs version 1702
or later, you must assign software update points to a boundary group before clients can find
and use them.

Resolution
Add the server running the software update point to the default site boundary group for the
clients. You can add individual software update points to different boundary groups to control
which servers a client can find. For more information, see software update points.

To add the software update point to the boundary group, follow these steps:

<!-- p.650 -->

  1. Create a boundary group if none exists, and add all the client machines to the boundary
     group with the software update point as the site server.
  2. Run Machine Policy Retrieval & Evaluation Cycle on the Configuration Manager.
  3. Check the LocationServices.log on a client machine to confirm the client can connect to
     the Windows Server Update Services (WSUS) server.

 ７ Note

 After doing this, you may experience some temporary timeouts if a large number of
 clients attempts to connect to the WSUS server. This can also cause high CPU usage on
 the WSUS server. As the clients connect CPU usage should return to normal. If the high
 CPU usage persists after all clients are connected, see Troubleshoot high CPU usage on a
 WSUS server.

Last updated on 03/30/2026

<!-- p.651 -->

Implement a shared SUSDB for
Configuration Manager software
update points

Summary
In a Configuration Manager site with multiple software update points (SUPs), each SUP uses a
WSUS database (SUSDB) to store update metadata. By default, each SUP maintains its own
SUSDB, which means clients perform a full metadata scan - potentially transferring more than 1
GB of data - every time they switch between SUPs.

A shared SUSDB lets multiple SUPs in the same site point to a single database. When clients
switch between SUPs that share a SUSDB, they perform delta scans instead of full scans, which
significantly reduces network overhead and speeds up compliance reporting.

This article explains how to:

      Prepare a shared content location and install the WSUS role for shared SUSDB use
      Run post-installation tasks and verify the configuration
      Install and configure the Configuration Manager SUP role
      Troubleshoot common issues, including content directory access failures and
      synchronization errors

For more information, see Use a shared WSUS database for software update points and Capacity
limits.

Install and configure WSUS for a shared SUSDB
Requirements
For architecture and planning guidance, see Best practices for software updates in Configuration
Manager and Plan for software updates in Configuration Manager.

All front-end WSUS servers that share a SUSDB should have:

   1. The same WSUS version.
   2. The same Windows Server version and patch level.

<!-- p.652 -->

   3. The same access requirements configuration for synchronization with Microsoft Update.
   4. A maximum of four SUPs sharing the same SUSDB.

For example, if you plan to have seven SUPs in your primary site, four can share one SUSDB. The
remaining three can share a different SUSDB or use separate databases.

Also verify SQL requirements in Size and scale numbers for Configuration Manager.

  ） Important

       WID (Windows Internal Database) isn't supported for this shared SUSDB design.
       Use a shared WSUS content path (UNC share or DFS path), and grant WSUS computer
       accounts Change permissions.
       The shared SUPs must belong to the same primary site code. You can't share a SUP
       installed under the central administration site (CAS) with one from a primary site, or a
       SUP from a primary site with one from a secondary site.

Prepare a shared content location
Create one shared content location for all WSUS front-end servers that use the same SUSDB.

   1. Create a file location for WSUS content that all clients can access. Use either of the following
     options:

              A standard SMB share backed by resilient storage (for example, RAID).
              A DFS namespace or path.

   2. Grant permissions at both the share and NTFS levels:

              Grant Change permissions to each WSUS front-end server computer account
              ( WSUSServer$ ) that uses the shared content location. If the share is local to the WSUS
              server, use the Network Service account.
              Grant Change permissions to the administrator account that runs WsusUtil.exe
              postinstall .

   3. Use a single UNC path for all nodes, and keep it consistent in setup and post-install
     commands. Example:

       text

<!-- p.653 -->

      \\FileServer\WSUS

  4. Validate access from every WSUS front-end server before installing the role:

          Browse the UNC path from each server.
          Create and delete a temporary test file or folder.

Install the WSUS role
You can install WSUS from Server Manager or PowerShell. For more information, see Getting
started with WSUS.

  1. Open Server Manager, select Manage, and then select Add roles and features.

  2. In Server Roles, select Windows Server Update Services.

<!-- p.654 -->

3. Accept the required features and continue to Role Services.

4. Clear WID Database and select SQL Server Connectivity.

<!-- p.655 -->

5. Specify the shared content path: \\FileServer\WSUS (or your UNC path) and select Next.

6. Specify the SQL Server (and instance if applicable), and then select Check connection.

<!-- p.656 -->

  7. Select Next, proceed to the Install screen, and complete the installation.

Run post-installation tasks
Run WsusUtil.exe from the command line to configure shared settings directly.

Option 1: WSUS console

<!-- p.657 -->

Option 2: Server Manager notification

Option 3 (recommended): WsusUtil.exe command line. Open PowerShell as an administrator
and run:

 PowerShell

 cd "C:\Program Files\Update Services\Tools"
 .\WsusUtil.exe postinstall SQL_INSTANCE_NAME="SQLServer\Instance"
 CONTENT_DIR="\\FileServer\WSUS"

  ７ Note

       Keep .\ in front of WsusUtil.exe when running it in PowerShell.
       For a default SQL instance, use the server name only.

Repeat on other nodes and configure SSL if needed
Repeat this WSUS setup on each additional front-end WSUS server for the same site.

<!-- p.658 -->

For SSL, see Configure a software update point to use TLS/SSL with a PKI certificate. SSL isn't
required, but if you use it, configure it consistently on all WSUS servers.

Verify the WSUS installation
   1. Open Windows Server Update Services (WSUS) from the Start menu. The Configuration
     Wizard opens the first time. Cancel it, and then confirm that you can browse nodes without
     errors.

   2. In IIS, right-click the Content virtual directory, select Manage Virtual Directory, and then
     select Advanced Settings.

<!-- p.659 -->

3. Validate the physical path format. Confirm that the UNC path starts with \\ .

  Incorrect example:

<!-- p.660 -->

Correct example:

<!-- p.661 -->

4. Validate the registry values under HKLM\Software\Microsoft\Update Services\Server\Setup .

<!-- p.662 -->

     Check these values:

                                                                                       ﾉ    Expand table

      Value                          Requirement

       ContentDir                    Same content path used during the post-install task.

       IISTargetWebsiteIndex         IIS site ID, used in default IIS log naming.

       PortNumber                    Usually 8530 (HTTP) or 8531 (HTTPS).

       SQLDatabaseName               Always SUSDB .

       SQLServerName                 SQL server and instance if used.

       UsingSSL                       0 for HTTP, 1 for HTTPS.

  ２ Warning

  The ContentDir registry value doesn't include the trailing WSUSContent\ directory. SQL
  LocalContentCacheLocation and the IIS Content virtual directory Physical path do include it.

   1. Optionally, verify the content path from SQL:

       SQL

       select LocalContentCacheLocation from tbConfigurationB

Install the Configuration Manager software update
point role
Install SUP roles by using Install and configure a software update point.

   1. Choose which SUP to install first.

   2. Add the SUP role. Create a new site system server, or add the role to an existing site system
     server.

<!-- p.663 -->

Configure the proxy and credentials if needed:

Select Software Update Point:

Set ports to match WSUS settings. Select Require SSL communication to the WSUS server
if WSUS is configured for SSL. You can adjust other options after the initial setup.

<!-- p.664 -->

   Complete the wizard with the additional proxy settings, if necessary.

 3. Monitor SUPSetup.log on the SUP server for the installation result.

Output

====================================================================
SMSWSUS Setup Started....
Parameters: E:\ConfigMgr\bin\x64\rolesetup.exe /install
/siteserver:SiteServer.contoso.com SMSWSUS 0
INFO: Checking MSODBC version on ServerName SUPServer
INFO: MSODBC version is 18.4.1.1
INFO: Microsoft ODBC 18 Driver for SQL Server had been installed already.
Installing Pre Reqs for SMSWSUS
        ======== Installing Pre Reqs for Role SMSWSUS ========
Found 0 Pre Reqs for Role SMSWSUS
        ======== Completed Installation of Pre Reqs for Role SMSWSUS ========
Installing the SMSWSUS
Checking for supported version of WSUS (min WSUS 4.0)
Checking runtime v4.0.30319...
Found supported assembly Microsoft.UpdateServices.Administration version 4.0.0.0, file
version 6.2.20348.1
Found supported assembly Microsoft.UpdateServices.BaseApi version 4.0.0.0, file
version 6.2.20348.143
Supported WSUS version found
Supported WSUS Server version (6.2.20348.143) is installed.

<!-- p.665 -->

 CTool::RegisterManagedBinary: run command line:
 "C:\Windows\Microsoft.NET\Framework64\v2.0.50727\RegAsm.exe"
 "E:\ConfigMgr\bin\x64\wsusmsp.dll"
 CTool::RegisterManagedBinary: Failed to register E:\ConfigMgr\bin\x64\wsusmsp.dll with
 .Net Fx 2.0
 CTool::RegisterManagedBinary: run command line:
 "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\RegAsm.exe"
 "E:\ConfigMgr\bin\x64\wsusmsp.dll"
 CTool::RegisterManagedBinary: Registered E:\ConfigMgr\bin\x64\wsusmsp.dll successfully
 Registered DLL E:\ConfigMgr\bin\x64\wsusmsp.dll
 Installation was successful.
 ~RoleSetup().

   1. Monitor WCM.log for the configuration refresh. If needed, restart the
     SMS_WSUS_CONFIGURATION_MANAGER component by using Configuration Manager Service

     Manager.

       Output

       Populating config from SCF
       Setting new configuration state to 1 (WSUS_CONFIG_PENDING)~
       Changes in active SUP list detected. New active SUP List is:~
           SUP0: SUPServer1.contoso.com, group = SUPServer1, nlb = ~
           SUP1: SUPServer2.contoso.com, group = SUPServer1, nlb = ~
       Updating active SUP groups...~

   2. Start synchronization, or wait for the scheduled synchronization cycle. Monitor
     WsyncMgr.log for completion.

       Output

       Starting Sync
       Performing sync on local request
       Read SUPs from SCF for SUPServer1.contoso.com
       Found 2 SUPs
       Found active SUP SUPServer1.contoso.com from SCF File.~
       Found active SUP SUPServer2.contoso.com from SCF File.~
       ...
       There are additional SUPs sharing the database with the default SUP
       SUPServer1.contoso.com, sync operations may use shared db SUPs.

Add additional SUPs for the same site. During initial setup, the source might temporarily show
Microsoft Update until upstream synchronization finishes.

Troubleshoot common issues with shared SUSDB

<!-- p.666 -->

Issue 1: WSUS front-end server can't access the shared
content directory
In Configuration Manager environments, update binaries typically aren't served from the WSUS
Content virtual directory in IIS, but End User License Agreement (EULA) files are. These files are

small text files that clients download during the update scan process. There's no requirement to
deploy an update that has EULA content to initiate this download.

A key indicator is a Configuration Manager client that reports a SucceededWithErrors scan result
code ( 0x80240033 ) during a software update scan. You can usually see this result in the built-in
reports under the "Software Updates – D Scan" category, such as "Scan 1 – Last scan states by
collection".

In Configuration Manager's WUAHandler.log on client devices, you see:

  Output

  Received 'SucceededWithErrors' code from WUA during search. Check WindowsUpdate.log in
  Windows directory.
  WU Agent reported the following 1 warning messages:
  HResult: 0x80240033 Context: uecGeneral Msg: The license terms of one or more updates
  are unavailable..

WindowsUpdate.log also reports the same error code:

  Output

  *FAILED* [80240033] ISusInternal:: GetEulaText

   Tip

  Use WsusUtil.exe checkhealth to validate the health of the WSUS server and its
  configuration. If accessing the shared content directory fails, the command produces an
  error event with ID 12072 in the Application event log similar to:

    Output

    The permissions on directory \\FileServer\WSUS\WsusContent are incorrect.

  or

    Output

<!-- p.667 -->

       The WSUS content directory is not accessible.

You can find more details in WindowsUpdate.log on the client and in IIS logs on the WSUS front-
end server. The following scenarios are common:

Scenario 1: The Content virtual directory is misconfigured

In this case, WindowsUpdate.log on the client shows:

  Output

  WARNING: Fail to download eula file
  http://SUPServer.contoso.com:8530/Content/AE/<file>.txt with error 0x80244019

This error code ( WU_E_PT_HTTP_STATUS_NOT_FOUND ) is also reflected in the IIS log for the WSUS
Administration website as HTTP 404 error for the same file:

  Output

  10.10.10.5 HEAD /Content/AE/<file>.txt 8530 - 10.10.10.221 Windows-Update-Agent - 404
  0 5 281

Fix:

Validate the Content virtual directory configuration for affected WSUS servers as described in
Verify the WSUS installation. A common mismatch is a local drive path on one server and the
shared UNC path on others. To resolve this mismatch:

   1. Run WsusUtil.exe postinstall again with the correct CONTENT_DIR pointing to the shared
        UNC path. For example:

         Output

         PS C:\Windows\system32> cd "C:\Program Files\Update Services\Tools"
         PS C:\Program Files\Update Services\Tools> .\WsusUtil.exe postinstall
         SQL_INSTANCE_NAME="SQLServer" CONTENT_DIR="\\FileServer\WSUS"
         Log file is located at
         C:\Users\admin\AppData\Local\Temp\WSUS_PostInstall_20260702T082349.log
         Post install is starting
         Post install has successfully completed

   2. Revalidate IIS, registry, and SQL path values as described in Verify the WSUS installation.

<!-- p.668 -->

   3. Run WsusUtil.exe reset to verify and redownload missing EULA content. It's sufficient to
       run this command on one of the WSUS servers sharing the same SUSDB.

        Output

        PS C:\Program Files\Update Services\Tools> .\WsusUtil.exe reset

   4. Confirm activity in SoftwareDistribution.log under C:\Program Files\Update
       Services\LogFiles resembling the following:

        Output

        TriggerEvent called for NotificationEventName: StateMachineReset, EventInfo:
        DispatchManager Worker Thread Processing NotificationEvent: StateMachineReset
        State Machine Reset Agent Starting
        ...
        State Machine Reset Agent Finished

Scenario 2: Misconfigured ACLs on the shared content directory

In this case, WindowsUpdate.log fails with a different error code:

  Output

  WARNING: WinHttp: SendRequestUsingProxy failed for
  http://SUPServer.contoso.com:8530/Content/AE/<file>.txt error 0x800710dd

IIS logs on the affected WSUS front-end server show HTTP 401.3 for the same file:

  Output

  10.10.10.5 HEAD /Content/AE/<file>.txt 8530 - 10.10.10.221 Windows-Update-Agent - 401
  3 5 281

These symptoms indicate authentication or permission issues when the Content virtual directory
tries to access the shared content location.

Fix:

Verify the ACLs on the shared content location and specifically on the
\\FileServer\WSUS\WSUSContent folder. Each WSUS front-end server computer account must have

Full Control permissions to the latter path at both the share and NTFS levels.

<!-- p.669 -->

After verifying permissions, re-run WsusUtil.exe checkhealth command on affected WSUS
servers to validate the content directory access.

Issue 2: Synchronization fails with generic network-related
errors or errors accessing Microsoft Update endpoints
When at least two SUPs share a SUSDB, you might see errors in WsyncMgr.log similar to the
following:

  Output

  Sync failed: UssCommunicationError: WebException: The remote name could not be
  resolved: 'sws.update.microsoft.com'~~at
  System.Net.HttpWebRequest.GetRequestStream(TransportContext& context). Source:
  Microsoft.SystemsManagementServer.SoftwareUpdatesManagement.WsusSyncAction.WSyncAction
  .SyncWSUS

  Output

  WebException: Unable to connect to the remote server --->
  System.Net.Sockets.SocketException: A connection attempt failed because the connected
  party did not properly respond after a period of time, or established connection
  failed because connected host has failed to respond (IP of Microsoft or Akamai)

This issue can occur when the master WSUS server changes and the new master doesn't meet the
same network access requirements for synchronization with Microsoft Update.

Configuration Manager assumes that the master is always the first SUP role installed in the
hierarchy, and it must match the output of the following WSUS command:

  Console

  Wsusutil.exe listfrontendservers

  Output

  C:\Program Files\Update Services\Tools>WsusUtil.exe listfrontendservers
  Server: SUPServer1.contoso.com, IsActive:True, IsMaster:True,
  LastContactedTime:7/2/2026 10:06:31 AM.
  Server: SUPServer2.contoso.com, IsActive:True, IsMaster:False,
  LastContactedTime:7/2/2026 10:06:35 AM.

Fix:

<!-- p.670 -->

Verify and configure network access requirements for synchronization with Microsoft Update on
all WSUS servers. For the complete list, see Internet endpoints for Configuration Manager.

As a temporary workaround (for example, if you can't immediately fix network configuration),
complete these steps to switch back to the original master WSUS/SUP server:

   1. Stop the WSUS service on all WSUS servers that don't meet internet access requirements
      while they share the same SUSDB.
   2. Trigger WSUS synchronization on the server that you want as the master front-end server.
      Verify the change by running Wsusutil.exe listfrontendservers again.
   3. After the sync starts, start the WSUS service on all other WSUS servers sharing the same
      SUSDB.

Related references
      Best practices for software updates in Configuration Manager
      Plan for software updates in Configuration Manager
      Install and configure a software update point
      Configure a software update point to use TLS/SSL with a PKI certificate
      Windows Server Update Services (WSUS) maintenance guide for Configuration Manager

）Note: The author created this article with assistance from AI. Learn more

 Last updated on 07/09/2026

<!-- p.671 -->

Windows Server Update Services best
practices
This article provides tips for avoiding configurations that experience poor performance
because of design or configuration limitations in WSUS.

Original product version: Configuration Manager (current branch), Windows Server Update
Services
Original KB number: 4490414

Capacity limits
Although WSUS can support 100,000 clients per server (150,000 clients when you use
Configuration Manager), we don't recommend approaching this limit.

Instead, consider using a configuration of 2-4 servers sharing the same SQL Server database.
This way you have safety in numbers. If one server goes down, it won't immediately spoil your
weekend because no client can update while you must be updated against the latest zero-day
exploit.

The shared database scenario also prevents a scan storm.

A scan storm can occur when many clients change WSUS servers and the servers don't share a
database. WSUS tracks activity in the database, so that both know what has changed since a
client last scanned and will only send metadata that's updated since then.

If clients change to a different WSUS server that uses a different database, they must do a full
scan. A full scan can cause large metadata transfers. Transfers of greater than 1 GB per client
may occur in these scenarios, especially if the WSUS server isn't maintained correctly. It can
generate enough load to cause errors when clients communicate with a WSUS instance. And
clients retry repeatedly in this case.

Sharing a database means when a client switches to another WSUS instance that uses the same
DB, the scan penalty isn't incurred. The load increases aren't the large penalty you pay for
switching databases.

Configuration Manager client scans put more demand on WSUS than the stand-alone
Automatic Updates. Configuration Manager, because it includes compliance checking, requests

<!-- p.672 -->

scans with criteria that will return all updates that are in any status except declined.

When the Automatic Updates Agent scans, or you select Check for Updates in Control Panel,
the agent sends criteria to retrieve only those updates Approved for Install. The metadata
returned will usually be less than when the scan is initiated by Configuration Manager. The
Update Agent does cache the data, and the next scan requests will return the data from the
client cache.

Disable recycling and configure memory limits
WSUS implements an internal cache that retrieves the update metadata from the database.
This operation is expensive and very memory intensive. It can cause the IIS application pool
that hosts WSUS (known as WSUSPool) to recycle when WSUSPool overruns the default private
and virtual memory limits.

When the pool recycles, the cache is removed and must be rebuilt. It isn't a large problem
when clients are undergoing delta scans. But if you end up in a scan storm scenario, the pool
will recycle constantly. And clients will receive errors when you make scan requests, such as
HTTP 503 errors.

We recommend that you increase the default Queue Length, and disable both the Virtual and
Private Memory Limit by setting them to 0. IIS implements an automatic recycling of the
application pool every 29 hours, Ping, and Idle Time-outs, all which should be disabled. These
settings are found in IIS Manager > Application Pools > choose WsusPool and then click the
Advanced Settings link in the right side pane of IIS manager.

Here's a summary of recommended changes, and a related screenshot. For more information,
see Plan for software updates in Configuration Manager.

                                                                                        ﾉ   Expand table

 Setting name                      Value

 Queue Length                      2000 (up from default of 1000)

 Idle Time-out (minutes)           0 (down from the default of 20)

 Ping Enabled                      False (from default of True)

 Private Memory Limit (KB)         0 (unlimited, up from the default of 1,843,200 KB)

 Regular Time Interval (minutes)   0 (to prevent a recycle, and modified from the default of 1740)

<!-- p.673 -->

In an environment that has around 17,000 updates cached, more than 24 GB of memory may
be needed as the cache is built until it stabilizes (at around 14 GB).

Check whether compression is enabled (if you want to
conserve bandwidth)

<!-- p.674 -->

WSUS uses a compression type calls Xpress encoding. It implements compression on update
metadata, and can result in significant bandwidth savings.

Xpress encoding is enabled in IIS ApplicationHost.config with this line under the
<httpCompression> element and a registry setting:

     ApplicationHost.Config

           <scheme name="xpress" doStaticCompression="false"
           doDynamicCompression="true" dll="C:\Program Files\Update
           Services\WebServices\suscomp.dll" staticCompressionLevel="10"
           dynamicCompressionLevel="0" />

     Registry key

      HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Update

     Services\Server\Setup\IIsDynamicCompression

If both aren't present, it can be enabled by running this command and then restarting the
WsusPool application pool in IIS.

 Console

 cscript "%programfiles%\update services\setup\DynamicCompression.vbs" /enable
 "%programfiles%\Update Services\WebServices\suscomp.dll"

Xpress encoding will add some CPU overhead, and can be disabled if bandwidth isn't a
concern, but CPU usage is. The following command will turn it off.

 Console

 cscript "%programfiles%\update services\setup\DynamicCompression.vbs" /disable

Configure products and categories
When you configure WSUS, choose only the products and categories that you plan to deploy.
You can always synchronize categories and products that you must have later. Adding them
when you don't plan to deploy them increases metadata size and overhead on the WSUS
servers.

<!-- p.675 -->

Disable Itanium updates and other unnecessary
updates
It shouldn't be an issue for much longer, because Windows Server 2008 R2 was the last version
to support Itanium. But it bears mentioning.

Customize and use this      script in your environment to decline Itanium architecture updates.
The script can also decline updates that contain Preview or Beta in the update title.

It leads to the WSUS console being more responsive, but doesn't affect the client scan.

Decline superseded updates and run maintenance
One of the most important things that you can do to help WSUS run better. Keeping updates
around that are superseded longer than needed (for example, after you're no longer deploying
them) is the leading cause of WSUS performance problems. It's ok to keep them around if
you're still deploying them. Remove them after you're done with them.

For information about declining superseded updates and other WSUS maintenance items, see
the Complete guide to Microsoft WSUS and Configuration Manager SUP maintenance
article.

WSUS with SSL setup
By default, WSUS isn't configured to use SSL for client communication. The first post-install
step should be to configured SSL on WSUS to make sure security between server-client
communications.

You must take one the following actions:

      Create a self-signed certificate. It isn't ideal because every client would have to trust this
      certificate.
      Obtain one from a third-party certificate provider.
      Obtain one from your internal certificate infrastructure.

Your certificate must have the short server name, FQDN, and SAN names (aliases) that it goes
by.

After you have the certificate installed, upgrade the Group Policy (or Client Configuration
settings for software updates in Configuration Manager) to use the address and SSL port of the

<!-- p.676 -->

WSUS server. The port is typically 8531 or 443.

For example, configure GPO Specify intranet Microsoft update service location to
< https://wsus.contoso.com:8531 >.

To get started, see Secure WSUS with the Secure Sockets Layer Protocol.

Configure Antivirus Exclusions
     Antivirus scans
     Microsoft Anti-Virus Exclusion List

About Cumulative Updates and Monthly Rollups
You may see the terms Monthly Rollups and Cumulative Update used for Windows OS
updates. They may be used interchangeably. Rollups refer to the updates published for
Windows 7, Windows 8.1, Windows Server 2008 R2, and Windows Server 2012 R2 that are only
partly cumulative.

For more information, see the following blog posts:

     Simplified servicing for Windows 7 and Windows 8.1: the latest improvements
     More on Windows 7 and Windows 8.1 servicing changes

With Windows 10 and Windows Server 2016, the updates were cumulative from the beginning:

     Windows 10 update servicing cadence

Cumulative means that: you install the release version of the OS, and only have to apply the
latest Cumulative Update to be fully patched. For the older operating systems, we don't have
such updates yet, although it's the direction we're heading in.

For Windows 7 and Windows 8.1, it means that after you install the latest monthly rollup, more
updates will still be needed. Here's an example for Windows 7 and Windows Server 2008 R2
on what it takes to have an almost fully patched system.

The following table contains the list of Windows Monthly Rollups and Cumulative Updates. You
can also find them by searching for Windows <version> update History.

                                                                               ﾉ   Expand table

<!-- p.677 -->

 Windows version                          Update

 Windows 7 SP1 and Windows Server 2008    Windows 7 SP1 and Windows Server 2008 R2 SP1 update
 R2 SP1                                   history

 Windows 8.1 and Windows Server 2012 R2   Windows 8.1 and Windows Server 2012 R2 update history

 Windows 10 and Windows Server 2016       Windows 10 and Windows Server update history

 Windows Server 2019                      Windows 10 and Windows Server 2019 update history

Another point to consider is that not all updates are published so that they sync automatically
to WSUS. For example, C and D week Cumulative Updates are preview updates and won't
synchronize to WSUS, but must be manually imported instead. See the Monthly quality
updates section of Windows 10 update servicing cadence .

Using PowerShell to connect to a WSUS server
Here's just a code example to get you started with PowerShell and the WSUS API. It can be
executed where the WSUS Administration Console is installed.

 PowerShell

 [void]
 [reflection.assembly]::LoadWithPartialName("Microsoft.UpdateServices.Administration
 ")
 $WSUSServer = 'WSUS'
 # This is your WSUS Server Name
 $Port = 8530
 # This is 8531 when SSL is enabled
 $UseSSL = $False
 #This is $True when SSL is enabled
 Try
 {
     $Wsus =
 [Microsoft.UpdateServices.Administration.AdminProxy]::GetUpdateServer($WSUSServer,$
 UseSSL,$Port)
 }
 Catch
 {
     Write-Warning "$($WSUSServer)<$($Port)>: $($_)"
     Break
 }

References
     SUS Blog

<!-- p.678 -->

     WSUS Product Team Blog

     The complete guide to Microsoft WSUS and Configuration Manager SUP maintenance

     How does Windows Update work?

     Introduction to WSUS and PowerShell

     Use PowerShell to Perform Basic Administrative Tasks on WSUS

     Approve or Decline WSUS Updates by Using PowerShell

     Use PowerShell to Find Missing Updates on WSUS Client Computers

     Get Windows Update Status Information by Using PowerShell

     Introduction to PoshWSUS, a Free PowerShell Module to Manage WSUS

     Use the Free PoshWSUS PowerShell Module for WSUS Administrative Work

     Download resources and applications for Windows, SharePoint, Office, and other
     products

     PowerShell UI used for auditing and installing updates from WSUS to local and remote
     systems

     PowerShell module to manage Windows Server Update Services (WSUS)

Last updated on 03/30/2026

<!-- p.679 -->

The complete guide to WSUS and
Configuration Manager SUP maintenance
This article addresses some common questions about WSUS maintenance for Configuration
Manager environments.

Original product version: Windows Servers, Windows Server Update Services, Configuration
Manager
Original KB number: 4490644

Introduction
Questions are often along the lines of How should I properly run this maintenance in a
Configuration Manager environment, or How often should I run this maintenance. It's not
uncommon for conscientious Configuration Manager administrators to be unaware that WSUS
maintenance should be run at all. Most of us just set up WSUS servers because it's a
prerequisite for a software update point (SUP). Once the SUP is set up, we close the WSUS
console and pretend it doesn't exist. Unfortunately, it can be problematic for Configuration
Manager clients, and the overall performance of the WSUS/SUP server.

With the understanding that this maintenance needs to be done, you're wondering what
maintenance you need to do and how often you need to be doing it. The answer is that you
should perform monthly maintenance. Maintenance is easy and doesn't take long for WSUS
servers that have been well maintained from the start. However, if it has been some time since
WSUS maintenance was done, the cleanup may be more difficult or time consuming the first
time. It will be much easier or faster in subsequent months.

For more information on concise steps and automatic scripts, see Manual and automatic WSUS
database maintenance.

Maintain WSUS while supporting Configuration
Manager current branch version 1906 and later
versions
If you are using Configuration Manager current branch version 1906 or later versions, we
recommend that you enable the WSUS Maintenance options in the software update point

<!-- p.680 -->

configuration at the top-level site to automate the cleanup procedures after each
synchronization. It would effectively handle all cleanup operations described in this article,
except backup and reindexing of WSUS database. You should still automate backup of WSUS
database along with reindexing of the WSUS database on a schedule.

For more information about software update maintenance in Configuration Manager, see
Software updates maintenance.

Important considerations

  ７ Note

  If you are utilizing the maintenance features that have been added in Configuration
  Manager, version 1906, you don't need to consider these items since Configuration
  Manager handles the cleanup after each synchronization.

   1. Before you start the maintenance process, read all of the information and instructions in
     this article.

   2. When using WSUS along with downstream servers, WSUS servers are added from the top
     down, but should be removed from the bottom up. When syncing or adding updates,
     they go to the upstream WSUS server first, then replicate down to the downstream
     servers. When performing a cleanup and removing items from WSUS servers, you should
     start at the bottom of the hierarchy.
