---
title: "Core infrastructure documentation — pages 2561-2600"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2561-2600
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2561-2600
family: sccm
documentKind: "doc"
abstract: "Introduction to software inventory in Configuration Manager Article • 10/04/2022 Applies to: Configuration Manager (current branch) Use software inventory to collect information about files on client devices. Software inventory can also collect files from client devices and stor"
---

# Core infrastructure documentation — pages 2561-2600

<!-- p.2561 -->

Introduction to software inventory in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use software inventory to collect information about files on client devices. Software
inventory can also collect files from client devices and store them on the site server.
Software inventory is collected when you select the Enable software inventory on
clients setting in client settings. You can also schedule the operation in client settings.

After you enable software inventory and the clients run a software inventory cycle, the
client sends the information to a management point in the client's site. The
management point then forwards the inventory information to the Configuration
Manager site server, which stores the information in the site database.

There are a few ways to view software inventory data:

      Create queries that return devices with specified files.

      Create query-based collections that include devices with specified files.

      Run reports that provide details about files on devices.

      Use Resource Explorer to examine detailed information about the files that were
      inventoried and collected from client devices.

When software inventory runs on a client device, the first report is a full inventory.
Subsequent reports contain only delta inventory information. The site server processes
delta information in the order received. If delta information for a client is missing, the
site server rejects further delta information and directs the client to run a full inventory.

Configuration Manager can discover dual-boot computers but only returns inventory
information from the operating system that's active at the time of inventory.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2562 -->

How to configure software inventory in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This procedure configures the default client settings for software inventory and applies
to all the computers in your hierarchy. If you want to apply these settings to only some
computers, create a custom device client setting and assign it to a collection. For more
information about how to create custom device settings, see How to configure client
settings.

To configure software inventory
   1. In the Configuration Manager console, choose Administration > Client Settings
      Default Client Settings.

   2. On the Home tab, in the Properties group, choose Properties.

   3. In the Default Settings dialog box, choose Software Inventory.

   4. In the Device Settings list, configure the following values:

            Enable software inventory on clients - From the drop-down list, select True.

            Schedule software inventory and file collection schedule - Configures the
            interval at which clients collect software inventory and files.

   5. Configure the client settings that you require. The Software inventory section of
      the About client settings article has a list of the client settings.

      Client computers will be configured with these settings when they next download
      client policy. To initiate policy retrieval for a single client, see How to manage
      clients.

         Tip

        Error code 80041006 in inventoryprovider.log means the WMI provider is out
        of memory. That is, the memory quota limit for a provider has been hit and
        inventory provider cannot continue. In this case, the inventory agent creates a
        report with 0 entries so no inventory items are reported.
        A possible solution for this error would be to reduce the scope of the software

<!-- p.2563 -->

        inventory collection. In circumstances when the error occurs after limiting the
        inventory scope, increasing the MemoryPerHost          property defined in the
        _ProviderHostQuotaConfiguration class can provide a solution.

To exclude folders from software inventory
   1. Using Notepad.exe, create an empty file named Skpswi.dat.

   2. Right-click the Skpswi.dat file and click Properties. In the file properties for the
     Skpswi.dat file, select the Hidden attribute.

   3. Place the Skpswi.dat file at the root of each client hard drive or folder structure
     that you want to exclude from software inventory.

  ７ Note

  Software inventory will not inventory the client drive again unless this file is deleted
  from the drive on the client computer.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2564 -->

How to use Resource Explorer to view
software inventory in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use Resource Explorer in Configuration Manager to view information about software
inventory that has been collected from computers in your hierarchy.

  ７ Note

  Resource Explorer will not display any inventory data until a software inventory
  cycle has run on the client.

Resource Explorer provides the following software inventory information:

      Software:

         Collected Files - Files that were collected during software inventory.

         File Details - Files that were inventoried during software inventory that are not
         associated with a specific product or manufacturer.

         Last Software Scan - Date and time of the last software inventory and file
         collection for the client computer.

         Product Details - Software products that were inventoried by software
         inventory, grouped by manufacturer.

To run Resource Explorer from the
Configuration Manager console
   1. In the Configuration Manager console, choose Assets and Compliance

   2. In the Assets and Compliance workspace, choose Devices or open any collection
      that displays devices.

   3. Choose the computer containing the inventory that you want to view and then, in
      the Home tab > Devices group, choose Start > Resource Explorer.

<!-- p.2565 -->

   4. You can right-click any item in the right-pane of the Resource Explorer window and
     choose Properties to view the collected inventory information in a more readable
     format.

View and manage collected diagnostic files
Starting in Configuration Manager version 2002, use Resource Explorer to view and
manage the files gathered when you use client notification to collect client logs.

   1. From the Devices node, right-click on the device you want to view logs for.
   2. Select Start, then Resource Explorer.
   3. From Resource Explorer, click on Diagnostic Files.
   4. In the Diagnostic Files list, you can see the collection date for the files. The name
     format of the client logs is Support_<guid>.zip .
   5. Right-click on the zip file and select one of the following options:

           Open Support Center: Launches Support Center.
           Copy: Copies the row information from Resource Explorer.
           View file: Opens the folder where the zip file is located with File Explorer.
           Save: Opens a Save File dialog for the selected file.
           Export: Saves the Resource Explorer columns shown in Diagnostic Files.
           Refresh: Refreshes the file list.
           Properties: Returns the properties on the selected file.

                                                                                       

Next steps
Use Support Center to view collected diagnostic files.

Feedback

<!-- p.2566 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2567 -->

Security and privacy for software
inventory in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic contains security and privacy information for software inventory in
Configuration Manager.

Security best practices for software inventory
Use the following security best practices for when you collect software inventory data
from clients:

                                                                                   ﾉ    Expand table

 Security best           More information
 practice

 Sign and encrypt        When clients communicate with management points by using HTTPS, all
 inventory data          data that they send is encrypted by using SSL. However, when client
                         computers use HTTP to communicate with management points on the
                         intranet, client inventory data and collected files can be sent unsigned
                         and unencrypted. Make sure that the site is configured to require signing
                         and use encryption. In addition, if clients can support the SHA-256
                         algorithm, select the option to require SHA-256.

 Do not use file         Configuration Manager software inventory uses all the rights of the
 collection to collect   LocalSystem account, which has the ability to collect copies of critical
 critical files or       system files, such as the registry or security account database. When
 sensitive information   these files are available at the site server, someone with the Read
                         Resource rights or NTFS rights to the stored file location could analyze
                         their contents and possibly discern important details about the client in
                         order to be able to compromise its security.

 Restrict local          A user with local administrative rights can send invalid data as inventory
 administrative rights   information.
 on client computers

