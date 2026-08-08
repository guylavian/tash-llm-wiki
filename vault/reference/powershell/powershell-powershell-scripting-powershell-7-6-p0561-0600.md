---
title: "How to use this documentation — pages 561-600"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0561-0600
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0561-0600
family: powershell
documentKind: "doc"
abstract: "history (a \"stack\") of directory paths where you have been, and you can step back through the history of directory paths using the Pop-Location cmdlet. For example, PowerShell typically starts in the user's home directory. PowerShell Get-Location Path ---- C:\\Documents and Setti"
---

# How to use this documentation — pages 561-600

<!-- p.561 -->

history (a "stack") of directory paths where you have been, and you can step back through the
history of directory paths using the Pop-Location cmdlet.

For example, PowerShell typically starts in the user's home directory.

 PowerShell

 Get-Location

 Path
 ----
 C:\Documents and Settings\PowerUser

  ７ Note

  The word stack has a special meaning in many programming settings, including .NET
  Framework. Like a physical stack of items, the last item you put onto the stack is the first
  item that you can pull off the stack. Adding an item to a stack is colloquially known as
  "pushing" the item onto the stack. Pulling an item off the stack is colloquially known as
  "popping" the item off the stack.

To push the current location onto the stack, and then move to the Local Settings folder, type:

 PowerShell

 Push-Location -Path "Local Settings"

You can then push the Local Settings location onto the stack and move to the Temp folder by
typing:

 PowerShell

 Push-Location -Path Temp

You can verify that you changed directories by entering the Get-Location command:

 PowerShell

 Get-Location

 Output

<!-- p.562 -->

 Path
 ----
 C:\Documents and Settings\PowerUser\Local Settings\Temp

You can then pop back into the most recently visited directory by entering the Pop-Location
command, and verify the change by entering the Get-Location command:

 PowerShell

 Pop-Location
 Get-Location

 Output

 Path
 ----
 C:\Documents and Settings\me\Local Settings

Just as with the Set-Location cmdlet, you can include the PassThru parameter when you enter
the Pop-Location cmdlet to display the directory that you entered:

 PowerShell

 Pop-Location -PassThru

 Output

 Path
 ----
 C:\Documents and Settings\PowerUser

You can also use the Location cmdlets with network paths. If you have a server named FS01
with a share named Public, you can change your location by typing

 PowerShell

 Set-Location \\FS01\Public

or

 PowerShell

 Push-Location \\FS01\Public

<!-- p.563 -->

You can use the Push-Location and Set-Location commands to change the location to any
available drive. For example, if you have a local CD-ROM drive with drive letter D that contains
a data CD, you can change the location to the CD drive by entering the Set-Location D:
command.

If the drive is empty, you get the following error message:

  PowerShell

  Set-Location D:

  Output

  Set-Location : Cannot find path 'D:\' because it does not exist.

When you are using a command-line interface, it's not convenient to use File Explorer to
examine the available physical drives. Also, File Explorer would not show you the all the
PowerShell drives. PowerShell provides a set of commands for manipulating PowerShell drives.

 Last updated on 03/24/2025

<!-- p.564 -->

Managing PowerShell drives
  This sample only applies to Windows platforms.

A PowerShell drive is a data store location that you can access like a filesystem drive in
PowerShell. The PowerShell providers create some drives for you, such as the file system drives
(including C: and D: ), the registry drives ( HKCU: and HKLM: ), and the certificate drive ( Cert: ),
and you can create your own PowerShell drives. These drives are useful, but they're available
only within PowerShell. You can't access them using other Windows tools, such as File Explorer
or Cmd.exe .

PowerShell uses the noun, PSDrive, for commands that work with PowerShell drives. For a list
of the PowerShell drives in your PowerShell session, use the Get-PSDrive cmdlet.

 PowerShell

 Get-PSDrive

 Output

 Name          Provider        Root                                          CurrentLocation
 ----          --------        ----                                          ---------------
 A             FileSystem      A:\
 Alias         Alias
 C             FileSystem      C:\                                       ...And Settings\me
 cert          Certificate     \
 D             FileSystem      D:\
 Env           Environment
 Function      Function
 HKCU          Registry        HKEY_CURRENT_USER
 HKLM          Registry        HKEY_LOCAL_MACHINE
 Variable      Variable

Although the drives in the display vary with the drives on your system, yours should look
similar to the output of the Get-PSDrive command shown above.

filesystem drives are a subset of the PowerShell drives. You can identify the filesystem drives by
the FileSystem entry in the Provider column. The filesystem drives in PowerShell are supported
by the PowerShell FileSystem provider.

<!-- p.565 -->

To see the syntax of the Get-PSDrive cmdlet, type a Get-Command command with the Syntax
parameter:

 PowerShell

 Get-Command -Name Get-PSDrive -Syntax

 Output

 Get-PSDrive [[-Name] <String[]>] [-Scope <String>] [-PSProvider <String[]>] [-V
 erbose] [-Debug] [-ErrorAction <ActionPreference>] [-ErrorVariable <String>] [-
 OutVariable <String>] [-OutBuffer <Int32>]

The PSProvider parameter lets you display only the PowerShell drives that are supported by a
particular provider. For example, to display only the PowerShell drives that are supported by
the PowerShell FileSystem provider, type a Get-PSDrive command with the PSProvider
parameter and the FileSystem value:

 PowerShell

 Get-PSDrive -PSProvider FileSystem

 Output

 Name         Provider       Root                                       CurrentLocation
 ----         --------       ----                                       ---------------
 A            FileSystem     A:\
 C            FileSystem     C:\                              ...nd Settings\PowerUser
 D            FileSystem     D:\

To view the PowerShell drives that represent registry hives, use the PSProvider parameter to
display only the PowerShell drives that are supported by the PowerShell Registry provider:

 PowerShell

 Get-PSDrive -PSProvider Registry

 Output

 Name         Provider       Root                                       CurrentLocation
 ----         --------       ----                                       ---------------
 HKCU         Registry       HKEY_CURRENT_USER
 HKLM         Registry       HKEY_LOCAL_MACHINE

<!-- p.566 -->

You can also use the standard Location cmdlets with the PowerShell drives:

 PowerShell

 Set-Location HKLM:\SOFTWARE
 Push-Location .\Microsoft
 Get-Location

 Output

 Path
 ----
 HKLM:\SOFTWARE\Microsoft

