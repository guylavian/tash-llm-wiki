---
title: "App management documentation — pages 281-309"
type: reference
domain: sccm
slug: sccm-intune-configmgr-apps-p0281-0309
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-apps-p0281-0309
family: sccm
documentKind: "doc"
abstract: "Additional information for error resolution: Verify the content for the application is on a distribution point and that the distribution point is accessible to the client. For more information, see Application download in Configuration Manager. 0x87D00667 Message: No current or"
---

# App management documentation — pages 281-309

<!-- p.281 -->

Additional information for error resolution: Verify the content for the application is on a
distribution point and that the distribution point is accessible to the client. For more information,
see Application download in Configuration Manager.

0x87D00667
Message: No current or future service window exists to install software updates

Additional information for error resolution: Ensure that the maintenance window on the client is
large enough to support the Maximum allowed run time (minutes) for the application
installation and that the client has received the policy for the window.

0x87D01106
Message: Failed to verify the executable file is valid or to construct the associated command line

Additional information for error resolution: Verify that the executable file is installable on its
own then verify it's installable with the given command line.

0x87D01107
Message: Failed to access all the provided program locations. This program may retry if the
maximum retry count has not been reached

Additional information for error resolution: The client is getting locations for the content, but
can't reach the locations. Review the client's LocationServices.log for the Distribution Point= .
Use ContentTransferManager.log and DataTransferService.log to monitor the download for
errors.

0x87D01201
Message: The content download cannot be performed because there is not enough available
space in cache or the disk is full

Additional information for error resolution: Check that the machine has enough space on the
drive. Compare the size of the ccmcache directory with the client cache settings and ensure the
setting is adequate for the application's size.

0x87D01202

<!-- p.282 -->

Message: The content download cannot be performed because the total size of the client cache
is smaller than the size of the requested content

Additional information for error resolution: Compare the size of the ccmcache directory with the
client cache settings and ensure the setting is adequate for the application's size.

0x87D01281
Message: A supported App-V client is not installed

Additional information for error resolution: Verify that a supported version of App-V is installed
on the client.

0x87D0128F
Message: The App-V sftmime command returned failure

Additional information for error resolution: For information on sftmime commands, see Manage
Virtual Applications by Using the Command Line.

0x87D01290
Message: An error occurred when querying the App-V WMI provider

Additional information for error resolution: For information on the App-V WMI provider, see
Application Virtualization Client WMI Provider.

0x87D103E8
Message: Error Unknown

Additional information for error resolution: Follow the application troubleshooting guide to
help locate the error and resolve it. It may be necessary to review additional logs for components
that support application installation. Searching for specific IDs or error codes in the logging may
help you identify the problem. For more information, see general troubleshooting tips.

0x87D1076C
Message: Application was successfully installed

Additional information for error resolution: The application was successfully installed.

<!-- p.283 -->

MSI errors
                                                                                              ﾉ   Expand table

 Error    Error     Error message
 code     source

 1602     MSI       User cancel installation

 1603     MSI       Fatal error during installation

 1605     MSI       This action is only valid for products that are currently installed

 1618     MSI       Another program is being installed. Please wait until that installation is complete, and
                    then try installing this software again

 1633     MSI       This installation package is not supported by this processor type. Contact your product
                    vendor

 1638     MSI       Another version of this product is already installed. Installation of this version cannot
                    continue. To configure or remove the existing version of this product, use Add/Remove
                    Programs on the Control Panel

 1642     MSI       The upgrade patch cannot be installed by the Windows Installer service because the
                    program to be upgraded may be missing, or the upgrade patch may update a different
                    version of the program. Verify that the program to be upgraded exists on your
                    computer and that you have the correct upgrade patch

General MSI troubleshooting tips
When errors are encountered from MSI, typically you'll need to Enable Windows Installer logging.
After the logging is enabled, you can retry the problem installation and Windows Installer will
track the progress and post it to the %temp% folder. The new log's file name is random. However,
the first letters are Msi and the file name has a .log extension.

The MsiExec.exe and InstMsi.exe Error Messages and Windows Installer Action Return Values lists
are useful when reviewing a Windows Installer log as are the general troubleshooting tips.

1602
Message: User cancel installation

Additional information for error resolution: The installation was canceled by the user. Ask the
user to install the application fully. If possible, you can attempt to run the installation for the
system rather than the user.

<!-- p.284 -->

1603
Message: Fatal error during installation

