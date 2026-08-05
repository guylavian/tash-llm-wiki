---
title: "Core infrastructure documentation — pages 321-360"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0321-0360
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0321-0360
family: sccm
documentKind: "doc"
abstract: "primary site supports 2250 distribution points when 2000 of those distribution points are configured as pull-distribution points. Each distribution point supports connections from up to 4,000 clients. A pull-distribution point acts like a client when it accesses content from a s"
---

# Core infrastructure documentation — pages 321-360

<!-- p.321 -->

       primary site supports 2250 distribution points when 2000 of those distribution
       points are configured as pull-distribution points.

       Each distribution point supports connections from up to 4,000 clients.

       A pull-distribution point acts like a client when it accesses content from a source
       distribution point.

    Each primary site supports a combined total of up to 5,000 distribution points. This
    total includes all the distribution points at the primary site and all the distribution
    points that belong to the primary site's child secondary sites.

    Each distribution point supports a combined total of up to 10,000 packages and
    applications.

 ２ Warning

 The actual number of clients that one distribution point can support depends on
 the speed of the network and the hardware configuration of the server.

 The number of pull-distribution points that one source distribution point can
 support similarly depends on the speed of the network and the hardware
 configuration of the source distribution point. But this number is also affected by
 the amount of content that you've deployed. This effect is because, unlike clients
 that typically access content at different times during a deployment, all pull-
 distribution points request content at the same time. Pull-distribution points can
 request all available content, not just the content that is applicable to them. When
 you place a high processing load on a source distribution point, there can be
 unexpected delays in distributing the content to the target distribution points.

Fallback status point
    Each fallback status point can support up to 100,000 clients.

Management point
    Each primary site supports up to 15 management points.

       Tip

      Don't install management points on servers that are across a slow link from
      the primary site server or the site database server. If the management point is

<!-- p.322 -->

        not in the same data center (also referred to as a fast link), you can experience
        latency on state and status messages. If you have a requirement for a remote
        management point, consider using a secondary site instead. This will avoid
        backlog issues for state and status messages.

     Each secondary site supports a single management point that must be installed on
     the secondary site server.

For information about the number of clients and devices that a management point can
support, see the Management points section.

  ７ Note

  If you enable the management point to support a cloud management gateway, it
  services internet-based client requests per normal. Sizing guidance for a
  management point doesn't change whether it services on-premises or internet-
  based clients.

Software update point
Use the following recommendations as a baseline. This baseline helps you determine the
information for the software updates capacity planning that is appropriate to your
organization. The actual capacity requirements might vary from the recommendations
listed in this article depending on the following criteria:

     Your specific networking environment
     The hardware that you use to host the software update point site system
     The number of managed clients
     The other site system roles installed on the server

  ７ Note

  If you enable the software update point to support a cloud management gateway,
  it services internet-based client requests per normal. Sizing guidance for a software
  update point doesn't change whether it services on-premises or internet-based
  clients.

Capacity planning for the software update point

<!-- p.323 -->

The number of supported clients depends on the version of Windows Server Update
Services (WSUS) that runs on the software update point. It also depends on whether the
software update point site system role coexists with another site system role:

     The software update point can support up to 25,000 clients when WSUS runs on
     the software update point server, and the software update point coexists with
     another site system role.

     The software update point can support up to 150,000 clients when a remote server
     meets WSUS requirements, WSUS is used with Configuration Manager, and you
     configure the following settings:

     IIS Application Pools:

        Increase the WsusPool Queue Length to 2000

        Increase the WsusPool Private Memory limit x4 times, or set to 0 (unlimited). For
        example, if the default limit is 1,843,200 KB, increase it to 7,372,800. For more
        information, see WSUS best practices.

        For more information about hardware requirements for the software update
        point, see Recommended hardware for site systems.

Capacity planning for software updates objects
Use the following capacity information to plan for software updates objects:

     Limit of 1000 software updates in a deployment -Limit the number of software
     updates to 1000 for each software update deployment. When you create an
     automatic deployment rule (ADR), specify criteria that limits the number of
     software updates. The ADR fails when the specified criteria returns more than 1000
     software updates. Check the status of the ADR from the Automatic Deployment
     Rules node in the Configuration Manager console. When you manually deploy
     software updates, don't select more than 1000 updates to deploy.

     Also limit the number of software updates to 1000 in a configuration baseline. For
     more information, see Create configuration baselines.

     Limit of 580 security scopes for automatic deployment rules - Limit the number
     of security scopes on automatic deployment rules (ADRs) to less than 580. When
     you create an ADR, the security scopes that have access to it are automatically
     added. If there are more than 580 security scopes set, the ADR will fail to run and
     an error is logged in ruleengine.log.

<!-- p.324 -->

SMS Provider
Each instance of the SMS Provider supports simultaneous connections from multiple
requests. The only limitations on these connections are the number of server
connections that are available to Windows, and the available resources on the server to
service the connection requests.

For more information, see Plan for the SMS Provider.

The administration service is a REST API on every instance of the SMS Provider. It
supports up to 5,000 requests per second, and 200 requests per client IP address.

Client numbers for sites and hierarchies
Use the following information to determine how many clients and which types of clients
you can support at a site or in a hierarchy.

Hierarchy with a central administration site
A central administration site supports a total number of devices that includes up to the
number of devices listed for the following three groups:

     700,000 Windows desktops. Also see support for embedded devices.

     25,000 devices that run macOS

     100,000 devices that you manage by using on-premises mobile device
     management (MDM)

For example, in a hierarchy you can support 700,000 desktops, up to 25,000 macOS
devices, and up to 100,000 devices managed by on-premises MDM. This hierarchy
supports a total of 825,000 devices.

  ） Important

  In a hierarchy where the central administration site uses a Standard edition of SQL
  Server, the hierarchy supports a maximum of 50,000 desktops and devices. To
  support more than 50,000 desktops and devices, you must use an Enterprise
  edition of SQL Server. This requirement applies only to a central administration site.
  It doesn't apply to a stand-alone primary site or a child primary site. The edition of
  SQL Server you use for a primary site doesn't limit its capacity to support the stated
  number of clients.

<!-- p.325 -->

The edition of SQL Server that is in use at a stand-alone primary site doesn't limit that
site's capacity to support up to the stated number of clients.

Child primary site
Each child primary site in a hierarchy with a central administration site supports the
following number of clients:

     150,000 total clients and devices that aren't limited to a specific group or type, as
     long as support doesn't exceed the number that is supported for the hierarchy.
     Also see, support for embedded devices.

For example, a primary site supports 25,000 macOS devices. That number is the limit for
a hierarchy. This primary site can then support an additional 125,000 desktop
computers. The total number of supported devices for the child primary site is the
supported maximum limit of 150,000.

Stand-alone primary site
A stand-alone primary site supports the following number of devices:

     175,000 total clients and devices, not to exceed:

        150,000 Windows clients. Also see, support for embedded devices.

        25,000 devices that run macOS

        50,000 devices that you manage by using on-premises MDM