Adding new PowerShell drives
You can add your own PowerShell drives by using the New-PSDrive command. To get the syntax
for the New-PSDrive command, enter the Get-Command command with the Syntax parameter:

 PowerShell

 Get-Command -Name New-PSDrive -Syntax

 Output

 New-[-Description <String>] [-Scope <String>] [-Credential <PSCredential>] [-
 Verbose] [-Debug ]
 [-ErrorAction <ActionPreference>] [-ErrorVariable <String>] [-OutVariable <St
 ring>]
 [-OutBuffer <Int32>] [-WhatIf] [-Confirm]

To create a new PowerShell drive, you must supply three parameters:

     A name for the drive (you can use any valid PowerShell name)
     The PSProvider - use FileSystem for filesystem locations and Registry for registry
     locations
     The root, that is, the path to the root of the new drive

For example, you can create a drive named Office that's mapped to the folder that contains
the Microsoft Office applications on your computer, such as C:\Program
Files\MicrosoftOffice\OFFICE11 . To create the drive, type the following command:

 PowerShell

<!-- p.567 -->

  New-PSDrive -Name Office -PSProvider FileSystem -Root "C:\Program Files\Microsoft
  Office\OFFICE11"

  Output

  Name         Provider       Root                                         CurrentLocation
  ----         --------       ----                                         ---------------
  Office       FileSystem     C:\Program Files\Microsoft Offic...

  ７ Note

  In general, paths aren't case-sensitive.

A PowerShell drive is accessed using its name followed by a colon ( : ).

A PowerShell drive can make many tasks much simpler. For example, some of the most
important keys in the Windows registry have extremely long paths, making them cumbersome
to access and difficult to remember. Critical configuration information resides under
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion . To view and change items in

the CurrentVersion registry key, you can create a PowerShell drive that's rooted in that key by
typing:

  PowerShell

  New-PSDrive -Name cvkey -PSProvider Registry -Root
  HKLM\Software\Microsoft\Windows\CurrentVersion

  Output

  Name         Provider       Root                                         CurrentLocation
  ----         --------       ----                                         ---------------
  cvkey        Registry       HKLM\Software\Microsoft\Windows\...

You can then change location to the cvkey: drive as you would any other drive:

  PowerShell

  cd cvkey:

or:

  PowerShell

<!-- p.568 -->

  Set-Location cvkey: -PassThru

  Output

  Path
  ----
  cvkey:\

The New-PSDrive cmdlet adds the new drive only to the current PowerShell session. If you close
the PowerShell window, the new drive is lost. To save a PowerShell drive, use the Export-
Console cmdlet to export the current PowerShell session, and then use the powershell.exe

PSConsoleFile parameter to import it. Or, add the new drive to your Windows PowerShell
profile.

Deleting PowerShell drives
You can delete drives from PowerShell using the Remove-PSDrive cmdlet. For example, if you
added the Office: PowerShell drive, as shown in the New-PSDrive topic, you can delete it by
typing:

  PowerShell

  Remove-PSDrive -Name Office

To delete the cvkey: PowerShell drive, use the following command:

  PowerShell

  Remove-PSDrive -Name cvkey

However, you can't delete it while you are in the drive. For example:

  PowerShell

  cd office:
  Remove-PSDrive -Name Office

  Output

  Remove-PSDrive : Cannot remove drive 'Office' because it is in use.
  At line:1 char:15
  + Remove-PSDrive <<<< -Name Office

<!-- p.569 -->

Adding and removing drives outside PowerShell
PowerShell detects filesystem drives that are added or removed in Windows, including:

     network drives that are mapped
     USB drives that are attached
     Drives that are deleted using the net use command or from a Windows Script Host
     (WSH) script

Last updated on 03/24/2025

<!-- p.570 -->

Working with files and folders
Navigating through PowerShell drives and manipulating the items on them is similar to
manipulating files and folders on Windows disk drives. This article discusses how to deal with
specific file and folder manipulation tasks using PowerShell.

Listing all files and folders within a folder
You can get all items directly within a folder using Get-ChildItem . Add the optional Force
parameter to display hidden or system items. For example, this command displays the direct
contents of PowerShell Drive C: .

 PowerShell

 Get-ChildItem -Path C:\ -Force

The command lists only the directly contained items, much like using the dir command in
cmd.exe or ls in a Unix shell. To show items in subfolder, you need to specify the Recurse

parameter. The following command lists everything on the C: drive:

 PowerShell

 Get-ChildItem -Path C:\ -Force -Recurse

Get-ChildItem can filter items with its Path, Filter, Include, and Exclude parameters, but those

are typically based only on name. You can perform complex filtering based on other properties
of items using Where-Object .

The following command finds all executables within the Program Files folder that were last
modified after October 1, 2005 and that are neither smaller than 1 megabyte nor larger than 10
megabytes:

 PowerShell

 Get-ChildItem -Path $Env:ProgramFiles -Recurse -Include *.exe |
     Where-Object -FilterScript {
         ($_.LastWriteTime -gt '2005-10-01') -and ($_.Length -ge 1mb) -and
 ($_.Length -le 10mb)
     }

Copying files and folders

<!-- p.571 -->

Copying is done with Copy-Item . The following command backs up your PowerShell profile
script:

  PowerShell

  if (Test-Path -Path $PROFILE) {
      Copy-Item -Path $PROFILE -Destination $($PROFILE -replace 'ps1$', 'bak')
  }

The Test-Path command checks whether the profile script exists.

If the destination file already exists, the copy attempt fails. To overwrite a pre-existing
destination, use the Force parameter:

  PowerShell

  if (Test-Path -Path $PROFILE) {
      Copy-Item -Path $PROFILE -Destination $($PROFILE -replace 'ps1$', 'bak') -Force
  }

This command works even when the destination is read-only.

Folder copying works the same way. This command copies the folder C:\temp\test1 to the
new folder C:\temp\DeleteMe recursively:

  PowerShell

  Copy-Item C:\temp\test1 -Recurse C:\temp\DeleteMe

You can also copy a selection of items. The following command copies all .txt files contained
anywhere in C:\data to C:\temp\text :

  PowerShell

  Copy-Item -Filter *.txt -Path C:\data -Recurse -Destination C:\temp\text

You can still run native commands like xcopy.exe and robocopy.exe to copy files.

Creating files and folders
Creating new items works the same on all PowerShell providers. If a PowerShell provider has
more than one type of item—for example, the FileSystem PowerShell provider distinguishes
between directories and files—you need to specify the item type.

