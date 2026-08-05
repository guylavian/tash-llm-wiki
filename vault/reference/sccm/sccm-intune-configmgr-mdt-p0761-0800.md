---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 761-800"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0761-0800
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0761-0800
family: sccm
documentKind: "doc"
abstract: "On this Do this wizard page iii. On the Select Resources page, select WDG-CLI-01, and then select Next. Note: The process for adding the target computer (WDG-CLI- 01) to All Systems can take a few minutes to complete. If WDG-CLI- 01 does not appear in the list, repeat steps b an"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 761-800

<!-- p.761 -->

      On this        Do this
      wizard page

                         iii. On the Select Resources page, select WDG-CLI-01, and then select
                              Next. Note: The process for adding the target computer (WDG-CLI-
                              01) to All Systems can take a few minutes to complete. If WDG-CLI-
                              01 does not appear in the list, repeat steps b and c until WDGCLI01
                              appears.
                         iv. On the Summary page, select Next.
                          v. On the Completion page, select Close.
                      c. Select Next.

      Summary        1. Review the information in the Details box that you provided while
                     completing the previous wizard pages.
                     2. Select Next.

      Progress       The progress for creating the device collection is displayed.

      Completion     Select Close.

     For more information, see the section, "How to Create Collections in Configuration
     Manager," in the Configuration manager Documentation Library, which is installed
     with Configuration Manager.

Step 6-3: Deploy the Target Computer Task Sequence
In the Configuration Manager console, deploy the task sequence created earlier in the
process for the target computers. Deploy the task sequence to the collection of target
computers created earlier in the process.

To deploy the task sequence
   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Task
     Sequences.

   4. In the preview pane, select Windows 8.1 Target Deployment.

   5. On the Ribbon, on the Home tab, in the Deployment group, select Deploy.

<!-- p.762 -->

   The Deploy Software Wizard starts.

 6. Complete the Deploy Software Wizard using the following information. Accept the
   default values unless otherwise specified.

                                                                           ﾉ   Expand table

    On this wizard page         Do this

    General                     1. In Collection, select Browse.
                                2. In the Browse Collection dialog box, select Microsoft
                                Deployment - Batch 01, and then select OK.
                                3. In Comment, type Deploy Windows 8.1 to the first batch
                                of target computers.
                                4. Select Next.

    Deployment Settings         1. In Purpose, select Available.
                                2. Select the Make available to boot media and PXE check
                                box.
                                3. Select Next.

    Deployment Settings:        Select Next.
    Schedule

    Deployment Settings: User   Select Next.
    Experience

    Deployment Settings:        Select Next.
    Alerts

    Deployment Settings:        Select Next.
    Distribution Points

    Summary                     1. Review the information in the Details box that you
                                provided while completing the previous wizard pages.
                                2. Select Next.

    Progress                    The progress for deploying the task sequence is displayed.

    Completion                  Select Close.

   For more information, see the section, "How to Deploy a Task Sequence," in the
   Configuration manager Documentation Library, which is installed with
   Configuration Manager.

Step 6-4: Start the Target Computer with the Task
Sequence Bootable Media

<!-- p.763 -->

Start the target computer (WDG-CLI-01) with the task sequence bootable media created
earlier in the process. This medium starts Windows PE on the reference computer and
initiates the MDT process. At the end of the MDT process, Windows 8.1 is deployed on
the target computer.

  ７ Note

  You can also initiate the MDT process by starting the target computer from
  Windows Deployment Services.

To start the target computer with the task sequence bootable
media
  1. Start WDG-CLI-01 with the task sequence bootable media created earlier in the
     process.

     Windows PE starts, and then the Task Sequence Wizard starts.

  2. Complete the Task Sequence Wizard using the following information. Accept the
     default values unless otherwise specified.

                                                                            ﾉ   Expand table

      On this wizard page           Do this

      Welcome to the Task           In Password, type P@ssw0rd, and then select Next.
      Sequence Wizard

      Select a Task Sequence        In the list box, select Windows 8.1 Target Deployment,
                                    and then select Next.

To monitor the reference computer deployment process using the
Deployment Workbench

  1. On WDG-MDT-01, select Start, and then point to All Programs. Point to Microsoft
     Deployment Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/MDT Deployment Share
     (C:\DeploymentShare$)/Monitoring.

  3. In the details pane, view the deployment process for WDG-CLI-01.

<!-- p.764 -->

4. In the Actions pane, periodically select Refresh.

  The status of the deployment process is updated in the details pane. Continue to
  monitor the deployment process until the process is complete.

5. In the details pane, select WDG-CLI-01.

6. In the Actions pane, select Properties.

  The WDG-CLI-01 Properties dialog box is displayed.

7. In the WDG-CLI-01 Properties dialog box, on the Identity tab, view the monitoring
  information provided about the deployment process as described in the following
  table:

                                                                           ﾉ   Expand table

   Information           Description

   ID                    Unique identifier for the computer being deployed.

   Computer Name         The name of the computer being deployed.

   Deployment status     The current status of the computer being deployed; the status can
                         be one of the following:

                         - Running. The task sequence is healthy and running.
                         - Failed. The task sequence failed, and the deployment process was
                         unsuccessful.
                         - Completed. The task sequence has finished.
                         - Unresponsive. The task sequence has not updated its status in the
                         past four hours and is assumed to be nonresponsive.

   Step                  The current task sequence step being run.

   Progress              The overall progress of the task sequence. The progress bar
                         indicates how many task sequence steps have been run out of the
                         total number of task sequence steps.

   Start                 The time the deployment process started.

   End                   The time the deployment process ended.

   Elapsed               The length of time the deployment process has been running or
                         took to run if the deployment process has finished.

   Errors                The number of errors encountered during the deployment process.

   Warnings              The number of warnings encountered during the deployment
                         process.

<!-- p.765 -->

   Information         Description

   Remote Desktop      This button allows you to establish a remote desktop connection
                       with the computer being deployed using the Windows Remote
                       Desktop feature. This method assumes that:

                       - The target operating system is running and has remote desktop
                       support enabled
                       - mstsc.exe is in the path Note: This button is always visible but may
                       not be able to establish a remote desktop session if the monitored
                       computer is running Windows PE, has not completed installation of
                       the target operating system, or does not have the Remote Desktop
                       feature enabled.

   VM Connection       This button allows you to establish a remote desktop connection to
                       a VM running in Hyper-V. This method assumes that:

                       - The deployment is being performed to a VM running on Hyper-V
                       - vmconnect.exe is located in the %ProgramFiles%\Hyper-V folder
                       Note: This button appears when ZTIGather.wsf detects that Hyper-V
                       integration components are running on the monitored computer.
                       Otherwise, this button will not be visible.

   DaRT Remote         This button allows you to establish a remote control session using
   Control             the remote viewer feature in the Diagnostics and Recovery Toolkit
                       (DaRT).

                       This method assumes that:

                       - DaRT has been deployed to the target computer and is currently
                       running
                       - DartRemoteViewer.exe is located in the
                       %ProgramFiles%\Microsoft DaRT 7\v7 folder Note: This button
                       appears when ZTIGather.wsf detects that DaRT is running on the
                       monitored computer. Otherwise, this button will not be visible.

   Automatically       Check box that controls whether the information in the dialog box is
   refresh this        automatically refreshed. If the check box is:
   information every
   10 seconds          - Selected, the information is refreshed every 10 seconds
                       - Cleared, the information is not automatically refreshed and must
                       be manually refreshed using the Refresh Now button

   Refresh Now         This button immediately refreshes the information displayed in the
                       dialog box.

