---
title: "How to use this documentation — pages 2881-2920"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2881-2920
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2881-2920
family: powershell
documentKind: "doc"
abstract: "See Also Writing a PowerShell Module Supporting Updatable Help Supporting Online Help Naming Help files 09/23/2025 ７ Note Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to write help in Markdown and then convert it to XML-based help. This mak"
---

# How to use this documentation — pages 2881-2920

<!-- p.2881 -->

See Also
  Writing a PowerShell Module
  Supporting Updatable Help
  Supporting Online Help

<!-- p.2882 -->

Naming Help files
09/23/2025

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This topic explains how to name an XML-based help file so that the Get-Help cmdlet can find
it. The name requirements differ for each command type.

Cmdlet Help files
The help file for a C# cmdlet must be named for the assembly in which the cmdlet is defined.
Use the following filename format:

  <AssemblyName>.dll-help.xml

The assembly name format is required even when the assembly is a nested module.

For example, the Get-WinEvent cmdlet is defined in the Microsoft.PowerShell.Diagnostics.dll
assembly. The Get-Help cmdlet looks for a help topic for the Get-WinEvent cmdlet only in the
Microsoft.PowerShell.Diagnostics.dll-help.xml file in the module directory.

Provider Help files
The help file for a PowerShell provider must be named for the assembly in which the provider
is defined. Use the following filename format:

<AssemblyName>.dll-help.xml

The assembly name format is required even when the assembly is a nested module.

For example, the Certificate provider is defined in the Microsoft.PowerShell.Security.dll
assembly. The Get-Help cmdlet looks for a help topic for the Certificate provider only in the
Microsoft.PowerShell.Security.dll-help.xml file in the module directory.

<!-- p.2883 -->

Function Help files
Functions can be documented using comment-based help or documented in an XML help file.
When the function is documented in an XML file, the function must have an .EXTERNALHELP
comment keyword that associates the function with the XML file. Otherwise, the Get-Help
cmdlet can't find the help file.

There are no technical requirements for the name of a function help file. However, a best
practice is to name the help file for the script module in which the function is defined. For
example, the following function is defined in the MyModule.psm1 file.

  PowerShell

  #.EXTERNALHELP MyModule.psm1-help.xml
  function Test-Function { ... }

Beginning in PowerShell 5.0, functions that are exported by a module can be documented in a
help file that is named for the module. You don't need to use .EXTERNALHELP comment
keyword. For example, if the Test-Function function is exported by the MyModule module, you
can name the help file MyModule-help.xml . The Get-Help cmdlet looks for help for the Test-
Function function in the MyModule-help.xml file in the module directory.

CIM Command Help files
The help file for a CIM command must be named for the CDXML file in which the CIM
command is defined. Use the following filename format:

<FileName>.cdxml-help.xml

CIM commands are defined in CDXML files that can be included in modules as nested modules.
When the CIM command is imported into the session as a function, PowerShell adds an
.EXTERNALHELP comment keyword to the function definition that associates the function with

an XML help file that is named for the CDXML file in which the CIM command is defined.

Script Workflow Help files
Script workflows that are included in modules can be documented in XML-based help files.
There are no technical requirements for the name of the help file. However, a best practice is to
name the help file for the script module in which the script workflow is defined. For example:

<ScriptModule>.psm1-help.xml

<!-- p.2884 -->

Unlike other scripted commands, script workflows don't require an .EXTERNALHELP comment
keyword to associate them with a help file. Instead, PowerShell searches the UI-Culture-specific
subdirectories of the module directory for XML-based help files and looks for help for the
script workflow in all the files. .EXTERNALHELP comment keyword are ignored.

Because the .EXTERNALHELP comment keyword is ignored, the Get-Help cmdlet can find help
for script workflows only when they're included in modules.

<!-- p.2885 -->

Supporting Updatable Help
The Windows PowerShell Updatable Help System, introduced in Windows PowerShell 3.0, is
designed to ensure that users always have the newest help topics at the command prompt on
their local computer. Along with Windows PowerShell online help, Updatable Help provides a
complete help solution for users. This section describes the Updatable Help System and
explains how module authors can support Updatable Help for their modules.

This section includes the following topics.

      Updatable Help Overview
      Updatable Help Authoring: Step-by-Step
      How Updatable Help Works
      How to Create a HelpInfo XML File
      How to Prepare Updatable Help CAB Files
      How to Update Help Files
      How to Test Updatable Help

See Also
      Supporting Online Help
      Updatable Help Status Table

 Last updated on 05/20/2025

<!-- p.2886 -->

Updatable Help Overview
This document provides a basic introduction to the design and operation of the PowerShell
Updatable Help feature. It's designed for module authors and others who deliver Windows
PowerShell help topics to users.

Introduction
PowerShell help topics are an integral part of the PowerShell experience. Like PowerShell
modules, help topics are continually updated and improved by the authors and by the
contributions of the community of PowerShell users.

The Updatable Help feature, introduced in Windows PowerShell 3.0, ensures that users have the
newest versions of help topics at the command prompt, even for built-in PowerShell
commands, without downloading new modules or running Windows Update. Updatable Help
makes updating simple by providing cmdlets that download the newest versions of help topics
from the internet and install them in the correct subdirectories on the user's local computer.
Even users who are behind firewalls can use the new cmdlets to get updated help from an
internal file share.