Additional information for error resolution: Enable Windows Installer logging and run the install
again. When reviewing the installer log, typically an entry stating Return value 3 is located near
the failure reason in the log. For more information on possible return values and their meaning,
see Windows Installer Action Return Values.

1605
Message: This action is only valid for products that are currently installed

Additional information for error resolution: Ensure that the product is installed before running a
dependant install.

1618
Message: Another program is being installed. Please wait until that installation is complete, and
then try installing this software again

Additional information for error resolution: Wait for the prior installation to complete before
running a new one. If the prior installation stops responding, you can attempt to stop the
installation or terminate the process. Terminating a process might have undesired results.

1633
Message: This installation package is not supported by this processor type. Contact your product
vendor

Additional information for error resolution: Ensure that the device's processor architecture is
appropriate for the software. Verify the target device meets or exceeds the minimum processor
requirement for the application. Contact the product vendor if the device's processor meets the
product's processor support specifications.

1638
Message: Another version of this product is already installed. Installation of this version cannot
continue. To configure or remove the existing version of this product, use Add/Remove Programs
on the Control Panel

<!-- p.285 -->

Additional information for error resolution: Uninstall the the unwanted version of the product. If
you aren't using Configuration Manager, a script, or another management tool to uninstall,
uninstall from the device manually. For Windows 10 or later clients, use Windows Settings >
Apps to uninstall the unwanted version of the product. For earlier versions of Windows, use
Programs and Features from the Control Panel to uninstall the unwanted version of the product.

1642
Message: The upgrade patch cannot be installed by the Windows Installer service because the
program to be upgraded may be missing, or the upgrade patch may update a different version of
the program. Verify that the program to be upgraded exists on your computer and that you have
the correct upgrade patch

Additional information for error resolution: Verify the device meets the product versioning
prerequisites for the installation.

Windows errors
                                                                                             ﾉ    Expand table

 Error code     Error         Error message
                source

 1              Windows       Incorrect function

 2              Windows       The system cannot find the file specified

 692            Windows       Debugger terminated process

 0x80000003     Windows       One or more arguments are invalid

 0x80000007L    Windows       Operation aborted

 0x80000009     Windows       General access denied error

 0x80004005     Windows       Unspecified error

 0x8000FFFF     Windows       Catastrophic failure

 0x80040154     Windows       Class not registered

 0x80091007     Windows       The hash value is not correct

 0xC0000142     Windows       Initialization of the dynamic link library failed. The process is terminating
                              abnormally

<!-- p.286 -->

General Windows troubleshooting tips
Use the Windows system error codes list or Download the Microsoft Error Lookup Tool for
looking up additional codes that aren't listed in this article. Using the Windows event logs and
the general troubleshooting tips can also help identify the cause of these errors.

1
Message: Incorrect function

Additional information for error resolution: Review the Windows event logs around the time of
the failure in combination with the installation logs to determine the possible cause of the error.

2
Message: The system cannot find the file specified

Additional information for error resolution:

     If the missing file is a system file, run the System File Checker tool to repair missing or
     corrupted system files     . You can also use /scanfile=file or /verifyfile with the sfc
     command to scan the binary and check if there is any issue with that file.
     If the missing file is an application file, you can repair or uninstall and reinstall the
     application to replace the missing file.
     If you're unsure which file is missing and the logs aren't listing it, you may want to use
     Process Monitor to help identify the problematic file.
        You can launch Process Monitor without capturing events and filters by using
         ProcMon.exe /NoConnect /NoFilter /AcceptEULA

692
Message: Debugger terminated process

Additional information for error resolution: Detach any debuggers attached to the process and
retry the application installation.

0x80000003
Message: One or more arguments are invalid

<!-- p.287 -->

Additional information for error resolution: Review the Windows event logs around the time of
the failure in combination with the installation logs to determine the possible cause of the error.

0x80000007L
Message: Operation aborted

Additional information for error resolution: Use the installation logs and Configuration Manager
application logs to determine why installation stopped. Merge the logs so you can easily review
what happened before the 0x80000007L error. Use eventvwr.msc to review the Windows event
logs for additional events that occurred around the time of the installation failure.

0x80000009
Message: General access denied error

Additional information for error resolution: If the issue isn't clear from the logs, using
eventvwr.msc to review Windows event logs and Process Monitor can help identify problematic

files or processes. If needed, use the Windows user interface or icacls to modify permissions on
the problematic file.

