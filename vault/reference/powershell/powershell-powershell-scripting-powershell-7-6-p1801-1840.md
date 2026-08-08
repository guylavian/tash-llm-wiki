---
title: "How to use this documentation — pages 1801-1840"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1801-1840
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1801-1840
family: powershell
documentKind: "doc"
abstract: "run certain pre-processing scripts. You can also use a manifest module as a convenient way to package up resources that other modules will use, such as nested modules, assemblies, types, or formats. For more information, see How to Write a PowerShell Module Manifest. Dynamic Mod"
---

# How to use this documentation — pages 1801-1840

<!-- p.1801 -->

run certain pre-processing scripts. You can also use a manifest module as a convenient way to
package up resources that other modules will use, such as nested modules, assemblies, types, or
formats. For more information, see How to Write a PowerShell Module Manifest.

Dynamic Modules
A dynamic module is a module that isn't loaded from, or saved to, a file. Instead, they're created
dynamically by a script, using the New-Module cmdlet. This type of module enables a script to
create a module on demand that doesn't need to be loaded or saved to persistent storage. By its
nature, a dynamic module is intended to be short-lived, and therefore can't be accessed by the
Get-Module cmdlet. Similarly, they usually don't need module manifests, nor do they likely need

permanent folders to store their related assemblies.

Module Manifests
A module manifest is a .psd1 file that contains a hash table. The keys and values in the hash
table do the following things:

     Describe the contents and attributes of the module.
     Define the prerequisites.
     Determine how the components are processed.

Manifests aren't required for a module. Modules can reference script files ( .ps1 ), script module
files ( .psm1 ), manifest files ( .psd1 ), formatting and type files ( .ps1xml ), cmdlet and provider
assemblies ( .dll ), resource files, Help files, localization files, or any other type of file or resource
that's bundled as part of the module. For an internationalized script, the module folder also
contains a set of message catalog files. If you add a manifest file to the module folder, you can
reference the multiple files as a single unit by referencing the manifest.

The manifest itself describes the following categories of information:

     Metadata about the module, such as the module version number, the author, and the
     description.
     Prerequisites needed to import the module, such as the Windows PowerShell version, the
     common language runtime (CLR) version, and the required modules.
     Processing directives, such as the scripts, formats, and types to process.
     Restrictions on the members of the module to export, such as the aliases, functions,
     variables, and cmdlets to export.

For more information, see How to Write a PowerShell Module Manifest.

<!-- p.1802 -->

Storing and Installing a Module
Once you have created a script, binary, or manifest module, you can save your work in a location
that others may access it. For example, your module can be stored in the system folder where
Windows PowerShell is installed, or it can be stored in a user folder.

Generally speaking, you can determine where you should install your module by using one of the
paths stored in the $Env:PSModulePath variable. Using one of these paths means that PowerShell
can automatically find and load your module when a user makes a call to it in their code. If you
store your module somewhere else, you can explicitly let PowerShell know by passing in the
location of your module as a parameter when you call Install-Module .

Regardless, the path of the folder is referred to as the base of the module (ModuleBase), and the
name of the script, binary, or manifest module file should be the same as the module folder
name, with the following exceptions:

     Dynamic modules that are created by the New-Module cmdlet can be named using the Name
     parameter of the cmdlet.
     Modules imported from assembly objects by the Import-Module -Assembly command are
     named according to the following syntax: "dynamic_code_module_" + assembly.GetName() .

For more information, see Installing a PowerShell Module and about_PSModulePath.

Module Cmdlets and Variables
The following cmdlets and variables are provided by Windows PowerShell for the creation and
management of modules.

     New-Module creates a new dynamic module that exists only in memory. The module is
     created from a script block, and its exported members, such as its functions and variables,
     are immediately available in the session and remain available until the session is closed.
     New-ModuleManifest creates a new module manifest ( .psd1 ) file, populates its values, and
     saves the manifest file to the specified path. This cmdlet can also be used to create a
     module manifest template that can be filled in manually.
     Import-Module adds one or more modules to the current session.
     Get-Module retrieves information about the modules that have been or that can be
     imported into the current session.
     Export-ModuleMember specifies the module members (such as cmdlets, functions,
     variables, and aliases) that are exported from a script module ( .psm1 ) file or from a dynamic

<!-- p.1803 -->

     module created by using the New-Module cmdlet.
     Remove-Module removes modules from the current session.
     Test-ModuleManifest verifies that a module manifest accurately describes the components
     of a module by verifying that the files that are listed in the module manifest file ( .psd1 )
     actually exist in the specified paths.
     $PSScriptRoot contains the directory from which the script module is being executed. It

     enables scripts to use the module path to access other resources.
     $Env:PSModulePath contains a list of the directories in which Windows PowerShell modules

     are stored. Windows PowerShell uses the value of this variable when importing modules
     automatically and updating Help topics for modules.

See Also
Writing a Windows PowerShell Module

Last updated on 06/16/2026

<!-- p.1804 -->

How to Write a PowerShell Script Module
A script module is any valid PowerShell script saved in a .psm1 extension. This extension allows
the PowerShell engine to use rules and module cmdlets on your file. Most of these capabilities
are there to help you install your code on other systems, as well as manage scoping. You can
also use a module manifest file, which describes more complex installations and solutions.

Writing a PowerShell script module
To create a script module, save a valid PowerShell script to a .psm1 file. The script and the
directory where it's stored must use the same name. For example, a script named
MyPsScript.psm1 is stored in a directory named MyPsScript .

The module's directory needs to be in a path specified in $Env:PSModulePath . The module's
directory can contain any resources that are needed to run the script, and a module manifest
file that describes to PowerShell how your module works.

Create a basic PowerShell module
The following steps describe how to create a PowerShell module.

   1. Save a PowerShell script with a .psm1 extension. Use the same name for the script and
     the directory where the script is saved.

     Saving a script with the .psm1 extension means that you can use the module cmdlets,
     such as Import-Module. The module cmdlets exist primarily so that you can import and
     export your code onto other user's systems. The alternate solution would be to load your
     code on other systems and then dot-source it into active memory, which isn't a scalable
     solution. For more information, see Understanding a Windows PowerShell Module. By
     default, when users import your .psm1 file, all functions in your script are accessible, but
     variables aren't.

     An example PowerShell script, entitled Show-Calendar , is available at the end of this
     article.

       PowerShell

       function Show-Calendar {
       param(

<!-- p.1805 -->

        [datetime] $Start = [datetime]::Today,
        [datetime] $End = $Start,
        $FirstDayOfWeek,
        [int[]] $HighlightDay,
        [string[]] $HighlightDate = [datetime]::Today.ToString('yyyy-MM-dd')
        )

        #actual code for the function goes here see the end of the topic for the
    complete code sample
    }

