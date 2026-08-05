---
title: "Software update management documentation — pages 1-40"
type: reference
domain: sccm
slug: sccm-intune-configmgr-sum-p0001-0040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-sum-p0001-0040
family: sccm
documentKind: "doc"
abstract: "Software update management documentation Configuration Manager helps manage the complex task of tracking and applying software updates to clients in your organization. About software update management ｅ OVERVIEW Introduction to software updates Deploy and monitor monthly softwar"
---

# Software update management documentation — pages 1-40

<!-- p.1 -->

Software update management documentation
Configuration Manager helps manage the complex task of tracking and applying software
updates to clients in your organization.

  About software update management

  ｅ OVERVIEW
  Introduction to software updates

  Deploy and monitor monthly software updates example

  Ｙ ARCHITECTURE
  Plan for software updates

  Best practices for software updates

  Get started

  ｀ DEPLOY
  Install a software update point

  Configure classifications and products

  Synchronize software updates

  ｃ HOW-TO GUIDE
  Automatically deploy software updates

  Monitor software updates

  Top tasks

  ｃ HOW-TO GUIDE
  Manage Microsoft 365 Apps updates

<!-- p.2 -->

Enable third-party updates

Manage settings for software updates

ｐ CONCEPT
Optimize Windows update delivery

Software updates maintenance

<!-- p.3 -->

Introduction to software updates in
Configuration Manager
Applies to: Configuration Manager (current branch)

Software updates in Configuration Manager provides a set of tools and resources that can help
manage the complex task of tracking and applying software updates to client computers in the
enterprise. An effective software update management process is necessary to maintain
operational efficiency, overcome security issues, and maintain the stability of the network
infrastructure. However, because of the changing nature of technology and the continual
appearance of new security threats, effective software update management requires consistent
and continual attention.

For an example scenario that shows how you might deploy software updates in your
environment, see Example scenario to deploy security software updates.

Software updates synchronization
Software updates synchronization in Configuration Manager connects to Microsoft Update to
retrieve software updates metadata. The top-level site (central administration site or stand-alone
primary site) synchronizes with Microsoft Update on a schedule or when you manually start
synchronization from the Configuration Manager console. When Configuration Manager finishes
software updates synchronization at the top-level site, software updates synchronization starts at
child sites, if they exist. When synchronization is complete at each primary site or secondary site,
a site-wide policy is created that provides to client computers the location of the software update
points.

  ７ Note

  Software updates are enabled by default in client settings. However, if you set the Enable
  software updates on clients client setting to No to disable software updates on a collection
  or in the default settings, the location for software update points are not sent to associated
  clients. For details, see software updates client settings.

After the client receives the policy, the client starts a scan for software updates compliance and
writes the information to Windows Management Instrumentation (WMI). The compliance

<!-- p.4 -->

information is then sent to the management point that then sends the information to the site
server. For more information about compliance assessment, see the Software updates compliance
assessment section in this topic.

You can install multiple software update points at a primary site. The first software update point
that you install is configured as the synchronization source. This synchronizes from Microsoft
Update or a WSUS server not in your Configuration Manager hierarchy. The other software
update points at the site use the first software update point as the synchronization source.

  ７ Note

  When the software updates synchronization process is complete at the top-level site, the
  software updates metadata is replicated to child sites by using database replication. When
  you connect a Configuration Manager console to the child site, Configuration Manager
  displays the software updates metadata. However, until you install and configure a software
  update point at the site, clients will not scan for software updates compliance, clients will not
  report compliance information to Configuration Manager, and you cannot successfully
  deploy software updates.

Synchronization on the top-level site
The software updates synchronization process at the top-level site retrieves from Microsoft
Update the software updates metadata that meet the criteria that you specify in Software Update
Point Component properties. You configure the criteria only at the top-level site.

  ７ Note

  You can specify an existing WSUS server that is not in the Configuration Manager hierarchy
  instead of Microsoft Updates as the synchronization source.

The following list describes the basic steps for the synchronization process on the top-level site:

   1. Software updates synchronization starts.

   2. WSUS Synchronization Manager sends a request to WSUS running on the software update
     point to start synchronization with Microsoft Update.

   3. The software updates metadata is synchronized from Microsoft Update, and any changes
     are inserted or updated in the WSUS database.

<!-- p.5 -->

   4. When WSUS has finished synchronization, WSUS Synchronization Manager synchronizes the
     software updates metadata from the WSUS database to the Configuration Manager
     database, and any changes after the last synchronization are inserted or updated in the site
     database. The software updates metadata is stored in the site database as a configuration
     item.

   5. The software updates configuration items are sent to child sites by using database
     replication.

   6. When synchronization has finished successfully, WSUS Synchronization Manager creates
     status message 6702.

   7. WSUS Synchronization Manager sends a synchronization request to all child sites.

   8. WSUS Synchronization Manager sends a request one at a time to WSUS running on other
     software update points at the site. The WSUS servers on the other software update points
     are configured to be replicas of WSUS running on the default software update point at the
     site.

Synchronization on child primary and secondary sites
During the software updates synchronization process on the top-level site, the software updates
configuration items are replicated to child sites by using database replication. At the end of the
process, the top-level site sends a synchronization request to the child site, and the child site
starts the WSUS synchronization. The following list provides the basic steps for the
synchronization process on a child primary site or secondary site:

   1. WSUS Synchronization Manager receives a synchronization request from the top-level site.

   2. Software updates synchronization starts.

   3. WSUS Synchronization Manager makes a request to WSUS running on the software update
     point to start synchronization.

   4. WSUS running on the software update point on the child site synchronizes software updates
     metadata from WSUS running on the software update point on the parent site.

   5. When synchronization has finished successfully, WSUS Synchronization Manager creates
     status message 6702.

   6. From a primary site, WSUS Synchronization Manager sends a synchronization request to any
     child secondary sites. The secondary site starts the software updates synchronization with

<!-- p.6 -->

     the parent primary site. The secondary site is configured as a replica of WSUS running on
     the parent site.

   7. WSUS Synchronization Manager sends a request one at a time to WSUS running on other
     software update points at the site. The WSUS servers on the other software update points
     are configured to be replicas of WSUS running on the default software update point at the
     site.

Software updates compliance assessment
Before you deploy software updates to client computers in Configuration Manager, start a scan
for software updates compliance on client computers. For each software update, a state message
is created that contains the compliance state for the update. The state messages are sent in bulk
to the management point and then to the site server, where the compliance state is inserted into
the site database. The compliance state for software updates is displayed in the Configuration
Manager console. You can deploy and install software updates on computers that require the
updates. The following sections provide information about the compliance states and describe
the process for scanning for software updates compliance.