Security issues for software inventory
Collecting inventory exposes potential vulnerabilities. Attackers can perform the
following:

<!-- p.2568 -->

     Send invalid data, which will be accepted by the management point even when the
     software inventory client setting is disabled and file collection is not enabled.

     Send excessively large amounts of data in a single file and in lots of files, which
     might cause a denial of service.

     Access inventory information as it is transferred to Configuration Manager.

     If users know that they can create a hidden file named Skpswi.dat and place it in
     the root of a client hard drive to exclude it from software inventory, you will not be
     able to collect software inventory data from that computer.

     Because a user with local administrative privileges can send any information as
     inventory data, do not consider inventory data that is collected by Configuration
     Manager to be authoritative.

     Software inventory is enabled by default as a client setting.

Privacy information for software inventory
Hardware inventory allows you to retrieve any information that is stored in the registry
and in WMI on Configuration Manager clients. Software inventory allows you to discover
all files of a specified type or to collect any specified files from clients. Asset Intelligence
enhances the inventory capabilities by extending hardware and software inventory and
adding new license management functionality.

Hardware inventory is enabled by default as a client setting and the WMI information
collected is determined by options that you select. Software inventory is enabled by
default but files are not collected by default. Asset Intelligence data collection is
automatically enabled, although you can select the hardware inventory reporting classes
to enable.

Inventory information is not sent to Microsoft. Inventory information is stored in the
Configuration Manager database. When clients use HTTPS to connect to management
points, the inventory data that they send to the site is encrypted during the transfer. If
clients use HTTP to connect to management points, you have the option to enable
inventory encryption. The inventory data is not stored in encrypted format in the
database. Information is retained in the database until it is deleted by the site
maintenance tasks Delete Aged Inventory History or Delete Aged Collected Files every
90 days. You can configure the deletion interval.

Before you configure hardware inventory, software inventory, file collection, or Asset
Intelligence data collection, consider your privacy requirements.

<!-- p.2569 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2570 -->

Introduction to asset intelligence in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in November 2021, this feature of Configuration Manager is deprecated.
  For more information, see Asset intelligence deprecation.

  This deprecation plan doesn't include the product lifecycle dashboard.

Inventory and manage software license usage throughout your enterprise by using the
asset intelligence catalog. Asset intelligence adds hardware inventory classes to improve
the breadth of information that Configuration Manager collects. This information
includes the hardware and software titles used in your environment. Over 60 reports
present this information in an easy-to-use format. Many of these reports link to more
specific reports. Query for general information and drill down to more detailed
information.

Add custom information to the asset intelligence catalog. For example, custom software
categories, software families, software labels, and hardware requirements. To
dynamically update the asset intelligence catalog with the most current information
available, connect it to the Microsoft Cloud.

Use asset intelligence to help reconcile your enterprise software license usage. Import
software license information into the Configuration Manager site database to view it
against what software is being used.

Asset intelligence catalog
The asset intelligence catalog is a set of database tables stored in the site database.
These tables include categorization and identification information for over 300,000
software titles and versions. They also help manage hardware requirements for specific
software titles.

Asset intelligence provides software license information for software titles that are being
used, both of Microsoft and of non-Microsoft software. A predefined set of hardware
requirements for software titles is available in the asset intelligence catalog, and you can

<!-- p.2571 -->

create new user-defined hardware requirement information to meet custom
requirements. You can also customize information in the asset intelligence catalog, and
you can upload software title information to the Microsoft cloud for categorization.

Asset intelligence catalog updates that include newly released software are available for
download periodically to perform bulk catalog updates. It can also be dynamically
updated by using the asset intelligence synchronization point.

Software categories
Asset intelligence software categories are used to widely categorize inventoried
software titles and as high-level groupings of more specific software families. For
example, a software category could be energy companies, and a software family within
that software category could be oil and gas or hydroelectric. Many software categories
are predefined in the asset intelligence catalog. You can create user-defined categories
to additionally define inventoried software. The validation state for all predefined
software categories is always Validated. Custom software category information added to
the asset intelligence catalog is User Defined.

For more information about how to manage software categories, see Configuring asset
intelligence.

  ７ Note

  Predefined software category information stored in the asset intelligence catalog is
  read-only. You can't change or delete it. Administrative users can add, modify, or
  delete user-defined software categories.

Software families
Asset intelligence software families are used to define inventoried software titles within
software categories. Many software families are predefined in the asset intelligence
catalog. You can create user-defined categories to additionally define inventoried
software. The validation state for all predefined software families is always Validated.
Custom software family information added to the asset intelligence catalog is User-
Defined.

For more information about how to manage software families, see Configuring asset
intelligence.

  ７ Note

<!-- p.2572 -->

  Predefined software family information is read-only and can't be changed.
  Administrative users can add, modify, or delete user-defined software families.

Software labels
Asset intelligence custom software labels let you create filters to group software titles
and to view them in asset intelligence reports. Use software labels to create user-
defined groups of software titles that share a common attribute. For example, you could
create a software label called Shareware, associate it with inventoried shareware titles,
and run a report to display all software titles with that label. There are no predefined
labels. The validation state for software labels is always User Defined.

For more information about how to manage software labels, see Configuring asset
intelligence.

Hardware requirements
Use the hardware requirements information to verify that computers meet the hardware
requirements for software titles before they're targeted for software deployments.
Manage hardware requirements for software titles in the Assets and Compliance
workspace in the Hardware Requirements node under the Asset Intelligence node.

Many hardware requirements are predefined in the asset intelligence catalog. Create
new user-defined hardware requirement information to meet custom requirements. The
validation state for all predefined hardware requirements is always Validated. User-
defined hardware requirements information added to the asset intelligence catalog is
User Defined.

For more information about how to manage hardware requirements, see Configuring
asset intelligence.

  ７ Note

  The hardware requirements displayed in the Configuration Manager console are
  retrieved from the asset intelligence catalog. They aren't based on inventoried
  software title information from clients.

  Hardware requirement information isn't updated as part of the synchronization
  process with Microsoft.

<!-- p.2573 -->

  You can create user-defined hardware requirements for inventoried software that
  doesn't have associated hardware requirements.

