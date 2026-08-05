---
title: "How to use this documentation — pages 1081-1120"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1081-1120
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1081-1120
family: powershell
documentKind: "doc"
abstract: "New-Item -Path 'src' -Type Directory New-Item -Path 'Output' -Type Directory New-Item -Path 'Tests' -Type Directory New-Item -Path $module -Type Directory Binary module setup This article is focused on the binary module so that's where we'll start. This section pulls examples fr"
---

# How to use this documentation — pages 1081-1120

<!-- p.1081 -->

 New-Item -Path 'src' -Type Directory
 New-Item -Path 'Output' -Type Directory
 New-Item -Path 'Tests' -Type Directory
 New-Item -Path $module -Type Directory

Binary module setup
This article is focused on the binary module so that's where we'll start. This section pulls
examples from the Creating a cross-platform binary module         guide. Review that guide if you
need more details or have any issues.

First thing we want to do is check the version of the dotnet core SDK      that we have installed.
I'm using 2.1.4, but you should have 2.0.0 or newer before continuing.

 PowerShell

 PS> dotnet --version
 2.1.4

I'm working out of the src folder for this section.

 PowerShell
 Set-Location 'src'

Using the dotnet command, create a new class library.

 PowerShell
 dotnet new classlib --name $module

This created the library project in a subfolder but I don't want that extra level of nesting. I'm
going to move those files up a level.

 PowerShell
 Move-Item -Path .\$module\* -Destination .\
 Remove-Item $module -Recurse

Set the .NET core SDK version for the project. I have the 2.1 SDK so I'm going to specify 2.1.0 .
Use 2.0.0 if you're using the 2.0 SDK.

 PowerShell

<!-- p.1082 -->

 dotnet new globaljson --sdk-version 2.1.0

Add the PowerShell Standard Library NuGet package           to the project. Make sure you use the
most recent version available for the level of compatibility that you need. I would default to the
latest version but I don't think this module leverages any features newer than PowerShell 3.0.

 PowerShell
 dotnet add package PowerShellStandard.Library --version 7.0.0-preview.1

We should have a src folder that looks like this:

 PowerShell
 PS> Get-ChildItem
     Directory: \MyModule\src

 Mode                  LastWriteTime                Length Name
 ----                  -------------                ------ ----
 d-----          7/14/2018   9:51 PM                       obj
 -a----          7/14/2018   9:51 PM                    86 Class1.cs
 -a----          7/14/2018 10:03 PM                    259 MyModule.csproj
 -a----          7/14/2018 10:05 PM                     45 global.json

Now we're ready to add our own code to the project.

Building a binary cmdlet
We need to update the src\Class1.cs to contain this starter cmdlet:

 C#
 using System;
 using System.Management.Automation;

 namespace MyModule
 {
     [Cmdlet( VerbsDiagnostic.Resolve , "MyCmdlet")]
     public class ResolveMyCmdletCommand : PSCmdlet
     {
         [Parameter(Position=0)]
         public Object InputObject { get; set; }

          protected override void EndProcessing()
          {
              this.WriteObject(this.InputObject);
              base.EndProcessing();
          }

<!-- p.1083 -->

     }
 }

Rename the file to match the class name.

 PowerShell
 Rename-Item .\Class1.cs .\ResolveMyCmdletCommand.cs

Then we can build our module.

 PowerShell
 PS> dotnet build

 Microsoft (R) Build Engine version 15.5.180.51428 for .NET Core
 Copyright (C) Microsoft Corporation. All rights reserved.

 Restore completed in 18.19 ms for C:\workspace\MyModule\src\MyModule.csproj.
 MyModule -> C:\workspace\MyModule\src\bin\Debug\netstandard2.0\MyModule.dll

 Build succeeded.
     0 Warning(s)
     0 Error(s)

 Time Elapsed 00:00:02.19

We can call Import-Module on the new dll to load our new cmdlet.

 PowerShell
 PS> Import-Module .\bin\Debug\netstandard2.0\$module.dll
 PS> Get-Command -Module $module

 CommandType Name                        Version Source
 ----------- ----                        ------- ------
 Cmdlet      Resolve-MyCmdlet            1.0.0.0 MyModule

If the import fails on your system, try updating .NET to 4.7.1 or newer. The Creating a cross-
platform binary module     guide goes into more details on .NET support and compatibility for
older versions of .NET.

Module manifest
It's cool that we can import the dll and have a working module. I like to keep going with it and
create a module manifest. We need the manifest if we want to publish to the PSGallery later.

<!-- p.1084 -->

From the root of our project, we can run this command to create the module manifest that we
need.

 PowerShell
 $manifestSplat = @{
     Path              = ".\$module\$module.psd1"
     Author            = 'Kevin Marquette'
     NestedModules     = @('bin\MyModule.dll')
     RootModule        = "$module.psm1"
     FunctionsToExport = @('Resolve-MyCmdlet')
 }
 New-ModuleManifest @manifestSplat

I'm also going to create an empty root module for future PowerShell functions.

 PowerShell
 Set-Content -Value '' -Path ".\$module\$module.psm1"

This allows me to mix both normal PowerShell functions and binary cmdlets in the same
project.

Building the full module
I compile everything together into an output folder. We need to create a build script to do that.
I would normally add this to an Invoke-Build script, but we can keep it simple for this example.
Add this to a build.ps1 at the root of the project.

 PowerShell

 $module = 'MyModule'
 Push-Location $PSScriptRoot

 dotnet build $PSScriptRoot\src -o $PSScriptRoot\output\$module\bin
 Copy-Item "$PSScriptRoot\$module\*" "$PSScriptRoot\output\$module" -Recurse -Force

 Import-Module "$PSScriptRoot\Output\$module\$module.psd1"
 Invoke-Pester "$PSScriptRoot\Tests"

These commands build our DLL and place it into our output\$module\bin folder. It then copies
the other module files into place.

 Output
 └───MyModule

<!-- p.1085 -->

      ├───MyModule.psd1
      ├───MyModule.psm1
      └───bin
          ├───MyModule.deps.json
          ├───MyModule.dll
          └───MyModule.pdb

At this point, we can import our module with the psd1 file.

 PowerShell
 Import-Module ".\Output\$module\$module.psd1"

From here, we can drop the .\Output\$module folder into our $Env:PSModulePath directory and
it autoloads our command whenever we need it.

Update: dotnet new PSModule
I learned that the dotnet tool has a PSModule template.

All the steps that I outlined above are still valid, but this template cuts many of them out. It's
still a fairly new template that's still getting some polish placed on it. Expect it to keep getting
better from here.

This is how you use install and use the PSModule template.

 PowerShell
 dotnet new -i Microsoft.PowerShell.Standard.Module.Template
 dotnet new psmodule
 dotnet build
 Import-Module "bin\Debug\netstandard2.0\$module.dll"
 Get-Module $module

This minimally-viable template takes care of adding the .NET SDK, PowerShell Standard Library,
and creates an example class in the project. You can build it and run it right away.

Important details
Before we end this article, here are a few other details worth mentioning.

Unloading DLLs
Once a binary module is loaded, you can't really unload it. The DLL file is locked until you
unload it. This can be annoying when developing because every time you make a change and

<!-- p.1086 -->

want to build it, the file is often locked. The only reliable way to resolve this is to close the
PowerShell session that loaded the DLL.

VS Code reload window action
I do most of my PowerShell dev work in VS Code . When I'm working on a binary module (or
a module with classes), I've gotten into the habit of reloading VS Code every time I build. Ctrl
+ Shift + P pops the command window and Reload Window is always at the top of my list.

Nested PowerShell sessions
One other option is to have good Pester test coverage. Then you can adjust the build.ps1 script
to start a new PowerShell session, perform the build, run the tests, and close the session.

Updating installed modules
This locking can be annoying when trying to update your locally installed module. If any
session has it loaded, you have to go hunt it down and close it. This is less of an issue when
installing from a PSGallery because module versioning places the new one in a different folder.

You can set up a local PSGallery and publish to that as part of your build. Then do your local
install from that PSGallery. This sounds like a lot of work, but this can be as simple as starting a
docker container. I cover a way to do that in my post on Using a NuGet server for a
PSRepository      .

Final thoughts
I didn't touch on the C# syntax for creating a cmdlet, but there is plenty of documentation on it
in the Windows PowerShell SDK. It's definitely something worth experimenting with as a
stepping stone into more serious C#.

 Last updated on 12/08/2025

<!-- p.1087 -->

Choosing the right PowerShell NuGet
package for your .NET project
Alongside the pwsh executable packages published with each PowerShell release, the
PowerShell team also maintains several packages available on NuGet      . These packages allow
targeting PowerShell as an API platform in .NET.

As a .NET application that provides APIs and expects to load .NET libraries implementing its
own (binary modules), it's essential that PowerShell be available in the form of a NuGet
package.

Currently there are several NuGet packages that provide some representation of the
PowerShell API surface area. Which package to use with a particular project isn't always clear.
This article sheds some light on a few common scenarios for PowerShell-targeting .NET
projects and how to choose the right NuGet package to target for your PowerShell-oriented
.NET project.

Hosting vs referencing
Some .NET projects seek to write code to be loaded into a preexisting PowerShell runtime
(such as pwsh , powershell.exe , the PowerShell Integrated Console, or the ISE), while others
want to run PowerShell in their own applications.

     Referencing is for when a project, usually a module, is intended to be loaded into
     PowerShell. You must compile the module against the APIs that PowerShell provides in
     order to interact with it. But PowerShell supplies the implementation by loading it in. A
     project can use reference assemblies or the actual runtime assemblies as a compilation
     target, but must ensure that it doesn't publish any of these assemblies with its build.
     Hosting is when a project needs its own implementation of PowerShell, usually because
     it's a standalone application that needs to run PowerShell. In this case, pure reference
     assemblies can't be used. Instead, a concrete PowerShell implementation must be
     depended upon. Because a concrete PowerShell implementation must be used, a specific
     version of PowerShell must be chosen for hosting; a single host application can't multi-
     target PowerShell versions.

Publishing projects that target PowerShell as a reference

  ７ Note

<!-- p.1088 -->

  We use the term publish in this article to refer to running dotnet publish , which places a
  .NET library into a directory with all of its dependencies, ready for deployment to a
  particular runtime.

Set the PrivateAssets attribute to prevent publishing project dependencies that are just being
used as compilation reference targets:

 XML
 <PackageReference Include="PowerShellStandard.Library" Version="5.1.0.0"
 PrivateAssets="all" />

If you don't set this attribute and use a reference assembly as your target, you can see issues
related to using the reference assembly's default implementation instead of the actual
implementation. For example, you can receive a NullReferenceException , since reference
assemblies often mock the implementation API by returning null .

Key kinds of PowerShell-targeting .NET projects
While any .NET library or application can embed PowerShell, there are some common scenarios
that use PowerShell APIs:

     Implementing a PowerShell binary module

     PowerShell binary modules are .NET libraries loaded by PowerShell that must implement
     PowerShell APIs like the PSCmdlet or CmdletProvider types in order to expose cmdlets or
     providers respectively. Because they're loaded in, modules seek to compile against
     references to PowerShell without publishing it in their build. It's also common for
     modules to want to support multiple PowerShell versions and platforms, ideally with a
     minimum of overhead of disk space, complexity, or repeated implementation. For more
     information, see about_Modules.

     Implementing a PowerShell Host

     A PowerShell Host provides an interaction layer for the PowerShell runtime. It's a specific
     form of hosting, where a PSHost is implemented as a new user interface to PowerShell.
     For example, the PowerShell ConsoleHost provides a terminal user interface for
     PowerShell executables, while the PowerShell Editor Services Host and the ISE Host both
     provide an editor-integrated partially graphical user interface around PowerShell. While
     it's possible to load a host onto an existing PowerShell process, it's much more common
     for a host implementation to act as a standalone PowerShell implementation that
     redistributes the PowerShell engine.

<!-- p.1089 -->

     Calling into PowerShell from another .NET application

     As with any application, you can call PowerShell as a subprocess to run workloads.
     However, as a .NET application, it's also possible to invoke PowerShell in-process to get
     back full .NET objects for use within the calling application. This is a more general form of
     hosting, where the application holds its own PowerShell implementation for internal use.
     For example, you could create a service or daemon running PowerShell to manage
     machine state, or a web application that runs PowerShell on request to do some work like
     managing cloud deployments.

     Unit testing PowerShell modules from .NET

     Usually, modules and other libraries designed to expose functionality to PowerShell
     should be tested from PowerShell. However, it's sometimes necessary to unit test APIs
     written for a PowerShell module from .NET.

PowerShell NuGet packages at a glance
The following NuGet packages expose PowerShell APIs:

     PowerShellStandard.Library , a reference assembly that enables building a single
     assembly that you can load in multiple PowerShell runtimes.
     Microsoft.PowerShell.SDK, the way to target and rehost the whole PowerShell SDK
     The System.Management.Automation              package, the core PowerShell runtime and
     engine implementation, that can be useful in minimal hosted implementations and for
     version-specific targeting scenarios.
     The Windows PowerShell reference assemblies, the way to target and effectively rehost
     Windows PowerShell (PowerShell versions 5.1 and below).

  ７ Note

  The PowerShell NuGet           package isn't a .NET library package at all, but instead provides
  the PowerShell dotnet global tool implementation. Don't use this package in any projects,
  since it only provides an executable.

PowerShellStandard.Library
The PowerShell Standard library is a reference assembly that captures the intersection of the
APIs of PowerShell v7 and v5.1. It provides a compile-time-checked API surface to compile .NET
code against, allowing .NET projects to target PowerShell v7 and v5.1 without risking calling an
API that that's not available.

<!-- p.1090 -->

Use PowerShell Standard to write PowerShell modules or other code only intended to be run
after loading it into a PowerShell process. Because it's a reference assembly, PowerShell
Standard contains no implementation itself, so it provides no functionality for standalone
applications.

