---
title: "Core infrastructure documentation — pages 1481-1520"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1481-1520
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1481-1520
family: sccm
documentKind: "doc"
abstract: "For information about sharing and using Power BI report templates with Community hub, see Integrate with Power BI Report Server. Console extensions are available for download, but contributions are currently limited Content for console extensions isn't hosted by Microsoft. Curre"
---

# Core infrastructure documentation — pages 1481-1520

<!-- p.1481 -->

             For information about sharing and using Power BI report templates with
             Community hub, see Integrate with Power BI Report Server.
          Console extensions are available for download, but contributions are
          currently limited
             Content for console extensions isn't hosted by Microsoft. Currently, the
             source download location displays in the verbose SmsAdminUi.log for the
             console that initiates the download.

  4. Select Browse to load your environment's object list for the selected type. The
     object's Name and Description (if available) will automatically load in the
     contribution wizard.

  5. Edit the following information to reflect what the community should see for your
     contribution:

          Name: Name of your object
          Description: The description of the object you're contributing.

  6. On the Organization page, select the GitHub Organization to use for organization
     branding if needed.

          None is the default.
          If your organization isn't listed, verify that the membership visibility   is set
          to Public in your GitHub profile.

  7. Select Next to submit the contribution.

  8. Once the contribution is complete, you'll see the GitHub pull request (PR) link. The
     link is also emailed to you. You can paste the link into a browser to view the PR.
     Your PR will go though the standard GitHub merge process.

          PRs should be submitted through the Configuration Manager console, not
          directly to the GitHub repository.

  9. Choose Close to exit the contribution wizard.

 10. Once the PR has been completed and merged, the new item will display in the
     Community hub home page for others to see.

Update contributed content
You can update content you've contributed to the Community hub.

<!-- p.1482 -->

   1. Select an item that you previously contributed. Currently, you can only edit items
     that you contributed.
   2. In the item details, select Push Update to open the contribute item wizard.
   3. Edit the Description of the item to note what changes were made.
   4. Select Next to upload the item.
   5. Once the item is uploaded, you'll be given the pull request URL of the change for
     monitoring.
   6. Select Close when you're done to exit the wizard.

Delete a contribution you made
You can delete contributions you've made if you no longer want it to be displayed in the
Community hub. There are two ways to delete your contributions.

Method 1:

   1. Go to Community > Community hub > Your hub.
   2. From the item you want to delete, select Delete in the far-right column.

Method 2:

If the pull request was never completed (merged) into the GitHub repository, then you
can just close the pull request. Ensure that you're signed into GitHub with the same
GitHub account that you used to create the pull request.

Personalization and organization branding of
contributed content
Starting in January 2021, your contributions are personalized. By default, your
contributions include your personal GitHub profile picture. The default GitHub
Identicon   is used if you don't have a profile picture. All contributions you've
submitted before January 2021 are automatically personalized using this default.

<!-- p.1483 -->

Community hub also allows new contributions to be branded instead of using the
default personalization. You can brand a contribution to one of your organization
memberships in GitHub that's publicly visible. When you choose to brand your
contribution, the organization's profile picture is used rather than your personal profile
picture. The organization's web page, Twitter handle, and company bio are included on
the contribution. Branding to the organization identity allows for uniformity regardless
of which user is submitting the contribution.

To use branding:

     The visibility of the organization membership     must be set to Public from the
     contributor's GitHub profile.
     On the Organization page in the Contribute item wizard, select the GitHub
     Organization to use for branding. For more information, see the Contribute
     content section.

Directly link to Community hub items
(Introduced in version 2006)

You can navigate to and reference items in the Configuration Manager console
Community hub node with a direct link. Collaborate with your colleagues easily by

<!-- p.1484 -->

sharing direct links to Community hub items. These deep links are currently only for
items in the Community hub node of the console.

Prerequisites for direct links:

     Configuration Manager console version 2006 or later

Share an item:

   1. Go the item in the hub and select Share.
   2. Paste the copied link and share it with others.

Open a shared link:

   1. Open the link from a machine that has the Configuration Manager console
     installed.
   2. Select Launch the Community hub when prompted.
   3. The console opens directly to the script in the Community hub node.

Publish query to Community hub from
CMPivot
(Applies to version 2107 or later)

Starting in version 2107, you can publish a CMPivot query to the Community hub
directly from the CMPivot window. Submitting your queries directly through CMPivot
makes contributing to the Community hub easier.

You'll need the following requirements for CMPivot and for contributing to the
Community hub:

     Meet all of the CMPivot prerequisites and permissions
     Enable Community hub.
         If needed, install the Microsoft Edge WebView2 extension from the
         Configuration Manager console notification.
     A GitHub account that's joined to Community hub
         You must accept the invitation sent in the email otherwise you won't be able to
         contribute content.

   1. Go to the Assets and Compliance workspace then select the Device Collections
     node.

   2. Select a target collection, target device, or group of devices then select Start
     CMPivot in the ribbon to launch the tool.

<!-- p.1485 -->

3. From the CMPivot window, select the Community hub icon on the menu.

4. Select Sign in, then sign into GitHub.

5. Create a CMPivot query, then select Run Query to verify it functions as expected.

        Optionally, select the folder icon to access your favorites list to use a query
        you've already created.

6. Select the Publish link at top of CMPivot's Community hub window when you're
  ready to submit your query.

7. Give your query a Name and Description, then select the Publish button to send
  your query to the Community hub.

<!-- p.1486 -->

   8. Once the contribution is complete, you can access your query anytime from the
     Me tab.

   9. To view the GitHub pull request (PR), go to
     https://github.com/Microsoft/configmgr-hub/pulls        . You can also access the PR
     link from the Your hub page in the Community hub node.

           PRs shouldn't be submitted directly to the GitHub repository.

  ７ Note

        Currently, when you publish a query through CMPivot, you can't edit or delete
        it after publishing.
        Community hub is only available in CMPivot when you run it from the
        Configuration Manager console. Community hub isn't available from
        standalone CMPivot.

Object type information

Configuration baselines
When you contribute a configuration baseline, each of the child configuration items is
verified. The verification starts at the lowest nested level. This means that configuration
items that are grandchildren are verified before direct child configuration items are. You
can have up to 50 child configuration items and up to 4 nested levels. The following
process occurs to ensure the configuration baseline is usable and complete:

   1. Check if the child configuration item is already in the Community hub. If the
     configuration item doesn't exist, it's created.

           A configuration item with software updates or version-specific references will
           cause an error and the contribution will fail.

   2. If the configuration item already exists in the Community hub, verify the
     contributor is the author. If the contributor isn't the author, a new configuration
     item is created in Community hub.
   3. If the contributor is the author, check for local updates to the configuration item. If
     the configuration item changed, update the item in the Community hub.

Console extensions

<!-- p.1487 -->

You contribute extensions the same way you would any other community hub object.
However, for there are additional requirements and additional information you need to
supply for an extension. When you contribute a console extension to Community hub,
the content must be signed. Content for console extensions isn't hosted by Microsoft.
When you contribute your item, you'll be asked to provide a location to the signed .cab
file along with other information for the extension. The following items are required for
contributing extensions:

     Content URL: Location for the downloadable .cab file
     SHA-256 hash of the content: SHA-256 hash of the .cab file
     License URL: URL of the license for the extension, such as https://mit-license.org/
     Privacy statement URL: URL of your privacy statement

Next steps
Learn more about creating and using the following objects:

     Create and run PowerShell scripts
     Introduction to reporting
     Create and manage task sequences
     Create and deploy an application
     Create configuration items
     Create and contribute console extensions

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1488 -->

Console extensions from Community
hub
Article • 10/31/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in March 2023, this feature of Configuration Manager is being removed. All
  future versions, starting with 2303 will not have the Community hub node in the
  admin console. The Community hub node in older versions will be redirected to
  deprecated features.

When you use Configuration Manager version 2103 or later, you can download console
extensions from the Community hub and have it applied to all consoles connected to a
hierarchy. The Console extensions node allows you to start managing the approval and
installation of console extensions used in your environment. Getting an extension from
community hub doesn't make it immediately available. First, an administrator has to
approve the extension for the site. Then console users can install the extension to their
local console.

After you approve an extension, when you open the console, you'll see a console
notification. From the notification, you can start the extension installer. After the installer
completes, the console restarts automatically, and then you can use the extension.

Find extensions in Community hub
Extensions in Community hub are recognizable by their icon. When browsing All objects
in the Community hub, you can easily notice if a new extension has been added.The
following icon is used for extensions:

<!-- p.1489 -->

You can also use a search filter to find an extension in Community hub. Start with the
search filter for type:extension , then add additional filters as needed. If you're not
finding an extension that's known to be available, double check the displayed categories
hierarchy setting for Community hub.

                                                                            ﾉ   Expand table

 Filter name            Example search                             Uses a like filter

 Type                   type:report                                Yes

 Curated                curated:false                              No

 User                   user:<GitHubUserName>                      No

 Organization           org:<GitHubOrganizationName>               No

 Name                   name:test_report                           Yes

 Description            desc:description                           Yes

When filtering Community hub items in search:

        The filtering on some items is done using like so you don't need to know the
        exact name of an item you are trying to find. For instance, using type:task would
        return task sequences.
        You can't use the same filter twice in a search. For instance, using type:report and
        type:extension would only return reports since the second filter gets ignored.

<!-- p.1490 -->

     Search filtering respects the hierarchy setting for displaying Community hub
     content categories.
        If your hierarchy is set to Display Microsoft and curated community content,
        then curated:false is ignored.
        If your hierarchy is set to Display Microsoft content, then the curated: filter is
        ignored.
     Starting in version 2203, the console displays a list of search filters you can use in
     Community hub.

Download and deploy the extension
You'll download the extension from Community hub, then use the Console Extensions
node to test the extension and deploy it to other Configuration Manager console users.
In-depth instructions for the deployment process and managing extensions can be
found in the Console Extensions article. Below is a high-level overview of the extension
deployment process:

   1. Once you've found an extension in Community hub that you want in your
     environment, select Download.
   2. The downloaded extension will appear in the Console Extensions node.
   3. Change the security scope for the extension, approve it, then install and test it on a
     local console. For more information on this process, see Install and test an
     extension on a local console.
   4. When testing is complete, enable user notifications for installation.

Console extension installation notifications
Users are notified when console extensions are approved for installation. These
notifications occur for users in the following scenarios:

     The Configuration Manager console requires a built-in extension, such as
     WebView2, to be installed or updated.

<!-- p.1491 -->

  Console extensions are approved and notifications are enabled from
  Administration > Overview > Updates and Servicing > Console Extensions.
     When notifications are enabled, users within the security scope for the
     extension receive the following prompts:

1. In the upper-right corner of the console, select the bell icon to display
  Configuration Manager console notifications.

2. The notification will say New custom console extensions are available.

3. Select the link Install custom console extensions to launch the install.

4. When the install completes, select Close to restart the console and enable the new
  extension.

７ Note

<!-- p.1492 -->

  When you upgrade to Configuration Manager 2107, you will be prompted to install
  the WebView2 console extension again. For more information about the WebView2
  installation, see the WebView2 installation section if the Community hub article.

Next steps
     Manage console extensions
     Import console extensions
     Create and contribute your own console extension

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1493 -->

CMPivot overview
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

CMPivot allows you to quickly assess the state of devices in your environment and take
action. When you enter a query, CMPivot will run a query in real time on all currently
connected devices in the selected collection. The data returned can then be filtered,
grouped, and refined to answer business questions, troubleshoot issues in your
environment, or respond to security threats. For more information about using CMPivot,
see Use CMPivot.

Queries
Queries can be used to search terms, identify trends, analyze patterns, and provide
many other insights based on your data. CMPivot uses a subset of the Azure Log
Analytics data flow model for the tabular expression statement. The typical structure of a
tabular expression statement is a composition of client entities and tabular data
operators (such as filters and projections). The composition is represented by the pipe
character (|), giving the statement a regular form that visually represents the flow of
tabular data from left to right. Each operator accepts a tabular data set "from the pipe",
and additional inputs (including other tabular data sets) from the body of the operator,
then emits a tabular data set to the next operator that follows: entity | operator1 |
operator2 | ...

In the following example, the entity is CCMRecentlyUsedApplications (a reference to the
recently used applications), and the operator is where (which filter out records from its
input according to some per-record predicate):

  CCMRecentlyUsedApplications | where CompanyName like '%Microsoft%' | project
  CompanyName, ExplorerFileName, LastUsedTime, LaunchCount, FolderPath

Entities
Entities are objects that can be queried from the client. We currently support the
following entities:

<!-- p.1494 -->

                                                                    ﾉ   Expand table

Entity                        Description

AadStatus                     Status of Microsoft Entra ID

Administrators                Members of the local administrators group

AppCrash                      Recent application crash reports

AppVClientApplication         AppV Client Application

AppVClientPackage             AppV Client Package

AutoStartSoftware             Software that starts automatically with, or immediately
                              after, the operating system

BaseBoard                     BaseBoard

Battery                       Battery

Bios                          System BIOS information

BitLocker                     BitLocker

BitLockerEncryptionDetails    BitLocker Encryption Details

BitLockerPolicy               BitLocker Policy

BootConfiguration             Boot Configuration

BrowserHelperObject           Browser Helper Object

BrowserUsage                  Browser Usage

CcmLog()                      Lines within 24 hours (by default) from a Ccm Log file

CCMRAX                        CCM_RAX

CCMRecentlyUsedApplications   Recently Used Applications

CCMWebAppInstallInfo          Web Applications

CDROM                         CDROM Drive

ClientEvents                  Client Events

ComputerSystem                Computer System

ComputerSystemEx              Computer System Ex

ComputerSystemProduct         Computer System Product

ConnectedDevice               Connected Device

<!-- p.1495 -->

Entity                      Description

Connection                  An active Tcp connection in or out of the device

Desktop                     Desktop

DesktopMonitor              Desktop Monitor

Device                      Basic information about the device

Disk                        Local storage device information on a computer system
                            running Windows

DMA                         DMA

DMAChannel                  DMA Channel

DriverVxD                   Driver - VxD

EmbeddedDeviceInformation   Embedded Device Information

Environment                 Environment

EPStatus                    Status of antimalware software on the computer
                            gathered by the Get-MpComputerStatus cmdlet.
                            Supported on Windows 10 and Server 2016, or later
                            with defender running.

EventLog()                  Events within 24 hours (by default) from an event log

File()                      Information about a specific file

FileShare                   Active file share information

Firmware                    Firmware

IDEController               IDE Controller

InstalledExecutable         Installed Executable

InstalledSoftware           An application installed on the device

IPConfig                    Gets network configuration, including usable interfaces,
                            IP addresses, and DNS servers

IRQTable                    IRQ Table

Keyboard                    Keyboard

LoadOrderGroup              Load Order Group

LogicalDisk                 Logical Disk

<!-- p.1496 -->

Entity                                 Description

MDMDevDetail                           Device Information

Memory                                 Memory

Modem                                  Modem

Motherboard                            Motherboard

NetworkAdapter                         Network Adapter

NetworkAdapterConfiguration            Network Adapter Configuration

NetworkClient                          Network Client

NetworkLoginProfile                    Network Login Profile

NTEventlogFile                         NT Eventlog File

Office365ProPlusConfigurations         Office 365 Apps Configurations

OfficeAddin                            Office add-ins

OfficeClientMetric                     Office Client Metric

OfficeDeviceSummary                    Office Device Summary

OfficeDocumentMetric                   Office document metrics

OfficeDocumentSolution                 Office Document Solution

OfficeMacroError                       Office Macro Error

OfficeProductInfo                      Office Product Info

OfficeVbaRuleViolation                 Office Vba Rule Violation

OfficeVbaSummary                       Office VBA scan summary

OperatingSystem                        Operating System

OperatingSystemEx                      Operating System Ex

OperatingSystemRecoveryConfiguration   Operating System Recovery Configuration

OptionalFeature                        Optional Feature

OS                                     Basic information about the operating system

PageFileSetting                        Page File Setting

ParallelPort                           Parallel Port

<!-- p.1497 -->

Entity                           Description

Partition                        Disk Partitions

PCMCIAController                 PCMCIA Controller

PhysicalDisk                     PhysicalDisk

PhysicalMemory                   Physical Memory

PNPDEVICEDRIVER                  PNP Device Driver

PointingDevice                   Pointing Device

PortableBattery                  Portable Battery

Ports                            Ports

PowerCapabilities                Power Capabilities

PowerClientOptOutSettings        Power Management Exclusion Settings

PowerConfigurations              Power Configuration

PowerManagementDaily             Power Management Daily Data

PowerManagementInsomniaReasons   Power Insomnia Reasons

PowerManagementMonthly           Power Management Monthly Data

PowerSettings                    Power Settings

PrinterConfiguration             Printer Configuration

PrinterDevice                    Printer Device

PrintJobs                        Print Jobs

Process                          A process on an operating system

ProcessModule()                  Modules loaded by specified processes

Processor                        Processor

ProtectedVolumeInformation       Protected Volume Information

Protocol                         Protocol

QuickFixEngineering              Quick Fix Engineering

Registry                         All values for a specific registry key

<!-- p.1498 -->

Entity                               Description

                                     Starting in version 2107, Key value was added to the
                                     Registry() entity

SCSIController                       SCSI Controller

SerialPortConfiguration              Serial Port Configuration

SerialPorts                          Serial Ports

ServerFeature                        Server Feature

Service                              A service on a computer system running Windows

Services                             Services

Shares                               Shares

SMBConfig                            SMB Configuration of a device

SMSAdvancedClientPorts               Configuration Manager Client Ports

SMSAdvancedClientSSLConfigurations   Configuration Manager Client SSL Configurations

SMSAdvancedClientState               Configuration Manager Client State

SMSDefaultBrowser                    Default Browser

SMSSoftwareTag                       Software Tag

SMSWindows8Application               Windows app

SMSWindows8ApplicationUserInfo       Windows app User Info

SoftwareShortcut                     Software Shortcut

SoftwareUpdate                       A software update applicable but not installed on the
                                     device

SoundDevices                         Sound Devices

SWLicensingProduct                   Software Licensing Product

SWLicensingService                   Software Licensing Service

SystemAccount                        System Account

SystemBootData                       System Boot Data

SystemBootSummary                    System Boot Summary

SystemConsoleUsage                   System Console Usage

<!-- p.1499 -->

Entity                       Description

SystemConsoleUser            System Console User

SystemDevices                System Devices

SystemDrivers                System Drivers

SystemEnclosure              System Enclosure

TapeDrive                    Tape Drive

TimeZone                     Time Zone

TPM                          TPM

TPMStatus                    TPM Status

TSIssuedLicense              TS Issued License

TSLicenseKeyPack             TS License Key Pack

UninterruptiblePowerSupply   Uninterruptible Power Supply

USBController                USB Controller

USBDevice                    USB Device

User                         A user account with an active connection to the device

USMFolderRedirectionHealth   Folder Redirection Health

USMUserProfile               User Profile Health

VideoController              Video Controller

VirtualMachine               Virtual Machine

VirtualMachine64             Virtual Machine (64)

Volume                       Volume

WindowsUpdate                Windows Update

WindowsUpdateAgentVersion    Windows Update Agent Version

WinEvent()                   Events within 24 hours (by default) from a Windows
                             event log

WriteFilterState             Write Filter State

Table operators

<!-- p.1500 -->

Table operators can be used filter, summarize, and transform data streams. Currently the
following operators are supported:

                                                                                       ﾉ   Expand table

 Table              Description
 operators

 count              Returns a table with a single record containing the number of records

 distinct           Produces a table with the distinct combination of the provided columns of the
                    input table

 join               Merge the rows of two tables to form a new table by matching row for the
                    same device

 order by           Sort the rows of the input table into order by one or more columns

 project            Select the columns to include, rename or drop, and insert new computed
                    columns

 take               Return up to the specified number of rows

 top                Returns the first N records sorted by the specified columns

 where              Filters a table to the subset of rows that satisfy a predicate

Scalar Operators
The following table summarizes operators:

                                                                                       ﾉ   Expand table

 Operators   Description                                                       Example

 ==          Equal                                                              1 == 1, 'aBc' ==
                                                                               'AbC'

 !=          Not Equal                                                          1 != 2, 'abc' !=
                                                                               'abcd'

 <           Less                                                               1 < 2, 'abc' < 'DEF'

 >           Greater                                                            2 > 1, 'xyz' > 'XYZ'

 <=          Less or Equal                                                      1 <= 2, 'abc' <=
                                                                               'abc'

<!-- p.1501 -->

 Operators     Description                                                 Example

 >=            Greater or Equal                                            2 >= 1, 'abc' >=
                                                                           'ABC'

 +             Add                                                         2 + 1, now() + 1d

 -             Subtract                                                    2 - 1, now() - 1h

 *             Multiply                                                    2 * 2

 /             Divide                                                      2 / 1

 %             Modulo                                                      2 % 1

 like          Left Hand Side (LHS) contains a match for Right Hand Side   'abc' like '%B%'
               (RHS)

 !like         LHS doesn't contain a match for RHS                         'abc' !like '_d_'

 contains      RHS occurs as a subsequence of LHS                          'abc' contains 'b'

 !contains     RHS doesn't occur in LHS                                    'team' !contains 'i'

 startswith    RHS is an initial subsequence of LHS                        'team' startswith
                                                                           'tea'

 !startswith   RHS isn't an initial subsequence of LHS                     'abc' !startswith
                                                                           'bc'

 endswith      RHS is a closing subsequence of LHS                         'abc' endswith 'bc'

 !endswith     RHS isn't a closing subsequence of LHS                      'abc' !endswith 'a'

 and           True if and only if RHS and LHS are true                    (1 == 1) and (2 == 2)

 or            True if and only if RHS or LHS is true                      (1 == 1) or (1 == 2)

Aggregation functions
Aggregation functions can be used with the summarize table operator to calculated
summarized values. Currently the following aggregation functions are supported:

                                                                                   ﾉ   Expand table

 Function      Description

 avg()         Returns the average of the values across the group

<!-- p.1502 -->

 Function       Description

 count()        Returns a count of the records per summarization group

 countif()      Returns a count of rows for which Predicate evaluates to true

 dcount()       Returns the number of distinct values in the group

 max()          Returns the maximum value across the group

 maxif()        Starting in version 2107, you can use maxif with the summarize table operator.

                Returns the maximum value across the group for which Predicate evaluates to true .

 min()          Returns the minimum value across the group

 minif()        Starting in version 2107, you can use minif with the summarize table operator.

                Returns the minimum value across the group for which Predicate evaluates to true .

 percentile()   Returns an estimate for the specified nearest-rank percentile of the population
                defined by Expr

 sum()          Returns the sum of the values across the group

 sumif()        Returns a sum of Expr for which Predicate evaluates to true

Scalar functions
Scalar functions can be used in expressions. Currently the following scalar functions are
supported:

                                                                                    ﾉ   Expand table

 Function          Description

 ago()             Subtracts the given timespan from the current UTC clock time

 bin()             Rounds values down to a number of datetime multiple of a given bin size

 case()            Evaluates a list of predicates and returns the first result expression whose
                   predicate is satisfied

 datetime_add()    Calculates a new datetime from a specified datepart multiplied by a specified
                   amount, added to a specified datetime

 datetime_diff()   Calculates the difference between two date time values

 iif()             Evaluates the first argument and returns the value of either the second or third
                   arguments depending on whether the predicate evaluated to true (second) or

<!-- p.1503 -->

Function        Description

                false (third)

indexof()       Function reports the zero-based index of the first occurrence of a specified
                string within input string

isnotnull()     Evaluates its sole argument and returns a Boolean value indicating if the
                argument evaluates to a non-null value

isnull()        Evaluates its sole argument and returns a Boolean value indicating if the
                argument evaluates to a null value

now()           Returns the current UTC clock time

strcat()        Concatenates between 1 and 64 arguments

strlen()        Returns the length, in characters, of the input string

substring()     Extracts a substring from a source string starting from some index to the end of
                the string

tostring()      Converts input to a string representation

Additional entities, operators, and functions for
CMPivot from Configuration Manager

 ） Important

 These items aren't supported when you run CMPivot from Microsoft Intune admin
 center.

                                                                               ﾉ    Expand table

Type          Item                       Description

Entity        AccountSID                 Account SID

Entity        FileContent()              Content of a specific file

Entity        NAPClient                  NAP Client

Entity        NAPSystemHealthAgent       NAP System Health Agent

Entity        RegistryKey()              Returns all registry keys matching the given expression
                                         (starting in version 2107)

<!-- p.1504 -->

 Type          Item                       Description

 Table         render                     Renders results as graphical output
 operator

Next steps
To learn more about CMPivot, see Use CMPivot.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1505 -->

CMPivot for real-time data in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager has always provided a large centralized store of device data,
which customers use for reporting purposes. The site typically collects this data on a
weekly basis. Starting in version 1806, CMPivot is a new in-console utility that now
provides access to real-time state of devices in your environment. It immediately runs a
query on all currently connected devices in the target collection and returns the results.
Then filter and group this data in the tool. By providing real-time data from online
clients, you can more quickly answer business questions, troubleshoot issues, and
respond to security incidents.

For example, in mitigating speculative execution side channel vulnerabilities   , one of
the requirements is to update the system BIOS. You can use CMPivot to quickly query on
system BIOS information, and find clients that aren't in compliance.

  ） Important

        Some security software may block scripts running from
        c:\windows\ccm\scriptstore. This can prevent successful execution of CMPivot
        queries. Some security software may also generate audit events or alerts when
        running CMPivot PowerShell.
        Certain anti-malware software may inadvertently trigger events against the
        Configuration Manager Run Scripts or CMPivot features. It is recommended to
        exclude %windir%\CCM\ScriptStore so that the anti-malware software permits
        those features to run without interference.

Prerequisites
The following components are required to use CMPivot:

      Upgrade the target devices to the latest version of the Configuration Manager
      client.

      Target clients require a minimum of PowerShell version 4.

<!-- p.1506 -->

     To gather data for the following entities, target clients require PowerShell version
     5.0:
        Administrators
        Connection
        IPConfig
        SMBConfig

     CMPivot and the Microsoft Edge installer are currently signed with the Microsoft
     Code Signing PCA 2011 certificate. If you set PowerShell execution policy to
     AllSigned, then you need to make sure that devices trust this signing certificate.
     You can export the certificate from a computer where you've installed the
     Configuration Manager console. View the certificate on "C:\Program Files
     (x86)\Microsoft Endpoint Manager\AdminConsole\bin\CMPivot.exe" , and then

     export the code signing certificate from the certification path. Then import it to the
     machine's Trusted Publishers store on managed devices. You can use the process
     in the following blog, but make sure to export the code signing certificate from the
     certification path: Adding a Certificate to Trusted Publishers using Intune .

Permissions
The following permissions are needed for CMPivot:

     Run CMPivot permission on the Collection
     Read permission on Inventory Reports
     Read permission on the SMS Scripts object
        Read for SMS Scripts isn't required starting in version 2107
        CMPivot doesn't need Read for SMS Scripts for it's primary scenario starting in
        version 2107. However, if the administration service is down and the permission
        has been removed, then when the administration service falls back, CMPivot will
        fail. The SMS Provider still requires Read permission on SMS Scripts if the
        administration service falls back to it due to a 503 (Service Unavailable) error, as
        seen in the CMPivot.log.
     The default scope.
        The default scope isn't required starting in version 2107

CMPivot permissions by Configuration Manager version

                                                                           ﾉ   Expand table

<!-- p.1507 -->

1902 and earlier    Versions 1906       2107 or later
                    through 2103

Run Script          Run CMPivot         Run CMPivot permission on the Collection
permission on the   permission on the
Collection          Collection

Read permission     Read permission     Read permission on Inventory Reports
on Inventory        on Inventory
Reports             Reports

Read permission     Read permission     N/A
on SMS Scripts      on SMS Scripts
                                        The SMS Provider still requires Read permission on
                                        SMS Scripts if the administration service falls back to it
                                        due to a 503 (Service Unavailable) error, as seen in the
                                        CMPivot.log.

Default scope       Default scope       N/A
permission          permission

Limitations
    CMPivot only returns data for clients connected to the current site unless it's run
    from the central administration site (CAS).
       If a collection contains devices from another site, CMPivot results are only from
       devices in the current site unless CMPivot is run from the CAS.
       In some environments, additional permissions are needed for CMPivot to run on
       the CAS. For more information, see CMPivot changes for version 1902.
    You can't customize entity properties, columns for results, or actions on devices.
    Only one instance of CMPivot can run at the same time on a computer that is
    running the Configuration Manager console.
    In CMPivot standalone, you're not able to access CMPivot queries stored in the
    Community hub.
    When single sign on with multifactor authentication is used, you may not be able
    to sign into Community hub from CMPivot when using Configuration Manager
    2103 and earlier.

Start CMPivot
 1. In the Configuration Manager console, connect to the primary site or the CAS. Go
    to the Assets and Compliance workspace, and select the Device Collections node.

<!-- p.1508 -->

     Select a target collection, and select Start CMPivot in the ribbon to launch the
     tool. If you don't see this option, check the following configurations:

          Confirm with a site administrator that your account has the required
          permissions. For more information, see Prerequisites.

  2. The interface provides further information about using the tool.

          Manually enter query strings at the top, or select the links in the in-line
          documentation.

          Select one of the Entities to add it to the query string.

          The links for Table Operators, Aggregation Functions, and Scalar Functions
          open language reference documentation in the web browser. CMPivot uses
          the Kusto Query Language (KQL).

  3. Keep the CMPivot window open to view results from clients. When you close the
     CMPivot window, the session is complete.

          If the query has been sent, then clients still send a state message response to
          the server.

How to use CMPivot

The CMPivot window contains the following elements:

  1. The collection that CMPivot currently targets is in the title bar at the top, and the
     status bar at the bottom of the window. For example, "PM_Team_Machines" in the
     above screenshot.

<!-- p.1509 -->

2. The pane on the left lists the Entities that are available on clients. Some entities
  rely upon WMI while others use PowerShell to get data from clients.

        Right-click an entity for the following actions:

           Insert: Add the entity to the query at the current cursor position. The
           query doesn't automatically run. This action is the default when you
           double-click an entity. Use this action when building a query.

           Query all: Run a query for this entity including all properties. Use this
           action to quickly query for a single entity.

           Query by device: Run a query for this entity and group the results. For
           example, Disk | summarize dcount( Device ) by Name

        Expand an entity to see specific properties available for each entity. Double-
        click a property to add it to the query at the current cursor position.

3. The Home tab shows general information about CMPivot, including links to
  sample queries and supporting documentation.

4. The Query tab displays the query pane, results pane, and status bar. The query tab
  is selected in the above screenshot example.

5. The query pane is where you build or type a query to run on clients in the
  collection.

        CMPivot uses a subset of the Kusto Query Language (KQL).

        Cut, copy, or paste content in the query pane.

        By default, this pane uses IntelliSense. For example, if you start typing D ,
        IntelliSense suggests all of the entities that start with that letter. Select an
        option and press Tab to insert it. Type a pipe character and a space | , and
        then IntelliSense suggests all of the table operators. Insert summarize and
        type a space, and IntelliSense suggests all of the aggregation functions. For
        more information on these operators and functions, select the Home tab in
        CMPivot.

        The query pane also provides the following options:

           Run the query.
                To rerun your current CMPivot query on the clients, hold Ctrl while
                clicking Run.

<!-- p.1510 -->

           Move backwards and forwards in the history list of queries.

           Create a direct membership collection.

           Export the query results to CSV or the clipboard.

6. The results pane displays the data returned by active clients for the query.

        The available columns vary based upon the entity and the query.

        The color saturation of the data in the results table or chart indicates if the
        data is live or from the last hardware inventory scan stored in the site
        database. For example, black is real-time data from an online client whereas
        grey is cached data.

        Select a column name to sort the results by that property.

        Right-click on any column name to group the results by the same information
        in that column, or sort the results.

        Right-click on a device name to take the following additional actions on the
        device:

           Pivot to: Query for another entity on this device.
              Starting in version 2006, Pivot to was replaced by Device Pivot. For
              more information, see CMPivot changes for version 2006.

           Run Script: Launch the Run Script wizard to run an existing PowerShell
           script on this device. For more information, see Run a script.

           Remote Control: Launch a Configuration Manager Remote Control session
           on this device. For more information, see How to remotely administer a
           Windows client computer.

           Resource Explorer: Launch Configuration Manager Resource Explorer for
           this device. For more information, see View hardware inventory or View
           software inventory.

        Right-click on any non-device cell to take the following additional actions:

           Copy: Copy the text of the cell to the clipboard.

           Show devices with: Query for devices with this value for this property. For
           example, from the results of the OS query, select this option on a cell in
           the Version row: OS | summarize countif( (Version == '10.0.17134') ) by
           Device | where (countif_ > 0)

<!-- p.1511 -->

           Show devices without: Query for devices without this value for this
           property. For example, from the results of the OS query, select this option
           on a cell in the Version row: OS | summarize countif( (Version ==
           '10.0.17134') ) by Device | where (countif_ == 0) | project Device

           Bing it: Launch the default web browser to https://www.bing.com          with
           this value as the query string.

        Select any hyperlinked text to pivot the view on that specific information.

        The results pane doesn't show more than 20,000 rows. Either adjust the query
        to further filter the data, or restart CMPivot on a smaller collection.

7. The status bar shows the following information (from left to right):

        The status of the current query to the target collection. This status includes:

           The number of active clients that completed the query (3)

           The number of total clients (5)

           The number of offline clients (2)

           Any clients that returned failure (0)

           For example: Query completed on 3 of 5 clients (2 clients offline and
           0 failure)

        The ID of the client operation. For example: id(16780221)

        The current collection. For example: PM_Team_Machines

        The total number of rows in the results pane. For example, 1 objects

 Tip

Starting in version 2107, use the Query devices again button, or Ctrl + F5 to force
the client to retrieve the data again for the query. Using Query devices again is
useful when you expect the data to change on the device since the last query, such
as during troubleshooting. Selecting Run query again after the initial results are
returned only parses the data CMPivot has already retrieved from the client.

<!-- p.1512 -->

Publish query to Community hub from
CMPivot
(Applies to version 2107 or later)

Starting in version 2107, you can publish a CMPivot query to the Community hub
directly from the CMPivot window. Submitting your queries directly through CMPivot
makes contributing to the Community hub easier.

You'll need the following requirements for CMPivot and for contributing to the
Community hub:

     Meet all of the CMPivot prerequisites and permissions
     Enable Community hub.
        If needed, install the Microsoft Edge WebView2 extension from the
        Configuration Manager console notification.
     A GitHub account that's joined to Community hub
        You must accept the invitation sent in the email otherwise you won't be able to
        contribute content.

   1. Go to the Assets and Compliance workspace then select the Device Collections
     node.

   2. Select a target collection, target device, or group of devices then select Start
     CMPivot in the ribbon to launch the tool.

   3. From the CMPivot window, select the Community hub icon on the menu.

   4. Select Sign in, then sign into GitHub.

<!-- p.1513 -->

5. Create a CMPivot query, then select Run Query to verify it functions as expected.

       Optionally, select the folder icon to access your favorites list to use a query
       you've already created.

6. Select the Publish link at top of CMPivot's Community hub window when you're
  ready to submit your query.

7. Give your query a Name and Description, then select the Publish button to send
  your query to the Community hub.

8. Once the contribution is complete, you can access your query anytime from the
  Me tab.

9. To view the GitHub pull request (PR), go to
  https://github.com/Microsoft/configmgr-hub/pulls       . You can also access the PR
  link from the Your hub page in the Community hub node.

<!-- p.1514 -->

           PRs shouldn't be submitted directly to the GitHub repository.

  ７ Note

        Currently, when you publish a query through CMPivot, you can't edit or delete
        it after publishing.
        Community hub is only available in CMPivot when you run it from the
        Configuration Manager console. Community hub isn't available from
        standalone CMPivot.

Example scenarios for CMPivot
The following sections provide examples of how you might use CMPivot in your
environment:

Example 1: Stop a running service
Your security administrator asks you to stop and disable the Computer Browser service
as quickly as possible on all devices in the accounting department. You start CMPivot on
a collection for all devices in accounting, and select Query all on the Service entity.

Service

As results appear, you right-click on the Name column and select Group by.

Service | summarize dcount( Device ) by Name

In the row for the Browser service, you select the hyperlinked number in the dcount_
column.

Service | where (Name == 'Browser') | summarize count() by Device

You multi-select all devices, right-click the selection, and choose Run Script. This action
launches the Run Script wizard, from which you run an existing script you have for
stopping and disabling a service. With CMPivot you quickly respond to the security
incident for all active computers, viewing results in the Run Script wizard. You then
followup to create a configuration baseline to remediate other computers in the
collection as they become active in the future.

<!-- p.1515 -->

Example 2: Proactively resolve application failures
To be proactive with operational maintenance, once a week you run CMPivot against a
collection of servers that you manage, and select Query all on the AppCrash entity. You
right-click the FileName column and select Sort Ascending. One device returns seven
results for sqlsqm.exe with a timestamp about 03:00 every day. You select the file name
in one of the rows, right-click it, and select Bing It. Browsing the search results in the
web browser, you find a Microsoft support article for this issue with more information
and resolution.

Example 3: BIOS version
To mitigate speculative execution side channel vulnerabilities     , one of the requirements
is to update the system BIOS. You start with a query for the BIOS entity. You then Group
by the Version property. Then right-click a specific value, such as "LENOVO - 1140", and
select Show devices with.

Bios | summarize countif( (Version == 'LENOVO - 1140') ) by Device | where
(countif_ > 0)

Example 4: Free disk space
You need to temporarily store a large file on a network file server, but aren't sure which
one has enough capacity. Start CMPivot against a collection of file servers, and query
the Disk entity. Modify the query for CMPivot to quickly return a list of active servers
with real-time storage data:

<!-- p.1516 -->

Disk | where (Description == 'Local Fixed Disk') | where isnotnull( FreeSpace ) |
order by FreeSpace asc

CMPivot standalone
You can use CMPivot as a standalone app. CMPivot standalone is only available in
English. Run CMPivot outside of the Configuration Manager console to view the real-
time state of devices in your environment. This change enables you to use CMPivot on a
device without first installing the console.

You can share the power of CMPivot with other personas, such as helpdesk or security
admins, who don't have the console installed on their computer. These other personas
can use CMPivot to query Configuration Manager alongside the other tools that they
traditionally use. By sharing this rich management data, you can work together to
proactively solve business problems that cross roles.

Install CMPivot standalone

   1. Set up the permissions needed to run CMPivot. For more information, see
     prerequisites. You can also use the Security Administrator role if the permissions
     are appropriate for the user.

   2. Find the CMPivot app installer in the following path: <site install
     path>\tools\CMPivot\CMPivot.msi . You can run it from that path, or copy it to

     another location.

   3. When you run the CMPivot standalone app, you'll be asked to connect to a site.
     Specify the fully qualified domain name or computer name of either the Central
     Administration or primary site server.

           Each time you open CMPivot standalone you'll be prompted to connect to a
           site server.

   4. Browse to the collection on which you want to run CMPivot, then run your query.

<!-- p.1517 -->

  ７ Note

        Right-click actions, such as Run Scripts, Resource Explorer, and web search
        aren't available in CMPivot standalone. CMPivot standalone's primary use is
        querying independently from the Configuration Manager infrastructure. To
        help security administrators, CMPivot standalone does include the ability to
        connect to Microsoft Defender Security Center.
        You can do local device query evaluation using CMPivot standalone.

Inside CMPivot
CMPivot sends queries to clients using the Configuration Manager "fast channel". This
communication channel from server to client is also used by other features such as client
notification actions, client status, and Endpoint Protection. Clients return results via the
similarly quick state message system. State messages are temporarily stored in the
database. For more information about the ports used for client notification, see the
Ports article.

The queries and the results are all just text. The entities InstallSoftware and Process
return some of the largest result sets. During performance testing, the largest state
message file size from one client for these queries was less than 1 KB. Scaled to a large
environment with 50,000 active clients, this one-time query would generate less than 50
MB of data across the network. All the items on the welcome page that are underlined,
will return less than 1 KB of info per client.

Starting in Configuration Manager 1810, CMPivot can query hardware inventory data,
including extended hardware inventory classes. These new entities (entities not
underlined on the welcome page) may return much larger data sets, depending on how

<!-- p.1518 -->

much data is defined for a given hardware inventory property. For example, the
"InstalledExecutable" entity might return multiple MB of data per client, depending on
the specific data you query on. Be mindful of the performance and scalability on your
systems when returning larger hardware inventory data sets from larger collections
using CMPivot.

A query times out after one hour. For example, a collection has 500 devices, and 450 of
the clients are currently online. Those active devices receive the query and return the
results almost immediately. If you leave the CMPivot window open, as the other 50
clients come online, they also receive the query, and return results.

Log files
CMPivot interactions are logged to the following log files:

Server-side:

     SmsProv.log
     BgbServer.log
     StateSys.log

Client-side:

     CcmNotificationAgent.log
     Scripts.log
     StateMessage.log

For more information, see Log files and Troubleshooting CMPivot.

Next steps
     Changes to CMPivot
     Troubleshooting CMPivot
     Create and run PowerShell scripts

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1519 -->

Changes to CMPivot
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the following information to learn about changes made to CMPivot between Configuration
Manager versions:

CMPivot changes for version 2107

Simplified CMPivot permissions requirements
We've simplified the CMPivot permissions requirements. The new permissions are applicable for
CMPivot standalone and CMPivot in the on-premises console. The following changes have been
made:

      CMPivot no longer requires SMS Scripts read permission
          The SMS Provider still requires this permission if the administration service falls back to it
          due to a 503 (Service Unavailable) error, as seen in the CMPivot.log.

      The default scope permission isn't required.

General improvements to CMPivot
We've made the following improvements to CMPivot:

      Added maxif and minif aggregators that can be used with the summarize operator
      Improvements to query autocomplete suggestions in the query editor
      Added a Key value to the Registry entity
      Added a new RegistryKey entity that returns all registry keys matching the given expression

To review the difference between the Registry and RegistryKey entities, you can use the following
samples:

  Kusto

  // Change the path to match your desired registry hive query

  Registry('hklm:\SOFTWARE\Microsoft\EnterpriseCertificates\Root\Certificates\*')
  RegistryKey('hklm:\SOFTWARE\Microsoft\EnterpriseCertificates\Root\Certificates\*')

  RegistryKey('hklm:\SOFTWARE\Microsoft\SMS\*')
  Registry('hklm:\SOFTWARE\Microsoft\SMS\*')

CMPivot changes for version 2103

<!-- p.1520 -->

Starting in version 2103, the following improvements have been made for CMPivot:

     Warning message and export CMPivot data option when results are too large
     Access the top queries shared in the Community hub from CMPivot

Warning message and export CMPivot data option when
results are too large
When results are too large the following warning message is displayed:

Your query returned a large number of results. Narrow the results by modifying the query, or
select this banner to export the results.

This message occurs in the following scenarios:

     When results are greater than 100,000 cells.
        For instance, the warning threshold is reached for 10,000 devices (rows) with 10 columns
        of entity data.
        In this case, you'll be given an option to export results to a .csv file

     When more than 128 KB of data is requested to be returned from a given device.
        For instance, CcmLog('ciagent', 120d) queries log results and is likely to be over the 128
        KB limit.
        When the results are over 128 KB, you'll get a warning, but you can't export them since
        they won't be returned from the client to the server.

Access the top queries shared in the Community hub from
CMPivot
Starting in version 2103, you can access the top CMPivot queries shared in the Community hub
from on-premises CMPivot. By using pre-created CMPivot queries shared by the broader
community, CMPivot users gain access to a wider variety of queries. On-premises CMPivot
accesses the Community hub and returns a list of the top downloaded CMPivot queries. Users can
review the top queries, customize them, and then run on-demand. This improvement gives a
wider selection of queries for immediate usage without having to construct them and also allows
information sharing on how to build queries for future reference.

  ７ Note

  These queries are available when you run CMPivot from the Configuration Manager console.
  They're not yet available from standalone CMPivot.

Prerequisites:
     Meet all of the CMPivot prerequisites and permissions