By default, the following information is displayed for each listed hardware requirement:

     Software Title: The software title associated with the hardware requirement

     Minimum CPU (MHz): The minimum processor speed in megahertz (MHz)
     required by the software title

     Minimum RAM (KB): The minimum RAM in kilobytes (KB) required by the software
     title

     Minimum Disk Space (KB): The minimum free hard disk space in KB required by
     the software title

     Minimum Disk Size (KB): The minimum hard disk size in KB required by the
     software title

     Validation State: The validation state for the hardware requirement

Predefined hardware requirements stored in the asset intelligence catalog are read-only
and can't be deleted. Administrative users can add, modify, or delete user-defined
hardware requirements for software titles that aren't stored in the asset intelligence
catalog.

Inventoried software titles
To view inventoried software title information in the Configuration Manager console, go
to the Assets and Compliance workspace, expand the Asset Intelligence node, and
select the Inventoried Software node. The hardware inventory agent collects the
inventoried software information from Configuration Manager clients based on the
software titles stored in the asset intelligence catalog.

  ７ Note

  The hardware inventory agent collects inventory based on the asset intelligence
  hardware inventory reporting classes that you enable. For more information about
  how to enable the reporting classes, see Configuring asset intelligence.

By default, the following information is displayed for each inventoried software title:

     Name: The name of the inventoried software title

<!-- p.2574 -->

     Vendor: The name of the vendor that developed the inventoried software title

     Version: The product version of the inventoried software title

     Category: The software category that's currently assigned to the inventoried
     software title

     Family: The software family that's currently assigned to the inventoried software
     title

     Label [1, 2, and 3]: The custom labels associated with the software title. Inventoried
     software titles can have up to three custom labels associated with them.

     Count: The number of Configuration Manager clients that have inventoried the
     software title

     State: The validation state for the inventoried software title

  ７ Note

  You can change the categorization information for inventoried software only at the
  top-level site in your hierarchy. This information includes product name, vendor,
  software category, and software family. After you modify the categorization
  information for predefined software, the validation state for the software changes
  from Validated to User Defined.

Asset intelligence synchronization point
The asset intelligence synchronization point is a Configuration Manager site system role.
It's used to connect to the Microsoft cloud on TCP port 443 to manage dynamic catalog
information updates. Install this site role only on the top-level site of the hierarchy.
Configure all asset intelligence catalog customization by using a Configuration Manager
console connected to the top-level site.

While you configure all updates at the top-level site, catalog information is replicated to
other sites in the hierarchy. The site role lets you request on-demand catalog
synchronization with Microsoft, or schedule automatic catalog synchronization. In
addition to downloading new catalog information, the asset intelligence synchronization
point can upload custom software title information to Microsoft for categorization.
Microsoft treats all uploaded software titles as public information. Make sure that your
custom software titles don't include confidential or proprietary information.

<!-- p.2575 -->

After you submit an uncategorized software title, Microsoft doesn't review it until there
are at least four categorization requests from customers for the same software title.
Then Microsoft researchers identify, categorize, and make the software title
categorization information available to all customers who are using the online service.
Software titles that represent the most requests for categorization receive the highest
priority to categorize. Custom software and line-of-business applications are unlikely to
receive a category. Don't send these software titles to Microsoft for categorization.

An asset intelligence synchronization point is required to connect to the Microsoft
cloud. For information about how to install the role, see Configuring asset intelligence.

Asset intelligence home page
The Asset Intelligence node in the Assets and Compliance workspace is the home page
for asset intelligence in Configuration Manager. This home page displays a summary
dashboard view for asset intelligence catalog information.

  ７ Note

  The Asset Intelligence home page doesn't automatically update while you're
  viewing it.

The Asset Intelligence home page includes the following sections:

     Catalog Synchronization: Information about whether asset intelligence is enabled
     and the current status of the asset intelligence synchronization point.

        ７ Note

        The home page only displays this section when you install an asset
        intelligence synchronization point.

     The section also provides the following information:

        Synchronization schedule

        If you've imported a customer license statement

        The last status update

        The time for the next scheduled update

<!-- p.2576 -->

        The number of changes after you installed the asset intelligence synchronization
        point

     Inventoried Software Status: The count and percentage of inventoried software,
     software categories, and software families that are identified by Microsoft,
     identified by an administrator, pending online identification, or unidentified and
     not pending. The information displayed in table format shows the count for each,
     and the information displayed in the chart shows the percentage for each.

Asset intelligence reports
The asset intelligence reports are located in the Configuration Manager console, in the
Monitoring workspace, in the Asset intelligence folder under the Reporting node. The
reports provide information about hardware, license management, and software. For
more information about reports in Configuration Manager, see Introduction to
reporting.

  ７ Note

  The accuracy of the quantity of installed software titles and license information
  displayed in asset intelligence reports might vary from the actual number of
  software titles installed or licenses that are used in the environment. This variation
  is because of the complex dependencies and limitations involved in inventorying
  software license information for software titles that are installed in enterprise
  environments. Don't use asset intelligence reports as the sole source for
  determining purchased software license compliance.

Hardware reports
Asset intelligence hardware reports provide information about hardware assets in the
organization. By using hardware inventory information such as speed, memory, and
peripheral devices, asset intelligence hardware reports can present information about
USB devices, about hardware that must be upgraded, and even about computers that
aren't ready for a specific software upgrade.

  ７ Note

<!-- p.2577 -->

  Some user data in asset intelligence hardware reports is collected from the
  Windows security event log. For better report accuracy, clear this log when you
  reassign a computer to a new user.

License management reports
Asset intelligence license management reports provide data about licenses that are
being used. The License Ledger report lists installed Microsoft applications in a format
congruent with a Microsoft License Statement (MLS). This format provides a convenient
method of matching acquired licenses with used licenses. Other license management
reports provide information about computers acting as servers that run the key
management service (KMS) for Windows activation statistics.

  ） Important

  Several of the asset intelligence license management reports present information
  about the function of KMS, a method of administering volume licensing. If you
  haven't implemented a KMS server, some reports might not return any data.

Software reports
Asset intelligence software reports provide information about software families,
categories, and specific software titles that are installed on computers in the
organization. The software reports present information such as browser helper objects
and software that starts automatically. These reports can be used to identify adware,
spyware, and other malware. You can also use them to identify software redundancy to
help streamline software acquisition and support.

Software identification tag reports
Asset intelligence software identification tag reports provide information about software
that includes a software identification tag compliant with ISO/IEC 19770-2. The software
identification tags provide authoritative information used to identify installed software.
When you enable the SMS_SoftwareTag hardware inventory reporting class,
Configuration Manager collects information about the software with software
identification tags.

The following reports provide information about the software:

<!-- p.2578 -->

     Software 14A - Search for software identification tag enabled software: The
     count of installed software with a software identification tag enabled

     Software 14B - Computers with specific software identification tag enabled
     software installed: All computers that have installed software with a specific
     software identification tag enabled

     Software 14C - Installed software identification tag enabled software on a
     specific computer: All installed software with a specific software identification tag
     enabled on a specific computer

Reporting limitations
Asset intelligence reports can provide large amounts of information about installed
software titles and acquired software licenses that are being used. Don't use this
information as the only source for determining acquired software license compliance.

Example dependencies

The accuracy of the quantity displayed in the asset intelligence reports for installed
software titles and license information can vary from the actual amounts currently used.
This variation is caused by the complex dependencies involved in inventorying software
license information for software titles in use in enterprise environments. The following
examples show the dependencies involved in inventorying installed software in the
enterprise by using asset intelligence that might affect the accuracy of asset intelligence
reports:

     Client hardware inventory dependencies: Asset intelligence installed software
     reports are based on data collected from Configuration Manager clients by
     extending hardware inventory to enable asset intelligence reporting. Because of
     this dependency on hardware inventory reporting, asset intelligence reports reflect
     data only from clients that successfully complete hardware inventory processes
     with the required asset intelligence WMI reporting classes enabled. Because
     Configuration Manager clients perform hardware inventory processes on a
     schedule defined by the administrative user, a delay might occur in data reporting
     that affects the accuracy of asset intelligence reports.

     For example, an inventoried licensed software title might be uninstalled after the
     client finishes a successful hardware inventory cycle. Asset intelligence reports
     display the software title as installed until the client's next scheduled hardware
     inventory reporting cycle.

<!-- p.2579 -->

     Software packaging dependencies: Asset intelligence reports are based on
     installed software title data collected by using standard Configuration Manager
     client hardware inventory processes. Some software title data might not be
     collected correctly. Examples that could cause inaccurate asset intelligence
     reporting:

        Software installations that don't comply with standard installation processes

        Software installations that were changed before installation

Legal limitations

The information displayed in asset intelligence reports is subject to many limitations.
The information displayed in them doesn't represent legal, accounting, or other
professional advice. The information provided by asset intelligence reports is for
information only. Don't use it as the only source of information for determining software
license usage compliance.

The following limitations are examples of using asset intelligence that might affect the
accuracy of the reports:

     Microsoft license usage quantity limitations:

        The quantity of acquired Microsoft software licenses is based on information
        that administrators supply. Closely review it to make sure that the correct
        number of software licenses is provided.

        The reported quantity of Microsoft software licenses includes information only
        about Microsoft software licenses acquired through volume licensing programs.
        It doesn't reflect information for software licenses acquired through retail, OEM,
        or other software license sales channels.

        Software licenses acquired in the last 45 days might not be included in the
        quantity of Microsoft software licenses reported because of software reseller
        reporting requirements and schedules.

        Software license transfers from company mergers or acquisitions might not be
        reflected in Microsoft software license quantities.

        Nonstandard terms and conditions in a Microsoft Volume Licensing (MVLS)
        agreement might affect the number of software licenses reported. They might
        require additional review by a Microsoft representative.

<!-- p.2580 -->

     Installed software title quantity limitations: Configuration Manager clients must
     successfully complete hardware inventory reporting cycles for the asset
     intelligence reports to accurately report the quantity of installed software titles.
     There might be a delay between the installation or uninstallation of a licensed
     software title after a successful hardware inventory reporting cycle. This action may
     not be reflected in asset intelligence reports run before the client reports its next
     scheduled hardware inventory.

     License reconciliation limitations: The reconciliation of the quantity of installed
     software titles to the quantity of acquired software licenses is calculated by using a
     comparison of the license quantity specified by the administrator and the quantity
     of installed software titles collected from Configuration Manager client hardware
     inventories based on the schedule set by the administrator. This comparison
     doesn't represent a final Microsoft conclusion of the license positions. The actual
     license position depends on the specific software title license and usage rights
     granted by the license terms.

Asset intelligence validation states
Asset intelligence validation states represent the source and current validation status of
asset intelligence catalog information. The following table shows possible asset
intelligence validation states and administrator actions that can cause them.

                                                                               ﾉ   Expand table

 State           Definition                   Administrator action        Comment

 Validated       Microsoft researchers        None                        Best state
                 defined the catalog item

 User Defined    Microsoft researchers        Customize the local         This state is displayed
                 haven't defined the          catalog information         in asset intelligence
                 catalog item                                             reports

 Pending         Microsoft researchers        No further action after     Catalog item remains
                 haven't defined the          requesting categorization   in this state until
                 catalog item, but you                                    Microsoft researchers
                 submitted the item to                                    categorize the item,
                 Microsoft for                                            and you synchronize
                 categorization                                           your asset intelligence
                                                                          catalog

 Updateable      A user-defined catalog       Use the Resolve Conflict    After you resolve a
                 item has been                action to decide whether    categorization conflict,
                 categorized differently by   to use the new              the item isn't

<!-- p.2581 -->

 State            Definition                 Administrator action        Comment

                  Microsoft during catalog   categorization              validated as
                  synchronization.           information or the          conflicting again
                                             previous user-defined       unless later
                                             value. For more             categorization
                                             information about how to    updates introduce
                                             resolve conflicts, see      new information
                                             Operations for asset        about the item.
                                             intelligence.

 Uncategorized    Catalog item hasn't been   Request categorization or   None
                  defined by Microsoft       customize your local
                  researchers, the item      catalog information. For
                  hasn't been submitted to   more information, see
                  Microsoft for              Operations for asset
                  categorization, and the    intelligence.
                  administrator hasn't
                  assigned a user-defined
                  categorization value.

  ７ Note

  Catalog items that you submit to Microsoft for categorization have a validation
  state of Pending on a central administration site, but continue to be displayed with
  a validation state of Uncategorized on child primary sites.

For examples of when a validation state might transition from one state to another, see
Example validation state transitions for asset intelligence.

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.2582 -->

Prerequisites for Asset Intelligence in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Asset Intelligence in Configuration Manager has external dependencies and
dependencies within the product.

