---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1361-1400"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1361-1400
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1361-1400
family: sccm
documentKind: "doc"
abstract: "Parameter Value Accept wildcard characters? False -Bundle [<SwitchParameter>] This parameter specifies that the application being imported is an application that is a bundle of two or more applications. This parameter is only valid for use in the last syntax example. ﾉ Expand ta"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1361-1400

<!-- p.1361 -->

 Parameter                                                 Value

 Accept wildcard characters?                               False

-Bundle [<SwitchParameter>]
This parameter specifies that the application being imported is an application that is a
bundle of two or more applications. This parameter is only valid for use in the last syntax
example.

                                                                            ﾉ   Expand table

 Parameter                                                 Value

 Required?                                                 False

 Position?                                                 Named

 Default value                                             -

 Accept pipeline input?                                    True (ByValue)

 Accept wildcard characters?                               False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a PSObject type object that references the application just
imported.

Example 1
  PowerShell

<!-- p.1362 -->

  Import-MDTApplication -Path "DS001:\Applications" -Name "Office 2010
  Professional Plus 32-bit" ApplicationSourcePath "\\WDG-MDT-
  01\Source$\Office2010ProPlus\x86" DestinationFolder "Office2010ProPlusx86"

Description
This example imports an application with source files from the network shared folder at
\\WDG-MDT-01\Source$\Office2010ProPlus\x86 and copies the source files to
DS001:\Applications\Office2010ProPlusx86 within the deployment share. The source
files are retained.

Example 2
  PowerShell

  Import-MDTApplication -Path "DS001:\Applications" -Name "Office 2010
  Professional Plus 32-bit" ApplicationSourcePath "\\WDG-MDT-
  01\Source$\Office2010ProPlus\x86" DestinationFolder "Office2010ProPlusx86" -
  Move

Description
This example imports an application with source files from the network shared folder at
\\WDG-MDT-01\Source$\Office2010ProPlus\x86 and moves the source files to
DS001:\Applications\Office2010ProPlusx86 within the deployment share. The source
files are removed from the network shared folder at \\WDG-MDT-
01\Source$\Office2010ProPlus\x86. The application is named Office 2012 Professional
Plus 32-bit.

Example 3
  PowerShell

  Import-MDTApplication -Path "DS001:\Applications" -Name "Office 2010
  Professional Plus 32-bit" NoSource

Description
This example imports an application named Office 2012 Professional Plus 32-bit with no
source files.

<!-- p.1363 -->

Example 4
  PowerShell

   Import-MDTApplication -Path "DS001:\Applications" -Name "Woodgrove Bank Core
   Applications" Bundle

Description
This example imports an application bundle named Woodgrove Bank Core Applications.

Import-MDTDriver
This section describes the Import-MDTDriver Windows PowerShell cmdlet. Run this
cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Import-MDTDriver [-Path <String>] -SourcePath <String[]> [ImportDuplicates]
   [<CommonParameters>]

Description
This cmdlet imports one or more device drivers into a deployment share. This cmdlet
searches for device drivers starting at the folder specified in the SourcePath parameter.
This cmdlet will locate multiple device drivers found in that folder structure.

Parameters
This subsection provides information about the various parameters that can be used
with the Import-MDTDriver cmdlet.

-Path <String>

<!-- p.1364 -->

This parameter specifies the fully qualified path to an existing folder where the device
driver being imported will be placed within the deployment share.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to the desired location within the deployment share. This parameter
  must be provided if the SourcePath parameter is not provided.

                                                                            ﾉ   Expand table

 Parameter                                                             Value

 Required?                                                             False

 Position?                                                             Named

 Default value                                                         -

 Accept pipeline input?                                                False

 Accept wildcard characters?                                           False

-SourcePath <String[ ]>

This parameter specifies one or more fully qualified paths in a string array for the source
folders where the device driver files are located. Each folder structure, starting with the
folder specified in this parameter, is searched for device drivers, including all subfolders
and the contents of .cab files in the folder structure.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to the folder where the device driver files are located. This parameter
  must be provided if the Path parameter is not provided.

                                                                            ﾉ   Expand table

 Parameter                                                    Value

 Required?                                                    True

 Position?                                                    1 and Named

<!-- p.1365 -->

 Parameter                                                         Value

 Default value                                                     -

 Accept pipeline input?                                            False

 Accept wildcard characters?                                       False

-ImportDuplicates [<SwitchParameter>]
This parameter specifies whether this cmdlet should import duplicate device drivers. By
default, duplicate device drivers are not imported. Duplicate device drivers are detected
by calculating a hash values for all the files in a device driver folder. If the calculated
hash value matches another device driver, the device driver to be imported is
considered a duplicate.

If a duplicate driver is detected and this parameter is not provided, the device driver will
be added and linked to the original, existing device driver.

If this parameter is:

     Specified, then the duplicate device drivers are imported

     Not specified, then the device drivers will be added and linked to the original,
     existing device drivers

                                                                                ﾉ   Expand table

 Parameter                                                     Value

 Required?                                                     False

 Position?                                                     Named

 Default value                                                 -

 Accept pipeline input?                                        True (ByValue)

 Accept wildcard characters?                                   False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more

<!-- p.1366 -->

information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs one or more PSObject type objects (one for each device driver
imported).