<!-- p.572 -->

This command creates a new folder C:\temp\New Folder :

 PowerShell

 New-Item -Path 'C:\temp\New Folder' -ItemType Directory

This command creates a new empty file C:\temp\New Folder\file.txt

 PowerShell

 New-Item -Path 'C:\temp\New Folder\file.txt' -ItemType File

  ） Important

  When using the Force switch with the New-Item command to create a folder, and the
  folder already exists, it won't overwrite or replace the folder. It will simply return the
  existing folder object. However, if you use New-Item -Force on a file that already exists,
  the file is overwritten.

Removing all files and folders within a folder
You can remove contained items using Remove-Item , but you will be prompted to confirm the
removal if the item contains anything else. For example, if you attempt to delete the folder
C:\temp\DeleteMe that contains other items, PowerShell prompts you for confirmation before

deleting the folder:

 PowerShell

 Remove-Item -Path C:\temp\DeleteMe

 Output

 Confirm
 The item at C:\temp\DeleteMe has children and the Recurse parameter wasn't
 specified. If you continue, all children will be removed with the item. Are you
 sure you want to continue?
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help
 (default is "Y"):

If you don't want to be prompted for each contained item, specify the Recurse parameter:

<!-- p.573 -->

 PowerShell

 Remove-Item -Path C:\temp\DeleteMe -Recurse

Mapping a local folder as a drive
You can also map a local folder, using the New-PSDrive command. The following command
creates a local drive P: rooted in the local Program Files directory, visible only from the
PowerShell session:

 PowerShell

 New-PSDrive -Name P -Root $Env:ProgramFiles -PSProvider FileSystem

Just as with network drives, drives mapped within PowerShell are immediately visible to the
PowerShell shell. To create a mapped drive visible from File Explorer, use the Persist parameter.
However, only remote paths can be used with Persist.

Reading a text file into an array
One of the more common storage formats for text data is in a file with separate lines treated as
distinct data elements. The Get-Content cmdlet can be used to read an entire file in one step,
as shown here:

 PowerShell

 Get-Content -Path $PROFILE
 # Load modules and change to the PowerShell-Docs repository folder
 Import-Module posh-git
 Set-Location C:\Git\PowerShell-Docs

Get-Content treats the data read from the file as an array, with one element per line of file
content. You can confirm this by checking the Length of the returned content:

 PowerShell

 PS> (Get-Content -Path $PROFILE).Length
 3

This command is most useful for getting lists of information into PowerShell. For example, you
might store a list of computer names or IP addresses in the file C:\temp\domainMembers.txt ,

<!-- p.574 -->

with one name on each line of the file. You can use Get-Content to retrieve the file contents
and put them in the variable $Computers :

  PowerShell

  $Computers = Get-Content -Path C:\temp\DomainMembers.txt

$Computers is now an array containing a computer name in each element.

 Last updated on 10/18/2023

<!-- p.575 -->

Working with files, folders and registry
keys
  This sample only applies to Windows platforms.

PowerShell uses the noun Item to refer to items found on a PowerShell drive. When dealing
with the PowerShell FileSystem provider, an Item might be a file, a folder, or the PowerShell
drive. Listing and working with these items is a critical basic task in most administrative
settings, so we want to discuss these tasks in detail.

Enumerating files, folders, and registry keys
Since getting a collection of items from a particular location is such a common task, the Get-
ChildItem cmdlet is designed specifically to return all items found within a container such as a

folder.

If you want to return all files and folders that are contained directly within the folder
C:\Windows , type:

  PS> Get-ChildItem -Path C:\Windows
      Directory: Microsoft.PowerShell.Core\FileSystem::C:\Windows

  Mode                  LastWriteTime        Length Name
  ----                  -------------        ------ ----
  -a---          2006-05-16   8:10 AM             0 0.log
  -a---          2005-11-29   3:16 PM            97 acc1.txt
  -a---          2005-10-23 11:21 PM           3848 actsetup.log
  ...

The listing looks similar to what you would see when you enter the dir command in cmd.exe ,
or the ls command in a Unix command shell.

You can perform complex listings using parameters of the Get-ChildItem cmdlet. You can see
the syntax the Get-ChildItem cmdlet by typing:

  PowerShell

  Get-Command -Name Get-ChildItem -Syntax

<!-- p.576 -->

These parameters can be mixed and matched to get highly customized output.

Listing all contained items
To see both the items inside a Windows folder and any items that are contained within the
subfolders, use the Recurse parameter of Get-ChildItem . The listing displays everything within
the Windows folder and the items in its subfolders. For example:

 PS> Get-ChildItem -Path C:\WINDOWS -Recurse

      Directory: Microsoft.PowerShell.Core\FileSystem::C:\WINDOWS
      Directory: Microsoft.PowerShell.Core\FileSystem::C:\WINDOWS\AppPatch
 Mode                 LastWriteTime     Length Name
 ----                 -------------     ------ ----
 -a---         2004-08-04   8:00 AM    1852416 AcGenral.dll
 ...

Filtering items by name
To display only the names of items, use the Name parameter of Get-ChildItem :

 PS> Get-ChildItem -Path C:\WINDOWS -Name
 addins
 AppPatch
 assembly
 ...

Forcibly listing hidden items
Items that are hidden in File Explorer or cmd.exe aren't displayed in the output of a Get-
ChildItem command. To display hidden items, use the Force parameter of Get-ChildItem . For

example:

 PowerShell

 Get-ChildItem -Path C:\Windows -Force

This parameter is named Force because you can forcibly override the normal behavior of the
Get-ChildItem command. Force is a widely used parameter that forces an action that a cmdlet

<!-- p.577 -->

wouldn't normally perform, although it can't perform any action that compromises the security
of the system.

Matching item names with wildcards
The Get-ChildItem command accepts wildcards in the path of the items to list.

Because wildcard matching is handled by the PowerShell engine, all cmdlets that accepts
wildcards use the same notation and have the same matching behavior. The PowerShell
wildcard notation includes:

     Asterisk ( * ) matches zero or more occurrences of any character.
     Question mark ( ? ) matches exactly one character.
     Left bracket ( [ ) character and right bracket ( ] ) character surround a set of characters to
     be matched.

Here are some examples of how wildcard specification works.

To find all files in the Windows directory with the suffix .log and exactly five characters in the
base name, enter the following command:

 PS> Get-ChildItem -Path C:\Windows\?????.log

      Directory: Microsoft.PowerShell.Core\FileSystem::C:\Windows
 Mode                 LastWriteTime     Length Name
 ----                 -------------     ------ ----
 ...
 -a---         2006-05-11   6:31 PM     204276 ocgen.log
 -a---         2006-05-11   6:31 PM      22365 ocmsn.log
 ...
 -a---         2005-11-11   4:55 AM         64 setup.log
 -a---         2005-12-15   2:24 PM      17719 VxSDM.log
 ...

To find all files that begin with the letter x in the Windows directory, type:

 PowerShell

 Get-ChildItem -Path C:\Windows\x*

To find all files whose names begin with "x" or "z", type:

 PowerShell

<!-- p.578 -->

      Get-ChildItem -Path C:\Windows\[xz]*

For more information about wildcards, see about_Wildcards.

Excluding items
You can exclude specific items using the Exclude parameter of Get-ChildItem . This lets you
perform complex filtering in a single statement.

For example, suppose you are trying to find the Windows Time Service DLL in the System32
folder, and all you can remember about the DLL name is that it begins with "W" and has "32" in
it.

An expression like w*32*.dll will find all DLLs that satisfy the conditions, but you may want to
further filter out the files and omit any win32 files. You can omit these files using the Exclude
parameter with the pattern win* :

      PS> Get-ChildItem -Path C:\WINDOWS\System32\w*32*.dll -Exclude win*

          Directory: C:\WINDOWS\System32

      Mode                LastWriteTime            Length Name
      ----                -------------            ------ ----
      -a---          3/18/2019 9:43 PM             495616 w32time.dll
      -a---          3/18/2019 9:44 PM              35328 w32topl.dll
      -a---          1/24/2020 5:44 PM             401920 Wldap32.dll
      -a---         10/10/2019 5:40 PM             442704 ws2_32.dll
      -a---          3/18/2019 9:44 PM              66048 wsnmp32.dll
      -a---          3/18/2019 9:44 PM              18944 wsock32.dll
      -a---          3/18/2019 9:44 PM              64792 wtsapi32.dll

Mixing Get-ChildItem parameters
You can use several of the parameters of the Get-ChildItem cmdlet in the same command.
Before you mix parameters, be sure that you understand wildcard matching. For example, the
following command returns no results:

      PowerShell

      Get-ChildItem -Path C:\Windows\*.dll -Recurse -Exclude [a-y]*.dll

<!-- p.579 -->

There are no results, even though there are two DLLs that begin with the letter "z" in the
Windows folder.

No results were returned because we specified the wildcard as part of the path. Even though
the command was recursive, the Get-ChildItem cmdlet restricted the items to those that are in
the Windows folder with names ending with .dll .

To specify a recursive search for files whose names match a special pattern, use the Include
parameter.

  PS> Get-ChildItem -Path C:\Windows -Include *.dll -Recurse -Exclude [a-y]*.dll

       Directory: Microsoft.PowerShell.Core\FileSystem::C:\Windows\System32\Setup

  Mode                   LastWriteTime      Length Name
  ----                   -------------      ------ ----
  -a---           2004-08-04   8:00 AM        8261 zoneoc.dll

       Directory: Microsoft.PowerShell.Core\FileSystem::C:\Windows\System32

  Mode                   LastWriteTime      Length Name
  ----                   -------------      ------ ----
  -a---           2004-08-04   8:00 AM      337920 zipfldr.dll

 Last updated on 03/24/2025

<!-- p.580 -->

Working with registry entries
  This sample only applies to Windows platforms.

Because registry entries are properties of keys and, as such, can't be directly browsed, we need
to take a slightly different approach when working with them.

Listing registry entries
There are many different ways to examine registry entries. The simplest way is to get the
property names associated with a key. For example, to see the names of the entries in the
registry key HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion , use Get-Item .
Registry keys have a property with the generic name of "Property" that's a list of registry
entries in the key. The following command selects the Property property and expands the items
so that they're displayed in a list:

  PowerShell

  Get-Item -Path
  Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion |
      Select-Object -ExpandProperty Property

  Output

  DevicePath
  MediaPathUnexpanded
  ProgramFilesDir
  CommonFilesDir
  ProductId

To view the registry entries in a more readable form, use Get-ItemProperty :

  PowerShell

  Get-ItemProperty -Path
  Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion

  Output

  ProgramFilesDir               : C:\Program Files
  CommonFilesDir                : C:\Program Files\Common Files

<!-- p.581 -->

 ProgramFilesDir (x86)    : C:\Program Files (x86)
 CommonFilesDir (x86)     : C:\Program Files (x86)\Common Files
 CommonW6432Dir           : C:\Program Files\Common Files
 DevicePath               : C:\WINDOWS\inf
 MediaPathUnexpanded      : C:\WINDOWS\Media
 ProgramFilesPath         : C:\Program Files
 ProgramW6432Dir          : C:\Program Files
 SM_ConfigureProgramsName : Set Program Access and Defaults
 SM_GamesName             : Games
 PSPath                   :
 Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWA
                            RE\Microsoft\Windows\CurrentVersion
 PSParentPath             :
 Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWA
                            RE\Microsoft\Windows
 PSChildName              : CurrentVersion
 PSDrive                  : HKLM
 PSProvider               : Microsoft.PowerShell.Core\Registry

The Windows PowerShell-related properties for the key are all prefixed with "PS", such as
PSPath, PSParentPath, PSChildName, and PSProvider.

You can use the *.* notation for referring to the current location. You can use Set-Location to
change to the CurrentVersion registry container first:

 PowerShell

 Set-Location -Path
 Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion

Alternatively, you can use the built-in HKLM: PSDrive with Set-Location :

 PowerShell

 Set-Location -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion

You can then use the . notation for the current location to list the properties without
specifying a full path:

 PowerShell

 Get-ItemProperty -Path .

 Output

 ...
 DevicePath               : C:\WINDOWS\inf

<!-- p.582 -->

 MediaPathUnexpanded : C:\WINDOWS\Media
 ProgramFilesDir     : C:\Program Files
 ...

Path expansion works the same as it does within the filesystem, so from this location you can
get the ItemProperty listing for HKLM:\SOFTWARE\Microsoft\Windows\Help using Get-
ItemProperty -Path ..\Help .

Getting a single registry entry
If you want to retrieve a specific entry in a registry key, you can use one of several possible
approaches. This example finds the value of DevicePath in
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion .

Using Get-ItemProperty , use the Path parameter to specify the name of the key, and the Name
parameter to specify the name of the DevicePath entry.

 PowerShell

 Get-ItemProperty -Path HKLM:\Software\Microsoft\Windows\CurrentVersion -Name
 DevicePath

 Output

 DevicePath    : C:\WINDOWS\inf
 PSPath        :
 Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\C
 urrentVersion
 PSParentPath :
 Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
 PSChildName : CurrentVersion
 PSDrive       : HKLM
 PSProvider    : Microsoft.PowerShell.Core\Registry

This command returns the standard Windows PowerShell properties as well as the DevicePath
property.

  ７ Note

  Although Get-ItemProperty has Filter, Include, and Exclude parameters, they can't be
  used to filter by property name. These parameters refer to registry keys, which are item
  paths and not registry entries, which are item properties.

<!-- p.583 -->

Another option is to use the reg.exe command line tool. For help with reg.exe , type reg.exe
/? at a command prompt. To find the DevicePath entry, use reg.exe as shown in the following

command:

 PowerShell

 reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion /v DevicePath

 Output

 ! REG.EXE VERSION 3.0

 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
     DevicePath REG_EXPAND_SZ    %SystemRoot%\inf

You can also use the WshShell COM object to find some registry entries, although this method
doesn't work with large binary data or with registry entry names that include characters such as
backslash ( \ ). Append the property name to the item path with a \ separator:

 PowerShell

 (New-Object -ComObject
 WScript.Shell).RegRead("HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\DevicePath")

 Output

 %SystemRoot%\inf

Setting a single registry entry
If you want to change a specific entry in a registry key, you can use one of several possible
approaches. This example modifies the Path entry under HKEY_CURRENT_USER\Environment . The
Path entry specifies where to find executable files.

   1. Retrieve the current value of the Path entry using Get-ItemProperty .
   2. Add the new value, separating it with a ; .
   3. Use Set-ItemProperty with the specified key, entry name, and value to modify the registry
     entry.

 PowerShell

<!-- p.584 -->

 $value = Get-ItemProperty -Path HKCU:\Environment -Name Path
 $newpath = $value.Path += ";C:\src\bin\"
 Set-ItemProperty -Path HKCU:\Environment -Name Path -Value $newpath

  ７ Note

  Although Set-ItemProperty has Filter, Include, and Exclude parameters, they can't be
  used to filter by property name. These parameters refer to registry keys—which are item
  paths—and not registry entries—which are item properties.

Another option is to use the Reg.exe command line tool. For help with reg.exe, type reg.exe
/? at a command prompt.

The following example changes the Path entry by removing the path added in the example
above. Get-ItemProperty is still used to retrieve the current value to avoid having to parse the
string returned from reg query . The SubString and LastIndexOf methods are used to retrieve
the last path added to the Path entry.

 PowerShell

 $value = Get-ItemProperty -Path HKCU:\Environment -Name Path
 $newpath = $value.Path.SubString(0, $value.Path.LastIndexOf(';'))
 reg add HKCU\Environment /v Path /d $newpath /f

 Output

 The operation completed successfully.

Creating new registry entries
To add a new entry named "PowerShellPath" to the CurrentVersion key, use New-ItemProperty
with the path to the key, the entry name, and the value of the entry. For this example, we will
take the value of the Windows PowerShell variable $PSHOME , which stores the path to the
installation directory for Windows PowerShell.

You can add the new entry to the key using the following command, and the command also
returns information about the new entry:

 PowerShell

<!-- p.585 -->

 $newItemPropertySplat = @{
     Path = 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion'
     Name = 'PowerShellPath'
     PropertyType = 'String'
     Value = $PSHOME
 }
 New-ItemProperty @newItemPropertySplat

 Output

 PSPath         :
 Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\C
 urrentVersion
 PSParentPath   :
 Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows
 PSChildName    : CurrentVersion
 PSDrive        : HKLM
 PSProvider     : Microsoft.PowerShell.Core\Registry
 PowerShellPath : C:\Program Files\Windows PowerShell\v1.0

The PropertyType must be the name of a Microsoft.Win32.RegistryValueKind enumeration
member from the following table:

     String - Used for REG_SZ values. Pass a [System.String] object to the Value parameter.

     ExpandString - Used for REG_EXPAND_SZ values. Pass a [System.String] object to the

     Value parameter. The string should contain unexpanded references to environment
     variables that are expanded when the value is retrieved.
     Binary - Used for REG_BINARY values. Pass a [System.Byte[]] object to the Value

     parameter.
     DWord - Used for REG_DWORD values. Pass a [System.Int32] object to the Value

     parameter.
     MultiString - Used for REG_MULTI_SZ values. Pass a [System.String[]] object to the

     Value parameter.
     QWord - Used for REG_QWORD values. Pass a [System.Int64] object to the Value

     parameter.

You can add a registry entry to multiple locations by specifying an array of values for the Path
parameter:

 PowerShell

 $newItemPropertySplat = @{
     Name = 'PowerShellPath'
     PropertyType = 'String'
     Value = $PSHOME

<!-- p.586 -->

      Path = 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion',
             'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion'
 }
 New-ItemProperty @newItemPropertySplat

You can also overwrite a pre-existing registry entry value by adding the Force parameter to any
New-ItemProperty command.

The following examples show how to create new registry entries of various types. The registry
values are created in a new key named MySoftwareKey under HKEY_CURRENT_USER\Software .
The $key variable is used to store the new key object.

 PowerShell

 $key = New-Item -Path HKCU:\Software -Name MySoftwareKey
 $newItemPropertySplat = @{
     Path = $key.PSPath
     Name = 'DefaultFolders'
     PropertyType = 'MultiString'
     Value = 'Home', 'Temp', 'Publish'
 }
 New-ItemProperty @newItemPropertySplat

 Output

 DefaultFolders : {Home, Temp, Publish}
 PSPath         :
 Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Software\MySoftwareKey
 PSParentPath   : Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Software
 PSChildName    : MySoftwareKey
 PSProvider     : Microsoft.PowerShell.Core\Registry

You can use the PSPath property of the key object in subsequent commands.

 PowerShell

 New-ItemProperty -Path $key.PSPath -Name MaxAllowed -PropertyType QWord -Value 1024

 Output

 MaxAllowed   : 1024
 PSPath       :
 Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Software\MySoftwareKey
 PSParentPath : Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Software
 PSChildName : MySoftwareKey
 PSProvider   : Microsoft.PowerShell.Core\Registry