For example, a stand-alone primary site that supports 150,000 desktops and 10,000
Macs can only support an additional 15,000 mobile devices managed by on-premises
MDM.

Primary sites and Windows Embedded devices
Primary sites support Windows Embedded devices that have File-Based Write Filters
(FBWF) enabled. When embedded devices don't have write filters enabled, a primary site
can support a number of embedded devices up to the allowed number of devices for
that site. When embedded devices have FBWF or Unified Write Filters (UWF) enabled, a
primary site can support a maximum of 10,000 Windows embedded devices. These
devices must be configured with the exceptions listed in the important note found in
the Planning for client deployment to Windows Embedded devices. A primary site

<!-- p.326 -->

supports only 3,000 Windows Embedded devices that have EWF enabled and that are
not configured for the exceptions.

Secondary sites
Secondary sites support the following number of devices:

     15,000 Windows clients

Management points
Each management point can support the following number of devices:

     25,000 total clients and devices, not to exceed:

        25,000 Windows clients

        One of the following (not both):

            10,000 devices that are managed by using on-premises MDM

            10,000 devices that run macOS

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.327 -->

Recommended hardware for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The following recommendations are guidelines to help you scale your Configuration
Manager environment to support more than a very basic deployment of sites, site
systems, and clients. They aren't intended to cover all possible site and hierarchy
configurations.

Use the information in the following sections as a guide to help you plan for hardware.
Make sure your hardware can meet the processing loads for clients and sites that use
the available Configuration Manager features.

Site systems
This section provides recommended hardware configurations for Configuration
Manager site systems. Use these recommendations to support the maximum number of
clients and use most or all Configuration Manager features. If your environment
supports less than the maximum number of clients, and doesn't use all available
features, it might require less resources. In general, the following key factors limit
performance of the overall system:

   1. Disk I/O performance

   2. Available memory

   3. CPU

For best performance, use RAID 10 configurations for all data drives and a 1-Gbps
Ethernet network.

Site servers

                                                                            ﾉ   Expand table

 Site configuration                          CPU         Memory       Memory allocation for
                                             (cores)     (GB)         SQL Server (%)

 Stand-alone primary site server with a      16          96           80

<!-- p.328 -->

 Site configuration                             CPU       Memory     Memory allocation for
                                                (cores)   (GB)       SQL Server (%)

 database site role on the same server Note 1

 Stand-alone primary site server with a         8         16         -
 remote site database

 Remote database server for a stand-alone       16        72         90
 primary site

 Central administration site server with a      20        128        80
 database site role on the same server Note 1

 Central administration site server with a      8         16         -
 remote site database

 Remote database server for a central           16        96         90
 administration site

 Child primary site with a database site role   16        96         80
 on the same server

 Child primary site server with a remote site   8         16         -
 database

 Remote database server for a child primary     16        72         90
 site

 Secondary site server                          8         16         -

Note 1: Collocated SQL
When you install the site server and SQL Server on the same computer, the deployment
supports the maximum sizing and scale numbers for sites and clients. This configuration
can limit high availability options, like using a SQL Server Always On failover cluster
instance. If you have a larger environment, because of the higher I/O requirements to
support both roles on the same computer, consider using a remote SQL Server.

Remote site system servers
The following guidance is for computers that hold a single site system role. Plan to
adjust when you install multiple site system roles on the same computer.

                                                                           ﾉ   Expand table

<!-- p.329 -->

 Site system role             CPU           Memory           Disk space (GB)
                              (cores)       (GB)

 Management point             4             8                50

 Distribution point           2             8                As required by the OS and to store content
                                                             that you deploy

 Software update point        8             16               As required by the OS and to store updates
 Note 2                                                      that you deploy

 All other site system        4             8                50
 roles

Note 2: WSUS configurations
The computer that hosts a software update point requires the following configurations
for IIS application pools:

      Increase the WsusPool Queue Length to 2000.

      Increase the WsusPool Private Memory limit by four times, or set it to 0
      (unlimited).

Disk space for site systems
Disk allocation and configuration contribute to the performance of Configuration
Manager. Because each Configuration Manager environment is different, the values that
you implement can vary from the following guidance.

For the best performance, place each object on a separate, dedicated RAID volume. For
all data volumes for Configuration Manager and its database files, use RAID 10 for the
best performance.

                                                                                      ﾉ      Expand table

 Data usage           Minimum           25,000     50,000     100,000    150,000     700,000 clients
                      disk space        clients    clients    clients    clients     (central
                                                                                     administration
                                                                                     site)

 Configuration        25 GB             50 GB      100 GB     200 GB     300 GB      200 GB
 Manager
 application and
 log files

<!-- p.330 -->

 Data usage        Minimum      25,000    50,000    100,000   150,000    700,000 clients
                   disk space   clients   clients   clients   clients    (central
                                                                         administration
                                                                         site)

 Site database     75 GB for    75 GB     150 GB    300 GB    500 GB     2 TB
 .mdf file         every
                   25,000
                   clients

 Site database     25 GB for    25 GB     50 GB     100 GB    150 GB     100 GB
 .ldf file         every
                   25,000
                   clients

 Temp database     As needed    As        As        As        As         As needed
 files (.mdf and                needed    needed    needed    needed
 .ldf)

For the Windows system disk, see sizing guidance for the installed OS version.

For content on distribution points, it depends upon your deployments. This guidance
doesn't include the disk space required for the content library on the site server or
distribution points. For more information, see The content library.

When you plan for disk space requirements, consider the following guidelines:

     Each client requires about 5-10 MB of space in the database. This number depends
     upon the hierarchy type, the configuration, and the number of clients. The size can
     be less for larger environments. Smaller sites have greater database usage per
     client.

     For the primary site's temp database, plan for a combined size that is 25% to 30%
     of the site database .mdf file. The actual size can be smaller or larger. It depends
     on the performance of the site server and the volume of incoming data over both
     short and long periods of time.

        ７ Note

        When you have 50,000 or more clients at a site, plan to use four or more temp
        database .mdf files.

     The temp database size for a central administration site is typically much smaller
     than for a primary site.

<!-- p.331 -->

     If you use SQL Server Express for the secondary site database, it limits the database
     size to 10 GB.

Clients
This section provides recommended hardware configurations for computers that you
manage by using Configuration Manager client software.

Client for Windows computers
The following minimum requirements are for Windows-based computers that you
manage by using Configuration Manager, including embedded editions:

     Processor and memory: Refer to the processor and RAM requirements for the OS.

     Disk space: 500 MB of available disk space, with 5 GB recommended for the
     Configuration Manager client cache. If you use customized settings to install the
     Configuration Manager client, less disk space is required.

        Use the client.msi property SMSCACHESIZE to set a cache size smaller than the
        default of 5120 MB. The minimum size is 1 MB. The following example creates a
        2-MB cache: CCMSetup.exe SMSCACHESIZE=2

        For more information, see About client installation properties.

           Tip

          Installing the client with minimal disk space is useful for Windows
          Embedded devices that typically have smaller disk sizes than standard
          Windows computers.

