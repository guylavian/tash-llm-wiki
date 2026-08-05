---
title: "Core infrastructure documentation — pages 1521-1560"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1521-1560
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1521-1560
family: sccm
documentKind: "doc"
abstract: "Enable Community hub. You don't need a GitHub account to download content. Verify which content categories are displayed for community hub Install the Microsoft Edge WebView2 extension from the Configuration Manager console notification Use CMPivot to access the top Community hu"
---

# Core infrastructure documentation — pages 1521-1560

<!-- p.1521 -->

    Enable Community hub. You don't need a GitHub account to download content.
    Verify which content categories are displayed for community hub
    Install the Microsoft Edge WebView2 extension from the Configuration Manager console
    notification

Use CMPivot to access the top Community hub queries
  1. Go to the Assets and Compliance workspace then select the Device Collections node.

  2. Select a target collection, target device, or group of devices then select Start CMPivot in the
    ribbon to launch the tool.

  3. Use the community hub icon on the menu.

  4. Review the list of top shared CMPivot queries.

                                                                                                

  5. Select one of the top queries to load it into the query pane.

  6. Edit the query if needed then select Run Query.

  7. Optionally, select the folder icon to access your favorites list. Add the original query or your
    edited version to your favorites list to run later. Select the community hub icon to search for
    another query.

  8. Keep the CMPivot window open to view results from clients. When you close the CMPivot
    window, the session is complete. If the query has been sent, then clients still send a state
    message response to the server.

<!-- p.1522 -->

CMPivot changes for version 2006
Starting in version 2006, the following improvements have been made for CMPivot:

     CMPivot standalone and CMPivot launched from the admin console have converged. When
     you launch CMPivot from the admin console, it uses the same underlying technology as
     CMPivot standalone to give you scenario parity.

     Improvements for keyboard navigation in CMPivot.

     You can run CMPivot from an individual device or multiple devices from the devices node
     without needing to select a device collection. This improvement makes it easier for people,
     such as those working as the Helpdesk persona, to create CMPivot queries for specific
     devices outside a pre-created collection.
       Select an individual device or multi-select devices in a device collection or then select
       Start CMPivot.

     Upon returning devices within a query list view, you can select Device Pivot on one or more
     devices and then pivot and query on just those devices to drill in further. This change allows
     you to drill in without querying the larger set of devices from the original collection. Device
     Pivot replaced Pivot to.
       Within an existing CMPivot operation, select an individual device or multi-select devices
       from the output. Right-click and pivot using the Device Pivot option. This action launches
       a separate CMPivot instance scoped to just the devices you selected. This makes it easier
       to pivot and just query on devices desired without needing to create a collection for
       them.

     When you run CMPivot for an individual device, the device name is listed at the top of the
     window. For multiple devices, the number of devices selected is listed at the top of the
     window.

     The Create Collection option in the Query Summary tab was removed since CMPivot no
     longer requires querying against a collection. Perform a Device Pivot to open a new instance
     of CMPivot scoped to just the devices you want to query on. Create Collection is still
     available on the main menu.

<!-- p.1523 -->

CMPivot changes for version 2002
We've made it easier to navigate CMPivot entities. Starting in Configuration Manager version
2002, you can search CMPivot entities. New icons have also been added to easily differentiate the
entities and the entity object types.

CMPivot changes for version 1910
Starting in version 1910, CMPivot was significantly optimized to reduce network traffic and load
on your servers. Additionally, a number of entities and entity enhancements were added to aid in
troubleshooting and hunting. The following changes were introduced for CMPivot in version 1910:

     Optimizations to the CMPivot engine
     Additional entities and entity enhancements:
        Windows event logs (WinEvent)
        File content (FileContent)

<!-- p.1524 -->

        Dlls loaded by processes (ProcessModule)
        Microsoft Entra information (AADStatus)
        Endpoint protection status (EPStatus)
     Local device query evaluation using CMPivot standalone
     Other enhancements to CMPivot

Optimizations to the CMPivot engine
To reduce network traffic and load on your servers, CMPivot was optimized in 1910. Many query
operations are now performed directly on the client rather than on the servers. This change also
means that some CMPivot operations return minimal data from the first query. If you decide to
drill into the data for more information, a new query might run to fetch the additional data from
the client. For instance, previously a large data set was returned to the server when you ran a
"summarized count" query. While returning a large data set offered immediate drill-down, many
times only the summarized count was needed. In 1910 when you choose to drill into a specific
client, another collection of the data occurs to return the additional data you've requested. This
change brings better performance and scalability to queries against a large number of clients.

Examples
The CMPivot optimizations drastically reduce the network and server CPU load needed to run
CMPivot queries. With these optimizations, we can now sift through gigabytes of client data in
real time. The following queries illustrate these optimizations:

     Search all event logs on all clients in your enterprise for authentication failures.

        Kusto

        EventLog('Security')
        | where EventID == 4673
        | summarize count() by Device
        | order by count_ desc

     Search for a file by hash.

        Kusto

        Device
        | join kind=leftouter ( File('%windir%\\system32\\*.exe')
        | where SHA256Hash ==
        'A92056D772260B39A876D01552496B2F8B4610A0B1E084952FE1176784E2CE77')
        | project Device, MalwareFound = iif( isnull(FileName), 'No', 'Yes')

WinEvent(<logname>,[<timespan>])
This entity is used to get events from event logs and event tracing log files. The entity gets data
from event logs that are generated by the Windows Event Log technology. The entity also gets

<!-- p.1525 -->

events in log files generated by Event Tracing for Windows (ETW). WinEvent looks at events that
have occurred within the last 24 hours by default. However, the 24-hour default can be overridden
by including a timespan.

  Kusto

  WinEvent('Microsoft-Windows-HelloForBusiness/Operational', 1d)
  | where LevelDisplayName =='Error'
  | summarize count() by Device

FileContent(<filename>)
FileContent is used to get the contents of a text file.

  Kusto

  FileContent('c:\\windows\\SMSCFG.ini')
  | where Content startswith 'SMS Unique Identifier='
  | project Device, SMSId= substring(Content,22)

ProcessModule(<processname>)
This entity is used to enumerate the modules (dlls) loaded by a given process. ProcessModule is
useful when hunting for malware that hides in legitimate processes.

  Kusto

  ProcessModule('powershell')
  | summarize count() by ModuleName
  | order by count_ desc

AadStatus
This entity can be used to get the current Microsoft Entra identity information from a device.

  Kusto

  AadStatus
  | project Device, IsAADJoined=iif( isnull(DeviceId),'No','Yes')
  | summarize DeviceCount=count() by IsAADJoined
  | render piechart

EPStatus
EPStatus is used to get the status of antimalware software installed on the computer.

  Kusto