Example 1
  PowerShell

  Import-MDTDriver -Path "DS001:\Out-of-Box Drivers" SourcePath "\\WDG-MDT-
  01\Source$\Drivers"

Description

This example imports all device drivers in the folders structure with the root of the folder
structure at \\WDG-MDT-01\Source$\Drivers. The device drivers are stored in the Out-
of-Box Drivers folder in the deployment share that is mapped to the DS001:
MDTProvder Windows PowerShell drive. If any duplicate device drivers are detected, the
device drivers will be added and linked to the original, existing device drivers in the
deployment share.

Example 2
  PowerShell

  $DriverSourcePath="\\WDG-MDT-01\Source$\VendorADrivers", "\\WDG-MDT-
  01\Source$\VendorBDrivers"
  Import-MDTDriver -Path "DS001:\Out-of-Box Drivers" SourcePath
  $DriverSourcePath ImportDuplicates

Description

<!-- p.1367 -->

This example imports all device drivers in the folders structure specified in the string
array $DriverSourcePath. The device drivers are stored in the Out-of-Box Drivers folder
in the deployment share that is mapped to the DS001: MDTProvder Windows
PowerShell drive. If any duplicate device drivers are detected, the duplicate device
drivers are imported.

Import-MDTOperatingSystem
This section describes the Import-MDTOperatingSystem Windows PowerShell cmdlet.
Run this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-
in loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Import-MDTOperatingSystem [-Path <String>] -SourcePath <String> [-
   DestinationFolder <String>] [-Move] [<CommonParameters>]

-or-

  PowerShell

   Import-MDTOperatingSystem [-Path <String>] [DestinationFolder <String>] -
   SourceFile <String> [SetupPath <String>] [-Move] [<CommonParameters>]

-or-

  PowerShell

   Import-MDTOperatingSystem [-Path <String>] -WDSServer <String>
   [<CommonParameters>]

Description
This cmdlet imports an operating system into a deployment share. The following
operating system types can be imported using this cmdlet:

       Operating systems from the original source files, using the SourcePath parameters.
       The first syntax example illustrates the use of this cmdlet for this type of operating

<!-- p.1368 -->

     system import.

     Custom operating systems image files, such as capture images from reference
     computers, using the SourceFile parameter. The second syntax example illustrates
     the use of this cmdlet for this type of operating system import.

     Operating system images that are present in Windows Deployment Services using
     the WDSServer parameter. The last syntax example illustrates the use of this cmdlet
     for this type of operating system import.

Parameters
This subsection provides information about the various parameters that can be used
with the Import-MDTOperatingSystem cmdlet.

-Path <String>

This parameter specifies the fully qualified path to an existing folder within the
deployment share where the operating system being imported will be placed. If the
DestinationFolder parameter is used, then the folder specified in the DestinationFolder
parameter is created beneath the folder specified in this parameter. This parameter is
used in all syntax usages for this cmdlet.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to the desired location within the deployment share.

                                                                           ﾉ   Expand table

 Parameter                                                             Value

 Required?                                                             False

 Position?                                                             Named

 Default value                                                         -

 Accept pipeline input?                                                False

 Accept wildcard characters?                                           False

-SourcePath <String>

<!-- p.1369 -->

This parameter specifies the fully qualified path to the operating system source files for
the operating system that will be imported into the deployment share. This parameter is
only valid for use in the first syntax example.

                                                                          ﾉ   Expand table

 Parameter                                                            Value

 Required?                                                            True

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

 Accept wildcard characters?                                          False

-DestinationFolder <String>

This parameter specifies the folder in the deployment share where the operating system
source files are to be imported. This folder is created beneath the folder specified in the
Path parameter. This parameter is only valid for use in the first and second syntax
examples.

                                                                          ﾉ   Expand table

 Parameter                                                            Value

 Required?                                                            True

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

 Accept wildcard characters?                                          False

-Move [<SwitchParameter>]
This parameter specifies if the operating system source files should be moved (instead
of copied) from the folder where the operating system source files are located, which is
specified in the DestinationFolder parameter.

If this parameter is:

<!-- p.1370 -->

     Specified, then the files are moved and the files in the folder specified in the
     DestinationFolder parameter are deleted

     Not specified, then the files are copied and the files in the folder specified in the
     DestinationFolder parameter are retained

     This parameter is only valid for use in the first and second syntax examples.

                                                                           ﾉ   Expand table

 Parameter                                                             Value

 Required?                                                             False

 Position?                                                             Named

 Default value                                                         -

 Accept pipeline input?                                                False

 Accept wildcard characters?                                           False

-SourceFile <String>

This parameter specifies the fully qualified path to the operating system source .wim file
for the operating system that will be imported into the deployment share. This
parameter is only valid for use in the second syntax example.

                                                                           ﾉ   Expand table

 Parameter                                                             Value

 Required?                                                             True

 Position?                                                             Named

 Default value                                                         -

 Accept pipeline input?                                                False

 Accept wildcard characters?                                           False

-SetupPath <String>

This parameter specifies the fully qualified path to the operating system setup files that
need to be imported along with the .wim file specified in the SourceFile parameter. This

<!-- p.1371 -->

parameter is only valid for use in the second syntax example.

                                                                        ﾉ   Expand table

 Parameter                                                          Value

 Required?                                                          True

 Position?                                                          Named

 Default value                                                      -

 Accept pipeline input?                                             False

 Accept wildcard characters?                                        False