<!-- p.587 -->

You can also pipe $key to New-ItemProperty to add a value to the key.

 PowerShell

 $date = Get-Date -Format 'dd-MMM-yyyy'
 $newItemPropertySplat = @{
     Name = 'BinaryDate'
     PropertyType = 'Binary'
     Value = ([System.Text.Encoding]::UTF8.GetBytes($date))
 }
 $key | New-ItemProperty @newItemPropertySplat

 Output

 BinaryDate   : {51, 49, 45, 74…}
 PSPath       :
 Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Software\MySoftwareKey
 PSParentPath : Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Software
 PSChildName : MySoftwareKey
 PSProvider   : Microsoft.PowerShell.Core\Registry

Displaying the content of $key shows the new entries.

 PowerShell

 $key

 Output

        Hive: HKEY_CURRENT_USER\Software

 Name                              Property
 ----                              --------
 MySoftwareKey                     DefaultFolders : {Home, Temp, Publish}
                                   MaxAllowed     : 1024
                                   BinaryDate     : {51, 49, 45, 74…}

The following example shows the value type for each kind of registry entry:

 PowerShell

 $key.GetValueNames() | Select-Object @{n='ValueName';e={$_}},
      @{n='ValueKind';e={$key.GetValueKind($_)}},
      @{n='Type';e={$key.GetValue($_).GetType()}},
      @{n='Value';e={$key.GetValue($_)}}

 Output

<!-- p.588 -->

 ValueName        ValueKind Type            Value
 ---------        --------- ----            -----
 DefaultFolders MultiString System.String[] {Home, Temp, Publish}
 MaxAllowed           QWord System.Int64    1024
 BinaryDate          Binary System.Byte[]   {51, 49, 45, 74…}

Renaming registry entries
To rename the PowerShellPath entry to "PSHome," use Rename-ItemProperty :

 PowerShell

 $renameItemPropertySplat = @{
     Path = 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion'
     Name = 'PowerShellPath'
     NewName = 'PSHome'
 }
 Rename-ItemProperty @renameItemPropertySplat

To display the renamed value, add the PassThru parameter to the command.

 PowerShell

 $renameItemPropertySplat = @{
     Path = 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion'
     Name = 'PowerShellPath'
     NewName = 'PSHome'
     PassThru = $true
 }
 Rename-ItemProperty @renameItemPropertySplat

Deleting registry entries
To delete both the PSHome and PowerShellPath registry entries, use Remove-ItemProperty :

 PowerShell

 Remove-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion -Name
 PSHome
 Remove-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion -Name
 PowerShellPath

Last updated on 02/24/2025

<!-- p.589 -->

Working with registry keys
  This sample only applies to Windows platforms.

Because registry keys are items on PowerShell drives, working with them is very similar to
working with files and folders. One critical difference is that every item on a registry-based
PowerShell drive is a container, just like a folder on a file system drive. However, registry entries
and their associated values are properties of the items, not distinct items.

Listing all subkeys of a registry key
You can show all items directly within a registry key using Get-ChildItem . Add the optional
Force parameter to display hidden or system items. For example, this command displays the
items directly within PowerShell drive HKCU: , which corresponds to the HKEY_CURRENT_USER
registry hive:

  PowerShell

  Get-ChildItem -Path HKCU:\ | Select-Object Name

  Output

     Hive: Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER

  Name
  ----
  HKEY_CURRENT_USER\AppEvents
  HKEY_CURRENT_USER\Console
  HKEY_CURRENT_USER\Control Panel
  HKEY_CURRENT_USER\DirectShow
  HKEY_CURRENT_USER\dummy
  HKEY_CURRENT_USER\Environment
  HKEY_CURRENT_USER\EUDC
  HKEY_CURRENT_USER\Keyboard Layout
  HKEY_CURRENT_USER\MediaFoundation
  HKEY_CURRENT_USER\Microsoft
  HKEY_CURRENT_USER\Network
  HKEY_CURRENT_USER\Printers
  HKEY_CURRENT_USER\Software
  HKEY_CURRENT_USER\System
  HKEY_CURRENT_USER\Uninstall
  HKEY_CURRENT_USER\WXP
  HKEY_CURRENT_USER\Volatile Environment

<!-- p.590 -->

These are the top-level keys visible under HKEY_CURRENT_USER in the Registry Editor
( regedit.exe ).

You can also specify this registry path by specifying the Registry provider's name, followed by
:: . The Registry provider's full name is Microsoft.PowerShell.Core\Registry , but this can be

shortened to just Registry . Any of the following commands will list the contents directly under
HKCU: .

  PowerShell

  Get-ChildItem -Path Registry::HKEY_CURRENT_USER
  Get-ChildItem -Path Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER
  Get-ChildItem -Path Registry::HKCU
  Get-ChildItem -Path Microsoft.PowerShell.Core\Registry::HKCU
  Get-ChildItem HKCU:

These commands list only the directly contained items, much like using DIR in cmd.exe or ls
in a Unix shell. To show contained items, you need to specify the Recurse parameter. To list all
registry keys in HKCU: , use the following command.

  PowerShell

  Get-ChildItem -Path HKCU:\ -Recurse

Get-ChildItem can perform complex filtering capabilities through its Path, Filter, Include, and

Exclude parameters, but those parameters are typically based only on name. You can perform
complex filtering based on other properties of items using the Where-Object cmdlet. The
following command finds all keys within HKCU:\Software that have no more than one subkey
and also have exactly four values:

  PowerShell

  Get-ChildItem -Path HKCU:\Software -Recurse |
      Where-Object {($_.SubKeyCount -le 1) -and ($_.ValueCount -eq 4) }

Copying keys
Copying is done with Copy-Item . The following example copies the CurrentVersion subkey of
HKLM:\SOFTWARE\Microsoft\Windows\ and all of its properties to HKCU:\ .

  PowerShell

<!-- p.591 -->

 Copy-Item -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion' -Destination
 HKCU:

If you examine this new key in the registry editor or using Get-ChildItem , you notice that you
don't have copies of the contained subkeys in the new location. In order to copy all of the
contents of a container, you need to specify the Recurse parameter. To make the preceding
copy command recursive, you would use this command:

 PowerShell

 Copy-Item -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion' -Destination
 HKCU: -Recurse

You can still use other tools you already have available to perform filesystem copies. Any
registry editing tools—including reg.exe , regini.exe , regedit.exe , and COM objects that
support registry editing, such as WScript.Shell and WMI's StdRegProv class can be used from
within PowerShell.

Creating keys
Creating new keys in the registry is simpler than creating a new item in a file system. Because
all registry keys are containers, you don't need to specify the item type. Just provide an explicit
path, such as:

 PowerShell

 New-Item -Path HKCU:\Software_DeleteMe

You can also use a provider-based path to specify a key:

 PowerShell

 New-Item -Path Registry::HKCU\Software_DeleteMe

Deleting keys
Deleting items is essentially the same for all providers. The following commands silently
remove items:

 PowerShell

<!-- p.592 -->

  Remove-Item -Path HKCU:\Software_DeleteMe
  Remove-Item -Path 'HKCU:\key with spaces in the name'

Removing all keys under a specific key
You can remove contained items using Remove-Item , but you will be prompted to confirm the
removal if the item contains anything else. For example, if we attempt to delete the
HKCU:\CurrentVersion subkey we created, we see this:

  PowerShell

  Remove-Item -Path HKCU:\CurrentVersion

  Output

  Confirm
  The item at HKCU:\CurrentVersion\AdminDebug has children and the Recurse
  parameter was not specified. If you continue, all children will be removed with
  the item. Are you sure you want to continue?
  [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default is
  "Y"):

To delete contained items without prompting, specify the Recurse parameter:

  PowerShell

  Remove-Item -Path HKCU:\CurrentVersion -Recurse

If you wanted to remove all items within HKCU:\CurrentVersion but not HKCU:\CurrentVersion
itself, you could instead use:

  PowerShell

  Remove-Item -Path HKCU:\CurrentVersion\* -Recurse

 Last updated on 03/24/2025

<!-- p.593 -->

Creating a custom input box
  This sample only applies to Windows platforms.

Script a graphical custom input box using Microsoft .NET Framework form-building features in
Windows PowerShell 3.0 and later releases.

Create a custom, graphical input box
Copy and then paste the following into Windows PowerShell ISE, and then save it as a
PowerShell script ( .ps1 ) file.

  PowerShell

  Add-Type -AssemblyName System.Windows.Forms
  Add-Type -AssemblyName System.Drawing

  $form = New-Object System.Windows.Forms.Form
  $form.Text = 'Data Entry Form'
  $form.Size = New-Object System.Drawing.Size(300,200)
  $form.StartPosition = 'CenterScreen'

  $okButton = New-Object System.Windows.Forms.Button
  $okButton.Location = New-Object System.Drawing.Point(75,120)
  $okButton.Size = New-Object System.Drawing.Size(75,23)
  $okButton.Text = 'OK'
  $okButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
  $form.AcceptButton = $okButton
  $form.Controls.Add($okButton)

  $cancelButton = New-Object System.Windows.Forms.Button
  $cancelButton.Location = New-Object System.Drawing.Point(150,120)
  $cancelButton.Size = New-Object System.Drawing.Size(75,23)
  $cancelButton.Text = 'Cancel'
  $cancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
  $form.CancelButton = $cancelButton
  $form.Controls.Add($cancelButton)

  $label = New-Object System.Windows.Forms.Label
  $label.Location = New-Object System.Drawing.Point(10,20)
  $label.Size = New-Object System.Drawing.Size(280,20)
  $label.Text = 'Please enter the information in the space below:'
  $form.Controls.Add($label)

  $textBox = New-Object System.Windows.Forms.TextBox
  $textBox.Location = New-Object System.Drawing.Point(10,40)
  $textBox.Size = New-Object System.Drawing.Size(260,20)

<!-- p.594 -->

 $form.Controls.Add($textBox)

 $form.Topmost = $true

 $form.Add_Shown({$textBox.Select()})
 $result = $form.ShowDialog()

 if ($result -eq [System.Windows.Forms.DialogResult]::OK)
 {
     $x = $textBox.Text
     $x
 }

The script begins by loading two .NET Framework classes: System.Drawing and
System.Windows.Forms. You then start a new instance of the .NET Framework class
System.Windows.Forms.Form. That provides a blank form or window to which you can start
adding controls.

 PowerShell

 $form = New-Object System.Windows.Forms.Form

After you create an instance of the Form class, assign values to three properties of this class.

     Text. This becomes the title of the window.
     Size. This is the size of the form, in pixels. The preceding script creates a form that's 300
     pixels wide by 200 pixels tall.
     StartingPosition. This optional property is set to CenterScreen in the preceding script. If
     you don't add this property, Windows selects a location when the form is opened. By
     setting the StartingPosition to CenterScreen, you're automatically displaying the form in
     the middle of the screen each time it loads.

 PowerShell

 $form.Text = 'Data Entry Form'
 $form.Size = New-Object System.Drawing.Size(300,200)
 $form.StartPosition = 'CenterScreen'

Next, create an OK button for your form. Specify the size and behavior of the OK button. In this
example, the button position is 120 pixels from the form's top edge, and 75 pixels from the left
edge. The button height is 23 pixels, while the button length is 75 pixels. The script uses
predefined Windows Forms types to determine the button behaviors.

 PowerShell

<!-- p.595 -->

 $okButton = New-Object System.Windows.Forms.Button
 $okButton.Location = New-Object System.Drawing.Point(75,120)
 $okButton.Size = New-Object System.Drawing.Size(75,23)
 $okButton.Text = 'OK'
 $okButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
 $form.AcceptButton = $OKButton
 $form.Controls.Add($OKButton)

Similarly, you create a Cancel button. The Cancel button is 120 pixels from the top, but 150
pixels from the left edge of the window.

 PowerShell

 $cancelButton = New-Object System.Windows.Forms.Button
 $cancelButton.Location = New-Object System.Drawing.Point(150,120)
 $cancelButton.Size = New-Object System.Drawing.Size(75,23)
 $cancelButton.Text = 'Cancel'
 $cancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
 $form.CancelButton = $cancelButton
 $form.Controls.Add($cancelButton)

Next, provide label text on your window that describes the information you want users to
provide.

 PowerShell

 $label = New-Object System.Windows.Forms.Label
 $label.Location = New-Object System.Drawing.Point(10,20)
 $label.Size = New-Object System.Drawing.Size(280,20)
 $label.Text = 'Please enter the information in the space below:'
 $form.Controls.Add($label)

