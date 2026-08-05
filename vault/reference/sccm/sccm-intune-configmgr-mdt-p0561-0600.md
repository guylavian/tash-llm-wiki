---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 561-600"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0561-0600
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0561-0600
family: sccm
documentKind: "doc"
abstract: "Viewing the List of Deployment Shares Using Windows PowerShell You can view the list of MDT deployment shares using the Get-PSDrive cmdlet and the MDTProvider Windows PowerShell provider. The same list of deployment shares can also be viewed in the Deployment Workbench. To view"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 561-600

<!-- p.561 -->

Viewing the List of Deployment Shares Using Windows
PowerShell
You can view the list of MDT deployment shares using the Get-PSDrive cmdlet and the
MDTProvider Windows PowerShell provider. The same list of deployment shares can
also be viewed in the Deployment Workbench.

To view a list of deployment shares using the MDT Windows PowerShell cmdlets

  1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
     Windows PowerShell Snap-In.

  2. Ensure that the MDT deployments share Windows PowerShell drives are restored
     using the Restore-MDTPersistentDrive cmdlet, as shown in the following example:

       PowerShell

       Restore-MDTPersistentDrive -Verbose

       ７ Note

       If the MDT deployments that share Windows PowerShell drives are already
       restored, you will receive a warning message indicating that the cmdlet is
       unable to restore the drive.

  3. View the list of MDT deployments that share Windows PowerShell drives, one for
     each deployment share, using the Get-PSDrive cmdlet, as follows:

       PowerShell

       Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

     The list of Windows PowerShell drives provided using the MDTProvider are listed,
     one for each deployment share.

Updating a Deployment Share Using Windows
PowerShell
You can update deployment shares using the Update-MDTDeploymentShare cmdlet
and the MDTProvider Windows PowerShell provider. Updating a deployment share
creates the Windows PE boot images (WIM and International Organization for

<!-- p.562 -->

Standardization [ISO] files) necessary to start LTI deployment. You can perform the same
process using the Deployment Workbench, as described in "Update a Deployment Share
in the Deployment Workbench".

To update a deployment share using Windows PowerShell

   1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
     Windows PowerShell Snap-In.

   2. Ensure that the MDT deployments that share Windows PowerShell drives are
     restored using the Restore-MDTPersistentDrive cmdlet, as shown in the following
     example:

       PowerShell

       Restore-MDTPersistentDrive -Verbose

       ７ Note

       If the MDT deployments that share Windows PowerShell drives are already
       restored, you will receive a warning message indicating that the cmdlet is
       unable to restore the drive.

   3. Verify that the MDT deployments that share Windows PowerShell drives are
     restored properly using the Get-PSDrive cmdlet, as follows:

       PowerShell

       Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

     The list of Windows PowerShell drives provided using the MDTProvider are listed.

   4. Update the deployment share using the Update-MDTDeploymentShare cmdlet, as
     shown in the following example:

       PowerShell

       Update-MDTDeploymentShare -Path "DS002:" -Force

     In this example, DS002: is the name of a Windows PowerShell drive returned in
     step 3.

<!-- p.563 -->

       ７ Note

       Updating the deployment share can take a long time. The progress of the
       cmdlet is shown at the top of the Windows PowerShell console.

     The cmdlet returns with no output if the update is successful.

Updating a Linked Deployment Share Using Windows
PowerShell
You can update (replicate) linked deployment shares using the Update-MDTLinkedDS
cmdlet and the MDTProvider Windows PowerShell provider. Updating a linked
deployment share replicates the content from the original deployment share to the
linked deployment share. You can perform the same process using the Deployment
Workbench, as described in "Replicate Linked Deployment Shares in the Deployment
Workbench".

To update a linked deployment share using Windows PowerShell

  1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
     Windows PowerShell Snap-In.

  2. Ensure that the MDT deployments that share Windows PowerShell drives are
     restored using the Restore-MDTPersistentDrive cmdlet, as shown in the following
     example:

       PowerShell

       Restore-MDTPersistentDrive -Verbose

       ７ Note

       If the MDT deployments that share Windows PowerShell drives are already
       restored, you will receive a warning message indicating that the cmdlet is
       unable to restore the drive.

  3. Verify that the MDT deployments that share Windows PowerShell drives are
     restored properly using the Get-PSDrive cmdlet, as follows:

       PowerShell

<!-- p.564 -->

       Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

     The list of Windows PowerShell drives provided using the MDTProvider are listed.

   4. Update the deployment share using the Update-MDTDeploymentShare cmdlet, as
     shown in the following example:

       PowerShell

       Update-MDTLinkedDS -Path "DS002:\Linked Deployment Shares\LINKED002"

     In this example, DS002: is the name of a Windows PowerShell drive returned in
     step 3.

       ７ Note

       Updating the linked deployment share can take a long time. The progress of
       the cmdlet is shown at the top of the Windows PowerShell console.

     The cmdlet returns with no output if the update is successful.

Updating Deployment Media Using Windows PowerShell
You can update (generate) deployment media using the Update-MDTMedia cmdlet and
the MDTProvider Windows PowerShell provider. Updating deployment media replicates
the content from the original deployment share to the linked deployment share, and
then generates .iso and .wim files. You can perform the same process using the
Deployment Workbench, as described in "Generate Media Images in the Deployment
Workbench".

When the Update-MDTMedia cmdlet finishes, the following files are created:

     An .iso file in the media_folder folder (where media_folder is the name of the folder
     that you specified for the media)

     Generating the .iso file is an option that you configure by:

        Selecting the Generate a Lite Touch bootable ISO image check box on the
        General tab of the media Properties dialog box (Clear this check box to reduce
        the time needed to generate the media unless you need to create bootable
        DVDs or start virtual machines [VMs] from the .iso file.)

<!-- p.565 -->

     Setting the same property using the Set-ItemProperty cmdlet

  WIM files in the media_folder\Content\Deploy\Boot folder (where media_folder is
  the name of the folder that you specified for the media)

  To update a linked deployment share using Windows PowerShell

1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
  Windows PowerShell Snap-In.

2. Ensure that the MDT deployments share Windows PowerShell drives are restored
  using the Restore-MDTPersistentDrive cmdlet, as shown in the following example:

    PowerShell

    Restore-MDTPersistentDrive -Verbose

    ７ Note

    If the MDT deployments that share Windows PowerShell drives are already
    restored, you will receive a warning message indicating that the cmdlet is
    unable to restore the drive.

3. Verify that the MDT deployments that share Windows PowerShell drives are
  restored properly using the Get-PSDrive cmdlet, as follows:

    PowerShell

    Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

  The list of Windows PowerShell drives provided using the MDTProvider are listed.

4. Update the deployment share using the Update-MDTDeploymentShare cmdlet, as
  shown in the following example:

    PowerShell

    Update-MDTLinkedDS -Path "DS002:\Linked Deployment Shares\LINKED002"

  In this example, DS002: is the name of a Windows PowerShell drive returned in
  step 3.

    ７ Note

<!-- p.566 -->

          Updating the linked deployment share can take a long time. The progress of
          the cmdlet is shown at the top of the Windows PowerShell console.

     The cmdlet returns with no output if the update is successful.

