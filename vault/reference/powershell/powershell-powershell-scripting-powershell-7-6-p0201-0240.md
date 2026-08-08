---
title: "How to use this documentation — pages 201-240"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0201-0240
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0201-0240
family: powershell
documentKind: "doc"
abstract: "You can still have a name conflict even when you add a prefix to the noun. I like to prefix my function nouns with my initials. Develop a standard and stick to it. PowerShell function Get-MrPSVersion { $PSVersionTable.PSVersion } This function is no different than the previous t"
---

# How to use this documentation — pages 201-240

<!-- p.201 -->

You can still have a name conflict even when you add a prefix to the noun. I like to prefix my
function nouns with my initials. Develop a standard and stick to it.

 PowerShell

 function Get-MrPSVersion {
     $PSVersionTable.PSVersion
 }

This function is no different than the previous two, except for using a more unique name to try
to prevent naming conflicts with other PowerShell commands.

 PowerShell

 Get-MrPSVersion

 Output

 Major    Minor   Build   Revision
 -----    -----   -----   --------
 5        1       14393   693

Once loaded into memory, you can see functions on the Function PSDrive.

 PowerShell

 Get-ChildItem -Path Function:\Get-*Version

 Output

 CommandType        Name                                                    Version
 -----------        ----                                                    -------
 Function           Get-Version
 Function           Get-PSVersion
 Function           Get-MrPSVersion

If you want to remove these functions from your current session, remove them from the
Function PSDrive or close and reopen PowerShell.

 PowerShell

 Get-ChildItem -Path Function:\Get-*Version | Remove-Item

Verify that the functions were indeed removed.

<!-- p.202 -->

 PowerShell

 Get-ChildItem -Path Function:\Get-*Version

If the functions were loaded as part of a module, you can unload the module to remove them.

 PowerShell

 Remove-Module -Name <ModuleName>

The Remove-Module cmdlet removes PowerShell modules from memory in your current
PowerShell session. It doesn't remove them from your system or disk.

Parameters
Don't statically assign values. Use parameters and variables instead. When naming your
parameters, use the same name as the default cmdlets for your parameter names whenever
possible.

In the following function, notice that I used ComputerName and not Computer, ServerName,
or Host for the parameter name. Using ComputerName standardizes the parameter name to
match the parameter name and case like the default cmdlets.

 PowerShell

 function Test-MrParameter {

      param (
          $ComputerName
      )

      Write-Output $ComputerName

 }

The following function queries all commands on your system and returns the number with
specific parameter names.

 PowerShell

 function Get-MrParameterCount {
     param (
         [string[]]$ParameterName
     )

<!-- p.203 -->

     foreach ($Parameter in $ParameterName) {
         $Results = Get-Command -ParameterName $Parameter -ErrorAction
 SilentlyContinue

           [pscustomobject]@{
               ParameterName   = $Parameter
               NumberOfCmdlets = $Results.Count
           }
      }
 }

As you can see in the following results, 39 commands that have a ComputerName parameter.
There aren't any commands with parameters such as Computer, ServerName, Host, or
Machine.

 PowerShell

 Get-MrParameterCount -ParameterName ComputerName, Computer, ServerName,
     Host, Machine

 Output

 ParameterName NumberOfCmdlets
 ------------- ---------------
 ComputerName               39
 Computer                    0
 ServerName                  0
 Host                        0
 Machine                     0

Use the same case for your parameter names as the default cmdlets. For example, use
ComputerName , not computername . This naming scheme helps people familiar with PowerShell

discover your functions and look and feel like the default cmdlets.

The param statement allows you to define one or more parameters. A comma ( , ) separates the
parameter definitions. For more information, see about_Functions_Advanced_Parameters.

Advanced functions
Turning a function into an advanced function in PowerShell is simple. One of the differences
between a function and an advanced function is that advanced functions have common
parameters that are automatically added. Common parameters include parameters such as
Verbose and Debug.

Start with the Test-MrParameter function that was used in the previous section.

<!-- p.204 -->

 PowerShell

 function Test-MrParameter {

      param (
          $ComputerName
      )

      Write-Output $ComputerName

 }

There are a couple of different ways to see the common parameters. One is by viewing the
syntax with Get-Command .

 PowerShell

 Get-Command -Name Test-MrParameter -Syntax

Notice the Test-MrParameter function doesn't have any common parameters.

 Output

 Test-MrParameter [[-ComputerName] <Object>]

Another is to drill down into the parameters property of Get-Command .

 PowerShell

 (Get-Command -Name Test-MrParameter).Parameters.Keys

 Output

 ComputerName

Add the CmdletBinding attribute to turn the function into an advanced function.

 PowerShell

 function Test-MrCmdletBinding {

      [CmdletBinding()] # Turns a regular function into an advanced function
      param (
          $ComputerName
      )

<!-- p.205 -->

      Write-Output $ComputerName

 }

When you specify CmdletBinding , the common parameters are added automatically.
CmdletBinding requires a param block, but the param block can be empty.

 PowerShell

 Get-Command -Name Test-MrCmdletBinding -Syntax

 Output

 Test-MrCmdletBinding [[-ComputerName] <Object>] [<CommonParameters>]

Drilling down into the parameters property of Get-Command shows the actual parameter names,
including the common ones.

 PowerShell

 (Get-Command -Name Test-MrCmdletBinding).Parameters.Keys

 Output

 ComputerName
 Verbose
 Debug
 ErrorAction
 WarningAction
 InformationAction
 ErrorVariable
 WarningVariable
 InformationVariable
 OutVariable
 OutBuffer
 PipelineVariable

SupportsShouldProcess
The SupportsShouldProcess attribute adds the WhatIf and Confirm risk mitigation parameters.
These parameters are only needed for commands that make changes.

 PowerShell

<!-- p.206 -->

 function Test-MrSupportsShouldProcess {

      [CmdletBinding(SupportsShouldProcess)]
      param (
          $ComputerName
      )

      Write-Output $ComputerName

 }

Notice that there are now WhatIf and Confirm parameters.

 PowerShell

 Get-Command -Name Test-MrSupportsShouldProcess -Syntax

 Output

 Test-MrSupportsShouldProcess [[-ComputerName] <Object>] [-WhatIf] [-Confirm]
 [<CommonParameters>]

Once again, you can also use Get-Command to return a list of the actual parameter names,
including the common, ones along with WhatIf and Confirm.

 PowerShell

 (Get-Command -Name Test-MrSupportsShouldProcess).Parameters.Keys

 Output

 ComputerName
 Verbose
 Debug
 ErrorAction
 WarningAction
 InformationAction
 ErrorVariable
 WarningVariable
 InformationVariable
 OutVariable
 OutBuffer
 PipelineVariable
 WhatIf
 Confirm

<!-- p.207 -->

Parameter validation
Validate input early on. Don't allow your code to continue on a path when it can't complete
without valid input.

Always specify a datatype for the variables used for parameters. In the following example,
String is specified as the datatype for the ComputerName parameter. This validation limits it to
only allow a single computer name to be specified for the ComputerName parameter.

 PowerShell

 function Test-MrParameterValidation {

      [CmdletBinding()]
      param (
          [string]$ComputerName
      )

      Write-Output $ComputerName

 }

An error is generated if more than one computer name is specified.

 PowerShell

 Test-MrParameterValidation -ComputerName Server01, Server02

 Output

 Test-MrParameterValidation : Cannot process argument transformation on
 parameter 'ComputerName'. Cannot convert value to type System.String.
 At line:1 char:42
 + Test-MrParameterValidation -ComputerName Server01, Server02
 +                                          ~~~~~~~~~~~~~~~~~~
     + CategoryInfo          : InvalidData: (:) [Test-MrParameterValidation]
    , ParameterBindingArgumentTransformationException
     + FullyQualifiedErrorId : ParameterArgumentTransformationError,Test-MrP
    arameterValidation

The problem with the current definition is that it's valid to omit the value of the
ComputerName parameter, but a value is required for the function to complete successfully.
This scenario is where the Mandatory parameter attribute is beneficial.

<!-- p.208 -->

The syntax used in the following example is compatible with PowerShell version 3.0 and higher.
[Parameter(Mandatory=$true)] could be specified to make the function compatible with

PowerShell version 2.0 or higher.

 PowerShell

 function Test-MrParameterValidation {

      [CmdletBinding()]
      param (
          [Parameter(Mandatory)]
          [string]$ComputerName
      )

      Write-Output $ComputerName

 }

Now that the ComputerName is required, if one isn't specified, the function prompts for one.

 PowerShell

 Test-MrParameterValidation

 Output

 cmdlet Test-MrParameterValidation at command pipeline position 1
 Supply values for the following parameters:
 ComputerName:

If you want to allow more than one value for the ComputerName parameter, use the String
datatype but add square brackets ( [] ) to the datatype to allow an array of strings.

 PowerShell

 function Test-MrParameterValidation {

      [CmdletBinding()]
      param (
          [Parameter(Mandatory)]
          [string[]]$ComputerName
      )

      Write-Output $ComputerName

 }

<!-- p.209 -->

Maybe you want to specify a default value for the ComputerName parameter if one isn't
specified. The problem is that default values can't be used with mandatory parameters. Instead,
use the ValidateNotNullOrEmpty parameter validation attribute with a default value.

Even when setting a default value, try not to use static values. In the following example,
$env:COMPUTERNAME is used as the default value, which is automatically translated to the local

computer name if a value isn't provided.

 PowerShell

 function Test-MrParameterValidation {

      [CmdletBinding()]
      param (
          [ValidateNotNullOrEmpty()]
          [string[]]$ComputerName = $env:COMPUTERNAME
      )

      Write-Output $ComputerName

 }

Verbose output
Inline comments are useful if you're writing complex code, but users don't see them unless
they look at the code.

The function in the following example has an inline comment in the foreach loop. While this
particular comment might not be difficult to locate, imagine if the function contained hundreds
of lines of code.

 PowerShell

 function Test-MrVerboseOutput {

      [CmdletBinding()]
      param (
          [ValidateNotNullOrEmpty()]
          [string[]]$ComputerName = $env:COMPUTERNAME
      )

      foreach ($Computer in $ComputerName) {
          #Attempting to perform an action on $Computer <<-- Don't use
          #inline comments like this, use write verbose instead.
          Write-Output $Computer
      }

<!-- p.210 -->

 }

A better option is to use Write-Verbose instead of inline comments.

 PowerShell

 function Test-MrVerboseOutput {

      [CmdletBinding()]
      param (
          [ValidateNotNullOrEmpty()]
          [string[]]$ComputerName = $env:COMPUTERNAME
      )

      foreach ($Computer in $ComputerName) {
          Write-Verbose -Message "Attempting to perform an action on $Computer"
          Write-Output $Computer
      }

 }

The verbose output isn't displayed when the function is called without the Verbose parameter.

 PowerShell

 Test-MrVerboseOutput -ComputerName Server01, Server02

The verbose output is displayed when the function is called with the Verbose parameter.

 PowerShell

 Test-MrVerboseOutput -ComputerName Server01, Server02 -Verbose

Pipeline input
Extra code is necessary when you want your function to accept pipeline input. As mentioned
earlier in this book, commands can accept pipeline input by value (by type) or by property
name. You can write your functions like the native commands so they accept either one or both
of these input types.

To accept pipeline input by value, specify the ValueFromPipeline parameter attribute for that
particular parameter. You can only accept pipeline input by value from one parameter of each
datatype. If you have two parameters that accept string input, only one of them can accept
pipeline input by value. If you specified by value for both of the string parameters, the input

<!-- p.211 -->

wouldn't know which parameter to bind to. This scenario is another reason I call this type of
pipeline input by type instead of by value.

Pipeline input is received one item at a time, similar to how items are handled in a foreach
loop. A process block is required to process each item if your function accepts an array as
input. If your function only accepts a single value as input, a process block isn't necessary but
is recommended for consistency.

 PowerShell

 function Test-MrPipelineInput {

      [CmdletBinding()]
      param (
          [Parameter(Mandatory,
                     ValueFromPipeline)]
          [string[]]$ComputerName
      )

      process {
          Write-Output $ComputerName
      }

 }

Accepting pipeline input by property name is similar, except you specify it with the
ValueFromPipelineByPropertyName parameter attribute, and it can be specified for any number

