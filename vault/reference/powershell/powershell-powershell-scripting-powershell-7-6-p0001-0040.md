---
title: "How to use this documentation — pages 1-40"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0001-0040
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0001-0040
family: powershell
documentKind: "doc"
abstract: "How to use the PowerShell documentation Welcome to the PowerShell online documentation. Features of the Learn platform The web page contains multiple elements that help you use and navigate the documentation. Navigation elements Site level navigation - The site level navigation"
---

# How to use this documentation — pages 1-40

<!-- p.1 -->

How to use the PowerShell documentation
Welcome to the PowerShell online documentation.

Features of the Learn platform
The web page contains multiple elements that help you use and navigate the documentation.

Navigation elements
     Site level navigation - The site level navigation appears at the top of the page. It contains
     links to other content on the Microsoft Learn platform.
     Related content navigation - The related content bar is immediately below the site level
     navigation. It contains links to content related to the current documentation set, which is
     PowerShell in this case.
     Article navigation - The article navigation appears at the top right of the article. It
     contains links to sections within the article.

Table of Contents

<!-- p.2 -->

     Version selector - The version selector appears above the Table of Contents (TOC) and
     controls which version of the cmdlet reference appears in the TOC.
     The Filter and search box allows you to quickly find articles in the TOC by filtering on
     words that appear in the title of an article.
     Conceptual content - The top section of the TOC contains conceptual articles that aren't
     version-specific.
     Cmdlet reference - The bottom section of the TOC contains the cmdlet reference for the
     version of PowerShell selected in the version selector.

Action and menu buttons
These buttons provide other ways of interacting with the content.

     The Ask Learn button opens an AI chat pane where you can ask questions and get help
     about the content.
     The Focus mode button hides the TOC and other distractions, allowing you to focus on
     the content.
     The Menu button provides a way to add content to a collection, provide feedback, edit
     the content, or share the content with others.

Feedback elements
There are two ways to provide feedback on the documentation.

     Anonymous feedback - The Was this helpful? section on the right side of the article
     allows you to provide a thumbs-up or thumbs-down rating. You can also enter more
     feedback in a text box.
     Feedback on GitHub - At the bottom of each article, you can provide feedback on the
     documentation or the product. These links take you to the GitHub repository where you
     can open an issue and give feedback.

Filter and search for articles
There are two ways to search for content in Docs.

     The filter and search box under the version selector allows filtering articles by words that
     appear in the title of an article or command aliases. The filter displays a list of matching
     articles as you type. You can also select the option to search for the words in the body of
     articles. When you search from here, the search is limited to the PowerShell
     documentation.

<!-- p.3 -->

     The search box in the site-level navigation bar searches the entire site. It returns a list of
     matching articles from all documentation sets.

In the following example, you see how the drop-down list is filtered to show the Get-ChildItem
command as you type the name. When you enter gci , the filter shows the Get-CimInstance
and Get-ChildItem commands because the alias for both commands starts with gci .

Next, the word idempotent is entered. The filter shows no articles. Clicking the search link
searches for idempotent in the PowerShell documentation. This search only returns 12 results.
Notice the difference when the same word is searched using the site-level search box. The
search returns 1,096 articles from the entire Microsoft Learn site.

Selecting the version of PowerShell
This site contains cmdlet reference for the following versions of PowerShell:

     PowerShell 7.6 (LTS)
     PowerShell 7.5
     PowerShell 7.4 (LTS)
     PowerShell 5.1

<!-- p.4 -->

Use the version selector located above the TOC to select the version of PowerShell you want.
By default, the page loads with the most current stable release version selected. The version
selector controls which version of the cmdlet reference appears in the TOC under the
Reference node. Some cmdlets work differently in different versions of PowerShell you're
using. Be sure you're viewing the documentation for the correct version of PowerShell.

The version selector doesn't affect conceptual documentation. The conceptual documents
appear above the Reference node in the TOC. The same conceptual articles appear for every
version selected. If there are version-specific differences, the documentation makes note of
those differences.

You can verify the version of PowerShell you're using by inspecting the
$PSVersionTable.PSVersion value. The following example shows the output for Windows

PowerShell 5.1.

 PowerShell

 $PSVersionTable.PSVersion

 Output

 Major    Minor   Build   Revision
 -----    -----   -----   --------
 5        1       26100   7705

Find articles for older versions of PowerShell

<!-- p.5 -->

Documentation for older versions of PowerShell is archived in our Previous Versions   site. You
can choose Previous Versions from the version selector.

The Previous versions option takes you to the site containing documentation for older and
unsupported versions of PowerShell:

     PowerShell 7.3
     PowerShell 7.2
     PowerShell 7.1
     PowerShell 7.0
     PowerShell 6
     PowerShell 5.0
        WMF 5.x Release notes
        PowerShell ISE object model
        PowerShell Workflows
        PowerShell Web Access
     PowerShell 4.0
     PowerShell 3.0

Download the documentation as a PDF
To download the documentation as a PDF, select the Download PDF button at the bottom of
the TOC.

<!-- p.6 -->

     If you're viewing a conceptual article, the Learn platform creates a PDF containing the
     conceptual content for the selected version.
     If you're viewing a reference article, the Learn platform creates a PDF containing the
     reference content for the selected version.

Last updated on 03/18/2026

<!-- p.7 -->

What is PowerShell?
PowerShell is a cross-platform task automation solution made up of a command-line shell, a
scripting language, and a configuration management framework. PowerShell runs on Windows,
Linux, and macOS.

Command-line Shell
PowerShell is a modern command shell that includes the best features of other popular shells.
Unlike most shells that only accept and return text, PowerShell accepts and returns .NET objects.
The shell includes the following features:

     Robust command-line history
     Tab completion and command prediction (See about_PSReadLine)
     Supports command and parameter aliases
     Pipeline for chaining commands
     In-console help system, similar to Unix man pages

Scripting language
As a scripting language, PowerShell is commonly used for automating the management of
systems. It's also used to build, test, and deploy solutions, often in CI/CD environments.
PowerShell is built on the .NET Common Language Runtime (CLR). All inputs and outputs are
.NET objects. No need to parse text output to extract information from output. The PowerShell
scripting language includes the following features:

     Extensible through functions, classes, scripts, and modules
     Extensible formatting system for easy output
     Extensible type system for creating dynamic types
     Built-in support for common data formats like CSV, JSON, and XML

Automation platform
The extensible nature of PowerShell provides an ecosystem of PowerShell modules to deploy and
manage almost any technology you work with. For example:

Microsoft modules

<!-- p.8 -->

       Azure
       Windows
       Exchange
       SQL

Third-party modules

       AWS
       VMware
       Oracle Cloud

Configuration management
PowerShell Desired State Configuration (DSC) is a management framework in PowerShell that
enables you to manage your enterprise infrastructure with configuration as code. With DSC, you
can:

       Create declarative configurations and custom scripts for repeatable deployments
       Enforce configuration settings and report on configuration drift
       Deploy configuration using push or pull models

Monad Manifesto
Jeffrey Snover, the inventor of PowerShell, wrote the Monad Manifesto to explain his vision for
PowerShell and how it would change the way we manage systems. Use the following link to
download a copy of the Monad Manifesto .

This PDF file is a version of the original Monad Manifesto, which articulated the long-term vision
and started the development effort that became PowerShell. PowerShell has delivered on many
of the elements described in this document.

Next steps
Getting started
Are you new to PowerShell and don't know where to start? Take a look at these resources.

       Install PowerShell
       Discover PowerShell
       PowerShell 101

<!-- p.9 -->

      Microsoft Virtual Academy videos
      PowerShell Learn modules

PowerShell in action
Take a look at how PowerShell is being used in different scenarios and on different platforms.

      PowerShell remoting over SSH
      Getting started with Azure PowerShell
      Building a CI/CD pipeline with DSC
      Managing Microsoft Exchange

 Last updated on 05/12/2026

<!-- p.10 -->

What is Windows PowerShell?
Windows PowerShell and PowerShell are two separate products.

     Windows PowerShell is the version of PowerShell that ships in Windows. This version of
     PowerShell uses the full .NET Framework, which only runs on Windows. The latest version
     is Windows PowerShell 5.1. Microsoft is no longer updating Windows PowerShell with
     new features. Support for Windows PowerShell is tied to the version of Windows you are
     using.

     PowerShell is built on the new versions of .NET instead of the .NET Framework and runs
     on Windows, Linux, and macOS. Support for PowerShell is based on the version of .NET
     that it was built on. For more information about the support lifecycle for PowerShell, see
     the PowerShell support lifecycle documentation.

Further reading
     For a more detailed explanation of the differences between Windows PowerShell and
     PowerShell, see Differences between Windows PowerShell 5.1 and PowerShell 7.x.
     For information about migrating from Windows PowerShell to PowerShell, see Migrating
     from Windows PowerShell 5.1 to PowerShell 7.
     For more information about previous versions of Windows PowerShell, see Previous
     versions of PowerShell.
     For more information about the terminology used in PowerShell documentation, see
     Product terminology and branding guidelines.

Last updated on 11/20/2025

<!-- p.11 -->

What is a command shell?
Many people use the terms command shell, command-line tool, and terminal interchangeably,
which can be confusing. This article explains the difference between these concepts and
provides examples of each.

A command shell is an interactive command-line interface for managing a computer, also
known as a Read-Eval-Print Loop (REPL      ).

A shell takes input from the keyboard, evaluates that input, and executes the input as a shell
command or forwards the input to the operating system to be executed. Most shells can also
read commands from a script file, and can include programming features like variables, flow
control, and functions.

Types of command shells
There are two main types of command shells:

     General purpose command shells

     General purpose command shells are designed to work with the operating system and
     allow you to run any command that the operating system supports. They also include
     shell-specific commands and programming features. The following list contains some
     examples of general purpose command shells:
        PowerShell
        Windows Command Shell
        bash    - popular on Linux
        zsh    - popular on macOS

     Utility command shells

     Utility command shells are designed to work with specific applications or services. These
     shells can only run commands that are specific to the application or service. Some utility
     shells support running commands from a batch script, but don't include programming
     features. Usually, these shells can only be used interactively.
        AI Shell - An interactive-only shell used to communicate with AI services such as Azure
        OpenAI.

<!-- p.12 -->

        netsh - Network shell (netsh) is a command-line utility that allows you to configure and
        display the status of various network components on Windows. It's both a command-
        line tool and a command shell. It also supports running commands from a script file.

Command-line tools
A command-line tool is a standalone program that you run from a command shell. Command-
line tools are typically designed to perform a specific task, such as managing files, configuring
settings, or querying for information. Command-line tools can be used in any shell that
supports running external programs.

     Azure CLI - a collection of command-line tools for managing Azure resources that can be
     run in any supported shell.
     Azure PowerShell - a collection of PowerShell modules for managing Azure resources that
     can be run in any supported version of PowerShell.
     OpenSSH for Windows - includes a command-line client and a server that provides secure
     communication over a network.
     Windows Commands - a collection of command-line tools that are built into Windows.

In general, command-line tools don't provide a command shell (REPL) interface. The netsh
command in Windows is an exception, as it's both a command-line tool and an interactive
command shell.

Terminals
A terminal is an application that provides a text-based window for hosting command shells.
Some terminals are designed to work with a specific shell, while others can host multiple shells.
They can also include advanced features such as:

     Ability to create multiple panes within a single window
     Ability to create multiple tabs to host multiple shells
     Ability to change color schemes and fonts
     Support for copy and paste operations

The following list contains some examples of terminal applications:

     Windows Terminal - a modern terminal application for Windows that can host multiple
     shells.
     Windows Console Host - the default host application on Windows for text-based
     applications. It can also host the Windows Command Shell or PowerShell.

<!-- p.13 -->

     Terminal for macOS       - the default terminal application on macOS that can host the bash
     or zsh shell.
     iTerm2 for macOS        - a popular 3rd-party terminal application for macOS.
     Azure Cloud Shell - a browser-based terminal application hosted in Microsoft Azure.
     Azure Cloud shell gives you the choice of using bash or PowerShell. Each shell comes
     preconfigured with many command-line tools for managing Azure resources.

Last updated on 07/07/2025

<!-- p.14 -->

What is a PowerShell command
(cmdlet)?
Article • 03/07/2024

Commands for PowerShell are known as cmdlets (pronounced command-lets). In
addition to cmdlets, PowerShell allows you to run any command available on your
system.

What is a cmdlet?
Cmdlets are native PowerShell commands, not stand-alone executables. Cmdlets are
collected into PowerShell modules that can be loaded on demand. Cmdlets can be
written in any compiled .NET language or in the PowerShell scripting language itself.

Cmdlet names
PowerShell uses a Verb-Noun name pair to name cmdlets. For example, the Get-Command
cmdlet included in PowerShell is used to get all the cmdlets that are registered in the
command shell. The verb identifies the action that the cmdlet performs, and the noun
identifies the resource on which the cmdlet performs its action.

Next steps
To learn more about PowerShell and how to find other cmdlets, see the PowerShell Bits
tutorial Discover PowerShell.

For more information about creating your own cmdlets, see the following resources:

Script-based cmdlets

      about_Functions_Advanced
      about_Functions_CmdletBindingAttribute
      about_Functions_Advanced_Methods

Compiled cmdlets (PowerShell SDK docs)

      Cmdlet overview

<!-- p.15 -->

Discover PowerShell
PowerShell is a command-line shell and a scripting language in one. PowerShell started out on
Windows to help automate administrative tasks. Now, it runs cross platform and can be used
for various tasks.

What makes PowerShell unique is that it accepts and returns .NET objects, rather than text. This
feature makes it easier to connect different commands in a pipeline.

What can PowerShell be used for?
Initially, PowerShell was Windows-only. Now, it's cross-platform and can be used for various
tasks like:

      Cloud management. PowerShell can be used to manage cloud resources. For example,
      you can retrieve information, update, or deploy new resources.
      CI/CD. It can also be used as part of a Continuous Integration/Continuous Deployment
      pipeline.
      Automate tasks for Active Directory and Exchange. You can use it to automate almost
      any task on Windows like creating users in Active Directory and mailboxes in Exchange.

Who uses PowerShell?
PowerShell is a powerful tool that can help people working in a multitude of roles. Traditionally,
PowerShell was used by the System Administrators. Now it's being used by people calling
themselves DevOps, Cloud Ops, and even Developers.

PowerShell cmdlets
PowerShell comes with hundreds of preinstalled commands. PowerShell commands are called
cmdlets (pronounced command-lets).

The name of each cmdlet consists of a Verb-Noun pair. For example, Get-Process . This naming
convention makes it easier to understand what the cmdlet does. It also makes it easier to find
the command you're looking for. When looking for a cmdlet to use, you can filter on the verb
or noun.

Using cmdlets to explore PowerShell

<!-- p.16 -->

When you first pick up PowerShell, it might feel intimidating as there seems to be so much to
learn. PowerShell is designed to help you learn a little at a time, as you need it.

PowerShell includes cmdlets that help you discover PowerShell. Using these four cmdlets, you
can discover what commands are available, what they do, and what types they operate on.

      Get-Verb . Running this command returns a list of verbs that most commands adhere to.

     The response includes a description of what these verbs do. Since most commands follow
     this naming convention, it sets expectations on what a command does. This command
     helps you select the appropriate verb and what to name a command when you create
     your own commands.
      Get-Command . This command retrieves a list of all commands installed on your machine.

      Get-Member . It operates on object based output and is able to discover what object,

     properties and methods are available for a command.
      Get-Help . Invoking this command with the name of a command as an argument displays

     a help page describing various parts of a command.

Using these commands, you can discover almost anything you need to know about PowerShell.

Verb
Verb is an important concept in PowerShell. It's a naming standard that most cmdlets follow.
It's also a naming standard you're expected to follow when you write your own commands. The
idea is that the Verb says what you're trying to do, like read or maybe change data. PowerShell
has a standardized list of verbs. To get a full list of all possible verbs, use the Get-Verb cmdlet:

 PowerShell

 Get-Verb

The cmdlet returns a long list of verbs. The Description provides context for what the verb is
meant to do. Here's the first few rows of output:

 Output

 Verb    AliasPrefix   Group     Description
 ----    -----------   -----     -----------
 Add     a             Common    Adds a resource to a container, or attaches an item
 to another item
 Clear   cl            Common    Removes all the resources from a container but does
 not delete the container
 Close   cs            Common    Changes the state of a resource to make it
 inaccessible, unavailable, or unusab…

<!-- p.17 -->

 Copy    cp            Common        Copies a resource to another name or to another
 container
 Enter   et            Common        Specifies an action that allows the user to move
 into a resource
 Exit    ex            Common        Sets the current environment or context to the most
 recently used context
 ...

Find commands with Get-Command
The Get-Command cmdlet returns a list of all available commands installed on your system. The
list can be large. You can limit the amount of information that comes back by filtering the
response using parameters or helper cmdlets.

Filter on name
You can filter the output of Get-Command using different parameters. Filtering allows you to find
commands that have certain properties. The Name parameter allows you to find a specific
command by name.

 PowerShell

 Get-Command -Name Get-Process

 Output

 CommandType       Name                Version      Source
 -----------       ----                -------      ------
 Cmdlet            Get-Process         7.0.0.0      Microsoft.PowerShell.Management

What if you want to find all the commands that work with processes? You can use a wildcard *
to match other forms of the string. For example:

 PowerShell

 Get-Command -Name *-Process

 Output

 CommandType       Name                Version      Source
 -----------       ----                -------      ------
 Cmdlet            Debug-Process       7.0.0.0      Microsoft.PowerShell.Management
 Cmdlet            Get-Process         7.0.0.0      Microsoft.PowerShell.Management
 Cmdlet            Start-Process       7.0.0.0      Microsoft.PowerShell.Management

<!-- p.18 -->

 Cmdlet             Stop-Process          7.0.0.0   Microsoft.PowerShell.Management
 Cmdlet             Wait-Process          7.0.0.0   Microsoft.PowerShell.Management

Filtering on Noun and Verb
There are other parameters that filter on verb and noun values. The verb part of a command's
name is the leftmost part. The verb should be one of the values returned by the Get-Verb
cmdlet. The rightmost part of a command is the noun part. A noun can be anything.

     Filter on verb. In the command Get-Process , the verb part is Get . To filter on the verb
     part, use the Verb parameter.

       PowerShell

       Get-Command -Verb 'Get'

     This example lists all commands that use the verb Get .

     Filter on noun. In the command Get-Process , the noun part is Process . To filter on the
     noun, use the Noun parameter. The following example returns all cmdlets that have
     nouns starting with the letter U .

       PowerShell

       Get-Command -Noun U*

Also, you can combine parameters to narrow down your search, for example:

 PowerShell

 Get-Command -Verb Get -Noun U*

 Output

 CommandType     Name                               Version     Source
 -----------     ----                               -------     ------
 Cmdlet          Get-UICulture                      7.0.0.0
 Microsoft.PowerShell.Utility
 Cmdlet          Get-Unique                         7.0.0.0
 Microsoft.PowerShell.Utility
 Cmdlet          Get-Uptime                         7.0.0.0
 Microsoft.PowerShell.Utility

Use helper cmdlets to filter results

<!-- p.19 -->

You can also use other cmdlets to filter results.

      Select-Object . This versatile command helps you pick out specific properties from one or

     more objects. You can also limit the number of items you get back. The following example
     returns the Name and Source property values for the first 5 commands available in the
     current session.

       PowerShell

       Get-Command | Select-Object -First 5 -Property Name, Source

       Output

       Name                      Source
       ----                      ------
       Add-AppPackage            Appx
       Add-AppPackageVolume      Appx
       Add-AppProvisionedPackage Dism
       Add-AssertionOperator     Pester
       Add-ProvisionedAppPackage Dism

     For more information, see Select-Object.

      Where-Object . This cmdlet lets you filter the objects returned based on the values of

     properties. The command takes an expression that can test the value of a property. The
     following example returns all processes where the ProcessName starts with p .

       PowerShell

       Get-Process | Where-Object {$_.ProcessName -like "p*"}

     The Get-Process cmdlet returns a collection of process objects. To filter the response,
     pipe the output to Where-Object . Piping means that two or more commands are
     connected via a pipe | character. The output from one command is sent as the input for
     the next command. The filter expression for Where-Object uses the -like operator to
     match processes that start with the letter p .

Explore objects with Get-Member
Once you locate the cmdlet you want, you want to know more about what output it produces.
The Get-Member cmdlet displays the type, properties, and methods of an object. Pipe the
output you want to inspect to Get-Member .

<!-- p.20 -->

 PowerShell

 Get-Process | Get-Member

The result displays the returned type as TypeName and all the properties and methods of the
object. Here's an excerpt of such a result:

 Output

 TypeName: System.Diagnostics.Process

 Name          MemberType       Definition
 ----          ----------       ----------
 Handles       AliasProperty    Handles = Handlecount
 Name          AliasProperty    Name = ProcessName
 ...

Using the MemberType parameter you can limit the information returned.

 PowerShell

 Get-Process | Get-Member -MemberType Method

By default PowerShell only displays a few properties. The previous example displayed the Name ,
MemberType , and Definition members. You can use Select-Object to specify properties you

want to see. For example, you want to display only the Name and Definition properties:

 PowerShell

 Get-Process | Get-Member | Select-Object Name, Definition

Search by parameter type
Get-Member showed us that Get-Process returns Process type objects. The ParameterType

parameter of Get-Command can be used to find other commands that take Process objects as
input.

 PowerShell

 Get-Command -ParameterType Process

 Output

<!-- p.21 -->

 CommandType     Name                          Version     Source
 -----------     ----                          -------     ------
 Cmdlet          Debug-Process                 7.0.0.0
 Microsoft.PowerShell.Managem…
 Cmdlet          Enter-PSHostProcess           7.1.0.0     Microsoft.PowerShell.Core
 Cmdlet          Get-Process                   7.0.0.0
 Microsoft.PowerShell.Managem…
 Cmdlet          Get-PSHostProcessInfo         7.1.0.0     Microsoft.PowerShell.Core
 Cmdlet          Stop-Process                  7.0.0.0
 Microsoft.PowerShell.Managem…
 Cmdlet          Wait-Process                  7.0.0.0
 Microsoft.PowerShell.Managem…

Knowing the output type of a command can help narrow down your search for related
commands.

Additional resources
     Get-Command
     Get-Member
     Select-Object

Last updated on 02/24/2026

<!-- p.22 -->

Install PowerShell on Windows, Linux,
and macOS
Learn how to install PowerShell on Windows, Linux, and macOS.

  Windows

  ｅ OVERVIEW
  Install PowerShell on Windows

  Install PowerShell on Windows IoT and Nano Server

  Supported Windows releases

  macOS

  ｅ OVERVIEW
  Install on macOS

  Supported macOS releases

  Alternate install methods

  Linux

  ｅ OVERVIEW
  Linux overview

  Alpine

  Debian

  Red Hat Enterprise Linux

  Ubuntu

<!-- p.23 -->

Q&A

ｂ GET STARTED
Alternate install methods

Community supported Linux

Using PowerShell in Docker

Arm Processor support

Microsoft Update FAQ for PowerShell

PowerShell Support Lifecycle

<!-- p.24 -->

Install PowerShell 7 on Windows
PowerShell 7 doesn't replace Windows PowerShell 5.1. It installs to a new directory and runs side-
by-side with Windows PowerShell 5.1. There are some Windows PowerShell modules that can be
run using the PowerShell 7 Windows Compatibility feature. Other modules require that you run
them in Windows PowerShell 5.1. For more information, see PowerShell 7 module compatibility.

There are multiple package versions of PowerShell 7 that can be installed. This article focuses on
installing the latest stable release package. For more information about the package versions, see
the PowerShell Support Lifecycle article.

Choose an installation method
There are multiple ways to install PowerShell in Windows. Each install method is designed to
support different scenarios and workflows. Choose the method that best suits your needs.

     WinGet - Recommended way to install PowerShell on Windows clients
     MSI package - Best choice for Windows Servers and enterprise deployment scenarios
     MSIX package - An easy way to install for casual users of PowerShell but has limitations
     ZIP package - Easiest way to side load or install multiple versions or install on Windows
     Server Core, Windows IoT, and Arm-based systems
     .NET Global tool - A good choice for .NET developers that install and use other global tools

Install PowerShell using WinGet
WinGet, the Windows Package Manager, is a command-line tool that enables you to discover,
install, upgrade, remove, and configure applications on Windows client computers. This tool is
the client interface to the Windows Package Manager service. The winget command-line tool is
included in Windows 11 and Windows Server 2025 as part of the App Installer. The winget
command can be run from any command shell, including the Windows Command shell
( cmd.exe ), Windows PowerShell ( powershell.exe ), or PowerShell ( pwsh.exe ).

  ７ Note

  See the winget documentation for a list of system requirements and install instructions.
  winget isn't available on Windows Server 2022 or earlier versions. Windows Server 2025

  includes winget for Windows Server with Desktop Experience only.

<!-- p.25 -->

Use the following winget commands to install PowerShell:

Search for the latest version of PowerShell

 PowerShell

 winget search --id Microsoft.PowerShell --exact

 Output

 Name               Id                           Version   Source
 -----------------------------------------------------------------
 PowerShell         Microsoft.PowerShell         7.6.4.0   winget

Beginning with the winget package for PowerShell 7.6.0, winget installs the MSIX package by
default.

Install the PowerShell 7 MSIX package:

 PowerShell

 winget install --id Microsoft.PowerShell --source winget

Use the following command to install the PowerShell 7 MSI package:

 PowerShell

 winget install --id Microsoft.PowerShell --source winget --installer-type wix

Alternatively, you can manually download and install the MSI package.

Use the following command to install PowerShell 7.7-preview packages:

 PowerShell

 winget install --id Microsoft.PowerShell.Preview --source winget

Beginning with the PowerShell 7.7.0 release, there is no MSI package available. WinGet only
installs the MSIX package.

Install the MSI package

<!-- p.26 -->

To install PowerShell on Windows, use the following links to download the install package from
GitHub.

Latest stable release:

     PowerShell-7.6.4-win-x64.msi
     PowerShell-7.6.4-win-arm64.msi

Once downloaded, double-click the installer file and follow the prompts.

Install the MSI package with command-line options
MSI packages can be installed from the command line allowing administrators to deploy
packages without user interaction. The MSI package includes the following properties to control
the installation options:

      USE_MU - This property has two possible values:

          1 (default) - Opts into updating through Microsoft Update, WSUS, or Configuration

          Manager
          0 - Don't opt into updating through Microsoft Update, WSUS, or Configuration Manager

      ENABLE_MU

          1 (default) - Opts into using Microsoft Update for Automatic Updates

          0 - Don't opt into using Microsoft Update

           ７ Note

           Enabling updates may have been set in a previous installation or manual
           configuration. Using ENABLE_MU=0 doesn't remove the existing settings. Also, this
           setting can be overruled by Group Policy settings controlled by your administrator.

      ADD_EXPLORER_CONTEXT_MENU_OPENPOWERSHELL - This property controls the option for adding

     the Open PowerShell item to the context menu in Windows Explorer.

      ADD_FILE_CONTEXT_MENU_RUNPOWERSHELL - This property controls the option for adding the Run

     with PowerShell item to the context menu in Windows Explorer.

      ENABLE_PSREMOTING - This property controls the option for enabling PowerShell remoting

     during installation.

<!-- p.27 -->

     REGISTER_MANIFEST - This property controls the option for registering the Windows Event

     Logging manifest.

     ADD_PATH - This property controls the option for adding PowerShell to the Windows PATH

     environment variable.

     DISABLE_TELEMETRY - This property controls the option for disabling PowerShell's telemetry

     by setting the POWERSHELL_TELEMETRY_OPTOUT environment variable.

     INSTALLFOLDER - This property controls the installation directory. The default is

     $Env:ProgramFiles\PowerShell\ . This is the location where the installer creates the versioned

     subfolder. You can't change the name of the versioned subfolder.
        For current releases, the versioned subfolder is 7
        For preview releases, the versioned subfolder is 7-preview

The following example shows how to silently install PowerShell with all the install options
enabled.

 PowerShell

 $msiParams = @(
     '/package PowerShell-7.6.4-win-x64.msi'
     '/quiet'
     'ADD_EXPLORER_CONTEXT_MENU_OPENPOWERSHELL=1'
     'ADD_FILE_CONTEXT_MENU_RUNPOWERSHELL=1'
     'ENABLE_PSREMOTING=1'
     'REGISTER_MANIFEST=1'
     'USE_MU=1'
     'ENABLE_MU=1'
     'ADD_PATH=1'
 )
 msiexec.exe @msiParams

For a full list of command-line options for Msiexec.exe , see Command line options.

Install the ZIP package
PowerShell binary ZIP archives are provided to enable advanced deployment scenarios.
Download one of the following ZIP archives from the current release      page.

     PowerShell-7.6.4-win-x64.zip
     PowerShell-7.6.4-win-arm64.zip

<!-- p.28 -->

Depending on how you download the file you may need to unblock the file using the Unblock-
File cmdlet. Unzip the contents to the location of your choice and run pwsh.exe from there.

Unlike installing the MSI packages, installing the ZIP archive doesn't check for prerequisites. For
remoting over WSMan to work properly, ensure that you've met the prerequisites.

Use this method to install the ARM-based version of PowerShell on computers like the Microsoft
Surface Pro X. For best results, install PowerShell to the $Env:ProgramFiles\PowerShell\7 folder. If
you are installing an additional version of PowerShell 7 side-by-side with an existing version of
PowerShell 7, install the additional version to a different folder. You must manually add a shortcut
to the Start Menu and add the location to the PATH environment variable.

Install as a .NET Global tool
If you already have the .NET Core SDK installed, you can install PowerShell as a .NET Global tool.

 dotnet tool install --global PowerShell

The dotnet tool installer adds $HOME\.dotnet\tools to your $Env:PATH environment variable.
However, the currently running shell doesn't have the updated $Env:PATH . You can start
PowerShell from a new shell by typing pwsh .

Install the MSIX package
PowerShell can be installed from the Microsoft Store     or by manually downloading the MSIX
package.

Benefits of the Microsoft Store package:

     Automatic updates built right into Windows
     Integrates with other software distribution mechanisms like Intune and Configuration
     Manager
     Can install on Windows systems using x64 or Arm64 processors

To manually install the MSIX package, download one of the following packages from the GitHub
releases page and double-click the file to install it.

     Next LTS - PowerShell-7.6.4.msixbundle
     Latest stable - PowerShell-7.5.9.msixbundle
     Current LTS - PowerShell-7.4.18.msixbundle

<!-- p.29 -->

     Current preview - PowerShellPreview-7.7.0-preview.3.msixbundle

Alternatively, you can use the following command to install the MSIX package from the
command line:

  PowerShell

  Add-AppxPackage -Path ".\PowerShell-7.6.4.msixbundle"

Limitations of a MSIX-based installation

Store-based installations are installed for a single user. There is no option to install it for all users.
Microsoft Store packages run in an application sandbox that virtualizes access to some filesystem
and registry locations. Changes to virtualized file and registry locations don't persist outside of
the application sandbox.

Store-based installations don't support PowerShell remoting. The application sandbox blocks all
changes to the application's root folder. Any system-level configuration settings stored in
$PSHOME can't be modified. This includes the WSMAN configuration. This prevents remote

sessions from connecting to Store-based installs of PowerShell. User-level configurations and SSH
remoting for outbound connections are supported.

The following commands aren't supported in a Microsoft Store instance of PowerShell. These
commands need write access to $PSHOME .

      Register-PSSessionConfiguration

      Update-Help -Scope AllUsers

      Enable-ExperimentalFeature -Scope AllUsers

      Set-ExecutionPolicy -Scope LocalMachine

For MSIX-based installations, you can't create or modify the all-users profile scripts
$PROFILE.AllUsersAllHosts and $PROFILE.AllUsersCurrentHost because those profiles must be

stored in $PSHOME . Current-user profiles are still supported.

The PowerShell package is exempt from file and registry virtualization. Changes to virtualized file
and registry locations now persist outside of the application sandbox. However, changes to the
application's root folder are still blocked.

For more information, see Understanding how packaged desktop apps run on Windows.

  ） Important

<!-- p.30 -->

  You must be running on Windows build 1903 or higher for this exemption to work.

Start PowerShell 7
After installing PowerShell 7, you can start it by running the pwsh command or open it from the
Start Menu. The installer creates shortcut entries in the Windows Start Menu.

By default, the installer installs the package in $Env:ProgramFiles\PowerShell\7 . Preview releases
of PowerShell 7 install to $Env:ProgramFiles\PowerShell\7-preview . The installed location is
added to your $Env:PATH environment variable.

  ７ Note

  To run PowerShell 7.5 side-by-side with other versions of PowerShell 7, use the ZIP install
  method to install the other version to a different folder. When you install using the ZIP
  method, you must manually add a shortcut to the Start Menu and add the location to the
  PATH environment variable.

The following screenshot shows multiple versions of PowerShell in the Start Menu. Select the item
labeled PowerShell 7.

<!-- p.31 -->

The selected entry is for PowerShell 7. Preview versions of PowerShell 7 install side-by-side with
stable versions. Select the item labeled PowerShell 7-preview to start the preview version.

The first and last entries shown are for Windows PowerShell 5.1, which are installed by default on
Windows. If you choose Windows PowerShell ISE, that starts the Windows PowerShell Integrated
Scripting Environment (ISE), which is a different application that only works with Windows
PowerShell 5.1.

Upgrade PowerShell 7
PowerShell 7 supports updates through Microsoft Update. When you enable this feature, you'll
get the latest PowerShell 7 updates in your traditional Microsoft Update (MU) management flow,
whether that's with Windows Update for Business, WSUS, Microsoft Endpoint Configuration
Manager, or the interactive MU dialog in Settings. For more information, see the PowerShell
Microsoft Update FAQ.

If you want to upgrade to the latest version of PowerShell 7 before it's available through
Microsoft Update, you should use the same install method you used when you first installed
PowerShell. Newer versions of PowerShell 7 replace existing previous versions of PowerShell 7.

<!-- p.32 -->

Preview versions of PowerShell can be installed side-by-side with non-preview versions of
PowerShell. Newer preview versions replace existing previous preview versions.

If you aren't sure how PowerShell was installed, you can check the value of the $PSHOME variable,
which always points to the directory containing PowerShell that the current session is running.

     If the value is $HOME\.dotnet\tools , PowerShell was installed with the .NET Global tool.
     If the value is $Env:ProgramFiles\PowerShell\7 , PowerShell was probably installed using the
     MSI package. You can verify this by looking for PowerShell in the Programs and Features
     Control Panel.
     If the value starts with $Env:ProgramFiles\WindowsApps\ , PowerShell was installed using the
     MSIX package.
     If the value is anything else, it's likely that PowerShell was installed as a ZIP package.

To determine whether PowerShell may be upgraded with WinGet, run the following command:

 PowerShell

 winget list --id Microsoft.PowerShell --upgrade-available

If there is an available upgrade, the output indicates the latest available version. Use the following
command to upgrade PowerShell using WinGet:

 PowerShell

 winget upgrade --id Microsoft.PowerShell

If available in the new version, WinGet uses the same package format (MSI or MSIX) that was
used to install the current version of PowerShell. Alternatively, you can manually download and
install the package you want.

Uninstall PowerShell 7
The process of uninstalling PowerShell 7 depends on the installation method you used.

     If you installed PowerShell using WinGet, run the following command:

       PowerShell

       winget uninstall --id Microsoft.PowerShell

<!-- p.33 -->

     If you installed PowerShell using the MSI package, you can uninstall it from the Programs
     and Features Control Panel.

     If you installed PowerShell using the ZIP package, delete the folder where you unzipped the
     files.

     If you installed PowerShell from the Microsoft Store, open the Start menu and search for
     PowerShell 7 . Select Uninstall from the menu of options.

     If you installed PowerShell as a .NET Global tool, run the following command:

       PowerShell

       dotnet tool uninstall --global PowerShell

Supported versions of Windows
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of
Windows reaches end-of-support.

The Docker images for the .NET SDK contain the latest versions of PowerShell. These images are
available from the Microsoft Artifact Registry   . These images may not have the latest security
updates. Microsoft recommends that you update the OS packages to the latest version to ensure
the latest security updates are applied. These images are provided for testing purposes. If you
need a Docker image for a production workload, you should build and maintain your own image.

  ７ Note

  Support for a specific version of Windows is determined by the Microsoft Support Lifecycle
  policies. For more information, see:

        Windows client lifecycle FAQ
        Modern Lifecycle Policy FAQ

You can check the version that you are using by running winver.exe .

Supported installation methods
Microsoft supports the installation methods in this document. There may be other third-party
methods of installation available from other sources. While those tools and methods may work,

<!-- p.34 -->

Microsoft can't support those methods.

  ７ Note

  The installation commands in this article are for the latest stable release of PowerShell. To
  install a different version of PowerShell, adjust the command to match the version you need.
  Open the Release tags page      on GitHub. Select the tag for the release version you want to
  install. The download links for every package are found in the Assets section of the release.
  The Assets section may be collapsed, so you may need to click to expand it.

Last updated on 07/20/2026

<!-- p.35 -->

PowerShell support for Linux
PowerShell can be installed on several different Linux distributions. Most Linux platforms and
distributions have a major release each year, and provide a package manager that's used to
install PowerShell. PowerShell can be installed on some distributions of Linux that aren't
supported by Microsoft. In those cases, you may find support from the community for
PowerShell on those platforms. For more information, see the PowerShell Support Lifecycle
documentation.

This article lists the supported Linux distributions and package managers. All PowerShell
releases remain supported until either the version of PowerShell or the version of the Linux
distribution reaches end-of-support.

For the best compatibility, choose a long-term release (LTS) version.

Alpine
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of
Alpine reaches end-of-life   .

Support for these versions of Alpine ends on the following dates:

     Alpine 3.23 - 2027-11-01
     Alpine 3.22 - 2027-05-01
     Alpine 3.21 - 2026-11-01
     Alpine 3.20 - 2026-04-01

The Docker images for the .NET SDK contain the latest versions of PowerShell. These images
are available from the Microsoft Artifact Registry   .

These images are built from official operating system (OS) images provided by the OS
distributor. These images may not have the latest security updates. Microsoft recommends that
you update the OS packages to the latest version to ensure the latest security updates are
applied.

These images are provided for testing purposes. If you need a Docker image for a production
workload, you should build and maintain your own.

For more information, see Install PowerShell on Alpine.

Debian
Debian uses APT (Advanced Package Tool) as a package manager.

<!-- p.36 -->

Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of
Debian reaches end-of-life    .

Support for these versions of Debian ends on the following dates:

     Debian 13 - 2028-08-09
     Debian 12 - 2026-06-10

Install package files ( .deb ) are also available from https://packages.microsoft.com/ .

The Docker images for the .NET SDK contain the latest versions of PowerShell. These images
are available from the Microsoft Artifact Registry   .

These images are built from official operating system (OS) images provide by the OS
distributor. These images may not have the latest security updates. Microsoft recommends that
you update the OS packages to the latest version to ensure the latest security updates are
applied.

These images are provided for testing purposes. If you need a Docker image for a production
workload, you should build and maintain your own.

For more information, see Install PowerShell on Debian.

Red Hat Enterprise Linux (RHEL)
RHEL 7 uses yum and RHEL 8 uses the dnf package manager.

Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of RHEL
reaches end-of-support    .

Support for these versions of RHEL ends on the following dates:

     RHEL 10 - 2035-05-31
     RHEL 9 - 2032-05-31
     RHEL 8 - 2029-05-31

Install package files ( .rpm ) are also available from https://packages.microsoft.com/ .

PowerShell is tested on Red Hat Universal Base Images (UBI). For more information, see the UBI
information page    .

For more information, see Install PowerShell on RHEL.

Ubuntu

<!-- p.37 -->

Ubuntu uses APT (Advanced Package Tool) as a package manager.

Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of
Ubuntu reaches end-of-support      .

Support for these versions of Ubuntu ends on the following dates:

     Ubuntu 24.04 - 2029-05-31
     Ubuntu 22.04 - 2027-04-01

Install package files ( .deb ) are also available from https://packages.microsoft.com/ .

The Docker images for the .NET SDK contain the latest versions of PowerShell. You can
download these images from the Microsoft Artifact Registry      .

These images are built from official operating system (OS) images provide by the OS
distributor. These images may not have the latest security updates. Microsoft recommends that
you update the OS packages to the latest version to ensure the latest security updates are
applied.

These images are provided for testing purposes. If you need a Docker image for a production
workload, you should build and maintain your own.

  ７ Note

  Ubuntu 25.10 (Questing Quokka) is an interim release. Microsoft doesn't test or support
  interim releases    of Ubuntu. For more information, see Community supported
  distributions.

For more information, see Install PowerShell on Ubuntu.

Community supported distributions
PowerShell can be installed on many distributions of Linux that aren't supported by Microsoft.
In those cases, you may find support from the community for PowerShell on those platforms.

To be supported by Microsoft, the Linux distribution must meet the following criteria:

     The version and architecture of the distribution is supported by .NET Core.
     The version of the distribution is supported for at least one year.
     The version of the distribution isn't an interim release or equivalent.
     The PowerShell team has tested the version of the distribution.

For more information, see Community support for PowerShell on Linux.

<!-- p.38 -->

Alternate installation methods
There are other ways to install PowerShell on Linux, including Linux distributions that aren't
officially supported. You can try to install PowerShell using the PowerShell Snap Package. You
can also try deploying PowerShell binaries directly using the Linux tar.gz package. For more
information, see Alternate ways to install PowerShell.

 Last updated on 03/31/2026

<!-- p.39 -->

Install PowerShell 7 on Alpine Linux
There are multiple package versions of PowerShell 7 that can be installed. This article focuses on
installing the latest stable release package. For more information about the package versions, see
the PowerShell Support Lifecycle article.

Newer versions of PowerShell 7 replace existing previous versions of PowerShell 7. Preview
versions of PowerShell can be installed side-by-side with other versions of PowerShell. Newer
preview versions replace existing previous preview versions. If you need to run PowerShell 7.5
side-by-side with a previous version, reinstall the previous version using the binary archive
method.

Install PowerShell 7
On Alpine Linux, PowerShell is installed from the tar.gz package downloaded from the
releases   page. Select the URL of the package version you want to install.

      PowerShell 7.6 (LTS) -
      https://github.com/PowerShell/PowerShell/releases/download/v7.6.4/powershell-7.6.4-

      linux-musl-x64.tar.gz

      PowerShell 7.5 -
      https://github.com/PowerShell/PowerShell/releases/download/v7.5.9/powershell-7.5.9-

      linux-musl-x64.tar.gz

      PowerShell 7.4 (LTS) -
      https://github.com/PowerShell/PowerShell/releases/download/v7.4.18/powershell-7.4.18-

      linux-musl-x64.tar.gz

Use the following shell commands to install PowerShell 7:

 sh

 #!/bin/bash
 # install the requirements
 sudo apk add --no-cache \
     ca-certificates \
     less \
     ncurses-terminfo-base \
     krb5-libs \
     libgcc \
     libintl \
     libssl3 \

<!-- p.40 -->

      libstdc++ \
      tzdata \
      userspace-rcu \
      zlib \
      icu-libs \
      curl

 apk -X https://dl-cdn.alpinelinux.org/alpine/edge/main add --no-cache \
     lttng-ust \
     openssh-client \

 # Download the powershell '.tar.gz' archive
 curl -L https://github.com/PowerShell/PowerShell/releases/download/v7.6.4/powershell-
 7.6.4-linux-musl-x64.tar.gz -o /tmp/powershell.tar.gz

 # Create the target folder where powershell will be placed
 sudo mkdir -p /opt/microsoft/powershell/7

 # Expand powershell to the target folder
 sudo tar zxf /tmp/powershell.tar.gz -C /opt/microsoft/powershell/7

 # Set execute permissions
 sudo chmod +x /opt/microsoft/powershell/7/pwsh

 # Create the symbolic link that points to pwsh
 sudo ln -s /opt/microsoft/powershell/7/pwsh /usr/bin/pwsh

 # Start PowerShell
 pwsh

Start PowerShell 7
After the package is installed, run pwsh from a terminal. If you have installed a Preview package,
run pwsh-preview .

     The location of $PSHOME varies based on the package you installed.
        For Stable and LTS packages: /opt/microsoft/powershell/7/
        For Preview packages: /opt/microsoft/powershell/7-preview/
     The profiles scripts are stored in the following locations:
        AllUsersAllHosts - $PSHOME/profile.ps1
        AllUsersCurrentHost - $PSHOME/Microsoft.PowerShell_profile.ps1
        CurrentUserAllHosts - ~/.config/powershell/profile.ps1
        CurrentUserCurrentHost - ~/.config/powershell/Microsoft.PowerShell_profile.ps1
     Modules are stored in the following locations:
        User modules - ~/.local/share/powershell/Modules
        Shared modules - /usr/local/share/powershell/Modules
        Default modules - $PSHOME/Modules