Additional tips for file permissions in Windows operating systems:

      Deny permissions always take precedence over Allow permissions.
      Explicit permissions take precedence over inherited permissions.
      If NTFS permissions conflict, or example, if group and user permissions are contradictory,
      the most liberal permissions take precedence.
      Permissions are cumulative.

0x80004005
Message: Unspecified error

Additional information for error resolution: Use the installation logs and Configuration Manager
application logs to determine why installation stopped. Merge the logs so you can easily review
what happened before the 0x80004005 error. Use eventvwr.msc to review the Windows event
logs for additional events that occurred around the time of the installation failure. Follow the
application troubleshooting guide to help resolve the error. Process Monitor can also help
identify the failure.

0x8000FFFF

<!-- p.288 -->

Message: Catastrophic failure

Additional information for error resolution: Review the Windows event logs around the time of
the failure in combination with the installation logs to determine the possible cause of the error.

0x80040154
Message: Class not registered

Additional information for error resolution: This is typically a configuration-related DCOM error.
Review DCOM configuration settings using dcomconfig. If there's a problematic .dll file, you can
use regsvr32 to register the dll file and try the install again. A large number of problematic files
could be a sign of an underlying issue that needs to be resolved before you can install the
application.

0x80091007
Message: The hash value is not correct

Additional information for error resolution: The hash of a file isn't correct and the installation
can't complete. Typically you will see this error in the CAS.log. Check to see if file contents for the
application were recently updated. There may be an issue with the package, in some cases you
may need to rebuild and redistribute it. This issue can also happen if there is a sharing violation
on a file, such as a security application scanning the file. Configuration Manager expects exclusive
access to the file during a hash check. You can identify the problematic process by running a
Process Monitor and adding a filter. The condition to be met is if the Result contains Sharing
Violation then Include the event.

0xC0000142
Message: Initialization of the dynamic link library failed. The process is terminating abnormally

Additional information for error resolution: If there is a problematic .dll file, you can use
regsvr32 to register the dll file and try again. A large number of problematic files could be a sign
of an underlying issue that needs to be resolved before you can install the application.

Windows Management Instrumentation (WMI) errors
                                                                                     ﾉ   Expand table

<!-- p.289 -->

 Error code     Error source                                     Error message

 0x80041001     Windows Management Instrumentation (WMI)         WBEM_E_FAILED

 0x80041009     Windows Management Instrumentation (WMI)         WBEM_E_NOT_AVAILABLE

 0x8004100E     Windows Management Instrumentation (WMI)         WBEM_E_INVALID_NAMESPACE

General WMI troubleshooting tips
Problematic namespaces can typically be found in the Configuration Manager log files and the
WMI logging. WMI relies on Component Object Model (COM)/Distributed Component Object
Model (DCOM), the registry, the file system, and Remote Procedure Call (RPC). DCOM
registrations and permissions are critical for WMI operations to be successful. You can review
DCOM configuration settings using dcomconfig.

When troubleshooting WMI problems, typically you start by verifying that the needed
namespaces, classes, and instances exists in the WMI repository and can be accessed.

Verify the namespace exists on the target first by running wmimgmt.msc from an elevated
command prompt. When WMI Control launches:

   1. Select Action then Properties.
   2. Select the Security tab to see all the namespaces.
   3. Navigate to the namespace in question.
   4. Verify the namespace exists and review the security on the namespace.

To connect WMI Control to another computer:

   1. Select Action then Connect to another computer.
   2. Select the option for Another computer: then supply the name.
   3. Select Properties to connect. The connection to the WMI repository on the remote
     computer doesn't occur until you select Properties.
   4. Verify the namespace exists and review the security on the namespace.
   5. You may also wish to try to connect with the IP address too to verify that you can connect.

Verify the namespace exists on the target and that you can query it properly. Run the Windows
Management Instrument Tester from an elevated command prompt by typing in wbemtest . When
the Windows Management Instrument Tester launches:

   1. Select Connect...