of parameters regardless of datatype. The key is the output of the command being piped in
must have a property name that matches the name of the parameter or a parameter alias of
your function.

 PowerShell

 function Test-MrPipelineInput {

      [CmdletBinding()]
      param (
          [Parameter(Mandatory,
                     ValueFromPipelineByPropertyName)]
          [string[]]$ComputerName
      )

      process {
              Write-Output $ComputerName
      }

 }

<!-- p.212 -->

begin and end blocks are optional. begin is specified before the process block and is used to

perform any initial work before the items are received from the pipeline. Values that are piped
in aren't accessible in the begin block. The end block is specified after the process block and is
used for cleanup after all items piped in are processed.

Error handling
The function shown in the following example generates an unhandled exception when a
computer can't be contacted.

 PowerShell

 function Test-MrErrorHandling {

      [CmdletBinding()]
      param (
          [Parameter(Mandatory,
                     ValueFromPipeline,
                     ValueFromPipelineByPropertyName)]
          [string[]]$ComputerName
      )

      process {
          foreach ($Computer in $ComputerName) {
              Test-WSMan -ComputerName $Computer
          }
      }

 }

There are a couple of different ways to handle errors in PowerShell. Try/Catch is the more
modern way to handle errors.

 PowerShell

 function Test-MrErrorHandling {

      [CmdletBinding()]
      param (
          [Parameter(Mandatory,
                     ValueFromPipeline,
                     ValueFromPipelineByPropertyName)]
          [string[]]$ComputerName
      )

      process {
          foreach ($Computer in $ComputerName) {
              try {

<!-- p.213 -->

                    Test-WSMan -ComputerName $Computer
               }
               catch {
                   Write-Warning -Message "Unable to connect to Computer: $Computer"
               }
          }
      }

 }

Although the function shown in the previous example uses error handling, it generates an
unhandled exception because the command doesn't generate a terminating error. Only
terminating errors are caught. Specify the ErrorAction parameter with Stop as its value to turn
a nonterminating error into a terminating one.

 PowerShell

 function Test-MrErrorHandling {

      [CmdletBinding()]
      param (
          [Parameter(Mandatory,
                     ValueFromPipeline,
                     ValueFromPipelineByPropertyName)]
          [string[]]$ComputerName
      )

      process {
          foreach ($Computer in $ComputerName) {
              try {
                  Test-WSMan -ComputerName $Computer -ErrorAction Stop
              }
              catch {
                  Write-Warning -Message "Unable to connect to Computer: $Computer"
              }
          }
      }

 }

Don't modify the global $ErrorActionPreference variable unless absolutely necessary. If you
change it in a local scope, it reverts to the previous value when you exit that scope.

If you're using something like .NET directly from within your PowerShell function, you can't
specify the ErrorAction parameter on the command itself. You can change the
$ErrorActionPreference variable just before you call the .NET method.

Comment-based help

<!-- p.214 -->

Adding help to your functions is considered a best practice. Help allows people you share them
with to know how to use them.

 PowerShell

 function Get-MrAutoStoppedService {

 <#
 .SYNOPSIS
     Returns a list of services that are set to start automatically, are not
     currently running, excluding the services that are set to delayed start.

 .DESCRIPTION
     Get-MrAutoStoppedService is a function that returns a list of services
     from the specified remote computer(s) that are set to start
     automatically, are not currently running, and it excludes the services
     that are set to start automatically with a delayed startup.

 .PARAMETER ComputerName
     The remote computer(s) to check the status of the services on.

 .PARAMETER Credential
     Specifies a user account that has permission to perform this action. The
     default is the current user.

 .EXAMPLE
      Get-MrAutoStoppedService -ComputerName 'Server1', 'Server2'

 .EXAMPLE
      'Server1', 'Server2' | Get-MrAutoStoppedService

 .EXAMPLE
      Get-MrAutoStoppedService -ComputerName 'Server1' -Credential (Get-Credential)

 .INPUTS
     String

 .OUTPUTS
     PSCustomObject

 .NOTES
     Author: Mike F. Robbins
     Website: https://mikefrobbins.com
     Twitter: @mikefrobbins
 #>

      [CmdletBinding()]
      param (

      )

      #Function Body

<!-- p.215 -->

 }

When you add comment-based help to your functions, help can be retrieved for them like the
default built-in commands.

All the syntax for writing a function in PowerShell can seem overwhelming for someone getting
started. If you can't remember the syntax for something, open a second instance of the
PowerShell Integrated Scripting Environment (ISE) on a separate monitor and view the "Cmdlet
(advanced function) - Complete" snippet while typing in the code for your functions. Snippets
can be accessed in the PowerShell ISE using the Ctrl + J key combination.

Summary
In this chapter, you learned the basics of writing functions in PowerShell, including how to:

       Create advanced functions
       Use parameter validation
       Use verbose output
       Support pipeline input
       Handle errors
       Create comment-based help

Review
     1. How do you obtain a list of approved verbs in PowerShell?
     2. How do you turn a PowerShell function into an advanced function?
     3. When should WhatIf and Confirm parameters be added to your PowerShell functions?
     4. How do you turn a nonterminating error into a terminating one?
     5. Why should you add comment-based help to your functions?

References
       about_Functions
       about_Functions_Advanced_Parameters
       about_CommonParameters
       about_Functions_CmdletBindingAttribute
       about_Functions_Advanced
       about_Try_Catch_Finally

<!-- p.216 -->

     about_Comment_Based_Help
     Video: PowerShell Toolmaking with Advanced Functions and Script Modules

Next steps
In Chapter 10, you'll learn how to package functions into script modules. You'll explore module
structure, manifests, exporting public commands, and best practices for organizing, sharing,
and maintaining reusable PowerShell tooling.

Last updated on 02/06/2026

<!-- p.217 -->

Chapter 10 - Script modules
If you find yourself using the same PowerShell one-liners or scripts often, turning them into
reusable tools is even more important. Packaging your functions in a script module gives them
a more professional feel and makes them easier to support and share with others.

Dot-sourcing functions
One thing we didn't cover in the previous chapter is dot-sourcing functions. When you define a
function in a script but not part of a module, the only way to load it into memory is by dot-
sourcing its .ps1 file.