<!-- p.1526 -->

  EPStatus
  | project Device, QuickScanAge=datetime_diff('day',now(),QuickScanEndTime)
  | summarize DeviceCount=count() by QuickScanAge
  | order by QuickScanAge
  | render barchart

Local device query evaluation using CMPivot standalone
When using CMPivot outside of the Configuration Manager console, you can query just the local
device without the need for the Configuration Manager infrastructure. You can now leverage the
CMPivot Azure Log Analytics queries to quickly view WMI information on the local device. This
also enables validation and refinement of CMPivot queries, before running them in a larger
environment. CMPivot standalone is only available in English. For more information about
CMPivot standalone, see CMPivot standalone.

Known issues for local device query evaluation
     If you query on This PC for a WMI entity that you don't have access to, such as a locked
     down WMI class, you may see a crash in CMPivot. Run CMPivot using an account with
     elevated privileges to query those entities.
     If you query non-WMI entities on This PC, you'll see an Invalid namespace or an ambiguous
     exception.
     Run CMPivot standalone from the start menu shortcut, not directly from the path of the
     executable file.

Other enhancements
     You can do regular expression type queries using the new like operator. For example:

       Kusto

       //Find BIOS manufacture that contains any word like Micro, such as Microsoft
       Bios
       | where Manufacturer like '%Micro%'

     We've updated the CcmLog() and EventLog() entities to only look at messages in the last 24
     hours by default. This behavior can be overridden by passing in an optional timespan. For
     example, the following query will look at events in the last 1 hour:

       Kusto

       CcmLog('Scripts',1h)

     The File() entity has been updated to collect information about Hidden and System files, and
     include the MD5 hash. While an MD5 hash isn't as accurate as the SHA256 hash, it tends to

<!-- p.1527 -->

     be the commonly reported hash in most malware bulletins.

     You can add comments in queries. This behavior is useful when sharing queries. For example:

       Kusto

       //Get the top ten devices sorted by user
       Device
       | top 10 by UserName

     CMPivot automatically connects to the last site. After you start CMPivot, you can connect to
     a new site if necessary.

     From the Export menu, select the new option to Query link to clipboard. This action copies
     a link to the clipboard that you can share with others. For example:

     cmpivot:Ly8gU2FtcGxlIHF1ZXJ5DQpPcGVyYXRpbmdTeXN0ZW0NCnwgc3VtbWFyaXplIGNvdW50KCkgYnkgQ2F

     wdGlvbg0KfCBvcmRlciBieSBjb3VudF8gYXNjDQp8IHJlbmRlciBiYXJjaGFydA==

     This link opens CMPivot standalone with the following query:

       Kusto

       // Sample query
       OperatingSystem
       | summarize count() by Caption
       | order by count_ asc
       | render barchart

        Tip

       For this link to work, install CMPivot standalone.

     In query results, if the device is enrolled in Microsoft Defender for Endpoint, right-click the
     device to launch the Microsoft Defender Security Center online portal.

Known issues for CMPivot in version 1910
     The maximum results banner may not be displayed when the limit is reached.
        Each client is limited to 128 KB worth of data per query.
        Results may be truncated if the results of the query exceed 128 KB.

CMPivot changes for version 1906
Starting in version 1906, the following items were added to CMPivot:

     Joins, additional operators, and aggregators

<!-- p.1528 -->

        Added CMPivot permissions to the Security Administrator role
        CMPivot standalone

Add joins, additional operators, and aggregators in CMPivot
You now have additional arithmetic operators, aggregators, and the ability to add query joins such
as using Registry and File together. The following items have been added:

Table operators

                                                                                         ﾉ   Expand table

 Table operators    Description

 join               Merge the rows of two tables to form a new table by matching row for the same device

 render             Renders results as graphical output

The render operator already exists in CMPivot. Support for multiple series and the with statement
were added. For more information, see the examples section and Kusto's join operator article.

Limitations for joins
     1. The join column is always implicitly done on the Device field.
     2. You can use a maximum of 5 joins per query.
     3. You can use a maximum of 64 combined columns.

Scalar operators

                                                                                         ﾉ   Expand table

 Operator                    Description                     Example

 +                           Add                             2 + 1, now() + 1d

 -                           Subtract                        2 - 1, now() - 1d

 *                           Multiply                        2 * 2

 /                           Divide                          2 / 1

 %                           Modulo                          2 % 1

Aggregation functions

                                                                                         ﾉ   Expand table

<!-- p.1529 -->

Function           Description

percentile()       Returns an estimate for the specified nearest-rank percentile of the population defined by Expr

sumif()            Returns a sum of Expr for which Predicate evaluates to true

Scalar functions

                                                                                                     ﾉ   Expand table

Function           Description

case()             Evaluates a list of predicates and returns the first result expression whose predicate is satisfied

iff()              Evaluates the first argument and returns the value of either the second or third arguments
                   depending on whether the predicate evaluated to true (second) or false (third)

indexof()          Function reports the zero-based index of the first occurrence of a specified string within input
                   string

strcat()           Concatenates between 1 and 64 arguments

strlen()           Returns the length, in characters, of the input string

substring()        Extracts a substring from a source string starting from some index to the end of the string

tostring()         Converts input to a string operation

Examples
        Show device, manufacturer, model, and OSVersion:

           Kusto

           ComputerSystem
           | project Device, Manufacturer, Model
           | join (OperatingSystem | project Device, OSVersion=Caption)

        Show graph of boot times for a device:

           Kusto

           SystemBootData
           | where Device == 'MyDevice'
           | project SystemStartTime, BootDuration, OSStart=EventLogStart, GPDuration,
           UpdateDuration
           | order by SystemStartTime desc
           | render barchart with (kind=stacked, title='Boot times for MyDevice',
           ytitle='Time (ms)')

<!-- p.1530 -->

Added CMPivot permissions to the Security Administrator
role
Starting in version 1906, the following permissions have been added to Configuration Manager's
built-in Security Administrator role:

         Read on SMS Script
         Run CMPivot on Collection
         Read on Inventory Report

  ７ Note

  Run Scripts is a super set of the Run CMPivot permission.

CMPivot standalone
You can use CMPivot as a standalone app. CMPivot standalone is only available in English. Run
CMPivot outside of the Configuration Manager console to view the real-time state of devices in
your environment. This change enables you to use CMPivot on a device without first installing the
console.

You can share the power of CMPivot with other personas, such as helpdesk or security admins,
who don't have the console installed on their computer. These other personas can use CMPivot to
query Configuration Manager alongside the other tools that they traditionally use. By sharing this
rich management data, you can work together to proactively solve business problems that cross
roles.

Install CMPivot standalone
   1. Set up the permissions needed to run CMPivot. For more information, see prerequisites. You
         can also use the Security Administrator role if the permissions are appropriate for the user.