The following minimum hardware requirements are for optional functionality in
Configuration Manager:

     OS deployment: At least 384 MB of RAM

     Software Center: At least a 500-MHz processor

     Remote Control: For an optimal experience, at least a Pentium 4 Hyper-Threaded 3
     GHz (single core) or comparable CPU, with at least 1-GB RAM.

Configuration Manager console

<!-- p.332 -->

The following minimum hardware requirements apply to each computer that runs the
Configuration Manager console:

        Intel i3 or comparable CPU

        2 GB of RAM

        2 GB of disk space

                                                                       ﾉ   Expand table

 DPI setting                         Minimum resolution

 96 / 100%                           1024 x 768

 120 /125%                           1280 x 960

 144 / 150%                          1600 x 1200

 196 / 200%                          2500 x 1600

Lab deployments
Use the following minimum hardware recommendations for lab and test deployments of
Configuration Manager. These recommendations apply to all site types, up to 100
clients:

                                                                       ﾉ   Expand table

 Role                            CPU (cores)       Memory (GB)   Disk space (GB)

 Site and database server        2-4               8 - 12        100

 Site system server              1-4               2-4           50

 Client                          1-2               1-3           30

Next steps
Site size and performance guidelines

Site size and performance FAQ

<!-- p.333 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.334 -->

Configuration Manager site size and
performance guidelines
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager leads the industry in scale and performance. Other
documentation covers maximum supported scale limits and hardware guidelines for
running sites at the largest environment sizes. This article gives supplemental
performance guidance for environments of all sizes. This guidance can help you more
accurately estimate the hardware you need to deploy Configuration Manager.

This article focuses on the largest contributor to Configuration Manager performance
bottlenecks: the disk input/output subsystem or IOPS.

      Presents details and test results focused on IOPS
      Documents how to reproduce the tests with your own environments and hardware
      Suggests disk IOPS requirements for various size environments

Performance test methodology
You can deploy Configuration Manager in many unique ways, but it's important to
understand a few variables in any sizing discussions. One variable is feature interval,
such as an inventory cycle. Another variable is the number of users, software
deployments, or other objects the system references or deploys. Performance testing
applies these variables as part of a load. The load generates objects at a typical rate for
enterprise customers using production deployments in different size environments.

  ７ Note

  Customer usage data allows for testing current branch builds with the most
  common scenarios, configurations, and settings for most customers. The
  recommendations in this article are based on these averages. Your experiences may
  vary based on your environment size and configuration. In general, Configuration
  Manager requires common sense when it comes to objects and intervals. Just
  because you can collect every file on a system, or set the interval for a cycle to one
  minute, doesn't mean you should.

<!-- p.335 -->

The following sections highlight some key settings and configurations to use when
testing and modeling processing needs for large enterprises. These guidelines help set
basic system performance expectations for the suggested hardware sizes.

Feature intervals settings
Most testing should use default intervals for the key cycles in the system. For example,
hardware inventory testing occurs once per week with a larger than default .mof file.
Some recurring feature intervals, especially hardware and software inventory cycles, can
have significant effects on an environment's performance characteristics. Environments
that enable aggressive default intervals for data collection need oversized hardware in
direct proportion to the increase in activity. For example, say you have 25,000 desktop
clients and want to collect hardware inventory two times faster than the default interval.
Start by sizing your site's hardware as if you had 50,000 clients.

Objects
Tests should use the upper average of the objects that large enterprises tend to use with
the system. Typical values are thousands of collections and applications, which are
deployed to hundreds of thousands of users or systems. Tests should run simultaneously
on all objects in the system at these limits. Many customers use several features, but
don't generally use all features of the product at these upper limits. Testing with all
product features helps ensure the best possible system-wide performance, and allows a
buffer for features that some customers may use above average.

Loads
Tests should also run on greater than standard average day loads, by doing simulations
that generate peak usage demands on the system. One example is simulating Patch
Tuesday rollouts, to make sure the system can return update compliance data promptly
during these days of peak activity. Another example is simulating site activity during a
widespread malware outbreak, to ensure timely notification and response are possible.
Although deployed machines of the recommended size may be underused on any given
day, more extreme situations require some processing buffer.

Configurations
Run testing on a range of physical, Hyper-V, and Azure hardware, with a mixture of
supported operating systems and SQL Server versions. Always validate the worst cases
for the supported configuration. In general, Hyper-V and Azure return comparable

<!-- p.336 -->

performance results to equivalent physical hardware when configured similarly. Current
server operating systems tend to have performance that's equal to or better than earlier
OS versions. While all supported platforms meet the minimum requirements, usually the
latest versions of supporting products like Windows and SQL Server produce even
better performance.

The largest variation comes from the SQL Server versions in use. For more information
about SQL Server versions, see What version of SQL Server should I run?.

Key performance determinants
You can test and measure Configuration Manager performance with different kinds of
settings, in different ways, and at different site sizes. The following settings and objects
can dramatically affect performance. Be sure to consider them when testing and
modeling performance in your environment.

  Ｕ Caution

  While few aspects of Configuration Manager have official maximums or user
  interface limits that prevent excessive usage, going beyond the guidelines can have
  significant adverse effects on a site's performance. Exceeding recommended levels
  or ignoring sizing guidance typically requires larger hardware, and may render your
  environment unmaintainable until you reduce the frequency or count of various
  objects.

Hardware inventory
To test baseline performance, set hardware inventory collection to once per week, with
the default .mof file size plus approximately 20% other properties. Don't enable all
properties, and collect only properties you actually need. Pay special attention when
collecting properties, such as available virtual memory, that will always change with
every inventory cycle. Collecting these properties can cause excessive churn on every
inventory cycle from every client.

Software inventory
To test baseline performance, set software inventory collection to once per week, with
product only details. Collecting many files can place a significant strain on the inventory
subsystem. Avoid specifying filters that could end up collecting thousands of files across
many clients, such as *.exe or *.dll .

<!-- p.337 -->

Collections
Baseline performance testing can include several thousand collections with different
kinds of scope, size, complexity, and update settings. Site performance isn't a direct
function of the sheer number of collections on a site. Performance is also a cross-
product of collections' query complexity, full and incremental updates and change
frequency, dependencies among collections, and numbers of clients in the collections.

Where possible, minimize collections that have expensive or complicated dynamic rule
queries. For collections that require these types of rules, set appropriate update intervals
and update times to minimize the affect of collection re-evaluation on the system. For
example, update at midnight instead of 8:00 AM.

Enabling incremental updates on collections ensures quick and timely updates to
collection membership. But even though incremental updates are efficient, they still put
load on the system. Balance the change frequency you expect with the need for near
real-time updates on membership. For example, say you expect heavy churn in
collection members, but you don't require near real-time membership updates. It's more
efficient and produces less load on the system to update the collection with a scheduled
full update at some interval, than to enable incremental updates.

When you enable incremental updates, reduce any scheduled full updates on the same
collections. They're only a backup method of evaluation, since incremental updates
should keep your collection membership updated in near real time. Best practices for
collections recommends a maximum number of total collections for incremental
updates, but as the article points out, your experience can vary based on many factors.

