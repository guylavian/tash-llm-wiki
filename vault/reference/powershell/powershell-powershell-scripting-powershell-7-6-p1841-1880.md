---
title: "How to use this documentation — pages 1841-1880"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1841-1880
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1841-1880
family: powershell
documentKind: "doc"
abstract: "PowerShell Import-Module -Name C:\\myRandomDirectory\\myModule -Verbose You can also use the -Verbose parameter to identify what is being exported out of the module, and what is being imported into active memory. Both exports and imports restrict what is exposed to the user: the d"
---

# How to use this documentation — pages 1841-1880

<!-- p.1841 -->

 PowerShell

 Import-Module -Name C:\myRandomDirectory\myModule -Verbose

You can also use the -Verbose parameter to identify what is being exported out of the module,
and what is being imported into active memory. Both exports and imports restrict what is
exposed to the user: the difference is who is controlling the visibility. Essentially, exports are
controlled by code within the module. In contrast, imports are controlled by the Import-Module
call. For more information, see Restricting Members That Are Imported, below.

Implicitly Importing a Module (PowerShell 3.0)
Beginning in Windows PowerShell 3.0, modules are imported automatically when any cmdlet or
function in the module is used in a command. This feature works on any module in a directory
that is included in the value of the PSModulePath environment variable. If you do not save
your module on a valid path however, you can still load them using the explicit Import-Module
option, described above.

The following actions trigger automatic importing of a module, also known as "module auto-
loading."

     Using a cmdlet in a command. For example, typing Get-ExecutionPolicy imports the
     Microsoft.PowerShell.Security module that contains the Get-ExecutionPolicy cmdlet.

     Using the Get-Command cmdlet to get the command. For example, typing Get-Command
     Get-JobTrigger imports the PSScheduledJob module that contains the Get-JobTrigger

     cmdlet. A Get-Command command that includes wildcard characters is considered to be
     discovery and does not trigger importing of a module.

     Using the Get-Help cmdlet to get help for a cmdlet. For example, typing Get-Help Get-
     WinEvent imports the Microsoft.PowerShell.Diagnostics module that contains the Get-

     WinEvent cmdlet.

To support automatic importing of modules, the Get-Command cmdlet gets all cmdlets and
functions in all installed modules, even if the module is not imported into the session. For more
information, see the help topic for the Get-Command cmdlet.

The Importing Process

<!-- p.1842 -->

When a module is imported, a new session state is created for the module, and a
System.Management.Automation.PSModuleInfo object is created in memory. A session-state is
created for each module that is imported (this includes the root module and any nested
modules). The members that are exported from the root module, including any members that
were exported to the root module by any nested modules, are then imported into the caller's
session state.

The metadata of members that are exported from a module have a ModuleName property.
This property is populated with the name of the module that exported them.

  ２ Warning

  If the name of an exported member uses an unapproved verb or if the name of the
  member uses restricted characters, a warning is displayed when the Import-Module
  cmdlet is run.

By default, the Import-Module cmdlet does not return any objects to the pipeline. However,
the cmdlet supports a PassThru parameter that can be used to return a
System.Management.Automation.PSModuleInfo object for each module that is imported. To
send output to the host, users should run the Write-Host cmdlet.

