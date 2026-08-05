---
title: "Core infrastructure documentation — pages 601-640"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0601-0640
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0601-0640
family: sccm
documentKind: "doc"
abstract: "CMPivot (Level 2) CMPivot usage statistics Count of saved CMPivot queries Count of queries by entity type Co-management (Level 2) Enrollment schedule and historical statistics Count of clients eligible for co-management Associated Microsoft Intune tenant Collections (Level 2) Co"
---

# Core infrastructure documentation — pages 601-640

<!-- p.601 -->

CMPivot (Level 2)
   CMPivot usage statistics

   Count of saved CMPivot queries

   Count of queries by entity type

Co-management (Level 2)
   Enrollment schedule and historical statistics

   Count of clients eligible for co-management

   Associated Microsoft Intune tenant

Collections (Level 2)
   Collection ID usage (not running out of IDs)

   Collection evaluation statistics: query time, assigned versus unassigned counts,
   counts by type, ID rollover, and rule usage

   Collections without a deployment

   Count of collections synchronized to Microsoft Entra ID, including type and size

   Statistics for collection member counts and collection rule counts

   Statistics about the collection rule WMI class query dependencies

Compliance settings (Level 2)
   Basic configuration baseline information: count, number of deployments, number
   of references, and frequency of changes

   Compliance policy error statistics

   Count of configuration items by type

   Count of deployments that reference built-in settings, including remediate setting

   Count of rules and deployments created for custom settings, including remediate
   setting

<!-- p.602 -->

   Count of deployed Simple Certificate Enrollment Protocol (SCEP), VPN, Wi-Fi,
   certificate (.pfx), and compliance policy templates

   Count of SCEP certificate, VPN, Wi-Fi, certificate (.pfx), and compliance policy
   deployments by platform

   Windows Hello for Business policy (created, deployed)

   Count of deployed Microsoft Edge Legacy browser policies

   Count of OneDrive policies (created, deployed)

   Count of compliance settings deployed by category, OS, and source (cloud vs on-
   premises)

   Company resource access profile settings usage

Configuration Manager console (Level 2)
   Counts of active and viewed console notification messages by type

   Count of folders by object type

   Console performance information

   25 most common actions, wizards, property sheets, and tree nodes accessed in the
   console

   List of installed console extensions, and whether they're enabled, required, or
   approved

   Summary of size and count of admin persisted settings

   Selected console usage information

   Unsigned extension policy

   Console dark mode usage

Content (Level 2)
   Boundary group statistics: how many fast, how many slow, count per group, and
   fallback relationships

   Boundary group information: count of boundaries and site systems that are
   assigned to each boundary group

<!-- p.603 -->

   Boundary group relationships and fallback configuration

   Client content download statistics

   Count of boundaries by type

   Count of peer cache clients, usage statistic, and partial download statistics

   Distribution Manager configuration information: threads, retry delay, number of
   retries, and pull distribution point settings

   Distribution point configuration information: use of branch cache and distribution
   point monitoring

   Distribution point group information: count of packages and distribution points
   that are assigned to each distribution point group

   Content library type, whether local or remote

   Count of boundary groups by configuration

   Count of subnets excluded from peer cache

   Count and type of operations on the SMSDPProvider service for distribution points

Protection (Level 2)
   Microsoft Defender for Endpoint policies (formerly known as Windows Defender
   for Endpoint): count of policies, and whether policies are deployed.

   Count of alerts that are configured for Endpoint Protection feature

   Count of collections that are selected to appear in Endpoint Protection dashboard

   Count of Windows Defender Exploit Guard policies, deployments, and targeted
   clients

   Endpoint Protection deployment errors, count of Endpoint Protection policy
   deployment error codes

   Endpoint Protection antimalware and Windows Firewall policy usage (number of
   unique policies assigned to group). This data doesn't include any information
   about the settings included in the policy.

   Aggregated statistics for Microsoft Defender for Endpoint policies

<!-- p.604 -->

   Count of Microsoft Defender Application Guard policies, deployments, and
   targeted clients

   Count of Microsoft Defender Application Control policies, deployments, and
   targeted clients