-WDSServer <String>

This parameter specifies the name of the Windows Deployment Services server on which
the operating system image files to be imported are located. All operating image files
on the Windows Deployment Services server will be imported into the deployment
share. The actual operating system image files are not copied to the deployment share.
Instead, the deployment share contains a link to each operating system file on the
Windows Deployment Services server.

This parameter is only valid for use in the last syntax example.

                                                                        ﾉ   Expand table

 Parameter                                                          Value

 Required?                                                          False

 Position?                                                          Named

 Default value                                                      -

 Accept pipeline input?                                             False

 Accept wildcard characters?                                        False

<CommonParameters>

This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more

<!-- p.1372 -->

information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs one or more PSObject type objects (one for each operating system
that was imported).

Example 1
  PowerShell

  Import-MDTOperatingSystem -Path "DS001:\Operating Systems" SourcePath
  "\\WDGMDT01\Source$\Windows8" DestinationFolder "Windows8x64"

Description

This example imports an operating system from the network shared folder at \\WDG-
MDT-01\Source$\Windows8 and copies the source files to DS001:\Operating
Systems\Windows8x64 within the deployment share. The source files are retained.

Example 2
  PowerShell

  Import-MDTOperatingSystem -Path "DS001:\Operating Systems" SourcePath
  "\\WDGMDT01\Source$\Windows8" DestinationFolder "Windows8x64" -Move

Description

This example imports an operating system from the network shared folder at \\WDG-
MDT-01\Source$\Windows8 and copies the source files to DS001:\Operating
Systems\Windows8x64 within the deployment share. The source files are removed from
the network shared folder at \\WDG-MDT-01\Source$\Windows8.

Example 3

<!-- p.1373 -->

  PowerShell

   Import-MDTOperatingSystem -Path "DS001:\Operating Systems" DestinationFolder
   "Windows8x64-Reference" -SourceFile "\\WDGMDT01\Capture$\WDG-REF-
   01_Capture.wim"

Description
This example imports an operating system captured, custom image file (.wim file) from
\\WDG-MDT-01\ Capture$\WDG-REF-01_Capture.wim and copies the image file to
DS001:\Operating Systems\Windows8x64-Reference within the deployment share. The
source .wim file is retained on the network shared folder.

Example 4
  PowerShell

   Import-MDTOperatingSystem -Path "DS001:\Operating Systems" WDSServer "WDG-
   WDS-01"

Description
This example imports all the operating system images from the Windows Deployment
Services server named WDG-WDS-01 and creates a link to each operating system image
in DS001:\Operating Systems within the deployment share. The source operating system
image files on the Windows Deployment Services server are retained on the Windows
Deployment Services server.

Import-MDTPackage
This section describes the Import-MDTPackage Windows PowerShell cmdlet. Run this
cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

<!-- p.1374 -->

  Import-MDTPackage [-Path <String>] [[-SourcePath] <String[]>]
  [<CommonParameters>]

Description
This cmdlet imports one or more operating system packages into a deployment share.
The types of operating system packages that can be imported include security updates,
language packs, or new components. Service packs should not be imported as operating
system packages as they cannot be installed offline.

Parameters
This subsection provides information about the various parameters that can be used
with the Import-MDTPackage cmdlet.

-Path <String>

This parameter specifies the fully qualified path to an existing folder within the
deployment share where the operating system packages being imported will be placed.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to the desired location within the deployment share.

                                                                           ﾉ   Expand table

 Parameter                                                             Value

 Required?                                                             False

 Position?                                                             Named

 Default value                                                         -

 Accept pipeline input?                                                False

 Accept wildcard characters?                                           False

-SourcePath <String>

<!-- p.1375 -->

This parameter specifies the fully qualified path to a folder structure to be scanned for
operating system packages to import. The specified folder structure will be scanned for
.cab and .msu files. For .msu files, the .cab files inside the .msu files are automatically
extracted.

                                                                              ﾉ   Expand table

 Parameter                                                      Value

 Required?                                                      True

 Position?                                                      1 and Named

 Default value                                                  -

 Accept pipeline input?                                         False

 Accept wildcard characters?                                    False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a PSObject type object that references the package just imported.

Example 1
  PowerShell

  Import-MDTOperatingSystem -Path "DS001:\Packages" SourcePath
  "\\WDGMDT01\Source$\OSPackages"

Description

<!-- p.1376 -->

This example scans network shared folder at \\WDG-MDT-01\Source$\OSPackages for
operating system packages and copies the source files to DS001:\Packages folder within
the deployment share. The source files are removed from the network shared folder at
\\WDG-MDT-01\Source$\OSPackages.

Import-MDTTaskSequence
This section describes the Import-MDTTaskSequence Windows PowerShell cmdlet. Run
this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Import-MDTTaskSequence [-Path <String>] -Template <String> -Name <String> -
   ID <String> [[-Comments] <String>] [[-Version] <String>] [-
   OperatingSystemPath <String>] [-OperatingSystem <PSObject>] [-FullName
   <String>] [-OrgName <String>] [-HomePage <String>] [-ProductKey <String>] [-
   OverrideProductKey <String>] [-AdminPassword <String>] [<CommonParameters>]