Managing Items in a Deployment Share Using Windows
PowerShell
A deployment share contains items that are used to perform deployments, such as
operating systems, applications, device drivers, operating system packages, and task
sequences. These items can managed using cmdlets from Windows PowerShell and
those provided with MDT.

For more information about manipulating items directly using Windows PowerShell
cmdlets, see Manipulating Items Directly. The folder structure for a deployment share
can also be managed using Windows PowerShell. For more information, see Managing
Deployment Share Folders Using Windows PowerShell.

Import an Item into a Deployment Share

You can import each type of item, such as operating systems, applications, or device
drivers, using MDT cmdlets. For each type of item, there is a specific MDT cmdlet. If you
want to import multiple items into a deployment share using Windows PowerShell, see
Automating Population of a Deployment Share.

The following table lists the MDT Windows PowerShell cmdlets used to import items
into a deployment share and provides a brief description of each cmdlet. Examples of
how to use each cmdlet is provided in the section that corresponds to each cmdlet.

                                                                               ﾉ   Expand table

 Cmdlet                       Description

 Import-MDTApplication        Imports an application into a deployment share

 Import-MDTDriver             Imports one or more device drivers into a deployment share

 Import-                      Imports one or more operating systems into a deployment share
 MDTOperatingSystem

 Import-MDTPackage            Imports one or more operating system packages into a
                              deployment share

 Import-MDTTaskSequence       Imports a task sequence into a deployment share

<!-- p.567 -->

View the Properties of an Item in a Deployment Share
Each item in a deployment share has different set of properties. You can view the
properties of an item in a deployment share using the Get-ItemProperty cmdlet. The
Get-ItemProperty cmdlet uses the MDTProvider to display the properties for a specific
item, just as you can see the properties in the Deployment Workbench.

If want wish to view the properties of multiple items in a deployment share using
Windows PowerShell, see Automating Population of a Deployment Share.

To view the properties of an item in a deployment share using Windows PowerShell

   1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
     Windows PowerShell Snap-In.

   2. Ensure that the MDT deployments that share Windows PowerShell drives are
     restored using the Restore-MDTPersistentDrive cmdlet, as shown in the following
     example:

       PowerShell

        Restore-MDTPersistentDrive -Verbose

       ７ Note

       If the MDT deployments that share Windows PowerShell drives are already
       restored, you will receive a warning message indicating that the cmdlet is
       unable to restore the drive.

   3. Verify that the MDT deployments that share Windows PowerShell drives are
     restored properly using the Get-PSDrive cmdlet, as shown in the following
     example:

       PowerShell

        Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

     The list of Windows PowerShell drives provided using the MDTProvider are listed.

   4. Return a list of the items for the type of item for which you are wanting to view the
     properties using the Get-Item cmdlet, as shown in the following example:

       PowerShell

<!-- p.568 -->

       Get-Item "DS001:\Operating Systems\*" | Format-List

     In the previous example, a list of all the operating systems in the deployment share
     is displayed. The output is piped to the Format-List cmdlet so that the long names
     of the operating systems can be seen. For more information on how to use the
     Format-List cmdlet, see Using the Format-List Cmdlet. The same process could be
     used to return the list of other types of items, such as device drivers or
     applications.

        Tip

       You could have also used the dir command to view the list of operating
       systems instead of the Get-Item cmdlet.

  5. View the properties of one of the items listed in the previous step using the Get-
     ItemProperty cmdlet, as shown in the following example:

       PowerShell

       Get-ItemProperty -Path "DS002:\Operating Systems\Windows 8 in Windows 8
       x64 install.wim"

     In this example, the value of the Path parameter is the fully qualified Windows
     PowerShell path to the item, including the file name that was returned in the
     previous step. You could use the same process to view the properties of other
     types of items, such as device drivers or applications.

Remove an Item from a Deployment Share
You can remove an item from a deployment share using the Remove-Item cmdlet. The
Remove-Item cmdlet uses the MDTProvider to remove a specific item, just as you can
remove an item in the Deployment Workbench. If you want to remove multiple items in
a deployment share using Windows PowerShell, see Automating Population of a
Deployment Share.

  ７ Note

  Removing an item that a task sequence uses causes the task sequence to fail.
  Ensure that an item is not referenced by other items in the deployment share prior
  to removing the item. Once an item is removed, it cannot be recovered.

<!-- p.569 -->

To remove an item from a deployment share using Windows PowerShell

  1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
    Windows PowerShell Snap-In.

  2. Ensure that the MDT deployments that share Windows PowerShell drives are
    restored using the Restore-MDTPersistentDrive cmdlet, as shown in the following
    example.

      PowerShell

       Restore-MDTPersistentDrive -Verbose

      ７ Note

      If the MDT deployments that share Windows PowerShell drives are already
      restored, you will receive a warning message indicating that the cmdlet is
      unable to restore the drive.

  3. Verify that the MDT deployments that share Windows PowerShell drives are
    restored properly using the Get-PSDrive cmdlet, as shown in the following
    example:

      PowerShell

       Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

    The list of Windows PowerShell drives provided using the MDTProvider are listed.

  4. Return a list of the items for the type of item for which you are wanting to view the
    properties using the Get-Item cmdlet, as shown in the following example:

      PowerShell

       Get-Item "DS001:\Operating Systems\*" | Format-List

    In the previous example, a list of all the operating systems in the deployment share
    is displayed. The output is piped to the Format-List cmdlet so that the long names
    of the operating systems can be seen. For more information on how to use the
    Format-List cmdlet, see Using the Format-List Cmdlet. You could use the same
    process to return the list of other types of items, such as device drivers or
    applications.

<!-- p.570 -->

        Tip

       You could have also used the dir command to view the list of operating
       systems instead of the Get-Item cmdlet.

   5. Remove one of the items listed in the previous step using the Remove-Item
     cmdlet, as shown in the following example:

       PowerShell

        Remove-Item -Path "DS002:\Operating Systems\Windows 8 in Windows 8 x64
        install.wim"

     In this example, the value of the Path parameter is the fully qualified Windows
     PowerShell path to the item, including the file name that was returned in the
     previous step.

     You could use the same process to remove other types of items, such as device
     drivers or applications.

       ７ Note

       Removing an item that a task sequence uses causes the task sequence to fail.
       Ensure that an item is not referenced by other items in the deployment share
       prior to removing the item.

Automating Population of a Deployment Share
The MDT Windows PowerShell cmdlets allow you to manage individual items. However,
by using some of the scripting features in Windows PowerShell, the cmdlets can be used
to automate the population of a deployment share.

For example, an organization may need to deploy multiple deployment shares for
different business units, or an organization may provide operating system deployment
services for other organizations. In both of these examples, the organizations need the
ability to create and populate deployment shares that are configured consistently.

One method for managing multiple items would be to use a comma-separated values
(CSV) file that contains a list of all the items you want to manage in a deployment share
using the Import-CSV     cmdlet.

<!-- p.571 -->

