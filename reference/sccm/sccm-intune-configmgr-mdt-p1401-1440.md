---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1401-1440"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1401-1440
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1401-1440
family: sccm
documentKind: "doc"
abstract: "PowerShell Get-MDTPersistentDrive Description This example restores the list of MDT persisted drives, by creating a Windows PowerShell drive using the MDTProvider type. The deployment share will not be upgraded when restored. Example 2 PowerShell Get-MDTPersistentDrive -Force De"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1401-1440

<!-- p.1401 -->

  PowerShell

   Get-MDTPersistentDrive

Description
This example restores the list of MDT persisted drives, by creating a Windows
PowerShell drive using the MDTProvider type. The deployment share will not be
upgraded when restored.

Example 2
  PowerShell

   Get-MDTPersistentDrive -Force

Description

This example restores the list of MDT persisted drives, by creating a Windows
PowerShell drive using the MDTProvider type. The deployment share will be upgraded
when restored (if required).

Set-MDTMonitorData
This section describes the Get-MDTPersistentDrive Windows PowerShell cmdlet. Run
this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Set-MDTMonitorData [-Path <String>] [-ComputerObject <PSObject>] [-Settings
   <Hashtable>] [<CommonParameters>]

-or-

  PowerShell

<!-- p.1402 -->

  Set-MDTMonitorData [-Path <String>] [-MacAddress <String>] [Settings
  <Hashtable>] [<CommonParameters>]

Description
This cmdlet creates a new monitoring data item, or updates an existing monitoring data
item, in a deployment share. You can identify the monitoring data to remove by
specifying the:

     Computer object for the monitoring item in the deployment share. The computer
     object can be obtained using the Get-MDTMonitorData cmdlet. The first syntax
     example illustrates this usage.

     MAC address of the primary network adapter of the monitoring item for a specific
     deployment share. The MAC address is automatically assigned to the monitoring
     data item when the item is created for the deployment share. The last syntax
     example illustrates this usage.

  ７ Note

  Once the monitoring data has been removed, there is no method for recovering
  the information.

Parameters
This subsection provides information about the various parameters that can be used
with the Get- MDTMonitorData cmdlet.

-Path <String>
This parameter specifies the MDTProvider Windows PowerShell drive for the desired
deployment share.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to a location within the desired MDTProvider Windows PowerShell
  drive.

<!-- p.1403 -->

                                                                              ﾉ   Expand table

 Parameter                                                             Value

 Required?                                                             False

 Position?                                                             Named

 Default value                                                         -

 Accept pipeline input?                                                False

 Accept wildcard characters?                                           False

-ComputerObject <PSObject>
This parameter specifies the monitoring data item to be created or updated using a
computer object. If this parameter is not specified, then the MACAddress parameter
must be specified to identify a particular monitoring data item.

                                                                              ﾉ   Expand table

 Parameter                                                   Value

 Required?                                                   False

 Position?                                                   Named

 Default value                                               -

 Accept pipeline input?                                      True (ByValue)

 Accept wildcard characters?                                 False

-MACAddress <String>

This parameter specifies the monitoring data item to be created or updated using the
MAC address of the primary network adapter of the computer being monitored. The
format of the MACAddress is xx:xx:xx:xx:xx:xx, where x is a hexadecimal character
specified in uppercase (as required). If this parameter is not specified, then the
ComputerObject parameter must be specified to identify a particular monitoring data
item.

                                                                              ﾉ   Expand table

<!-- p.1404 -->

 Parameter                                                Value

 Required?                                                False

 Position?                                                Named

 Default value                                            -

 Accept pipeline input?                                   True (ByValue)

 Accept wildcard characters?                              False

