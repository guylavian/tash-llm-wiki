---
title: "Core infrastructure documentation — pages 561-600"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0561-0600
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0561-0600
family: sccm
documentKind: "doc"
abstract: "Diagnostics and usage data for Configuration Manager Applies to: Configuration Manager (current branch) Configuration Manager collects diagnostics and usage data about itself, which is used by Microsoft to improve the installation experience, quality, and security of future rele"
---

# Core infrastructure documentation — pages 561-600

<!-- p.561 -->

Diagnostics and usage data for
Configuration Manager
Applies to: Configuration Manager (current branch)

Configuration Manager collects diagnostics and usage data about itself, which is used by
Microsoft to improve the installation experience, quality, and security of future releases. With
version 2509, no further changes or updates are planned for diagnostic and usage data
collection.

Each Configuration Manager hierarchy enables diagnostics and usage data. It consists of SQL
Server queries that run on a weekly basis on each primary site and at the central administration
site (CAS). When the hierarchy uses a CAS, child primary sites replicate their data to that CAS. At
the top-level site of your hierarchy, the service connection point submits this information when it
checks for updates. If the service connection point is in offline mode, you transfer the information
by using the service connection tool.

  ７ Note

  Configuration Manager collects data only from the site's SQL Server database, and it doesn't
  collect data directly from clients or site servers.

For more information, see the Microsoft privacy statement     .

Next, learn about how Microsoft uses the diagnostics and usage data that Configuration
Manager collects:

  How Microsoft uses diagnostics and usage data

   Tip

  The ConfigurationManager PowerShell module also collects usage data. For more
  information, see Configuration Manager cmdlet library privacy statement.

  Some of the tools that are included with Configuration Manager collect usage data. For
  more information, see Diagnostic usage data for tools.

<!-- p.562 -->

Last updated on 06/04/2026

<!-- p.563 -->

How Microsoft uses Configuration
Manager diagnostics and usage data
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Diagnostic and usage data that Configuration Manager collects provides Microsoft
nearly immediate feedback about how the product is working and is used to adjust
future updates. Microsoft can also see configuration data that helps them engineer and
test the configurations that you use in production. For example:

      The Windows server versions used on site servers

      Installed language packs

      The delta of the SQL Server schema against the product default

This data helps the engineering team plan future tests to make sure you have the best
experience with the most common configurations. This data is crucial to quickly adjust
and adapt with a frequent release cycle.

Equally important is how the diagnostics and usage data isn't used. Microsoft doesn't
use this data for:

      Licensing audits, such as comparing customer usage against license agreements

      Auditing of products that are out of support

      Advertising based on available data such as feature usage or geolocation (time
      zone)

Microsoft uses available data to improve the product. For example:

      The initial support offered by the current branch of Configuration Manager limited
      the support timeline for Windows Server 2008 R2. Microsoft examined the usage
      data from customers who had upgraded to the Configuration Manager current
      branch. They then identified the need to revise and extend this timeline to support
      customers who still use this OS.

      Microsoft improved the prerequisite checks for installing an update. They removed
      obsolete rules, accounted for additional cases, and automatically remediated some
      issues.

<!-- p.564 -->

Next, learn about how Configuration Manager collects diagnostics and usage data
about itself:

  How Configuration Manager collects data

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.565 -->

How Configuration Manager collects
diagnostics and usage data
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To collect diagnostics and usage data for Configuration Manager, each primary site runs
SQL Server queries on a weekly basis. In a multi-site hierarchy, the data is replicated to
the central administration site.

At the top-level site of a hierarchy, the service connection point submits this information
when it checks for updates. The mode of the service connection point determines how
the data is transferred:

      Online: Once a week, the service connection point automatically sends diagnostics
      and usage data to the cloud service.

      Offline: You manually transfer diagnostics and usage data with the service
      connection tool.

For more information, see About the service connection point.

Next, you can view diagnostic and usage data to confirm that your Configuration
Manager hierarchy contains no sensitive information:

  How to view diagnostics and usage data

   Tip

  The ConfigurationManager PowerShell module also collects usage data. For more
  information, see Configuration Manager cmdlet library privacy statement.

  Some of the tools that are included with Configuration Manager collect usage data.
  For more information, see Diagnostic usage data for tools.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.566 -->

How to view diagnostics and usage data
for Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can view diagnostic and usage data from your Configuration Manager hierarchy to
confirm that it includes no sensitive or identifiable information. The site summarizes and
stores its diagnostic data in the TEL_TelemetryResults table of the site database. It
formats the data to be programmatically usable and efficient.

The information in this article gives you a view of the exact data sent to Microsoft. It's
not intended to be used for other purposes, like data analysis.

View data in database
Use the following SQL command to view the contents of this table and show the exact
data that's sent:

  SQL

  SELECT * FROM TEL_TelemetryResults

Export the data
When the service connection point is in offline mode, use the service connection tool to
export the current data to a comma-separated values (CSV) file. Run the service
connection tool on the service connection point with the -Export parameter.

For more information, see Use the service connection tool.

One-way hashes
Some data consists of strings of random alphanumeric characters. Configuration
Manager uses the SHA-256 algorithm to create one-way hashes. This process makes
sure that Microsoft doesn't collect potentially sensitive data. The hashed data can still be
used for correlation and comparison purposes.