<!-- p.290 -->

   2. Type in the problematic namespace such as root\cimv2 or root\ccm and user credentials if
     needed. To connect to another machine, supply the name or the IP address such as
      \\Machine1\root\ccm and credentials if needed.

   3. Select Enum Classes... to verify you get classes listed for the problematic namespace.
   4. Set the superclass info to Recursive and select OK to verify classes list for the problematic
     namespace.
   5. Launch the object editor for one of the classes by double-clicking on it.

           If you're using the root\ccm namespace, select a class that starts with "CCM_" such as
           CCM_ClientIdentificationInformation.
           If you're using root\cimv2 , choose one that starts with "Win32_" such as Win32_BIOS.

   6. Select Instances to verify the instances of the selected class load. For some classes, it's ok if
     there aren't any instances, just make sure that the Query Result window states Done. Long
     running queries to list of instances or queries that never finish may indicate a problem.

Verify the repository:

   1. From an elevated command prompt, run winmgmt /verifyrepository . Verifying is typically
     useful for invalid class errors especially if you had to recently recompile a .mof file using
     mofcomp.
   2. If problems are found during verification, you can try to salvage using winmgmt
     /salvagerepository

   3. Typically, you won't use /resetrepository unless it's truly needed an no other alternative
     exists. Some namespaces won't automatically rebuild and you'll need to either reinstall the
     software associated with the missing namespace or mofcomp the application's .mof files to
     rebuild them.

WMI resources:

     Introduction to wbemtest
     Winmgmt service
     WMI Log Files
     Enable trace and debug logging for WMI events
        Ensure you change the default log size to cover your troubleshooting session.
        Once you have finished troubleshooting, remember to disable the trace and debug
        logging.
     Setting namespace security with the WMI Control
     WMI troubleshooting
     Ask The Performance Team: WMI

<!-- p.291 -->

0x80041001
Message: WBEM_E_FAILED

Additional information for error resolution: WBEM_E_FAILED is a generic WMI failure error. The
error can be caused by a number of things. The error will sometimes tell you which method or
instance failed. You'll probably also see related log entires around the same time if you merge
logs together based on similar function. For instance, if you see the error related to content for
an application, you may want to merge together CAS.log, ContentTransferManager.log and
DataTransfer.log. If the error happened on a site server not a client, you may want to review
SMSProv.log for additional information. Use the General WMI troubleshooting tips to help
identify the issue along with the application installation logs.

0x80041009
Message: WBEM_E_NOT_AVAILABLE

Additional information for error resolution: The resource, in many cases a remote machine, isn't
currently available. Verify the device is online. Use the General WMI troubleshooting tips to help
verify connectivity to WMI on the device.

0x8004100E
Message: WBEM_E_INVALID_NAMESPACE

Additional information for error resolution: The namespace specified could not be found. Verify
the target computer can connect to WMI by following the General WMI troubleshooting tips.
Verify namespace specified exists.

Windows Update Agent errors
                                                                                         ﾉ   Expand table

 Error code   Error source            Error message

 0x00240006   Windows Update          The update to be installed is already installed on the system
              Agent

 0x80240017   Windows Update          Operation was not performed because there are no applicable
              Agent                   updates

General Windows Update Agent troubleshooting tips

<!-- p.292 -->

The errors for the installation originated from the Windows Update Agent. In many cases, you
can attempt to install these updates using the built-in software update management from
Configuration Manager, Windows Update client policies, or Microsoft Update. In certain
circumstances where it's not feasible to use your regular patching mechanism, the .msu package
can be installed with the Windows Update Standalone Installer (wusa.exe)      like an application.
Use the Windows Update logging and general troubleshooting tips to help determine the cause
of the issue.

0x00240006
Message: The update to be installed is already installed on the system

Additional information for error resolution: The update is already installed on the device.

0x80240017
Message: Operation was not performed because there are no applicable updates

Additional information for error resolution: The update isn't applicable to the device. Verify that
the device meets the requirements of the update. In cases where a superseding update has been
installed, it's very rare that the superseded update would be applicable to the device.

 Last updated on 02/22/2023

<!-- p.293 -->

Troubleshoot the Microsoft Store for
Business and Education integration with
Configuration Manager
This article provides key troubleshooting tips and fixes for some of the top issues that you may
have with the Microsoft Store for Business and Education (MSfB) integration with Configuration
Manager.

For more information about using the Microsoft Store for Business and Education with
Configuration Manager, see Manage apps from the Microsoft Store for Business and Education
with Configuration Manager.

Monitor
Component status
In the Configuration Manager console, go to the Monitoring workspace, expand System Status,
and select the Component Status node. Monitor status of the following components:

     SMS_BUSINESS_APP_PROCESS_MANAGER
     SMS_CLOUDCONNECTION

