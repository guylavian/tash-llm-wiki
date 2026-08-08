---
title: "Core infrastructure documentation — pages 2041-2080"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2041-2080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2041-2080
family: sccm
documentKind: "doc"
abstract: "There are eight columns: Status Icon: There are three possible status icons: Ready: Indicates that a particular job has finished all the verification steps. It's ready to be added to the running concurrent jobs. Jobs in this state are usually in a waiting stage. They wait for th"
---

# Core infrastructure documentation — pages 2041-2080

<!-- p.2041 -->

There are eight columns:

     Status Icon: There are three possible status icons:

        Ready: Indicates that a particular job has finished all the verification steps. It's
        ready to be added to the running concurrent jobs. Jobs in this state are usually
        in a waiting stage. They wait for the current running processes to finish to open
        up a space for them.

        Running: Indicates that a particular job is currently running on a distribution
        point. For long running jobs (large packages), usually there's time to get the
        progress (%) towards completion. It shows this percentage in the Progress
        column in this view. For small packages, the Progress column may stay empty.
        The job may already be completed by the time it receives status from the
        remote distribution point.

        Retry: Indicates that a particular job has failed and is now in a retry state. This
        job is retried after the retry interval. This interval is configurable, and set to 30
        minutes by default.

     Software: Name of the package that's targeted to a particular distribution point

     Package ID: Package ID of the package that's targeted to a particular distribution
     point

     Size: Size of the package in KB

     Progress: Job completion percentage. For more information, see the Running
     status icon description.

     Start/Restart Time: For a running job, this value is the start time (green). For a retry
     job, this value is the time that it will retry the job.

     Retries: Number of times it has retried this package.

     Distribution Point Name: The fully qualified domain name (FQDN) of the
     distribution point

   Tip

       To sort each column in this tab, click on the column name

       Manually refresh the information in this tab by clicking Refresh

<!-- p.2042 -->

        Automatically refresh the information in this tab by clicking Start Auto
        Refresh and setting the auto refresh interval. The default refresh interval is
        two minutes.

        If you need to modify a particular job, right-click the job in this view, and
        select Manage Job. This action opens the Manage Jobs tab.

Manage Jobs tab
Shows in one flat view a list of all the jobs and their statuses. It contains the same eight
columns as the Distribution Point Info tab. In this view, right-click the jobs for the
following actions:

     Run: Starts a job that's in any state other than running

     Move To Top: Moves one or more jobs to the top of the queue. This action may
     result in the jobs running immediately. A lower priority job may pause because of
     this action.

     Move Up: Moves a particular job one row above. A lower priority job may pause
     running because of this action.

     Move Down: Moves a particular job one row below.

     Move To Bottom: Moves one or more jobs to the bottom of the queue.

         Tip

        Drag-and-drop jobs in the list to move them.

     Cancel: Tries to cancel one or more jobs.

        ７ Note

        You can't cancel jobs near their final completion time. If the site server is also
        a distribution point, you can't cancel jobs on the site server.

See also
     Fundamental concepts for content management

<!-- p.2043 -->

     Package transfer manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2044 -->

Collection Evaluation Viewer
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Collection Evaluation Viewer is one of the Configuration Manager tools. Use it to view
and troubleshoot the collection evaluation process on the primary site server.

  ） Important

  Starting in Configuration Manager version 2103, this standalone tool isn't
  supported. The tool is no longer included with the Configuration Manager
  installation source. Starting in version 2010, its functionality is built-in to the
  console. For more information, see, How to view collection evaluation.

The tool displays the following information:

      Both historic and live information for full and incremental collection evaluations

      The evaluation queue status

      The time for collection evaluations to complete

      Which collections are currently being evaluated

      The estimated time that a collection evaluation will start and complete

About collection evaluation
The collection evaluation process runs by evaluating the membership rules of a
collection to update its members. The site places a collection that it's evaluating in one
of four different queues:

      Manual Queue: For collections that an administrator has manually selected for
      evaluation from the console

      New Queue: For newly created collections

      Full Queue: For collections due for full evaluation

      Incremental Queue: For collections with incremental evaluation

<!-- p.2045 -->

There are four threads that run to evaluate the collections in the above queues. Each
queue includes a series of arrays, and each array includes the collections to be
evaluated. The thread that's running for the queue selects a collection from the array
and runs the evaluation. The queue length indicates the number of arrays in the queue.

Requirements
     Run the tool on the site server

     Run the tool by an administrative user with at least the Read-Only Analyst role

     The user also requires Read permission to the site database in SQL

     SQL must be on the default port

Usage
Run CEViewer.exe. The main menu of the tool contains the following tabs:

     Connect: Establish the initial connection to the primary site server and SQL Server

     Full Evaluation: Lists the detailed information about all past full evaluations

     Incremental evaluation: Lists the detailed information about all past incremental
     evaluations

     All Queues: Summarizes the current collection evaluations for all four queues

     Manual Queue: Lists the detailed information about the current collection
     evaluation in the manual queue

     New Queue: Lists the detailed information about the current collection evaluation
     in the new queue

     Full Queue: Lists the detailed information about the current collection evaluation in
     the full queue

     Incremental Queue: Lists the detailed information about the current collection
     evaluation in the incremental queue

Connect tab
This tab allows you to establish the initial connection to the primary site server. The tool
also establishes a connection to the SQL Server that hosts the site database.

<!-- p.2046 -->

The connections to both primary site server and SQL Servers use the current signed-in
user credential. Connections to the central administration site or a secondary site aren't
supported. No collection evaluation process runs on those sites.

Once the tool successfully establishes a connection, see a notification at the bottom of
the Collection Evaluation Viewer that confirms the tool's connection to the SQL Server.

Full Evaluation tab
Shows detailed information about past full collection evaluations. There are eight
columns:

     Collection Name: Name of the collection

     Site ID: Site ID of the collection

     Run Time: How long the last collection evaluation ran, in seconds

     Last Evaluation Completion Time: When the last collection evaluation completed

     Next Evaluation Time: When the next full evaluation starts

     Member Changes: The member changes in the last collection evaluation. These
     changes are either plus (members added) or minus (members removed).

     Last Member Change Time: The most recent time that there was a membership
     change in the collection evaluation

     Percent: The percentage of evaluation time for this collection over the total (all
     collections) evaluation time

Incremental evaluation tab
Shows detailed information about past incremental collection evaluations. There are
seven columns:

     Collection Name: Name of the collection

     Site ID: Site ID of the collection

     Run Time: How long the last collection evaluation ran, in seconds

     Last Evaluation Completion Time: When the last collection evaluation completed

     Member Changes: The member changes in the last collection evaluation. These
     changes are either plus (members added) or minus (members removed).

<!-- p.2047 -->

     Last Member Change Time: The most recent time that there was a membership
     change in the collection evaluation

     Percent: The percentage of evaluation time for this collection over the total (all
     collections) evaluation time

All Queues tab
Summarizes the live collection evaluations for all four queues. There are six sections:

     Summary: Lists the total collection number and the queue length for all collections
     in all four queues

     Running Evaluation: Lists which collection is currently being evaluated in each
     queue, and how long it has been running

     Manual Update: Shows a brief summary of the collections being evaluated, the
     estimated completion time, and the order of the evaluation in the manual queue

     New Collection: Shows a brief summary of the collections being evaluated, the
     estimated completion time, and the order of the evaluation in the new collection
     queue

     Full Evaluation: Shows a brief summary of the collections being evaluated, the
     estimated completion time, and the order of the evaluation in the full evaluation
     queue

     Incremental Evaluation: Shows a brief summary of the collections being evaluated,
     the estimated completion time, and the order of the evaluation in the incremental
     evaluation queue

Manual Queue tab
Shows information about the manual collection evaluation currently being evaluated.
The order in the list is the order in which the collection will be evaluated. There are four
columns:

     Collection Name: Name of the collection

     Site ID: Site ID of the collection

     Estimated Completion Time: When the evaluation is estimated to complete

<!-- p.2048 -->

     Estimated Run Time: How long the evaluation is estimated to run, in
     day:hour:minute:second format

New Queue tab
Shows the live information about the new collection evaluation being evaluated. The
order in the list is the order in which the collection will be evaluated. There are four
columns:

     Collection Name: Name of the collection

     Site ID: Site ID of the collection

     Estimated Completion Time: When the evaluation is estimated to complete

     Estimated Run Time: How long the evaluation is estimated to run, in
     day:hour:minute:second format

Full Queue tab
Shows information about the full collection evaluation currently being evaluated. The
order in the list is the order in which the collection will be evaluated. There are four
columns:

     Collection Name: Name of the collection

     Site ID: Site ID of the collection

     Estimated Completion Time: When the evaluation is estimated to complete

     Estimated Run Time: How long the evaluation is estimated to run, in
     day:hour:minute:second format

Incremental Queue tab
Shows information about the incremental collection evaluation currently being
evaluated. The order in the list is the order in which the collection will be evaluated.
There are four columns:

     Collection Name: Name of the collection

     Site ID: Site ID of the collection

     Estimated Completion Time: When the evaluation is estimated to complete

<!-- p.2049 -->

     Estimated Run Time: How long the evaluation is estimated to run, in
     day:hour:minute:second format

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2050 -->

Content Library Explorer
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Content Library Explorer is one of the Configuration Manager tools. Use the tool for the
following activities:

      Explore the content library on a specific distribution point

      Troubleshoot issues with the content library

      Copy packages, contents, folders, and files out of the content library

      Redistribute packages to the distribution point

      Validate packages on remote distribution points

Requirements
      Run the tool using an account that has administrative access to:

         The target distribution point

         The WMI provider on the site server

         The Configuration Manager provider

      Only the Full Administrator and Read-Only Analyst roles have sufficient rights to
      view all information from this tool.

         Other roles, such as Application Administrator, can view partial information. For
         more information, see Disabled packages.

         The Read-Only Analyst can't redistribute packages from this tool.

      Run the tool from any computer, as long as it can connect to:

         The target distribution point

         The primary site server

         The Configuration Manager provider

      If the distribution point is colocated with the site server, it's still necessary to have
      administrative access to the site server.

<!-- p.2051 -->

Usage
When you start ContentLibraryExplorer.exe, enter the fully qualified domain name
(FQDN) of the target distribution point. It then connects to the distribution point. If the
distribution point is part of a secondary site, it prompts you for the FQDN of the primary
site server, and the primary site code.

In the left pane, view the packages that are distributed to this distribution point. Expand
the packages, and explore their folder structure. This structure matches the folder
structure from which you created the package.

When you select a folder, it displays in the right pane any files within the folder. This
view includes the following information:

     File name
     File size
     Which drive it's on
     Other packages that use the same file on the drive
     When the file was last changed on the distribution point

The tool also connects to the Configuration Manager provider. This connection is to
determine which packages are distributed to the distribution point, and whether they're
actually in the distribution point's content library. For instance, a package that's pending
distribution may not yet exist in the content library. Such a package would appear as
"PENDING" in the tool, and no actions are enabled for this package.

Disabled packages
Some packages are present on the distribution point but not visible in the Configuration
Manager console. These packages are marked with an asterisk (*). No actions may be
performed on these packages. Other packages may also be marked with an asterisk and
have actions disabled.

There are three primary reasons for disabled packages:

     The package is the Configuration Manager client upgrade. This package includes
     "ccmsetup.exe".

     Your user account can't access the package, likely due to role-based
     administration. For instance, the Application Author role can't see driver packages
     in the console, so any driver packages on the distribution point are marked as
     disabled.

<!-- p.2052 -->

     The package is orphaned on the distribution point.

Validate packages
Validate packages by using Package > Validate on the toolbar. First select a package
node in the left pane Don't select a content or a folder. The tool connects to the WMI
provider on the distribution point for this action. When the tool starts, packages that are
missing one or more contents are marked invalid. Validating the package reveals which
content is missing. If all content is present but the data is corrupted, validation detects
the corruption.

Redistribute packages
Redistribute packages using Package > Redistribute on the toolbar. First select a
package node in the left pane. This action requires permissions to redistribute packages.

Other actions
Use Edit > Copy to copy packages, contents, folders, and files out of the content library
to a specified folder. You can't copy the content library itself. Select more than one file,
but you can't select multiple folders.

Search for packages using Edit > Find Package. This action searches for your query in
the package name and package ID.

Limitations
     The tool can't manipulate the content library directly in any way. Changes to the
     content library may result in malfunctions.

     The tool can redistribute packages, but only to the target distribution point.

     When you colocate the distribution point with the site server, you can't validate
     package data. Use the Configuration Manager console instead. The tool still
     inspects the package to make sure that all the content is present, though not
     necessarily intact.

     You can't delete content with this tool.

See also

<!-- p.2053 -->

     Fundamental concepts for content management
     The content library

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2054 -->

Content Library Transfer tool
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Content Library Transfer tool is one of the Configuration Manager tools. It transfers
content from one disk drive to another. The tool is designed to run on distribution point
site systems. It supports distribution points colocated with a site or remote site systems.

The tool is useful for the scenario when the disk drive hosting the content library
becomes full. First add or identify another hard disk with sufficient space to host the
content library. Then use ContentLibraryTransfer.exe to transfer content from the old
filled hard disk to the new, empty drive.

Once the transfer is complete, content is accessible to client computers from the new
location.

Usage
Run ContentLibraryTransfer.exe as a user with administrative permissions on the
distribution point.

Syntax
ContentLibraryTransfer.exe –SourceDrive <drive letter of source drive> –TargetDrive

<drive letter of destination drive>

Example
ContentLibraryTransfer –SourceDrive E –TargetDrive G

Limitations
      Run the tool locally on the distribution point. You can't run it from a remote
      computer.

      Only use it when clients aren't actively accessing the distribution point. If you run
      the tool while clients are accessing content, the content library on the destination
      drive may have incomplete data. The data transfer might fail altogether leading to
      an unusable content library.

<!-- p.2055 -->

     Don't distribute content to the distribution point when you run the tool. If you run
     the tool while content is being written to the distribution point, the content library
     on the destination drive may have incomplete data. The data transfer might fail
     altogether leading to an unusable content library.

See also
     Fundamental concepts for content management
     The content library

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2056 -->

Content Ownership Tool
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Content Ownership Tool is one of the Configuration Manager tools. It changes
ownership of orphaned packages in Configuration Manager. Orphaned packages don't
have an owning site server. Packages can become orphaned by removing the site server
while they're still owned by this site server.

Run the Content Ownership Tool on any site server in the Configuration Manager
hierarchy. Sign in as an administrative user with sufficient package permissions.

   Tip

  Use ContentLibraryCleanup.exe in
   CD.Latest\SMSSETUP\TOOLS\ContentLibraryCleanup to remove orphaned content

  from a distribution point. For more information, see Content library cleanup tool.

Features
      Display all orphaned packages

      Display all packages, even if they're not orphaned

      View the status of the connection to a site

      Filter packages by name, site code, or package type

      Sort by any displayed column

      Change assignment of one or more packages with a single action

      View progress of the ownership transfer activity

Usage
Run ContentOwnershipTool.exe to start the tool. Local administrator permissions on the
computer aren't required to run the tool.

There are no command-line parameters.

<!-- p.2057 -->

  ） Important

  This tool changes the ownership of an orphaned package. The package itself
  doesn't move from the distribution point that it's stored on. This ownership change
  doesn't cause the package to update on distribution points. It also doesn't cause
  clients to reevaluate policy for deployment of the package. After the ownership
  changes, make sure that the new site server can access the source files. It should
  have at least Read permissions to the source files of each package.

See also
     Fundamental concepts for content management
     The content library

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2058 -->

Extend and migrate an on-premises site
to Microsoft Azure
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Starting in version 1910, this tool helps you to programmatically create Azure virtual
machines (VMs) for Configuration Manager. It can install with default settings site roles
like a passive site server, management points, and distribution points. Once you validate
the new roles, use them as additional site systems for high availability. You can also
remove the on-premises site system role and only keep the Azure VM role.

Prerequisites
      An Azure subscription

      Starting in version 2010, it supports environments with virtual networks other than
      ExpressRoute. In version 2006 and earlier, it requires an Azure virtual network with
      ExpressRoute gateway.

      Starting in version 2010, you can use the tool in a hierarchy or a standalone
      primary site. In version 2006 and earlier, it only works with a standalone primary
      site.

      Starting in version 2010, it supports a site with a collocated site database. In
      version 2006 and earlier, it requires the database to be on a remote SQL Server.

      Your user account needs to be a Configuration Manager Full Administrator and
      have administrator rights on the primary site server.

      To add a site server in passive mode, the site server must meet the high availability
      requirements. For example, it requires a remote content library.

Required Azure permissions
You'll need the following permissions in Azure when you run the tool:

      Microsoft.Resources/subscriptions/resourceGroups/read
      Microsoft.Resources/subscriptions/resourceGroups/write
      Microsoft.Resources/deployments/read
      Microsoft.Resources/deployments/write

<!-- p.2059 -->

     Microsoft.Resources/deployments/validate/action
     Microsoft.Compute/virtualMachines/extensions/read
     Microsoft.Compute/virtualMachines/extensions/write
     Microsoft.Compute/virtualMachines/read
     Microsoft.Compute/virtualMachines/write
     Microsoft.Network/virtualNetworks/read
     Microsoft.Network/virtualNetworks/subnets/read
     Microsoft.Network/virtualNetworks/subnets/join/action
     Microsoft.Network/networkInterfaces/read
     Microsoft.Network/networkInterfaces/write
     Microsoft.Network/networkInterfaces/join/action
     Microsoft.Network/networkSecurityGroups/write
     Microsoft.Network/networkSecurityGroups/read
     Microsoft.Network/networkSecurityGroups/join/action
     Microsoft.Storage/storageAccounts/write
     Microsoft.Storage/storageAccounts/read
     Microsoft.Storage/storageAccounts/listkeys/action
     Microsoft.Storage/storageAccounts/listServiceSas/action
     Microsoft.Storage/storageAccounts/blobServices/containers/write
     Microsoft.Storage/storageAccounts/blobServices/containers/read
     Microsoft.KeyVault/vaults/deploy/action
     Microsoft.KeyVault/vaults/read

For more information about permissions and assigning roles, see Add or remove Azure
role assignments using the Azure portal.

Virtual network support
Starting in version 2010, to support other virtual networks other than ExpressRoute,
make the following configurations:

     In the configuration of the virtual network, go to the DNS servers settings. Add a
     Custom DNS server with the IP address of a domain controller.

     On the site server where you'll run the tool, set the following registry value:
     HKCU\Software\Microsoft\ConfigMgr10\ExtendToAzure, SkipVNetCheck = 1

Run the tool
   1. Sign on to the site server and run the following tool in the Configuration Manager
     installation directory:

<!-- p.2060 -->

   Cd.Latest\SMSSETUP\TOOLS\ExtendMigrateToAzure\ExtendMigrateToAzure.exe

 2. Review the information on the General tab, and then switch to the Azure
   Information tab.

 3. On the Azure Information tab, choose your Azure environment, and then Sign in.

      Tip

     You may need to add https://*.microsoft.com to your trusted websites list to
     correctly sign in.

                                                                                 

 4. After you sign in, select your Subscription ID and Virtual network.

     ７ Note

     In version 2006 and earlier, the tool only lists networks with an ExpressRoute
     gateway.

Site server high availability

<!-- p.2061 -->

1. On the Site Server High Availability tab, select Check to evaluate your site's
  readiness.

  If any of the checks fail, select More detail to determine how to remediate the
  problem. For more information about these prerequisites, see Site server high
  availability.

2. If you want to extend or migrate your site server to Azure, select Create a site
  server in Azure. Then fill in the following fields:

                                                                             ﾉ   Expand table

   Name             Description

   Subscription     Read only. Shows the subscription name and ID.

   Resource         Lists available resource groups. If you need to create a new resource
   group            group, use the Azure portal , and then rerun this tool.

   Location         Read only. Determined by your virtual network's location

   VM Size          Choose a size to fit your workload. Microsoft recommends the
                    Standard_DS3_v2.

   Operating        Read only. The tool uses Windows Server 2019.
   system

   Disk type        Read only. The tool uses Premium SSD for best performance.

   Virtual          Read only.
   network

   Subnet           Select the subnet to use. If you need to create a new subnet, use the
                    Azure portal .

   Machine          Enter the name of the passive site server VM in Azure. It's the same name
   name             shown in the Azure portal .

   Local admin      Enter the name of the local administrative user that the Azure VM creates
   username         before it joins the domain.

   Local admin      The password of the local administrative user. To protect the password
   password         during Azure deployment, store the password as a secret in Azure Key
                    Vault. Then, use the reference here. If needed, create a new one from the
                    Azure portal   .

   Domain FQDN      The fully qualified domain name for the Active Directory domain to join.
                    By default, the tool gets this value from your current machine.

<!-- p.2062 -->

   Name            Description

   Domain          The name of the domain user allowed to join the domain. By default, the
   username        tool uses the name of the currently signed in user.

   Domain          The password of the domain user to join the domain. The tool verifies it
   password        after you select Start. To protect the password during Azure deployment,
                   store the password as a secret in Azure Key Vault. Then, use the reference
                   here. If needed, create a new one from the Azure portal   .

   Domain DNS      Used for joining the domain. By default, the tool uses the current DNS
   IP              from your current machine.

   Type            Read only. It shows Passive Site Server as the type.

    ） Important

    By default the virtual machines are set to No for Use existing Windows Server
    license. If you want to utilize your on-premises Windows Server licenses with
    Software Assurance, configure this setting in the Azure portal           after the
    virtual machines are provisioned. For more information, see Azure Hybrid
    Benefit for Windows Server.

3. To start provisioning the Azure VM, select Start. To monitor the deployment status,
  switch to the Deployments in Azure tab in the tool. To get the latest status, select
  Refresh deployment status.

     Tip

    You can also use the Azure portal        to check the status, find errors, and
    determine potential fixes.

4. When the deployment finishes, go to your SQL Servers, and grant permissions for
  the new Azure VM. For more information, see Site server high availability -
  Prerequisites.

5. To add the Azure VM as a site server in passive mode, select Add site server in
  passive mode.

6. Once the site adds the site server in passive mode, the Site Server High
  Availability tab shows the status.

<!-- p.2063 -->

                                                                                     

   7. Next, switch to the Deployments in Azure tab to finish the deployment.

Site database
The tool doesn't currently have any tasks to migrate the database from on-premises to
Azure. You can choose to move the database from an on-premises SQL Server to an
Azure SQL Server VM. The tool lists the following articles on the Site Database tab to
help:

        Backup and restore the database
        Configure a SQL Server Always On availability group and allow the data to replicate
        Migrate a SQL Server database to an Azure SQL Server VM

Site system roles
   1. Switch to the Site System Roles tab. To provision a new site system role with the
        default settings, select Create new. You can provision roles such as the
        management point, distribution point, and software update point. Not all roles are
        currently available in the tool.

<!-- p.2064 -->

                                                                                      

 2. In the provisioning window, fill in the fields to provision the site role's VM in Azure.
   These details are similar to the above list for the site server.

 3. To start provisioning the Azure VM, select Start. To monitor the deployment status,
   switch to the Deployments in Azure tab in the tool. To get the latest status, select
   Refresh deployment status.

       Tip

      You can also use the Azure portal      to check the status, find errors, and
      determine potential fixes.

 4. Repeat this process to add more site system roles.

 5. Next, go to the Deployments in Azure tab to finish the deployment.

 6. When the deployment finishes, go to the Configuration Manager console to make
   additional changes to the site role.

Deployments in Azure
 1. Once Azure creates the VM, switch to the Deployments in Azure tab in the tool.
   Select Deploy to configure the role with the default settings.

<!-- p.2065 -->

   2. Select Run to start the PowerShell script.

                                                                                     

   3. Repeat this process to configure more roles.

Add site roles to an existing VM
Starting in Configuration Manager version 2002, the tool supports provisioning multiple
site system roles on a single Azure VM. You can add site system roles after the initial
Azure VM deployment has completed. To add a new role to an existing VM, do the
following steps:

   1. On the Deployments in Azure tab, select on a virtual machine deployment that has
     a Completed status.

   2. Select Create new to add an additional role to the virtual machine.

Next steps
Review your changes in the Azure portal

Feedback

<!-- p.2066 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2067 -->

Role-based administration and auditing
tool
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The role-based administration and auditing tool is one of the Configuration Manager
tools. Use this tool for the following tasks:

      Model security roles with specific permissions

      Audit the security scopes and security roles that other users have

Requirements
      Run it on the same computer as the Configuration Manager site server

      You have the Full Administrator, Read-only Analyst, or Security Administrator
      role

      Assign your account to the All security scope and all collections

      (Optional) To analyze report folder security, you need SQL Server access

      (Optional) To analyze report drill-through, run this tool on the site system server
      with the reporting services point role

Procedures

Model permissions for a new role
Use the following procedure to model permissions for a new role that you want to
create:

   1. Run RBAViewer.exe.

   2. Select the base security roles you want to build on, or start from an empty
      permission set. Select the necessary permissions.

   3. Select Analyze to see the user interface this custom role will see.

<!-- p.2068 -->

        ７ Note

        To see whether there's an existing security role that meets your requirements,
        switch to the Similarity tab.

   4. Select Export to save the role as an XML file. Then import it to the Configuration
     Manager console. For more information, see Create custom security roles.

Audit existing security scopes
Use the following procedure to audit all existing administrative users, collections, and
security scopes in Configuration Manager:

   1. Run RBAViewer.exe.

   2. Select the Audit RBA button in the toolbar.

      a. To view the collection-limited relationships in a tree view, switch to the
         Collection Summary tab.

      b. To view objects assigned to a security role, switch to the Scope Summary tab.

Audit a specific user
Use the following procedure to audit the role-based administration configuration for a
specific user:

   1. Run RBAViewer.exe.

   2. Select the Run As button in the toolbar.

   3. Input the specific user name to check the permissions for that account.

   4. The tool displays the security roles assigned to the user or the security group the
     user belongs to. It also displays the objects this user can see and the actions they
     can take in the console.

See also
     Fundamentals of role-based administration

     Configure role-based administration

<!-- p.2069 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2070 -->

Run Meter Summarization Tool
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Run Meter Summarization Tool is one of the Configuration Manager tools. Use it to
immediately trigger the maintenance tasks for software metering summarization on
primary sites. By default, these tasks run as scheduled in Site Maintenance tasks, which
start after 12:00 AM every day.

These tasks summarize the data in the MeterData SQL Server table, and write the
summary results into the FileUsageSummary and MonthlyUsageSummary tables. Then
you see the summarized result in software metering reports. Any Configuration
Manager administrative user who can connect to the primary site database can use this
tool to run summarization.

This tool runs the File Usage Summary and Monthly Usage Summary software
metering data summarization tasks. It summarizes all existing meter data without the
usual 12-hour waiting period. Run it on the SQL Server that hosts the site database. If
summarization is successful, the exit code is set to 0 . If there was an error, the exit code
is 1 .

Usage

Command Line
runmetersumm [sms database name] <delay in hours for summarization <default=0>>

Options

Database name
The name of the site database on the SQL Server.

Delay in hours for summarization
The tool summarizes the software metering usage generated before the delay. By
default, this delay is zero.

<!-- p.2071 -->

Example

Summarize the software metering usage generated 12 hours ago
runmetersumm CCM_ABC <12>

See also
     Maintenance tasks
     Monitor app usage with software metering

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2072 -->

Settings to manage high-risk
deployments for Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

With Configuration Manager, you can configure deployment verification site settings.
These settings warn administrators if they create a high-risk task sequence deployment.
A high-risk deployment is:

      A deployment that's automatically installed

      Has the potential to cause unwanted results

For example, a task sequence with a purpose of Required that deploys an operating
system is considered high-risk.

  ２ Warning

  If you use PXE deployments, and configure device hardware with the network
  adapter as the first boot device, these devices can automatically start an OS
  deployment task sequence without user interaction. Deployment verification
  doesn't manage this configuration. While this configuration may simplify the
  process and reduce user interaction, it puts the device at greater risk for accidental
  reimage.

Deployment verification settings
To reduce the risk of an unwanted high-risk deployment, you can configure size limits in
these deployment verification settings:

      Collection size limits: When you create a deployment, hide collections that include
      more clients than your limit.

         Default size: When you create a deployment, this setting hides collections by
         default that include more clients than this limit. You can still see these
         collections when creating the deployment, but they're hidden by default. The
         default value is 100. To ignore this setting, enter a value of 0.

         Maximum size: When you create a deployment, this setting always hides
         collections with more clients than this limit. The default value is 0, which ignores

<!-- p.2073 -->

        this setting. The Maximum size value must be greater than the Default size
        value.

        For example, you set Default size to 100 and the Maximum size to 1000. When
        you create a high-risk deployment, the Select Collection window only displays
        collections that include fewer than 100 clients. If you clear the setting to Hide
        collections with a member count greater than the site's minimum size
        configuration, the window displays collections that include fewer than 1000
        clients.

     Collections with site system servers: When the target collection includes a
     computer with a site system role, block deployments or require verification before
     creating the deployment. When a deployment is blocked, select a different
     collection that meets the deployment verification criteria to continue creating the
     deployment.

  ７ Note

  High-risk deployments are always limited to custom collections, collections that
  you create, and the built-in Unknown Computers collection. When you create a
  high-risk deployment, you can't select a built-in collection such as All Systems.

Configure deployment verification
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, select Sites, and then select the primary site to
     configure.

   2. In the ribbon, select Properties, and then switch to the Deployment Verification
     tab.

   3. Configure the settings you want to use, and then select OK to save the
     configuration and close the properties.

Next steps
High-impact task sequence settings

Configure sites and hierarchies

<!-- p.2074 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2075 -->

Client installation methods in
Configuration Manager
Article • 10/18/2024

Applies to: Configuration Manager (current branch)

You can use different methods to install the Configuration Manager client software. Use
one method, or a combination of methods. This article describes each method, so you
can learn which one works best for your organization.

Client push installation
Supported client platform: Windows

Advantages

      Can be used to install the client on a single computer, a collection of computers, or
      to the results from a query.

      Can be used to automatically install the client on all discovered computers.

      Automatically uses client installation properties defined on the Client tab in the
      Client Push Installation Properties dialog box.

Disadvantages
      Can cause high network traffic when pushing to large collections.

      Can only be used on computers that have been discovered by Configuration
      Manager.

      Can't be used to install clients in a workgroup.

      A client push installation account must be specified that has administrative rights
      to the intended client computer.

      Windows Firewall must be configured with exceptions on client computers.

      You can't cancel client push installation. Configuration Manager tries to install the
      client on all discovered resources. It retries any failures for up to seven days.

For more information, see How to install clients with client push.

<!-- p.2076 -->

Software update point-based installation
Supported client platform: Windows

Advantages

     Can use your existing software updates infrastructure to manage the client
     software.

     If Windows Server Update Services (WSUS) and group policy settings in Active
     Directory Domain Services are configured correctly, it can automatically install the
     client software on new computers.

     Doesn't require computers to be discovered before the client can be installed.

     Computers can read client installation properties that have been published to
     Active Directory Domain Services.

     If the client is removed, this method reinstalls it.

     Doesn't require you to configure and maintain an installation account for the
     intended client computer.

Disadvantages

     Requires a functioning software updates infrastructure as a prerequisite.

     Must use the same server for client installation and software updates. This server
     must reside in a primary site.

     To install new clients, you must configure a group policy object in Active Directory
     Domain Services with the client's active software update point and port.

     If the Active Directory schema isn't extended for Configuration Manager, you must
     use group policy settings to provision computers with client installation properties.

For more information, see How to install clients with software update-based installation.

Group policy installation
Supported client platform: Windows

Advantages

<!-- p.2077 -->

     Doesn't require computers to be discovered before the client can be installed.

     Can be used for new client installations or for upgrades.

     Computers can read client installation properties that have been published to
     Active Directory Domain Services.

     Doesn't require you to configure and maintain an installation account for the
     intended client computer.

Disadvantages
     If a large number of clients are being installed, it can cause high network traffic.

     If the Active Directory schema isn't extended for Configuration Manager, you must
     use group policy settings to add client installation properties to computers in your
     site.

For more information, see How to install clients with group policy.

Logon script installation
Supported client platform: Windows

Advantages

     Doesn't require computers to be discovered before the client can be installed.

     Supports using command-line properties for CCMSetup.

Disadvantages
     If a large number of clients are being installed over a short time period, it can
     cause high network traffic.

     If users don't frequently log on to the network, it can take a long time to install on
     all client computers.

For more information, see How to install clients with logon scripts.

Manual installation
Supported client platform: Windows, macOS X

<!-- p.2078 -->

Advantages
     Doesn't require computers to be discovered before the client can be installed.

     Can be useful for testing purposes.

     Supports using command-line properties for CCMSetup.

Disadvantages

     No automation, therefore time consuming.

For more information about how to manually install the client on each of platform, see
the following articles:

     How to deploy clients to Windows computers

     How to deploy clients to Macs

Microsoft Intune MDM installation
Supported client platforms: Windows 10 or later

Advantages
     Doesn't require computers to be discovered before the client can be installed.

     Doesn't require you to configure and maintain an installation account for the
     intended client computer.

     Can use modern authentication with Microsoft Entra ID.

     Can install and assign computers on the internet.

     Can automate with Windows Autopilot and Microsoft Intune for co-management.

Disadvantages
     Requires additional technologies outside of Configuration Manager.

     Requires the device have access to the internet, even if it is not internet-based.

For more information, see the following articles:

     How to install clients to Intune MDM-managed Windows devices

<!-- p.2079 -->

     Install and assign Configuration Manager clients using Microsoft Entra ID for
     authentication

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2080 -->

Prerequisites for deploying clients to
Windows computers
Article • 03/28/2024

Applies to: Configuration Manager (current branch)

Deploying Configuration Manager clients in your environment has the following external
dependencies and dependencies within the product. Additionally, each client
deployment method has its own dependencies that must be met for client installations
to be successful.

For more information on the minimum hardware and OS requirements for the
Configuration Manager client, see Supported configurations.

  ７ Note

  The software version numbers shown in this article only list the minimum version
  numbers required.

Use the following information to determine the prerequisites for when you install the
Configuration Manager client on Windows devices.

Dependencies external to Configuration
Manager

Windows components
Many of these components are services or features that Windows enables by default.
Don't disable these components on Configuration Manager clients.

                                                                              ﾉ   Expand table

 Component                   Description

 Windows Installer           Required to support the use of Windows Installer files for
                             applications and software updates.

 Background Intelligent      Required to allow throttled data transfers between the client
 Transfer Service (BITS)     computer and Configuration Manager site systems.