Description
This cmdlet imports a task sequence into a deployment share. The newly imported task
sequence will be based on an existing task sequence template specified in the Template
property.

Parameters
This subsection provides information about the various parameters that can be used
with the Import-MDTPackage cmdlet.

-Path <String>

This parameter specifies the fully qualified path to an existing folder within the
deployment share where the task sequence being imported will be placed. By default,
the path should point to the Control folder and or a subfolder of the Control folder in
the deployment share. The value of the ID parameter will be used to create a subfolder
within the path specified in this parameter.

<!-- p.1377 -->

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to the desired location within the deployment share.

                                                                            ﾉ   Expand table

 Parameter                                                            Value

 Required?                                                            False

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

 Accept wildcard characters?                                          False

-Template <String>

This parameter specifies the task sequence template to be used for importing the new
task sequence. Task sequence templates are .xml files that contain the task sequence
steps for a particular type of task sequence. If the task sequence template is located in:

     The installation_folder\Templates folder (where installation_folder is the folder in
     which MDT is installed), then only the .xml file name is required.

     Another folder, then the fully qualified path, including the name of the task
     sequence template .xml, is required.

     For more information on the task sequence templates that are included with MDT
     for LTI deployments, see the section "Create a New Task Sequence in the
     Deployment Workbench" in the MDT document, Using the Microsoft Deployment
     Toolkit.

                                                                            ﾉ   Expand table

 Parameter                                                    Value

 Required?                                                    True

 Position?                                                    1 and Named

 Default value                                                -

<!-- p.1378 -->

 Parameter                                                   Value

 Accept pipeline input?                                      False

 Accept wildcard characters?                                 False

-Name <String>
This parameter specifies the name of the task sequence to be imported. The value of
this parameter must be unique within the deployment share.

                                                                          ﾉ   Expand table

 Parameter                                                  Value

 Required?                                                  True

 Position?                                                  2 and Named

 Default value                                              -

 Accept pipeline input?                                     False

 Accept wildcard characters?                                False

-ID <String>

This parameter specifies the identifier of the task sequence to be imported. The value of
this parameter must be unique within the deployment share. The value assigned to this
parameter should be in uppercase and not have any spaces or special characters. This
value is used to create a subfolder in the folder specified in the Path parameter, which
should be under the Control folder in the deployment share.

                                                                          ﾉ   Expand table

 Parameter                                                  Value

 Required?                                                  True

 Position?                                                  3 and Named

 Default value                                              -

 Accept pipeline input?                                     False

 Accept wildcard characters?                                False

<!-- p.1379 -->

-Comments <String>
This parameter specifies the text that provides additional, descriptive information about
the task sequence to be imported. This descriptive information is visible in the
Deployment Workbench.

                                                                          ﾉ   Expand table

 Parameter                                                  Value

 Required?                                                  False

 Position?                                                  4 and Named

 Default value                                              -

 Accept pipeline input?                                     False

 Accept wildcard characters?                                False

-Version <String>
This parameter specifies the version number of the task sequence to be imported. The
value of this parameter is informational only and is not used by MDT for version-related
processing.

                                                                          ﾉ   Expand table

 Parameter                                                  Value

 Required?                                                  False

 Position?                                                  4 and Named

 Default value                                              -

 Accept pipeline input?                                     False

 Accept wildcard characters?                                False

-OperatingSystemPath <String>
This parameter specifies the fully qualified Windows PowerShell path to the folder in the
deployment share that contains the operating system to be used with this task
sequence, such as DS001:\Operating Systems\Windows 8. The operating system must
already exist in the deployment share where the task sequence is being imported.

<!-- p.1380 -->

  ７ Note

  If you do not provide this parameter and the task sequence needs to reference an
  operating system, then you must provide the OperatingSystem parameter.

                                                                       ﾉ   Expand table

 Parameter                                                         Value

 Required?                                                         False

 Position?                                                         Named

 Default value                                                     -

 Accept pipeline input?                                            False

 Accept wildcard characters?                                       False

-OperatingSystem <PSObject>

This parameter specifies the operating system object to be used with this task sequence.
The operating system must already exist in the deployment share where the task
sequence is being imported.

You can retrieve the Windows PowerShell object for an operating system using the Get-
Item cmdlet, such as the following example:

  PowerShell

  $OS=Get-Item "DS001:\Operating Systems\Windows 8"

For more information on the Get-Item cmdlet, see Using the Get-Item Cmdlet.

  ７ Note

  If you do not provide this parameter and the task sequence needs to reference an
  operating system, then you must provide the OperatingSystemPath parameter.

                                                                       ﾉ   Expand table

<!-- p.1381 -->

 Parameter                                                            Value

 Required?                                                            False

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

 Accept wildcard characters?                                          False

-FullName <String>
This parameter specifies the name of the registered owner of the operating system to be
used with this task sequence. This name is saved in the RegisteredOwner registry key at
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion. The value of
this parameter is injected into the Unattend.xml file to be associated with this task
sequences.

                                                                          ﾉ   Expand table

 Parameter                                                            Value

 Required?                                                            False

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

 Accept wildcard characters?                                          False

-OrgName <String>
This parameter specifies the name of the organization for the registered owner of the
operating system to be used with this task sequence. This name is saved in the
RegisteredOrganization registry key at
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion. The value of
this parameter is injected into the Unattend.xml file to be associated with this task
sequences.

                                                                          ﾉ   Expand table

<!-- p.1382 -->

 Parameter                                                            Value

 Required?                                                            False

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

 Accept wildcard characters?                                          False

-HomePage <String>
This parameter specifies the URL to be used as the home page in Internet Explorer. The
value of this parameter is injected into the Unattend.xml file to be associated with this
task sequences.

                                                                          ﾉ   Expand table

 Parameter                                                            Value

 Required?                                                            False

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

 Accept wildcard characters?                                          False

-ProductKey <String>
This parameter specifies the product key to be used for the operating system to be used
with this task sequence. This product key is valid only for retail versions of Windows
operating systems. The value of this parameter is injected into the Unattend.xml file to
be associated with this task sequences.

  ７ Note

  If this parameter is not provided, then the product key must be provided when
  deploying this task sequence in the Deployment Wizard, in the CustomSettings.ini
  file, or in the MDT DB.

<!-- p.1383 -->

                                                                         ﾉ   Expand table

 Parameter                                                           Value

 Required?                                                           False

 Position?                                                           Named

 Default value                                                       -

 Accept pipeline input?                                              False

 Accept wildcard characters?                                         False

-OverrideProductKey <String>
This parameter specifies the MAK key to be used for the operating system to be used
with this task sequence. This product key is valid only for volume license versions of
Windows. The value of this parameter is injected into the Unattend.xml file to be
associated with this task sequences.

  ７ Note

  If this parameter is not provided, then the MAK key must be provided when
  deploying this task sequence in the Deployment Wizard, in the CustomSettings.ini
  file, or in the MDT DB.

                                                                         ﾉ   Expand table

 Parameter                                                           Value

 Required?                                                           False

 Position?                                                           Named

 Default value                                                       -

 Accept pipeline input?                                              False

 Accept wildcard characters?                                         False

-AdminPassword <String>

This parameter specifies the password to be assigned to the built-in, local Administrator
account on the target computer. The value of this parameter is injected into the

<!-- p.1384 -->

Unattend.xml file to be associated with this task sequences.

  ７ Note

  If this parameter is not provided, then the password to be assigned to the built-in,
  local Administrator account on the target computer must be provided when
  deploying this task sequence in the Deployment Wizard, in the CustomSettings.ini
  file, or in the MDT DB.

                                                                         ﾉ   Expand table

 Parameter                                                           Value

 Required?                                                           False

 Position?                                                           Named

 Default value                                                       -

 Accept pipeline input?                                              False

 Accept wildcard characters?                                         False

<CommonParameters>

This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a PSObject type object that references the task sequence just
imported.

Example 1
  PowerShell

<!-- p.1385 -->

  Import-MDTTaskSequence -Path "DS001:\Control" -Template "Client.xml" -Name
  "Deploy Windows 8 to Reference Computer" -ID "WIN8REFERENCE" -Comments "Task
  sequence for deploying Windows 8 to the reference computer (WDG-REF-01)" -
  Version "1.00" -OperatingSystemPath "DS001:\Operating Systems\Windows 8_x64"
  -FullName "Woodgrove Bank Employee" -OrgName "Woodgrove Bank" HomePage
  "https://www.woodgrovebank.com" OverrideProductKey
  "1234512345123451234512345" AdministratorPassword "P@ssw0rd"

Description
This example imports a task sequence named Deploy Windows 8 to Reference Computer
and creates the task sequence in the DS001:\Control\WIN8REFERENCE folder in the
deployment share. The comment, "Task sequence for deploying Windows 8 to the
reference computer (WDG-REF-01)," is assigned to the task sequence. The version
number of the task sequence is set to 1.00.

The operating system associated with the task sequence is located at DS001:\Operating
Systems\Windows 8_x64 in the deployment share. The registered owner of the
operating system will be set to Woodgrove Bank Employee. The registered organization
of the operating system will be set to Woodgrove Bank. The Internet Explorer home
page will default to https://www.woodgrovebank.com . The password for the local, built-in
Administrator account will be set to a value of P@ssw0rd . The product key for the
operating system will be set to 1234512345123451234512345.

Example 2
  PowerShell

  $OSObject=Get-Item "DS001:\Operating Systems\Windows 8_x64"
  Import-MDTTaskSequence -Path "DS001:\Control" -Template "Client.xml" -Name
  "Deploy Windows 8 to Reference Computer" -ID "WIN8REFERENCE" -Comments "Task
  sequence for deploying Windows 8 to the reference computer (WDG-REF-01)" -
  Version "1.00"-OperatingSystem $OSObject -FullName "Woodgrove Bank Employee"
  -OrgName "Woodgrove Bank" HomePage "https://www.woodgrovebank.com"
  AdministratorPassword "P@ssw0rd"

Description

This example imports a task sequence named Deploy Windows 8 to Reference Computer
and creates the task sequence in the DS001:\Control\WIN8REFERENCE folder in the
deployment share. The comment, "Task sequence for deploying Windows 8 to the

<!-- p.1386 -->

reference computer (WDG-REF-01)," is assigned to the task sequence. The version
number of the task sequence is set to 1.00.