Software updates compliance states
The following lists and describes each compliance state that is displayed in the Configuration
Manager console for software updates.

     Required

     Specifies that the software update is applicable and required on the client computer. Any of
     the following conditions could be true when the software update state is Required:

        The software update was not deployed to the client computer.

        The software update was installed on the client computer. However, the most recent
        state message has not yet been inserted into the database on the site server. The client
        computer rescans for the update after the installation has finished. There might be a
        delay of up to two minutes before the client sends the updated state to the management
        point that then forwards the updated state to the site server.

        The software update was installed on the client computer. However, the software update
        installation requires a computer restart before the update is completed.

        The software update was deployed to the client computer but has not yet been installed.

<!-- p.7 -->

     Not Required

     Specifies that the software update is not applicable on the client computer. Therefore, the
     software update is not required.

     Installed

     Specifies that the software update is applicable on the client computer and that the client
     computer already has the software update installed.

     Unknown

     Specifies that the site server has not received a state message from the client computer,
     typically because one of the following:

        The client computer did not successfully scan for software updates compliance.

        The scan finished successfully on the client computer. However, the state message has
        not yet been processed on the site server, possibly because of a state message backlog.

        The scan finished successfully on the client computer, but the state message has not
        been received from the child site.

        The scan finished successfully on the client computer, but the state message file was
        corrupted in some way and could not be processed.

Scan for software updates compliance process
When the software update point is installed and synchronized, a site-wide machine policy is
created that informs client computers that Configuration Manager software updates was enabled
for the site. When a client receives the machine policy, a compliance assessment scan is
scheduled to start randomly within the next two hours. When the scan is started, a Software
Updates Client Agent process clears the scan history, submits a request to find the WSUS server
that should be used for the scan, and updates the local Group Policy with the WSUS server
location.

  ７ Note

  Internet-based clients must connect to the WSUS server by using SSL.

<!-- p.8 -->

A scan request is passed to the Windows Update Agent (WUA). The WUA then connects to the
WSUS server location that is listed in the local policy, retrieves the software updates metadata
that has been synchronized on the WSUS server, and scans the client computer for the updates. A
Software Updates Client Agent process detects that the scan for compliance has finished, and it
creates state messages for each software update that changed in compliance state after the last
scan. The state messages are sent to the management point in bulk every 15 minutes. The
management point then forwards the state messages to the site server, where the state messages
are inserted into the site server database.

After the initial scan for software updates compliance, the scan is started at the configured scan
schedule. However, if the client has scanned for software updates compliance in the time frame
indicated by the Time to Live (TTL) value, the client uses the software updates metadata that is
stored locally. When the last scan is outside the TTL, the client must connect to WSUS running on
the software update point and update the software updates metadata stored on the client.

Including the scan schedule, the scan for software updates compliance can start in the following
ways:

        Software updates scan schedule: The scan for software updates compliance starts at the
        configured scan schedule that is configured in the Software Updates Client Agent settings.
        For more information about how to configure the Software Updates client settings, see
        software updates client settings.

        Configuration Manager Properties action: The user can start the Software Updates Scan
        Cycle or Software Updates Deployment Evaluation Cycle action on the Action tab in the
        Configuration Manager Properties dialog box on the client computer.

        Deployment reevaluation schedule: The deployment evaluation and scan for software
        updates compliance starts at the configured deployment reevaluation schedule, which is
        configured in the Software Updates Client Agent settings. For more information about the
        Software Updates client settings, see software updates client settings.

        Prior to downloading update files: When a client computer receives an assignment policy
        for a new required deployment, the Software Updates Client Agent downloads the software
        update files to the local client cache. Before downloading the software update files, the
        client agent starts a scan to verify that the software update is still required.

        Prior to software update installation: Just before the software update installation, the
        Software Updates Client Agent starts a scan to verify that the software updates are still
        required.

<!-- p.9 -->

     After software update installation: Just after a software update installation is complete, the
     Software Updates Client Agent starts a scan to verify that the software updates are no
     longer required and creates a new state message that states that the software update is
     installed. When the installation has finished, but a restart is necessary, the state message
     indicates that the client computer is pending a restart.

     After system restart: When a client computer is pending a system restart for the software
     update installation to finish, the Software Updates Client Agent starts a scan after the restart
     to verify that the software update is no longer required and creates a state message that
     states that the software update is installed.

Time to live value

The software updates metadata that is required for the scan for software updates compliance is
stored on the local client computer, and by default, is relevant for up to 24 hours. This value is
known as the Time to Live (TTL).

Scan for software updates compliance types

The client scans for software updates compliance by using an online or offline scan and a forced
or non-forced scan, depending on the way the scan for software updates compliance is started.
Whether the client actually connects to WSUS is the result of two independent decisions:

     Forced or non-forced determines whether the client reuses its cached scan results. A non-
     forced scan reuses the results of the last scan when they're still current and within the TTL,
     and it only runs a new scan when the cache is stale. A forced scan always runs a new scan
     and ignores the cache.

     Online or offline determines where a scan that does run gets its metadata. An online scan
     connects to WSUS on the software update point to refresh the metadata before it evaluates
     the client. An offline scan evaluates the client by using metadata already stored locally,
     without connecting to WSUS.

  ７ Note

  Online describes what a scan is allowed to do, not what it always does. A non-forced online
  scan connects to WSUS only when the cached results are outside the TTL. When the last scan
  is still within the TTL, the client answers from its local cache and doesn't connect to WSUS,
  even though the scan type is online. This is also why forced offline isn't a contradiction: forced

<!-- p.10 -->

  means the cache isn't reused, and offline means the resulting scan uses local metadata
  instead of WSUS. A non-forced offline scan doesn't exist.

The following diagram shows how the two decisions combine:

<!-- p.11 -->

<!-- p.12 -->

The following table summarizes the combinations:

                                                                                               ﾉ   Expand table

 Scan             What it means                                                      Contacts WSUS?
 behavior

 Non-forced       Reuse the cached results if they're still current and within the   Only when the last scan is
 online           TTL; otherwise refresh the metadata from WSUS.                     outside the TTL.

 Forced online    Always refresh the metadata from WSUS, regardless of the           Always.
                  TTL.

 Forced offline   Always run a scan, but evaluate by using local metadata.           Never.