For example, save the following function in a file named Get-MrPSVersion.ps1 .

 PowerShell

 function Get-MrPSVersion {
     $PSVersionTable
 }

When you run the script, it appears that nothing happens.

 PowerShell

 .\Get-MrPSVersion.ps1

Attempting to call the function results in an error because it isn't loaded into memory.

 PowerShell

 Get-MrPSVersion

 Output

 Get-MrPSVersion : The term 'Get-MrPSVersion' is not recognized as the name
 of a cmdlet, function, script file, or operable program. Check the spelling
 of the name, or if a path was included, verify that the path is correct and
 try again.
 At line:1 char:1
 + Get-MrPSVersion
 + ~~~~~~~~~~~~~~~
     + CategoryInfo          : ObjectNotFound: (Get-MrPSVersion:String) [],

<!-- p.218 -->

     CommandNotFoundException
      + FullyQualifiedErrorId : CommandNotFoundException

You can confirm whether functions are loaded into memory by verifying their existence on the
Function: PSDrive.

 PowerShell

 Get-ChildItem -Path Function:\Get-MrPSVersion

 Output

 Get-ChildItem : Cannot find path 'Get-MrPSVersion' because it does not
 exist.
 At line:1 char:1
 + Get-ChildItem -Path Function:\Get-MrPSVersion
 + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     + CategoryInfo          : ObjectNotFound: (Get-MrPSVersion:String) [Get
    -ChildItem], ItemNotFoundException
     + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.Ge
    tChildItemCommand

The issue with running the script that defines the function is that it loads it into the Script
scope. Once the script finishes executing, PowerShell discards that scope along with the
function.

To keep the function available after the script runs, it needs to be loaded into the Global scope.
You can accomplish this by dot-sourcing the script file. You can use a relative path for this
purpose.

 PowerShell

 . .\Get-MrPSVersion.ps1

You can also use the full path to the script when dot-sourcing it.

 PowerShell

 . C:\Demo\Get-MrPSVersion.ps1

If part of the path is stored in a variable, you can combine it with the rest of the path. There's
no need to use string concatenation to do this.

 PowerShell

<!-- p.219 -->

  $Path = 'C:\'
  . $Path\Get-MrPSVersion.ps1

Now, if you check the Function PSDrive, you see the Get-MrPSVersion function is available.

  PowerShell

  Get-ChildItem -Path Function:\Get-MrPSVersion

  Output

  CommandType         Name                                                   Version
  -----------         ----                                                   -------
  Function            Get-MrPSVersion

Script modules
In PowerShell, a script module is simply a .psm1 file that contains one or more functions, just
like a regular script, but with a different file extension.

How do you create a script module? You might assume with a command named something like
New-Module . That assumption is a reasonable guess, but that command actually creates a

dynamic module, not a script module.

This scenario is a good reminder to always read the help documentation, even when a
command name looks exactly like what you need.

  PowerShell

  help New-Module

  Output

  NAME
         New-Module

  SYNOPSIS
      Creates a new dynamic module that exists only in memory.

  SYNTAX
      New-Module [-Name] <System.String> [-ScriptBlock]
      <System.Management.Automation.ScriptBlock> [-ArgumentList
      <System.Object[]>] [-AsCustomObject] [-Cmdlet <System.String[]>]
      [-Function <System.String[]>] [-ReturnResult] [<CommonParameters>]

<!-- p.220 -->

 DESCRIPTION
     The `New-Module` cmdlet creates a dynamic module from a script block.
     The members of the dynamic module, such as functions and variables, are
     immediately available in the session and remain available until you
     close the session.

     Like static modules, by default, the cmdlets and functions in a dynamic
     module are exported and the variables and aliases are not. However, you
     can use the Export-ModuleMember cmdlet and the parameters of
     `New-Module` to override the defaults.

     You can also use the **AsCustomObject** parameter of `New-Module` to return
     the dynamic module as a custom object. The members of the modules, such
     as functions, are implemented as script methods of the custom object
     instead of being imported into the session.

     Dynamic modules exist only in memory, not on disk. Like all modules,
     the members of dynamic modules run in a private module scope that is a
     child of the global scope. Get-Module cannot get a dynamic module, but
     Get-Command can get the exported members.

     To make a dynamic module available to `Get-Module`, pipe a `New-Module`
     command to Import-Module, or pipe the module object that `New-Module`
     returns to `Import-Module`. This action adds the dynamic module to the
     `Get-Module` list, but it does not save the module to disk or make it
     persistent.

 RELATED LINKS
     Online Version: https://learn.microsoft.com/powershell/module/microsoft.
     powershell.core/new-module?view=powershell-5.1&WT.mc_id=ps-gethelp
     Export-ModuleMember
     Get-Module
     Import-Module
     Remove-Module
     about_Modules

 REMARKS
     To see the examples, type: "Get-Help New-Module -Examples".
     For more information, type: "Get-Help New-Module -Detailed".
     For technical information, type: "Get-Help New-Module -Full".
     For online help, type: "Get-Help New-Module -Online"

The previous chapter mentioned that functions should use approved verbs. Otherwise,
PowerShell generates a warning when the module is imported.

The following example uses the New-Module cmdlet to create a dynamic module in memory,
specifically to demonstrate what happens when you don't use an approved verb.

 PowerShell

<!-- p.221 -->

 New-Module -Name MyModule -ScriptBlock {

      function Return-MrOsVersion {
          Get-CimInstance -ClassName Win32_OperatingSystem |
          Select-Object -Property @{Label='OperatingSystem';Expression={$_.Caption}}
      }

      Export-ModuleMember -Function Return-MrOsVersion

 } | Import-Module

 Output

 WARNING: The names of some imported commands from the module 'MyModule' include
 unapproved verbs that might make them less discoverable. To find the commands with
 unapproved verbs, run the Import-Module command again with the Verbose parameter.
 For a
 list of approved verbs, type Get-Verb.

Although you used the New-Module cmdlet in the previous example, as mentioned before, it's
not the command for creating script modules in PowerShell.