Migration (Level 2)
   Count of migrated objects (use of migration wizard)

Mobile device management (MDM) (Level 2)
   Count of issued mobile device actions: lock, pin rest, wipe, retire, and sync now
   commands

   Count of mobile device policies

   Count of mobile devices Configuration Manager manages, and how you enrolled
   them (bulk, user-based)

   Count of users who have multiple enrolled mobile devices

   Mobile device polling schedule and statistics for mobile device check-in duration

On-premises mobile device management (MDM) (Level 2)
   Count of Windows bulk enrollment packages and profiles

   Deployment success/failure statistics for on-premises MDM application
   deployments

OS deployment (Level 2)
   Count of boot images, drivers, driver packages, multicast-enabled distribution
   points, PXE-enabled distribution points, and task sequences

   Count of boot images by Configuration Manager client version

   Count of boot images by Windows PE version

   Count of edition upgrade policies

   Count of hardware identifiers excluded from PXE

<!-- p.605 -->

   Count of OS deployment by OS version

   Count of OS upgrades over time

   Count of task sequence deployments using option to pre-download content

   Counts of task sequence step usage

   Version of Windows ADK installed

   Count of image servicing tasks

   Count of imported machines

   Count of duplicate hardware identifiers (MAC address and SMBIOS GUID) excluded
   from PXE and client registration

   Count of task sequences by type (OS deployment or generic task sequence)

   Count of packages with pre-cache content settings

   Grouped sizes of task sequence policies

   Count of error codes from feature upgrades for Windows clients

   Count of supported and unsupported OS versions

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

<!-- p.606 -->

Configurations that are used for active Windows servicing plans

Count of deployed Microsoft 365 Apps updates

Count of Microsoft Surface drivers synced

Count of update groups and assignments

Count of update packages and the maximum/minimum/average number of
distribution points that are targeted with packages

Count of updates that are created and deployed with System Center Update
Publisher

Count of Windows Update for Business policies created and deployed

Aggregated statistics of Windows Update for Business configurations

Number of automatic deployment rules that are tied to synchronization

Number of automatic deployment rules that create new or add updates to an
existing group

Number of automatic deployment rules that have multiple deployments

Number of update groups and minimum/maximum/average number of updates
per group

Number of updates and percentage of updates that are deployed, expired,
superseded, downloaded, and contain EULAs

Software update point load-balancing statistics

Software update point synchronization schedule

Total/average number of collections that have software update deployments and
the maximum/average number of deployed updates

Update scan error codes and machine count

Windows servicing dashboard content versions

Count of third-party software update catalog subscriptions and usage

Count of software updates deployed with and without content

Aggregated statistics on the number of UUP updates that are required, deployed,
expired, superseded, and downloaded

<!-- p.607 -->

   Use of UUP product categories

   Count of clients that have deployed at least one UUP quality update or UUP
   feature update

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

   Discovery types, enabled, and schedule (full, incremental)

   SQL Server change tracking performance issues, retention period, and autocleanup
   state

   SQL Server change tracking retention period

   State and status message performance statistics including most common and most
   expensive message types

   Management point traffic statistics (total bytes sent and received by endpoint)

   Management point performance counter measurements

   Aggregated performance statistics of calls made to Software Center endpoints on
   the management point

   SQL Server maintenance task configuration and status

   Status of recent re-initialization requests

<!-- p.608 -->

Miscellaneous (Level 2)
     Configuration of data warehouse service point including synchronization schedule,
     average time, and use of customized tables feature

     Count of scripts and run/edit statistics

     Count of sites with Wake On LAN (WOL)

     Reporting usage and performance statistics

     Phased deployment usage statistics

     Management insights item counts and progress

     Count of crashes for unique non-Configuration Manager processes on the site
     server, and Watson signature ID, if available

     Aggregated system boot time statistics by OS, form-factor, and drive type

     Usage of the Azure migration tool

     Count of clients with browser usage

     Summary of how many site systems have the proxy enabled and how many are
     authenticated proxy, including configuration, usage patterns, and traffic patterns

     Usage information for the last seven days of in-console product feedback

     Count of site-to-site accounts by type

     Usage statistics for user and device custom properties

     Count and type of edits to asset intelligence categories

