---
title: "Welcome — pages 481-520"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0481-0520
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0481-0520
family: sccm
documentKind: "doc"
abstract: "central administration site. 3. In the Configuration Manager console, go to Assets and Compliance > Overview > Device Collections. 4. Double-click the All Unknown Computers collection. 5. In the results pane, sort the objects in the All Unknown Computers collection by selecting"
---

# Welcome — pages 481-520

<!-- p.481 -->

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
   the list of columns.

 8. Determine the lowest Resource ID value for each x64 Unknown Computer object or each
   x86 Unknown Computer object for any one site. In most cases, for the first Primary site in
   an environment, the resource IDs for the original Unknown Computer objects for the sites
   will be 2046820352 (x86 Unknown Computer) and 2046820353 (x64 Unknown
   Computer).

 9. After you determine the lowest Resource ID, all other x64 Unknown Computer objects or
   x86 Unknown Computer objects for any site can be deleted. Note all the Resource IDs
   that can be deleted and which site they belong to.

10. Open SQL Server Management Studio, and then connect to the database for the site that
   hosts the extra Unknown Computer objects.

11. Expand the Databases node, and select the Configuration Manager database (usually
   CM_Site_Code).

12. On the toolbar, select New Query.

13. Make sure that the correct database is selected in the drop-down menu to the left of the
   Execute button on the toolbar.

14. In the query pane, run the following SQL query:

     SQL

<!-- p.482 -->

     SELECT C.CollectionID, C.SiteID, C.CollectionName, CM.MachineID, CM.Name FROM
     Collections C
     JOIN CollectionMembers CM ON C.SiteID = CM.SiteID
     JOIN UnknownSystem_DISC USD ON USD.ItemKey = CM.MachineID

   This query displays all the Collections that all the Unknown Computer objects belong to.
   Use this query to determine which collections the Unknown Computer objects that are
   being kept have to be added to. This should be based on the memberships of the
   Unknown Computer objects that are being deleted. The Resource ID is listed in the
   MachineID column.

15. In the query pane, run the following SQL query:

     SQL

     SELECT * FROM UnknownSystem_DISC WHERE ItemKey IN
     ('Extra_Resource_ID_1','Extra_Resource_ID_2', 'Extra_Resource_ID_3')

   In this query, Extra_Resource_ID_x is the Resource ID of each of the extra Unknown
   Computer objects, as determined in step 9. For example, if the extra Resource IDs are
   2046820354 and 2046820355, the query would be as follows:

     SQL

     SELECT * FROM UnknownSystem_DISC WHERE ItemKey IN ('2046820354','2046820355 ')

16. Verify that the records that are returned by the query in step 15 are correct. If they are,
   then run the following query to delete the records:

     SQL

     DELETE FROM UnknownSystem_DISC WHERE ItemKey IN
     ('Extra_Resource_ID_1','Extra_Resource_ID_2', 'Extra_Resource_ID_3')

   In this query, Extra_Resource_ID_x is the Resource ID of each of the extra Unknown
   Computer objects, as determined in step 9. For example, if the extra Resource IDs are
   2046820354 and 2046820355, the delete query would be as follows:

     SQL

     DELETE FROM UnknownSystem_DISC WHERE ItemKey IN ('2046820354', '2046820355')

<!-- p.483 -->

 17. Wait a few minutes, return to the Configuration Manager console, and then go to Assets
      and Compliance > Overview > Device Collections.

 18. Right-click the All Unknown Computers collection, and then select Update Membership.

 19. Wait a few minutes, and then select Refresh. Verify that only one x 64 Unknown
      Computer object or x86 Unknown Computer object exists for each site.

 20. Repeat steps 10-19 for all additional primary sites, as necessary.

Recreate Unknown Computer objects in case of
accidental deletion
For whatever reason, if all Unknown Computer objects are accidentally deleted for any one site
that uses this process, they can be re-created by using the following steps. These steps should
be taken only if there are no Unknown Computer objects for a site. If only one of the two
Unknown Computer objects exist at a site, delete the one remaining Unknown Computer
object by using the steps in Resolution, and then follow the steps in Recreate Unknown
Computer objects in case of accidental deletion.

The Unknown Computer objects should be automatically re-created soon. You can check the
progress of this process in the DDM.log on the primary site server.

 Last updated on 03/30/2026

<!-- p.484 -->

"Check online for updates from
Microsoft Update" option is unavailable
Article • 03/03/2025

Symptoms
After you upgrade an operating system to Windows 11, version 24H2 using a task
sequence in Configuration Manager, the Check online for updates from Microsoft
Update option becomes invisible and unavailable.

Cause
Before the upgrade, the task sequence engine enables the following local group policy
to prevent the client from connecting to Microsoft Update:

      Do not connect to any Windows Update Internet locations

        ７ Note

        The group policy is located under Local Computer Policy > Computer
        Configuration > Administrative Templates > Windows Components >
        Windows Update > Manage updates offered from Windows Server Update
        Service.

Once the upgrade is complete and the task sequence finishes, the task sequence
disables the group policy. This group policy is controlled by the following registry key:

      Registry key:
      HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate

      Value name: DoNotConnectToWindowsUpdateInternetLocations
      Value data:
         1 = Enabled
         0 = Disabled

However, when the registry value is set to 0 , the Check online for updates from
Microsoft Update option is hidden in Windows 11, version 24H2.

Resolution

<!-- p.485 -->

To resolve this issue, change the state of the local group policy to Not Configured,
which removes the registry value ( DoNotConnectToWindowsUpdateInternetLocations ).

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.486 -->

No mouse cursor appears during a
Configuration Manager OSD task sequence
Original product version: Configuration Manager
Original KB number: 4494800

