---
title: "Core infrastructure documentation — pages 441-480"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0441-0480
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0441-0480
family: sccm
documentKind: "doc"
abstract: "The following information describes how Package Transfer Manager manages the transfer of content to standard distribution points, and to distribution points configured as pull-distribution points: 1. Admin deploys content to one or more distribution points at a site. Standard di"
---

# Core infrastructure documentation — pages 441-480

<!-- p.441 -->

The following information describes how Package Transfer Manager manages the
transfer of content to standard distribution points, and to distribution points configured
as pull-distribution points:

   1. Admin deploys content to one or more distribution points at a site.

           Standard distribution point: Distribution Manager creates a content transfer
           job for that content.

           Pull-distribution point: Distribution Manager creates a content transfer job
           for that content.

   2. Distribution Manager runs preliminary checks.

           Standard distribution point: Distribution Manager runs a basic check to
           confirm that each distribution point is ready to receive the content. After this
           check, Distribution Manager notifies Package Transfer Manager to start the
           transfer of content to the distribution point.

           Pull-distribution point: Distribution Manager starts Package Transfer
           Manager, which then notifies the pull-distribution point that there is a new
           content transfer job. Distribution Manager does not check on the status of
           remote distribution points that are pull-distribution points, because each
           pull-distribution point manages its own content transfers.

   3. Package Transfer Manager prepares to transfer content.

           Standard distribution point: Package Transfer Manager examines the single
           instance content store of each specified remote distribution point. The
           purpose of this is to identify any files that are already on that distribution
           point. Then, Package Transfer Manager queues up for transfer only those files
           that are not already present.

              ７ Note

              To copy each file in the distribution to the distribution point, even if the
              files are already present in the single instance store of the distribution
              point, use the Redistribute action for content.

           Pull-distribution point: For each pull-distribution point in the distribution,
           Package Transfer Manager checks the pull-distribution points source
           distribution points, to confirm if the content is available.

<!-- p.442 -->

          When the content is available on at least one source distribution point,
          Package Transfer Manager sends a notification to that pull-distribution
          point. The notification directs that distribution point to begin the process
          of transferring content. The notification includes file names and sizes,
          attributes, and hash values.

          When the content is not yet available, Package Transfer Manager does not
          send a notification to the distribution point. Instead, it repeats the check
          every 20 minutes until the content is available. Then, when the content is
          available, Package Transfer Manager sends the notification to that pull-
          distribution point.

          ７ Note

          For the pull-distribution point to copy each file in the distribution to the
          distribution point, even if the files are already present in the single
          instance store of the pull-distribution point, use the Redistribute action
          for content.

4. Content begins to transfer.

       Standard distribution point: Package Transfer Manager copies files to each
       remote distribution point. During the transfer to a standard distribution point:

          By default, Package Transfer Manager can simultaneously process three
          unique packages, and distribute them to five distribution points in parallel.
          Collectively, these are called Concurrent distribution settings. To set up
          concurrent distribution, in the Software Distribution Component
          Properties for each site, go to the General tab.

          Package Transfer Manager uses the scheduling and network bandwidth
          configurations of each distribution point when transferring content to that
          distribution point. To configure these settings, in the Properties of each
          remote distribution point, go to the Schedule and Rate Limits tabs. For
          more information, see Manage content and content infrastructure for
          Configuration Manager.

       Pull-distribution point: When a pull-distribution point receives a notification
       file, the distribution point begins the process to transfer the content. The
       transfer process runs independently on each pull-distribution point:

        a. The pull-distribution identifies the files in the content distribution that it
          does not already have in its single instance store, and prepares to

<!-- p.443 -->

              download that content from one of its source distribution points.

            b. Next, the pull-distribution point checks with each of its source distribution
              points, in order, until it locates a source distribution point that has the
              content available. When the pull-distribution point identifies a source
              distribution point with the content, it begins the download of that content.

              ７ Note

              The process to download content by the pull-distribution point is the
              same as that used by Configuration Manager clients. For the transfer of
              content by the pull-distribution point, concurrent transfer settings aren't
              used. Scheduling and throttling options that you configure for standard
              distribution points aren't used either.

   5. Content transfer completes.

           Standard distribution point: After the Package Transfer Manager is done
           transferring files to each designated remote distribution point, it verifies the
           hash of the content on the distribution point. Then it notifies Distribution
           Manager that the distribution is complete.

           Pull-distribution point: After the pull-distribution point completes the
           content download, the distribution point verifies the hash of the content.
           Then it submits a status message to the site management point to indicate
           success. If, after 60 minutes, this status is not received, the Package Transfer
           Manager wakes up again. It checks with the pull-distribution point to confirm
           whether the pull-distribution point has downloaded the content. If the
           content download is in progress, the Package Transfer Manager sleeps for
           another 60 minutes before it checks with the pull-distribution point again.
           This cycle continues until the pull-distribution point completes the content
           transfer.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.444 -->

Manage network bandwidth for content
Article • 10/04/2022

To help you manage network bandwidth that is used for the content management
process of Configuration Manager, you can use built-in controls for scheduling and
throttling. You can also use prestaged content. The following sections describe these
options in more detail.

Scheduling and throttling
When you create a package, change the source path for the content, or update content
on the distribution point, the files are copied from the source path to the content library
on the site server. Then, the content is copied from the content library on the site server
to the content library on the distribution points. When content source files are updated,
and the source files have already been distributed, Configuration Manager retrieves only
the new or updated files, and then sends them to the distribution point.

You can use scheduling and throttling controls for site-to-site communication, and for
communication between a site server and a remote distribution point. If network
bandwidth is limited even after you set up the scheduling and throttling controls, you
might consider prestaging the content on the distribution point.

In Configuration Manager, you can set up a schedule and specify throttling settings on
remote distribution points that determine when and how content distribution is
performed. Each remote distribution point can have different configurations that help
address network bandwidth limitations from the site server to the remote distribution
point. The controls for scheduling and throttling to the remote distribution point are
similar to the settings for a standard sender address. In this case, the settings are used
by a new component, called Package Transfer Manager.