<!-- p.567 -->

For example, instead of collecting the names of tables in the site database, it captures
the one-way hash for each table name. This behavior makes sure that any custom table
names aren't visible. Microsoft then does the same one-way hash process of the default
SQL Server table names. Comparing the results of the two queries determines the
deviation of your database schema from the product default. This information is then
used to improve updates that require changes to the SQL Server schema.

When you view the raw data, a common hashed value appears in each row of data. This
hash is the support ID, also known as the hierarchy ID. It's used to correlate data with
the same hierarchy without identifying the customer or source.

How the one-way hash works
   1. Get your support ID from the Configuration Manager console. Select the arrow in
     the upper left corner of the ribbon, and then choose About Configuration
     Manager. You can select and copy the support ID from the window that opens.

   2. Use the following Windows PowerShell script to do the one-way hash of your
     support ID.

        PowerShell

        Param( [Parameter(Mandatory=$True)] [string]$value )
          $guid = [System.Guid]::NewGuid()
          if( [System.Guid]::TryParse($value,[ref] $guid) -eq $true ) {
          #many of the values we hash are Guids
          $bytesToHash = $guid.ToByteArray()
        } else {
          #otherwise hash as string (unicode)
          $ue = New-Object System.Text.UnicodeEncoding
          $bytesToHash = $ue.GetBytes($value)
        }
          # Load Hash Provider (https://en.wikipedia.org/wiki/SHA-2)
        $hashAlgorithm = [System.Security.Cryptography.SHA256Cng]::Create()
        # Hash the input
        $hashedBytes = $hashAlgorithm.ComputeHash($bytesToHash)
        # Base64 encode the result for transport
        $result = [Convert]::ToBase64String($hashedBytes)
        return $result

   3. Compare the script output against the GUID in the raw data. This process shows
     how the data is obscured.

Next steps

<!-- p.568 -->

Next, learn about the levels of diagnostics and usage data that Configuration Manager
collects:

  Levels of diagnostic usage data

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.569 -->

Diagnostic usage data for tools
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Some of the tools that are included with Configuration Manager collect usage data.
Microsoft uses this data to improve the quality of these tools, and better understand
customer usage. Microsoft collects data for the following Configuration Manager tools:

      Client tools
      Server tools
      Support Center
      CMTrace

For more general information about these tools, see Configuration Manager Tools.

  ７ Note

  The ConfigurationManager PowerShell module also collects usage data. For more
  information, see Configuration Manager cmdlet library privacy statement.

The following data is collected for these tools:

      Version
      Start and stop times to calculate duration of use

Because these tools can run on any Windows device, they all use the Windows
diagnostic data channel. They don't rely on Configuration Manager diagnostic data
collection. The device on which the tool runs needs to be configured for at least
Optional diagnostic data. If you configure the device for any other setting, Windows
won't collect data for these Configuration Manager tools. For more information on these
Windows diagnostic data levels, see the following articles:

      Windows 10, version 1709 and newer optional diagnostic data
      Configure Windows diagnostic data in your organization

Next, see the frequently asked questions about diagnostic and usage data for
Configuration Manager:

  Frequently asked questions

<!-- p.570 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.571 -->

Levels of diagnostic usage data
Applies to: Configuration Manager (current branch)

Configuration Manager collects three levels of diagnostics and usage data: Basic, Enhanced, and
Full. By default, this feature is set at the Enhanced level.

  ） Important

  Configuration Manager doesn't collect site codes, sites names, IP addresses, user names,
  computer names, physical addresses, or email addresses on the Basic or Enhanced levels.
  Any collection of this information on the Full level isn't purposeful. It's potentially included in
  advanced diagnostic information like log files or memory snapshots. Microsoft doesn't use
  this information to identify you, contact you, or develop advertising.

Levels
Basic
The Basic level includes data about your hierarchy. It's required to help improve your installation
or upgrade experience. This data also helps determine the Configuration Manager updates that
are applicable for your hierarchy.

Enhanced
The Enhanced level is the default after setup finishes. This level includes data that's collected in
the Basic level and feature-specific data. It shows frequency and duration of use of different
features. It also includes Configuration Manager client settings data: component name, state, and
certain settings like polling intervals. Information about software updates is basic on feature
usage, it doesn't include data about update compliance at this level.

Microsoft recommends this level because it provides the minimum data to make product and
service improvements.

Some examples of data that this level doesn't collect include:

     Names of sites, users, computer, or other objects

<!-- p.572 -->

     Details of security-related objects

     Vulnerabilities like counts of systems that require software updates

Full
The Full level includes all data in the Basic and Enhanced levels. It also includes additional
information about Endpoint Protection, update compliance percentages, and software update
information. This level can also include advanced diagnostic information like system files and
memory snapshots. This advanced data might include personal information exists in memory or
log files at the time of capture.

How to change the level
To change the data collection level, you need Modify permissions on the Site object class.

   1. In the Configuration Manager console, go to the Administration workspace, expand Site
     Configuration, and select the Sites node.

   2. Select Hierarchy Settings in the ribbon.

   3. Switch to the Diagnostic and Usage Data tab, then choose the data level.

