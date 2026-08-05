---
title: "How to use this documentation — pages 721-760"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0721-0760
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0721-0760
family: powershell
documentKind: "doc"
abstract: "Cmdlet name 5.1 7.4 and higher Note Get-ItemPropertyValue Get-Location Get-Process Get-PSDrive Get-PSProvider Get-Service Windows only Get-TimeZone Windows only Get-Transaction Windows only Get-WmiObject Windows only Invoke-Item Invoke-WmiMethod Windows only Join-Path Limit-Even"
---

# How to use this documentation — pages 721-760

<!-- p.721 -->

Cmdlet name             5.1   7.4 and higher   Note

Get-ItemPropertyValue

Get-Location

Get-Process

Get-PSDrive

Get-PSProvider

Get-Service                                    Windows only

Get-TimeZone                                   Windows only

Get-Transaction                                Windows only

Get-WmiObject                                  Windows only

Invoke-Item

Invoke-WmiMethod                               Windows only

Join-Path

Limit-EventLog                                 Windows only

Move-Item

Move-ItemProperty

New-EventLog                                   Windows only

New-Item

New-ItemProperty

New-PSDrive

New-Service                                    Windows only

New-WebServiceProxy                            Windows only

Pop-Location

Push-Location

Register-WmiEvent                              Windows only

Remove-Computer                                Windows only

Remove-EventLog                                Windows only

<!-- p.722 -->

Cmdlet name                     5.1   7.4 and higher   Note

Remove-Item

Remove-ItemProperty

Remove-PSDrive

Remove-Service                                         Windows only

Remove-WmiObject                                       Windows only

Rename-Computer                                        Windows only

Rename-Item

Rename-ItemProperty

Reset-ComputerMachinePassword                          Windows only

Resolve-Path

Restart-Computer                                       Added Linux/macOS support in 7.1

Restart-Service                                        Windows only

Restore-Computer                                       Windows only

Resume-Service                                         Windows only

Set-Clipboard

Set-Content

Set-Item

Set-ItemProperty

Set-Location

Set-Service                                            Windows only

Set-TimeZone                                           Windows only

Set-WmiInstance                                        Windows only

Show-ControlPanelItem                                  Windows only

Show-EventLog                                          Windows only

Split-Path

Start-Process

<!-- p.723 -->

 Cmdlet name                         5.1   7.4 and higher   Note

 Start-Service                                              Windows only

 Start-Transaction                                          Windows only

 Stop-Computer                                              Added Linux/macOS support in 7.1

 Stop-Process

 Stop-Service                                               Windows only

 Suspend-Service                                            Windows only

 Test-ComputerSecureChannel                                 Windows only

 Test-Connection

 Test-Path

 Undo-Transaction                                           Windows only

 Use-Transaction                                            Windows only

 Wait-Process

 Write-EventLog                                             Windows only

Microsoft.PowerShell.ODataUtils
This modules is only available in Windows PowerShell.

                                                                                ﾉ   Expand table

 Cmdlet name                                                       5.1          Note

 Export-ODataEndpointProxy

Microsoft.PowerShell.Operation.Validation
This modules is only available in Windows PowerShell.

                                                                                ﾉ   Expand table

 Cmdlet name                                                       5.1          Note

 Get-OperationValidation

 Invoke-OperationValidation

<!-- p.724 -->

Microsoft.PowerShell.PSResourceGet

                                                                                       ﾉ   Expand table

Cmdlet name                                7.4 and higher          Note

Compress-PSResource                                                Added in v1.1.0 of the module

Find-PSResource

Get-InstalledPSResource

Get-PSResource

Get-PSResourceRepository

Get-PSScriptFileInfo

Import-PSGetRepository

Install-PSResource

New-PSScriptFileInfo

Publish-PSResource

Register-PSResourceRepository

Save-PSResource

Set-PSResourceRepository

Test-PSScriptFileInfo

Uninstall-PSResource

Unregister-PSResourceRepository

Update-PSModuleManifest

Update-PSResource

Update-PSScriptFileInfo

Microsoft.PowerShell.Security

                                                                                       ﾉ   Expand table

Cmdlet name                       5.1   7.4 and higher      Note

ConvertFrom-SecureString

<!-- p.725 -->

Cmdlet name                   5.1     7.4 and higher      Note

ConvertTo-SecureString

Get-Acl                                                   Windows only

Get-AuthenticodeSignature                                 Windows only

Get-CmsMessage                                            Support for Linux/macOS added in 7.1

Get-Credential

Get-ExecutionPolicy                                       Returns Unrestricted on Linux/macOS

Get-PfxCertificate

New-FileCatalog                                           Windows only

Protect-CmsMessage                                        Support for Linux/macOS added in 7.1

Set-Acl                                                   Windows only

Set-AuthenticodeSignature                                 Windows only

Set-ExecutionPolicy                                       Does nothing on Linux/macOS

Test-FileCatalog                                          Windows only

Unprotect-CmsMessage                                      Support for Linux/macOS added in 7.1

Microsoft.PowerShell.Utility

                                                                                   ﾉ    Expand table

Cmdlet name                 5.1     7.4 and higher     Note

Add-Member

Add-Type

Clear-Variable

Compare-Object

Convert-String

ConvertFrom-CliXml                                     Added in 7.5