Sync status
In the Configuration Manager console, go to the Administration workspace, expand Cloud
Services, and select the Microsoft Store for Business node. Check the Last Sync Status column.

View synchronized apps
In the Configuration Manager console, go to the Software Library workspace, expand
Application Management, and select the License Information for Store Apps node.

Log files
WSfBSyncWorker.log

<!-- p.294 -->

This log file is located on the service connection point, under \Logs in the Configuration Manager
installation directory. It records information about the communication with the cloud service. This
information includes metadata, icons, packages, and license file retrieval.

  ） Important

  This section, method, or task contains steps that tell you how to modify the registry.
  However, serious problems might occur if you modify the registry incorrectly. Therefore,
  make sure that you follow these steps carefully. For protection, back up the registry before
  you modify it so that you can restore it if a problem occurs. For more information about how
  to back up and restore the registry, see How to back up and restore the registry in
  Windows      .

To change the log level, change the LoggingLevel value to 0 in the
HKLM\SOFTWARE\Microsoft\SMS\Tracing\SMS_CLOUDCONNECTION registry subkey. For more

information, see Configure logging options.

SMS_CLOUDCONNECTION.log
This log file is located on the service connection point, under \Logs in the Configuration Manager
installation directory. If the WSfBSyncWorker service isn't started, or repeatedly starts and stops,
review the entries in this log file.

  ７ Note

  This log file is shared with other features.

BusinessAppProcessWorker.log
This log file is located on the site server for the top-level site in the hierarchy. It's under \Logs in
the Configuration Manager installation directory. It records information about the following
processes:

      Insert the metadata information synced by the BusinessAppProcessWorker component into
      the database
      Process files in \InstallDir\inboxes\businessappprocess.box

SMS_BUSINESS_APP_PROCESS_MANAGER.log

<!-- p.295 -->

This log file is located on the site server for the top-level site in the hierarchy. It's under \Logs in
the Configuration Manager installation directory. If the BusinessAppProcessWorker service isn't
started, or repeatedly starts and stops, review the entries in this log file.

Last sync failed
When the last sync status is failed, start by reviewing the following log files to identify the
symptom:

     WSfbSyncWorker.log
     SMS_CLOUDCONNECTION.log

Then look at one of the following sections for common issues:

     Authorization error
     The secret key is invalid
     Error getting application token
     Content location doesn't exist or incorrect permissions
     Error occurred making http request calling 'GET' method
     Cannot write more bytes to the buffer
     Online application download fails with 0x8024500c

Authorization error
Cause

This issue can occur if the configured Microsoft Entra application doesn't have permissions to
manage the Microsoft Store for Business and Education for this tenant.

Workaround

   1. Sign in as an administrator to the Microsoft Store for Business or Education portal.
   2. Go to Settings, and select Management tools.
   3. If the application isn't listed, select Add a management tool. Then search by name and
     select the Microsoft Entra application associated with the same ClientID as Configuration
     Manager.
   4. If the status doesn't show Active, then select Activate in the Action section.
   5. In the Configuration Manager console, go to the Administration workspace, expand Cloud
     Services, and select the Microsoft Store for Business node. Synchronize with the store, or
     wait for the next sync interval to occur.

<!-- p.296 -->

   Tip

  To find the ClientID in Configuration Manager, follow these steps:

       1. In the Configuration Manager console, go to the Administration workspace, expand
         Cloud Services, and select the Microsoft Entra Tennts node.
       2. Select the tenant that you use for the Microsoft Store for Business and Education
         integration.
       3. In the results pane, find the matching application, and look at the Client ID column.

The secret key is invalid
Cause

This issue can occur if the secret key has expired on the Microsoft Entra app for the Microsoft
Store for Business and Education configuration.

Resolution

Renew the secret key for the Microsoft Entra application. For more information, see Renew secret
key.

Error getting application token
Cause

This issue can occur if the connected app no longer exists in Microsoft Entra ID.

Resolution

Delete and recreate the connection to the Microsoft Store for Business and Education.

   1. In the Configuration Manager console, go to the Administration workspace, expand Cloud
       Services, and select the Microsoft Store for Business node.
   2. Select the existing connection.
   3. Select Delete in the ribbon.

Then recreate the connection. For more information, see the following articles:

       Configure Azure Services
       Set up Microsoft Store for Business and Education synchronization

<!-- p.297 -->

Content location doesn't exist or incorrect permissions
Cause