This article fixes an issue in which no mouse cursor appears during a Configuration Manager
OS deployment (OSD) task sequence.

Symptoms
You're running a Configuration Manager OSD task sequence that deploys Windows 10. During
the Setup Windows and ConfigMgr task, the device restarts out of Windows PE and into the
newly installed Windows system. If you then open a Command Prompt window by pressing F8,
no mouse cursor appears. This issue continues to occur for the rest of the task sequence. After
the task sequence finishes, the mouse cursor appears.

Cause
This issue is caused by a design change in Windows 10 in which the mouse cursor is
suppressed during Windows Setup. Because Configuration Manager OSD task sequences run
entirely within Windows Setup in the newly installed Windows system, the mouse cursor is
suppressed during this phase of the task sequence.

Resolution
To resolve this issue, change the policy that suppresses the mouse cursor during Windows
Setup by default. This is easily accomplished by changing the registry key value that's
associated with the policy. The registry key value is located in the following subkey:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System

                                                                                    ﾉ   Expand table

 Value name                  Value type       Values

 EnableCursorSuppression     REG_DWORD        1 = Enabled: Mouse cursor is suppressed (default)

<!-- p.487 -->

 Value name                  Value type       Values

                                              0 = Disabled: Mouse cursor is not suppressed

To make sure that the mouse cursor is available throughout the task sequence, set this registry
key during the Windows PE portion of the task sequence to the offline Windows system. This
can be done at any point between the Apply Operating System and Setup Windows and
ConfigMgr tasks.

To make this change, use the following method to manually set the task sequence:

   1. In the Configuration Manager console under Software Library > Operating Systems >
     Task Sequences, navigate to the affected task sequence.

   2. Right-click the affected task sequence, and select Edit.

<!-- p.488 -->

3. In the affected task sequence, select the Apply Operating System task.

<!-- p.489 -->

4. Add a new group immediately after the Apply Operating System task. To do this, open
  the Add menu, and select New Group.

5. Select the newly created group, and rename it to Correct Missing Mouse Cursor.

<!-- p.490 -->

6. Under the Correct Missing Mouse Cursor group, add a Run Command Line task. To do
  this, open the Add menu, and then select General > Run Command Line.

<!-- p.491 -->

7. Select the newly created Run Command Line task, and specify the following values:

       Name: Load Registry SOFTWARE Hive

       Command line command:

       reg.exe load HKLM\Temp %OSDTargetSystemDrive%\Windows\system32\config\software

<!-- p.492 -->

8. Immediately after the Load Registry SOFTWARE Hive task, add another Run Command
  Line task. To do this, open the Add menu, and select General > Run Command Line.

<!-- p.493 -->

9. Select the newly created Run Command Line task, and specify the following values:

       Name: Disable Suppressed Mouse Cursor

       Command line command:

       reg.exe add "HKLM\Temp\Microsoft\Windows\CurrentVersion\Policies\System" /v

       EnableCursorSuppression /t REG_DWORD /d 0 /f

<!-- p.494 -->

10. Immediately after the Disable Suppressed Mouse Cursor task, add another Run
   Command Line task. To do this, open the Add menu, and select General > Run
   Command Line.

<!-- p.495 -->

11. Select the newly created Run Command Line task, and specify the following values:

        Name: Unmount Registry SOFTWARE Hive

        Command line command:

         reg.exe unload HKLM\Temp

<!-- p.496 -->

12. Select the last task in the task sequence.

   The last task in the task sequence may differ from the one that's shown in the screenshot.

<!-- p.497 -->

13. Add a Run Command Line task. To do this, open the Add menu, and then select General
   > Run Command Line. This should add the Run Command Line task as the last task in
   the task sequence.

<!-- p.498 -->

14. Select the newly created Run Command Line task and specify the following values:

        Name: Reset Mouse Suppression to Default

        Command Line:

         reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v

        EnableCursorSuppression /t REG_DWORD /d 1 /f

<!-- p.499 -->

15. Select the OK or Apply button to save the task sequence.

<!-- p.500 -->

 ７ Note

        For step 13, the last task that's selected does not necessarily have to be the absolute
        last task in the task sequence. However, it should be located toward the end of the
        task sequence.
        For MDT task sequences, steps 13-15 should be performed two times: One time at
        the end of the State Restore group, and again at the end of the Gather Logs and
        StateStore on Failure group. Additionally, on the Options tab of the the Reset
        Mouse Suppression to Default task that's added to the end of the Gather Logs and
        StateStore on Failure group, the Continue on error option should be selected.
        Steps 12-14 restore the EnableCursorSuppression policy to its default value in
        Windows. Although it's not required for the solution to work, we recommend that
        you reset the EnableCursorSuppression policy to its default value. This will make sure
        that there are no unusual consequences in Windows after the task sequence finishes
        changing the policy from its default value.

Last updated on 03/30/2026

<!-- p.501 -->

Sending with winhttp failed 80072f8f error
in Smsts.log during OS deployment by
using bootable or prestaged media
This article helps you fix an issue in which the Task Sequence Wizard returns error 80004005
and Smsts.log logs the Sending with winhttp failed; 80072f8f error during an OS deployment
that uses bootable or prestaged media.

Original product version: Configuration Manager (current branch), Microsoft System Center
2012 R2 Configuration Manager, Microsoft System Center 2012 Configuration Manager
Original KB number: 4551033

Symptoms
You create bootable media or prestaged media in Configuration Manager. When the media is
used to start the destination computer, the Task Sequence Wizard gets stuck at the Retrieving
policy for this computer step for about 90 seconds, then returns the following error message:

  Failed to Run Task Sequence
  An error occurred while retrieving policy for this computer (0x80004005). For more
  information, contact your system administrator or helpdesk operator.