Version-specific details
The following articles detail the specific data that Configuration Manager collects at each level
with each supported version:

     Diagnostic and usage data for 2509
     Diagnostic and usage data for 2503
     Diagnostic and usage data for 2409

With version 2509, no further version-specific changes are planned to the collection of diagnostic
usage data.

Next steps
Next, learn about the diagnostics and usage data that Configuration Manager collects for its
tools:

  Diagnostic usage data for tools

<!-- p.573 -->

Last updated on 06/04/2026

<!-- p.574 -->

Diagnostic and usage data for version 2509
ﾃ     Summarize this article for me

Applies to: Configuration Manager (current branch)

The following sections provide additional detail about data collected at each level. For more
information on the levels and how to change them, see Levels of diagnostic usage data.

Changes from previous versions are noted with [New], [Updated], [Removed], or [Moved].

    ） Important

    Configuration Manager doesn't collect IP addresses, user names, computer names,
    physical addresses, or email addresses on the Basic or Enhanced levels. Any collection of
    this information on the Full level is not purposeful. It is potentially included in advanced
    diagnostic information like log files or memory snapshots. Microsoft doesn't use this
    information to identify you, contact you, or develop advertising.

Level 1 - Basic
For Configuration Manager version 2509, this level includes the following data:

Application management (Level 1)
       Basic application and deployment type counts: total apps, total apps with multiple
       deployment types, total apps with dependencies, total superseded apps, and count of
       deployment technologies in use

       Count of Microsoft Edge installations

       Count of clients by default and preferred browser

Client (Level 1)
       Count of client languages and locales

       Count of Configuration Manager client versions, OS versions, and Office versions

       Count of Windows 10 and later devices by branch, build, and unique Active Directory
       forest

<!-- p.575 -->

   Count of clients joined to Microsoft Entra ID

   Count of extended interoperability clients

   Count of clients by Windows OS age, to the nearest three-month interval

   Top 10 processor names used on clients and servers

   Use of the bulk registration token

   Count of clients by identity source and registration method. For example, Active
   Directory, Microsoft Entra ID, or PKI client authentication certificate.

   Count of clients by OS type and version that are joined to Microsoft Entra ID or hybrid-
   joined

   Count of clients by OS and system processor type

   Statistics for the number of collections and machines with power configuration
   management settings assigned

Cloud services (Level 1)
   Count of existing and new devices that are cloud attached since the last data collection

   Count of clients by co-management enrollment method

   Error statistics for co-management enrollment

   Aggregated usage statistics of co-management: number of clients ever enrolled, number
   of enrolled clients, number of clients pending enrollment, clients receiving policy,
   workload states, pilot/exclusion collection sizes, and enrollment errors

   Count of clients piloting or using each co-management workload

   Count of Microsoft Entra applications and services connected to Configuration Manager

   Cloud attach and detach actions

   Status of last sync with Intune cloud service

   Configuration and usage statistics of cloud management gateway: counts of regions and
   environments, and authentication/authorization statistics

   Summarized count of Endpoint Analytics event

   Aggregated statistics on Desktop Analytics enrollment errors and usage

<!-- p.576 -->

   Count of clients by OS type and version that are co-managed, cloud-attached, or use a
   cloud management gateway (CMG)

Configuration Manager console (Level 1)
   Statistics about Configuration Manager console connections: OS version, language, SKU
   and architecture, system memory, logical processor count, connect site ID, installed .NET
   versions, console language packs, and capable authentication level

   Hashed list of extensions to Configuration Manager console property pages and wizards

   Configuration Manager console crash locations

   Configuration Manager console usage statistics

   Configuration Manager console notification configuration and status

Protection (Level 1)
   Basic Endpoint Protection information about antimalware client versions

   Existence of Microsoft BitLocker Administration and Monitoring (MBAM) server-side
   extensions

   BitLocker management client counts summarized by enrollment and TPM state

Setup (Level 1)
   Build, install type, language packs, features that you enabled

   Pre-release use, setup media type, branch type

   Software Assurance expiration date

   Update pack deployment status and errors, download progress, and prerequisite errors

   Use of early update ring

   Version of post-upgrade script

   Central administration site removal status

Site database (Level 1)

<!-- p.577 -->

   Basic database configuration: processors, memory size, memory settings, Configuration
   Manager database configuration, Configuration Manager database size, cluster
   configuration, configuration of distributed views, and change tracking version

   Database performance metrics: replication processing information, top SQL Server stored
   procedures by processor, and disk usage

   SQL Server version, service pack level, edition, collation ID, and character set

   Hashed list of top SQL queries by memory usage and lock count

   SQL Server Always On availability group replica information, usage, and health status

