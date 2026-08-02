---
title: "Core infrastructure documentation — pages 401-440"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0401-0440
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0401-0440
family: sccm
documentKind: "doc"
abstract: "Prestaged content: Transferring content to a distribution point without distributing the content across the network. Scheduling and throttling: Configurations that help you control when and how content is distributed to distribution points. For more information, see Manage netwo"
---

# Core infrastructure documentation — pages 401-440

<!-- p.401 -->

     Prestaged content: Transferring content to a distribution point without distributing
     the content across the network.

     Scheduling and throttling: Configurations that help you control when and how
     content is distributed to distribution points.

For more information, see Manage network bandwidth.

Network connection speed to content source
Several things have changed with Configuration Manager current branch in the way that
clients find a distribution point that has content. These changes include the network
speed to a content source.

Network connection speeds that define a distribution point as Fast or Slow are no
longer used. Instead, each site system that's associated with a boundary group is treated
the same.

For more information, see Boundary groups.

On-demand content distribution
On-demand content distribution is an option for individual applications and packages.
This option enables on-demand content distribution to preferred servers.

     To enable On-Demand content distribution for a package/application, do the
     following :

        In the Distribution Point properties, inside the Boundary Groups tab, select :
        Enable for on-demand distribution.

        Inside the distribution settings tab for package/application properties, select :
        Enable for on-demand distribution.

     When you enable this option for a deployment, and a client requests that content
     but the content isn't available on any of the client's preferred distribution points,
     Configuration Manager automatically distributes that content to the client's
     preferred distribution points.

     Although this triggers Configuration Manager to automatically distribute the
     content to that client's preferred distribution points, the client might obtain that
     content from other distribution points before the preferred distribution points for
     the client receive the deployment. When this behavior occurs, the content will then

<!-- p.402 -->

     be present on that distribution point for use by the next client that seeks that
     deployment.

For more information, see Boundary groups.

Package transfer manager
Package transfer manager is the site server component that transfers content to
distribution points on other computers.

For more information, see Package transfer manager.

Prestage content
Prestaging content is a process of transferring content to a distribution point without
distributing the content across the network.

For more information, see Manage network bandwidth.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.403 -->

Use a pull-distribution point with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When you distribute content to a standard distribution point in the Configuration
Manager console, the site server pushes the content to the distribution point. A pull-
distribution point gets content by downloading it from a source location like a client.

When you distribute content to many distribution points, pull-distribution points help
reduce the processing load on the site server. They can also speed the content transfer
to each server. Normally the distribution manager component on the site server sends
content to each distribution point. Instead, the site offloads the process of transferring
the content to the pull-distribution points.

You configure individual distribution points to be pull-distribution points. For each pull-
distribution point, specify one or more source distribution points from which it can get
content. A pull-distribution point can only download content from a distribution point
that you specify as a source distribution point.

When you distribute content to a pull-distribution point in the console, the site server
sends it a notification. The pull-distribution point then downloads the content from a
source distribution point. A pull-distribution point manages the content transfer by
downloading from a distribution point that already has a copy of the content.

Pull-distribution points support the same configurations and functionality as typical
distribution points. For example, a pull-distribution point supports:

      Multicast and PXE configurations
      Content validation
      On-demand content distribution
      HTTP or HTTPS communications from clients
      The same certificate options as other distribution points
      Manage individually or as a member of a distribution point group

Configure a pull-distribution point when you install the distribution point. After you
create a distribution point, configure it as a pull-distribution point by editing the role
properties. For more information on how to enable a distribution point as a pull-
distribution point, see Pull-distribution point.

<!-- p.404 -->

Remove the configuration to be a pull-distribution point by editing the properties of the
distribution point. When you remove the configuration as a pull-distribution point, it
returns to normal operation. The site server manages future content transfers to the
distribution point.

Distribution process
When you distribute content to a pull-distribution point, the following sequence of
events occurs:

     Once you distribute content to a pull-distribution point in the console, the Package
     Transfer Manager component on the site server checks the site database to
     confirm if the content is available on a source distribution point. If it can't confirm
     that the content is on a source distribution point for the pull-distribution point, it
     repeats the check every 20 minutes until the content is available.

     When the Package Transfer Manager confirms that the content is available, it
     notifies the pull-distribution point to download the content. If this notification fails,
     it retries based on the Software Distribution component Retry settings for pull-
     distribution points. When the pull-distribution point receives this notification, it
     tries to download the content from its source distribution points.

     While the pull-distribution point downloads the content, the Package Transfer
     Manager polls the status based on the Software Distribution component Status
     polling settings for pull-distribution points. When the pull-distribution point
     completes the download of content, it submits this status to a management point.

Configure site component settings
When you use a pull-distribution point, review and configure the following site
component settings:

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. Select the site. In the ribbon, select Configure Site Components, and select
     Software Distribution.

   3. Switch to the Pull Distribution Point tab.

   4. In the Retry settings group, review the following values:

<!-- p.405 -->

        Number of retries: The number of times that the Package Transfer Manager
        tries to notify the pull-distribution point to download the content. After it
        tries this number of times, the Package Transfer Manager cancels the transfer.
        This value is 30 by default.

        Delay before retrying (minutes): The number of minutes that the Package
        Transfer Manager waits between attempts. This value is 20 by default.

 5. In the Status polling settings group, review the following values:

        Number of polls: The number of times that the Package Transfer Manager
        contacts the pull-distribution point to retrieve the job status. If it tries this
        number of times before the job completes, the Package Transfer Manager
        cancels the transfer. This value is 72 by default.

        Delay before retrying (minutes): The number of minutes that the Package
        Transfer Manager waits between attempts. This value is 60 by default.

     ７ Note

     When the Package Transfer Manager cancels a job because it exceeds the
     number of polling retries, the pull-distribution point continues to download
     the content. When it finishes, the pull-distribution point sends the appropriate
     status message, and the console reflects the new status.

Limitations
   You can't configure a content-enabled cloud management gateway as a pull-
   distribution point.

   You can't configure the distribution point role on a site server as a pull-distribution
   point.

   The prestage content configuration overrides the pull-distribution point
   configuration. If you turn on the option to Enable this distribution point for
   prestaged content on a pull-distribution point, it waits for the content. It doesn't
   pull content from the source distribution point. Like a standard distribution point
   enabled for prestaged content, it doesn't receive content from the site server. For
   more information, see Prestaged content.

   A pull-distribution point doesn't use schedule or rate limit configurations. When
   you configure a previously installed distribution point to be a pull-distribution

<!-- p.406 -->

     point, configurations for schedule and rate limits are saved, but not used. If you
     later remove the pull-distribution point configuration, the schedule and rate limit
     configurations are implemented as previously configured.

          ７ Note

          The Schedule and Rate Limits tabs aren't visible in the properties of the
          distribution point.

     Pull-distribution points don't use the settings on the General tab of the Software
     Distribution Component Properties for each site. These settings include
     Concurrent distribution and Multicast retry.

     To transfer content from a source distribution point in a remote forest, install the
     Configuration Manager client on the pull-distribution point. Also configure a
     network access account that can access the source distribution point. If you enable
     the site option to Use Configuration Manager-generated certificates for HTTP
     site systems, then you don't need a network access account.

     If the pull-distribution point is also a Configuration Manager client, the client
     version must be the same as the Configuration Manager site that installs the pull-
     distribution point. The pull-distribution point uses the CCMFramework that is
     common to both the pull-distribution point and the Configuration Manager client.

About source distribution points
When you configure the pull-distribution point, specify one or more source distribution
points:

     The wizard only displays distribution points that qualify to be source distribution
     points.

     A pull-distribution point can be specified as a source distribution point for another
     pull-distribution point.

     Only distribution points that support HTTP can be specified as source distribution
     points when you use the Configuration Manager console.

     To use a source distribution point that's configured for HTTPS, install the
     Configuration Manager client on the pull-distribution point.

     If your remote offices have a better connection to the internet, or to reduce load
     on your WAN links, use a content-enabled cloud management gateway (CMG) in

<!-- p.407 -->

    Microsoft Azure as the source. The pull-distribution point needs internet access to
    communicate with Microsoft Azure. The content must be distributed to the source
    CMG.

      ７ Note

      This feature does incur charges to your Azure subscription for data storage
      and network egress. For more information, see the Cost of CMG.

  Tip

 When a pull-distribution point downloads content from a source distribution point,
 that pull-distribution point is counted as a client in the Client Accessed (Unique)
 column of the Distribution point usage summary report.

Source priorities
    Assign a separate priority to each source distribution point, or assign multiple
    source distribution points to the same priority.

    The priority determines the order in which the pull-distribution point requests
    content from its source distribution points.

    Pull-distribution points initially contact a source distribution point with the lowest
    value for priority. If there are multiple source distribution points with the same
    priority, the pull-distribution point randomly selects one of the sources with that
    priority.

    If the content isn't available on a selected source, the pull-distribution point then
    tries to download the content from another distribution point with that same
    priority.

    If none of the distribution points with a given priority has the content, the pull-
    distribution point tries to download the content from a source distribution point
    with the next priority level. It continues this search until the content is located.

    If none of the assigned source distribution points have the content, the pull-
    distribution point waits for 30 minutes, and then starts the process again.

Inside the pull-distribution point

<!-- p.408 -->

   To manage the transfer of content, pull-distribution points use the CCMFramework
   component. The Configuration Manager client includes this component.

   When you enable the pull-distribution point, the site installs pulldp.msi. This
   installer also adds the CCMFramework component. The framework doesn't require
   the Configuration Manager client.

   After the pull-distribution point is installed, it primarily uses the CCMExec service
   to function.

   When the pull-distribution point transfers content, it uses the Background
   Intelligent Transfer Service (BITS) built into Windows. A pull-distribution point
   doesn't require that you install the BITS Extension for IIS Server.

        ７ Note

        If you install a pull-distribution point on a workstation OS, the client enables
        BITS with the default settings. This behavior happens even if the client settings
        are set to disable BITS. These default settings may not be optimum for a pull-
        distribution point. Review the client settings and group policies for BITS that
        you apply to devices that you enable as a pull-distribution point.

   For operational details, see the following log files on the pull-distribution point:
        DataTransferService.log
        PullDP.log

 Tip

If you see HTTP 403 errors in the log files after you add up a pull-distribution point,
make the following change:

   1. On the source distribution point, set the following registry value:
        HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL,

        ClientAuthTrustMode = 2 (REG_DWORD)

   2. Restart the source distribution point server.