Updatable Help is fully supported by all Windows PowerShell modules in Windows 8 and
Windows Server 2012, and its features are available to all Windows PowerShell module authors.
Updatable Help supports only XML-based help files. It doesn't support comment-based help.

Updatable Help includes the following features.

      The Update-Help cmdlet, which determines whether users have the newest help files for a
      module and, if not, downloads the newest help files from the internet, unpacks them, and
      installs them in the correct module subdirectories on the user's computer. Users can use
      the Get-Help cmdlet to view the newly-installed help topics immediately. They don't need
      to restart PowerShell.

      The Save-Help cmdlet, which downloads the newest help files from the internet and saves
      them in a file system directory. Users can use the Update-Help cmdlet to get help files
      from the file system directory, and unpack and install them in the module subdirectories
      on the user's computer. The Save-Help cmdlet is designed for users who have limited or
      no internet access and for enterprises who prefer to limit internet access.

<!-- p.2887 -->

     Help for a Module. Help files for a module are managed and delivered as a unit, so users
     can get all of the help files for the modules they use. Updatable help is supported only for
     modules, not for Windows PowerShell snap-ins.

     Version support. Updatable Help uses standard four-position (N1.N2.N3.N4) version
     numbers. Updatable Help downloads help files when the version number of the help files
     on the user's computer (or in the Save-Help directory) is lower than the version number
     of the help files at the internet location.

     Multi-language support. Updatable Help supports module help files in multiple UI
     cultures. Updatable Help filenames include standard language codes, such as "en-US" and
     "ja-JP", and the Update-Help and Save-Help cmdlets place the help files into language-
     specific subdirectories of the module directory.

     Auto-generated help. The Get-Help cmdlet displays basic help for commands that don't
     have help files. The auto-generated help includes the command syntax and aliases, and
     instructions for using online help and Updatable Help.

     Enhanced Online help. Easy access to online help no longer requires help files. The
     Online parameter of the Get-Help cmdlet now gets the URL of an online help topic from
     the value of the HelpUri property of any command, if it can't find the online help URL in a
     help file. You can populate the HelpUri property by adding a HelpUri attribute to the
     code of cmdlets, functions, and CIM commands, or using the .LINK comment-based help
     keyword in workflows and scripts.

     To make our help files updatable, the Windows PowerShell modules in Windows don't
     come with help files. Users can use Updatable Help to install help files and update them.
     Authors of other modules can include help files in modules or omit them. Support for
     Updatable Help is optional, but recommended.

Last updated on 05/20/2025

<!-- p.2888 -->

Updatable Help Authoring: Step-by-Step
This article documents the steps required to publish Updatable Help.

Authoring Updatable Help: Step-by-Step
Updatable Help is designed for end-users, but it also provides significant benefits to module
authors and help writers, including the ability to add content, fix errors, deliver in multiple UI
cultures, and respond to user comments and requests, long after the module has shipped. This
topic explains how you package and upload help files so that users can download and install
them using the Update-Help and Save-Help cmdlets.

The following steps provide an overview of the process of supporting Updatable Help.

Step 1: Find an internet site for your help files
The first step in creating updatable help is to find an internet location for your module's help
files. Actually, you can use two different locations. You can keep your module's help
information file (HelpInfo XML - described below) at one internet location and the help content
files (CAB and ZIP) at another internet location. All help content files for a module must be in
the same location. You can place help content files for different modules in the same location.

Step 2: Add a HelpInfoURI key to your module manifest
Add a HelpInfoURI key to your module manifest. The value of the key is the Uniform Resource
Identifier (URI) of the location of the HelpInfo XML information file for your module. For
security, the address must begin with http: or https: . The URI should specify an internet
location for the HelpInfo XML file. Don't include the HelpInfo XML filename.

For example:

 PowerShell

 @{
      RootModule = TestModule.psm1
      ModuleVersion = '2.0'
      HelpInfoURI = 'https://go.microsoft.com/fwlink/?LinkID=0123'
 }

<!-- p.2889 -->

   ７ Note

   The HelpInfoURI must end with a forward slash ( / ) character or redirect to a location that
   ends with a forward slash ( / ).

Step 3: Create a HelpInfo XML file
The HelpInfo XML information file contains the URI of the internet location of your help files
and the version numbers of the newest help files for your module in each supported UI culture.
Every PowerShell module has one HelpInfo XML file. When you update your help files, you
must update the HelpInfo XML file. For more information, see How to Create a HelpInfo XML
File.

Step 4: Create CAB and ZIP files
PowerShell on Windows expects the help content files a module to be stored in a CAB file.
PowerShell on Linux or macOS expects the help content files a module to be stored in a ZIP
file. If your module runs across multiple platforms you must create both formats.

Use a tool, such as MakeCab.exe , to create a CAB file that contains the help files for your
module. Create a separate CAB file for the help files in each supported UI culture. For more
information, see How to Prepare Updatable Help CAB Files.

You can use the Compress-Archive cmdlet to create a ZIP file.

Step 5: Upload your files
To publish new or updated help files, upload the help content files to the internet location
specified by the HelpContentUri element in the HelpInfo XML file. Then, upload the HelpInfo
XML file to the internet location specified by the value of the HelpInfoUri key in the module
manifest.