The following error messages are logged in X:\Windows\Temp\SMSTSLog\smsts.log on the
computer when the task sequence engine first tries to contact the management point to sync
the time information:

  TSMBootstrap    Current time info:
  TSMBootstrap    Getting MP time information
  TSMBootstrap    Requesting client identity
  TSMBootstrap    Setting the authenticator.
  TSMBootstrap    CLibSMSMessageWinHttpTransport::Send: WinHttpOpenRequest - URL:
  <MP>:443 CCM_POST /ccm_system_AltAuth/request
  TSMBootstrap    SSL, using authenticator in request.
  TSMBootstrap    In SSL, but with no client cert.
  TSMBootstrap    [TSMESSAGING] AsyncCallback():

<!-- p.502 -->

  -----------------------------------------------------------------
  TSMBootstrap      [TSMESSAGING] AsyncCallback():
  WINHTTP_CALLBACK_STATUS_SECURE_FAILURE Encountered
  TSMBootstrap      [TSMESSAGING]                : dwStatusInformationLength is 4
  TSMBootstrap      [TSMESSAGING]                : *lpvStatusInformation is 0x8
  TSMBootstrap      [TSMESSAGING]             : WINHTTP_CALLBACK_STATUS_FLAG_INVALID_CA
  is set
  TSMBootstrap      [TSMESSAGING] AsyncCallback():
  -----------------------------------------------------------------
  TSMBootstrap      Error. Received 0x80072f8f from WinHttpSendRequest.
  TSMBootstrap      Sending with winhttp failed; 80072f8f. retrying.
  TSMBootstrap      Retrying and Ignoring date security failures.
  TSMBootstrap      [TSMESSAGING] AsyncCallback():
  -----------------------------------------------------------------
  TSMBootstrap      [TSMESSAGING] AsyncCallback():
  WINHTTP_CALLBACK_STATUS_SECURE_FAILURE Encountered
  TSMBootstrap      [TSMESSAGING]                : dwStatusInformationLength is 4
  TSMBootstrap      [TSMESSAGING]                : *lpvStatusInformation is 0x8
  TSMBootstrap      [TSMESSAGING]             : WINHTTP_CALLBACK_STATUS_FLAG_INVALID_CA
  is set
  TSMBootstrap      [TSMESSAGING] AsyncCallback():
  -----------------------------------------------------------------
  TSMBootstrap      hr, HRESULT=80072f8f
  TSMBootstrap      Sending with winhttp failed; 80072f8f

After the initial error, the task sequence engine tries an additional four times to contact the
management point, and experiences an increasing pause between each attempt. However, all
attempts fail and return the same error messages before some final error messages are
returned, as follows:

     If the media is configured as dynamic media, the following final error messages are
     logged in Smsts.log:

           TSMBootstrap   Send (pReply, nReplySize), HRESULT=80072f8f
           TSMBootstrap   failed to send the request
           TSMBootstrap   DoRequest (sReply, true), HRESULT=80072f8f
           TSMBootstrap   Failed to get client identity (80072f8f)
           TSMBootstrap   ClientIdentity.RequestClientIdentity (), HRESULT=80072f8f

<!-- p.503 -->

  TSMBootstrap     failed to request for client
  TSMBootstrap     SyncTimeWithMP() failed. 80072f8f.
  TSMBootstrap     Failed to get time information from MP: https://<MP> .
  TSMBootstrap     MpCnt > 0, HRESULT=80004005
  TSMBootstrap     QueryMPLocator: no valid MP locations are received
  TSMBootstrap     TSMBootstrapUtil::QueryMPLocator ( true,
  sSMSTSLocationMPs.c_str(), sMediaPfx.c_str(), sMediaGuid.c_str(),
  sAuthenticator.c_str(), sEnterpriseCert.c_str(), sServerCerts.c_str(), nHttpPort,
  nHttpsPort, bUseCRL, m_bWinPE, httpS, http, accessibleMpCnt), HRESULT=80004005
  TSMBootstrap     Failed to query Management Point locator
  TSMBootstrap     Exiting TSMediaWizardControl::GetPolicy.
  TSMBootstrap     pWelcomePage->m_pTSMediaWizardControl->GetPolicy(),
  HRESULT=80004005
  TSMBootstrap     Setting wizard error: An error occurred while retrieving policy for this
  computer (0x80004005). For more information, contact your system administrator or
  helpdesk operator.

If the media is configured as site-based, the following final error messages are logged in
Smsts.log:

  TSMBootstrap     Send (pReply, nReplySize), HRESULT=80072f8f
  TSMBootstrap     failed to send the request
  TSMBootstrap     DoRequest (sReply, true), HRESULT=80072f8f
  TSMBootstrap     Failed to get client identity (80072f8f)
  TSMBootstrap     ClientIdentity.RequestClientIdentity (), HRESULT=80072f8f
  TSMBootstrap     failed to request for client
  TSMBootstrap     SyncTimeWithMP() failed. 80072f8f.
  TSMBootstrap     Failed to get time information from MP: https://<MP> .
  TSMBootstrap     sMP.length() > 0, HRESULT=80004005
  TSMBootstrap     TSMBootstrapUtil::SelectMP ( sSMSTSMP.c_str(), sMediaPfx.c_str(),
  sMediaGuid.c_str(), sAuthenticator.c_str(), sEnterpriseCert.c_str(), sServerCerts.c_str(),
  nHttpPort, nHttpsPort, bUseCRL, m_bWinPE, sSiteCode, sAssignedSiteCode, sMP,
  sCertificates, sX86UnknownMachineGUID, sX64UnknownMachineGUID),
  HRESULT=80004005
  TSMBootstrap     Failed to select MP
  TSMBootstrap     Exiting TSMediaWizardControl::GetPolicy.
  TSMBootstrap     pWelcomePage->m_pTSMediaWizardControl->GetPolicy(),
  HRESULT=80004005

<!-- p.504 -->

        TSMBootstrap          Setting wizard error: An error occurred while retrieving policy for this
        computer (0x80004005). For more information, contact your system administrator or
        helpdesk operator.

The following detail information applies to error 80072F8F:

  Error Code: 0x80072F8F (2147954575)
  Error Name: WININET_E_DECODING_FAILED
  Error Source: Windows
  Error Message: Content decoding has failed

Cause
This issue occurs if the following conditions are true:

      You use PKI in your Configuration Manager environment.
      You create the bootable media or prestaged media at the central administration site.
      You configure your management points to use HTTPS.

If you use PKI in your Configuration Manager environment, the root certificate authority (CA) is
specified at the primary site but not at the central administration site. Because the central
administration site doesn't have the root CA information, the created media doesn't contain
the root CA information. Therefore, requests that are sent to an HTTPS-enabled management
point fail without the root CA information.

Resolution
To fix the issue, create the bootable media or prestaged media at a primary site instead of at
the central administration site.

More information
For media that will be used across multiple sites, configure the media as dynamic media. You
can create dynamic media at any site. You are not limited to creating it at the central
administration site.

 Last updated on 03/30/2026

<!-- p.505 -->

Task sequence fails in Configuration
Manager if software updates require
multiple restarts
This article provides the information to solve the issue that the Task Sequence environment
not found error occurs when using a Configuration Manager task sequence.

Original product version: Microsoft System Center 2012 Configuration Manager, Microsoft
System Center 2012 R2 Configuration Manager, Configuration Manager (current branch)
Original KB number: 2894518

Summary
The issue is fixed in Cumulative Update 3 for System Center 2012 Configuration Manager
Service Pack 2 and System Center 2012 R2 Configuration Manager Service Pack 1, and in
Configuration Manager current branch version 1602.

A new optional task sequence variable, SMSTSWaitForSecondReboot , is available to better control
client behavior when a software update installation requires two restarts.

For more information, see the Software updates management/operating system deployment
section in Description of Cumulative Update 3 for Configuration Manager       .

For Configuration Manager current branch, see Task sequence variables.

Symptoms
Assume that a Configuration Manager task sequence that uses the Install Software Updates
step installs a software update that triggers multiple restarts after the task sequence
successfully runs the Install Software Updates task. In this situation, the task sequence can fail
and generate the following error message:

  Task Sequence environment not found

  ７ Note

<!-- p.506 -->

  You can avoid this issue in Configuration Manager by using the new Retry option in the
  Install Software Updates task sequence step.

Cause
The first restart that is initiated by the software update is controlled by the task sequence.
However, the second restart request is initiated by a Windows component (typically,
Component-Based Servicing) and is not controlled by the task sequence. Therefore, the task
sequence execution state is not saved before the restart because the second restart is not
controlled by the task sequence. When the task sequence resumes after the second restart, no
state is available to continue successfully.

Resolution
To resolve this issue, we recommend that you apply any updates that require dual restarts by
using the usual software updates feature of Configuration Manager instead of using task
sequences. The following software updates were reported to require multiple restarts.

     3126446 MS16-017: Description of the security update for Remote Desktop display driver:
     February 9, 2016
     3096053 September 2015 servicing stack update for Windows 8 and Windows Server
     2012
     3075222 MS15-082: Description of the security update for RDP in Windows: August 11,
     2015
     3067904 MS15-082: Description of the security update for Windows RDP: July 14, 2015
     3069762 MS15-067: Description of the security update for Windows RDP: July 14, 2015
     3003729 April 2015 servicing stack update for Windows 8 and Windows Server 2012
     3035017 MS15-030: Description of the security update for Remote Desktop protocol:
     March 10, 2015
     3039976 MS15-030: Vulnerability in Remote Desktop protocol could allow denial of
     service: March 10, 2015
     3036493 MS15-030: Description of the security update for Remote Desktop protocol:
     March 10, 2015
     3003743 MS14-074: Vulnerability in Remote Desktop Protocol could allow security feature
     bypass: November 11, 2014
     2984976 RDP 8.0 update for restricted administration on Windows 7 or Windows Server
     2008 R2

<!-- p.507 -->

     2981685 Security updates cannot be installed if BitLocker is not installed on your
     computer
     2966034 Description of the security update for Remote Desktop Security Release for
     Windows 8.1 systems that do not have the 2919355 update installed: June 10, 2014
     2965788 MS14-030: Description of the security update for Remote Desktop Security
     Release for Windows: June 10, 2014
     2920189 Description of the update rollup of revoked noncompliant UEFI modules: May
     13, 2014
     2862330 MS13-081: Description of the security update for USB drivers: October 8, 2013
     2871777 A servicing stack update is available for Windows RT, Windows 8, and Windows
     Server 2012: September 2013
     2871690 Microsoft security advisory: Update to revoke noncompliant UEFI boot loader
     modules
     2821895 A servicing stack update is available for Windows RT and Windows 8: June 2013
     2771431 A servicing stack update is available for Windows 8 and Windows Server 2012
     2545698 Text in some core fonts appears blurred in Internet Explorer 9 on a computer
     that is running Windows Vista, Windows Server 2008, Windows 7, or Windows Server
     2008 R2
     2529073 Binary files in some USB drivers are not updated after you install Windows 7 SP1
     or Windows Server 2008 R2 SP1