8. In the WDG-REF-01 Properties dialog box, select OK.

9. Close the Deployment Workbench.

<!-- p.766 -->

To monitor the reference computer deployment process using the
Get-MDTMonitorData cmdlet

  1. On WDG-MDT-01, select Start, point to Administrative Tools, and then select
    Windows PowerShell Modules.The Windows PowerShell Modules command
    prompt opens.

  2. Create a PowerShell drive that uses the MDT PowerShell provider by running the
    New-PSDrive cmdlet as shown in the following example:

      PowerShell

      New-PSDrive -Name DS001 -PSProvider mdtprovider -Root
      d:\DeploymentShare$

  3. View the MDT monitoring process by running the Get-MDTMonitorData cmdlet as
    shown in the following example:

      PowerShell

      Get-MDTMonitorData -Path DS001:

    This command returns the monitoring data collected by the MDT monitoring
    service running on the same computer that hosts the deployment share as shown
    in the following example output:

      PowerShell

      Name               : WDG-REF-01
      PercentComplete    : 96
      Settings           :
      Warnings           : 0
      Errors             : 0
      DeploymentStatus   : 1
      StartTime          : 6/7/2012 6:45:39 PM
      EndTime            :
      ID                 : 1
      UniqueID           : 94a0830e-f2bb-421c-b1e0-6f86f9eb9fa1
      CurrentStep        : 130
      TotalSteps         : 134
      StepName           : Gather
      LastTime           : 6/7/2012 8:46:32 PM
      DartIP             :
      DartPort           :
      DartTicket         :
      VMHost             : XYL-DC-02
      VMName             : WDG-REF-01
      ComputerIdentities : {}

<!-- p.767 -->

        Name               : WDG-CLI-01
        PercentComplete    : 26
        Settings           :
        Warnings           : 0
        Errors             : 0
        DeploymentStatus   : 1
        StartTime          : 6/7/2012 3:07:13 AM
        EndTime            :
        ID                 : 2
        UniqueID           : 94a0830e-f2bb-421c-b1e0-6f86f9eb9fa1
        CurrentStep        : 49
        TotalSteps         : 134
        StepName           : Capture Network Settings using MDT
        LastTime           : 6/7/2012 3:08:32 AM
        DartIP             :
        DartPort           :
        DartTicket         :
        VMHost             :
        VMName             :
        ComputerIdentities : {}

   4. Close the Windows PowerShell console.

     If any problems occur during the deployment, consult the MDT document
     Troubleshooting Reference. When successfully completed, the target computer is
     running a Windows 8.1 operating system configured like the reference computer.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.768 -->

Quick Start Guide for User-Driven
Installation
Article • 02/12/2024

Microsoft Deployment Toolkit (MDT) 2013 provides technology for deploying Windows
operating systems, and Microsoft Office. This quick start guide helps you quickly
evaluate MDT 2013 by providing condensed, step-by-step instructions for using it to
install the Windows 8.1 operating system and Microsoft Office Professional Plus 2010
with User-Driven Installation (UDI) and Microsoft System Center 2012 R2 Configuration
Manager. This quick start guide demonstrates how to perform the MDT New Computer
deployment scenario, which covers the deployment of Windows 8.1 to a new computer.
This scenario assumes that there is no user data or profile to preserve.

  ７ Note

  In this document, Windows applies to the Windows 8.1, Windows 8, Windows 7,
  Windows Server® 2012 R2, Windows Server 2012, and Windows Server 2008 R2
  operating systems unless otherwise noted. MDT does not support ARM processor-
  based versions of Windows. Similarly, MDT refers to MDT 2013 unless otherwise
  stated.

After using this guide to evaluate MDT, review the rest of the MDT guidance to learn
more about the technology's advanced features.

  ７ Note

  The infrastructure setup described here is for evaluation purposes and not intended
  for a production system.

Prerequisites
UDI installations using System Center 2012 R2 Configuration Manager have the
following prerequisites.

Required Software
To complete this guide, the following software is required:

<!-- p.769 -->

     Windows Server 2008 R2

     Microsoft SQL Server® 2008 R2

     SQL Server 2008 R2 Service Pack 1 (SP1)

     SQL Server 2008 R2 SP1 Cumulative Update 6 (CU6)

     Windows 8.1

     System Center 2012 R2 Configuration Manager

     Office Professional Plus 2010 volume license, 32-bit version

     Microsoft .NET Framework version 3.5 with SP1

     Windows PowerShell™ version 2.0

     Windows Preinstallation Environment (Windows PE), which is included in
     Configuration Manager

     Networking services, including Domain Name System (DNS) and Dynamic Host
     Configuration Protocol (DHCP)

     Active Directory® Domain Services (AD DS)

  ７ Note

  The Task Sequencer used in MDT deployments requires that the Create Global
  Object right be assigned to credentials used to access and run the Deployment
  Workbench and the deployment process. This right is normally available to
  accounts with Administrator-level permissions (unless explicitly removed). Also, the
  Specialized Security - Limited Functionality (SSLF) security profile removes the
  Create Global Object right and should not be applied to computers deployed using
  MDT.

Computer Configuration
To complete this guide, set up the computers listed in Table 1. These computers can be
either physical computers or virtual machines (VMs) with the system resources
designated.

Table 1. Computers Used in This Guide

<!-- p.770 -->

                                                                                  ﾉ    Expand table

 Computer      Description and system resources

 WDG-MDT-      This computer runs the MDT infrastructure and Configuration Manager. The
 01            computer runs Windows Server 2008 R2 with the following networking services
               installed:

               - AD DS
               - DNS Server
               - DHCP Server
               - Windows Deployment Services

               The system resources of the computer are as follows:

               - Quad-core processor running at 2.66 gigahertz (GHz) or faster
               - 4 gigabytes (GB) or more of physical memory
               - A disk partition that has 40 GB or more of available disk space; it will become the
               drive C partition
               - One CD-ROM or DVD-ROM drive that will be assigned the drive letter D
               - A disk partition that has 40 GB or more of available disk space; it will become
               partition E.

 WDG-REF-      This is the reference computer, which runs no current operating system. The system
 01            resources of the computer are as follows:

               - Processor running at 1.4 GHz or faster
               - 1 GB or more of physical memory
               - 16 GB or more of available disk space

 WDG-CLI-      This is the target computer, which runs no current operating system. The system
 01            resources of the computer are as follows:

               - Processor running at 1.4 GHz or faster
               - 1 GB or more of physical memory
               - 16 GB or more of available disk space