The following is an excerpt of a Windows PowerShell script to import a list of
applications based on information in a .csv file using the Import-CSV , ForEach-Object,
and Import-MDTApplication cmdlets:

  PowerShell

  $List=Import-CSV "C:\MDT\Import-MDT-Apps.csv"
  ForEach-Object ($App in $List) {
       Import-MDTApplication -path $App.ApplicationFolder -enable "True" -Name
  $App.DescriptiveName -ShortName $App.Shortname -Version $App.Version -
  Publisher $App.Publisher -Language $App.Language -CommandLine
  $App.CommandLine -WorkingDirectory $App.WorkingDirectory -
  ApplicationSourcePath $App.SourceFolder -DestinationFolder
  $App.DestinationFolder -Verbose
  }

In this example, the C:\MDT\Import-MDT-Apps.csv file contains a field for each variable
necessary to import an application. For more information about how to create a .csv file
for use with the Import-CSV     cmdlet, see Using the Import-Csv Cmdlet.

You can use this same method to import operating systems, device drivers, and other
items in a deployment share by performing the following steps:

   1. Create a .csv file for each type of deployment share item that you want to
     populate.

   2. For more information about how to create a .csv file for use with the Import-CSV
     cmdlet, see Using the Import-Csv Cmdlet.

   3. Create a Windows PowerShell script file that will be used to automate the
     population of the deployment share.

     For more information about how to create a Windows PowerShell script, see
     Scripting with Windows PowerShell.

   4. Create any prerequisite folder structure required in the deployment share prior to
     importing the deployment share items.

     For more information, see Managing Deployment Share Folders Using Windows
     PowerShell.

   5. Add the Import-CSV      cmdlet line for one of the .csv files created in step 1.

     For more information on the Import-CSV         cmdlet, see Using the Import-Csv
     Cmdlet.

<!-- p.572 -->

   6. Create a ForEach-Object cmdlet loop that processes each item from the .csv file
     referenced in the Import-CSV    cmdlet in the previous step.

     For more information on the ForEach-Object cmdlet, see Using the ForEach-Object
     Cmdlet.

   7. Add the corresponding MDT cmdlet for importing the deployment share items
     inside the ForEach-Object cmdlet loop created in the previous step.

     For more information on the MDT cmdlets used for importing items into a
     deployment share, see Import an Item into a Deployment Share.

Managing Deployment Share Folders Using Windows
PowerShell
You can manage folders in a deployment share using command-line tools, such as the
mkdir command, or using Windows PowerShell cmdlets, such as the New-Item cmdlet
and the MDTProvider Windows PowerShell provider. The same folder structure of
deployment shares can also be seen and managed in the Deployment Workbench. For
more information about manipulating items directly using Windows PowerShell cmdlets,
see Manipulating Items Directly.

Create a Folder in a Deployment Share Using Windows PowerShell

To create a folder in a deployment share using Windows PowerShell

   1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
     Windows PowerShell Snap-In.

   2. Ensure that the MDT deployments that share Windows PowerShell drives are
     restored using the Restore-MDTPersistentDrive cmdlet, as shown in the following
     example:

       PowerShell

       Restore-MDTPersistentDrive -Verbose

       ７ Note

<!-- p.573 -->

    If the MDT deployments that share Windows PowerShell drives are already
    restored, you will receive a warning message indicating that the cmdlet is
    unable to restore the drive.

3. View the list of MDT deployments that share Windows PowerShell drives, one for
  each deployment share, using the Get-PSDrive cmdlet as follows:

    PowerShell

    Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

  The list of Windows PowerShell drives provided using the MDTProvider are listed,
  one for each deployment share

4. Create a folder named Windows_8 in the Operating Systems folder in a
  deployment share using the New-Item command, as shown in the following
  example:

    PowerShell

    New-Item "DS002:\Operating Systems\Windows_8"

  In this example, DS002: is the name of a Windows PowerShell drive returned in
  step 3.

5. Verify that the folder is created correctly by typing the following command:

    PowerShell

    Get-ChildItem "DS002:\Operating Systems"

  The Windows_8 folder and any other existing folders in the Operating Systems
  folder is displayed.

6. Create a folder named Windows_7 folder in the Operating Systems folder in a
  deployment share using the New-Item cmdlet, as shown in the following example
  and described in Using the New-Item Cmdlet:

    PowerShell

    New-Item "DS002:\Operating Systems\Windows_7" -Type directory

  The cmdlet displays the successful creation of the folder.

<!-- p.574 -->

  7. Verify that the folder is created correctly by typing the following command:

       PowerShell

       Get-ChildItem "DS002:\Operating Systems"

     The Windows_7 folder and any other existing folders in the Operating Systems
     folder is displayed.

Delete a Folder in a Deployment Share Using Windows PowerShell
To delete a folder in a deployment share using Windows PowerShell

  1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
     Windows PowerShell Snap-In.

  2. Ensure that the MDT deployments that share Windows PowerShell drives are
     restored using the Restore-MDTPersistentDrive cmdlet, as shown in the following
     example:

       PowerShell

       Restore-MDTPersistentDrive -Verbose

       ７ Note

       If the MDT deployments that share Windows PowerShell drives are already
       restored, you will receive a warning message indicating that the cmdlet is
       unable to restore the drive.

  3. View the list of MDT deployments that share Windows PowerShell drives, one for
     each deployment share, using the Get-PSDrive cmdlet as follows:

       PowerShell

       Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

     The list of Windows PowerShell drives provided using the MDTProvider are listed,
     one for each deployment share.

  4. Delete (remove) a folder named Windows_8 in the Operating Systems folder in a
     deployment share using the New-Item command, as shown in the following

<!-- p.575 -->

    example:

       PowerShell

       Remove-Item "DS002:\Operating Systems\Windows_8"

    In this example, DS002: is the name of a Windows PowerShell drive returned in
    step 3.

  5. Verify that the folder is removed correctly by typing the following command:

       PowerShell

       Get-ChildItem "DS002:\Operating Systems"

    The Windows_8 folder is no longer displayed in the list of folders in the Operating
    Systems folder

  6. Delete (remove) a folder named Windows_7 folder in the Operating Systems folder
    in a deployment share using the Remove-Item cmdlet, as shown in the following
    example:

       PowerShell

       Remove-Item "DS002:\Operating Systems\Windows_7"

    The cmdlet displays the successful removal of the folder.

  7. Verify that the folder is created correctly by typing the following command:

       PowerShell

       Get-ChildItem "DS002:\Operating Systems"

    The Windows_7 folder is no longer displayed in the list of folders in the Operating
    Systems folder.

Rename a Folder in a Deployment Share Using Windows
PowerShell

To rename a folder in a deployment share using Windows PowerShell

<!-- p.576 -->

1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
  Windows PowerShell Snap-In.

2. Ensure that the MDT deployments share Windows PowerShell drives are restored
  using the Restore-MDTPersistentDrive cmdlet, as shown in the following example:

    PowerShell

    Restore-MDTPersistentDrive -Verbose

    ７ Note

    If the MDT deployments that share Windows PowerShell drives are already
    restored, you will receive a warning message indicating that the cmdlet is
    unable to restore the drive.

