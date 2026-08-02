---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 601-640"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0601-0640
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0601-0640
family: sccm
documentKind: "doc"
abstract: "that deploys Windows 8). 2. Select the first task in the sequence, and then select the Options tab. 3. Select Add Condition, and then select Registry Setting. 4. In the Root key list, select HKEY_LOCAL_MACHINE. 5. In the Key box, type SOFTWARE\\WOODGROVE. 6. Select not exists for"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 601-640

<!-- p.601 -->

     that deploys Windows 8).

   2. Select the first task in the sequence, and then select the Options tab.

   3. Select Add Condition, and then select Registry Setting.

   4. In the Root key list, select HKEY_LOCAL_MACHINE.

   5. In the Key box, type SOFTWARE\WOODGROVE.

   6. Select not exists for the condition. In this case, the task will run, and the sequence
     continue only if the key does not exist.

   7. Optionally, the condition could check for the nonexistence of a value if the value
     name is typed in the Value name box.

   8. If a condition other than exists/not exists was used, specify a value and value type.

   9. Select OK.

WMI Queries in Conditions
Use the WMI Query condition to run any WMI query. The condition is evaluated as True
if the query returns at least one result. For example, consider that a deployment team
needs to upgrade the operating system of all servers of a given model—Dell 1950, for
instance. You can use a WMI query to check each computer's model and proceed with
the deployment only if the right model is found.

To add a WMI Query condition to a task sequence step

   1. In the Configuration Manager console or in the Deployment Workbench, in the
     task sequence editor, edit task_sequence (where task sequence is the task sequence
     that will upgrade the servers).

   2. Select the first task in the sequence, and then select the Options tab.

   3. Select Add Condition, and then select Query WMI.

   4. In the WMI Namespace box, type root\cimv2.

   5. In the WQL Query box, type Select * From Win32_ComputerSystem WHERE
     Model LIKE "%Dell%%1950%". Select OK.

Installed Software in Conditions

<!-- p.602 -->

Use an Installed Software condition to check if a particular piece of software is currently
installed on a target computer. Only software installed using Microsoft Installer (MSI)
files can be evaluated using this condition. As an example, imagine that you want to
upgrade the operating system of all servers except those running Microsoft SQL Server
2012.

To add an Installed Software condition to a task sequence step

   1. In the Configuration Manager console or in the Deployment Workbench, in the
        task sequence editor, edit task_sequence (where task sequence is the task sequence
        that will upgrade the servers).

   2. Select the first task in the sequence, and then select the Options tab.

   3. Select Add Condition, and then select Installed Software.

   4. Select Browse, and then select the MSI file for SQL Server 2012.

   5. Select the Match this specific product check box to specify that only computers
        with SQL Server 2012 and not any other versions are the target computers this
        query should detect.

   6. Select OK.

Complex Conditions
Multiple conditions can be grouped using IF statements to create complex conditions.
For instance, imagine that a particular step should only be run for Contoso 1950
computers running Windows Server 2003 or Windows Server 2008. Written as a
programmatic IF statement, it would look similar to the following:

IF ((Computer Model IS "Contoso 1950") AND (operating system=2003 OR operating

system=2008))

To add a complex condition

   1. In the Configuration Manager console or in the Deployment Workbench, in the
        task sequence editor, edit task_sequence (where task sequence is the task sequence
        that will upgrade the servers).

   2. Select the task sequence step to which to add the condition, and then select the
        Options tab.

   3. Select Add condition, select If Statement, and then select All conditions. Select
        OK.

<!-- p.603 -->

   4. Select the condition statement, select Add condition, and then select WMI Query.

   5. Ensure root\cimv2 is specified as the WMI namespace, and then, in the WQL
     Query box, type SELECT * FROM Win32_ComputerSystem WHERE
     ComputerModel LIKE "%Contoso%1950%". Select OK.

   6. Select the IF statement, and then select Add condition. Select If statement, and
     then select Any condition. Select OK.

   7. Select the second IF statement. Select Add condition, and then select Operating
     System Version.

   8. In the Architecture box, select the architecture for the servers. For this example,
     select x86.

   9. In the Operating system box, select the operating system and version. For this
     example, select x86 Windows 2003 original release. Select OK.

 10. Select the second IF statement. Select Add condition, and then select Operating
     System Version.

 11. In the Architecture box, select the architecture for the servers. For this example,
     select x86.

 12. In the Operating system box, select the operating system and version. For this
     example, select x86 Windows 2008 original release. Select OK.

Creating a Highly Scalable LTI Deployment
Infrastructure
In this scenario, no electronic software distribution is available for the deployment
infrastructure to leverage, so you use MDT to build a fully automated LTI deployment
infrastructure. The scalable LTI infrastructure uses SQL Server, Windows Deployment
Services, and Windows Server 2003 Distributed File System Replication (DFS-R)
technologies.

Scale the LTI infrastructure by:

     Ensuring that the appropriate infrastructure exists as described in Ensuring That
     the Appropriate Infrastructure Exists

     Adding content to MDT as described in Adding Content to MDT

<!-- p.604 -->

     Preparing Windows Deployment Services as described in Preparing Windows
     Deployment Services

     Configuring DFS-R as described in Configuring Distributed File System Replication

     Preparing for SQL Server replication as described in Preparing for SQL Server
     Replication

     Configuring SQL Server replication as described in Configuring SQL Server
     Replication

     This scenario presumes that MDT is configured on a master deployment server and
     that the configuration of the MDT DB has already been completed as discussed at
     the beginning of this document.

Ensuring That the Appropriate Infrastructure Exists
The highly scalable LTI deployment infrastructure uses a hub-and-spoke topology for
replication of content; therefore, first nominate a deployment server in the production
environment that will perform the role of the master deployment server. The following
lists the required components for the master deployment server.

                                                                              ﾉ   Expand table

 Required component            Purpose/comment

 Windows Server 2003 R2        Required to support DFS-R

 MDT                           Contains the master copy of the deployment share

 SQL Server 2005               Must be a full version to allow replication of the MDT DB

 DFS-R                         Required for replication of the deployment share

 Windows Deployment Services   Required to allow network PXE-based installations to be initiated

When you have selected the master deployment server, provision additional servers at
each site to support LTI deployments. The following lists the required components for
the child deployment server.

                                                                              ﾉ   Expand table

 Required component                  Purpose/comment

 Windows Server 2003 R2              Required to support DFS-R

<!-- p.605 -->

 Required component                  Purpose/comment

 Microsoft SQL Server 2005 Express   Receives replicated copies of the MDT DB
 Edition

 DFS-R                               Required for replication of deployment share

 Windows Deployment Services         Required to allow network PXE-based installations to be
                                     initiated

  ７ Note

  Windows Deployment Services must be set up and configured on each child server,
  but it is not necessary to add boot or installation images.

Adding Content to MDT
Populate the master deployment server with content using the Deployment Workbench,
and create and populate the MDT DB as described in the following sections. For
information on populating the database with:

     Applications, see the section, "Configuring Applications in the Deployment
     Workbench", in the MDT document Using the Microsoft Deployment Toolkit

     Operating systems, see the section, "Configuring Operating Systems in the
     Deployment Workbench", in the MDT document Using the Microsoft Deployment
     Toolkit

     Operating system packages, see the section, "Configuring Packages in the
     Deployment Workbench", in the MDT document Using the Microsoft Deployment
     Toolkit

     Device drivers, see the section, "Configuring Device Drivers in the Deployment
     Workbench", in the MDT document Using the Microsoft Deployment Toolkit

     Task sequences, see the section, "Configuring Task Sequences in the Deployment
     Workbench", in the MDT document Using the Microsoft Deployment Toolkit

  ７ Note

  Ensure that the LiteTouchPE_x86.wim file created when the deployment share is
  updated has been added to Windows Deployment Services.

<!-- p.606 -->

Preparing Windows Deployment Services
Because the LiteTouchPE_x86.wim file will be replicated on a periodic basis through the
DFS-R replication group, the boot configuration data store must be updated periodically
to reflect the newly replicated Windows PE environment. Perform the following steps on
each of the deployment servers.

To prepare Windows Deployment Services

   1. Open a Command Prompt window.

   2. Type WDSUtil/set-server/BCDRefreshPolicy/Enabled:yes/RefreshPeriod:60, and
       then press ENTER.

  ７ Note

  In the example presented here, the refresh period is set to 60 minutes; however,
  you could configure this value to replicate during a period equal to that of the DFS-
  R.

Configuring Distributed File System Replication
When scaling the LTI deployment architecture, you use DFS-R as the basis for replicating
the content from both the MDT deployment share and the Windows PE Lite Touch boot
environment and from the master deployment server to the child deployment servers.

  ７ Note

  Ensure that DFS-R is installed before performing the following steps.

To configure DFS-R to replicate the deployment content

   1. Open DFS Management console.

   2. In the DFS Management console, expand DFS Management.

   3. Right-click Replication, and then select New Replication Group.

   4. In the New Replication Group Wizard, on the Replication Group Type page, select
       New Multipurpose Replication Group.

   5. Select Next.

<!-- p.607 -->

 6. On the Name and Domain page, type the following information:

          In the Name for replication group box, type a name for the replication group
          —for example, MDT 2010 Replication Group.

          In the Optional description of replication group box, type a description of
          the replication group—for example, Group for replication of MDT 2010 data.

          Ensure that the Domain box contains the correct domain name.

 7. Select Next.

 8. On the Replication Group Members page, perform these steps:

    a. Select Add.

    b. Type the names of all servers that are to be members of this replication group—
      for example, all child deployment servers and the master deployment server.

    c. Select OK.

 9. Select Next.

10. On the Topology Selection page, select Hub and Spoke, and then select Next.

11. On the Hub Members page, select the master deployment server, and then select
   Add.

12. Select Next.

13. On the Hub and Spoke Connections page, ensure that for each child deployment
   server the master deployment server listed is the Required Hub Member.

14. Select Next.

15. On the Replication Group Schedule and Bandwidth page, specify a schedule for
   replicating the content between servers.

16. Select Next.

17. On the Primary Member page, in the Primary Member box, select the master
   deployment server.

18. Select Next.

19. On the Folders to Replicate page, select Add, and then perform these steps:

<!-- p.608 -->

    a. In the Local Path of the folder to replicate box, select Browse to go to the
      X:\Deployment folder (where X is the drive letter on the deployment server).

    b. Select Use name based on path.

    c. Select OK.

    d. Select Add.

    e. In the Add Folder to Replicate dialog box, select Browse to go to the
      X:\RemoteInstall\Boot folder.

    f. Select Use name based on path.

20. Select Next.

21. On the Local Path of Distribution on Other Members page, perform these steps:

    a. Select all the members in the distribution group, and then select Edit.

    b. In the Edit Local Path dialog box, select Enabled.

    c. Type the path where the Deployment Share folder should be stored on the child
      deployment server—for example, X:\Deployment (where X is the drive letter on
      the deployment server).

    d. Select OK.

22. Select Next.

23. On the Local Path of Boot on Other Members page, perform these steps:

    a. Select all the members in the distribution group, and then select Edit.

    b. In the Edit Local Path dialog box, select Enabled.

    c. Type the path where the Boot folder should be stored on the child deployment
      server—for example, X:\RemoteInstall\Boot (where X is the drive letter on the
      deployment server).

    d. Select OK.

24. Select Next.

25. On the Remote Settings and Create Replication Group page, select Create to
   complete the New Replication Group Wizard.

26. On the Confirmation page, select Close to close the wizard.

<!-- p.609 -->

  ７ Note

  Ensure that the new replication group is now listed beneath the Replication node.

Preparing for SQL Server Replication
Before SQL Server replication can be configured, complete several pre-configuration
steps to ensure that the deployment servers are correctly configured.

To prepare for SQL Server replication on the master deployment server

   1. Create a folder to store the database snapshots, and then configure the folder as a
     share.

       ７ Note

       For more information about securing the snapshot folder, see Secure the
       Snapshot Folder.

   2. Ensure that the SQL Server Browser service is enabled and set to Automatic.

   3. In the SQL Server Surface Area Configuration box, select Local and Remote
     connections.

     To prepare for SQL Server replication on the child deployment server

   4. In the SQL Server Surface Area Configuration box, select Local and Remote
     connections.

   5. Optionally, create an empty database to host the replicated MDT DB.

  ７ Note

  This database must be given the same name as the MDT DB on the master
  deployment server. For example, if the MDT DB on the master deployment server is
  called MDTDB, create an empty database called MDTDB on the child deployment
  server.

Configuring SQL Server Replication

<!-- p.610 -->

After configuring the replication of files and folders required to build the deployment
infrastructure, configure SQL Server to replicate the MDT DB.

  ７ Note

  It is also possible to maintain only a single central MDT DB; however, by
  maintaining a replicated version of the MDT DB, greater control can be maintained
  over data transferring across the wide area network (WAN).

SQL Server 2005 uses a replication model that is similar to a magazine distribution
model:

   1. A magazine is made available (published) by a publisher.

   2. Distributors are used to distribute the publication.

   3. Readers can subscribe to a publication so that publication is delivered to the
     subscriber periodically (a push subscription).

     This terminology is used through the SQL Server replication setup and
     configuration wizards.

Configure a SQL Server Publisher

To configure the master deployment server as a SQL Server publisher, perform these
steps:

   1. Open SQL Server Management Studio.

   2. Right-click the Replication node, and then select Configure Distribution.

   3. In the Configure Distribution Wizard, select Next.

   4. On the Distributor page, select will act as its own Distributor; SQL Server will
     create a distribution database and log, and then select Next.

   5. On the Snapshot Folder page, in the Preparing for SQL Server Replication section,
     type the UNC path to the snapshot folder created.

   6. On the Distribution Database page, select Next.

   7. On the Publishers page, select the master deployment server to set it as the
     distributor, and then select Next.

   8. On the Wizard Actions page, select Configure Distribution, and then select Next.

<!-- p.611 -->

   9. Select Finish, and then select Close when the wizard is finished.

Enable the MDT DB for Replication
To enable the MDT DB for replication on the master deployment server, perform these
steps:

   1. In SQL Server Management Studio, right-click the Replication node, and then
     select Publisher Properties.

   2. On the Publisher Properties page, perform these steps:

         a. Select Publisher Databases.

         b. Select the MDT DB, and then select Transactional.

         c. Select OK.

     The MDT DB is now configured for transactional and snapshot replication.

Create a Publication of the MDT DB

To create a publication of the MDT DB to which the child deployment servers can
subscribe, perform these steps:

   1. In SQL Server Management Studio, expand Replication, right-click Local
     Publications, and then select New Publication.

   2. In the New Publication Wizard, select Next.

   3. On the Publication Database page, select the MDT DB, and then select Next.

   4. On the Publication Type page, select Snapshot publication, and then select Next.

   5. On the Articles page, select all Tables, Stored Procedures, and Views, and then
     select Next.

   6. On the Articles Issues page, select Next.

   7. On the Filter Table Rows page, select Next.

   8. On the Snapshot Agent page, perform these steps:

         a. Select Create a snapshot immediately and keep the snapshot available to
           initialize subscriptions.

<!-- p.612 -->

      b. Select Schedule the Snapshot Agent to run at the following times.

      c. Select Change.

        ７ Note

        Specify a schedule that will occur one hour before the database replicates.

   9. Select Next.

 10. On the Agent Security page, select the account under which the snapshot agent
     will run, and then select Next.

 11. On the Wizard Actions page, select Create the publication, and then select Next.

 12. On the Complete the Wizard page, in the publication name box, type a
     descriptive publication name.

 13. Select Finish to complete the wizard, and then select Close when the wizard has
     created the publication.

        ７ Note

        The publication will now be visible beneath the Local Publications node in SQL
        Server Management Studio.

Subscribe Child Deployment Servers to the Published MDT DB
Now that the MDT DB has been published, you can add the child deployment servers as
subscribers to this publication; that is, that they will receive a copy of the database on a
schedule so that during a deployment the client computers can query a database that is
local to the network instead of going across the WAN.

To subscribe the child deployment servers to the MDT DB publication

   1. In SQL Server Management Studio, go to Replication/Local Publications.

   2. Right-click the publication created in the previous section, and then select New
     Subscriptions.

   3. In the New Subscriptions Wizard, select Next.

   4. On the Publication page, select the publication created in the previous section.

<!-- p.613 -->

 5. On the Distribution Agent Location page, select Run all agents at the Distributor
   SERVERNAME (push subscriptions), and then select Next.

 6. On the Subscribers page, add each of the child deployment servers by performing
   the following steps:

    a. Select Add Subscriber, and then select Add SQL Server Subscriber.

    b. Add each child deployment server.

    c. For each child deployment server added, in the Subscription Database box,
      select the empty MDT DB on that child deployment server.

      ７ Note

      If the empty MDT DB has not yet been created, in the Subscription Database
      box, select the option to create a new database.

      ７ Note

      This database must be given the same name as the MDT DB on the master
      deployment server. For example, if the MDT DB on the master deployment
      server is called MDTDB, create an empty database called MDTDB on the child
      deployment server.

 7. Select Next.

 8. On the Distribution Agent Security page, select ... to open the Distribution Agent
   Security dialog box.

 9. Type the details of the account to use for the distribution agent, and then select
   Next.

10. On the Synchronization Schedule page, perform these steps:

    a. In the Agent Schedule box, select <Define schedule>.

    b. Specify the schedule that should be used to replicate the database between
      master and child deployment servers, and then select Next.

11. On the Initialize Subscription page, select Next.

12. On the Wizard Actions page, select Create the subscription(s), and then select
   Next.

<!-- p.614 -->

 13. Select Finish, and then select Close when the wizard has successfully finished.

     SQL Server replication is now configured, and the MDT DB will be replicated from
     the master deployment server to all child deployment servers that have been
     subscribed to it on a periodic basis.

Configure CustomSettings.ini

The LTI deployment infrastructure has now been successfully created, and each location
will contain an LTI deployment server, with a replicated copy of:

     The deployment share

     The MDT DB

     The LiteTouchPE_x86 Windows PE environment that has been added to Windows
     Deployment Services

     Now, you can configure the CustomSettings.ini file for the deployment share to
     use the deployment content (deployment share and database) from its local
     deployment server, the server that delivers the LiteTouchPE_x86.wim environment
     through Windows Deployment Services.

     When the LiteTouchPE_x86.wim file is delivered from Windows Deployment
     Services, a registry key is configured with the name of the Windows Deployment
     Services server you are using. MDT captures this server name in a variable
     (%WDSServer%) that you can use to configure CustomSettings.ini.

     To always use the local LTI deployment server

  ７ Note

  The following procedure assumes that the deployment share has been created and
  set as the Deployment$ share.

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

   3. In the Actions pane, select Properties.

<!-- p.615 -->

 4. Select the Rules tab, and then modify the CustomSettings.ini file to configure the
      following properties:

           For each SQL Server section added, configure SQLServer to use the server
           name **%WDSServer%—**for example, SQLServer=%WDSServer%.

           If configuring DeployRoot, configure DeployRoot to use the %WDSServer%
           variable—for example, DeployRoot=\\%WDSServer%\Deployment$.

 5. Select Edit Bootstrap.ini.

 6. Configure BootStrap.ini to use the %WDSServer% property by adding or changing
      the DeployRoot value to DeployRoot=\\%WDSServer%\Deployment$.

 7. Select File, and then select Save to save the changes to the BootStrap.ini file.

 8. Select OK.

      The deployment share and LiteTouchPE_x86.wim Windows PE environment need to
      be updated.

 9. In the Actions pane, select Update Deployment Share.

      The Update Deployment Share Wizard starts.

10. On the Options page, select the desired options for updating the deployment
      share, and then select Next.

11. On the Summary page, verify the details are correct, and then select Next.

12. On the Confirmation page, select Finish.

      The following example illustrates CustomSettings.ini after performing the steps
      outlined in this section.

      Sample CustomSettings.ini Configured for Scalable LTI Deployment
      Infrastructure

ini

[Settings]
Priority=CSettings,CPackages, CApps, CAdmins, CRoles, Default
Properties=MyCustomProperty

[Default]
OSInstall=Y
ScanStateArgs=/v:5 /o /c
LoadStateArgs=/v:5 /c /lac

<!-- p.616 -->

 [CSettings]
 SQLServer=%WDSServer%
 Instance=
 Database=MDTDB
 Netlib=DBNMPNTW
 SQLShare=
 Table=ComputerSettings
 Parameters=UUID, AssetTag, SerialNumber, MacAddress
 ParameterCondition=OR

 [CPackages]
 SQLServer=%WDSServer%
 Database=MDTDB
 Netlib=DBNMPNTW
 SQLShare=
 Table=ComputerPackages
 Parameters=UUID, AssetTag, SerialNumber, MacAddress
 ParameterCondition=OR
 Order=Sequence

 [CApps]
 SQLServer=%WDSServer%
 Database=MDTDB
 Netlib=DBNMPNTW
 SQLShare=
 Table=ComputerApplications
 Parameters=UUID, AssetTag, SerialNumber, MacAddress
 ParameterCondition=OR
 Order=Sequence

 [CAdmins]
 SQLServer=%WDSServer%
 Database=MDTDB
 Netlib=DBNMPNTW
 SQLShare=
 Table=ComputerAdministrators
 Parameters=UUID, AssetTag, SerialNumber, MacAddress
 ParameterCondition=OR

 [CRoles]
 SQLServer=%WDSServer%
 Database=MDTDB
 Netlib=DBNMPNTW
 SQLShare=
 Table=ComputerRoles
 Parameters=UUID, AssetTag, SerialNumber, MacAddress
 ParameterCondition=OR

Selecting a Local MDT Server When Multiple
Servers Exist

<!-- p.617 -->

In this scenario, multiple MDT servers are being used to support a high volume of
simultaneous deployments and deployments across multiple sites. When an LTI
deployment is initialized, the default behavior is to request a path to the MDT server to
connect to and access the required files to begin the deployment process.

The Windows Deployment Wizard can use the LocalServer.xml file to present a choice of
known deployment servers for each location.

Use the LocationServer.xml file by:

     Understanding the purpose and use of LocationServer.xml as described in
     Understanding LocationServer.xml

     Creating the LocationServer.xml file as described in Creating the
     LocationServer.xml File

     Adding the LocationServer.xml file to the Extra Files directory as described in
     Adding the LocationServer.xml File to the Extra Files Directory

     Updating the BootStrap.ini file as described in Updating the BootStrap.ini File

     Updating the deployment share as described in Updating the Deployment Share

     This scenario assumes that MDT is configured on a deployment server.

Understanding LocationServer.xml
First, you must understand How MDT uses LocationServer.xml. During LTI, MDT scripts
read and process the BootStrap.ini file to gather initial information about the
deployment. This happens before a connection has been made to the deployment
server. Therefore, the DeployRoot property is commonly used to specify in the
BootStrap.ini file the deployment server to which it should make a connection.

If the BootStrap.ini file does not contain a DeployRoot property, MDT scripts load a
wizard page to prompt the user for a path to the deployment server. While initializing
the HTML Application (HTA) wizard page, MDT scripts check for the existence of the
LocationServer.xml file and, if it exists, use LocationServer.xml to display available
deployment servers.

Understand When to Use LocationServer.xml

MDT offers multiple ways to determine which server to connect to during an LTI
deployment. Different methods for locating the deployment server are best suited for

<!-- p.618 -->

different scenarios; therefore, it is important to understand when to use
LocationServer.xml.

MDT provides several methods for automatically discovering and using the most
appropriate deployment server. These methods are listed in the following table.

                                                                                 ﾉ   Expand table

 Method               Details

 %WDSServer%          This method is used when the MDT server is co-hosted on the Windows
                      Deployment Services server.

                      When an LTI deployment is initiated from Windows Deployment Services, an
                      environmental variable—%WDSServer%—is created and populated with the
                      name of the Windows Deployment Services server.

                      The DeployRoot variable can use this variable to automatically connect to a
                      deployment share on the Windows Deployment Services server—for
                      example:

                      DeployRoot=\\%WDSServer%\Deployment$

 Location-based       MDT can use location-based automation in the BootStrap.ini file to determine
 automation           the server to which it should deploy.

                      Use the Default Gateway property to distinguish between different locations;
                      for each Default Gateway, a different MDT server is specified.

                      For more information about using location-based automation, refer to
                      "Selecting the Methods for Applying Configuration Settings".

Each approach listed in the preceding table offers one way to automate the selection of
the deployment server at a given location for certain scenarios. These approaches are
targeted to specific scenarios—for example, when the MDT server is co-hosted with
Windows Deployment Services.

There are other scenarios in which these approaches are not suitable—for example, if
there are multiple deployment servers at a given location or automation logic is not
possible (for example, the network is not segmented enough to allow location
determination or the MDT server is separated from Windows Deployment Services).

In these scenarios, the LocationServer.xml file provides a flexible way to present this
information at deployment time without requiring knowledge of server names and
deployment share names.

<!-- p.619 -->

Creating the LocationServer.xml File
To present a list of available deployment servers during an LTI deployment, create a
LocationServer.xml file that contains details about each server. There is no default
LocationServer.xml file in MDT, so create one using the following guidance.

Create a LocationServer.xml File to Support Multiple Locations
The simplest method for creating and using LocationServer.xml is to create a
LocationServer.xml file and add entries for each deployment server in the environment
(this can be either at the same location or at different locations).

Construct the LocationServer.xml file by creating a new section for each server, and then
adding the following information:

     A unique identifier

     A location name, used to present an easily identifiable name for that location

     A UNC path to the MDT server for that location

     The following illustrates how the LocationServer.xml file is created using each of
     these properties using a sample LocationServer.xml file configured for multiple
     locations.

     Example LocationServer.xml File to Support Multiple Locations

  XML

  <?xml version="1.0" encoding="utf-8" ?>
  <servers>
      <QueryDefault></QueryDefault>
      <server>
          <serverid>1</serverid>
          <friendlyname>
            Contoso HQ, Seattle, USA
          </friendlyname>
          <UNCPath>\\STLDS01\Deployment$</UNCPath>
      </server>
      <server>
          <serverid>2</serverid>
          <friendlyname>
            Contoso NYC, New York, USA
          </friendlyname>
          <UNCPath>\\NYCDS01\Deployment$</UNCPath>
      </server>
  </servers>

<!-- p.620 -->

Using this format, specify different server entries for each location or for situations in
which there are multiple servers within a single location by specifying a different server
entry for each server at that location, as shown in the following example.

Example LocationServer.xml File to Support Multiple Servers at Multiple Locations

  XML

  <?xml version="1.0" encoding="utf-8" ?>
  <servers>
      <QueryDefault></QueryDefault>
      <server>
          <serverid>1</serverid>
          <friendlyname>
            Contoso HQ DS1, Seattle, USA
          </friendlyname>
          <UNCPath>\\STLDS01\Deployment$</UNCPath>
      </server>
      <server>
          <serverid>2</serverid>
          <friendlyname>
            Contoso HQ DS2, Seattle, USA
          </friendlyname>
          <UNCPath>\\STLDS02\Deployment$</UNCPath>
      </server>
  </servers>

Create a LocationServer.xml File to Load Balance Multiple Servers
at Different Locations
Using LocationServer.xml, specify multiple servers per location entry, and then perform
basic load balancing so that when a location is chosen, MDT automatically selects a
deployment server from the list of available servers. To provide this functionality, the
LocationServer.xml file supports specifying a weighting metric.

The following illustrates a sample LocationServer.xml file configured for multiple servers
at different locations.

Example LocationServer.xml File for Different Locations

  XML

  <?xml version="1.0" encoding="utf-8" ?>
  <servers>
      <QueryDefault></QueryDefault>
      <server>
          <serverid>1</serverid>
          <friendlyname>

<!-- p.621 -->

            Contoso HQ, Seattle, USA
          </friendlyname>
          <Server1>\\STLDS01\Deployment$</Server1>
          <Server2>\\STLDS02\Deployment$</Server2>
          <Server3>\\STLDS03\Deployment$</Server3>
          <Server weight="1">\\STLDS01\Deployment$</Server>
          <Server weight="2">\\STLDS02\Deployment$</Server>
          <Server weight="4">\\STLDS03\Deployment$</Server>
      </server>
      <server>
          <serverid>2</serverid>
          <friendlyname>
            Contoso NYC, New York, USA
          </friendlyname>
          <UNCPath>\\NYCDS01\Deployment$</UNCPath>
      </server>
  </servers>