Then the pull distribution point should start downloading content from the source.
For more information on this registry key, see Overview of TLS - SSL (Schannel
SSP).

<!-- p.409 -->

See also
Fundamental concepts for content management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.410 -->

The content library in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The content library is a single-instance store of content in Configuration Manager. The
site uses it to reduce the overall size of the combined body of content that you
distribute. The content library stores all content files for software deployments, for
example: software updates, applications, and OS deployments.

      The site automatically creates and maintains a copy of the content library on each
      site server and each distribution point.

      Before Configuration Manager adds content files to the site server or copies the
      files to distribution points, it verifies whether each content file is already in the
      content library.

      If the content file is available, Configuration Manager doesn't copy the file. It
      instead associates the existing content file with the application or package.

On distribution point servers, configure the following options:

      One or more disk drives on which you want to create the content library.

      A priority for each drive that you use.

Configuration Manager copies content files to the drive with the highest priority until
that drive contains less than a minimum amount of free space that you specify.

      You configure the drive settings during the distribution point installation.

      You can't configure the drive settings in the distribution point properties after the
      installation has finished.

For more information about how to configure the drive settings for the distribution
point, see Manage content and content infrastructure.

  ７ Note

<!-- p.411 -->

  To move the content library to a different location on a distribution point after the
  installation, use the Content Library Transfer tool in the Configuration Manager
  tools. For more information, see the Content Library Transfer tool.

About the content library on the CAS
By default, Configuration Manager creates a content library on the central
administration site (CAS) when the site is installed. The content library is placed on the
drive of the site server that has the most free disk space. Because you can't install a
distribution point on the CAS, you can't prioritize the drives for use by the content
library. Similar to the content library on other site servers and on distribution points,
when the drive that contains the content library runs out of available disk space, the
content library automatically spans to the next available drive.

Configuration Manager uses the content library on the CAS in the following scenarios:

     You create content on the CAS.

     You migrate content from another Configuration Manager site, and assign the CAS
     as the site that manages that content.

  ７ Note

  When you create content at a primary site, and then distribute it to a different
  primary site or a secondary site below a different primary site, the CAS temporarily
  stores that content in its scheduler inbox. It doesn't add that content to its content
  library.

Use the following options to manage the content library on the CAS:

     To prevent the content library from being installed on a specific drive, create an
     empty file named NO_SMS_ON_DRIVE.SMS. Copy it to the root of the drive before
     the content library is created.

     After the content library has been created, use the Content Library Transfer tool
     from the Configuration Manager tools to manage the location of the content
     library. For more information, see the Content Library Transfer tool.

  ７ Note

<!-- p.412 -->

  Content-enabled cloud management gateways don't use single-instance storage.
  The site encrypts packages before sending to Azure, and each package has a
  unique encrypted key. Even if two files were identical, the encrypted versions
  wouldn't be the same.

Inside the content library

  ２ Warning

  The following section is provided for informational purposes only. Don't alter, add,
  or remove any files or folders in the content library. Doing so could corrupt
  packages, contents, or the content library as a whole. If you suspect any missing,
  corrupt, or otherwise invalid data, use the validation feature in the Configuration
  Manager console to detect such issues. Then redistribute the affected content to
  correct the issues.

By default, the content library is stored on the root of a drive in a folder called
SCCMContentLib. This folder is shared by default as SCCMContentLib$. The folder and
share have restricted permissions to prevent accidental damage. All changes should be
made from the Configuration Manager console. Within this folder are the following
objects:

     The package library (PkgLib folder): Information about what packages are present
     on the distribution point.

     The data library (DataLib folder): Information about the original structure of the
     packages.

     The file library (FileLib folder): The original files in the package. This folder is
     typically what uses the bulk of the storage.

<!-- p.413 -->

                                                                                       

   Tip

  Use the Content Library Explorer tool from the Configuration Manager tools to
  browse the contents of the content library. You can't use this tool to modify the
  contents. It provides insight into what's present, as well as allowing validation and
  redistribution. For more information, see the Content Library Explorer.

Package library
The package library folder, PkgLib, includes one file for each package distributed to the
distribution point. The file name is the package ID, for example, ABC00001.INI . In this file
under the [Packages] section is a list of content IDs that are part of the package, as well
as other information such as the version. For example, ABC00001 is a legacy package at
version 1. The content ID in this file is ABC00001.1 .

<!-- p.414 -->

Data library
The data library folder, DataLib, includes one file and one folder for each of the contents
in each package. For example, this file and folder are named ABC00001.1.INI and
ABC00001.1 , respectively. The file includes information for validation. The folder

recreates the folder structure from the original package.

The files in the data library are replaced by INI files with the name of the original file in
the package. For example, MyFile.exe.INI . These files include information about the
original file, such as the size, time modified, and the hash. Use the first four characters of
the hash to locate the original file in the file library. For example, the hash in
MyFile.exe.INI is DEF98765, and the first four characters are DEF9.

File library
If the content library spans across multiple drives, the package files could be in the file
library folder, FileLib, on any of these drives.

Locate a specific file using the first four characters from the hash found in the data
library. Inside the file library folder are many folders, each with a four-character name.
Find the folder that matches the first four characters from the hash. Once you find this
folder, it includes one or more sets of three files. These files share the same name, but
one has the extension INI, one has the extension SIG, and one has no file extension. The
original file is the one with no extension whose name is equal to the hash from the data
library.