When you set up the Microsoft Store for Business and Education connection, you specify a
network share for storing synchronized content. This issue can occur if this share doesn't exist or
has incorrect permissions. The computer account for the service connection point should be the
owner of this directory and any sub-directories. If it isn't, you'll see an error similar to the
following error:

 Output

 Failed to download package d788cc1b-ab00-bb5f-1548-f2dfe717583b-X86-Arm for product
 9WZDNCRFJ3PS\0015.
 System.IO.IOException: This security ID may not be assigned as the owner of this
 object.

To see the location that you configured:

   1. In the Configuration Manager console, go to the Administration workspace, expand Cloud
     Services, and select the Microsoft Store for Business node.

   2. Select the account and open its Properties.

   3. Switch to the Configuration tab. The Location setting shows the network path to store
     application content downloaded from the Microsoft Store for Business and Education.

Workaround

   1. If it doesn't already exist, create the share.

   2. Check NTFS permissions on the folder, and the permissions on the network share. Grant the
     computer account of the service connection point Read and Write permissions.

If you want to reconfigure the location, delete and recreate the connection with the new content
location.

Error occurred making http request calling 'GET' method
Cause

This issue can occur if the sync of applications from the store took so long that the content URL
expired.

<!-- p.298 -->

Workaround

Retry the sync process

   1. In the Configuration Manager console, go to the Administration workspace, expand Cloud
     Services, and select the Microsoft Store for Business node.
   2. Select the connection. In the ribbon, select Sync from Microsoft Store for Business.

With each time, it should continue further. It may take several retries depending on the following
factors:

     The number of offline applications
     The size of the packages
     The network speed

With each attempt, you should see the error fewer times. If the number of errors doesn't reduce,
there's another issue.

Cannot write more bytes to the buffer
Cause

This issue can occur if the application's package is larger than 500 MB. Configuration Manager
only supports automatic synchronization of offline applications with packages less than 500 MB.

Workaround

You can't automatically sync these apps, but you can download the content, and manually create
the application:

   1. Get the failing application ID from the following line in WSfbSynWorker.log:

       Output

       Error(s) syncing or downloading application <ApplicationID> from the Microsoft
       Store for Business.

   2. Sign in as an administrator to the Microsoft Store for Business or Education portal. Find the
     page for this application.

            Tip

<!-- p.299 -->

          The URL for the page is similar to: https://businessstore.microsoft.com/en-
          us/store/p/app/ApplicationID .

      a. Select Offline, if it isn't already selected. Then select Manage.

      b. Create a separate folder on your application content share for all supported platforms.

      c. Download the package to the package folder.

      d. Download the encoded license file as a .bin file to the package folder.

      e. Download all required frameworks to the package folder.

   3. In the Configuration Manager console, go to the Software Library workspace, expand
     Application Management, and select the Applications node.

   4. Create an application, manually specifying the application information.

      a. Create a deployment type for each supported platform that you previously downloaded.

      b. Type: Windows app package (*.appx, *.appxbundle)

      c. Specify the appx/appxbundle for the actual app package, not a required dependency
          package.

Confirm the following details on the final Import Information page:

     License file: Specifies the .bin file. This license file is required for offline apps.
     Windows app dependencies: Verify that all of the required dependencies are downloaded
     for this package.

Online application download fails with 0x8024500c
Cause

An 0x8024500c error during download is typically caused by the Do not connect to any Windows
Update Internet locations group policy that blocks Windows Update access.

Workaround

Don't enable the Do not connect to any Windows Update Internet locations group policy
object.

<!-- p.300 -->

Sync doesn't run
This section covers the following sync issues:

     You manually start the sync process, but it doesn't run
     The site doesn't automatically sync each day

Start by reviewing the following log files to identify the symptom:

     BusinessAppProcessWorker.log
     SMS_BUSINESS_APP_PROCESS_MANAGER.log
     WsfbSyncWorker.log
     SMS_CLOUDCONNECTION.log

Then look at one of the following sections for common issues:

     Manual sync doesn't start
     Automatic daily sync doesn't run and "shutting down # workers" error in
     SMS_BUSINESS_APP_PROCESS_MANAGER.log

Manual sync doesn't start
Cause

This issue can occur if you start a sync less than 10 minutes after the previous sync. You can't sync
more frequently than every 10 minutes.

Resolution

Wait for at least 10 minutes before starting another sync.

Automatic daily sync doesn't run and "shutting down #
workers" error in SMS_BUSINESS_APP_PROCESS_MANAGER.log
Cause