Collections with only direct membership rules and with a limiting collection that isn't
doing incremental updates don't need scheduled full updates. Disable update schedules
for these types of collections to prevent unnecessary load on the system. If the limiting
collection uses incremental updates, collections with only direct membership rules may
not reflect membership updates for up to 24 hours, or until a scheduled refresh takes
place.

While not a best practice, some organizations create hundreds or even thousands of
collections as part of various business processes. If you use automation to create
collections, it's important to enable any needed incremental updates correctly. Minimize
and spread out any full update schedules to avoid hot spots of collection evaluation
during a single time period. Establish a regular grooming process to delete unused
collections, especially if you automatically create collections that you no longer need
after some time.

<!-- p.338 -->

Remember that Configuration Manager creates policies for all objects in your collections
when you target tasks like deployments to them. Membership changes, either through
scheduled refresh or incremental updates, can create much more work for the whole
system. The latest current branch builds have special policy optimizations for the All
Systems and All Users collections. When targeting your entire enterprise, use the built-in
collections instead of a clone of these built-in collections.

To investigate collection performance even deeper, view collection evaluation in the
console. For more information, see How to view collection evaluation.

Discovery methods
For baseline performance testing, run server-based discovery methods once a week,
enabling delta discovery as appropriate to keep the data fresh during the week. The
tests should discover an object quantity proportional to the simulated enterprise size.
The performance baseline test for heartbeat discovery should also run once a week.

Discovery data is global data. A common performance-related problem is to
misconfigure server-based discovery methods in a hierarchy, causing duplicate
discovery of the same resources from multiple primary sites. Carefully configure
discovery methods to optimize communication with the target service, such as Active
Directory domain controllers, while avoiding duplication of the same discovery scope on
multiple primary sites.

General sizing guidelines
Based on the preceding performance test methodology, the following table gives
general minimum hardware requirement guidelines for specific numbers of managed
clients. These values should allow most customers with the specified number of clients
to process objects fast enough to administer the specified site. Computing power
continues to decrease in price every year, and some of the requirements below are small
for modern server hardware configurations. Hardware that exceeds the following
guidelines proportionally increases performance for sites that require more processing
power, or have special product usage patterns.

                                                                         ﾉ   Expand table

<!-- p.339 -->

Desktop   Site            Cores    Memory   SQL Server   IOPS:     IOPS:    Storage
clients   type/role       Note 1   (GB)     memory       Inboxes   SQL      space
                                            allocation   Note 3    Server   required
                                            Note 2                 Note 3   (GB) Note 4

25k       Primary or      6        24       65%          600       1700     350
          CAS with
          database site
          role on the
          same server

25k       Primary or      4        8                     600                100
          CAS

          Remote SQL      4        16       70%                    1700     250
          Server

50k       Primary or      8        32       70%          1200      2800     600
          CAS with
          database site
          role on the
          same server

50k       Primary or      4        8                     1200               200
          CAS

          Remote SQL      8        24       70%                    2800     400
          Server

100k      Primary or      12       64       70%          1200      5000     1100
          CAS with
          database site
          role on the
          same server

100k      Primary or      6        12                    1200               300
          CAS

          Remote SQL      12       48       80%                    5000     800
          Server

150k      Primary or      16       96       70%          1800      7400     1600
          CAS with
          database site
          role on the
          same server

150k      Primary or      8        16                    1800               400

<!-- p.340 -->

 Desktop    Site            Cores    Memory   SQL Server    IOPS:     IOPS:     Storage
 clients    type/role       Note 1   (GB)     memory        Inboxes   SQL       space
                                              allocation    Note 3    Server    required
                                              Note 2                  Note 3    (GB) Note 4

            CAS

            Remote SQL      16       72       90%                     7400      1200
            Server

 700k       CAS with        20+      128+     80%           1800+     9000+     5000+
            database site
            role on the
            same server

 700k       CAS             8+       16+                    1800+               500+

            Remote SQL      16+      96+      90%                     9000+     4500+
            Server

 5k         Secondary       4        8                      500       -         200
            Site

 15k        Secondary       8        16                     500       -         300
            Site

Notes on general sizing guidelines

Note 1: Cores

Configuration Manager runs many simultaneous processes, so needs a certain minimum
number of CPU cores for various site sizes. While cores get faster each year, it's
important to ensure that a certain minimum number of cores work in parallel. In general,
any server-level CPU produced after 2015 meets the basic performance needs for the
cores specified in the table. Configuration Manager takes advantage of other cores
beyond the recommendations. Once you have the minimum suggested cores, prioritize
CPU resource investment to increase the speed of existing cores. Don't add more, slower
cores. For example, Configuration Manager has better performance on key processing
tasks with 16 fast cores than with 24 slower cores. This performance assumes that there
are enough other system resources like disk IOPS.

The relationship between cores and memory is also important. In general, having less
than 3-4 GB of RAM per core reduces the total processing capability on your SQL

<!-- p.341 -->

Servers. You need more RAM per core when SQL Server is colocated with the site server
components.

  ７ Note

  All testing sets machine power plans to allow maximum CPU power consumption
  and performance.

Note 2: SQL Server memory allocation
Use this value to configure the Maximum server memory (in MB) in the properties of
the SQL Server. It's the percentage of the total amount of memory available on the
server.

Don't configure the minimum and maximum values the same. This guidance is
specifically for the maximum memory that you should allow SQL Server to allocate.

Note 3: IOPS: Inboxes and IOPS: SQL

These values refer to the IOPS needs for the Configuration Manager and SQL Server
logical drives. The IOPS: Inboxes column shows the IOPS requirements for the logical
drive with the Configuration Manager inbox directories. The IOPS: SQL column shows
the total IOPS needs for the logical drive(s) that various SQL Server files use. These
columns are different because the two drives should have different formatting. For more
information and examples on suggested SQL Server disk configurations and file best
practices, including details on splitting files across multiple volumes, see the Site sizing
and performance FAQ.

Both of these IOPS columns use data from the industry-standard tool, Diskspd. See How
to measure disk performance for instructions on duplicating these measurements. In
general, once you meet basic CPU and memory requirements, the storage subsystem
has the largest affect on site performance, and improvements here will give the most
payback on investment.

Note 4: Storage space required
These real-world values may differ from other documented recommendations. We
provide these numbers only as a general guideline; individual requirements could vary
widely. Carefully plan for disk space needs before site installation. Assume that some
amount of this storage remains as free disk space most of the time. You may use this

<!-- p.342 -->

buffer space in a recovery scenario, or for upgrade scenarios that need free disk space
for setup package expansion. Your site may require more storage for large amounts of
data collection, longer periods of data retention, and large amounts of software
distribution content. You can also store these items on separate, lower-throughput
volumes.