For example, folder DEF9 includes DEF98765.INI , DEF98765.SIG , and DEF98765 . DEF98765
is the original MyFile.exe . The INI file includes a list of "users" or content IDs that share
the same file. The site doesn't remove a file unless all of these contents are also
removed.

Drive spanning
The content library can be spanned across multiple drives. You choose these drives
when creating the distribution point. By default, Configuration Manager automatically
chooses the drives when spanning the content library.

When you choose the drives, select a primary and secondary drive. The site stores all
metadata on the primary drive. It only spans the file library across to the secondary
drive. The folder's share name for secondary drives includes the drive letter. For
example, if D: and E: are secondary drives for the content library, the share names are
SCCMContentLibD$ and SCCMContentLibE$.

<!-- p.415 -->

If you chose the Automatic option, Configuration Manager selects the drive with the
most available free space as its primary drive. It stores all of the metadata on this drive.
The site only spans the file library across to secondary drives.

You specify a reserve space amount during configuration. Configuration Manager
attempts to use a secondary disk once the best available disk has only this reserve space
amount left free. Each time a new drive is selected for use, the drive with the most
available free space is selected.

You can't specify that a distribution point should use all drives except for a specific set.
Prevent this behavior by creating an empty file on the root of the drive, called
NO_SMS_ON_DRIVE.SMS . Place this file before Configuration Manager selects the drive for

use. If Configuration Manager detects this file on the root of the drive, it doesn't use the
drive for the content library.

Troubleshoot
The following tips may help you troubleshoot issues with the content library:

     Review the logs on the site server (distmgr.log and PkgXferMgr.log) and the
     distribution point (smsdpprov.log) for any pointers to the failures.

     Use the Content Library Explorer tool.

     Check for file locks by other processes, such as antivirus software. Exclude the
     content library on all drives from automatic antivirus scans, as well as the
     temporary staging directory, SMS_DP$, on each drive.

     To see if there are any hash mismatches, validate the package from the
     Configuration Manager console.

     As a last option, redistribute the content. This action should resolve most issues.

For more in-depth information, see Understand and troubleshoot content distribution.

Next steps
Configure a remote content library for the site server

Flowchart - Manage content library

Feedback

<!-- p.416 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.417 -->

Configure a remote content library for
the site server
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To configure site server high availability or to free up hard drive space on your central
administration or primary site servers, relocate the content library to another storage
location. Move the content library to another drive on the site server, a separate server,
or fault-tolerant disks in a storage area network (SAN). A SAN is recommended, because
it's highly available, and provides elastic storage that grows or shrinks over time to meet
your changing content requirements. For more information, see High availability
options.

A remote content library is a prerequisite for site server high availability.

This action only moves the content library on the site server. It doesn't impact the
location of the content library on distribution points.

   Tip

  Also plan for managing package source content, which is external to the content
  library. Every software object in Configuration Manager has a package source on a
  network share. Consider centralizing all sources to a single share, but make sure
  this location is redundant and highly available.

  If you move the content library to the same storage volume as your package
  sources, you can't mark this volume for data deduplication. While the content
  library supports data deduplication, the package sources volume doesn't support it.
  For more information, see Data deduplication.

Prerequisites
      The site server computer account needs Full control permissions to the network
      path to which you're moving the content library. This permission applies to both
      the share and the file system. No components are installed on the remote system.

      The site server can't have the distribution point role. The distribution point also
      uses the content library, and this role doesn't support a remote content library.

<!-- p.418 -->

    After moving the content library, you can't add the distribution point role to the
    site server.

       ７ Note

       The Manage Content Library option isn't available if the distribution point
       role exists on the site server. To enable the option, remove the distribution
       point role from the site server.

    The remote system for the content library needs to be in a trusted domain.

 ） Important

 Don't reuse a shared network location between multiple sites. For example, don't
 use the same path for both a central administration site and a child primary site.
 This configuration has the potential to corrupt the content library, and require you
 to rebuild it.

Manage the content library
 1. Create a folder in a network share as the target for the content library. For
    example, \\server\share\folder .

       ２ Warning

       Don't reuse an existing folder with content. For example, don't use the same
       folder as your package sources. Before copying the content library,
       Configuration Manager removes any existing content from the location you
       specify.

 2. In the Configuration Manager console, switch to the Administration workspace.
    Expand Site Configuration, select the Sites node, and select the site. On the
    Summary tab at the bottom of the details pane, notice a new column for the
    Content Library.

 3. Select Manage Content Library on the ribbon.

 4. In the Manage Content Library window, the Current Location field shows the local
    drive and path. Enter a valid network path for the New Location. This path is the

<!-- p.419 -->

     location to which the site moves the content library. It must include a folder name
     that already exists on the share, for example, \\server\share\folder . Select OK.

   5. Note the Status value in the Content Library column on the Summary tab of the
     details pane. It updates to show the site's progress in moving the content library.

           While In progress, the Move Progress (%) value displays the percentage
           complete.

              ７ Note

              If you have a large content library, you may see 0% progress in the
              console for a while. For example, with a 1 TB library, it has to copy 10 GB
              before it shows 1% . Review distmgr.log, which shows the number of files
              and bytes copied. The log file also shows an estimated time remaining.

           If there's an error state, the status displays the error. Common errors include
           access denied or disk full.

           When complete it displays Complete.

     See the distmgr.log for details. For more information, see Site server and site
     system server logs.

        ７ Note

        Starting in version 2010, you can enable verbose logging to troubleshoot the
        content library move process. Set the following registry key on the site server:
        HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\DP, LibraryMoveVerboseLog = 1

        (REG_DWORD) .