Using PowerShell Standard with different .NET runtimes
PowerShell Standard targets the .NET Standard 2.0 target runtime, which is a façade runtime
designed to provide a common surface area shared by .NET Framework and .NET Core. It
allows you to target a single runtime to produce a single assembly that works with multiple
PowerShell versions, but has the following consequences:

     The PowerShell instance loading the module or library must be running a minimum of
     .NET 4.6.1; .NET 4.6 and .NET 4.5.2 don't support .NET Standard.

        ７ Note

        A newer Windows PowerShell version doesn't mean a newer .NET Framework
        version. Windows PowerShell 5.1 can run on .NET 4.5.2.

     To work with a PowerShell running .NET Framework 4.7.1 or below, the .NET 4.6.1
     NETStandard.Library       implementation is required to provide the netstandard.dll and
     other shim assemblies in older .NET Framework versions.

PowerShell 6 (and higher) provides its own shim assemblies for type forwarding from .NET
Framework 4.6.1 (and higher) to .NET Core. As long as a module uses only APIs that exist in
.NET Core, PowerShell 6 (and higher) can load and run it if it was built for .NET Framework 4.6.1
(the net461 runtime target).

Binary modules using PowerShell Standard to target multiple PowerShell versions with a single
published DLL have two options:

   1. Publishing an assembly built for the net461 target runtime involves:

           Publishing the project for the net461 runtime
           Also compiling against the netstandard2.0 runtime (without using its build output)
           to ensure that all APIs used are also present in .NET Core.

   2. Publishing an assembly build for the netstandard2.0 target runtime requires:

           Publishing the project for the netstandard2.0 runtime

<!-- p.1091 -->

             Taking the net461 dependencies of NETStandard.Library and copying them into the
             project assembly's publish location so that the assembly is type-forwarded corrected
             in .NET Framework.

To build PowerShell modules or libraries targeting older .NET Framework versions, you might
find it preferable to target multiple .NET runtimes. Doing so publishes an assembly for each
target runtime. The correct assembly must be loaded at module load time, for example with a
small .psm1 file as the root module.

Testing PowerShell Standard projects in .NET
When you test your module in .NET with test runners like xUnit, remember that compile-time
checks can only go so far. You must test your module against the relevant PowerShell
platforms.

To test APIs built against PowerShell Standard in .NET, you should add
Microsoft.PowerShell.SDK as a testing dependency with .NET Core (with the version set to

match the desired PowerShell version), and the appropriate Windows PowerShell reference
assemblies with .NET Framework.

For more information on PowerShell Standard and using it to write a binary module that works
in multiple PowerShell versions, see this blog post   . Also see the PowerShell Standard
repository     on GitHub.

Microsoft.PowerShell.SDK
Microsoft.PowerShell.SDK is a meta-package that pulls together all of the components of the

PowerShell SDK into a single NuGet package. A self-contained .NET application can use
Microsoft.PowerShell.SDK to run arbitrary PowerShell functionality without depending on any
external PowerShell installations or libraries.

  ７ Note

  The PowerShell SDK just refers to all the component packages that make up PowerShell,
  and which can be used for .NET development with PowerShell.

A given Microsoft.PowerShell.SDK version contains the concrete implementation of the same
version of the PowerShell application. Version 7.0 contains the implementation of PowerShell
7.0. Commands or scripts behave like running them in PowerShell 7.0. However, running
PowerShell commands from the SDK isn't the same as running them from pwsh . For example,

<!-- p.1092 -->

Start-Job depends on the pwsh executable being available, so it doesn't work with
Microsoft.PowerShell.SDK by default.

Targeting Microsoft.PowerShell.SDK from a .NET application allows you to integrate with all of
PowerShell's implementation assemblies, such as System.Management.Automation ,
Microsoft.PowerShell.Management , and other module assemblies.

Publishing an application targeting Microsoft.PowerShell.SDK includes all these assemblies,
and any dependencies PowerShell requires. It also includes other assets that PowerShell
required in its build, such as the module manifests for Microsoft.PowerShell.* modules and
the ref directory required by Add-Type.

Microsoft.PowerShell.SDK is best suited for:

     Implementation of PowerShell hosts.
     xUnit testing of libraries targeting PowerShell reference assemblies.
     Invoking PowerShell in-process from a .NET application.

You can use Microsoft.PowerShell.SDK as a reference target for a .NET project to create a
PowerShell module or assembly loaded by PowerShell that depends on APIs only present in a
particular version of PowerShell. An assembly published for a specific version of
Microsoft.PowerShell.SDK is only safe to load and use in that version of PowerShell. To target

multiple PowerShell versions with specific APIs, multiple builds are required, each targeting
their own version of Microsoft.PowerShell.SDK .

  ７ Note

  The PowerShell SDK is only available for PowerShell v6 and higher. To provide equivalent
  functionality with Windows PowerShell, use the Windows PowerShell reference assemblies
  described later in this article.

System.Management.Automation
The System.Management.Automation package is the heart of the PowerShell SDK. It exists on
NuGet, primarily, as an asset for Microsoft.PowerShell.SDK to pull in. However, it can also be
used directly as a package for smaller hosting scenarios and version-targeting modules.

Specifically, the System.Management.Automation package is the preferred when:

     You're only looking to use PowerShell language functionality from the
     System.Management.Automation.Language namespace, such as the PowerShell parser, AST,

<!-- p.1093 -->

     and AST visitor APIs.
     You only wish to execute specific commands from the Microsoft.PowerShell.Core module
     and can execute them in a session state created with the CreateDefault2 factory method.

Additionally, System.Management.Automation is a useful reference assembly when:

     You wish to target APIs that are only present within a specific PowerShell version
     You aren't depending on types occurring outside the System.Management.Automation
     assembly, such as types exported by cmdlets in Microsoft.PowerShell.* modules.

Windows PowerShell reference assemblies
For Windows PowerShell versions 5.1 and older, there's no SDK to provide an implementation
of PowerShell, since Windows PowerShell's implementation is a part of Windows. Instead, the
Windows PowerShell reference assemblies provide both reference targets and a way to rehost
Windows PowerShell, acting the same as the PowerShell SDK does for version 6 and higher.
Windows PowerShell reference assemblies have a different package for each version of
Windows PowerShell:

     PowerShell 5.1
     PowerShell 4
     PowerShell 3

You can find information about how to use the Windows PowerShell reference assemblies in
the Windows PowerShell SDK.

Real-world examples using these NuGet packages
Different PowerShell tooling projects target different PowerShell NuGet packages depending
on their needs. Listed here are some notable examples.

PSReadLine
PSReadLine    , the PowerShell module that provides much of PowerShell's rich console
experience, targets PowerShell Standard as a dependency rather than a specific PowerShell
version, and targets the net461 .NET runtime in its csproj   .

PowerShell v6 (and higher) supplies its own shim assemblies that allow a DLL targeting the
net461 runtime to just work when loaded. The shim simplifies the delivery and module layout

of PSReadLine. PowerShell Standard ensures that the module only uses APIs that are available

<!-- p.1094 -->

in both Windows PowerShell 5.1 and PowerShell 6 (and higher), which allows the module to
ship with only a single assembly.

The .NET 4.6.1 target does mean that Windows PowerShell running on .NET 4.5.2 and .NET 4.6
isn't supported though.

PowerShell Editor Services
PowerShell Editor Services    (PSES) is the backend for the PowerShell extension     for Visual
Studio Code    . This PowerShell module gets loaded by a PowerShell and then takes over that
process to rehost PowerShell within itself, while also providing Language Service Protocol and
Debug Adapter features.