Site infrastructure (Level 1)
   Count of Microsoft Entra users and Windows users requesting in Admin Service

   Basic Configuration Manager site hierarchy data: site list, type, version, status, client
   count, time zone, and health status

   Basic discovery statistics: discovery count, minimum/maximum/average group sizes, and
   when the site is running entirely with Microsoft Entra services

   Basic site system server information: site system roles used, internet and SSL status, OS,
   processors, physical or virtual machine, and usage of site server high availability

   Configured level for diagnostics and usage data, online or offline mode, and fast update
   configuration

   Distribution point and management point types and basic configuration information:
   protected, prestaged, PXE, multicast, SSL state, pull/peer distribution points, MDM-
   enabled, and SSL-enabled

   Diagnostics and usage data statistics: when run, runtime, errors

   Hashed list of hardware inventory properties longer than 255 characters

   Count and processing rates of key Configuration Manager objects: data discovery records
   (DDR), state messages, status messages, hardware inventory, software inventory, and
   overall count of files in inboxes

   Site server disk and processor performance information

   Uptime and memory usage information for Configuration Manager site server processes

<!-- p.578 -->

     Count of crashes for Configuration Manager site server processes, and Watson signature
     ID, if available

     Hash of key site attributes (site ID, site codes, sites names, SQL Server broker ID, and site
     exchange key)

     Status and health of the administration service

     Counts of errors from administration service

     Site health information

     Site health check configuration and status

     Version of Visual Studio redistributable and .NET Framework installed on clients and site
     system servers

     Summarized hierarchy health and activity status

Miscellaneous (Level 1)
     Basic OS deployment counts of images

     Count of Windows clients that use Windows Update for Business

     Count of operating systems for managed devices and policies set by the Exchange
     Connector

     Count of phased deployments created by type

     Count of categorized and uncategorized applications for asset intelligence

     Aggregated count of upgrade readiness assessments

     Number of software updates referenced by task sequence

     Count of scripts scheduled and run statistics

     External Service Notification usage statistics

Level 2 - Enhanced
For Configuration Manager version 2509, this level includes the following data:

Application management (Level 2)

<!-- p.579 -->

App requirements: count of built-in conditions referenced by deployment technology

App supersedence, maximum depth of chain

Application approval statistics and usage frequency

Application content size statistics

Application deployment information: use of install versus uninstall, requires approval, user
interaction enabled/disabled, dependency, supersedence, and usage count of install
behavior feature

Application policy size and complexity statistics

Available application request statistics

Basic configuration information for packages and programs: deployment options and
program flags

Basic usage/targeting information for deployment types: user versus device targeted,
required versus available, and universal apps

Count of application applicability by OS

Count of applications referenced in a task sequence

Count of distinct branding for application catalog

Count of Microsoft 365 Apps applications created using dashboard

Count of packages by type

Count of package/program deployments

Count of Windows 10 and later licensed application licenses

Count of Windows Installer deployment types by uninstall content settings

Count of Microsoft Store for Business apps and sync statistics: summarized types of apps,
licensed app status, and number of online and offline licensed apps

Maintenance window type and duration

Minimum/maximum/average number of application deployments per user/device per
time period

Most common application installation error codes by deployment technology

<!-- p.580 -->

   MSI configuration options and counts

   Statistics on end-user interaction with notification for required software deployments

   Universal Data Access usage, how created

   Aggregated user device affinity statistics

   Max and average primary users per device

   Application global condition usage by type

   Software Center customization configuration, including use of settings to configure
   Software Center and notification branding

   Package Conversion Manager readiness and counts

   Count of application detection methods by type

   Count of application enforcement errors

   MSI installer properties

   Statistics of user install requests

   Aggregated statistics on the use of the email approval feature

   File count, content size, services count, and custom action count of MSIs in application
   catalog

   Count of devices by Office ProPlus readiness state

   Aggregated statistics on the use of application groups

   Aggregated statistics on Office add-ins, usage of the Office Readiness Toolkit, and counts
   of clients with Microsoft 365 Apps

   Aggregated statistics on Office add-in health

   Count and size of Office Pro Plus pilot collections

   Number of Office Pro Plus devices sending Office health data

   Count of the type of actions used on apps over time

Client (Level 2)
   Active Management Technology (AMT) client version

<!-- p.581 -->

BIOS age in years, and distribution of ages in months

Count of devices with Secure Boot enabled

Count of devices by TPM state

Client auto-upgrade: deployment configuration including client piloting and exclusion
usage (extended interoperability client)

Client deployment download errors

Client health statistics and top issue summary by client version, component, OS, and
workload

Client notification operation action status: how many times each is run, max number of
targeted clients, and average success rate

Count of client installations from each source location type

Count of client installation failures

Count of devices virtualized by Hyper-V or Azure

Count of Software Center actions

Count of UEFI-enabled devices

Deployment methods used for client and count of clients per deployment method

List/count of enabled client agents

OS age in months

Number of hardware inventory classes, software inventory rules, file collection rules, and
overall health status

Statistics for device health attestation: most common error codes, number of on-premises
servers, and counts of devices in various states

Count of devices by default browser

Count of Configuration Manager-generated server authentication certificates

Count of Microsoft Surface devices by model

Count of client health check failures by issue type

Count of status (total/approved/blocked) for client certificate types

<!-- p.582 -->

   Client counts for different user/device relationship types

   Count of clients in VPN boundaries

   Power plans with their peak and non-peak usage statistics

   Power plan peak usage statistics

   Power plan setting options usage statistics

Cloud services (Level 2)
   Microsoft Entra discovery statistics

   Count of collections synced to Azure Log Analytics

   Count of Upgrade Analytics Connectors

   Whether the Azure Log Analytics cloud connector is enabled

   Count of pull-distribution points with a cloud distribution point as a source location

   Usage of the cloud services onboarding wizard

   Cloud services configuration onboarding properties

   Cloud services endpoint connectivity and component health

   Usage of the cloud-attach wizard

   Cloud Distribution Point usage statistics

CMPivot (Level 2)
   CMPivot usage statistics

   Count of saved CMPivot queries

   Count of queries by entity type

Co-management (Level 2)
   Enrollment schedule and historical statistics

   Count of clients eligible for co-management

   Associated Microsoft Intune tenant

<!-- p.583 -->

Collections (Level 2)
   Collection ID usage (not running out of IDs)

   Collection evaluation statistics: query time, assigned versus unassigned counts, counts by
   type, ID rollover, and rule usage

   Collections without a deployment

   Count of collections synchronized to Microsoft Entra ID, including type and size

   Statistics for collection member counts and collection rule counts

   Statistics about the collection rule WMI class query dependencies

Compliance settings (Level 2)
   Basic configuration baseline information: count, number of deployments, number of
   references, and frequency of changes

   Compliance policy error statistics

   Count of configuration items by type

   Count of deployments that reference built-in settings, including remediate setting

   Count of rules and deployments created for custom settings, including remediate setting

   Count of deployed Simple Certificate Enrollment Protocol (SCEP), VPN, Wi-Fi, certificate
   (.pfx), and compliance policy templates

   Count of SCEP certificate, VPN, Wi-Fi, certificate (.pfx), and compliance policy
   deployments by platform

   Windows Hello for Business policy (created, deployed)

   Count of deployed Microsoft Edge Legacy browser policies

   Count of OneDrive policies (created, deployed)

   Count of compliance settings deployed by category, OS, and source (cloud vs on-
   premises)

   Company resource access profile settings usage

Configuration Manager console (Level 2)

<!-- p.584 -->

   Counts of active and viewed console notification messages by type

   Count of folders by object type

   Console performance information

   25 most common actions, wizards, property sheets, and tree nodes accessed in the
   console

   List of installed console extensions, and whether they're enabled, required, or approved

   Summary of size and count of admin persisted settings

   Selected console usage information

   Unsigned extension policy

   Console dark mode usage

Content (Level 2)
   Boundary group statistics: how many fast, how many slow, count per group, and fallback
   relationships

   Boundary group information: count of boundaries and site systems that are assigned to
   each boundary group

   Boundary group relationships and fallback configuration

   Client content download statistics

   Count of boundaries by type

   Count of peer cache clients, usage statistic, and partial download statistics

   Distribution Manager configuration information: threads, retry delay, number of retries,
   and pull distribution point settings

   Distribution point configuration information: use of branch cache and distribution point
   monitoring

   Distribution point group information: count of packages and distribution points that are
   assigned to each distribution point group

   Content library type, whether local or remote

   Count of boundary groups by configuration

<!-- p.585 -->

   Count of subnets excluded from peer cache

   Count and type of operations on the SMSDPProvider service for distribution points

Protection (Level 2)
   Microsoft Defender for Endpoint policies (formerly known as Windows Defender for
   Endpoint): count of policies, and whether policies are deployed.

   Count of alerts that are configured for Endpoint Protection feature

   Count of collections that are selected to appear in Endpoint Protection dashboard

   Count of Windows Defender Exploit Guard policies, deployments, and targeted clients

   Endpoint Protection deployment errors, count of Endpoint Protection policy deployment
   error codes

   Endpoint Protection antimalware and Windows Firewall policy usage (number of unique
   policies assigned to group). This data doesn't include any information about the settings
   included in the policy.

   Aggregated statistics for Microsoft Defender for Endpoint policies

   Count of Microsoft Defender Application Guard policies, deployments, and targeted
   clients

   Count of Microsoft Defender Application Control policies, deployments, and targeted
   clients

Migration (Level 2)
   Count of migrated objects (use of migration wizard)

Mobile device management (MDM) (Level 2)
   Count of issued mobile device actions: lock, pin rest, wipe, retire, and sync now
   commands

   Count of mobile device policies

   Count of mobile devices Configuration Manager manages, and how you enrolled them
   (bulk, user-based)

   Count of users who have multiple enrolled mobile devices

<!-- p.586 -->

   Mobile device polling schedule and statistics for mobile device check-in duration

On-premises mobile device management (MDM) (Level 2)
   Count of Windows bulk enrollment packages and profiles

   Deployment success/failure statistics for on-premises MDM application deployments

OS deployment (Level 2)
   Count of boot images, drivers, driver packages, multicast-enabled distribution points,
   PXE-enabled distribution points, and task sequences

   Count of boot images by Configuration Manager client version

   Count of boot images by Windows PE version

   Count of edition upgrade policies

   Count of hardware identifiers excluded from PXE

   Count of OS deployment by OS version

   Count of OS upgrades over time

   Count of task sequence deployments using option to pre-download content

   Counts of task sequence step usage

   Version of Windows ADK installed

   Count of image servicing tasks

   Count of imported machines

   Count of duplicate hardware identifiers (MAC address and SMBIOS GUID) excluded from
   PXE and client registration

   Count of task sequences by type (OS deployment or generic task sequence)

   Count of packages with pre-cache content settings

   Grouped sizes of task sequence policies

   Count of error codes from feature upgrades for Windows clients

   Count of supported and unsupported OS versions