The following describes which methods for starting the scan are online or offline and whether the
scan is forced or non-forced.

     Software updates scan schedule (non-forced online scan)

     At the configured scan schedule, the client connects to WSUS running on the software
     update point to retrieve the software updates metadata only when the last scan was outside
     the TTL.

     Software Updates Scan Cycle or Software Updates Deployment Evaluation Cycle (forced
     online scan)

     The client computer always connects to WSUS running on the software update point to
     retrieve the software updates metadata before the client computer scans for software
     updates compliance. After the scan is complete, the TTL counter is reset. For example, if the
     TTL is 24 hours, after a user starts a scan for software updates compliance, the TTL is reset
     to 24 hours.

     Deployment reevaluation schedule (non-forced online scan)

     At the configured deployment reevaluation schedule, the client connects to WSUS running
     on the software update point to retrieve the software updates metadata only when the last
     scan was outside the TTL.

     Prior to downloading update files (non-forced online scan)

     Before the client can download update files in required deployments, the client connects to
     WSUS running on the software update point to retrieve the software updates metadata only
     when the last scan was outside the TTL.

<!-- p.13 -->

     Prior to software update installation (non-forced online scan)

     Before the client installs software updates in required deployments, the client connects to
     WSUS running on the software update point to retrieve the software updates metadata only
     when the last scan was outside the TTL.

     After software update installation (forced offline scan)

     After a software update is installed, the Software Updates Client Agent starts a scan by
     using the local metadata. The client never connects to WSUS running on the software
     update point to retrieve software updates metadata.

     After system restart (forced offline scan)

     After a software update is installed and the computer is restarted, the Software Updates
     Client Agent starts a scan by using the local metadata. The client never connects to WSUS
     running on the software update point to retrieve software updates metadata.

A scan evaluates the whole catalog, not a single deployment

A scan evaluates the client against all update metadata that's synchronized on the software
update point, not against a single deployment. One scan produces compliance for updates in
new deployments, updates in existing deployments, and updates that aren't deployed at all, in a
single pass.

As a result, the number of deployments doesn't change the number of scans. Whether a client is
targeted by 1 deployment or 10, a single scan against the software update point evaluates the
client for all of them at once.

A scan updates compliance, but installation still requires
deployment policy

Running a Software Updates Scan Cycle refreshes compliance for all updates that the software
update point knows about. However, the client can only install a newly added update after it also
receives the deployment (machine) policy for that update. Refreshing compliance and acting on a
deployment are separate steps:

     To refresh compliance across all updates, use the Software Updates Scan Cycle.

     To make the client act on a new or changed deployment, use the Machine Policy Retrieval
     & Evaluation Cycle, followed by the Software Updates Deployment Evaluation Cycle.

<!-- p.14 -->

Software update deployment packages
A software update deployment package is the vehicle used to download software updates to a
network shared folder, and copy the software update source files to the content library on site
servers and on distribution points that are defined in the deployment. By using the Download
Updates Wizard, you can download software updates and add them to deployment packages
before you deploy them. This wizard lets you provision software updates on distribution points
and verify that this part of the deployment process is successful before you deploy the software
updates to clients.

When you deploy downloaded software updates by using the Deploy Software Updates Wizard,
the deployment automatically uses the deployment package that contains the software updates.
When software updates that have not been downloaded are deployed, you must specify a new or
existing deployment package in the Deploy Software Updates Wizard, and the software updates
are downloaded when the wizard is finished.

  ） Important

  You must manually create the shared network folder for the deployment package source
  files before you specify it in the wizard. Each deployment package must use a different
  shared network folder.

  ） Important

  The SMS Provider computer account and the administrative user who actually downloads
  the software updates both require Write permissions to the package source. Restrict access
  to the package source to reduce the risk of an attacker tampering with the software updates
  source files in the package source.

When a new deployment package is created, the content version is set to 1 before any software
updates are downloaded. When the software update files are downloaded by using the package,
the content version is incremented to 2. Therefore, all new deployment packages start with a
content version of 2. Every time that the content changes in a deployment package, the content
version is incremented by 1. For more information, see Fundamental concepts for content
management.

Clients install software updates in a deployment by using any distribution point that has the
software updates available, regardless of the deployment package. Even if a deployment package

<!-- p.15 -->

is deleted for an active deployment, clients still can install the software updates in the
deployment as long as each update was downloaded to at least one other deployment package
and is available on a distribution point that can be accessed from the client. When the last
deployment package that contains a software update is deleted, client computers cannot retrieve
the software update until the update is downloaded again to a deployment package. Software
updates appear with a red arrow in the Configuration Manager console when the update files are
not in any deployment packages. Deployments appear with a double red arrow if they contain
any updates in this condition.

Software update deployment workflows
There are two main scenarios for deploying software updates in your environment, manual
deployment and automatic deployment. Typically, you deploy software updates manually to
create a baseline for client computers, and then you manage software updates on clients by
using automatic deployment. The following sections provide a summary for the workflow for
manual and automatic deployment for software updates.

Manual deployment of software updates
Manual deployment of software updates is the process of selecting software updates in the
Configuration Manager console and manually starting the deployment process. You typically use
this method of deployment to get the client computers up-to-date with required software
updates before you create automatic deployment rules that manage ongoing monthly software
update deployments, and to deploy out of band software update requirements. The following list
provides the general workflow for manual deployment of software updates:

   1. Filter for software updates that use specific requirements. For example, you could provide
     criteria that retrieves all security or critical software updates that are required on more than
     50 client computers.

   2. Create a software update group that contains the software updates.

   3. Download the content for the software updates in the software update group.

   4. Manually deploy the software update group.

Automatic deployment of software updates
Automatic software updates deployment is configured by using an automatic deployment rule
(ADR). You typically use this method of deployment for your monthly software updates (generally

<!-- p.16 -->

known as Patch Tuesday) and for managing definition updates. When the rule runs, software
updates are removed from the software update group (if using an existing group), the software
updates that meet a specified criteria (for example, all security software updates released in the
last week) are added to a software update group, the content files for the software updates are
downloaded and copied to distribution points, and the software updates are deployed to client
computers in the target collection. The following list provides the general workflow for automatic
deployment of software updates:

   1. Create an ADR that specifies deployment settings such as the following:

           Target collection

           Decide whether to enable the deployment or report on software updates compliance
           for the client computers in the target collection

           Software updates criteria

           Evaluation and deployment schedules

           User experience

           Download properties

   2. The software updates are added to a software update group.

   3. The software update group is deployed to the client computers in the target collection, if it
     is specified.

     You must determine what deployment strategy to use in your environment. For example,
     you might create the ADR and target a collection of test clients. After you verify that the
     software updates are installed on the test group, you can add a new deployment to the rule
     or change the collection in the existing deployment to a target collection that includes a
     larger set of clients. The software update objects that are created by the ADRs are
     interactive.

     Software updates that were deployed by using an ADR are automatically deployed to new
     clients added to the target collection.

     New software updates added to a software update group are automatically deployed to the
     clients in the target collection.

     You can enable or disable deployments at any time for the ADR.

<!-- p.17 -->

     After you create an ADR, you can add additional deployments to the rule. This can help you
     manage the complexity of deploying different updates to different collections. Each new
     deployment has the full range of functionality and deployment monitoring experience, and
     each new deployment that you add:

     Uses the same update group and package which is created when the ADR first runs

     Can specify a different collection

     Supports unique deployment properties including:

         Activation time

         Deadline

         Show or hide end user experience

         Separate alerts for this deployment

Software update deployment process
After you deploy software updates or when an automatic deployment rule runs and deploys
software updates, a deployment assignment policy is added to the machine policy for the site.
The software updates are downloaded from the download location, the Internet, or network
shared folder, to the package source. The software updates are copied from the package source
to the content library on the site server, and then copied to the content library on the distribution
point.

When a client computer in the target collection for the deployment receives the machine policy,
the Software Update Client Agent starts an evaluation scan. The client agent downloads the
content for required software updates from a distribution point to the local client cache at the
Software available time setting for the deployment and then the software updates are available
to install. The software updates in optional deployments (deployments that do not have an
installation deadline) are not downloaded until a user manually starts the installation.

When the configured deadline passes, the Software Updates Client Agent performs a scan to
verify that the software updates are still required. Then it checks the local cache on the client
computer to verify that the software update source files are still available. Finally, the client
installs the software updates. If the content was deleted from the client cache to make room for
another deployment, the client re-downloads the software updates from the distribution point to
the client cache. Software updates are always downloaded to the client cache regardless of the

<!-- p.18 -->

configured maximum client cache size. When the installation is complete, the client agent verifies
that the software updates are no longer required, and then sends a state message to the
management point to indicate that the software updates are now installed on the client.

Required system restart
By default, when software updates from a required deployment are installed on a client computer
and a system restart is required for the installation to finish, the system restart is started. For
software updates that were installed before the deadline, the automatic system restart is
postponed until the deadline, unless the computer is restarted before that for some other reason.
The system restart can be suppressed for servers and workstations. These settings are configured
in the User Experience page of the Deploy Software Updates Wizard or Create Automatic
Updates Rule Wizard.

Deployment reevaluation cycle
By default, client computers start a deployment reevaluation cycle every 7 days. During this
evaluation cycle, the client computer scans for software updates that were previously deployed
and installed. If any software updates are missing, the software updates are reinstalled from the
local cache. If a software update is no longer available in the local cache, it is downloaded from a
distribution point and then installed. You can configure the reevaluation schedule on the
Software Updates page in client settings for the site.

Support for Windows embedded devices that use
write filters
When you deploy software updates to Windows Embedded devices that are write filter-enabled,
you can specify whether to disable the write filter on the device during the deployment and then
restart the device after the deployment. If the write filter is not disabled, the software is deployed
to a temporary overlay and the software will no longer be installed when the device restarts
unless another deployment forces changes to be persisted.

  ７ Note

  When you deploy a software update to a Windows Embedded device, make sure that the
  device is a member of a collection that has a configured maintenance window. This lets you
  manage when the write filter is disabled and enabled, and when the device restarts.

<!-- p.19 -->

The user experience setting that controls the write filter behavior is a check box named Commit
changes at deadline or during a maintenance windows (requires restarts).

For more information about how Configuration Manager manages embedded devices that use
write filters, see Planning for client deployment to Windows Embedded devices.

Extend software updates in Configuration Manager
Use System Center Updates Publisher to manage software updates that are not available from
Microsoft Update. After you publish the software updates to the update server and synchronize
the software updates in Configuration Manager, you can deploy the software updates to
Configuration Manager clients. For more information about Updates Publisher, see Updates
Publisher 2011.

Next steps
Plan for software updates

Last updated on 07/19/2026

<!-- p.20 -->

Icons used for software updates in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Synchronized software updates are displayed in the Configuration Manager console,
and the first column for each software update contains an icon that indicates a specific
state. Software update groups are also represented with an icon that provides
information about the state of the software updates contained in the group. This section
provides information about the software update icons and what each icon represents.

Icons for Software Updates
Synchronized software updates are represented by one of the following icons.

Normal Icon

     The icon with the green arrow represents a normal software update.

Description:

Normal software updates have been synchronized and are available for software
deployment.

Operational Concerns:

There are no operational concerns.

Expired Icon

     The icon with the black X represents an expired software update. You can also
identify expired software updates by viewing the Expired column for the software
update when it displays in the Configuration Manager console.

Description:

Expired software updates were previously deployable to client computers, but once a
software update is expired, new deployments can no longer be created for the software

<!-- p.21 -->

updates. Expired software updates are removed from active deployments and will no
longer be made available to clients.

Operational Concerns:

There are no operational concerns.

Superseded Icon

     The icon with the yellow star represents a superseded software update. You can
also identify superseded software updates by viewing the Superseded column for the
software update when it displays in the Configuration Manager console.

Description:

Superseded software updates have been replaced with newer versions of the software
update. Typically, a software update that supersedes another software update does one
or more of the following things:

     Enhances, improves, or adds to the fix provided by one or more previously
     released software updates.

     Improves the efficiency of its software update file package, which clients install if
     the software update is approved for installation. For example, the superseded
     software update might contain files that are no longer relevant to the fix or to the
     operating systems now supported by the new software update, so those files aren't
     included in the superseding software update's file package.

     Updates newer versions of a product, or in other words, is no longer applicable to
     older versions or configurations of a product. Software updates can also supersede
     other software updates if modifications have been made to expand language
     support. For example, a later revision of a product update for Microsoft 365 Apps
     might remove support for an older operating system, but add additional support
     for new languages in the initial software update release.

     On the Supersedence Rules tab in the Software Update Point Component
     properties, you can specify how to manage superseded software updates. For
     more information, see Supersedence rules.

     Operational Concerns:
     Configuration Manager can automatically expire superseded updates based on a
     schedule you choose. The default setting is to wait 3 months before expiring a
     superseded update. The 3 month default is to give you time to verify the update is

<!-- p.22 -->

     no longer needed by any of your client computers. It's recommended that you
     don't assume that superseded updates should be immediately expired in favor of
     the new, superseding update. You can display a list of the software updates that
     supersede the software update on the Supersedence Information tab in the
     software update properties.

Invalid Icon

     The icon with the red X represents an invalid software update.

Description:

Invalid software updates are in an active deployment, but for some reason the content
(software update files) isn't available. The following are scenarios in which this state can
occur:

     You successfully deploy the software update, but the software update file is
     removed from the deployment package and is no longer available.

     You create a software update deployment at a site and the deployment object is
     successfully replicated to a child site, but the deployment package hasn't
     successfully replicated to the child site.

     Operational Concerns:

     When the content is missing for a software update, clients are unable to install the
     software update until the content becomes available on a distribution point. You
     can redistribute the content to distribution points by using the Redistribute action.
     When content is missing for a software update in a deployment created at a parent
     site, the software update must be replicated or redistributed to the child site. For
     more information about content redistribution, see Manage the content you've
     distributed.

Metadata-Only Icon

     The icon with the blue arrow represents a metadata-only software update.

Description:

Metadata-only software updates are available in the Configuration Manager console for
reporting. You can't deploy or download metadata-only software updates because a
software update file isn't associated with the software updates metadata.

<!-- p.23 -->

Operational Concerns:

Metadata-only software updates are available for reporting purposes and aren't
intended for software update deployment.

Icons for Software Update Groups
Software update groups are represented by one of the following icons.

Normal Icon

     The icon with the green arrow represents a software update group that contains
only normal software updates.

Operational Concerns:

There are no operational concerns.

Expired Icon

     The icon with the black X represents a software update group that contains one or
more expired software updates.

Operational Concerns:

Remove or replace expired software updates in the software update group when
possible.

Superseded Icon

     The icon with the yellow star represents a software update group that contains one
or more superseded software updates.

Operational Concerns:

Replace the superseded software update in the software update group with the
superseding software update when possible.

Invalid Icon

<!-- p.24 -->

     The icon with the red X represents a software update group that contains one or
more invalid software updates.

Operational Concerns:

When the content is missing for a software update, clients are unable to install the
software update until the content becomes available on a distribution point. You can
redistribute the content to distribution points by using the Redistribute action. When
content is missing for a software update in a deployment created at a parent site, the
software update needs to be replicated or redistributed to the child site. For more
information about content redistribution, see Manage the content you've distributed.

Next steps
Plan for software updates

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.25 -->

Plan for software updates in
Configuration Manager
Article • 04/11/2023

Applies to: Configuration Manager (current branch)

Before you use software updates in a Configuration Manager production environment,
it's important that you go through the planning process. Having a good plan for the
software update point infrastructure is key to a successful software updates
implementation. For information about capacity planning for software updates, see Size
and scale numbers.

Determine the software update point
infrastructure
This section includes the following subtopics:

      Software update point list
      Software update point switching
      Manually switch clients to a new software update point
      Software update points in an untrusted forest
      Use an existing WSUS server as the synchronization source at the top-level site
      Software update point on a secondary site
      Plan for internet-based clients
      Plan software update content
      Plan for third-party updates

The central administration site and all child primary sites must have a software update
point. As you plan for the software update point infrastructure, determine the following
dependencies:

      Where to install the software update point for the site
      Which sites require a software update point that accepts communication from
      internet-based clients
      Whether you need a software update point at secondary sites

  ） Important

<!-- p.26 -->

  For more information about the internal and external dependencies that are
  required for software updates, see Prerequisites for software updates.

Add multiple software update points at a Configuration Manager primary site to provide
fault tolerance. The failover design of the software update point is different than the
pure randomization model that's used in the design for management points. Unlike in
the design of management points, there are client and network performance costs in
the software update point design when clients switch to a new software update point.
When the client switches to a new WSUS server to scan for software updates, the result
is an increase in the catalog size and associated client-side and network performance
demands. Therefore, the client preserves affinity with the last software update point
from which it successfully scanned.

The first software update point that you install on a primary site is the synchronization
source for all additional software update points that you add at the primary site. After
you add software update points and start synchronization, view the status of the
software update points and the synchronization source from the Software Update Point
Synchronization Status node in the Monitoring workspace.

When there's a failure of the software update point configured as the synchronization
source for the site, manually remove the failed role. Then select a new software update
point to use as the synchronization source. For more information, see Remove a site
system role.

Software update point list
Configuration Manager provides the client with a software update point list in the
following scenarios:

     A new client receives the policy to enable software updates

     A client can't contact its assigned software update point and needs to switch to
     another

The client randomly selects a software update point from the list. It prioritizes the
software update points in the same forest. Configuration Manager provides clients with
a different list depending on the type of client:

     Intranet-based clients: Receive a list of software update points that you can
     configure to allow connections only from the intranet, or a list of software update
     points that allow internet and intranet client connections.

<!-- p.27 -->

      Internet-based clients: Receive a list of software update points that you configure
      to allow connections only from the internet, or a list of software update points that
      allow internet and intranet client connections.

Software update point switching

  ７ Note

  Clients use boundary groups to find a new software update point. If their current
  software update point is no longer accessible, they also use boundary groups to
  fallback and find a new one. Add individual software update points to different
  boundary groups to control which servers a client can find. For more information,
  see Software update points.

If you have multiple software update points at a site, and one fails or becomes
unavailable, clients will connect to a different software update point. With this new
server, clients continue to scan for the latest software updates. When a client is first
assigned a software update point, it stays assigned to that software update point unless
it fails to scan.

The scan for software updates can fail with a number of different retry and non-retry
error codes. When the scan fails with a retry error code, the client starts a retry process
to scan for the software updates on the software update point. The high-level
conditions that result in a retry error code are typically because the WSUS server is
unavailable or because it is temporarily overloaded. When the client fails to scan for
software updates, it uses the following process:

   1. The client scans for software updates:

            At its scheduled time
            When it's manually run from the control panel on the client
            When it's manually run from the Configuration Manager console via a client
            notification action
            When it's run from a Configuration Manager SDK method

   2. If the scan fails, the client waits 30 minutes to retry the scan. It uses the same
      software update point.

   3. The client retries a minimum of four times every 30 minutes. After the fourth
      failure, and after it waits an additional two minutes, the client moves to the next
      software update point in its list.

<!-- p.28 -->

   4. The client repeats this process with the new software update point. After a
       successful scan, the client continues to connect to the new software update point.

The following list provides additional information to consider for software update point
retry and switching scenarios:

       If a client is disconnected from the intranet and fails to scan for software updates,
       it doesn't switch to another software update point. This failure is expected,
       because the client can't reach the internal network or a software update point that
       allows connections from the intranet. The Configuration Manager client
       determines the availability of the intranet software update point.

       If you're managing clients on the internet, and have configured multiple software
       update points to accept communication from clients on the internet, the switching
       process follows the standard retry process previously described.

       If the scan process starts, but the client is turned off before the scan completes, it
       isn't considered a scan failure and it doesn't count as one of the four retries.

When Configuration Manager receives any of the following Windows Update Agent
error codes, the client retries the connection:

2149842970, 2147954429, 2149859352, 2149859362, 2149859338, 2149859344,
2147954430, 2147747475, 2149842974, 2149859342, 2149859372, 2149859341,
2149904388, 2149859371, 2149859367, 2149859366, 2149859364, 2149859363,
2149859361, 2149859360, 2149859359, 2149859358, 2149859357, 2149859356,
2149859354, 2149859353, 2149859350, 2149859349, 2149859340, 2149859339,
2149859332, 2149859333, 2149859334, 2149859337, 2149859336, 2149859335

To look up the meaning of an error code, convert the decimal error code to
hexadecimal, and then search for the hexadecimal value on a site such as the Windows
Update Agent - Error Codes Wiki       . For example, the decimal error code 2149842970 is
hexadecimal 8024001A, which means WU_E_POLICY_NOT_SET A policy value was not
set.

Manually switch clients to a new software update point
Switch Configuration Manager clients to a new software update point when there are
issues with the active software update point. This change only happens when a client
receives multiple software update points from a management point.

  ） Important

<!-- p.29 -->

  When you switch devices to use a new server, the devices use fallback to find that
  new server. Clients switch to the new software update point during their next
  software updates scan cycle.

  Before you start this change, review your boundary group configurations to make
  sure that your software update points are in the correct boundary groups. For more
  information, see Software update points.

  Switching to a new software update point generates additional network traffic. The
  amount of traffic depends on your WSUS configuration settings, for example, the
  synchronized classifications and products, or use of a shared WSUS database. If you
  plan to switch multiple devices, consider doing so during maintenance windows.
  This timing reduces the impact to your network when clients scan with the new
  software update point.

Process to switch software update points

Start this change on a device collection. Once triggered, the clients look for another
software update point at the next scan.

   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select the Device Collections node.

   2. Select the target collection. On the Home tab of the ribbon, in the Collection
     group, select Client Notification, and then select Switch to next Software Update
     Point.

Software update points in an untrusted forest
Create one or more software update points at a site to support clients in an untrusted
forest. To add a software update point in another forest, first install and configure a
WSUS server in that forest. Then start the wizard to add a Configuration Manager site
server with the software update point site system role. In the wizard, configure the
following settings to successfully connect to WSUS in the untrusted forest:

     Specify a Site System Installation account that can access the WSUS server in the
     untrusted forest.

     Specify a WSUS Server Connection account to connect to the WSUS server.

For example, you have a primary site in forest A with two software update points (SUP01
and SUP02). For the same primary site, you also have two software update points

<!-- p.30 -->

(SUP03 and SUP04) in forest B. When switching to the next software update point, the
clients prioritize the servers from the same forest.

Use an existing WSUS server as the synchronization
source at the top-level site
Typically, the top-level site in your hierarchy is configured to synchronize software
updates metadata with Microsoft Update. When your organizational security policy
doesn't allow the top-level site to access to the internet, configure the synchronization
source for the top-level site to use an existing WSUS server. This WSUS server isn't in
your Configuration Manager hierarchy. For example, you have a WSUS server in an
internet-connected network (DMZ), but your top-level site is in an internal network
without internet access. Configure the WSUS server in the DMZ as your synchronization
source for software updates metadata. Configure the WSUS server in the DMZ to
synchronize software updates with the same criteria that you need in Configuration
Manager. Otherwise, the top-level site might not synchronize the software updates that
you expect. When you install the software update point, configure a WSUS server
connection account. This account needs access to the WSUS server in the DMZ. Also
confirm that the firewall permits traffic for the appropriate ports. For more information,
see the ports used by the software update point to the synchronization source.

Software update point on a secondary site
The software update point is optional on a secondary site. Install only one software
update point at a secondary site. When a software update point isn't installed at the
secondary site, devices within the boundaries of a secondary site use a software update
point at their assigned primary site. You typically install a software update point at a
secondary site when there's limited network bandwidth between the devices in the
secondary site and the software update points at the parent primary site. You may also
use this configuration when the software update point at the primary site approaches
the capacity limit. After you successfully install and configure a software update point at
the secondary site, a site-wide policy is updated for clients, and they start to use the
new software update point.

Plan for internet-based clients
When you need to manage devices that roam off your network onto the internet,
develop a plan for how to manage software updates on these devices. Configuration
Manager supports several technologies for this scenario. Use one or a combination as
necessary to meet the requirements of your organization.

<!-- p.31 -->

Cloud management gateway
Create a cloud management gateway in Microsoft Azure and enable at least one on-
premises software update point to allow traffic from internet-based clients. As clients
roam onto the internet, they continue to scan against your software update points. All
internet-based clients always get content from the Microsoft Update cloud service.

For more information, see Overview of cloud management gateway and Configure
boundary groups.

  ７ Note

  Starting in version 2203, you can set clients to prefer to scan against a cloud
  management gateway (CMG) software update point (SUP) over an on-premises
  SUP. This behavior is controlled by the Prefer cloud based source over on-
  premises source option in the boundary group. To reduce the performance impact
  of this change, existing clients don't automatically switch their SUP to a cloud-
  based SUP. The client will stay assigned to their current SUP unless their current
  SUP fails or the client is manually switched to a new SUP.

Internet-based client management
Place a software update point in an internet-facing network and enable it to allow traffic
from internet-based clients. As clients roam onto the internet, they switch to this
software update point for scanning. All internet-based clients always get content from
the Microsoft Update cloud service.

For more information on the advantages and disadvantages of internet-based client
management, see Manage clients on the internet.

Windows Update for Business
Windows Update for Business allows you to keep Windows 10 or later devices always
up-to-date with the latest quality and feature updates. These devices connect directly to
the Windows Update cloud service. Configuration Manager can differentiate between
Windows computers that use WUfB and WSUS for getting software updates.

For more information, see Integration with Windows Update for Business.

Plan software update content

<!-- p.32 -->

Clients need to download the content files for software updates in order to install them.
Configuration Manager provides several technologies to support management and
delivery of this content. Or configure software update deployments to allow or require
clients to get content directly from the Microsoft Update cloud service.

  ７ Note

  Starting March 28, 2023, on-premises Windows 11, version 22H2 devices will
  receive quality updates via the Unified Update Platform (UUP). UUP on-premises
  interoperates with WSUS and Microsoft Configuration Manager. UUP quality
  updates continue to be cumulative and include all released Windows quality and
  security fixes. On-premises update management with Unified Update Platform
  (UUP) requires an additional 10 GB of space per Windows version and processor
  architecture for each version. For more information, see the UUP considerations
  section.

Download and distribute content
By default, the software update management process in Configuration Manager uses
the built-in content management features. These features include the centralized,
single-instance store content library, and the distributed design of the distribution point
site system role. You use these features when you download and distribute software
update deployment packages.

For more information, see Download software updates.

Manage express installation files for Windows 10 or later
Configuration Manager supports the use of express installation files for Windows
updates. Express update files and supporting technologies such as Delivery Optimization
can help reduce the network impact of large content files downloading to clients.

For more information, see Optimize Windows update delivery.

Clients download content from the internet
When you deploy software updates to clients, configure the deployment for clients to
download content from the Microsoft Update cloud service. When clients aren't able to
download content from another content source, they can still download the content
from the internet.

<!-- p.33 -->

You don't have to create a deployment package when deploying software updates.
When you select the No deployment package option, clients can still download content
from local sources if available, but typically download from the Microsoft Update
service.

Internet-based clients always download content from the Microsoft Update cloud
service. Don't distribute software update deployment packages to a content-enabled
cloud management gateway (CMG).

Plan for third-party updates
Configuration Manager integrates with WSUS, which natively supports software updates
published by Microsoft. Most customers use other third-party applications that also
need updates. There are several options to consider for keeping third-party applications
up to date.

Supersede applications to update

Use a supersedence relationship with the application management feature in
Configuration Manager to upgrade or replace existing applications. When you
supersede an application, specify a new deployment type to replace the deployment
type of the superseded application. Also decide whether to upgrade or uninstall the
superseded application before the superseding application is installed.

For more information, see Revise and supersede applications.

Third-party software updates

You can use the Third-Party Software Update Catalogs node in the Configuration
Manager console to subscribe to third-party catalogs, publish their updates to your
software update point, and then deploy them to clients.

For more information, see Third-party software updates.

System Center Updates Publisher

System Center Updates Publisher (SCUP) is a stand-alone tool that enables independent
software publishers or line-of-business application developers to manage custom
updates. These updates include those with dependencies, like drivers and update
bundles. SCUP can also be used for third-party update catalogs that aren't available
directly in the console.

<!-- p.34 -->

For more information, see System Center Updates Publisher.

Plan for software update point installation
This section includes the following subtopics:

     Requirements for the software update point
     Plan for WSUS installation
     Configure firewalls

This section provides information about the steps to take to successfully plan and
prepare for the software update point installation. Before you create a site system role
for the software update point in Configuration Manager, there are several requirements
to consider. The specific requirements depend on your Configuration Manager
infrastructure. When you configure the software update point to communicate by using
HTTPS, this section is especially important to review. HTTPS-enabled servers require
additional steps to work properly.

Requirements for the software update point
Install the software update point role on a site system that meets the minimum
requirements for WSUS and the supported configurations for Configuration Manager
site systems.

     For more information about the minimum requirements for the WSUS server role
     in Windows Server, see Review considerations and system requirements.

     For more information about the supported configurations for Configuration
     Manager site systems, see Site and site system prerequisites.

Plan for WSUS installation
Install a supported version of WSUS on all site system servers that you configure for the
software update point role. When you don't install the software update point on the site
server, install the WSUS Administration Console on the site server. This component
allows the site server to communicate with WSUS that runs on the software update
point.

When you use WSUS on Windows Server 2012 or later, configure additional permissions
to allow the WSUS Configuration Manager component in Configuration Manager to
connect to WSUS. This component performs periodic health checks. Choose one of the
following options to configure the required permission:

<!-- p.35 -->

     Add the SYSTEM account to the WSUS Administrators group

     Add the NT AUTHORITY\SYSTEM account as a user for the WSUS database
     (SUSDB). Configure a minimum of the webService database role membership.

For more information about how to install WSUS on Windows Server, see Install the
WSUS Server Role.

When you install more than one software update point at a primary site, use the same
WSUS database for each software update point in the same Active Directory forest.
Sharing the same database improves performance when clients switch to a new software
update point. For more information, see Use a shared WSUS database for software
update points.

Configuring the WSUS content directory path
When you install WSUS, you'll need to provide a content directory path. The WSUS
content directory is primarily used for storing the Microsoft Software License Terms files
needed by clients during scanning. The Configuration Manager The WSUS content
directory shouldn't overlap with your content source directory for Configuration
Manager software deployment packages. Overlapping the WSUS content directory and
the Configuration Manager package source will result in incorrect files being removed
from the WSUS content directory.

Configure WSUS to use a custom website
When you install WSUS, you have the option to use the existing IIS Default website, or
to create a custom WSUS website. Create a custom website for WSUS so that IIS hosts
the WSUS services in a dedicated virtual website. Otherwise it shares the same website
that's used by the other Configuration Manager site systems or applications. This
configuration is especially necessary when you install the software update point role on
the site server. When you run WSUS in Windows Server 2012 or later, WSUS is
configured by default to use port 8530 for HTTP and port 8531 for HTTPS. Specify these
ports when you create the software update point at a site.

Configure WSUS as a replica server
When you add the software update point role on a primary site server, you can't use a
WSUS server that's configured as a replica. When the WSUS server is configured as a
replica, Configuration Manager fails to configure the WSUS server, and the WSUS
synchronization fails. The first software update point that you install at a primary site is

<!-- p.36 -->

the default software update point. Additional software update points at the site are
configured as replicas of the default software update point.

Decide whether to configure WSUS to use SSL

Using the SSL protocol to help secure the software update point is highly
recommended. WSUS uses SSL to authenticate client computers and downstream WSUS
servers to the WSUS server. WSUS also uses SSL to encrypt software update metadata.
When you choose to secure WSUS with SSL, prepare the WSUS server before you install
the software update point.

When you install and configure the software update point, select the option to Enable
SSL communications for the WSUS Server. Otherwise, Configuration Manager
configures WSUS not to use SSL. When you enable SSL on a software update point, also
configure any software update points at child sites to use SSL. For more information, see
the Configure a software update point to use TLS/SSL with a PKI certificate tutorial.

  ７ Note

  To ensure that the best security protocols are in place, we highly recommend that
  you use the TLS/SSL protocol to help secure your software update infrastructure.
  Beginning with the September 2020 cumulative update, HTTP-based WSUS servers
  will be secure by default. A client scanning for updates against an HTTP-based
  WSUS will no longer be allowed to leverage a user proxy by default. If you still
  require a user proxy despite the security trade-offs, a new software updates client
  setting is available to allow these connections. For more information about the
  changes for scanning WSUS, see September 2020 changes to improve security for
  Windows devices scanning WSUS           .

Configure firewalls
The software update point at a Configuration Manager central administration site
communicates with WSUS on the software update point. WSUS communicates with the
synchronization source to synchronize software updates metadata. Software update
points at a child site communicate with the software update point at the parent site.
When there's more than one software update point at a primary site, the additional
software update points communicate with the default software update point. The
default role is the first software update point that's installed at the site.

You might need to configure the firewall to allow the HTTP or HTTPS traffic that WSUS
uses in following scenarios:

<!-- p.37 -->

     Between the software update point and the internet
     Between a software update point and its upstream synchronization source
     Between additional software update points

The connection to Microsoft Update is always configured to use port 80 for HTTP and
port 443 for HTTPS. Use a custom port for the connection from WSUS on the software
update point at a child site to WSUS on the software update point at the parent site.
When your security policy doesn't allow the connection, use the export and import
synchronization method. For more information, see the Synchronization source section
in this article. For more information about the ports that WSUS uses, see How to
determine the port settings used by WSUS in Configuration Manager.

Restrict access to specific domains
If your organization restricts network communication with the internet using a firewall or
proxy device, you need to allow the active software update point to access internet
endpoints. Then WSUS and Automatic Updates can communicate with the Microsoft
Update cloud service.

For more information, see Internet access requirements.

Plan for synchronization settings
This section includes the following subtopics:

     Synchronization source
     Synchronization schedule
     Update classifications
     Products
     Supersedence rules
     Languages
     Maximum run time

Software updates synchronization in Configuration Manager downloads the software
updates metadata based on criteria that you configure. The top-level site in your
hierarchy synchronizes software updates from Microsoft Update. You have the option to
configure the software update point on the top-level site to synchronize with an existing
WSUS server, not in the Configuration Manager hierarchy. The child primary sites
synchronize software updates metadata from the software update point on the central
administration site. Before you install and configure a software update point, use this
section to plan for the synchronization settings.

<!-- p.38 -->

Synchronization source
The synchronization source settings for the software update point specify the location
for where the software update point retrieves software updates metadata. It also
specifies whether the synchronization process creates WSUS reporting events.

     Synchronization source: By default, the software update point at the top-level site
     configures the synchronization source for Microsoft Update. You have the option
     to synchronize the top-level site with an existing WSUS server. The software
     update point on a child primary site configures the synchronization source as the
     software update point at the central administration site.

        The first software update point that you install at a primary site, which is the
        default software update point, synchronizes with the central administration site.
        Additional software update points at the primary site synchronize with the
        default software update point at the primary site.

        When a software update point is disconnected from Microsoft Update or from
        the upstream update server, configure the synchronization source not to
        synchronize with a configured synchronization source. Instead configure it to
        use the export and import function of the WSUSUtil tool to synchronize
        software updates. For more information, see Synchronize software updates from
        a disconnected software update point.

     WSUS reporting events: The Windows Update Agent on client computers can
     create event messages for WSUS reporting. These events aren't used by
     Configuration Manager. Thus, the option, Do not create WSUS reporting events, is
     selected by default. When these events aren't created, the only time that the client
     should connect to the WSUS server is during software update evaluation and
     compliance scans. If these events are needed for reporting outside of
     Configuration Manager, modify this setting to create WSUS reporting events.

  ） Important

  If you're sharing the WSUS database (SUSDB) across multiple software update
  points for the top-level site, make sure that each of those WSUS servers meets the
  internet access requirements for software updates. When the database is shared
  the top-level site, Configuration Manager can select any one of those WSUS servers
  to sync with Microsoft Update.

Synchronization schedule

<!-- p.39 -->

Configure the synchronization schedule only at the software update point on the top-
level site in the Configuration Manager hierarchy. When you configure the
synchronization schedule, the software update point synchronizes with the
synchronization source at the date and time that you specified. The custom schedule
allows you to synchronize software updates to optimize for your environment. Consider
the performance demands of the WSUS server, site server, and network. For example,
2:00 AM once a week. Alternatively, manually start synchronization on the top-level site
by using the Synchronization Software Updates action from the All Software Updates
or Software Update Groups nodes in the Configuration Manager console.

   Tip

  Schedule the software updates synchronization to run by using a time that's
  appropriate for your environment. One common scenario is to set the
  synchronization schedule to run shortly after Microsoft's regular software update
  release on the second Tuesday of each month. This day is typically referred to as
  Patch Tuesday. If you use Configuration Manager to deliver Endpoint Protection
  and Windows Defender definition and engine updates, consider setting the
  synchronization schedule to run daily.

After the software update point successfully synchronizes, it sends a synchronization
request to child sites. If you have additional software update points at a primary site, it
sends a synchronization request to each software update point. This process is repeated
on every site in the hierarchy.

Update classifications
Every software update is defined with an update classification that helps to organize the
different types of updates. During the synchronization process, the site synchronizes the
metadata for the specified classifications.

Configuration Manager supports synchronization of the following update classifications:

     Critical Updates: A broadly released update for a specific problem that addresses a
     critical, non-security-related bug.

     Definition Updates: An update to virus or other definition files.

     Feature Packs: New product features that are distributed outside of a product
     release and are typically included in the next full product release.

<!-- p.40 -->

     Security Updates: A broadly released update for a product-specific, security-
     related issue.

     Service Packs: A cumulative set of hotfixes that is applied to an OS or application.
     These hotfixes include security updates, critical updates, and software updates.

     Tools: A utility or feature that helps to complete one or more tasks.

     Update Rollups: A cumulative set of hotfixes that is packaged together for easy
     deployment. These hotfixes include security updates, critical updates, and software
     updates. An update rollup generally addresses a specific area, such as security or a
     product component.

     Updates: An update to an application or file that's currently installed.

     Upgrades: A feature update to a new version of Windows.

Configure the update classification settings only on the top-level site. The update
classification settings aren't configured on the software update point on child sites,
because the software updates metadata is replicated from the top-level site. When you
select the update classifications, be aware the more classifications that you select, the
longer it takes to synchronize the software updates metadata.

  ２ Warning

  As a best practice, clear all classifications before you synchronize for the first time.
  After the initial synchronization, select the desired classifications, and then rerun
  synchronization.

Products
The metadata for each software update defines one or more products for which the
update is applicable. A product is a specific edition of an OS or application. An example
of a product is Microsoft Windows 10. A product family is the base OS or application
from which the individual products are derived. An example of a product family is
Microsoft Windows, of which Windows 10 and Windows Server 2016 are members.
Select a product family or individual products within a product family.

When software updates are applicable to multiple products, and at least one of the
products is selected for synchronization, all of the products appear in the Configuration
Manager console even if some products weren't selected. For example, you only select