PSES provides concrete implementation targets for netcoreapp2.1 to target PowerShell 6+
(since PowerShell 7's netcoreapp3.1 runtime is backwards compatible) and net461 to target
Windows PowerShell 5.1, but contains most of its logic in a second assembly that targets
netstandard2.0 and PowerShell Standard. This design allows it to pull in dependencies

required for .NET Core and .NET Framework platforms, while still simplifying most of the
codebase behind a uniform abstraction.

Because PSES targets PowerShell Standard, it requires a runtime implementation to be tested
correctly. To do this, PSES's xUnit   tests pull in Microsoft.PowerShell.SDK and
Microsoft.PowerShell.5.ReferenceAssemblies to provide a PowerShell implementation in the

test environment.

Since PSES can't support .NET 4.6 and older, it performs a check     at runtime before calling
any of the APIs that could cause a crash on the lower .NET Framework runtimes.

PSScriptAnalyzer
PSScriptAnalyzer    , the linter for PowerShell, must target syntactic elements only introduced in
certain versions of PowerShell. Because recognition of these syntactic elements is accomplished
by implementing an AstVisitor2, it's not possible to use PowerShellStandard and also
implement AST visitor methods for newer PowerShell syntaxes.

Instead, PSScriptAnalyzer targets each PowerShell version     as a build configuration and
produces a separate DLL for each version. This increases build size and complexity, but allows:

     Version-specific API targeting
     Version-specific functionality to be implemented with essentially no runtime cost
     Total support for Windows PowerShell running on .NET Framework 4.5.2 and higher

<!-- p.1095 -->

Summary
This article listed and discussed the NuGet packages you can target and the reasons for using
each one. The general recommendations are:

     PowerShell modules should compile against PowerShell Standard if they only require APIs
     common to different PowerShell versions.
     PowerShell hosts and applications that need to run PowerShell internally should target:
        The PowerShell SDK for PowerShell v6 and higher
        Or the relevant Windows PowerShell reference assemblies for Windows PowerShell
     PowerShell modules that need version-specific APIs should target the PowerShell SDK or
     Windows PowerShell reference assemblies for the required PowerShell versions. Use them
     as reference assemblies so you don't publish the PowerShell dependencies.

Last updated on 12/09/2025

<!-- p.1096 -->

Resolving PowerShell module assembly
dependency conflicts
When writing a binary PowerShell module in C#, it's natural to take dependencies on other
packages or libraries to provide functionality. Taking dependencies on other libraries is
desirable for code reuse. PowerShell always loads assemblies into the same context. This
presents issues when a module's dependencies conflict with already-loaded DLLs and may
prevent using two otherwise unrelated modules in the same PowerShell session.

If you've had this problem, you've seen an error message like this:

This article looks at some ways dependency conflicts occur in PowerShell and ways to mitigate
dependency conflict issues. Even if you're not a module author, there are some tricks in here
that might help you with dependency conflicts occurring in modules that you use.

Why do dependency conflicts occur?
In .NET, dependency conflicts occur when two versions of the same assembly are loaded into
the same Assembly Load Context. This term means slightly different things on different .NET
platforms, which is covered later in this article. This conflict is a common problem that occurs in
any software where versioned dependencies are used.

Conflict issues are compounded by the fact that a project almost never deliberately or directly
depends on two versions of the same dependency. Instead, the project has two or more
dependencies that each require a different version of the same dependency.

For example, say your .NET application, DuckBuilder , brings in two dependencies, to perform
parts of its functionality and looks like this:

<!-- p.1097 -->

Because Contoso.ZipTools and Fabrikam.FileHelpers both depend on different versions of
Newtonsoft.Json, there may be a dependency conflict depending on how each dependency is
loaded.

Conflicting with PowerShell's dependencies
In PowerShell, the dependency conflict issue is magnified because PowerShell's own
dependencies are loaded into the same shared context. This means the PowerShell engine and
all loaded PowerShell modules must not have conflicting dependencies. A classic example of
this is Newtonsoft.Json:

<!-- p.1098 -->

In this example, the module FictionalTools depends on Newtonsoft.Json version 12.0.3 ,
which is a newer version of Newtonsoft.Json than 11.0.2 that ships in the example PowerShell.

  ７ Note

  This is an example. PowerShell 7.0 currently ships with Newtonsoft.Json 12.0.3. Newer
  versions of PowerShell have newer versions of Newtonsoft.Json.

Because the module depends on a newer version of the assembly, it won't accept the version
that PowerShell already has loaded. But because PowerShell has already loaded a version of the
assembly, the module can't load its own version using the conventional load mechanism.

Conflicting with another module's dependencies

<!-- p.1099 -->

Another common scenario in PowerShell is that a module is loaded that depends on one
version of an assembly, and then another module is loaded later that depends on a different
version of that assembly.

This often looks like the following:

In this case, the FictionalTools module requires a newer version of
Microsoft.Extensions.Logging than the FilesystemManager module.

Imagine these modules load their dependencies by placing the dependency assemblies in the
same directory as the root module assembly. This allows .NET to implicitly load them by name.
If we're running PowerShell 7.0 (on top of .NET Core 3.1), we can load and run FictionalTools ,
then load and run FilesystemManager without issue. However, in a new session, if we load and
run FilesystemManager , then load FictionalTools , we get a FileLoadException from the
FictionalTools command because it requires a newer version of

Microsoft.Extensions.Logging than the one loaded. FictionalTools can't load the version

needed because an assembly of the same name has already been loaded.

PowerShell and .NET
PowerShell runs on the .NET platform, which is responsible for resolving and loading assembly
dependencies. We must understand how .NET operates here to understand dependency
conflicts.

<!-- p.1100 -->

We must also confront the fact that different versions of PowerShell run on different .NET
implementations. In general, PowerShell 5.1 and below run on .NET Framework, while
PowerShell 6 and above run on .NET Core. These two implementations of .NET load and handle
assemblies differently. This means that resolving dependency conflicts can vary depending on
the underlying .NET platform.

Assembly Load Contexts
In .NET, an Assembly Load Context (ALC) is a runtime namespace into which assemblies are
loaded. The assemblies' names must be unique. This concept allows assemblies to be uniquely
resolved by name in each ALC.

Assembly reference loading in .NET
The semantics of assembly loading depend on both the .NET implementation (.NET Core vs
.NET Framework) and the .NET API used to load a particular assembly. Rather than go into
detail here, there are links in the Further reading section that go into great detail on how .NET
assembly loading works in each .NET implementation.

In this article we'll refer to the following mechanisms:

     Implicit assembly loading (effectively Assembly.Load(AssemblyName) ), when .NET implicitly
     tries to load an assembly by name from a static assembly reference in .NET code.
      Assembly.LoadFrom() , a plugin-oriented loading API that adds handlers to resolve

     dependencies of the loaded DLL. This method may not resolve dependencies the way we
     want.
      Assembly.LoadFile() , a basic loading API intended to load only the assembly asked for

     and does not handle any dependencies.

Differences in .NET Framework vs .NET Core
The way these APIs work has changed in subtle ways between .NET Core and .NET Framework,
so it's worth reading through the included links. Importantly, Assembly Load Contexts and
other assembly resolution mechanisms have changed between .NET Framework and .NET Core.

In particular, .NET Framework has the following features:

     The Global Assembly Cache, for machine-wide assembly resolution
     Application Domains, which work like in-process sandboxes for assembly isolation, but
     also present a serialization layer to contend with

<!-- p.1101 -->

      A limited assembly load context model that has a fixed set of assembly load contexts,
      each with their own behavior:
        The default load context, where assemblies are loaded by default
        The load-from context, for loading assemblies manually at runtime
        The reflection-only context, for safely loading assemblies to read their metadata
        without running them
        The mysterious void that assemblies loaded with Assembly.LoadFile(string path) and
         Assembly.Load(byte[] asmBytes) live in

For more information, see Best Practices for Assembly Loading.

.NET Core (and .NET 5+) has replaced this complexity with a simpler model:

      No Global Assembly Cache. Applications bring all their own dependencies. This removes
      an external factor for dependency resolution in applications, making dependency
      resolution more reproducible. PowerShell, as the plugin host, complicates this slightly for
      modules. Its dependencies in $PSHOME are shared with all modules.
      Only one Application Domain, and no ability to create new ones. The Application Domain
      concept is maintained in .NET to be the global state of the .NET process.
      A new, extensible Assembly Load Context (ALC) model. Assembly resolution can be
      namespaced by putting it in a new ALC. .NET processes begin with a single default ALC
      into which all assemblies are loaded (except for those loaded with
      Assembly.LoadFile(string) and Assembly.Load(byte[]) ). But the process can create and

      define its own custom ALCs with its own loading logic. When an assembly is loaded, the
      first ALC it's loaded into is responsible for resolving its dependencies. This creates
      opportunities to implement powerful .NET plugin loading mechanisms.

In both implementations, assemblies are loaded lazily. This means that they're loaded when a
method requiring their type is run for the first time.

For example, here are two versions of the same code that load a dependency at different times.

The first always loads its dependency when Program.GetRange() is called, because the
dependency reference is lexically present within the method:

 C#

 using Dependency.Library;

 public static class Program
 {
     public static List<int> GetRange(int limit)

<!-- p.1102 -->

      {
          var list = new List<int>();
          for (int i = 0; i < limit; i++)
          {
              if (i >= 20)
              {
                  // Dependency.Library will be loaded when GetRange is run
                  // because the dependency call occurs directly within the method
                  DependencyApi.Use();
              }

              list.Add(i);
          }
          return list;
      }
 }

The second loads its dependency only if the limit parameter is 20 or more, because of the
internal indirection through a method:

 C#

 using Dependency.Library;

 public static class Program
 {
     public static List<int> GetNumbers(int limit)
     {
         var list = new List<int>();
         for (int i = 0; i < limit; i++)
         {
             if (i >= 20)
             {
                 // Dependency.Library is only referenced within
                 // the UseDependencyApi() method,
                 // so will only be loaded when limit >= 20
                 UseDependencyApi();
             }

              list.Add(i);
          }
          return list;
      }

      private static void UseDependencyApi()
      {
          // Once UseDependencyApi() is called, Dependency.Library is loaded
          DependencyApi.Use();
      }
 }

<!-- p.1103 -->

This is a good practice since it minimizes the memory and filesystem I/O and uses the
resources more efficiently. The unfortunate a side effect of this is that we won't know that the
assembly fails to load until we reach the code path that tries to load the assembly.

It can also create a timing condition for assembly load conflicts. If two parts of the same
program try to load different versions of the same assembly, the version loaded depends on
which code path is run first.

For PowerShell, this means that the following factors can affect an assembly load conflict:

     Which module was loaded first?
     Was the code path that uses the dependency library run?
     Does PowerShell load a conflicting dependency at startup or only under certain code
     paths?

Quick fixes and their limitations
In some cases, it's possible to make small adjustments to your module and fix things with
minimal effort. But these solutions tend to come with caveats. While they may apply to your
module, they won't work for every module.

Change your dependency version
The simplest way to avoid dependency conflicts is to agree on a dependency. This may be
possible when:

     Your conflict is with a direct dependency of your module and you control the version.
     Your conflict is with an indirect dependency, but you can configure your direct
     dependencies to use a workable indirect dependency version.
     You know the conflicting version and can rely on it not changing.

The Newtonsoft.Json package is a good example of this last scenario. This is a dependency of
PowerShell 6 and above, and isn't used in Windows PowerShell. Meaning a simple way to
resolve versioning conflicts is to target the lowest version of Newtonsoft.Json across the
PowerShell versions you wish to target.

For example, PowerShell 6.2.6 and PowerShell 7.0.2 both currently use Newtonsoft.Json version
12.0.3. To create a module targeting Windows PowerShell, PowerShell 6, and PowerShell 7, you
would target Newtonsoft.Json 12.0.3 as a dependency and include it in your built module.
When the module is loaded in PowerShell 6 or 7, PowerShell's own Newtonsoft.Json assembly

<!-- p.1104 -->

is already loaded. Since it's the version required for your module, resolution succeeds. In
Windows PowerShell, the assembly isn't already present in PowerShell, so it's loaded from your
module folder instead.

Generally, when targeting a concrete PowerShell package, like Microsoft.PowerShell.Sdk or
System.Management.Automation, NuGet should be able to resolve the right dependency
versions required. Targeting both Windows PowerShell and PowerShell 6+ becomes more
difficult because you must choose between targeting multiple frameworks or
PowerShellStandard.Library.

Circumstances where pinning to a common dependency version won't work include:

     The conflict is with an indirect dependency, and none of your dependencies can be
     configured to use a common version.
     The other dependency version is likely to change often, so settling on a common version
     is only a short-term fix.

Use the dependency out of process
This solution is more for module users than module authors. This is a solution to use when
confronted with a module that won't work due to an existing dependency conflict.

Dependency conflicts occur because two versions of the same assembly are loaded into the
same .NET process. A simple solution is to load them into different processes, as long as you
can still use the functionality from both together.

In PowerShell, there are several ways to achieve this:

     Invoke PowerShell as a subprocess

     To run a PowerShell command out of the current process, start a new PowerShell process
     directly with the command call:

       PowerShell

       pwsh -c 'Invoke-ConflictingCommand'

     The main limitation here is that restructuring the result can be trickier or more error
     prone than other options.

     The PowerShell job system

<!-- p.1105 -->

The PowerShell job system also runs commands out of process, by sending commands to
a new PowerShell process and returning the results:

 PowerShell

 $result = Start-Job { Invoke-ConflictingCommand } | Receive-Job -Wait

In this case, you just need to be sure that any variables and state are passed in correctly.

The job system can also be slightly cumbersome when running small commands.

PowerShell remoting

When it's available, PowerShell remoting can be a useful way to run commands out of
process. With remoting, you can create a fresh PSSession in a new process, call its
commands over PowerShell remoting, then use the results locally with the other modules
containing the conflicting dependencies.

An example might look like this:

 PowerShell

 # Create a local PowerShell session
 # where the module with conflicting assemblies will be loaded
 $s = New-PSSession

 # Import the module with the conflicting dependency via remoting,
 # exposing the commands locally
 Import-Module -PSSession $s -Name ConflictingModule

 # Run a command from the module with the conflicting dependencies
 Invoke-ConflictingCommand

Implicit remoting to Windows PowerShell

Another option in PowerShell 7 is to use the -UseWindowsPowerShell flag on Import-
Module . This imports the module through a local remoting session into Windows

PowerShell:

 PowerShell

 Import-Module -Name ConflictingModule -UseWindowsPowerShell

Be aware that modules may not be compatible with or may work differently with
Windows PowerShell.

<!-- p.1106 -->

When out-of-process invocation shouldn't be used

As a module author, out-of-process command invocation is difficult to bake into a module and
may have edge cases that cause issues. In particular, remoting and jobs may not be available in
all environments where your module needs to work. However, the general principle of moving
the implementation out of process and allowing the PowerShell module to be a thinner client,
may still be applicable.

As a module user, there are cases where out-of-process invocation won't work:

     When PowerShell remoting is unavailable because you don't have privileges to use it or it
     isn't enabled.
     When a particular .NET type is needed from output as input to a method or another
     command. Commands running over PowerShell remoting emit deserialized objects rather
     than strongly-typed .NET objects. This means that method calls and strongly typed APIs
     don't work with the output of commands imported over remoting.

More robust solutions
The previous solutions all had scenarios and modules that don't work. However, they also have
the virtue of being relatively simple to implement correctly. The following solutions are more
robust, but require more effort to implement correctly and can introduce subtle bugs if not
written carefully.

Loading through .NET Core Assembly Load Contexts
Assembly Load Contexts (ALCs) were introduced in .NET Core 1.0 to specifically address the
need to load multiple versions of the same assembly into the same runtime.

Within .NET, they offer the most robust solution to the problem of loading conflicting versions
of an assembly. However, custom ALCs aren't available in .NET Framework. This means that this
solution only works in PowerShell 6 and above.

Currently, the best example of using an ALC for dependency isolation in PowerShell is in
PowerShell Editor Services, the language server for the PowerShell extension for Visual Studio
Code. An ALC is used       to prevent PowerShell Editor Services' own dependencies from clashing
with those in PowerShell modules.

Implementing module dependency isolation with an ALC is conceptually difficult, but we will
work through a minimal example. Imagine we've a simple module that's only intended to work

<!-- p.1107 -->

in PowerShell 7. The source code is organized as follows:

 + AlcModule.psd1
 + src/
     + TestAlcModuleCommand.cs
     + AlcModule.csproj

The cmdlet implementation looks like this:

 C#

 using Shared.Dependency;

 namespace AlcModule
 {
     [Cmdlet(VerbsDiagnostic.Test, "AlcModule")]
     public class TestAlcModuleCommand : Cmdlet
     {
         protected override void EndProcessing()
         {
             // Here's where our dependency gets used
             Dependency.Use();
             // Something trivial to make our cmdlet do *something*
             WriteObject("done!");
         }
     }
 }

The (heavily simplified) manifest, looks like this:

 PowerShell

 @{
       Author = 'Me'
       ModuleVersion = '0.0.1'
       RootModule = 'AlcModule.dll'
       CmdletsToExport = @('Test-AlcModule')
       PowerShellVersion = '7.0'
 }

And the csproj looks like this:

 XML

 <Project Sdk="Microsoft.NET.Sdk">
   <PropertyGroup>
     <TargetFramework>netcoreapp3.1</TargetFramework>

<!-- p.1108 -->

   </PropertyGroup>
   <ItemGroup>
     <PackageReference Include="Shared.Dependency" Version="1.0.0" />
     <PackageReference Include="Microsoft.PowerShell.Sdk" Version="7.0.1"
 PrivateAssets="all" />
   </ItemGroup>
 </Project>

When we build this module, the generated output has the following layout:

 AlcModule/
   + AlcModule.psd1
   + AlcModule.dll
   + Shared.Dependency.dll

In this example, our problem is in the Shared.Dependency.dll assembly, which is our imaginary
conflicting dependency. This is the dependency that we need to put behind an ALC so that we
can use the module-specific version.

We need to re-engineer the module so that:

     Module dependencies are only loaded into our custom ALC, and not into PowerShell's
     ALC, so there can be no conflict. Moreover, as we add more dependencies to our project,
     we don't want to continuously add more code to keep loading working. Instead, we want
     reusable, generic dependency resolution logic.
     Loading the module still works as normal in PowerShell. Cmdlets and other types that the
     PowerShell module system needs are defined within PowerShell's own ALC.

To mediate these two requirements, we must break up our module into two assemblies:

     A cmdlets assembly, AlcModule.Cmdlets.dll , that contains definitions of all the types that
     PowerShell's module system needs to load our module correctly. Namely, any
     implementations of the Cmdlet base class and the class that implements
     IModuleAssemblyInitializer , which sets up the event handler for

     AssemblyLoadContext.Default.Resolving to properly load AlcModule.Engine.dll through

     our custom ALC. Since PowerShell 7 deliberately hides types defined in assemblies loaded
     in other ALCs, any types that are meant to be publicly exposed to PowerShell must also
     be defined here. Finally, our custom ALC definition needs to be defined in this assembly.
     Beyond that, as little code as possible should live in this assembly.
     An engine assembly, AlcModule.Engine.dll , that handles the actual implementation of
     the module. Types from this are available in the PowerShell ALC, but it's initially loaded

<!-- p.1109 -->

      through our custom ALC. Its dependencies are only loaded into the custom ALC.
      Effectively, this becomes a bridge between the two ALCs.

Using this bridge concept, our new assembly situation looks like this:

To make sure the default ALC's dependency probing logic doesn't resolve the dependencies to
be loaded into the custom ALC, we need to separate these two parts of the module in different
directories. The new module layout has the following structure:

 AlcModule/
   AlcModule.Cmdlets.dll
   AlcModule.psd1
   Dependencies/
   | + AlcModule.Engine.dll
   | + Shared.Dependency.dll

To see how the implementation changes, we'll start with the implementation of
AlcModule.Engine.dll :

 C#

 using Shared.Dependency;

 namespace AlcModule.Engine
 {
     public class AlcEngine
     {
         public static void Use()
         {
             Dependency.Use();

<!-- p.1110 -->

          }
      }
 }

This is a simple container for the dependency, Shared.Dependency.dll , but you should think of
it as the .NET API for your functionality that the cmdlets in the other assembly wrap for
PowerShell.

The cmdlet in AlcModule.Cmdlets.dll looks like this:

 C#

 // Reference our module's Engine implementation here
 using AlcModule.Engine;

 namespace AlcModule.Cmdlets
 {
     [Cmdlet(VerbsDiagnostic.Test, "AlcModule")]
     public class TestAlcModuleCommand : Cmdlet
     {
         protected override void EndProcessing()
         {
             AlcEngine.Use();
             WriteObject("done!");
         }
     }
 }

At this point, if we were to load AlcModule and run Test-AlcModule , we get a
FileNotFoundException when the default ALC tries to load Alc.Engine.dll to run
EndProcessing() . This is good, since it means the default ALC can't find the dependencies we

want to hide.

Now we need to add code to AlcModule.Cmdlets.dll so that it knows how to resolve
AlcModule.Engine.dll . First we must define our custom ALC to resolve assemblies from our

module's Dependencies directory:

 C#

 namespace AlcModule.Cmdlets
 {
     internal class AlcModuleAssemblyLoadContext : AssemblyLoadContext
     {
         private readonly string _dependencyDirPath;

          public AlcModuleAssemblyLoadContext(string dependencyDirPath)
          {
              _dependencyDirPath = dependencyDirPath;

<!-- p.1111 -->

            }

            protected override Assembly Load(AssemblyName assemblyName)
            {
                // We do the simple logic here of looking for an assembly of the given
 name
                // in the configured dependency directory.
                string assemblyPath = Path.Combine(
                    _dependencyDirPath,
                    $"{assemblyName.Name}.dll");

                if (File.Exists(assemblyPath))
                {
                    // The ALC must use inherited methods to load assemblies.
                    // Assembly.Load*() won't work here.
                    return LoadFromAssemblyPath(assemblyPath);
                }

                // For other assemblies, return null to allow other resolutions to
 continue.
                return null;
            }
        }
 }

Then we need to hook up our custom ALC to the default ALC's Resolving event, which is the
ALC version of the AssemblyResolve event on Application Domains. This event is fired to find
AlcModule.Engine.dll when EndProcessing() is called.

 C#

 namespace AlcModule.Cmdlets
 {
     public class AlcModuleResolveEventHandler : IModuleAssemblyInitializer,
 IModuleAssemblyCleanup
     {
         // Get the path of the dependency directory.
         // In this case we find it relative to the AlcModule.Cmdlets.dll location
         private static readonly string s_dependencyDirPath = Path.GetFullPath(
             Path.Combine(
                 Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location),
                 "Dependencies"));

            private static readonly AlcModuleAssemblyLoadContext s_dependencyAlc =
                new AlcModuleAssemblyLoadContext(s_dependencyDirPath);

            public void OnImport()
            {
                // Add the Resolving event handler here
                AssemblyLoadContext.Default.Resolving += ResolveAlcEngine;
            }

<!-- p.1112 -->

          public void OnRemove(PSModuleInfo psModuleInfo)
          {
              // Remove the Resolving event handler here
              AssemblyLoadContext.Default.Resolving -= ResolveAlcEngine;
          }

         private static Assembly ResolveAlcEngine(AssemblyLoadContext defaultAlc,
 AssemblyName assemblyToResolve)
         {
             // We only want to resolve the Alc.Engine.dll assembly here.
             // Because this will be loaded into the custom ALC,
             // all of *its* dependencies will be resolved
             // by the logic we defined for that ALC's implementation.
             //
             // Note that we're safe in our assumption that the name is enough
             // to distinguish our assembly here,
             // since it's unique to our module.
             // There should be no other AlcModule.Engine.dll on the system.
             if (!assemblyToResolve.Name.Equals("AlcModule.Engine"))
             {
                 return null;
             }

              // Allow our ALC to handle the directory discovery concept
              //
              // This is where Alc.Engine.dll is loaded into our custom ALC
              // and then passed through into PowerShell's ALC,
              // becoming the bridge between both
              return s_dependencyAlc.LoadFromAssemblyName(assemblyToResolve);
          }
      }
 }

