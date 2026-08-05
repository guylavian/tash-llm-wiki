---
title: "Install prerequisites for SharePoint Server from a network share - SharePoint Server"
type: reference
domain: sharepoint
slug: install-install-prerequisites-from-network-share
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/install/install-prerequisites-from-network-share
family: install
documentKind: "install-set-up-deploy"
abstract: "Learn how to how to install the SharePoint Server prerequisites from an offline shared network location by using the prerequisite installer (PrerequisiteInstaller.exe) tool."
---

# Install prerequisites for SharePoint Server from a network share - SharePoint Server

Note

Install prerequisites for SharePoint Server from a network share

# Install prerequisites for SharePoint Server from a network share

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Installing prerequisites from an offline location is typically required when the servers on which you want to install SharePoint Server are isolated from the Internet. Even if this is not the case, by installing prerequisites from a central, offline location, you can ensure farm server consistency by installing a well-known and controlled set of images.

Note

The Microsoft SharePoint Products Preparation Tool is a user interface built on PrerequisiteInstaller.exe. The Microsoft SharePoint Products Preparation Tool accepts no user input.

Installer switches and arguments

## Installer switches and arguments

By using PrerequisiteInstaller.exe with switches and arguments, you control the versions of the required software that are installed and the location from which they are installed.

PrequisiteInstaller.exe accepts single or multiple switch and argument pairs. A switch identifies the prerequisite and the argument specifies the action and the location of the prerequisite.

A switch and argument pair uses the following format:

*/switch*:  *<path>*

Where:

**/** *switch* is a valid switch to identify a prerequisite. For example, **/SQLNCli:** is the switch for the Microsoft SQL Server 2012 SP1 Native Client.

*<path>* is expressed as the path of a local file or the path of a file share, for example, "C:\foldername\sqlncli.msi" or "\<servername>\<sharename>\sqlncli.msi".

Each switch and its argument are separated by a colon and a space. The argument is enclosed in quotation marks.

The switch and argument pairs can be passed to PrerequisiteInstaller.exe at the command prompt or read from an arguments text file.

Download and combine the SharePoint Server prerequisites on a file share

## Download and combine the SharePoint Server prerequisites on a file share

You can download and combine prerequisites by performing the steps in the following procedures.

**To identify prerequisites**

Refer to the article, Hardware and software requirements for SharePoint Server 2016, which lists all the required and optional software for SharePoint Server 2016. Additionally, this article provides the download location for each prerequisite that can be downloaded from the Internet. For hardware and software requirements for SharePoint Server 2019, see Hardware and software requirements for SharePoint Server 2019

For the SharePoint 2013 version, see Hardware and software requirements for SharePoint 2013.

From the command prompt, navigate to the root of the SharePoint Server installation media or folder location.

At the command prompt, type the following command, and then press Enter:

PrerequisiteInstaller.exe /?

This displays a list of the command-line options and switches and their corresponding arguments for installing a prerequisite from the command-line.

Tip

To copy the contents of the active About window to the Clipboard, press Ctrl+C.

Verify that you have an accurate list of the required software. Compare the output from the prerequisite installer to the list of prerequisites in step 1.

Download the prerequisites to a computer that has Internet access.

Next, follow these steps to create a central location that you can use for installing SharePoint Server prerequisites on all the farm servers.

**To combine prerequisites**

Create a shared folder on a computer that can be accessed by the servers on which the prerequisites will be installed.

Copy the files that you downloaded from the Internet to the shared folder.

After you finish creating an available network location for the prerequisites, use the procedure in the following section to install SharePoint Server prerequisites on a server.

Install the SharePoint Server prerequisites at the command prompt

## Install the SharePoint Server prerequisites at the command prompt

You can install one or more of the prerequisites from the command line using the following procedure.

**To install from the command line**

From the **Start** menu, open the Command Prompt window using **the Run as administrator** option.

Navigate to the SharePoint Server source directory.

Type the prerequisite program switch and corresponding argument for the program that you want to install, and then press Enter, for SharePoint Server 2016, type:

PrerequisiteInstaller.exe /SQLNCli:"\o16-sf-admin\SP_prereqs\sqlncli.msi"

Note