Using PlatyPS to create help content
PlatyPS is a PowerShell module designed to help you create Help content for your modules.
You author the help content in Markdown files. PlatyPS can create Markdown templates for
your cmdlet, convert the Markdown files to the XML help format (MAML), create HelpInfo XML
files, and package the MAML help content into CAB and ZIP files.

<!-- p.2890 -->

For more information, see Create XML-based help using PlatyPS.

Last updated on 05/20/2025

<!-- p.2891 -->

How Updatable Help Works
This topic explains how Updatable Help processes the HelpInfo XML file and CAB files for each
module, and installs updated help for users.

The Update-Help Process
The following list describes the actions of the Update-Help cmdlet when a user runs a
command to update the help files for a module in a particular UI culture.

   1. Update-Help gets the remote HelpInfo XML file from the location specified by the value of
     the HelpInfoURI key in the module manifest and validates the file against the schema. (To
     view the schema, see HelpInfo XML Schema.) Then Update-Help looks for a local HelpInfo
     XML file for the module in the module directory on the user's computer.

   2. Update-Help compares the version number of the help files for the specified UI culture in
     the remote and local HelpInfo XML files for the module. If the version number on the
     remote file is greater than version number on the local file, or if there is no local HelpInfo
     XML file for the module, Update-Help prepares to download new help files.

   3. Update-Help selects the CAB file for the module from the location specified by the
     HelpContentUri element in the remote HelpInfo XML file. It uses the module name,
     module GUID, and UI culture to identify the CAB file.

   4. Update-Help downloads the CAB file, unpacks it, validates the help content files, and
     saves the help content files in the language-specific subdirectory of the module directory
     on the user's computer.

   5. Update-Help creates a local HelpInfo XML file by copying the remote HelpInfo XML file. It
     edits the local HelpInfo XML file so that it includes elements only for the CAB file that it
     installed. Then it saves the local HelpInfo XML file in the module directory and concludes
     the update.

The Save-Help Process
The following list describes the actions of the Save-Help and Update-Help cmdlets when a user
runs commands to update the help files in a file share, and then use those files to update the
help files on the user's computer.

<!-- p.2892 -->

The Save-Help cmdlet performs the following actions in response to a command to save the
help files for a module in a file share that's specified by the DestinationPath parameter.

   1. Save-Help gets the remote HelpInfo XML file from the location specified by the value of
     the HelpInfoURI key in the module manifest and validates the file against the schema. (To
     view the schema, see HelpInfo XML Schema.) Then Save-Help looks for a local HelpInfo
     XML file in the directory that's specified by the DestinationPath parameter in the Save-
     Help command.

   2. Save-Help compares the version number of the help files for the specified UI culture in
     the remote and local HelpInfo XML files for the module. If the version number on the
     remote file is greater than version number on the local file, or if there is no local HelpInfo
     XML file for the module in the DestinationPath directory, Save-Help prepares to
     download new help files.

   3. Save-Help selects the CAB file for the module from the location specified by the
     HelpContentUri element in the remote HelpInfo XML file. It uses the module name,
     module GUID, and UI culture to identify the CAB file.

   4. Save-Help downloads the CAB file and saves it in the DestinationPath directory. (It does
     not create any language-specific subdirectories.)

   5. Save-Help creates a local HelpInfo XML file by copying the remote HelpInfo XML file. It
     edits the local HelpInfo XML file so that it includes elements only for the CAB file that it
     saved. Then it saves the local HelpInfo XML file in the DestinationPath directory and
     concludes the update.

     The Update-Help cmdlet performs the following actions in response to a command to
     update the help files on a user's computer from the files in a file share that's specified by
     the SourcePath parameter.

   6. Update-Help gets the remote HelpInfo XML file from the SourcePath directory. Then it
     looks for a local HelpInfo XML file in the module directory on the user's computer.

   7. Update-Help compares the version number of the help files for the specified UI culture in
     the remote and local HelpInfo XML files for the module. If the version number on the
     remote file is greater than version number on the local file, or if there is no local HelpInfo
     XML file, Update-Help prepares to install new help files.

   8. Update-Help selects the CAB file for the module from SourcePath directory. It uses the
     module name, module GUID, and UI culture to identify the CAB file.

<!-- p.2893 -->

  9. Update-Help unpacks the CAB file, validates the help content files, and saves the help
     content files in the language-specific subdirectory of the module directory on the user's
     computer.

 10. Update-Help creates a local HelpInfo XML file by copying the remote HelpInfo XML file. It
     edits the local HelpInfo XML file so that it includes elements only for the CAB file that it
     installed. Then it saves the local HelpInfo XML file in the module directory and concludes
     the update.

Last updated on 02/19/2026

<!-- p.2894 -->

How to create a HelpInfo XML file

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This topics in this section explains how to create and populate a help information file,
commonly known as a "HelpInfo XML file," for the PowerShell Updatable Help feature.

HelpInfo XML file overview
The HelpInfo XML file is the primary source of information about Updatable Help for the
module. It includes the location of the help files for the modules, the supported UI cultures,
and the version numbers that Updatable Help uses to determine whether the user has the
newest help files.

Each module has just one HelpInfo XML file, even if the module includes multiple help files for
multiple UI cultures. The module author creates the HelpInfo XML file and places it in the
internet location that's specified by the HelpInfoUri key in the module manifest. When the
module help files are updated and uploaded, the module author updates the HelpInfo XML file
and replaces the original HelpInfo XML file with the new version.

It's critical that the HelpInfo XML file is carefully maintained. If you upload new files, but forget
to increment the version numbers, Updatable Help will not download the new files to users'
computers. if you add help files for a new UI culture, but don't update the HelpInfo XML file or
place it in the correct location, Updatable Help will not download the new files.

In this section
This section includes the following topics.

     HelpInfo XML Schema
     HelpInfo XML Sample File
     How to Name a HelpInfo XML File

<!-- p.2895 -->

     How to Set HelpInfo XML Version Numbers

See also
Supporting Updatable Help

Last updated on 05/20/2025

<!-- p.2896 -->

HelpInfo XML Schema
This topic contains the XML schema for Updatable Help Information files, commonly known as
"HelpInfo XML files."

HelpInfo XML Schema
HelpInfo XML files are based on the following XML schema.

 XML

 <?xml version="1.0" encoding="utf-8"?>
 <schema elementFormDefault="qualified"
 targetNamespace="http://schemas.microsoft.com/powershell/help/2010/05"
 xmlns="http://www.w3.org/2001/XMLSchema">
   <element name="HelpInfo">
     <complexType>
       <sequence>
         <element name="HelpContentURI" type="anyURI" minOccurs="1" maxOccurs="1" />
         <element name="SupportedUICultures" minOccurs="1" maxOccurs="1">
           <complexType>
             <sequence>
               <element name="UICulture" minOccurs="1" maxOccurs="unbounded">
                 <complexType>
                   <sequence>
                     <element name="UICultureName" type="language" minOccurs="1"
 maxOccurs="1" />
                     <element name="UICultureVersion" type="string" minOccurs="1"
 maxOccurs="1" />
                   </sequence>
                 </complexType>
               </element>
             </sequence>
           </complexType>
         </element>
       </sequence>
     </complexType>
   </element>
 </schema>

HelpInfo XML Elements
The HelpInfo XML file includes the following elements.

<!-- p.2897 -->

     HelpContentURI - Contains the URI of the location of the help CAB files for the module.
     The URI must begin with "http" or "https". The URI should specify an internet location, but
     must not include the CAB filename. The HelpContentURI value can be the same or
     different from the HelpInfoURI value.

     SupportedUICultures - Represents the module help files in all UI cultures. Contains
     UICulture elements, each of which represents a set of help files for the module in a
     specified UI culture.

     UICulture - Represents a set of help files for the module in a specified UI culture. Add a
     UICulture element for each UI culture in which the help files are written.

     UICultureName - Contains the language code for the UI culture in which the help files are
     written.

     UICultureVersion - Contains a 4-part version number in "N1.N2.N3.N4" format that
     represents the version of the help CAB file in the UI culture. Increment this version
     number whenever you upload new help CAB files in the UI culture that's specified by
     UICultureName. For more information about this value, see Version Class.

 ７ Note

 Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
 write help in Markdown and then convert it to XML-based help. This makes it much easier
 to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
 For more information, see Create XML-based help using PlatyPS.

Last updated on 05/20/2025

<!-- p.2898 -->

HelpInfo XML Sample File
This topic displays a sample of a well-formed Updatable Help Information file, commonly
known as "HelpInfo XML file." In this sample file, the UI culture elements are arranged in
alphabetical order by UI culture name. Alphabetical ordering is a best practice, but it's not
required.

HelpInfo XML Sample File
  XML

  <?xml version="1.0" encoding="utf-8"?>
  <HelpInfo xmlns="http://schemas.microsoft.com/powershell/help/2010/05">
     <HelpContentURI>https://go.microsoft.com/fwlink/?LinkID=141553</HelpContentURI>
     <SupportedUICultures>
      <UICulture>
        <UICultureName>de-DE</UICultureName>
        <UICultureVersion>2.15.0.10</UICultureVersion>
      </UICulture>
      <UICulture>
        <UICultureName>en-US</UICultureName>
        <UICultureVersion>3.2.0.7</UICultureVersion>
      </UICulture>
      <UICulture>
        <UICultureName>it-IT</UICultureName>
        <UICultureVersion>1.1.0.5</UICultureVersion>
      </UICulture>
      <UICulture>
        <UICultureName>ja-JP</UICultureName>
        <UICultureVersion>3.2.0.4</UICultureVersion>
      </UICulture>
     </SupportedUICultures>
  </HelpInfo>

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

 Last updated on 05/20/2025

<!-- p.2899 -->

How to name a HelpInfo XML file

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This topic explains the required name format for the Updatable Help Information files,
commonly known as HelpInfo XML files. A HelpInfo XML file must have a name with the
following format.

<ModuleName>_<ModuleGUID>_HelpInfo.xml

The elements of the name are as follows.

     <ModuleName> - The value of the Name property of the ModuleInfo object that the Get-

     Module cmdlet returns.

     <ModuleGUID> - The value of the GUID key in the module manifest.