Specify the weighting metric by using the <server weight> tag, which MDT uses in the
server-selection process. The likelihood of a server being selected is calculated by:

Server weight/sum of all server weights

In the previous example, the three servers at Contoso HQ are listed as 1, 2, and 4. The
likelihood of a server with a weighting of 2 being selected becomes 2 in 7. Therefore, to
use the weighting system, determine the capacity of the servers available at a location,
and weight each server by the server's capacity in relation to each of the other servers.

Adding the LocationServer.xml File to the Extra Files
Directory
After you have created the LocationServer.xml file, add it to the LiteTouch_x86 and
LiteTouch_x64 Windows PE boot images in the X:\Deploy\Control folder. Using the
Deployment Workbench, add other files and folders to these Windows PE images by
specifying an additional directory to add in the deployment share properties.

To add LocationServer.xml to the deployment share

   1. Create a folder called Extra Files in the root deployment share folder (for example,
     D:\Production Deployment Share\Extra Files).

   2. Create a folder structure in the Extra Files folder that mirrors the Windows PE
     location where the additional file should reside.

     For example, the LocationServer.xml file must reside in the \Deploy\Control folder
     in Windows PE; therefore, create the same folder structure under Extra Files (for
     example, D:\Production Deployment Share\Extra Files\Deploy\Control).

<!-- p.622 -->

   3. Copy LocationServer.xml to the deployment_share\Extra Files\Deploy\Control folder
     (where deployment_share is the fully qualified path to the root folder of the
     deployment share).

   4. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   5. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

   6. In the Actions pane, select Properties.

   7. In the deployment_shareProperties dialog box (where deployment_share is the
     name of the deployment share), perform these steps:

      a. Select the Windows PE platform Settings tab (where platform is the
        architecture of the Windows PE image to be configured).

      b. In the Windows PE Customizations section, in the Extra directory to add box,
        type path (where path is the fully qualified path to the Extra Files folder—for
        example, D:\Production Deployment Share\Extra Files), and then select OK.

Updating the BootStrap.ini File
When you create a deployment share using the Deployment Workbench, a DeployRoot
property is automatically created and populated in the BootStrap.ini file. Because the
LocationServer.xml file is used to populate the DeployRoot property, you must remove
this value from the BootStrap.ini file.

To remove the DeployRoot property from BootStrap.ini

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

   3. In the Actions pane, select Properties.

   4. In the deployment_shareProperties dialog box (where deployment_share is the
     name of the deployment share), select the Rules tab, and then select Edit
     BootStrap.ini.

<!-- p.623 -->

   5. Remove the DeployRoot value (for example, DeployRoot=\\Server\Deployment$).

   6. Select File, and then select Save to save the changes to the BootStrap.ini file.

   7. Select OK to submit the changes.

Updating the Deployment Share
The deployment share must next be updated to generate a new LiteTouch_x86 and
LiteTouch_x64 boot environment that contains the LocationServer.xml file and the
updated BootStrap.ini file.

To update the deployment share

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

   3. In the Actions pane, select Update Deployment Share.

     The Update Deployment Share Wizard starts.

   4. On the Options page, select the desired options for updating the deployment
     share, and then select Next.

   5. On the Summary page, verify the details are correct, and then select Next.

   6. On the Confirmation page, select Finish.

  ７ Note

  When the update process has finished, add the new LiteTouch_x86 and
  LiteTouch_x64 Windows PE environments back into Windows Deployment Services,
  or burn them to boot media to use during deployment.

Replacing an Existing Computer with a New
Computer Using Lite Touch Installation
You can use MDT to deploy an image to a new computer that will substitute an existing
computer in the enterprise architecture. This situation could arise when upgrading from

<!-- p.624 -->

one operating system to another (a new operating system could require new hardware)
or if the organization needs newer, faster computers for existing applications.

When replacing an existing computer with a new computer, Microsoft recommends
taking into account all settings that will be migrated from one computer to another,
such as user accounts and user state data. In addition, it is important to create a
recovery solution in case the migration fails.

In this sample deployment, replace the existing computer (WDG-EXIST-01) with a new
computer (WDG-NEW-02) in the CORP domain by capturing user state data from WDG-
EXIST-01 and saving it to a network share. Then, deploy an existing image to WDG-
NEW-02, and finally restore the captured user state data to WDG-NEW-02. The
deployment will be performed from a deployment server (WDG-MDT-01).

In MDT, use the Standard Client Replace Task Sequence template to create a task
sequence that will perform all the necessary deployment tasks.

This demonstration assumes that:

     MDT has been installed on the deployment server (WDG MDT 01)

     The deployment share has already been created and populated, including
     operating system images, applications, and device drivers

     An image of a reference computer has already been captured and will be deployed
     to the new computer (WDG NEW 02)

     A network shared folder (UserStateCapture$) has been created and shared on the
     deployment server (WDG MDT 01) with the appropriate share permissions

     A deployment share should exist prior to beginning this sample. For more
     information about creating a deployment share, see the section, "Managing
     Deployment Shares in the Deployment Workbench", in the MDT document Using
     the Microsoft Deployment Toolkit.

Step 1: Create a Task Sequence to Capture the User State
Create MDT task sequences in the Task Sequences node in the Deployment Workbench
using the New Task Sequence Wizard. To perform the first part of the Replace Computer
deployment scenario (capturing the user state on the existing computer), select the
Standard Client Replace Task Sequence template in the New Task Sequence Wizard.

To create a task sequence to capture the user state in the Replace Computer
deployment scenario

<!-- p.625 -->

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/ deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share to configure).

   3. In the Actions pane, select New Task Sequence.

     The New Task Sequence Wizard starts.

   4. Complete the New Task Sequence Wizard by using the following information.
     Accept the default values unless otherwise specified.

                                                                                 ﾉ   Expand table

      On this wizard   Do this
      page

      General          1. In Task sequence ID, type VISTA_EXIST.
      Settings         2. In Task sequence name, type Perform Replace Computer Scenario on
                       Existing Computer.
                       3. Select Next.

      Select           In The following task sequence templates are available. Select the one
      Template         you would like to use as a starting point, select Standard Client Replace
                       Task Sequence, and then select Next.

      Summary          Verify that the configuration details are correct, and then select Next.

      Confirmation     Select Finish.

     The New Task Sequence Wizard finishes, and the VISTA_EXIST task sequence is
     added to the list of task sequences.

Step 2: Create a Task Sequence to Deploy Operating
System and Restore the User State
Create MDT task sequences in the Task Sequences node in the Deployment Workbench
by using the New Task Sequence Wizard. To perform the second part of the Replace
Computer deployment scenario (deploying the operating system, and then restoring the
user state on the existing computer), select the Standard Client Task Sequence template
in the New Task Sequence Wizard.

To create a task sequence to deploy the user state in the Replace Computer
deployment scenario

<!-- p.626 -->

1. Select Start, and then point to All Programs. Point to Microsoft Deployment
  Toolkit, and then select Deployment Workbench.

2. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares/deployment_share/Task Sequences (where
  deployment_share is the name of the deployment share to configure).

3. In the Actions pane, select New Task Sequence.

  The New Task Sequence Wizard starts.

4. Complete the New Task Sequence Wizard by using the following information.
  Accept the default values unless otherwise specified.

                                                                           ﾉ   Expand table

   On this        Do this
   wizard page

   General        1. In Task sequence ID, type VISTA_NEW.
   Settings       2. In Task sequence name, type Perform Replace Computer Scenario on
                  New Computer.
                  3. Select Next.

   Select         In The following task sequence templates are available. Select the one
   Template       you would like to use as a starting point, select Standard Client Task
                  Sequence, and then select Next.

   Select OS      In The following operating system images are available to be deployed
                  with this task sequence. Select one to use, select captured_vista_image
                  (where captured_vista_image is the captured image the reference
                  computer added to the Operating Systems node in the Deployment
                  Workbench), and then select Next.

   Specify        Select Do not specify a product key at this time, and then select Next.
   Product Key

   OS Settings    1. In Full Name, type Woodgrove Employee.
                  2. In Organization, type Woodgrove Bank.
                  3. In Internet Explorer Home Page, type
                  http://www.woodgrovebank.com.
                  4. Select Next.

   Admin          In Administrator Password and Please confirm Administrator Password,
   Password       type P@ssw0rd, and then select Finish.

   Confirmation   Select Finish.

<!-- p.627 -->

     The New Task Sequence Wizard finishes, and the VISTA_NEW task sequence is
     added to the list of task sequences.

Step 3: Customize the MDT Configuration Files
When the MDT task sequence has been created, customize the MDT configuration files
that provide the configuration settings for capturing user state information. Specifically,
customize the CustomSettings.ini file by modifying the file in the properties of the
deployment share created earlier in the deployment process. In a later step, the
deployment share will be updated to ensure that the configuration file is updated in the
deployment share.

To customize the MDT configuration files for capturing user state information

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

   3. In the Actions pane, select Properties.

     The Properties dialog box appears.

   4. In the Properties dialog box, select the Rules tab.

   5. On the Rules tab, modify the CustomSettings.ini file to reflect the necessary
     changes as shown in the following example. Make any additional modifications the
     environment requires.

     Customized CustomSettings.ini File

        ini

        [Settings]
        Priority=Default
        Properties=MyCustomProperty

        [Default]
        OSInstall=Y

        UDShare=\\WDG-MDT-01\UserStateCapture$
        UDDir=%OSDCOMPUTERNAME%
        UserDataLocation=NETWORK
        SkipCapture=NO
        SkipAdminPassword=YES

<!-- p.628 -->

       SkipProductKey=YES

  6. In the Properties dialog box, select OK.

  7. Close all open windows and dialog boxes.

Step 4: Configure the Windows PE Options for the
Deployment Share
Configure the Windows PE options for the deployment share in the Deployment Shares
node in the Deployment Workbench.

  ７ Note

  If the device drivers for the existing computer (WDG-EXIST-01) and the new
  computer (WDG-NEW-01) are included with Windows Vista, skip this step and
  proceed with the following step.

To configure the Windows PE options for the deployment share

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

  3. In the Actions pane, select Properties.

     The Properties dialog box appears.

  4. In the Properties dialog box, on the Windows PE platform Components tab
     (where platform is the architecture of the Windows PE image to be configured), in
     Selection profile, select device_drivers (where device_drivers is the name of the
     device driver selection profile), and then select OK.

Step 5: Update the Deployment Share
After configuring the Windows PE options for the deployment share, update the
deployment share. Updating the deployment share updates all the MDT configuration
files and generates a customized version of Windows PE. The customized version of

<!-- p.629 -->

Windows PE is used to start the reference computer and initiate the LTI deployment
process.

To update the deployment share in the Deployment Workbench

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

   3. In the Actions pane, select Update DeploymentShare.

     The Update Deployment Share Wizard starts.

   4. On the Options page, select the desired options for updating the deployment
     share, and then select Next.

   5. On the Summary page, verify the details are correct, and then select Next.

   6. On the Confirmation page, select Finish.

     The Deployment Workbench starts updating the deployment share. The
     Deployment Workbench creates the LiteTouchPE_x86.iso and LiteTouchPE_x86.wim
     files (for 32-bit target computers) or LiteTouchPE_x64.iso and LiteTouchPE_x64.wim
     files (for 64-bit target computers) in the deployment_share\Boot folder (where
     deployment_share is the shared folder used as the deployment share).

Step 6: Create the LTI Bootable Media
Provide a method for starting the computer with the customized version of Windows PE
created when the deployment share was updated. The Deployment Workbench creates
the LiteTouchPE_x86.iso and LiteTouchPE_x86.wim files (for 32-bit target computers) or
LiteTouchPE_x64.iso and LiteTouchPE_x64.wim files (for 64-bit target computers) in the
deployment_share\Boot folder (where deployment_share is the shared folder used as the
deployment share). Create the appropriate LTI bootable media from one of these
images.

To create the LTI bootable media

   1. In Windows Explorer, navigate to deployment_share\Boot folder (where
     deployment_share is the shared folder used as the deployment share).

<!-- p.630 -->

   2. Based on the type of computer used for the existing computer (WDG-EXIST-01)
     and new computer (WDG-NEW-02), perform one of the following tasks:

           If the reference computer is a physical computer, create a CD or DVD of the
           ISO file.

           If the reference computer is a VM, start the VM directly from the ISO file or
           from a CD or DVD of the ISO file.

Step 7: Start the Existing Computer with the LTI Bootable
Media
Start the existing computer (WDG-EXIST-01) with the LTI bootable media created earlier
in the process. This CD starts Windows PE on the existing computer and initiates the
MDT deployment process. At the end of the MDT deployment process, the user state
migration information is stored in the UserStateCapture$ shared folder.

  ７ Note

  You can also initiate the MDT process by starting the target computer from
  Windows Deployment Services. For more information, see the section, "Preparing
  Windows Deployment Services", in the MDT document Using the Microsoft
  Deployment Toolkit.

To start the existing computer with the LTI bootable media

   1. Start WDG-EXIST-01 with the LTI bootable media created earlier in the process.

     Windows PE starts, and then the Windows Deployment Wizard starts.

   2. Complete the Windows Deployment Wizard using the following information.
     Accept the default values unless otherwise specified.

                                                                               ﾉ   Expand table

      On this wizard page               Do this

      Welcome to Deployment             Select Run the Deployment Wizard to install a new
                                        operating system, and then select Next.

      Specify Credentials for           1. In User Name, type Administrator.
      connecting to network shares.     2. In Password, type P@ssw0rd.
                                        3. In Domain, type CORP.
                                        4. Select OK.

<!-- p.631 -->

      On this wizard page                 Do this

      Select a task sequence to execute   Select Perform Replace Computer Scenario on Existing
      on this computer.                   Computer, and then select Next.

      Specify where to save your data     Select Next.
      and settings

      Specify where to save a complete    Select Do not back up the existing computer, and
      computer backup                     then select Next.

      Ready to begin                      Select Begin.

     If any errors or warnings occur, consult the MDT document Troubleshooting
     Reference.

  3. In the Deployment Summary dialog box, select Details.

     If any errors or warnings occurred, review the errors or warnings and record any
     diagnostic information.

  4. In the Deployment Summary dialog box, select Finish.

     The user state migration information is captured and is stored in the network
     shared folder (UserStateCapture$) created earlier in the process.

Step 8: Start the New Computer with the LTI Bootable
Media
Start the new computer (WDG-NEW-02) with the LTI bootable media created earlier in
the process. This CD starts Windows PE on the reference computer and initiates the MDT
deployment process. At the end of the MDT deployment process, Windows Vista is
deployed on the new computer and the captured user state migration information is
restored to the new computer.

  ７ Note

  You can also initiate the MDT process by starting the target computer from
  Windows Deployment Services. For more information, see the section, "Preparing
  Windows Deployment Services", in the MDT document Using the Microsoft
  Deployment Toolkit.

To start the new computer with the LTI bootable media

<!-- p.632 -->

1. Start WDG-NEW-02 with the LTI bootable media created earlier in the process.

  Windows PE starts, and then the Windows Deployment Wizard starts.

2. Complete the Windows Deployment Wizard by using the following information.
  Accept the default values unless otherwise specified.

                                                                          ﾉ   Expand table

   On this wizard page             Do this

   Welcome to Deployment           Select Run the Deployment Wizard to install a new
                                   operating system, and then select Next.

   Specify Credentials for         1. In User Name, type Administrator.
   connecting to network shares.   2. In Password, type P@ssw0rd.
                                   3. In Domain, type CORP.
                                   4. Select OK.

   Select a task sequence to       Select Perform Replace Computer Scenario on New
   execute on this computer.       Computer, and then select Next.

   Configure the computer name     In Computer name, type WDG-NEW-02, and then select
                                   Next.

   Join the computer to a domain   Select Next.
   or workgroup

   Specify whether to restore      1. Select Specify a location.
   user data                       2. In Location, type \\WDG-MDT-
                                   01\UserStateCapture$\WDG-EXIST-01.
                                   3. Select Next.

   Locale Selection                Select Next.

   Set the Time Zone               Select Next.

   Specify whether to capture an   Select Do not capture an image of this computer, and
   image                           then select Next.

   Specify the BitLocker           Select Do not enable BitLocker for this computer, and
   configuration                   then select Next.

   Ready to begin                  Select Begin.

  If any errors or warnings should occur, consult the MDT document Troubleshooting
  Reference.

3. In the Deployment Summary dialog box, select Details.

<!-- p.633 -->

     If any errors or warnings occurred, review the errors or warnings and record any
     diagnostic information.

   4. In the Deployment Summary dialog box, select Finish.

     Windows Vista is now installed on the new computer and the captured user state
     migration information is also restored.

Integrating Custom Deployment Code into
MDT
It is common for a deployment team to have complex requirements, specific to their
target environment, that are not met by the Deployment Workbench predefined task
sequence actions or by default MDT configuration files. In this situation, implement
custom code to meet their requirements.

Integrate custom deployment code into MDT by:

     Choosing a scripting language as described in Choosing the Appropriate Scripting
     Language

     Leveraging ZTIUtility.vbs as described in Understanding How to Leverage ZTIUtility

     Integrating custom deployment code as described in Integrating Custom
     Deployment Code

     The following sections assume that MDT is configured on a deployment server.

Choosing the Appropriate Scripting Language
Although any code that can be run on Windows or Windows PE can be called as an
application installation or through an MDT task sequence step, Microsoft recommends
using scripts in the form of .vbs or .wsf files.

The advantage of using .wsf files is built-in logging in addition to some other predefined
functions already used by the ZTI and LTI processes. These functions are available in the
ZTIUtility script distributed with MDT.

When referenced from a custom script, the ZTIUtility script initializes the MDT
environment and setup classes. These classes are available:

     Logging. This class provides the logging functionality that all MDT scripts use. It
     also creates a single log file for each script run during deployment and a

<!-- p.634 -->

  consolidated log file of all scripts. These log files are created in a format designed
  to be read by CMTrace.

  Environment. This class configures environment variables gathered through WMI
  and MDT rule processing and allows them to be referenced directly from the script.
  This allows deployment properties to be read, giving access to all the configuration
  information used by the ZTI and LTI processes.

  Utility. This class provides general utilities that are used throughout ZTI and LTI
  scripts. Microsoft recommends that any time custom code is developed this class
  should be examined to see if any code can simply be reused. Additional
  information about some of the functionality provided in this class is included later
  in this section.

  Database. This class performs functions like connecting to databases and reading
  information from databases. In general, accessing the database class directly is not
  recommended; instead, rule processing should be used to perform database
  lookups.

  Strings. This class performs common string processing routines like creating a
  delimited list of items, displaying a hex value, trimming white space from a string,
  right aligning a string, left aligning a string, forcing a value to string format, forcing
  a value to array format, generating a random globally unique identifier (GUID), and
  Base64 conversions.

  FileHandling. This class performs functions like normalizing paths and copying,
  moving, and deleting files and folders.

  clsRegEx. This class performs regular expression functions.

  In MDT, a couple of changes have been implemented to the script architecture to
  make client Microsoft Visual Basic Scripting Edition (VBScript) more robust and
  reliable. These changes include:

  Extensive changes to ZTIUtility.vbs (the main script library), including new APIs and
  better error handling

  A new look to the overall structure of the ZTI_xxx.wsf scripts

  The overall structure of the MDT scripts has also changed. Most MDT scripts are
  now encapsulated within VBScript Class objects. The class is initialized and called
  with the RunNewInstance function.

７ Note

<!-- p.635 -->

  Most existing MDT 2008 Update 1 scripts will work as-is in MDT, even with the
  extensive changes to ZTIUtility.vbs, as most MDT scripts will include ZTIUtility.vbs.

Understanding How to Leverage ZTIUtility
The ZTIUtility.vbs file contains object classes that can be leveraged in your custom code.
Integrate custom code with MDT by using the:

     Logging class defined in ZTIUtility.vbs as described in Use the ZTIUtility Logging
     Class

     Environment class defined in ZTIUtility.vbs as described in Use the ZTIUtility
     Environment Class

     Utility class defined in ZTIUtility.vbs as described in Use the ZTIUtility Utility Class

Use the ZTIUtility Logging Class

The logging class in ZTIUtiliy.vbs provides a simple mechanism for custom code to log
status information, warnings, and errors in the same manner as other scripts during a
ZTI or LTI deployment. This standardization also ensures that the LTI Deployment
Summary dialog box correctly reports the status of any custom code that is run.

The following illustrates an example custom code script that uses the
oLogging.CreateEntry and TestAndFail functions to log different types of messages,
depending on the results of the various script actions.

Example Script Using ZTIUtility Logging: ZTI_Example.wsf

  Visual Basic Script

  <job id="ZTI_Example">
  <script language="VBScript" src="ZTIUtility.vbs"/>
  <script language="VBScript">

  ' //*******************************************************
  ' //
  ' // Copyright (c) Microsoft Corporation. All rights reserved
  ' // Microsoft Deployment Toolkit Solution Accelerator
  ' // File: ZTI_Example.wsf
  ' //
  ' // Purpose: Example of scripting with the
  ' //          Microsoft Deployment Toolkit.
  ' //
  ' // Usage: cscript ZTI_Example.wsf [/debug:true]
  ' //

<!-- p.636 -->

' //*******************************************************

Option Explicit
RunNewInstance

'//--------------------------------------------------------
'// Main Class
'//--------------------------------------------------------
Class ZTI_Example

'//--------------------------------------------------------
'// Main routine
'//--------------------------------------------------------

Function Main()

  Dim iRetVal
  Dim sScriptPath

  iRetVal = SUCCESS

  oLogging.CreateEntry "Begin example script...", _
    LogTypeInfo

  ' %ServerA% is a generic variable available within
  ' every CustomSettings.ini file.

  sScriptPath = "\\" & oEnvironment.Item("ServerA") & _
    "\public\products\Applications\User\Technet\USEnglish"

  ' Validate a connection to server, net connect with
  ' credentials if necessary.
  iRetVal = oUtility.ValidateConnection( sScriptPath )
  TestAndFail iRetVal, 9991, "Validate Connection to [" & _
    sScriptPath & "]"

  'Run Setup Program

  iRetVal = oUtility.RunWithHeartbeat( """" & _
    sScriptPath & "\setup.exe"" /?" )
  TestAndFail iRetVal, 9991, "RunWithHeartbeat [" & _
    sScriptPath & "]"

  'Perform any cleanup from installation process

  oShell.RegWrite "HKLM\Software\Microsoft\SomeValue", _
    "Done with Execution of XXX.", "REG_SZ"

  Main = iRetVal

End Function

End Class

<!-- p.637 -->

  </script>
  </job>

  ７ Note

  If you want to continue using scripts that call ZTIProcess() with ProcessResults(),
  you can continue to do so. However, certain enhanced error-handling features will
  not be enabled.

Use the ZTIUtility Environment Class

The environment class in ZTIUtiliy.vbs provides access to, and the ability to update, MDT
properties. In preceding example, oEnvironment.Item("Memory") is used to retrieve the
amount of available RAM; this can also be used to retrieve the value of any of the
properties described in the MDT document Toolkit Reference.

Use the ZTIUtility Utility Class

The ZTIUtility.vbs script contains a number of commonly used utilities that any custom
deployment script can use. You can add these utilities to any script the same way as the
oLogging and oEnvironment classes.

The following table details some useful functions available, and their output. For a full
list of available functions, refer to the ZTIUtility.vbs file.

                                                                                 ﾉ   Expand table

 Function                                    Output

 oUtility.LocalRootPath                      Returns the path of the root folder being used by the
                                             deployment process on the target computer—for
                                             example, C:\MININT

 oUtility.BootDevice                         Returns the system boot device—for example,
                                             MULTI(0)DISK(0)RDISK(0)PARTITION(1)

 oUtility.LogPath                            Returns the path to the logs folder being used during
                                             the deployment—for example,
                                             C:\MININT\SMSOSD\OSDLOGS

 oUtility.StatePath                          Returns the path of the currently configured state
                                             store—for example, C:\MININT\StateStore

<!-- p.638 -->

Function                                  Output

oUtility.ScriptName                       Returns the name of the script calling the function—
                                          for example, Z-RAMTest

oUtility.ScriptDir                        Returns the path to the script that is calling the
                                          function—for example,
                                          \\server_name\Deployment$\Scripts

oUtility.ComputerName                     Determines the computer name that will be used
                                          during the build process—for example,
                                          computer_name

oUtility.ReadIni(file, section, item)     Allows the specified item to be read from an .ini file

oUtility.WriteIni(file, section, item,    Allows the specified item to be written to an .ini file
value)

oUtility.Sections(file)                   Reads the sections of an .ini file and stores them in an
                                          object for reference

oUtility.SectionContents(file, section)   Reads the contents of the specified .ini file and stores
                                          them in an object

oUtility.RunWithHeartbeat(sCmd)           When the command is run, write heartbeat
                                          information to the logs every 0.5 seconds

oUtility.FindFile                         Searches for the specified file in the DeployRoot
                                          folder and standard subfolders, including Servicing,
(sFilename,sFoundPath)                    Tools, USMT, Templates, Scripts, and Control

oUtility.findMappedDrive(sServerUNC)      Checks to see whether a drive is mapped to the
                                          specified UNC path and returns the drive letter

oUtility.ValidateConnection(sServerUNC)   Checks to see whether there is an existing connection
                                          to the server specified and, if there is not, attempts to
                                          create one

MapNetworkDrive                           Maps a drive letter to the UNC path specified as the
                                          share and returns the drive letter used; returns an
(sShare, SDomID, sDomPwd)                 error if unsuccessful

VerifyPathExists(strPath)                 Verifies that the specified path exists

oEnvironment.Substitute(sVal)             Given a string, expands any variables or functions
                                          within that string

oEnvironment.Item                         Reads or writes a variable to a persistent store

(sName)

<!-- p.639 -->

 Function                                Output

 oEnvironment.Exists                     Tests to see whether the variable exists

 (sName)

 oEnvironment.ListItem                   Reads or writes a variable of type array to a persistent
                                         store
 (sName)

 oLogging.ReportFailure                  Used to perform a structured exit if an unrecoverable
                                         error is detected
 (sMessage, iError)

 oLogging.CreateEvent                    Writes a message to the log file and posts the event
                                         to a defined server
 (iEventID, iType, sMessage, arrParms)

 oLogging.CreateEntry                    Writes a message to the log file

 (sLogMsg, iType)

 TestAndFail(iRc, iError, sMessage)      Exits the script with iError if iRc is false or fail

 TestAndLog(iRc , sMessage)              Logs a warning only if iRc is false or fail

Integrating Custom Deployment Code
Custom deployment code can be integrated into the MDT process in several ways;
however, regardless of the method used, the following two rules should be met:

     The custom deployment code script name should always begin with the letter Z.

     The custom deployment code should be placed in the Scripts folder on the
     deployment share—for example, D:\Production Deployment Share\Scripts.

     The most frequently used methods for integrating custom code that also ensure
     consistent logging are:

     Deploy the code as an MDT application

     Launch the code as an MDT task sequence command

     Launch the code as a user exit script

Deploy Custom Code as an MDT Application

<!-- p.640 -->

Custom deployment code can be imported into the Deployment Workbench and
managed the same way as any other application.

To create a new application to run custom deployment code

  1. Copy the custom deployment code to the deployment_share\Scripts folder (where
     deployment_share is the fully qualified path to the deployment share).

  2. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  3. In the Deployment Workbench console tree, go to Deployment
     Shares/deployment_share/Applications (where deployment_share is the name of the
     deployment share to configure).

  4. In the Actions pane, select New Application.

     The New Application Wizard starts.

  5. Complete the New Application Wizard using the following information. Accept
     defaults unless otherwise specified.

                                                                                 ﾉ   Expand table

      On this wizard   Do this
      page

      Application      Select Application without source files or elsewhere on the network, and
      Type             then select Next.

      Details          Complete this page based on the information from the application, and
                       then select Next.

      Command          1. In the Command line box, type cscript.exe
      Details          %SCRIPTROOT%\custom_code (where custom_code is the name of the
                       custom code that has been developed).
                       2. In the Working directory box, type working_directory (where
                       working_directory is the name of the working directory of the custom
                       code; this is typically the same folder specified in the Command line box).
                       3. Select Next.

      Summary          Verify that the configuration settings are correct, and then select Next.

      Confirmation     Select Finish.

     The application appears in the Applications node in the Deployment Workbench.