2. To control user access to certain functions or variables, call Export-ModuleMember at the
  end of your script.

  The example code at the bottom of the article has only one function, which by default
  would be exposed. However, it's recommended you explicitly call out which functions you
  wish to expose, as described in the following code:

    PowerShell

    function Show-Calendar {
          }
    Export-ModuleMember -Function Show-Calendar

  You can restrict what's imported using a module manifest. For more information, see
  Importing a PowerShell Module and How to Write a PowerShell Module Manifest.

3. If you have modules that your own module needs to load, you can use Import-Module , at
  the top of your module.

  The Import-Module cmdlet imports a targeted module onto a system, and can be used at
  a later point in the procedure to install your own module. The sample code at the bottom
  of this article doesn't use any import modules. But if it did, they would be listed at the top
  of the file, as shown in the following code:

    PowerShell

    Import-Module GenericModule

4. To describe your module to the PowerShell Help system, you can either use standard help
  comments inside the file, or create an additional Help file.

  The code sample at the bottom of this article includes the help information in the
  comments. You could also write expanded XML files that contain additional help content.

<!-- p.1806 -->

   For more information, see Writing Help for Windows PowerShell Modules.

 5. If you have additional modules, XML files, or other content you want to package with
   your module, you can use a module manifest.

   A module manifest is a file that contains the names of other modules, directory layouts,
   versioning numbers, author data, and other pieces of information. PowerShell uses the
   module manifest file to organize and deploy your solution. For more information, see
   How to write a PowerShell module manifest.

 6. To install and run your module, save the module to one of the appropriate PowerShell
   paths, and use Import-Module .

   The paths where you can install your module are located in the $Env:PSModulePath global
   variable. For example, a common path to save a module on a system would be
   %SystemRoot%/users/<user>/Documents/PowerShell/Modules/<moduleName> . Be sure to create

   a directory for your module that uses the same name as the script module, even if it's
   only a single .psm1 file. If you didn't save your module to one of these paths, you would
   have to specify the module's location in the Import-Module command. Otherwise,
   PowerShell wouldn't be able to find the module.

     ７ Note

     Starting with PowerShell 3.0, if you've placed your module in one of the PowerShell
     module paths, you don't need to explicitly import it. Your module is automatically
     loaded when a user calls your function. For more information about the module
     path, see Importing a PowerShell Module and about_PSModulePath.

 7. To remove a module from active service in the current PowerShell session, use Remove-
   Module.

     ７ Note

      Remove-Module removes a module from the current PowerShell session, but doesn't

     uninstall the module or delete the module's files.

Show-Calendar code example

<!-- p.1807 -->

The following example is a script module that contains a single function named Show-Calendar .
This function displays a visual representation of a calendar. The sample contains the PowerShell
Help strings for the synopsis, description, parameter values, and code. When the module is
imported, the Export-ModuleMember command ensures that the Show-Calendar function is
exported as a module member.

 PowerShell

 <#
  .SYNOPSIS
    Displays a visual representation of a calendar.

  .DESCRIPTION
   Displays a visual representation of a calendar. This function supports multiple
 months
   and lets you highlight specific date ranges or days.

  .PARAMETER Start
   The first month to display.

  .PARAMETER End
   The last month to display.

  .PARAMETER FirstDayOfWeek
   The day of the month on which the week begins.

  .PARAMETER HighlightDay
   Specific days (numbered) to highlight. Used for date ranges like (25..31).
   Date ranges are specified by the Windows PowerShell range syntax. These dates are
   enclosed in square brackets.

  .PARAMETER HighlightDate
   Specific days (named) to highlight. These dates are surrounded by asterisks.

  .EXAMPLE
    # Show a default display of this month.
    Show-Calendar

  .EXAMPLE
    # Display a date range.
    Show-Calendar -Start "March, 2010" -End "May, 2010"

  .EXAMPLE
    # Highlight a range of days.
    Show-Calendar -HighlightDay (1..10 + 22) -HighlightDate "2008-12-25"
 #>
 function Show-Calendar {
 param(
     [datetime] $Start = [datetime]::Today,
     [datetime] $End = $Start,
     $FirstDayOfWeek,
     [int[]] $HighlightDay,

<!-- p.1808 -->

    [string[]] $HighlightDate = [datetime]::Today.ToString('yyyy-MM-dd')
    )

## Determine the first day of the start and end months.
$Start = New-Object DateTime $Start.Year,$Start.Month,1
$End = New-Object DateTime $End.Year,$End.Month,1

## Convert the highlighted dates into real dates.
[datetime[]] $HighlightDate = [datetime[]] $HighlightDate

## Retrieve the DateTimeFormat information so that the
## calendar can be manipulated.
$dateTimeFormat = (Get-Culture).DateTimeFormat
if($FirstDayOfWeek)
{
    $dateTimeFormat.FirstDayOfWeek = $FirstDayOfWeek
}

$currentDay = $Start

## Process the requested months.
while($Start -le $End)
{
    ## Return to an earlier point in the function if the first day of the month
    ## is in the middle of the week.
    while($currentDay.DayOfWeek -ne $dateTimeFormat.FirstDayOfWeek)
    {
        $currentDay = $currentDay.AddDays(-1)
    }

    ## Prepare to store information about this date range.
    $currentWeek = New-Object PsObject
    $dayNames = @()
    $weeks = @()

    ## Continue processing dates until the function reaches the end of the month.
    ## The function continues until the week is completed with
    ## days from the next month.
    while(($currentDay -lt $Start.AddMonths(1)) -or
        ($currentDay.DayOfWeek -ne $dateTimeFormat.FirstDayOfWeek))
    {
        ## Determine the day names to use to label the columns.
        $dayName = "{0:ddd}" -f $currentDay
        if($dayNames -notcontains $dayName)
        {
            $dayNames += $dayName
        }

       ## Pad the day number for display, highlighting if necessary.
       $displayDay = " {0,2} " -f $currentDay.Day

       ## Determine whether to highlight a specific date.
       if($HighlightDate)
       {
           $compareDate = New-Object DateTime $currentDay.Year,

<!-- p.1809 -->

                    $currentDay.Month,$currentDay.Day
                if($HighlightDate -contains $compareDate)
                {
                    $displayDay = "*" + ("{0,2}" -f $currentDay.Day) + "*"
                }
           }

           ## Otherwise, highlight as part of a date range.
           if($HighlightDay -and ($HighlightDay[0] -eq $currentDay.Day))
           {
               $displayDay = "[" + ("{0,2}" -f $currentDay.Day) + "]"
               $null,$HighlightDay = $HighlightDay
           }

           ## Add the day of the week and the day of the month as note properties.
           $currentWeek | Add-Member NoteProperty $dayName $displayDay

           ## Move to the next day of the month.
           $currentDay = $currentDay.AddDays(1)

           ## If the function reaches the next week, store the current week
           ## in the week list and continue.
           if($currentDay.DayOfWeek -eq $dateTimeFormat.FirstDayOfWeek)
           {
               $weeks += $currentWeek
               $currentWeek = New-Object PsObject
           }
      }

      ## Format the weeks as a table.
      $calendar = $weeks | Format-Table $dayNames -AutoSize | Out-String

      ## Add a centered header.
      $width = ($calendar.Split("`n") | Measure-Object -Maximum Length).Maximum
      $header = "{0:MMMM yyyy}" -f $Start
      $padding = " " * (($width - $header.Length) / 2)
      $displayCalendar = " `n" + $padding + $header + "`n " + $calendar
      $displayCalendar.TrimEnd()

      ## Move to the next month.
      $Start = $Start.AddMonths(1)

 }
 }
 Export-ModuleMember -Function Show-Calendar