<!-- p.1531 -->

   2. Find the CMPivot app installer in the following path: <site install
     path>\tools\CMPivot\CMPivot.msi . You can run it from that path, or copy it to another

     location.

   3. When you run the CMPivot standalone app, you'll be asked to connect to a site. Specify the
     fully qualified domain name or computer name of either the Central Administration or
     primary site server.

           Each time you open CMPivot standalone you'll be prompted to connect to a site server.

   4. Browse to the collection on which you want to run CMPivot, then run your query.

  ７ Note

       Right-click actions, such as Run Scripts, Resource Explorer, and web search aren't
       available in CMPivot standalone. CMPivot standalone's primary use is querying
       independently from the Configuration Manager infrastructure. To help security
       administrators, CMPivot standalone does include the ability to connect to Microsoft
       Defender Security Center.
       You can do local device query evaluation using CMPivot standalone.

CMPivot changes for version 1902
Starting in Configuration Manager version 1902, you can run CMPivot from the central
administration site (CAS) in a hierarchy. The primary site still handles the communication to the
client. When running CMPivot from the central administration site, it communicates with the
primary site over the high-speed message subscription channel. This communication doesn't rely
upon standard SQL Server replication between sites.

Running CMPivot on the CAS will require additional permissions when SQL Server or the SMS
Provider aren't on the same machine or in the case of SQL Server Always On availability group
configuration. With these remote configurations, you have a "double hop scenario" for CMPivot.

To get CMPivot to work on the CAS in such a "double hop scenario", you can define constrained
delegation. To understand the security implications of this configuration, read the Kerberos
constrained delegation article. Kerberos needs to work through all of the hops between the
machines. If you have more than one remote configuration such as SQL Server or SMS Provider

<!-- p.1532 -->

being colocated with the CAS or not, or multiple trusted forests, you may require a combination
of permission settings. Below are the steps that you may need to take:

CAS has a remote SQL Server
   1. Go to each primary site's SQL Server.
     a. Add the CAS remote SQL Server and the CAS site server to the Configmgr_DviewAccess
        group.

   2. Go to Active Directory Users and Computers.
     a. For each primary site server, right click and select Properties.
         i. In the delegation tab, choose the third option, Trust this computer for delegation to
           specified services only.
        ii. Choose Use Kerberos only.
        iii. Add the CAS's SQL Server service with port and instance.
        iv. Make sure these changes align with your company security policy!
     b. For the CAS site, right click and select Properties.
         i. In the delegation tab, choose the third option, Trust this computer for delegation to
           specified services only.
        ii. Choose Use Kerberos only.
        iii. Add each primary site's SQL Server service with port and instance.
        iv. Make sure these changes align with your company security policy!

<!-- p.1533 -->

CAS has a remote provider
 1. Go to each primary site's SQL Server.
   a. Add the CAS provider machine account and the CAS site server to the
      Configmgr_DviewAccess group.
 2. Go to Active Directory Users and Computers.
   a. Select the CAS provider machine, right click and select Properties.
       i. In the delegation tab, choose the third option, Trust this computer for delegation to
         specified services only.
      ii. Choose Use Kerberos only.
      iii. Add each primary site's SQL Server service with port and instance.
      iv. Make sure these changes align with your company security policy!
   b. Select the CAS site server, right click and select Properties.
       i. In the delegation tab, choose the third option, Trust this computer for delegation to
         specified services only.
      ii. Choose Use Kerberos only.
      iii. Add each primary site's SQL Server service with port and instance.
      iv. Make sure these changes align with your company security policy!
 3. Restart the CAS remote provider machine.

SQL Server Always On availability groups
 1. Go to each primary site's SQL Server.

<!-- p.1534 -->

     a. Add the CAS site server to the Configmgr_DviewAccess group.
  2. Go to Active Directory Users and Computers.
     a. For each primary site server, right click and select Properties.
         i. In the delegation tab, choose the third option, Trust this computer for delegation to
          specified services only.
        ii. Choose Use Kerberos only.
       iii. Add the CAS's SQL Server service accounts for the SQL Server nodes with port and
          instance.
        iv. Make sure these changes align with your company security policy!
     b. Select the CAS site server, right click and select Properties.
         i. In the delegation tab, choose the third option, Trust this computer for delegation to
          specified services only.
        ii. Choose Use Kerberos only.
       iii. Add each primary site's SQL Server service with port and instance.
        iv. Make sure these changes align with your company security policy!
  3. Make sure the SPN is published for the CAS listener name and each primary listener name.
  4. Restart the primary SQL Server nodes.
  5. Restart the CAS site server and the CAS SQL Server nodes.

CMPivot changes for version 1810
CMPivot includes the following improvements starting in Configuration Manager version 1810:

     CMPivot utility and performance
     Scalar functions
     Rendering visualizations
     Hardware inventory
     Scalar operators
     Query summary
     Audit status messages

CMPivot utility and performance
     CMPivot will return up to 100,000 cells rather than 20,000 rows.
       If the entity has 5 properties, meaning 5 columns, up to 20,000 rows will be shown.
       For an entity with 10 properties, up to 10,000 rows will be shown.
       The total data shown will be less than or equal to 100,000 cells.

     On the Query Summary tab, select the count of Failed or Offline devices, and then select the
     option to Create Collection. This option makes it easy to target those devices with a
     remediation deployment.
       This option was removed in version 2006 since CMPivot no longer requires querying
       against a collection.

<!-- p.1535 -->

     Save Favorite queries by clicking the folder icon.

     Clients updated to the 1810 version return output less than 80 KB to the site over a fast
     communication channel.
        This change increases the performance of viewing script or query output.
        If the script or query output is greater than 80 KB, the client sends the data via a state
        message.
        If the client isn't updated to the 1810 client version, it continues to use state messages.

     You may see the following error when you start CMPivot: You can't use CMPivot right now
     due to an incompatible script version. This issue may be because the hierarchy is in the
     process of upgrading a site. Wait until the upgrade is complete and then try again.
        If you see this message, it could mean:
           The security scope isn't set up properly.
           There are issues with Upgrade in the process.
           The underlying CMPivot script is incompatible.

Scalar functions
CMPivot supports the following scalar functions:

     ago(): Subtracts the given timespan from the current UTC clock time
     datetime_diff(): Calculates the calendar difference between two datetime values
     now(): Returns the current UTC clock time
     bin(): Rounds values down to an integer multiple of a given bin size

  ７ Note

  The datetime data type represents an instant in time, typically expressed as a date and time
  of day. Time values are measured in 1-second units. A datetime value is always in the UTC

<!-- p.1536 -->

  time zone. Always express date time literals in ISO 8601 format, for example, yyyy-mm-dd
  HH:MM:ss

Examples
     datetime(2015-12-31 23:59:59.9) : A specific date time literal

     now() : The current time
     ago(1d) : The current time minus one day

Rendering visualizations
CMPivot now includes basic support for the KQL render operator. This support includes the
following types:

     barchart: First column is x-axis, and can be text, datetime or numeric. The second columns
     must be numeric and is displayed as a horizontal strip.
     columnchart: Like barchart, with vertical strips instead of horizontal strips.
     piechart: First column is color-axis, second column is numeric.
     timechart: Line graph. First column is x-axis, and should be datetime. Second column is y-
     axis.

Example: bar chart
The following query renders the most recently used applications as a bar chart:

  Kusto

  CCMRecentlyUsedApplications
  | summarize dcount( Device ) by ProductName
  | top 10 by dcount_
  | render barchart

<!-- p.1537 -->

Example: time chart
To render time charts, use the new bin() operator to group events in time. The following query
shows when devices have started in the last seven days:

  Kusto

  OperatingSystem
  | where LastBootUpTime <= ago(7d)
  | summarize count() by bin(LastBootUpTime,1d)
  | render timechart

<!-- p.1538 -->

Example: pie chart
The following query displays all OS versions in a pie chart:

  Kusto

  OperatingSystem
  | summarize count() by Caption
  | render piechart

Hardware inventory
Use CMPivot to query any hardware inventory class. These classes include any custom extensions
you make to hardware inventory. CMPivot immediately returns cached results from the last
hardware inventory scan stored in the site database. At the same time, it updates the results if
necessary with live data from any online clients.

The color saturation of the data in the results table or chart indicates if the data is live or cached.
For example, dark blue is real-time data from an online client. Light blue is cached data.

Example
  Kusto

  LogicalDisk
  | summarize sum( FreeSpace ) by Device
  | order by sum_ desc
  | render columnchart

<!-- p.1539 -->

Limitations
      The following hardware inventory entities aren't supported:
        Array properties, for example IP address
        Real32/Real64
        Embedded object properties
      Inventory entity names must begin with a character
      You can't overwrite the built-in entities by creating an inventory entity of the same name

Scalar operators
CMPivot includes the following scalar operators:

  ７ Note

        LHS: string to the left of the operator
        RHS: string to the right of the operator

                                                                                    ﾉ   Expand table

 Operator       Description                                     Example (yields true)

 ==             Equals                                          "aBc" == "aBc"

<!-- p.1540 -->

 Operator           Description                                      Example (yields true)

 !=                 Not equals                                           "abc" != "ABC"

 like               LHS contains a match for RHS                         "FabriKam" like "%Brik%"

 !like              LHS doesn't contain a match for RHS                  "Fabrikam" !like "%xyz%"

 contains           RHS occurs as a subsequence of LHS                   "FabriKam" contains "BRik"

 !contains          RHS doesn't occur in LHS                             "Fabrikam" !contains "xyz"

 startswith         RHS is an initial subsequence of LHS                 "Fabrikam" startswith "fab"

 !startswith        RHS isn't an initial subsequence of LHS              "Fabrikam" !startswith "kam"

 endswith           RHS is a closing subsequence of LHS                  "Fabrikam" endswith "Kam"

 !endswith          RHS isn't a closing subsequence of LHS               "Fabrikam" !endswith "brik"

Query summary
Select the Query Summary tab at the bottom of the CMPivot window. This status helps you
identify clients that are offline, or troubleshoot errors that may occur. Select a value in the Count
column to open a list of specific devices with that status.

For example, select the count of devices with a Failure status. See the specific error message, and
export a list of these devices. If the error is that a specific cmdlet isn't recognized, create a
collection from the exported device list to deploy a Windows PowerShell update.

CMPivot audit status messages
Starting in version 1810, when you run CMPivot, an audit status message is created with
MessageID 40805. You can view the status messages by going to Monitoring > System Status >
Status Message Queries. You can run All Audit status Messages for a Specific User, All Audit
status Messages for a Specific Site, or create your own status message query.

The following format is used for the message:

MessageId 40805: User <UserName> ran script <Script-Guid> with hash <Script-Hash> on
collection <Collection-ID>.

         7DC6B6F1-E7F6-43C1-96E0-E1D16BC25C14 is the Script-Guid for CMPivot.
         The Script-Hash can be seen in the client's scripts.log file.
         You can also see the hash stored in the client's script store. The filename on the client is
         <Script-Guid>_<Script-Hash>.
            Example file name: C:\Windows\CCM\ScriptStore\7DC6B6F1-E7F6-43C1-96E0-
            E1D16BC25C14_abc1d23e45678901fabc123d456ce789fa1b2cd3e456789123fab4c56789d0123.ps

<!-- p.1541 -->

Next steps
Troubleshooting CMPivot

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1542 -->

CMPivot sample scripts
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

Below are a few common query needs and how CMPivot can be used to meet them.
CMPivot uses a subset of the Kusto Query Language (KQL).

Operating system
Gets operating system information.

  Kusto

  // Sample query for OS information
  OperatingSystem

Recently used applications
The following query gets recently used applications (last 2 hours):

  Kusto

  CCMRecentlyUsedApplications
  | where (LastUsedTime > ago(2h))
  | project CompanyName, ProductName, ProductVersion, LastUsedTime

Device start times
The following query shows when were the devices started in the last seven days:

  Kusto

  OperatingSystem
  | where LastBootUpTime <= ago(7d)
  | summarize count() by bin(LastBootUpTime,1d)

Free disk space
The following query shows free disk space:

<!-- p.1543 -->

  Kusto

  LogicalDisk
  | project Device, DeviceID, Name, Description, FileSystem, Size, FreeSpace
  | order by DeviceID asc

Device information
Show device, manufacturer, model, and OSVersion:

  Kusto

  ComputerSystem
  | project Device, Manufacturer, Model
  | join (OperatingSystem | project Device, OSVersion=Caption)

Boot times for a device
Show boot times for devices:

  Kusto

  SystemBootData
  | project Device, SystemStartTime, BootDuration, OSStart=EventLogStart,
  GPDuration, UpdateDuration
  | order by SystemStartTime desc

Authentication failures
Search the event logs for authentication failures.

  Kusto

  EventLog('Security')
  | where EventID == 4673

ProcessModule(<processname>)
Enumerates all the modules (dlls) loaded by a given process. ProcessModule is useful
when hunting for malware that hides in legitimate processes.

<!-- p.1544 -->

  Kusto

  ProcessModule('powershell')
  | summarize count() by ModuleName
  | order by count_ desc

Antimalware software status
Gets the status of antimalware software installed on the computer gathered by the Get-
MpComputerStatus cmdlet. The entity is supported on Windows 10 and Server 2016, or

later with Defender running. |

  Kusto

  EPStatus
  | project Device, QuickScanAge=datetime_diff('day',now(),QuickScanEndTime)
  | summarize DeviceCount=count() by QuickScanAge

Find BIOS Manufacturer that contains any word
like Micro
  Kusto

  Bios
  // Find BIOS Manufacturer that contains any word like Micro, such as
  Microsoft
  | where Manufacturer like '%Micro%'

Find file by its hash
Search for a file by hash.

  Kusto

  Device
  | join kind=leftouter ( File('%windir%\\system32\\*.exe')
  | where SHA256Hash ==
  'A92056D772260B39A876D01552496B2F8B4610A0B1E084952FE1176784E2CE77')
  | project Device, MalwareFound = iif( isnull(FileName), 'No', 'Yes')

<!-- p.1545 -->

Find 'Scripts' in the CCM logs in the last hour
The following query looks at events in the last 1 hour:

  Kusto

  CcmLog('Scripts',1h)

Find information in the registry
Search for registry information.

  Kusto

  // Change the path to match your desired registry hive query
  // The RegistryKey entity (added in version 2107) isn't supported with
  CMPivot for tenant attached devices.

  Registry('hklm:\SOFTWARE\Microsoft\EnterpriseCertificates\Root\Certificates\
  *')
  RegistryKey('hklm:\SOFTWARE\Microsoft\EnterpriseCertificates\Root\Certificat
  es\*')

  RegistryKey('hklm:\SOFTWARE\Microsoft\SMS\*')
  Registry('hklm:\SOFTWARE\Microsoft\SMS\*')

Next steps
To learn more about CMPivot, see Use CMPivot.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1546 -->

Troubleshoot CMPivot
Article • 10/04/2022

CMPivot is a tool that provides access to a real-time state of the devices in your
environment. CMPivot runs a query on all currently connected devices in the target
collection and returns the results.

Occasionally, you might need to troubleshoot CMPivot. For example, if a state message
from a client to CMPivot gets corrupted, the site server can't process the message. This
article helps you understand the flow of information for CMPivot.

Troubleshoot CMPivot in version 1902 and later
In Configuration Manager versions 1902 and later, you can run CMPivot from the central
administration site (CAS) in a hierarchy. The primary site still handles the communication
to the client.

When you run CMPivot from CAS, it uses the high-speed message subscription channel
to communicate with the primary site. CMPivot doesn't use standard SQL Server
replication between sites. If your SQL Server instance or your SMS provider is remote, or
if you use a SQL Server Always On availability group, you'll have a "double hop scenario"
for CMPivot. For information on how to define constrained delegation for a "double hop
scenario", see CMPivot starting in version 1902.

  ） Important

  When troubleshooting CMPivot, enable verbose logging on your management
  points (MPs) and on the site server's SMS_MESSAGE_PROCESSING_ENGINE to get
  more information. Also, if the client's output is larger than 80 KB, enable verbose
  logging on the MP and the site server's SMS_STATE_SYSTEM component. For
  information about how to enable verbose logging, see Site server logging options.

Get information from the site server
By default, the site server log files are located in C:\Program Files\Microsoft
Configuration Manager\logs . This location might be different if you specified a non-

default installation directory or offloaded items like the SMS Provider to another server.
If you run CMPivot from the CAS, the logs are on the primary site server.

<!-- p.1547 -->

Look in smsprov.log for these lines:

     Configuration Manager version 1906:

        Auditing: User <username> initiated client operation 145 to collection
        <CollectionId>.

     Configuration Manager version 1902:

        Type parameter is 135.
        Auditing: User <username> ran script 7DC6B6F1-E7F6-43C1-96E0-
        E1D16BC25C14 with hash
        dc6c2ad05f1bfda88d880c54121c8b5cea6a394282425a88dd4d8714547dc4a2 on
        collection <CollectionId>.

7DC6B6F1-E7F6-43C1-96E0-E1D16BC25C14 is the Script-Guid for CMPivot. You can also see

this GUID in CMPivot audit status messages.

Next, find the ID in the CMPivot window. This ID is the ClientOperationID .

Find the TaskID from the ClientAction table. The TaskID corresponds to the UniqueID in
the ClientAction table.

  SQL

  select * from ClientAction where ClientOperationId=<id>

<!-- p.1548 -->

In BgbServer.log , look for the TaskID you gathered from SQL Server and note the
PushID . The TaskID is labeled TaskGUID . For example:

  Starting to send push task (PushID: 9 TaskID: 12 TaskGUID: 9A4E59D2-2F5B-
  4067-A9FA-B99602A3A4A0 TaskType: 15 TaskParam:
  PFNjcmlwdENvbnRlbnQgU2NyaXB0R3VpZD0nN0RDNkI2RjEtRTdGNi00M0MxL (truncated log
  entry)
  Finished sending push task (PushID: 9 TaskID: 12) to 2 clients

Client logs
After you have the information from the site server, check the client logs. By default, the
client logs are located in C:\Windows\CCM\Logs .

In CcmNotificationAgent.log , look for log entries that look like the following lines:

  Receive task from server with pushid=9, taskid=12, taskguid=9A4E59D2-2F5B-
  4067-A9FA-B99602A3A4A0, tasktype=15 and
  taskParam=PFNjcmlwdEhhc2ggU2NyaXB0SGF (truncated log entry)
  Send Task response message <BgbResponseMessage TimeStamp="2019-09-
  13T17:29:09Z"><PushID>5</PushID><TaskID>4</TaskID><ReturnCode>1</ReturnCode>
  </BgbResponseMessage> successfuly.

Check Scripts.log for the TaskID . In the following example, you see Task ID
{9A4E59D2-2F5B-4067-A9FA-B99602A3A4A0} :

  Sending script state message (fast): {9A4E59D2-2F5B-4067-A9FA-B99602A3A4A0}
  Result are sent for ScriptGuid: 7DC6B6F1-E7F6-43C1-96E0-E1D16BC25C14 and
  TaskID: {9A4E59D2-2F5B-4067-A9FA-B99602A3A4A0}

  ７ Note

  If you don't see "(fast)" in the Scripts.log , then the data is likely over 80 KB. In this
  case, the information is sent to the site server as a state message. Use client's
  StateMessage.log and the site server's Statesys.log .

<!-- p.1549 -->

Review messages on the site server
When verbose logging is enabled on the management point, you can see how incoming
client messages are handled. In MP_RelayMsgMgr.log , look for the TaskID .

In the MP_RelayMsgMgr.log example, you can see the client's ID (GUID:83F67728-2E6D-
4E4F-8075-ED035C31B783) and the Task ID {9A4E59D2-2F5B-4067-A9FA-B99602A3A4A0} . A

message ID gets assigned to the client's response before it's sent to the message
processing engine:

  MessageKey: GUID:83F67728-2E6D-4E4F-8075-ED035C31B783{9A4E59D2-2F5B-4067-
  A9FA-B99602A3A4A0}
  Create message succeeded for message id 22f00adf-181e-4bad-b35e-d18912f39f89
  Add message payload succeeded for message id 22f00adf-181e-4bad-b35e-
  d18912f39f89
  Put message succeeded for message id 22f00adf-181e-4bad-b35e-d18912f39f89
  CRelayMsgMgrHandler::HandleMessage(): ExecuteTask() succeeded

When verbose logging is enabled on SMS_MESSAGE_PROCESSING_ENGINE.log , the client
results are processed. Use the message ID you found from the MP_RelayMsgMgr.log . The
processing log entries are similar to the following example:

  Processing 2 messages with type Instant and IDs 22f00adf-181e-4bad-b35e-
  d18912f39f89[19], 434d80ae-09d4-4d84-aebf-28a4a29a9852[20]...
  Processed 2 messages with type Instant. Failed to process 0 messages. All
  message IDs 22f00adf-181e-4bad-b35e-d18912f39f89[19], 434d80ae-09d4-4d84-
  aebf-28a4a29a9852[20]

   Tip

  If you get an exception during processing, you can review it by running the
  following SQL query and looking at the Exception column. After the message is
  processed, it will no longer be in the MPE_RequestMessages_Instant table.

    SQL

     select * from MPE_RequestMessages_Instant where MessageID=<ID from
     SMS_MESSAGE_PROCESSING_ENGINE.log>

<!-- p.1550 -->

In BgbServer.log , look for the PushID to see the number of clients that reported or
failed.

  Generated BGB task status report c:\ConfigMgr\inboxes\bgb.box\Bgb5c1db.BTS
  at 09/16/2019 16:46:39. (PushID: 9 ReportedClients: 2 FailedClients: 0)

Check the monitoring view for CMPivot from SQL Server by using the TaskID .

  SQL

  select * from vSMS_CMPivotStatus where TaskID='{9A4E59D2-2F5B-4067-A9FA-
  B99602A3A4A0}'

                                                                                     

Troubleshoot CMPivot in 1810 and earlier
In Configuration Manager versions 1810 and earlier, your site server handles the
communication to the client.

Get information from the site server
By default, the site server log files are located in C:\Program Files\Microsoft
Configuration Manager\logs . This location might be different if you specified a non-

default installation directory or offloaded items like the SMS Provider to another server.

Look in smsprov.log for this line:

  Auditing: User <username> initiated client operation 135 to collection
  <CollectionId>.

Find the ID in the CMPivot window. This ID is the ClientOperationID .

<!-- p.1551 -->

Find the TaskID from the ClientAction table. The TaskID corresponds to the UniqueID in
the ClientAction table.

  SQL

  select * from ClientAction where ClientOperationId=<id>

In BgbServer.log , look for the TaskID you gathered from SQL. It's labeled TaskGUID . For
example:

  Starting to send push task (PushID: 260 TaskID: 258 TaskGUID: F8C7C37F-B42B-
  4C0A-B050-2BB44DF1098A TaskType: 15
  TaskParam: PFNjcmlwdEhhc2ggU2NyaXB0SGF...truncated...to 5 clients with
  throttling (strategy: 1 param: 42)
  Finished sending push task (PushID: 260 TaskID: 258) to 5 clients

Client logs
After you have the information from the site server, check the client logs. By default, the
client logs are located in C:\Windows\CCM\Logs .

In CcmNotificationAgent.log , look for logs that are similar to the following entry:

<!-- p.1552 -->

  Error! Bookmark not
  defined.+PFNjcmlwdEhhc2ggU2NyaXB0SGFzaEFsZz0nU0hBMjU2Jz42YzZmNDY0OGYzZjU3M2M
  yNTQyNWZiNT
  g2ZDVjYTIwNzRjNmViZmQ1NTg5MDZlMWI5NDRmYTEzNmFiMDE0ZGNjPC9TY3JpcHRIYXNoPjxTY3
  Jp (truncated log entry)

Look in Scripts.log for the TaskID . In the following example, we see Task ID
{F8C7C37F-B42B-4C0A-B050-2BB44DF1098A} :

  Sending script state message: 7DC6B6F1-E7F6-43C1-96E0-E1D16BC25C14
  State message: Task Id {F8C7C37F-B42B-4C0A-B050-2BB44DF1098A}

Look in StateMessage.log . In the following example, you see that TaskID is near the
bottom of the message next to <Param> :

  XML

  StateMessage body: <?xml version="1.0" encoding="UTF-16"?>
  <Report><ReportHeader><Identification><Machine>
  <ClientInstalled>1</ClientInstalled><ClientType>1
  </ClientType><ClientID>GUID:DBAC52C9-57E6-47D7-A8D6-E0A5A64B57E6</ClientID>
  <ClientVersion>5.00.8670.1000</ClientVersion>
  <NetBIOSName>R613924</NetBIOSName><CodePage>437</CodePage>
  <SystemDefaultLCID>1033</SystemDefaultLCID><Priority>0</Priority></Machine>
  </Identification>
  <ReportDetails><ReportContent>State Message Data</ReportContent>
  <ReportType>Full</ReportType>
  <Date>20180703184447.673000+000</Date><Version>1.0</Version>
  <Format>1.0</Format>
  </ReportDetails></ReportHeader><ReportBody><StateMessage
  MessageTime="20180703184447.517000+000"><Topic ID="7DC6B6F1-E7F6-43C1-96E0-
  E1D16BC25C14" Type="9003" IDType="0" User="" UserSID=""/><State ID="1"
  Criticality="0"/>
  <StateDetails Type="1"><!
  [CDATA["PAA/AHgAbQBsACAAdgBlAHIAcwBpAG8AbgA9ACIAMQAuADAAIgAgAGUAbgBjAG8AZABp
  AG4AZwA9ACIAdQB0AGYALQAxADYAIgA/AD4APAByAGUAcwB1AGwAdAAgAFIAZQBzAHUAbAB0AEMA
  bwBkAGUAPQAiADAAIgA+ADwAZQAgAE4AYQBtAGUAPQAiAEkAbgB0AGUAbAAoAFIAKQAgAFgAZQBv
  AG4AKABSACkAIABDAFAAVQAgAEUANQAtADIANgA3ADMAIAB2ADQAIABAACAAMgAuADMAMABHAEgA
  egAiACAATQBhAG4AdQBmAGEAYwB0AHUAcgBlAHIAPQAiAEEAbQBlAHIAaQBjAGEAbgAgAE0AZQBn
  AGEAdAByAGUAbgBkAHMAIABJAG4AYwAuACIAIABWAGUAcgBzAGkAbwBuAD0AIgBWAFIAVABVAEEA
  TAAgAC0AIAA2ADAAMAAxADcAMAAyACIAIABSAGUAbABlAGEAcwBlAEQAYQB0AGUAPQAiADIAMAAx
  ADcALQAwADYALQAwADIAIAAwADAAOgAwADAAOgAwADAAIgAgAFMAZQByAGkAYQBsAE4AdQBtAGIA
  ZQByAD0AIgAwADAAMAAwAC0AMAAwADEAOAAtADMANgA4ADIALQA0ADcAMAA4AC0ANwA2ADQAMAAt
  ADcANgAwADAALQAzADMAIgAgAFMATQBCAEkATwBTAEIASQBPAFMAVgBlAHIAcwBpAG8AbgA9ACIA
  MAA5ADAAMAAwADcAIAAiACAALwA+ADwALwByAGUAcwB1AGwAdAA+AA=="~~]]>
  </StateDetails><UserParameters Flags="0" Count="2">
  <Param>{F8C7C37F-B42B-4C0A-B050-2BB44DF1098A}</Param><Param>0</Param>
  </UserParameters></StateMessage></ReportBody></Report>

<!-- p.1553 -->

  Successfully forwarded State Messages to the MP StateMessage 7/3/2018
  11:44:47 AM 5036 (0x13AC)

Review messages on the site server
Open statesys.log to see if the message is received and processed. In the following
example, you see TaskID near the bottom of the message next to <Param> . Enable
verbose logging on the SMS_STATE_SYSTEM component to see these log entries.

  XML

  CMessageProcessor - the cmdline to DB exec dbo.spProcessStateReport N'?<?xml
  version="1.0" encoding="UTF-
  16"?>~~<Report><ReportHeader><Identification><Machine>
  <ClientInstalled>1</ClientInstalled><ClientType>1
  </ClientType><ClientID>GUID:DBAC52C9-57E6-47D7-A8D6-E0A5A64B57E6</ClientID>
  <ClientVersion>5.00.8670.1000</ClientVersion>
  <NetBIOSName>R613924</NetBIOSName><CodePage>437</CodePage>
  <SystemDefaultLCID>1033</SystemDefaultLCID><Priority>0</Priority></Machine>
  </Identification>
  <ReportDetails><ReportContent>State Message Data</ReportContent>
  <ReportType>Full</ReportType>
  <Date>20180703184447.673000+000</Date><Version>1.0</Version>
  <Format>1.0</Format>
  </ReportDetails></ReportHeader><ReportBody><StateMessage
  MessageTime="20180703184447.517000+000"><Topic ID="7DC6B6F1-E7F6-43C1-96E0-
  E1D16BC25C14" Type="9003" IDType="0" User="" UserSID=""/><State ID="1"
  Criticality="0"/>
  <StateDetails Type="1"><!
  [CDATA["PAA/AHgAbQBsACAAdgBlAHIAcwBpAG8AbgA9ACIAMQAuADAAIgAgAGUAbgBjAG8AZABp
  AG4AZwA9ACIAdQB0AGYALQAxADYAIgA/AD4APAByAGUAcwB1AGwAdAAgAFIAZQBzAHUAbAB0AEMA
  bwBkAGUAPQAiADAAIgA+ADwAZQAgAE4AYQBtAGUAPQAiAEkAbgB0AGUAbAAoAFIAKQAgAFgAZQBv
  AG4AKABSACkAIABDAFAAVQAgAEUANQAtADIANgA3ADMAIAB2ADQAIABAACAAMgAuADMAMABHAEgA
  egAiACAATQBhAG4AdQBmAGEAYwB0AHUAcgBlAHIAPQAiAEEAbQBlAHIAaQBjAGEAbgAgAE0AZQBn
  AGEAdAByAGUAbgBkAHMAIABJAG4AYwAuACIAIABWAGUAcgBzAGkAbwBuAD0AIgBWAFIAVABVAEEA
  TAAgAC0AIAA2ADAAMAAxADcAMAAyACIAIABSAGUAbABlAGEAcwBlAEQAYQB0AGUAPQAiADIAMAAx
  ADcALQAwADYALQAwADIAIAAwADAAOgAwADAAOgAwADAAIgAgAFMAZQByAGkAYQBsAE4AdQBtAGIA
  ZQByAD0AIgAwADAAMAAwAC0AMAAwADEAOAAtADMANgA4ADIALQA0ADcAMAA4AC0ANwA2ADQAMAAt
  ADcANgAwADAALQAzADMAIgAgAFMATQBCAEkATwBTAEIASQBPAFMAVgBlAHIAcwBpAG8AbgA9ACIA
  MAA5ADAAMAAwADcAIAAiACAALwA+ADwALwByAGUAcwB1AGwAdAA+AA=="~~]]>
  </StateDetails><UserParameters Flags="0" Count="2">
  <Param>{F8C7C37F-B42B-4C0A-B050-2BB44DF1098A}</Param><Param>0</Param>
  </UserParameters></StateMessage></ReportBody></Report>~~'

If the message hasn't been processed, check the state message inbox. The default inbox
location is C:\Program Files\Microsoft Configuration
Manager\inboxes\auth\statesys.box\ . Look for the files in these locations:

<!-- p.1554 -->

     Incoming
     Corrupted
     Process

Check the monitoring view for CMPivot via the following SQL query using the TaskID :

  SQL

  select * from vSMS_CMPivotStatus where TaskID='{F8C7C37F-B42B-4C0A-B050-
  2BB44DF1098A}'

  ７ Note

  For clients that are using version 1810 or higher, state messaging isn't used unless
  the output is larger than 80 KB. When troubleshooting CMPivot in these cases, you
  can get more information when you enable verbose logging on your MPs and the
  site server's SMS_MESSAGE_PROCESSING_ENGINE. For information on how to
  enable verbose logging, see Site server logging options.

  To troubleshoot, refer to the following logs:

        MP_Relay.log

        SMS_MESSAGE_PROCESSING_ENGINE.log

Next steps
     Using CMPivot
     Create and run PowerShell scripts

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1555 -->

Maintenance tasks for Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager sites and hierarchies require regular maintenance and
monitoring to provide services effectively and continuously. Regular maintenance
ensures that the hardware, software, and Configuration Manager database continue to
function correctly and efficiently. Optimal performance greatly reduces the risk of
failure.

To set up alerts and use the status system to monitor the health of Configuration
Manager, see Use the status system and Configure alerts.

Maintenance tasks
Regular maintenance is important to ensure correct site operations. Keep a maintenance
log to document maintenance dates, who did maintenance, and any maintenance-
related comments about the tasks. To maintain your site, consider daily or weekly
maintenance. Some tasks might require a different schedule. Common maintenance can
include both the built-in maintenance tasks and other tasks like account maintenance to
maintain compliance with your company policies.

Use the following information as a guide to help you plan when to do different
maintenance tasks. Use these lists as a starting point, and add tasks that you might
require.

Daily Tasks
The following are maintenance tasks that you might consider for on a daily schedule:

      Check that predefined maintenance tasks that are scheduled to run daily are
      running successfully.

      Check the Configuration Manager database status.

      Check site server status.

      Check Configuration Manager site system inboxes for file backlogs.

<!-- p.1556 -->

     Check site systems status.

     Check the operating system event logs from the site systems.

     Check the SQL Server error log from the site database computer.

     Check system performance.

     Check Configuration Manager alerts.

Weekly Tasks
The following are maintenance tasks that you might consider for a weekly schedule:

     Check that predefined maintenance tasks that are scheduled to run weekly are
     running successfully.

     Delete unnecessary files from site systems.

     Produce and distribute end-user reports if necessary.

     Back up application, security, and system event logs and clear them.

     Check the site database size and verify there's enough available disk space on the
     site database server so that the site database can grow.

     Do SQL Server database maintenance on the site database according to your SQL
     Server maintenance plan.

     Check available disk space on all site systems.

     Run disk defragmentation tools on all site systems.

Periodic Tasks
Some tasks that don't require daily or weekly maintenance are important to ensure
overall site health. These tasks also ensure that security and disaster recovery plans are
up-to-date. The following are maintenance tasks that you might consider for a more
periodic schedule than the daily or weekly tasks:

     Change accounts and passwords, if it's necessary, according to your security plan.

     Review the maintenance plan to check that scheduled maintenance tasks are
     scheduled correctly and effectively depending on configured site settings.

     Review the Configuration Manager hierarchy design for any required changes.

<!-- p.1557 -->

     Check network performance to ensure that changes haven't been made that affect
     site operations.

     Check that Active Directory settings that affect site operations haven't changed.
     For example, check that subnets that are assigned to Active Directory sites and that
     are used as boundaries for Configuration Manager site haven't changed.

     Review your disaster recovery plan for any required changes.

     Do a site recovery according to the disaster recovery plan in a test lab by using a
     backup copy of the most recent backup that the Backup Site Server maintenance
     task created.

     Check hardware for any errors or for available hardware updates.

     Check the overall health of the site.

Maintain the operational health of your site
database
While your Configuration Manager site and hierarchy do the tasks that you schedule
and set up, site components continually add data to the Configuration Manager
database. As the amount of data grows, database performance and the free storage
space in the database decline. You can set up site maintenance tasks to remove aged
data that you no longer require.

Configuration Manager provides predefined maintenance tasks that you can use to
maintain the health of the Configuration Manager database. Not all maintenance tasks
are available at each site, by default. Several tasks are enabled while some aren't, and all
support a schedule that you can set up.

Most maintenance tasks periodically remove out-of-date data from the Configuration
Manager database. Reducing the size of the database by removing unnecessary data
improves the performance and the integrity of the database, which increases the
efficiency of the site and hierarchy. Other tasks, like Rebuild Indexes, help maintain the
database efficiency. Other tasks, like the Backup Site Server task, help you prepare for
disaster recovery.

  ） Important

  When you plan the schedule of any task that deletes data, consider the use of that
  data across the hierarchy. When a task that deletes data runs at a site, the

<!-- p.1558 -->

  information is removed from the Configuration Manager database, and this change
  replicates to all sites in the hierarchy. This deletion can affect other tasks that rely
  on that data. For example, at the central administration site, you might set up
  Discovery to run one time per month to identify non-client computers. You plan to
  install the Configuration Manager client to these computers within two weeks of
  their discovery. However, at one site in the hierarchy, an admin sets up the Delete
  Aged Discovery Data task to run every seven days. The result is that seven days
  after non-client computers are discovered, they are deleted from the Configuration
  Manager database. Back at the central administration site, you prepare to push
  install the Configuration Manager client to these new computers on day 10.
  However, because the Delete Aged Discovery Data task has recently run and
  deleted data that's seven days or older, the recently discovered computers are no
  longer available in the database.

After you install a Configuration Manager site, review the available maintenance tasks
and enable those tasks that your operations require. Review the default schedule of
each task, and when necessary, set up the schedule to fine-tune the maintenance task to
fit your hierarchy and environment. Although the default schedule of each task should
suit most environments, monitor the performance of your sites and database and expect
to fine-tune tasks to increase your deployment's efficiency. Plan to periodically review
the site and database performance and reconfigure maintenance tasks and their
schedules to maintain that efficiency.

Set up maintenance tasks
Each Configuration Manager site supports maintenance tasks that help maintain the
operational efficiency of the site database. By default, several maintenance tasks are
enabled in each site, and all tasks support independent schedules. Maintenance tasks
are set up individually for each site and apply to the database at that site. However,
some tasks, like Delete Aged Discovery Data, affect information that is available in all
sites in a hierarchy.

Only the maintenance tasks that you can set up at a site are displayed in the
Configuration Manager console. For a complete list of maintenance tasks by site type,
see Reference for maintenance tasks for Configuration Manager.

Use the following procedure to help you set up the common settings of maintenance
tasks.

To set up maintenance tasks for Configuration Manager

<!-- p.1559 -->

Site server maintenance tasks can now be viewed, edited, and monitored from their own
tab on the details view of a site server. You can still edit maintenance tasks by choosing
Site Maintenance in the Settings group like you did in previous Configuration Manager
versions.

   1. In the Configuration Manager console, go to Administration > Site Configuration
     >Sites.
   2. Select a site from your list, then click on the Maintenance Tasks tab in the detail
     panel.
   3. Only tasks that are available at the selected site are displayed. Right-click one of
     the maintenance tasks and choose one of the following options:

            Enable - Turn on the task.
            Disable - Turn off the task.
            Edit - Edit the task schedule or its properties.

The Maintenance Tasks tab gives you information such as:

     If the task is enabled
     The task schedule
     Last start time
     Last completion time
     If the task completed successfully

Database reindexing can temporarily impact
the replication link status
When the Configuration Manager database is reindexing, either through the built in
maintenance task or SQL Server Management Studio, you may notice that replication
links will temporarily go into a degraded or failed state during this process. The state
degradation occurs because when a reindex is run on the database tables they're
blocked and can't be written to. It's an offline operation and is fundamental to how

<!-- p.1560 -->

DBCC REINDEX functions. In order for a sync on a replication group to be considered
successful, the site actually has to be able to process the data that it received. This
means that during this reindexing process, the link status can bounce between
degraded, failed, active, and back again. Depending on how much data is being
replicated between the sites, the amount of time to go from a failed state to an active
state will vary from environment to environment.

If the state change during a reindex is problematic for your monitoring, each replication
link has a set of thresholds that can be modified to adjust when the link goes into a
degraded state or when it goes into a failed state. Replication links contain multiple
replication groups, which are broken up into two types: global data and site data. Global
data attempts to sync every one minute and site data syncs every five minutes. By
default, the link changes to degraded when the threshold of 12 failures is reached then
changes to the failed state at 24. To set these thresholds, select the link under the
Database Replication node then select Link Properties. In the Alerts tab, there are
thresholds for setting the link to degraded or failed. By default these values are set to 12
and 24 respectively.

Next steps
Reference for maintenance tasks

Feedback
Was this page helpful?      Yes    No

Provide product feedback