3. View the list of MDT deployments share Windows PowerShell drives, one for each
  deployment share, using the Get-PSDrive cmdlet as follows:

    PowerShell

    Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

  The list of Windows PowerShell drives provided using the MDTProvider are listed,
  one for each deployment share.

4. Rename a folder named Windows_8 to Win_8 in the Operating Systems folder in a
  deployment share using the ren command, as shown in the following example:

    PowerShell

    ren "DS002:\Operating Systems\Windows_8" "Win_8"

  In this example, DS002: is the name of a Windows PowerShell drive returned in
  step 3.

5. Verify that the folder is removed correctly by typing the following command:

    PowerShell

    Get-ChildItem "DS002:\Operating Systems"

  The Windows_8 folder is renamed to Win_8.

<!-- p.577 -->

   6. Rename a folder named Windows_7 to Win-7 in the Operating Systems folder in a
     deployment share using the Rename-Item cmdlet, as shown in the following
     example:

       PowerShell

        Rename-Item "DS002:\Operating Systems\Windows_7" "Win_7"

     The cmdlet displays the successful rename of the folder.

   7. Verify that the folder is created correctly by typing the following command:

       PowerShell

        Get-ChildItem "DS002:\Operating Systems"

     The Windows_7 folder is renamed to Win_7.

Automating the Application of Operating
System Service Packs in Deployment Shares
Operating system service packs are a normal part of the software life cycle. The existing
operating systems in deployment shares need to be updated with these service packs to
help ensure that newly deployed or refreshed computers are current with the latest
security recommendations and configuration settings.

In instances where an organization has many deployment shares with multiple operating
systems in each deployment share, the process for manually updating the operating
systems in each deployment share with the service packs can be time consuming. The
methods for automating the application of operating system service packs in
deployment shares include:

     Copying updated source content that already contains the service pack (for
     example, Windows 7 with SP1 media) to the folder in the deployment share in
     which the existing operating system resides, as described in Automating the
     Application of Operating System Service Packs from Updated Source Media

     Applying the service pack to a reference computer, and then capturing an updated
     image from a reference computer, as described in Automating the Application of
     Operating System Service Packs Using a Reference Computer and Windows
     PowerShell

<!-- p.578 -->

Automating the Application of Operating System Service
Packs from Updated Source Media
You can automate the process of updating operating system service packs using
Windows PowerShell when you have source media that include the service pack, such as
having a DVD that has Windows 7 with SP1 already integrated.

For this method, the operating system source media with the service pack is copied over
the existing operating system files without the service pack in the deployment share
using Windows PowerShell.

To automate the application of operating system service packs from updates source
media using Windows PowerShell

   1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
     Windows PowerShell Snap-In.

   2. Ensure that the MDT deployments that share Windows PowerShell drives are
     restored using the Restore-MDTPersistentDrive cmdlet, as shown in the following
     example:

       PowerShell

       Restore-MDTPersistentDrive -Verbose

       ７ Note

       If the MDT deployments that share Windows PowerShell drives are already
       restored, you will receive a warning message indicating that the cmdlet is
       unable to restore the drive.

   3. View the list of MDT deployments share Windows PowerShell drives, one for each
     deployment share, using the Get-PSDrive cmdlet, as shown in the following
     example:

       PowerShell

       Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

     The list of Windows PowerShell drives provided using the MDTProvider are listed,
     one for each deployment share.

<!-- p.579 -->

   4. Remove the folder for the existing operating system from the deployment share
     using the Get-ChildItem and Remove-Item cmdlets, as shown in the following
     example:

       PowerShell

       Get-ChildItem "DS002:\Operating Systems\Windows 7" -recurse | Remove-
       Item -recurse -force

     In this example, DS002: is the name of a Windows PowerShell drive returned in
     step 3.

   5. Copy the contents of the operating system source files that have the service pack
     integrated using the Copy-Item cmdlet, as shown in the following example:

       PowerShell

       Copy-Item "E:\*" -Destination "DS002:\Operating Systems\Windows 7"-
       Recurse -Force

     In this example, the operating system source files are on drive E, and DS002: is the
     name of a Windows PowerShell drive returned in step 3.

   6. Update any MDT deployment media based on deployment share using Update-
     MDTMedia cmdlet.

     For more information about how to update MDT deployment media based on
     deployment share using Update-MDTMedia cmdlet, see Updating Deployment
     Media Using Windows PowerShell.

Automating the Application of Operating System Service
Packs Using a Reference Computer and Windows
PowerShell
You can automate the process of updating operating system service packs using
Windows PowerShell when you have only the service pack that is not yet integrated with
the operating system, such as having SP1 for Windows 7 not yet integrated with a
Windows 7 image.

For this method, deploy the operating system without the service pack to a reference
computer. Then, apply the service pack to the reference computer. Next, capture an
operating system image of the reference computer. Finally, copy the captured .wim file

<!-- p.580 -->

over the Install.wim file in the operating system in the deployment share using Windows
PowerShell.

To automate the application of operating system service packs from updates source
media using Windows PowerShell

   1. Deploy the target operating system to a reference computer.

     For more information on how to deploy a reference computer, see the following
     resources in the MDT document, Using the Microsoft Deployment Toolkit:

          "Preparing for LTI Deployment to the Reference Computer"

          "Deploying To and Capturing an Image of the Reference Computer in LTI"

   2. Install the desired service pack to the reference computer.

     For more information on how to install the service pack, see the documentation
     accompanying the service pack.

   3. Capture an image of the reference computer by creating and deploying a task
     sequence based on the Sysprep and Capture task sequence template.

     For more information about creating a task sequence based on the Sysprep and
     Capture task sequence template, see "Create a New Task Sequence in the
     Deployment Workbench".

   4. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
     Windows PowerShell Snap-In.

   5. Ensure the MDT deployments that share Windows PowerShell drives are restored
     using the Restore-MDTPersistentDrive cmdlet, as shown in the following example:

       PowerShell

        Restore-MDTPersistentDrive -Verbose

       ７ Note

       If the MDT deployments that share Windows PowerShell drives are already
       restored, you will receive a warning message indicating that the cmdlet is
       unable to restore the drive.

<!-- p.581 -->

   6. View the list of MDT deployments share Windows PowerShell drives, one for each
     deployment share, using the Get-PSDrive cmdlet, as shown in the following
     example:

        PowerShell

        Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

     The list of Windows PowerShell drives provided using the MDTProvider are listed,
     one for each deployment share.

   7. Copy the .wim file captured in step 3 over the Install.wim file in the operating
     system in the deployment share using the Copy-Item cmdlet, as shown in the
     following example:

        PowerShell

        Copy-Item "DS002:\Captures\Win7SP1.wim" -Destination "DS002:\Operating
        Systems\Windows 7\sources\Install.wim" Force

     In this example, the captured operating system image file (Win7SP1.wim) in the
     Captures folder in the share DS002: is the name of a Windows PowerShell drive
     returned in step 6, and the existing Windows 7 operating system is stored in folder
     named Windows 7.

   8. Update any MDT deployment media based on deployment share using Update-
     MDTMedia cmdlet.

     For more information about how to update MDT deployment media based on
     deployment share using Update-MDTMedia cmdlet, see Updating Deployment
     Media Using Windows PowerShell.