The resources listed in Table 1 reflect the system resources recommended to perform
the steps in this guide. For information on the minimum system resource requirements
for:

       Windows Server 2008 R2, see Installing Windows Server 2008 R2

       SQL Server 2008 R2, see Hardware and Software Requirements for Installing SQL
       Server 2008 R2

  ７ Note

<!-- p.771 -->

  This guide assumes that MDT is being evaluated on 64-bit (x64) physical or virtual
  computers. If evaluating MDT on 32-bit (x86) platforms, download and install the
  x86 editions of MDT and the components that this guide describes.

Step 1: Prepare the Prerequisite Infrastructure
For purposes of this guide, all the prerequisite infrastructure services run on the
computer named WDG-MDT-01. Install the prerequisite software, server roles, and
services on this computer before installing MDT.

  ７ Note

  This section assumes that you are creating a new Configuration Manager
  infrastructure for MDT. If you are using an existing Configuration Manager
  infrastructure, review the steps in this section and substitute existing resource
  names for the resources created in this section (such as the computer name and
  shared network folders). After reviewing this section, proceed to Step 2: Prepare
  the MDT Environment

Prepare the prerequisite infrastructure before installing MDT by:

     Installing Windows Server 2008 R2 as described in Step 1-1: Install Windows Server
     2008 R2

     Creating the required folders and network shares as described in Step 1-2: Create
     the Required Folders and Network Shares

     Obtaining the software required to perform the steps in this guide as described in
     Step 1-3: Obtain the Required Software

     Installing the AD DS server role as described in Step 1-4: Install the AD DS Server
     Role

     Installing the DHCP Server server role as described in Step 1-5: Install the DHCP
     Server Server Role

     Installing the Web Services (IIS) server role as described in Step 1-6: Install the Web
     Services (IIS) Server Role

     Adding the required Windows Server 2008 R2 features as described in Step 1-7:
     Add the Required Windows Server 2008 R2 Features

<!-- p.772 -->

     Creating the user and service accounts required to perform the steps in this guide
     as described in Step 1-8: Create the Required User and Service Accounts

     Installing SQL Server 2008 R2 for Configuration Manager to use as described in
     Step 1-9: Install SQL Server 2008 R2

     Adding the site server to the Administrators security group as described in Step 1-
     10: Add the Site Server to the Administrators Security Group

     Installing Configuration Manager as described in Step 1-11: Install Configuration
     Manager

     Configuring the Network Access Account that Configuration Manager clients use
     to access Configuration Manager distribution points as described in Step 1-12:
     Configure the Network Access Account

     Configuring the Configuration Manager site boundaries and boundary groups as
     described in Step 1-13: Configure the Configuration Manager Site Boundaries and
     Boundary Groups

     Configuring the publishing of site information in AD DS and DNS as described in
     Step 1-14: Configure the Publishing of Site Information in AD DS and DNS

     Configuring discovery of users in AD DS as described in Step 1-15: Configure
     Discovery of Active Directory Users

Step 1-1: Install Windows Server 2008 R2
Use the information in 2 to install Windows Server 2008 R2. Accept default values unless
otherwise specified.

Table 2. Information for Installing Windows Server 2008
R2

                                                                        ﾉ   Expand table

 When prompted for         Provide these values

 Where do you want to      Disk 0 Unallocated Space
 install Windows?

 Password                  Any strong password

 Computer name             WDG-MDT-01

<!-- p.773 -->

 When prompted for            Provide these values

 Format for volumes C and     NTFS
 E

 TCP/IP configuration         Configure with a static IP address configuration, with the other
                              TCP/IP configuration options as appropriate for the environment

Step 1-2: Create the Required Folders and Network Shares
The MDT deployment process requires additional folders that are used as the source for
files or to store files created during the MDT deployment process. Some of these folders
need to be shared so that they can be accessed from other computers.

To create the required folders and shares

     1. Create the folders and shares listed in Table 3 with the permissions specified for
       each share

       Table 3. Folders That the MDT Deployment Process
       Requires

                                                                                ﾉ   Expand table

        Create this folder     With this share name          With these share permissions

        E:\Source$             Source$                       Administrators: Co-owner

                                                             Everyone: Read

        E:\Images$             Images$                       Administrators: Co-owner

                                                             Everyone: Read

        E:\Capture$            Capture$                      Administrators: Co-owner

                                                             Everyone: Read

        E:\Packages$           Packages$                     Administrators: Co-owner

                                                             Everyone: Read

     2. Create the following folders:

             E:\CMDownloads

<!-- p.774 -->

            E:\Source$\CustomSettings

            E:\Source$\Drivers

            E:Source$Windows_8-1

            E:Source$MDT_2013

            E:Source$SQL2008R2

            E:Source$SQL2008R2SP1

            E:Source$SQL2008R2CU6

            E:Source$OfficeProPlus2010

            E:Source$ConfigMgr

            E:Packages$Drivers

   3. Copy the device drivers for the reference computer (WDG-REF-01) and the target
     computer (WDG-CLI-01) to E:\Source$\Drivers.

        ７ Note

        The processes in this guide assume that the reference computer and target
        computer have the same devices and do not require different devices drivers.

Step 1-3: Obtain the Required Software
Besides Windows Server 2008 R2, Windows 8.1, and System Center 2012 R2
Configuration Manager, certain software is required to evaluate MDT based on the
processes in this guide. Table 4 lists the software required to perform deployments using
MDT, where to obtain the software, and where to place the software on WDG-MDT-01.

Table 4. Additional Software Required for Deployment
Using MDT

                                                                         ﾉ   Expand table

 Obtain this software                                       Place in this folder

 MDT 2013                                                   E:\Source$\MDT_2013

<!-- p.775 -->

 Obtain this software                                                Place in this folder

 Windows 8.1 distribution files from the product media               E:\Source$\Windows_8-1

 Device drivers required for the reference and target computers      E:\Source$\Drivers
 (WDG-REF-01 and WDG-CLI-01)

 SQL Server 2008 R2 from the product media                           E:\Source$\SQL2008

 SQL Server 2008 R2 SP1, available at                                E:\Source$\SQL2008R2SP1
 https://www.microsoft.com/download/details.aspx?id=26113

 SQL Server 2008 R2 SP1 CU6, available at                            E:\Source$\SQL2008R2SP1CU6
 https://support.microsoft.com/kb/2679367

 System Center 2012 R2 Configuration Manager from the product        E:\Source$\ConfigMgr
 media

 Office Professional Plus 2010 32-bit Volume Licensing version       E:\ Source$\OfficeProPlus2010
 from the product media

Step 1-4: Install the AD DS Server Role
AD DS is required to provide authentication and act as a repository for configuration
values for the Microsoft products and technologies that MDT uses, such as Microsoft
SQL Server and Configuration Manager.

To install AD DS, run the DCPROMO Wizard to configure the computer as a domain
controller. Install AD DS using the information in Table 5, accepting any defaults unless
otherwise specified.

Table 5. Information for Installing AD DS

                                                                                  ﾉ   Expand table

 When prompted                                             Do this

 For the domain type                                       Create a new domain in a new forest.

 For the fully qualified domain name                       Type
                                                           mdt2013.corp.woodgrovebank.com.

 For the forest functional level                           Select Windows Server 2008 R2.

 To install the DNS Server service as part of the domain   Select Yes.
 controller installation process

<!-- p.776 -->

Step 1-5: Install the DHCP Server Server Role
The DHCP Server server role is required to provide automatic IP configuration for the
target computers. Install DHCP Server using the information in Table 6, accepting any
defaults unless otherwise specified.

  ７ Note

  If you are using a virtualized environment, disable any DHCP configuration that the
  computer-virtualization software provides. Ensure that the DHCP Server service
  running WDG-MDT-01 is the only provider of IP configuration using DHCP.

Table 6. Information for Installing the DHCP Server Server
Role

                                                                                ﾉ   Expand table

 On this wizard page           Do this

 Authorize DHCP server in      Authorize WDG-MDT-01 to provide client IP configuration.
 Active Directory

 DHCP scopes                   Create an appropriate scope that can be used to automatically
                               configure TCP/IP for WDG-REF-01 and WDG-CLI-01.

 DHCPv6 stateless mode         Disable DHCPv6 stateless mode for this server.
 configuration

Step 1-6: Install the Web Services (IIS) Server Role
Install the Web Services (IIS) server role with the role services listed in Table 7, which are
required for SQL Server 2008 R2 and Configuration Manager. Unless otherwise specified,
use the default values.

Table 7. Information for Installing the Web Services (IIS)
Server Role

                                                                                ﾉ   Expand table

<!-- p.777 -->

Role service              Status

Web Server                Installed

Common HTTP Features      Installed

Static Content            Installed

Default Document          Installed

Directory Browsing        Installed

HTTP Errors               Installed

HTTP Redirection          Installed

WebDAV Publishing         Installed

Application Development   Installed

ASP.NET                   Installed

.NET Extensibility        Installed

ASP                       Not installed

CGI                       Not installed

ISAPI Extensions          Installed

ISAPI Filters             Installed

Server Side Includes      Not installed

Health and Diagnostics    Installed

HTTP Logging              Installed

Logging Tools             Installed

Request Monitor           Installed

Tracing                   Installed

Custom Logging            Not installed

ODBC Logging              Not installed

Security                  Installed

Basic Authentication      Not installed

Windows Authentication    Installed

<!-- p.778 -->

 Role service                                                       Status

 Digest Authentication                                              Not installed

 Client Certificate Mapping Authentication                          Not installed

 IIS Client Certificate Mapping Authentication                      Not installed

 URL Authorization                                                  Not installed

 Request Filtering                                                  Installed

 IP and Domain Restriction                                          Not installed

 Performance                                                        Installed

 Static Content Compression                                         Installed

 Dynamic Content Compression                                        Not installed

 Management Tools                                                   Installed

 IIS Management Console                                             Installed

 IIS Management Scripts and Tools                                   Not installed

 Management Service                                                 Not installed

 IIS 6 Management Compatibility                                     Installed

 IIS 6 Metabase Compatibility                                       Installed

 IIS 6 WMI Compatibility                                            Installed

 IIS 6 Scripting Tools                                              Not installed

 IIS 6 Management Console                                           Not installed

 FTP Publishing Service                                             Not installed

 FTP Server                                                         Not installed

 FTP Management Console                                             Not installed

 IIS Hostable Web Core                                              Not installed

Step 1-7: Add the Required Windows Server 2008 R2
Features
In addition to installing the required Windows Server 2008 R2 server roles, add the
following required features in Server Manager in the Features Summary section:

<!-- p.779 -->

     Background Intelligent Transfer Service

     Remote Differential Compression

Step 1-8: Create the Required User and Service Accounts
Configuration Manager and SQL Server 2008 R2 require user accounts during the
installation process. Table 8 lists the information needed for creating these accounts.

Table 8. Information for Creating the Required Accounts

                                                                               ﾉ      Expand table

 Create this account                With these settings

 SQL Server Agent service account   1. In First name, type SQL Agent.
                                    2. In Last name, type Service Account.
                                    3. In User logon name, type SQLAgent.
                                    4. In Password and Confirm password, type P@ssw0rd.
                                    5. Clear the User must change password at next logon check
                                    box.
                                    6. Select the Password never expires check box.
                                    7. Make the account a member of the Domain Admins
                                    security group.
                                    8. In Description, type Service account used to run SQL
                                    Server 2008 R2 Agent service.

 SQL Server Database Engine         1. In First name, type SQL DB Engine.
 service account                    2. In Last name, type Service Account.
                                    3. In User logon name, type SQLDBEngine.
                                    4. In Password and Confirm password, type P@ssw0rd.
                                    5. Clear the User must change password at next logon check
                                    box.
                                    6. Select the Password never expires check box.
                                    7. Make the account a member of the Domain Admins
                                    security group.
                                    8. In Description, type Service account used to run SQL
                                    Server 2008 R2 database engine.

 SQL Server Reporting Services      1. In First name, type SQL Reporting.
 service account                    2. In Last name, type Service Account.
                                    3. In User logon name, type SQLReport.
                                    4. In Password and Confirm password, type P@ssw0rd.
                                    5. Clear the User must change password at next logon check
                                    box.
                                    6. Select the Password never expires check box.
                                    7. Make the account a member of the Domain Admins

<!-- p.780 -->

 Create this account               With these settings

                                   security group.
                                   8. In Description, type Service account used to run SQL
                                   Server 2008 R2 reporting services.

 Configuration Manager Client      1. In First name, type CM 2012.
 Network Access account            2. In Last name, type Client Network Access.
                                   3. In User logon name, type CMNetAccess.
                                   4. In Password and Confirm password, type P@ssw0rd.
                                   5. Clear the User must change password at next logon check
                                   box.
                                   6. Select the Password never expires check box.
                                   7. In Description, type Service account used as the network
                                   access account for Configuration Manager Client.

Step 1-9: Install SQL Server 2008 R2
Before installing Configuration Manager, install SQL Server 2008 R2 SP1 and CU6.

  ７ Note

  To enable all SQL Server 2008 R2 features, install the Web Services (IIS) server role
  before installing SQL Server 2008 R2.