Level 3 - Full
For Configuration Manager version 2503, this level includes the following data:

     Automatic deployment rule evaluation schedule information

     ATP health summary

     Collection evaluation and refresh statistics

     Compliance policy statistics on compliance and errors

<!-- p.609 -->

Compliance settings: SCEP, VPN, Wi-Fi, and compliance policy template
configuration details

DCM config pack for Configuration Manager usage

Detailed client deployment installation errors

Endpoint Protection health summary: including count of protected, at risk,
unknown, and unsupported clients

Endpoint Protection policy configuration

List of processes configured with installation behavior for applications

Minimum/maximum/average number of hours since last software update scan

Minimum/maximum/average number of inactive clients in software update
deployment collections

Minimum/maximum/average number of software updates per package

MSI product code deployment statistics

Overall compliance of software update deployments

Count of groups that contain expired software updates

Software update deployment error codes and counts

Software update deployment information: percentage of deployments that are
targeted with client versus UTC time, required versus optional versus silent, and
reboot suppression

Software update products synced by software update point

Software update scan success percentages

Top 50 CPUs in the environment

Type of Exchange Active Sync (EAS) Conditional Access policies (block or
quarantine) for devices that Microsoft Intune manages

Microsoft Store for Business application details: non-aggregate list of synced
applications including AppID, online state or offline state, and total purchased
license counts

Count of clients pushed with option to not allow fallback to NTLM

<!-- p.610 -->

     List of Configuration Manager console extensions

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.611 -->

Diagnostic and usage data for version
2409
Article • 12/04/2024

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
For Configuration Manager version 2409, this level includes the following data:

Application management (Level 1)
        Basic application and deployment type counts: total apps, total apps with multiple
        deployment types, total apps with dependencies, total superseded apps, and count
        of deployment technologies in use

        Count of Microsoft Edge installations

        Count of clients by default and preferred browser

Client (Level 1)
        Count of client languages and locales

<!-- p.612 -->

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

<!-- p.613 -->

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

<!-- p.614 -->

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

<!-- p.615 -->

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

<!-- p.616 -->

     Count of scripts scheduled and run statistics

     External Service Notification usage statistics

Level 2 - Enhanced
For Configuration Manager version 2409, this level includes the following data:

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

<!-- p.617 -->

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

<!-- p.618 -->

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

<!-- p.619 -->

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

<!-- p.620 -->

CMPivot (Level 2)
   CMPivot usage statistics

   Count of saved CMPivot queries

   Count of queries by entity type

Co-management (Level 2)
   Enrollment schedule and historical statistics

   Count of clients eligible for co-management

   Associated Microsoft Intune tenant

Collections (Level 2)
   Collection ID usage (not running out of IDs)

   Collection evaluation statistics: query time, assigned versus unassigned counts,
   counts by type, ID rollover, and rule usage

   Collections without a deployment

   Count of collections synchronized to Microsoft Entra ID, including type and size

   Statistics for collection member counts and collection rule counts

   Statistics about the collection rule WMI class query dependencies

Compliance settings (Level 2)
   Basic configuration baseline information: count, number of deployments, number
   of references, and frequency of changes

   Compliance policy error statistics

   Count of configuration items by type

   Count of deployments that reference built-in settings, including remediate setting

   Count of rules and deployments created for custom settings, including remediate
   setting

<!-- p.621 -->

   Count of deployed Simple Certificate Enrollment Protocol (SCEP), VPN, Wi-Fi,
   certificate (.pfx), and compliance policy templates

   Count of SCEP certificate, VPN, Wi-Fi, certificate (.pfx), and compliance policy
   deployments by platform

   Windows Hello for Business policy (created, deployed)

   Count of deployed Microsoft Edge Legacy browser policies

   Count of OneDrive policies (created, deployed)

   Count of compliance settings deployed by category, OS, and source (cloud vs on-
   premises)

   Company resource access profile settings usage