-Settings <Hashtable>
This parameter specifies the monitoring data settings for the monitoring data item to be
created or updated. The format of the hashtable provided with this parameter is
@{"Setting"="Value"; "Setting1"="Value1"; "Setting2"="Value2} . If this parameter is

not specified, then the monitoring data item is created, but no monitoring information is
stored.

"Setting" can be any property listed in the ZTIGather.xml file. Value can be any valid

value for the property specified in "Setting" .

                                                                           ﾉ   Expand table

 Parameter                                                Value

 Required?                                                False

 Position?                                                Named

 Default value                                            -

 Accept pipeline input?                                   True (ByValue)

 Accept wildcard characters?                              False

<CommonParameters>

This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

<!-- p.1405 -->

  Get-Help about_CommonParameters

Outputs
This cmdlet does not generate any output.

Example 1
  PowerShell

  $MonitorObject=Get-MDTMonitorData | Where-Object {$_.Name eq 'WDG-REF-01'}
  Set-MDTMonitorData -ComputerObject $MonitorObject Setting
  @{"OSDComputerName"="WDG-MDT-01";"SkipWizard"="YES"}

Description

This example removes any monitoring data item where the name of the computer is
WDG-REF-01. The object is found using the Get-MDTMonitorData cmdlet and the
Where-Object cmdlet. For more information on the Where-Object cmdlet, see Using
the Where-Object Cmdlet. The OSDComputerName property is recorded as having a
value of WDG-MDT-01, and the SkipWizard property is recorded as having a value of
YES.

Example 2
  PowerShell

  Set-MDTMonitorData -MACAddress "00:11:22:33:44:55" MonitorObject Setting
  @{"OSDComputerName"="WDG-MDT-01";"SkipWizard"="YES"}

Description

This example creates or updates a monitoring data item with a MACAddress that has a
value of 00:11:22:33:44:55. The OSDComputerName property is recorded as having a
value of WDG-MDT-01, and the SkipWizard property is recorded as having a value of
YES.

Test-MDTDeploymentShare

<!-- p.1406 -->

Although this cmdlet is returned using the Get-Command cmdlet as being in the
Microsoft.BDD.PSSnapIn snap-in, it is not implemented.

Test-MDTMonitorData
This section describes the Test-MDTMonitorData Windows PowerShell cmdlet. Run this
cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Test-MDTMonitorData -ServerName <String> -EventPort <Int32> -DataPort
   <Int32> [<CommonParameters>]

Description
This cmdlet validates if the MDT monitoring service, which runs on the computer on
which MDT is installed, is enabled and running properly. The MDT monitoring service
collects monitoring information that can be displayed:

       In the Monitoring node in a deployment share in the Deployment Workbench

       Using the Get-MDTMonitorData cmdlet

       The MDT monitoring service can be disabled using the Disable-
       MDTMonitorService. Monitoring information can be written to the MDT
       monitoring service using the Set-MDTMonitorData cmdlet.

  ７ Note

  For this cmdlet to function properly there must be at least one MDT monitoring
  data item in the deployment share. If no MDT monitoring information has been
  recorded, the deployment share will fail the test.

For more information on the MDT monitoring service, see the section "Monitoring MDT
Deployments" in the MDT document, Using the Microsoft Deployment Toolkit.

<!-- p.1407 -->

Parameters
This subsection provides information about the various parameters that can be used
with the Test-MDTMonitorData cmdlet.

-Server <String>

Specifies the name of the computer on which MDT is installed and the MDT monitoring
service is running.

                                                                      ﾉ   Expand table

 Parameter                                                        Value

 Required?                                                        True

 Position?                                                        Named

 Default value                                                    None

 Accept pipeline input?                                           False

 Accept wildcard characters?                                      False

-DataPort <Int32>

This parameter specifies the TCP port used as the data port for the MDT monitoring
service.

                                                                      ﾉ   Expand table

 Parameter                                                        Value

 Required?                                                        True

 Position?                                                        Named

 Default value                                                    -

 Accept pipeline input?                                           False

 Accept wildcard characters?                                      False

-EventPort <Int32>

<!-- p.1408 -->

This parameter specifies the TCP port used as the event port for the MDT monitoring
service.

                                                                          ﾉ   Expand table

 Parameter                                                            Value

 Required?                                                            True

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

 Accept wildcard characters?                                          False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a Boolean value that represents the success (true) or failure (false)
of the text.

Example 1
  PowerShell

  Test-MDTMonitorData -Server "WDG-MDT-01" -DataPort "9801" EventPort "9800"

Description

<!-- p.1409 -->

This example verifies if the MDT monitoring service on WDG-MDT-01 is installed and
running. The cmdlet will verify using a data port of 9801 and an event port of 9800.

Update-MDTDatabaseSchema
This section describes the Update-MDTDatabaseSchema Windows PowerShell cmdlet.
Run this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-
in loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Update-MDTDatabaseSchema -SQLServer <String> [-Instance <String>] [-Port
   <String>] [-Netlib <String>] -Database <String> [-SQLShare <String>]
   [<CommonParameters>]

Description
This cmdlet updates an existing MDT DB database to the latest version of the MDT DB
database schema. Each deployment share can be associated with only one MDT DB
database.

This cmdlet is automatically called when a deployment share is being upgraded, such as
when running the Restore-MDTPersistentDrive cmdlet with the Force parameter and the
Update-MDTDeploymentShare cmdlet.

Parameters
This subsection provides information about the various parameters that can be used
with the Upgrade-MDTDatabaseSchema cmdlet.

-SQLServer <String>

This parameter specifies the name of the computer running SQL Server where the MDT
DB database will be upgraded.

                                                                        ﾉ   Expand table

<!-- p.1410 -->

 Parameter                                                           Value

 Required?                                                           True

 Position?                                                           Named

 Default value                                                       -

 Accept pipeline input?                                              False

 Accept wildcard characters?                                         False

-Instance <String>
This parameter specifies the SQL Server instance on which the MDT DB database to be
upgraded exists. If this parameter is omitted, then the MDT DB database is assumed to
be in the default SQL Server instance.

  ７ Note

  The SQL Server Browser service must be running on the computer running SQL
  Server for the cmdlet to locate the instance specified in this parameter.

                                                                         ﾉ    Expand table

 Parameter                                                           Value

 Required?                                                           False

 Position?                                                           Named

 Default value                                                       -

 Accept pipeline input?                                              False

 Accept wildcard characters?                                         False

-Port <String>
This parameter specifies the TCP port to be used in communication with the SQL Server
instance specified in the SQLServer parameter. The default port that SQL Server uses is
1433. Specify this parameter when SQL Server is configured to use a port other than the
default value. The value of this parameter must match the port configured for SQL
Server.

<!-- p.1411 -->

                                                                       ﾉ   Expand table

 Parameter                                                         Value

 Required?                                                         False

 Position?                                                         Named

 Default value                                                     -

 Accept pipeline input?                                            False

 Accept wildcard characters?                                       False

-Netlib <String>
This parameter specifies the SQL Server network library that is used in communication
with the SQL Server instance specified in the SQLServer parameter. The parameter can
be set to one of the following values:

     DBNMPNTW, which is used to specify named pipes communication

     DBSMSOCN, which is used to specify TCP/IP sockets communication

     If this parameter is not provided, the named pipes SQL Server network library
     (DBNMPNTW) is used.

  ７ Note

  The Deployment Workbench does not provide the option for configuring the SQL
  Server network library. The Deployment Workbench always uses named pipes
  communication. However, the SQL Server network library can be configured in the
  CustomSettings.ini file.

                                                                       ﾉ   Expand table

 Parameter                                                         Value

 Required?                                                         False

 Position?                                                         Named

 Default value                                                     -

 Accept pipeline input?                                            False

<!-- p.1412 -->

 Parameter                                                          Value

 Accept wildcard characters?                                        False

-Database <String>
This parameter specifies the name of the database to be upgraded in the SQL Server
instance specified in the Instance parameter on the SQL Server instance specified in the
SQLServer parameter.

                                                                        ﾉ   Expand table

 Parameter                                                          Value

 Required?                                                          True

 Position?                                                          Named

 Default value                                                      -

 Accept pipeline input?                                             False

 Accept wildcard characters?                                        False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a PSObject type object for the MDT database that was upgraded.
This cmdlet also outputs a String type data if the Verbose common parameter is
included.

Example 1

<!-- p.1413 -->

  PowerShell

   Update-MDTDatabaseSchema -SQLServer "WDGSQL01" Database "MDTDB"

Description
This example updates the schema for an MDT database named MDTDB in the default
SQL Server instance on a computer named WDG-SQL-01. The connection will be made
to the SQL Server instance using the default TCP port and the Named Pipes protocol.

Example 2
  PowerShell

   Update-MDTDatabaseSchema -SQLServer "WDGSQL01" -Instance "MDTInstance" -Port
   "6333" Database "MDTDB"

Description
This example updates the schema for an MDT database named MDTDB in the SQL
Server instance named MDTInstance on a computer named WDG-SQL-01. The
connection will be made to the SQL Server using TCP port 6333 and the Named Pipes
protocol.

Update-MDTDeploymentShare
This section describes the Update-MDTDeploymentShare Windows PowerShell cmdlet.
Run this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-
in loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Update-MDTDeploymentShare [-Path <String>] [-Force] [Compress]
   [<CommonParameters>]

<!-- p.1414 -->

Description
This cmdlet updates an existing deployment share with the latest files from the
Windows ADK. This cmdlet also updates or regenerates the required Windows PE boot
images in both WIM and ISO file formats.

Parameters
This subsection provides information about the various parameters that can be used
with the Update-MDTDeploymentShare cmdlet.

-Path <String>
This parameter specifies the fully qualified path to an existing folder in the deployment
share that is being updated.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to the desired location within the deployment share.

                                                                         ﾉ   Expand table

 Parameter                                                           Value

 Required?                                                           False

 Position?                                                           Named

 Default value                                                       -

 Accept pipeline input?                                              False

 Accept wildcard characters?                                         False

-Force [<SwitchParameter>]
This parameter specifies whether Windows PE boot images (.iso and .wim files) for the
deployment share should be completely regenerated. If this parameter is:

     Provided, then the cmdlet creates new versions of the Windows PE boot images.
     This process takes more time than optimizing the existing Windows PE boot
     images.

<!-- p.1415 -->

     Omitted, then the cmdlet optimizes the existing Windows PE boot images. This
     process takes less time than generating new versions of the Windows PE boot
     images. If this parameter is omitted, the Compress parameter can be used to
     reduce the size of the boot images as a part of the Windows PE boot image
     optimization process.

                                                                           ﾉ   Expand table

 Parameter                                                Value

 Required?                                                False

 Position?                                                Named

 Default value                                            -

 Accept pipeline input?                                   True (ByValue)

 Accept wildcard characters?                              False

-Compress [<SwitchParameter>]

This parameter specifies whether Windows PE boot images (.iso and .wim files) for the
deployment share should be compressed when they are optimized (without the Force
parameter). If this parameter is:

     Provided, then the cmdlet compresses the Windows PE boot images as they are
     being optimized

     Omitted, then the cmdlet does not compress the Windows PE boot images as they
     are being optimized

  ７ Note

  This parameter should only be provided if the Force parameter is not provided. If
  the Force parameter is included, new Windows PE boot images are generated and
  are compressed to the minimal size.

                                                                           ﾉ   Expand table

 Parameter                                                Value

 Required?                                                False

<!-- p.1416 -->

 Parameter                                                Value

 Position?                                                Named

 Default value                                            -

 Accept pipeline input?                                   True (ByValue)

 Accept wildcard characters?                              False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a String type data and produces additional String type data if the
Verbose common parameter is included.

Example 1
  PowerShell

  Update-MDTDepoymentShare

Description
This example updates the deployment share at the Windows PowerShell working
directory. The Windows PE boot images will be optimized. The Windows PE boot images
will not be compressed.

Example 2
  PowerShell

<!-- p.1417 -->

   Update-MDTDepoymentShare -Path "DS001:"

Description
This example updates the deployment share at the MDT Windows PowerShell drive
named DS001:. The Windows PE boot images will be optimized. The Windows PE boot
images will not be compressed.

Example 3
  PowerShell

   Update-MDTDepoymentShare -Path "DS001:" -Compress

Description

This example updates the deployment share at the MDT Windows PowerShell drive
named DS001:. The Windows PE boot images will be optimized. The Windows PE boot
images will be compressed.

Example 4
  PowerShell

   Update-MDTDepoymentShare -Path "DS001:" -Force

Description

This example updates the deployment share at the MDT Windows PowerShell drive
named DS001:. New versions of the Windows PE boot images will be generated.

Update-MDTLinkedDS
This section describes the Update-MDTLinkedDS Windows PowerShell cmdlet. Run this
cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

<!-- p.1418 -->

Syntax
  PowerShell

  Update-MDTLinkedDS -Path <String> [<CommonParameters>]

Description
This cmdlet replicates content from a deployment share to a linked deployment share
using the selection profile used to define the linked deployment share. The replication
behavior is determined based on the configuration settings for the linked deployment
share.

Parameters
This subsection provides information about the various parameters that can be used
with the Update-MDTLinkedDS cmdlet.

-Path <String>

This parameter specifies the fully qualified path to the linked deployment share that is
being updated.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to the desired location within the deployment share.

                                                                         ﾉ   Expand table

 Parameter                                                           Value

 Required?                                                           True

 Position?                                                           Named

 Default value                                                       -

 Accept pipeline input?                                              False

 Accept wildcard characters?                                         False

<!-- p.1419 -->

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

   Get-Help about_CommonParameters

Outputs
This cmdlet outputs a String type data and produces additional String type data if the
Verbose common parameter is included.

Example 1
  PowerShell

   Update-MDTLinkedDS -Path "DS001:\Linked Deployment Shares\LINKED001"

Description
This example replicates content from the deployment share to the linked deployment
share at the Windows PowerShell path DS001:\Linked Deployment Shares\LINKED001
folder.

Update-MDTMedia
This section describes the Update-MDTMedia Windows PowerShell cmdlet. Run this
cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

<!-- p.1420 -->

  Update-MDTMedia -Path <String> [<CommonParameters>]

Description
This cmdlet replicates content from a deployment share to a folder that contains
deployment media using the selection profile used to define the deployment media. The
replication behavior is determined based on the configuration settings for the
deployment media.

Media in LTI allows you to perform LTI deployments solely from local media without
connecting to a deployment share. You can store the media on a DVD, USB hard disk, or
other portable device. After you create the media, generate bootable WIM images that
allow the deployment to be performed from portable media devices locally available on
the target computer.

Parameters
This subsection provides information about the various parameters that can be used
with the Update-MDTMedia cmdlet.

-Path <String>

This parameter specifies the fully qualified path to the folder that contains the
deployment media that is being updated.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to the desired location within the deployment share.

                                                                          ﾉ   Expand table

 Parameter                                                            Value

 Required?                                                            True

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

<!-- p.1421 -->

 Parameter                                                         Value

 Accept wildcard characters?                                       False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a String type data and produces additional String type data if the
Verbose common parameter is included.

Example 1
  PowerShell

  Update-MDTMedia -Path "DS001:\Media\MEDIA001"

Description
This example replicates content from the deployment share to the folder containing the
deployment media at the Windows PowerShell path DS001:\Media \MEDIA001 folder.

Related articles
     Task Sequence Steps.
     Properties.
     Scripts.
     Support Files.
     Utilities.
     Tables and Views in the MDT DB.
     Windows 7 Feature Dependency Reference.

<!-- p.1422 -->

     UDI Reference.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1423 -->

Tables and Views in the MDT DB
Article • 02/12/2024

In MDT, many property settings can be stored (typically configured in the
CustomSettings.ini file) in a database. Configuring the properties in a database helps
create a generic CustomSettings.ini file that requires fewer modifications and allows one
CustomSettings.ini file to be used in more images (because the file is more generic).

Customize the database in the Database node in the Deployment Workbench. Using the
Deployment Workbench, the deployment settings can be configured and saved in
tables.

However, queries about the information in the tables are done using views. Views help
simplify the queries by joining results from multiple tables. ZTIGather.wsf queries the
views to return the result set that the Parameters and ParameterCondition properties
specify.

Tables in the MDT DB
The following table lists the database tables that Deployment Workbench creates and
manages.

                                                                                 ﾉ   Expand table

 Table                             Description

 ComputerIdentity                  Used to identify a specific computer using any combination of
                                   the AssetTag, UUID, SerialNumber, and MACAddress
                                   properties. The table includes a Description column to provide
                                   a user-friendly method of describing the computer (usually
                                   the computer name).

 Descriptions                      Contains descriptions of all properties configurable via the
                                   database.

 LocationIdentity                  Used to identify geographic locations using the Location
                                   property. The values for this property are stored in a
                                   corresponding column in the table.

 LocationIdentity_DefaultGateway   Relates the default gateway values with a location identified in
                                   the LocationIdentity table. There is a one-to-many relationship
                                   between this table and the LocationIdentity table.

 MakeModelIdentity                 Used to identify a specific make and model of a computer
                                   using the Make and Model properties. The values for these

<!-- p.1424 -->

 Table                          Description

                                properties are stored in corresponding columns in the table.

 PackageMapping                 Used to associate the name presented in the Add or Remove
                                Programs Control Panel item with a Configuration Manager
                                package and program to be deployed in place of the
                                application in Add or Remove Programs. For more information
                                on this table, see the section, "Deploying Applications Based
                                on Earlier Application Versions", in the MDT document
                                Microsoft Deployment Toolkit Samples Guide.

 RoleIdentity                   Used to identify the purpose of a computer or the users of a
                                computer using the Role property. The values for this property
                                are stored in a corresponding column in the table.

 Settings                       Identifies the settings that are applied to an individual
                                computer or a group of computers based on the settings in
                                the Computers, Roles, Locations, and Make and Model nodes
                                in the Database node in the Deployment Workbench.

 Settings_Administrators        Identifies the user accounts to be added to the local
                                Administrator group on the target computer based on the
                                settings in the Computers, Roles, Locations, and Make and
                                Model nodes in the Database node in the Deployment
                                Workbench.

 Settings_Applications          Identifies the applications to be deployed to the target
                                computer based on the settings in the Computers, Roles,
                                Locations, and Make and Model nodes in the Database node
                                in the Deployment Workbench.

 Settings_Packages              Identifies the packages to be deployed to the target computer
                                based on the settings in the Computers, Roles, Locations, and
                                Make and Model nodes in the Database node in the
                                Deployment Workbench.

 Settings_Roles                 Identifies the roles to be associated with the target computer
                                based on the settings in the Computers, Locations, and Make
                                and Model nodes in the Database node in the Deployment
                                Workbench.

Views in the MDT DB
The following table lists and describes the database views that are used when querying
configuration information in the MDT DB.

                                                                               ﾉ   Expand table

<!-- p.1425 -->

View                     Description

ComputerAdministrators   Used to find all accounts to be made members of the local
                         Administrators group on the target computer. The view is a join of
                         the ComputerIdentity and Settings_Administrators tables.

ComputerApplications     Used to find all applications to be deployed to the target computer.
                         The view is a join of the ComputerIdentity and Settings_Applications
                         tables.

ComputerPackages         Used to find all packages to be deployed to the target computer.
                         The view is a join of the ComputerIdentity and Settings_Packages
                         tables.

ComputerRoles            Used to find all roles to be associated with the target computer. The
                         view is a join of the ComputerIdentity and Settings_Roles tables.

ComputerSettings         Used to find all property settings to be configured for the target
                         computer. The view is a join of the ComputerIdentity and Settings
                         tables.

LocationAdministrators   Used to find all the accounts to be made a member of the local
                         Administrators group on the target computers within a location. The
                         view is a join of the LocationIdentity,
                         LocationIdentity_DefaultGateway, and Settings_Administrators
                         tables.

LocationApplications     Used to find all the applications to be deployed to the target
                         computers within a location. The view is a join of the
                         LocationIdentity, LocationIdentity_DefaultGateway, and
                         Settings_Applications tables.

LocationPackages         Used to find all the packages to be deployed to the target
                         computers within a location. The view is a join of the
                         LocationIdentity, LocationIdentity_DefaultGateway, and
                         Settings_Packages tables.

LocationRoles            Used to find all the roles to be associated with the target computers
                         within a location. The view is a join of the LocationIdentity,
                         LocationIdentity_DefaultGateway, and Settings_Roles tables.

Locations                Used to find the IP addresses for the default gateways within a
                         location or for all the locations that contain a specified IP address for
                         a default gateway. The view is a join of the LocationIdentity and
                         LocationIdentity_DefaultGateway tables.

LocationSettings         Used to find all the property settings to be configured for the target
                         computers within a location. The view is a join of the
                         LocationIdentity, LocationIdentity_DefaultGateway, and Settings
                         tables.

<!-- p.1426 -->

View                       Description

MakeModelAdministrators    Used to find all accounts to be made members of the local
                           Administrators group on the target computers with a given make
                           and model. The view is a join of the MakeModelIdentity and
                           Settings_Administrators tables.

MakeModelApplications      Used to find all applications to be deployed to the target computers
                           with a given make and model. The view is a join of the
                           MakeModelIdentity and Settings_Applications tables.

MakeModelPackages          Used to find all packages to be deployed to the target computers
                           with a given make and model. The view is a join of the
                           MakeModelIdentity and Settings_Applications tables.

MakeModelRoles             Used to find all roles associated with the target computers with a
                           given make and model. The view is a join of the MakeModelIdentity
                           and Settings_Roles tables.

MakeModelSettings          Used to find all property settings to be configured for the target
                           computers with a given make and model. The view is a join of the
                           MakeModelIdentity and Settings tables.

RoleAdministrators         Used to find all accounts to be made members of the local
                           Administrators group on the target computers with a given role. The
                           view is a join of the RoleIdentity and Settings_Administrators tables.

RoleApplications           Used to find all applications to be deployed to the target computers
                           with a given role. The view is a join of the RoleIdentity and
                           Settings_Applications tables.

RolePackages               Used to find all packages to be deployed to the target computers
                           with a given role. The view is a join of the RoleIdentity and
                           Settings_Packages tables.

RoleSettings               Used to find all property settings to be configured for the target
                           computers with a given role. The view is a join of the RoleIdentity
                           and Settings tables.

Related articles
    Task Sequence Steps.
    Properties.
    Scripts.
    Support Files.
    Utilities.
    MDT Windows PowerShell Cmdlets.
    Windows 7 Feature Dependency Reference.

<!-- p.1427 -->

     UDI Reference.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1428 -->

Windows 7 Feature Dependency
Reference
Article • 02/12/2024

Table 8 lists the Windows 7 features, the parent feature, and any dependent features.
You can use this information to determine which features and roles need to be installed
to support a specific feature using the Install Roles and Features and Uninstall Roles and
Features task sequence steps.

Table 8. Windows 7 Feature Dependency
Reference
                                                                                    ﾉ   Expand table

 Feature               Parent Feature                     Dependent Features

 Windows Media®        Media Features                     Might affect other Windows features
 Center

 Windows DVD           Media Features                     Might affect other Windows features
 Maker

 Windows Media         Media Features                     Might affect other Windows features
 Player

 Windows Search        N/A                                Might affect other Windows features

 Internet Explorer     N/A                                Might affect other Windows features
 (amd64)

 World Wide Web        Microsoft Internet Information     - Microsoft Message Queuing (MSMQ)
 services              Services (IIS)                     HTTP support

                                                          - Windows Communication Foundation
                                                          (WCF) HTTP activation

 IIS 6 WMI             IIS, Web management tools, IIS 6   IIS 6 scripting tooling
 compatibility         management compatibility

 Microsoft .NET        IIS, World Wide Web services,      - Microsoft ASP.NET
 extensibility         application development features
                                                          - MSMQ HTTP support

                                                          - WCF HTTP activation

<!-- p.1429 -->

Feature             Parent Feature                  Dependent Features

Default document    IIS, World Wide Web services,   MSMQ HTTP support
                    common HTTP features

Directory           IIS, World Wide Web services,   MSMQ HTTP support
browsing            common HTTP features

HTTP redirection    IIS, World Wide Web services,   MSMQ HTTP support
                    common HTTP features

Static content      IIS, World Wide Web services,   - Web-based Distributed Authoring
                    common HTTP features            and Versioning (WebDAV) publishing

                                                    - MSMQ HTTP support

Custom logging      IIS, World Wide Web services,   MSMQ HTTP support
                    health and diagnostics

HTTP logging        IIS, World Wide Web services,   MSMQ HTTP support
                    health and diagnostics

ODBC logging        IIS, World Wide Web services,   MSMQ HTTP support
                    health and diagnostics

Request Monitor     IIS, World Wide Web services,   MSMQ HTTP support
                    health and diagnostics

Tracing             IIS, World Wide Web services,   MSMQ HTTP support
                    health and diagnostics

Static content      IIS, World Wide Web services,   MSMQ HTTP support
compression         performance features

Security            IIS, World Wide Web services    - Microsoft .NET extensibility

                                                    - MSMQ HTTP support

                                                    - WCF HTTP activation

Request Filtering   IIS, World Wide Web services,   - Microsoft .NET extensibility
                    security
                                                    - MSMQ HTTP support

                                                    - WCF HTTP activation

XPS Viewer          N/A                             Might affect other Windows features

Related articles

<!-- p.1430 -->

     Task Sequence Steps.
     Properties.
     Scripts.
     Support Files.
     Utilities.
     MDT Windows PowerShell Cmdlets.
     Tables and Views in the MDT DB.
     UDI Reference.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1431 -->

UDI Reference
Article • 02/12/2024

This reference provides further information about UDI and includes topics on:

      UDI concepts as described in UDI Concepts

      OSDResults as described in OSDResults Reference

      User Centric App Installer as described in User-Centric App Installer Reference

      UDI stages as described in UDI Stage Reference

      UDI tasks as described in UDI Task Reference

      UDI validators as described in UDI Validator Reference

      UDI Wizard Pages as described in UDI Wizard Page Reference

Each of these reference topics are discussed in subsequent sections.

UDI Concepts
This section contains concepts that help describe UDI, the UDI Wizard, and the UDI
Wizard Designer.

Display Name
The display name is used to provide a user-friendly, descriptive name for a wizard page
within the Page Library in the UDI Wizard Designer. The display name is displayed in
blue text for each wizard page in the Page Library and on the Flow tab in the UDI
Wizard Designer.

When you add a page to the Page Library, you must provide the display name. After the
wizard page is added to the Page Library, you cannot change the display name.

Flow
The Flow tab displays the list of wizard pages within a UDI stage in the UDI Wizard
Designer. You can use the Flow tab to perform the following tasks:

      Add a wizard page from the Page Library to a UDI stage by dragging the page
      from the Page Library to the UDI stage.

<!-- p.1432 -->

     Remove a wizard page from a UDI stage.

     Change the sequence of wizard pages within a UDI stage.

Page Library
The Page Library contains all the pages currently loaded in the UDI Wizard Designer.
When loading a UDI Wizard configuration file, all of the wizard pages defined in the
configuration file are displayed to the Page Library. The Page Library shows the wizard
pages in alphabetical order by page types. Each instance of a specific page type is listed
under the page type.

For example, you may need two different WelcomePage wizard pages for different
stages. The two WelcomePage wizard pages will be listed under the WelcomePage
wizard page type in the Page Library in the UDI Wizard Designer.

In addition, each wizard page instance in the Page Library indicates how many times the
wizard page is used in the stage flows. When you hover over a wizard page in the Page
Library, a thumbnail of the wizard page is displayed along with the stages that include
that page.

Page Name
The page name is used to uniquely identify a wizard page within the Page Library in the
UDI Wizard Designer. The page name is the name a UDI stage references so that the UDI
Wizard knows which wizard page to display within a specific UDI stage. When you add a
page to the Page Library, you must provide the page name. After the wizard page is
added to the Page Library, you cannot change the page name. In the UDI Wizard
Designer, the page name is shown at the bottom of each wizard page in the Page
Library in smaller, non-bold text.

Prestaged Media Deployments
Prestaged media support is an operating system deployment feature in Configuration
Manager that allows an administrator to copy and apply prestage bootable media and
an operating system image to a hard disk prior to the provisioning process. This work
can reduce network traffic and the time needed for the provisioning process. Prestaged
media can be deployed as part of the manufacturing process or at an enterprise staging
center that is not connected to the Configuration Manager environment.

For more information about prestaged media deployments, see the following resources:

<!-- p.1433 -->

     Planning for Media Operating System Deployments in Configuration Manager

     About Prestaged Media for Operating System Deployment

Stage Group
Use a stage group to group one or more stages in the UDI Wizard Designer. UDI stage
groups are loosely related to MDT deployment scenarios, but there is no one-to-one
correlation between the two.

Stage
A stage is a subset of all the pages in the UDI Wizard configuration file that an MDT
deployment scenario uses. When you start the UDI Wizard using the UDI Wizard task
sequence step, the /stage parameter specifies the stage to run, which in turn specifies
the set of pages to use. You can preview how wizard pages will appear in a stage by
selecting Preview in the Preview Wizard group on the Ribbon. You can use a UDI stage
in more than one MDT deployment scenario, even though the UDI stage is defined only
once in the UDI Wizard Designer. For example, the NewComputer stage can be used in
the MDT New Computer and Replace Computer deployment scenarios.

Task
UDI tasks are software that is run on a wizard page to perform specific functions. In
some instances, these tasks are used to verify that the target computer is ready for
deployment. Other tasks can be used to perform deployment steps, such as copying
configuration or result files.

  ７ Note

  The Next button on the wizard page where the tasks are run will be disabled if any
  of the tasks finish with warning or error completion status.

UDI includes several built-in tasks that allow you to perform most of the tasks necessary
for deployment. For more information about the UDI built-in tasks, see Built-in UDI
Tasks.

The Shell Execute built-in UDI task allows you to run any software (scripts) that can be
initiated from a command line, such as Visual Basic or Windows PowerShell scripts. This
functionality allows you create tasks using familiar scripting languages. For more
information, see Shell Execute Task.

<!-- p.1434 -->

If your requirements go beyond scripting, you can write custom UDI tasks. UDI tasks are
DLLs written in C++ and implement the ITask interface. You register the DLL with the
UDI Wizard Designer task library by creating a UDI Wizard Designer configuration
(.config) file and placing it in the installation_folder\Bin\Config folder (where
installation_folder is the folder in which you installed MDT). For more information on
developing custom UDI tasks, see the section, "Creating Custom UDI Tasks", in the User-
Driven Installation Developers Guide.

UDI Task Sequence
You create a UDI task sequence using one of the following UDI-specific MDT task
sequence templates, which run the UDI Wizard at the appropriate step in the task
sequence:

     User-Driven Installation Task Sequence. This task sequence template is used for
     the New Computer, Refresh Computer, and Replace Computer MDT deployment
     scenarios.

     User-Driven Installation Replace Task Sequence. This task sequence template is
     the first step in a two-step process in the Replace Computer deployment scenario
     and is used to capture user state migration data. The second step in the two-step
     process is the User-Driven Installation Task Sequence task sequence template,
     which you use to deploy the target applications and operating system and restore
     the user state migration data saved during the first step of the process.

     For more information about UDI task sequence templates, see the section,
     "Identify the UDI Task Sequence Templates in MDT", in the MDT document Using
     the Microsoft Deployment Toolkit. For more information about these components,
     see the section, "Identify UDI Deployment Process Components", in the MDT
     document Using the Microsoft Deployment Toolkit, which is included with MDT.

UDI Wizard
The UDI Wizard provides the UI for collecting deployment settings that the UDI task
sequences consume. The UDI Wizard is initiated as a part of a UDI task sequence and
collects the necessary configuration information for customizing the deployment of the
Windows client operating systems and applications. The wizard pages read their
configuration settings from the UDI Wizard configuration file, which is customized using
the UDI Wizard Designer.

The UDI Wizard is initiated by the UDI Wizard task sequence step in task sequences
created using the UDI task sequence templates. The UDI Wizard task sequence step

<!-- p.1435 -->

runs the UDIWizard.wsf script, which in turn initiates the UDI Wizard
(OSDSetupWizard.exe). Table 9 lists the UDI Wizard command-line parameters and
provides a brief description of each.

Table 9. UDI Wizard Command-Line Parameters
                                                                                   ﾉ   Expand table

 Parameter   Description

 /preview    Allows you to preview the current configuration of the wizard by enabling the Next
             button, which allows you to move from page to page without requiring valid input.

 /xml        Specifies the name of the UDI Wizard configuration file. The UDIWizard.wsf script
             automatically sets this parameter to the OSDSetupWizard.xml file, which is stored in
             the folder in which the task sequence stores log files. This parameter defaults to the
             config.xml file.

             The syntax for this parameter is as follows (where <full_path> is the fully qualified
             path to the .xml file, including the file name and extension):

             /xml:<full_path>

 /stage      Specifies the name of the UDI stage to run. The UDIWizard.wsf script automatically
             sets this parameter to the appropriate stage, as described in UDI Stage Reference.
             This parameter defaults to the first stage in the UDI Wizard configuration file.

             The syntax for this parameter is as follows (where <stage_name> is the name of the
             stage to be run):

             /stage:<stage_name>

             Note:

             The value for <stage_name> is case sensitive.

 /locale     Specifies the language to use in the UDI Wizard in the form of a locale identifier
             (LCID), which is represented by a numeric value. For a list of the available LCIDs, see
             Locale IDs Assigned by Microsoft.

             You would use this list to identify the language you want to use, and then provide
             the corresponding LCID.

             The syntax for this parameter is as follows (where <locale_id> is the numeric value
             of the LCID to be used):

             /locale:<locale_id>

<!-- p.1436 -->

UDI Wizard Application Configuration File
The ApplicationPage wizard page configures the UDI Wizard application configuration
file, which maintains the list of software to be installed. This file contains an entry for
each Configuration Manager application or program and package that was added using
the UDI Wizard Designer.

This file has the same name as the UDI Wizard configuration file but with a .app
extension. For example, if the UDI Wizard configuration file is named Config.xml, then
the corresponding UDI Wizard application configuration file would be Config.xml.app.
This file is the companion to the UDI Wizard configuration file.

UDI Wizard Configuration File
The UDI Wizard reads the UDI Wizard configuration file to determine the wizard pages
to be displayed, the sequence of the wizard pages, any default for controls on the
wizard pages, and whether the controls are enabled or disabled. This file contains all the
configuration settings that are displayed in the UDI Wizard and are configured using the
UDI Wizard Designer.

A separate configuration file—the UDI Wizard application configuration file—is used to
configure applications to be installed on the target computer.

UDI Wizard Designer
The UDI Wizard Designer is the primary tool for customizing wizard pages for the
different deployment scenarios that UDI supports. Changes made in the UDI Wizard
Designer are saved in the UDI Wizard configuration file and ultimately reflected in the
user experience in the UDI Wizard. The user performing the deployment will see only
the wizard pages in the UDI Wizard that you have selected and configured using the
UDI Wizard Designer.

Although the UDI Wizard would run with the default UDI Wizard configuration file, the
wizard pages would not be configured correctly. It is recommended that you use the
UDI Wizard Designer to configure the UDI Wizard user experience.

  ７ Note

  To run the UDI Wizard Designer, you must have the appropriate rights in
  Configuration Manager to access objects such as packages, applications, or images.

<!-- p.1437 -->

Validator
You use UDI validators to help ensure that the correct information is entered into text
fields on wizard pages in the UDI Wizard. UDI includes several built-in validators that
help you perform typical validations of fields used for entering text, such as preventing
users from entering invalid characters and ensuring that the field is not empty. When a
validator detects an invalid entry in a text box, a message is displayed on the wizard
page, and the Next button is disabled until all invalid entries are resolved.

UDI includes built-in validators that allow you to perform most of the validation
necessary for deployment. For more information about the UDI built-in validators, see
Built-in UDI Validators.

If your requirements go beyond the built-in UDI validators, you can write custom UDI
validators. UDI validators are DLLs written in C++ that implement the IValidator
interface. Register the DLL with the UDI Wizard Designer validator library by creating a
UDI Wizard Designer configuration (.config) file and placing it in the
installation_folder\Bin\Config folder (where installation_folder is the folder in which you
installed MDT). For more information on developing custom UDI tasks, see the section,
"Creating Custom UDI Validators", in the MDT document User-Driven Installation
Developers Guide.

Wizard Page
You use a wizard page to collect configuration information in the UDI Wizard. Configure
UDI wizard pages using the UDI Wizard Designer. The configuration settings are stored
in the UDI Wizard configuration file and are read by the wizard page when the page is
initialized in the UDI Wizard.

Wizard pages are stored in the wizard Page Library, and they can be used in one or
more UDI stages. This design allows you to configure a wizard page that is shared
between stages once for all stages, dramatically reducing the amount of effort required
and the complexity of updating wizard page configuration.

UDI includes built-in wizard pages and wizard page editors that are typically sufficient
for most deployments. For more information about the built-in wizard pages, see Built-
in UDI Wizard Pages.

If your requirements go beyond the built-in UDI wizard pages and corresponding wizard
page editors, you can write custom UDI wizard pages and wizard page editors. UDI
wizard pages are implemented as DLLs that the UDI Wizard reads. Wizard page editors
are created using C++ in Visual Studio.

<!-- p.1438 -->

For more information on developing custom UDI wizard pages, see the section,
"Creating Custom UDI Wizard Pages", in the MDT document User-Driven Installation
Developers Guide.

Wizard Page Editor
You use a wizard page editor to configure a wizard page in the UDI Wizard Designer. A
wizard page editor updates the wizard page configuration settings in the UDI Wizard
configuration file; UDI includes a built-in wizard page editor for each built-in wizard
page. For more information about the built-in wizard pages and wizard page editors,
see Built-in UDI Wizard Pages.

If your requirements go beyond the built-in UDI wizard pages and corresponding wizard
page editors, you can write custom UDI wizard pages and wizard page editors. UDI
wizard page editors are implemented as DLLs that the UDI Wizard Designer reads.
Create wizard page editors using:

     Windows Presentation Foundation version 4.0

     Microsoft Prism    version 4.0

     Microsoft Unity Application Block     (Unity) version 2.1

     For more information on developing custom UDI wizard page editors, see the
     section, "Creating Custom Wizard Page Editors", in the MDT document User-Driven
     Installation Developers Guide.

OSDResults Reference
OSDResults is a part of UDI that displays the results of a deployment performed using
UDI. OSDResults displays the Deployment Complete dialog box. OSDResults is
displayed prior to Windows logon the first time the target computer is started. The user
can use OSDResults and the information in the Deployment Complete dialog box to
determine the completion status of the deployment process and the configuration of
the computer prior to logging on for the first time. In addition, the information in
OSDResults can be used for troubleshooting any problems encountered during the
deployment process.

You can configure some of the user interface elements for OSDResults using the
OSDResults.exe.config file, which resides in Tools\OSDResults in the MDT files
Configuration Manager package. Table 10 lists the configuration settings in the
OSDResults.exe.config file.

<!-- p.1439 -->

Table 10. Configuration Settings in the
OSDResults.exe.config File
                                                                                 ﾉ    Expand table

 Setting               Description

 headerImagePath       This setting allows you to specify the fully qualified or relative path to a
                       .bmp file that is displayed in the header of the OSDResults dialog box.

                       The default value for this setting is as follows:

                       images\UDI_Wizard_Banner.bmp

 backgroundWallpaper   This setting allows you to specify the fully qualified or relative path to a
                       .jpg file that is displayed as the wallpaper in the OSDResults dialog box.

                       The default value for this setting is as follows:

                       images\Wallpaper.jpg

 welcomeText           This setting allows you to specify the text that welcomes the user and
                       provides information about the deployment process. It is displayed in
                       the OSDResults dialog box.

 completedText         This setting allows you to specify the text that indicates whether the
                       deployment process is complete. It is displayed in the OSDResults dialog
                       box.

 timeoutMinutes        This setting allows you to specify the length of time the OSDResults
                       dialog box is displayed prior to automatically displaying the Windows
                       logon screen. The value for this setting is specified in minutes.

                       The default value for this setting is zero (0), which indicates that the
                       OSDResults dialog box will be displayed indefinitely until manually
                       closed.

The following is the high-level process for how the OSDResults feature works in UDI:

   1. A task sequence runs on the target computer.

     The task sequence is based on one of the followUDI task sequence templates:

           User Driven Installation Task Sequence. This task sequence template is used
           for the MDT New Computer, Refresh Computer, and Replace Computer MDT
           deployment scenarios.

<!-- p.1440 -->

        User-Driven Installation Replace Task Sequence. This task sequence template
        is the first step in a two-step process in the MDT Replace Computer
        deployment scenario and is used to capture user state migration data. The
        second step in the two step process is the MDT New Computer deployment
        scenario using the User Driven Installation Task Sequence task sequence
        template, which is used to deploy the target applications and operating
        system and restore the user state migration data saved during the first step
        of the process

        For more information about the:

        UDI task sequence templates, see the section, "Identify the UDI Task
        Sequence Templates in MDT", in the MDT document Using the Microsoft
        Deployment Toolkit

        Relationship between MDT deployment scenarios and UDI stages, see UDI
        Stage Reference

2. During the task sequence, the configuration settings provided by task sequence
  variables and from user input in the UDI Wizard are saved in the
  %DEPLOYROOT%\Tools\OSDResults folder on the target computer (where
  %DEPLOYROOT% is the root of the folder in which the MDT files are locally cached
  on the target computer).

3. In the OSD Results and Branding group in the task sequence, the following task
  sequence steps are run that affect OSDResults:

        Cache OSD Results. This task sequence step copies the contents of the
        %DEPLOYROOT%\Tools\OSDResults folder to the %WINDIR%\UDI folder on
        the target computer. This ensures that the contents of the OSDResults folder
        will be persisted after the task sequence finishes.

        Run OSD Results. This tasks sequence step configures the target computer to
        run OSDResults the first time the computer starts.

4. The target computer starts for the first time, and OSDResults.exe is run prior to the
  Windows logon screen.

  The Welcome tab in the Deployment Complete dialog box is displayed. The
  Welcome tab provides helpful information about the deployment and contact
  information in the event that issues with the deployment are discovered.

  Review the information on the Deployment Summary and Applications Installed
  tabs to verify that the operating system and applications were installed correctly.