Last updated on 05/20/2025

<!-- p.1810 -->

How to Write a PowerShell Binary Module
06/12/2025

A binary module can be any assembly ( .dll ) that contains cmdlet classes. By default, all the
cmdlets in the assembly are imported when the binary module is imported. However, you can
restrict the cmdlets that are imported by creating a module manifest whose root module is the
assembly. (For example, the CmdletsToExport key of the manifest can be used to export only
those cmdlets that are needed.) In addition, a binary module can contain additional files, a
directory structure, and other pieces of useful management information that a single cmdlet
cannot.

The following procedure describes how to create and install a PowerShell binary module.

How to create and install a PowerShell binary
module
   1. Create a binary PowerShell solution (such as a cmdlet written in C#), with the capabilities
     you need, and ensure that it runs properly.

     From a code perspective, the core of a binary module is a cmdlet assembly. In fact,
     PowerShell treats a single cmdlet assembly as a module for loading and unloading, with
     no additional effort on the part of the developer. For more information about writing a
     cmdlet, see Writing a Windows PowerShell Cmdlet.

   2. If necessary, create the rest of your solution: (additional cmdlets, XML files, and so on)
     and describe them with a module manifest.

     In addition to describing the cmdlet assemblies in your solution, a module manifest can
     describe how you want your module exported and imported, what cmdlets will be
     exposed, and what additional files will go into the module. As stated previously however,
     PowerShell can treat a binary cmdlet like a module with no additional effort. As such, a
     module manifest is useful mainly for combining multiple files into a single package, or for
     explicitly controlling publication for a given assembly. For more information, see How to
     Write a PowerShell Module Manifest.

     The following code is a simplified C# example that contains three cmdlets in the same file
     that can be used as a module.

          C#

          using System.Management.Automation;                // Windows PowerShell
          namespace.

<!-- p.1811 -->

    namespace ModuleCmdlets
    {
      [Cmdlet(VerbsDiagnostic.Test,"BinaryModuleCmdlet1")]
      public class TestBinaryModuleCmdlet1Command : Cmdlet
      {
        protected override void BeginProcessing()
        {
          WriteObject("BinaryModuleCmdlet1 exported by the ModuleCmdlets
    module.");
        }
      }

      [Cmdlet(VerbsDiagnostic.Test, "BinaryModuleCmdlet2")]
      public class TestBinaryModuleCmdlet2Command : Cmdlet
      {
          protected override void BeginProcessing()
          {
               WriteObject("BinaryModuleCmdlet2 exported by the ModuleCmdlets
    module.");
          }
      }

      [Cmdlet(VerbsDiagnostic.Test, "BinaryModuleCmdlet3")]
      public class TestBinaryModuleCmdlet3Command : Cmdlet
      {
          protected override void BeginProcessing()
          {
               WriteObject("BinaryModuleCmdlet3 exported by the ModuleCmdlets
    module.");
          }
      }

    }

3. Package your solution, and save the package to somewhere in the PowerShell module
  path.

  The $env:PSModulePath global environment variable describes the default paths that
  PowerShell uses to locate your module. For example, a common path to save a module
  on a system would be %SystemRoot%\Users\<user>\Documents\WindowsPowerShell\Modules\
  <moduleName> . If you don't use the default paths, you need to explicitly state the location

  of your module during installation. Be sure to create a folder to save your module in, as
  you may need the folder to store multiple assemblies and files for your solution.

  Technically, you don't need to install your module anywhere on the $env:PSModulePath -
  those are simply the default locations that PowerShell will look for your module. However,
  it's considered best practice to do so, unless you have a good reason for storing your

<!-- p.1812 -->

     module somewhere else. For more information, see Installing a PowerShell Module and
     about_PSModulePath.

   4. Import your module into PowerShell with a call to Import-Module.

     Calling to Import-Module loads your module into active memory. If you are using
     PowerShell 3.0 and later, invoking a command from your module in code also imports it.
     For more information, see Importing a PowerShell Module.

Module initialization and cleanup code
If your module needs to do something upon import or removal such as a discovery task or
initialization, you can implement the IModuleAssemblyInitializer and IModuleAssemblyCleanup
interfaces.

  ７ Note

  This pattern is discouraged unless absolutely necessary. To keep PowerShell performant,
  you should lazily load things at the point your commands are called rather than on import.

Importing snap-in assemblies as modules
Cmdlets and providers that exist in snap-in assemblies can be loaded as binary modules. When
the snap-in assemblies are loaded as binary modules, the cmdlets and providers in the snap-in
are available to the user, but the snap-in class in the assembly is ignored, and the snap-in isn't
registered. As a result, the snap-in cmdlets provided by Windows PowerShell can't detect the
snap-in even though the cmdlets and providers are available to the session.

In addition, any formatting or types files that are referenced by the snap-in can't be imported
as part of a binary module. To import the formatting and types files you must create a module
manifest. See, How to Write a PowerShell Module Manifest.

See Also
     Writing a Windows PowerShell Module

<!-- p.1813 -->

How to write a PowerShell module manifest
After you've written your PowerShell module, you can add an optional module manifest that
includes information about the module. For example, you can describe the author, specify files in
the module (such as nested modules), run scripts to customize the user's environment, load type
and formatting files, define system requirements, and limit the members that the module exports.

Creating a module manifest
A module manifest is a PowerShell data file ( .psd1 ) that describes the contents of a module and
determines how a module is processed. The manifest file is a text file that contains a hash table of
keys and values. You link a manifest file to a module by naming the manifest the same as the
module, and storing the manifest in the module's root directory.

For simple modules that contain only a single .psm1 or binary assembly, a module manifest is
optional. But, the recommendation is to use a module manifest whenever possible, as they're
useful to help you organize your code and maintain versioning information. And, a module
manifest is required to export an assembly that is installed in the Global Assembly Cache. A
module manifest is also required for modules that support the Updatable Help feature.
Updatable Help uses the HelpInfoUri key in the module manifest to find the Help information
(HelpInfo XML) file that contains the location of the updated help files for the module. For more
information about Updatable Help, see Supporting Updatable Help.

To create and use a module manifest
   1. The best practice to create a module manifest is to use the New-ModuleManifest cmdlet.
     You can use parameters to specify one or more of the manifest's default keys and values.
     The only requirement is to name the file. New-ModuleManifest creates a module manifest
     with your specified values, and includes the remaining keys and their default values. If you
     need to create multiple modules, use New-ModuleManifest to create a module manifest
     template that can be modified for your different modules. For an example of a default
     module manifest, see the Sample module manifest.

     New-ModuleManifest -Path C:\myModuleName.psd1 -ModuleVersion "2.0" -Author

     "YourNameHere"

<!-- p.1814 -->

   An alternative is to manually create the module manifest's hash table using the minimal
   information required, the ModuleVersion. You save the file with the same name as your
   module and use the .psd1 file extension. You can then edit the file and add the appropriate
   keys and values.

 2. Add any additional elements that you want in the manifest file.

   To edit the manifest file, use any text editor you prefer. But, the manifest file is a script file
   that contains code, so you may wish to edit it in a scripting or development environment,
   such as Visual Studio Code. All elements of a manifest file are optional, except for the
   ModuleVersion number.

   For more information, see the parameter descriptions in the New-ModuleManifest cmdlet.
   For descriptions of the keys and values you can include in a module manifest, see
   about_Module_Manifests.

 3. To address any scenarios that might not be covered by the base module manifest elements,
   you have the option to add additional code to your module manifest.

   For security concerns, PowerShell only runs a small subset of the available operations in a
   module manifest file. Generally, you can use the if statement, arithmetic and comparison
   operators, and the basic PowerShell data types.

 4. After you've created your module manifest, you can test it to confirm that any paths
   described in the manifest are correct. To test your module manifest, use Test-
   ModuleManifest.

   Test-ModuleManifest myModuleName.psd1

 5. Be sure that your module manifest is located in the top level of the directory that contains
   your module.

   When you copy your module onto a system and import it, PowerShell uses the module
   manifest to import your module.

 6. Optionally, you can directly test your module manifest with a call to Import-Module by dot-
   sourcing the manifest itself.

   Import-Module .\myModuleName.psd1

Sample module manifest

<!-- p.1815 -->

The following sample module manifest was created with New-ModuleManifest in PowerShell 7 and
contains the default keys and values. For a detailed description of each element in a module
manifest, see about_Module_Manifests.

 PowerShell

 #
 # Module manifest for module 'SampleModuleManifest'
 #
 # Generated by: User01
 #
 # Generated on: 10/15/2019
 #

 @{

 # Script module or binary module file associated with this manifest.
 # RootModule = ''

 # Version number of this module.
 ModuleVersion = '0.0.1'

 # Supported PSEditions
 # CompatiblePSEditions = @()

 # ID used to uniquely identify this module
 GUID = 'b632e90c-df3d-4340-9f6c-3b832646bf87'

 # Author of this module
 Author = 'User01'

 # Company or vendor of this module
 CompanyName = 'Unknown'

 # Copyright statement for this module
 Copyright = '(c) User01. All rights reserved.'

 # Description of the functionality provided by this module
 # Description = ''

 # Minimum version of the PowerShell engine required by this module
 # PowerShellVersion = ''

 # Name of the PowerShell host required by this module
 # PowerShellHostName = ''

 # Minimum version of the PowerShell host required by this module
 # PowerShellHostVersion = ''

 # Minimum version of Microsoft .NET Framework required by this module. This
 prerequisite is valid for the PowerShell Desktop edition only.
 # DotNetFrameworkVersion = ''

<!-- p.1816 -->

# Minimum version of the common language runtime (CLR) required by this module. This
prerequisite is valid for the PowerShell Desktop edition only.
# CLRVersion = ''

# Processor architecture (None, X86, Amd64) required by this module
# ProcessorArchitecture = ''

# Modules that must be imported into the global environment prior to importing this
module
# RequiredModules = @()

# Assemblies that must be loaded prior to importing this module
# RequiredAssemblies = @()

# Script files (.ps1) that are run in the caller's environment prior to importing this
module.
# ScriptsToProcess = @()

# Type files (.ps1xml) to be loaded when importing this module
# TypesToProcess = @()

# Format files (.ps1xml) to be loaded when importing this module
# FormatsToProcess = @()

# Modules to import as nested modules of the module specified in
RootModule/ModuleToProcess
# NestedModules = @()

# Functions to export from this module, for best performance, do not use wildcards and
do not delete the entry, use an empty array if there are no functions to export.
FunctionsToExport = @()

# Cmdlets to export from this module, for best performance, do not use wildcards and
do not delete the entry, use an empty array if there are no cmdlets to export.
CmdletsToExport = @()

# Variables to export from this module
VariablesToExport = '*'

# Aliases to export from this module, for best performance, do not use wildcards and
do not delete the entry, use an empty array if there are no aliases to export.
AliasesToExport = @()

# DSC resources to export from this module
# DscResourcesToExport = @()

# List of all modules packaged with this module
# ModuleList = @()

# List of all files packaged with this module
# FileList = @()

# Private data to pass to the module specified in RootModule/ModuleToProcess. This may
also contain a PSData hashtable with additional module metadata used by PowerShell.
PrivateData = @{

<!-- p.1817 -->

     PSData = @{

         # Tags applied to this module. These help with module discovery in online
 galleries.
         # Tags = @()

          # A URL to the license for this module.
          # LicenseUri = ''

          # A URL to the main website for this project.
          # ProjectUri = ''

          # A URL to an icon representing this module.
          # IconUri = ''

          # ReleaseNotes of this module
          # ReleaseNotes = ''

          # Prerelease string of this module
          # Prerelease = ''

         # Flag to indicate whether the module requires explicit user acceptance for
 install/update/save
         # RequireLicenseAcceptance = $false

          # External dependent modules of this module
          # ExternalModuleDependencies = @()

     } # End of PSData hashtable

 } # End of PrivateData hashtable

 # HelpInfo URI of this module
 # HelpInfoURI = ''

 # Default prefix for commands exported from this module. Override the default prefix
 using Import-Module -Prefix.
 # DefaultCommandPrefix = ''

 }

See also
     about_Comparison_Operators
     about_If
     Global Assembly Cache
     Import-Module
     New-ModuleManifest
     Test-ModuleManifest

<!-- p.1818 -->

     Update-ModuleManifest
     Writing a Windows PowerShell Module

Last updated on 05/04/2026

<!-- p.1819 -->

Installing a PowerShell Module
After you have created your PowerShell module, you will likely want to install the module on a
system, so that you or others may use it. Generally speaking, this consists of copying the
module files (ie, the .psm1 , or the binary assembly, the module manifest, and any other
associated files) onto a directory on that computer. For a very small project, this may be as
simple as copying and pasting the files with Windows Explorer onto a single remote computer;
however, for larger solutions you may wish to use a more sophisticated installation process.
Regardless of how you get your module onto the system, PowerShell can use a number of
techniques that will let users find and use your modules. Therefore, the main issue for
installation is ensuring that PowerShell will be able to find your module. For more information,
see Importing a PowerShell Module.

Rules for Installing Modules
The following information pertains to all modules, including modules that you create for your
own use, modules that you get from other parties, and modules that you distribute to others.

Install Modules in PSModulePath
Whenever possible, install all modules in a path that is listed in the PSModulePath
environment variable or add the module path to the PSModulePath environment variable
value.

The PSModulePath environment variable ( $Env:PSModulePath ) contains the locations of
Windows PowerShell modules. Cmdlets rely on the value of this environment variable to find
modules.

By default, the PSModulePath environment variable value contains the following system and
user module directories, but you can add to and edit the value.

         $PSHOME\Modules ( %windir%\System32\WindowsPowerShell\v1.0\Modules )

          ２ Warning

          This location is reserved for modules that ship with Windows. Do not install modules
          to this location.

<!-- p.1820 -->

   $HOME\Documents\WindowsPowerShell\Modules

   ( %HOMEDRIVE%%HOMEPATH%\Documents\WindowsPowerShell\Modules )

   $Env:ProgramFiles\WindowsPowerShell\Modules

   ( %ProgramFiles%\WindowsPowerShell\Modules )

   To get the value of the PSModulePath environment variable, use either of the following
   commands.

    PowerShell

    $Env:PSModulePath
    [Environment]::GetEnvironmentVariable("PSModulePath")

   To add a module path to value of the PSModulePath environment variable value, use the
   following command format. This format uses the SetEnvironmentVariable method of the
   System.Environment class to make a session-independent change to the PSModulePath
   environment variable.

    PowerShell

    #Save the current value in the $p variable.
    $p = [Environment]::GetEnvironmentVariable("PSModulePath")

    #Add the new path to the $p variable. Begin with a semi-colon separator.
    $p += ";C:\Program Files (x86)\MyCompany\Modules\"

    #Add the paths in $p to the PSModulePath value.
    [Environment]::SetEnvironmentVariable("PSModulePath",$p)

     ） Important

     Once you have added the path to PSModulePath, you should broadcast an
     environment message about the change. Broadcasting the change allows other
     applications, such as the shell, to pick up the change. To broadcast the change, have
     your product installation code send a WM_SETTINGCHANGE message with lParam
     set to the string "Environment". Be sure to send the message after your module
     installation code has updated PSModulePath.

Use the Correct Module Directory Name

<!-- p.1821 -->

A well-formed module is a module that is stored in a directory that has the same name as the
base name of at least one file in the module directory. If a module is not well-formed, Windows
PowerShell does not recognize it as a module.

The "base name" of a file is the name without the file name extension. In a well-formed
module, the name of the directory that contains the module files must match the base name of
at least one file in the module.

For example, in the sample Fabrikam module, the directory that contains the module files is
named "Fabrikam" and at least one file has the "Fabrikam" base name. In this case, both
Fabrikam.psd1 and Fabrikam.dll have the "Fabrikam" base name.

 C:\Program Files
   Fabrikam Technologies
     Fabrikam Manager
       Modules
         Fabrikam
           Fabrikam.psd1 (module manifest)
           Fabrikam.dll (module assembly)

Effect of Incorrect Installation
If the module is not well-formed and its location is not included in the value of the
PSModulePath environment variable, basic discovery features of Windows PowerShell, such as
the following, do not work.

     The Module Auto-Loading feature cannot import the module automatically.

     The ListAvailable parameter of the Get-Module cmdlet cannot find the module.

     The Import-Module cmdlet cannot find the module. To import the module, you must
     provide the full path to the root module file or module manifest file.

     Additional features, such as the following, do not work unless the module is imported
     into the session. In well-formed modules in the PSModulePath environment variable,
     these features work even when the module is not imported into the session.

     The Get-Command cmdlet cannot find commands in the module.

     The Update-Help and Save-Help cmdlets cannot update or save help for the module.

     The Show-Command cmdlet cannot find and display the commands in the module.

<!-- p.1822 -->

     The commands in the module are missing from the Show-Command window in Windows
     PowerShell Integrated Scripting Environment (ISE).

Where to Install Modules
This section explains where in the file system to install Windows PowerShell modules. The
location depends on how the module is used.

Installing Modules for a Specific User
If you create your own module or get a module from another party, such as a Windows
PowerShell community website, and you want the module to be available for your user account
only, install the module in your user-specific Modules directory.

$HOME\Documents\WindowsPowerShell\Modules\<Module Folder>\<Module Files>

The user-specific Modules directory is added to the value of the PSModulePath environment
variable by default.

Installing Modules for all Users in Program Files
If you want a module to be available to all user accounts on the computer, install the module in
the Program Files location.

$Env:ProgramFiles\WindowsPowerShell\Modules\<Module Folder>\<Module Files>

  ７ Note

  The Program Files location is added to the value of the PSModulePath environment
  variable by default in Windows PowerShell 4.0 and later. For earlier versions of Windows
  PowerShell, you can manually create the Program Files location
  (%ProgramFiles%\WindowsPowerShell\Modules) and add this path to your PSModulePath
  environment variable as described above.

Installing Modules in a Product Directory
If you are distributing the module to other parties, use the default Program Files location
described above, or create your own company-specific or product-specific subdirectory of the
%ProgramFiles% directory.

<!-- p.1823 -->

For example, Fabrikam Technologies, a fictitious company, is shipping a Windows PowerShell
module for their Fabrikam Manager product. Their module installer creates a Modules
subdirectory in the Fabrikam Manager product subdirectory.

 C:\Program Files
   Fabrikam Technologies
     Fabrikam Manager
       Modules
         Fabrikam
           Fabrikam.psd1 (module manifest)
           Fabrikam.dll (module assembly)

To enable the Windows PowerShell module discovery features to find the Fabrikam module, the
Fabrikam module installer adds the module location to the value of the PSModulePath
environment variable.

 PowerShell

 $p = [Environment]::GetEnvironmentVariable("PSModulePath")
 $p += ";C:\Program Files\Fabrikam Technologies\Fabrikam Manager\Modules\"
 [Environment]::SetEnvironmentVariable("PSModulePath",$p)

Installing Modules in the Common Files Directory
If a module is used by multiple components of a product or by multiple versions of a product,
install the module in a module-specific subdirectory of the %ProgramFiles%\Common
Files\Modules subdirectory.

In the following example, the Fabrikam module is installed in a Fabrikam subdirectory of the
%ProgramFiles%\Common Files\Modules subdirectory. Note that each module resides in its own

subdirectory in the Modules subdirectory.

 C:\Program Files
   Common Files
     Modules
       Fabrikam
         Fabrikam.psd1 (module manifest)
         Fabrikam.dll (module assembly)

<!-- p.1824 -->

Then, the installer assures the value of the PSModulePath environment variable includes the
path of the Common Files\Modules subdirectory.

 PowerShell

 $m = $Env:ProgramFiles + '\Common Files\Modules'
 $p = [Environment]::GetEnvironmentVariable("PSModulePath")
 $q = $p -split ';'
 if ($q -notcontains $m) {
     $q += ";$m"
 }
 $p = $q -join ';'
 [Environment]::SetEnvironmentVariable("PSModulePath", $p)

Installing Multiple Versions of a Module
To install multiple versions of the same module, use the following procedure.

   1. Create a directory for each version of the module. Include the version number in the
     directory name.
   2. Create a module manifest for each version of the module. In the value of the
     ModuleVersion key in the manifest, enter the module version number. Save the manifest
     file ( .psd1 ) in the version-specific directory for the module.
   3. Add the module root folder path to the value of the PSModulePath environment variable,
     as shown in the following examples.

To import a particular version of the module, the end-user can use the MinimumVersion or
RequiredVersion parameters of the Import-Module cmdlet.

For example, if the Fabrikam module is available in versions 8.0 and 9.0, the Fabrikam module
directory structure might resemble the following.

 C:\Program Files
 Fabrikam Manager
  Fabrikam8
    Fabrikam
      Fabrikam.psd1 (module manifest: ModuleVersion = "8.0")
      Fabrikam.dll (module assembly)
  Fabrikam9
    Fabrikam
      Fabrikam.psd1 (module manifest: ModuleVersion = "9.0")
      Fabrikam.dll (module assembly)

<!-- p.1825 -->

The installer adds both of the module paths to the PSModulePath environment variable value.

 PowerShell

 $p = [Environment]::GetEnvironmentVariable("PSModulePath")
 $p += ";C:\Program Files\Fabrikam\Fabrikam8;C:\Program Files\Fabrikam\Fabrikam9"
 [Environment]::SetEnvironmentVariable("PSModulePath",$p)

When these steps are complete, the ListAvailable parameter of the Get-Module cmdlet gets
both of the Fabrikam modules. To import a particular module, use the MinimumVersion or
RequiredVersion parameters of the Import-Module cmdlet.

If both modules are imported into the same session, and the modules contain cmdlets with the
same names, the cmdlets that are imported last are effective in the session.

Handling Command Name Conflicts
Command name conflicts can occur when the commands that a module exports have the same
name as commands in the user's session.

When a session contains two commands that have the same name, Windows PowerShell runs
the command type that takes precedence. When a session contains two commands that have
the same name and the same type, Windows PowerShell runs the command that was added to
the session most recently. To run a command that is not run by default, users can qualify the
command name with the module name.

For example, if the session contains a Get-Date function and the Get-Date cmdlet, Windows
PowerShell runs the function by default. To run the cmdlet, preface the command with the
module name, such as:

 PowerShell

 Microsoft.PowerShell.Utility\Get-Date

To prevent name conflicts, module authors can use the DefaultCommandPrefix key in the
module manifest to specify a noun prefix for all commands exported from the module.

Users can use the Prefix parameter of the Import-Module cmdlet to use an alternate prefix. The
value of the Prefix parameter takes precedence over the value of the DefaultCommandPrefix
key.

<!-- p.1826 -->

Supporting paths on non-Windows systems
Non-Windows platforms use the colon ( : ) character as a path separator and a forward-slash
( / ) character as a directory separator. The [System.IO.Path] class has static members that can
be used to make your code work on any platform:

      [System.IO.Path]::PathSeparator - returns the character used to separate paths in a

      PATH environment variable for the host platform
      [System.IO.Path]::DirectorySeparatorChar - returns the character used to separate

      directory names with a path for the host platform

Use these static properties to in place of the ; and \ characters when you are constructing
path strings.

See Also
about_Command_Precedence

Writing a Windows PowerShell Module

 Last updated on 05/20/2025

<!-- p.1827 -->

Registering Cmdlets
The topics in this section describe modules and snap-ins and how to use modules and snap-ins
to make cmdlets available in a Windows PowerShell session.

In This Section
Modules and Snap-ins Describes the differences between registering cmdlets through modules
and through snap-ins.

How to Register Cmdlets using Modules Describes how to register cmdlets using modules.

How to Create a Windows PowerShell Snap-in Describes how to register cmdlets using snap-
ins.

See Also
Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1828 -->

Modules and Snap-ins
Cmdlets can be added to a session using modules (introduced by Windows PowerShell 2.0) or
snap-ins. Once the cmdlet is added to the session it can be run programmatically by a host
application or interactively at the command line.

We recommend that you use modules as the delivery method for adding cmdlets to a session
for the following reasons:

      Modules allow you to add cmdlets by loading the assembly where the cmdlet is defined.
      There is no need to implement a snap-in class.

      Modules allow you to add other resources, such as variables, functions, scripts, types and
      formatting files, and more.

      Snap-ins can be used only to add cmdlets and providers to the session.

See Also
Writing a Windows PowerShell Module

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1829 -->

How to Import Cmdlets Using Modules
This article describes how to import cmdlets to a PowerShell session by using a binary module.

  ７ Note

  The members of modules can include cmdlets, providers, functions, variables, aliases, and
  much more. Snap-ins can contain only cmdlets and providers.

How to load cmdlets using a module
   1. Create a module folder that has the same name as the assembly file in which the cmdlets
     are implemented. In this procedure, the module folder is created in the Windows
     system32 folder.

     %SystemRoot%\system32\WindowsPowerShell\v1.0\Modules\mymodule

   2. Make sure that the PSModulePath environment variable includes the path to your new
     module folder. By default, the system folder is already added to the PSModulePath
     environment variable. To view the PSModulePath , type: $Env:PSModulePath .

   3. Copy the cmdlet assembly into the module folder.

   4. Add a module manifest file ( .psd1 ) in the module's root folder. PowerShell uses the
     module manifest to import your module. For more information, see How to Write a
     PowerShell Module Manifest.

   5. Run the following command to add the cmdlets to the session:

     Import-Module [Module_Name]

     This procedure can be used to test your cmdlets. It adds all the cmdlets in the assembly
     to the session. For more information about modules, see Writing a Windows PowerShell
     Module.

See also
How to Write a PowerShell Module Manifest

<!-- p.1830 -->

Importing a PowerShell Module

Import-Module

Installing Modules

about_PSModulePath

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1831 -->

How to Create a Windows PowerShell
Snap-in
A Windows PowerShell snap-in provides a mechanism for registering sets of cmdlets and
another Windows PowerShell provider with the shell, thus extending the functionality of the
shell. A Windows PowerShell snap-in can register all the cmdlets and providers in a single
assembly, or it can register a specific list of cmdlets and providers.

Snap-in assemblies should be installed in a protected directory, just as they would be with
other operating systems. Otherwise, malicious users can replace an assembly with unsafe code.

Windows PowerShell Snap-in Classes
All Windows PowerShell snap-in classes derive from the
System.Management.Automation.PSSnapIn or
System.Management.Automation.CustomPSSnapIn classes.

Examples
Writing a Windows PowerShell Snap-in: This example shows how to create a snap-in that is
used to register all the cmdlets and providers in an assembly.

Writing a Custom Windows PowerShell Snap-in: This example shows how to create a custom
snap-in that is used to register a specific set of cmdlets and providers that might or might not
exist in a single assembly.

See Also
System.Management.Automation.PSSnapIn

System.Management.Automation.CustomPSSnapIn

Registering Cmdlets

Windows PowerShell Shell SDK

 Last updated on 05/20/2025

<!-- p.1832 -->

Writing a Windows PowerShell Snap-in
This example shows how to write a Windows PowerShell snap-in that can be used to register all
the cmdlets and Windows PowerShell providers in an assembly.

With this type of snap-in, you do not select which cmdlets and providers you want to register.
To write a snap-in that allows you to select what is registered, see Writing a Custom Windows
PowerShell Snap-in.

Writing a Windows PowerShell Snap-in
   1. Add the RunInstallerAttribute attribute.

   2. Create a public class that derives from the System.Management.Automation.PSSnapIn
     class.

     In this example, the class name is "GetProcPSSnapIn01".

   3. Add a public property for the name of the snap-in (required). When naming snap-ins, do
     not use any of the following characters: # , . , , , ( , ) , { , } , [ , ] , & , - , / , \ , $ , ; , : , " ,
     ', <, >, |, ?, @, `, *

     In this example, the name of the snap-in is "GetProcPSSnapIn01".

   4. Add a public property for the vendor of the snap-in (required).

     In this example, the vendor is "Microsoft".

   5. Add a public property for the vendor resource of the snap-in (optional).

     In this example, the vendor resource is "GetProcPSSnapIn01,Microsoft".

   6. Add a public property for the description of the snap-in (required).

     In this example, the description is "This is a Windows PowerShell snap-in that registers the
     Get-Proc cmdlet".

   7. Add a public property for the description resource of the snap-in (optional).

     In this example, the vendor resource is "GetProcPSSnapIn01,This is a Windows PowerShell
     snap-in that registers the Get-Proc cmdlet".

<!-- p.1833 -->

Example
This example shows how to write a Windows PowerShell snap-in that can be used to register
the Get-Proc cmdlet in the Windows PowerShell shell. Be aware that in this example, the
complete assembly would contain only the GetProcPSSnapIn01 snap-in class and the Get-Proc
cmdlet class.

 C#

 [RunInstaller(true)]
 public class GetProcPSSnapIn01 : PSSnapIn
 {
   /// <summary>
   /// Create an instance of the GetProcPSSnapIn01 class.
   /// </summary>
   public GetProcPSSnapIn01()
          : base()
   {
   }

    /// <summary>
    /// Specify the name of the PowerShell snap-in.
    /// </summary>
    public override string Name
    {
      get
      {
        return "GetProcPSSnapIn01";
      }
    }

    /// <summary>
    /// Specify the vendor for the PowerShell snap-in.
    /// </summary>
    public override string Vendor
    {
      get
      {
        return "Microsoft";
      }
    }

    /// <summary>
    /// Specify the localization resource information for the vendor.
    /// Use the format: resourceBaseName,VendorName.
    /// </summary>
    public override string VendorResource
    {
      get
      {
        return "GetProcPSSnapIn01,Microsoft";

<!-- p.1834 -->

       }
   }

   /// <summary>
   /// Specify a description of the PowerShell snap-in.
   /// </summary>
   public override string Description
   {
     get
     {
       return "This is a PowerShell snap-in that includes the Get-Proc cmdlet.";
     }
   }

   /// <summary>
   /// Specify the localization resource information for the description.
   /// Use the format: resourceBaseName,Description.
   /// </summary>
   public override string DescriptionResource
   {
     get
     {
       return "GetProcPSSnapIn01,This is a PowerShell snap-in that includes the Get-
 Proc cmdlet.";
     }
   }
 }

See Also
How to Register Cmdlets, Providers, and Host Applications

Windows PowerShell Shell SDK

Last updated on 05/20/2025

<!-- p.1835 -->

Writing a Custom Windows PowerShell
Snap-in
This example shows how to write a Windows PowerShell snap-in that registers specific cmdlets.

With this type of snap-in, you specify which cmdlets, providers, types, or formats to register.
For more information about how to write a snap-in that registers all the cmdlets and providers
in an assembly, see Writing a Windows PowerShell Snap-in.

To write a Windows PowerShell Snap-in that
registers specific cmdlets.
   1. Add the RunInstallerAttribute attribute.

   2. Create a public class that derives from the
     System.Management.Automation.CustomPSSnapIn class.

     In this example, the class name is "CustomPSSnapinTest".

   3. Add a public property for the name of the snap-in (required). When naming snap-ins, do
     not use any of the following characters: # , . , , , ( , ) , { , } , [ , ] , & , - , / , \ , $ , ; , : , " ,
     ', <, >, |, ?, @, `, *

     In this example, the name of the snap-in is "CustomPSSnapInTest".

   4. Add a public property for the vendor of the snap-in (required).

     In this example, the vendor is "Microsoft".

   5. Add a public property for the vendor resource of the snap-in (optional).

     In this example, the vendor resource is "CustomPSSnapInTest,Microsoft".

   6. Add a public property for the description of the snap-in (required).

     In this example, the description is: "This is a custom Windows PowerShell snap-in that
     includes the Test-HelloWorld and Test-CustomSnapinTest cmdlets".

   7. Add a public property for the description resource of the snap-in (optional).

<!-- p.1836 -->

      In this example, the vendor resource is:

        CustomPSSnapInTest, This is a custom Windows PowerShell snap-in that includes the
        Test-HelloWorld and Test-CustomSnapinTest cmdlets".

   8. Specify the cmdlets that belong to the custom snap-in (optional) using the
      System.Management.Automation.Runspaces.CmdletConfigurationEntry class. The
      information added here includes the name of the cmdlet, its .NET type, and the cmdlet
      Help file name (the format of the cmdlet Help file name should be name.dll-help.xml ).

      This example adds the Test-HelloWorld and TestCustomSnapinTest cmdlets.

   9. Specify the providers that belong to the custom snap-in (optional).

      This example does not specify any providers.

 10. Specify the types that belong to the custom snap-in (optional).

      This example does not specify any types.

 11. Specify the formats that belong to the custom snap-in (optional).

      This example does not specify any formats.

Example
This example shows how to write a Custom Windows PowerShell snap-in that can be used to
register the Test-HelloWorld and Test-CustomSnapinTest cmdlets. Be aware that in this
example, the complete assembly could contain other cmdlets and providers that would not be
registered by this snap-in.

 C#

 [RunInstaller(true)]
 public class CustomPSSnapinTest : CustomPSSnapIn
 {
   /// <summary>
   /// Creates an instance of CustomPSSnapInTest class.
   /// </summary>
   public CustomPSSnapinTest()
           : base()
   {
   }

    /// <summary>
    /// Specify the name of the custom PowerShell snap-in.

<!-- p.1837 -->

  /// </summary>
  public override string Name
  {
    get
    {
      return "CustomPSSnapInTest";
    }
  }

  /// <summary>
  /// Specify the vendor for the custom PowerShell snap-in.
  /// </summary>
  public override string Vendor
  {
    get
    {
      return "Microsoft";
    }
  }

  /// <summary>
  /// Specify the localization resource information for the vendor.
  /// Use the format: resourceBaseName,resourceName.
  /// </summary>
  public override string VendorResource
  {
    get
    {
        return "CustomPSSnapInTest,Microsoft";
    }
  }

  /// <summary>
  /// Specify a description of the custom PowerShell snap-in.
  /// </summary>
  public override string Description
  {
    get
    {
      return "This is a custom PowerShell snap-in that includes the Test-HelloWorld
and Test-CustomSnapinTest cmdlets.";
    }
  }

  /// <summary>
  /// Specify the localization resource information for the description.
  /// Use the format: resourceBaseName,Description.
  /// </summary>
  public override string DescriptionResource
  {
    get
    {
        return "CustomPSSnapInTest,This is a custom PowerShell snap-in that
includes the Test-HelloWorld and Test-CustomSnapinTest cmdlets.";
    }

<!-- p.1838 -->

  }

  /// <summary>
  /// Specify the cmdlets that belong to this custom PowerShell snap-in.
  /// </summary>
  private Collection<CmdletConfigurationEntry> _cmdlets;
  public override Collection<CmdletConfigurationEntry> Cmdlets
  {
    get
    {
      if (_cmdlets == null)
      {
        _cmdlets = new Collection<CmdletConfigurationEntry>();
        _cmdlets.Add(new CmdletConfigurationEntry("test-customsnapintest",
typeof(TestCustomSnapinTest), "TestCmdletHelp.dll-help.xml"));
        _cmdlets.Add(new CmdletConfigurationEntry("test-helloworld",
typeof(TestHelloWorld), "HelloWorldHelp.dll-help.xml"));
      }

          return _cmdlets;
      }
  }

  /// <summary>
  /// Specify the providers that belong to this custom PowerShell snap-in.
  /// </summary>
  private Collection<ProviderConfigurationEntry> _providers;
  public override Collection<ProviderConfigurationEntry> Providers
  {
    get
    {
      if (_providers == null)
      {
        _providers = new Collection<ProviderConfigurationEntry>();
      }

          return _providers;
      }
  }

  /// <summary>
  /// Specify the types that belong to this custom PowerShell snap-in.
  /// </summary>
  private Collection<TypeConfigurationEntry> _types;
  public override Collection<TypeConfigurationEntry> Types
  {
    get
    {
      if (_types == null)
      {
        _types = new Collection<TypeConfigurationEntry>();
      }

          return _types;
      }

<!-- p.1839 -->

     }

     /// <summary>
     /// Specify the formats that belong to this custom PowerShell snap-in.
     /// </summary>
     private Collection<FormatConfigurationEntry> _formats;
     public override Collection<FormatConfigurationEntry> Formats
     {
       get
       {
         if (_formats == null)
         {
           _formats = new Collection<FormatConfigurationEntry>();
         }

             return _formats;
         }
     }
 }

For more information about registering snap-ins, see How to Register Cmdlets, Providers, and
Host Applications in the Windows PowerShell Programmer's Guide.

See Also
How to Register Cmdlets, Providers, and Host Applications

Windows PowerShell Shell SDK

Last updated on 11/20/2025

<!-- p.1840 -->

Importing a PowerShell Module
Once you have installed a module on a system, you will likely want to import the module.
Importing is the process that loads the module into active memory, so that a user can access
that module in their PowerShell session. In PowerShell 2.0, you can import a newly-installed
PowerShell module with a call to Import-Module cmdlet. In PowerShell 3.0, PowerShell is able
to implicitly import a module when one of the functions or cmdlets in the module is called by a
user. Note that both versions assume that you install your module in a location where
PowerShell is able to find it; for more information, see Installing a PowerShell Module. You can
use a module manifest to restrict what parts of your module are exported, and you can use
parameters of the Import-Module call to restrict what parts are imported.

Importing a Snap-In (PowerShell 1.0)
Modules did not exist in PowerShell 1.0: instead, you had to register and use snap-ins.
However, it is not recommended that you use this technology at this point, as modules are
generally easier to install and import. For more information, see How to Create a Windows
PowerShell Snap-in.

Importing a Module with Import-Module
(PowerShell 2.0)
PowerShell 2.0 uses the appropriately-named Import-Module cmdlet to import modules. When
this cmdlet is run, Windows PowerShell searches for the specified module within the directories
specified in the PSModulePath variable. When the specified directory is found, Windows
PowerShell searches for files in the following order: module manifest files ( .psd1 ), script
module files ( .psm1 ), binary module files (.dll). For more information about adding directories
to the search, see about_PSModulePath. The following code describes how to import a module:

  PowerShell

  Import-Module myModule

Assuming that myModule was located in the PSModulePath , PowerShell would load myModule
into active memory. If myModule was not located on a PSModulePath path, you could still
explicitly tell PowerShell where to find it:
