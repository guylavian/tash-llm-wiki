---
title: "How to use this documentation — pages 681-720"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0681-0720
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0681-0720
family: powershell
documentKind: "doc"
abstract: "Renamed powershell.exe to pwsh.exe The binary name for PowerShell has been changed from powershell(.exe) to pwsh(.exe) . This change provides a deterministic way for users to run PowerShell on machines and support side-by-side installations of Windows PowerShell and PowerShell."
---

# How to use this documentation — pages 681-720

<!-- p.681 -->

Renamed powershell.exe to pwsh.exe
The binary name for PowerShell has been changed from powershell(.exe) to pwsh(.exe) . This
change provides a deterministic way for users to run PowerShell on machines and support
side-by-side installations of Windows PowerShell and PowerShell.

Additional changes to pwsh(.exe) from powershell.exe :

     Changed the first positional parameter from -Command to -File . This change fixes the
     usage of #! (aka as a shebang) in PowerShell scripts that are being executed from non-
     PowerShell shells on non-Windows platforms. It also means that you can run commands
     like pwsh foo.ps1 or pwsh fooScript without specifying -File . However, this change
     requires that you explicitly specify -c or -Command when trying to run commands like
     pwsh.exe -Command Get-Command .

     pwsh accepts the -i (or -Interactive ) switch to indicate an interactive shell. This allows

     PowerShell to be used as a default shell on Unix platforms.
     Removed parameters -ImportSystemModules and -PSConsoleFile from pwsh.exe .
     Changed pwsh -Version and built-in help for pwsh.exe to align with other native tools.
     Invalid argument error messages for -File and -Command and exit codes consistent with
     Unix standards
     Added -WindowStyle parameter on Windows. Similarly, package-based installations
     updates on non-Windows platforms are in-place updates.

The shortened name is also consistent with naming of shells on non-Windows platforms.

Support running a PowerShell script with bool parameter
Previously, using pwsh.exe to execute a PowerShell script using -File provided no way to pass
$true / $false as parameter values. Support for $true / $false as parsed values to parameters

was added. Switch values are also supported.

Improved backwards compatibility with Windows
PowerShell
For Windows, a new [switch] parameter UseWindowsPowerShell is added to Import-Module .
This parameter creates a proxy module in PowerShell 7 that uses a local Windows PowerShell
process to implicitly run any cmdlets contained in that module. For more information, see
Import-Module.

<!-- p.682 -->

For more information on which Microsoft modules work with PowerShell 7.0, see the Module
Compatibility Table   .

Microsoft Update support for Windows
PowerShell 7.2 added support for Microsoft Update. When you enable this feature, you'll get
the latest PowerShell 7 updates in your traditional Windows Update (WU) management flow,
whether that's with Windows Update for Business, WSUS, SCCM, or the interactive WU dialog
in Settings.

The PowerShell 7.2 MSI package includes following command-line options:

      USE_MU - This property has two possible values:

         1 (default) - Opts into updating through Microsoft Update or WSUS

         0 - Don't opt into updating through Microsoft Update or WSUS

      ENABLE_MU

         1 (default) - Opts into using Microsoft Update the Automatic Updates or Windows

        Update
         0 - Don't opt into using Microsoft Update the Automatic Updates or Windows Update

Engine changes
Support PowerShell as a default Unix shell
On Unix, it's a convention for shells to accept -i for an interactive shell and many tools expect
this behavior ( script for example, and when setting PowerShell as the default shell) and calls
the shell with the -i switch. This change is breaking in that -i previously could be used as
short hand to match -InputFormat , which now needs to be -in .

Custom snap-ins
PowerShell snap-ins are a predecessor to PowerShell modules that don't have widespread
adoption in the PowerShell community.

Due to the complexity of supporting snap-ins and their lack of usage in the community, we no
longer support custom snap-ins in PowerShell.

Experimental feature flags

<!-- p.683 -->

PowerShell 6.2 enabled support for Experimental Features. This allows PowerShell developers
to deliver new features and get feedback before the design is complete. This way we avoid
making breaking changes as the design evolves.

Use Get-ExperimentalFeature to get a list of available experimental features. You can enable or
disable these features with Enable-ExperimentalFeature and Disable-ExperimentalFeature .

Load assembly from module base path before trying to load
from the GAC
Previously, when a binary module has the module assembly in GAC, we loaded the assembly
from GAC before trying to load it from module base path.

Skip null-element check for collections with a value-type
element type
For the Mandatory parameter and ValidateNotNull and ValidateNotNullOrEmpty attributes, skip
the null-element check if the collection's element type is value type.

Preserve $? for ParenExpression, SubExpression and
ArrayExpression
This PR alters the way we compile subpipelines (...) , subexpressions $(...) and array
expressions @() so that $? isn't automatically true. Instead the value of $? depends on the
result of the pipeline or statements executed.

Fix $? to not be $false when native command writes to
stderr

$? isn't set to $false when native command writes to stderr . It's common for native

commands to write to stderr without intending to indicate a failure. $? is set to $false only
when the native command has a non-zero exit code.

Make $ErrorActionPreference not affect stderr output of
native commands
It's common for native commands to write to stderr without intending to indicate a failure.
With this change, stderr output is still captured in ErrorRecord objects, but the runtime no
longer applies $ErrorActionPreference if the ErrorRecord comes from a native command.

<!-- p.684 -->

Change $OutputEncoding to use UTF-8 NoBOM encoding rather
than ASCII
The previous encoding, ASCII (7-bit), would result in incorrect alteration of the output in some
cases. Making UTF-8 NoBOM the default preserves Unicode output with an encoding supported
by most tools and operating systems.

Unify cmdlets with parameter -Encoding to be of type
System.Text.Encoding

The -Encoding value Byte has been removed from the FileSystem provider cmdlets. A new
parameter, -AsByteStream , is now used to specify that a byte stream is required as input or that
the output is a stream of bytes.

Change New-ModuleManifest encoding to UTF8NoBOM on non-
Windows platforms
Previously, New-ModuleManifest creates psd1 manifests in UTF-16 with BOM, creating a
problem for Linux tools. This breaking change changes the encoding of New-ModuleManifest to
be UTF (no BOM) in non-Windows platforms.

Remove AllScope from most default aliases
To speed up scope creation, AllScope was removed from most default aliases. AllScope was
left for a few frequently used aliases where the lookup was faster.

-Verbose and -Debug no longer overrides
$ErrorActionPreference

Previously, if -Verbose or -Debug were specified, it overrode the behavior of
$ErrorActionPreference . With this change, -Verbose and -Debug no longer affect the behavior

of $ErrorActionPreference .

Also, the -Debug parameter sets $DebugPreference to Continue instead of Inquire.

Make $PSCulture consistently reflect in-session culture
changes

<!-- p.685 -->

In Windows PowerShell, the current culture value is cached, which can allow the value to get
out of sync with the culture is change after session-startup. This caching behavior is fixed in
PowerShell core.

Allow explicitly specified named parameter to supersede the
same one from hashtable splatting
With this change, the named parameters from splatting are moved to the end of the parameter
list so that they're bound after all explicitly specified named parameters are bound. Parameter
binding for simple functions doesn't throw an error when a specified named parameter can't
be found. Unknown named parameters are bound to the $args parameter of the simple
function. Moving splatting to the end of the argument list changes the order the parameters
appears in $args .

For example:

 PowerShell

 function SimpleTest {
     param(
         $Name,
         $Path
     )
     "Name: $Name; Path: $Path; Args: $args"
 }

In the previous behavior, MyPath isn't bound to -Path because it's the third argument in the
argument list. ## So it ends up being stuffed into '$args' along with Blah = "World"

 PowerShell

 PS> $hash = @{ Name = "Hello"; Blah = "World" }
 PS> SimpleTest @hash "MyPath"
 Name: Hello; Path: ; Args: -Blah: World MyPath

With this change, the arguments from @hash are moved to the end of the argument list.
MyPath becomes the first argument in the list, so it's bound to -Path .

 PowerShell

 PS> SimpleTest @hash "MyPath"
 Name: Hello; Path: MyPath; Args: -Blah: World

<!-- p.686 -->

Language changes
Null-coalescing operator ??
The null-coalescing operator ?? returns the value of its left-hand operand if it isn't null.
Otherwise, it evaluates the right-hand operand and returns its result. The ?? operator doesn't
evaluate its right-hand operand if the left-hand operand evaluates to non-null.

 PowerShell

 $x = $null
 $x ?? 100

 Output

 100

In the following example, the right-hand operand won't be evaluated.

 PowerShell

 [string] $todaysDate = '1/10/2020'
 $todaysDate ?? (Get-Date).ToShortDateString()

 Output

 1/10/2020

Null-coalescing assignment operator ??=
The null-coalescing assignment operator ??= assigns the value of its right-hand operand to its
left-hand operand only if the left-hand operand evaluates to null. The ??= operator doesn't
evaluate its right-hand operand if the left-hand operand evaluates to non-null.

 PowerShell

 $x = $null
 $x ??= 100
 $x

 Output

<!-- p.687 -->

 100

In the following example, the right-hand operand won't be evaluated.

 PowerShell

 [string] $todaysDate = '1/10/2020'
 $todaysDate ??= (Get-Date).ToShortDateString()

 Output

 1/10/2020

Null-conditional operators

  ７ Note

  This feature was moved from experimental to mainstream in PowerShell 7.1.

A null-conditional operator applies a member access, ?. , or element access, ?[] , operation to
its operand only if that operand evaluates to non-null; otherwise, it returns null.

Since PowerShell allows ? to be part of the variable name, formal specification of the variable
name is required for using these operators. So it's required to use {} around the variable
names like ${a} or when ? is part of the variable name ${a?} .

In the following example, the value of PropName is returned.

 PowerShell

 $a = @{ PropName = 100 }
 ${a}?.PropName

 Output

 100

The following example will return null, without trying to access the member name PropName.

 PowerShell

<!-- p.688 -->

 $a = $null
 ${a}?.PropName

Similarly, the value of the element will be returned.

 PowerShell

 $a = 1..10
 ${a}?[0]

 Output

 1

And when the operand is null, the element isn't accessed and null is returned.

 PowerShell

 $a = $null
 ${a}?[0]

  ７ Note

  The variable name syntax of ${<name>} shouldn't be confused with the $() subexpression
  operator. For more information, see Variable name section of about_Variables.

Added & operator for job control
Putting & at the end of a pipeline causes the pipeline to be run as a PowerShell job. When a
pipeline is backgrounded, a job object is returned. Once the pipeline is running as a job, all of
the standard *-Job cmdlets can be used to manage the job. Variables (ignoring process-
specific variables) used in the pipeline are automatically copied to the job so Copy-Item $foo
$bar & just works. The job is also run in the current directory instead of the user's home

directory.

New methods/properties on PSCustomObject
We've added new methods and properties to PSCustomObject . PSCustomObject now includes a
Count / Length property like other objects.

<!-- p.689 -->

 PowerShell

 $PSCustomObject = [pscustomobject]@{foo = 1}

 $PSCustomObject.Length

 Output

 1

 PowerShell

 $PSCustomObject.Count

 Output

 1

This work also includes ForEach and Where methods that allow you to operate and filter on
PSCustomObject items:

 PowerShell

 $PSCustomObject.ForEach({$_.foo + 1})

 Output

 2

 PowerShell

 $PSCustomObject.Where({$_.foo -gt 0})

 Output

 foo
 ---
   1

Conversions from PSMethod to Delegate
You can convert a PSMethod into a delegate. This allows you to do things like passing PSMethod
[M]::DoubleStrLen as a delegate value into [M]::AggregateString :

<!-- p.690 -->

 PowerShell

 class M {
     static [int] DoubleStrLen([string] $value) { return 2 * $value.Length }

     static [long] AggregateString([string[]] $values, [Func[string, int]]
 $selector) {
         [long] $res = 0
         foreach($s in $values){
              $res += $selector.Invoke($s)
         }
         return $res
     }
 }

 [M]::AggregateString((gci).Name, [M]::DoubleStrLen)

String comparison behavior changed in PowerShell 7.1
PowerShell 7.1 is built on .NET 5.0, which introduced the following breaking change:

     Behavior changes when comparing strings on .NET 5+

As of .NET 5.0, culture invariant string comparisons ignore non-printing control characters.

For example, the following two strings are considered to be identical:

 PowerShell

 # Escape sequence "`a" is Ctrl-G or [char]7
 'Food' -eq "Foo`ad"

 Output

 True

New cmdlets
New Get-Uptime cmdlet
The Get-Uptime cmdlet returns the time elapsed since the last boot of the operating system.
The cmdlet was introduced in PowerShell 6.0.

New Remove-Alias cmdlet

<!-- p.691 -->

The Remove-Alias cmdlet removes an alias from the current PowerShell session. The cmdlet
was introduced in PowerShell 6.0.

New Remove-Service cmdlet
The Remove-Service cmdlet removes a Windows service in the registry and in the service
database. The Remove-Service cmdlet was introduced in PowerShell 6.0.

New Markdown cmdlets
Markdown is a standard for creating readable plaintext documents with basic formatting that
can be rendered into HTML.

The following cmdlets were added in PowerShell 6.1:

     ConvertFrom-Markdown - Convert the contents of a string or a file to a MarkdownInfo
     object.
     Get-MarkdownOption - Returns the current colors and styles used for rendering
     Markdown content in the console.
     Set-MarkdownOption - Sets the colors and styles used for rendering Markdown content
     in the console.
     Show-Markdown - Displays Markdown content in the console or as HTML

New Test-Json cmdlet
The Test-Json cmdlet tests whether a string is a valid JavaScript Object Notation (JSON)
document and can optionally verify that JSON document against a provided schema.

This cmdlet was introduced in PowerShell 6.1

New cmdlets to support Experimental Features
The following cmdlets were added in PowerShell 6.2 to support Experimental Features.

     Disable-ExperimentalFeature
     Enable-ExperimentalFeature
     Get-ExperimentalFeature

New Join-String cmdlet

<!-- p.692 -->

The Join-String cmdlet combines objects from the pipeline into a single string. This cmdlet was
added in PowerShell 6.2.

New view ConciseView and cmdlet Get-Error
PowerShell 7.0 enhances the display of error messages to improve the readability of interactive
and script errors with a new default view, ConciseView. The views are user-selectable through
the preference variable $ErrorView .

With ConciseView, if an error isn't from a script or parser error, then it's a single line error
message:

 PowerShell

 Get-ChildItem -Path C:\NotReal

 Output

 Get-ChildItem: Can't find path 'C:\NotReal' because it doesn't exist

If the error occurs during script execution or is a parsing error, PowerShell returns a multiline
error message that contains the error, a pointer, and an error message showing where the error
is in that line. If the terminal doesn't support ANSI color escape sequences (VT100), then colors
aren't displayed.

The default view in PowerShell 7 is ConciseView. The previous default view was NormalView
and you can select this by setting the preference variable $ErrorView .

 PowerShell

 $ErrorView = 'NormalView' # Sets the error view to NormalView
 $ErrorView = 'ConciseView' # Sets the error view to ConciseView

  ７ Note

  A new property ErrorAccentColor is added to $Host.PrivateData to support changing the
  accent color of the error message.

The new Get-Error cmdlet provides a complete detailed view of the fully qualified error when
desired. By default the cmdlet displays the full details, including inner exceptions, of the last

<!-- p.693 -->

error that occurred.

The Get-Error cmdlet supports input from the pipeline using the built-in variable $Error . Get-
Error displays all piped errors.

  PowerShell

  $Error | Get-Error

The Get-Error cmdlet supports the Newest parameter, allowing you to specify how many
errors from the current session you wish displayed.

  PowerShell

  Get-Error -Newest 3 # Displays the lst three errors that occurred in the session

For more information, see Get-Error.

Cmdlet changes
Parallel execution added to ForEach-Object
Beginning in PowerShell 7.0, the ForEach-Object cmdlet, which iterates items in a collection,
now has built-in parallelism with the new Parallel parameter.

By default, parallel script blocks use the current working directory of the caller that started the
parallel tasks.

This example retrieves 50,000 log entries from 5 system logs on a local Windows machine:

  PowerShell

  $logNames = 'Security','Application','System','Windows PowerShell','Microsoft-
  Windows-Store/Operational'

  $logEntries = $logNames | ForEach-Object -Parallel {
      Get-WinEvent -LogName $_ -MaxEvents 10000
  } -ThrottleLimit 5

  $logEntries.Count

  50000

The Parallel parameter specifies the script block that's run in parallel for each input log name.

<!-- p.694 -->

The new ThrottleLimit parameter limits the number of script blocks running in parallel at a
given time. The default is 5.

Use the $_ variable to represent the current input object in the script block. Use the Using:
scope modifier to pass variable references to the running script block.

For more information, see ForEach-Object.

Check system32 for compatible built-in modules on Windows
In the Windows 10 1809 update and Windows Server 2019, we updated a number of built-in
PowerShell modules to mark them as compatible with PowerShell.

When PowerShell starts up, it automatically includes $windir\System32 as part of the
PSModulePath environment variable. However, it only exposes modules to Get-Module and

Import-Module if its CompatiblePSEdition is marked as compatible with Core .

You can override this behavior to show all modules using the -SkipEditionCheck [switch]
parameter. We've also added a PSEdition property to the table output.

-lp alias for all -LiteralPath parameters

We created a standard parameter alias -lp for all the built-in PowerShell cmdlets that have a -
LiteralPath parameter.

Fix Get-Item -LiteralPath a*b if a*b doesn't actually exist to
return error
Previously, -LiteralPath given a wildcard would treat it the same as -Path and if the wildcard
found no files, it would silently exit. Correct behavior should be that -LiteralPath is literal so if
the file doesn't exist, it should error. Change is to treat wildcards used with -Literal as literal.

Set working directory to current directory in Start-Job
The Start-Job cmdlet now uses the current directory as the working directory for the new job.

Remove -Protocol from *-Computer cmdlets
The -Protocol parameter was removed from following cmdlets:

      Rename-Computer

<!-- p.695 -->

      Restart-Computer

      Stop-Computer

DCOM is no longer supported for remoting. The cmdlets only support WSMAN remoting.

Remove -ComputerName from *-Service cmdlets
In order to encourage the consistent use of PSRP, the -ComputerName parameter was removed
from *-Service cmdlets. Use Invoke-Command to run the cmdlets on remote computers instead.

Fix Get-Content -Delimiter to not include the delimiter in the
returned lines
Previously, the output while using Get-Content -Delimiter was inconsistent and inconvenient
as it required further processing of the data to remove the delimiter. This change removes the
delimiter in returned lines.

Changes to Format-Hex
The -Raw parameter now does nothing. The Format-Hex cmdlet displays a true representation
of numbers that includes all the bytes for its type. This is what the -Raw parameter did prior to
this change.

Typo fix in Get-ComputerInfo property name
BiosSerialNumber was misspelled as BiosSeralNumber and has been changed to the correct

spelling.

Changes to available hash algorithms
The following hash algorithms have been removed from .NET:

      MACTripleDES

      RIPEMD160

This change affects the Get-FileHash cmdlet.

Add validation on Get-* cmdlets where passing $null returns
all objects instead of error
Passing $null to any of the following now throws an error:

<!-- p.696 -->

      Get-Credential -UserName

      Get-Event -SourceIdentifier

      Get-EventSubscriber -SourceIdentifier

      Get-Help -Name

      Get-PSBreakpoint -Script

      Get-PSProvider -PSProvider

      Get-PSSessionConfiguration -Name

      Get-Runspace -Name

      Get-RunspaceDebug -RunspaceName

      Get-Service -Name

      Get-TraceSource -Name

      Get-Variable -Name

Add support for the W3C Extended Log File Format in Import-
Csv

Previously, the Import-Csv cmdlet can't be used to directly import the log files in W3C
extended log format and additional action would be required. With this change, W3C extended
log format is supported.

Import-Csv applies pstypenames upon import when type
information is present in the CSV
Previously, objects exported using Export-Csv with TypeInformation imported with
ConvertFrom-Csv weren't retaining the type information. This change adds the type information

to pstypenames member if available from the CSV file.

-NoTypeInformation is the default on Export-Csv

Previously, the Export-Csv cmdlet would output a comment as the first line containing the type
name of the object. The change excludes the type information by default because it's not
understood by most CSV tools. This change was made to address customer feedback.

Use -IncludeTypeInformation to retain the previous behavior.

Allow * to be used in registry path for Remove-Item
Previously, -LiteralPath given a wildcard would treat it the same as -Path and if the wildcard
found no files, it would silently exit. Correct behavior should be that -LiteralPath is literal so if

<!-- p.697 -->

the file doesn't exist, it should error. Change is to treat wildcards used with -Literal as literal.

Group-Object now sorts the groups

As part of the performance improvement, Group-Object now returns a sorted listing of the
groups. Although you shouldn't rely on the order, you could be broken by this change if you
wanted the first group. We decided that this performance improvement was worth the change
since the impact of being dependent on previous behavior is low.

Standard deviation in Measure-Object
The output from Measure-Object now includes a StandardDeviation property.

 PowerShell

 Get-Process | Measure-Object -Property CPU -AllStats

 Output

 Count             : 308
 Average           : 31.3720576298701
 Sum               : 9662.59375
 Maximum           : 4416.046875
 Minimum           :
 StandardDeviation : 264.389544720926
 Property          : CPU

Get-PfxCertificate -Password

Get-PfxCertificate now has the Password parameter, which takes a SecureString . This allows

you to use it non-interactively:

 PowerShell

 $certFile = '\\server\share\pwd-protected.pfx'
 $certPass = Read-Host -AsSecureString -Prompt 'Enter the password for certificate:
 '

 $certThumbPrint = (Get-PfxCertificate -FilePath $certFile -Password $certPass
 ).ThumbPrint

Removal of the more function

<!-- p.698 -->

In the past, PowerShell shipped a function on Windows called more that wrapped more.com .
That function has now been removed.

Also, the help function changed to use more.com on Windows, or the system's default pager
specified by $Env:PAGER on non-Windows platforms.

cd DriveName: now returns users to the current working
directory in that drive
Previously, using Set-Location or cd to return to a PSDrive sent users to the default location
for that drive. Users are now sent to the last known current working directory for that session.

cd - returns to previous directory

 PowerShell

 C:\Windows\System32> cd C:\
 C:\> cd -
 C:\Windows\System32>

Or on Linux:

 ShellSession

 PS /etc> cd /usr/bin
 PS /usr/bin> cd -
 PS /etc>

Also, cd and cd -- change to $HOME .

Update-Help as non-admin

By popular demand, Update-Help no longer needs to be run as an administrator. Update-Help
now defaults to saving help to a user-scoped folder.

Where-Object -Not

With the addition of -Not parameter to Where-Object , can filter an object at the pipeline for
the non-existence of a property, or a null/empty property value.

For example, this command returns all services that don't have any dependent services defined:

<!-- p.699 -->

 PowerShell

 Get-Service | Where-Object -Not DependentServices

Changes to Web Cmdlets
The underlying .NET API of the Web Cmdlets has been changed to
System.Net.Http.HttpClient . This change provides many benefits. However, this change along

with a lack of interoperability with Internet Explorer have resulted in several breaking changes
within Invoke-WebRequest and Invoke-RestMethod .

     Invoke-WebRequest now supports basic HTML Parsing only. Invoke-WebRequest always

     returns a BasicHtmlWebResponseObject object. The ParsedHtml and Forms properties have
     been removed.
     BasicHtmlWebResponseObject.Headers values are now String[] instead of String .

     BasicHtmlWebResponseObject.BaseResponse is now a System.Net.Http.HttpResponseMessage

     object.
     The Response property on Web Cmdlet exceptions is now a
     System.Net.Http.HttpResponseMessage object.

     Strict RFC header parsing is now default for the -Headers and -UserAgent parameter. This
     can be bypassed with -SkipHeaderValidation .
     file:// and ftp:// URI schemes are no longer supported.

     System.Net.ServicePointManager settings are no longer honored.

     There is currently no certificate based authentication available on macOS.
     Use of -Credential over an http:// URI will result in an error. Use an https:// URI or
     supply the -AllowUnencryptedAuthentication parameter to suppress the error.
     -MaximumRedirection now produces a terminating error when redirection attempts exceed

     the provided limit instead of returning the results of the last redirection.
     In PowerShell 6.2, a change was made to default to UTF-8 encoding for JSON responses.
     When a charset isn't supplied for a JSON response, the default encoding should be UTF-8
     per RFC 8259.
     Default encoding set to UTF-8 for application-json responses
     Added -SkipHeaderValidation parameter to allow Content-Type headers that aren't
     standards-compliant
     Added -Form parameter to support simplified multipart/form-data support
     Compliant, case-insensitive handling of relation keys
     Added -Resume parameter for web cmdlets

<!-- p.700 -->

Invoke-RestMethod returns useful info when no data is
returned
When an API returns just null , Invoke-RestMethod was serializing this as the string "null"
instead of $null . This change fixes the logic in Invoke-RestMethod to properly serialize a valid
single value JSON null literal as $null .

Web Cmdlets warn when -Credential is sent over
unencrypted connections
When using HTTP, content including passwords are sent as clear-text. This change is to not
allow this by default and return an error if credentials are being passed insecurely. Users can
bypass this by using the -AllowUnencryptedAuthentication switch.

Make -OutFile parameter in web cmdlets to work like -
LiteralPath

Beginning in PowerShell 7.1, the OutFile parameter of the web cmdlets works like LiteralPath
and doesn't process wildcards.

API changes
Remove AddTypeCommandBase class
The AddTypeCommandBase class was removed from Add-Type to improve performance. This class
is only used by the Add-Type cmdlet and shouldn't impact users.

Removed VisualBasic as a supported language in Add-Type
In the past, you could compile Visual Basic code using the Add-Type cmdlet. Visual Basic was
rarely used with Add-Type . We removed this feature to reduce the size of PowerShell.

Removed RunspaceConfiguration support
Previously, when creating a PowerShell runspace programmatically using the API, you could
use the legacy RunspaceConfiguration or the newer InitialSessionState classes. This change
removed support for RunspaceConfiguration and only supports InitialSessionState .

<!-- p.701 -->

CommandInvocationIntrinsics.InvokeScript bind arguments to
$input instead of $args

An incorrect position of a parameter resulted in the args passed as input instead of as args.

Remove ClrVersion and BuildVersion properties from
$PSVersionTable

The ClrVersion property of $PSVersionTable isn't useful with CoreCLR. End users shouldn't be
using that value to determine compatibility.

The BuildVersion property was tied to the Windows build version, which isn't available on
non-Windows platforms. Use the GitCommitId property to retrieve the exact build version of
PowerShell.

Implement Unicode escape parsing
`u#### or `u{####} is converted to the corresponding Unicode character. To output a literal

`u , escape the backtick: ``u .

Parameter binding problem with ValueFromRemainingArguments
in PS functions
ValueFromRemainingArguments now returns the values as an array instead of a single value which

itself is an array.

Cleaned up uses of CommandTypes.Workflow and
WorkflowInfoCleaned

Clean up code related to the uses of CommandTypes.Workflow and WorkflowInfo in
System.Management.Automation.

These minor breaking changes mainly affect help provider code.

      Change the public constructors of WorkflowInfo to internal. We don't support workflow
      anymore, so it makes sense to not allow people to create Workflow instances.
      Remove the type System.Management.Automation.DebugSource since it's only used for
      workflow debugging.
      Remove the overload of SetParent from the abstract class Debugger that's only used for
      workflow debugging.

<!-- p.702 -->

     Remove the same overload of SetParent from the derived class RemotingJobDebugger.

Don't wrap return result in PSObject when converting a
ScriptBlock to a delegate

When a ScriptBlock is converted to a delegate type to be used in C# context, wrapping the
result in a PSObject brings unneeded troubles:

     When the value is converted to the delegate return type, the PSObject essentially gets
     unwrapped. So the PSObject is unneeded.
     When the delegate return type is object , it gets wrapped in a PSObject making it hard to
     work with in C# code.

After this change, the returned object is the underlying object.

Remoting Support
PowerShell Remoting (PSRP) using WinRM isn't supported for non-Windows platforms. You can
use PowerShell Remoting (PSRP) over WinRM from Windows to connect to other Windows
machines. PowerShell also supports remoting over SSH on all platforms (Windows, macOS, and
Linux). For more information, see SSH remoting in PowerShell.

PowerShell Direct for Containers tries to use pwsh first
PowerShell Direct      is a feature of PowerShell and Hyper-V that allows you to connect to a
Hyper-V VM or Container without network connectivity or other remote management services.

In the past, PowerShell Direct connected using the built-in Windows PowerShell instance on
the Container. Now, PowerShell Direct first attempts to connect using any available pwsh.exe
on the PATH environment variable. If pwsh.exe isn't available, PowerShell Direct falls back to
use powershell.exe .

Enable-PSRemoting now creates separate remoting endpoints
for preview versions
Enable-PSRemoting now creates two remoting session configurations:

     One for the major version of PowerShell. For example, PowerShell.6 . This endpoint that
     can be relied upon across minor version updates as the "system-wide" PowerShell 6
     session configuration

<!-- p.703 -->

     One version-specific session configuration, for example: PowerShell.6.1.0

This behavior is useful if you want to have multiple PowerShell 6 versions installed and
accessible on the same machine.

Additionally, preview versions of PowerShell now get their own remoting session
configurations after running the Enable-PSRemoting cmdlet:

 PowerShell

 C:\WINDOWS\system32> Enable-PSRemoting

Your output may be different if you haven't set up WinRM before.

 Output

 WinRM is already set up to receive requests on this computer.
 WinRM is already set up for remote management on this computer.

Then you can see separate PowerShell session configurations for the preview and stable builds
of PowerShell 6, and for each specific version.

 PowerShell

 Get-PSSessionConfiguration

 Output

 Name          : PowerShell.6.2-preview.1
 PSVersion     : 6.2
 StartupScript :
 RunAsUser     :
 Permission    : NT AUTHORITY\INTERACTIVE AccessAllowed, BUILTIN\Administrators
 AccessAllowed, BUILTIN\Remote Management Users AccessAllowed

 Name          : PowerShell.6-preview
 PSVersion     : 6.2
 StartupScript :
 RunAsUser     :
 Permission    : NT AUTHORITY\INTERACTIVE AccessAllowed, BUILTIN\Administrators
 AccessAllowed, BUILTIN\Remote Management Users AccessAllowed

 Name          : powershell.6
 PSVersion     : 6.1
 StartupScript :
 RunAsUser     :
 Permission    : NT AUTHORITY\INTERACTIVE AccessAllowed, BUILTIN\Administrators

<!-- p.704 -->

  AccessAllowed, BUILTIN\Remote Management Users AccessAllowed

  Name          : powershell.6.1.0
  PSVersion     : 6.1
  StartupScript :
  RunAsUser     :
  Permission    : NT AUTHORITY\INTERACTIVE AccessAllowed, BUILTIN\Administrators
  AccessAllowed, BUILTIN\Remote Management Users AccessAllowed

user@host:port syntax supported for SSH

SSH clients typically support a connection string in the format user@host:port . With the
addition of SSH as a protocol for PowerShell Remoting, we've added support for this format of
connection string:

Enter-PSSession -HostName fooUser@ssh.contoso.com:2222

Telemetry can only be disabled with an
environment variable
PowerShell sends basic telemetry data to Microsoft when it's launched. The data includes the
OS name, OS version, and PowerShell version. This data allows us to better understand the
environments where PowerShell is used and enables us to prioritize new features and fixes.

To opt-out of this telemetry, set the environment variable POWERSHELL_TELEMETRY_OPTOUT to
true , yes , or 1 . We no longer support deletion of the file

DELETE_ME_TO_DISABLE_CONSOLEHOST_TELEMETRY to disable telemetry.

 Last updated on 04/08/2026

<!-- p.705 -->

PowerShell differences on non-Windows
platforms
PowerShell strives to provide feature parity across all supported platforms. However, some
features behave differently or aren't available due to differences in .NET Core and platform-
specific differences. Other changes were made to improve the interoperability of PowerShell on
non-Windows platforms.

.NET Framework vs .NET Core
PowerShell on Linux and macOS uses .NET Core, a subset of the full .NET Framework on
Microsoft Windows. As a result, scripts that run on Windows might not run on non-Windows
platforms because of the differences in the frameworks.

For more information about changes in .NET Core, see Breaking changes for migration from
.NET Framework to .NET Core.

General Unix interoperability changes
     Added support for native command globbing on Unix platforms. This means you can use
     wildcards with native commands like ls *.txt .
     The more functionality respects the Linux $PAGER and defaults to less .
     Trailing backslash is automatically escaped when dealing with native command
     arguments.
     Fixed ConsoleHost to honor NoEcho on Unix platforms.
     Don't add PATHEXT environment variable on Unix.
     A powershell man-page is included in the package.

Execution policy
PowerShell ignores execution policies when running on non-Windows platforms. Get-
ExecutionPolicy returns Unrestricted on Linux and macOS. Set-ExecutionPolicy does nothing

on Linux and macOS.

Case-sensitivity in PowerShell

<!-- p.706 -->

Historically, PowerShell has been uniformly case-insensitive, with few exceptions. On Unix-like
operating systems, the file system is predominantly case-sensitive, and PowerShell adheres to
the standard of the file system.

     You must use the correct case when a filename in specified in PowerShell.
     If a script tries to load a module and the module name isn't cased correctly, then the
     module load fails. This behavior might cause a problem with existing scripts if the name
     referenced by the module doesn't match the proper case of the actual filename.
     While names in the filesystem are case-sensitive, tab-completion of filenames isn't case-
     sensitive. Tab-completion cycles through the list of names using case-insensitive
     matching.
     Get-Help supports case-insensitive pattern matching on Unix platforms.

     Import-Module is case insensitive when used with a filename to determine the module

     name.

Filesystem support for Linux and macOS
     Paths given to cmdlets are now slash-agnostic (both / and \ work as directory
     separators)
     XDG Base Directory Specification is now respected and used by default:
        The Linux/macOS profile path is located at ~/.config/powershell/profile.ps1
        The history save path is located at
        ~/.local/share/powershell/PSReadLine/ConsoleHost_history.txt

        The user module path is located at ~/.local/share/powershell/Modules
     Support for file and folder names containing the colon character on Unix.
     Support for script names or full paths that have commas.
     Detect when the LiteralPath parameter is used to suppress wildcard expansion for
     navigation cmdlets.
     Updated Get-ChildItem to work more like the *nix ls -R and the Windows DIR /S native
     commands. Get-ChildItem now returns the symbolic links encountered during a recursive
     search and doesn't search the directories that those links target.

.PS1 File Extensions
PowerShell scripts must end in .ps1 for the interpreter to understand how to load and run
them in the current process. Running scripts in the current process is the expected usual
behavior for PowerShell. You can add the #! magic number to a script that doesn't have a
.ps1 extension, but this causes the script to be run in a new PowerShell instance, preventing

<!-- p.707 -->

the script from working correctly when interchanging objects. This behavior might be desirable
when executing a PowerShell script from Bash or another shell.

Convenience aliases removed
PowerShell provides a set of aliases on Windows that map to Linux command names for user
convenience. On Linux and macOS, the "convenience aliases" for the basic commands ls , cp ,
mv , rm , cat , man , mount , and ps were removed to allow the native executable to run without

specifying a path.

Logging
On macOS, PowerShell uses the native os_log APIs to log to Apple's unified logging system           .
On Linux, PowerShell uses Syslog , a ubiquitous logging solution.

Job Control
There's no Unix-style job-control support in PowerShell on Linux or macOS. The fg and bg
commands aren't available. However, you can use PowerShell jobs that work on all platforms.

Putting & at the end of a pipeline causes the pipeline to be run as a PowerShell job. When a
pipeline is backgrounded, a job object is returned. Once the pipeline is running as a job, all *-
Job cmdlets can be used to manage the job. Variables (ignoring process-specific variables)

used in the pipeline are automatically copied to the job so Copy-Item $foo $bar & just works.
The job runs in the current directory instead of the user's home directory.

Remoting Support
PowerShell Remoting (PSRP) using WinRM on Unix platforms requires NTLM/Negotiate or
Basic Auth over HTTPS. PSRP on macOS only supports Basic Auth over HTTPS. Kerberos-based
authentication isn't supported.

PowerShell supports PowerShell Remoting (PSRP) over SSH on all platforms (Windows, Linux,
and macOS). For more information, see SSH remoting in PowerShell.

Just-Enough-Administration (JEA) Support
PowerShell on Linux or macOS doesn't allow you to create constrained administration (JEA)
remoting endpoints.

<!-- p.708 -->

sudo , exec , and PowerShell
Because PowerShell runs most commands in memory (like Python or Ruby), you can't use sudo
directly with PowerShell built-ins. You can run pwsh from sudo . If it's necessary to run a
PowerShell cmdlet from within PowerShell with sudo , for example, sudo Set-Date 8/18/2016 ,
then you would use sudo pwsh Set-Date 8/18/2016 .

Modules included on non-Windows platforms
For non-Windows platforms, PowerShell includes the following modules:

     Microsoft.PowerShell.Archive
     Microsoft.PowerShell.Core
     Microsoft.PowerShell.Host
     Microsoft.PowerShell.Management
     Microsoft.PowerShell.Security
     Microsoft.PowerShell.Utility
     PackageManagement
     PowerShellGet
     PSReadLine
     ThreadJob

A large number of the commands (cmdlets) commonly available in PowerShell aren't available
on Linux or macOS. Often, these commands don't apply to these platforms. For example,
commands for Windows-specific features like the registry or services aren't available. Other
commands, like Set-ExecutionPolicy , are present but not functional.

For a comprehensive list of modules and cmdlets and the platforms they support, see Release
history of modules and cmdlets.

Modules no longer shipped with PowerShell
For various compatibility reasons, the following modules are no longer included in PowerShell.

     ISE
     Microsoft.PowerShell.LocalAccounts
     Microsoft.PowerShell.ODataUtils
     Microsoft.PowerShell.Operation.Validation
     PSScheduledJob

<!-- p.709 -->

     PSWorkflow
     PSWorkflowUtility

The following Windows-specific modules aren't included in PowerShell for Linux or macOS.

     CimCmdlets
     Microsoft.PowerShell.Diagnostics
     Microsoft.WSMan.Management
     PSDiagnostics

Cmdlets not available on non-Windows platforms
Some cmdlets were removed from PowerShell. Others aren't available or might work differently
on non-Windows platforms. For a comprehensive list of cmdlets removed from PowerShell, see
Cmdlets removed from PowerShell.

Microsoft.PowerShell.Core
The following cmdlets aren't available on Linux or macOS:

     Disable-PSRemoting

     Enable-PSRemoting

     Connect-PSSession

     Disconnect-PSSession

     Receive-PSSession

     Get-PSSessionCapability

     Disable-PSSessionConfiguration

     Enable-PSSessionConfiguration

     Get-PSSessionConfiguration

     Register-PSSessionConfiguration

     Set-PSSessionConfiguration

     Unregister-PSSessionConfiguration

     Test-PSSessionConfigurationFile

The ShowWindow parameter of Get-Help isn't available for non-Windows platforms.
PowerShell 7.3 added the Switch-Process cmdlet and the exec function for Linux and macOS.
These commands aren't available on Windows.

Microsoft.PowerShell.Security cmdlets

<!-- p.710 -->

The following cmdlets aren't available on Linux or macOS:

     Get-Acl

     Set-Acl

     Get-AuthenticodeSignature

     Set-AuthenticodeSignature

     New-FileCatalog

     Test-FileCatalog

These cmdlets are only available beginning in PowerShell 7.1.

     Get-CmsMessage

     Protect-CmsMessage

     Unprotect-CmsMessage

Microsoft.PowerShell.Management cmdlets
The following cmdlets aren't available on Linux and macOS:

     Rename-Computer

     Get-ComputerInfo

     Get-HotFix

     Clear-RecycleBin

     Get-Service

     New-Service

     Remove-Service

     Restart-Service

     Resume-Service

     Set-Service

     Start-Service

     Stop-Service

     Suspend-Service

     Set-TimeZone

The following cmdlets are available with limitations:

     Get-Clipboard - available in PowerShell 7.0+

     Set-Clipboard - available in PowerShell 7.0+

     Restart-Computer - available for Linux and macOS in PowerShell 7.1+

     Stop-Computer - available for Linux and macOS in PowerShell 7.1+

<!-- p.711 -->

Microsoft.PowerShell.Utility cmdlets
The following cmdlets aren't available on Linux and macOS:

         Convert-String

         ConvertFrom-String

         ConvertFrom-SddlString

         Out-GridView

         Out-Printer

         Show-Command

Aliases not available on Linux or macOS
The following table lists the aliases available for Windows that aren't available on non-
Windows platforms. These aliases aren't available because the alias conflicts with a native
command on those platforms.

                                                                                 ﾉ   Expand table

 Alias                            Cmdlet

 ac                               Add-Content

 cat                              Get-Content

 clear                            Clear-Host

 compare                          Compare-Object

 cp                               Copy-Item

 cpp                              Copy-ItemProperty

 diff                             Compare-Object

 kill                             Stop-Process

 ls                               Get-ChildItem

 man                              help

 mount                            New-PSDrive

 mv                               Move-Item

 ps                               Get-Process

<!-- p.712 -->

 Alias                            Cmdlet

 rm                               Remove-Item

 rmdir                            Remove-Item

 sleep                            Start-Sleep

 sort                             Sort-Object

 start                            Start-Process

 tee                              Tee-Object

 write                            Write-Output

The table doesn't include aliases unavailable for cmdlets that don't exist on non-Windows
platforms.

PowerShell Desired State Configuration (DSC)
Beginning with PowerShell 7.2, the PSDesiredStateConfiguration module was removed from
PowerShell and is published in the PowerShell Gallery. For more information, see the
announcement        on the PowerShell Team blog. For more information about using DSC on
Linux, see Get started with DSC for Linux. DSC v1.1 and v2.x aren't supported on macOS. DSC
v3 is supported on Windows, Linux, and macOS, but it's still in early development.

Last updated on 03/24/2025

<!-- p.713 -->

Release history of modules and cmdlets
This article lists the modules and cmdlets that are included in various versions of PowerShell. This
is a summary of information found in the release notes. More detailed information can be found
in the release notes:

     What's new in PowerShell 7.5
     What's new in PowerShell 7.4
     What's new in PowerShell 7.3
     What's new in PowerShell 7.2
     What's new in PowerShell 7.1
     What's new in PowerShell 7.0

This is a work in progress. Please help us keep this information fresh.

Module release history
                                                                                          ﾉ   Expand table

 ModuleName / PSVersion                      5.1   7.4 and   Note
                                                   higher

 CimCmdlets                                                  Windows only

 ISE (introduced in 2.0)                                     Windows only

 Microsoft.PowerShell.Archive

 Microsoft.PowerShell.Core

 Microsoft.PowerShell.Diagnostics                            Windows only

 Microsoft.PowerShell.Host

 Microsoft.PowerShell.LocalAccounts                          Windows only (64-bit only)

 Microsoft.PowerShell.Management

 Microsoft.PowerShell.ODataUtils                             Windows only

 Microsoft.PowerShell.Operation.Validation                   Windows only

 Microsoft.PowerShell.PSResourceGet                          New versions available from the Gallery

 Microsoft.PowerShell.Security

<!-- p.714 -->

ModuleName / PSVersion            5.1     7.4 and    Note
                                          higher

Microsoft.PowerShell.ThreadJob                       Installable in PowerShell 5.1 - Replaced
                                                     ThreadJob in PowerShell 7.6

Microsoft.PowerShell.Utility

Microsoft.WsMan.Management                           Windows only

PackageManagement

PowerShellGet 1.1                                    Must upgrade to v2.x

PowerShellGet 2.x                                    New versions available from the Gallery

PSDesiredStateConfiguration 1.1                      Removed in 7.2 - available from the Gallery

PSDesiredStateConfiguration 2.x                      Removed in 7.2 - available from the Gallery

PSDesiredStateConfiguration 3.x                      Preview available from the Gallery

PSDiagnostics                                        Windows only

PSReadLine                                           New versions available from the Gallery

PSScheduledJob                                       Windows only

PSWorkflow                                           Windows only

PSWorkflowUtility                                    Windows only

ThreadJob                                            Replaced by Microsoft.PowerShell.ThreadJob
                                                     in PowerShell 7.6

Cmdlet release history
CimCmdlets

                                                                                   ﾉ   Expand table

Cmdlet name                             5.1     7.4 and higher              Note

Export-BinaryMiLog                                                          Windows only

Get-CimAssociatedInstance                                                   Windows only

Get-CimClass                                                                Windows only

Get-CimInstance                                                             Windows only

<!-- p.715 -->

 Cmdlet name                                 5.1   7.4 and higher   Note

 Get-CimSession                                                     Windows only

 Import-BinaryMiLog                                                 Windows only

 Invoke-CimMethod                                                   Windows only

 New-CimInstance                                                    Windows only

 New-CimSession                                                     Windows only

 New-CimSessionOption                                               Windows only

 Register-CimIndicationEvent                                        Windows only

 Remove-CimInstance                                                 Windows only

 Remove-CimSession                                                  Windows only

 Set-CimInstance                                                    Windows only

ISE (introduced in 2.0)
This modules is only available in Windows PowerShell.

                                                                           ﾉ   Expand table

 Cmdlet name                                                5.1     Note

 Get-IseSnippet

 Import-IseSnippet

 New-IseSnippet

Microsoft.PowerShell.Archive

                                                                           ﾉ   Expand table

 Cmdlet name                           5.1         7.4 and higher              Note

 Compress-Archive

 Expand-Archive

Microsoft.PowerShell.Core

<!-- p.716 -->

                                                                                 ﾉ   Expand table

Cmdlet name                      5.1   7.4 and higher   Note

Add-History

Add-PSSnapin                                            Windows only

Clear-History

Clear-Host

Connect-PSSession                                       Windows only

Debug-Job

Disable-ExperimentalFeature                             Added in 6.2

Disable-PSRemoting                                      Windows only

Disable-PSSessionConfiguration                          Windows only

Disconnect-PSSession                                    Windows only

Enable-ExperimentalFeature                              Added in 6.2

Enable-PSRemoting                                       Windows only

Enable-PSSessionConfiguration                           Windows only

Enter-PSHostProcess                                     Added Linux support in 6.2

Enter-PSSession

Exit-PSHostProcess                                      Added Linux support in 6.2

Exit-PSSession

Export-Console                                          Windows only

Export-ModuleMember

ForEach-Object

Get-Command

Get-ExperimentalFeature                                 Added in 6.2

Get-Help

Get-History

Get-Job

<!-- p.717 -->

Cmdlet name                       5.1   7.4 and higher   Note

Get-Module

Get-PSHostProcessInfo                                    Added Linux support in 6.2

Get-PSSession

Get-PSSessionCapability

Get-PSSessionConfiguration

Get-PSSnapin                                             Windows only

Get-Verb                                                 Moved to Microsoft.PowerShell.Utility 6.0+

Import-Module

Invoke-Command

Invoke-History

New-Module

New-ModuleManifest

New-PSRoleCapabilityFile

New-PSSession

New-PSSessionConfigurationFile                           Added Linux support in 7.3

New-PSSessionOption

New-PSTransportOption

Out-Default

Out-Host

Out-Null

Receive-Job

Receive-PSSession                                        Windows only

Register-ArgumentCompleter

Register-PSSessionConfiguration                          Windows only

Remove-Job

Remove-Module

<!-- p.718 -->

Cmdlet name                             5.1   7.4 and higher   Note

Remove-PSSession

Remove-PSSnapin                                                Windows only

Resume-Job

Save-Help

Set-PSDebug

Set-PSSessionConfiguration                                     Windows only

Set-StrictMode

Start-Job

Stop-Job

Switch-Process                                                 Linux and macOS only

Suspend-Job                                                    Windows only

Test-ModuleManifest

Test-PSSessionConfigurationFile                                Windows only

Unregister-PSSessionConfiguration                              Windows only

Update-Help

Wait-Job

Where-Object

Microsoft.PowerShell.Diagnostics

                                                                                       ﾉ     Expand table

Cmdlet name                       5.1         7.4 and higher                  Note

Export-Counter                                                                Windows only

Get-Counter                                                                   Windows only

Get-WinEvent                                                                  Windows only

Import-Counter                                                                Windows only

New-WinEvent                                                                  Windows only

<!-- p.719 -->

Microsoft.PowerShell.Host

                                                                     ﾉ    Expand table

 Cmdlet name                       5.1        7.4 and higher             Note

 Start-Transcript

 Stop-Transcript

Microsoft.PowerShell.LocalAccounts (64-bit only)
This modules is only available in Windows PowerShell.

                                                                     ﾉ    Expand table

 Cmdlet name                                                   5.1   Note

 Add-LocalGroupMember

 Disable-LocalUser

 Enable-LocalUser

 Get-LocalGroup

 Get-LocalGroupMember

 Get-LocalUser

 New-LocalGroup

 New-LocalUser

 Remove-LocalGroup

 Remove-LocalGroupMember

 Remove-LocalUser

 Rename-LocalGroup

 Rename-LocalUser

 Set-LocalGroup

 Set-LocalUser

Microsoft.PowerShell.Management

<!-- p.720 -->

                                                                 ﾉ   Expand table

Cmdlet name                5.1   7.4 and higher   Note

Add-Computer                                      Windows only

Add-Content

Checkpoint-Computer                               Windows only

Clear-Content

Clear-EventLog                                    Windows only

Clear-Item

Clear-ItemProperty

Clear-RecycleBin                                  Windows only

Complete-Transaction                              Windows only

Convert-Path

Copy-Item

Copy-ItemProperty

Debug-Process

Disable-ComputerRestore                           Windows only

Enable-ComputerRestore                            Windows only

Get-ChildItem

Get-Clipboard

Get-ComputerInfo                                  Windows only

Get-ComputerRestorePoint                          Windows only

Get-Content

Get-ControlPanelItem                              Windows only

Get-EventLog                                      Windows only

Get-HotFix                                        Windows only

Get-Item

Get-ItemProperty