Restricting the Members That Are Imported
When a module is imported by using the Import-Module cmdlet, by default, all exported
module members are imported into the session, including any commands exported to the
module by a nested module. By default, variables and aliases are not exported. To restrict the
members that are exported, use a module manifest. To restrict the members that are imported,
use the following parameters of the Import-Module cmdlet.

     Function: This parameter restricts the functions that are exported. (If you are using a
     module manifest, see the FunctionsToExport key.)

     `Cmdlet: This parameter restricts the cmdlets that are exported (If you are using a module
     manifest, see the CmdletsToExport key.)

     Variable: This parameter restricts the variables that are exported (If you are using a
     module manifest, see the VariablesToExport key.)

<!-- p.1843 -->

     Alias: This parameter restricts the aliases that are exported (If you are using a module
     manifest, see the AliasesToExport key.)

See Also
Writing a Windows PowerShell Module

Last updated on 05/20/2025

<!-- p.1844 -->

Windows PowerShell Provider Quickstart
This topic explains how to create a Windows PowerShell provider that has basic functionality of
creating a new drive. For general information about providers, see Windows PowerShell
Provider Overview. For examples of providers with more complete functionality, see Provider
Samples.

Writing a basic provider
The most basic functionality of a Windows PowerShell provider is to create and remove drives.
In this example, we implement the
System.Management.Automation.Provider.DriveCmdletProvider.NewDrive* and
System.Management.Automation.Provider.DriveCmdletProvider.RemoveDrive* methods of the
System.Management.Automation.Provider.DriveCmdletProvider class. You will also see how to
declare a provider class.

When you write a provider, you can specify default drives-drives that are created automatically
when the provider is available. You also define a method to create new drives that use that
provider.

The examples provided in this topic are based on the AccessDBProviderSample02 sample,
which is part of a larger sample that represents an Access database as a Windows PowerShell
drive.

Setting up the project
In Visual Studio, create a Class Library project named AccessDBProviderSample. Complete the
following steps to configure your project so that Windows PowerShell will start, and the
provider will be loaded into the session, when you build and start your project.

Configure the provider project

   1. Add the System.Management.Automation assembly as a reference to your project.

   2. Click Project > AccessDBProviderSample Properties > Debug. In Start project, click Start
     external program, and navigate to the Windows PowerShell executable (typically
     C:\Windows\System32\WindowsPowerShell\v1.0\.powershell.exe).

<!-- p.1845 -->

     3. Under Start Options, enter the following into the Command line arguments box: -NoExit
       -Command "[Reflection.Assembly]::LoadFrom(AccessDBProviderSample.dll' ) | Import-

       Module"

Declaring the provider class
Our provider derives from the System.Management.Automation.Provider.DriveCmdletProvider
class. Most providers that provide real functionality (accessing and manipulating items,
navigating the data store, and getting and setting content of items) derive from the
System.Management.Automation.Provider.NavigationCmdletProvider class.

In addition to specifying that the class derives from
System.Management.Automation.Provider.DriveCmdletProvider, you must decorate it with the
System.Management.Automation.Provider.CmdletProviderAttribute as shown in the example.

 C#

 namespace Microsoft.Samples.PowerShell.Providers
 {
   using System;
   using System.Data;
   using System.Data.Odbc;
   using System.IO;
   using System.Management.Automation;
   using System.Management.Automation.Provider;

     #region AccessDBProvider

     [CmdletProvider("AccessDB", ProviderCapabilities.None)]
     public class AccessDBProvider : DriveCmdletProvider
     {

 }
 }

Implementing NewDrive
The System.Management.Automation.Provider.DriveCmdletProvider.NewDrive* method is
called by the Windows PowerShell engine when a user calls the
Microsoft.PowerShell.Commands.NewPSDriveCommand cmdlet specifying the name of your
provider. The PSDriveInfo parameter is passed by the Windows PowerShell engine, and the
method returns the new drive to the Windows PowerShell engine. This method must be
declared within the class created above.

<!-- p.1846 -->

The method first checks to make sure both the drive object and the drive root that were passed
in exist, returning null if either of them do not. It then uses a constructor of the internal class
AccessDBPSDriveInfo to create a new drive and a connection to the Access database the drive
represents.

 C#

 protected override PSDriveInfo NewDrive(PSDriveInfo drive)
     {
       // Check if the drive object is null.
       if (drive == null)
       {
         WriteError(new ErrorRecord(
                    new ArgumentNullException("drive"),
                    "NullDrive",
                    ErrorCategory.InvalidArgument,
                    null));

              return null;
          }

          // Check if the drive root is not null or empty
          // and if it is an existing file.
          if (String.IsNullOrEmpty(drive.Root) || (File.Exists(drive.Root) == false))
          {
            WriteError(new ErrorRecord(
                       new ArgumentException("drive.Root"),
                       "NoRoot",
                       ErrorCategory.InvalidArgument,
                       drive));

              return null;
          }

          // Create a new drive and create an ODBC connection to the new drive.
          AccessDBPSDriveInfo accessDBPSDriveInfo = new AccessDBPSDriveInfo(drive);
          OdbcConnectionStringBuilder builder = new OdbcConnectionStringBuilder();

          builder.Driver = "Microsoft Access Driver (*.mdb)";
          builder.Add("DBQ", drive.Root);

          OdbcConnection conn = new OdbcConnection(builder.ConnectionString);
          conn.Open();
          accessDBPSDriveInfo.Connection = conn;

          return accessDBPSDriveInfo;
      }

The following is the AccessDBPSDriveInfo internal class that includes the constructor used to
create a new drive, and contains the state information for the drive.

<!-- p.1847 -->

 C#

 internal class AccessDBPSDriveInfo : PSDriveInfo
   {
     /// <summary>
     /// A reference to the connection to the database.
     /// </summary>
     private OdbcConnection connection;

       /// <summary>
       /// Initializes a new instance of the AccessDBPSDriveInfo class.
       /// The constructor takes a single argument.
       /// </summary>
       /// <param name="driveInfo">Drive defined by this provider</param>
       public AccessDBPSDriveInfo(PSDriveInfo driveInfo)
              : base(driveInfo)
       {
       }

       /// <summary>
       /// Gets or sets the ODBC connection information.
       /// </summary>
       public OdbcConnection Connection
       {
           get { return this.connection; }
           set { this.connection = value; }
       }
   }

Implementing RemoveDrive
The System.Management.Automation.Provider.DriveCmdletProvider.RemoveDrive* method is
called by the Windows PowerShell engine when a user calls the
Microsoft.PowerShell.Commands.RemovePSDriveCommand cmdlet. The method in this
provider closes the connection to the Access database.

 C#

 protected override PSDriveInfo RemoveDrive(PSDriveInfo drive)
     {
       // Check if drive object is null.
       if (drive == null)
       {
         WriteError(new ErrorRecord(
                    new ArgumentNullException("drive"),
                    "NullDrive",
                    ErrorCategory.InvalidArgument,
                    drive));

            return null;
        }

<!-- p.1848 -->

          // Close the ODBC connection to the drive.
          AccessDBPSDriveInfo accessDBPSDriveInfo = drive as AccessDBPSDriveInfo;

          if (accessDBPSDriveInfo == null)
          {
             return null;
          }

          accessDBPSDriveInfo.Connection.Close();

          return accessDBPSDriveInfo;
      }

Last updated on 08/15/2025

<!-- p.1849 -->

Windows PowerShell Provider Overview
A Windows PowerShell provider allows any data store to be exposed like a file system as if it
were a mounted drive. For example, the built-in Registry provider allows you to navigate the
registry like you would navigate the c drive of your computer. A provider can also override the
Item cmdlets (for example, Get-Item , Set-Item , etc.) such that the data in your data store can

be treated like files and directories are treated when navigating a file system. For more
information about providers and drives, and the built-in providers in Windows PowerShell, see
about_Providers.

Providers and Drives
A Provider defines the logic that is used to access, navigate, and edit a data store, while a drive
specifies a specific entry point to a data store (or a portion of a data store) that is of the type
defined by the provider. For example, the Registry provider allows you to access hives and keys
in a registry, and the HKLM and HKCU drives specify the corresponding hives within the
registry. The HKLM and HKCU drives both use the Registry provider.

When you write a provider, you can specify default drives-drives that are created automatically
when the provider is available. You also define a method to create new drives that use that
provider.

Type of Providers
There are several types of providers, each of which provides a different level of functionality. A
provider is implemented as a class that derives from one of the descendants of the
System.Management.Automation.SessionStateCategory CmdletProvider class. For information
about the different types of providers, see Provider types.

Provider cmdlets
Providers can implement methods that correspond to cmdlets, creating custom behaviors for
those cmdlets when used in a drive for that provider. Depending on the type of provider,
different sets of cmdlets are available. For a complete list of the cmdlets available for
customization in providers, see Provider cmdlets.

<!-- p.1850 -->

Provider paths
Users navigate provider drives like file systems. Because of this, they expect the syntax of paths
to correspond to the paths used in file system navigation. When a user runs a provider cmdlet,
they specify a path to the item to be accessed. The path that is specified can be interpreted in
several ways. A provider should support one or more of the following path types.

Drive-qualified paths
A drive-qualified path is a combination of the item name, the container and subcontainers in
which the item is located, and the Windows PowerShell drive through which the item is
accessed. (Drives are defined by the provider that is used to access the data store. This path
starts with the drive name followed by a colon (:). For example: Get-ChildItem C:

Provider-qualified paths
To allow the Windows PowerShell engine to initialize and uninitialize your provider, the
provider must support a provider-qualified path. For example, the user can initialize and
uninitialize the FileSystem provider because it defines the following provider-qualified path:
FileSystem::\\uncshare\abc\bar .

Provider-direct paths
To allow remote access to your Windows PowerShell provider, it should support a provider-
direct path to pass directly to the Windows PowerShell provider for the current location. For
example, the registry Windows PowerShell provider can use \\server\regkeypath as a
provider-direct path.

Provider-internal paths
To allow the provider cmdlet to access data using non-Windows PowerShell application
programming interfaces (APIs), your Windows PowerShell provider should support a provider-
internal path. This path is indicated after the "::" in the provider-qualified path. For example, the
provider-internal path for the FileSystem Windows PowerShell provider is \\uncshare\abc\bar .

Overriding cmdlet parameters
The behavior of some provider-specific cmdlets can be overridden by a provider. For a list of
parameters that can be overridden, and how to override them in your provider class, see

<!-- p.1851 -->

Provider cmdlet parameters

Dynamic parameters
Providers can define dynamic parameters that are added to a provider cmdlet when the user
specifies a certain value for one of the static parameters of the cmdlet. A provider does this by
implementing one or more dynamic parameter methods. For a list of cmdlet parameters that
can be used to add dynamic parameter, and the methods used to implement them, see
Provider cmdlet dynamic parameters.

Provider capabilities
The System.Management.Automation.Provider.ProviderCapabilities enumeration defines a
number of capabilities that providers can support. These include the ability to use wildcards,
filter items, and support transactions. To specify capabilities for a provider, add a list of values
of the System.Management.Automation.Provider.ProviderCapabilities enumeration, combined
with a logical OR operation, as the
System.Management.Automation.Provider.CmdletProviderAttribute.ProviderCapabilities*
property (the second parameter of the attribute) of the
System.Management.Automation.Provider.CmdletProviderAttribute attribute for your provider
class. For example, the following attribute specifies that the provider supports the
System.Management.Automation.Provider.ProviderCapabilities ShouldProcess and
System.Management.Automation.Provider.ProviderCapabilities Transactions capabilities.

 C#

 [CmdletProvider(RegistryProvider.ProviderName, ProviderCapabilities.ShouldProcess |
 ProviderCapabilities.Transactions)]

Provider cmdlet help
When writing a provider, you can implement your own Help for the provider cmdlets that you
support. This includes a single help topic for each provider cmdlet or multiple versions of a
help topic for cases where the provider cmdlet acts differently based on the use of dynamic
parameters. To support provider cmdlet-specific help, your provider must implement the
System.Management.Automation.Provider.ICmdletProviderSupportsHelp interface.

<!-- p.1852 -->

The Windows PowerShell engine calls the
System.Management.Automation.Provider.ICmdletProviderSupportsHelp.GetHelpMaml*
method to display the Help topic for your provider cmdlets. The engine provides the name of
the cmdlet that the user specified when running the Get-Help cmdlet and the current path of
the user. The current path is required if your provider implements different versions of the
same provider cmdlet for different drives. The method must return a string that contains the
XML for the cmdlet Help.

The content for the Help file is written using PSMAML XML. This is the same XML schema that
is used for writing Help content for stand-alone cmdlets. Add the content for your custom
cmdlet Help to the Help file for your provider under the CmdletHelpPaths element. The
following example shows the command element for a single provider cmdlet, and it shows how
you specify the name of the provider cmdlet that your provider. supports

  XML

  <CmdletHelpPaths>
    <command:command>
      <command:details>
        <command:name>ProviderCmdletName</command:name>
        <command:verb>Verb</command:verb>
        <command:noun>Noun</command:noun>
      <command:details>
    </command:command>
  <CmdletHelpPath>

See Also
Windows PowerShell Provider Functionality

Provider Cmdlets

Writing a Windows PowerShell Provider

 Last updated on 05/20/2025

<!-- p.1853 -->

Provider types
Providers define their basic functionality by changing how the provider cmdlets, provided by
PowerShell, perform their actions. For example, providers can use the default functionality of
the Get-Item cmdlet, or they can change how that cmdlet operates when retrieving items from
the data store. The provider functionality described in this document includes functionality
defined by overwriting methods from specific provider base classes and interfaces.

  ７ Note

  For provider features that are pre-defined by PowerShell, see Provider capabilities   .

Drive-enabled providers
Drive-enabled providers specify the default drives available to the user and allow the user to
add or remove drives. In most cases, providers are drive-enabled providers because they
require some default drive to access the data store. However, when writing your own provider
you might or might not want to allow the user to create and remove drives.

To create a drive-enabled provider, your provider class must derive from the
System.Management.Automation.Provider.DriveCmdletProvider class or another class that
derives from that class. The DriveCmdletProvider class defines the following methods for
implementing the default drives of the provider and supporting the New-PSDrive and Remove-
PSDrive cmdlets. In most cases, to support a provider cmdlet you must overwrite the method

that the PowerShell engine calls to invoke the cmdlet, such as the NewDrive method for the
New-PSDrive cmdlet, and optionally you can overwrite a second method, such as

NewDriveDynamicParameters , for adding dynamic parameters to the cmdlet.

     The InitializeDefaultDrives method defines the default drives that are available to the user
     whenever the provider is used.

     The NewDrive and NewDriveDynamicParameters methods defines how your provider
     supports the New-PSDrive provider cmdlet. This cmdlet allows the user to create drives to
     access the data store.

     The RemoveDrive method defines how your provider supports the Remove-PSDrive
     provider cmdlet. This cmdlet allows the user to remove drives from the data store.

<!-- p.1854 -->

Item-enabled providers
Item-enabled providers allow the user to get, set, or clear the items in the data store. An "item"
is an element of the data store that the user can access or manage independently. To create an
item-enabled provider, your provider class must derive from the
System.Management.Automation.Provider.ItemCmdletProvider class or another class that
derives from that class.

The ItemCmdletProvider class defines the following methods for implementing specific
provider cmdlets. In most cases, to support a provider cmdlet you must overwrite the method
that the PowerShell engine calls to invoke the cmdlet, such as the ClearItem method for the
Clear-Item cmdlet, and optionally you can overwrite a second method, such as

ClearItemDynamicParameters , for adding dynamic parameters to the cmdlet.

     The ClearItem and ClearItemDynamicParameters methods define how your provider
     supports the Clear-Item provider cmdlet. This cmdlet allows the user to remove of the
     value of an item in the data store.

     The GetItem and GetItemDynamicParameters methods define how your provider supports
     the Get-Item provider cmdlet. This cmdlet allows the user to retrieve data from the data
     store.

     The SetItem and SetItemDynamicParameters methods define how your provider supports
     the Set-Item provider cmdlet. This cmdlet allows the user to update the values of items
     in the data store.

     The InvokeDefaultAction and InvokeDefaultActionDynamicParameters methods define
     how your provider supports the Invoke-Item provider cmdlet. This cmdlet allows the user
     to perform the default action specified by the item.

     The ItemExists and ItemExistsDynamicParameters methods define how your provider
     supports the Test-Path provider cmdlet. This cmdlet allows the user to determine if all
     the elements of a path exist.

In addition to the methods used to implement provider cmdlets, the ItemCmdletProvider class
also defines the following methods:

     The ExpandPath method allows the user to use wildcards when specifying the provider
     path.

<!-- p.1855 -->

     The IsValidPath is used to determine if a path is syntactically and semantically valid for the
     provider.

Container-enabled providers
Container-enabled providers allow the user to manage items that are containers. A container is
a group of child items under a common parent item. To create a container-enabled provider,
your provider class must derive from the
System.Management.Automation.Provider.ContainerCmdletProvider class or another class that
derives from that class.

  ） Important

  Container-enabled providers can't access data stores that contain nested containers. If a
  child item of a container is another container, you must implement a navigation-enabled
  provider.

The ContainerCmdletProvider class defines the following methods for implementing specific
provider cmdlets. In most cases, to support a provider cmdlet you must overwrite the method
that the PowerShell engine calls to invoke the cmdlet, such as the CopyItem method for the
Copy-Item cmdlet, and optionally you can overwrite a second method, such as

CopyItemDynamicParameters , for adding dynamic parameters to the cmdlet.

     The CopyItem and CopyItemDynamicParameters methods define how your provider
     supports the Copy-Item provider cmdlet. This cmdlet allows the user to copy an item from
     one location to another.

     The GetChildItems and GetChildItemsDynamicParameters methods define how your
     provider supports the Get-ChildItem provider cmdlet. This cmdlet allows the user to
     retrieve the child items of the parent item.

     The GetChildNames and GetChildNamesDynamicParameters methods define how your
     provider supports the Get-ChildItem provider cmdlet if its Name parameter is specified.

     The NewItem and NewItemDynamicParameters methods define how your provider
     supports the New-Item provider cmdlet. This cmdlet allows the user to create new items in
     the data store.

<!-- p.1856 -->

     The RemoveItem and RemoveItemDynamicParameters methods define how your provider
     supports the Remove-Item provider cmdlet. This cmdlet allows the user to remove items
     from the data store.

     The RenameItem and RenameItemDynamicParameters methods define how your provider
     supports the Rename-Item provider cmdlet. This cmdlet allows the user to rename items in
     the data store.

In addition to the methods used to implement provider cmdlets, the ContainerCmdletProvider
class also defines the following methods:

     The HasChildItems method can be used by the provider class to determine whether an
     item has child items.

     The ConvertPath method can be used by the provider class to create a new provider-
     specific path from a specified path.

Navigation-enabled providers
Navigation-enabled providers allow the user to move items in the data store. To create a
navigation-enabled provider, your provider class must derive from the
System.Management.Automation.Provider.NavigationCmdletProvider class.

The NavigationCmdletProvider class defines the following methods for implementing specific
provider cmdlets. In most cases, to support a provider cmdlet you must overwrite the method
that the PowerShell engine calls to invoke the cmdlet, such as the MoveItem method for the
Move-Item cmdlet, and optionally you can overwrite a second method, such as

MoveItemDynamicParameters , for adding dynamic parameters to the cmdlet.

     The MoveItem and MoveItemDynamicParameters methods define how your provider
     supports the Move-Item provider cmdlet. This cmdlet allows the user to move an item
     from one location in the store to another location.

     The MakePath method defines how your provider supports the Join-Path provider
     cmdlet. This cmdlet allows the user to combine a parent and child path segment to create
     a provider-internal path.

In addition to the methods used to implement provider cmdlets, the
NavigationCmdletProvider class also defines the following methods:

     The GetChildName method extracts the name of the child node of a path.

<!-- p.1857 -->

     The GetParentPath method extracts the parent part of a path.

     The IsItemContainer method determines whether the item is a container item. In this
     context, a container is a group of child items under a common parent item.

     The NormalizeRelativePath method returns a path to an item that's relative to a specified
     base path.

Content-enabled providers
Content-enabled providers allow the user to clear, get, or set the content of items in a data
store. For example, the FileSystem provider allows you to clear, get, and set the content of files
in the file system. To create a content enabled provider, your provider class must implement
the methods of the System.Management.Automation.Provider.IContentCmdletProvider
interface.

The IContentCmdletProvider interface defines the following methods for implementing
specific provider cmdlets. In most cases, to support a provider cmdlet you must overwrite the
method that the PowerShell engine calls to invoke the cmdlet, such as the ClearContent
method for the Clear-Content cmdlet, and optionally you can overwrite a second method,
such as ClearContentDynamicParameters , for adding dynamic parameters to the cmdlet.

     The ClearContent and ClearContentDynamicParameters methods define how your
     provider supports the Clear-Content provider cmdlet. This cmdlet allows the user to
     delete the content of an item without deleting the item.

     The GetContentReader and GetContentReaderDynamicParameters methods define how
     your provider supports the Get-Content provider cmdlet. This cmdlet allows the user to
     retrieve the content of an item. The GetContentReader method returns an
     System.Management.Automation.Provider.IContentReader interface that defines the
     methods used to read the content.

     The GetContentWriter and GetContentWriterDynamicParameters methods define how
     your provider supports the Set-Content provider cmdlet. This cmdlet allows the user to
     update the content of an item. The GetContentWriter method returns an
     System.Management.Automation.Provider.IContentWriter interface that defines the
     methods used to write the content.

Property-enabled providers

<!-- p.1858 -->

Property-enabled providers allow the user to manage the properties of the items in the data
store. To create a property-enabled provider, your provider class must implement the methods
of the System.Management.Automation.Provider.IPropertyCmdletProvider and
System.Management.Automation.Provider.IDynamicPropertyCmdletProvider interfaces. In most
cases, to support a provider cmdlet you must overwrite the method that the PowerShell engine
calls to invoke the cmdlet, such as the ClearProperty method for the Clear-Property cmdlet,
and optionally you can overwrite a second method, such as ClearPropertyDynamicParameters ,
for adding dynamic parameters to the cmdlet.

The IPropertyCmdletProvider interface defines the following methods for implementing
specific provider cmdlets:

     The ClearProperty and ClearPropertyDynamicParameters methods define how your
     provider supports the Clear-ItemProperty provider cmdlet. This cmdlet allows the user to
     delete the value of a property.

     The GetProperty and GetPropertyDynamicParameters methods define how your provider
     supports the Get-ItemProperty provider cmdlet. This cmdlet allows the user to retrieve
     the property of an item.

     The SetProperty and SetPropertyDynamicParameters methods define how your provider
     supports the Set-ItemProperty provider cmdlet. This cmdlet allows the user to update the
     properties of an item.

The IDynamicPropertyCmdletProvider interface defines the following methods for
implementing specific provider cmdlets:

     The CopyProperty and CopyPropertyDynamicParameters methods define how your
     provider supports the Copy-ItemProperty provider cmdlet. This cmdlet allows the user to
     copy a property and its value from one location to another.

     The MoveProperty and MovePropertyDynamicParameters methods define how your
     provider supports the Move-ItemProperty provider cmdlet. This cmdlet allows the user to
     move a property and its value from one location to another.

     The NewProperty and NewPropertyDynamicParameters methods define how your
     provider supports the New-ItemProperty provider cmdlet. This cmdlet allows the user to
     create a new property and set its value.

     The RemoveProperty and RemovePropertyDynamicParameters methods define how your
     provider supports the Remove-ItemProperty cmdlet. This cmdlet allows the user to delete

<!-- p.1859 -->

     a property and its value.

     The RenameProperty and RenamePropertyDynamicParameters methods define how your
     provider supports the Rename-ItemProperty cmdlet. This cmdlet allows the user to change
     the name of a property.

See also
about_Providers

Writing a Windows PowerShell Provider

Last updated on 08/25/2025

<!-- p.1860 -->

Provider cmdlets
The cmdlets that the user can run to manage a data store are referred to as provider cmdlets.
To support these cmdlets, you need to overwrite some of the methods defined by the base
provider classes and interfaces.

Here are the provider cmdlets that can be run by the user:

PSDrive cmdlets
Get-PSDrive

This cmdlet returns the PowerShell drives in the current session. You do not need to overwrite
any methods to support this cmdlet.

New-PSDrive

This cmdlet allows the user to create PowerShell drives to access the data store. To support this
cmdlet, overwrite the following methods of
System.Management.Automation.Provider.DriveCmdletProvider class:

     NewDrive
     NewDriveDynamicParameters

Remove-PSDrive

This cmdlet allows the user to remove PowerShell drives that access the data store. To support
this cmdlet, overwrite the
System.Management.Automation.Provider.DriveCmdletProvider.RemoveDrive method.

Item cmdlets
Clear-Item

This cmdlet allows the user to remove the value of an item in the data store. To support this
cmdlet, overwrite the following methods of
System.Management.Automation.Provider.ItemCmdletProvider class:

<!-- p.1861 -->

     ClearItem
     ClearItemDynamicParameters

Copy-Item

This cmdlet allows the user to copy an item from one location to another. To support this
cmdlet, overwrite the following methods of
System.Management.Automation.Provider.ContainerCmdletProvider class:

     CopyItem
     CopyItemDynamicParameters

Get-Item

This cmdlet allows the user to retrieve data from the data store. To support this cmdlet,
overwrite the following methods of
System.Management.Automation.Provider.ItemCmdletProvider class:

     GetItem
     GetItemDynamicParameters

Get-ChildItem

This cmdlet allows the user to retrieve the child items of the parent item. To support this
cmdlet, overwrite the following methods of
System.Management.Automation.Provider.ContainerCmdletProvider class:

     GetChildItems
     GetChildItemsDynamicParameters
     GetChildNames
     GetChildNamesDynamicParameters

Invoke-Item

This cmdlet allows the user to perform the default action specified by the item. To support this
cmdlet, overwrite the
System.Management.Automation.Provider.ItemCmdletProvider.InvokeDefaultAction method.

Move-Item

<!-- p.1862 -->

This cmdlet allows the user to move an item from one location to another location. To support
this cmdlet, overwrite the following methods of
System.Management.Automation.Provider.NavigationCmdletProvider class:

         MoveItem
         MoveItemDynamicParameters

New-Item

This cmdlet allows the user to create a new item in the data store. To support this cmdlet,
overwrite the following methods of
System.Management.Automation.Provider.ContainerCmdletProvider class:

         NewItem
         NewItemDynamicParameters

Remove-Item

This cmdlet allows the user to remove items from the data store. To support this cmdlet,
overwrite the following methods of
System.Management.Automation.Provider.ContainerCmdletProvider class:

         RemoveItem
         RemoveItemDynamicParameters

Rename-Item

This cmdlet allows the user to rename items in the data store. To support this cmdlet, overwrite
the following methods of System.Management.Automation.Provider.ContainerCmdletProvider
class:

         RenameItem
         RenameItemDynamicParameters

Set-Item

This cmdlet allows the user to update the values of items in the data store. To support this
cmdlet, overwrite the following methods of
System.Management.Automation.Provider.ItemCmdletProvider class:

         SetItem

<!-- p.1863 -->

     SetItemDynamicParameters

Item content cmdlets
Add-Content

This cmdlet allows the user to add content to an item.

Clear-Content

This cmdlet allows the user to delete content from an item without deleting the item. To
support this cmdlet, overwrite the following methods of
System.Management.Automation.Provider.IContentCmdletProvider interface:

     ClearContent
     ClearContentDynamicParameters

Get-Content

This cmdlet allows the user to retrieve the content of an item. To support this cmdlet, overwrite
the following methods of System.Management.Automation.Provider.IContentCmdletProvider
interface:

     GetContentReader
     GetContentReaderDynamicParameters

The GetContentReader method returns an
System.Management.Automation.Provider.IContentReader interface that defines the methods
used to read the content.

Set-Content

This cmdlet allows the user to update the content of an item. To support this cmdlet, overwrite
the following methods of System.Management.Automation.Provider.IContentCmdletProvider
interface:

     GetContentWriter
     GetContentWriterDynamicParameters

The GetContentWriter method returns an
System.Management.Automation.Provider.IContentWriter interface that defines the methods

<!-- p.1864 -->

used to write the content.

Item property cmdlets
Clear-ItemProperty

This cmdlet allows the user to delete the value of a property. To support this cmdlet, overwrite
the following methods of System.Management.Automation.Provider.IPropertyCmdletProvider
interface:

     ClearProperty
     ClearPropertyDynamicParameters

Copy-ItemProperty

This cmdlet allows the user to copy a property and its value from one location to another. To
support this cmdlet, overwrite the following methods of
System.Management.Automation.Provider.IDynamicPropertyCmdletProvider interface:

     CopyProperty
     CopyPropertyDynamicParameters

Get-ItemProperty

This cmdlet retrieves the properties of an item. To support this cmdlet, overwrite the following
methods of System.Management.Automation.Provider.IPropertyCmdletProvider interface:

     GetProperty
     GetPropertyDynamicParameters

Move-ItemProperty

This cmdlet allows the user to move a property and its value from one location to another. To
support this cmdlet, overwrite the following methods of
System.Management.Automation.Provider.IDynamicPropertyCmdletProvider interface:

     MoveProperty
     MovePropertyDynamicParameters

New-ItemProperty

<!-- p.1865 -->

This cmdlet allows the user to create a new property and set its value. To support this cmdlet,
overwrite the following methods of
System.Management.Automation.Provider.IDynamicPropertyCmdletProvider interface:

     NewProperty
     NewPropertyDynamicParameters

Remove-ItemProperty

This cmdlet allows the user to delete a property and its value. To support this cmdlet, overwrite
the following methods of
System.Management.Automation.Provider.IDynamicPropertyCmdletProvider interface:

     RemoveProperty
     RemovePropertyDynamicParameters

Rename-ItemProperty

This cmdlet allows the user to change the name of a property. To support this cmdlet, overwrite
the following methods of
System.Management.Automation.Provider.IDynamicPropertyCmdletProvider interface:

     RenameProperty
     RenamePropertyDynamicParameters

Set-ItemProperty

This cmdlet allows the user to update the properties of an item. To support this cmdlet,
overwrite the following methods of
System.Management.Automation.Provider.IPropertyCmdletProvider interface:

     SetProperty
     SetPropertyDynamicParameters

Location cmdlets
Get-Location

Retrieves information about the current working location. You do not need to overwrite any
methods to support this cmdlet.

<!-- p.1866 -->

Pop-Location

This cmdlet changes the current location to the location most recently pushed onto the stack.
You do not need to overwrite any methods to support this cmdlet.

Push-Location

This cmdlet adds the current location to the top of a list of locations (a "stack"). You do not
need to overwrite any methods to support this cmdlet.

Set-Location

This cmdlet sets the current working location to a specified location. You do not need to
overwrite any methods to support this cmdlet.

Path cmdlets
Join-Path

This cmdlet allows the user to combine a parent and child path segment to create a provider-
internal path. To support this cmdlet, overwrite the
System.Management.Automation.Provider.NavigationCmdletProvider.MakePath method.

Convert-Path

This cmdlet converts a path from a PowerShell path to a PowerShell provider path.

Split-Path

Returns the specified part of a path.

Resolve-Path

Resolves the wildcard characters in a path, and displays the path contents.

Test-Path

This cmdlet determines whether all elements of a path exist. To support this cmdlet, overwrite
the following methods of System.Management.Automation.Provider.ItemCmdletProvider class:

     ItemExists

<!-- p.1867 -->

     ItemExistsDynamicParameters

PSProvider cmdlets
Get-PSProvider

This cmdlet returns information about the providers available in the session. You do not need
to overwrite any methods to support this cmdlet.

Last updated on 12/19/2025

<!-- p.1868 -->

Provider cmdlet parameters
Provider cmdlets come with a set of static parameters that are available to all providers that
support the cmdlet, as well as dynamic parameters that are added when the user specifies a
certain value for certain static parameters of the provider cmdlet.

Provider Cmdlet Static Parameters
Static parameters are defined by Windows PowerShell. A large set of these parameters is
implemented by Windows PowerShell to provide consistency across all the providers and to
provide a simpler development experience. Examples of these parameters include the
LiteralPath , Exclude , and Include parameters of the Get-Item cmdlet. A smaller set of these

parameters can be overwritten to provide actions that are specific to your provider. Examples
of these parameters include the Path and Value parameter of the Set-Item cmdlet. Here is a
list of the parameters that can be overwritten for the provider cmdlets.

Clear-Content cmdlet You can define how your provider will use the values passed to the Path

parameter of the Clear-Content cmdlet by implementing the
System.Management.Automation.Provider.IContentCmdletProvider.ClearContent* method.

Clear-Item cmdlet You can define how your provider will use the values passed to the Path

parameter of the Clear-Item cmdlet by implementing the
System.Management.Automation.Provider.ItemCmdletProvider.ClearItem* method.

Clear-ItemProperty cmdlet You can define how your provider will use the values passed to the

Path and Name parameters of the Clear-ItemProperty cmdlet by implementing the

System.Management.Automation.Provider.IPropertyCmdletProvider.ClearProperty* method.

Copy-Item cmdlet You can define how your provider will use the values passed to the Path ,

Destination , and Recurse parameters of the Copy-Item cmdlet by implementing the

System.Management.Automation.Provider.ContainerCmdletProvider.CopyItem method.

Get-ChildItems cmdlet You can define how your provider will use the values passed to the Path
and Recurse parameters of the Get-ChildItem cmdlet by implementing the
System.Management.Automation.Provider.ContainerCmdletProvider.GetChildItems* and
System.Management.Automation.Provider.ContainerCmdletProvider.GetChildNames* methods.

<!-- p.1869 -->

Get-Content cmdlet You can define how your provider will use the values passed to the Path

parameter of the Get-Content cmdlet by implementing the
System.Management.Automation.Provider.IContentCmdletProvider.GetContentReader*
method.

Get-Item cmdlet You can define how your provider will use the values passed to the Path

parameter of the Get-Item cmdlet by implementing the
System.Management.Automation.Provider.ItemCmdletProvider.GetItem* method.

Get-ItemProperty cmdlet You can define how your provider will use the values passed to the

Path and Name parameters of the Get-ItemProperty cmdlet by implementing the

System.Management.Automation.Provider.IPropertyCmdletProvider.GetProperty* method.

Invoke-Item cmdlet You can define how your provider will use the values passed to the Path

parameter of the Invoke-Item cmdlet by implementing the
System.Management.Automation.Provider.ItemCmdletProvider.InvokeDefaultAction* method.

Move-Item cmdlet You can define how your provider will use the values passed to the Path and

Destination parameters of the Move-Item cmdlet by implementing the

System.Management.Automation.Provider.NavigationCmdletProvider.MoveItem* method.

New-Item cmdlet You can define how your provider will use the values passed to the Path ,

ItemType , and Value parameters of the New-Item cmdlet by implementing the

System.Management.Automation.Provider.ContainerCmdletProvider.NewItem* method.

New-ItemProperty cmdlet You can define how your provider will use the values passed to the

Path , Name , PropertyType , and Value parameters of the New-ItemProperty cmdlet by

implementing the Microsoft.PowerShell.Commands.RegistryProvider.NewProperty* method.

Remove-Item You can define how your provider will use the values passed to the Path and

Recurse parameters of the Remove-Item cmdlet by implementing the

System.Management.Automation.Provider.ContainerCmdletProvider.RemoveItem* method.

Remove-ItemProperty You can define how your provider will use the values passed to the Path

and Name parameters of the Remove-ItemProperty cmdlet by implementing the
System.Management.Automation.Provider.IDynamicPropertyCmdletProvider.RemoveProperty*
method.

Rename-Item cmdlet You can define how your provider will use the values passed to the Path

and NewName parameters of the Rename-Item cmdlet by implementing the
System.Management.Automation.Provider.ContainerCmdletProvider.RenameItem* method.

<!-- p.1870 -->

Rename-ItemProperty You can define how your provider will use the values passed to the Path ,

NewName , and Name parameters of the Rename-ItemProperty cmdlet by implementing the

System.Management.Automation.Provider.IDynamicPropertyCmdletProvider.RenameProperty*
method.

Set-Content cmdlet You can define how your provider will use the values passed to the Path

parameter of the Set-Content cmdlet by implementing the
System.Management.Automation.Provider.IContentCmdletProvider.GetContentWriter* method.

Set-Item cmdlet You can define how your provider will use the values passed to the Path and

Value parameters of the Set-Item cmdlet by implementing the

System.Management.Automation.Provider.ItemCmdletProvider.SetItem* method.

Set-ItemProperty cmdlet You can define how your provider will use the values passed to the

Path and Value parameters of the Set-Item cmdlet by implementing the

System.Management.Automation.Provider.IPropertyCmdletProvider.SetProperty* method.

Test-Path cmdlet You can define how your provider will use the values passed to the Path

parameter of the Test-Path cmdlet by implementing the
System.Management.Automation.Provider.ItemCmdletProvider.InvokeDefaultAction* method.

In addition, you cannot specify the characteristics of these parameters, such as whether they
are optional or required, nor can you give these parameters an alias or specify any of the
validation attributes. In contrast, you can specify parameter characteristics in stand-alone
cmdlets by using attributes such as the Parameters attribute.

Provider Cmdlet Dynamic Parameters
Dynamic parameters for cmdlet providers are similar to dynamic providers for stand-alone
cmdlets. In both cases, the parameters are added to the cmdlet when the user specifies a
certain value for one of the default parameters, such as the path parameter. However, not all
of the static parameters can be used to trigger the addition of dynamic parameters. For more
information about dynamic parameters, see Provider Cmdlet Dynamic Parameters.

See Also
Provider Cmdlet Dynamic Parameters

Writing a Windows PowerShell Provider

<!-- p.1871 -->

Last updated on 05/20/2025

<!-- p.1872 -->

Provider cmdlet dynamic parameters
Providers can define dynamic parameters that are added to a provider cmdlet when the user
specifies a certain value for one of the static parameters of the cmdlet. For example, a provider
can add different dynamic parameters based on what path the user specifies when they call the
Get-Item or Set-Item provider cmdlets.

Dynamic Parameter Methods
Dynamic parameters are defined by implementing one of the dynamic parameter methods,
such as the
System.Management.Automation.Provider.ItemCmdletProvider.GetItemDynamicParameters*
and
System.Management.Automation.Provider.SetItemDynamicParameters.SetItemDynamicParamet
ers* methods. These methods return an object that has public properties that are decorated
with attributes similar to those of stand-alone cmdlets. Here is an example of an
implementation of the
System.Management.Automation.Provider.ItemCmdletProvider.GetItemDynamicParameters*
method taken from the Certificate provider:

 C#

 protected override object GetItemDynamicParameters(string path)
 {
     return new CertificateProviderDynamicParameters();
 }

Unlike the static parameters of provider cmdlets, you can specify the characteristics of these
parameters in the same way that parameters are defined in stand-alone cmdlets. Here is an
example of a dynamic parameter class taken from the Certificate provider:

 C#

 internal sealed class CertificateProviderDynamicParameters
 {
   /// <summary>
   /// Dynamic parameter the controls whether we only return
   /// code signing certs.
   /// </summary>
   [Parameter()]
   public SwitchParameter CodeSigningCert

<!-- p.1873 -->

     {
         get
         {
           {
                 return codeSigningCert;
             }
         }

         set
         {
           {
                 codeSigningCert = value;
             }
         }
     }

         private SwitchParameter codeSigningCert = new SwitchParameter();
 }

Dynamic Parameters
Here is a list of the static parameters that can be used to add dynamic parameters.

         Clear-Content cmdlet - You can define dynamic parameters that are triggered by the

         Path parameter of the Clear-Clear cmdlet by implementing the

         System.Management.Automation.Provider.IContentCmdletProvider.ClearContentDynamic
         Parameters* method.

         Clear-Item cmdlet - You can define dynamic parameters that are triggered by the Path

         parameter of the Clear-Item cmdlet by implementing the
         System.Management.Automation.Provider.ItemCmdletProvider.ClearItemDynamicParamet
         ers* method.

         Clear-ItemProperty cmdlet - You can define dynamic parameters that are triggered by

         the Path parameter of the Clear-ItemProperty cmdlet by implementing the
         System.Management.Automation.Provider.IPropertyCmdletProvider.ClearPropertyDynami
         cParameters* method.

         Copy-Item cmdlet - You can define dynamic parameters that are triggered by the Path ,

         Destination , and Recurse parameters of the Copy-Item cmdlet by implementing the

         System.Management.Automation.Provider.ContainerCmdletProvider.CopyItemDynamicPa
         rameters* method.

         Get-ChildItem cmdlet - You can define dynamic parameters that are triggered by the

         Path and Recurse parameters of the Get-ChildItem cmdlet by implementing the

<!-- p.1874 -->

System.Management.Automation.Provider.ContainerCmdletProvider.GetChildItemsDynam
icParameters* and
System.Management.Automation.Provider.ContainerCmdletProvider.GetChildNamesDyna
micParameters* methods.

Get-Content cmdlet - You can define dynamic parameters that are triggered by the Path

parameter of the Get-Content cmdlet by implementing the
System.Management.Automation.Provider.IContentCmdletProvider.GetContentReaderDyn
amicParameters* method.

Get-Item cmdlet - You can define dynamic parameters that are triggered by the Path

parameter of the Get-Item cmdlet by implementing the
System.Management.Automation.Provider.ItemCmdletProvider.GetItemDynamicParamete
rs* method.

Get-ItemProperty cmdlet - You can define dynamic parameters that are triggered by the

Path and Name parameters of the Get-ItemProperty cmdlet by implementing the

System.Management.Automation.Provider.IPropertyCmdletProvider.GetPropertyDynamicP
arameters* method.

Invoke-Item cmdlet - You can define dynamic parameters that are triggered by the Path

parameter of the Invoke-Item cmdlet by implementing the
System.Management.Automation.Provider.ItemCmdletProvider.InvokeDefaultActionDyna
micParameters* method.

Move-Item cmdlet - You can define dynamic parameters that are triggered by the Path

and Destination parameters of the Move-Item cmdlet by implementing the
System.Management.Automation.Provider.NavigationCmdletProvider.MoveItemDynamicP
arameters* method.

New-Item cmdlet - You can define dynamic parameters that are triggered by the Path ,

ItemType , and Value parameters of the New-Item cmdlet by implementing the

System.Management.Automation.Provider.ContainerCmdletProvider.NewItemDynamicPar
ameters* method.

New-ItemProperty cmdlet - You can define dynamic parameters that are triggered by the

Path , Name , PropertyType , and Value parameters of the New-ItemProperty cmdlet by

implementing the
System.Management.Automation.Provider.IDynamicPropertyCmdletProvider.NewProperty
DynamicParameters* method.

<!-- p.1875 -->

New-PSDrive cmdlet - You can define dynamic parameters that are triggered by the

System.Management.Automation.PSDriveInfo object returned by the New-PSDrive cmdlet
by implementing the
System.Management.Automation.Provider.DriveCmdletProvider.NewDriveDynamicParame
ters* method.

Remove-Item cmdlet - You can define dynamic parameters that are triggered by the Path

and Recurse parameters of the Remove-Item cmdlet by implementing the
System.Management.Automation.Provider.ContainerCmdletProvider.RemoveItemDynamic
Parameters* method.

Remove-ItemProperty cmdlet - You can define dynamic parameters that are triggered by

the Path and Name parameters of the Remove-ItemProperty cmdlet by implementing the
System.Management.Automation.Provider.IDynamicPropertyCmdletProvider.RemoveProp
ertyDynamicParameters* method.

Rename-Item cmdlet - You can define dynamic parameters that are triggered by the Path

and NewName parameters of the Rename-Item cmdlet by implementing the
System.Management.Automation.Provider.ContainerCmdletProvider.RenameItemDynamic
Parameters* method.

Rename-ItemProperty - You can define dynamic parameters that are triggered by the

Path , Name , and NewName parameters of the Rename-ItemProperty cmdlet by implementing

the
System.Management.Automation.Provider.IDynamicPropertyCmdletProvider.RenameProp
ertyDynamicParameters* method.

Set-Content cmdlet - You can define dynamic parameters that are triggered by the Path

parameter of the Set-Content cmdlet by implementing the
System.Management.Automation.Provider.IContentCmdletProvider.GetContentWriterDyn
amicParameters* method.

Set-Item cmdlet - You can define dynamic parameters that are triggered by the Path and

Value parameters of the Set-Item cmdlet by implementing the

System.Management.Automation.Provider.ItemCmdletProvider.SetItemDynamicParameter
s* method.

Set-ItemProperty cmdlet - You can define dynamic parameters that are triggered by the

Path and Value parameters of the Set-Item cmdlet by implementing the

<!-- p.1876 -->

     System.Management.Automation.Provider.IPropertyCmdletProvider.SetPropertyDynamicP
     arameters* method.

     Test-Path cmdlet - You can define dynamic parameters that are triggered by the Path

     parameter of the Test-Path cmdlet by implementing the
     System.Management.Automation.Provider.ItemCmdletProvider.InvokeDefaultActionDyna
     micParameters* method.

See Also
Writing a Windows PowerShell Provider

Last updated on 08/25/2025

<!-- p.1877 -->

Writing an item provider
This topic describes how to implement the methods of a Windows PowerShell provider that
access and manipulate items in the data store. To be able to access items, a provider must
derive from the System.Management.Automation.Provider.ItemCmdletProvider class.

The provider in the examples in this topic uses an Access database as its data store. There are
several helper methods and classes that are used to interact with the database. For the
complete sample that includes the helper methods, see AccessDBProviderSample03

For more information about Windows PowerShell providers, see Windows PowerShell Provider
Overview.

Implementing item methods
The System.Management.Automation.Provider.ItemCmdletProvider class exposes several
methods that can be used to access and manipulate the items in a data store. For a complete
list of these methods, see ItemCmdletProvider Methods. In this example, we will implement
four of these methods.
System.Management.Automation.Provider.ItemCmdletProvider.GetItem* gets an item at a
specified path. System.Management.Automation.Provider.ItemCmdletProvider.SetItem* sets
the value of the specified item.
System.Management.Automation.Provider.ItemCmdletProvider.ItemExists* checks whether an
item exists at the specified path.
System.Management.Automation.Provider.ItemCmdletProvider.IsValidPath* checks a path to
see if it maps to a location in the data store.

  ７ Note

  This topic builds on the information in Windows PowerShell Provider QuickStart. This
  topic does not cover the basics of how to set up a provider project, or how to implement
  the methods inherited from the
  System.Management.Automation.Provider.DriveCmdletProvider class that create and
  remove drives.

Declaring the provider class

<!-- p.1878 -->

Declare the provider to derive from the
System.Management.Automation.Provider.ItemCmdletProvider class, and decorate it with the
System.Management.Automation.Provider.CmdletProviderAttribute.

 C#

 [CmdletProvider("AccessDB", ProviderCapabilities.None)]

      public class AccessDBProvider : ItemCmdletProvider
      {

    }

Implementing GetItem
The System.Management.Automation.Provider.ItemCmdletProvider.GetItem* is called by the
PowerShell engine when a user calls the Microsoft.PowerShell.Commands.GetItemCommand
cmdlet on your provider. The method returns the item at the specified path. In the Access
database example, the method checks whether the item is the drive itself, a table in the
database, or a row in the database. The method sends the item to the PowerShell engine by
calling the System.Management.Automation.Provider.CmdletProvider.WriteItemObject*
method.

 C#

 protected override void GetItem(string path)
       {
           // check if the path represented is a drive
           if (PathIsDrive(path))
           {
               WriteItemObject(this.PSDriveInfo, path, true);
               return;
           }// if (PathIsDrive...

              // Get table name and row information from the path and do
              // necessary actions
              string tableName;
              int rowNumber;

              PathType type = GetNamesFromPath(path, out tableName, out rowNumber);

              if (type == PathType.Table)
              {
                  DatabaseTableInfo table = GetTable(tableName);
                  WriteItemObject(table, path, true);
              }

<!-- p.1879 -->

              else if (type == PathType.Row)
              {
                   DatabaseRowInfo row = GetRow(tableName, rowNumber);
                   WriteItemObject(row, path, false);
              }
              else
              {
                   ThrowTerminatingInvalidPathException(path);
              }

         }

Implementing SetItem
The System.Management.Automation.Provider.ItemCmdletProvider.SetItem* method is called
by the PowerShell engine calls when a user calls the
Microsoft.PowerShell.Commands.SetItemCommand cmdlet. It sets the value of the item at the
specified path.

In the Access database example, it makes sense to set the value of an item only if that item is a
row, so the method throws NotSupportedException when the item is not a row.

 C#

 protected override void SetItem(string path, object values)
        {
            // Get type, table name and row number from the path specified
            string tableName;
            int rowNumber;

              PathType type = GetNamesFromPath(path, out tableName, out rowNumber);

              if (type != PathType.Row)
              {
                  WriteError(new ErrorRecord(new NotSupportedException(
                        "SetNotSupported"), "",
                     ErrorCategory.InvalidOperation, path));

                  return;
              }

              // Get in-memory representation of table
              OdbcDataAdapter da = GetAdapterForTable(tableName);

              if (da == null)
              {
                  return;
              }
              DataSet ds = GetDataSetForTable(da, tableName);
              DataTable table = GetDataTable(ds, tableName);

<!-- p.1880 -->

              if (rowNumber >= table.Rows.Count)
              {
                  // The specified row number has to be available. If not
                  // NewItem has to be used to add a new row
                  throw new ArgumentException("Row specified is not available");
              } // if (rowNum...

              string[] colValues = (values as string).Split(',');

              // set the specified row
              DataRow row = table.Rows[rowNumber];

              for (int i = 0; i < colValues.Length; i++)
              {
                  row[i] = colValues[i];
              }

              // Update the table
              if (ShouldProcess(path, "SetItem"))
              {
                  da.Update(ds, tableName);
              }

         }

Implementing ItemExists
The System.Management.Automation.Provider.ItemCmdletProvider.ItemExists* method is
called by the PowerShell engine when a user calls the
Microsoft.PowerShell.Commands.TestPathCommand cmdlet. The method determines whether
there is an item at the specified path. If the item does exist, the method passes it back to the
PowerShell engine by calling
System.Management.Automation.Provider.CmdletProvider.WriteItemObject*.

 C#

 protected override bool ItemExists(string path)
        {
            // check if the path represented is a drive
            if (PathIsDrive(path))
            {
                return true;
            }

              // Obtain type, table name and row number from path
              string tableName;
              int rowNumber;

              PathType type = GetNamesFromPath(path, out tableName, out rowNumber);