ConvertFrom-Csv

ConvertFrom-Json

<!-- p.726 -->

Cmdlet name              5.1   7.4 and higher   Note

ConvertFrom-Markdown                            Added in 6.1

ConvertFrom-SddlString                          Windows only

ConvertFrom-String

ConvertFrom-StringData

ConvertTo-CliXml                                Added in 7.5

ConvertTo-Csv

ConvertTo-Html

ConvertTo-Json

ConvertTo-Xml

Debug-Runspace

Disable-PSBreakpoint

Disable-RunspaceDebug

Enable-PSBreakpoint

Enable-RunspaceDebug

Export-Alias

Export-Clixml

Export-Csv

Export-FormatData

Export-PSSession

Format-Custom

Format-Hex

Format-List

Format-Table

Format-Wide

Get-Alias

Get-Culture

<!-- p.727 -->

Cmdlet name           5.1   7.4 and higher   Note

Get-Date

Get-Error

Get-Event                                    No event sources available on Linux/macOS

Get-EventSubscriber

Get-FileHash

Get-FormatData

Get-Host

Get-MarkdownOption                           Added in 6.1

Get-Member

Get-PSBreakpoint

Get-PSCallStack

Get-Random

Get-Runspace

Get-RunspaceDebug

Get-SecureRandom                             Added in 7.4

Get-TraceSource

Get-TypeData

Get-UICulture

Get-Unique

Get-Uptime

Get-Variable

Get-Verb                                     Moved from Microsoft.PowerShell.Core

Group-Object

Import-Alias

Import-Clixml

Import-Csv

<!-- p.728 -->

Cmdlet name                 5.1   7.4 and higher   Note

Import-LocalizedData

Import-PowerShellDataFile

Import-PSSession

Invoke-Expression

Invoke-RestMethod

Invoke-WebRequest

Join-String

Measure-Command

Measure-Object

New-Alias

New-Event                                          No event sources available on Linux/macOS

New-Guid

New-Object

New-TemporaryFile

New-TimeSpan

New-Variable

Out-File

Out-GridView                                       Windows only

Out-Printer                                        Windows only

Out-String

Read-Host

Register-EngineEvent                               No event sources available on Linux/macOS

Register-ObjectEvent

Remove-Alias

Remove-Event                                       No event sources available on Linux/macOS

Remove-PSBreakpoint

<!-- p.729 -->

Cmdlet name          5.1   7.4 and higher   Note

Remove-TypeData

Remove-Variable

Select-Object

Select-String

Select-Xml

Send-MailMessage

Set-Alias

Set-Date

Set-MarkdownOption                          Added in 6.1

Set-PSBreakpoint

Set-TraceSource

Set-Variable

Show-Command                                Windows only

Show-Markdown                               Added in 6.1

Sort-Object

Start-Sleep

Tee-Object

Test-Json

Trace-Command

Unblock-File                                Added support for macOS in 7.0

Unregister-Event                            No event sources available on Linux/macOS

Update-FormatData

Update-List

Update-TypeData

Wait-Debugger

Wait-Event

<!-- p.730 -->

Cmdlet name              5.1   7.4 and higher     Note

Write-Debug

Write-Error

Write-Host

Write-Information

Write-Output

Write-Progress

Write-Verbose

Write-Warning

Microsoft.WsMan.Management

                                                                        ﾉ   Expand table

Cmdlet name                           5.1       7.4 and higher   Note

Connect-WSMan                                                    Windows only

Disable-WSManCredSSP                                             Windows only

Disconnect-WSMan                                                 Windows only

Enable-WSManCredSSP                                              Windows only

Get-WSManCredSSP                                                 Windows only

Get-WSManInstance                                                Windows only

Invoke-WSManAction                                               Windows only

New-WSManInstance                                                Windows only

New-WSManSessionOption                                           Windows only

Remove-WSManInstance                                             Windows only

Set-WSManInstance                                                Windows only

Set-WSManQuickConfig                                             Windows only

Test-WSMan                                                       Windows only

PackageManagement

<!-- p.731 -->

                                                                   ﾉ   Expand table

Cmdlet name                       5.1         7.4 and higher            Note

Find-Package

Find-PackageProvider

Get-Package

Get-PackageProvider

Get-PackageSource

Import-PackageProvider

Install-Package

Install-PackageProvider

Register-PackageSource

Save-Package

Set-PackageSource

Uninstall-Package

Unregister-PackageSource

PowerShellGet 2.x

                                                                   ﾉ   Expand table

Cmdlet name                             5.1       7.4 and higher          Note

Find-Command

Find-DscResource

Find-Module

Find-RoleCapability

Find-Script

Get-CredsFromCredentialProvider

Get-InstalledModule

Get-InstalledScript

<!-- p.732 -->

 Cmdlet name                                        5.1      7.4 and higher           Note

 Get-PSRepository

 Install-Module

 Install-Script

 New-ScriptFileInfo

 Publish-Module

 Publish-Script

 Register-PSRepository

 Save-Module

 Save-Script

 Set-PSRepository

 Test-ScriptFileInfo

 Uninstall-Module

 Uninstall-Script

 Unregister-PSRepository

 Update-Module

 Update-ModuleManifest

 Update-Script

 Update-ScriptFileInfo