To install SQL Server 2008 R2

   1. Start the SQL Server Installation Center.

   2. In the SQL Server Installation Center, in the navigation pane, select Installation.

   3. In the preview pane, select New installation or add features to an existing
     installation.

     SQL Server 2008 R2 Setup Wizard starts.

   4. Install SQL Server 2008 R2 using the information in Table 9, accepting the defaults
     unless otherwise specified.

     Table 9. Information for Installing SQL Server 2008 R2

                                                                              ﾉ   Expand table

<!-- p.781 -->

On this wizard page    Do this

Setup Support Rules    Select OK.

Product Key            Select Next.

License Terms          Select the I accept the license terms check box, and then select
                       Next.

Setup Support Files    Select Install.

Setup Support Rules    Ensure that no critical results exist for the rules, and then select
                       Next.

Setup Role             Select SQL Server Feature Installation, and then select Next.

Feature Selection      1. Select the Database Engine Services check box.
                       2. Select the Reporting Services check box.
                       3. Select the Full-Text Search check box.
                       4. Select the Management Tools - Complete check box.
                       5. Select Next.

Installation Rules     Select Next.

Instance               Select Next.
Configuration

Disk Space             Select Next.
Requirements

Server Configuration   1. For SQL Server Agent, in Account Name, type
                       MDT2013\SQLAgent, in Password, type P@ssw0rd.
                       2. For SQL Server Database Engine, in Account Name, type
                       MDT2013\SQLDBEngine, in Password, type P@ssw0rd.
                       3. For SQL Server Reporting Services, in Account Name, type
                       MDT2013\SQLReport, in Password, type P@ssw0rd.
                       4. Select Next.

Database Engine        Select Add Current User, and then select Next.
Configuration

Reporting Services     Select Next.
Configuration

Error Reporting        Select Next.

Installation           Select Next.
Configuration Rules

Ready to Install       Select Install.

Complete               Select Close.

<!-- p.782 -->

5. Close the SQL Server Installation Center.

  To install SQL Server 2008 R2 SP1

6. In Windows Explorer, go to E:\Source$\SQL2008R2SP1, and double-click
  SQLServer2008R2SP1-KB2528583-x64-ENU.exe.

  The Extracting Files dialog box displays the file-extraction process. When the
  process is complete, the SQL Server 2008 R2 Service Pack 1 Update Setup Wizard
  starts.

7. Install SQL Server 2008 R2 SP1 using the information in Table 10, accepting the
  defaults unless otherwise specified.

  Table 10. Information for Installing SQL Server 2008
  R2 SP1

                                                                           ﾉ   Expand table

   On this wizard page     Do this

   SQL Server 2008 R2      Select Next.
   update

   License Terms           Select the I accept the license terms check box, and then select
                           Next.

   Select Features         Select Next.

   Check Files In Use      Select Next.

   Ready to update         Select Update.

   Update Progress         The progress is displayed on the wizard page as the update is
                           performed and finishes.

   Complete                Select Close.

  To install SQL Server 2008 R2 SP1 CU6

8. In Windows Explorer, go to E:\Source$\SQL2008R2SP1CU6, and double-click
  446622_intl_x64_zip.exe.

  The Microsoft Self-Extractor dialog box appears.

9. In the Microsoft Self-Extractor dialog box, select Continue.

<!-- p.783 -->

10. In the Microsoft Self-Extractor dialog box, in Select the folder where you want to
   unzip the files to, type E:\Source$\SQL2008R2SP1CU6, and then select OK.

      ７ Note

      You can select the ellipsis (...) to browse for the E:\Source$\SQL2008R2SP1CU6
      folder.

   The extraction process is displayed. When the process is complete, the completion
   status is displayed.

11. In the Microsoft Self-Extractor dialog box, select OK.

12. In Windows Explorer, go to E:\Source$\SQL2008R2SP1CU6, and double-click
   SQLServer2008R2- KB2679367-x64.exe.

   The Extracting Files dialog box displays the file-extraction process. When the
   process is complete, the SQL Server 2008 R2 Service Pack 1 CU6 Update Setup
   Wizard starts.

13. Install SQL Server 2008 R2 SP1 CU6 using the information in Table 11, accepting
   the defaults unless otherwise specified.

   Table 11. Information for Installing SQL Server 2008 R2
   SP1 CU6

                                                                            ﾉ   Expand table

    On this wizard page     Do this

    SQL Server 2008 R2      Select Next.
    update

    License Terms           Select the I accept the license terms check box, and then select
                            Next.

    Select Features         Select Next.

    Check Files In Use      Select Next.

    Ready to update         Select Update.

    Update Progress         The progress is displayed on the wizard page as the update is
                            performed and finishes.

<!-- p.784 -->

      On this wizard page    Do this

      Complete               Select Close.

     The Install a SQL Server 2008 R2 update dialog box appears prompting you to
     restart the computer to complete the setup.

 14. In the Install a SQL Server 2008 R2 update dialog box, select OK.

 15. Restart the computer.

 16. After installing SQL Server 2008 R2 SP1 CU6, the SQL Server build number should
     be 10.51.2811.0.

        Tip

       You can verify the SQL Server build number by viewing the SQL Server
       updates applied in the Programs and Features Control Panel item by selecting
       View installed updates.

Step 1-10: Add the Site Server to the Administrators
Security Group
When all computers are in the same forest, manually add the site server computer
account to the local Administrators group on each computer. Complete this step before
configuring the computer as a site system.

To add the site server to the Administrators security group

   1. Select Start, point to Administrative Tools, and then select Active Directory Users
     and Computers.

   2. In the Active Directory Users and Computers console tree, go to
     mdt2013.corp.woodgrovebank.com/Builtin.

   3. In the preview pane, right-click Administrators, and then select Properties.

   4. In the Administrators Properties dialog box, select the Members tab, and then
     select Add.

   5. In the Select Users, Contacts, Computers, or Groups dialog box, select Object
     Types.

<!-- p.785 -->

   6. In the Object Types dialog box, in Object types, select Computers, and then select
     OK.

   7. In the Select Users, Contacts, Computers, or Groups dialog box, in Enter the
     object names to select, type WDG-MDT-01. Select Check Names, and then select
     OK.

   8. Close any open windows.

Step 1-11: Install Configuration Manager
When the other products and technologies have been installed, install Configuration
Manager. Before doing so, however, extend the Active Directory schema so that
computers can locate the distribution points, service locator points, and other server
roles. Also, you can extend the schema after you have installed Configuration Manager.
For more information about how to extend the Active Directory schema for
Configuration Manager, see the section, "Extend the Active Directory Schema," in the
Configuration Manager Documentation Library, which is installed with Configuration
Manager.

After extending the Active Directory schema, install Configuration Manager. The
configuration of WDG-MDT-01 supports Configuration Manager for this sample. The
configuration of computers in the production network may vary. To find out more about
the prerequisites for installing Configuration Manager, see Supported Configurations for
Configuration Manager.