For example, if the module name is "TestModule" and the module GUID is 9cabb9ad-f2ac-
4914-a46b-bfc1bebf07f9, the name of the HelpInfo XML file for the module would be:

TestModule_9cabb9ad-f2ac-4914-a46b-bfc1bebf07f9_HelpInfo.xml

Last updated on 05/20/2025

<!-- p.2900 -->

How to set HelpInfo XML version numbers

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

The version numbers in a HelpInfo XML file are critical to the operation of Updatable Help. The
Update-Help and Save-Help cmdlets download new help files only when the version number
for a UI culture in the remote HelpInfo XML file is greater than the version number for that UI
culture in the local HelpInfo XML, or there is no local HelpInfo XML file.

The HelpInfo XML file uses the 4-part version number that's defined in the System.Version
class of the Microsoft .NET Framework. The format is N1.N2.N3.N4 . Module authors can use any
version numbering scheme that's permitted by the System.Version class. Updatable Help
requires only that the version number for a UI culture increase when a new version of the CAB
file for that UI culture is uploaded to the location that's specified by the HelpContentURI
element in the HelpInfo XML file.

The following example shows the elements of the HelpInfo XML file for the German (de-DE) UI
culture when the version is 2.15.0.10.

 XML

 <UICulture>
   <UICultureName>de-DE</UICultureName>
   <UICultureVersion>2.15.0.10</UICultureVersion>
 </UICulture>

The version number for a UI culture reflects the version of the CAB file for that UI culture. The
version number applies to the entire CAB file. You can't set different version numbers for
different files in the CAB file. The version number for each UI culture is evaluated
independently and need not be related to the version numbers for other UI cultures that the
module supports.

<!-- p.2901 -->

Last updated on 05/20/2025

<!-- p.2902 -->

How to prepare Updatable Help CAB files

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This topic explains the contents and use of cabinet files in Windows PowerShell Updatable
Help.

This section includes the following topics.

        How to Create and Upload CAB Files
        How to Name an Updatable Help CAB File
        File Types Permitted in an Updatable Help CAB File

See also
Supporting Updatable Help

 Last updated on 05/20/2025

<!-- p.2903 -->

How to create and upload CAB files

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This topic explains how to create Updatable Help CAB files and upload them to the location
where the Updatable Help cmdlets can find them.

How to create and upload updatable help CAB files
You can use the Updatable Help feature to deliver new or updated help files for a module in
multiple languages and cultures. An Updatable Help package for a module consists of one
HelpInfo XML file and one or more cabinet ( .CAB ) files. Each CAB file contains help files for the
module in one UI culture. Use the following procedure to create CAB files for Updatable Help.

   1. Organize the help files for the module by UI culture. Each Updatable Help CAB file
     contains the help files for one module in one UI culture. You can deliver multiple help CAB
     files for the module, each for a different UI culture.

   2. Verify that help files include only the file types permitted for Updatable Help and validate
     them against a help file schema. If the Update-Help cmdlet encounters a file that's invalid
     or is not a permitted type, it doesn't install the invalid file and stops installing files from
     the CAB. For a list of permitted file types, see File Types Permitted in an Updatable Help
     CAB File.

   3. Include all the help files for the module in the UI culture, not only files that are new or
     have changed. If the CAB file is incomplete, users who download help files for the first
     time or do not download every update, won't have all the help files.

   4. Use a utility that creates cabinet files, such as MakeCab.exe . PowerShell doesn't include
     cmdlets that create CAB files.

   5. Name the CAB files. For more information, see How to Name an Updatable Help CAB File.

<!-- p.2904 -->

  6. Upload the CAB files for the module to the location that's specified by the
     HelpContentUri element in the HelpInfo XML file for the module. Then upload the
     HelpInfo XML file to the location that's specified by the HelpInfoUri key of the module
     manifest. The HelpContentUri and HelpInfoUri can point to the same location.

 Ｕ Caution

 The value of the HelpInfoUri key and the HelpContentUri element must begin with http
 or https . The value must a URL path pointing to the location (folder) containing the
 updateable help. The URL must end with / . The URL must not include a filename.

Last updated on 05/20/2025

<!-- p.2905 -->

How to name an Updatable Help CAB file

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

An updatable cabinet ( .CAB ) file must have a name with the following format.

<ModuleName>_<ModuleGUID>_<UICulture>_HelpContent.cab

The elements of the name are as follows.

      <ModuleName> -The value of the Name property of the ModuleInfo object that the Get-

      Module cmdlet returns.
      <ModuleGUID> - The value of the GUID key in the module manifest.

      <UICulture> - The UI culture of the help files in the CAB file. This value must match the

      value of one of the UICulture elements in the HelpInfo XML file for the module.

For example, if the module name is "TestModule," the module GUID is 9cabb9ad-f2ac-4914-
a46b-bfc1bebf07f9, and the UI culture is en-US , the name of the CAB file would be:

TestModule_9cabb9ad-f2ac-4914-a46b-bfc1bebf07f9_en-US_HelpContent.cab

 Last updated on 05/20/2025

<!-- p.2906 -->

File Types Permitted in an Updatable Help
CAB File
Uncompressed CAB file content is limited to 1 GB by default. To bypass this limit, users have to
use the Force parameter of the Update-Help and Save-Help cmdlets.