More information
Because this second restart is not controlled by the task sequence, no execution state is saved
before the restart. When the task sequence resumes after the restart, no state is available to
continue successfully. Additionally, the following message may be logged to the Smsts.log file
when you experience this issue:

  !sVolumeID.empty(), HRESULT=80004005
  !sTSMDataPath.empty(), HRESULT=80070002
  TS::Utility::GetTSMDataPath( sDataDir ), HRESULT=80070002
  Failed to set log directory. Some execution history may be lost.
  The system cannot find the file specified. (Error: 80070002; Source: Windows)
  Executing task sequence
  !sVolumeID.empty(), HRESULT=80004005
  !sTSMDataPath.empty(), HRESULT=80070002
  Task Sequence environment not found

<!-- p.508 -->

Also, clients that are running release versions that are earlier than Microsoft System Center
2012 Configuration Manager Service Pack 1 may contain the following log entry:

  Task sequence completed in Windows PE.

The client computer may also be stuck in provisioning mode after the task sequence fails. To
determine whether the computer is in provisioning mode, check the
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\CCM\CcmExec registry subkey.

ProvisioningMode should be set to false. If it is set to true, use one of the following methods to

take the client out of provisioning mode:

      Use the Windows Management Instrumentation (WMI) method
      SetClientProvisioningMode to take the client out of provisioning mode correctly. The

      easiest way to do this is to run the following Windows PowerShell command:

        PowerShell

        Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name
        SetClientProvisioningMode -ArgumentList $false

      Or, run the following command at an elevated command prompt:

        Console

        powershell Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name
        SetClientProvisioningMode -ArgumentList $false

      Reinstall the client.

  ） Important

  Do not try to fix the client by changing the value of ProvisioningMode to false. This action
  will not fully take the client out of provisioning mode.

 Last updated on 03/30/2026

<!-- p.509 -->

Configuration Manager OSD task sequence
fails with error code 80070005
This article fixes an issue in which an OSD task sequence fails during the Setup Windows and
ConfigMgr step.

Original product version: Configuration Manager
Original KB number: 4509131

Symptoms
A Configuration Manager OSD task sequence fails during the Setup Windows and ConfigMgr
step when the step still runs in Windows PE.

The following error messages are logged in the X:\windows\temp\smstslog\smsts.log file:

  OSDSetupWindows Installing hook to 'C:\WINDOWS'
  OSDSetupWindows Command line for extension .EXE is "%1" %*
  OSDSetupWindows Set command line: "X:\sms\bin\x64\OSDSETUPHOOK.EXE"
  "/install:C:\WINDOWS" /version:10.0
  OSDSetupWindows Executing command line: "X:\sms\bin\x64\OSDSETUPHOOK.EXE"
  "/install:C:\WINDOWS" /version:10.0
  OSDSetupHook Installing OSD setup hook
  OSDSetupHook !shCmdFile.null(), HRESULT=80070005 (..\vistasetuphook.cpp,96)
  OSDSetupHook Failed to install the setup hook. Permissions on the requested may be
  configured incorrectly.
  Access is denied. (Error: 80070005; Source: Windows)
  OSDSetupHook pHook->install(sWindowsDir), HRESULT=80070005
  (..\osdsetuphook.cpp,385)
  OSDSetupHook Failed to install OSD setup hook (0x80070005)
  OSDSetupWindows Process completed with exit code 2147942405
  OSDSetupWindows exitCode, HRESULT=80070005 (setupwindows.cpp,785)
  OSDSetupWindows Install setup hook failed with error code (80070005).
  OSDSetupWindows this->installSetupHook(), HRESULT=80070005 (setupwindows.cpp,452)
  OSDSetupWindows Failed to install setup hook (80070005)
  OSDSetupWindows setup.run(), HRESULT=80070005 (setupwindows.cpp,1650)

<!-- p.510 -->

  OSDSetupWindows Exiting with code 0x80070005
  TSManager Process completed with exit code 2147942405
  TSManager !-----------------------------------------------------------------------!
  TSManager Failed to run the action: Setup Windows and ConfigMgr. Permissions on the
  requested may be configured incorrectly.
  Access is denied. (Error: 80070005; Source: Windows)

Here's the detail information about error code 80070005 (2147942405):

  Error Code: 0x80070005 (2147942405)
  Error Name: E_ACCESSDENIED
  Error Source: Windows
  Error Message: General access denied error

Cause
This issue occurs if a custom SetupComplete.cmd file is specified. OSD task sequences use the
SetupComplete.cmd file to continue the task sequence after Windows Setup finishes. If a
custom SetupComplete.cmd file is specified, the task sequence can't install its own
SetupComplete.cmd file. And it returns the Access is denied error. So custom
SetupComplete.cmd files aren't allowed with Configuration Manager OSD task sequences.

A custom SetupComplete.cmd file may be specified in one of the following ways:

     It's copied to the appropriate location in a task (usually a Run Command Line task)
     between the Apply Operating System and Setup Windows and ConfigMgr tasks. Below
     is an example of the command line in a Run Command Line task:

     cmd.exe /c copy SetupComplete.cmd %OSDTargetSystemDrive%\Windows\Setup\Scripts

     It's included as part of a custom OS WIM file.

The SetupComplete.cmd file is located in the %WINDIR%\Setup\Scripts folder, in either the
offline OS or the OS WIM image.

For more information about the SetupComplete.cmd file, see Add a Custom Script to Windows
Setup.

Resolution

<!-- p.511 -->

To fix this issue, remove the custom SetupComplete.cmd file. In most cases, any actions being
taken in the custom SetupComplete.cmd file can instead be moved as tasks in the task
sequence.

