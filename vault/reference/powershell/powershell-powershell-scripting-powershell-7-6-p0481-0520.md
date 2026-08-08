---
title: "How to use this documentation — pages 481-520"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0481-0520
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0481-0520
family: powershell
documentKind: "doc"
abstract: "about RCW access. If you specify the Strict parameter and then create a COM object that uses an RCW, you get a warning message: PowerShell $xl = New-Object -ComObject Excel.Application -Strict Output New-Object : The object written to the pipeline is an instance of the type \"Mic"
---

# How to use this documentation — pages 481-520

<!-- p.481 -->

about RCW access. If you specify the Strict parameter and then create a COM object that uses
an RCW, you get a warning message:

  PowerShell

  $xl = New-Object -ComObject Excel.Application -Strict

  Output

  New-Object : The object written to the pipeline is an instance of the type "Mic
  rosoft.Office.Interop.Excel.ApplicationClass" from the component's primary interop
  assembly. If
  this type exposes different members than the IDispatch members , scripts written to
  work with this
  object might not work if the primary interop assembly isn't installed. At line:1
  char:17 + $xl =
  New-Object <<<< -ComObject Excel.Application -Strict

Although the object is still created, you are warned that it isn't a standard COM object.

 Last updated on 02/24/2025

<!-- p.482 -->

Using static classes and methods
Not all .NET Framework classes can be created using New-Object . For example, if you try to
create a System.Environment or a System.Math object with New-Object , you will get the
following error messages:

 PowerShell

 New-Object System.Environment

 Output

 New-Object : Constructor not found. Cannot find an appropriate constructor for
 type System.Environment.
 At line:1 char:11
 + New-Object <<<< System.Environment

 PowerShell

 New-Object System.Math

 Output

 New-Object : Constructor not found. Cannot find an appropriate constructor for
 type System.Math.
 At line:1 char:11
 + New-Object <<<< System.Math

These errors occur because there is no way to create a new object from these classes. These
classes are reference libraries of methods and properties that don't change state. You don't
need to create them, you simply use them. Classes and methods such as these are called static
classes because they're not created, destroyed, or changed. To make this clear we will provide
examples that use static classes.

Getting environment data with
System.Environment
Usually, the first step in working with an object in Windows PowerShell is to use Get-Member
to find out what members it contains. With static classes, the process is a little different

<!-- p.483 -->

because the actual class isn't an object.

Referring to the static System.Environment class
You can refer to a static class by surrounding the class name with square brackets. For example,
you can refer to System.Environment by typing the name within brackets. Doing so displays
some generic type information:

 PowerShell

 [System.Environment]

 Output

 IsPublic IsSerial Name                                           BaseType
 -------- -------- ----                                           --------
 True     False    Environment                                    System.Object

  ７ Note

  As we mentioned previously, Windows PowerShell automatically prepends 'System.' to
  type names when you use New-Object . The same thing happens when using a bracketed
  type name, so you can specify [System.Environment] as [Environment].

The System.Environment class contains general information about the working environment
for the current process, which is powershell.exe when working within Windows PowerShell.

If you try to view details of this class by typing [System.Environment] | Get-Member, the
object type is reported as being System.RuntimeType , not System.Environment:

 PowerShell

 [System.Environment] | Get-Member

 Output

     TypeName: System.RuntimeType

To view static members with Get-Member, specify the Static parameter:

 PowerShell