To assure the security of help files that are downloaded from the internet, an Updatable Help
CAB file can include only the file types listed below. The Update-Help cmdlet validates all files
against the help topic schemas. If the Update-Help cmdlet encounters a file that's invalid or is
not a permitted type, it doesn't install the invalid file and stops installing files from the CAB on
the user's computer.

      XML-based help topics for cmdlets.
      XML-based help topics for scripts and functions.
      XML-based help topics for PowerShell providers.
      Text-based help topics, such as About topics.

The Update-Help verifies the CAB contents when it unpacks the CAB. If Update-Help finds non-
compliant file types in an Updatable Help CAB file, it generates a terminating error and stops
the operation. It doesn't install any help files from the CAB, even those of compliant file types.

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

 Last updated on 05/20/2025

<!-- p.2907 -->

How to update help files

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

There are many reasons to update help files, such as correcting errors, clarifying a concept,
answering a frequently asked question, adding new files, or adding new and better examples.

To update a help file:

   1. Change the files.
   2. Translate the files into other UI cultures.
   3. Collect all help files (new, changed, and unchanged) for the module in each UI culture.
   4. Validate the files against the XML schema.
   5. Rebuild the CAB files for each UI culture.
   6. In the HelpInfo XML file, increment the version numbers of the CAB file for each UI
      culture.
   7. Upload the new CAB files to the location that's specified by the value of the
      HelpContentUri element in the HelpInfo XML file. Replace the older CAB files with the
      new CAB files.
   8. Upload the updated HelpInfo XML file to the location that's specified by the HelpInfoUri
      key in the module manifest. Replace the older HelpInfo XML file with the new file.

 Last updated on 05/20/2025

<!-- p.2908 -->

How to test Updatable Help

   ７ Note

   Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
   write help in Markdown and then convert it to XML-based help. This makes it much easier
   to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
   For more information, see Create XML-based help using PlatyPS.

This topic describes approaches to testing Updatable Help for a module.

Using verbose to detect errors
After uploading the HelpInfo XML file and CAB files for your module, test the files by running
an Update-Help command with the Verbose parameter. The Verbose parameter directs
Update-Help to report the critical steps in its actions, from reading the HelpInfoUri key in the

module manifest to validating the file types in the unpacked CAB file and placing the files in
the language-specific module directory.

When all verbose messages are resolved, run an Update-Help command with the Debug
parameter. This parameter should detect any remaining problems with the Updatable Help
files.

 Last updated on 05/20/2025

<!-- p.2909 -->

Supporting Online Help

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

Beginning in PowerShell 3.0, there are two ways to support the Get-Help Online feature for
PowerShell commands. This topic explains how to implement this feature for different
command types.

About Online Help
Online help has always been a vital part of PowerShell. Although the Get-Help cmdlet displays
help topics at the command prompt, many users prefer the experience of reading online,
including color-coding, hyperlinks, and sharing ideas in Community Content and wiki-based
documents. Most importantly, before the advent of Updatable Help, online help provided the
most up-to-date version of the help files.

With the advent of Updatable Help in PowerShell 3.0, online help still plays a vital role. In
addition to the flexible user experience, online help provides help to users who don't or can't
use Updatable Help to download help topics.

How Get-Help -Online Works
To help users find the online help topics for commands, the Get-Help command has an Online
parameter that opens the online version of help topic for a command in the user's default
internet browser.

For example, the following command opens the online help topic for the Invoke-Command
cmdlet.

 PowerShell

 Get-Help Invoke-Command -Online

<!-- p.2910 -->

To implement Get-Help -Online , the Get-Help cmdlet looks for a Uniform Resource Identifier
(URI) for the online version help topic in the following locations.

     The first link in the Related Links section of the help topic for the command. The help
     topic must be installed on the user's computer. This feature was introduced in PowerShell
     2.0.

     The HelpUri property of any command. The HelpUri property is accessible even when the
     help topic for the command isn't installed on the user's computer. This feature was
     introduced in PowerShell 3.0.

      Get-Help looks for a URI in the first entry in the Related Links section before getting the

     HelpUri property value. If the property value is incorrect or has changed, you can override
     it by entering a different value in the first related link. However, the first related link works
     only when the help topics are installed on the user's computer.

Adding a URI to the first related link of a command
help topic
You can support Get-Help -Online for any command by adding a valid URI to the first entry in
the Related Links section of the XML-based help topic for the command. This option is valid
only in XML-based help topics and works only when the help topic is installed on the user's
computer. When the help topic is installed and the URI is populated, this value takes
precedence over the HelpUri property of the command.

To support this feature, the URI must appear in the maml:uri element under the first
maml:relatedLinks/maml:navigationLink element in the maml:relatedLinks element.

The following XML shows the correct placement of the URI. The Online version: text in the
maml:linkText element is a best practice, but it's not required.

 XML

 <maml:relatedLinks>
     <maml:navigationLink>
         <maml:linkText>Online version:</maml:linkText>
         <maml:uri>https://go.microsoft.com/fwlink/?LinkID=113279</maml:uri>
     </maml:navigationLink>
     <maml:navigationLink>
         <maml:linkText>about_History</maml:linkText>
         <maml:uri/>

<!-- p.2911 -->

     </maml:navigationLink>
 </maml:relatedLinks>