To install Configuration Manager

   1. Start the System Center 2012 R2 Configuration Manager Setup splash screen.

   2. On the System Center 2012 R2 Configuration Manager Setup splash screen, select
     the Install link.

     The Microsoft System Center 2012 R2 Configuration Manager Setup Wizard starts.

   3. Complete the Microsoft System Center 2012 R2 Configuration Manager Setup
     Wizard using the information in Table 12. Accept the defaults unless otherwise
     specified.

     Table 12. Information for Installing Configuration
     Manager

<!-- p.786 -->

                                                                           ﾉ   Expand table

On this wizard page              Do this

Before You Begin                 Select Next.

Getting Started                  Select Next.

Product Key                      In Enter your 25-character product key, type product_key
                                 (where product_key is your product key for Configuration
                                 Manager).

Microsoft Software License       Select the I accept these license terms check box, and
Terms                            then select Next.

Update Prerequisite              In Download and use the latest updates. Updates will be
Components                       saved to the following location, type E:\CMDownloads,
                                 and then select Next.

Server Language Selection        Select Next.

Client Language Selection        Select Next.

Site and Installation Settings   1. In Site code, type NYC.
                                 2. In Site name, type New York City Site.
                                 3. Select Next.

Primary Site Installation        1. Select Install the primary site as a stand-alone site.
                                 2. Select Next.
                                 The Configuration Manager dialog box appears,
                                 confirming that you want to install this site as a stand-
                                 alone site.
                                 3. In the Configuration Manager dialog box, select Yes.

Database Information             Select Next.

SMS Provider Settings            Select Next.

Client Computer                  Select Configure the communication method on each
Communication Settings           site system role, and then select Next.

Site System Roles                Select Next.

Customer Experience              Select the appropriate participation in the Customer
Improvement Program              Experience Improvement program for your organization,
Configuration                    and then select Next.

Settings Summary                 Select Next.

Prerequisite Check               Select Begin Install.

<!-- p.787 -->

      On this wizard page           Do this

      Install                       Monitor the installation process until it is complete, and
                                    then select Close.

   4. Close all open windows and dialog boxes.

     When the wizard is complete, Configuration Manager is installed.

Step 1-12: Configure the Network Access Account
The Configuration Manager client needs an account to provide credentials when
accessing the Configuration Manager distribution points, MDT deployment shares, and
shared folders. This account is called the Network Access account. The CMNetAccess
account was created earlier in the process to use as the Network Access account.

To configure the Network Access account

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select
     Administration.

   3. In the Administration workspace, go to Overview/Site Configuration/Sites.

   4. In the preview pane, select NYC - New York City Site.

   5. On the Ribbon, select Settings, select Configure Site Components, and then select
     Software Distribution.

   6. In the Software Distribution Properties dialog box, select the Network Access
     Account tab.

   7. In Network Access Account, select Specify the account that accessed network
     locations, select Set, and then select New Account.

     The Windows User Account dialog box appears.

   8. Complete the Windows User Account dialog box using the information in Table
     13, and then select OK.

     Table 13. Information Required to Complete the
     Windows User Account Dialog Box

<!-- p.788 -->

                                                                       ﾉ      Expand table

      For this                         Do this

      User name                        Type MDT2013\CMNetAccess.

      Password                         Type P@ssw0rd.

      Confirm password                 Type P@ssw0rd.

   9. In the Software Distribution Properties dialog box, select OK.

 10. Close any open windows.

Step 1-13: Configure the Configuration Manager Site
Boundaries and Boundary Groups
The Configuration Manager client needs to know the boundaries for the site. Unless the
site boundaries are specified, the client assumes that the computer running
Configuration Manager is in a remote site. Add a site boundary based on the IP subnet
that WDG-MDT-01, WDG-REF-01, and WDG-CLI-01 use. Then, add the site boundary to
a site boundary group.

To create a Configuration Manager site boundary

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manger
     Console.

   2. In the Configuration Manager console, in the navigation pane, select
     Administration.

   3. In the Administration workspace, go to Overview/Hierarchy
     Configuration/Boundaries.

   4. On the Ribbon, select Create Boundary.

     The Create Boundary dialog box opens.

   5. Complete the Create Boundary dialog box using the information in Table 14, and
     then select OK.

       ７ Note

<!-- p.789 -->

    For this sample, the site boundary is specified by network address. However,
    you can also specify site boundaries using an AD DS site name or an IP
    address range.

  Table 14. Information Required to Complete the
  Create Boundary Dialog Box

                                                                         ﾉ   Expand table

   For this      Do this

   Description   Type IP Subnet Boundary.

   Type          Select IP subnet.

   Network       Type network_address (where network_address is the network address of the
                 subnet where the computers are installed).

   Subnet        Type subnet_mask (where subnet_mask is the subnet mask of the subnet
   mask          where the computers are installed).

  To add the Configuration Manager site boundary to a site boundary group

6. In the Configuration Manager console, in the navigation pane, select
  Administration.

7. In the Administration workspace, go to Overview/Hierarchy
  Configuration/Boundary Groups.

8. On the Ribbon, select Create Boundary Group.

  The Create Boundary Group dialog box opens.

9. Complete the General tab of the Create Boundary Group dialog box using the
  information in Table 15.

  Table ARABIC 15. Information Required to Complete
  the General Tab of the Create Boundary Group Dialog
  Box

                                                                         ﾉ   Expand table

<!-- p.790 -->

        For this      Do this

        Name          Type New York City Boundary Group.

        Description   Type Boundary group for the site boundaries at the New York City site.

        Boundaries    1. Select Add.
                      The Add Boundaries dialog box appears.
                      2. In the Add Boundaries dialog box, select site_boundary (where
                      site_boundary is the site boundary you created earlier in the process), and
                      then select OK.
                      The site boundary appears in the list of boundaries.

 10. Complete the References tab of the Create Boundary Group dialog box using the
       information in Table 16, and then select OK.

       Table 16. Information Required to Complete the
       References Tab of the Create Boundary Group Dialog
       Box

                                                                                    ﾉ   Expand table

        For this        Do this

        Site            Select the Use this boundary group for site assignment check box.
        assignment

        Content         1. Select Add.
        location        The Add Site Systems dialog box appears.
                        2. In the Add Site Systems dialog box, select \\WDG-MDT-
                        01.mdt2013.corp.woodgrovebank.com, and then select OK.
                        The site system server appears in the list of site system servers.

 11. Close any open windows.

Step 1-14: Configure the Publishing of Site Information in
AD DS and DNS
The Configuration Manager client needs to locate the various Configuration Manager
server roles. Modify the site properties to publish the site information in AD DS and in
DNS.

To configure the publishing of site information in AD DS and in DNS

<!-- p.791 -->

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select
     Administration.

   3. In the Administration workspace, go to Overview/Site Configuration/Sites.

   4. In the preview pane, select NYC - New York City Site.

   5. On the Ribbon, select Properties.

   6. In the New York City Site Properties dialog box, on the Publishing tab, verify that
     the mdt2013.corp.woodgrovebank.com Active Directory forest is listed, and then
     select Cancel.

   7. Close any open windows.

Step 1-15: Configure Discovery of Active Directory Users
In some instances, software will be deployed to user collections that Configuration
Manager discovers. Configuration Manager can discovery user accounts stored in AD DS
using the Active Directory User Discovery method.

To configure discovery of Active Directory users

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select
     Administration.

   3. In the Administration workspace, go to Overview/Hierarchy/Discovery Methods.

   4. In the preview pane, select Active Directory User Discovery.

   5. On the Ribbon, on the Home tab, select Properties.

     The Active Directory User Discovery Properties dialog box appears.

   6. In the Active Directory User Discovery Properties dialog box, on the General tab,
     perform the following steps:

      a. Select the Enable Active Directory User Discovery check box.

<!-- p.792 -->

     b. In Active Directory containers, select New.

        The New Active Directory Container dialog box appears.

     c. In the New Active Directory Container dialog box, in Path, select Browse.

        The Select New Container dialog box appears.

     d. In the Select New Container dialog box, select mdt2013, and then select OK.

        In the New Active Directory Container dialog box, the Lightweight Directory
        Access Protocol (LDAP) path is displayed in the Path box.

     e. In the New Active Directory Container dialog box, select OK.

        The LDAP path appears in the Active Directory containers list box.

  7. In the Active Directory User Discovery Properties dialog box, select OK.

     The Configuration Manager dialog box appears, querying whether you want to
     perform the discovery as soon as possible.

  8. In the Configuration Manager dialog box, select Yes.

  9. In the Configuration Manager console, in the navigation pane, select Assets and
     Compliance.

 10. In the Assets and Compliance workspace, go to Overview/Users.

     The list of users discovered in AD DS is displayed in the preview pane.

 11. Close any open windows.

Step 2: Prepare the MDT Environment
The first step in the deployment process is to prepare the MDT environment. When this
step is complete, you can create the reference computer and deploy a captured image
of it to the target computer (WDG-CLI-01) using Configuration Manager integration
with MDT.

Prepare the MDT environment by:

     Installing MDT as described in Step 2-1: Install MDT

     Enabling Configuration Manager console integration by running the Configure
     ConfigMgr Integration wizard as described in Step 2-2: Enable Configuration
     Manager Console Integration

<!-- p.793 -->

Step 2-1: Install MDT
To install MDT, complete the following steps:

   1. In Windows Explorer, go to E:\Source$\MDT_2013.

   2. Double-click MicrosoftDeploymentToolkit2013_x64.msi (for 64-bit operating
     systems) or MicrosoftDeploymentToolkit2013_x86.msi (for 32-bit operating
     systems), and then select Install.

     The Microsoft Deployment Toolkit 2013 Setup Wizard starts.

   3. Complete the Microsoft Deployment Toolkit 2013 Setup Wizard using the
     information in Table 17. Accept the default values unless otherwise specified.

     Table 17. Information for Completing the Microsoft
     Deployment Toolkit 2013 Setup Wizard

                                                                             ﾉ   Expand table

      On this wizard page                       Do this

      Welcome to the Microsoft Deployment       Select Next.
      Toolkit 2013 Setup Wizard

      End-User License Agreement                Select I accept the terms in the License
                                                Agreement, and then select Next.

      Custom Setup                              Select Next.

      Ready to install Microsoft Deployment     Select Install.
      Toolkit 2013

      Installing Microsoft Deployment Toolkit   The progress for installing MDT is displayed.
      2013

      Completed the Microsoft Deployment        Select Finish.
      Toolkit 2013 Setup Wizard

     The Microsoft Deployment Toolkit 2013 Setup Wizard finishes, and MDT is installed
     on WDG-MDT-01.

Step 2-2: Enable Configuration Manager Console
Integration

<!-- p.794 -->

Before you can use the Configuration Manager integration features of MDT, run the
Configure ConfigMgr Integration wizard. This wizard copies the appropriate integration
files to the folder in which Configuration Manager is installed. The wizard also adds
Windows Management Instrumentation (WMI) classes for the new MDT custom actions.
The classes are added by compiling a new Managed Object Format (.mof) file that
contains the new class definitions.

To enable Configuration Manager console integration

  ７ Note

  Ensure that the Configuration Manager console is closed while performing these
  steps.

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Configure ConfigMgr Integration.

     The Configure ConfigMgr Integration Wizard starts.

   2. Complete the Configure ConfigMgr Integration Wizard using the information in
     Table 18. Accept the default values unless otherwise specified.

     Table 18. Information for Completing the Configure
     ConfigMgr Integration Wizard

                                                                             ﾉ   Expand table

      On this wizard    Do this
      page

      Options           1. Verify that the Install the MDT console extensions for ConfigMgr
                        2012 check box is selected.
                        2. Verify that the Add the MDT task sequence actions to a ConfigMgr
                        server check box is selected.
                        3. In Site server name, verify that the value is WDG-MDT-
                        01.mdt2013.corp.woodgrovebank.com.
                        4. In Site code, verify that the value is NYC.
                        5. Select Next.

      Confirmation      Select Finish.

     The Configure ConfigMgr Integration Wizard finishes, and MDT is integrated with
     Configuration Manager.

<!-- p.795 -->

Step 3: Create and Configure a Task Sequence
to Create a Reference Computer
When you have prepared the MDT environment, create the reference computer. The
reference computer is the template for deploying new images to the target computers.
Configure this computer (WDG-REF-01) exactly as you will configure the target
computers. You will then capture an image of the reference computer and deploy the
image to the target computers.

Create the reference computer, WDG-REF-01, by:

     Creating an MDT task sequence to deploy Windows 8.1 to the reference computer
     as described in Step 3-1: Create an MDT Task Sequence for Deploying the
     Reference Computer

     Selecting the distribution points for the new packages and images that the Create
     MDT Task Sequence Wizard creates as described in Step 3-2: Select the Distribution
     Points for the New Packages and Images

     Adding the necessary device drivers to a new drive package and to the appropriate
     boot images as described in Step 3-3: Add the Necessary Device Drivers

     Enable monitoring of the MDT deployment process as described in Step 3-4:
     Enable MDT Deployment Process Monitoring

     Configuring the MDT configuration files for the reference computer—specifically,
     the CustomSettings.ini file—as described in Step 3-5: Customize the MDT
     Configuration Files for the Reference Computer

     Updating the Configuration Manager distribution points for the Custom Settings
     Files package as described in Step 3-6: Update the Distribution Points for the
     Custom Settings Files Package

     Customizing the task sequence for the reference computer as described in Step 3-
     7: Customize the Task Sequence for the Reference Computer

Step 3-1: Create an MDT Task Sequence for Deploying the
Reference Computer
Use the Create MDT Task Sequence Wizard in the Configuration Manager console to
create task sequences in Configuration Manager that are integrated with MDT. MDT
includes the Standard Client Task Sequence template, which you can use to deploy the
reference computer.