Customizing Deployment Based on Chassis
Type
You can customize the deployment based on the chassis type of the computer. The
scripts create local variables that can be processed in the CustomSettings.ini file. The
local variables IsLaptop , IsDesktop , and IsServer indicate whether the computer is a
portable computer, desktop computer, or server, respectively.

  ７ Note

<!-- p.582 -->

  In earlier versions of the Deployment Workbench, the IsServer flag indicated that
  the existing operating system is a server operating system (such as Windows Server
  2003 Enterprise Edition). This flag has been renamed to IsServerOS .

To implement local variables in the CustomSettings.ini file

   1. In the [Settings] section, on the Priority line, add a custom section to customize
        deployment based on the chassis type ( ByChassisType in the following example,
        where Chassis represents the type of computer).

   2. Create the custom section that corresponds to the custom section defined in step
        1 ( ByChassisType in the example in following example, where Chassis represents
        the type of computer).

   3. Define a subsection for each chassis type to detect ( Subsection=Laptop-%IsLaptop%,
        Subsection=Desktop-%IsDesktop%, Subsection=Server-%IsServer% in the following

        example).

   4. Create a subsection for each True and False state of each subsection defined in
        step 3 (such as [Laptop-True], [Laptop-False], [Desktop-True], [Desktop-False]
        in the following example).

   5. Under each True and False subsection, add the appropriate settings based on the
        chassis type.

        Listing 1. Example of Customizing Deployment Based on Chassis Type in the
        CustomSettings.ini File

  ini

  [Settings]

  Priority=...,ByLaptopType,ByDesktopType,ByServerType

  [ByLaptopType]
  Subsection=Laptop-%IsLaptop%

  [ByDesktopType]
  Subsection=Desktop-%IsDesktop%

  [ByServerType]
  Subsection=Server-%IsServer%
  .
  .
  .

  [Laptop-True]

<!-- p.583 -->

  .
  .
  .

  [Laptop-False]
  .
  .
  .

  [Desktop-True]
  .
  .
  .

  [Desktop-False]
  .
  .
  .

  [Server-True]
  .
  .
  .

  [Server-False]
  .
  .
  .

Deploying Applications Based on Earlier
Application Versions
Often, when installing an operating system on an existing computer, you will install the
same applications you previously installed on the computer. Do this using MDT scripts
(in particular, ZTIGather.wsf) to query two separate sources of information:

      Configuration Manager software inventory feature. Contains one record for each
      application package—in this case, listings in Program and Features in Windows 8.1,
      Windows 8, Windows 7, Windows Server 2012 R2, Windows Server 2012, Windows
      Server 2008 R2—installed the last time Configuration Manager inventoried the
      computer.

      A mapping table. Describes which package and program need to be installed for
      each record (because the Program and Features or Add or Remove Programs
      records do not specify exactly which package installed the application, making it
      impossible to automatically select the package based on inventory alone).

<!-- p.584 -->

  To perform a dynamic computer-specific application installation

1. Use the table in the MDT DB to connect specific packages with applications listed
  in the target operating system.

2. Populate the table with data that associates the appropriate package with the
  application listed in Program and Features or Add or Remove Programs.

  SQL Query to Populate the Table

    SQL

    use [MDTDB]
    go
    INSERT INTO [PackageMapping] (ARPName, Packages) VALUES('Office12.0',
    'XXX0000F:Install Office 2010 Professional Plus')
    go

  The inserted row connects any computer that has the entry Office12.0 with the
  Microsoft Office 2010 Professional Plus package.

  This means that Microsoft Office 2010 Professional Plus will be installed on any
  computer currently running the 2007 Microsoft Office system (Office 12.0). Add
  similar entries for any other packages. Any item for which there is no entry is
  ignored (no package will be installed).

3. Create a stored procedure to simplify joining the information in the new table with
  the inventory data.

    SQL

    use [MDTDB]
    go

    if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].
    [RetrievePackages]') and OBJECTPROPERTY(id, N'IsProcedure') = 1)
    drop procedure [dbo].[RetrievePackages]
    go

    CREATE PROCEDURE [dbo].[RetrievePackages]
    @MacAddress CHAR(17)
    AS

    SET NOCOUNT ON

    /* Select and return all the appropriate records based on current
    inventory */
    SELECT * FROM PackageMapping
    WHERE ARPName IN

<!-- p.585 -->

     (
        SELECT ProdID0 FROM CM_DB.dbo.v_GS_ADD_REMOVE_PROGRAMS a,
     CM_DB.dbo.v_GS_NETWORK_ADAPTER n
        WHERE a.ResourceID = n.ResourceID AND
        MACAddress0 = @MacAddress
     )
     go

  The stored procedure in the preceding example assumes that the Configuration
  Manager central primary site database resides on the computer on which SQL
  Server is running as the MDT DB. If the central primary site database resides on a
  different computer, the appropriate modifications need to be made to the stored
  procedure. In addition, the name of the database ( CM_DB ) must be updated. Also
  consider granting additional accounts Read access to the
  v_GS_ADD_REMOVE_PROGRAMS view in the Configuration Manager database.

4. Configure the CustomSettings.ini file to query this database table by specifying the
  name of a section ( [DynamicPackages] in the Priority list) that points to the
  database information.

    ini

     [Settings]
     ...
     Priority=MacAddress, DefaultGateway, DynamicPackages, Default
     ...

5. Create a [DynamicPackages] section to specify the name of a database section.

    ini

     [DynamicPackages]
     SQLDefault=DB_DynamicPackages

6. Create a database section to specify the database information and query details.

    ini

     [DB_DynamicPackages]
     SQLServer=SERVER1
     Database=MDTDB
     StoredProcedure=RetrievePackages
     Parameters=MacAddress
     SQLShare=Logs
     Instance=SQLEnterprise2005

<!-- p.586 -->

        Port=1433
        Netlib=DBNMPNTW

     In the preceding example, the MDT DB named MDTDB on the computer running
     the SQL Server instanced named SERVER1 will be queried. The database contains a
     stored procedure named RetrievePackages (created in step 3).

     When ZTIGather.wsf runs, a Structured Query Language (SQL) SELECT statement is
     automatically generated, and the value of the MakeModelQuery custom key is
     passed as a parameter to the query:

       SQL

        EXECUTE RetrievePackages ?

     The actual value of the MACAddress custom key will be substituted for the
     corresponding "?". This query returns a record set with the rows entered in step 2.

     A variable number of arguments cannot be passed to a stored procedure. As a
     result, when a computer has more than one MAC address, not all MAC addresses
     can be passed to the stored procedure. As an alternative, replace the stored
     procedure with a view that allows querying the view with a SELECT statement with
     an IN clause to pass all the MAC address values.

     Based on the scenario presented here, if the current computer has the value
     Office12.0 inserted into the table (step 2), the one row is returned

     ( XXX0000F:Install Office 2010 Professional Plus ). This indicates that package
     XXX0000F:Install Office 2001 Professional Plus will be installed by the ZTI process
     during the State Restore Phase.