Add the control (in this case, a text box) that lets users provide the information you've
described in your label text. There are many other controls you can apply besides text boxes.
For more controls, see System.Windows.Forms Namespace.

 PowerShell

 $textBox = New-Object System.Windows.Forms.TextBox
 $textBox.Location = New-Object System.Drawing.Point(10,40)
 $textBox.Size = New-Object System.Drawing.Size(260,20)
 $form.Controls.Add($textBox)

Set the Topmost property to $true to force the window to open atop other open windows and
dialog boxes.

<!-- p.596 -->

  PowerShell

  $form.Topmost = $true

Next, add this line of code to activate the form, and set the focus to the text box that you
created.

  PowerShell

  $form.Add_Shown({$textBox.Select()})

Add the following line of code to display the form in Windows.

  PowerShell

  $result = $form.ShowDialog()

Finally, the code inside the if block instructs Windows what to do with the form after users
provide text in the text box, and then click the OK button or press the Enter key.

  PowerShell

  if ($result -eq [System.Windows.Forms.DialogResult]::OK) {
      $x = $textBox.Text
      $x
  }

See also
      GitHub: Dave Wyatt's WinFormsExampleUpdates         )
      Windows PowerShell Tip of the Week: Creating a Custom Input Box

 Last updated on 03/24/2025

<!-- p.597 -->

Creating a graphical date picker
Article • 12/09/2022

  This sample only applies to Windows platforms.

Use Windows PowerShell 3.0 and later releases to create a form with a graphical,
calendar-style control that lets users select a day of the month.

Create a graphical date-picker control
Copy and then paste the following into Windows PowerShell ISE, and then save it as a
PowerShell script ( .ps1 ) file.

  PowerShell

  Add-Type -AssemblyName System.Windows.Forms
  Add-Type -AssemblyName System.Drawing

  $form = New-Object Windows.Forms.Form -Property @{
      StartPosition = [Windows.Forms.FormStartPosition]::CenterScreen
      Size          = New-Object Drawing.Size 243, 230
      Text          = 'Select a Date'
      Topmost       = $true
  }

  $calendar = New-Object Windows.Forms.MonthCalendar -Property @{
      ShowTodayCircle   = $false
      MaxSelectionCount = 1
  }
  $form.Controls.Add($calendar)

  $okButton = New-Object Windows.Forms.Button -Property @{
      Location     = New-Object Drawing.Point 38, 165
      Size         = New-Object Drawing.Size 75, 23
      Text         = 'OK'
      DialogResult = [Windows.Forms.DialogResult]::OK
  }
  $form.AcceptButton = $okButton
  $form.Controls.Add($okButton)

  $cancelButton = New-Object Windows.Forms.Button -Property @{
      Location     = New-Object Drawing.Point 113, 165
      Size         = New-Object Drawing.Size 75, 23
      Text         = 'Cancel'
      DialogResult = [Windows.Forms.DialogResult]::Cancel
  }
  $form.CancelButton = $cancelButton
  $form.Controls.Add($cancelButton)

<!-- p.598 -->

  $result = $form.ShowDialog()

  if ($result -eq [Windows.Forms.DialogResult]::OK) {
      $date = $calendar.SelectionStart
      Write-Host "Date selected: $($date.ToShortDateString())"
  }

The script begins by loading two .NET Framework classes: System.Drawing and
System.Windows.Forms. You then start a new instance of the .NET Framework class
Windows.Forms.Form. That provides a blank form or window to which you can start
adding controls.

  PowerShell

  $form = New-Object Windows.Forms.Form -Property @{
      StartPosition = [Windows.Forms.FormStartPosition]::CenterScreen
      Size          = New-Object Drawing.Size 243, 230
      Text          = 'Select a Date'
      Topmost       = $true
  }

This example assigns values to four properties of this class by using the Property
property and hashtable.

   1. StartPosition: If you don't add this property, Windows selects a location when the
        form is opened. By setting this property to CenterScreen, you're automatically
        displaying the form in the middle of the screen each time it loads.

   2. Size: This is the size of the form, in pixels. The preceding script creates a form
        that's 243 pixels wide by 230 pixels tall.

   3. Text: This becomes the title of the window.

   4. Topmost: By setting this property to $true , you can force the window to open
        atop other open windows and dialog boxes.

Next, create and then add a calendar control in your form. In this example, the current
day isn't highlighted or circled. Users can select only one day on the calendar at one
time.

  PowerShell

  $calendar = New-Object Windows.Forms.MonthCalendar -Property @{
      ShowTodayCircle   = $false
      MaxSelectionCount = 1

<!-- p.599 -->

  }
  $form.Controls.Add($calendar)

Next, create an OK button for your form. Specify the size and behavior of the OK button.
In this example, the button position is 165 pixels from the form's top edge, and 38 pixels
from the left edge. The button height is 23 pixels, while the button length is 75 pixels.
The script uses predefined Windows Forms types to determine the button behaviors.

  PowerShell

  $okButton = New-Object Windows.Forms.Button -Property @{
      Location     = New-Object Drawing.Point 38, 165
      Size         = New-Object Drawing.Size 75, 23
      Text         = 'OK'
      DialogResult = [Windows.Forms.DialogResult]::OK
  }
  $form.AcceptButton = $okButton
  $form.Controls.Add($okButton)

Similarly, you create a Cancel button. The Cancel button is 165 pixels from the top, but
113 pixels from the left edge of the window.

  PowerShell

  $cancelButton = New-Object Windows.Forms.Button -Property @{
      Location     = New-Object Drawing.Point 113, 165
      Size         = New-Object Drawing.Size 75, 23
      Text         = 'Cancel'
      DialogResult = [Windows.Forms.DialogResult]::Cancel
  }
  $form.CancelButton = $cancelButton
  $form.Controls.Add($cancelButton)

Add the following line of code to display the form in Windows.

  PowerShell

  $result = $form.ShowDialog()

Finally, the code inside the if block instructs Windows what to do with the form after
users select a day on the calendar, and then click the OK button or press the Enter key.
Windows PowerShell displays the selected date to users.

  PowerShell

<!-- p.600 -->

 if ($result -eq [Windows.Forms.DialogResult]::OK) {
     $date = $calendar.SelectionStart
     Write-Host "Date selected: $($date.ToShortDateString())"
 }

See also
   GitHub: Dave Wyatt's WinFormsExampleUpdates
   Windows PowerShell Tip of the Week: Creating a Graphical Date Picker)