PSDesiredStateConfiguration v1.1
This modules is only available from in Windows PowerShell.

                                                                               ﾉ   Expand table

 Cmdlet name                                                             5.1       Note

 Configuration

 Disable-DscDebug

 Enable-DscDebug

<!-- p.733 -->

 Cmdlet name                                                          5.1        Note

 Get-DscConfiguration

 Get-DscConfigurationStatus

 Get-DscLocalConfigurationManager

 Get-DscResource

 Invoke-DscResource

 New-DSCCheckSum

 Publish-DscConfiguration

 Remove-DscConfigurationDocument

 Restore-DscConfiguration

 Set-DscLocalConfigurationManager

 Start-DscConfiguration

 Stop-DscConfiguration

 Test-DscConfiguration

 Update-DscConfiguration

PSDesiredStateConfiguration v2.0.5
This modules is only available from the PowerShell Gallery.

                                                                             ﾉ   Expand table

 Cmdlet name                                     2.0.5        Note

 Configuration

 Get-DscResource

 Invoke-DscResource                                           Experimental

 New-DSCCheckSum

PSDesiredStateConfiguration v3.x - Preview
This modules is only available from the PowerShell Gallery.

<!-- p.734 -->

                                                                 ﾉ   Expand table

Cmdlet name                            3.0 (preview)                 Note

Configuration

ConvertTo-DscJsonSchema

Get-DscResource

Invoke-DscResource

New-DscChecksum

PSDiagnostics

                                                                 ﾉ   Expand table

Cmdlet name                    5.1     7.4 and higher         Note

Disable-PSTrace                                               Windows only

Disable-PSWSManCombinedTrace                                  Windows only

Disable-WSManTrace                                            Windows only

Enable-PSTrace                                                Windows only

Enable-PSWSManCombinedTrace                                   Windows only

Enable-WSManTrace                                             Windows only

Get-LogProperties                                             Windows only

Set-LogProperties                                             Windows only

Start-Trace                                                   Windows only

Stop-Trace                                                    Windows only

PSReadLine

                                                                 ﾉ   Expand table

Cmdlet name                          5.1     7.4 and higher            Note

Get-PSReadLineKeyHandler

Get-PSReadLineOption

<!-- p.735 -->

 Cmdlet name                                       5.1   7.4 and higher          Note

 PSConsoleHostReadLine

 Remove-PSReadLineKeyHandler

 Set-PSReadLineKeyHandler

 Set-PSReadLineOption

PSScheduledJob
This modules is only available in Windows PowerShell.

                                                                          ﾉ   Expand table

 Cmdlet name                                                   5.1        Note

 Add-JobTrigger

 Disable-JobTrigger

 Disable-ScheduledJob

 Enable-JobTrigger

 Enable-ScheduledJob

 Get-JobTrigger

 Get-ScheduledJob

 Get-ScheduledJobOption

 New-JobTrigger

 New-ScheduledJobOption

 Register-ScheduledJob

 Remove-JobTrigger

 Set-JobTrigger

 Set-ScheduledJob

 Set-ScheduledJobOption

 Unregister-ScheduledJob

<!-- p.736 -->

PSWorkflow & PSWorkflowUtility
This modules is only available in Windows PowerShell.

                                                                               ﾉ   Expand table

 Cmdlet name                                                          5.1          Note

 New-PSWorkflowExecutionOption

 New-PSWorkflowSession

 Invoke-AsWorkflow

Microsoft.PowerShell.ThreadJob (formerly ThreadJob)
This module can be installed from the PowerShell Gallery on any supported version of
PowerShell. The ThreadJob module was initially included in PowerShell 6.0. The ThreadJob
module was renamed to Microsoft.PowerShell.ThreadJob in PowerShell 7.6.

                                                                               ﾉ   Expand table

 Cmdlet name                        5.1        7.4 and higher                      Note

 Start-ThreadJob

Last updated on 04/28/2026

<!-- p.737 -->

PowerShell 7 module compatibility
08/06/2025

This article contains a partial list of PowerShell modules published by Microsoft.

The PowerShell team is working with the various feature teams that create PowerShell modules
to help them produce modules that work in PowerShell 7. These modules are not owned by the
PowerShell team.

The following modules are known to support PowerShell 7.

Azure PowerShell
The Az PowerShell module is a set of cmdlets for managing Azure resources directly from
PowerShell. PowerShell 7.0.6 LTS or higher is the recommended version of PowerShell for use
with the Azure Az PowerShell module on all platforms.

For more information, see Introducing the Azure Az PowerShell module.

MSGraph PowerShell SDK
The Microsoft Graph SDKs are designed to simplify building high-quality, efficient, and resilient
applications that access Microsoft Graph. PowerShell 7 and later is the recommended
PowerShell version for use with the Microsoft Graph PowerShell SDK.

For more information, see Install the Microsoft Graph PowerShell SDK.

Windows management modules
The Windows management modules provide management and support for various Windows
features and services. Most of these modules have been updated to work natively with
PowerShell 7, or tested for compatibility with PowerShell 7.

These modules are installed in different ways depending on the Edition of Windows, and how
the module is packaged for that Edition.

For more information about installation and compatibility, see PowerShell 7 module
compatibility in the Windows documentation.

Exchange Online Management 2.0

<!-- p.738 -->

The Exchange Online PowerShell V2 module (EXO V2) connects to all Exchange-related
PowerShell environments in Microsoft 365: Exchange Online PowerShell, Security & Compliance
PowerShell, and standalone Exchange Online Protection (EOP) PowerShell.

EXO v2.0.4 or later is supported in PowerShell 7.0.3 or later.

For more information, see About the Exchange Online PowerShell V2 module.

PowerShell modules for SQL Server
There are two SQL Server PowerShell modules:

     SqlServer: This module includes new cmdlets to support the latest SQL features, including
     updated versions of the cmdlets in SQLPS.
     SQLPS: The SQLPS is the module used by SQL Agent to run agent jobs in agent job steps
     using the PowerShell subsystem.

The SqlServer modules require PowerShell version 5.0 or greater.

For more information, see Install the SQL Server PowerShell module.

Finding the status of other modules
You can find a complete list of modules using the PowerShell Module Browser. Using the
Module Browser, you can find documentation for other PowerShell modules to determine their
PowerShell version requirements.

<!-- p.739 -->

Windows PowerShell update message FAQ
When you start Windows PowerShell you see a message that tells you to install the latest version
of PowerShell along with a URL.

This article explains the intent of this message and provides answers to frequently asked
questions.

Why am I seeing this message?
Windows PowerShell displays this message at startup to make you aware that there is a newer
version of PowerShell available.

I opened the URL but it didn't install an
update. How do I install PowerShell 7?
The aka.ms link shown in the Windows PowerShell console takes you to this page. To install the
latest version of PowerShell 7, follow the instructions in the Install PowerShell on Windows
article.

But I installed PowerShell 7, why am I still
seeing this message?

<!-- p.740 -->

Because you ran Windows PowerShell instead of PowerShell 7. PowerShell 7 and Windows
PowerShell 5.1 are separate products. PowerShell 7 doesn't replace Windows PowerShell 5.1.
PowerShell 7 installs side-by-side. You can run either version.

How do I run PowerShell 7?
For instructions, see the Start PowerShell 7 section of the Install PowerShell on Windows article.

Why would I want to install PowerShell 7?
PowerShell 7 is faster, more secure, and is available for Windows, Linux and macOS. PowerShell 7
is actively developed and supported. Windows PowerShell 5.1 is no longer being developed. For
more information, see the Differences between Windows PowerShell 5.1 and PowerShell 7 article.

Do I need to install PowerShell 7?
No, you don't need to install PowerShell 7 unless you have a specific requirement for the features
it provides.

My install of Windows is up-to-date. Why am I
still getting this message?
This message appears every time you start Windows PowerShell 5.1. It doesn't mean that
Windows PowerShell 5.1 is not up-to-date.

How does Windows PowerShell 5.1
get updated?
Microsoft only publishes security updates for Windows PowerShell 5.1. It's important to
understand that Windows PowerShell 5.1 is no longer being developed. Windows PowerShell 5.1
is a built-in component of Windows. All updates are managed through standard Windows update
channels.

Can I disable the message?
No. There is no way to disable the message.

<!-- p.741 -->

Starting Windows PowerShell
Article • 03/27/2025

Windows PowerShell is a scripting engine embedded into multiple hosts. The most
common hosts are the interactive command-line powershell.exe and the Interactive
Scripting Environment powershell_ise.exe .

PowerShell binary name
PowerShell version 6 and higher uses .NET (Core). Supported versions are available on
Windows, macOS, and Linux.

Beginning in PowerShell 6, the PowerShell binary named pwsh.exe for Windows and
pwsh for macOS and Linux. You can start PowerShell preview versions using pwsh-

preview . For more information, see About pwsh.

To find cmdlet reference and installation documentation for PowerShell 7, use the
following links:

                                                                       ﾉ   Expand table

 Document                          Link

 Cmdlet reference                  PowerShell Module Browser

 Windows installation              Installing PowerShell on Windows

 macOS installation                Installing PowerShell on macOS

 Linux installation                Installing PowerShell on Linux

To view content for other PowerShell versions, see How to use the PowerShell
documentation.

Run from the Start Menu
      Open the Start menu, type Windows PowerShell, select Windows PowerShell,
      then select Open.

Run from the Command Prompt

<!-- p.742 -->

In Windows Command shell, Windows PowerShell, or Windows PowerShell ISE, to start
Windows PowerShell, type: PowerShell .

You can also use the parameters of the powershell.exe program to customize the
session. For more information, see about_PowerShell_exe.

Run with administrative privileges
Open the Start menu, type Windows PowerShell, select Windows PowerShell, and then
select Run as administrator.

How to Start Windows PowerShell ISE on
Earlier Releases of Windows
Use any of the following methods to start Windows PowerShell ISE.

Run from the Start Menu
      Open the Start menu, type ISE, select Windows PowerShell ISE, then select Open.

At the Command Prompt
In Windows Command shell, Windows PowerShell, or Windows PowerShell ISE, to start
Windows PowerShell, type: PowerShell_ISE . In Windows PowerShell, you can use the
alias ise .

Run with administrative privileges
Select Start, type ISE, right-click Windows PowerShell ISE, and then click Run as
administrator.

Starting the 32-Bit Version of Windows
PowerShell
64-bit versions of Windows include a 32-bit version of Windows PowerShell, Windows
PowerShell (x86), in addition to the 64-bit version. The 64-bit version runs by default.

However, you might occasionally need to run Windows PowerShell (x86), such as when
you're using a module that requires the 32-bit version or when you're connecting

<!-- p.743 -->

remotely to a 32-bit computer.

To start a 32-bit version of Windows PowerShell, use any of the following procedures.

     Select Start, type Windows PowerShell, select Windows PowerShell (x86), then
     select Open.

<!-- p.744 -->

The Windows PowerShell ISE
The Windows PowerShell Integrated Scripting Environment (ISE) is a host application for
Windows PowerShell. In the ISE, you can run commands and write, test, and debug scripts in a
single Windows-based graphic user interface. The ISE provides multiline editing, tab
completion, syntax coloring, selective execution, context-sensitive help, and support for right-
to-left languages. Menu items and keyboard shortcuts are mapped to many of the same tasks
that you would do in the Windows PowerShell console. For example, when you debug a script
in the ISE, you can right-click on a line of code in the edit pane to set a breakpoint.

Support
The ISE was first introduced with Windows PowerShell V2 and was re-designed with PowerShell
V3. The ISE is supported in all supported versions of Windows PowerShell up to and including
Windows PowerShell V5.1.

  ７ Note

  The PowerShell ISE is no longer in active feature development. As a shipping component
  of Windows, it continues to be officially supported for security and high-priority servicing
  fixes. We currently have no plans to remove the ISE from Windows.

  There is no support for the ISE in PowerShell v6 and beyond. Users looking for
  replacement for the ISE should use Visual Studio Code        with the PowerShell
  Extension    .

Key Features
Key features in Windows PowerShell ISE include:

     Multiline editing: To insert a blank line under the current line in the Command pane, press
      SHIFT + ENTER .

     Selective execution: To run part of a script, select the text you want to run, and then click
     the Run Script button. Or, press F5 .
     Context-sensitive help: Type Invoke-Item , and then press F1 . The Help file opens to the
     article for the Invoke-Item cmdlet.

The Windows PowerShell ISE lets you customize some aspects of its appearance. It also has its
own Windows PowerShell profile script.

<!-- p.745 -->

To start the Windows PowerShell ISE
Click Start, select Windows PowerShell, and then click Windows PowerShell ISE. Alternately,
you can type powershell_ise.exe in any command shell or in the Run box.

To get Help in the Windows PowerShell ISE
On the Help menu, click Windows PowerShell Help. Or, press F1 . The file that opens describes
Windows PowerShell ISE and Windows PowerShell, including all the help available from the
Get-Help cmdlet.

Last updated on 11/20/2025

<!-- p.746 -->

Exploring the Windows PowerShell ISE
You can use the Windows PowerShell Integrated Scripting Environment (ISE) to create, run, and
debug commands and scripts.

The Windows PowerShell ISE consists of the menu bar, Windows PowerShell tabs, the toolbar,
script tabs, a Script Pane, a Console Pane, a status bar, a text-size slider and context-sensitive
Help.

Menu Bar
The menu bar contains the File, Edit, View, Tools, Debug, Add-ons, and Help menus.

The buttons on the menus allow you to perform tasks related to writing and running scripts
and running commands in the Windows PowerShell ISE.

Toolbar

<!-- p.747 -->

The following buttons are located on the toolbar.

                                                                                       ﾉ   Expand table

 Button                 Function

 New                    Opens a new script.

 Open                   Opens an existing script or file.

 Save                   Saves a script or file.

 Cut                    Cuts the selected text and copies it to the clipboard.

 Copy                   Copies the selected text to the clipboard.

 Paste                  Pastes the contents of the clipboard at the cursor location.

 Clear Console Pane     Clears all content in the Console Pane.

 Undo                   Reverses the action that was just performed.

 Redo                   Performs the action that was just undone.

 Run Script             Runs a script.

 Run Selection          Runs a selected portion of a script.

 Stop Operation         Stops a script that's running.

 New Remote             Creates a new PowerShell Tab that establishes a session on a remote computer. A
 PowerShell Tab         dialog box appears and prompts you to enter details required to establish the
                        remote connection.

 Start powershell.exe   Opens a PowerShell Console.

 Show Script Pane       Moves the Script Pane to the top in the display.
 Top

 Show Script Pane       Moves the Script Pane to the right in the display.
 Right

 Show Script Pane       Maximizes the Script Pane.
 Maximized

 Show Command           Shows the Commands Pane for installed Modules, as a separate Window.
 Window

<!-- p.748 -->

 Button                Function

 Show Command          Shows the Commands Pane for installed Modules, as a sidebar Add-on.
 Add-on

Windows PowerShell Tabs

A Windows PowerShell tab is the environment in which a Windows PowerShell script runs. You
can open new Windows PowerShell tabs in the Windows PowerShell ISE to create separate
environments on your local computer or on remote computers. You may have a maximum of
eight PowerShell tabs simultaneously open.

For more information, see How to Create a PowerShell Tab in Windows PowerShell ISE.

Script Tab

Displays the name of the script you are editing. You can click a script tab to select the script
you want to edit.

When you point to the script tab, the fully qualified path to the script file appears in a tooltip.

Script Pane

<!-- p.749 -->

Allows you to create and run scripts. You can open, edit and run existing scripts in the Script
Pane. For more information, see How to Write and Run Scripts in the Windows PowerShell ISE.

Console Pane
Displays the results of the commands and scripts you have run. You can run commands in the
Console pane. You can also copy and clear the contents in the Console Pane.

For more information, see the following articles:

     How to Use the Console Pane in the Windows PowerShell ISE
     How to Debug Scripts in Windows PowerShell ISE
     How to Use Tab Completion in the Script Pane and Console Pane

Status Bar
Allows you to see whether the commands and scripts that you run are complete. The status bar
is at the bottom of the window. Selected portions of error messages are displayed on the
status bar.

Text-Size Slider
Increases or decreases the size of the text on the screen.

<!-- p.750 -->

Help
Help for Windows PowerShell ISE is available on Microsoft Learn. You can open the Help by
clicking Windows PowerShell ISE Help on the Help menu or by pressing the F1 key anywhere
except when the cursor is on a cmdlet name in either the Script Pane or the Console Pane.
From the Help menu you can also run the Update-Help cmdlet, and display the Command
Window, which assists you in constructing commands by showing you all the parameters for a
cmdlet and enabling you to fill in the parameters in an easy-to-use form.

See Also
     Introducing the Windows PowerShell ISE
     How to Use Profiles in Windows PowerShell ISE
     Accessibility in Windows PowerShell ISE
     Keyboard Shortcuts for the Windows PowerShell ISE

Last updated on 11/20/2025

<!-- p.751 -->

How to Create a PowerShell Tab in
Windows PowerShell ISE
Tabs in the Windows PowerShell Integrated Scripting Environment (ISE) allow you to
simultaneously create and use several execution environments within the same application.
Each PowerShell tab corresponds to a separate execution environment or session.

  ７ Note

  Variables, functions, and aliases that you create in one tab don't carry over to another.
  They are different Windows PowerShell sessions.

Use the following steps to open or close a tab in Windows PowerShell. To rename a tab, set the
DisplayName property on the Windows PowerShell Tab scripting object.

To create and use a new PowerShell Tab
On the File menu, click New PowerShell Tab. The new PowerShell tab always opens as the
active window. PowerShell tabs are incrementally numbered in the order that they're opened.
Each tab is associated with its own Windows PowerShell console window. You can have up to
32 PowerShell tabs with their own session open at a time (this is limited to 8 on Windows
PowerShell ISE 2.0.)

Note that clicking the New or Open icons on the toolbar doesn't create a new tab with a
separate session. Instead, those buttons open a new or existing script file on the currently
active tab with a session. You can have multiple script files open with each tab and session. The
script tabs for a session only appear below the session tabs when the associated session is
active.

To make a PowerShell tab active, click the tab. To select from all PowerShell tabs that are open,
on the View menu, click the PowerShell tab you want to use.

To create and use a new Remote PowerShell tab
On the File menu, click New Remote PowerShell Tab to establish a session on a remote
computer. A dialog box appears and prompts you to enter details required to establish the
remote connection. The remote tab functions just like a local PowerShell tab, but the
commands and scripts are run on the remote computer.

<!-- p.752 -->

To close a PowerShell Tab
To close a tab, you can use any of the following techniques:

      Click the tab that you want to close.

      On the File menu, click Close PowerShell Tab, or click the Close button (X) on an active
      tab to close the tab.

If you have unsaved files open in the PowerShell tab that you are closing, you are prompted to
save or discard them. For more information about how to save a script, see How to Save a
Script.

See Also
      Introducing the Windows PowerShell ISE
      How to Use the Console Pane in the Windows PowerShell ISE

 Last updated on 11/20/2025

<!-- p.753 -->

How to Debug Scripts in Windows
PowerShell ISE
This article describes how to debug scripts on a local computer by using the Windows
PowerShell Integrated Scripting Environment (ISE) visual debugging features.

How to manage breakpoints
A breakpoint is a designated spot in a script where you would like operation to pause so that
you can examine the current state of the variables and the environment in which your script is
running. Once your script is paused by a breakpoint, you can run commands in the Console
Pane to examine the state of your script. You can output variables or run other commands. You
can even modify the value of any variables that are visible to the context of the currently
running script. After you have examined what you want to see, you can resume operation of
the script.

You can set three types of breakpoints in the Windows PowerShell debugging environment:

   1. Line breakpoint. The script pauses when the designated line is reached during the
      operation of the script

   2. Variable breakpoint. The script pauses whenever the designated variable's value changes.

   3. Command breakpoint. The script pauses whenever the designated command is about to
      be run during the operation of the script. It can include parameters to further filter the
      breakpoint to only the operation you want. The command can also be a function you
      created.

Of these, in the Windows PowerShell ISE debugging environment, only line breakpoints can be
set by using the menu or the keyboard shortcuts. The other two types of breakpoints can be
set, but they are set from the Console Pane by using the Set-PSBreakpoint cmdlet. This section
describes how you can perform debugging tasks in Windows PowerShell ISE by using the
menus where available, and perform a wider range of commands from the Console Pane by
using scripting.

To set a breakpoint
A breakpoint can be set in a script only after it has been saved. Right-click the line where you
want to set a line breakpoint, and then click Toggle Breakpoint. Or, click the line where you
want to set a line breakpoint, and press F9 or, on the Debug menu, click Toggle Breakpoint.