Configuration Manager console (Level 2)
   Counts of active and viewed console notification messages by type

   Count of folders by object type

   Console performance information

   25 most common actions, wizards, property sheets, and tree nodes accessed in the
   console

   List of installed console extensions, and whether they're enabled, required, or
   approved

   Summary of size and count of admin persisted settings

   Selected console usage information

   Unsigned extension policy

   Console dark mode usage

Content (Level 2)
   Boundary group statistics: how many fast, how many slow, count per group, and
   fallback relationships

   Boundary group information: count of boundaries and site systems that are
   assigned to each boundary group

<!-- p.622 -->

   Boundary group relationships and fallback configuration

   Client content download statistics

   Count of boundaries by type

   Count of peer cache clients, usage statistic, and partial download statistics

   Distribution Manager configuration information: threads, retry delay, number of
   retries, and pull distribution point settings

   Distribution point configuration information: use of branch cache and distribution
   point monitoring

   Distribution point group information: count of packages and distribution points
   that are assigned to each distribution point group

   Content library type, whether local or remote

   Count of boundary groups by configuration

   Count of subnets excluded from peer cache

   Count and type of operations on the SMSDPProvider service for distribution points

Protection (Level 2)
   Microsoft Defender for Endpoint policies (formerly known as Windows Defender
   for Endpoint): count of policies, and whether policies are deployed.

   Count of alerts that are configured for Endpoint Protection feature

   Count of collections that are selected to appear in Endpoint Protection dashboard

   Count of Windows Defender Exploit Guard policies, deployments, and targeted
   clients

   Endpoint Protection deployment errors, count of Endpoint Protection policy
   deployment error codes

   Endpoint Protection antimalware and Windows Firewall policy usage (number of
   unique policies assigned to group). This data doesn't include any information
   about the settings included in the policy.

   Aggregated statistics for Microsoft Defender for Endpoint policies

<!-- p.623 -->

   Count of Microsoft Defender Application Guard policies, deployments, and
   targeted clients

   Count of Microsoft Defender Application Control policies, deployments, and
   targeted clients

Migration (Level 2)
   Count of migrated objects (use of migration wizard)

Mobile device management (MDM) (Level 2)
   Count of issued mobile device actions: lock, pin rest, wipe, retire, and sync now
   commands

   Count of mobile device policies

   Count of mobile devices Configuration Manager manages, and how you enrolled
   them (bulk, user-based)

   Count of users who have multiple enrolled mobile devices

   Mobile device polling schedule and statistics for mobile device check-in duration

On-premises mobile device management (MDM) (Level 2)
   Count of Windows bulk enrollment packages and profiles

   Deployment success/failure statistics for on-premises MDM application
   deployments

OS deployment (Level 2)
   Count of boot images, drivers, driver packages, multicast-enabled distribution
   points, PXE-enabled distribution points, and task sequences

   Count of boot images by Configuration Manager client version

   Count of boot images by Windows PE version

   Count of edition upgrade policies

   Count of hardware identifiers excluded from PXE

<!-- p.624 -->

   Count of OS deployment by OS version

   Count of OS upgrades over time

   Count of task sequence deployments using option to pre-download content

   Counts of task sequence step usage

   Version of Windows ADK installed

   Count of image servicing tasks

   Count of imported machines

   Count of duplicate hardware identifiers (MAC address and SMBIOS GUID) excluded
   from PXE and client registration

   Count of task sequences by type (OS deployment or generic task sequence)

   Count of packages with pre-cache content settings

   Grouped sizes of task sequence policies

   Count of error codes from feature upgrades for Windows clients

   Count of supported and unsupported OS versions

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

<!-- p.625 -->

Configurations that are used for active Windows servicing plans

Count of deployed Microsoft 365 Apps updates

Count of Microsoft Surface drivers synced

Count of update groups and assignments

Count of update packages and the maximum/minimum/average number of
distribution points that are targeted with packages

Count of updates that are created and deployed with System Center Update
Publisher

Count of Windows Update for Business policies created and deployed