Fully Automated LTI Deployment Scenario
The main purpose of LTI is to automate the deployment process as much as possible.
Although ZTI provides full deployment automation using the MDT scripts and Windows
Deployment Services, LTI is designed to work with fewer infrastructure requirements.

You can automate the Windows Deployment Wizard used in the LTI deployment process
to reduce (or eliminate) the wizard pages displayed. You can skip the entire Windows
Deployment Wizard by specifying the SkipWizard property in CustomSettings.ini. To
skip individual wizard pages, use the following properties:

     SkipAdminPassword

<!-- p.587 -->

     SkipApplications

     SkipBDDWelcome

     SkipBitLocker

     SkipBitLockerDetails

     SkipTaskSequence

     SkipCapture

     SkipComputerBackup

     SkipComputerName

     SkipDomainMembership

     SkipFinalSummary

     SkipLocaleSelection

     SkipPackageDisplay

     SkipProductKey

     SkipSummary

     SkipTimeZone

     SkipUserData

For more information about these individual properties, see the corresponding property
in the MDT document Toolkit Reference.

For each wizard page skipped, provide the values for the corresponding properties that
are typically collected through the wizard page in the CustomSettings.ini and
BootStrap.ini files. For more information about the properties that must be configured in
these files, see the section, "Providing Properties for Skipped Deployment Wizard
Pages", in the MDT document Toolkit Reference.

Fully Automated LTI Deployment for a Refresh
Computer Scenario
The following illustrates a CustomSettings.ini file used for a Refresh Computer scenario
to skip all Windows Deployment Wizard pages. In this sample, the properties to provide

<!-- p.588 -->

when skipping the wizard page are immediately beneath the property that skips the
wizard page.

  ini

  [Settings]
  Priority=Default
  Properties=MyCustomProperty

  [Default]
  OSInstall=Y
  ScanStateArgs=/v:5 /o /c
  LoadStateArgs=/v:5 /c /lac /lae
  SkipCapture=YES
  SkipAdminPassword=YES
  SkipProductKey=YES

  DeploymentType=REFRESH

  SkipDomainMembership=YES
  JoinDomain=DomainName
  DomainAdmin=Administrator
  DomainAdminDomain=DomainName
  DomainAdminPassword=a_secure_password

  SkipUserData=yes
  UserDataLocation=AUTO
  UDShare=\\Servername\Sharename\Directory
  UDDir=%ComputerName%

  SkipComputerBackup=YES
  ComputerBackuplocation=AUTO
  BackupShare=\\Servername\Backupsharename
  BackupDir=%ComputerName%

  SkipTaskSequence=YES
  TaskSequenceID=Enterprise

  SkipComputerName=YES
  OSDComputerName=%ComputerName%

  SkipPackageDisplay=YES
  LanguagePacks001={3af4e3ce-8122-41a2-9cf9-892145521660}
  LanguagePacks002={84fc70d4-db4b-40dc-a660-d546a50bf226}

  SkipLocaleSelection=YES
  UILanguage=en-US
  UserLocale=en-CA
  KeyboardLocale=0409:00000409

  SkipTimeZone=YES
  TimeZoneName=China Standard Time

  SkipApplications=YES

<!-- p.589 -->

  Applications001={a26c6358-8db9-4615-90ff-d4511dc2feff}
  Applications002={7e9d10a0-42ef-4a0a-9ee2-90eb2f4e4b98}
  UserID=Administrator
  UserDomain=DomainName
  UserPassword=P@ssw0rd

  SkipBitLocker=YES
  SkipSummary=YES
  Powerusers001=DomainName\Username

Fully Automated LTI Deployment for a New
Computer Scenario
The following is an example of a CustomSettings.ini file used for a New Computer
scenario to skip all Windows Deployment Wizard pages. In this sample, the properties to
provide when skipping the wizard page are immediately beneath the property that skips
the wizard page.

  ini

  [Settings]
  Priority=Default
  Properties=MyCustomProperty

  [Default]
  OSInstall=Y
  ScanStateArgs=/v:5 /o /c
  LoadStateArgs=/v:5 /c /lac /lae

  SkipCapture=YES
  ComputerBackupLocation=\\WDG-MDT-01\Backup$\
  BackupFile=MyCustomImage.wim

  SkipAdminPassword=YES
  SkipProductKey=YES

  SkipDomainMembership=YES
  JoinDomain=WOODGROVEBANK
  DomainAdmin=Administrator
  DomainAdminDomain=WOODGROVEBANK
  DomainAdminPassword=P@ssw0rd

  SkipUserData=Yes
  UserDataLocation=\\WDG-MDT-01\UserData$\Directory\usmtdata

  SkipTaskSequence=YES
  TaskSequenceID=Enterprise

  SkipComputerName=YES
  OSDComputerName=%SerialNumber%

<!-- p.590 -->

  SkipPackageDisplay=YES
  LanguagePacks001={3af4e3ce-8122-41a2-9cf9-892145521660}
  LanguagePacks002={84fc70d4-db4b-40dc-a660-d546a50bf226}

  SkipLocaleSelection=YES
  UILanguage=en-US
  UserLocale=en-CA
  KeyboardLocale=0409:00000409

  SkipTimeZone=YES
  TimeZoneName=China Standard Time

  SkipApplications=YES
  Applications001={a26c6358-8db9-4615-90ff-d4511dc2feff}
  Applications002={7e9d10a0-42ef-4a0a-9ee2-90eb2f4e4b98}

  SkipBitLocker=YES
  SkipSummary=YES
  Powerusers001=WOODGROVEBANK\PilarA
  CaptureGroups=YES
  SLShare=\\WDG-MDT-01\UserData$\Logs
  Home_page=https://www.microsoft.com/NewComputer

Calling Web Services in MDT
In earlier versions of MDT, rules processing was supported through CustomSettings.ini
and databases, from which you could retrieve values from the local computer—typically
using WMI—to make decisions on what needed to be done on each computer during
deployment. In addition, you could make SQL queries and stored procedure calls to
retrieve additional information from external databases. There were challenges with that
approach, though—especially with making secure SQL Server connections.

To help with this problem, MDT has the ability to make web service calls based on
simple rules defined in CustomSettings.ini. These web service requests do not require
any special security context and can use whatever TCP/IP port is needed to simplify
firewall configurations.

The following shows how to configure CustomSettings.ini to call a particular web
service. In this scenario, the web service is chosen at random from an Internet search. It
takes a postal code as input and returns the city, state, area code, and time zone (as a
letter) for the specified postal code.

  ini

  [Settings]
  Priority=Default, USZipService

<!-- p.591 -->

  Properties=USZip, City, State, Zip, Area_Code, Time_Zones
  [Default]
  USZip=98052
  [USZipService]
  WebService=http://www.webservicex.net/uszip.asmx/GetInfoByZIP
  Parameters=USZip