To create a script module, save your functions in a .psm1 file. For example, save the following
two functions in a file named MyScriptModule.psm1 .

 PowerShell

 function Get-MrPSVersion {
     $PSVersionTable
 }

 function Get-MrComputerName {
     $env:COMPUTERNAME
 }

Try to run one of the functions.

 PowerShell

 Get-MrComputerName

When you call the function, you receive an error saying PowerShell can't find it. Like before,
checking the Function: PSDrive confirms that it isn't loaded into memory.

 Output

<!-- p.222 -->

 Get-MrComputerName : The term 'Get-MrComputerName' is not recognized as the
 name of a cmdlet, function, script file, or operable program. Check the
 spelling of the name, or if a path was included, verify that the path is
 correct and try again.
 At line:1 char:1
 + Get-MrComputerName
 + ~~~~~~~~~~~~~~~~~~
     + CategoryInfo          : ObjectNotFound: (Get-MrComputerName:String) [
    ], CommandNotFoundException
     + FullyQualifiedErrorId : CommandNotFoundException

To make the function available, you can manually import the MyScriptModule.psm1 file using the
Import-Module cmdlet.

 PowerShell

 Import-Module C:\MyScriptModule.psm1

PowerShell introduced module autoloading in version 3. To take advantage of this feature, the
script module must be saved in a folder with the same base name as the .psm1 file. That folder
must be located in one of the directories specified in the $env:PSModulePath environment
variable.

 PowerShell

 $env:PSModulePath

The output of $env:PSModulePath is difficult to read.

 Output

 C:\Users\mike-ladm\Documents\WindowsPowerShell\Modules;C:\Program Files\Wind
 owsPowerShell\Modules;C:\Windows\system32\WindowsPowerShell\v1.0\Modules;C:\
 Program Files (x86)\Microsoft SQL Server\130\Tools\PowerShell\Modules\

To make the results more readable, split the paths on the semicolon path separator so each
one appears on its own line.

 PowerShell

 $env:PSModulePath -split ';'

The first three paths in the list are the default module locations. SQL Server Management
Studio added the last path when you installed it.

<!-- p.223 -->

 Output

 C:\Users\mike-ladm\Documents\WindowsPowerShell\Modules
 C:\Program Files\WindowsPowerShell\Modules
 C:\Windows\system32\WindowsPowerShell\v1.0\Modules
 C:\Program Files (x86)\Microsoft SQL Server\130\Tools\PowerShell\Modules\

For module autoloading to work, you must place the MyScriptModule.psm1 file must in a folder
named MyScriptModule , and that folder must reside directly inside one of the paths listed in
$env:PSModulePath .

Not all those paths are equally useful. For example, the current user path on my system isn't
the first one in the list. That's because I sign in to Windows with a different account than the
one I use to run PowerShell. So, it doesn't point to my user's documents folder.

The second path is the AllUsers path, which is where I store all of my modules.

The third path points to C:\Windows\System32 , a protected system location. Only Microsoft
should be placing modules there, as it falls under the operating system's directory structure.

Once you place the .psm1 file in an appropriate folder within one of these paths, PowerShell
automatically loads the module the first time you call one of its commands.

Module manifests
Every module should include a module manifest, which is a .psd1 file containing metadata
about the module. While the .psd1 extension is used for manifests, not all .psd1 files are
module manifests. You can also use them for other purposes, such as defining environment
data in a DSC
configuration.

You can create a module manifest using the New-ModuleManifest cmdlet. The only required
parameter is Path, but for the module to work correctly, you must also specify the RootModule
parameter.

It's a best practice to include values like Author and Description, especially if you plan to
publish your module to a NuGet repository using PowerShellGet. These fields are required in
that scenario.

One quick way to tell if a module lacks a manifest is to check its version.

 PowerShell

<!-- p.224 -->

 Get-Module -Name MyScriptModule