Dependencies external to Configuration
Manager
The following table provides the dependencies for Asset Intelligence that are external to
Configuration Manager.

                                                                                   ﾉ    Expand table

 Dependency            More Information

 Auditing of           Four Asset Intelligence reports display information gathered from the
 Success Logon         Windows Security event logs on client computers. If the Security event log
 Events                settings are not configured to log all Success logon events, these reports
 Prerequisites         contain no data even if the appropriate hardware inventory reporting class is
                       enabled.

                       The following Asset Intelligence reports depend on collected Windows
                       Security event log information:

                       - Hardware 03A - Primary Computer Users
                       - Hardware 03B - Computers for a Specific Primary Console User
                       - Hardware 04A - Shared (Multi-user) Computers
                       - Hardware 05A - Console Users on a Specific Computer

                       To enable the Hardware Inventory Client Agent to inventory the information
                       required to support these reports, you must first modify the Windows Security
                       event log settings on clients to log all Success logon events, and enable the
                       SMS_SystemConsoleUser hardware inventory reporting class. For more
                       information about modifying Security event log settings to log all Success
                       logon events, see Enable auditing of success logon events.

  ７ Note

<!-- p.2583 -->

  The SMS_SystemConsoleUser hardware inventory reporting class retains successful
  logon event data for only the previous 90 days of the Security event log, regardless
  of the length of the log. If the Security event log has fewer than 90 days of data, the
  entire log is read.

Dependencies Internal to Configuration
Manager
The following table provides the dependencies for Asset Intelligence that are internal to
Configuration Manager.

                                                                                   ﾉ   Expand table

 Dependency             More Information

 Client Agent           The Asset Intelligence reports depend on client information that is
 Prerequisites          obtained through client hardware and software inventory reports. To
                        obtain the information necessary for all Asset Intelligence reports, the
                        following client agents must be enabled:

                        - Hardware Inventory Client Agent
                        - Software Metering Client Agent

 Hardware Inventory     To collect inventory data required for some Asset Intelligence reports, the
 Client Agent           Hardware Inventory Client Agent must be enabled. In addition, some
 Dependencies           hardware inventory reporting classes that Asset Intelligence reports
                        depend on must be enabled on primary site server computers.

                        For information about enabling the Hardware Inventory Client Agent, see
                        How to extend hardware inventory.

 Software Metering      A number of Asset Intelligence software reports depend on the Software
 Client Agent           Metering Client Agent for data. For information about enabling the
 Dependencies           Software Metering Client Agent, see Monitor app usage with software
                        metering.

                        The following Asset Intelligence reports depend on the Software Metering
                        Client Agent to provide data:

                        - Software 07A - Recently Used Executables by Number of Computers
                        - Software 07B - Computers that Recently Used a Specified Executable
                        - Software 07C - Recently Used Executables on a Specific Computer
                        - Software 08A - Recently Used Executables by Number of Users
                        - Software 08B - Users that Recently Used a Specified Executable
                        - Software 08C - Recently Used Executables by a Specified User

<!-- p.2584 -->

 Dependency              More Information

 Asset Intelligence      Asset Intelligence reports in Configuration Manager depend on specific
 Hardware Inventory      hardware inventory reporting classes. Until the hardware inventory
 Reporting Class         reporting classes are enabled and clients have reported hardware
 Prerequisites           inventory based on these classes, the associated Asset Intelligence reports
                         do not contain any data. You can enable the following hardware inventory
                         reporting classes to support Asset Intelligence reporting requirements:

                         - SMS_SystemConsoleUsage1
                         - SMS_SystemConsoleUser1
                         - SMS_InstalledSoftware
                         - SMS_AutoStartSoftware
                         - SMS_BrowserHelperObject
                         - Win32_USBDevice
                         - SMS_InstalledExecutable
                         - SMS_SoftwareShortcut
                         - SoftwareLicensingService
                         - SoftwareLicensingProduct
                         - SMS_SoftwareTag

                         1 By default, the SMS_SystemConsoleUsage and SMS_SystemConsoleUser

                         Asset Intelligence hardware inventory reporting classes are enabled.

                         You can edit the Asset Intelligence hardware inventory reporting classes in
                         the Configuration Manager console, in the Assets and Compliance
                         workspace, when you click the Asset Intelligence node. For more
                         information, see the Enable Asset Intelligence hardware inventory
                         reporting classes section in the Configuring Asset Intelligence topic.

 Reporting services      The reporting services point site system role must be installed before
 point                   software updates reports can be displayed. For more information about
                         creating a reporting services point, see Configuring reporting.

Feedback
Was this page helpful?      Yes       No

Provide product feedback

<!-- p.2585 -->

Configure Asset Intelligence in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Asset Intelligence inventories and manages software license usage.

Steps to configure Asset Intelligence
      Step 1:To collect the inventory data required for Asset Intelligence reports, you
      have to enable the hardware inventory client agent as described in How to extend
      hardware inventory.
      Step 2: Enable Asset Intelligence Hardware Inventory Reporting Classes.
      Step 3: Install an Asset Intelligence Synchronization Point
      Step 4: Enable auditing of success logon events
      Step 5: Import Software License Information
      Step 6: Configure Asset Intelligence maintenance tasks

Enable Asset Intelligence hardware inventory reporting
classes
To enable Asset Intelligence in Configuration Manager sites, you must enable one or
more Asset Intelligence hardware inventory reporting classes. You can enable the classes
on the Asset Intelligence home page, or, in the Administration workspace, in the Client
Settings node, in client settings properties. Use one of the following procedures.

To enable Asset Intelligence hardware inventory reporting classes
from the Asset Intelligence home page

   1. In the Configuration Manager console, choose Asset and Compliance > Asset
      Intelligence.

   2. On the Home tab, in the Asset Intelligence group, choose Edit Inventory Classes.

   3. To enable Asset Intelligence reporting, select Enable all Asset Intelligence
      reporting classes or Enable only the selected Asset Intelligence reporting classes,
      and select at least one reporting class from the classes displayed.

<!-- p.2586 -->

         ７ Note

         Asset Intelligence reports that depend on the hardware inventory classes that
         you enable by using this procedure do not display data until clients have
         scanned for and returned hardware inventory.

To enable Asset Intelligence hardware inventory reporting classes
from client settings properties

   1. In the Configuration Manager console, choose Administration > Client Settings >
       Default Client Agent Settings. If you have created custom client settings, you can
       select those instead.

   2. On the Home tab > Properties group, choose Properties.

   3. Choose Hardware Inventory > Set Classes. .

   4. Choose Filter by category > Asset Intelligence Reporting Classes. The list of
       classes is refreshed with only the Asset Intelligence hardware inventory reporting
       classes.

   5. Select at least one reporting class from the list.

         ７ Note

         Asset Intelligence reports that depend on the hardware inventory classes that
         you enable by using this procedure do not display data until clients have
         scanned for and returned hardware inventory.

Install an Asset Intelligence Synchronization Point
The Asset Intelligence synchronization point site system role is used to connect
Configuration Manager sites to System Center Online to synchronize Asset Intelligence
catalog information. The Asset Intelligence synchronization point can only be installed
on a site system located at the top-level site of the Configuration Manager hierarchy
and requires Internet access to synchronize with System Center Online by using TCP port
443.

In addition to downloading new Asset Intelligence catalog information, the Asset
Intelligence synchronization point can upload custom software title information to
System Center Online for categorization. Microsoft treats all uploaded software titles as

<!-- p.2587 -->

public information. Ensure that your custom software titles do not contain confidential
or proprietary information. For more information about requesting software title
categorization, see Request a catalog update for uncategorized software titles.

To install an Asset Intelligence synchronization point site system
role

   1. In the Configuration Manager console, choose Administration> Site
     Configuration > Servers and Site System Roles.

   2. Add the Asset Intelligence synchronization point site system role to a new or
     existing site system server:

          For a New site system server: On the Home tab, in the Create group, choose
          Create Site System Server to start the wizard.

             ７ Note

             By default, when Configuration Manager installs a site system role, the
             installation files are installed on the first available NTFS-formatted hard
             disk drive that has the most available free hard disk space. To prevent
             Configuration Manager from installing on specific drives, create an
             empty file named NO_SMS_ON_DRIVE.SMS and copy it to the root
             folder of the drive before you install the site system server.

          For an Existing site system server: Choose the server on which you want to
          install the Asset Intelligence synchronization point site system role. When you
          choose a server, a list of the site system roles that are already installed on the
          server are displayed in the details pane.

          On the Home tab, in the Server group, choose Add Site System Role to start
          the wizard.

   3. Complete the General page. When you add the Asset Intelligence synchronization
     point to an existing site system server, verify the values that were previously
     configured.

   4. On the System Role Selection page, select Asset Intelligence Synchronization
     Point from the list of available roles.

   5. On the Asset Intelligence Synchronization Point Connection Settings page,
     choose Next.

<!-- p.2588 -->

     By default, the Use this Asset Intelligence Synchronization Point setting is
     selected and cannot be configured on this page. System Center Online accepts
     network traffic only over TCP port 443, therefore the SSL port number setting
     cannot be configured on this page of the wizard.

   6. Optionally, you can specify a path to the System Center Online authentication
     certificate (.pfx) file. Typically, you do not specify a path for the certificate because
     the connection certificate is automatically provisioned during site role installation.

   7. On the Proxy Server Settings page, specify whether the Asset Intelligence
     synchronization point will use a proxy server when connecting to System Center
     Online to synchronize the catalog and whether to use credentials to connect to the
     proxy server.

       ２ Warning

       If a proxy server is required to connect to System Center Online, the
       connection certificate might also be deleted if the user account password
       expires for the account configured for proxy server authentication.

   8. On the Synchronization Schedule page, specify whether to synchronize the Asset
     Intelligence catalog on a schedule. When you enable the synchronization schedule,
     you specify a simple or custom synchronization schedule. During scheduled
     synchronization, the Asset Intelligence synchronization point connects to System
     Center Online to retrieve the latest Asset Intelligence catalog. You can manually
     synchronize the Asset Intelligence catalog from the Asset Intelligence node in the
     Configuration Manager console. For the steps to manually synchronize the Asset
     Intelligence catalog, see the To manually synchronize the Asset Intelligence catalog
     section in the Operations for Asset Intelligence.

   9. Complete the wizard

Enable auditing of success logon events
Four Asset Intelligence reports display information gathered from the Windows Security
event logs on client computers. Here's how to configure computer security policy logon
settings to enable auditing of Success logon events.

To enable success logon event logging by using a local security
policy

<!-- p.2589 -->

   1. On a Configuration Manager client computer, choose Start > Administrative Tools
     > Local Security Policy.

   2. In the Local Security Policy dialog box, under Security Settings, expand Local
     Policies, and then choose Audit Policy.

   3. In the results pane, double-click Audit logon events, ensure that the Success check
     box is selected, and then choose OK.

To enable success logon event logging by using an Active
Directory domain security policy

   1. On a domain controller computer, choose Start, point to Administrative Tools, and
     then choose Domain Security Policy.

   2. In the Local Security Policy dialog box, under Security Settings, expand Local
     Policies, and then choose Audit Policy.

   3. In the results pane, double-click Audit logon events, ensure that the Success check
     box is selected, and then choose OK.

Import software license information
The following sections describe the procedures necessary to import both Microsoft and
general software licensing information into the Configuration Manager site database by
using the Import Software License Wizard. When you import software license
information into the site database from license statement files, the site server computer
account requires Full Control permissions for the NTFS file system to the file share that
is used to import software license information.

  ） Important

  When software license information is imported into the site database, existing
  software license information is overwritten. Ensure that the software license
  information file that you use with the Import Software License Wizard contains a
  complete listing of all necessary software license information.

To import software license information into the Asset Intelligence
catalog

   1. In the Asset and Compliance workspace, choose Asset Intelligence.

<!-- p.2590 -->

   2. On the Home tab, in the Asset Intelligence group, choose Import Software
     Licenses.

   3. On the Import page, specify whether you are importing a Microsoft Volume
     Licensing (MVLS) file (.xml or .csv) or a General License Statement file (.csv). For
     more information about creating a General License Statement file, see Create a
     general license statement information file for import later in this topic.

        ２ Warning

        To download an MVLS file in .csv format that you can import to the Asset
        Intelligence catalog, see Microsoft Volume Licensing Service Center . To
        access this information, you must have a registered account on the website.
        You must contact your Microsoft account representative for information about
        how to get your MVLS file in .xml format.

   4. Enter the UNC path to the license statement file or choose Browse to select a
     network shared folder and file.

        ７ Note

        The shared folder should be correctly secured to prevent unauthorized access
        to the licensing information file, and the computer account of the computer
        that the wizard is being run on must have Full Control permissions to the
        share that contains the license import file.

   5. Complete the wizard.

Create a general license statement information file for
import
A general license statement can also be imported into the Asset Intelligence catalog by
using a manually created license import file in comma delimited (.csv) file format.

  ７ Note

  While only the Name, Publisher, Version, and EffectiveQuantity fields are required
  to contain data, all fields must be entered on the first row of the license import file.
  All date fields should be displayed in the following format: Month/Day/Year, for
  example, 08/04/2008.

<!-- p.2591 -->