Executing this code produces output similar to the following:

  Output

  Added new custom property USZIP
  Added new custom property CITY
  Added new custom property STATE
  Added new custom property ZIP
  Added new custom property AREA_CODE
  Added new custom property TIME_ZONES
  Using from [Settings]: Rule Priority = DEFAULT, USZIPSERVICE
  ------ Processing the [DEFAULT] section ------
  Property USZIP is now = 98052
  Using from [DEFAULT]: USZIP = 98052
  ------ Processing the [USZIPSERVICE] section ------
  Using COMMAND LINE ARG: Ini file = CustomSettings.ini
  CHECKING the [USZIPSERVICE] section
  About to execute web service call to
  http://www.webservicex.net/uszip.asmx/GetInfoByZIP: USZip=98052
  Response from web service: 200 OK
  Successfully executed the web service.
  Property CITY is now = Redmond
  Obtained CITY value from web service: CITY = Redmond
  Property STATE is now = WA
  Obtained STATE value from web service: STATE = WA
  Property ZIP is now = 98052
  Obtained ZIP value from web service: ZIP = 98052
  Property AREA_CODE is now = 425
  Obtained AREA_CODE value from web service: AREA_CODE = 425
  ------ Done processing CustomSettings.ini ------

There are a few minor complications to watch for when running a web service:

     Do not do anything special with proxy servers. If there is an anonymous proxy
     present, use it, but authenticating proxies could cause problems. In most cases, a
     web service will not be called.

     CustomSettings.ini or ZTIGather.xml searches for properties defined in the XML
     markup returned as a result of the web service call (just as with a database query
     or other rule). However, the XML search is case sensitive. Fortunately, the web
     service described here returns all uppercase property names, which is what

<!-- p.592 -->

     ZTIGather.xml expects. It is possible to remap lowercase or mixed-case entries to
     get around this.

     A POST request to the web service is recommended, so the web service call must
     be able to support a POST .

Connecting to Network Resources
During LTI and ZTI deployment processes, you might require access to a network
resource on a server different from the server hosting the deployment share. You must
be authenticated on the other server so that you can access shared folders or services
there. For example, you can install an application from a shared folder on a server other
than the server hosting the deployment share that the MDT scripts use.

  ７ Note

  To query SQL Server databases hosted on a server other than the server hosting the
  deployment share, see the Database, DBID, DBPwd, Instance, NetLib, Order,
  Parameters, ParameterCondition, SQLServer, SQLShare, and Table properties in
  the MDT document Toolkit Reference.

Using the ZTIConnect.wsf script, you can connect to other servers and access resources
on them. The syntax for the ZTIConnect.wsf script is as follows (where unc_path is a
Universal Naming Convention [UNC] path to connect to the server):

  Windows Command Prompt

  cscript.exe "%SCRIPTROOT%\ZTIConnect.wsf" /uncpath:unc_path

In most instances, you run the ZTIConnect.wsf script as a Task Sequencer task. Run the
ZTIConnect.wsf script prior to tasks requiring access to a server other than the server
hosting the deployment share.

To add the ZTIConnect.wsf script as a task to the task sequence of a build

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share to configure).

<!-- p.593 -->

3. In the details pane, select task_sequence (where task_sequence is the task sequence
  to modify).

4. In the Actions pane, select Properties.

5. Select the Task Sequence tab, browse to group (where group is the group in which
  to run the ZTIConnec.wsf script), and select Add. Select General, and then select
  Run Command Line.

    ７ Note

    Add the task before adding any tasks that require access to resources on the
    target server.

6. Complete the Properties tab of the new task using the following information:

                                                                            ﾉ    Expand table

   In this box   Do this

   Name          Type Connect to server (where server is the name of the server to which to
                 connect).

   Description   Type text that explains why the connection needs to be made.

   Command       Type cscript.exe "%SCRIPTROOT%\ZTIConnect.wsf" /uncpath:unc_path
                 (where unc_path is the UNC path to a shared folder on the server).

7. Complete the Options tab of the new task using the following information. Unless
  specified, accept default values, and then select OK.

                                                                            ﾉ    Expand table

   In this box        Do this

   Success codes      Type 0 3010. (The ZTIConnect.wsf script returns these codes upon
                      successful completion.)

   Conditions list    Add any conditions that might be necessary. (In most instances this task
   box                requires no conditions.)

  After adding the task that will run the ZTIConnect.wsf script, subsequent tasks can
  access network resources on the server specified in the /uncpath option of the
  ZTIConnect.wsf script.

<!-- p.594 -->

Deploying the Correct Device Drivers to
Computers with the Same Hardware Devices
but Different Make and Model
Variations on model numbers and names can exist with virtually no difference in the
driver set. These variations in model numbers and names can unnecessarily increase
time spent making multiple database entries for a given model. The following procedure
shows how to define a new property using a user exit function call that returns a
substring of the model number.

To create model aliases

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

   3. In the Actions pane, select Properties.

   4. In the Properties dialog box, select the Rules tab.

   5. Create aliases for hardware types in the Make and Model sections of the MDT DB.
     Truncate the model type at the open parentheses "(" in the model name. For
     example, HP DL360 (G112) becomes HP DL360.

   6. Add the custom variable ModelAlias to each section.

   7. Create a new [SetModel] section.

   8. Add the [SetModel] section to the Priority settings in the [Settings] section.

   9. Add a line to the ModelAlias section to refer to a user exit script that will truncate
     the model name at the "(".

 10. Create an MMApplications database lookup where ModelAlias is equal to Model.

 11. Create a user exit script and place it in the same directory as the
     CustomSettings.ini file to truncate the model name.

     The following shows a CustomSettings.ini and the user exit script, respectively.

     CustomSettings.ini:

<!-- p.595 -->

       ini

       [Settings]
       Priority=SetModel, MMApplications, Default
       Properties= ModelAlias
       [SetModel]
       ModelAlias=#SetModelAlias()#
       Userexit=Userexit.vbs
       [MMApplications]
       SQLServer=Server1
       Database=MDTDB
       Netlib=DBNMPNTW
       SQLShare=logs
       Table= MakeModelSettings
       Parameters=Make, ModelAlias
       ModelAlias=Model
       Order=Sequence

     User Exit Script:

       vbs

       Function UserExit(sType, sWhen, sDetail, bSkip)
         UserExit = Success
       End Function

       Function SetModelAlias()
         If Instr(oEnvironment.Item("Model"), "(") <> 0 Then
           SetModelAlias = Left(oEnvironment.Item("Model"), _
                             Instr(oEnvironment.Item("Model"), _
                                "(") - 1)
           oLogging.CreateEntry "USEREXIT - " & _
             "ModelAlias has been set to " & SetModelAlias, _
             LogTypeInfo
         Else
           SetModelAlias = oEnvironment.Item("Model")
           oLogging.CreateEntry " USEREXIT - " & _
             "ModelAlias has not been changed.", LogTypeInfo
         End if
       End Function

Configuring Conditional Task Sequence Steps
In some scenarios, consider running a task sequence step conditionally based on
defined criteria. Any combinations of these conditions can be added to determine
whether the task sequence step should run. For example, use the value of a task
sequence variable and the value of a registry setting to determine whether a task
sequence step should run.

<!-- p.596 -->