Aggregated statistics of Windows Update for Business configurations

Number of automatic deployment rules that are tied to synchronization

Number of automatic deployment rules that create new or add updates to an
existing group

Number of automatic deployment rules that have multiple deployments

Number of update groups and minimum/maximum/average number of updates
per group

Number of updates and percentage of updates that are deployed, expired,
superseded, downloaded, and contain EULAs

Software update point load-balancing statistics

Software update point synchronization schedule

Total/average number of collections that have software update deployments and
the maximum/average number of deployed updates

Update scan error codes and machine count

Windows servicing dashboard content versions

Count of third-party software update catalog subscriptions and usage

Count of software updates deployed with and without content

Aggregated statistics on the number of UUP updates that are required, deployed,
expired, superseded, and downloaded

<!-- p.626 -->

   Use of UUP product categories

   Count of clients that have deployed at least one UUP quality update or UUP
   feature update

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

   Discovery types, enabled, and schedule (full, incremental)

   SQL Server change tracking performance issues, retention period, and autocleanup
   state

   SQL Server change tracking retention period

   State and status message performance statistics including most common and most
   expensive message types

   Management point traffic statistics (total bytes sent and received by endpoint)

   Management point performance counter measurements

   Aggregated performance statistics of calls made to Software Center endpoints on
   the management point

   SQL Server maintenance task configuration and status

   Status of recent re-initialization requests

<!-- p.627 -->

Miscellaneous (Level 2)
     Configuration of data warehouse service point including synchronization schedule,
     average time, and use of customized tables feature

     Count of scripts and run/edit statistics

     Count of sites with Wake On LAN (WOL)

     Reporting usage and performance statistics

     Phased deployment usage statistics

     Management insights item counts and progress

     Count of crashes for unique non-Configuration Manager processes on the site
     server, and Watson signature ID, if available

     Aggregated system boot time statistics by OS, form-factor, and drive type

     Usage of the Azure migration tool

     Count of clients with browser usage

     Summary of how many site systems have the proxy enabled and how many are
     authenticated proxy, including configuration, usage patterns, and traffic patterns

     Usage information for the last seven days of in-console product feedback

     Count of site-to-site accounts by type

     Usage statistics for user and device custom properties

     Count and type of edits to asset intelligence categories

Level 3 - Full
For Configuration Manager version 2409, this level includes the following data:

     Automatic deployment rule evaluation schedule information

     ATP health summary

     Collection evaluation and refresh statistics

     Compliance policy statistics on compliance and errors

<!-- p.628 -->

Compliance settings: SCEP, VPN, Wi-Fi, and compliance policy template
configuration details

DCM config pack for Configuration Manager usage

Detailed client deployment installation errors

Endpoint Protection health summary: including count of protected, at risk,
unknown, and unsupported clients

Endpoint Protection policy configuration

List of processes configured with installation behavior for applications

Minimum/maximum/average number of hours since last software update scan

Minimum/maximum/average number of inactive clients in software update
deployment collections

Minimum/maximum/average number of software updates per package

MSI product code deployment statistics

Overall compliance of software update deployments

Count of groups that have expired software updates

Software update deployment error codes and counts

Software update deployment information: percentage of deployments that are
targeted with client versus UTC time, required versus optional versus silent, and
reboot suppression

Software update products synced by software update point

Software update scan success percentages

Top 50 CPUs in the environment

Type of Exchange Active Sync (EAS) Conditional Access policies (block or
quarantine) for devices that Microsoft Intune manages

Microsoft Store for Business application details: non-aggregate list of synced
applications including AppID, online state or offline state, and total purchased
license counts

Count of clients pushed with option to not allow fallback to NTLM

<!-- p.629 -->

     List of Configuration Manager console extensions

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.630 -->

Frequently asked questions about
diagnostics and usage data
Applies to: Configuration Manager (current branch)

This article provides answers to frequently asked questions about diagnostic and usage data in
Configuration Manager.

Can I turn off diagnostic and usage data?
To help manage when the site sends data, use the service connection point in offline mode. Then
use the service connection tool to manually send data. For more information, see the following
articles:

      About the service connection point
      Use the service connection tool

To support new versions of Windows and cloud services like Microsoft Intune, you need to
update the current branch of Configuration Manager on a regular basis. Microsoft requires at
least the basic level of diagnostic and usage data. This data is used to keep the product up to
date, improve the update experience, and improve the quality and security of the product.

No data is sent to the service when the service connection point is in offline mode. When you
switch to online mode or use the service connection tool, it sends data to the service to check for
updates.

You can also choose the level of data that Configuration Manager collects. For more information,
see Levels of diagnostic usage data.

What is the data retention period?
Microsoft stores Configuration Manager diagnostic and usage data for one year.

Is diagnostics and usage data sent when
setup runs?
No. Diagnostics and usage data is only sent after the site is installed and operational.

<!-- p.631 -->

How frequently is the data sent?
The SQL Server stored procedures run every seven days from the date you installed the site.

     In online mode, the service connection point uploads the data after the queries run.

     In offline mode, you use the service connection tool to upload the data. (The data isn't
     initially available for offline use until seven days after you install the site.)

Can the data be used to form a network map?
No. This data doesn't include any network details, such as IP addresses or detailed geographic
information. For more information, see Levels of diagnostic usage data, and find more detail for
the version you're using.

The data does include time zone information from each site. This information can provide insight
into the broad geolocation and global dispersion of sites in a hierarchy.

Can you see data in custom SQL Server tables?
No. Configuration Manager collects diagnostics and usage data via SQL Server stored
procedures. These stored procedures run against default product tables in the database. All of
these SQL Server tables are prefixed with TEL_. As part of the SQL Server schema detection query,
all table names are hashed for comparison against the known defaults. This behavior determines
that custom tables exist in the database. The presence of custom tables informs Microsoft that
you extended the database schema from the default. It doesn't include any of the data stored
within those tables.

Can you see other databases?
No. The stored procedures to collect data are limited to the Configuration Manager site
database. Microsoft can't see the names of other databases, or any data in other databases.

Is any data sent to other integrated
cloud services?
Yes, when you integrate those services with Configuration Manager. As part of the interaction
with any cloud service, Configuration Manager sends some data to that service. This data is

<!-- p.632 -->

specific to that cloud service, and separate from Configuration Manager diagnostics and usage
data. For more information on the specific data used in the interaction with another cloud service,
see the documentation for that service.

For example, the following cloud services are a part of Microsoft Intune family of products:

      Tenant attach data collection
      Endpoint analytics data collection
      Privacy and personal data in Intune
      Windows Autopilot requirements

Does Configuration Manager collect any
personal data?
No. Configuration doesn't collect or transmit any personal data or customer data. It's an on-
premises product that you directly deploy, manage, and operate. The diagnostics and usage data
that Microsoft collects improves the installation experience, quality, and security of future
releases.

For more information about Configuration Manager data, see Levels of diagnostic usage data.

 Last updated on 04/09/2026

<!-- p.633 -->

Plan for security in Configuration
Manager
Article • 11/16/2023

Applies to: Configuration Manager (current branch)

This article describes the following concepts for you to consider when planning for
security with your Configuration Manager implementation:

      Certificates (self-signed and PKI)

      The trusted root key

      Signing and encryption

      Role-based administration

      Microsoft Entra ID

      SMS Provider authentication

Before you start, make sure you're familiar with the fundamentals of security in
Configuration Manager.

Certificates
Configuration Manager uses a combination of self-signed and public key infrastructure
(PKI) digital certificates. Use PKI certificates whenever possible. Some scenarios require
PKI certificates. When PKI certificates aren't available, the site automatically generates
self-signed certificates. Some scenarios always use self-signed certificates.

For more information, see Plan for certificates.

The trusted root key
The Configuration Manager trusted root key provides a mechanism for Configuration
Manager clients to verify that site systems belong to their hierarchy. Every site server
generates a site exchange key to communicate with other sites. The site exchange key
from the top-level site in the hierarchy is called the trusted root key.