With the new implementation, take a look at the sequence of calls that occurs when the
module is loaded and Test-AlcModule is run:

<!-- p.1113 -->

Some points of interest are:

     The IModuleAssemblyInitializer is run first when the module loads and sets the
     Resolving event.

     We don't load the dependencies until Test-AlcModule is run and its EndProcessing()
     method is called.
     When EndProcessing() is called, the default ALC fails to find AlcModule.Engine.dll and
     fires the Resolving event.
     Our event handler hooks up the custom ALC to the default ALC and loads
     AlcModule.Engine.dll only.

     When AlcEngine.Use() is called within AlcModule.Engine.dll , the custom ALC again kicks
     in to resolve Shared.Dependency.dll . Specifically, it always loads our
     Shared.Dependency.dll since it never conflicts with anything in the default ALC and only

     looks in our Dependencies directory.

Assembling the implementation, our new source code layout looks like this:

 + AlcModule.psd1
 + src/
   + AlcModule.Cmdlets/
   | + AlcModule.Cmdlets.csproj
   | + TestAlcModuleCommand.cs
   | + AlcModuleAssemblyLoadContext.cs
   | + AlcModuleInitializer.cs
   |
   + AlcModule.Engine/

<!-- p.1114 -->

    | + AlcModule.Engine.csproj
    | + AlcEngine.cs