Using MDT, run a task sequence conditionally based on:

     One or more IF statements

     A task sequence variable

     The version of the target operating system

     The Boolean results of a WMI query

     A registry setting

     The software installed on the target computer

     The properties of a folder

     The properties of a file

Configuring a Conditional Task Sequence Step
Conditional task sequence steps are configured in the Deployment Workbench, on the
Options tab of a task sequence step. You can add one or more conditions to the task
sequence step to create the appropriate condition for running or not running the step.

  ７ Note

  Every conditional task sequence step needs at least one IF statement.

To view the Options tab of a task sequence step

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share to configure).

   3. In the details pane, select task_sequence (where task_sequence is the name of the
     task sequence to configure).

   4. In the Actions pane, select Properties.

   5. In the task_sequence Properties dialog box, on the Task Sequence tab, select step
     (where step is the name of the task sequence step to configure), and then select
     the Options tab.

<!-- p.597 -->

     On the Options tab of the task sequence step, perform the following actions:

     Add. Select this button to add a condition to the task sequence step.

     Remove. Select this button to remove an existing condition in a task sequence
     step.

     Edit. Select this button to modify an existing condition in a task sequence step.

IF Statements in Conditions
All task sequence conditions include one or more IF statements. IF statements are the
foundation for creating conditional task sequence steps. A task sequence step condition
can include only one IF statement, but multiple IF statements can be nested beneath the
top-level IF statement to create more complex conditions.

An IF statement can be based on the conditions listed in the following table, which are
configured in the IF Statement Properties dialog box.

                                                                                ﾉ   Expand table

 Condition            Select this option to run the task sequence if

 All conditions       All the conditions beneath this IF statement must be true.

 Any conditions       Any the conditions beneath this IF statement are true.

 None                 None the conditions beneath this IF statement are true.

Complete the condition for running the task sequence step by adding other criteria to
the conditions (for example, task sequence variables or values in a registry setting).

To add an IF statement condition to a task sequence step

   1. On the step Option tab (where step is the name of the task sequence step to
     configure), select Add, and then select If statement.

   2. In the If Statement Properties dialog box, select condition (where condition is one
     of the conditions listed in the previous table), and then select OK.

Task Sequence Variables in Conditions
Use the Task Sequence Variable condition to evaluate any task sequence variable
created by a Set Task Sequence Variable task or by any task in the task sequence. For
example, consider a network that contains Windows XP client computers that are part of

<!-- p.598 -->

a domain and some that are in a workgroup. Knowing that the current domain policy
forces all user settings to be saved on the network, user settings may need to be saved
only for computers that are not part of the domain—that is, computers that are in the
workgroup. In such case, add a condition to the Capture User Files and Settings task
that targets the computers in the workgroup.

To add a condition based on a task sequence variable

   1. On the step Options tab (where step is the name of the task sequence step to
     configure), select Add Condition, and then select Task Sequence Variable.

   2. In the Task Sequence Variable Condition dialog box, in the Variable box, type
     OSDJoinType.

        ７ Note

        This variable is set to 0 for computers that are joined to a domain and to 1 for
        those in a workgroup.

   3. In the Condition box, select equal.

   4. In the Value box, type 1, and then select OK.

Operating System Version in Conditions
Use the Operating System Version condition to verify the existing operating system
version of a target computer or the existing client (when capturing an image). For
instance, consider a network that contains several servers that will be upgraded from
Windows Server 2003 to Windows Server 2008. Network settings should be copied and
applied only to servers that are running Windows Server 2003. All other servers will have
the default network settings that Windows Server 2008 uses.

To add a condition based on operating system version

   1. In the Task Sequence Editor, select the Capture Network Settings task.

   2. Select Add Condition, and then select Operating System Version.

   3. In the Architecture box, select the relevant server. For this example, select x86.

   4. In the Operating system box, select the operating system and version for which to
     set a condition. For this example, select x86 Windows 2003.

   5. In the Condition box, select the relevant condition, and then select OK.

<!-- p.599 -->

File Properties in Conditions
Use the File Properties condition to verify the version and/or times tamp of a given file
to determine whether or not to run a task or a group of tasks. In this example, the
production environment contains a Windows Server 2003 image that is constantly
updated and used for every new server that is added to the network. All server
computers in the environment run a custom application that requires the Digital Access
Object (DAO) application programming interface (API) version 3.60.6815.

All existing servers are working properly. However, each new server added to the
network with the image is unable to run the application. Because it is the responsibility
of a different group to maintain and update images, you decide that the deployment
task sequence be changed to install the relevant version of DAO if the existing version of
DAO deployed with the image is incorrect.

To add a File Properties condition to a task sequence step in Configuration Manager

   1. In Configuration Manager, create a package to install DAO 3.60.6815. Call this
     package DAO, with a program called InstallDAO. To learn more about creating
     packages, see How to create a package.

   2. Create an Install Software step to deploy the DAO package.

   3. Select the Install Software task sequence step created in step 2, and then select
     the Options tab.

   4. Select Add Condition, and then select File Properties.

   5. In the Path box, type C:\Program Files\Microsoft Shared\DAO\dao360.dll.

   6. Select the Check the version check box, and then select not equals for the
     condition.

   7. In the Version box, type 3.60.6815.

   8. In this case, clear the Check the timestamp check box, and then select OK.

Folder Properties in Conditions
Use the Folder Properties condition to verify the time stamp of a given folder to
determine whether to run a task or a group of tasks. For instance, consider a situation in
which an internally developed application has been updated to work with Windows 8.
However, not all of the computers in the network have the most recent version of the

<!-- p.600 -->

application installed, and you must perform a data-conversion process before you can
upgrade the application.

If the time stamp of the folder in which the application is installed is 12/31/2007 or
earlier, then the target computer is running the incompatible version of the application,
and you should run the data-conversion process on the target computer. Conditionally,
run a task sequence step to run the data-conversion process on computers that have an
earlier version of the application.

To add a Folder Properties condition to a task sequence step

   1. In the Configuration Manager console or in the Deployment Workbench, in the
     task sequence editor, edit task_sequence (where task sequence is the task sequence
     you want to edit).

   2. Create a Command Line task to perform the data-conversion process.

   3. Select the task created in step 1.

   4. Select Add Condition, and then select Folder Properties.

   5. In the Path box, type the path of the folder that contains the application.

   6. Select the Check the timestamp check box.

   7. Select Less than or equals for the condition.

   8. In the Date box, select 12/31/2007.

   9. In the Time box, select 12:00:00 AM, and then select OK.

Registry Settings in Conditions
Use the Registry Setting condition to verify the existence of keys and values in the
registry and the corresponding data stored in registry values. For instance, consider a
case in which an application currently used on a small set of computers cannot run on
Windows 8, and a Windows 8 deployment is in place to upgrade computers that
currently are running Windows XP. Create a condition on the very first task in a
sequence to check the registry for an entry for the incompatible application and to
interrupt the deployment process for that computer if it is found.

To add a Registry Setting condition to a task sequence step

   1. In the Configuration Manager console or in the Deployment Workbench, in the
     task sequence editor, edit task_sequence (where task sequence is the task sequence