This issue can occur if the SMS_BUSINESS_APP_PROCESS_MANAGER component stops the
WsfbSyncWorker thread. The error may specify either 2 or 4 workers.

Workaround

Restart the SMS_EXECUTIVE service.

<!-- p.301 -->

If you're not able to restart that main service, stop both components with MSfB workers, and then
start both.

  ） Important

  This section, method, or task contains steps that tell you how to modify the registry.
  However, serious problems might occur if you modify the registry incorrectly. Therefore,
  make sure that you follow these steps carefully. For protection, back up the registry before
  you modify it so that you can restore it if a problem occurs. For more information about how
  to back up and restore the registry, see How to back up and restore the registry in
  Windows      .

   1. Open the Windows registry on the server that runs the service connection point

   2. Go to HKLM\SOFTWARE\Microsoft\SMS\COMPONENTS\SMS_EXECUTIVE\Threads\SMS_CLOUDCONNECTION

      a. Set Requested Operation to Stop .

      b. Refresh to verify Current State = Stopped .

   3. Go to
      HKLM\SOFTWARE\Microsoft\SMS\COMPONENTS\SMS_EXECUTIVE\Threads\SMS_BUSINESS_APP_PROCESS_

     MANAGER

      a. Set Requested Operation to Stop .

      b. Refresh to verify Current State = Stopped .

   4. In SMS_CLOUDCONNECTION , set Requested Operation to Start .

   5. In SMS_BUSINESS_APP_PROCESS_MANAGER , set Requested Operation to Start .

Language-related issues
This section includes the following common issues:

     Language selection changes aren't applied
     Not all selected languages are present for all license information

Language selection changes aren't applied
Cause

<!-- p.302 -->

This issue can occur if the language selection is cached, and isn't cleared after the property values
are changed.

Workaround

To resolve this problem, restart the SMS_Executive service.

Not all selected languages are present for all
license information
Cause

This issue can occur if the Microsoft Store for Business and Education application's license
information doesn't contain localized data for the specified language.

Workaround

Manually add any missing languages for created applications.

Offline applications
This section includes the following common issues:

         Fail to create offline application because content can't be verified
         Fail to install application created from offline license information

Fail to create offline application because content can't
be verified
Cause

This issue can occur if the synchronized content for the offline application is corrupt or modified.

Workaround

Start a new sync. When the sync completes, it should verify and download any incorrect content
files.

Fail to install application created from offline
license information

<!-- p.303 -->

Cause

This issue can occur if you deploy the application to a client running a version of Windows 10
earlier than version 1511. Offline licensed apps from the Microsoft Store for Business and
Education are only supported on Windows 10 version 1511 and later.

Resolution

Install the latest version of Windows 10.

Next steps
To find additional help, see Find help for using Configuration Manager.

 Last updated on 03/30/2026

<!-- p.304 -->

Troubleshoot Package Conversion
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the information in this article to help you troubleshoot problems when using
Package Conversion Manager.

SMS Provider
Package Conversion Manager uses the SMS Provider. For more information, see Plan for
the SMS Provider.

If the SMS Provider isn't working properly, the Configuration Manager console including
the Package Conversion Manager doesn't work.

Package readiness
Before converting a package to an application, analyze the package using the Package
Conversion Manager Analyze function. After the analysis, add the Readiness column in
the Packages node of the Configuration Manager console. The list of packages displays
one of the following readiness states of the analyzed package:

      Automatic: The package can be directly converted using the Convert function.

        ７ Note

        An automatic conversion doesn't convert WQL queries into application
        requirements. Use the Fix and Convert process to convert these queries.

      Manual: The package needs some additions or changes before you can convert it
      using the Fix and Convert function.

      Not Applicable: The package isn't suitable for conversion. Either correct any
      problems with the package, or continue to deploy it as a package.

      Error: The package contains errors. Manually correct these errors before you can
      analyze and convert it.

<!-- p.305 -->

The details pane of the Packages node in the Configuration Manager console shows any
readiness issues. Select a package, and then select the Summary tab in the details pane.

Log files

Enable logging
When you enable logging for Package Conversion Manager, it logs all of its actions,
exceptions, and errors.

To enable logging for this component in the Configuration Manager, modify
Microsoft.ConfigurationManagement.exe.Config. By default, this configuration file is
located in the following path:
C:\Program Files (x86)\Microsoft Endpoint