<!-- p.484 -->

 [System.Environment] | Get-Member -Static

 Output

     TypeName: System.Environment

 Name                          MemberType Definition
 ----                          ---------- ----------
 Equals                        Method     static System.Boolean Equals(Object ob...
 Exit                          Method     static System.Void Exit(Int32 exitCode)
 ...
 CommandLine                   Property    static System.String CommandLine {get;}
 CurrentDirectory              Property    static System.String CurrentDirectory ...
 ExitCode                      Property    static System.Int32 ExitCode {get;set;}
 HasShutdownStarted            Property    static System.Boolean HasShutdownStart...
 MachineName                   Property    static System.String MachineName {get;}
 NewLine                       Property    static System.String NewLine {get;}
 OSVersion                     Property    static System.OperatingSystem OSVersio...
 ProcessorCount                Property    static System.Int32 ProcessorCount {get;}
 StackTrace                    Property    static System.String StackTrace {get;}
 SystemDirectory               Property    static System.String SystemDirectory {...
 TickCount                     Property    static System.Int32 TickCount {get;}
 UserDomainName                Property    static System.String UserDomainName {g...
 UserInteractive               Property    static System.Boolean UserInteractive ...
 UserName                      Property    static System.String UserName {get;}
 Version                       Property    static System.Version Version {get;}
 WorkingSet                    Property    static System.Int64 WorkingSet {get;}
 TickCount                                   ExitCode

We can now select properties to view from System.Environment.

Displaying static properties of System.Environment
The properties of System.Environment are also static, and must be specified in a different way
than normal properties. We use :: to indicate to Windows PowerShell that we want to work
with a static method or property. To see the command that was used to launch Windows
PowerShell, we check the CommandLine property by typing:

 PowerShell

 [System.Environment]::CommandLine

 Output

 "C:\Program Files\Windows PowerShell\v1.0\powershell.exe"

<!-- p.485 -->

To check the operating system version, display the OSVersion property by typing:

 PowerShell

 [System.Environment]::OSVersion

 Output

              Platform ServicePack           Version              VersionString
              -------- -----------           -------              -------------
               Win32NT Service Pack 2        5.1.2600.131072      Microsoft Windows...

We can check whether the computer is in the process of shutting down by displaying the
HasShutdownStarted property:

 PowerShell

 [System.Environment]::HasShutdownStarted

 Output

 False

Doing math with System.Math
The System.Math static class is useful for performing some mathematical operations. The class
includes several useful methods, which we can display using Get-Member .

  ７ Note

  System.Math has several methods with the same name, but they're distinguished by the
  type of their parameters.

Type the following command to list the methods of the System.Math class.

 PowerShell

 [System.Math] | Get-Member -Static -MemberType Methods

 Output

<!-- p.486 -->

    TypeName: System.Math

 Name            MemberType Definition
 ----            ---------- ----------
 Abs             Method     static System.Single Abs(Single value), static Sy...
 Acos            Method     static System.Double Acos(Double d)
 Asin            Method     static System.Double Asin(Double d)
 Atan            Method     static System.Double Atan(Double d)
 Atan2           Method     static System.Double Atan2(Double y, Double x)
 BigMul          Method     static System.Int64 BigMul(Int32 a, Int32 b)
 Ceiling         Method     static System.Double Ceiling(Double a), static Sy...
 Cos             Method     static System.Double Cos(Double d)
 Cosh            Method     static System.Double Cosh(Double value)
 DivRem          Method     static System.Int32 DivRem(Int32 a, Int32 b, Int3...
 Equals          Method     static System.Boolean Equals(Object objA, Object ...
 Exp             Method     static System.Double Exp(Double d)
 Floor           Method     static System.Double Floor(Double d), static Syst...
 IEEERemainder   Method     static System.Double IEEERemainder(Double x, Doub...
 Log             Method     static System.Double Log(Double d), static System...
 Log10           Method     static System.Double Log10(Double d)
 Max             Method     static System.SByte Max(SByte val1, SByte val2), ...
 Min             Method     static System.SByte Min(SByte val1, SByte val2), ...
 Pow             Method     static System.Double Pow(Double x, Double y)
 ReferenceEquals Method     static System.Boolean ReferenceEquals(Object objA...
 Round           Method     static System.Double Round(Double a), static Syst...
 Sign            Method     static System.Int32 Sign(SByte value), static Sys...
 Sin             Method     static System.Double Sin(Double a)
 Sinh            Method     static System.Double Sinh(Double value)
 Sqrt            Method     static System.Double Sqrt(Double d)
 Tan             Method     static System.Double Tan(Double a)
 Tanh            Method     static System.Double Tanh(Double value)
 Truncate        Method     static System.Decimal Truncate(Decimal d), static...

This displays several mathematical methods. Here is a list of commands that demonstrate how
some of the common methods work:

 PowerShell

 [System.Math]::Sqrt(9)
 3
 [System.Math]::Pow(2,3)
 8
 [System.Math]::Floor(3.3)
 3
 [System.Math]::Floor(-3.3)
 -4
 [System.Math]::Ceiling(3.3)
 4
 [System.Math]::Ceiling(-3.3)
 -3
 [System.Math]::Max(2,7)
 7

<!-- p.487 -->

 [System.Math]::Min(2,7)
 2
 [System.Math]::Truncate(9.3)
 9
 [System.Math]::Truncate(-9.3)
 -9

Last updated on 03/24/2025

<!-- p.488 -->

Getting WMI objects with Get-CimInstance
  This sample only applies to Windows platforms.

Windows Management Instrumentation (WMI) is a core technology for Windows system
administration because it exposes a wide range of information in a uniform manner. Because of
how much WMI makes possible, the PowerShell cmdlet for accessing WMI objects, Get-
CimInstance , is one of the most useful for doing real work. We're going to discuss how to use

the CIM cmdlets to access WMI objects and then how to use WMI objects to do specific things.

Listing WMI classes
The first problem most WMI users face is trying to find out what can be done with WMI. WMI
classes describe the resources that can be managed. There are hundreds of WMI classes, some
of which contain dozens of properties.

Get-CimClass addresses this problem by making WMI discoverable. You can get a list of the

WMI classes available on the local computer by typing:

 PowerShell

 Get-CimClass -Namespace root/CIMV2 |
     Where-Object CimClassName -Like Win32* |
     Select-Object CimClassName

 Output

 CimClassName
 ------------
 Win32_DeviceChangeEvent
 Win32_SystemConfigurationChangeEvent
 Win32_VolumeChangeEvent
 Win32_SystemTrace
 Win32_ProcessTrace
 Win32_ProcessStartTrace
 Win32_ProcessStopTrace
 Win32_ThreadTrace
 Win32_ThreadStartTrace
 Win32_ThreadStopTrace
 ...

<!-- p.489 -->

You can retrieve the same information from a remote computer using the ComputerName
parameter, specifying a computer name or IP address:

 PowerShell

 Get-CimClass -Namespace root/CIMV2 -ComputerName 192.168.1.29

The class listing returned by remote computers may vary due to the specific operating system
the computer is running and the particular WMI extensions are added by installed applications.

  ７ Note

  When using CIM cmdlets to connect to a remote computer, the remote computer must be
  running WMI and the account you are using must be in the local Administrators group on
  the remote computer. The remote system doesn't need to have PowerShell installed. This
  allows you to administer operating systems that aren't running PowerShell, but do have
  WMI available.

Displaying WMI class details
If you already know the name of a WMI class, you can use it to get information immediately.
For example, one of the WMI classes commonly used for retrieving information about a
computer is Win32_OperatingSystem.

 PowerShell

 Get-CimInstance -Class Win32_OperatingSystem

 Output

 SystemDirectory     Organization BuildNumber RegisteredUser SerialNumber
 Version
 ---------------     ------------ ----------- -------------- ------------
 -------
 C:\WINDOWS\system32 Microsoft    22621       USER1          00330-80000-00000-AA175
 10.0.22621

Although we're showing all of the parameters, the command can be expressed in a more
succinct way. The ComputerName parameter isn't necessary when connecting to the local
system. We show it to demonstrate the most general case and remind you about the
parameter. The Namespace defaults to root/CIMV2, and can be omitted as well. Finally, most

<!-- p.490 -->

cmdlets allow you to omit the name of common parameters. With Get-CimInstance , if no name
is specified for the first parameter, PowerShell treats it as the Class parameter. This means the
last command could have been issued by typing:

 PowerShell

 Get-CimInstance Win32_OperatingSystem

The Win32_OperatingSystem class has many more properties than those displayed here. You
can use Get-Member to see all the properties. The properties of a WMI class are automatically
available like other object properties:

 PowerShell

 Get-CimInstance -Class Win32_OperatingSystem | Get-Member -MemberType Property

 Output

     TypeName:
 Microsoft.Management.Infrastructure.CimInstance#root/cimv2/Win32_OperatingSystem
 Name                                      MemberType Definition
 ----                                      ---------- ----------
 BootDevice                                Property   string BootDevice {get;}
 BuildNumber                               Property   string BuildNumber {get;}
 BuildType                                 Property   string BuildType {get;}
 Caption                                   Property   string Caption {get;}
 CodeSet                                   Property   string CodeSet {get;}
 CountryCode                               Property   string CountryCode {get;}
 CreationClassName                         Property   string CreationClassName
 {get;}
 CSCreationClassName                       Property   string CSCreationClassName
 {get;}
 CSDVersion                                Property   string CSDVersion {get;}
 CSName                                    Property   string CSName {get;}
 CurrentTimeZone                           Property   int16 CurrentTimeZone {get;}
 DataExecutionPrevention_32BitApplications Property   bool
 DataExecutionPrevention_32BitApplications {get;}
 DataExecutionPrevention_Available         Property   bool
 DataExecutionPrevention_Available {get;}
 ...

Displaying non-default properties with Format
cmdlets

<!-- p.491 -->

If you want the information contained in the Win32_OperatingSystem class that isn't displayed
by default, you can display it by using the Format cmdlets. For example, if you want to display
available memory data, type:

  PowerShell

  Get-CimInstance -Class Win32_OperatingSystem | Format-Table -Property
  TotalVirtualMemorySize, TotalVisibleMemorySize, FreePhysicalMemory,
  FreeVirtualMemory, FreeSpaceInPagingFiles

  Output

  TotalVirtualMemorySize TotalVisibleMemorySize FreePhysicalMemory FreeVirtualMemory
  FreeSpaceInPagingFiles
  ---------------------- ---------------------- ------------------ -----------------
  ----------------------
                41787920               16622096            9537952          33071884
  25056628

  ７ Note

  Wildcards work with property names in Format-Table , so the final pipeline element can be
  reduced to Format-Table -Property Total*Memory*, Free*

The memory data might be more readable if you format it as a list by typing:

  PowerShell

  Get-CimInstance -Class Win32_OperatingSystem | Format-List Total*Memory*, Free*

  Output

  TotalVirtualMemorySize : 41787920
  TotalVisibleMemorySize : 16622096
  FreePhysicalMemory     : 9365296
  FreeSpaceInPagingFiles : 25042952
  FreeVirtualMemory      : 33013484
  Name                   : Microsoft Windows 11
  Pro|C:\Windows|\Device\Harddisk0\Partition2

 Last updated on 03/24/2025

<!-- p.492 -->

Manipulating items directly
The elements that you see in PowerShell drives, such as the files and folders or registry keys,
are called Items in PowerShell. The cmdlets for working with them item have the noun Item in
their names.

The output of the Get-Command -Noun Item command shows that there are nine PowerShell
item cmdlets.

 PowerShell

 Get-Command -Noun Item

 Output

 CommandType       Name                                 Definition
 -----------       ----                                 ----------
 Cmdlet            Clear-Item                           Clear-Item [-Path] <String[]...
 Cmdlet            Copy-Item                            Copy-Item [-Path] <String[]>...
 Cmdlet            Get-Item                             Get-Item [-Path] <String[]> ...
 Cmdlet            Invoke-Item                          Invoke-Item [-Path] <String[...
 Cmdlet            Move-Item                            Move-Item [-Path] <String[]>...
 Cmdlet            New-Item                             New-Item [-Path] <String[]> ...
 Cmdlet            Remove-Item                          Remove-Item [-Path] <String[...
 Cmdlet            Rename-Item                          Rename-Item [-Path] <String>...
 Cmdlet            Set-Item                             Set-Item [-Path] <String[]> ...

Creating new items
To create a new item in the filesystem, use the New-Item cmdlet. Include the Path parameter
with path to the item, and the ItemType parameter with a value of File or Directory .

For example, to create a new directory named New.Directory in the C:\Temp directory, type:

 PowerShell

 New-Item -Path C:\temp\New.Directory -ItemType Directory

 Output

        Directory: Microsoft.PowerShell.Core\FileSystem::C:\temp

 Mode                   LastWriteTime       Length Name

<!-- p.493 -->

  ----                  -------------        ------ ----
  d----          2006-05-18 11:29 AM                New.Directory

To create a file, change the value of the ItemType parameter to File . For example, to create a
file named file1.txt in the New.Directory directory, type:

  PowerShell

  New-Item -Path C:\temp\New.Directory\file1.txt -ItemType File

  Output

        Directory: Microsoft.PowerShell.Core\FileSystem::C:\temp\New.Directory

  Mode                  LastWriteTime        Length Name
  ----                  -------------        ------ ----
  -a---          2006-05-18 11:44 AM              0 file1

You can use the same technique to create a new registry key. In fact, a registry key is easier to
create because the only item type in the Windows registry is a key. (Registry entries are item
properties.) For example, to create a key named _Test in the CurrentVersion subkey, type:

  PowerShell

  New-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\_Test

  Output

     Hive:
  Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\C
  urrentVersion

  SKC   VC Name                               Property
  ---   -- ----                               --------
    0    0 _Test                              {}

When typing a registry path, be sure to include the colon ( : ) in the PowerShell drive names,
HKLM: and HKCU: . Without the colon, PowerShell doesn't recognize the drive name in the path.

Why registry values aren't items
When you use the Get-ChildItem cmdlet to find the items in a registry key, you will never see
actual registry entries or their values.

<!-- p.494 -->

For example, the registry key
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run usually contains several

registry entries that represent applications that run when the system starts.

However, when you use Get-ChildItem to look for child items in the key, all you will see is the
OptionalComponents subkey of the key:

 PowerShell

 Get-ChildItem HKLM:\Software\Microsoft\Windows\CurrentVersion\Run

 Output

    Hive:
 Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\C
 urrentVersion\Run
 SKC VC Name                            Property
 --- -- ----                            --------
   3   0 OptionalComponents             {}

Although it would be convenient to treat registry entries as items, you can't specify a path to a
registry entry in a way that ensures that it's unique. The path notation doesn't distinguish
between the registry subkey named Run and the (Default) registry entry in the Run subkey.
Furthermore, because registry entry names can contain the backslash character ( \ ), if registry
entries were items, then you couldn't use the path notation to distinguish a registry entry
named Windows\CurrentVersion\Run from the subkey that's located in that path.

Renaming existing items
To change the name of a file or folder, use the Rename-Item cmdlet. The following command
changes the name of the file1.txt file to fileOne.txt .

 PowerShell

 Rename-Item -Path C:\temp\New.Directory\file1.txt fileOne.txt

The Rename-Item cmdlet can change the name of a file or a folder, but it can't move an item.
The following command fails because it attempts to move the file from the New.Directory
directory to the Temp directory.

 PowerShell

<!-- p.495 -->

 Rename-Item -Path C:\temp\New.Directory\fileOne.txt C:\temp\fileOne.txt

 Output

 Rename-Item : can't rename because the target specified isn't a path.
 At line:1 char:12
 + Rename-Item <<<< -Path C:\temp\New.Directory\fileOne C:\temp\fileOne.txt

Moving items
To move a file or folder, use the Move-Item cmdlet.

For example, the following command moves the New.Directory directory from the C:\temp
directory to the root of the C: drive. To verify that the item was moved, include the PassThru
parameter of the Move-Item cmdlet. Without PassThru, the Move-Item cmdlet doesn't display
any results.

 PowerShell

 Move-Item -Path C:\temp\New.Directory -Destination C:\ -PassThru

 Output

      Directory: Microsoft.PowerShell.Core\FileSystem::C:\

 Mode                  LastWriteTime        Length Name
 ----                  -------------        ------ ----
 d----          2006-05-18 12:14 PM                New.Directory

Copying items
If you are familiar with the copy operations in other shells, you might find the behavior of the
Copy-Item cmdlet in PowerShell to be unusual. When you copy an item from one location to

another, Copy-Item doesn't copy its contents by default.

For example, if you copy the New.Directory directory from the C: drive to the C:\temp
directory, the command succeeds, but the files in the New.Directory directory aren't copied.

 PowerShell

 Copy-Item -Path C:\New.Directory -Destination C:\temp

<!-- p.496 -->

If you display the contents of C:\temp\New.Directory , you will find that it contains no files:

  PS> Get-ChildItem -Path C:\temp\New.Directory
  PS>

Why doesn't the Copy-Item cmdlet copy the contents to the new location?

The Copy-Item cmdlet was designed to be generic; it isn't just for copying files and folders.
Also, even when copying files and folders, you might want to copy only the container and not
the items within it.

To copy all of the contents of a folder, include the Recurse parameter of the Copy-Item cmdlet
in the command. If you have already copied the directory without its contents, add the Force
parameter, which allows you to overwrite the empty folder.

  PowerShell

  Copy-Item -Path C:\New.Directory -Destination C:\temp -Recurse -Force -PassThru

  Output

      Directory: Microsoft.PowerShell.Core\FileSystem::C:\temp

  Mode                  LastWriteTime        Length Name
  ----                  -------------        ------ ----
  d----          2006-05-18   1:53 PM               New.Directory

      Directory: Microsoft.PowerShell.Core\FileSystem::C:\temp\New.Directory

  Mode                  LastWriteTime        Length Name
  ----                  -------------        ------ ----
  -a---          2006-05-18 11:44 AM              0 file1

Deleting items
To delete files and folders, use the Remove-Item cmdlet. PowerShell cmdlets, such as Remove-
Item , that can make significant, irreversible changes will often prompt for confirmation when

you enter its commands. For example, if you try to remove the New.Directory folder, you will
be prompted to confirm the command, because the folder contains files:

  PowerShell

<!-- p.497 -->

 Remove-Item C:\temp\New.Directory

 Output

 Confirm
 The item at C:\temp\New.Directory has children and the -Recurse parameter was not
 specified. If you continue, all children will be removed with the item. Are you
  sure you want to continue?
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help
 (default is "Y"):

Because Yes is the default response, to delete the folder and its files, press the Enter key. To
remove the folder without confirming, use the Recurse parameter.

 PowerShell

 Remove-Item C:\temp\New.Directory -Recurse

Executing items
PowerShell uses the Invoke-Item cmdlet to perform a default action for a file or folder. This
default action is determined by the default application handler in the registry; the effect is the
same as if you double-click the item in File Explorer.

For example, suppose you run the following command:

 PowerShell

 Invoke-Item C:\WINDOWS

An Explorer window that's located in C:\Windows appears, just as if you had double-clicked the
C:\Windows folder.

If you invoke the Boot.ini file on a system prior to Windows Vista:

 PowerShell

 Invoke-Item C:\boot.ini

If the .ini file type is associated with Notepad, the boot.ini file opens in Notepad.

<!-- p.498 -->

Last updated on 03/24/2025

<!-- p.499 -->

Changing computer state
Article • 12/18/2023

  This sample only applies to Windows platforms.

To reset a computer in PowerShell, use either a standard command-line tool, WMI, or a
CIM class. Although you are using PowerShell only to run the tool, learning how to
change a computer's power state in PowerShell illustrates some of the important details
about working with external tools in PowerShell.

Locking a computer
The only way to lock a computer directly with the standard available tools is to call the
LockWorkstation() function in user32.dll:

  PowerShell

  rundll32.exe user32.dll,LockWorkStation

This command immediately locks the workstation. It uses rundll32.exe to call the
LockWorkStation function in user32.dll .

When you lock a workstation while Fast User Switching is enabled, such as on Windows
XP, the computer displays the user logon screen rather than starting the current user's
screensaver.

To shut down particular sessions on a Terminal Server, use the tsshutdn.exe command-
line tool.

Logging off the current session
You can use several different techniques to log off of a session on the local system. The
simplest way is to use the Remote Desktop/Terminal Services command-line tool,
logoff.exe (For details, at the PowerShell prompt, type logoff /? ). To log off the current
active session, type logoff with no arguments.

You can also use the shutdown.exe tool with its logoff option:

  PowerShell

<!-- p.500 -->

  shutdown.exe -l

Another option is to use WMI. The Win32_OperatingSystem class has a Shutdown
method. Invoking the method with the 0 flag initiates logoff:

For more information, see the Shutdown method of the Win32_OperatingSystem class.

  PowerShell

  Get-CimInstance -ClassName Win32_OperatingSystem | Invoke-CimMethod -
  MethodName Shutdown

Shutting down or restarting a computer
Shutting down and restarting computers are similar tasks. Most command-line tools
support both actions. Windows includes two command-line tools for restarting a
computer. Use either tsshutdn.exe or shutdown.exe with appropriate arguments. You
can get detailed usage information from tsshutdn.exe /? or shutdown.exe /? .

You can also perform shutdown and restart operations directly from PowerShell.

To shut down the computer, use the Stop-Computer command

  PowerShell

  Stop-Computer

To restart the operating system, use the Restart-Computer command

  PowerShell

  Restart-Computer

To force an immediate restart of the computer, use the -Force parameter.

  PowerShell

  Restart-Computer -Force

<!-- p.501 -->

Collecting information about computers
Article • 12/09/2022

  This sample only applies to Windows platforms.

Cmdlets from CimCmdlets module are the most important cmdlets for general system
management tasks. All critical subsystem settings are exposed through WMI.
Furthermore, WMI treats data as objects that are in collections of one or more items.
Because PowerShell also works with objects and has a pipeline that allows you to treat
single or multiple objects in the same way, generic WMI access allows you to perform
some advanced tasks with very little work.

Listing desktop settings
We'll begin with a command that collects information about the desktops on the local
computer.

  PowerShell

  Get-CimInstance -ClassName Win32_Desktop

This returns information for all desktops, whether they're in use or not.

  ７ Note

  Information returned by some WMI classes can be very detailed, and often include
  metadata about the WMI class.

Because most of these metadata properties have names that begin with Cim, you can
filter the properties using Select-Object . Specify the -ExcludeProperty parameter with
"Cim*" as the value. For example:

  PowerShell

  Get-CimInstance -ClassName Win32_Desktop | Select-Object -ExcludeProperty
  "CIM*"

To filter out the metadata, use a pipeline operator (|) to send the results of the Get-
CimInstance command to Select-Object -ExcludeProperty "CIM*" .

<!-- p.502 -->

Listing BIOS Information
The WMI Win32_BIOS class returns fairly compact and complete information about the
system BIOS on the local computer:

  PowerShell

  Get-CimInstance -ClassName Win32_BIOS

Listing Processor Information
You can retrieve general processor information by using WMI's Win32_Processor class,
although you will likely want to filter the information:

  PowerShell

  Get-CimInstance -ClassName Win32_Processor | Select-Object -ExcludeProperty
  "CIM*"

For a generic description string of the processor family, you can just return the
SystemType property:

  PowerShell

  Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -Property
  SystemType

  SystemType
  ----------
  X86-based PC

Listing computer manufacturer and model
Computer model information is also available from Win32_ComputerSystem. The
standard displayed output will not need any filtering to provide OEM data:

  PowerShell

  Get-CimInstance -ClassName Win32_ComputerSystem

  Output

<!-- p.503 -->

  Name PrimaryOwnerName Domain    TotalPhysicalMemory Model
  Manufacturer
  ---- ---------------- ------    ------------------- -----
  ------------
  MyPC Jane Doe         WORKGROUP 804765696           DA243A-ABA 6415cl NA910
  Compaq Presario 06

Your output from commands such as this, which return information directly from some
hardware, is only as good as the data you have. Some information isn't correctly
configured by hardware manufacturers and may therefore be unavailable.

Listing installed hotfixes
You can list all installed hotfixes by using Win32_QuickFixEngineering:

  PowerShell

  Get-CimInstance -ClassName Win32_QuickFixEngineering

This class returns a list of hotfixes that looks like this:

  Output

  Source Description     HotFixID InstalledBy    InstalledOn PSComputerName
  ------ -----------     -------- -----------    ----------- --------------
         Security Update KB4048951 Administrator 12/16/2017 .

For more succinct output, you may want to exclude some properties. Although you can
use the Get-CimInstance 's Property parameter to choose only the HotFixID, doing so
will actually return more information, because all the metadata is displayed by default:

  PowerShell

  Get-CimInstance -ClassName Win32_QuickFixEngineering -Property HotFixID

  Output

  InstalledOn                :
  Caption                    :
  Description                :
  InstallDate                :
  Name                       :
  Status                     :
  CSName                     :

<!-- p.504 -->

  FixComments           :
  HotFixID              : KB4533002
  InstalledBy           :
  ServicePackInEffect   :
  PSComputerName        :
  CimClass              : root/cimv2:Win32_QuickFixEngineering
  CimInstanceProperties : {Caption, Description, InstallDate, Name…}
  CimSystemProperties   :
  Microsoft.Management.Infrastructure.CimSystemProperties
  ...

The additional data is returned, because the Property parameter in Get-CimInstance
restricts the properties returned from WMI class instances, not the object returned to
PowerShell. To reduce the output, use Select-Object :

  PowerShell

  Get-CimInstance -ClassName Win32_QuickFixEngineering -Property HotFixId |
      Select-Object -Property HotFixId

  Output

  HotFixId
  --------
  KB4048951

Listing operating system version information
The Win32_OperatingSystem class properties include version and service pack
information. You can explicitly select only these properties to get a version information
summary from Win32_OperatingSystem:

  PowerShell

  Get-CimInstance -ClassName Win32_OperatingSystem |
    Select-Object -Property
  BuildNumber,BuildType,OSType,ServicePackMajorVersion,ServicePackMinorVersion

You can also use wildcards with the Property parameter. Because all the properties
beginning with either Build or ServicePack are important to use here, we can shorten
this to the following form:

  PowerShell

<!-- p.505 -->

  Get-CimInstance -ClassName Win32_OperatingSystem |
      Select-Object -Property Build*,OSType,ServicePack*

  Output

  BuildNumber             : 18362
  BuildType               : Multiprocessor Free
  OSType                  : 18
  ServicePackMajorVersion : 0
  ServicePackMinorVersion : 0

Listing local users and owner
General information about local users can be found with a selection of
Win32_OperatingSystem class properties. You can explicitly select the properties to
display like this:

  PowerShell

  Get-CimInstance -ClassName Win32_OperatingSystem |
      Select-Object -Property NumberOfLicensedUsers, NumberOfUsers,
  RegisteredUser

A more succinct version using wildcards is:

  PowerShell

  Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object -Property
  *user*

Getting available disk space
To see the disk space and free space for local drives, you can use the Win32_LogicalDisk
class. You need to see only instances with a DriveType of 3, the value WMI uses for fixed
hard disks.

  PowerShell

  Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType=3"

  Output

<!-- p.506 -->

  DeviceID DriveType ProviderName VolumeName Size         FreeSpace
  PSComputerName
  -------- --------- ------------ ---------- ----         ---------   --------
  ------
  C:       3                      Local Disk 203912880128 65541357568 .
  Q:       3                      New Volume 122934034432 44298250240 .

  PowerShell

  Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType=3" |
      Measure-Object -Property FreeSpace,Size -Sum |
      Select-Object -Property Property,Sum

  Output

  Property           Sum
  --------           ---
  FreeSpace 109839607808
  Size      326846914560

Getting logon session information
You can get general information about logon sessions associated with users through the
Win32_LogonSession WMI class:

  PowerShell

  Get-CimInstance -ClassName Win32_LogonSession

Getting the user logged on to a computer
You can display the user logged on to a particular computer system using
Win32_ComputerSystem. This command returns only the user logged on to the system
desktop:

  PowerShell

  Get-CimInstance -ClassName Win32_ComputerSystem -Property UserName

Getting local time from a computer

<!-- p.507 -->

You can retrieve the current local time on a specific computer using the
Win32_LocalTime WMI class.

  PowerShell

  Get-CimInstance -ClassName Win32_LocalTime

  Output

  Day            : 23
  DayOfWeek      : 1
  Hour           : 8
  Milliseconds   :
  Minute         : 52
  Month          : 12
  Quarter        : 4
  Second         : 55
  WeekInMonth    : 4
  Year           : 2019
  PSComputerName :

Displaying service status
To view the status of all services on a specific computer, you can locally use the Get-
Service cmdlet. For remote systems, you can use the Win32_Service WMI class. If you

also use Select-Object to filter the results to Status, Name, and DisplayName, the
output format is almost identical to that from Get-Service :

  PowerShell

  Get-CimInstance -ClassName Win32_Service |
      Select-Object -Property Status,Name,DisplayName

To allow the complete display of names for services with long names, use the AutoSize
and Wrap parameters of Format-Table . These parameters optimize column width and
allow long names to wrap instead of being truncated:

  PowerShell

  Get-CimInstance -ClassName Win32_Service |
      Format-Table -Property Status, Name, DisplayName -AutoSize -Wrap

<!-- p.508 -->

Creating Get-WinEvent queries with
FilterHashtable
  This sample only applies to Windows platforms.

To read the original June 3, 2014 Scripting Guy blog post, see Use FilterHashTable to Filter
Event Log with PowerShell    .

This article is an excerpt of the original blog post and explains how to use the Get-WinEvent
cmdlet's FilterHashtable parameter to filter event logs. PowerShell's Get-WinEvent cmdlet is a
powerful method to filter Windows event and diagnostic logs. Performance improves when a
Get-WinEvent query uses the FilterHashtable parameter.

When you work with large event logs, it's not efficient to send objects down the pipeline to a
Where-Object command. Prior to PowerShell 6, the Get-EventLog cmdlet was another option to

get log data. For example, the following commands are inefficient to filter the Microsoft-
Windows-Defrag logs:

 PowerShell

 Get-EventLog -LogName Application | Where-Object Source -Match defrag

 Get-WinEvent -LogName Application | Where-Object { $_.ProviderName -match 'defrag'
 }

The following command uses a hash table that improves the performance:

 PowerShell

 Get-WinEvent -FilterHashtable @{
    LogName='Application'
    ProviderName='*defrag'
 }

Blog posts about enumeration
This article presents information about how to use enumerated values in a hash table. For more
information about enumeration, read these Scripting Guy blog posts. To create a function that

<!-- p.509 -->

returns the enumerated values, see Enumerations and Values       . For more information, see the
Scripting Guy series of blog posts about enumeration .

Hash table key-value pairs
To build efficient queries, use the Get-WinEvent cmdlet with the FilterHashtable parameter.
FilterHashtable accepts a hash table as a filter to get specific information from Windows event
logs. A hash table uses key-value pairs. For more information about hash tables, see
about_Hash_Tables.

If the key-value pairs are on the same line, they must be separated by a semicolon. If each key-
value pair is on a separate line, the semicolon isn't needed. For example, this article places key-
value pairs on separate lines and doesn't use semicolons.

This sample uses several of the FilterHashtable parameter's key-value pairs. The completed
query includes LogName, ProviderName, Keywords, Id, and Level.

The accepted key-value pairs are shown in the following table and are included in the
documentation for the Get-WinEvent FilterHashtable parameter.

The following table displays the key names, data types, and whether wildcard characters are
accepted for a data value.

                                                                                   ﾉ   Expand table

 Key name                Value data type            Accepts wildcard characters?

 LogName                 <String[]>                 Yes

 ProviderName            <String[]>                 Yes

 Path                    <String[]>                 No

 Keywords                <Long[]>                   No

 ID                      <Int32[]>                  No

 Level                   <Int32[]>                  No

 StartTime               <DateTime>                 No

 EndTime                 <DateTime>                 No

 UserID                  <SID>                      No

<!-- p.510 -->

 Key name               Value data type            Accepts wildcard characters?

 Data                    <String[]>                No

 <named-data>            <String[]>                No

The <named-data> key represents a named event data field. For example, the Perflib event 1008
can contain the following event data:

 XML

 <EventData>
   <Data Name="Service">BITS</Data>
   <Data Name="Library">C:\Windows\System32\bitsperf.dll</Data>
   <Data Name="Win32Error">2</Data>
 </EventData>

You can query for these events using the following command:

 PowerShell

 Get-WinEvent -FilterHashtable @{LogName='Application'; 'Service'='Bits'}

  ７ Note

  The ability to query for <named-data> was added in PowerShell 6.

Building a query with a hash table
To verify results and troubleshoot problems, it helps to build the hash table one key-value pair
at a time. The query gets data from the Application log. The hash table is equivalent to Get-
WinEvent -LogName Application .

To begin, create the Get-WinEvent query. Use the FilterHashtable parameter's key-value pair
with the key, LogName, and the value, Application.

 PowerShell

 Get-WinEvent -FilterHashtable @{
    LogName='Application'
 }

<!-- p.511 -->

Continue to build the hash table with the ProviderName key. Usually, the ProviderName is the
name that appears in the Source field in the Windows Event Viewer. For example, .NET
Runtime in the following screenshot:

Image of Windows Event Viewer sources

Update the hash table and include the key-value pair with the key, ProviderName, and the
value, .NET Runtime .

 PowerShell

 Get-WinEvent -FilterHashtable @{
    LogName='Application'
    ProviderName='.NET Runtime'
 }

  ７ Note

  For some event providers, the correct ProviderName can be obtained by looking on the
  Details tab in Event Properties. For example, events where the Source field shows Defrag ,
  the correct ProviderName is Microsoft-Windows-Defrag .

If your query needs to get data from archived event logs, use the Path key. The Path value
specifies the full path to the log file. For more information, see the Scripting Guy blog post,
Use PowerShell to Parse Saved Event Logs for Errors     .

Using enumerated values in a hash table
Keywords is the next key in the hash table. The Keywords data type is an array of the [long]
value type that holds a large number. Use the following command to find the maximum value
of [long] :

 PowerShell

 [long]::MaxValue

 Output

 9223372036854775807

<!-- p.512 -->

For the Keywords key, PowerShell uses a number, not a string such as Security. Windows Event
Viewer displays the Keywords as strings, but they're enumerated values. In the hash table, if
you use the Keywords key with a string value, an error message is displayed.

Open the Windows Event Viewer and from the Actions pane, click on Filter current log. The
Keywords drop-down menu displays the available keywords, as shown in the following
screenshot:

Image of Windows Event Viewer keywords

Use the following command to display the StandardEventKeywords property names.

 PowerShell

 [System.Diagnostics.Eventing.Reader.StandardEventKeywords] |
     Get-Member -Static -MemberType Property

 Output

     TypeName: System.Diagnostics.Eventing.Reader.StandardEventKeywords
 Name              MemberType Definition
 —-              ———- ———-
 AuditFailure      Property   static
 System.Diagnostics.Eventing.Reader.StandardEventKey…
 AuditSuccess      Property   static
 System.Diagnostics.Eventing.Reader.StandardEventKey…
 CorrelationHint Property     static
 System.Diagnostics.Eventing.Reader.StandardEventKey…
 CorrelationHint2 Property    static
 System.Diagnostics.Eventing.Reader.StandardEventKey…
 EventLogClassic Property     static
 System.Diagnostics.Eventing.Reader.StandardEventKey…
 None              Property   static
 System.Diagnostics.Eventing.Reader.StandardEventKey…
 ResponseTime      Property   static
 System.Diagnostics.Eventing.Reader.StandardEventKey…
 Sqm               Property   static
 System.Diagnostics.Eventing.Reader.StandardEventKey…
 WdiContext        Property   static
 System.Diagnostics.Eventing.Reader.StandardEventKey…
 WdiDiagnostic     Property   static
 System.Diagnostics.Eventing.Reader.StandardEventKey…

The enumerated values are documented in the .NET Framework. For more information, see
StandardEventKeywords Enumeration.

The Keywords names and enumerated values are as follows:

<!-- p.513 -->

                                                                             ﾉ   Expand table

 Name                                       Value

 AuditFailure                               4503599627370496

 AuditSuccess                               9007199254740992

 CorrelationHint2                           18014398509481984

 EventLogClassic                            36028797018963968

 Sqm                                        2251799813685248

 WdiDiagnostic                              1125899906842624

 WdiContext                                 562949953421312

 ResponseTime                               281474976710656

 None                                       0

Update the hash table and include the key-value pair with the key, Keywords, and the
EventLogClassic enumeration value, 36028797018963968.

 PowerShell

 Get-WinEvent -FilterHashtable @{
    LogName='Application'
    ProviderName='.NET Runtime'
    Keywords=36028797018963968
 }

Keywords static property value (optional)
The Keywords key is enumerated, but you can use a static property name in the hash table
query. Rather than using the returned string, the property name must be converted to a value
with the value__ property.

For example, the following script uses the value__ property.

 PowerShell

 $C = [System.Diagnostics.Eventing.Reader.StandardEventKeywords]::EventLogClassic
 Get-WinEvent -FilterHashtable @{
    LogName='Application'
    ProviderName='.NET Runtime'

<!-- p.514 -->

     Keywords=$C.value__
 }

Filtering by Event Id
To get more specific data, the query's results are filtered by Event Id. The Event Id is referenced
in the hash table as the key Id and the value is a specific Event Id. The Windows Event Viewer
displays the Event Id. This example uses Event Id 1023.

Update the hash table and include the key-value pair with the key, Id and the value, 1023.

 PowerShell

 Get-WinEvent -FilterHashtable @{
    LogName='Application'
    ProviderName='.NET Runtime'
    Keywords=36028797018963968
    ID=1023
 }

Filtering by Level
To further refine the results and include only events that are errors, use the Level key. Windows
Event Viewer displays the Level as string values, but they're enumerated values. In the hash
table, if you use the Level key with a string value, an error message is displayed.

Level has values such as Error, Warning, or Informational. Use the following command to
display the StandardEventLevel property names.

 PowerShell

 [System.Diagnostics.Eventing.Reader.StandardEventLevel] |
     Get-Member -Static -MemberType Property

 Output

     TypeName: System.Diagnostics.Eventing.Reader.StandardEventLevel

 Name          MemberType Definition
 ----          ---------- ----------
 Critical      Property   static
 System.Diagnostics.Eventing.Reader.StandardEventLevel Critical {get;}
 Error         Property   static
 System.Diagnostics.Eventing.Reader.StandardEventLevel Error {get;}
 Informational Property   static

<!-- p.515 -->

 System.Diagnostics.Eventing.Reader.StandardEventLevel Informational {get;}
 LogAlways     Property   static
 System.Diagnostics.Eventing.Reader.StandardEventLevel LogAlways {get;}
 Verbose       Property   static
 System.Diagnostics.Eventing.Reader.StandardEventLevel Verbose {get;}
 Warning       Property   static
 System.Diagnostics.Eventing.Reader.StandardEventLevel Warning {get;}

The enumerated values are documented in the .NET Framework. For more information, see
StandardEventLevel Enumeration.

The Level key's names and enumerated values are as follows:

                                                                               ﾉ    Expand table

 Name                                                           Value

 Verbose                                                        5

 Informational                                                  4

 Warning                                                        3

 Error                                                          2

 Critical                                                       1

 LogAlways                                                      0

The hash table for the completed query includes the key, Level, and the value, 2.

 PowerShell

 Get-WinEvent -FilterHashtable @{
    LogName='Application'
    ProviderName='.NET Runtime'
    Keywords=36028797018963968
    ID=1023
    Level=2
 }

Level static property in enumeration (optional)
The Level key is enumerated, but you can use a static property name in the hash table query.
Rather than using the returned string, the property name must be converted to a value with
the value__ property.

For example, the following script uses the value__ property.

<!-- p.516 -->

 PowerShell

 $C = [System.Diagnostics.Eventing.Reader.StandardEventLevel]::Informational
 Get-WinEvent -FilterHashtable @{
    LogName='Application'
    ProviderName='.NET Runtime'
    Keywords=36028797018963968
    ID=1023
    Level=$C.value__
 }

Last updated on 03/24/2025

<!-- p.517 -->

Managing processes with Process cmdlets
  This sample only applies to Windows PowerShell 5.1.

You can use the Process cmdlets in PowerShell to manage local and remote processes in
PowerShell.

Getting processes
To get the processes running on the local computer, run a Get-Process with no parameters.

You can get particular processes by specifying their process names or process IDs. The
following command gets the Idle process:

 PowerShell

 Get-Process -Id 0

 Output

 Handles      NPM(K)    PM(K)        WS(K) VM(M)     CPU(s)       Id ProcessName
 -------      ------    -----        ----- -----     ------       -- -----------
       0           0        0           16     0                   0 Idle

Although it's normal for cmdlets to return no data in some situations, when you specify a
process by its ProcessId, Get-Process generates an error if it finds no matches, because the
usual intent is to retrieve a known running process. If there is no process with that ID, it's likely
that the ID is incorrect or that the process of interest has already exited:

 PowerShell

 Get-Process -Id 99

 Output

 Get-Process : No process with process ID 99 was found.
 At line:1 char:12
 + Get-Process <<<< -Id 99

<!-- p.518 -->

You can use the Name parameter of the Get-Process cmdlet to specify a subset of processes
based on the process name. The Name parameter can take multiple names in a comma-
separated list and it supports the use of wildcards, so you can type name patterns.

For example, the following command gets process whose names begin with "ex."

 PowerShell

 Get-Process -Name ex*

 Output

 Handles   NPM(K)      PM(K)      WS(K) VM(M)     CPU(s)      Id ProcessName
 -------   ------      -----      ----- -----     ------      -- -----------
     234        7       5572      12484   134       2.98    1684 EXCEL
     555       15      34500      12384   134     105.25     728 explorer

Because the .NET System.Diagnostics.Process class is the foundation for PowerShell processes,
it follows some of the conventions used by System.Diagnostics.Process. One of those
conventions is that the process name for an executable never includes the .exe at the end of
the executable name.

Get-Process also accepts multiple values for the Name parameter.

 PowerShell

 Get-Process -Name exp*,power*

 Output

 Handles   NPM(K)      PM(K)      WS(K) VM(M)     CPU(s)      Id ProcessName
 -------   ------      -----      ----- -----     ------      -- -----------
     540       15      35172      48148   141      88.44     408 explorer
     605        9      30668      29800   155       7.11    3052 powershell

You can use the ComputerName parameter of Get-Process to get processes on remote
computers. For example, the following command gets the PowerShell processes on the local
computer (represented by "localhost") and on two remote computers.

 PowerShell

 Get-Process -Name powershell -ComputerName localhost, Server01, Server02

<!-- p.519 -->

 Output

 Handles   NPM(K)    PM(K)       WS(K) VM(M)    CPU(s)       Id ProcessName
 -------   ------    -----       ----- -----    ------       -- -----------
     258        8    29772       38636   130               3700 powershell
     398       24    75988       76800   572               5816 powershell
     605        9    30668       29800   155        7.11   3052 powershell

The computer names aren't evident in this display, but they're stored in the MachineName
property of the process objects that Get-Process returns. The following command uses the
Format-Table cmdlet to display the process Id, ProcessName and MachineName

(ComputerName) properties of the process objects.

 PowerShell

 Get-Process -Name powershell -ComputerName localhost, Server01, Server01 |
     Format-Table -Property Id, ProcessName, MachineName

 Output

   Id ProcessName MachineName
   -- ----------- -----------
 3700 powershell Server01
 3052 powershell Server02
 5816 powershell localhost

This more complex command adds the MachineName property to the standard Get-Process
display.

 PowerShell

 Get-Process powershell -ComputerName localhost, Server01, Server02 |
     Format-Table -Property Handles,
         @{Label="NPM(K)";Expression={[int]($_.NPM/1024)}},
         @{Label="PM(K)";Expression={[int]($_.PM/1024)}},
         @{Label="WS(K)";Expression={[int]($_.WS/1024)}},
         @{Label="VM(M)";Expression={[int]($_.VM/1MB)}},
         @{Label="CPU(s)";Expression={if ($_.CPU -ne $()){$_.CPU.ToString("N")}}},
         Id, ProcessName, MachineName -Auto

 Output

 Handles   NPM(K)   PM(K) WS(K) VM(M) CPU(s)   Id ProcessName MachineName
 -------   ------   ----- ----- ----- ------   -- ----------- -----------
     258        8   29772 38636   130          3700 powershell Server01

<!-- p.520 -->

      398       24   75988 76800     572           5816 powershell localhost
      605        9   30668 29800     155 7.11      3052 powershell Server02

Stopping processes
PowerShell gives you flexibility for listing processes, but what about stopping a process?

The Stop-Process cmdlet takes a Name or Id to specify a process you want to stop. Your ability
to stop processes depends on your permissions. Some processes can't be stopped. For
example, if you try to stop the idle process, you get an error:

 PowerShell

 Stop-Process -Name Idle

 Output

 Stop-Process : Process 'Idle (0)' cannot be stopped due to the following error:
  Access is denied
 At line:1 char:13
 + Stop-Process <<<< -Name Idle

You can also force prompting with the Confirm parameter. This parameter is particularly useful
if you use a wildcard when specifying the process name, because you may accidentally match
some processes you don't want to stop:

 PowerShell

 Stop-Process -Name t*,e* -Confirm

 Output

 Confirm
 Are you sure you want to perform this action?
 Performing operation "Stop-Process" on Target "explorer (408)".
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help
 (default is "Y"):n
 Confirm
 Are you sure you want to perform this action?
 Performing operation "Stop-Process" on Target "taskmgr (4072)".
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help
 (default is "Y"):n
