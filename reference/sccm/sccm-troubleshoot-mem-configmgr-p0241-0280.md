---
title: "Welcome — pages 241-280"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0241-0280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0241-0280
family: sccm
documentKind: "doc"
abstract: "and starting BITS service.\" } } Function Restart-CcmExec { $DisplayName = \"SMS Agent Host\" Write-Host \"\" Write-Log \"$DisplayName - Checking if service restart is required.\" if ($script:serviceRestartRequired) { if ($WhatIf) { Write-Log \" (What-If Mode) Service Restart will be re"
---

# Welcome — pages 241-280

<!-- p.241 -->

and starting BITS service."
    }
}

Function Restart-CcmExec {

    $DisplayName = "SMS Agent Host"

    Write-Host ""
    Write-Log "$DisplayName - Checking if service restart is required."
    if ($script:serviceRestartRequired) {

        if ($WhatIf) {
            Write-Log "     (What-If Mode) Service Restart will be required." -
WhatIfMode
            if ($NotifyPullDP) {
                Write-Log "     (What-If Mode) NotifyPullDP method will be
executed." -WhatIfMode
            }
            else {
                Write-Log "     (What-If Mode) NotifyPullDP method will NOT be
executed because -NotifyPullDP switch was NOT used." -WhatIfMode
            }
            return
        }

        try {
            Write-Host ""
            Write-Log "### Restarting CCMEXEC service... ###"
            Restart-Service CcmExec
            Write-Log "### Success! ###"
        } catch {
            Write-Log "### ERROR! Restart CcmExec Manually in order to
recreate BITS jobs for content transfer! ###"
        }

        if (-not $DeletePullDPNotifications -and $NotifyPullDP) {
            # Only do this if notifications were not deleted. If they were
deleted, NotifyPullDP will not do anything.
            try {
                Write-Host ""
                Write-Log "### Invoking NotifyPullDP WMI method against the
SMS_DistributionPoint class in $DPNamespace."
                Invoke-WmiMethod -Namespace root\SCCMDP -Class
SMS_DistributionPoint -Name NotifyPullDP | Out-Null
                Write-Log "### Success! ###"
            } catch {
                Write-Log "### ERROR! Failed to invoke NotifyPullDP method!
You can use wbemtest or WMI Explorer to invoke the method manually. ###"
            }
        }
        else {
            if (-not $NotifyPullDP) {
                Write-Log "### Skipped invoking NotifyPullDP WMI method
because -NotifyPullDP was NOT specified" -IsWarning

<!-- p.242 -->

                Write-Log "### You can use wbemtest or WMI Explorer to invoke
the method manually, if necessary. ###"
            }

            if ($DeletePullDPNotifications) {
                Write-Log "### Skipped invoking NotifyPullDP WMI method
because -DeletePullDPNotifications was specified" -IsWarning
                Write-Log "### Executing NotifyPullDP when there are no
notifications does not do anything." -IsWarning
            }

       }
    }
    else {
        Write-Log "    Service Restart is NOT required. " -WhatIfMode
        if ($NotifyPullDP) {
            Write-Log "    NotifyPullDP method skipped. " -WhatIfMode
        }
    }
}

Write-Host ""
Write-Log "### Script Started ###"
$script:serviceRestartRequired = $false

if ($WhatIf) {
    Write-Host ""
    Write-Log "*** Running in What-If Mode" -WhatIfMode
}

$DPNamespace = "root\SCCMDP"
$DTSNamespace = "root\CCM\DataTransferService"

Delete-WmiInstances -Namespace $DTSNamespace -ClassName "CCM_DTS_JobEx" -
Filter "NotifyEndpoint like '%PullDP%'" -Property1 "ID"
Delete-WmiInstances -Namespace $DTSNamespace -ClassName "CCM_DTS_JobItemEx" -
Property1 "JobID"
Delete-WmiInstances -Namespace $DPNamespace -ClassName "SMS_PullDPState" -
Property1 "PackageID" -Property2 "PackageVersion" -Property3 "PackageState"
Delete-WmiInstances -Namespace $DPNamespace -ClassName
"SMS_PullDPContentState" -Property1 "PackageKey" -Property2 "ContentId" -
Property3 "ContentState"

if ($DeletePullDPNotifications) {
    Delete-WmiInstances -Namespace $DPNamespace -ClassName
"SMS_PullDPNotification" -Property1 "PackageID" -Property2 "PackageVersion"
}
else {
    Write-Host ""
    Write-Log "SMS_PullDPNotification - Connecting to WMI Class on
$ComputerName"

    $temp = Get-WmiObject -ComputerName $ComputerName -Namespace $DPNamespace
-Class "SMS_PullDPNotification" -ErrorVariable WmiError -ErrorAction
SilentlyContinue

<!-- p.243 -->

           if ($WmiError.Count -ne 0) {
               Write-Log "    SMS_PullDPNotification - Failed to connect. Error:
       $($WmiError[0].Exception.Message)" -IsErrorMessage
               $WmiError.Clear()
           }
           else {
               Write-Log "    Found $(($temp | Measure-Object).Count) instances."
               Write-Log "    Skipped because DeletePullDPNotifications switch was
       NOT used." -IsWarning
           }
       }

       if ($ComputerName -eq $env:COMPUTERNAME) {
           Check-BITSJobs
       }
       else {
           Write-Host ""
           Write-Log "BITS Jobs"
           Write-Log "    Skipped because script is running against a remote
       computer." -IsWarning
       }

       Restart-CcmExec

       Write-Host ""
       Write-Log "### Script Ended ###"
       Write-Host "### Check $LogFile for more details. ###" -ForegroundColor Cyan
       #if (-not $WhatIf -and $serviceRestartRequired) {Write-Log "### Please restart
       the WMI service (which also restarts CcmExec). ###" -IsWarning}
       Write-Host ""

     Content shows Installed on the pull DP but URL and URLSubPath for the pull DP is not
     populated in ContentDPMap , which causes issues with packages having SMB Access
     enabled.

     When the pull DP has the content successfully installed, it sends a state message that
     contains the data necessary to update the URL/URLSubPath values in ContentDPMap . This
     happens when the pull DP response is processed. Review steps 16-22 in Distribute a
     package to pull DP to understand the flow and review the relevant logs to investigate why
     the state message is not getting processed. Most likely cause for this issue is either a
     backlog of state messages in the \MP\outboxes\StateMsg.box on the management point
     or MPFDM failing to copy files to the site server due to permission issues.

Missing content files in content library
There are times when you would notice content missing from the content library. This could
happen due to previous content distribution issues or someone/something accidentally

<!-- p.244 -->

deleting files from the content library. To confirm that the content is missing from the content
library, identify an affected package and track the package content from PkgLib to FileLib .

Once you confirm that the required content for a Package is missing in the Content Library, see
Resend compressed copy of a package to a site for information on how to re-populate the
content.

Generic issues
     The DistMgr or PkgXferMgr log shows a file/path not found error:

       Output

       SMS_PACKAGE_TRANSFER_MANAGER 3776 (0xec0) CContentDefinition::TotalFileSizes
       failed; 0x80070003
       SMS_PACKAGE_TRANSFER_MANAGER 3776 (0xec0) Sending content 000f8a0a-825c-457b-
       a15b-57ade145a09b for package \<PackageID>
       SMS_PACKAGE_TRANSFER_MANAGER 3776 (0xec0) CSendFileAction::SendFiles failed;
       0x80070003
       SMS_PACKAGE_TRANSFER_MANAGER 3776 (0xec0) CSendFileAction::SendContent failed;
       0x80070003
       SMS_PACKAGE_TRANSFER_MANAGER 648 (0x288) Sent status to the distribution
       manager for pkg <PackageID>, version 14, status 4 and distribution point
       ["Display=\\DPNAME.CONTOSO.COM\"]MSWNET:["SMS_SITE=S01"]\\DPNAME.CONTOSO.COM\~

     or

       Output

       SMS_PACKAGE_TRANSFER_MANAGER 11228 (0x2bdc) Sending legacy content P0100053.2
       for package <PackageID>
       SMS_PACKAGE_TRANSFER_MANAGER 11228 (0x2bdc) CContentDefinition::TotalFileSizes
       failed; 0x80070003
       SMS_PACKAGE_TRANSFER_MANAGER 11228 (0x2bdc) CSendFileAction::SendFiles failed;
       0x80070003

     Common error codes: 0x80070002, 0x80070003.

     For file/path not found errors, the problem is likely due to the fact that the content library
     on the site server is missing content files for the package. As a result, PkgXferMgr is not
     able to send the files to the DP.

     In these cases, you can identify the content ID from the log and track the content from
     PkgLib to FileLib to ensure that the files exist. You can also use Content Library Explorer

     to check if the package content files are available in the content library, however Content

<!-- p.245 -->

Library Explorer can take some time to load and it may be easier to manually track the
content from PkgLib to FileLib . Alternatively, you can capture a Process Monitor trace
to verify if the necessary files are missing from the content library on the site server.

If the site that is missing content in the content library is the package source site, it is
necessary to update the package to increment the Package Source version so that
DistMgr takes a snapshot of the content from the package source directory again and re-
populates the missing content.

If the site missing the content in the content library is different from the package source
site, you can force the package source site to resend the compressed copy of the package
to the affected site. See Resend compressed copy of a package to a site for more
information.

DistMgr/PkgXferMgr log shows a network error:

 Output

 SMS_DISTRIBUTION_MANAGER 5112 (0x13f8) Failed to make a network connection to
 \\DPNAME.CONTOSO.COM\ADMIN$ (0x35).~
 SMS_DISTRIBUTION_MANAGER 5112 (0x13f8) ~Cannot establish connection to
 ["Display=\\DPNAME.CONTOSO.COM\"]MSWNET:["SMS_SITE=PS1"]\\DPNAME.CONTOSO.COM\.
 Error = 53
 SMS_DISTRIBUTION_MANAGER 5112 (0x13f8) Error occurred. Performing error
 cleanup prior to returning.

Common error codes: 2, 3, 53, 64.

For network related errors, review the log and identify the server you're trying to
communicate with when you get the error. Once identified, test the following:

   1. Can you ping the affected SERVERNAME using the FQDN/NetBIOS/IP address?
   2. Can you access \\SERVERNAME\admin$ share using the FQDN/NetBIOS/IP address
     using the SYSTEM account from the site server?
   3. Can you access \\SERVERNAME\admin$ share using the FQDN/NetBIOS/IP address
     using the logged in user's account from the site server?
   4. Is there a firewall between the site server and the affected server? Are relevant ports
     (RPC/SMB) open?

If the above tests are successful, capture a network trace (from the site server as well as
the affected server) while reproducing the error for review.

DistMgr/PkgXferMgr log shows an access denied error:

<!-- p.246 -->

       Output

       SMS_DISTRIBUTION_MANAGER    7076 (0x1ba4)    Taking package snapshot for
       package <PackageID> from source \\PS1SITE\PKGSOURCE\DummyPackage
       SMS_DISTRIBUTION_MANAGER    7076 (0x1ba4)    ~The source directory
       \\PS1SITE\PKGSOURCE\DummyPackage doesn't exist or the SMS service cannot
       access it, Win32 last error = 5
       SMS_DISTRIBUTION_MANAGER    7076 (0x1ba4)    ~Failed to take snapshot of
       package <PackageID>

     Common error codes: 5, 0x80070005.

     For permissions related errors, review the log and identify the path you're trying to access
     when you get the error. Once identified, test the following:

        1. Can you ping the affected SERVERNAME if the path is a UNC path?
        2. Does the site server computer account have permissions to access the path?
        3. Can you access the affected path using the FQDN/NetBIOS/IP address when using
           the SYSTEM account from the site server?
        4. Can you access the affected path using the FQDN/NetBIOS/IP address when using
           the logged in user's account from the site server?
        5. Is there a firewall between the site server and the affected server? Are relevant ports
           (RPC/SMB) open?

     If the above tests are successful, capture a Process Monitor trace from the site server
     while reproducing the error for review.

     DistMgr/PkgXferMgr look for content in the \bin\x64\FileLib directory instead of the
     actual content library location.

     This is due to a known issue in the Content Library Transfer tool.

Last updated on 03/30/2026

<!-- p.247 -->

Advanced troubleshooting tips for content
distribution
This article provides some advanced troubleshooting tips to help you identify and solve
content distribution issues.

Original product version: Configuration Manager current branch, Microsoft System Center
2012 Configuration Manager, Microsoft System Center 2012 R2 Configuration Manager

Enable verbose logging
     PkgXferMgr.log

     For Package Transfer Manager, verbose logging provides more information in the log
     about content copy process, file hashes, and job scheduling. Verbose logging can be
     enabled by setting the following registry value to 0:

      HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\SMS_PACKAGE_TRANSFER_MANAGER\Loggi

     ngLevel

     For Package Transfer Manager, debug logging provides more information about the
     content copy process. Debug logging can be enabled by setting the following registry
     value to 1:

      HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\SMS_PACKAGE_TRANSFER_MANAGER\Debug

     Logging

        ７ Note

        These registry change(s) do not require a restart of SMS_Executive service.

     Client logs (includes pull DP and management point logs)

     Verbose logging can be enabled by setting the following registry value to 0:

      HKEY_LOCAL_MACHINE\Software\Microsoft\CCM\Logging\@GLOBAL\LogLevel

     Debug logging can be enabled by setting the following registry value as REG_SZ with
     value True:

<!-- p.248 -->

HKEY_LOCAL_MACHINE\Software\Microsoft\CCM\Logging\DebugLogging\Enabled

The CCM log size can be increased to 5M by setting the following registry value to
5242880 (decimal)

HKEY_LOCAL_MACHINE\Software\Microsoft\CCM\Logging\@GLOBAL\LogMaxSize

Additionally, you can edit the DWORD value for the following registry value to increase
the number of history log files to be retained:

HKEY_LOCAL_MACHINE\Software\Microsoft\CCM\Logging\@GLOBAL\LogMaxHistory

     ７ Note

     These registry change(s) require a restart of SMS Agent Host service.

StateSys.log

Verbose logging for StateSys.log can be enabled by setting the following registry value to
1:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\COMPONENTS\SMS_STATE_SYSTEM\Verbose

logging

     ７ Note

     This registry key change does not require a restart of SMS_Executive service.

(Global - site server only) SQL queries

To get information about SQL queries executed by ConfigMgr components, SQL tracing
can be enabled by setting the following registry value to 1:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\SqlEnabled

This registry value adds SQL trace logging for all site server logs. This should only be
done temporarily while troubleshooting, and should be disabled after getting the relevant
logs.

     ７ Note

<!-- p.249 -->

    This registry change does not require a restart of SMS_Executive service.

  (Global - site server only) Enable log archiving

  There are occasions when the issue does not reproduce on demand and while waiting for
  the issue to reproduce, there's a risk of logs rolling over. In these situations, enabling log
  archiving can be useful as it allows you to have more historical logs. This is only relevant
  for site server logs.

  Log archiving can be enabled by setting the following registry values:

   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\ArchiveEnabled = 1

   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\ArchivePath = <ArchiveLocation>

  After enabling log archiving, ConfigMgr will archive the rolled over logs to the
  <ArchiveLocation>, and will keep 10 copies of each log.

  To increase the number of copies maintained for a specific component when log archiving
  is enabled, set the following registry value to 20:

   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\COMPONENT_NAME\LogMaxHistory

    ７ Note

    These registry change(s) require a restart of SMS_Executive service.

  (Per log - site server only) Increase log file size

  To increase log file size for an individual log to 50 MB, set the component-specific registry
  value to 52428800 (decimal):

   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\COMPONENT_NAME\MaxFileSize

    ７ Note

    This registry change requires a restart of SMS_Executive service.

Resend compressed copy of a package to a site

<!-- p.250 -->

When a package is first distributed to a site, DistMgr sends a compressed copy of the package
to the site. After the package is extracted in the content library on the site, the local copy of the
content is used to send the package to DPs as long as the same package version is being
distributed to the DPs in the site.

There are a few occasions where it's necessary to force a site to resend the compressed copy of
a package to a specified site. Most notably, this is required when:

   1. Content is missing from content library ( PkgLib , DataLib , or FileLib ) on a primary or
     secondary site server itself.
   2. DistMgr.log consistently complains about the content not having arrived from the parent
     site (for example: 'The contents for the package CS100026 hasn't arrived from site CS1 yet,
     will retry later').

In most cases, the message 'The contents for the package CS100026 hasn't arrived from site CS1
yet, will retry later' is logged temporarily while the package content is in transit. When you see
this message, review the Sender/Despooler logs to ensure that there are no issues with site
communications. Review Distribute a package to DP across sites to understand the log flow.

How does DistMgr know if the current site has a copy of the
package installed
DistMgr checks if there is a Type 1 row in PkgStatus for the package for the package version in
question. If there is a Type 1 row for the site with Status = Installed, the local copy of the
package content is used to send to the DPs. If there is no Type 1 row in PkgStatus , it means
that the package content is not yet installed on the site server.

Does redistribute package to DP colocated on the site server
cause the compressed copy of the package to get resent
No. Redistributing the package relies on the site already having the package content in the
package source directory. If the package was sent to the site at some point and marked as
Installed, then a redistribute action on the DP colocated on the site server doesn't do anything
as DistMgr thinks that the content is already installed and the following line will be logged in
DistMgr.log:

  The distribution point is on the siteserver and the package is a content type package. There
  is nothing to be copied over.

<!-- p.251 -->

What if the content is missing in the content library on the
package source site
If the content is missing in the content library on the package source site, then resetting the
SourceVersion will not help. The only way to repopulate the missing content is to update the

package. Updating the package causes the package source site to take a package snapshot
from the package source location and write the content to the content library.

How do I force the package source site to resend the
compressed copy of the package to a specific site
After confirming that the package source site has the required content, it's possible to force
the package source site to resend the package PCK file to a specific site by setting
SourceVersion to 0 for the Type 1 row in PkgStatus for the affected site. This row can be

identified by running the following SQL query on the package source site's database after
replacing the PACKAGEID and SITECODE of the desired package and site:

 SQL

 SELECT * FROM PkgStatus WHERE Type = 1 AND ID = 'PACKAGEID' AND SiteCode =
 'SITECODE'

After confirming that this query returns a unique and correct row, running the below query will
reset SourceVersion for this row to 0:

 SQL

 UPDATE PkgStatus SET SourceVersion = 0 WHERE Type = 1 AND ID = 'PACKAGEID' AND
 SiteCode = 'SITECODE'

After resetting the SourceVersion to 0 for the Type 1 row, redistributing the package to any DP
in the affected site will force the package source site to resend the compressed copy of the
package to the affected site.

  ７ Note

  It is very important to run the above query on the site that owns the package, i.e., the
  package source site.

<!-- p.252 -->

Relevant tables for content distribution
   SMSPackages - Contains a list of all packages

   Interesting columns:

                                                                             ﾉ   Expand table

    Column                     Values

    Action                     0 - NONE
                               1 - UPDATE
                               2 - ADD
                               3 - DELETE
                               4 - VALIDATE
                               5 - CANCEL

    PackageType                0 - Regular Package
                               3 - Driver Package
                               4 - Task Sequence
                               5 - Software Updates Package
                               6 - Device Settings Package
                               7 - Virtual App Package
                               8 - Content Package (Application)
                               257 - Operating System Image
                               258 - Boot Image
                               259 - OS Installation Package
                               260 - VHD Package

   PkgServers - Contains a list of all the packages along with the DPs they are currently

   targeted to.

   Interesting columns:

                                                                             ﾉ   Expand table

    Column                                  Values

    Action                                  0 - NONE
                                            1 - UPDATE
                                            2 - ADD
                                            3 - DELETE
                                            4 - VALIDATE
                                            5 - CANCEL

   PkgStatus - Contains a list of the current package status for each package for each DP.

<!-- p.253 -->

Interesting columns:

                                                                                    ﾉ   Expand table

 Column    Values

 Type      1 - SITE (MASTER)
           2 - DP (COPY)

           Type 1 rows are created for each site the package is targeted to. PkgServer for this row is
           the site server FQDN.

           Type 2 rows are created for each DP the package is targeted to. PkgServer is the DP
           NALPATH.

 Status    0 - NONE
           1 - SENT
           2 - RECEIVED
           3 - INSTALLED
           4 - RETRY
           5 - FAILED
           6 - REMOVED
           7 - PENDING REMOVE (Not Used)
           8 - REMOVE FAILED
           9 - RETRY REMOVE

DistributionJobs - Contains a list of Package Transfer Manager Jobs along with their

current state.

Interesting columns:

                                                                                    ﾉ   Expand table

 Column                        Values

 Action                        0 - NONE
                               1 - UPDATE
                               2 - ADD
                               3 - DELETE
                               4 - VALIDATE
                               5 - CANCEL

 State                         0 - PENDING
                               1 - READY
                               2 - STARTED
                               3 - INPROGRESS
                               4 - PENDING RESTART
                               5 - COMPLETE

<!-- p.254 -->

 Column                      Values

                             6 - FAILED
                             7 - CANCELED
                             8 - SUSPENDED

DistributionPoints - Contains a list of all the distribution points.

Interesting columns:

                                                                        ﾉ   Expand table

 Column                                   Values

 Action                                   0 - NONE
                                          1 - UPDATE
                                          2 - ADD
                                          3 - DELETE
                                          4 - VALIDATE
                                          5 - CANCEL

PullDPResponse - Temporarily contains the package status response sent from the pull

DPs. DistMgr processes the response and updates PkgStatus .

Interesting columns:

                                                                        ﾉ   Expand table

 Column                    Values

 ActionState               1 - SUCCESS
                           2 - WARNING
                           4 - ERROR
                           8 - DOWNLOAD STARTED
                           16 - DOWNLOAD IN PROGRESS
                           32 - DOWNLOADED
                           64 - CANCELED
                           128 - CANCELLATION REQUESTED

PkgNotification - Notification table monitored by SMSDBMON to trigger DistMgr to

process a package. Type column defines the type of package notification. Rows in this
table are removed after SMSDBMON triggers DistMgr.

Interesting columns:

<!-- p.255 -->

                                                                       ﾉ   Expand table

 Column                Values

 Type                  0 - UNKNOWN
                       1 - PACKAGE
                       2 - PROGRAM
                       4 - PACKAGE SERVER (DP)
                       8 - PACKAGE ACCESS ACCOUNT
                       15 - ALL

Pull DP state messages - List of state message IDs raised by pull DP

Interesting columns:

                                                                       ﾉ   Expand table

 Column                Values

 State ID              1 - SUCCESS
                       2 - WARNING
                       4 - FAILURE
                       8 - DOWNLOAD STARTED
                       16 - DOWNLOAD IN PROGRESS
                       32 - DOWNLOADED
                       64 - CANCELED

Sample State Message Report:

 Console

     <Report>
      <ReportHeader>
         <Identification>
            <Machine>
               <ClientInstalled>0</ClientInstalled>
               <ClientType>1</ClientType>
               <Unknown>0</Unknown>
               <ClientID IDType="0" IDFlag="1">00001111-aaaa-2222-bbbb-
 3333cccc4444</ClientID>
               <ClientVersion>5.00.0000.0000</ClientVersion>
               <NetBIOSName>P01PDP1.CONTOSO.COM</NetBIOSName>
               <CodePage>437</CodePage>
               <SystemDefaultLCID>1033</SystemDefaultLCID>
            </Machine>
         </Identification>
         <ReportDetails>
            <ReportContent>StateMessage</ReportContent>
            <ReportType>Full</ReportType>
            <Date>20190107200618.000000+000</Date>

<!-- p.256 -->

                  <Version>1.0</Version>
                  <Format>1.1</Format>
               </ReportDetails>
            </ReportHeader>
            <ReportBody>
               <StateMessage MessageTime="20190107200618.000000+000"
       SerialNumber="3">
                  <Topic ID="P010000F" Type="902" IDType="0"/>
                  <State ID="1" Criticality="0"/>
                  <UserParameters Flags="0" Count="4">
                     <Param>P010000F</Param>
                     <Param>["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\</Param>
                     <Param>{04AD1BB3-5E54-457A-9873-DFB2E8035090}</Param>
                     <Param/>
                  </UserParameters>
               </StateMessage>
            </ReportBody>
         </Report>

Useful SQL queries
Here are some SQL queries that may be helpful when troubleshooting various content
distribution related issues.

Package/DP status queries
     All Failed packages/DPs

       SQL

       SELECT distinct DPSD.DPName, DPSD.PackageID, SP.Name, DPSD.MessageState,
       DPSD.LastStatusTime, DPSD.SiteCode
       FROM vSMS_DPStatusDetails DPSD
       JOIN SMSPackages_All SP ON DPSD.PackageID = SP.PkgID
       WHERE MessageState = 4

     All In Progress packages/DPs

       SQL

       SELECT distinct DPSD.DPName, DPSD.PackageID, SP.Name, DPSD.MessageState,
       DPSD.LastStatusTime, DPSD.SiteCode
       FROM vSMS_DPStatusDetails DPSD
       JOIN SMSPackages_All SP ON DPSD.PackageID = SP.PkgID
       WHERE MessageState = 2

     All Success packages/DPs

<!-- p.257 -->

 SQL

 SELECT distinct DPSD.DPName, DPSD.PackageID, SP.Name, DPSD.MessageState,
 DPSD.LastStatusTime, DPSD.SiteCode
 FROM vSMS_DPStatusDetails DPSD
 JOIN SMSPackages_All SP ON DPSD.PackageID = SP.PkgID
 WHERE MessageState = 1

All package/DPs in In Progress state for more than three days

 SQL

 SELECT distinct DPSD.DPName, DPSD.PackageID, SP.Name, DPSD.MessageState,
 DPSD.LastStatusTime, DPSD.SiteCode
 FROM vSMS_DPStatusDetails DPSD
 JOIN SMSPackages_All SP ON DPSD.PackageID = SP.PkgID
 WHERE DPSD.LastStatusTime < DATEAdd(dd,-3,GETDate())
 AND MessageState = 2

All package/DPs in Failed state for more than three days

 SQL

 SELECT distinct DPSD.DPName, DPSD.PackageID, SP.Name, DPSD.MessageState,
 DPSD.LastStatusTime, DPSD.SiteCode
 FROM vSMS_DPStatusDetails DPSD
 JOIN SMSPackages_All SP ON DPSD.PackageID = SP.PkgID
 WHERE DPSD.LastStatusTime < DATEAdd(dd,-3,GETDate())
 AND MessageState = 4

Count of all states

 SQL

 SELECT MessageState,
 COUNT(MessageState) AS [Count]
 FROM vSMS_DPStatusDetails
 WHERE PackageID <> ''
 GROUP BY MessageState

Counts of package states per DP

 SQL

 SELECT DPName,
 CASE
      WHEN MessageState = 1 THEN 'Success'
      WHEN MessageState = 2 THEN 'InProgress'

<!-- p.258 -->

     WHEN MessageState = 4 THEN 'Failed'
 END AS [State],
 COUNT(MessageState) AS [Count]
 FROM vSMS_DPStatusDetails
 WHERE PackageID <> ''
 AND DPName = 'PS1DP1.CONTOSO.COM'
 GROUP BY DPName, MessageState
 ORDER BY DPName

State of all DPs for a given package

 SQL

 SELECT DPName,
 CASE
      WHEN MessageState = 1 THEN 'Success'
      WHEN MessageState = 2 THEN 'InProgress'
      WHEN MessageState = 4 THEN 'Failed'
 END AS [State]
 FROM vSMS_DPStatusDetails
 WHERE PackageID = '<PackageID>'
 GROUP BY DPName, MessageState
 ORDER BY State

Count of DP states per package

 SQL

 SELECT
 CASE
      WHEN MessageState = 1 THEN 'Success'
      WHEN MessageState = 2 THEN 'InProgress'
      WHEN MessageState = 4 THEN 'Failed'
 END AS [State],
 COUNT(MessageState) AS [Count]
 FROM vSMS_DPStatusDetails
 WHERE PackageID = '<PackageID>'
 GROUP BY MessageState

Package/DP current state

 SQL

 SELECT distinct DPSD.DPName, DPSD.PackageID, SP.Name, DPSD.LastStatusTime,
 DPSD.SiteCode, DPSD.MessageState,
 CASE
      WHEN MessageState = 1 THEN 'Success'
      WHEN MessageState = 2 THEN 'InProgress'
      WHEN MessageState = 4 THEN 'Failed'
 END AS [State]

<!-- p.259 -->

        FROM vSMS_DPStatusDetails DPSD
        JOIN SMSPackages_All SP ON DPSD.PackageID = SP.PkgID
        WHERE DPName = 'PS1DP1.CONTOSO.COM'
        AND DPSD.PackageID = '<PackageID>'

Finding orphaned DP references
The query below can be used to identify if there are any orphaned rows left in the database for
a DP that is no longer in the environment. There could be orphaned rows if the DP was not
removed properly.

  SQL

  DECLARE @DPName NVARCHAR(100)
  SET @DPName = 'PS1DP.CONTOSO.COM'
  SELECT * FROM ContentDPMap WHERE ServerName = @DPName
  SELECT * FROM DistributionPoints WHERE ServerName = @DPName
  SELECT * FROM DPInfo WHERE ServerName = @DPName
  SELECT * FROM PkgServers_G WHERE NALPath like '%' + @DPName + '%'
  SELECT * FROM PkgServers_L WHERE NALPath like '%' + @DPName + '%'
  SELECT * FROM PkgStatus_G WHERE PkgServer like '%' + @DPName + '%'
  SELECT * FROM PkgStatus_L WHERE PkgServer like '%' + @DPName + '%'
  SELECT * FROM SysResList WHERE RoleName = 'SMS Distribution Point' AND ServerName =
  @DPName
  SELECT * FROM SC_SysResUse WHERE NALPath like '%' + @DPName + '%' AND RoleTypeID =
  3

Similar query for a specific DP in a specific site:

  SQL

  DECLARE @DPName NVARCHAR(100)
  DECLARE @DPSiteCode NVARCHAR(3)
  SET @DPName = 'DPNAME.CONTOSO.COM'
  SET @DPSiteCode = 'PS1'

  SELECT * FROM ContentDPMap WHERE ServerName = @DPName AND SiteCode = @DPSiteCode
  SELECT * FROM DistributionPoints WHERE ServerName = @DPName AND SMSSiteCode =
  @DPSiteCode
  SELECT * FROM DPInfo WHERE ServerName = @DPName AND SiteCode = @DPSiteCode
  SELECT * FROM PkgServers_L WHERE NALPath like '%' + @DPName + '%' AND SiteCode =
  @DPSiteCode
  SELECT * FROM PkgServers_G WHERE NALPath like '%' + @DPName + '%' AND SiteCode =
  @DPSiteCode
  SELECT * FROM PkgStatus_L WHERE PkgServer like '%' + @DPName + '%' AND SiteCode =
  @DPSiteCode
  SELECT * FROM PkgStatus_G WHERE PkgServer like '%' + @DPName + '%' AND SiteCode =
  @DPSiteCode
  SELECT * FROM SysResList WHERE RoleName = 'SMS Distribution Point' AND ServerName =
  @DPName AND SiteCode = @DPSiteCode

<!-- p.260 -->

 SELECT * FROM SC_SysResUse WHERE NALPath like '%' + @DPName + '%SMS_SITE=' +
 @DPSiteCode + '%' AND RoleTypeID = 3

Site Control File (SCF) properties
     SCF properties for DistMgr for current site

       SQL

       SELECT SD.SiteCode, SC.ComponentName, SCP.Name, SCP.Value1, SCP.Value2,
       SCP.Value3
       FROM SC_Component SC
       JOIN SC_SiteDefinition SD ON SD.SiteNumber = SC.SiteNumber
       JOIN SC_Component_Property SCP ON SCP.ComponentID = SC.ID
       WHERE SD.SiteCode = dbo.fnGetSiteCode() AND SC.ComponentName =
       'SMS_DISTRIBUTION_MANAGER'

     SCF properties for a DP

       SQL

       SELECT SRU.RoleName, SRU.ServerName, SRUP.* FROM vSMS_SC_SysResUse SRU
       JOIN vSMS_SC_SysResUse_Properties SRUP ON SRU.ID = SRUP.ID
       WHERE SRU.RoleName = 'SMS Distribution Point'
       AND SRU.ServerName = 'PS1DP1.CONTOSO.COM'

Packages containing specified software update
List all packages containing the given update Unique ID.

 SQL

 SELECT distinct UI.ArticleID, CI.CI_UniqueID, CP.PkgID, P.Name FROM v_UpdateInfo UI
 JOIN v_ConfigurationItems CI ON UI.CI_ID = CI.CI_ID
 JOIN v_CIContents_All CIC ON CI.CI_ID = CIC.CI_ID
 JOIN CI_ContentPackages CP ON CP.Content_ID = CIC.Content_ID
 JOIN v_Package P ON CP.PkgID = P.PackageID
 WHERE CI.CI_UniqueID = '<UniqueID>'

Last updated on 03/30/2026

<!-- p.261 -->

Troubleshoot Configuration Manager
Database Replication Service overview
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

To better understand and help troubleshoot issues with Database Replication Service, use these
diagrams.

     Database replication
     DRS configuration
     DRS performance
     DRS reinitialization (reinit)
     Global data reinit
     Site data reinit
     Reinit missing message

These troubleshooting diagrams are interconnected. Use the following diagram to understand
their relationships:

For more information, see the following series of blogs from Microsoft Support:

<!-- p.262 -->

     ConfigMgr DRS Synchronization Internals
     ConfigMgr 2012 Data Replication Service (DRS) Unleashed
     ConfigMgr 2012 DRS – Troubleshooting FAQs
     ConfigMgr 2012 DRS Initialization Internals
     ConfigMgr 2012: DRS and SQL Server service broker certificate issues

Last updated on 03/27/2026

<!-- p.263 -->

Troubleshoot Database Replication Service
links
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS replication when a link fails:

                                                       Troubleshoot SQL replication
                                           Replication link failure
                                 Start

  SELECT * FROM
                                 CAS /      Check if the replication group
  RCM_ReplicationLinkStatus
                                Primary     link is in degraded or failed state
  WHERE Status IN (8, 9)

                                             No
                                            Result

                                 Has
                                Result
                                                                                   DECLARE @cutoffTime DATETIME
                                                                                   SELECT @cutoffTime =
                                                                                   DATEADD(minute, -30,
                                                                                   GETUTCDATE())
                                                                                                                               Check if replication group
                                                                                   SELECT * FROM                               link is recently calculated
                                                                                   RCM_ReplicationLinkStatus
                                                                                   WHERE UpdateTime >@cutoffTime

  SELECT * FROM ServerData                                                                                    No
                                          Check SQL maintenance mode
  WHERE Status = 120                                                                                         Result

                                                                                                                       Has
                                                                                                                      Result

                        Has                  No
                       Result               Result

           Continue to                        Continue to                      Continue to
                                                                                                                       End
       SQL replication reinit               SQL performance                  SQL configuration

Queries
This diagram uses the following queries:

Check if the replication group link is in degraded or failed
state

<!-- p.264 -->

 SQL

 SELECT * FROM RCM_ReplicationLinkStatus
 WHERE Status IN (8, 9)

Check if replication group link is recently calculated

 SQL

 DECLARE @cutoffTime DATETIME
 SELECT @cutoffTime = DATEADD(minute, -30, GETUTCDATE())
 SELECT * FROM RCM_ReplicationLinkStatus
 WHERE UpdateTime >@cutoffTime

Check SQL Server maintenance mode

 SQL

 SELECT * FROM ServerData
 WHERE SiteStatus = 120

Next steps
     DRS reinitialization (reinit)
     DRS performance
     DRS configuration

Last updated on 03/27/2026

<!-- p.265 -->

SQL Server instance configuration
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS configuration related to SQL Server
Service Broker:

                               Troubleshoot SQL configuration
                                                      Troubleshoot SQL configuration
                                           Start
                                                      related to SQL service broker (SSB)

   SELECT
   transmission_status, *
   FROM                                    CAS /
                                                     Check if SQL can deliver SSB messages
   sys.transmission_queue                 Primary
   ORDER BY enqueue_time
   DESC

                                                     No
                                                                                                             End
                                                    Result
                                            Has
                                           Result

                                                    Check transmission_status
                                                    You may need to refresh the
                                                    previous query as it could be blank

                                Has                 Transmission_status
                               Result                    is empty

                            Remediate the issues
                                                                                            Run SQL profiler to
                End         reported from                                      End
                                                                                            trace SSB events
                            transmission_status

Queries
This diagram has the following queries and actions:

Check if SQL Server can deliver SSB messages

 SQL

<!-- p.266 -->

 SELECT transmission_status, *
 FROM sys.transmission_queue
 ORDER BY enqueue_time DESC

Remediation actions

Remediate the issues reported from transmission_status
Common issues:

     Firewall configuration
     Network configuration
     SSB certificate misconfigured

Run SQL Server profiler to trace SSB events
Run SQL Server profiler on the CAS and primary site database to trace events related to the
SQL Server Service Broker:

     Audit Broker Login
     Audit Broker Conversation
     Events in Broker category

Last updated on 03/27/2026

<!-- p.267 -->

Database Replication Service performance
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS performance that can impact
replication status:

                                                                                         

<!-- p.268 -->

Queries
This diagram uses the following queries:

Make sure SQL Server change tracking table is cleaned up

 SQL

 DECLARE @RetentionUnit INT = 0;
 DECLARE @RetentionPeriod INT = 0;
 DECLARE @CTCutOffTime DATETIME;
 DECLARE @CTMinTime DATETIME;

 SELECT @RetentionPeriod=retention_period,
     @RetentionUnit=retention_period_units
 FROM sys.change_tracking_databases
 WHERE database_id = DB_ID();

 IF @RetentionUnit = 1
     SET @CTCutOffTime = DATEADD(MINUTE,-@RetentionPeriod,GETUTCDATE())
 ELSE IF @RetentionUnit = 2
     SET @CTCutOffTime = DATEADD(HOUR,-@RetentionPeriod,GETUTCDATE())
 ELSE IF @RetentionUnit = 3
     SET @CTCutOffTime = DATEADD(DAY,-@RetentionPeriod,GETUTCDATE())

 -- give a buffer of two days
 SET @CTCutOffTime = DATEADD(DAY, -2, @CTCutOffTime)
 select top 1 @CTMinTime=commit_time from sys.dm_tran_commit_table order by
 commit_ts asc
 IF @CTMinTime < @CTCutOffTime
     PRINT 'there is change tracking backlog, please contact Microsoft support'

Change current sessions that handle SQL Server service
broker messages are blocked

 SQL

 select
        req.session_id
        ,req.blocking_session_id
        ,req.last_wait_type
        ,req.wait_type
        ,req.wait_resource
        ,t.text
 from sys.dm_exec_sessions s
 inner join sys.dm_exec_requests req on s.Session_id=req.session_id
 cross apply sys.dm_exec_sql_text(sql_handle) t
 where program_name='SMS_data_replication_service'

<!-- p.269 -->

Check sessions asking too much memory

 SQL

 SELECT * FROM sys.dm_exec_query_memory_grants
 ORDER BY requested_memory_kb DESC

Check sessions taking too many locks

 SQL

 SELECT TOP 10 request_session_id,
 program_name = (SELECT program_name FROM sys.dm_exec_sessions WHERE
 session_id=request_session_id),
 COUNT (*) num_locks
 FROM sys.dm_tran_locks
 GROUP BY request_session_id
 ORDER BY count (*) DESC

See also
SQL Server configuration

Last updated on 03/27/2026

<!-- p.270 -->

Database Replication Service reinitialization
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS reinitialization (reinit):

                                          Troubleshoot SQL replication reinit
                                                               Start           SQL replication reinitialization (reinit)

                  SELECT * FROM ServerData                    CAS /
                                                                               Check if site is in maintenance mode
                  WHERE SiteStatus = 120                     Primary

                                                                             No
                                                                                                                           End
                                                                            Result
                                                               Has
                                                              Result

                   SELECT * FROM
                   RCM_DrsInitializationTracking                              Check which replication group
                   WHERE InitializationStatus NOT IN                          hasn't completed reinit
                   (6,7)

                                                                                No
                                                                               Result

                                                               Has
                                                              Result

                  SELECT * FROM
                  RCM_DrsInitializationTracking dt
                  INNER JOIN ReplicationData rg
                  ON dt.ReplicationGroup =
                  rg.ReplicationGroup                                         Check global data
                  WHERE dt.InitializationStatus NOT IN
                  (6,7)
                  AND rg.ReplicationPattern=N'GLOBAL'

                                                Has                                No
                                               Result                             Result

                                                   SELECT * FROM
                                                   RCM_DrsInitializationTracking dt
                                                   INNER JOIN ReplicationData rg
                                                   ON dt.ReplicationGroup =
                                                   rg.ReplicationGroup
                                                                                                       Check site data
                                                   WHERE dt.InitializationStatus NOT IN
                                                   (6,7)
                                                   AND rg.ReplicationPattern=N'Site'

        Continue to                                Continue to                     Has                 No                          Continue to
     Global data reinit                           Site data reinit                Result              Result                     SQL configuration

<!-- p.271 -->

Queries
This diagram uses the following queries:

Check if site is in maintenance mode

 SQL

 SELECT * FROM ServerData
 WHERE Status = 120

Check that reinit isn't completed for which replication group

 SQL

 SELECT * FROM RCM_DrsInitializationTracking
 WHERE InitializationStatus NOT IN (6,7)

Check global data

 SQL

 SELECT * FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N'GLOBAL'

Check site data

 SQL

 SELECT * FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N'Site'

Next steps
     Global data reinit
     Site data reinit

<!-- p.272 -->

     SQL Server configuration

Last updated on 03/27/2026

<!-- p.273 -->

Troubleshoot global data reinitialization
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS reinitialization (reinit) for global data in
a Configuration Manager hierarchy:

<!-- p.274 -->

                                                                   Troubleshoot global data reinit
                                                                        Start            Troubleshoot SQL replication
                                                                                         reinit for global data

 SELECT * FROM                                                                  SELECT * FROM
 RCM_DrsInitializationTracking dt                                               RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg                                                  INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup =
                                            Check if site replication           ON dt.ReplicationGroup =
 rg.ReplicationGroup                 CAS                                        rg.ReplicationGroup                          Primary
 WHERE dt.InitializationStatus NOT          hasn't finished reinit              WHERE dt.InitializationStatus NOT
 IN (6,7)                                                                       IN (6,7)
 AND                                                                            AND
 rg.ReplicationPattern=N'Global'                                                rg.ReplicationPattern=N'Global'

                                                                                      No
                                                                                                                                          End
                                                                                     Result
                                                                         Has
                                                                        Result

                                                                                  SELECT RequestTrackingGUID,
                                                                                  InitializationStatus
                                                                                  FROM RCM_DrsInitializationTracking dt
                                                                                  INNER JOIN ReplicationData rg
                                                                                                                                       Get the TrackingGuid &
                                                                                  ON dt.ReplicationGroup =
                                                                                  rg.ReplicationGroup                                  Status from the primary site
                                                                                  WHERE dt.InitializationStatus NOT IN
                                                                                  (6,7)
                                                                                  AND rg.ReplicationPattern=N'Global'

                                                                                  SELECT RequestTrackingGUID,
                                                                                  InitializationStatus
                                                                                  FROM RCM_DrsInitializationTracking dt
                                                                                                                                       Get the TrackingGuid &
                                                                                  WHERE                                                Status from the CAS
                                                                                  RequestTrackingGUID=@trackingGuid

                                                                                                                                        No                                Continue to
                                                                                                                                       Result                       Reinit missing message

                                                                                                                               Has
                                                                                                                              Result

                                                                                                                                       Check InitializationStatus

                                                                                                           == 3 or                                                          Continue to
                                                                                                                                            == 99
                                                                                                            == 4                                                            Reinit failed

                                                                                                                               == 5
   SELECT Status FROM
   RCM_InitPackageRequest WHERE
                                           Check request status for
   RequestTrackingGUID=@trackGuid          the tracking ID
                                                                                                                                                                Rcmctrl.log (primary site)

                                                                                                          RCM on primary site is BCP in the data                BcpIn for group <group name>
                                                                                                                                                                …
                                                                                                                                                                Failed to BCP in for table <table name>

                                                                                                                                                                Rcmctrl.log (CAS)
                                                                                                              RCM is preparing the data, check
                                                                           == 1                                                                                 Creating init package for replication
                                                                                                            rcmctrl.log on CAS for BCP progress                 group <replication group> for site
                                                                                                                                                                <CAS>

                                                                                                                                                                Rcmctrl.log (CAS)

                                                                                                                  RCM has finished BCP the data,                Created minijob to send compressed
                                                                          == 2
                                                                                                                   create/compress the package                  copy of DRS INIT BCP Package to site
                                                                                                                                                                <CAS>. Transfer root = <CAB file to
                                                                                                                                                                transfer>

                                                                                                             File replication Job created. Check                Sender.log (CAS)
                                                                         == 3
                                                                                                             sender.log on primary for progress                 Sending completed [CAB file to transfer]

                                                                                                                                                                Despoolr.log (primary site)

                                                                                                                                                                Verified Package signature
                                                                                                                                                                …
                                                                                                             File replication Job done. Check                   Executing instruction of type
                                                                                                           despoolr.log on Primary for progress                 MICROSOFT|SMS|MINIJOBINSTRUCTION
                                                                                                                                                                |DRSINIT
                                                                                                                                                                ...
                                                                                                                                                                Decompressing snapshot package
                                                                                                                                                                <compressed file> to [rcm inbox]

Queries
This diagram uses the following queries:

<!-- p.275 -->

Check if reinit isn't finished for global replication

 SQL

 SELECT * FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N`Global'

Get the TrackingGuid & Status from the primary site

 SQL

 SELECT RequestTrackingGUID, InitializationStatus
 FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N`Global'

Get the TrackingGuid & Status from the CAS

 SQL

 SELECT RequestTrackingGUID, InitializationStatus
 FROM RCM_DrsInitializationTracking dt
 WHERE RequestTrackingGUID=@trackingGuid

Check request status for the tracking ID

 SQL

 SELECT Status FROM RCM_InitPackageRequest
 WHERE RequestTrackingGUID=@trackGuid

Next steps
     Reinit missing message

Last updated on 03/27/2026

<!-- p.276 -->

Troubleshoot site data reinit
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS reinitialization (reinit) for site data in a
Configuration Manager hierarchy:

<!-- p.277 -->

                                                   Troubleshoot site data reinit
                                                                                  Start

SELECT * FROM                                                                              SELECT * FROM
RCM_DrsInitializationTracking dt                                                           RCM_DrsInitializationTracking dt
INNER JOIN ReplicationData rg                                                              INNER JOIN ReplicationData rg
ON dt.ReplicationGroup =                        Check if site replication                  ON dt.ReplicationGroup =
rg.ReplicationGroup                 CAS                                                    rg.ReplicationGroup                 Primary
                                                hasn't finished reinit
WHERE dt.InitializationStatus NOT                                                          WHERE dt.InitializationStatus NOT
IN (6,7)                                                                                   IN (6,7)
AND rg.ReplicationPattern=N'Site'                                                          AND rg.ReplicationPattern=N'Site'

                                                                                               No
                                                                                                                                            End
                                                                                              Result

                                                                                   Has
                                                                                  Result

                                          SELECT RequestTrackingGUID,
                                          InitializationStatus
                                          FROM RCM_DrsInitializationTracking dt
                                          INNER JOIN ReplicationData rg
                                          ON dt.ReplicationGroup =
                                                                                               Get the TrackingGuid &
                                          rg.ReplicationGroup                                  Status from CAS
                                          WHERE dt.InitializationStatus NOT IN
                                          (6,7)
                                          AND rg.ReplicationPattern=N'Site'

                                          SELECT RequestTrackingGUID,
                                          InitializationStatus
                                          FROM RCM_DrsInitializationTracking dt
                                                                                             Get the TrackingGuid &
                                          WHERE                                              Status from the primary site
                                          RequestTrackingGUID=@trackingGuid

                                                                                              No                                     Continue to
                                                                                             Result                            Reinit missing message

                                                                                   Has
                                                                                  Result

                                                                                              Check InitializationStatus

                                                                                                                                    Continue to
                                                                == 5                             == 99
                                                                        == 4                                                        Reinit failed

                                                                                  == 3

                                          SELECT * FROM ServerData
                                          WHERE SiteStatus = 125                              Check primary site isn't
                                          AND SiteCode=dbo.fnGetSiteCode()                    in maintenance mode
                                          AND ServerRole=N'Peer'

                                                                                                 No                                  Continue to
                                                                                                Result                            Global data reinit

                                                                                   Has
                                                                                  Result

                                          SELECT Status FROM                                Check request status
                                          RCM_InitPackageRequest WHERE
                                          RequestTrackingGUID=@trackGuid                    for the tracking ID

<!-- p.278 -->

                                                == 3
                                                == 2
                                                          == 1

                                                                                  Rcmctrl.log (primary site)
                                          RCM is preparing the data, check
                                       rcmctrl.log on primary for BCP progress    Creating init package for replication
                                                                                  group <replication group> for site <CAS>

                                                                                  Rcmctrl.log (primary site)
                                            RCM has finished BCP the data,
                                                                                  Created minijob to send compressed copy
                                             create/compress the package          of DRS INIT BCP Package to site <CAS>.
                                                                                  Tranfer root = <CAB file to transfer>

                                                                                  Sender.log (primary site)
                                            File replication job created, check
                                           sender.log on primary for progress     Sending completed [CAB file to transfer]

                                                                                  Despoolr.log (CAS)

                                                                                  Verified Package signature
                                                                                  …
                                            File replication job done, check      Executing instruction of type
                                           despoolr.log on CAS for progress       MICROSOFT|SMS|MINIJOBINSTRUCTION|
                                                                                  DRSINIT
                                                                                  ...
                                                                                  Decompressing snapshot package
                                                                                  <compressed file> to [rcm inbox]

                                                                                  Rcmctrl.log (CAS)

                                             RCM on CAS is BCP in the data        BcpIn for group <group name>
                                                                                  …
                                                                                  Failed to BCP in for table <table name>

Queries
This diagram uses the following queries:

Check if reinit isn't finished for site replication

 SQL

 SELECT * FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N`Site'

Get the TrackingGuid & Status from the CAS

 SQL

 SELECT RequestTrackingGUID, InitializationStatus
 FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup

<!-- p.279 -->

 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N'Site'

Get the TrackingGuid & Status from the primary site

 SQL

 SELECT RequestTrackingGUID, InitializationStatus
 FROM RCM_DrsInitializationTracking dt
 WHERE RequestTrackingGUID=@trackingGuid

Check primary site isn't in maintenance mode

 SQL

 SELECT * FROM ServerData
 WHERE SiteStatus = 125
 AND SiteCode=dbo.fnGetSiteCode()
 AND ServerRole=N'Peer'

Check request status for the tracking ID

 SQL

 SELECT Status FROM RCM_InitPackageRequest
 WHERE RequestTrackingGUID=@trackGuid

Next steps
     Reinit missing message
     Global data reinit

Last updated on 03/27/2026

<!-- p.280 -->

Reinitialize a missing message
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting a missing message with DRS reinitialization
(reinit):

                                       Troubleshoot reinit missing message
                                                                                       Start

   SELECT * FROM                                                                                SELECT * FROM
   RCM_DrsInitializationTracking dt                                                             RCM_DrsInitializationTracking dt
   INNER JOIN ReplicationData rg                                                                INNER JOIN ReplicationData rg
   ON dt.ReplicationGroup =            Subscriber    Check if site replication                  ON dt.ReplicationGroup =            Publishing
   rg.ReplicationGroup                    site       hasn't finished reinit                     rg.ReplicationGroup                    site
   WHERE dt.InitializationStatus NOT                                                            WHERE dt.InitializationStatus NOT
   IN (6,7)                                                                                     IN (6,7)

                                                                                                            No
                                                                                                           Result

                                                                                        Has
                                                                                       Result                                         End

                                               SELECT RequestTrackingGUID,
                                               InitializationStatus
                                               FROM RCM_DrsInitializationTracking dt
                                               INNER JOIN ReplicationData rg                         Get the TrackingGuid &
                                               ON dt.ReplicationGroup =                              Status from subscriber site
                                               rg.ReplicationGroup
                                               WHERE dt.InitializationStatus NOT IN
                                               (6,7)

                                               SELECT RequestTrackingGUID,
                                               InitializationStatus
                                               FROM RCM_DrsInitializationTracking dt
                                                                                                      Get the TrackingGuid & Status
                                               WHERE                                                  from the publishing site
                                               RequestTrackingGUID=@trackingGuid

                                                                               Has                      No
                                                                              Result                   Result

                                                    Go to SQL replication reinit                     Take remediation actions

Queries
This diagram uses the following queries:
