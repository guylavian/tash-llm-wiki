---
title: "Core infrastructure documentation — pages 2001-2040"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2001-2040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2001-2040
family: sccm
documentKind: "doc"
abstract: "Example for registry data collection To collect registry keys for the classic programs installed on the device, add the following <add/> element in the <registryKeys> element: <add key=\"software\\\\microsoft\\\\windows\\\\currentversion\\\\uninstall\"/> XML <RegistryDataCollector> <regis"
---

# Core infrastructure documentation — pages 2001-2040

<!-- p.2001 -->

Example for registry data collection
To collect registry keys for the classic programs installed on the device, add the
following <add/> element in the <registryKeys> element: <add
key="software\\microsoft\\windows\\currentversion\\uninstall"/>

  XML

  <RegistryDataCollector>
    <registryKeys>
      <!-- Registry keys (and all subkeys) to collect -->
      <add key="software\\microsoft\\ccm"/>
      <add key="software\\microsoft\\sms"/>
      <add key="software\\microsoft\\ccmsetup"/>
      <add key="software\\microsoft\\windows\\currentversion\\uninstall"/>
    </registryKeys>
  </RegistryDataCollector>

Customize log file groups
To customize which log files Support Center collects, and how it presents them in the
Log groups list, use elements in the <logGroups> element. When you start Support
Center, it scans this section of the configuration file. It then creates a group on the Log
groups list for each unique key attribute value found in the <add/> elements contained
in the <logGroups> element.

     Component log group: The <componentLogGroup> element uses a key attribute to
     define the name of the log group that appears in the list. It also uses a value
     attribute that contains a regular expression (regex). It uses this regex to collect a
     set of related log files.

     Static log group: The <staticLogGroup> element uses a key attribute to define the
     name of the log group that appears in the list. It also uses a value attribute that
     defines a log file name.

If the same key attribute value is used in an <add/> element within both the
<componentLogGroup> element and the <staticLogGroup> element, Support Center

creates a single group. This group includes the log files defined by both elements that
use the same key.

Example for log file groups
  XML

<!-- p.2002 -->

   <logGroups>
     <componentLogGroup>
       <add key="Application Management"
   value="^(app.*|ci.*|contentaccess|contenttransfermanager|datatransferservice
   |dcm.*|execmgr.*|UserAffinity.*|.*Handler$|.*Provider$)"/>
       <add key="Client Registration"
   value="^(clientregistration|locationservices|ccmmessaging|ccmexec)"/>
       <add key="Inventory"
   value="^(ccmmessaging|inventoryagent|mtrmgr|swmtrreportgen|virtualapp|mtr.*|
   filesystemfile)"/>
       <add key="Policy"
   value="^(ccmmessaging|policyagent_.*|policyevaluator_.*)"/>
       <add key="Software Updates"
   value="^(ci.*|contentaccess|contenttransfermanager|datatransferservice|dcm.*
   |update.*|wuahandler|xmlstore|scanagent)"/>
       <add key="Software Distribution"
   value="^(datatransferservice|execmgr.*|contenttransfermanager|locationservic
   es|contentaccess|filebits)"/>
       <add key="Desired Configuration Management" value="^(ci.*|dcm.*)"/>
       <add key="Operating System Deployment" value="^(ts.*)"/>
     </componentLogGroup>
     <staticLogGroup>
       <add key="Application Management" value="ccmsdkprovider.log"/>
       <add key="Desired Configuration Management" value="ccmsdkprovider.log"/>
       <add key="Software Updates" value="ccmsdkprovider.log"/>
     </staticLogGroup>
   </logGroups>

Collect other log files with wildcards
To collect other log files, use wildcards in the file path or filename. These wildcards
include system-wide environment variables such as %WINDIR% , but exclude user-scoped
environment variables such as %USERPROFILE% . To collect other log files using this non-
recursive log file search, use an <add/> element within the <additionalLogFiles>
element.

These examples show how Support Center uses this feature in the default configuration
file.

Example 1: Collect all Windows Update log files in the
Windows directory
The following element collects any file named WindowsUpdate.log found in the Windows
directory:

<add key="%WINDIR%\WindowsUpdate.log" />

<!-- p.2003 -->

Example 2: Collect all log files in the Windows Logs
directory
The following element collects any file that ends in .log found in the Windows logs
directory:

<add key="%WINDIR%\logs\*.log" />

Full example XML
  XML

  <CcmLogDataCollector>
    <additionalLogFiles>
      <!-- Collect these additional log files. Can pass in a wildcard for the
  filename. System variables are also supported. -->
      <!--
      <add key="%WINDIR%\WindowsUpdate.log" />
      <add key="%WINDIR%\logs\*.log" />
      -->
    </additionalLogFiles>
  </CcmLogDataCollector>

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2004 -->

Accessibility features in Support Center
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Support Center has many helpful accessibility features that make it easier for everyone
to use.

Use the keyboard to move around the ribbon
Use keyboard shortcuts to access every menu of the Support Center ribbon. This ribbon
contains all commands used by Support Center.

        Press Alt or F10 to see keyboard shortcuts for each menu.

        To switch to a menu, press the associated shortcut key. For example, to go to the
        Logs menu, press Alt and then L.

Use the keyboard to perform common tasks
You can also use a keyboard to perform common tasks in the Support Center suite of
tools. The following table lists the most common tasks that you can perform with the
keyboard:

                                                                                  ﾉ   Expand table

 Task                                                          Keyboard shortcut

 Open application configuration options                        F4

 Exit                                                          Alt + F4

 Load or Refresh client details                                F5
 (on the Support Center Client Details tab)

 Load selected policy view                                     F5
 (on the Support Center Client Policy tab)

 Refresh a policy                                              F5
 (on the Support Center Client Policy tab, after selecting a
 policy)

 Copy as MOF                                                   Ctrl + Shift + C
 (on the Support Center Client Policy tab, after selecting a

<!-- p.2005 -->

Task                                                          Keyboard shortcut

policy; also available for WMI events)

Copy a policy as local client MOF                             Ctrl + Shift + X
(on the Support Center Client Policy tab, after selecting a
policy)

Request policy                                                Ctrl + R
(on the Support Center Client Policy tab)

Evaluate policy                                               Ctrl + E
(on the Support Center Client Policy tab)

Load or refresh content view                                  F5
(on the Support Center Content tab)

Load inventory                                                F5
(on the Support Center Inventory tab)

Start troubleshooting                                         F5
(on the Support Center Troubleshooting tab)

Open data bundle                                              Ctrl + O
(on the Support Center Viewer Home tab)

Open log files                                                Ctrl + O
(on the Support Center Logs tab, and in the Log Viewer
window)

Open log files in current view                                Ctrl + Shift + O
(on the Support Center Logs tab, and in the Log Viewer
window)

Open log files in a new Log Viewer window                     Ctrl + N
(on the Support Center Logs tab, and in the Log Viewer
window)

Close all log files                                           Ctrl + W
(on the Support Center Logs tab, and in the Log Viewer
window)

Search in log files                                           - Ctrl + F: Opens the Find dialog to
                                                              enter search string
                                                              - F3: Find the next match
                                                              - Shift + F3: Find the previous
                                                              match

Look up an error code                                         Ctrl + L
(on Logs tab, and in the Log Viewer window)

<!-- p.2006 -->

 Task                                                   Keyboard shortcut

 Copy from a log file                                   - Ctrl + C: Copies log file text
                                                        - Ctrl + Shift + C: Copies the log
                                                        entry without formatting

 Quick filter using log file text                       Ctrl + Shift + C
 (on Logs tab, and in the Log Viewer window)

 Annotate a log file                                    Ctrl + Shift + N Note 1
 (on Logs tab, and in the Log Viewer window)

 Open Help                                              F1

Note 1: Annotate a log file
Support Center stores annotations in memory. You can only use them within a log
viewing session. To retain an annotation for future use, take a screen capture to save the
resulting image.

Next steps
Accessibility features in Configuration Manager

Feedback
Was this page helpful?       Yes    No

Provide product feedback

<!-- p.2007 -->

Configuration Manager Tools
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

The Configuration Manager tools primarily include client-based and server-based tools.
Use these tools to help support and troubleshoot your Configuration Manager
infrastructure.

These tools are included in the CD.Latest\SMSSETUP\Tools folder on the site server. No
further installation is required. Use these versions of the tools with supported versions of
Configuration Manager current branch.

All Windows operating systems listed as supported clients in Supported operating
systems for clients and devices are supported for use with these tools.

  ７ Note

  For supported versions of Configuration Manager current branch, use the versions
  of the tools in the CD.Latest folder on the site server. Some tools were formerly in
  the toolkit but not included current branch. These legacy tools are no longer
  supported.

Client tools
These tools are in the ClientTools subfolder:

      Client Spy: Troubleshoot issues related to software distribution, inventory, and
      metering

      Deployment Monitoring Tool: Troubleshoot applications, updates, and baseline
      deployments

      Policy Spy: View policy assignments

      Power Viewer Tool: View status of power management feature

      Send Schedule Tool: Trigger schedules and evaluations of configuration baselines

  ７ Note

<!-- p.2008 -->

  The ClientTools folder also includes the file
  Microsoft.Diagnostics.Tracing.EventSource.dll. Several client tools require this
  library. You can't directly use it.

Server tools
These tools are in the ServerTools subfolder:

     DP Job Queue Manager: Troubleshoots content distribution jobs to distribution
     points

     Collection Evaluation Viewer: View collection evaluation details

        ） Important

        Starting in Configuration Manager version 2103, this standalone tool isn't
        supported. The tool is no longer included with the Configuration Manager
        installation source. Starting in version 2010, its functionality is built-in to the
        console. For more information, see, How to view collection evaluation.

     Content Library Explorer: View contents of the content library single instance store

     Content Library Transfer: Transfers content library between drives

     Content Ownership Tool: Changes ownership of orphaned packages. These
     packages exist in the site without an owning site server.

     Role-based Administration and Auditing Tool: Helps administrators audit roles
     configuration

        ７ Note

        Starting in version 2107, RBAViewer has moved from
        <installdir>\tools\servertools\rbaviewer.exe . It's now located in the

        Configuration Manager console directory. After you install the console,
        RBAViewer.exe will be in the same directory. The default location is C:\Program
        Files (x86)\Microsoft Endpoint Manager\AdminConsole\bin\rbaviewer.exe .

     Run Meter Summarization Tool: Run metering summarization task and analyze
     metering data

<!-- p.2009 -->

  ７ Note

  The ServerTools folder also includes the following files:

       AdminUI.WqlQueryEngine.dll
       Microsoft.ConfigurationManagement.ManagementProvider.dll
       Microsoft.Diagnostics.Tracing.EventSource.dll

  Several server tools require these libraries. You can't directly use them.

More tools in the folder
The following tools are in the CD.Latest\SMSSETUP\TOOLS folder on the site server:

     CMTrace: View, monitor, and analyze Configuration Manager log files.

     CMPivot: Use the standalone version of this tool to query real-time data from
     clients.

     Update reset tool: Fix issues when in-console updates have problems downloading
     or replicating.

     Configuration Manager group policy administrative template: Configure and assign
     client installation properties by using a group policy object.

     Content library cleanup tool: Remove orphaned content from a distribution point.

     Extend and migrate on-premises site to Microsoft Azure: Helps you to
     programmatically create Azure virtual machines (VMs) for Configuration Manager.

     Synchronize Microsoft 365 Apps updates from a disconnected software update
     point (OfflineUpdateExporter): Import Microsoft 365 Apps updates from an
     internet connected WSUS server into a disconnected Configuration Manager
     environment.

     Configure client communication ports: Reconfigure the port numbers for existing
     clients.

     Service Connection Tool: Keep your site up to date when your service connection
     point is offline.

     Support Center: Gather information from clients for easier analysis when
     troubleshooting.

<!-- p.2010 -->

     OneTrace is a modern log viewer with Support Center. It works similarly to
     CMTrace, with improvements. For more information, see Support Center OneTrace.

     Send feedback that you saved for later submission (UploadOfflineFeedback): Save
     your product feedback locally and submit it later.

Other tools
     Hierarchy Maintenance Tool: Use Preinst.exe in the \
     <SiteServerName>\SMS_<SiteCode>\bin\X64\00000409 shared folder on the site server

     to pass commands to the hierarchy manager component.

     Microsoft Deployment Toolkit (MDT): A collection of tools, processes, and guidance
     for automating desktop and server OS deployments.

     System Center Updates Publisher (SCUP): A stand-alone tool to manage and
     import custom software updates.

     Package Conversion Manager: Convert legacy packages into applications.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2011 -->

CMTrace
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

CMTrace is one of the Configuration Manager tools. It allows you to view and monitor
log files, including the following types:

      Log files in Configuration Manager or Client Component Manager (CCM) format

      Plain ASCII or Unicode text files, such as Windows Installer logs

The tool helps to analyze log files by highlighting, filtering, and error lookup.

  ７ Note

  CMTrace isn't automatically registered with Windows to open the .log file
  extension. For more information, see File associations.

Configuration Manager version 2107 includes multiple performance improvements to
the CMTrace log viewer.

Locations
Configuration Manager automatically installs CMTrace in the following locations:

      The site server's tools directory. For example:
      cd.latest\SMSSETUP\Tools\CMTrace.exe

      The Management point's installation directory. For example:
      C:\SMS_CCM\CMTrace.exe

      The client installation directory. For example: C:\Windows\CCM\CMTrace.exe
      OS deployment boot images. For example: X:\sms\bin\x64\CMTrace.exe

If you have a copy of CMTrace in another location, consider removing it and using a
copy in one of the default paths. If it's in a custom location that meets your business
requirements, then make sure you have a process to keep it up to date. If your custom
location might be of benefit to other customers, file product feedback.

For more information, see Direct links to Community hub items.

Usage

<!-- p.2012 -->

Run CMTrace.exe. The first time you run the tool, you see a prompt for file association.
For more information, see File associations.

You take most actions in CMTrace from the following menus:

     File
     Tools

File menu
The following actions are available in the File menu:

     Open
     Open on Server
     Print
     Preferences

The File menu also lists the last eight recent files. Quickly reopen one of these logs by
selecting it from the File menu.

Open

Displays the Open dialog box to browse for a log file.

Filter the view for files of the following types:

     Log files (*.log)
     Old log files (*.lo_)
     All files (*.*)

The following two options aren't selected by default:

     Ignore existing lines: When selected, CMTrace ignores the existing contents of the
     selected log file and displays new lines only as they're added. Use this option to
     monitor only new actions when you don't need the full history of the log file.

     Merge selected files: If you enable this option and select more than one log file,
     CMTrace merges the selected logs in the view. It displays them as if they're a single
     log file. The merged log updates the same, and supports all other CMTrace
     features as if it's a single log file.

Open on Server

<!-- p.2013 -->

Browse the Configuration Manager logs folder on a site system computer with the
standard Browse dialog box. You can also browse the network for a remote computer.

When you select a remote computer to browse, CMTrace checks for the Configuration
Manager share. If it can't find a share with Configuration Manager log files, it displays an
error message.

To connect directly to a known computer without browsing, use the Open action. Then
enter a server name and share using the UNC format.

Print

Display the standard Windows Print dialog box. This action sends the current log file to
a printer. It formats the output according to the settings on the Printing tab of CMTrace
Preferences.

Preferences

Configure settings for CMTrace. The following options are available:

     General tab

        Update Interval: Controls how often CMTrace checks for changes to log files
        and loads new lines. By default, this value is 500 milliseconds.

        Highlight: Sets the color that CMTrace uses when highlighting log lines that you
        choose. By default, this color is basic yellow (Red: 255, Green: 255, Blue: 0).

        Columns: Configures the columns that are visible in the log view and the order
        in which they appear. By default, it displays Log Text, Component, Date/Time,
        and Thread.

     Printing tab

        Columns: Configure which columns it uses when printing log files and the order
        in which they appear. By default, it prints the same columns as it displays.

        Orientation: Sets the default print orientation when printing log files. Override
        this setting in the Print dialog box. By default, it uses Portrait orientation.

     Advanced tab

        Refresh Interval: Forces CMTrace to update the log view at a specified interval
        when loading a large number of lines. By default, this option is disabled with a
        value of zero.

<!-- p.2014 -->

              ７ Note

              In general, don't modify the Refresh Interval. It can significantly increase
              the amount of time it takes to open large log files.

Tools menu
The following actions are available in the Tools menu:

     Find
     Find Next
     Copy to Clipboard
     Highlight
     Filter
     Error Lookup
     Pause
     Show/Hide Details
     Show/Hide Info Pane

Find
Search the open log file for a specified text string.

Find Next
Finds the next matching string, as you previously specified in the Find dialog box.

Copy to Clipboard
Copies the selected lines as plain text to the Windows clipboard. If you're examining
Configuration Manager and CCM log files, it copies the columns in the same order as
the view. It separates each column by a tab character. Use this action when copying logs
into email messages or other documents.

Highlight
Enter a string that CMTrace uses to search the text of each log entry. It then highlights
any log text that matches the string you enter.

     The highlight uses the color you specified in Preferences.

<!-- p.2015 -->

        To turn off highlighting, clearing the string from this field.

        If you enter a decimal or hexadecimal number, CMTrace tries to match the value to
        the Thread column. Use this behavior to highlight the processing of a single
        thread, without filtering out other threads that might interact with it.

        To compare strings by case, enable the option for Case sensitive.

Filter
Show or hide log lines based on the specified criteria. Apply filters to any of the four
columns regardless of whether they're visible. These settings apply to each opened log
file.

Examples:

        Filter smsts.log on entry text containing "the action" or "the group".
        Filter InventoryAgent.log where entry text contains "destination".

Error Lookup

Type or paste an error code in either decimal or hexadecimal format to display a
description. Possible error sources include: Windows, WMI, or Winhttp.

Pause
Suspend or restart log monitoring. The following use cases are some of the possible
reasons to use this action:

        When CMTrace is displaying log file information too quickly

        When you pause log monitoring, the information that CMTrace displays isn't lost if
        the current file rolls over to a new log

        When you want to stop CMTrace from displaying new data while you examine the
        log file

Show/Hide Details

Show or hide all columns other than the log text. It also expands the log text column to
the width of the window. Use this action when you're viewing logs on a computer with
low display resolution. It displays more of the log text.

<!-- p.2016 -->

  ７ Note

  When viewing plain-text files, CMTrace automatically hides details because they're
  always empty.

Show/Hide Info Pane
Show or hide the Info pane. Use this action when you're viewing logs on a computer
with low display resolution. It displays more logging details.

Log pane
The log pane is at the top of the CMTrace window. It displays lines from log files.

When you select a line, it's temporarily highlighted using the Windows selection color
scheme.

Highlighted lines match the criteria you define with the Highlight option in the Tools
menu. The highlight uses the color that you specify in Preferences.

CMTrace displays lines with errors using a red background and yellow text color. In
CCM-format logs, log entries have an explicit type value that indicates the entry as an
error. For other log formats, CMTrace does a case-insensitive search in each entry for
any text string matching "error".

It displays lines with warnings using a yellow background. In CCM-format logs, log
entries have an explicit type value that indicates the entry as a warning. For other log
formats, CMTrace does a case-insensitive search in each entry for any text string
matching "warn".

Info pane
The Info pane is at the bottom of the CMTrace window. It includes the following
features:

     Details about the currently selected log entry

     A text box that displays the log text

     It displays carriage returns so that formatted text is easier to read

     Easier to read long entries that aren't fully visible in the Log pane

<!-- p.2017 -->

Show or hide the Info pane with the Show/Hide Info Pane option on the Tools menu. If
the Info pane takes up more than half of the log window, CMTrace automatically hides
it.

Progress bar
When you first open a log file, CMTrace replaces the Info pane by a progress bar. This
progress indicates how much of the existing file contents it's loaded. The progress
reaches 100 percent, CMTrace removes the progress bar, and replaces it with the Info
pane. When you load large files, this behavior provides you with an indication of how
long the load might take.

Status bar
For Configuration Manager-format and CCM-format log files, the status bar displays the
elapsed time for the selected log entries. If you select a single entry, the tool displays
the time from the first log entry to the selected entry. If you select multiple entries, it
calculates the time from the top-most selected entry to the bottom-most selected entry.
CMTrace formats this information as follows:

Elapsed time is <hours>h <minutes>m <seconds>s <milliseconds>ms

(<seconds+milliseconds> seconds)

Windows shell integration
CMTrace supports file associations and drag-and-drop.

File associations
CMTrace can associate itself with .log and .lo_ file name extensions. When the program
starts, it checks the registry to determine whether it's already associated with these file
name extensions. If CMTrace isn't already associated with any file name extensions,
you're prompted to associate the file name extensions with CMTrace. If you select Do
not ask me this again, CMTrace skips this check whenever it's run on this computer.

Drag-and-drop
CMTrace supports basic drag-and-drop functionality. Drag a log file from Windows
Explorer into CMTrace to open it.

<!-- p.2018 -->

Other tips

Last Directory registry key
By default, CMTrace saves the last log location that you opened. This behavior is useful
on the site server, as it defaults to the logs path every time.

The first time you launch it on a client, it defaults to the current working directory. This
location may be the path where you saved CMTrace, or a path like
%userprofile%\Desktop .

The Last Directory value in the registry key
HKEY_CURRENT_USER\Software\Microsoft\Trace32 controls this default location. If you set

this value to %windir%\CCM\Logs on your clients, then CMTrace opens files in the client
log location the first time you run it.

Next steps
     Log files

     Support Center log file viewer

OneTrace is the log viewer with Support Center. It works similarly to CMTrace, with
improvements. For more information, see Support Center OneTrace.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2019 -->

Client Spy
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Client Spy is one of the Configuration Manager tools. It's a tool for troubleshooting
software distribution, inventory, and software metering on Configuration Manager
clients.

Most of the information retrieved by the tool pertains to software deployments:

      All current software deployments
      Software distribution history
      The client cache configuration
      Cached items
      Pending required deployments
      Available deployments

It also displays the following inventory information

      The latest inventory cycle date
      The last report date
      Software inventory major and minor versions
      File collection
      Hardware inventory
      IDMIF collection
      Discovery data records (DDRs)

Software metering rules are also displayed.

  ７ Note

  To improve performance, the tool only collects information for each tab when you
  select it. Similarly, when you click Refresh, it only refreshes the information for the
  currently displayed tab.

Usage

Tools menu

<!-- p.2020 -->

The following actions are available in the Tools menu:

Connect
Retrieve information from a different computer.

     By default, the tool displays information from the current computer.

     Connect using the remote computer name, user name, and password for the
     account. The tool makes a connection to the IPC$ share on the remote computer.
     It deletes the connection when either the tool exits or you connect to another
     computer.

     It requires an account with sufficient credentials to obtain the information.

     If you don't specify a user name and password, Client Spy uses the security context
     of the currently signed-in user to attempt to make the connection.

     When you connect to a remote computer, all tabs that are displayed show
     information from the remote computer.

Software Distribution
Displays the Software Distribution tabs and hides the other tabs. By default, Client Spy
displays the Software Distribution tabs.

Inventory

Displays the Inventory tab and hides the other tabs.

Software Metering

Displays the Software Metering tab and hides the other tabs.

Save current tab to file

Saves the information in the currently displayed tab to a text file that you specify.

Save all tabs to file
Saves the information in all tabs to a text file that you specify. It only saves information
your account can see.

<!-- p.2021 -->

Software Distribution tab
Configure settings on the following four tabs:

     Software Distribution Execution Requests
     Software Distribution History
     Software Distribution Cache Information
     Software Distribution Pending Executions

Software Distribution Execution Requests
This tab displays all existing deployments, including both device- and user-targeted
deployments.

Each tree item in the Software Distribution Execution Requests tab contains the
following four attributes:

     Advertisement ID. This value might be blank, if it's an available deployment.
     Package ID
     Program Name
     User. This might be the targeted user SID or the SID of the user who initiated the
     request. If both are system requests, the displayed user is System.

For each run request, it also displays the following information in a subtree structure:

     Program Name
     Package ID
     Package Name
     Request Creation Time
     State
     Running State, if State is Running
     Execution Context (User or Admin)
     History State (Success, Failure, or NotRun)
     LastRunTime (Never, if the program hasn't been run before)
     RetryCount, if State is WaitingRetry
     ContentAccess (Retry Count, if State is WaitingRetry)
     FailureCode, if State is WaitingRetry
     FailureReason, if State is WaitingRetry

If the request requires content, the state is WaitingContent. The Software Distribution
Cache Information tab shows the details for this download request.

<!-- p.2022 -->

If the run request is a download request, it also displays the number of bytes
downloaded.

  ７ Note

  It uses different icons for varying states of a run request.

Software Distribution History
This tab contains information about all previously run programs. This information is
stored in the registry.

The main branches of this tree are the different user histories, including System. It
displays a subtree containing the list of packages from which programs have been run
for each user.

The package ID and package name for each package subtree displays a list of programs
that have run. It displays the following attributes for each:

     Program name
     Run state
     Last run time
     Failure code
     Failure reason

The failure code and failure reason are blank when a program was successfully run.

Software Distribution Cache Information

Cache Config
Contains information about the Configuration Manager Client cache. This information
includes the cache location, the cache size, and whether it's currently in use.

Cached Items
Contains a subtree of all items currently in the cache. Each tree item includes the
following information about each item:

     The item's location (folder) in the cache
     Current state

<!-- p.2023 -->

     Package ID
     Package name
     Package version
     Package size
     Current reference count
     Last referenced time (UTC)

Downloading Items
These are the items that the client is currently downloading. Each of them shows the
same information displayed by the cached items, and the number of kilobytes
downloaded.

Software Distribution Pending Executions
This tab contains information that details past and future required deployments and a
list of available deployments.

Each tree branch is for each user account with deployments available, including System.

For each user, a sub tree contains the following three items:

Mandatory Advertisements With Future Executions

These are mandatory advertisements that still have programs remaining to be run.
These can be either recurring, one-time, or multiple schedule advertisements. Each
displays the advertisement ID, the next run time, and the schedule on which the
advertisement runs.

Optional Advertisements
Displays a list of all advertisements that are published. It also displays details such as
advertisement ID, program name, and package name for each.

Past Mandatory Advertisements With No Future Scheduled
Executions

This is a list of advertisements that exist on the client that have no future programs
scheduled to run. The advertisement ID, package name, and program name are
displayed. A subtree item is displayed for any advertisements that are optional.

<!-- p.2024 -->

  ７ Note

  Package name information is only available for packages that have advertised
  policies associated to them on the computer being viewed. Packages that no longer
  have available policies associated to them display the message "Package Name No
  Longer Available".

Inventory tab
There's only one tab containing inventory information. The main tree contains the
following five items:

     Software Inventory: Contains the date that the last cycle started, the date of the
     last report, and the minor and major versions of the last report.

     File Collection: Contains the date that the last cycle started, the date of the last
     report, and the minor and major versions of the last report.

     Hardware Inventory: Contains the date that the last cycle started, the date of the
     last report, and the minor and major versions of the last report.

     IDMIF Collection: Contains the date that the last cycle started, the date of the last
     report, and the minor and major versions of the last report.

     DDR: Contains the date that the last cycle started, the date of the last report, and
     the minor and major versions of the last report. The DDR information is also
     displayed in a subtree.

Software Metering tab
This tab displays information as a subtree, and includes all software metering rules. It
displays each rule as a node, which it identifies by the file name and rule ID. Expand
each node in the tree, and view the following information:

     Explorer file name
     Original file name
     Rule ID
     File version
     Language

<!-- p.2025 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2026 -->

Deployment Monitoring Tool
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Deployment Monitoring Tool is one of the Configuration Manager tools. It's a
graphical user interface designed to assist in troubleshooting application, software
update, and configuration baseline deployments on a Configuration Manager client. The
tool is read-only as it doesn't change any state on the client. You can safely use it to
diagnose common deployment scenarios.

Features
      Run it as an administrator to troubleshoot deployments on a local client.

      Troubleshoot deployments on a remote client. Launch the tool and connect to a
      remote machine as an administrator.

      Export to XML all the data collected in the tool. Share the XML file with others, and
      use it as a common platform for talking about troubleshooting deployments.

      Import previously exported data to a different machine, and use it to run the tool
      in offline mode.

Usage
The Deployment Monitoring Tool supports graphical user interface only. To launch the
tool, run DeploymentMonitoringTool.exe as an administrator. There are three views:

      Client Properties: A list of useful attributes about the device and the Configuration
      Manager client. This view is the default.

      Deployments: View all of the currently targeted deployments. Select a deployment
      in the results pane to view more information in the details pane.

      All Updates: View all of the software updates and their status.

To copy data in any view, select a cell, and press CTRL + C.

Actions menu
The following actions are available in the Actions menu:

<!-- p.2027 -->

     Connect to remote machine: Select a computer to connect to. When you don't
     specify a user name and password, it uses the current credentials. Click Save to
     connect to remote computer.

     Export Data: Select the file to write the data into, and click Save. Use the exported
     XML file for remote troubleshooting on a different computer.

     Import Data: Select a file to import into the tool.

     View Log: Opens an associated log file, depending upon the view:
        Client Properties: \\<hostname>\c$\Windows\CCM\Logs\PolicyAgent.log
        Deployments: \\<hostname>\c$\Windows\CCM\Logs\PolicyAgent.log
        All Updates: C:\Windows\WindowsUpdate.log

See also
     Deploy applications
     Deploy software updates
     Deploy configuration baselines

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2028 -->

Policy Spy
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Policy Spy is one of the Configuration Manager tools. It's a tool for viewing and
troubleshooting the policy system on Configuration Manager clients. Run PolicySpy.exe
to open the user interface. For more information on command-line usage, see
Command-line syntax.

  ） Important

  Run Policy Spy as an administrator. If you don't Run as administrator, you see the
  following error in Client Info:
   There is no client installed on this machine. Connection to client policy

  failed with error 80041003

Command-line syntax
Policy Spy is primarily intended for use through its user interface. It does provide limited
command-line options to support automation and batch processing.

PolicySpy.exe [/export <ExportFilename> [<computername>]]

Option: /export
This option silently exports the policy of the local or remote computer.
<ExportFilename> is the file name to which the tool saves the XML exported policy. If

you specify the <computername> option, Policy Spy exports the policy of that computer
instead of the local computer.

  ７ Note

  This command-line option doesn't provide a way to specify user credentials. To use
  alternative credentials to access a remote computer, use the runas command to
  open a new command prompt with the required security credentials.

Usage

<!-- p.2029 -->

Tools menu
The following actions are available in the Tools menu:

     Open Remote: Connects to the Configuration Manager client policy on a remote
     computer. Use the Connect dialog box to retrieve the name of the remote
     computer and optional user credentials. If the connection fails, it displays error
     information in the Client Info pane. If the connection fails again, try connecting by
     selecting Refresh on the Edit menu, or by pressing F5.

     Open File: Opens a policy export file (XML) created by the Export Policy option.
     The tool displays the exported policy exactly the same as a live policy. It disables
     some features that only apply when you connect to an actual client.

     Request Machine Assignments: Triggers a request for machine policy assignments
     on the target computer. This feature is disabled when viewing exported policy.

     Evaluate Machine Policy: Triggers a machine policy evaluation on the target
     computer. This feature is disabled when viewing an exported policy.

     Request User Assignments: Triggers a request for user policy assignments for the
     currently signed-in user. This feature is only available when viewing a policy on the
     local computer.

     Evaluate User Policy: Triggers a user policy evaluation for the currently signed-in
     user. This feature is only available when viewing a policy on the local computer.

     Reset Policy: Removes all non-default policies and resets the policy cookies for the
     site. It then triggers a request for machine policy assignments. This feature is
     disabled when viewing an exported policy.

     Export Policy: Exports the target computer's policy to an XML file. View this file on
     any computer with Policy Spy. To open the export file, select Open File on the
     Tools menu. This feature is disabled when viewing an exported policy.

Edit menu
The following actions are available in the Edit menu:

     Delete: Deletes the instance selected in the Results pane. This action is only
     supported for policy instances. If you try to delete anything other than policy
     instances, the tool displays an error message. This feature is disabled when viewing
     an exported policy.

<!-- p.2030 -->

     Refresh: Refreshes all results to view the latest information. All tree nodes that are
     expanded before refreshing are automatically expanded afterward. If Policy Spy
     hasn't successfully connected to the target computer's policy, it tries to connect
     again. This feature is disabled when viewing an exported policy.

     Clear Events: Clears all items from the Events tab.

Results pane
The results pane displays different views of the policy system on the target computer.
Access these views by clicking on one of the following four tabs:

     Actual
     Requested
     Default
     Events

Actual
This tab displays the current policy of the client. The current policy determines a client's
behavior and the behavior of its client agents, such as software distribution and
inventory. The tab displays results in a tree format with a root node for the computer
namespace and each user-specific namespace. Expand a namespace node to display a
list of classes. Expand a class to display a list of its instances. The class list includes only
classes that have instances.

Requested
This tab displays the policy assignments that the client retrieved from its assigned site.
The tab displays results in tree format with a root node for the Machine namespace and
each user-specific namespace. Expanding a namespace node displays the following
nodes:

     Configuration: Displays a list of configuration classes derived from
     CCM_Policy_Config, which includes policy object, assignments, and others.

     Settings: Displays all active settings generated by policies. Settings are displayed
     under the Configuration node.

  ７ Note

<!-- p.2031 -->

  Multiple instances can exist with the same name because the client hasn't merged
  these settings into a final resultant set. Policy Spy displays instances under this
  node by using the RealKey properties instead of their true policy keys. Correlate
  these instances to the resultant set displayed on the Actual tab.

Default
This tab displays the same information as the Requested tab. It also includes contents of
the DefaultMachine and DefaultUser namespaces.

Events
This tab displays policy agent events as they happen. The view creates a WMI event
subscription for all events derived from CCM_PolicyAgent_Event. The view shows a
maximum of 200 events. It removes the oldest events from the top of the list, as
necessary. If you select the last item in the list, the list automatically scrolls down as it
adds new events. Otherwise, the view maintains its current position, and you must scroll
down or press the End key to view new events. This view is always empty when viewing
an exported policy.

Client Info pane
The Client Info pane displays a list of properties for the target computer. It displays the
following properties, if available:

     Name
     ID
     Version
     Site
     Assigned MP
     Resident MP
     Proxy MP
     Proxy State

Details pane
The Details pane displays detailed information about the current selection. If no
selection is active, it displays information about Policy Spy itself, including the version.

<!-- p.2032 -->

Otherwise, it displays a Manage Object Format (MOF) representation of the selected
item.

Policy Spy uses its own MOF-generation routine to create a more user-friendly HTML
display than the plain-text MOF generated by WMI. This behavior allows Policy Spy to
add the following features to make the MOF more legible:

        Syntax highlighting

        Indented objects and arrays

        Properties are arranged into system, inherited, and local groups. By default, it
        collapses the system and inherited groups. You can immediately see which
        properties the instance actually uses.

        Copy MOF or copy plain-text MOF to the clipboard. This feature is useful for
        pasting the MOF into other applications by directly calling the MofComp tool.

For instances of Policy objects derived from CCM_Policy_Policy, the details pane displays
the policy body below the MOF that displays. If the client hasn't downloaded the policy
body, Policy Spy displays a hyperlink. Click the link to download the policy body directly
from the client's management point. If the tool successfully downloads the policy body,
it replaces the hyperlink with the contents of the reply. Otherwise, Policy Spy updates
the display indicating that the request failed.

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.2033 -->

Power Viewer Tool
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Power Viewer tool is one of the Configuration Manager tools. Use it to view the
status of the power management feature on a Configuration Manager client.

Run PowerVwr.exe as an administrator. When the tool launches, it displays the power
capabilities and power settings of the local computer on the Power Config tab.

To view the power management data of a remote computer:

   1. Go to the File menu, and click Connect.

   2. Enter the Computer name, and a Username and Password, if necessary.

There are three tabs in Power Viewer:

      Power Config: View the power capabilities and power settings of the targeted
      computer.

      Daily Activity: View the daily activity charts of the client, which includes the
      following information:

         Computer on: The power status of the computer in one day. Sleep mode is
         considered as power off.

         Monitor on: On or off status of monitor in one day.

         User Active: User activity information in one day.

      Power Events: View all of the daily power events. The client summarizes these
      events at 12:00 AM. This summarization generates data for the daily activity chart.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2034 -->

Send Schedule Tool
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Send Schedule Tool is one of the Configuration Manager tools. Use it to trigger a
schedule on a client or trigger the evaluation of a specified configuration baseline. It
works for the local computer or targeting a remote client.

For example, use the tool to trigger an inventory schedule or compliance evaluation. If a
number of Configuration Manager clients haven't recently reported inventory or
compliance status, run the tool to initiate the necessary schedule on each client.

Usage
Run SendSchedule.exe as an administrator.

SendSchedule /L [Computer Name] SendSchedule "<Message GUID | DCM UID>" [Computer
Name]

After you trigger a message (GUID), see SMSClientMethodProvider.log. For more
information about available message GUIDs, see Message IDs.

After you trigger the evaluation of a configuration baseline (DCM UID), see
DCMAgent.log.

Command-line options

Option: /L
List all Message GUID or DCM UID available for sending. Display the meaningful name
of messages in the data table for each one. If the computer name is absent, it uses the
local computer. If you specify a message without a machine name, then it sends the
message to the local machine.

Examples

List the available messages on the local machine

<!-- p.2035 -->

SendSchedule /L

List the available messages on the client MyPC:
SendSchedule /L MyPC

Trigger hardware inventory on the local machine
SendSchedule {00000000-0000-0000-0000-000000000001}

Trigger hardware inventory on MyPC:
SendSchedule {00000000-0000-0000-0000-000000000001} MyPC

Trigger the evaluation of a specific configuration baseline on MyPC:
SendSchedule ScopeId_611E8382-C064-4B62-B0DE-EFFB52AE8994/Baseline_36722778-69dd-

4423-9632-b61148b2b67e MyPC

Message IDs
                                                                   ﾉ   Expand table

 Message ID                    Display Name

 {00000000-0000-0000-0000-     Hardware Inventory
 000000000001}

 {00000000-0000-0000-0000-     Software Inventory
 000000000002}

 {00000000-0000-0000-0000-     Discovery Inventory
 000000000003}

 {00000000-0000-0000-0000-     File Collection
 000000000010}

 {00000000-0000-0000-0000-     IDMIF Collection
 000000000011}

 {00000000-0000-0000-0000-     Request Machine Assignments
 000000000021}

<!-- p.2036 -->

Message ID                  Display Name

{00000000-0000-0000-0000-   Evaluate Machine Policies
000000000022}

{00000000-0000-0000-0000-   Refresh Default MP Task
000000000023}

{00000000-0000-0000-0000-   LS (Location Service) Refresh Locations Task
000000000024}

{00000000-0000-0000-0000-   LS Timeout Refresh Task
000000000025}

{00000000-0000-0000-0000-   Policy Agent Request Assignment (User)
000000000026}

{00000000-0000-0000-0000-   Policy Agent Evaluate Assignment (User)
000000000027}

{00000000-0000-0000-0000-   Software Metering Generating Usage Report
000000000031}

{00000000-0000-0000-0000-   Source Update Message
000000000032}

{00000000-0000-0000-0000-   Clearing proxy settings cache
000000000037}

{00000000-0000-0000-0000-   Machine Policy Agent Cleanup
000000000040}

{00000000-0000-0000-0000-   User Policy Agent Cleanup
000000000041}

{00000000-0000-0000-0000-   Policy Agent Validate Machine Policy / Assignment
000000000042}

{00000000-0000-0000-0000-   Policy Agent Validate User Policy / Assignment
000000000043}

{00000000-0000-0000-0000-   Retrying/Refreshing certificates in AD on MP
000000000051}

{00000000-0000-0000-0000-   Peer DP Status reporting
000000000061}

{00000000-0000-0000-0000-   Peer DP Pending package check schedule
000000000062}

{00000000-0000-0000-0000-   SUM Updates install schedule
000000000063}

<!-- p.2037 -->

Message ID                  Display Name

{00000000-0000-0000-0000-   Hardware Inventory Collection Cycle
000000000101}

{00000000-0000-0000-0000-   Software Inventory Collection Cycle
000000000102}

{00000000-0000-0000-0000-   Discovery Data Collection Cycle
000000000103}

{00000000-0000-0000-0000-   File Collection Cycle
000000000104}

{00000000-0000-0000-0000-   IDMIF Collection Cycle
000000000105}

{00000000-0000-0000-0000-   Software Metering Usage Report Cycle
000000000106}

{00000000-0000-0000-0000-   Windows Installer Source List Update Cycle
000000000107}

{00000000-0000-0000-0000-   Software Updates Policy Action Software Updates
000000000108}               Assignments Evaluation Cycle

{00000000-0000-0000-0000-   PDP Maintenance Policy Branch Distribution Point
000000000109}               Maintenance Task

{00000000-0000-0000-0000-   DCM policy
000000000110}

{00000000-0000-0000-0000-   Send Unsent State Message
000000000111}

{00000000-0000-0000-0000-   State System policy cache cleanout
000000000112}

{00000000-0000-0000-0000-   Update source policy
000000000113}

{00000000-0000-0000-0000-   Update Store Policy
000000000114}

{00000000-0000-0000-0000-   State system policy bulk send high
000000000115}

{00000000-0000-0000-0000-   State system policy bulk send low
000000000116}

{00000000-0000-0000-0000-   Application manager policy action
000000000121}

<!-- p.2038 -->

 Message ID                         Display Name

 {00000000-0000-0000-0000-          Application manager user policy action
 000000000122}

 {00000000-0000-0000-0000-          Application manager global evaluation action
 000000000123}

 {00000000-0000-0000-0000-          Power management start summarizer
 000000000131}

 {00000000-0000-0000-0000-          Endpoint deployment reevaluate
 000000000221}

 {00000000-0000-0000-0000-          Endpoint AM policy reevaluate
 000000000222}

 {00000000-0000-0000-0000-          External event detection
 000000000223}

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2039 -->

DP Job Queue Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Distribution Point (DP) Job Queue Manager is one of the Configuration Manager
tools. Use it to troubleshoot and manage ongoing content distribution jobs to
Configuration Manager distribution points.

The tool displays the list of jobs that the package transfer manager component has in its
queue. It also shows the status of the jobs: ready to be executed, running, or retrying. It
lets you manipulate the jobs in the queue, move jobs higher on the list, cancel a job, or
manually start running a job.

It also gets information from the site server on which distribution point is running a job.
The tool connects through the provider to the site server. It doesn't connect to every
remote distribution point to gather this information. Because it triggers actions and gets
information through the provider, there's a delay in reflecting changes from remote
distribution points.

Usage
Run DPJobMgr.exe. The main menu of the tool contains the following tabs:

      Connect: Establish the initial connection to the primary site server

      Overview: Summarizes in a single view all the jobs that are running on all
      distribution points

      Distribution Point Info: Multi-select distribution points to track them, and manage
      a single job of interest

      Manage Jobs: Shows in one flat view a list of all the jobs and their statuses.
      Manipulate jobs, move them up, cancel, or manually start.

Connect tab
Use this tab to establish the initial connection to the primary site server. It uses the
currently signed-in user's credentials. You can't connect to the central administration site
or secondary sites. The connection requires the Full Administrator security role.

<!-- p.2040 -->

Once the tool successfully establishes a connection, a notification at the bottom of the
tool confirms that it's connected to the site server.

Overview tab
Shows a summary of all the jobs on all distribution points. See the following columns:

     Distribution Point: Lists the names of the distribution points

     Running Jobs: Shows the number of concurrent jobs that are running on a
     particular distribution point.

         Tip

        The number of concurrent software distributions is a site setting. Modified this
        setting in the Software Distribution Component Properties.

     Total Jobs: Shows the number of all the jobs targeted to a particular distribution
     point. This number includes the jobs that are running, retrying, or waiting to be
     executed.

     Total Retries: Shows the number of times jobs have been retrying in a particular
     distribution point. A higher number may represent a general problem with that
     particular distribution point.

   Tip

        To sort each column in this tab, click on the column name

        Manually refresh the information in this tab by clicking Refresh

        Automatically refresh the information in this tab by clicking Start Auto
        Refresh and setting the auto refresh interval. The default refresh interval is
        two minutes.

Distribution Point Info tab
Shows the list of all the distribution points under the connected site. The pane on the
left lists all the distribution points. Click Select All or Unselect All as necessary, or multi-
select specific distribution points in this list. The pane on the right shows the jobs for the
selected distribution points.