How to measure disk performance
You can use the industry-standard tool Diskspd to provide standardized suggestions for
the IOPS that various-sized Configuration Manager environments require. While not
exhaustive, the following test steps and command lines provide a simple and
reproducible way to estimate your servers' disk subsystem throughput. You can compare
your results to the minimum recommended IOPS in the general sizing guidelines table.

For test results from different kinds of hardware configurations in lab environments, see
Example disk configurations. You can use the data for a rough starting point when
designing the storage subsystem for a new environment from scratch.

How to test disk IOPS
   1. Download the Diskspd utility   .

   2. Make sure you have at least 100 GB of free disk space. Disable any apps that might
     interfere or cause extra load on the disk, such as active antivirus scanning of the
     directory, SQL, or SMSExec.

   3. Run Diskspd from an elevated command prompt.

     Run the tool twice in sequence for the volume that you want to test. The first test
     at 64k size with random write operations for one minute. This test validates
     controller cache loading and disk space allocation, in case the volume is
     dynamically expanding. Discard the results of the first test. The second test should
     immediately follow the first test, and do the same load for five minutes.

     For example, use the following specific command lines to test the G: volume.

       Command

        DiskSpd.exe -r -w100 -t8 -o8 -b64K -c100G -d60 -h -L
        G:\\test\testfile.dat

        del G:\\test\testfile.dat

<!-- p.343 -->

        DiskSpd.exe -r -w100 -t8 -o8 -b64K -c100G -d300 -h -L
        G:\\test\testfile.dat

   4. Review the output from the second test to find the total IOPS in the I/O per s
     column. In the following example, the total IOPS are 3929.18.

       Output

        Total IO
        | thread | bytes       | I/Os    | MB/s | I/O per s | AvgLat |
        LatStdDev |
        |--------|-------------|---------|--------|-----------|--------|-------
        ----|
        |   1    | 9651814400 | 147275 | 30.68 |       490.92 | 16.294 | 10.210
        |
        |   2    | 9676652544 | 147654 | 30.76 |       492.18 | 16.252 | 9.998
        |
        |   3    | 9638248448 | 147068 | 30.64 |       490.23 | 16.317 | 10.295
        |
        |   4    | 9686089728 | 147798 | 30.79 |       492.66 | 16.236 | 10.072
        |
        |   5    | 9590931456 | 146346 | 30.49 |       487.82 | 16.398 | 10.384
        |
        |   6    | 9677242368 | 147663 | 30.76 |       492.21 | 16.251 | 10.067
        |
        |   7    | 9637330944 | 147054 | 30.64 |       490.18 | 16.319 | 10.249
        |
        |   8    | 9692577792 | 147897 | 30.81 |       492.99 | 16.225 | 10.125
        |
        | Total: | 77250887680 | 1178755 | 245.57 |   3929.18 | 16.286 | 10.176
        |

Example disk configurations
The following tables show results from running the test steps in How to measure disk
performance with various test lab configurations. Use this data for a rough starting point
when designing the storage subsystem for a new environment from scratch.

Physical machines and Hyper-V
Hardware is always improving. Expect newer generations of hardware and different
hardware combinations, like SSDs and SANs, to exceed the performance stated below.
These results are a basic starting point to consider when designing a server or
discussing with your hardware vendor.

<!-- p.344 -->

The following table shows the test results across various disk subsystems, including
spindle and SSD-based hard drives, in various test lab configurations. All configurations
format the disks with 64k clusters and attach them to an enterprise class disk controller.
In addition to the RAID array disk count, they each have at least one spare disk.

                                                                           ﾉ     Expand table

 Disk type     Disk count, not including +1 spare disk          RAID     IOPS measured

 15k SAS       2                                                1        620

 15k SAS       4                                                10       1206

 15k SAS       6                                                10       1751

 15k SAS       8                                                10       2322

 15k SAS       10                                               10       2882

 15k SAS       12                                               10       3476

 15k SAS       16                                               10       4236

 15k SAS       20                                               10       5148

 15k SAS       30                                               10       7398

 15k SAS       40                                               10       9913

 SSD SATA      2                                                1        3300

 SSD SATA      4                                                10       5542

 SSD SATA      6                                                10       7201

 SSD SAS       2                                                1        7539

 SSD SAS       4                                                10       14346

 SSD SAS       6                                                10       15607

The following table lists the specific devices used in this example. This information isn't a
recommendation for any specific hardware model or manufacturer.

                                                                           ﾉ     Expand table

 Disk type          Model               RAID controller    Cache memory and configuration

 15k RPM SAS HD     HP EH0300JDYTH      Smart Array P822   2 GB, 20% Read / 80% Write

<!-- p.345 -->

 Disk type        Model               RAID controller     Cache memory and configuration

 SSD SATA         ATA MK0200GCTYV     Smart Array P420i   1 GB, 20% Read / 80% Write

 SSD SAS          HP MO0800 JEFPB     Smart Array P420i   1 GB, 20% Read / 80% Write

Azure machine and disk performance
Azure disk performance depends on several factors, such as the size of the Azure VM,
and the number and type of disks it uses. Azure is also constantly adding new machine
types and disk speeds that are different from the following chart. For more information
about Configuration Manager running on Azure, and additional information on
understanding disk I/O on Azure, see Configuration Manager on Azure frequently asked
questions.

All disks are formatted NTFS 64k cluster size, and rows with more than one disk are
configured as striped volumes via the Windows Disk Management utility.

                                                                          ﾉ    Expand table

 Azure VM        Azure       Disk        Available         IOPS               Limiting
                 disk        count       space             measured           factor

 DS2/DS11        P20         1           512 GB            965                Azure VM size

 DS2/DS11        P20         2           1024 GB           996                Azure VM size

 DS2/DS11        P30         1           1024 GB           996                Azure VM size

 DS2/DS11        P30         2           2048 GB           996                Azure VM size

 DS3/DS12/F4S    P20         1           512 GB            1994               Azure VM size

 DS3/DS12/F4S    P20         2           1024 GB           1992               Azure VM size

 DS3/DS12/F4S    P30         1           1024 GB           1993               Azure VM size

 DS3/DS12/F4S    P30         2           2048 GB           1992               Azure VM size

 DS4/DS13/F8S    P20         1           512 GB            2334               P20 disk

 DS4/DS13/F8S    P20         2           1024 GB           3984               Azure VM size

 DS4/DS13/F8S    P20         3           1536 GB           3984               Azure VM size

 DS4/DS13/F8S    P30         1           1024 GB           3112               P30 disk

 DS4/DS13/F8S    P30         2           2048 GB           3984               Azure VM size

<!-- p.346 -->

 Azure VM         Azure            Disk       Available   IOPS             Limiting
                  disk             count      space       measured         factor

 DS4/DS13/F8S     P30              3          3072 GB     3996             Azure VM size

 DS5/DS14/F16S    P20              1          512 GB      2335             P20 disk

 DS5/DS14/F16S    P20              2          1024 GB     4639             P20 disk

 DS5/DS14/F16S    P20              3          1536 GB     6913             P20 disk

 DS5/DS14/F16S    P20              4          2048 GB     7966             Azure VM size

 DS5/DS14/F16S    P30              1          1024 GB     3112             P30 disk

 DS5/DS14/F16S    P30              2          2048 GB     6182             P30 disk

 DS5/DS14/F16S    P30              3          3072 GB     7963             Azure VM size

 DS5/DS14/F16S    P30              4          4096 GB     7968             Azure VM size

 DS15             P30              1          1024 GB     3113             P30 disk

 DS15             P30              2          2048 GB     6184             P30 disk

 DS15             P30              3          3072 GB     9225             P30 disk

 DS15             P30              4          4096 GB     10200            Azure VM size

For more information on the currently available disks, see Select a disk type for Azure
IaaS VMs.

See also
     Site sizing and performance FAQ
     Configuration Manager on Azure frequently asked questions
     Size and scale numbers
     Recommended hardware

Feedback
Was this page helpful?      Yes        No

Provide product feedback

<!-- p.347 -->

Configuration Manager site sizing and
performance FAQ
Applies to: Configuration Manager (current branch)

This document addresses frequently asked questions about Configuration Manager site sizing
guidance and common performance issues.

Machine and disk configuration
How should I format the disks on my site server and
SQL Server?
Separate the Configuration Manager inboxes and SQL Server files on at least two different
volumes. This separation lets you optimize cluster allocation sizes for the different kinds of I/O
they perform.

For the volume hosting your sites server inboxes, use NTFS with 4K or 8K allocation units. ReFS
writes 64k even for small files. Configuration Manager has many small files, so ReFS can produce
unnecessary disk overhead.

For disks containing SQL Server database files, use either NTFS or ReFS formatting, with 64K
allocation units.

How and where should I lay out my SQL Server
database files?
Modern arrays of solid-state drives (SSD) and Azure Premium Storage can provide high IOPS on a
single volume, with few disks. You typically add more drives to an array for additional storage, not
additional throughput. If you're using physical spindle-based disks, you may need more IOPS
than you can generate on a single volume. You should allocate 60% of the total recommended
IOPS and disk space for the .mdf file, 20% for the .ldf file, and 20% for the log and data temp files.
The .ldf and temp files can all reside on a single volume with 40% (20% + 20%) of your allocated
IOPS.

<!-- p.348 -->

SQL Server versions earlier than SQL Server 2016 created by default only one temp data file. You
should create more, to avoid SQL Server locks and waiting for access to a single file. Community
opinions vary on the best number of temp data files to create, from four to eight. Testing reveals
little difference between four to eight, so you can create four equally sized temp data files. Your
tempdb data files should be up to 20-25% the size of your full database.

Are there any other recommendations for disk setup?
When configurable, set RAID controller memory to 70% allocation for write operations and 30%
for read operations. In general, use a RAID 10 array configuration for the site database. RAID 1 is
also acceptable for small-scale sites with low I/O requirements, or if you use fast SSDs. With
larger disk arrays, configure spare disks to automatically replace failing disks.

Example: Physical machine with physical disks

Sizing guidelines for a colocated site server and SQL Server with 100,000 clients are 1200 IOPS for
site server inboxes and 5000 IOPS for SQL Server files.

Your resulting disk configuration might look like:

                                                                                        ﾉ   Expand table

   Drives1      RAID       Format        Volume              Minimum IOPS           Approx. IOPS
                                         contents            needed                 supplied2

   2x10k        1          -             Windows                                    -

   6x15k        10         NTFS 8k       ConfigMgr           1700                   1751
                                         inboxes

   12x15k       10         64k           SQL .mdf            60%*5000 =             3476
                           ReFS                              3000

   8x15k        10         64k           SQL .ldf, temp      40%*5000 =             2322
                           ReFS          files               2000

   1. Doesn't include recommended spare disks.
   2. This value is from Example disk configurations.

<!-- p.349 -->

I use Hyper-V on Windows Server. How should I
configure the disks for my Configuration Manager
VMs for best performance?
Hyper-V delivers similar performance to a physical server, if hardware resources (CPU cores and
pass-through storage) are 100% dedicated to the virtual machine (VM). Using fixed-size .vhd or
.vhdx disk files causes a minimal 1-5% I/O performance impact. Using dynamically expanding .vhd
or .vhdx disk files causes up to 25% I/O performance impact for the Configuration Manager
workload. If you need dynamically expanding disks, compensate by adding an additional 25%
IOPS performance to the array.

When running your Configuration Manager site server or SQL Server inside a VM, isolate the
Hyper-V host OS drives from the VM OS and data drives.

For more information about optimizing VMs, see Performance Tuning Hyper-V Servers.

Example: Hyper-V VM-based site server

Sizing guidelines for a colocated site server and SQL Server with 150,000 clients are 1800 IOPS for
site server inboxes and 7400 IOPS for SQL Server files.

Your resulting disk configuration might look like:

                                                                                  ﾉ   Expand table

   Drives1      RAID       Format2       Volume contents      Minimum             Approx. IOPS
                                                              IOPS needed         supplied3

   2x10k        1          -             Hyper-V host OS      -                   -

   2x10k        1          -             (VM) site server     -                   -
                                         OS

   2xSSD        1          NTFS 8k       (VM) ConfigMgr       1800                7539
   SAS                                   inboxes

   4xSSD        10         64k           (VM) Host SQL        7400                14346
   SAS                     ReFS          Server (all files)

   1. Doesn't include recommended spare disks.

<!-- p.350 -->

   2. Fixed-size, pass-through .vhdx for the VM drive dedicated to the underlying volume.
   3. This value is from Example disk configurations.

Are there any suggestions for Configuration Manager
environments in Microsoft Azure?
Start by reading the Configuration Manager on Azure frequently asked questions.

Azure infrastructure as a service (IaaS) VMs that leverage Premium Storage-based disks can have
high IOPS. On these VMs, configure additional disks for anticipated disk space needs, rather than
for additional IOPS.

Azure storage is inherently redundant and doesn't require multiple disks for availability. You can
stripe disks in Disk Manager or Storage Spaces to provide additional space and performance.

For more information and recommendations on how to maximize Premium Storage performance
and run SQL Servers in Azure IaaS VMs, see:

     Optimize application performance

     Disks guidance

Example: Azure-based site server

Sizing guidelines for a colocated site server and SQL Server with 50,000 clients are 8 cores, 32 GB,
and 1200 IOPS for site server inboxes, and 2800 IOPS for SQL Server files.

Your resulting Azure machine might be a DS13v2 (8 cores, 56 GB) with the following disk
configuration:

                                                                                   ﾉ   Expand table

   Drives              Format      Contains             Minimum IOPS           Approx. IOPS
                                                        needed                 supplied1

   <standard>          -           Site server OS       -                      -

   1xP20 (512          NTFS 8k     ConfigMgr            1200                   2334
   GB)                             inboxes

<!-- p.351 -->

  Drives             Format        Contains             Minimum IOPS           Approx. IOPS
                                                        needed                 supplied1

  1xP30 (1024        64k           SQL Server (all      2800                   3112
  GB)                ReFS          files2)

   1. This value is from Example disk configurations.
   2. Azure guidance allows for placing the TempDB on the local, SSD-based D: drive, given it
     won't exceed available space and allows for additional disk I/O distribution.

Example: Azure-based site server (for instant performance increase)

Azure disk throughput is limited by the size of the VM. The configuration in the preceding Azure
example may limit future expansion or additional performance. If you add additional disks during
initial deployment of your Azure VM, you can upsize your Azure VM for increased processing
power in the future, with minimal upfront investment. It's much simpler to plan ahead to increase
site performance as requirements change, instead of later needing to do a more complicated
migration.

Change the disks in the preceding Azure example to see how the IOPS change.

DS13v2

                                                                                     ﾉ   Expand table

  Drives1            Format        Contains             Minimum IOPS           Approx. IOPS
                                                        needed                 supplied2

  <standard>         -             Site server OS       -                      -

  2xP20 (1024        NTFS 8k       ConfigMgr            1200                   3984
  GB)                              inboxes

  2xP30 (2048        64k           SQL Server (all      2800                   3984
  GB)                ReFS          files3)

   1. Disks are striped using Storage Spaces.
   2. This value is from Example disk configurations. VM size limits performance.

<!-- p.352 -->

   3. Azure guidance allows for placing the TempDB on the local, SSD-based D: drive, given it
     won't exceed available space and allows for additional disk I/O distribution.

If you need more performance in future, you can upsize your VM to a DS14v2, which doubles
CPU and memory. The additional disk bandwidth allowed by that VM size also instantly boosts
the available disk IOPS on your previously configured disks.

DS14v2

                                                                                     ﾉ   Expand table

   Drives1          RAID        Format                Contains   Minimum             Approx. IOPS
                                                                 IOPS needed         supplied2

   <standard>       -           Site server           -          -
                                OS

   2xP20 (1024      NTFS        ConfigMgr             1200       4639
   GB)              8k          inboxes

   2xP30 (2048      64k         SQL Server            2800       6182
   GB)              ReFS        (all files3)

   1. Disks are striped using Storage Spaces.
   2. This value is from Example disk configurations. VM size limits performance.
   3. Azure guidance allows for placing the TempDB on the local, SSD-based D: drive, given it
     won't exceed available space and allows for additional disk I/O distribution.

SQL Server performance
Is it better to run with SQL Server colocated with the
site server, or run it on a remote server?
Both can perform adequately, assuming the single server is appropriately sized, or network
connectivity is sufficient between the two servers.

Remote SQL Server requires the upfront and operational cost of an additional server, but is
typical among the majority of large-scale customers. Benefits of this configuration include:

<!-- p.353 -->

     Increased site availability options, such as SQL Server Always On
     Ability to run heavy reporting with less overheard to site processing
     Simpler disaster recovery in some situations
     Easier security management
     Role separation for SQL Server management, such as with a separate DBA team

Colocated SQL Server requires a single server, and is typical for most small-scale customers.
Benefits of this configuration include:

     Lower costs for machines, licenses, and maintenance
     Fewer points of failure in the site
     Better control for planning downtime

How much RAM should I allocate for SQL?
By default, SQL Server uses all available memory on your server, potentially starving the OS and
other processes on the machine. To avoid potential performance issues, it's important to allocate
memory to SQL Server explicitly. On site servers colocated with SQL Server, make sure the OS has
enough RAM for file caching and other operations. Make sure there's enough RAM remaining for
SMSExec and other Configuration Manager processes. When running SQL Server on a remote
server, you can allocate the majority of the memory to SQL, but not all. Review the sizing
guidelines for initial guidance.

SQL Server memory allocation should be rounded to whole GB. Also, as RAM increases to large
amounts, you can let SQL Server have a higher percentage. For example, when 256 GB or more of
RAM is available, you can configure SQL Server for up to 95%, as that still preserves plenty of
memory for the OS. Monitoring the page file is a good way to ensure there is enough memory
for the OS and any Configuration Manager processes.

Cores are cheap these days. Should I just add a bunch
of them to my SQL Server?
You may run into memory contention issues if there are more than 16 physical cores and not
enough RAM on your SQL Server. The Configuration Manager workload performs better when at
least 3-4 GB of RAM per core is available for SQL. When adding cores to your SQL Server, be sure
to increase RAM in proportional amounts.

<!-- p.354 -->

Will a SQL Server Always On availability group impact
my performance?
In general, availability groups have negligible effect on performance of the system when
sufficient networking is available between the replica servers. You can have rapid database log .ldf
file growth in a busy availability group environment. However, log file space is automatically
released after a successful database backup. Add a SQL Server job for the Configuration Manager
database to perform a backup, for example every 24 hours, and an .ldf backup every six hours.
For more information about availability groups and Configuration Manager, including more
about SQL Server backup strategies, see Prepare to use a SQL Server Always On availability
group.

Should I enable SQL Server compression on
my database?
SQL Server compression isn't recommended for the Configuration Manager database. While
there are no functional issues with enabling compression on a Configuration Manager database,
test results don't show much size savings compared to the potential sizable performance impact
to the system.

Should I enable SQL Server encryption on
my database?
Any secrets in the Configuration Manager database are already stored securely, but adding SQL
Server encryption can add yet another layer of security. There are no functional issues with
enabling encryption on your database, but there can be up to a 25% performance degradation.
Therefore, encrypt with caution, especially in large-scale environments. Also remember to update
your backup and recovery plans to ensure you can successfully recover the encrypted data.

What version of SQL Server should I run?
For supported versions of SQL, see Support for SQL Server versions. From a performance
standpoint, all supported versions of SQL Server meet required performance criteria. Upgrading
SQL Server in place doesn't update compatibility levels.

If you see unusual timeouts or slowness on certain SQL queries on SQL Server 2016 or later, such
as when using RBAC in the Admin Console, try changing the SQL Server compatibility level on the

<!-- p.355 -->

Configuration Manager database to 110. Running at SQL Server compatibility level 110 on SQL
Server 2014 and newer versions of SQL Server is fully supported. For more information, see SQL
query times out or console slow on certain Configuration Manager database queries.

As of January 2018, you should avoid the following SQL Server versions, because of various
known performance-related or other potential issues:

     SQL Server 2012 SP3 CU1 to CU5
     SQL Server 2014 SP1 CU6 to SP2 CU2
     SQL Server 2016 RTM to CU3, SP1 CU3 to CU5

Should I implement any additional SQL Server
maintenance tasks?
The built-in "Rebuild Indexes" maintenance task rebuilds only highly fragmented indexes. The
Query Optimizer then updates statistics on related objects as described in After Maintenance
Operations section in SQL documentation. Therefore, if you rely solely on this built-in task,
statistics may not be updated on some tables and views, leading to suboptimal query plans and
poor performance.

You should perform index maintenance as often as once a week and update statistics of tables
and views as often as once a day to maintain SQL Server performance.