Manager\AdminConsole\bin\Microsoft.ConfigurationManagement.exe.config

  ） Important

  Starting in version 1910, this path changed to use the Microsoft Endpoint Manager
  folder. Make sure you don't use an older version of the file that might exist in
  another folder.

Insert the following switches and trace XML elements in the system.diagnostics
element after the last sources element:

  XML

  </sources>

      <switches>
        <add name="PcmLogging" value="3"/>
      </switches>
      <trace autoflush="true" indentsize="4">
        <listeners>
          <add name="PcmTraceListener"
  type="Microsoft.ConfigurationManagement.UserCentric.Logging.RolloverLogTrace
  Listener, Microsoft.ConfigurationManagement.UserCentric.Logging"
  initializeData="%UserProfile%\AppData\Local\Temp\PcmTrace.log"/>
        </listeners>
      </trace>

  </system.diagnostics>

<!-- p.306 -->

This sample uses the file PCMTrace.log. This log is on the computer running the
Configuration Manager console in the following path:
%UserProfile%\AppData\Local\Temp

To configure the level of detail, change the PcmLogging trace switch setting. Set the this
value to four levels of detail, from least detailed ( 1 ) to most detailed ( 4 ).

SMSProv.log
In some situations, information relevant to troubleshooting the package conversion
process is in the SMSProv.log file. This file captures information from the Configuration
Manager SMS Provider.

By default, this log file is located on the Configuration Manager site server at the
following path:
C:\Program Files\Microsoft Configuration Manager\Logs

If you see one of the following error messages, the SMSProv.log file may contain
relevant troubleshooting information:

      The SMS Provider reported an error

      Generic Failure

These error messages typically indicate that an error occurred on the site server, and
that the error information wasn't sent to the Configuration Manager console.

For more information, see Technical reference for Package Conversion Manager error
messages.

Changing package attributes after analysis
After you analyze a package and it has a readiness state of Automatic or Manual, the
conversion process might fail if you change any of the relevant attributes.

For example, you analyze a package and its readiness state is Automatic. Then you add
another program to the package. The package conversion might fail.

If you need to make changes to a package after analysis, rerun analysis before
conversion.

See also

<!-- p.307 -->

Technical reference for Package Conversion Manager error messages

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.308 -->

Technical reference for Package
Conversion Manager error messages
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article describes the error messages that Package Conversion Manager displays. It
also includes the possible causes of the error, and methods to correct the error. Package
Conversion Manager logs error messages in PCMTrace.log. For more information,
including how to control the verbosity level, see Log files.

Application creation failed with the following exception
The specified exception occurred during the submission of the application object to the
Configuration Manager server.

Check your permissions in Configuration Manager, validate your connectivity, and then
retry. If those actions don't fix the problem, examine the PCMtrace.log file (verbosity
level 4) and SMSProv.log.

Conversion Error – APPLIES TO A PACKAGE TRANSFORM STATUS

A general exception occurred during the conversion of the package. Look in the
PCMtrace.log file (verbosity level 4).

Check the user permissions for the network share (package data source), validate your
connectivity, and then retry. If those actions don't fix the problem, examine the
PCMtrace.log file (verbosity level 4).

Did not find a converted package and its resultant application in
the workflow outputs

The application (converted package/program) was deleted.

Modify the dependent package/program to ensure that the dependent
package/program exists.

Objects were not created successfully

There are several possible causes.

<!-- p.309 -->

Check your permissions in Configuration Manager, validate your connectivity, and then
retry. If those actions don't fix the problem, examine the PCMtrace.log file (verbosity
level 4) and the SMSProv.log file.

Please close the wizard and resolve any issues with the selected
package. See PCMTrace.Log for more details

There are several possible causes.

Check your permissions in Configuration Manager, validate your connectivity, and then
retry. If those actions don't fix the problem, examine the PCMtrace.log file (verbosity
level 4) and the SMSProv.log file.

Some Deployment Types are missing Detection Methods. All
Deployment Types must have Detection Methods
Detection methods are missing from the program.

Add one or more detection methods during the Fix and Convert process.

There was an error preparing the package for conversion

There are several possible causes.

Check your permissions in Configuration Manager, validate your connectivity, and then
retry. If those actions don't fix the problem, examine the PCMtrace.log file (verbosity
level 4) and the SMSProv.log file.

Feedback
Was this page helpful?      Yes    No

Provide product feedback