A version number of 0.0 is a clear sign that the module lacks a manifest.

 Output

 ModuleType Version       Name                                     ExportedCommands
 ---------- -------       ----                                     ----------------
 Script     0.0           MyScriptModule                           {Get-MrComputer...

You should include all recommended details when creating a module manifest to ensure your
module is well-documented and ready for sharing or publishing.

 PowerShell

 $moduleManifestParams = @{
     Path =
 "$env:ProgramFiles\WindowsPowerShell\Modules\MyScriptModule\MyScriptModule.psd1"
     RootModule = 'MyScriptModule'
     Author = 'Mike F. Robbins'
     Description = 'MyScriptModule'
     CompanyName = 'mikefrobbins.com'
 }

 New-ModuleManifest @moduleManifestParams

If you omit any values when initially creating the module manifest, you can add or update it
later using the Update-ModuleManifest cmdlet. Avoid recreating the manifest with New-
ModuleManifest once you create it, as doing so generates a new GUID.

Defining public and private functions
Sometimes, your module might include helper functions you don't want to expose to users.
These private functions are used internally by other functions in the module but aren't exposed
to users. There are a few ways to handle this scenario.

If you're not following best practices and only have a .psm1 file without a module manifest,
your only option is to control visibility using the Export-ModuleMember cmdlet. This option lets
you explicitly define which functions should be exposed directly from within the .psm1 script
module file, keeping everything else private by default.

In the following example, only the Get-MrPSVersion function is exposed to users of your
module, while the Get-MrComputerName function remains accessible internally to other functions

<!-- p.225 -->

within the module.

 PowerShell

 function Get-MrPSVersion {
     $PSVersionTable
 }

 function Get-MrComputerName {
     $env:COMPUTERNAME
 }

 Export-ModuleMember -Function Get-MrPSVersion

Determine what commands are available publicly in the MyScriptModule module.

 PowerShell

 Get-Command -Module MyScriptModule

 Output

 CommandType         Name                                                     Version
 -----------         ----                                                     -------
 Function            Get-MrPSVersion                                          1.0

If you add a module manifest to your module, it's a best practice to explicitly list the functions
you want to export in the FunctionsToExport section. This option gives you control over what
you expose to users from the .psd1 module manifest file.

 PowerShell

 FunctionsToExport = 'Get-MrPSVersion'

You don't need to use both Export-ModuleMember in the .psm1 file and the FunctionsToExport
section in the module manifest. Either approach is enough on its own.

Summary
In this chapter, you learned how to turn your functions into a script module in PowerShell. You
also explored best practices for creating script modules, including the importance of adding a
module manifest to define metadata and manage exported commands.

<!-- p.226 -->

Review
  1. How do you create a script module in PowerShell?
  2. Why is it important to use approved verbs for your function names?
  3. How do you create a module manifest in PowerShell?
  4. What are the two ways to export only specific functions from a module?
  5. What conditions must be met for a module to autoload when you run one of its
     commands?

References
     How to Create PowerShell Script Modules and Module Manifests
     about_Modules
     New-ModuleManifest
     Export-ModuleMember

Last updated on 11/06/2025

<!-- p.227 -->

Appendix - Answers to Review Questions
This appendix provides concise answers to the review questions found at the end of each
chapter. Use it to validate your understanding and reinforce key concepts.

Chapter 1 - Getting started with PowerShell
   1. Use the $PSVersionTable automatic variable.
   2. Only when you need to bypass User Account Control (UAC) for tasks that require elevation
     on the local computer.
   3. The default execution policy on Windows client systems is Restricted , which prevents
     running scripts.
   4. Use Get-ExecutionPolicy to determine the current execution policy.
   5. Use Set-ExecutionPolicy (for example, Set-ExecutionPolicy -ExecutionPolicy
     RemoteSigned ).

Chapter 2 - The Help system
   1. No. The DisplayName parameter of Get-Service is named, not positional.
   2. Get-Process has six parameter sets.
   3. Use Get-Command -Noun EventLog .
   4. Use Get-Process -Name powershell .
   5. Run Update-Help (elevated as an administrator in Windows PowerShell) to download and
     install the latest help content.

Chapter 3 - Discovering objects, properties,
and methods
   1. Get-Process produces a System.Diagnostics.Process object.
   2. Pipe the command to Get-Member .
   3. Check whether the object has a method that performs the action.
   4. Use the command's PassThru parameter, if it has one.
   5. Run the command once and store the results in a variable to avoid repeatedly generating
     large amounts of output while prototyping.

Chapter 4 - One-Liners and the pipeline

<!-- p.228 -->

 1. A PowerShell one-liner is a single continuous pipeline, regardless of how many physical
   lines it spans.
 2. Natural line breaks can occur at characters such as the pipe ( | ), comma ( , ), opening
   brackets ( [ ] ), braces ( { } ), and parentheses ( ( ) ).
 3. You should filter left to improve performance and efficiency by reducing the amount of data
   passed through the pipeline.
 4. A command can accept pipeline input by value (by type) or by property name.
 5. Because most content in the PowerShell Gallery is community-contributed and may not be
   vetted, it should be reviewed and tested before use.

Chapter 5 - Formatting, aliases, providers, comparison
 1. Because formatting cmdlets produce format objects, which break the pipeline and can't be
   used by most other commands.
 2. Use Get-Alias -Name % to determine the actual cmdlet.
 3. Because aliases reduce readability and portability, making scripts more difficult for others to
   understand.
 4. Use Get-ChildItem -Path HKLM:\, HKCU:\ to list registry keys in both hives.
 5. The -replace operator is case-insensitive by default, whereas the .Replace() method is
   case-sensitive.

Chapter 6 - Flow control
 1. ForEach-Object processes items one at a time from the pipeline (streaming), while the
   foreach statement processes items from a collection that's already loaded into memory.

 2. A while loop evaluates its condition before running, so it may not run at all if the condition
   is false, unlike do while and do until , which run at least once.
 3. break exits the loop entirely, while continue skips the current iteration and proceeds to the
   next one.

Chapter 7 - Working with WMI
 1. WMI cmdlets (for example, Get-WmiObject ) are older and use DCOM, while CIM cmdlets (for
   example, Get-CimInstance ) are newer and use WSMan by default.
 2. WSMan (Windows Remote Management).
 3. CIM sessions allow reuse of connections, support alternate credentials, improve
   performance, and simplify managing multiple remote connections.

<!-- p.229 -->

 4. Create a session option with New-CimSessionOption , for example, to use DCOM, and pass it
   to New-CimSession , then use that session with Get-CimInstance .
 5. Use Remove-CimSession .

Chapter 8 - PowerShell remoting
 1. Use Enable-PSRemoting .
 2. Use Enter-PSSession .
 3. It allows you to use a persistent session instead of specifying the computer name and
   credentials with each command.
 4. Yes, you can use a PowerShell session (PSSession) in a one-to-one interactive remoting
   scenario.
 5. Locally run cmdlets return live objects with methods, while remote commands return
   deserialized objects without methods.

Chapter 9 - Functions
 1. Use Get-Verb .
 2. Add the [CmdletBinding()] attribute to the function.
 3. When the function makes changes to system state or performs potentially impactful actions.
 4. Specify -ErrorAction Stop .
 5. To document how to use the function so you and others can easily understand it and access
   help with Get-Help .

Chapter 10 - Script modules
 1. Create a .psm1 file and place your functions in it.
 2. Using approved verbs ensures consistency, avoids warnings, and improves discoverability.
 3. Use New-ModuleManifest .
 4. Use Export-ModuleMember in the .psm1 file or specify functions in the FunctionsToExport
   field of the .psd1 file.
 5. The module must be in a folder named the same as the module, located in a path listed in
   $env:PSModulePath , and contain the appropriate module file ( .psm1 or manifest).

Final Notes
   These answers are intentionally concise to reinforce key concepts.
   Revisit the chapters for deeper understanding.

<!-- p.230 -->

Last updated on 05/04/2026

<!-- p.231 -->

Optimizing your shell experience
PowerShell is a command-line shell and a scripting language used for automation.

Wikipedia      includes the following description of a shell:

  A shell manages the user-system interaction by prompting users for input, interpreting
  their input, and then handling output from the underlying operating system (much like a
  read-eval-print loop or REPL      ).

Similar to other shells like bash or cmd.exe , PowerShell allows you to run any command
available on your system, not just PowerShell commands.

PowerShell commands are known as cmdlets (pronounced command-lets). Cmdlets are
PowerShell commands, not stand-alone executables. PowerShell commands can't be run in
other shells without running PowerShell first.

Features of the PowerShell command-line interface
PowerShell is a modern command shell that includes the best features of other popular shells.
Unlike most shells that only accept and return text, PowerShell accepts and returns .NET
objects. The shell has several features that you can use to optimize your interactive user
experience.

      Robust command-line history
      Tab completion and command prediction
      Supports command and parameter aliases
      Pipeline for chaining commands
      In-console help system, similar to Unix man pages

 Last updated on 11/21/2025

<!-- p.232 -->

Running commands in the shell
PowerShell is a command-line shell and a scripting language used for automation. Similar to
other shells, like bash on Linux or the Windows Command Shell ( cmd.exe ), PowerShell lets you
run any command available on your system, not just PowerShell commands.

Types of commands
For any shell in any operating system there are three types of commands:

     Shell language keywords are part of the shell's scripting language.
        Examples of bash keywords include: if , then , else , elif , and fi .
        Examples of cmd.exe keywords include: dir , copy , move , if , and echo .
        Examples of PowerShell keywords include: for , foreach , try , catch , and trap .

     Shell language keywords can only be used within the runtime environment of the shell.
     There's no executable file, external to the shell, that provides the keyword's functionality.

     OS-native commands are executable files installed in the operating system. The executables
     can be run from any command-line shell, like PowerShell. This includes script files that
     require other shells to work properly. For example, if you run a Windows batch script ( .cmd
     file) in PowerShell, PowerShell runs cmd.exe and passes in the batch file for execution.

     Shell environment-specific commands are commands defined in external files that can only
     be used within the runtime environment of the shell. This include scripts, functions, and
     modules that add commands to the shell runtime. In PowerShell, these commands added by
     a module are known as cmdlets (pronounced "command-lets").

Running native commands
Any native command can be run from the PowerShell command line. Usually you run the
command exactly as you would in bash or cmd.exe . The following example shows running the
grep command in bash on Ubuntu Linux.

 Bash

 sdwheeler@circumflex:~$ grep sdwheeler /etc/passwd
 sdwheeler:x:1000:1000:,,,:/home/sdwheeler:/bin/bash
 sdwheeler@circumflex:~$ pwsh
 PowerShell 7.2.6

<!-- p.233 -->

 Copyright (c) Microsoft Corporation.

 https://aka.ms/powershell
 Type 'help' to get help.

After starting PowerShell on Ubuntu, you can run the same command from the PowerShell
command line:

 PowerShell

 PS /home/sdwheeler> grep sdwheeler /etc/passwd
 sdwheeler:x:1000:1000:,,,:/home/sdwheeler:/bin/bash

Passing arguments to native commands
Most shells include features for using variables, evaluating expressions, and handling strings. But
each shell does these things differently. In PowerShell, all parameters start with a hyphen ( - )
character. In cmd.exe , most command parameters use a forward slash ( / ) character. Other
command-line tools might use spaces, hyphens, double-dash ( -- ).

Each shell has its own way of handling and evaluating strings on the command line. When
running native commands in PowerShell that expect strings to be quoted in a specific way, you
might need to adjust how you pass those strings.

For more information, see the following articles:

     about_Parsing
     about_Quoting_Rules

PowerShell 7.2 introduced the experimental feature PSNativeCommandArgumentPassing that
improved native command handling. PowerShell 7.3 made this feature mainstream. For more
information, see $PSNativeCommandArgumentPassing.

Handling output and errors
PowerShell also has several more output streams than other shells. The bash and cmd.exe shells
have stdout and stderr. PowerShell has six output streams. For more information, see
about_Redirection and about_Output_Streams.

In general, the output sent to stdout by a native command is sent to the Success stream in
PowerShell. Output sent to stderr by a native command is sent to the Error stream in PowerShell.

<!-- p.234 -->

When a native command has a nonzero exit code, $? is set to $false . If the exit code is zero, $?
is set to $true .

However, PowerShell 7.2 changed this behavior. Error records redirected from native commands,
like when using redirection operators ( 2>&1 ), aren't written to PowerShell's $Error variable and
the preference variable $ErrorActionPreference doesn't affect the redirected output.

Many native commands write to stderr as an alternative stream for additional information. This
behavior can cause confusion in PowerShell when looking through errors and the additional
output information can be lost if $ErrorActionPreference is set to a state that mutes the output.

PowerShell 7.3 added a new experimental feature PSNativeCommandErrorActionPreference that
allows you to control how you handle non-zero exit codes from native commands. For more
information, see $PSNativeCommandUseErrorActionPreference.

Running PowerShell commands
As previously noted, PowerShell commands are known as cmdlets. Cmdlets are collected into
PowerShell modules that can be loaded on demand. Cmdlets can be written in any compiled .NET
language or using the PowerShell scripting language itself.

PowerShell commands that run other commands
The PowerShell call operator ( & ) lets you run commands that are stored in variables and
represented by strings or script blocks. You can use the operator to run any native command or
PowerShell command. This is useful in a script when you need to dynamically construct the
command-line parameters for a native command. For more information, see the call operator.

The Start-Process cmdlet can be used to run native commands, but should only be used when
you need to control how the command is executed. The cmdlet has parameters to support the
following scenarios:

      Run a command using different credentials
      Hide the console window created by the new process
      Redirect stdin, stdout, and stderr streams
      Use a different working directory for the command

The following example runs the native command sort.exe with redirected input and output
streams.

<!-- p.235 -->

  PowerShell

  $processOptions = @{
      FilePath = "sort.exe"
      RedirectStandardInput = "TestSort.txt"
      RedirectStandardOutput = "Sorted.txt"
      RedirectStandardError = "SortError.txt"
      UseNewEnvironment = $true
  }
  Start-Process @processOptions

For more information, see Start-Process.

On Windows, the Invoke-Item cmdlet performs the default action for the specified item. For
example, it runs an executable file or opens a document file using the application associated with
the document file type. The default action depends on the type of item and the PowerShell
provider that provides access to the item.

The following example opens the PowerShell source code repository in your default web browser.

  PowerShell

  Invoke-Item https://github.com/PowerShell/PowerShell

For more information, see Invoke-Item.

 Last updated on 06/29/2026

<!-- p.236 -->

Using tab-completion in the shell
ﾃ     Summarize this article for me

PowerShell provides completions on input to provide hints, enable discovery, and speed up
input entry. Command names, parameter names, argument values, and file paths can all be
completed by pressing the Tab key.

The Tab key is the default key binding on Windows. PSReadLine also provides a MenuComplete
function bound to Ctrl + Space . The MenuComplete function displays a list of matching
completions below the command line.

The keybindings can be changed using PSReadLine cmdlets or the application that's hosting
PowerShell. Keybindings can be different on non-Windows platforms. For more information,
see about_PSReadLine_Functions.

Built-in tab completion features
PowerShell enables tab completion for many aspects of the command line experience.

Filename completion
To fill in a filename or path from the available choices automatically, type part of the name and
press the Tab key. PowerShell automatically expands the name to the first match that it finds.
Pressing the Tab key again cycles through all the available choices with each key press.

Command and parameter name completion
The tab expansion of cmdlet names is slightly different. To use tab expansion on a cmdlet
name, type the entire first part of the name (the verb) and the hyphen that follows it. You can
fill in more of the name for a partial match. For example, if you type get-co and then press the
Tab   key, PowerShell automatically expands what you typed to the Get-Command cmdlet (notice
that it also changes the case of letters to their standard form). If you press Tab key again,
PowerShell replaces it with the next matching cmdlet, Get-Content . Tab completion also works
to resolve PowerShell aliases and native executables.

The following graphic shows examples of tab and menu completion.

<!-- p.237 -->

Other tab completion enhancements
Each new version of PowerShell includes improvements to tab completion that fix bugs and
improve usability.

PowerShell 7.0

     Tab completion resolves variable assignments that are enums or are type constrained
     Tab completion expands abbreviated cmdlets and functions. For example, i-psdf<tab>
     returns Import-PowerShellDataFile

PowerShell 7.2

     Fix tab completion for unlocalized about* articles
     Fix splatting being treated as positional parameter in completions
     Add completions for Comment-based Help keywords
     Add completion for #Requires statements
     Add tab completion for View parameter of Format-* cmdlets
     Add support for class-based argument completers

PowerShell 7.3

     Fix tab completion within the script block specified for the ValidateScriptAttribute
     Added tab completion for loop labels after break and continue
     Improve Hashtable completion in multiple scenarios
        Parameter splatting

<!-- p.238 -->

        Arguments parameter for Invoke-CimMethod
        FilterHashtable parameter for Get-WinEvent
        Property parameter for the CIM cmdlets
        Removes duplicates from member completion scenarios
     Support forward slashes in network share (UNC path) completion
     Improve member auto completion
     Prioritize ValidateSet completions over enums for parameters
     Add type inference support for generic methods with type parameters
     Improve type inference and completions
        Allows methods to be shown in completion results for ForEach-Object -MemberName
        Prevents completion on expressions that return void like ( [void]"" )
        Allows nondefault Class constructors to show up when class completion is based on
        the AST

Other ways to enhance tab completion of
command parameters
Built-in tab expansion is controlled by the internal function TabExpansion or TabExpansion2.
It's possible to create functions or modules that replace the default behavior of these functions.
You can find examples in the PowerShell Gallery by searching for the TabExpansion      keyword.

Using the ValidateSet or ArgumentCompletions attributes with
parameters
The ArgumentCompletions attribute allows you to add tab completion values to a specific
parameter. The ArgumentCompletions attribute is similar to ValidateSet . Both attributes take a
list of values to be presented when the user presses Tab after the parameter name. However,
unlike ValidateSet , the values aren't validated.

For more information, see:

     ArgumentCompletions
     ValidateSet

Using the ArgumentCompleter attribute or Register-
ArgumentCompleter with parameters

An argument completer is a script block or function that provides dynamic tab completion for
parameter values.

<!-- p.239 -->

The ArgumentCompleter attribute allows you to register a function that provides tab completion
values to for the parameter. The argument completer function must be available to the
function containing the parameter with the ArgumentCompleter attribute. Usually, the function is
defined in the same script or module. For more information, see ArgumentCompleter.

The Register-ArgumentCompleter cmdlet registers a script block as an argument completer
function at run time for any command you specify. Using Register-ArgumentCompleter allows
you to define argument completers outside of the script or module or for native commands.
For more information, see Register-ArgumentCompleter.

Predictive IntelliSense in PSReadLine
PSReadLine 2.1.0 introduced the Predictive IntelliSense feature. Predictive IntelliSense provides
suggestions for full commands based on items from your PSReadLine history.

PSReadLine 2.2.2 extends the power of Predictive IntelliSense by adding support for plug-in
modules that use advanced logic to provide suggestions for full commands. The
Az.Tools.Predictor module was the first plug-in for Predictive IntelliSense. It uses Machine
Learning to predict what Azure PowerShell command you want to run and the parameters you
want to use.

Prediction suggestions aren't tab-completion suggestions. They're generated from a different
source. By default, prediction suggestions appear in gray text following the cursor. Use the
RightArrow   key to accept the suggestion. If you hit the Tab key instead, the suggestion will be
ignored and the next tab-completion option is offered.

For more information, see Using predictors.

 Last updated on 03/04/2026

<!-- p.240 -->

Using predictors in PSReadLine
PSReadLine 2.1.0 introduced the Predictive IntelliSense feature. Predictive IntelliSense
provides suggestions for full commands based on items from your PSReadLine history.
PSReadLine 2.2.2 extends the power of Predictive IntelliSense by adding support for plug-in
modules that use advanced logic to provide suggestions for full commands. The latest version,
PSReadLine 2.2.6, enables predictions by default.

Using Predictive IntelliSense
When Predictive IntelliSense is enabled, the prediction suggestion appears as colored text
following the user's cursor. The suggestions from Predictive IntelliSense help new and
experienced users of PowerShell discover, edit, and execute full commands based on matching
predictions. Suggestions can come from the user's history and other domain-specific plugins.

The previous image shows the default InlineView of the suggestion. Pressing RightArrow key
accepts an inline suggestion. After accepting the suggestion, you can edit the command line
before hitting Enter to run the command.

PSReadLine also offers a ListView presentation of the suggestions.

When in the list view, you can use the arrow keys to scroll through the available suggestions.
List view also shows the source of the prediction.