There is no one-size-fits-all approach to database maintenance. The optimal strategy depends on
factors such as database size, workload characteristics, and operational requirements. Engaging
an in-house SQL Server expert or a Microsoft Cloud Solution Architect (CSA) can help you design
the maintenance strategy tailored to your environment.

Additional guidance is available from the Configuration Manager and SQL Server communities,
including non-Microsoft maintenance scripts. The SQL Recommendations for MECM
whitepaper summarizes Microsoft CSAs' field experience on SQL maintenance and tuning.

In large sites, some database tables, such as CI_CurrentComplianceStatusDetails, HinvChangeLog,
might be large, depending on your usage patterns. You may need to reduce or alter your
approach to maintain these one by one.

When should I use full SQL Server instead of SQL
Server Express on my secondary sites?

<!-- p.356 -->

SQL Server Express doesn't have any significant performance implications on secondary sites, and
it's adequate for most customers. It's also easy to deploy and manage, and is the recommended
configuration for nearly all customers at any size.

There's one situation where a full SQL Server installation might be needed. If you have a large
number of distribution points and packages or sources in your environment, it's possible to
exceed the 10-GB size limit of SQL Server Express. If the number of packages times the number of
distribution points is more than 4,000,000, such as 2,000 DPs with 2,000 pieces of content,
consider using full SQL Server at your secondary sites.

Should I change MaxDOP settings on my database?
Leaving your setting at 0 (use all available processors) is optimal for overall processing
performance in most circumstances.

Many Configuration Manager administrators follow the guidance at Recommendations and
guidelines for the "max degree of parallelism" configuration option in SQL Server. On most
modern large hardware, this guidance leads to a suggested maximum setting of eight. However,
if you run many smaller queries compared to your number of processors, it may help to set it to a
higher number. Limiting yourself to eight isn't necessarily the best setting on larger sites when
more cores are available.

On SQL Servers with greater than eight cores, start with a setting of 0, and only make changes if
you experience performance issues or excessive locking. If you need to change MaxDOP because
you are encountering performance issues at 0, start with a new value at least greater than or
equal to the minimum recommended number of cores for that site's SQL Server sizing. Going
lower than this value nearly always has negative performance implications. For example, a remote
SQL Server for a 100,000 client site needs at least 12 cores. If your SQL Server has 16 cores, start
testing your MaxDOP setting with a value of 12.

Anti-malware configuration
Which folders on the site server (or other roles)
should I exclude for antivirus software?
Take care when disabling antivirus protection on any system. In high volume and secure
environments, we recommend disabling active monitoring for optimum performance.

<!-- p.357 -->

For more information about recommended antivirus exclusions, see Recommended antivirus
exclusions for Configuration Manager site servers, site systems, and clients.

WSUS Maintenance
What can I do to make WSUS perform better when
it's used with Configuration Manager?
Changing a few key IIS settings, such as WsusPool Queue Length and WsusPool Private Memory
limit, can improve WSUS performance, even on smaller installations. For more information, see
WSUS note at Recommended hardware.

Also make sure you have the latest updates installed for the operating system running WSUS:

     Windows Server 2012: Any non "Security only" cumulative update released October 2017 or
     later. (KB4041690   )
     Windows Server 2012 R2: Any non "Security only" cumulative update released August 2017
     or later. (KB4039871    )
     Windows Server 2016: any non "Security only" cumulative update released August 2017 or
     later. (KB4039396   )

What type of maintenance should I run on my
WSUS servers?
See The complete guide to Microsoft WSUS and Configuration Manager SUP maintenance.

I want to set up basic performance monitoring for my
site. What should I watch?
Traditional server performance monitoring works effectively for general Configuration Manager.
You can also leverage monitoring solutions like the Azure Monitor to monitor basic health of your
servers: see ConfigMgr Performance Baseline the Easy Way       blog post. You can also directly
monitor the Windows Performance Monitor (PerfMon) counters Configuration Manager provides.
Monitor the backlogs in the various inboxes for early warning signs of potential site performance
issues or backlogs.

See also

<!-- p.358 -->

     Site sizing and performance guidelines
     Configuration Manager on Azure frequently asked questions

Last updated on 04/07/2026

<!-- p.359 -->

Choose a device management solution
Article • 03/31/2023

Microsoft offers different solutions for managing PCs, servers, and devices. These
solutions are available on-premises, cloud-based, or a combination of both. Choose the
solution that's right for the business requirements of your organization. Base your
decision on the device platforms you need to manage and the management
functionality you need.

Overview
There are several Microsoft solutions that might work best for you in different scenarios.
You don't need to choose just one.

      For a small organization, a tool like the Windows administration center may be a
      great fit.
      Approximately 75% of IT organizations use Configuration Manager to manage
      their devices.
      Microsoft Azure provides various solutions from the cloud or on-premises with
      Azure Arc and Azure Stack that primarily target server management.
      Microsoft Intune provides cloud management of clients.
      You can combine Configuration Manager and Intune with co-management.
      You can use Security Management for Microsoft Defender for Endpoint (MDE) to
      manage security settings for devices utilizing Microsoft Defender for Endpoint.

Use the following table to help compare these management technologies:

                                                                             ﾉ   Expand table

                   Cloud-only        Cloud-attached      On-premises         Disconnected

 Hyper-V           Not applicable    - Azure Stack       - Azure Stack       - Azure Stack
 host                                - Windows Admin     - Windows Admin     - Windows
                                     Center              Center              Admin Center
                                     - Security          - Virtual Machine   - Virtual Machine
                                     Management for      Manager             Manager
                                     MDE
                                     - Virtual Machine
                                     Manager

 Windows           - Azure Arc       - Azure Arc         - Azure Arc         Configuration
 Server            - Configuration   - Configuration     - Configuration     Manager
                   Manager           Manager             Manager

<!-- p.360 -->

                Cloud-only         Cloud-attached    On-premises        Disconnected

                - Security         - Security
                Management for     Management for
                MDE                MDE

 Linux Server   Azure Arc          Azure Arc         Azure Arc

 Windows        - Intune           - Intune          - Intune           Configuration
 10/11          - Configuration    - Configuration   - Configuration    Manager
                Manager            Manager           Manager
                - Security         - Security        - Security
                Management for     Management for    Management for
                MDE                MDE               MDE

 Windows 7      Configuration      Configuration     Configuration      Configuration
 or 8.1         Manager            Manager           Manager            Manager

 Azure          Configuration      Not applicable    Not applicable     Not applicable
 Virtual        Manager
 Desktop

For more information, see the following articles:

     What is Azure Stack?
     What is Windows Admin Center?
     What is Virtual Machine Manager?
     Azure Arc products
     What is Azure Virtual Desktop?
     Security Management for Microsoft Defender for Endpoint (MDE)

For more information on the Configuration Manager and Intune solutions, continue to
the next section.

Client management
This section compares the following four client management solutions:

     Configuration Manager client
     Co-management with Microsoft Intune
     Microsoft Exchange

You can use these solutions by themselves or in combination with each other. For
example, use the client-based management approach to manage the computers and
servers in your organization, and also use co-management to manage internet-based