Asset Intelligence matches the products that you specify in the general license
statement by using the product name and product version, but not publisher name. You
must use a product name in the general license statement that is an exact match with
the product name stored in the site database. Asset Intelligence takes the
EffectiveQuantity number given in the general license statement and compares the
number with the number of installed products found in Configuration Manager
inventory.

   Tip

  To get a complete list of the product names stored in the Configuration Manager
  site database, you can run the following query on the site database: SELECT
  DISTINCT ProductName0 FROM v_GS_INSTALLED_SOFTWARE.

You can specify exact versions for a product or specify part of the version, such as only
the major version. The following examples provide the resulting version matches for a
general license statement version entry for a specific product.

                                                                            ﾉ   Expand table

 General license statement      Matching site database entries
 entry

 Name: "MySoftware",            ProductName0: "Mysoftware", ProductVersion0: "2.01.1234"
 ProductVersion0:"2"
                                ProductName0: "MySoftware", ProductVersion0: "2.02.5678"

                                ProductName0: "MySoftware", ProductVersion0: "2.05.1234"

                                ProductName0: "MySoftware", ProductVersion0: "2.05.5678"

                                ProductName0: "MySoftware", ProductVersion0:
                                "2.05.3579.000"

                                ProductName0: "MySoftware", ProductVersion0: "2.10.1234"

 Name: "MySoftware", Version    ProductName0: "MySoftware", ProductVersion0: "2.05.1234"
 "2.05"
                                ProductName0: "MySoftware", ProductVersion0: "2.05.5678"

                                ProductName0: "MySoftware", ProductVersion0:
                                "2.05.3579.000"

 Name: "Mysoftware", Version    Error during import. The import fails when more than one entry
 "2"                            matches the same product version.

<!-- p.2592 -->

 General license statement        Matching site database entries
 entry

 Name: "Mysoftware", Version
 "2.05"

To create a general license statement import file by using
Microsoft Excel

   1. Open Microsoft Excel and create a new spreadsheet.

   2. On the first row of the new spreadsheet, enter all software license data field names.

   3. On the second and subsequent rows of the new spreadsheet, enter software
     license information as required. Ensure that at least all of the required software
     license data fields are entered on subsequent rows for each software license to be
     imported. The software title name entered in the spreadsheet must be the same as
     the software title that is displayed in Resource Explorer for a client computer after
     hardware inventory has run.

   4. Save the file in .csv format.

   5. Copy the .csv file to the file share that is used to import software license
     information into the Asset Intelligence catalog.

   6. In the Configuration Manager console, use the Import Software License Wizard to
     import the newly created .csv file.

   7. Run the Asset Intelligence License 15A - Third Party Software Reconciliation
     Report to verify that the licensing information has been successfully imported into
     the Asset Intelligence catalog.

  ７ Note

  For an example of a general software license file that you can use for testing
  purposes, see Example Asset Intelligence general license import file.

Sample table to describe software licenses
When creating a general license statement import file, the information in the following
table can be used to describe software licenses to be imported into the Asset
Intelligence catalog.

<!-- p.2593 -->

                                                                             ﾉ    Expand table

 Column name             Data type                         Required    Example

 Name                    Up to 255 characters              Yes         Software title

 Publisher               Up to 255 characters              Yes         Software publisher

 Version                 Up to 255 characters              Yes         Software title version

 Language                Up to 255 characters              Yes         Software title language

 EffectiveQuantity       Integer value                     Yes         Number of licenses
                                                                       purchased

 PONumber                Up to 255 characters              No          Purchase order
                                                                       information

 ResellerName            Up to 255 characters              No          Reseller information

 DateOfPurchase          Date value in the following       No          Date of license
                         format: MM/DD/YYYY                            purchase

 SupportPurchased        Bit value                         No          0 or 1: Enter 0 for Yes,
                                                                       or 1 for No

 SupportExpirationDate   Date value in the following       No          End date of purchased
                         format: MM/DD/YYYY                            support

 Comments                Up to 255 characters              No          Optional comments

Configure Asset Intelligence maintenance tasks
The following maintenance tasks are available for Asset Intelligence:

     Check Application Title with Inventory Information: Checks that the software title
     that is reported in software inventory is reconciled with the software title in the
     Asset Intelligence catalog. By default, this task is enabled and scheduled to run on
     Saturday after 12:00 A.M. and before 5:00 A.M. This maintenance task is only
     available at the top-level site in your Configuration Manager hierarchy.

     Summarize Installed Software Data: Provides the information that is displayed in
     the Assets and Compliance workspace, in the Inventoried Software node, under
     the Asset Intelligence node. When the task runs, Configuration Manager gathers a
     count for all inventoried software titles at the primary site. By default, this task is
     enabled and scheduled to run every day after 12:00 A.M. and before 5:00 A.M. This
     maintenance task is available only on primary sites.

<!-- p.2594 -->

To configure Asset Intelligence maintenance tasks

   1. In the Configuration Manager console, choose Administration > Site
     Configuration > Sites.

   2. Select the site on which to configure the Asset Intelligence maintenance task.

   3. On the Home tab, in the Settings group, choose Site Maintenance. Select a task,
     and choose Edit to modify the settings.

     We recommend that you set the time period to off-peak hours of the site. The time
     period is the time interval in which the task can run. It is defined by the Start after
     and Latest start time specified in the Task Properties dialog box.

     You can initiate the task right away by selecting the current day and setting the
     Start after time to a couple minutes after the present time.

   4. Choose OK to save your settings. The task now runs according to its schedule.

        ７ Note

        If a task fails to run on the first attempt, Configuration Manager attempts to
        rerun the task until either the task runs successfully or until the time period in
        which the task can run has passed.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2595 -->

How to use Asset Intelligence in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic contains information to help you manage typical Asset Intelligence tasks in
your Configuration Manager hierarchy:

View Asset Intelligence information
You can view Asset Intelligence information on the Asset Intelligence home page and in
Asset Intelligence reports.

Asset Intelligence home page
The Asset Intelligence home page displays a summary dashboard for Asset Intelligence
catalog information. On the home page, you can view information about catalog
synchronization and inventoried software status. The Asset Intelligence home page is
divided into the following sections:

      Catalog Synchronization: Provides information about whether Asset Intelligence is
      enabled, the current status of the Asset Intelligence synchronization point, the
      synchronization schedule, whether the customer license statement is imported,
      when status was last updated and the time for the next scheduled update, and the
      number of changes that occurred after the Asset Intelligence synchronization point
      site system was installed.

        ７ Note

        The Asset Intelligence catalog synchronization section of the Asset
        Intelligence home page is only displayed if an Asset Intelligence
        synchronization point site system role has been installed.

      Inventoried Software Status: Provides the count and percentage of inventoried
      software, software categories, and software families that are identified by
      Microsoft, identified by an administrative user, pending online identification, or
      unidentified and not pending. The information displayed in table format shows the

<!-- p.2596 -->

     count for each, while the information displayed in the chart shows the percentage
     for each.

     Use the following procedure to view Asset Intelligence information on the Asset
     Intelligence home page.

To view Asset Intelligence information on the Asset Intelligence
home page

   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Asset and Compliance workspace, click Asset Intelligence. The Asset
     Intelligence reports are displayed.

Asset Intelligence reports
There are over 60 Asset Intelligence reports that display the information collected by
Asset Intelligence. Many of these reports link to more specific reports in which you can
query for general information and drill down to more detailed information. The Asset
Intelligence reports are located in the Configuration Manager console, in the
Monitoring workspace, under the Reporting node. The reports provide information
about hardware, license management, and software. For more information about reports
in Configuration Manager, see Introduction to reporting.

  ７ Note

  The accuracy of installed software title quantities and license information displayed
  in Asset Intelligence reports might vary from the actual number of software titles
  installed or licenses in use in the environment because of the complex
  dependencies and limitations involved in inventorying software license information
  for software titles installed in enterprise environments. Asset Intelligence reports
  should not be used as the sole source for determining purchased software license
  compliance.

Use the following procedure to view Asset Intelligence information by using the Asset
Intelligence reports.

To view collected Asset Intelligence information by using Asset
Intelligence reports

   1. In the Configuration Manager console, click Monitoring.

<!-- p.2597 -->

   2. In the Monitoring workspace, expand Reporting, expand Reports, and click Asset
     Intelligence. The Asset Intelligence reports are displayed.

        ２ Warning

        If no report folders exist under the Reports node, verify that you have
        configured reporting. For more information, see Configuring reporting.

   3. Select the Asset Intelligence report that you want to run, and then on the Home
     tab, in the Report Group group, click Run.

Synchronize the Asset Intelligence catalog
You can synchronize the local Asset Intelligence catalog with System Center Online to
retrieve the latest software title categorization. When you manually request catalog
synchronization with System Center Online, it could take 15 minutes or longer to
complete the synchronization process with System Center Online. Configuration
Manager updates the Last Successful Update setting on the Asset Intelligence home
page with the current time for when synchronization successfully finishes.

  ７ Note

  An Asset Intelligence synchronization point site system role must first be installed
  before by using the procedures. For information about installing an Asset
  Intelligence synchronization point, see Configuring Asset Intelligence.

Use the following procedure to create a synchronization schedule for the Asset
Intelligence catalog.

To create a synchronization schedule for the Asset Intelligence
catalog

   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, click Asset Intelligence.

   3. On the Home tab, in the Create group, click Synchronize, and then click Schedule
     Synchronization.

   4. In the Asset Intelligence Synchronization Point Schedule dialog box, select Enable
     synchronization on a schedule, and then configure a simple or custom schedule.

<!-- p.2598 -->

   5. Click OK to save the changes.

       ７ Note

       For information about the synchronization schedule, including the next
       scheduled synchronization, see the Asset Intelligence node in the Assets and
       Compliance workspace on the top-level site of the hierarchy.

     Use the following procedure to manually synchronize the Asset Intelligence
     catalog.

  ２ Warning

  System Center Online accepts only one manual synchronization request in a 12-
  hour period.

To manually synchronize the Asset Intelligence catalog
   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, click Asset Intelligence.

   3. On the Home tab, in the Create group, click Synchronize, click Synchronize Asset
     Intelligence Catalog, and then click OK.

Customize the Asset Intelligence catalog
Asset Intelligence catalog categorization information received from System Center
Online is stored in the site database with read-only permissions and cannot be modified
or deleted. However, you can create, modify, and delete custom software categories,
software families, software labels, and hardware requirements catalog information. Then
you can use custom categorization data instead of the information supplied by System
Center Online for existing or user-defined software title information. When you change
or add categorization information, the catalog information is considered user-defined.
User-defined categorization information is stored in different database tables than
validated catalog information.

Software categories

<!-- p.2599 -->

Asset Intelligence software categories are used to broadly categorize inventoried
software titles and are also used as high-level groupings of more specific software
families. For example, a software category could be energy companies, and a software
family within that software category could be oil and gas or hydroelectric. Many
software categories are predefined in the Asset Intelligence catalog, and additional user-
defined categories can be created to further define inventoried software. The validation
state for all predefined software categories is always Validated, while custom software
category information added to the Asset Intelligence catalog is User Defined.

Use the following procedure to create a user-defined software category.

To create a user-defined software category

   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, click Asset Intelligence, and then click
     Catalog.

   3. On the Home tab, in the Create group, click Create Software Category.

   4. On the General page, enter a name for the new software category and, optionally,
     a description.

        ７ Note

        The validation state for all new custom software categories is always set to
        User Defined.

     Click Next.

   5. On the Summary page, review the settings, and then click Next.

   6. On the Completion page, click Close to exit the wizard.

Software families
Asset Intelligence software families are used to further define inventoried software titles
within software categories. For example, a software category could be energy
companies, and a software family within that software category could be oil and gas or
hydroelectric. Many software families are predefined in the Asset Intelligence catalog,
and additional user-defined families can be created to define inventoried software. The
validation state for all predefined software families is always Validated, while custom
software family information added to the Asset Intelligence catalog is User Defined.

<!-- p.2600 -->

Use the following procedure to create a user-defined software family.

To create a user-defined software family

   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, click Asset Intelligence, and then click
     Catalog.

   3. On the Home tab, in the Create group, click Create Software Family.

   4. On the General page, enter a name for the new software family and, optionally, a
     description.

        ７ Note

        The validation state for all new custom software families is always set to User
        Defined.

   5. On the Summary page, review the settings, and then click Next.

   6. On the Completion page, click Close to exit the wizard.

Software labels
Asset Intelligence custom software labels let you create filters that you can use to group
software titles and view them by using Asset Intelligence reports. For example, you can
create a software label called shareware, associate it with a number of applications, and
then run a report that shows you all titles with the software label of shareware. The
validation state is User Defined for all custom software labels that you add to the Asset
Intelligence catalog.

Use the following procedure to create a user-defined custom label.

To create a user-defined software label

   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, click Asset Intelligence, and then click
     Catalog.

   3. On the Home tab, in the Create group, click Create Software Label.