AlcModule.Cmdlets.csproj looks like:

 XML

 <Project Sdk="Microsoft.NET.Sdk">
   <PropertyGroup>
     <TargetFramework>netcoreapp3.1</TargetFramework>
   </PropertyGroup>
   <ItemGroup>
     <ProjectReference Include="..\AlcModule.Engine\AlcModule.Engine.csproj" />
     <PackageReference Include="Microsoft.PowerShell.Sdk" Version="7.0.1"
 PrivateAssets="all" />
   </ItemGroup>
 </Project>

AlcModule.Engine.csproj looks like this:

 XML

 <Project Sdk="Microsoft.NET.Sdk">
   <PropertyGroup>
     <TargetFramework>netcoreapp3.1</TargetFramework>
   </PropertyGroup>
   <ItemGroup>
     <PackageReference Include="Shared.Dependency" Version="1.0.0" />
   </ItemGroup>
 </Project>

So, when we build the module, our strategy is:

     Build AlcModule.Engine
     Build AlcModule.Cmdlets
     Copy everything from AlcModule.Engine into the Dependencies directory, and remember
     what we copied
     Copy everything from AlcModule.Cmdlets that wasn't in AlcModule.Engine into the base
     module directory

Since the module layout here is so crucial to dependency separation, here's a build script to
use from the source root:

 PowerShell

 param(
     # The .NET build configuration

<!-- p.1115 -->

      [ValidateSet('Debug', 'Release')]
      [string]
      $Configuration = 'Debug'
 )

 # Convenient reusable constants
 $mod = "AlcModule"
 $netcore = "netcoreapp3.1"
 $copyExtensions = @('.dll', '.pdb')

 # Source code locations
 $src = "$PSScriptRoot/src"
 $engineSrc = "$src/$mod.Engine"
 $cmdletsSrc = "$src/$mod.Cmdlets"

 # Generated output locations
 $outDir = "$PSScriptRoot/out/$mod"
 $outDeps = "$outDir/Dependencies"

 # Build AlcModule.Engine
 Push-Location $engineSrc
 dotnet publish -c $Configuration
 Pop-Location

 # Build AlcModule.Cmdlets
 Push-Location $cmdletsSrc
 dotnet publish -c $Configuration
 Pop-Location

 # Ensure out directory exists and is clean
 Remove-Item -Path $outDir -Recurse -ErrorAction Ignore
 New-Item -Path $outDir -ItemType Directory
 New-Item -Path $outDeps -ItemType Directory

 # Copy manifest
 Copy-Item -Path "$PSScriptRoot/$mod.psd1"

 # Copy each Engine asset and remember it
 $deps = [System.Collections.Generic.Hashtable[string]]::new()
 Get-ChildItem -Path "$engineSrc/bin/$Configuration/$netcore/publish/" |
     Where-Object { $_.Extension -in $copyExtensions } |
     ForEach-Object { [void]$deps.Add($_.Name); Copy-Item -Path $_.FullName -
 Destination $outDeps }

 # Now copy each Cmdlets asset, not taking any found in Engine
 Get-ChildItem -Path "$cmdletsSrc/bin/$Configuration/$netcore/publish/" |
     Where-Object { -not $deps.Contains($_.Name) -and $_.Extension -in
 $copyExtensions } |
     ForEach-Object { Copy-Item -Path $_.FullName -Destination $outDir }

Finally, we've a general way to isolate our module's dependencies in an Assembly Load Context
that remains robust over time as more dependencies are added.

<!-- p.1116 -->

For a more detailed example, go to this GitHub repository . This example demonstrates how
to migrate a module to use an ALC, while keeping that module working in .NET Framework. It
also shows how to use .NET Standard and PowerShell Standard to simplify the core
implementation.

This solution is also used by the Bicep PowerShell module   , and the blog post Resolving
PowerShell Module Conflicts     is another good read about this solution.

Assembly resolving handler for side-by-side loading
Although being robust, the solution described above requires the module assembly to not
directly reference the dependency assemblies, but instead, reference a wrapper assembly that
references the dependency assemblies. The wrapper assembly acts like a bridge, forwarding
the calls from the module assembly to the dependency assemblies. This makes it usually a non-
trivial amount of work to adopt this solution:

     For a new module, this would add additional complexity to the design and
     implementation
     For an existing module, this would require significant refactoring

There is a simplified solution to achieve side-by-side assembly loading, by hooking up a
Resolving event with a custom AssemblyLoadContext instance. Using this method is easier for

the module author but has two limitations. Check out the PowerShell-ALC-Samples
repository for sample code and documentation that describes these limitations and detailed
scenarios for this solution.

  ） Important

  Don't use Assembly.LoadFile for the dependency isolation purpose. Using
   Assembly.LoadFile creates a Type Identity issue when another module loads a different

  version of the same assembly into the default AssemblyLoadContext . While this API loads
  an assembly to a separate AssemblyLoadContext instance, the assemblies loaded are
  discoverable by PowerShell's type resolution code    . Therefore, there could be duplicate
  types with the same fully qualifed type name available from two different ALCs.

Custom Application Domains
The final and most extreme option for assembly isolation is to use custom Application
Domains. Application Domains are only available in .NET Framework. They're used to provide

<!-- p.1117 -->

in-process isolation between parts of a .NET application. One of the uses is to isolate assembly
loads from each other within the same process.

However, Application Domainsare serialization boundaries. Objects in one application domain
can't be referenced and used directly by objects in another application domain. You can work
around this by implementing MarshalByRefObject . But when you don't control the types, as is
often the case with dependencies, it's not possible to force an implementation here. The only
solution is to make large architectural changes. The serialization boundary also has serious
performance implications.

Because Application Domains have this serious limitation, are complicated to implement, and
only work in .NET Framework, we won't give an example of how you might use them here.
While they're worth mentioning as a possibility, they're not recommended.

If you're interested in trying to use a custom application domain, the following links might
help:

        Conceptual documentation on Application Domains
        Examples for using Application Domains

Solutions for dependency conflicts that don't work
for PowerShell
Finally, we'll address some possibilities that come up when researching .NET dependency
conflicts in .NET that can look promising, but generally won't work for PowerShell.

These solutions have the common theme that they're changes to deployment configurations
for an environment where you control the application and possibly the entire machine. These
solutions are oriented toward scenarios like web servers and other applications deployed to
server environments, where the environment is intended to host the application and is free to
be configured by the deploying user. They also tend to be very much .NET Framework oriented,
meaning they don't work with PowerShell 6 or higher.

If you know that your module is only used in Windows PowerShell 5.1 environments that you
have total control over, some of these may be options. In general however, modules shouldn't
modify global machine state like this. It can break configurations that cause problems in
powershell.exe , other modules, or other dependent applications that cause your module to fail

in unexpected ways.

<!-- p.1118 -->

Static binding redirect with app.config to force using the
same dependency version
.NET Framework applications can take advantage of an app.config file to configure some
application behaviors declaratively. It's possible to write an app.config entry that configures
assembly binding to redirect assembly loading to a particular version.

Two issues with this for PowerShell are:

     .NET Core doesn't support app.config , so this solution only applies to powershell.exe .
     powershell.exe is a shared application that lives in the System32 directory. It's likely that

     your module won't be able to modify its contents on many systems. Even if it can,
     modifying the app.config could break an existing configuration or affect the loading of
     other modules.

Setting codebase with app.config
For the same reasons, trying to configure the codebase setting in app.config isn't going to
work in PowerShell modules.

Installing dependencies to the Global Assembly Cache (GAC)
Another way to resolve dependency version conflicts in .NET Framework is to install
dependencies to the GAC, so that different versions can be loaded side-by-side from the GAC.

Again, for PowerShell modules, the chief issues here are:

     The GAC only applies to .NET Framework, so this doesn't help in PowerShell 6 and above.
     Installing assemblies to the GAC is a modification of global machine state and may cause
     side-effects in other applications or to other modules. It may also be difficult to do
     correctly, even when your module has the required access privileges. Getting it wrong
     could cause serious, machine-wide issues in other .NET applications.

Further reading
There's plenty more to read on .NET assembly version dependency conflicts. Here are some
nice jumping off points:

     .NET: Assemblies in .NET
     .NET Core: The managed assembly loading algorithm

<!-- p.1119 -->

     .NET Core: Understanding System.Runtime.Loader.AssemblyLoadContext
     .NET Core: Discussion about side-by-side assembly loading solutions
     .NET Framework: Redirecting assembly versions
     .NET Framework: Best practices for assembly loading
     .NET Framework: How the runtime locates assemblies
     .NET Framework: Resolve assembly loads
     Stack Overflow: Assembly binding redirect, how and why?
     PowerShell: Discussion about implementing AssemblyLoadContexts
     PowerShell: Assembly.LoadFile() doesn't load into default AssemblyLoadContext
     Rick Strahl: When does a .NET assembly dependency get loaded?
     Jon Skeet: Summary of versioning in .NET
     Nate McMaster: Deep dive into .NET Core primitives

Last updated on 12/09/2025

<!-- p.1120 -->

How to create a command-line predictor
PSReadLine 2.1.0 introduced the concept of a smart command-line predictor by implementing
the Predictive IntelliSense feature. PSReadLine 2.2.2 expanded on that feature by adding a
plugin model that allows you create your own command-line predictors.

Predictive IntelliSense enhances tab completion by providing suggestions, on the command
line, as you type. The prediction suggestion appears as colored text following your cursor. This
enables you to discover, edit, and execute full commands based on matching predictions from
your command history or additional domain-specific plugins.

System requirements
To create and use a plugin predictor, you must be using the following versions of software:

     PowerShell 7.2 (or higher) - provides the APIs necessary for creating a command predictor
     PSReadLine 2.2.2 (or higher) - allows you to configure PSReadLine to use the plugin

Overview of a predictor
A predictor is a PowerShell binary module. The module must implement the
System.Management.Automation.Subsystem.Prediction.ICommandPredictor interface. This

interface declares the methods used to query for prediction results and provide feedback.

A predictor module must register a CommandPredictor subsystem with PowerShell's
SubsystemManager when loaded and unregister itself when unloaded.

The following diagram shows the architecture of a predictor in PowerShell.