<!-- p.754 -->

The following script is an example of how you can set a variable breakpoint from the Console
Pane by using the Set-PSBreakpoint cmdlet.

 PowerShell

 # This command sets a breakpoint on the Server variable in the Sample.ps1 script.
 Set-PSBreakpoint -Script sample.ps1 -Variable Server

List all breakpoints
Displays all breakpoints in the current Windows PowerShell session.

On the Debug menu, click List Breakpoints. The following script is an example of how you can
list all breakpoints from the Console Pane by using the Get-PSBreakpoint cmdlet.

 PowerShell
 # This command lists all breakpoints in the current session.
 Get-PSBreakpoint

Remove a breakpoint
Removing a breakpoint deletes it.

If you think you might want to use it again later, consider Disable a Breakpoint it instead.
Right-click the line where you want to remove a breakpoint, and then click ToggleBreakpoint.
Or, click the line where you want to remove a breakpoint, and on the Debug menu, click
Toggle Breakpoint. The following script is an example of how to remove a breakpoint with a
specified ID from the Console Pane by using the Remove-PSBreakpoint cmdlet.

 PowerShell
 # This command deletes the breakpoint with breakpoint ID 2.
 Remove-PSBreakpoint -Id 2

Remove All Breakpoints
To remove all breakpoints defined in the current session, on the Debug menu, click Remove All
Breakpoints.

The following script is an example of how to remove all breakpoints from the Console Pane by
using the Remove-PSBreakpoint cmdlet.

<!-- p.755 -->

 PowerShell

 # This command deletes all of the breakpoints in the current session.
 Get-PSBreakpoint | Remove-PSBreakpoint

Disable a Breakpoint
Disabling a breakpoint doesn't remove it. It turns it off until it's enabled. To disable a specific
line breakpoint, right-click the line where you want to disable a breakpoint, and then click
Disable Breakpoint.

Or, click the line where you want to disable a breakpoint, and press F9 or, on the Debug
menu, click Disable Breakpoint. The following script is an example of how you can remove a
breakpoint with a specified ID from the Console Pane using the Disable-PSBreakpoint cmdlet.

 PowerShell

 # This command disables the breakpoint with breakpoint ID 0.
 Disable-PSBreakpoint -Id 0

Disable All Breakpoints
Disabling a breakpoint doesn't remove it; it turns it off until it's enabled. To disable all
breakpoints in the current session, on the Debug menu, click Disable all Breakpoints. The
following script is an example of how you can disable all breakpoints from the Console Pane by
using the Disable-PSBreakpoint cmdlet.

 PowerShell
 # This command disables all breakpoints in the current session.
 # You can abbreviate this command as: "gbp | dbp".
 Get-PSBreakpoint | Disable-PSBreakpoint

Enable a Breakpoint
To enable a specific breakpoint, right-click the line where you want to enable a breakpoint, and
then click Enable Breakpoint. Or, click the line where you want to enable a breakpoint, and
then press F9 or, on the Debug menu, click Enable Breakpoint. The following script is an
example of how you can enable specific breakpoints from the Console Pane by using the
Enable-PSBreakpoint cmdlet.

 PowerShell

<!-- p.756 -->

 # This command enables breakpoints with breakpoint IDs 0, 1, and 5.
 Enable-PSBreakpoint -Id 0, 1, 5

Enable All Breakpoints
To enable all breakpoints defined in the current session, on the Debug menu, click Enable all
Breakpoints. The following script is an example of how you can enable all breakpoints from the
Console Pane by using the Enable-PSBreakpoint cmdlet.

 PowerShell
 # This command enables all breakpoints in the current session.
 # You can abbreviate the command by using their aliases: "gbp | ebp".
 Get-PSBreakpoint | Enable-PSBreakpoint

How to manage a debugging session
Before you start debugging, you must set one or more breakpoints. You can't set a breakpoint
unless the script that you want to debug is saved. For directions on of how to set a breakpoint,
see How to manage breakpoints or Set-PSBreakpoint. After you start debugging, you can't edit
a script until you stop debugging. A script that has one or more breakpoints set is
automatically saved before it's run.

To start debugging
Press F5 or, on the toolbar, click the Run Script icon, or on the Debug menu click
Run/Continue. The script runs until it encounters the first breakpoint. It pauses operation there
and highlights the line on which it paused.

To continue debugging
Press F5 or, on the toolbar, click the Run Script icon, or on the Debug menu, click
Run/Continue or, in the Console Pane, type C and then press ENTER . This causes the script to
continue running to the next breakpoint or to the end of the script if no further breakpoints are
encountered.

To view the call stack
The call stack displays the current run location in the script. If the script is running in a function
that was called by a different function, then that's represented in the display by additional rows

<!-- p.757 -->

in the output. The bottom-most row displays the original script and the line in it in which a
function was called. The next line up shows that function and the line in it in which another
function might have been called. The top-most row shows the current context of the current
line on which the breakpoint is set.

While paused, to see the current call stack, press CTRL + SHIFT + D or, on the Debug menu, click
Display Call Stack or, in the Console Pane, type K and then press ENTER .

To stop debugging
Press SHIFT + F5 or, on the Debug menu, click Stop Debugger, or, in the Console Pane, type Q
and then press ENTER .

How to step over, step into, and step out while
debugging
Stepping is the process of running one statement at a time. You can stop on a line of code, and
examine the values of variables and the state of the system. The following table describes
common debugging tasks such as stepping over, stepping into, and stepping out.

                                                                                            ﾉ   Expand table

 Debugging     Description                                                  How to accomplish it in
 Task                                                                       PowerShell ISE

 Step Into     Executes the current statement and then stops at the         Press F11 or, on the Debug
               next statement. If the current statement is a function       menu, click Step Into, or in the
               or script call, then the debugger steps into that            Console Pane, type S and press
               function or script, otherwise it stops at the next           ENTER .
               statement.

 Step Over     Executes the current statement and then stops at the         Press F10 or, on the Debug
               next statement. If the current statement is a function       menu, click Step Over, or in the
               or script call, then the debugger executes the whole         Console Pane, type V and press
               function or script, and it stops at the next statement       ENTER .
               after the function call.

 Step Out      Steps out of the current function and up one level if        Press SHIFT + F11 , or on the
               the function is nested. If in the main body, the script is   Debug menu, click Step Out, or
               executed to the end, or to the next breakpoint. The          in the Console Pane, type O and
               skipped statements are executed, but not stepped             press ENTER .
               through.

 Continue      Continues execution to the end, or to the next               Press F5 or, on the Debug
               breakpoint. The skipped functions and invocations are        menu, click Run/Continue, or in

<!-- p.758 -->

 Debugging        Description                                           How to accomplish it in
 Task                                                                   PowerShell ISE

                  executed, but not stepped through.                    the Console Pane, type C and
                                                                        press ENTER .

How to display the values of variables while
debugging
You can display the current values of variables in the script as you step through the code.

To display the values of standard variables
Use one of the following methods:

        In the Script Pane, hover over the variable to display its value as a tool tip.

        In the Console Pane, type the variable name and press ENTER .

All panes in ISE are always in the same scope. Therefore, while you are debugging a script, the
commands that you type in the Console Pane run in script scope. This allows you to use the
Console Pane to find the values of variables and call functions that are defined only in the
script.

To display the values of automatic variables
You can use the preceding method to display the value of almost all variables while you are
debugging a script. However, these methods don't work for the following automatic variables.

        $_

        $input
        $MyInvocation

        $PSBoundParameters

        $args

If you try to display the value of any of these variables, you get the value of that variable for in
an internal pipeline the debugger uses, not the value of the variable in the script. You can work
around this for a few variables ( $_ , $input , $MyInvocation , $PSBoundParameters , and $args ) by
using the following method:

   1. In the script, assign the value of the automatic variable to a new variable.

<!-- p.759 -->

   2. Display the value of the new variable, either by hovering over the new variable in the
      Script Pane, or by typing the new variable in the Console Pane.

For example, to display the value of the $MyInvocation variable, in the script, assign the value
to a new variable, such as $scriptName , and then hover over or type the $scriptName variable
to display its value.

 PowerShell
 # In C:\ps-test\MyScript.ps1
 $scriptName = $MyInvocation.PSCommandPath

 PowerShell
 # In the Console Pane:
 .\MyScript.ps1
 $scriptName

 Output
 C:\ps-test\MyScript.ps1

See Also
Exploring the Windows PowerShell ISE

 Last updated on 11/20/2025

<!-- p.760 -->

How to Use Profiles in Windows PowerShell
ISE
This article explains how to use Profiles in Windows PowerShell® Integrated Scripting
Environment (ISE). We recommend that before performing the tasks in this section, you review
about_Profiles, or in the Console Pane, type, Get-Help about_Profiles and press ENTER .

A profile is a Windows PowerShell ISE script that runs automatically when you start a new
session. You can create one or more Windows PowerShell profiles for Windows PowerShell ISE
and use them to add the configure the Windows PowerShell or Windows PowerShell ISE
environment, preparing it for your use, with variables, aliases, functions, and color and font
preferences that you want available. A profile affects every Windows PowerShell ISE session
that you start.

  ７ Note

  The Windows PowerShell execution policy determines whether you can run scripts and
  load a profile. The default execution policy, "Restricted," prevents all scripts from running,
  including profiles. If you use the "Restricted" policy, the profile can't load. For more
  information about execution policy, see about_Execution_Policies.

Selecting a profile to use in the Windows
PowerShell ISE
Windows PowerShell ISE supports profiles for the current user and all users. It also supports the
Windows PowerShell profiles that apply to all hosts.

The profile that you use is determined by how you use Windows PowerShell and Windows
PowerShell ISE.

     If you use only Windows PowerShell ISE to run Windows PowerShell, then save all your
     items in one of the ISE-specific profiles, such as the CurrentUserCurrentHost profile for
     Windows PowerShell ISE or the AllUsersCurrentHost profile for Windows PowerShell ISE.

     If you use multiple host programs to run Windows PowerShell, save your functions,
     aliases, variables, and commands in a profile that affects all host programs, such as the
     CurrentUserAllHosts or the AllUsersAllHosts profile, and save ISE-specific features, like
     color and font customization in the CurrentUserCurrentHost profile for Windows
     PowerShell ISE profile or the AllUsersCurrentHost profile for Windows PowerShell ISE.