The function of the trusted root key in Configuration Manager resembles a root
certificate in a public key infrastructure. Anything signed by the private key of the

<!-- p.634 -->

trusted root key is trusted further down the hierarchy. Clients store a copy of the site's
trusted root key in the root\ccm\locationservices WMI namespace.

For example, the site issues a certificate to the management point, which it signs with
the private key of the trusted root key. The site shares with clients the public key of its
trusted root key. Then clients can differentiate between management points that are in
their hierarchy and management points that aren't in their hierarchy.

Clients automatically get the public copy of the trusted root key by using two
mechanisms:

     You extend the Active Directory schema for Configuration Manager, and publish
     the site to Active Directory Domain Services. Then clients retrieve this site
     information from a global catalog server. For more information, see Prepare Active
     Directory for site publishing.

     When you install clients using the client push installation method. For more
     information, see Client push installation.

If clients can't get the trusted root key by using one of these mechanisms, they trust the
trusted root key that's provided by the first management point that they communicate
with. In this scenario, a client might be misdirected to an attacker's management point
where it would receive policy from the rogue management point. This action requires a
sophisticated attacker. This attack is limited to the short time before the client retrieves
the trusted root key from a valid management point. To reduce this risk of an attacker
misdirecting clients to a rogue management point, pre-provision the clients with the
trusted root key.

For more information and procedures to manage the trusted root key, see Configure
security.

Signing and encryption
When you use PKI certificates for all client communications, you don't have to plan for
signing and encryption to help secure client data communication. If you set up any site
systems that run IIS to allow HTTP client connections, decide how to help secure the
client communication for the site.

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP client
  communication are deprecated. Configure the site for HTTPS or Enhanced HTTP.

<!-- p.635 -->

  For more information, see Enable the site for HTTPS-only or enhanced HTTP.

To help protect the data that clients send to management points, you can require clients
to sign the data. You can also require the SHA-256 algorithm for signing. This
configuration is more secure, but don't require SHA-256 unless all clients support it.
Many operating systems natively support this algorithm, but older operating systems
might require an update or hotfix.

While signing helps protect the data from tampering, encryption helps protect the data
from information disclosure. You can enable encryption for the inventory data and state
messages that clients send to management points in the site. You don't have to install
any updates on clients to support this option. Clients and management points require
more CPU usage for encryption and decryption.

  ７ Note

  To encrypt the data, the client uses the public key of the management point's
  encryption certificate. Only the management point has the corresponding private
  key, so only it can decrypt the data.

  The client bootstraps this certificate with the management point's signing
  certificate, which it bootstraps with the site's trusted root key. Make sure to
  securely provision the trusted root key on clients. For more information, see The
  trusted root key.

For more information about how to configure the settings for signing and encryption,
see Configure signing and encryption.

For more information on the cryptographic algorithms used for signing and encryption,
see Cryptographic controls technical reference.

Role-based administration
With Configuration Manager, you use role-based administration to secure the access
that administrative users need to use Configuration Manager. You also secure access to
the objects that you manage, like collections, deployments, and sites.

With the combination of security roles, security scopes, and collections, you segregate
the administrative assignments that meet your organization's requirements. Used
together, they define the administrative scope of a user. This administrative scope

<!-- p.636 -->

controls the objects that an administrative user views in the Configuration Manager
console, and it controls the permissions that a user has on those objects.

For more information, see Fundamentals of role-based administration.

Microsoft Entra ID
Configuration Manager integrates with Microsoft Entra ID to enable the site and clients
to use modern authentication.

For more information about Microsoft Entra ID, see Microsoft Entra documentation.

Onboarding your site with Microsoft Entra ID supports the following Configuration
Manager scenarios:

Client scenarios
     Manage clients on the internet via cloud management gateway

     Manage cloud domain-joined devices

     Co-management

     Deploy user-available apps

     Microsoft Store for Business online apps

     Manage Microsoft 365 Apps for enterprise

Server scenarios
     Tenant attach

     Endpoint analytics

     Azure Log Analytics

     Community Hub

     User discovery

SMS Provider authentication

<!-- p.637 -->

You can specify the minimum authentication level for administrators to access
Configuration Manager sites. This feature enforces administrators to sign in to Windows
with the required level before they can access Configuration Manager. It applies to all
components that access the SMS Provider. For example, the Configuration Manager
console, SDK methods, and Windows PowerShell cmdlets.

Configuration Manager supports the following authentication levels:

     Windows authentication: Require authentication with Active Directory domain
     credentials. This setting is the previous behavior, and the current default setting.

     Certificate authentication: Require authentication with a valid certificate that's
     issued by a trusted PKI certificate authority. You don't configure this certificate in
     Configuration Manager. Configuration Manager requires the administrator to be
     signed into Windows using PKI.

     Windows Hello for Business authentication: Require authentication with strong
     two-factor authentication that's tied to a device and uses biometrics or a PIN. For
     more information, see Windows Hello for Business.

       ） Important

       When you select this setting, the SMS Provider and administration service
       require the user's authentication token to contain a multi-factor
       authentication (MFA) claim from Windows Hello for Business. In other words,
       a user of the console, SDK, PowerShell, or administration service has to
       authenticate to Windows with their Windows Hello for Business PIN or
       biometric. Otherwise the site rejects the user's action.

       This behavior is for Windows Hello for Business, not Windows Hello.

For more information on how to configure this setting, see Configure SMS Provider
authentication.

Next steps
     Certificates in Configuration Manager

     Plan for PKI certificates

     Configure security

     Cryptographic controls technical reference

<!-- p.638 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.639 -->

Configure security in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the information in this article to help you set up security-related options for
Configuration Manager. Before you start, make sure you have a Plan for security.

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP client
  communication are deprecated. Configure the site for HTTPS or Enhanced HTTP.
  For more information, see Enable the site for HTTPS-only or enhanced HTTP.

Client PKI certificates
If you want to use public key infrastructure (PKI) certificates for client connections to site
systems that use Internet Information Services (IIS), use the following procedure to
configure settings for these certificates.

   1. In the Configuration Manager console, go to the Administration workspace,
      expand Site Configuration, and select the Sites node. Select the primary site to
      configure.

   2. In the ribbon, choose Properties. Then switch to the Communication Security tab.

   3. Select the settings for site systems that use IIS.

            HTTPS only: Clients that are assigned to the site always use a client PKI
            certificate when they connect to site systems that use IIS. For example, a
            management point and distribution point.

            HTTPS or HTTP: You don't require clients to use PKI certificates.

            Use Configuration Manager-generated certificates for HTTP site systems:
            For more information on this setting, see Enhanced HTTP.

   4. Select the settings for client computers.

<!-- p.640 -->

           Use client PKI certificate (client authentication capability) when available: If
           you chose the HTTPS or HTTP site server setting, choose this option to use a
           client PKI certificate for HTTP connections. The client uses this certificate
           instead of a self-signed certificate to authenticate itself to site systems. If you
           chose HTTPS only, this option is automatically chosen.

           When more than one valid PKI client certificate is available on a client, select
           Modify to configure the client certificate selection methods. For more
           information about the client certificate selection method, see Planning for PKI
           client certificate selection.

           Clients check the certificate revocation list (CRL) for site systems: Enable
           this setting for clients to check your organization's CRL for revoked
           certificates. For more information about CRL checking for clients, see
           Planning for PKI certificate revocation.

   5. To import, view, and delete the certificates for trusted root certification authorities,
     select Set. For more information, see Planning for the PKI trusted root certificates
     and the certificate issuers List.

Repeat this procedure for all primary sites in the hierarchy.

Manage the trusted root key
Use these procedures to pre-provision and verify the trusted root key for a
Configuration Manager client.

  ７ Note

  If clients can get the trusted root key from Active Directory Domain Services or
  client push, you don't have to pre-provision it.

  When clients use HTTPS communication to management points, you don't have to
  pre-provision the trusted root key. They establish trust by the PKI certificates.

For more information on the trusted root key, see Plan for security.

Pre-provision a client with the trusted root key by using a
file