The operating system associated with the task sequence is located at DS001:\Operating
Systems\Windows 8_x64 in the deployment share, which is passed to the cmdlet using
the $OSObject variable. The $OSObject variable is set to an existing operating system
object using the Get-Item cmdlet.

The registered owner of the operating system will be set to Woodgrove Bank
Employee. The registered organization of the operating system will be set to
Woodgrove Bank. The Internet Explorer home page will default to
https://www.woodgrovebank.com . The password for the local, built-in Administrator

account will be set to a value of P@ssw0rd . The product key for the operating system will
need to be provided when deploying this task sequence in the Deployment Wizard, in
the CustomSettings.ini file, or in the MDT DB.

New-MDTDatabase
This section describes the New-MDTDatabase Windows PowerShell cmdlet. Run this
cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   New-MDTDatabase [-Path <String>] [-Force] -SQLServer <String> [-Instance
   <String>] [-Port <String>] [-Netlib <String>] -Database <String> [-SQLShare
   <String>] [<CommonParameters>]

Description
This cmdlet creates a new MDT DB database that is associated with a deployment share.
Each deployment share can be associated with only one MDT DB database.

Parameters
This subsection provides information about the various parameters that can be used
with the New-MDTDatabase cmdlet.

<!-- p.1387 -->

-Path <String>
This parameter specifies the fully qualified Windows PowerShell path to the deployment
share to which the new MDT DB database will be associated placed.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to the desired location within the deployment share.

                                                                            ﾉ   Expand table

 Parameter                                                           Value

 Required?                                                           False

 Position?                                                           Named

 Default value                                                       -

 Accept pipeline input?                                              False

 Accept wildcard characters?                                         False

-Force [<SwitchParameter>]
This parameter specifies that tables within the MDT DB should be recreated if the
database specified in the Database parameter already exist. If this parameter is:

     Provided, then the tables within an existing MDT DB will be re-created

     Omitted, then the tables within an existing MDT DB will not be re-created

                                                                            ﾉ   Expand table

 Parameter                                                 Value

 Required?                                                 False

 Position?                                                 Named

 Default value                                             -

 Accept pipeline input?                                    True (ByValue)

 Accept wildcard characters?                               False

<!-- p.1388 -->

-SQLServer <String>
This parameter specifies the name of the computer running SQL Server where the new
MDT DB database will be created.

                                                                         ﾉ    Expand table

 Parameter                                                           Value

 Required?                                                           True

 Position?                                                           Named

 Default value                                                       -

 Accept pipeline input?                                              False

 Accept wildcard characters?                                         False

-Instance <String>

This parameter specifies the SQL Server instance in which the new MDT DB database will
be created. If this parameter is omitted, the MDT DB database is created in the default
SQL Server instance.

  ７ Note

  The SQL Server Browser service must be running on the computer running SQL
  Server for the cmdlet to locate the instance specified in this parameter.

                                                                         ﾉ    Expand table

 Parameter                                                           Value

 Required?                                                           False

 Position?                                                           Named

 Default value                                                       -

 Accept pipeline input?                                              False

 Accept wildcard characters?                                         False

-Port <String>

<!-- p.1389 -->

This parameter specifies the TCP port to be used in communication with the SQL Server
instance specified in the SQLServer parameter. The default port that SQL Server uses is
1433. Specify this parameter when SQL Server is configured to use a port other than the
default value. The value of this parameter must match the port configured for SQL
Server.

                                                                        ﾉ   Expand table

 Parameter                                                          Value

 Required?                                                          False

 Position?                                                          Named

 Default value                                                      -

 Accept pipeline input?                                             False

 Accept wildcard characters?                                        False

-Netlib <String>

This parameter specifies the SQL Server network library used in communication with the
SQL Server instance specified in the SQLServer parameter. The parameter can be set to
one of the following values:

     DBNMPNTW, which is used to specify named pipes communication

     DBSMSOCN, which is used to specify TCP/IP sockets communication

     If this parameter is not provided, the named pipes SQL Server network library
     (DBNMPNTW) is used.

                                                                        ﾉ   Expand table

 Parameter                                                          Value

 Required?                                                          False

 Position?                                                          Named

 Default value                                                      -

 Accept pipeline input?                                             False

 Accept wildcard characters?                                        False

<!-- p.1390 -->

-Database <String>
This parameter specifies the name of the database to be created in the SQL Server
instance specified in the Instance parameter on the SQL Server specified in the
SQLServer parameter. The default location and naming convention will be used for the
database and log files when creating the database.

If the database specified in this parameter already exists, the database will not be
recreated. The tables within the database can be recreated based on the Force
parameter.

                                                                          ﾉ   Expand table

 Parameter                                                            Value

 Required?                                                            True

 Position?                                                            Named

 Default value                                                        -

 Accept pipeline input?                                               False

 Accept wildcard characters?                                          False

-SQLShare <String>

This parameter specifies the name of a network shared folder on the computer where
SQL Server is running. This connection is used to establish Windows Integrated Security
connections using the Named Pipes protocol.

  ７ Note

  If this parameter is not included, then a secured IPC$ connection is not established.
  As a result, named pipes communication with SQL Server may fail.

                                                                          ﾉ   Expand table

 Parameter                                                            Value

 Required?                                                            False

 Position?                                                            Named

 Default value                                                        -

<!-- p.1391 -->

 Parameter                                                        Value

 Accept pipeline input?                                           False

 Accept wildcard characters?                                      False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a PSObject type object for the new MDT DB that was created.

Example 1
  PowerShell

  New-MDTDatabase -Path "DS001:" -SQLServer "WDGSQL01" Database "MDTDB" -
  SQLShare "\\WDGSQL01\MDTShare$"

Description

This example creates an MDT DB named MDTDB in the default SQL Server instance on a
computer named WDG-SQL-01. If the database already exists, the tables in the existing
database will not be recreated. The connection will be made using the default SQL
Server TCP port and the Named Pipes protocol.

Example 2
  PowerShell

  New-MDTDatabase -Path "DS001:" -Force -SQLServer "WDGSQL01" -Instance

<!-- p.1392 -->

   "MDTInstance" Database "MDTDB" -SQLShare "\\WDGSQL01\MDTShare$"

Description
This example creates an MDT DB named MDTDB in the SQL Server instance named
MDTInstance on a computer named WDG-SQL-01. If the database already exists, the
tables in the existing database will be recreated. The connection will be made using the
default SQL Server TCP port and the Named Pipes protocol.

Remove-MDTMonitorData
This section describes the Get-MDTPersistentDrive Windows PowerShell cmdlet. Run
this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-in
loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Remove-MDTMonitorData [-Path <String>] [-ID <Int32>] [<CommonParameters>]

-or-

  PowerShell

   Remove-MDTMonitorData [-Path <String>] [-ComputerObject <PSObject>]
   [<CommonParameters>]

Description
This cmdlet removes collected monitoring data from the existing collected monitoring
data in a deployment share. You can identify the monitoring data to remove by
specifying the:

       Identifier (ID) of the monitoring item for a specific deployment share. The
       monitoring item IDs are automatically generated and assigned to the item when
       the item is created for the deployment share. The first syntax example illustrates
       this usage.

<!-- p.1393 -->

     Computer object for the monitoring item in the deployment share. The computer
     object can be obtained using the Get-MDTMonitorData cmdlet. The last syntax
     example illustrates this usage.

  ７ Note

  Once the monitoring data has been removed, there is no method for recovering
  the information.

Parameters
This subsection provides information about the various parameters that can be used
with the Get- MDTMonitorData cmdlet.

-Path <String>
This parameter specifies the MDTProvider Windows PowerShell drive for the desired
deployment share.

  ７ Note

  If this parameter is not provided, then the Windows PowerShell working directory
  must default to a location within the desired MDTProvider Windows PowerShell
  drive.

                                                                      ﾉ   Expand table

 Parameter                                                        Value

 Required?                                                        False

 Position?                                                        Named

 Default value                                                    -

 Accept pipeline input?                                           False

 Accept wildcard characters?                                      False

-ID <Nullable>

<!-- p.1394 -->

This parameter specifies the monitoring data item to be removed using the identifier of
the monitoring data item. If this parameter is not specified, then the ComputerObject
parameter must be specified to identify a particular monitoring data item.

                                                                            ﾉ   Expand table

 Parameter                                                 Value

 Required?                                                 False

 Position?                                                 Named

 Default value                                             -

 Accept pipeline input?                                    True (ByValue)

 Accept wildcard characters?                               False

-ComputerObject <PSObject>

This parameter specifies the monitoring data item to be removed using a computer
object. If this parameter is not specified, then the ID parameter must be specified to
identify a particular monitoring data item.

                                                                            ﾉ   Expand table

 Parameter                                                 Value

 Required?                                                 False

 Position?                                                 Named

 Default value                                             -

 Accept pipeline input?                                    True (ByValue)

 Accept wildcard characters?                               False

<CommonParameters>

This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

<!-- p.1395 -->

  Get-Help about_CommonParameters

Outputs
This cmdlet may output a String type object if the Verbose common parameter is
included; otherwise, no output is generated.

Example 1
  PowerShell

  Remove-MDTMonitorData -Path "DS001:" -ID 3

Description
This example removes the monitoring data item with an ID that has a value of 3 from
the deployment share at the Windows PowerShell path DS001:.

Example 2
  PowerShell

  Remove-MDTMonitorData -ID 3

Description

This example removes the monitoring data item with an ID that has a value of 3 from
the deployment share at the default Windows PowerShell path.

Example 3
  PowerShell

  $MonitorObject=Get-MDTMonitorData | Where-Object {$_.Name eq 'WDG-REF-01'}
  Remove-MDTMonitorData -ComputerObject $MonitorObject

Description

<!-- p.1396 -->

This example removes any monitoring data item where the name of the computer is
WDG-REF-01. The object is found using the Get-MDTMonitorData cmdlet and the
Where-Object cmdlet. For more information on the Where-Object cmdlet, see Using
the Where-Object Cmdlet.

Remove-MDTPersistentDrive
This section describes the Remove-MDTPersistentDriveWindows Windows PowerShell
cmdlet. Run this cmdlet from a Windows PowerShell console that has the MDT
PowerShell snap-in loaded. For more information on how to start a Windows PowerShell
console that has the MDT PowerShell snap-in loaded, see "Loading the MDT Windows
PowerShell Snap-In".

Syntax
  PowerShell

  Remove-MDTPersistentDrive [-Name] <String> [[-InputObject] <PSObject>]
  [<CommonParameters>]

Description
This cmdlet removes an existing Windows PowerShell drive created using the
MDTProvider from the list of drives that are persisted in the Deployment Workbench or
in a Windows PowerShell session using the Restore-MDTPersistentDrive cmdlet. This
cmdlet is called when a deployment share is closed in (removed from) the Deployment
Workbench.

  ７ Note

  The list of persisted MDTProvider drives is maintained on a per-user based in the
  user profile.

The list of persisted MDTProvider drives can be displayed using the Get-
MDTPersistentDrive cmdlet. An MDTProvider drive can be added to the list of persisted
drives using the Add-MDTPersistentDrive cmdlet.

Parameters

<!-- p.1397 -->

This subsection provides information about the various parameters that can be used
with the Add-MDTPersistentDriveWindows cmdlet.

-Name <String>

Specifies the name of a Windows PowerShell drive created using the MDT provider and
corresponds to an existing deployment share. The name was created using the New-
PSDrive      cmdlet and specifying the MDTProvider in the PSProvider parameter.

For more information on how to create a new Windows PowerShell drive using the
MDTProvider and how to create a deployment share using Windows PowerShell, see the
section "Creating a Deployment Share Using Windows PowerShell" in the MDT
document, Microsoft Deployment Toolkit Samples Guide.

                                                                           ﾉ   Expand table

 Parameter                                                Value

 Required?                                                True

 Position?                                                1 and Named

 Default value                                            None

 Accept pipeline input?                                   True (ByValue)

 Accept wildcard characters?                              False

-InputObject <PSObject>

This parameter specifies a Windows PowerShell drive object that was created earlier in
the process. Enter a PSObject object, such as one generated by the New-PSDrive
cmdlet.

                                                                           ﾉ   Expand table

 Parameter                                                Value

 Required?                                                False

 Position?                                                2 and Named

 Default value                                            -

 Accept pipeline input?                                   True (ByValue)

<!-- p.1398 -->

 Parameter                                               Value

 Accept wildcard characters?                             False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet provides no outputs.

Example 1
  PowerShell

  Remove-MDTPersistentDrive -Name "DS001:"

Description

This example removes the deployment share with the Windows PowerShell drive name
of DS001 from the list of persisted drives.

Example 2
  PowerShell

  $MDTPSDrive = Get-PSDrive | Where-Object {$_.Root -eq "C:\DeploymentShare" -
  and $_.Provider -like "*MDTProvider"}
  Remove-MDTPersistentDrive -InputObject $MDTPSDrive

Description

<!-- p.1399 -->

This example removes the deployment share at C:\DeploymentShare$ from the list of
persisted drives. The GetPSDrive and Where-Object cmdlets are used to return the MDT
persisted Windows PowerShell drive to the Remove-MDTPersistentDrive cmdlet using
the $MDTPSDrive variable. For more information on the Where-Object cmdlet, see
Using the Where-Object Cmdlet. For more information on the Get-PSDrive cmdlet, see
Using the Get-PSDrive Cmdlet.

Restore-MDTPersistentDrive
This section describes the Restore-MDTPersistentDrive Windows PowerShell cmdlet.
Run this cmdlet from a Windows PowerShell console that has the MDT PowerShell snap-
in loaded. For more information on how to start a Windows PowerShell console that has
the MDT PowerShell snap-in loaded, see "Loading the MDT Windows PowerShell Snap-
In".

Syntax
  PowerShell

   Restore-MDTPersistentDrive [-Force] [<CommonParameters>]

Description
This cmdlet restores a persisted MDT Windows PowerShell drive to the list of active
Windows PowerShell drive for each deployment share that was added to the list of
persisted MDT Windows PowerShell drives. The list of persisted MDT Windows
PowerShell drives is managed using the Add-MDTPersistentDrive and Remove-
MDTPersistentDrive cmdlets or the Deployment Workbench.

This cmdlet calls the New-PSDrive cmdlet to create a Windows PowerShell drive for
each drive in the MDT persisted list. Persisted MDT Windows PowerShell drives are
similar to persisted network drive mappings.

  ７ Note

  This list of persisted MDT Windows PowerShell drives is maintained on a per-user
  basis and are stored in the user profile.

Parameters

<!-- p.1400 -->

This subsection provides information about the various parameters that can be used
with the Restore-MDTPersistentDrive cmdlet.

-Force [<SwitchParameter>]

This parameter specifies that the deployment share should be upgraded when restored
(if required). If this parameter is:

      Provided, then the deployment share will be upgraded when restored (if required)

      Omitted, then deployment share will not be upgraded when restored

                                                                          ﾉ   Expand table

 Parameter                                               Value

 Required?                                               False

 Position?                                               Named

 Default value                                           -

 Accept pipeline input?                                  True (ByValue)

 Accept wildcard characters?                             False

<CommonParameters>
This cmdlet supports the following common parameters: Verbose, Debug, ErrorAction,
ErrorVariable, OutBuffer, OutVariable, WarningAction, and WarningVariable. For more
information, see the topic, "about_CommonParameters," which you can access by typing
the following command, and then pressing ENTER:

  PowerShell

  Get-Help about_CommonParameters

Outputs
This cmdlet outputs a PSObject type object for each MDT Provider Windows PowerShell
drive that is restored.

Example 1