Package Transfer Manager distributes content from a site server, as a primary site or
secondary site, to a distribution point that is installed on a site system. The throttling
settings are specified on the Rate Limits tab, and the scheduling settings are specified
on the Schedule tab, for a distribution point that is not on a site server. The time
settings are based on the time zone from the sending site, not the distribution point.

  ） Important

  The Rate Limits and Schedule tabs are displayed only in the properties for
  distribution points that are not installed on a site server.

<!-- p.445 -->

For more information, see Install and configure distribution points for Configuration
Manager.

Prestaged content
You can prestage content to add the content files to the content library on a site server
or distribution point, before you distribute the content. Because the content files are
already in the content library, they do not transfer over the network when you distribute
the content. You can prestage content files for applications and packages.

In the Configuration Manager console, select the content that you want to prestage, and
then use the Create Prestaged Content File Wizard. This creates a compressed,
prestaged content file that contains the files and associated metadata for the content.
Then, you can manually import the content at a site server or distribution point. Note
the following points:

     When you import the prestaged content file on a site server, the content files are
     added to the content library on the site server, and then registered in the site
     server database.

     When you import the prestaged content file on a distribution point, the content
     files are added to the content library on the distribution point. A status message is
     sent to the site server that informs the site that the content is available on the
     distribution point.

You can optionally configure the distribution point as prestaged to help manage
content distribution. Then, when you distribute content, you can choose whether you
want to:

     Always prestage the content on the distribution point.

     Prestage the initial content for the package, and then use the standard content
     distribution process when there are updates to the content.

     Always use the standard content distribution process for the content in the
     package.

Determine whether to prestage content
Consider prestaging content for applications and packages in the following scenarios:

     To address the issue of limited network bandwidth from the site server to a
     distribution point. If scheduling and throttling aren't enough to satisfy your

<!-- p.446 -->

concerns about bandwidth, consider prestaging the content on the distribution
point. Each distribution point has the Enable this distribution point for prestaged
content setting that you can choose in the distribution point properties. When you
enable this option, the distribution point is identified as a prestaged distribution
point, and you can choose how to manage the content on a per-package basis.

The following settings are available in the properties for an application, package,
driver package, boot image, operating system installer, and image. These settings
let you choose how content distribution is managed on remote distribution points
that are identified as prestaged:

  Automatically download content when packages are assigned to distribution
  points: Use this option when you have smaller packages, and the scheduling
  and throttling settings provide enough control for content distribution.

  Download only content changes to the distribution point: Use this option
  when you expect future updates to the content in the package to be generally
  smaller than the initial package. For example, you might prestage an application
  like Microsoft 365 Apps, because the initial package size is over 700 MB and is
  too large to send over the network. However, content updates to this package
  might be less than 10 MB, and are acceptable to distribute over the network.
  Another example might be driver packages, where the initial package size is
  large, but incremental driver additions to the package might be small.

  Manually copy the content in this package to the distribution point: Use this
  option when you have large packages, with content such as an operating
  system, and you never want to use the network to distribute the content to the
  distribution point. When you select this option, you must prestage the content
  on the distribution point.

  ） Important

  The preceding options are applicable on a per-package basis, and are only
  used when a distribution point is identified as prestaged. Distribution points
  that have not been identified as prestaged ignore these settings. In this case,
  content always is distributed over the network from the site server to the
  distribution points.

To restore the content library on a site server. When a site server fails, information
about packages and applications that is contained in the content library is restored
to the site database as part of the restore process, but the content library files are
not restored as part of the process. If you do not have a file system backup to

<!-- p.447 -->

     restore the content library, you can create a prestaged content file from another
     site that contains the packages and applications that you have to have. You can
     then extract the prestaged content file on the recovered site server. For more
     information about site server backup and recovery, see Backup and recovery for
     Configuration Manager.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.448 -->

Security and privacy for content
management in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article contains security and privacy information for content management in
Configuration Manager.

Security guidance

Advantages and disadvantages of HTTPS or HTTP for
intranet distribution points
For distribution points on the intranet, consider the advantages and disadvantages of
using HTTPS or HTTP. In most scenarios, using HTTP and package access accounts for
authorization provides more security than using HTTPS with encryption but without
authorization. However, if you have sensitive data in your content that you want to
encrypt during transfer, use HTTPS.

      When you use HTTPS for a distribution point: Configuration Manager doesn't use
      package access accounts to authorize access to the content. The content is
      encrypted when it's transferred over the network.

      When you use HTTP for a distribution point: You can use package access accounts
      for authorization. The content isn't encrypted when it's transferred over the
      network.

Consider enabling Enhanced HTTP for the site. This feature allows clients to use
Microsoft Entra authentication to securely communicate with an HTTP distribution point.
For more information, see Enhanced HTTP.

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP client
  communication are deprecated. Configure the site for HTTPS or Enhanced HTTP.
  For more information, see Enable the site for HTTPS-only or enhanced HTTP.

<!-- p.449 -->

Protect the client authentication certificate file
If you use a PKI client authentication certificate rather than a self-signed certificate for
the distribution point, protect the certificate file (.pfx) with a strong password. If you
store the file on the network, secure the network channel when you import the file into
Configuration Manager.

When you require a password to import the client authentication certificate that the
distribution point uses to communicate with management points, this configuration
helps to protect the certificate from an attacker. To prevent an attacker from tampering
with the certificate file, use server message block (SMB) signing or IPsec between the
network location and the site server.

Remove the distribution point role from the site server
By default, Configuration Manager setup installs a distribution point on the site server.
Clients don't have to communicate directly with the site server. To reduce the attack
surface, assign the distribution point role to other site systems and remove it from the
site server.

Secure content at the package access level
The distribution point share allows read access to all users. To restrict which users can
access the content, use package access accounts when the distribution point is
configured for HTTP. This configuration doesn't apply to content-enabled cloud
management gateways, which don't support package access accounts.

For more information, see Package access accounts.

Configure IIS on the distribution point role
If Configuration Manager installs IIS when you add a distribution point site system role,
remove HTTP redirection and IIS Management Scripts and Tools when the distribution
point installation is complete. The distribution point doesn't require these components.
To reduce the attack surface, remove these role services for the web server role.

For more information about the role services for the web server role for distribution
points, see Site and site system prerequisites.

Set package access permissions when you create the
package

<!-- p.450 -->

Because changes to the access accounts on the package files become effective only
when you redistribute the package, set the package access permissions carefully when
you first create the package. This configuration is important when the package is large
or distributed to many distribution points, and when the network bandwidth capacity for
content distribution is limited.

Implement access controls to protect media that contains
prestaged content
Prestaged content is compressed but not encrypted. An attacker could read and modify
the files that are downloaded to devices. Configuration Manager clients reject content
that's tampered with, but they still download it.

Import prestaged content with ExtractContent
Only import prestaged content by using the ExtractContent.exe command-line tool. To
avoid tampering and elevation of privileges, use only the authorized command-line tool
that comes with Configuration Manager.

For more information, see Deploy and manage content.

Secure the communication channel between the site
server and the package source location
Use IPsec or SMB signing between the site server and the package source location when
you create applications, package, and other objects with content. This configuration
helps to prevent an attacker from tampering with the source files.

Remove default virtual directories for custom website
with the distribution point role
If you change the site configuration option to use a custom website rather than the
default website after installing a distribution point role, remove the default virtual
directories. When you switch from the default website to a custom website,
Configuration Manager doesn't remove the old virtual directories. Remove the following
virtual directories that Configuration Manager originally created under the default
website:

      SMS_DP_SMSPKG$

      SMS_DP_SMSSIG$

<!-- p.451 -->

      NOCERT_SMS_DP_SMSPKG$

      NOCERT_SMS_DP_SMSSIG$

For more information about using a custom website, see Websites for site system
servers.

For content-enabled cloud management gateways,
protect your Azure subscription details and certificates
When you use content-enabled cloud management gateways (CMGs), protect the
following high-value items:

     The user name and password for your Azure subscription
     The secret keys for Azure app registrations
     The server authentication certificate

Store the certificates securely. If you browse to them over the network when you
configure the CMG, use IPsec or SMB signing between the site system server and the
source location.

For service continuity, monitor the expiry date of the
CMG certificates
Configuration Manager doesn't warn you when the imported certificates for the CMG
are about to expire. Monitor the expiry dates independently from Configuration
Manager. Make sure that you renew and then import the new certificates before the
expiry date. This action is important if you acquire a server authentication certificate
from an external, public provider, because you might need more time to acquire a
renewed certificate.

If a certificate expires, the Configuration Manager cloud services manager generates a
status message with ID 9425. The CloudMgr.log file contains an entry to indicate that
the certificate is in expired state, with the expiry date also logged in UTC.

Security considerations
     Clients don't validate content until after it's downloaded. Configuration Manager
     clients validate the hash on content only after it's downloaded to their client cache.
     If an attacker tampers with the list of files to download or with the content itself,

<!-- p.452 -->

     the download process can take up considerable network bandwidth. Then the
     client discards the content when it finds the invalid hash.

     When you use content-enabled cloud management gateways:

        It automatically restricts access to the content to your organization. You can't
        restrict it further to selected users or groups.

        The management point first authenticates the client. Then the client uses a
        Configuration Manager token to access cloud storage. The token is valid for
        eight hours. This behavior means that if you block a client because it's no longer
        trusted, it can continue to download content from cloud storage until this token
        expires. The management point won't issue another token for the client because
        it's blocked.

        To avoid a blocked client from downloading content within this eight-hour
        window, stop the cloud service. In the Configuration Manager console, go to the
        Administration workspace, expand Cloud Services, and select the Cloud
        Management Gateway node.

Privacy information
Configuration Manager doesn't include any user data in content files, although an
administrative user might choose to do this action.

Next steps
     Fundamental concepts for content management

     Security and privacy for application management

     Security and privacy for software updates

     Security and privacy for OS deployment

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.453 -->

Data transfers between sites
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager uses file-based replication and database replication to transfer
different types of information between sites. Learn about how Configuration Manager
moves data between sites, and how you can manage the transfer of data across your
network.

Types of replication

File-based replication
Configuration Manager uses file-based replication to transfer file-based data between
sites in your hierarchy. This data includes applications and packages that you want to
deploy to distribution points in child sites. It also handles unprocessed discovery data
records that the site transfers to its parent site and then processes.

For more information, see File-based replication.

Database replication
Configuration Manager database replication uses SQL Server to transfer data. It uses this
method to merge changes in its site database with the information from the database at
other sites in the hierarchy.

For more information, see Database replication.

For help with troubleshooting SQL Server replication, see Troubleshoot SQL Server
replication.

See also
Monitor replication

Feedback

<!-- p.454 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.455 -->

File-based replication
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager uses file-based replication to transfer file-based data between
sites in your hierarchy. This data includes applications and packages that you want to
deploy to distribution points in child sites. It also handles unprocessed discovery data
records that the site transfers to its parent site and then processes.

File-based communication between sites uses the server message block (SMB) protocol
on TCP/IP port 445. To control the amount of data the site transfers across the network,
specify bandwidth throttling and pulse mode. Use schedules to control when to send
data across the network.

Routes
The following information can help you set up and use file replication routes.

File replication route
Each file replication route identifies a destination site to which a site transfers file-based
data. Each site supports one file replication route to a specific destination site.

To manage a file replication route, go to the Administration workspace. Expand the
Hierarchy Configuration node, and then select File Replication.

You can change the following settings for file replication routes:

File replication account

This account connects to the destination site, and writes data to that site's SMS_Site
share. The receiving site processes the data written to this share. By default, when you
add a site to the hierarchy, Configuration Manager assigns the new site server's
computer account as its file replication account. It then adds this account to the
destination site's SMS_SiteToSiteConnection_<sitecode> group. This group is local to the
computer that grants access to the SMS_Site share. You can change this account to be a
Windows user account. If you change the account, make sure you add the new account
to the destination site's SMS_SiteToSiteConnection_<sitecode> group.

<!-- p.456 -->

  ７ Note

  Secondary sites always use the computer account of the secondary site server as
  the File Replication Account.

Schedule
Set the schedule for each file replication route. This action restricts the type of data and
time when data can transfer to the destination site.

Rate limits

Specify rate limits for each file replication route. This action controls the network
bandwidth the site uses when it transfers data to the destination site:

     Pulse mode: Specify the size of the data blocks that the site sends to the
     destination site. You can also specify a time delay between sending each data
     block. Use this option when you must send data across a low-bandwidth network
     connection to the destination site.

     For example, you have constraints to send 1 KB of data every five seconds, but not
     1 KB every three seconds. This constraint is regardless of the speed of the link or
     its usage at a given time.

     Limited to maximum transfer rates by hour: The site sends data to a destination
     site by using only the percentage of time that you specify. Configuration Manager
     doesn't identify the network's available bandwidth. It divides the time it can send
     data into slices of time. It then sends the data in a short block of time, which is
     followed by blocks of time when it doesn't send data.

     For example, you set the maximum rate to 50%. Configuration Manager transmits
     data for an amount of time followed by an equal period of time when it doesn't
     send any data. It doesn't manage the actual size of the data block that it sends.
     The site only manages the amount of time during which it sends data.

        Ｕ Caution

        By default, a site can use up to three concurrent sendings to transfer data to
        a destination site. When you enable rate limits for a file replication route, it
        limits the concurrent sendings to that site to one. This behavior applies even
        when the Limit available bandwidth (%) is set to 100%. For example, if you

<!-- p.457 -->

        use the default settings for the sender, this reduces the transfer rate to the
        destination site to be one-third of the default capacity.

Routes between secondary sites

Configure a file replication route between two secondary sites to route file-based
content between those sites.

Sender
Each site has one sender. The sender manages the network connection from one site to
a destination site. It can establish connections to multiple sites at the same time. To
connect to a site, the sender uses the file replication route to the site and identifies the
account it uses to establish the network connection. The sender also uses this account
to write data to the destination site's SMS_Site share.

By default, the sender writes data to a destination site by using multiple concurrent
sendings, or a thread. Each thread can transfer a different file-based object to the
destination site. When the sender begins to send an object, it continues to write blocks
of data for that object until it sends the entire object. After it sends all the data for the
object, a new object can begin to send on that thread.

To manage the sender for a site, go to the Administration workspace, and expand the
Site Configuration node. Select the Sites node, and then select Properties for the site
you want to manage. Switch to the Sender tab to change the sender settings.

You can change the following settings for a sender:

Maximum concurrent sendings

By default, each site uses five concurrent sendings (threads). Three threads are available
for use when it sends data to any one destination site. When you increase this number,
you can increase the throughput of data between sites. More threads mean that
Configuration Manager can transfer more files at the same time. Increasing this number
also increases the demand for network bandwidth between sites.

Retry settings
By default, each site retries a problem connection two times, with a one-minute delay
between connection attempts. You can modify the number of connection attempts the
site makes, and how long to wait between attempts.

<!-- p.458 -->

Next steps
Database replication

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.459 -->

Database replication
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager database replication uses SQL Server to transfer data. It uses this
method to merge changes in its site database with the information from the database at
other sites in the hierarchy.

Note the following points about database replication:

      All sites share the same information.

      When you install a site in a hierarchy, Configuration Manager automatically
      establishes database replication between the new site and its parent site.

      When the site installation finishes, database replication automatically starts.

When you add a new site to a hierarchy, Configuration Manager creates a generic
database at the new site. The parent site creates a snapshot of the relevant data in its
database. It then transfers the snapshot to the new site using file-based replication. The
new site then uses the SQL Server Bulk Copy Program (BCP) to load the information into
its local copy of the Configuration Manager database. After the snapshot loads, each
site conducts database replication with the other site.

To replicate data between sites, Configuration Manager uses its own database
replication service. The database replication service uses SQL Server change tracking to
monitor the local site database for changes. It then replicates the changes to other sites
by using SQL Server Service Broker (SSB). By default, this process uses TCP port 4022.

Replication groups
Configuration Manager groups data that replicates by database replication into different
replication groups. Each replication group has a separate, fixed replication schedule. The
site uses this schedule to determine how frequently it replicates changes to other sites.

For example, a change to a role-based administration configuration replicates quickly to
other sites. This behavior makes sure that the other site can quickly enforce these
changes. A lower-priority configuration change, such as a request to install a new
secondary site, replicates with less urgency. It can take several minutes for a new site
request to reach the destination primary site.

<!-- p.460 -->

Settings
You can modify the following settings for database replication:

     Database replication links: Control when specific traffic traverses the network.

     Distributed views: When a central administration site (CAS) requests selected site
     data, it can access the data directly from the database at a child primary site.

     Schedules: Specify when a replication link is used, and when different types of site
     data replicate.

     Summarization: Change settings for data summarization about network traffic that
     traverses replication links. By default, summarization occurs every 15 minutes. It's
     used in reports for database replication.

     Database replication thresholds: Define when the site reports links as degraded or
     failed. You can also configure when Configuration Manager raises alerts about
     replication links that have a degraded or failed status.

Types of data
Configuration Manager primarily classifies the data that it replicates as either global data
or site data. When database replication occurs, the site transfers changes to global data
and site data across the database replication link. Global data replicates to a parent or
child site. Site data replicates only to a parent site. A third data type, local data, doesn't
replicate to other sites. Local data is information that other sites don't require.

Global data
Global data is administrator-created objects that replicate to all sites throughout the
hierarchy. Secondary sites only receive a subset of global data, as global proxy data. You
create global data at the CAS and primary sites. This type includes the following data:

     Software deployments
     Software updates
     Collection definitions
     Role-based administration security scopes

Site data

<!-- p.461 -->

Site data is operational information created by Configuration Manager primary sites and
their assigned clients. Site data replicates to the CAS, but not to other primary sites. Site
data is only viewable at the CAS and at the primary site where the data originates. You
can only modify site data at the primary site where you created it. This type includes the
following data:

      Hardware inventory
      Status messages
      Alerts
      The results of query-based collections

All site data replicates to the CAS. The CAS does administration and reporting for the
entire site hierarchy.

Database replication links
When you install a new site in a hierarchy, Configuration Manager automatically creates
a database replication link between the parent site and the new site. It creates a single
link to connect the two sites.

To control the transfer of data across the replication link, change settings for each link.
Each replication link supports separate configurations. Each database replication link
includes the following controls:

      Stop the replication of selected site data from a primary site to the CAS. This action
      causes the CAS to access this data directly from the database of the primary site.

      Schedule selected site data to transfer from a child primary site to the CAS.

      Define the settings that determine when a database replication link has a
      degraded or failed status.

      Specify when to raise alerts for a failed replication link.

      Specify how frequently Configuration Manager summarizes data about the
      replication traffic that uses the replication link. It uses this data in reports.

To configure a database replication link, in the Configuration Manager console, go to
the Monitoring workspace. Select the Database Replication node, and edit the
properties for the link. This node is also in the Administration workspace, under the
Hierarchy Configuration node. Edit a replication link from either the parent site or the
child site of the replication link.

<!-- p.462 -->

   Tip

  You can edit database replication links from the Database Replication node in
  either workspace. However, when you use the Database Replication node in the
  Monitoring workspace, you can also view the status of database replication. It also
  provides access to the Replication Link Analyzer tool. Use this tool to help
  investigate problems with database replication.

For more information about how to configure replication links, see Site database
replication controls. For more information about how to monitor replication, see
Monitor database replication.

Distributed views
Through distributed views, when you make a request at the CAS for selected site data, it
directly accesses the database at the child primary site. This direct access replaces the
need to replicate site data from the primary site to the CAS. Because each replication
link is independent from other replication links, you can use distributed views on the
replication links that you choose. You can't use distributed views between a primary site
and a secondary site.

Distributed views provide the following benefits:

     Reduce the CPU load to process database changes at the CAS and primary sites

     Reduce the amount of data that transfers across the network to the CAS

     Improve the performance of the SQL Server that hosts the CAS database

     Reduce the disk space used by the CAS database

Consider using distributed views when a primary site is closely located to the CAS on the
network, the two sites are always on, and always connected. Distributed views replace
the replication of the selected data between the sites with direct connections between
the site database servers at each site. The CAS makes a direct connection each time you
request this data.

The site requests distributed view data in the following example scenarios:

     When you run reports or queries
     When you view information in Resource Explorer
     Collection evaluation for collections that include site data-based rules

<!-- p.463 -->

By default, distributed views are turned off for each replication link. When you turn on
distributed views, you select site data that won't replicate to the CAS across that link.
The CAS accesses this data directly from the database of the child primary site that
shares the link. You can configure the following types of site data for distributed views:

     Hardware inventory data from clients
     Software inventory and software metering data from clients
     Status messages from clients, the primary site, and all secondary sites

When you view data in the Configuration Manager console or in reports, distributed
views are operationally invisible to you. When you request data that's enabled for
distributed views, the CAS site database server directly accesses the child primary site's
database to retrieve the information.

For example, you use a Configuration Manager console connected to the CAS. You
request information about hardware inventory from two primary sites: ABC and XYZ. You
only enabled hardware inventory for distributed views at site ABC. The CAS retrieves
inventory information for XYZ clients from its own database. The CAS retrieves inventory
information for ABC clients directly from the database at site ABC. This information
appears in the Configuration Manager console or in a report without identifying the
source.

If a replication link has a type of data enabled for distributed views, the child primary
site doesn't replicate that data to the CAS. When you turn off distributed views for a
type of data, the child primary site resumes normal data replication to the CAS. Before
this data is available at the CAS, the replication groups for this data must reinitialize
between the primary site and the CAS. After you uninstall a primary site that has
distributed views turned on, the CAS must complete reinitialization of its data before
you can access data that you enabled for distributed views on the CAS.

  ） Important

  When you use distributed views on any replication link in the site hierarchy, before
  you uninstall any primary site, turn off distributed views for all replication links. For
  more information, see Uninstall a primary site that uses distributed views.

Prerequisites and limitations for distributed views
     Only use distributed views on replication links between the CAS and a primary site.

     The CAS must use SQL Server Enterprise edition. The primary site doesn't have this
     requirement.

<!-- p.464 -->

     The CAS can have only one instance of the SMS Provider. Install that single
     instance on the site database server. This configuration supports Kerberos
     authentication. The SQL Server at the CAS requires Kerberos to access the SQL
     Server at the child primary site. There are no limitations on the SMS Provider at the
     child primary site.

     You can only install one reporting services point at the CAS. Install SQL Server
     Reporting Services on the site database server. This configuration supports
     Kerberos authentication. The SQL Server at the CAS requires Kerberos to access the
     SQL Server at the child primary site.

     You can host the site database on a SQL Server Always On failover cluster instance,
     if it has the following configurations:
        The CAS database is on a single SQL Server with a local SMS Provider.
        The primary site listener is on port 1433.

     The computer account of the CAS database server requires Read permissions on
     the primary site database.

  ） Important

  Distributed views and schedules for when data can replicate are mutually exclusive
  settings for a database replication link.

Schedule transfers of site data
To help you control the network bandwidth that's used to replicate site data from a child
primary site to the CAS, schedule when a replication link is used. Then specify when
different types of site data replicate. You can control when the primary site replicates
status messages, inventory, and metering data. Database replication links from
secondary sites don't support schedules for site data. You can't schedule the transfer of
global data.

When you configure a database replication link schedule, you can restrict the transfer of
selected site data from the primary site to the CAS. You can also configure different
times to replicate different types of site data.

  ） Important

  Distributed views and schedules for when data can replicate are mutually exclusive
  configurations for a database replication link.

<!-- p.465 -->

Summarization of traffic
Each site periodically summarizes data about the network traffic that traverses database
replication links for the site. The site uses summarized data in reports for database
replication. Both sites on a replication link summarize the network traffic that traverses
the replication link. The site database server summarizes the data. After it summarizes
data, the information replicates to other sites as global data.

By default, summarization occurs every 15 minutes. To modify the frequency of
summarization for network traffic, in the properties of the database replication link, edit
the Summarization interval. The frequency of summarization affects the information
that you view in reports about database replication. You can choose an interval from 5
to 60 minutes. When you increase the frequency of summarization, you increase the
processing load on the SQL Server at each site on the replication link.

Database replication thresholds
Database replication thresholds define when Configuration Manager reports the status
of a database replication link as either degraded or failed. By default, it sets a link as
degraded when any one replication group fails to complete replication for 12
consecutive attempts. It sets the link as failed when any replication group fails to
replicate in 24 consecutive attempts.

You can specify custom values for degraded or failed status. If you adjust these values,
you can more accurately monitor the health of database replication across the links.

One or more replication groups can fail to replicate while other replication groups
continue to successfully replicate. Plan to review the replication status of a link when it
first reports as degraded.

Consider modifying the retry values for the degraded or failed status of the link in the
following situations:

     There are recurring delays for specific replication groups, and their delay isn't a
     problem

     The network link between sites has low available bandwidth

When you increase the number of retries before the site sets the link to degraded or
failed, you can eliminate false warnings for known issues. This action lets you more
accurately track the status of the link.

<!-- p.466 -->

To understand how frequently replication of that group occurs, consider the replication
sync interval for each replication group. To view the Synchronization Interval for
replication groups, go to the Monitoring workspace in the Configuration Manager
console. In the Database Replication node, select the Replication Detail tab of a
replication link.

For more information about how to monitor database replication, including how to view
the replication status, see Monitor database replication.

Site database replication controls
To help you control the network bandwidth used for database replication, change the
settings for each site database. The settings apply only to the site database in which you
configure the settings. The settings are always used when the site replicates any data by
database replication to any other site.

You can modify the following replication controls for each site database:

      The SSB port.

      The period of time to wait before replication failures trigger the site to reinitialize
      its copy of the site database.

      Compress the data that a site replicates. It only compresses the data for transfer
      between sites, and not for storage in the site database at either site.

To change the settings for the replication controls for a site database, in the
Configuration Manager console, on the Database Replication node, edit the properties
of the site database. This node appears under the Hierarchy Configuration node in the
Administration workspace, and also appears in the Monitoring workspace. To edit the
properties of the site database, select the replication link between the sites, and then
open either Parent Database Properties or Child Database Properties.

   Tip

  You can configure database replication controls from the Database Replication
  node in either workspace. However, when you use the Database Replication node
  in the Monitoring workspace, you can also view the status of database replication
  for a replication link, and access the Replication Link Analyzer tool to help you
  investigate problems with replication.

<!-- p.467 -->

Next steps
Monitor replication

Troubleshoot SQL Server replication

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.468 -->

How clients find site resources and
services
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager clients use a process called service location to locate site system
servers. Clients can communicate with these servers and they provide services that
clients can use. To better configure your sites to successfully support client tasks, you
need to understand how and when clients use service location to find site resources.
These configurations can require the site to interact with domain and network
configurations like Active Directory Domain Services and DNS. They can also require you
to configure more complex alternatives.

Some examples of site system roles that provide services include:

      The core site system server for clients.
      The management point.
      Other site system servers that the client can communicate with, like distribution
      points and software update points.

Fundamentals of service location
When a client uses service location to find a management point to communicate with, it
evaluates the following aspects:

      Current network location
      Communication protocol preference
      Assigned site

Client communication with a management point
A client communicates with a management point (MP) to:

      Download information about other management points for the site. It then builds
      a list of known management points for future service location cycles. This list is
      also known as the MP list.

      Upload configuration details, like inventory and status.

<!-- p.469 -->

     Download a policy that sets configurations on the client, informs it of software to
     install, and other related tasks.

     Request information about other site system roles that provide services that the
     client can use. For example, distribution points for software that the client can
     install, or a software update point for metadata about software updates.

Client service location requests
A Configuration Manager client makes a service location request:

     Every 25 hours of continuous operation.

     When the client detects a change in its network configuration or location.

     When the ccmexec.exe service on the computer starts. This Windows service is the
     core client service.

     When the client needs to locate a site system role that provides a required service.

Client requests for site system roles
When a client attempts to find servers that host roles, it uses service location. It tries to
find a role that supports its communication protocol, either HTTP or HTTPS. By default,
clients use the most secure method available to them.

     To use HTTPS, you need a public key infrastructure (PKI) and install PKI certificates
     on clients and servers. For more information, see PKI certificate requirements for
     Configuration Manager.

     For roles that use IIS and support client communication, you configure them for
     HTTP or HTTPS. If you use HTTP, also consider signing and encryption choices. For
     more information, see Planning for signing and encryption.

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP client
  communication are deprecated. Configure the site for HTTPS or Enhanced HTTP.
  For more information, see Enable the site for HTTPS-only or enhanced HTTP.

Determine assigned management point

<!-- p.470 -->

Primary sites support multiple management points. Each client independently identifies
a management point as its default. When a client first assigns to a primary site, it selects
its default management point. This default management point then becomes that
client's assigned management point.

   Tip

  You can use client installation properties to set the assigned management point for
  a client. For more information, see Client installation properties.

A client selects a management point to communicate with based on the client's current
network location and boundary group configurations. Even though it has an assigned
management point, this server may not be the management point that the client uses.

  ７ Note

  A client always uses the assigned management point for registration messages and
  certain policy messages. This behavior happens even when other communications
  are sent to a proxy or local management point.

You can use preferred management points. Preferred management points are
management points from a client's assigned site that are associated with a boundary
group that the client uses to find site system servers. A preferred management point's
association with a boundary group is similar to how distribution points or state
migration points are associated with a boundary group. If you enable preferred
management points for the hierarchy, when a client uses a management point from its
assigned site, it tries to use a preferred management point before using other
management points from its assigned site.

   Tip

  You can configure management point affinity with a registry key configuration on
  the client. Management point affinity overrides the default behavior for assigned
  management points and lets the client use one or more specific management
  points. For more information, see this blog post from a Microsoft Premier
  engineer.

Each time a client needs to contact a management point, it first checks the MP list. The
client creates an initial MP list when it installs. The client then periodically updates the
list with details about each management point in the hierarchy.

<!-- p.471 -->

When the client can't find a valid management point in its MP list, it searches the service
location sources. It uses the following sources in order, until it finds a management
point that it can use:

    1. Management point
    2. Active Directory Domain Services (AD DS)
    3. DNS

After a client successfully locates and contacts a management point, it downloads the
current list of available management points. It then updates its own local MP list.

This process is the same for all clients. For example, when a Configuration Manager
client that's on the internet connects to an internet-based management point, the
management point sends that client a list of available internet-based management
points. A client that's not on the internet only gets a list of internal management points.

The MP list
The MP list is the preferred service location source for a client. It's a prioritized list of
management points that the client previously identified. The client sorts its MP list
based on its current network location. It stores the list locally in WMI.

Build the initial MP list
During installation of the client, the client uses the following rules to build its initial MP
list:

        Include management points specified during client installation. For example, when
        you use the SMSMP property or /mp parameter.

        Query AD DS for published management points. The client identifies management
        points from AD DS that are in its assigned site and the same product version.

        If it doesn't get any management points from the first two rules, the client checks
        DNS for published management points.

MP list categories
Clients organize their list of management points by using the following categories:

        Proxy: A management point at a secondary site.

<!-- p.472 -->

     Local: Any management point that's associated with the client's current network
     location, as defined by site boundaries.

        When a client belongs to more than one boundary group, it determines the list
        of local management points from the union of all boundaries that include the
        current network location of the client.

        Local management points are typically a subset of a client's assigned
        management points. Unless the client is in a network location that's associated
        with another site with management points servicing its boundary groups.

     Assigned: Any management point that's in the client's assigned site.

You can use preferred management points. Management points at a site that aren't
associated with a boundary group, or that aren't in a boundary group associated with a
client's current network location, aren't considered preferred. The client uses these
management points when it can't find an available preferred management point.

Select a management point to use
For typical communications, a client tries to use a management point in the following
order, based on the client's network location:

   1. Proxy
   2. Local
   3. Assigned

The client always uses the assigned management point for registration messages and
certain policy messages. This behavior happens even when it sends other
communication to a proxy or local management point.

Within each category, the client attempts to use a management point based on
preferences, in the following order:

   1. When the client is configured for HTTPS communication:
      a. HTTPS-capable in a trusted or local forest
      b. HTTPS-capable not in a trusted or local forest
   2. HTTP-capable in a trusted or local forest
   3. HTTP-capable not in a trusted or local forest

From the set of management points sorted by preference, the client attempts to use the
first management point on the list. This sorted list of management points is otherwise
randomized and can't be ordered any further. The order of the list can change each time
the client updates its MP list.

<!-- p.473 -->

When a client can't contact the first management point, it tries each successive
management point on its list. It tries each preferred management point in the category
before trying the non-preferred management points. If a client can't successfully
communicate with any management point in the category, it attempts to contact a
preferred management point from the next category, until it finds a management point
to use.

After a client establishes communication with a management point, it continues to use
that same management point until:

     The client is unable to communicate with the management point for five attempts
     over a period of 10 minutes.

The client then randomly selects a new management point to use.

Active Directory
Domain-joined clients can use AD DS for service location. This behavior requires sites to
publish data to Active Directory.

A client can use AD DS for service location when all the following conditions are true:

     You extended the Active Directory schema.

     You configured the Active Directory forest for publishing, and you configured the
     Configuration Manager site to publish.

     The client computer is a member of an Active Directory domain and can access a
     global catalog server.

If a client can't find a management point to use for service location from AD DS, it
attempts to use DNS.

DNS
Clients on the intranet can use DNS for service location. This behavior requires at least
one site in a hierarchy to publish information about management points to DNS.

Consider using DNS for service location when any of the following conditions are true:

     You haven't extended the AD DS schema to support Configuration Manager.

     Clients on the intranet are in a forest that you haven't enabled for Configuration
     Manager publishing.

<!-- p.474 -->

     You have clients on workgroup computers, and you haven't configured those
     clients for internet-only client management. A workgroup client configured for the
     internet communicates only with internet-facing management points and won't
     use DNS for service location.

     You can configure clients to find management points from DNS.

When a site publishes service location records for management points to DNS:

     Publishing is applicable only to management points that accept client connections
     from the intranet.

     Publishing adds a service location resource record (SRV RR) in the DNS zone of the
     management point server. That server needs a corresponding host entry in DNS.

By default, domain-joined clients search DNS for management point records from the
client's local domain. You can configure a client installation property to specify another
domain suffix.

For more information, see How to configure client computers to find management
points by using DNS publishing.

Publish management points to DNS
To publish management points to DNS, the following two conditions must be true:

     Your DNS servers support service location resource records, by using a version of
     BIND that's at least 8.1.2.

     The specified intranet FQDNs for the management points in Configuration
     Manager have host entries (A records) in DNS.

  ） Important

  Configuration Manager DNS publishing doesn't support a disjointed namespace. If
  you have a disjointed namespace, you can manually publish management points to
  DNS. You can also use one of the other service location methods.

DNS configuration scenarios

The DNS server supports automatic updates

<!-- p.475 -->

You can configure Configuration Manager to automatically publish management points
on the intranet to DNS, or you can manually publish these records to DNS. When
Configuration Manager publishes management points to DNS, it adds their intranet
FQDN and port number in the service location (SRV) record. You configure DNS
publishing in the site's Management Point Component Properties. For more
information, see Site components - Management point.

The DNS zone is set to "Secure only" for dynamic updates

With default permissions, only the first management point can successfully publish to
DNS.

If only one management point can successfully publish and change its DNS record,
clients can get the full MP list from that management point. As long as that one
published management point is healthy, clients can then find their preferred
management point.

The DNS server doesn't support automatic updates but supports
service location records

In this scenario, manually publish management points to DNS. Manually configure the
service location resource record (SRV RR). Configuration Manager supports RFC 2782 for
service location records. These records have the following format:
_Service._Protocol.Name TTL Class SRV Priority Weight Port Target

To publish a management point to Configuration Manager, specify the following values:

       _Service: _mssms_mp_<sitecode> . For example, _mssms_mp_xyz
       ._Protocol: ._tcp
       .Name: Specify the DNS suffix of the management point, for example contoso.com
       TTL: Use 14400 for four hours.
       Class: Specify IN for RFC 1035.
       Priority: Configuration Manager doesn't use this field.
       Weight: Configuration Manager doesn't use this field.
       Port: Specify the port number that the management point uses. For example, 443
       by default for HTTPS.
       Target: Specify the intranet FQDN of the site system server with the management
       point role.

Configure Windows Server DNS

<!-- p.476 -->

If you use Windows Server DNS, use the following procedures to enter this DNS record
for intranet management points.

Configure automatic publishing for a site

  1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

  2. Select the site to configure publishing. In the ribbon, select Configure Site
     Components and choose Management Point.

  3. Select the management points that you want to publish. This selection applies to
     publishing for AD DS and DNS.

  4. Enable the option to Publish selected intranet management points in DNS.

Manually publish management points to DNS on Windows Server

  1. In the DNS management console, select the DNS zone for the management point
     computer.

  2. Verify that there's a host record (A or AAAA) for the intranet FQDN of the site
     system. If this record doesn't exist, create it.

  3. Select New Other Records, choose Service Location (SRV), and then choose
     Create Record.

  4. Specify the following information, and then select Done:

          Domain: If necessary, enter the DNS suffix of the management point, for
          example contoso.com .
          Service: _mssms_mp_<sitecode> . For example, _mssms_mp_xyz
          Protocol: ._tcp
          Priority: Configuration Manager doesn't use this field.
          Weight: Configuration Manager doesn't use this field.
          Port: Specify the port number that the management point uses. For example,
           443 by default for HTTPS.
          Host offering this service: Specify the intranet FQDN of the site system
          server with the management point role.

Repeat these steps for each management point on the intranet that you want to publish
to DNS.

<!-- p.477 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.478 -->

Security and privacy for site
administration in Configuration
Manager
Article • 04/05/2024

Applies to: Configuration Manager (current branch)

This article contains security and privacy information for Configuration Manager sites
and the hierarchy.

Security guidance for site administration
Use the following guidance to help you secure Configuration Manager sites and the
hierarchy.

Run setup from a trusted source and secure
communication
To help prevent someone from tampering with the source files, run Configuration
Manager setup from a trusted source. If you store the files on the network, secure the
network location.

If you do run setup from a network location, to help prevent an attacker from tampering
with the files as they're transmitted over the network, use IPsec or SMB signing between
the source location of the setup files and the site server.

If you use the Setup Downloader to download the files that are required by setup, make
sure that you secure the location where these files are stored. Also secure the
communication channel for this location when you run setup.

Extend the Active Directory schema and publish sites to
the domain
Schema extensions aren't required to run Configuration Manager, but they do create a
more secure environment. Clients and site servers can retrieve information from a
trusted source.

If clients are in an untrusted domain, deploy the following site system roles in the
clients' domains:

<!-- p.479 -->

     Management point

     Distribution point

  ７ Note

  A trusted domain for Configuration Manager requires Kerberos authentication. If
  clients are in another forest that doesn't have a two-way forest trust with the site
  server's forest, these clients are considered to be in an untrusted domain. An
  external trust isn't sufficient for this purpose.

Use IPsec to secure communications
Although Configuration Manager does secure communication between the site server
and the computer that runs SQL Server, Configuration Manager doesn't secure
communications between site system roles and SQL Server. You can only configure
some site systems with HTTPS for intrasite communication.

If you don't use additional controls to secure these server-to-server channels, attackers
can use various spoofing and man-in-the-middle attacks against site systems. Use SMB
signing when you can't use IPsec.

  ） Important

  Secure the communication channel between the site server and the package source
  server. This communication uses SMB. If you can't use IPsec to secure this
  communication, use SMB signing to make sure that the files aren't tampered with
  before clients download and run them.

Don't change the default security groups
Don't change the following security groups that Configuration Manager creates and
manages for site system communication:

     SMS_SiteSystemToSiteServerConnection_MP_<SiteCode>

     SMS_SiteSystemToSiteServerConnection_SMSProv_<SiteCode>

     SMS_SiteSystemToSiteServerConnection_Stat_<SiteCode>

<!-- p.480 -->

Configuration Manager automatically creates and manages these security groups. This
behavior includes removing computer accounts when a site system role is removed.

To make sure service continuity and least privileges, don't manually edit these groups.

Manage the trusted root key provisioning process
If clients can't query the global catalog for Configuration Manager information, they
must rely on the trusted root key to authenticate valid management points. The trusted
root key is stored in the client registry. It can be set by using group policy or manual
configuration.

If the client doesn't have a copy of the trusted root key before it contacts a
management point for the first time, it trusts the first management point it
communicates with. To reduce the risk of an attacker misdirecting clients to an
unauthorized management point, you can pre-provision the clients with the trusted root
key. For more information, see Planning for the trusted root key.

Use non-default port numbers
Using non-default port numbers can provide additional security. They make it harder for
attackers to explore the environment in preparation for an attack. If you decide to use
non-default ports, plan for them before you install Configuration Manager. Use them
consistently across all sites in the hierarchy. Client request ports and Wake On LAN are
examples where you can use non-default port numbers.

Use role separation on site systems
Although you can install all the site system roles on a single computer, this practice is
rarely used on production networks. It creates a single point of failure.

Reduce the attack profile
Isolating each site system role on a different server reduces the chance that an attack
against vulnerabilities on one site system can be used against a different site system.
Many roles require the installation of Internet Information Services (IIS) on the site
system, and this need increases the attack surface. If you must combine roles to reduce
hardware expenditure, combine IIS roles only with other roles that require IIS.

  ） Important