To install more than one prerequisite, type each switch and argument pair. Be sure to separate each pair by a space, for example: > PrerequisiteInstaller.exe /IDFX:"\< *path*>\Windows6.1-KB974405-x64.msu" /sqlncli:"\< *path*>\sqlncli.msi" /Sync:"\< *path*>\Synchronization.msi"

Install the SharePoint Server prerequisites by using an arguments file

## Install the SharePoint Server prerequisites by using an arguments file

You can install the prerequisites from the file share using an arguments file that consists of switches and corresponding path statements to the programs that have to be installed.

When you run PrerequisiteInstaller.exe with an arguments file, the following happens:

PrerequisiteInstaller.exe reads the argument file to verify that each switch is valid and that the program identified in the path statement exists.

Note

If you specify an argument, PrerequisiteInstaller.exe ignores the arguments file and processes only the command-line argument.

PrerequisiteInstaller.exe scans the local system to determine whether any of the prerequisites are already installed.

PrerequisiteInstaller.exe installs the programs in the argument file and returns one of the following exit codes:

0 - Success

1 - Another instance of this application is already running

2 - Invalid command line parameter

1001 - A pending restart blocks installation

3010 - A restart is needed

- If a prerequisite requires a restart, a 3010 code is generated and you are prompted to click **Finish** to restart the system. The behavior of the installer after a 3010 code varies depending on which of the following conditions are true on the computer:

If the component that requires a restart is already installed on the system, the 3010 code is generated, and the remaining prerequisites are installed. After the last prerequisite is installed, you are prompted to restart the system.

If the component that requires a restart is installed on the system by PrerequisiteInstaller.exe, the installer generates the 3010 code, and the installation of the remaining prerequisites is skipped. You are prompted to restart the system.

After the system restarts, PrerequisiteInstaller.exe starts to run again because the startup file that is created before the restart contains a /continue flag.

Multiple components might require you to restart. So PrerequisiteInstaller.exe might have to be restarted several times. After you restart, PrerequisiteInstaller.exe ignores the arguments file and attempts to download and install the remaining prerequisites from the Internet. For more information, see Known issues.

Use the following procedure to create an arguments file.

**To create an arguments file**

Using a text editor, create a new text document named PrerequisiteInstaller.Arguments.txt. Save this file to the same location as PrerequisiteInstaller.exe. This file will contain the switches and arguments that are used when you run the Microsoft SharePoint Products Preparation Tool.

Using a text editor, edit PrerequisiteInstaller.Arguments.txt and provide file paths to the installation source for each prerequisite switch by using the following syntax:

*/switch*: *<path>*

Where  */switch* is a valid switch and  *<path>* is a path of the installation source.

After you finish editing PrerequisiteInstaller.Arguments.txt, save your edits, and verify that this file is in the same directory as PrerequisiteInstaller.exe.

Use the following procedure to install the prerequisites.

**To install the prerequisites using an arguments file**

Run PrerequisiteInstaller.exe at the command prompt to install the prerequisites.

Caution

If you are prompted to click **Finish** to restart the system, do not do so. Instead, click **Cancel**. For more information, see Known issues before you continue with the next step.

Manually restart the system.

At the command prompt, type the following command, and then press Enter:

PrerequisiteInstaller.exe

Known issues

### Known issues

There are two known issues that affect the use of an arguments file:

Using line breaks in the arguments file

If you create an arguments file and use line breaks to put each switch and argument on a separate line, the prerequisite installer fails. The workaround is to enter all the switch and argument pairs on a single line.

After a computer restart, the arguments file is not used

After you restart, PrerequisiteInstaller.exe runs the startup command file, which contains a /continue flag. The /continue flag forces the installer to ignore the arguments file.

You must prevent a restart by deleting the startup task in this command file by using one of the following options:

**Option 1**

Run PrerequisiteInstaller.exe by double-clicking it. The program will display the first screen with the list of prerequisites.

Click **Cancel**. PrerequisiteInstaller.exe deletes the startup task.

**Option 2**

From the **Start** menu, choose **Run**, and then type regedit to open the registry.

Open the key HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders.

Check the value for "Common Startup". This shows the directory where the startup tasks are listed.

Close the registry editor without making any changes.

Navigate to the startup directory, which is usually <systemdir>\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup.

Delete the startup task by deleting "SharePointServerPreparationToolStartup_0FF1CE14-0000-0000-0000-000000000000.cmd".

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