For more information on this process, see Flowchart - Manage content library.

The site actually copies the content library files to the remote location. This process
doesn't delete the content library files at the original location on the site server. To free
up space, an administrator must manually delete these original files.

If the original content library spans two drives, it's merged into a single folder at the
new destination.

During the copy process, the Despooler and Distribution manager components don't
process new packages. This action makes sure that content isn't added to the library

<!-- p.420 -->

while it's moving. Regardless, schedule this change during a system maintenance.

If you need to move the content library back to the site server, repeat this process, but
enter a local drive and path for the New Location. It must include a folder name that
already exists on the drive, for example, D:\SCCMContentLib . When the original content
still exists, the process quickly moves the configuration to the location local to the site
server.

   Tip

  To move the content to another drive on the site server, use the Content Library
  Transfer tool. For more information, see the Content Library Transfer tool.

Support untrusted domains
If your environment has distribution points in untrusted domains, you need to make
other configuration changes.

   1. On the computer that will host the distribution point role in the untrusted domain:

      a. Create a local user account.

      b. When you add the distribution point role to this computer, use this local
          account as the site system installation account. For example,
          COMPUTER.UNTRUSTEDDOMAIN\LocalAccount .

   2. On the server that hosts the remote content library for the site, create a local user
     account. This account should have the same name and password as the account in
     the first step.

When the distribution manager component distributes content to the server in the
untrusted domain, it will use the local user account. During content distribution, this
component gets the files from the content library server in the context of the
distribution point's local account. Since this same account exists on the content library
server, distribution manager can authenticate to read the content files and copy to the
remote distribution point.

Next steps
Flowchart - Manage content library

<!-- p.421 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.422 -->

Flowchart - Manage content library
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This flowchart diagram shows the process by which the site moves the content library to
a remote location. For more information, see the following articles:

      The content library
      Site server high availability

<!-- p.423 -->

<!-- p.424 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.425 -->

Content library cleanup tool
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the content library cleanup command-line tool to remove content that's no longer
associated with an object on a distribution point. This type of content is called orphaned
content. This tool replaces older versions of similar tools released for past Configuration
Manager products.

The tool only affects the content on the distribution point that you specify when you run
the tool. The tool can't remove content from the content library on the site server.

If you remove content from a distribution point while the site system is offline, an
orphaned record can exist in WMI. Over time, this behavior can eventually lead to a
warning status on the distribution point. To mitigate the issue in version 2006 and
earlier, you had to manually remove the orphaned entries from WMI. Making a mistake
during this process could cause more severe issues with the server. Starting in version
2010, the tool can also remove orphaned content records from the WMI provider on a
distribution point.

Find ContentLibraryCleanup.exe in CD.Latest\SMSSETUP\TOOLS\ContentLibraryCleanup
on the site server. For more information on this location, see The CD.Latest folder.

Requirements
      Only run the tool against a single distribution point at a time.

      Run it directly on the server that hosts the distribution point to clean up, or
      remotely from another computer.

      The tool doesn't support removing content from the site server, which has a single
      content library. When the site server also has the distribution point role, if a
      package isn't targeted to the server, the package is still in the single content
      library.

      The tool doesn't support a content-enabled cloud management gateway.

      The user account that runs the tool must have permissions the same as the Full
      Administrator security role in Configuration Manager.

<!-- p.426 -->

Modes of operation
Run the tool in the following two modes: What-if and Delete.

   Tip

  Start with the what-if mode. When you're satisfied with the results, then run the
  tool in delete mode.

What-if mode
If you don't specify the /delete parameter, the tool runs in what-if mode. This mode
identifies the content that would be deleted from the distribution point.

     When run in this mode, the tool doesn't delete any data.

     The tool writes to the log file information about the content that it would delete.
     You're not prompted to confirm each potential deletion.

Delete mode
When you run the tool with the /delete parameter, the tool runs in delete mode.

     When run in this mode, orphaned content that it finds on the specified distribution
     point can be deleted from the distribution point's content library.

     Starting in version 2010, it can also remove orphaned content records from the
     WMI provider on the distribution point.

     Before deleting each file, confirm that the tool should delete it. Select Y for yes, N
     for no, or Yes to all to skip further prompts and delete all orphaned content.

Log file
When the tool runs in either mode, it automatically creates a log file. It names the file
with the following information:

     The mode the tool runs in
     The name of the distribution point
     The date and time of operation

When the tool finishes, it automatically opens the log file in Windows.

<!-- p.427 -->

By default, the tool writes the log file to the temp folder of the user account that runs
the tool. This location is on the computer where you run the tool, which isn't always the
target of the tool. Use the /log parameter to redirect the log file to another location,
including a network share.

Run the tool
To run the tool:

   1. Open a command prompt as an administrator. Change directory to the folder that
       contains ContentLibraryCleanup.exe.

   2. Enter a command line that includes the required command-line parameters, and
       any optional parameters you want to use.

Command-line parameters
Use these command-line parameters in any order.

Required parameters

                                                                                  ﾉ   Expand table

 Parameter         Details

 /dp               Specify the fully qualified domain name (FQDN) of the distribution point to
 <distribution     clean.
 point FQDN>

 /ps <primary      Required only when cleaning content from a distribution point at a secondary
 site FQDN>        site. The tool connects to the parent primary site to run queries against the
                   SMS Provider. These queries let the tool determine what content should be on
                   the distribution point. It can then identify the orphaned content to remove.
                   This connection to the parent primary site must be made for distribution
                   points at a secondary site because the required details aren't available directly
                   from the secondary site.

 /sc <primary      Required only when cleaning content from a distribution point at a secondary
 site code>        site. Specify the site code of the parent primary site.

Example: Scan and log what content it would delete (what-if)
ContentLibraryCleanup.exe /dp server1.contoso.com

<!-- p.428 -->

Example: Scan and log content for a DP at a secondary site
ContentLibraryCleanup.exe /dp server1.contoso.com /ps siteserver1.contoso.com /sc

ABC

Optional parameters

                                                                                  ﾉ   Expand table

 Parameter        Details

 /delete          Use this parameter when you're ready to delete content from the distribution
                  point. It prompts you before it deletes content.

                  When you don't use this parameter, the tool logs results about what content it
                  would delete. Without this parameter, it doesn't actually delete any content
                  from the distribution point.

 /q               This parameter runs the tool in a quiet mode that suppresses all prompts.
                  These prompts include when it deletes content. It also doesn't automatically
                  open the log file.

 /ps <primary     Optional only when cleaning content from a distribution point at a primary
 site FQDN>       site. Specify the FQDN of the primary site that the distribution point belongs
                  to.

 /sc <primary     Optional only when cleaning content from a distribution point at a primary
 site code>       site. Specify the site code of the primary site that the distribution point
                  belongs to.

 /log <log file   Specify the location where the tool writes the log file. This location can be a
 directory>       local drive or a network share.

                  When you don't use this parameter, the tool places the log file in the user's
                  temp directory on the computer where the tool runs.

Example: Delete content
ContentLibraryCleanup.exe /dp server1.contoso.com /delete

Example: Delete content without prompts
ContentLibraryCleanup.exe /q /dp server1.contoso.com /delete

Example: Log to local drive

<!-- p.429 -->

ContentLibraryCleanup.exe /dp server1.contoso.com /log
C:\Users\Administrator\Desktop

Example: Log to network share
ContentLibraryCleanup.exe /dp server1.contoso.com /log \\server\share

Known issue
In version 2103 and earlier, when any package or deployment has failed, or is in
progress, the tool might return the following error:

System.InvalidOperationException: This content library cannot be cleaned up right

now because package <packageID> is not fully installed.

To work around this issue, update the site to version 2107. The tool can't reliably identify
orphaned files, but will display a warning and continue.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.430 -->

Peer cache for Configuration Manager
clients
Article • 03/28/2024

Applies to: Configuration Manager (current branch)

Use peer cache to help manage deployment of content to clients in remote locations.
Peer cache is a built-in Configuration Manager solution that enables clients to share
content with other clients directly from their local cache.

Overview
Definitions:

      Peer cache client: Any Configuration Manager client that downloads content from
      a peer.

      Peer cache source: A Configuration Manager client that you enable for peer cache,
      and that has content to share with other clients.

Use client settings to enable clients to be peer cache sources. You don't need to enable
peer cache clients. When you enable clients as peer cache sources, the management
point includes them in the list of content location sources. For more information on this
process, see Operations.

A peer cache source must be a member of the current boundary group of the peer
cache client. The management point doesn't include peer cache sources from a
neighbor boundary group in the list of content sources it provides the client. It only
includes distribution points from a neighbor boundary group. For more information
about current and neighbor boundary groups, see Boundary groups.

The Configuration Manager client uses peer cache to serve to other clients every type of
content in the cache. This content includes:

      Microsoft 365 Apps for enterprise files
      Express installation files

Peer cache doesn't replace the use of other solutions like Windows BranchCache or
Delivery Optimization. Peer cache works along with other solutions. These technologies
give you more options for extending traditional content deployment solutions such as

<!-- p.431 -->

distribution points. Peer cache is a custom solution with no reliance on BranchCache. If
you don't enable or use BranchCache, peer cache still works.

  ７ Note

  Windows BranchCache is always enabled on deployments. If the distribution point
  supports it, and it's enabled in client settings, clients use BranchCache. For more
  information, see Configure BranchCache.

Operations
To enable peer cache, deploy the client settings to a collection. Then members of that
collection act as a peer cache source for other clients in the same boundary group.

     A client that operates as a peer content source submits a list of available cached
     content to its management point using state messages. A peer content source
     client also sends a state message to the management point when it removes
     content from its local cache.

       ７ Note

       For the list of applicable peer content source state messages, see State
       messages in Configuration Manager. Specifically those with state message
       IDs of 7200, 7201, 7202, and 7203.

     Another client in the same boundary group makes a content location request to
     the management point. The server returns the list of potential content sources.
     This list includes each peer cache source that has the content and is online. It also
     includes the distribution points and other content source locations in that
     boundary group. For more information, see Content source priority.

     As usual, the client that's seeking the content selects one source from the provided
     list. The client then attempts to get the content.

Boundary groups include settings to give you more control over content distribution in
your environment. For more information, see Boundary group options for peer
downloads.

  ７ Note

<!-- p.432 -->

  If the client falls back to a neighbor boundary group for content, the management
  point doesn't add the peer cache sources from the neighbor boundary group to
  the list of potential content source locations.

Choose only clients best suited as peer cache sources. Evaluate client suitability based
on attributes such as chassis type, disk space, and network connectivity. For more
information that can help you select the best clients to use for peer cache, see this blog
by a Microsoft consultant   .

  ７ Note

  By default, if the first 25 peer cache sources are offline or unreachable, a peer cache
  client may fail to download the content. You can configure this setting with the site
  definition properties SuperPeerLocationCount and SuperPeerLocationCountMax . Their
  default values are 25 and 50 . For more information, see How to read and write to
  the site control file by using WMI.

  You can also reduce these values, for example, 5 and 10 . This configuration causes
  the client to more quickly fall back to other content locations. For more
  information, see Content source priority.

Limited access to a peer cache source
A peer cache source rejects requests for content when it meets any of the following
conditions at the time a peer requests content:

     Low battery mode

     Processor load exceeds 80%

     Disk I/O has an AvgDiskQueueLength that exceeds 10

     There are no more available connections to the computer

   Tip

  Configure these settings using the client configuration server WMI class for the
  peer source feature ( SMS_WinPEPeerCacheConfig ) in the Configuration Manager SDK.

When the peer cache source rejects a request for the content, the peer cache client
continues to seek content from its list of content source locations.

<!-- p.433 -->

Requirements
   Peer cache supports all Windows versions listed as supported in Supported
   operating systems for clients and devices. Non-Windows operating systems aren't
   supported as peer cache sources or peer cache clients.

     ７ Note

     Windows 10/11 Arm64 isn't supported as peer cache source or peer cache
     clients.

   A peer cache source must be a domain-joined Configuration Manager client.
   However, a client that's not domain-joined can get content from a domain-joined
   peer cache source.

   Clients can only download content from peer cache sources in their current
   boundary group.

     ７ Note

     Configuration Manager determines if a peer cache source has roamed to
     another location. This behavior makes sure the management point offers it as
     a content source to clients in the new location and not the old location.

   A network access account isn't required with the following exception:

     Configure a network access account in the site when a peer cache-enabled
     client runs a task sequence from Software Center, and it reboots to a boot
     image. When the device is in Windows PE, it uses the network access account to
     get content from the peer cache source.

     When required, the peer cache source uses the network access account to
     authenticate download requests from peers. This account requires only domain
     user permissions for this purpose.

   Before attempting to download content, the management point first validates that
   the peer cache source is online. This validation happens via the "fast channel" for
   client notification, which uses TCP port 10123.

 ７ Note

<!-- p.434 -->

  To take advantage of new Configuration Manager features, first update clients to
  the latest version. While new functionality appears in the Configuration Manager
  console when you update the site and console, the complete scenario isn't
  functional until the client version is also the latest.

Client settings
For more information about the peer cache client settings, see Client cache settings.

For more information on configuring these settings, see How to configure client
settings.

On peer cache-enabled clients that use the Windows Firewall, Configuration Manager
configures the firewall ports that you specify in client settings.

Partial download support
Client peer cache sources can divide content into parts. These parts minimize the
network transfer to reduce WAN usage. The management point provides more detailed
tracking of the content parts. It tries to eliminate more than one download of the same
content per boundary group.

Example scenario
Contoso has a single primary site with two boundary groups: Headquarters (HQ) and
Branch Office. There's a 30-minute fallback relationship between the boundary groups.
The management point and distribution point for the site are only in the HQ boundary.
The branch office location has no local distribution point. Two of the four clients at the
branch office are configured as peer cache sources.

<!-- p.435 -->

1. You target a deployment with content to all four clients in the branch office. You
  only distributed the content to the distribution point.

2. Client3 and Client4 don't have a local source for the deployment. The management
  point instructs the clients to wait 30 minutes before falling back to the remote
  boundary group.

3. Client1 (PCS1) is the first peer cache source to refresh policy with the management
  point. Because this client is enabled as a peer cache source, the management point
  instructs it to immediately start downloading part A from the distribution point.

4. When Client2 (PCS2) contacts the management point, as part A is already in
  progress but not yet complete, the management point instructs it to immediately
  start downloading part B from the distribution point.

5. PCS1 finishes downloading part A, and immediately notifies the management
  point. As part B is already in progress but not yet complete, the management point
  instructs it to start downloading part C from the distribution point.

6. PCS2 finishes downloading part B, and immediately notifies the management
  point. The management point instructs it to start downloading part D from the
  distribution point.

<!-- p.436 -->

 7. PCS1 finishes downloading part C, and immediately notifies the management
    point. The management point informs it that there are no more parts available
    from the remote distribution point. The management point instructs it to
    download part B from its local peer, PCS2.

 8. This process continues until both client peer cache sources have all of the parts
    from each other. The management point prioritizes parts from the remote
    distribution point before instructing the peer cache sources to download parts
    from local peers.

 9. Client3 is the first to refresh policy after the 30-minute fallback period expires. It
    now checks back with the management point, which informs the client of new local
    sources. Instead of downloading the content in full from the distribution point
    across the WAN, it downloads the content in full from one of the client peer cache
    sources. Clients prioritize local peer sources.

 ７ Note

 If the number of client peer cache sources is greater than the number of content
 parts, then the management point instructs the additional peer cache sources to
 wait for fallback like a normal client.

Configure partial download
 1. Set up boundary groups and peer cache sources per normal.

 2. In the Configuration Manager console, go to the Administration workspace,
    expand Site Configuration, and select Sites. Select Hierarchy Settings in the
    ribbon.

 3. On the General tab, enable the option to Configure client peer cache sources to
    divide content into parts.

 4. Create a required deployment with content.

      ７ Note

      This functionality only works when the client downloads content in the
      background, such as with a required deployment. On-demand downloads,
      such as when the user installs an available deployment in Software Center,
      behaves as usual.

<!-- p.437 -->

To see them handling the download of content in parts, examine the
ContentTransferManager.log on the client peer cache source and the MP_Location.log
on the management point.

Guidance for cache management
Peer cache relies on the Configuration Manager client cache to share content. Consider
the following points for managing the client cache in your environment:

     The Configuration Manager client cache isn't like the content library on a
     distribution point. While you manage the content that you distribute to a
     distribution point, the Configuration Manager client automatically manages the
     content in its cache. There are settings and methods to help control what content
     is in the cache of a peer cache source. For more information, see Configure the
     client cache.

     Size and maintenance of the cache applies to peer cache sources. For more
     information, see Configure client cache size. Consider the size of larger content
     such as OS upgrade packages or Windows express update files. Compare your
     need for this content against the available disk space on peer cache sources.

     The peer cache source client updates the last referenced time of content in the
     cache when a peer downloads it. The client uses this timestamp when it
     automatically maintains its cache, removing older content first. So it should wait to
     remove content that peer cache clients more frequently download, if at all.

     If necessary, during an OS deployment task sequence, use the
     SMSTSPreserveContent variable to keep content in the client cache. For more
     information, see Task sequence variables.

     If necessary, when creating the following software, use the option to Persist
     content in the client cache:
        Applications
        Packages
        OS images
        OS upgrade packages
        Boot images

Monitoring
To help you understand the use of peer cache, view the Client Data Sources dashboard.
For more information, see Client data sources dashboard.

<!-- p.438 -->

Also use reports to view peer cache use. In the console, go to the Monitoring
workspace, expand Reporting, and select the Reports node. The following reports all
have a type of Software Distribution Content:

     Peer cache source content rejection: How often the peer cache sources in a
     boundary group reject a content request.

       ７ Note

       Known issue: When drilling down on results like MaxCPULoad or MaxDiskIO,
       you might receive an error that suggests the report or details can't be found.
       To work around this issue, use the other two reports that directly show the
       results.

     Peer cache source content rejection by condition: Shows rejection details for a
     specified boundary group or rejection type.

       ７ Note

       Known issue: You can't select from available parameters and instead must
       enter them manually. Enter the values for Boundary Group Name and
       Rejection Type as seen in the Peer cache source content rejection report. For
       example, for Rejection Type you might enter MaxCPULoad or MaxDiskIO.

     Peer cache source content rejection details: Show the content that the client was
     requesting when rejected.

       ７ Note

       Known issue: You can't select from available parameters and instead must
       enter them manually. Enter the value for Rejection Type as displayed in the
       Peer cache source content rejection report. Then enter the Resource ID for
       the content source about which you want more information.

       To find the Resource ID of the content source:

          1. Find the computer name that displays as the Peer cache source in the
             results of the Peer cache source content rejection by condition report.

          2. Go to the Assets and Compliance workspace, select the Devices node,
             and search for that computer's name. Use the value from the Resource

<!-- p.439 -->

              ID column.

Next steps
     Microsoft Connected Cache with Configuration Manager

     Support for Windows BranchCache

     Peer caching technologies

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.440 -->

Package Transfer Manager in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

In a Configuration Manager site, the Package Transfer Manager is a component of the
SMS_Executive service that manages the transfer of content from a site server computer
to remote distribution points in a site. (A remote distribution point is one that is not
located on the site server computer.) The Package Transfer Manager does not support
configurations by the admin, but understanding how it operates can help you plan your
content management infrastructure. It can also help you resolve problems with content
distribution.

When you distribute content to one or more remote distribution points at a site, the
Distribution Manager creates a content transfer job. It then notifies the Package
Transfer Manager on primary and secondary site servers to transfer the content to the
remote distribution points.

Package Transfer Manager logs its actions in the pkgxfermgr.log file on the site server.
The log file is the only location where you can view the activities of the Package Transfer
Manager.

  ７ Note

  In previous versions of Configuration Manager, the Distribution Manager manages
  the transfer of content to a remote distribution point. Distribution Manager also
  manages the transfer of content between sites. With the Configuration Manager,
  Distribution Manager continues to manage the transfer of content between two
  sites. However, the Package Transfer Manager now manages the transfer of content
  to large numbers of distribution points. This helps to increase the overall
  performance of content deployment both between sites and to distribution points
  within a site.

To transfer content to a standard distribution point, Package Transfer Manager operates
the same as the Distribution Manager operates in previous versions of Configuration
Manager. That is, it actively manages the transfer of files to each remote distribution
point. However, to distribute content to a pull-distribution point, the Package Transfer
Manager notifies the pull-distribution point that content is available. The pull-
distribution point then takes over the transfer process.