Depending on how the custom SetupComplete.cmd file is specified, use one of the following
methods to remove the file:

     If it's specified in a Run Command Line task between the Apply Operating System and
     Setup Windows and ConfigMgr tasks, remove the Run Command Line task from the task
     sequence.

     If it's part of a custom OS image, add a Run Command Line task between the Apply
     Operating System and Setup Windows and ConfigMgr tasks. In the command line of the
     Run Command Line task, enter the following command to delete the custom
     SetupComplete.cmd file:

     cmd.exe /c del SetupComplete.cmd %OSDTargetSystemDrive%\Windows\Setup\Scripts /F /Q

Last updated on 03/30/2026

<!-- p.512 -->

An OSD task sequence doesn't continue
after Windows Setup or an in-place
upgrade finishes
Original product version: Configuration Manager (current branch), System Center
Configuration Manager 2012 R2
Original KB number: 4494015

This article fixes an issue in which a task sequence doesn't continue after Windows Setup or an
in-place upgrade finishes if an OEM product key is used during Windows deployment.

Symptoms
When you run an OS deployment task sequence in Configuration Manager, you experience the
following issues:

     A Refresh or New Computer task sequence doesn't continue after Windows Setup
     finishes during the Setup Windows and ConfigMgr step.

     The following entry is logged in the %windir%\panther\unattendGC\Setupact.log file:

       [windeploy.exe] OEM license detected, will not run SetupComplete.cmd

     An In-Place Upgrade task sequence doesn't continue after the in-place upgrade finishes
     during the Upgrade Operating System step.

     The following is logged in the %windir%\panther\unattendGC\Setupact.log file:

       [windeploy.exe] Client OS detected: 1
       [windeploy.exe] OEM Licensing detected: 1
       [windeploy.exe] EnterpriseS or Enterprise or EnterpriseSN or EnterpriseN edition
       detected: 0
       [windeploy.exe] Client OS edition and OEM license detected and no enterprise edition
       detected, will not run SetupComplete.cmd
       [windeploy.exe] Not allowed to run the Setupcomplete.cmd, will not run
       SetupComplete.cmd

<!-- p.513 -->

These issues usually occur when you deploy a nonenterprise edition of Windows, such as
Windows Professional edition, Windows Embedded, or Windows IoT.

Cause
These issues occur because an OEM product key is used during Windows deployment. When
an OEM product key is used, Setupcomplete.cmd is disabled. This behavior occurs in all
currently supported versions of Windows. For more information, see Windows Deployment
Issues:

     [September 2012] Changes in Out-Of-Box (OOBE) Experience

     Oobe.cmd and Setupcomplete.cmd are disabled if an OEM product key is used. This is to
     ensure that end-users reach Start as quickly as possible. If you have any tools or services
     that use this infrastructure, these must be changed to tasks that occur after the OOBE.

SetupComplete.cmd is a custom script that runs during or after the Windows Setup process. It
contains commands to restart the Configuration Manager task sequence after Windows Setup
finishes. When SetupComplete.cmd is disabled, the task sequence can't continue after
Windows Setup finishes.

Resolution
To fix the issue, specify the KMS client setup keys in the locations where the OEM product key
is specified for the version of Windows that you want to deploy. For example, specify the KMS
client setup key in the Apply Windows Settings or the Upgrade Operating System step.

If the OEM product key must be used, follow these steps in addition to specifying the KMS
client setup key:

   1. Add a Run Command Line step after the Setup Windows and ConfigMgr step in a
     Refresh or New Computer task sequence, or after the Upgrade Operating System step in
     an In-Place Upgrade task sequence.
   2. In the Run Command Line step, use changepk.exe or slmgr.vbs to specify the OEM key in
     Command line.

If the OEM key in the BIOS or firmware of the device must be used, run the following
PowerShell command to get the key:

 PowerShell

<!-- p.514 -->

  Get-CIMInstance SoftwareLicensingService | Select -ExpandProperty
  OA3xOriginalProductKey

OEM product key locations
The OEM product key can be specified in the following locations:

      In a Refresh or New Computer task sequence:
         In the Apply Windows Settings step.
         In a custom answer file (Unattend.xml). This file is usually specified in the Apply
         Operating System step.
         Through variables such as OSDProductKey or ProductKey (in an MDT-integrated task
         sequence).
      In an In-Place Upgrade task sequence:
         In the Upgrade Operating System step.
         Through the OSDSetupAdditionalUpgradeOptions variable by using the /PKey command
         line option.

The OEM product key can also be obtained automatically by Windows Setup from the BIOS or
firmware of the device. In this case, the following entry is logged in the
%windir%\panther\Setupact.log file:

  MOUPG ProductKey: Product key found in Digital Marker.
  MOUPG ProductKey: Validating Product Key for Image.
  SPValidateProductKey: Calling PidGenX
  MOUPG ProductKey: Product key using pkey edition = [Professional].
  MOUPG ProductKey: Matching Install Wim For Exact Editions
  MOUPG ProductKey: Matching Install Wim.
  MOUPG ProductKey: Matched Professional with Professional
  MOUPG ProductKey: Matching Install Wim: Found [1] matching images.
  MOUPG ProductKey: Extracting Eula
  MOUPG ProductKey: Product key was successfully validated.
  MOUPG ProductKey: Product EditionID = Professional
  MOUPG ProductKey: Product InstallChannel = OEM
  MOUPG ProductKey: Eula = C:\$WINDOWS.~BT\Sources\Panther\<file>.tmp
  MOUPG ProductKey: Valid product key found = [TRUE].

 Last updated on 03/30/2026

<!-- p.515 -->

Troubleshoot the Install Application task
sequence step in Configuration Manager
This guide helps you understand the Install Application task sequence step and troubleshoot
common problems that may occur. This guide assumes that the Configuration Manager
environment has already been installed and configured.

Original product version: Configuration Manager current branch, Microsoft System Center
2012 Configuration Manager, Microsoft System Center 2012 R2 Configuration Manager
Original KB number: 18408

The Install Application task sequence step installs applications as part of the overall task
sequence. This step can install a set of specified applications, or a set of applications that are
specified by a dynamic list of task sequence variables. When this step is run, the application
installation begins immediately without waiting for a policy polling interval.

Overview
The Install Application step described in this article covers a single application install task. It
can also be used to troubleshoot the installation of multiple applications based on a list.

When the Install Application step runs, the application checks the applicability of the
requirement rules and detection method on the deployment types of the application. Based on
the results of this check, the application installs the applicable deployment type. If a
deployment type contains dependencies, the dependent deployment type is evaluated and
installed as part of the Install Application step.

  ７ Note

  Application dependencies aren't supported for stand-alone media.

Step 1: Task Sequence Manager parses the task
sequence XML and begins the Install Application task
Application installations in a task sequence have a lot in common with application installations
outside of a task sequence. They both use Configuration Manager compliance settings. But

<!-- p.516 -->

they don't function exactly the same. There are more components involved due to the nature
of running a task sequence.

As the task sequence progresses, it maintains the status of tasks and the associated execution
status using task sequence environment variables. These built-in variables provide information
about the environment where the task sequence is running. The values for these variables are
available throughout the whole task sequence. These built-in variables are initialized before the
Install Application step runs in the task sequence.

   1. Task Sequence Manager sets the following global environment variables for the next
     instruction:

           _SMSTSCurrentActionName to Install Application

           _SMSTSNexInstructionPointer to the Instruction Pointer assigned to this task

     The following entries are logged in SMSTS.log:

       01-13-2016 17:56:35.510 TSManager 2176 (0x880) Start executing an instruction.
       Instructionname: Install Application. Instruction pointer: 32
       01-13-2016 17:56:35.510 TSManager 2176 (0x880) Set a global environment variable
       _SMSTSCurrentActionName=Install Application
       01-13-2016 17:56:35.510 TSManager 2176 (0x880) Set a global environment variable
       _SMSTSNextInstructionPointer=32

   2. Task Sequence Manager then saves the execution state of the task sequence and the
     environment (TSEnv.dat) to the local hard disk, as seen in SMSTS.log:

       01-13-2016 17:56:35.510 TSManager 2176 (0x880) Successfully save execution state
       and environment to local hard disk

   3. Task Sequence Manager starts the execution of the next instruction in the sequence,
     based on the execution history of the previous instruction and the next instruction
     pointer:

       01-13-2016 17:56:35.510 TSManager 2176 (0x880) Start executing an instruction.
       Instructionname: Install Application. Instruction pointer: 32

   4. Task Sequence Manager then sets local default variables for applications:

<!-- p.517 -->

        01-13-201617:56:35.510 TSManager 2176 (0x880) Set a local default variable
        OSDApp0Description
        01-13-201617:56:35.510 TSManager 2176 (0x880) Set a local default variable
        OSDApp0DisplayName
        01-13-201617:56:35.510 TSManager 2176 (0x880) Set a local default variable
        OSDApp0Name
        01-13-201617:56:35.510 TSManager 2176 (0x880) Set a local default variable
        OSDAppCount
        01-13-201617:56:35.525 TSManager 2176 (0x880) Set a global environment variable
        _SMSTSLogPath=C:\WINDOWS\CCM\Logs\SMSTSLog

   5. Task Sequence Manager sets the command line for the application install
     (smsappinstall.exe) based on the task sequence XML policy that it has parsed, and begins
     executing it by calling smsappinstall.exe. The following entry is logged in SMSTS.log:

        01-13-2016 17:56:35.525 TSManager 2176 (0x880) Executing command line:
        smsappinstall.exe/app:ScopeId_GUID/Application_GUID/basevar:
        /continueOnError:False

At this point the Install Application task (smsappinstall.exe) begins to install the application,
although the command line to run the installation won't happen for some time yet. All the
necessary information must be acquired first.

Troubleshoot step 1
Based on the flow and execution of the task sequence, it's unlikely that a failure occurs during
this step of the Install Application process. At this point, Task Sequence Manager has
successfully parsed the task sequence XML and set an instruction pointer for the current task.
Also, the policy for the task sequence is downloaded when the task sequence begins. The
results are returned to the task sequence. They are stored in the task sequence environment
using variables that are saved on disk as TSEnv.dat.

Here are some items to consider when investigating these issues. There may be an additional
piece of information uncovered that can be used for troubleshooting the error condition.

   Tip

  The policy body for the task sequence selected is downloaded from the database at the
  beginning of the task sequence and stored within the Task Sequence Environment using

<!-- p.518 -->

  variables.

MP_GetPolicy will log this activity. To find this request in the MP_GetPolicy log, search for the

Deployment ID or Task Sequence ID.

  01-13-2016 17:32:54.579 MP_GetPolicy_ISAPI 12688 (0x3190) MP GP: Query String Before
  Decode: MEH20009-MEH0000A-6F6BCC28.15_00
  01-13-2016 17:32:54.579 MP_GetPolicy_ISAPI 12688 (0x3190) MP GP: ID : MEH20009-
  MEH0000A-6F6BCC28
  01-13-2016 17:32:54.579 MP_GetPolicy_ISAPI 12688 (0x3190) MP GP: Initializing request
  from client GUID:ClientGUID.

The following stored procedure is executed to retrieve the policy body:

exec MP_GetPolicyBodyAfterAuthorization

The results of the policy body request are returned to the machine and saved in the task
sequence environment (TSEnv.dat). The policy body for the task sequence and all its dependent
policies are stored using variables. Task Sequence Manager will log a large portion of what it's
reading from the environment.

Step 2: The Install Application component evaluates
the task sequence policy and stores it in WMI
During this step, the Install Application component evaluates the task sequence policy and
stores it in WMI. The application checks the applicability of the requirement rules and detection
method on the deployment types of the application. CIStore and CIStateStore are used to
evaluate the applicability and state of the Configuration Items (CIs) and the Configuration
Data Content associated with the application and deployment type. The result is that the CIs
will be marked for download.

   1. Install Application parses the command line and identifies the application name. The
     following entries are logged in SMSTS.log:

       01-13-2016 17:56:35.572 InstallApplication 1608 (0x648) Application Names:
       01-13-2016 17:56:35.572 InstallApplication 1608 (0x648)
       'ScopeId_GUID/Application_GUID'

<!-- p.519 -->

2. Install Application sets variables for the application. The following entries are logged in
  SMSTS.log:

    01-13-2016 17:56:35.666 InstallApplication 1608 (0x648) Setting TSEnv variable
    'SMSTSAppPolicyEvaluationJobID__ScopeId_GUID/Application_GUID'=''
    01-13-2016 17:56:35.666 InstallApplication 1608 (0x648) Setting TSEnv variable
    'SMSTSInstallApplicationJobID__ScopeId_GUID/Application_GUID'=''

3. It then looks for policy scope ID. The following entry is logged in SMSTS.log:

    01-13-2016 17:56:35.666 InstallApplication 1608 (0x648) Retrieving value from TSEnv
    for '_SMSTSPolicy_ScopeId_GUID/Application_GUID

4. Now it looks for and retrieves the value of the application policy from the task sequence
  environment (TSEnv.dat). The following entry is logged in SMSTS.log:

    01-13-2016 17:56:35.666 InstallApplication 1608 (0x648) Found App policy
    modelname:ScopeId_GUID/RequiredApplication_GUID and CIversion:10

5. Install Application then decompresses the policy. The following entries are logged in
  SMSTS.log:

    01-13-2016 17:56:35.666 InstallApplication 1608 (0x648) Found App policy
    modelname:ScopeId_GUID/RequiredApplication_GUID and CIversion:10
    01-13-2016 17:56:35.682 InstallApplication 1608 (0x648) ::DecompressBuffer(65536)
    01-13-2016 17:56:35.682 InstallApplication 1608 (0x648) Decompression (zlib)
    succeeded: original size 145382, uncompressed size 1238794.

6. The policies are stored in WMI by the Install Application component in the
  root\ccm\policy\actualconfig namespace. The following entries are logged in SMSTS.log:

    01-13-2016 17:56:36.119 InstallApplication 1608 (0x648) Locked ActualConfig
    successfully
    01-13-2016 17:56:36.150 InstallApplication 1608 (0x648) New/Changed ActualConfig
    policy instance(s) : 6
    01-13-2016 17:56:36.150 InstallApplication 1608 (0x648) [1] Added/updated setting
    'ccm_applicationciassignment:assignmentid=dep-meh20009-
    scopeid_GUID/application_GUID'.

<!-- p.520 -->

    01-13-2016 17:56:36.150 InstallApplication 1608 (0x648) [2] Added/updated setting
    'ccm_civersioninfo:modelname=scopeid_GUID/application_GUID:version=10'.
    01-13-2016 17:56:36.150 InstallApplication 1608 (0x648) [3] Added/updated setting
    'ccm_civersioninfo:modelname=scopeid_GUID/deploymenttype_GUID:version=6'.
    01-13-2016 17:56:36.150 InstallApplication 1608 (0x648) [4] Added/updated setting
    'ccm_civersioninfo:modelname=scopeid_GUID/requiredapplication_GUID:version=10'.
    01-13-2016 17:56:36.150 InstallApplication 1608 (0x648) [5] Added/updated setting
    'ccm_civersioninfo:modelname=windows/all_windows_client_server:version=1'.
    01-13-2016 17:56:36.150 InstallApplication 1608 (0x648) [6] Added/updated setting
    'ccm_scheduler_scheduledmessage:scheduledmessageid=dep-meh20009-
    scopeid_GUID/application_GUID'.
    01-13-2016 17:56:36.150 InstallApplication 1608 (0x648) Unlocked ActualConfig
    successfully
    01-13-2016 17:56:36.150 InstallApplication 1608 (0x648) Raising event:
    instance of CCM_PolicyAgent_SettingsEvaluationComplete
    {
    ClientID = "GUID:ClientGUID";
    DateTime = "20160113225636.150000+000";
    PolicyNamespace = " \\\\.\\root\\ccm\\policy\\machine\\actualconfig ";
    ProcessID = 1392; ThreadID = 1608;
    };

7. Policy Agent Provider then processes the change in the actualconfig policy namespace.
  The following entries are logged in PolicyAgentProvider.log:

    01-13-2016 17:56:36.150 PolicyAgentProvider 2424 (0x978) [000000B205C423A8] 1
    settings change(s) detected.
    01-13-2016 17:56:36.182 PolicyAgentProvider 2424 (0x978) [000000B205C423A8]
    Queued worker to process these 1 settings change(s)
    01-13-2016 17:56:36.182 PolicyAgentProvider 2420 (0x974) --- Processing 1 settings
    change(s).
    01-13-2016 17:56:36.182 PolicyAgentProvider 2420 (0x974) --- [1]
    __InstanceCreationEvent settings change on object
    CCM_ApplicationCIAssignment.AssignmentID="DEP-MEH20009-
    ScopeId_GUID/Application_GUID".
    01-13-2016 17:56:36.182 PolicyAgentProvider 2420 (0x974) --- Begin Indicating 1
    settings change(s).