<!-- p.587 -->

   Count of task sequences and legacy packages with custom icons

Site updates (Level 2)
   Versions of installed Configuration Manager hotfixes

Software updates (Level 2)
   Available and deadline deltas that are used in automatic deployment rules

   Average and maximum number of assignments per update

   Client update evaluation and scan schedules

   Classifications synced by the software update point

   Cluster patching statistics

   Configuration of Windows express updates

   Configurations that are used for active Windows servicing plans

   Count of deployed Microsoft 365 Apps updates

   Count of Microsoft Surface drivers synced

   Count of update groups and assignments

   Count of update packages and the maximum/minimum/average number of distribution
   points that are targeted with packages

   Count of updates that are created and deployed with System Center Update Publisher

   Count of Windows Update for Business policies created and deployed

   Aggregated statistics of Windows Update for Business configurations

   Number of automatic deployment rules that are tied to synchronization

   Number of automatic deployment rules that create new or add updates to an existing
   group

   Number of automatic deployment rules that have multiple deployments

   Number of update groups and minimum/maximum/average number of updates per
   group

<!-- p.588 -->

   Number of updates and percentage of updates that are deployed, expired, superseded,
   downloaded, and contain EULAs

   Software update point load-balancing statistics

   Software update point synchronization schedule

   Total/average number of collections that have software update deployments and the
   maximum/average number of deployed updates

   Update scan error codes and machine count

   Windows servicing dashboard content versions

   Count of third-party software update catalog subscriptions and usage

   Count of software updates deployed with and without content

   Aggregated statistics on the number of UUP updates that are required, deployed, expired,
   superseded, and downloaded

   Use of UUP product categories

   Count of clients that have deployed at least one UUP quality update or UUP feature
   update

   Top UUP error codes and count of affected devices

   List of subscriptions to third-party software update catalogs

   Use of WSUS maintenance settings

   Orchestration group usage

   Windows Update fallback configuration settings

   Type, size, and timeout settings of orchestration group scripts

   Software Update Point setting options statistics

SQL/performance data (Level 2)
   Configuration and duration of site summarization

   Count of largest database tables

   Discovery operational statistics (count of objects found)

<!-- p.589 -->

   Discovery types, enabled, and schedule (full, incremental)

   SQL Server change tracking performance issues, retention period, and autocleanup state

   SQL Server change tracking retention period

   State and status message performance statistics including most common and most
   expensive message types

   Management point traffic statistics (total bytes sent and received by endpoint)

   Management point performance counter measurements

   Aggregated performance statistics of calls made to Software Center endpoints on the
   management point

   SQL Server maintenance task configuration and status

   Status of recent re-initialization requests

Miscellaneous (Level 2)
   Configuration of data warehouse service point including synchronization schedule,
   average time, and use of customized tables feature

   Count of scripts and run/edit statistics

   Count of sites with Wake On LAN (WOL)

   Reporting usage and performance statistics

   Phased deployment usage statistics

   Management insights item counts and progress

   Count of crashes for unique non-Configuration Manager processes on the site server, and
   Watson signature ID, if available

   Aggregated system boot time statistics by OS, form-factor, and drive type

   Usage of the Azure migration tool

   Count of clients with browser usage

   Summary of how many site systems have the proxy enabled and how many are
   authenticated proxy, including configuration, usage patterns, and traffic patterns

   Usage information for the last seven days of in-console product feedback

<!-- p.590 -->

     Count of site-to-site accounts by type

     Usage statistics for user and device custom properties

     Count and type of edits to asset intelligence categories

Level 3 - Full
For Configuration Manager version 2509, this level includes the following data:

     Automatic deployment rule evaluation schedule information

     ATP health summary

     Collection evaluation and refresh statistics

     Compliance policy statistics on compliance and errors

     Compliance settings: SCEP, VPN, Wi-Fi, and compliance policy template configuration
     details

     DCM config pack for Configuration Manager usage

     Detailed client deployment installation errors

     Endpoint Protection health summary: including count of protected, at risk, unknown, and
     unsupported clients

     Endpoint Protection policy configuration

     List of processes configured with installation behavior for applications

     Minimum/maximum/average number of hours since last software update scan

     Minimum/maximum/average number of inactive clients in software update deployment
     collections

     Minimum/maximum/average number of software updates per package

     MSI product code deployment statistics

     Overall compliance of software update deployments

     Count of groups that contain expired software updates

     Software update deployment error codes and counts

<!-- p.591 -->

     Software update deployment information: percentage of deployments that are targeted
     with client versus UTC time, required versus optional versus silent, and reboot
     suppression

     Software update products synced by software update point

     Software update scan success percentages

     Top 50 CPUs in the environment

     Type of Exchange Active Sync (EAS) Conditional Access policies (block or quarantine) for
     devices that Microsoft Intune manages

     Microsoft Store for Business application details: non-aggregate list of synced applications
     including AppID, online state or offline state, and total purchased license counts

     Count of clients pushed with option to not allow fallback to NTLM

     List of Configuration Manager console extensions

Last updated on 02/26/2026

<!-- p.592 -->

Diagnostic and usage data for version
2503
Article • 03/31/2025

Applies to: Configuration Manager (current branch)

The following sections provide additional detail about data collected at each level. For
more information on the levels and how to change them, see Levels of diagnostic usage
data.

Changes from previous versions are noted with [New], [Updated], [Removed], or
[Moved].

  ） Important

  Configuration Manager doesn't collect IP addresses, user names, computer names,
  physical addresses, or email addresses on the Basic or Enhanced levels. Any
  collection of this information on the Full level is not purposeful. It is potentially
  included in advanced diagnostic information like log files or memory snapshots.
  Microsoft doesn't use this information to identify you, contact you, or develop
  advertising.

Level 1 - Basic
For Configuration Manager version 2503, this level includes the following data:

Application management (Level 1)
        Basic application and deployment type counts: total apps, total apps with multiple
        deployment types, total apps with dependencies, total superseded apps, and count
        of deployment technologies in use

        Count of Microsoft Edge installations

        Count of clients by default and preferred browser

Client (Level 1)
        Count of client languages and locales

<!-- p.593 -->

   Count of Configuration Manager client versions, OS versions, and Office versions

   Count of Windows 10 and later devices by branch, build, and unique Active
   Directory forest

   Count of clients joined to Microsoft Entra ID

   Count of extended interoperability clients

   Count of clients by Windows OS age, to the nearest three-month interval

   Top 10 processor names used on clients and servers

   Use of the bulk registration token

   Count of clients by identity source and registration method. For example, Active
   Directory, Microsoft Entra ID, or PKI client authentication certificate.

   Count of clients by OS type and version that are joined to Microsoft Entra ID or
   hybrid-joined

   Count of clients by OS and system processor type

   Statistics for the number of collections and machines with power configuration
   management settings assigned

Cloud services (Level 1)
   Count of existing and new devices that are cloud attached since the last data
   collection

   Count of clients by co-management enrollment method

   Error statistics for co-management enrollment

   Aggregated usage statistics of co-management: number of clients ever enrolled,
   number of enrolled clients, number of clients pending enrollment, clients receiving
   policy, workload states, pilot/exclusion collection sizes, and enrollment errors

   Count of clients piloting or using each co-management workload

   Count of Microsoft Entra applications and services connected to Configuration
   Manager

   Cloud attach and detach actions

   Status of last sync with Intune cloud service

<!-- p.594 -->

   Configuration and usage statistics of cloud management gateway: counts of
   regions and environments, and authentication/authorization statistics

   Summarized count of Endpoint Analytics event

   Aggregated statistics on Desktop Analytics enrollment errors and usage

   Count of clients by OS type and version that are co-managed, cloud-attached, or
   use a cloud management gateway (CMG)

Configuration Manager console (Level 1)
   Statistics about Configuration Manager console connections: OS version, language,
   SKU and architecture, system memory, logical processor count, connect site ID,
   installed .NET versions, console language packs, and capable authentication level

   Hashed list of extensions to Configuration Manager console property pages and
   wizards

   Configuration Manager console crash locations

   Configuration Manager console usage statistics

   Configuration Manager console notification configuration and status

Protection (Level 1)
   Basic Endpoint Protection information about antimalware client versions

   Existence of Microsoft BitLocker Administration and Monitoring (MBAM) server-
   side extensions

   BitLocker management client counts summarized by enrollment and TPM state

Setup (Level 1)
   Build, install type, language packs, features that you enabled

   Pre-release use, setup media type, branch type

   Software Assurance expiration date

   Update pack deployment status and errors, download progress, and prerequisite
   errors

<!-- p.595 -->

   Use of early update ring

   Version of post-upgrade script

   Central administration site removal status

Site database (Level 1)
   Basic database configuration: processors, memory size, memory settings,
   Configuration Manager database configuration, Configuration Manager database
   size, cluster configuration, configuration of distributed views, and change tracking
   version

   Database performance metrics: replication processing information, top SQL Server
   stored procedures by processor, and disk usage

   SQL Server version, service pack level, edition, collation ID, and character set

   Hashed list of top SQL queries by memory usage and lock count

   SQL Server Always On availability group replica information, usage, and health
   status

Site infrastructure (Level 1)
   Count of Microsoft Entra users and Windows users requesting in Admin Service

   Basic Configuration Manager site hierarchy data: site list, type, version, status,
   client count, time zone, and health status

   Basic discovery statistics: discovery count, minimum/maximum/average group
   sizes, and when the site is running entirely with Microsoft Entra services

   Basic site system server information: site system roles used, internet and SSL status,
   OS, processors, physical or virtual machine, and usage of site server high
   availability

   Configured level for diagnostics and usage data, online or offline mode, and fast
   update configuration

   Distribution point and management point types and basic configuration
   information: protected, prestaged, PXE, multicast, SSL state, pull/peer distribution
   points, MDM-enabled, and SSL-enabled

   Diagnostics and usage data statistics: when run, runtime, errors

<!-- p.596 -->

   Hashed list of hardware inventory properties longer than 255 characters

   Count and processing rates of key Configuration Manager objects: data discovery
   records (DDR), state messages, status messages, hardware inventory, software
   inventory, and overall count of files in inboxes

   Site server disk and processor performance information

   Uptime and memory usage information for Configuration Manager site server
   processes

   Count of crashes for Configuration Manager site server processes, and Watson
   signature ID, if available

   Hash of key site attributes (site ID, site codes, sites names, SQL Server broker ID,
   and site exchange key)

   Status and health of the administration service

   Counts of errors from administration service

   Site health information

   Site health check configuration and status

   Version of Visual Studio redistributable and .NET Framework installed on clients
   and site system servers

   Summarized hierarchy health and activity status

Miscellaneous (Level 1)
   Basic OS deployment counts of images

   Count of Windows clients that use Windows Update for Business

   Count of operating systems for managed devices and policies set by the Exchange
   Connector

   Count of phased deployments created by type

   Count of categorized and uncategorized applications for asset intelligence

   Aggregated count of upgrade readiness assessments

   Number of software updates referenced by task sequence

<!-- p.597 -->

     Count of scripts scheduled and run statistics

     External Service Notification usage statistics

Level 2 - Enhanced
For Configuration Manager version 2503, this level includes the following data:

Application management (Level 2)
     App requirements: count of built-in conditions referenced by deployment
     technology

     App supersedence, maximum depth of chain

     Application approval statistics and usage frequency

     Application content size statistics

     Application deployment information: use of install versus uninstall, requires
     approval, user interaction enabled/disabled, dependency, supersedence, and usage
     count of install behavior feature

     Application policy size and complexity statistics

     Available application request statistics

     Basic configuration information for packages and programs: deployment options
     and program flags

     Basic usage/targeting information for deployment types: user versus device
     targeted, required versus available, and universal apps

     Count of application applicability by OS

     Count of applications referenced in a task sequence

     Count of distinct branding for application catalog

     Count of Microsoft 365 Apps applications created using dashboard

     Count of packages by type

     Count of package/program deployments

     Count of Windows 10 and later licensed application licenses

<!-- p.598 -->

Count of Windows Installer deployment types by uninstall content settings

Count of Microsoft Store for Business apps and sync statistics: summarized types
of apps, licensed app status, and number of online and offline licensed apps

Maintenance window type and duration

Minimum/maximum/average number of application deployments per user/device
per time period

Most common application installation error codes by deployment technology

MSI configuration options and counts

Statistics on end-user interaction with notification for required software
deployments

Universal Data Access usage, how created

Aggregated user device affinity statistics

Max and average primary users per device

Application global condition usage by type

Software Center customization configuration, including use of settings to configure
Software Center and notification branding

Package Conversion Manager readiness and counts

Count of application detection methods by type

Count of application enforcement errors

MSI installer properties

Statistics of user install requests

Aggregated statistics on the use of the email approval feature

File count, content size, services count, and custom action count of MSIs in
application catalog

Count of devices by Office ProPlus readiness state

Aggregated statistics on the use of application groups

<!-- p.599 -->

   Aggregated statistics on Office add-ins, usage of the Office Readiness Toolkit, and
   counts of clients with Microsoft 365 Apps

   Aggregated statistics on Office add-in health

   Count and size of Office Pro Plus pilot collections

   Number of Office Pro Plus devices sending Office health data

   Count of the type of actions used on apps over time

Client (Level 2)
   Active Management Technology (AMT) client version

   BIOS age in years, and distribution of ages in months

   Count of devices with Secure Boot enabled

   Count of devices by TPM state

   Client auto-upgrade: deployment configuration including client piloting and
   exclusion usage (extended interoperability client)

   Client deployment download errors

   Client health statistics and top issue summary by client version, component, OS,
   and workload

   Client notification operation action status: how many times each is run, max
   number of targeted clients, and average success rate

   Count of client installations from each source location type

   Count of client installation failures

   Count of devices virtualized by Hyper-V or Azure

   Count of Software Center actions

   Count of UEFI-enabled devices

   Deployment methods used for client and count of clients per deployment method

   List/count of enabled client agents

   OS age in months

<!-- p.600 -->

   Number of hardware inventory classes, software inventory rules, file collection
   rules, and overall health status

   Statistics for device health attestation: most common error codes, number of on-
   premises servers, and counts of devices in various states

   Count of devices by default browser

   Count of Configuration Manager-generated server authentication certificates

   Count of Microsoft Surface devices by model

   Count of client health check failures by issue type

   Count of status (total/approved/blocked) for client certificate types

   Client counts for different user/device relationship types

   Count of clients in VPN boundaries

   Power plans with their peak and non-peak usage statistics

   Power plan peak usage statistics

   Power plan setting options usage statistics

Cloud services (Level 2)
   Microsoft Entra discovery statistics

   Count of collections synced to Azure Log Analytics

   Count of Upgrade Analytics Connectors

   Whether the Azure Log Analytics cloud connector is enabled

   Count of pull-distribution points with a cloud distribution point as a source
   location

   Usage of the cloud services onboarding wizard

   Cloud services configuration onboarding properties

   Cloud services endpoint connectivity and component health

   Usage of the cloud-attach wizard

   Cloud Distribution Point usage statistics