Adding the HelpUri property to a command
This section shows how to add the HelpUri property to commands of different types.

Adding a HelpUri Property to a Cmdlet
For cmdlets written in C#, add a HelpUri attribute to the Cmdlet class. The value of the
attribute must be a URI that begins with http or https .

The following code shows the HelpUri attribute of the Get-History cmdlet class.

 C#

 [Cmdlet(VerbsCommon.Get, "History", HelpUri = "https://go.microsoft.com/fwlink/?
 LinkID=001122")]

Adding a HelpUri property to an advanced function
For advanced functions, add a HelpUri property to the CmdletBinding attribute. The value of
the property must be a URI that begins with "http" or "https".

The following code shows the HelpUri attribute of the New-Calendar function

 PowerShell

 function New-Calendar {
     [CmdletBinding(SupportsShouldProcess=$true,
     HelpUri="https://go.microsoft.com/fwlink/?LinkID=01122")]

Adding a HelpUri attribute to a cim command
For CIM commands, add a HelpUri attribute to the CmdletMetadata element in the CDXML
file. The value of the attribute must be a URI that begins with http or https .

The following code shows the HelpUri attribute of the Start-Debug CIM command

 XML

 <CmdletMetadata Verb="Debug" HelpUri="https://go.microsoft.com/fwlink/?
 LinkID=001122"/>

<!-- p.2912 -->

Adding a HelpUri attribute to a workflow
For workflows that are written in the PowerShell language, add an .EXTERNALHELP comment
keyword to the workflow code. The value of the keyword must be a URI that begins with http
or https .

  ７ Note

  The HelpUri property isn't supported for XAML-based workflows in PowerShell.

The following code shows the .EXTERNALHELP keyword in a workflow file.

  PowerShell

  # .EXTERNALHELP "https://go.microsoft.com/fwlink/?LinkID=138338"

 Last updated on 05/20/2025

<!-- p.2913 -->

How to add dynamic parameters to a
provider help topic

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This section explains how to populate the DYNAMIC PARAMETERS section of a provider help
topic.

Dynamic parameters are parameters of a cmdlet or function that are available only under
specified conditions.

The dynamic parameters that are documented in a provider help topic are the dynamic
parameters that the provider adds to the cmdlet or function when the cmdlet or function is
used in the provider drive.

Dynamic parameters can also be documented in custom cmdlet help for a provider. When
writing both provider help and custom cmdlet help for a provider, include the dynamic
parameter documentation in both documents.

If a provider doesn't implement any dynamic parameters, the provider help topic contains an
empty DynamicParameters element.

To add dynamic parameters
   1. In the <AssemblyName>.dll-help.xml file, within the providerHelp element, add a
         DynamicParameters element. The DynamicParameters element should appear after the

         Tasks element and before the RelatedLinks element.

     For example:

          XML

<!-- p.2914 -->

    <providerHelp>
        <Tasks>
        </Tasks>
        <DynamicParameters>
        </DynamicParameters>
        <RelatedLinks>
        </RelatedLinks>
    </providerHelp>

  If the provider doesn't implement any dynamic parameters, the DynamicParameters
  element can be empty.

2. Within the DynamicParameters element, for each dynamic parameter, add a
  DynamicParameter element.

  For example:

    XML

    <DynamicParameters/>
        <DynamicParameter>
        </DynamicParameter>
    </DynamicParameters>

3. In each DynamicParameter element, add a Name and CmdletSupported element.

       Name - Specifies the parameter name
       CmdletSupported - Specifies the cmdlets in which the parameter is valid. Type a
       comma-separated list of cmdlet names.

  For example, the following XML documents the Encoding dynamic parameter that the
  Windows PowerShell FileSystem provider adds to the Add-Content , Get-Content , Set-
  Content cmdlets.

    XML

    <DynamicParameters/>
        <DynamicParameter>
            <Name> Encoding </Name>
            <CmdletSupported> Add-Content, Get-Content, Set-Content
    </CmdletSupported>
    </DynamicParameters>

<!-- p.2915 -->

4. In each DynamicParameter element, add a Type element. The Type element is a container
  for the Name element which contains the .NET type of the value of the dynamic
  parameter.

  For example, the following XML shows that the .NET type of the Encoding dynamic
  parameter is the FileSystemCmdletProviderEncoding enumeration.

    XML

    <DynamicParameters/>
        <DynamicParameter>
            <Name> Encoding </Name>
            <CmdletSupported> Add-Content, Get-Content, Set-Content
    </CmdletSupported>
            <Type>
                <Name>
    Microsoft.PowerShell.Commands.FileSystemCmdletProviderEncoding </Name>
            <Type>
    ...
    </DynamicParameters>

5. Add the Description element, which contains a brief description of the dynamic
  parameter. When composing the description, use the guidelines prescribed for all cmdlet
  parameters in How to Add Parameter Information.

  For example, the following XML includes the description of the Encoding dynamic
  parameter.

    XML

    <DynamicParameters/>
        <DynamicParameter>
            <Name> Encoding </Name>
            <CmdletSupported> Add-Content, Get-Content, Set-Content
    </CmdletSupported>
            <Type>
                <Name>
    Microsoft.PowerShell.Commands.FileSystemCmdletProviderEncoding </Name>
            <Type>
            <Description> Specifies the encoding of the output file that contains
    the content. </Description>
    ...
    </DynamicParameters>

6. Add the PossibleValues element and its child elements. Together, these elements
  describe the values of the dynamic parameter. This element is designed for enumerated

<!-- p.2916 -->

     values. If the dynamic parameter doesn't take a value, such as is the case with a [switch]
     parameter, or the values can't be enumerated, add an empty PossibleValues element.

     The following table lists and describes the PossibleValues element and its child elements.

          PossibleValues - This element is a container. Its child elements are described below.
          Add one PossibleValues element to each provider help topic. The element can be
          empty.
          PossibleValue - This element is a container. Its child elements are described below.
          Add one PossibleValue element for each value of the dynamic parameter.
          Value - Specifies the value name.
          Description - This element contains a Para element. The text in the Para element
          describes the value that's named in the Value element.

     For example, the following XML shows one PossibleValue element of the Encoding
     dynamic parameter.

       XML

       <DynamicParameters/>
           <DynamicParameter>
       ...
               <Description> Specifies the encoding of the output file that contains
       the content. </Description>
               <PossibleValues>
                   <PossibleValue>
                       <Value> ASCII </Value>
                       <Description>
                           <para> Uses the encoding for the ASCII (7-bit) character
       set. </para>
                       </Description>
                   </PossibleValue>
       ...
               </PossibleValues>
       </DynamicParameters>

Example
The following example shows the DynamicParameters element of the Encoding dynamic
parameter.

 XML

 <DynamicParameters/>
     <DynamicParameter>

<!-- p.2917 -->

           <Name> Encoding </Name>
           <CmdletSupported> Add-Content, Get-Content, Set-Content </CmdletSupported>
           <Type>
               <Name> Microsoft.PowerShell.Commands.FileSystemCmdletProviderEncoding
 </Name>
         <Type>
         <Description> Specifies the encoding of the output file that contains the
 content. </Description>
         <PossibleValues>
             <PossibleValue>
                 <Value> ASCII </Value>
                 <Description>
                     <para> Uses the encoding for the ASCII (7-bit) character set.
 </para>
                 </Description>
             </PossibleValue>
             <PossibleValue>
                 <Value> Unicode </Value>
                 <Description>
                     <para> Encodes in UTF-16 format using the little-endian byte
 order. </para>
                 </Description>
             </PossibleValue>
         </PossibleValues>
 </DynamicParameters>

Last updated on 04/08/2026

<!-- p.2918 -->

How to Add a See Also Section to a
Provider Help Topic

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This section explains how to populate the SEE ALSO section of a provider help topic.

The SEE ALSO section consists of a list of topics that are related to the provider or might help
the user better understand and use the provider. The topic list can include cmdlet help,
provider help and conceptual ("about") help topics in Windows PowerShell. It can also include
references to books, paper, and online topics, including an online version of the current
provider help topic.

When you refer to online topics, provide the URI or a search term in plain text. The Get-Help
cmdlet doesn't link or redirect to any of the topics in the list. Also, the Online parameter of the
Get-Help cmdlet doesn't work with provider help.

The See Also section is created from the RelatedLinks element and the tags that it contains.
The following XML shows how to add the tags.

To Add SEE ALSO Topics
   1. In the <AssemblyName>.dll-help.xml file, within the providerHelp element, add a
      RelatedLinks element. The RelatedLinks element should be the last element in the

      providerHelp element. Only one RelatedLinks element is permitted in each provider help

     topic.

     For example:

       XML

       <providerHelp>
           <RelatedLinks>

<!-- p.2919 -->

        </RelatedLinks>
    </providerHelp>

2. For each topic in the SEE ALSO section, within the RelatedLinks element, add a
  navigationLink element. Then, within each navigationLink element, add one linkText

  element and one uri element. If you aren't using the uri element, you can add it as an
  empty element (<uri/>).

  For example:

    XML

    <providerHelp>
        <RelatedLinks>
            <navigationLink>
                <linkText> </linkText>
                <uri> </uri>
            </navigationLink>
        </RelatedLinks>
    </providerHelp>

3. Type the topic name between the linkText tags. If you are providing a URI, type it
  between the uri tags. To indicate the online version of the current provider help topic,
  between the linkText tags, type "Online version:" instead of the topic name. Typically,
  the "Online version:" link is the first topic in the SEE ALSO topic list.

  The following example include three SEE ALSO topics. The first refer to the online version
  of the current topic. The second refers to a Windows PowerShell cmdlet help topic. The
  third refers to another online topic.

    XML

    <providerHelp>
        <RelatedLinks>
            <navigationLink>
                <linkText> Online version: </linkText>
                <uri>http://www.fabrikam.com/help/myFunction.htm</uri>
            </navigationLink>
            <navigationLink>
                <linkText> about_functions </linkText>
                <uri/>
            </navigationLink>
            <navigationLink>
                <linkText> Windows PowerShell Getting Started Guide </linkText>
                <uri>https://go.microsoft.com/fwlink/?LinkID=89597<uri/>
            </navigationLink>

<!-- p.2920 -->

           </RelatedLinks>
       </providerHelp>

Last updated on 05/20/2025