<!-- p.796 -->

The Create MDT Task Sequence Wizard substitutes the packages and images selected
for the placeholders in the task sequence templates. After completing the wizard, the
new task sequence references the appropriate packages and images.

  ７ Note

  Always use the Create MDT Task Sequence Wizard to create task sequences based
  on the MDT task sequence templates. Although you can manually import the task
  sequence templates, Microsoft does not recommend this process.

To create a task sequence for deploying the reference computer

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Task
     Sequences.

   4. On the Ribbon, on the Home tab, in the Task Sequences group, select Create MDT
     Task Sequence.

     The Create MDT Task Sequence Wizard starts.

   5. Complete the Create MDT Task Sequence Wizard using the information in Table 19.
     Accept the default values unless otherwise specified.

     Table 19. Information for Completing the Create MDT
     Task Sequence Wizard

                                                                               ﾉ   Expand table

      On this wizard      Do this
      page

      Choose Template     Select Client Task Sequence, and then select Next.

      Choose Template:    1. In Task sequence name, type Windows 8.1 Reference Deployment.
      General             2. In Task sequence comments, type Task sequence for deploying
                          Windows 8.1 to the reference computer (WDG-REF-01), and then
                          select Next.

<!-- p.797 -->

On this wizard     Do this
page

Choose Template:   1. Select Join a workgroup.
Details            2. In Workgroup, type WORKGROUP.
                   3. In User name, type Woodgrove Bank Employee.
                   4. In Organization name, type Woodgrove Bank.
                   5. In Product key, type product_key (where product_key is the product
                   key for Windows 8.1).
                   6. Select Next.

Choose Template:   a. Select This task sequence may be used to capture and image.
Capture Settings   b. In Capture destination, type \\WDG-MDT-01\Capture$\WDG-
                      REF-01.wim.
                   c. In Capture account, select Set.
                   d. Complete the Windows User Account dialog box by performing
                      the following steps:

                        i. In User name, type MDT2013\Administrator.
                       ii. In Password and Confirm password, type P@ssw0rd.
                   e. Select OK.
                    f. Select Next.

Boot Image         1. Select Create a new boot image package.
                   2. In Package source folder to be created, type \\WDG-MDT-
                   01\Packages$\WINPE_Custom, and then select Next.

Boot Image:        1. In Name, type Windows PE Custom.
General Settings   2. In Version, type 1.00.
                   3. In Comments, type Customized version of Windows PE to be
                   used in deployment of reference and target computers, and then
                   select Next.

Boot Image:        Under Platform, select x64, and then select Next.
Options

Boot Image:        Select Next.
Components

Boot Image:        Select Next.
Customization

MDT Package        1. Select Create a new Microsoft Deployment Toolkit Files package.
                   2. In Package source folder to be created, type \\WDG-MDT-
                   01\Packages$\MDT_Files, and then select Next.

MDT Package:       1. In Name, type MDT Files.
MDT Details        2. In Version, type 1.00.
                   3. In Comments, type Provides access to MDT files during
                   Configuration Manager deployment process, and then select Next.

<!-- p.798 -->

 On this wizard      Do this
 page

 OS Image            1. Select Create a new OS install package.
                     2. In OS installation folder location, type \\WDG-MDT-
                     01\Source$\Windows_8-1.
                     3. In Package source folder to be created, type \\WDG-MDT-
                     01\Packages$\Windows_8-1, and then select Next.

 OS Image: Image     1. In Name, type Windows 8.1.
 Details             2. In Version, type 1.00.
                     3. In Comments, type Windows 8.1 package used to deploy to
                     reference computers, and then select Next.

 Deployment          Select Next.
 Method

 Client Package      Select Create a new ConfigMgr client package, and then select Next.

 USMT Package        1. Select Create a new USMT package.
                     2. In Package source folder to be created, type \\WDG-MDT-
                     01\Packages$\USMT, and then select Next.

 USMT Package:       1. In Name, type USMT.
 USMT Details        2. In Version, type 1.00.
                     3. In Comments, type USMT files used to capture and restore user
                     state migration information, and then select Next.

 Settings Package    1. Select Create a new settings package.
                     2. In Package source folder to be created, type \\WDG-MDT-
                     01\Packages$\CustomSettings_Reference, and then select Next.

 Settings Package:   1. In Name, type MDT Reference Computer Custom Settings.
 Settings Details    2. In Version, type 1.00.
                     3. In Comments, type Configuration settings for MDT deployment
                     process (such as CustomSettings.ini) for the reference computer,
                     and then select Next.

 Sysprep Package     Select Next.

 Summary             Review the information in the Details box that you provided while
                     completing the previous wizard pages, and then select Next.

 Progress            The progress for creating the task sequence is displayed.

 Confirmation        Select Finish.

The new task sequence appears in the preview pane.

<!-- p.799 -->

Step 3-2: Select the Distribution Points for the New
Packages and Images
The Create MDT Task Sequence Wizard creates a number of packages and images. After
these packages and images are created, select the distribution points from which the
packages and images will be copied and available to target computers.

  ７ Note

  In this sample, there is only one distribution point (WDG-MDT-01). However, most
  production networks have multiple distribution points. When performing this step
  in a production environment, select the appropriate distribution points for the
  network.

To select the distribution points for software distribution packages

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Task
     Sequences.

   4. In the preview pane, select Windows 8.1 Reference Deployment.

   5. On the Ribbon, on the Home tab, in the Deployment group, select Distribute
     Content.

     The Distribute Content Wizard starts.

   6. Complete the Distribute Content Wizard using the information in 20. Accept
     default values unless otherwise specified.

     Table 20. Information for Completing the Distribute
     Content Wizard

                                                                        ﾉ   Expand table

<!-- p.800 -->

      On this wizard    Do this
      page

      General           Select Next.

      General:          Select Next.
      Content

      General:          1. Select Add, and then select Distribution Point.
      Content           The Add Distribution Points dialog box appears.
      Destination       2. In the Add Distribution Points dialog box, select
                        \\WDGMDT01.mdt2013.corp.woodgrovebank.com, and then select OK.
                        \\WDGMDT01.mdt2013.corp.woodgrovebank.com appears in the
                        Content destination list.
                        3. Select Next.

      Summary           Review the information in the Details box that you provided while
                        completing the previous wizard pages, and then select Next.

      Progress          The progress for distributing the software is displayed.

      Completion        Select Close.

   7. Close all open windows and dialog boxes.

Step 3-3: Add the Necessary Device Drivers
When the MDT task sequence has been created, add any device drivers required for the
reference computer (WDG-REF-01) to the Windows PE boot image and to the Windows
8.1 image. Add the device drivers in the Drivers node in the Configuration Manager
console. Create a package that contains the device drivers, and inject the drivers into the
custom Windows PE image created earlier in the process.

After creating the package that contains the device drivers, select the distribution point
to which the package will be deployed.

To add the necessary device drivers

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Drivers.
