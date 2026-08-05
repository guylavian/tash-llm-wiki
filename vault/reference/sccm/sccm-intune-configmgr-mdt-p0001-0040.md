---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1-40"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0001-0040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0001-0040
family: sccm
documentKind: "doc"
abstract: "Tell us about your PDF experience. Microsoft Deployment Toolkit documentation Microsoft Deployment Toolkit (MDT) provides a unified collection of tools, processes, and guidance for automating desktop and server deployments. Get MDT ａ DOWNLOAD Download MDT Release notes Known iss"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1-40

<!-- p.1 -->

                                                               Tell us about your PDF experience.

Microsoft Deployment Toolkit
documentation
Microsoft Deployment Toolkit (MDT) provides a unified collection of tools, processes, and
guidance for automating desktop and server deployments.

  Get MDT

  ａ DOWNLOAD
  Download MDT

  Release notes

  Known issues

  FAQ

  ｃ HOW-TO GUIDE
  How to use MDT

  Samples guide

  Scenario guides

  ｆ QUICKSTART
  Lite-touch (LTI)

  Zero-touch (ZTI)

  User-driven (UDI)

  MDT References

  ｉ REFERENCE
  Toolkit reference

  Troubleshoot MDT

  Task Sequence Steps

<!-- p.2 -->

Properties

Scripts

Support Files

Utilities

MDT Windows PowerShell Cmdlets

Tables and Views in the MDT DB

Windows 7 Feature Dependency Reference

UDI References

ｉ REFERENCE
UDI developer's guide

UDI Reference

<!-- p.3 -->

Microsoft Deployment Toolkit release notes
This article provides details on the latest release of the Microsoft Deployment Toolkit (MDT).
These details include supported platforms, prerequisites, and any limitations. It assumes
familiarity with MDT version concepts, features, and capabilities.

  Ｕ Caution

  Microsoft Deployment Toolkit (MDT) is retired.
    Microsoft Deployment Toolkit (MDT) is retired. MDT integration with Configuration
    Manager and MDT Standalone are no longer supported. Customers should remove
    all MDT task sequence steps and then remove MDT integration to prevent task
    sequence corruption and modification failures. Consider moving to modern
    provisioning solutions such as Windows Autopilot, which provides cloud‑driven,
    zero‑touch provisioning for Windows devices. Learn more about Autopilot: here. For
    customers with on-premises infrastructure and existing Configuration Manager
    environments, OSD remains a fully supported option.

  For full details on this retirement, see the Removed and Deprecated Features page.

Latest release
MDT build 8456 is the latest version available on the Microsoft Download Center      .

This update begins support for Windows 10, version 1809, and Windows Server 2019. For more
information, see the supported platforms section.

Significant changes
Here is a summary of the significant changes in MDT build 8456.

Supported configuration updates
     Windows ADK for Windows 10, version 1809
     Windows 10, version 1809
     Configuration Manager, version 1810

<!-- p.4 -->

Major changes
The following list is a summary of the major changes in this version:

     Nested task sequence support for LTI scenario
     Modern language pack support Known issue
     Support for Configuration Manager version 1810
     IsVM evaluates to False on Parallels VMs
     IsVM = False when VMware VM is configured with EFI boot firmware
     Gather doesn't recognize All-in-One chassis type
     MDT doesn't automatically install BitLocker on Windows Server 2016
     BDEDisablePreProvisioning typo in ZTIGather.xml

Supported platforms
MDT releases are no longer tagged with year or update version. To align better with the current
branches of Windows 10 and Configuration Manager, and to simplify the branding and release
process, it's now simply Microsoft Deployment Toolkit. The build number is used to
distinguish each release. For example, the latest build available for download is 8456.

Unlike Configuration Manager with a predetermined release schedule, MDT only releases as
required to support new versions of Windows, the Windows ADK, or Configuration Manager
current branch. Any known issues with these components will be documented in this article as
necessary.

The following OS versions are supported for deployment with this build of MDT:

     Windows 10, version 1809
     Windows 10, version 1803
     Windows 10, version 1709
     Other supported versions of Windows 10
     Windows Server 2019
     Windows Server 2016

  ７ Note

  MDT doesn't support Windows 10 ARM64 devices or any Windows versions released after
  those listed above.

FAQ: Is this release only supported with Windows 10, Windows ADK, or Configuration Manager
version X?

<!-- p.5 -->

Prerequisites
MDT requires the following components, which are included in Windows:

      Microsoft .NET Framework 4.0
      Windows PowerShell version 3.0

MDT requires the latest Windows ADK for Windows 10. MDT also requires the Windows PE
add-on for the Windows ADK.

  ７ Note

  Windows recommends using the Windows ADK that matches the version of Windows
  you're deploying. For example, use the Windows ADK for Windows 10 version 1809 when
  deploying Windows 10 version 1809. For more information on Windows ADK component
  supportability, see DISM supported platforms and USMT requirements.

When integrating MDT with Configuration Manager for ZTI and UDI scenarios, use the latest
version of Configuration Manager current branch.

Upgrade MDT
The MDT installation process removes any existing instances of MDT installed on the same
computer. Existing deployment shares, distribution points, and databases are preserved during
this process. They must be upgraded when the installation is complete.

The current release of MDT supports upgrading from the following versions of MDT:

      MDT build 8450

   Tip

  Create a backup of the existing MDT infrastructure before attempting an upgrade.

LTI
After installing MDT, upgrade an existing deployment share by running the Open Deployment
Share Wizard from the Deployment Shares node in the Deployment Workbench. Specify the
path to the existing deployment share directory, and then select the Upgrade check box. This
process also upgrades existing network deployment shares and media deployment shares, so

<!-- p.6 -->

those shares should be accessible. Don't upgrade with active deployments, because in-use files
can cause upgrade problems.

ZTI
Existing MDT task sequences present in Configuration Manager aren't modified during the
installation process of MDT. They should continue to work without any issue. No mechanism is
provided to upgrade these task sequences. If you want to use any of the new MDT capabilities,
create new MDT-integrated task sequences in Configuration Manager.

When the upgrade process is complete:

      Run the Configure ConfigMgr Integration Wizard after the upgrade. It registers the new
      components and installs the updated ZTI task sequence templates.

      Create a new Microsoft Deployment Toolkit Files package for any new ZTI task
      sequences you create. You can use the existing MDT Files package for any ZTI task
      sequences created before the upgrade. Create a new MDT Files package for new ZTI task
      sequences.

Next steps
Known issues

Frequently asked questions

Last updated on 01/06/2026

<!-- p.7 -->

Microsoft Deployment Toolkit known
issues
Article • 01/18/2023

This article provides details of any current known issues and limitations with the
Microsoft Deployment Toolkit (MDT). It assumes familiarity with MDT version concepts,
features, and capabilities.

  ） Important

  MDT is not supported with Windows 11. Any listed known issues for Windows 11 or
  the ADK for Windows 11 is for informational purposes only and does not imply
  support. For additional information, please see Supported platforms

The Create Boot Image using MDT wizard fails
when creating a boot image in Microsoft
Configuration Manager after upgrading to ADK
for Windows 11, version 22H2
After upgrading to the ADK for Windows 11, version 22H2, the Create Boot Image using
MDT wizard fails when trying to create a boot image with the following error:

Could not find a part of the path 'C:\Program Files (x86)\Windows Kits\10\Assessment
and Deployment Kit\Windows Preinstallation Environment\x86\WinPE_OCs'.

This error occurs regardless if the boot image being created is x64.

This error is an expected error since starting with the ADK for Windows 11, version
22H2, the 32-bit versions of Windows PE are no longer included. Additionally, MDT isn't
supported with Windows 11 or the ADK for Windows 11. For more information, see
Download and install the Windows ADK.

The Create Boot Image using MDT wizard was created when Configuration Manager
had no out of box functionality to create boot images using the currently installed ADK
directly in the console. Integrating MDT with Configuration Manager added the
functionality to create boot images using the currently installed ADK in the console.
However, Configuration Manager has since added the ability to create boot images in
console out of the box without the need for MDT integration.

<!-- p.8 -->

Additionally, boot images created using the Create Boot Image using MDT wizard
aren't required for task sequences created using the Create MDT Task Sequence wizard.
These boot images and task sequences are commonly called "MDT" boot images and
"MDT" task sequences. However, there's nothing special about an "MDT" boot image
and they're binary equivalent to a Configuration Manager boot image. "MDT" task
sequences are also not special. They're just Configuration Manager task sequences that
happen to run MDT scripts. In other words, "MDT" boot images are not required for
"MDT" task sequences to work. There are no additional binaries in an "MDT" boot image
that are required by "MDT" task sequences. Configuration Manager boot images will
work without issue with "MDT" task sequences.

Instead of using the Create Boot Image using MDT wizard to create boot images in
Configuration Manager, use the out of box functionality in Configuration Manager to
create boot images. For more information, see Managing boot images with
Configuration Manager: Update distribution points with the boot image.

To create a new boot image using the out of box Configuration Manager functionality:

   1. Navigate to the path that hosts the default x64 boot image on the Configuration
     Manager site server. This path would normally be
     <Configuration_Manager_install_directory>\OSD\boot\x64 .

   2. In the \OSD\boot\x64 directory, make a copy of boot.wim and rename it to the
     name of your choice.

   3. In the Configuration Manager console, go to the Software Library node and then
     navigate to Overview > Operating Systems > Boot Images.

   4. Right-click on Boot Images and select Add Boot Image.

   5. Follow the Add Boot Image Wizard to import the copy of boot.wim created in
     Step 2 as a new boot image. For more information on adding a boot image using
     the Add Boot Image Wizard, see Manage boot images with Configuration
     Manager: Add a boot image.

   6. Once the Add Boot Image Wizard completes and the new boot image has been
     added, right-click on the newly created boot image and select Update Distribution
     Points.

       ７ Note

       Don't first distribute the newly created boot image to distribution points
       before selecting Update Distribution Points. The next steps will finish

<!-- p.9 -->

        updating the newly created boot image so that it is the same version as the
        currently installed ADK and Windows PE. This can be accomplished without
        first distributing the newly created boot image to the distribution points. It is
        better to finish properly creating the boot image before distributing the boot
        image to distribution points to avoid unnecessary updates to the distribution
        points. Distributing the boot image first before finishing updating the boot
        image will result in unneeded updates to the distribution points.

   7. In the Update Distribution Points Wizard, select the option Reload this boot
     image with the current Windows PE version from the Windows ADK, select Next
     >, and then Next > again.

   8. Allow the Update Distribution Points Wizard to complete.

Once the Update Distribution Points Wizard completes, the newly created boot image
will be at the same version as the currently installed ADK and Windows PE.

If additional components need to be added to the boot image:

   1. Right-click on the newly created boot image and select Properties.

   2. In the boot image properties window, select the Optional Components tab

   3. Add in the desired optional components. For more information, see Manage boot
     images with Configuration Manager: Optional components.

Make any additional desired changes to the newly created boot image, such as adding
drivers, and then distribute the boot image to distribution points.

  ７ Note

  The above guide only shows x64 boot images since only x64 boot images are
  supported with the ADK for Windows 11, version 22H2 or newer.

HTA applications report Script error after
upgrading to ADK for Windows 11, version
22H2
After you updated your MDT boot image to ADK for Windows 11, version 22H2, HTA
applications stop working and a message box is displayed:

<!-- p.10 -->

Script Error - An error has occurred in the script on this page.

HTA applications rely on MSHTML and starting with Windows 11, version 22H2, the
default legacy scripting engine was changed.

To work around this issue, you need to add the following registry value in WinPE:

  Windows Command Prompt

   reg.exe add "HKLM\Software\Microsoft\Internet Explorer\Main" /t REG_DWORD
  /v JscriptReplacement /d 0 /f

To enable this change in MDT, we recommend that you back up the following file:
C:\Program Files\Microsoft Deployment Toolkit\Templates\Unattend_PE_x64.xml and to

modify it as follows:

  XML

  <unattend xmlns="urn:schemas-microsoft-com:unattend">
      <settings pass="windowsPE">
          <component name="Microsoft-Windows-Setup"
  processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35"
  language="neutral" versionScope="nonSxS"
  xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State">
              <Display>
                  <ColorDepth>32</ColorDepth>
                  <HorizontalResolution>1024</HorizontalResolution>
                  <RefreshRate>60</RefreshRate>
                  <VerticalResolution>768</VerticalResolution>
              </Display>
              <RunSynchronous>
                  <RunSynchronousCommand wcm:action="add">
                      <Description>Fix HTA scripts error Windows 11 ADK
  22H2</Description>
                      <Order>1</Order>
                      <Path>reg.exe add "HKLM\Software\Microsoft\Internet
  Explorer\Main" /t REG_DWORD /v JscriptReplacement /d 0 /f</Path>
                  </RunSynchronousCommand>
                  <RunSynchronousCommand wcm:action="add">
                      <Description>Lite Touch PE</Description>
                      <Order>2</Order>
                      <Path>wscript.exe X:\Deploy\Scripts\LiteTouch.wsf</Path>
                  </RunSynchronousCommand>
              </RunSynchronous>
          </component>
      </settings>
  </unattend>

After saving the changes, you'll need to completely regenerate the boot images.

<!-- p.11 -->

Windows Deployment Services (WDS) multicast
stops working after upgrading to ADK for
Windows 11
After you updated your MDT boot image to ADK for Windows 11, you might see popups
in Windows PE (WinPE) multicast enabled environments prompting wdscommonlib.dll
and imagelib.dll are missing in WinPE.

The right way to add WDS multicast to WinPE is to install WinPE-WDS-Tools OC (WinPE
optional components) into WinPE.

Follow this example to install WinPE-WDS-Tools OC in WinPE (assuming the mount
folder E:\mnt exists).

  Windows Command Prompt

  Dism /mount-wim
  /WimFile:"E:\DeploymentShare\Boot\LiteTouchPE_multicast_x64.wim" /Index:1
  /MountDir:E:\mnt
  Dism /Image:"E:\mnt" /Add-Package /PackagePath:"C:\Program Files
  (x86)\Windows Kits\10\Assessment and Deployment Kit\Windows Preinstallation
  Environment\amd64\WinPE_OCs\WinPE-WDS-Tools.cab"
  Dism /Image:"E:\mnt" /Add-Package /PackagePath:"C:\Program Files
  (x86)\Windows Kits\10\Assessment and Deployment Kit\Windows Preinstallation
  Environment\amd64\WinPE_OCs\en-us\WinPE-WDS-Tools_en-us.cab"
  Dism /Unmount-Wim /MountDir:E:\mnt /Commit

Add or replace the multicast enabled boot image in WDS snap-in for Microsoft
Management Console (MMC).

ZTI extensions with version 2013 or 2107
If you install a new Configuration Manager site with version 2103 or 2107, when you run
the MDT Configure ConfigMgr Integration Wizard, the MDT extensions aren't added to
the site.

To work around this issue, disable the hierarchy setting for approved console extensions.
For more information, see Enable or disable hierarchy approved console extensions.

Windows 10, version 2004
When you use MDT build 8456 with the Windows ADK for Windows 10, version 2004,
the BIOS firmware type is incorrectly identified as UEFI. This issue results in failures when

<!-- p.12 -->

refreshing an existing computer with a new version of Windows. To mitigate this issue,
install the MDT hotfix 4564442     .

Modern language pack support
Starting with Windows 10 version 1809, language interface packs (LIPs) are delivered as
local experience packs (LXPs). LXPs are AppX bundles. When specified in the
unattend.xml file, they aren't automatically selected, and the deployment fails. Don't set
LXPs as default. Users should select an applied LXP from Windows settings.

Security risk when run over the network
Binaries or scripts that run over the network aren't verified against a digital signature.
This issue increases the risk of an attacker tampering with the binaries and injecting
malicious code.

To mitigate this issue, protect the network connection with IPsec or SMB signing.

Next steps
Release notes

Frequently asked questions

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.13 -->

Microsoft Deployment Toolkit frequently
asked questions (FAQ)
This article provides frequently asked questions (FAQ) about the Microsoft Deployment Toolkit
(MDT). It assumes familiarity with MDT version concepts, features, and capabilities.

What's the MDT support life cycle?
For more information, see Microsoft Deployment Toolkit support life cycle.

Is this release only supported with version
'X' of Windows client, Windows ADK, or
Configuration Manager?
We primarily tested this build of MDT with the configuration listed in the supported platforms
list. Unless there are any explicit known issues, anything outside of the above configuration has
a high probability of still working. Your mileage may vary as we haven't explicitly tested other
combinations.

  ７ Note

  This answer also applies to Windows 11.

How do I get help with MDT?
Use one of the following methods to get help with MDT (in prioritized order):

   1. Post to the MDT forum. MVPs and others in the community watch and respond to posts
     there. This method is probably the most efficient way to get help.

   2. Contact Microsoft Support. Open a support case and get some professional help.

   3. If you can consistently reproduce an issue and think it's a product bug, file it in the
     Windows 10 Feedback Hub        . The product team investigates everything that's reported.
     When filing feedback, use the Enterprise Management category and OS Deployment
     subcategory. This categorization helps classify and route your feedback to the MDT team.

<!-- p.14 -->

Next steps
Release notes

Known issues

<!-- p.15 -->

Using the Microsoft Deployment Toolkit
Article • 10/26/2022

Microsoft® Deployment Toolkit (MDT) 2013 allows you to automate the deployment of
computers in your organization. This document provides guidance on how to plan,
build, and deploy Windows® operating systems and applications using MDT 2013.

  ７ Note

  In this document, Windows applies to the Windows 8.1, Windows 8, Windows 7,
  Windows Server® 2012 R2, Windows Server 2012, and Windows Server 2008 R2
  unless otherwise noted. MDT does not support ARM processor-based versions of
  Windows. Similarly, MDT refers to MDT 2013 unless otherwise stated.

MDT performs deployments by using the Lite Touch Installation (LTI), Zero Touch
Installation (ZTI), and User-Driven Installation (UDI) deployment methods. Only MDT is
used in LTI deployments, while ZTI and UDI deployments are performed using MDT with
Microsoft System Center 2012 R2 Configuration Manager.

This document covers these deployment methods and shows how to customize the
deployment process for an organization. In addition to this document, Table 1 lists other
documents that will help you perform deployments using MDT in your organization.

Table 1. Additional MDT Documents for Use in the
Deployment Process

                                                                               ﾉ   Expand table

 Document                Description

 Microsoft Deployment    Provides scenario-based samples of how to solve common deployment
 Toolkit Samples Guide   issues using MDT. Most samples include example configuration files and
                         step-by-step processes for implementing the solution. Use this
                         document to help solve difficult deployment problems.

 Toolkit Reference       Provides information about the task sequence steps, properties, support
                         files, utilities, and databases used in MDT deployments. Use this
                         document to help customize MDT deployments for your organization.

 Troubleshooting         Provides information to assist in troubleshooting common problems
 Reference               with MDT deployments, including lists of known issues, reviewing logs,
                         and identifying issues by error code.

<!-- p.16 -->

This document is organized to help you through the planning, building, and deploying
processes in your organization. The following sections in this guide help you perform
LTI, ZTI, and UDI deployments and customize the deployment process. Table 2 lists each
section in this guide, with a brief overview of each.

Table 2. Sections in This Document

                                                                                   ﾉ   Expand table

 Section                   Overview

 Planning MDT              Provides guidance for completing the planning tasks in preparation for
 Deployments               MDT deployments. Review this section to help identify prerequisites,
                           perform capacity planning, and perform any infrastructure remediation
                           prior to deployment in a production environment, and learn how to
                           install MDT in the environment.

 Installing or Upgrading   Provides guidance for performing a new installation of MDT or
 to MDT                    upgrading to MDT from previous versions of MDT.

 Performing LTI            Provides guidance for deploying Windows operating systems and
 Deployments               applications using only MDT. The guidance presented in this section
                           starts immediately after the installation of MDT and provides the steps
                           for creating a reference computer, capturing an image of the reference
                           computer, and then deploying the captured image to target computers
                           in the organization.

 Managing LTI              Provides guidance and step-by-step instructions for managing LTI
 Deployments in the        deployments using the Deployment Workbench, including managing
 Deployment                operating systems, device drivers, applications, the MDT database (MDT
 Workbench                 DB), and other deployment elements in the Deployment Workbench.

 Running the               Provides guidance of how to run the Deployment Wizard to deploy
 Deployment Wizard         operating systems, device drivers, and applications to the target
                           computers in your organization.

 Performing ZTI            Provides guidance for deploying Windows operating systems and
 Deployments Using         applications using MDT and Configuration Manager. The guidance
 Configuration Manager     presented in this section starts immediately after the installation of
                           MDT and provides the steps for creating a reference computer,
                           capturing an image of the reference computer, and then deploying the
                           captured image to target computers in the organization using
                           Configuration Manager.

 Managing ZTI              Provides guidance and step-by-step instructions for managing ZTI
 Deployments in the        deployments using the Configuration Manager console in
 Configuration Manager     Configuration Manager, including managing operating systems, device
                           drivers, applications, and other deployment elements.

<!-- p.17 -->

Section                 Overview

Console in
Configuration Manager

Performing UDI          Provides guidance for deploying Windows operating systems and
Deployments             applications using MDT, Configuration Manager, and the UDI Wizard.
                        The guidance presented in this section starts immediately after the
                        installation of MDT and provides the steps for creating a reference
                        computer, capturing an image of the reference computer, and then
                        deploying the captured image to target computers in the organization
                        using the Configuration Manager console and the UDI Wizard.

Managing UDI            Provides guidance and step-by-step instructions for managing UDI
Deployments             deployments using the Configuration Manager console, the UDI Wizard
                        Designer, and the UDI Wizard, including:

                        - Managing operating systems, device drivers, applications, and other
                        deployment elements in the Configuration Manager console.

                        Most of the deployment process and step-by-step instructions for ZTI
                        are applicable to UDI.

                        - Managing the behavior of the UDI Wizard.

Running the UDI         Provides guidance of how to run the UDI Wizard to deploy operating
Wizard                  systems, device drivers, and applications to the target computers in
                        your organization.

Configuring MDT         Provides guidance on how to customize the process for more advanced
Deployments             deployment scenarios, including a discussion of the MDT configuration
                        files, how to apply configuration settings to groups of computers, and
                        how to apply configuration settings to individual computers.

Performing              Provides guidance on customizing the process for more advanced
Deployments Using the   deployment scenarios, including how to add entries to and retrieve
MDT DB                  configuration settings from the MDT DB.

Preparing the MDT       Provides guidance on preparing the appropriate resources used in the
Migration Resources     MDT deployment process, including network shared folders and
                        database access.

Preparing Windows       Provides guidance on preparing Windows Deployment Services for use
Deployment Services     in initiating the LTI, ZTI, and UDI deployment processes, including
                        creating images and configuring for integration with LTI, ZTI, and UDI
                        deployments.

Planning for            Provides guidance on how to deploy applications by using MDT,
Application             Configuration Manager, and Microsoft Application Virtualization (App-
Deployment              V), including deployment of applications with the operating system
                        image or after the image is deployed.

<!-- p.18 -->

Planning MDT Deployments
The planning process helps you prepare for deployments in a production environment.
The process starts with conceptual designs, which are proven and refined in a test
environment. The result of the planning process is a set of design documents that you
can use to build an MDT deployment infrastructure and perform automated operating
system and application deployments in a production environment.

Overview of the MDT Deployment Process
The purpose of MDT is to help automate the deployment of Windows operating systems
and applications to desktop, portable, and server computers in the environment. At a
high level, MDT automates the deployment process by configuring the unattended
Setup files for Windows and packaging the necessary files into a consolidated image file
that you then deploy to reference and target computers.

Figure 1 illustrates the high-level LTI, ZTI, and UDI deployment processes.

Figure 1. High-level deployment process

The high-level LTI, ZTI, and UDI deployment process is as follows:

   1. Collect the files necessary to perform an MDT deployment, including:

           Windows operating system source files or images

           Windows operating system language packs

<!-- p.19 -->

            Device drivers for reference and target computers

   2. Create the system images, configuration settings, and task sequences to be used in
      deploying Windows and applications to the reference computers.

   3. Deploy the system images to the reference computer and capture an image of the
      reference computer.

   4. Create the configuration settings and task sequences that will deploy the captured
      images of the reference computers to the target computers.

   5. Deploy the captured images of the reference computers to the target computers.

Planning Checklist
Table 3 provides a planning checklist in the form of a list of questions that you can use
to help in the planning process. For each question, use the information provided in the
Overview column to help find answers based on your organization's requirements.

Table 3. Planning Checklist

                                                                                 ﾉ   Expand table

 Question                        Overview

 Where will you store your       Files for the operating system and applications are stored in
 distribution files?             deployment shares for LTI and distribution points for ZTI and
                                 UDI. These files can require many gigabytes of space. Some
                                 organizations might need multiple deployment shares or
                                 distribution points for different regional offices.For more
                                 information, see Estimating MDT Storage Requirements.

 Will you deploy across the      If you are deploying across the network, verify that there is
 network, with removable         sufficient bandwidth between the deployment shares,
 media, or both? Will you use    distribution points, and the target computers, and provide
 multicast deployments?          regional distribution points.For more information, see Choosing
                                 a Deployment Method and Evaluating Network Requirements.

 What is your imaging and        For more information, see Using Reference Computers in MDT
 source file strategy?           Deployments.

 Will you deploy a full set of   For more information, see Using Reference Computers in MDT
 operating system files or a     Deployments.
 custom image?

<!-- p.20 -->

Question                           Overview

How will you handle product        Small organizations might assign each user an individual
keys and licensing?                product key. Larger organizations should use Key Management
                                   Service (KMS) or Multiple Activation Key (MAK) activation. For
                                   more information, see Product Activation and Key
                                   Information   .

Are you going to allow users       Users can select this information at deployment time, or you can
to choose their own operating      configure the information ahead of time. For more information,
system, applications, locale,      see Choosing LTI, ZTI, or UDI Deployments.
time zone, and administrative
password?

Will users refresh their current   For more information, see Identifying Deployment Scenarios.
computer in place, migrate
settings to a new operating
system installation, or get a
new computer?

Which users will be able to        For more information, see Planning for Application Deployment.
install which applications?

Are you going to migrate user      For more information, see Estimate Storage Requirements for
state?                             User State Migration Data.

Do you want to back up             For more information, see Estimate Storage Requirements for
computers before                   Target Computer Backup.
deployment?

Do you want to use                 For more information, see Planning for BitLocker Drive
BitLocker® Drive Encryption?       Encryption.

Will you deploy 32-bit and 64-     For more information, see Estimating MDT Storage
bit operating systems?             Requirements.

Will you deploy different          For more information, see Estimating MDT Storage
product editions (such as          Requirements.
Professional, Ultimate, or
Business)?

What type of deployments will      For more information, see Identifying Deployment Scenarios.
be performed (for example,
deploy a new computer,
replace an existing computer)?

Estimating MDT Storage Requirements

<!-- p.21 -->

LTI deployments store the system images, applications, and other files in deployment
shares. ZTI and UDI deployments store these files on Configuration Manager
distribution points. To determine your storage needs, estimate storage requirements for:

     Computers running MDT as described in Estimate Storage Requirements for
     Computers Running MDT

     Each MDT deployment share as described in Estimate Storage Requirements for
     MDT Deployment Shares

     Each Configuration Manager distribution point as described in Estimate Storage
     Requirements for Configuration Manager Distribution Points

     User state migration data as described in Estimate Storage Requirements for User
     State Migration Data

     Backing up existing computers prior to deployment for Refresh Computer
     deployment scenario as described in Estimate Storage Requirements for Target
     Computer Backup

Estimate Storage Requirements for Computers Running MDT

The computer running MDT has the following storage requirements:

     At least 4 gigabytes (GB) of free space is required on the drive containing the
     %TEMP% folder if you will create a media images. Otherwise, 1 GB of free space is
     required on the drive containing the %TEMP% folder.

     Free space of 1 GB is required on the drive containing the MDT program files.

Estimate Storage Requirements for MDT Deployment Shares
Ensure that sufficient space is available for storing the operating system images,
language packs, and device drivers used in the Deployment Workbench. You store these
images in the MDT deployment shares created in the Deployment Workbench.

Determine the storage requirements for each of the following items in the deployment
share:

     Windows operating system

     Operating system language pack

     Device drivers

<!-- p.22 -->

     Applications

     Determine the size of each image and the number of images required in the
     deployment. Create a unique image for each:

     Version of the Windows operating system to be deployed. A separate image is
     required for each version of Windows, such as Windows 8.1, Windows 7, Windows
     Server 2012 R2, or Windows Server 2008 R2.

     Edition of the Windows operating system to be deployed. A separate image is
     required for each edition of Windows, such as Tablet PC, Ultimate, Business,
     Enterprise, or Datacenter.

     Processor type. A separate image is required for 32-bit and 64-bit versions of
     Windows.

Estimate Storage Requirements for Configuration Manager
Distribution Points

Estimate the storage requirements for Configuration Manager distribution points using
the same calculations described in Estimate Storage Requirements for MDT Deployment
Shares. If the images are distributed to multiple distribution points, the storage
requirements apply to each distribution point.

For more information about planning Configuration Manager distribution points, see
the section, "Distribution Point," in the section, "Planning Configuration Manager Site
Systems for Operating System Deployments," in the Configuration Manager
Documentation Library, which is installed with Configuration Manager.

Estimate Storage Requirements for User State Migration Data

Estimate the amount of storage required for user state migration data that the Windows
User State Migration Tool (USMT) saved during the deployment process by:

     Determining whether to store the user state migration data locally on the target
     computers or network shared folders as described in Determine Where to Store
     User State Migration Data

     Determining the storage requirements for the user state migration data as
     described in Determine Storage Requirements for User State Migration Data

Determine Where to Store User State Migration Data

<!-- p.23 -->

After determining the storage requirements for the user state migration data, determine
where to store the data. Store user state migration data in these locations:

     On the local computer to reduce the time to deploy Windows as well as network
     utilization (recommended)

        ７ Note

        This option can be used only in a Refresh Computer scenario.

     On a shared folder located on a local server to provide a consistent method of
     storing user state migration data or when local storage is not available.

     If user state migration data will be stored locally on the target computers,
     designate a shared folder in which the deploy process can store the data. By
     default, the process attempts to store user state data on the local hard disk for the
     Replace Computer and Refresh Computer scenarios. However, you can override
     this behavior with configuration settings in CustomSettings.ini. In the event that
     there is insufficient disk space for the user state data and new image, the
     deployment scripts attempt to store the information in a shared folder. Providing
     the shared folder as an alternate storage location makes the deployment process
     more reliable.

     Create a share on a server designated during the planning process for holding the
     USMT store files. MDT uses values found in CustomSettings.ini to locate the user
     state store folder.

Determine Storage Requirements for User State Migration Data

For planning purposes, complete the following tasks to estimate the user state
migration storage requirements:

     Run Scanstate.exe in the USMT with the /p option to estimate the size of the user
     state migration data. By using the /p option, you can estimate the disk space
     requirements without actually performing the migration.

     View the size of the contents of the folders in the user profile. Randomly sample
     targeted computers to determine a typical amount of storage required to back up
     the user state migration. Keep in mind that there may be several profiles (user
     name folders) on each target computer, so include each profile to be migrated.

     Calculate the total capacity required by multiplying the average size of the user
     state migration data by the number of days to retain the data, and then

<!-- p.24 -->

     multiplying that result by the number of users to be migrated during the retention
     period. For example, if the average user state migration size is 3 GB, data must be
     stored for five days, 100 users are being migrated each day, and the total storage
     requirement is 1,500 GB (3 GB × 5 days × 100 users per day).

Estimate Storage Requirements for Target Computer Backup

As an optional step in the deployment process for the Refresh Computer scenario, you
can perform a backup of a target computer before deploying the target operating
system.

You perform the backup process in MDT by using the Imagex.exe tool. The backup
process creates an image of the disk volume on which the user state migration data is
stored. The purpose of this backup is for recovery of user state migration data, not to
restore the target computer from the image.

The storage requirements are a function of the average size of the target computer hard
disks, the number of target computers deployed each day, and the length of time you
want to retain the backup. For example, if the average target computer hard disk
contains 80 GB of data, you are deploying 100 computers per day, and you want to
retain the data for one week, the storage requirements for backups are 56 terabytes
(TB), or 80 GB × 100 × 7.

  ７ Note

  By default, the MDT backup process does not back up multiple partitions. If you
  need to back up multiple partitions, modify the MDT deployment process or use an
  alternative backup method.

Planning for Application Deployment
Applications can be deployed as a part of the operating system image or after the
operating system is deployed to the target computer. In preparation for deployment,
perform these tasks:

     Create an application portfolio. Application portfolios include a list of applications
     and the compatibility status of each application. You can create this application
     portfolio by using software-inventory software such as the Application
     Compatibility Toolkit (ACT), the Asset and Compliance feature in Configuration
     Manager.

<!-- p.25 -->

     Identify any dependencies between applications. Applications may have
     dependencies on other applications. For example, an application may rely on
     Microsoft Office Excel® 2007. Identify these dependencies, and include the
     dependent software in the deployment plans.

     Determine whether to deploy applications with the operating system image or
     afterwards. You can deploy applications as part of the operating system image or
     after the operating system is deployed to the target computer. If the application is
     deployed after the operating system is deployed, you can use any software-
     deployment software, such as MDT, Group Policy Software Installation, the
     Application Management feature in Configuration Manager.

     Determine the appropriate method for running applications. You can install and
     run applications on the local computer or deploy them dynamically in a virtualized
     application environment, such as App-V.

     Identify the users approved to install applications. Determine whether users will
     install their applications or if the applications need to be installed by deployment
     technicians. Ensure that the user installing the application has the appropriate
     rights and permissions.

     Identify applications that require a restart of the operating system. Applications
     that require a restart of the operating system after installation require additional
     configuration. For more information, see Configure the Computer to Restart After
     Application Installation.

Defining Operating System Components and Settings
As part of establishing a standardized configuration, determine which operating system
components to include and the settings for these components. This determination
includes optional components in all operating systems, server roles in Windows Server
operating systems, and components to include in Windows Preinstallation Environment
(Windows PE). For example, you may decide to remove unnecessary Windows operating
system components from desktop and portable computer deployments to reduce the
security footprint of those computers.

For each operating system image, determine the:

     **Operating system components.**Select the components required for the
     applications and user roles performed on the target computers. Install only the
     components that are required to help reduce the attack surface of the target
     computer and the image size.

<!-- p.26 -->

     Server roles. Select the server roles required for the server computers. Install only
     the server roles that are required to help reduce the attack surface of the target
     computer and the image size.

     Windows PE components. These components include Microsoft ActiveX® Data
     Objects (ADO) support, fonts, and the necessary drivers and packages. You can
     select the components for 32-bit and 64-bit versions of Windows PE.

     Configuration settings. Identify the configuration settings for components
     included in the images. Select configuration settings that meet the business and
     security requirements of the organization. For more information about target
     computer security, see Planning Target Computer Security.

Choosing a Deployment Method
Typically, target computers have high-speed, persistent connections to the deployment
infrastructure. However, some target computers may connect to an intranet remotely or
not at all. MDT includes the following methods for deploying operating systems and
applications using LTI based on the network connectivity:

     Deployment share. This method uses a network shared folder in which all the
     deployment files reside. The target computer starts Windows PE, and then
     connects to the deployment share to perform the deployment. Select this method
     when the target computers have high-speed, persistent connections to the
     deployment infrastructure.

     Media. This method creates an image that you can use to perform deployments
     from removable media, such as DVDs or USB flash drives (UFDs). You use Windows
     PE to start the computer from the media. Select this method when the target
     computers may be remotely connected or may not have connectivity at all.

Evaluating Network Requirements
Because of the size of the images being distributed to the target computers (500
megabytes [MB] to 4 GB), computers must have a high-speed, persistent connection to
the servers used in the deployment process. These servers need to be on adjacent
subnets to the target computers to ensure high-speed connectivity to the computers.

  ７ Note

  Network-based deployments using MDT are not supported for wireless networks.
  Use media-based deployments for computers connected by wireless networks or

<!-- p.27 -->

  networks with slow or unreliable connectivity.

If the organization cannot provide sufficient network capacity to deploy images,
software, and migration data to computers, perform one of the following actions:

     Temporarily place the appropriate servers (for example, servers hosting the various
     shared folders or the server running Windows Deployment Services) closer to the
     target computers for the duration of the migration.

     Temporarily move the target computers to a staging area where the computers can
     be deployed, and then return them to their original location.

     Store user state migration data locally on the target computers.

     Perform automated deployments locally using media deployments in LTI.

     In addition to network capacity, you must enable the appropriate network
     protocols and traffic. For example, if you want to initiate LTI, ZTI, or UDI
     deployment using Windows Deployment Services and multicast deployment, you
     must enable multicast traffic between the MDT infrastructure and target
     computers.

Using Reference Computers in MDT Deployments
The MDT deployment process uses the reference computer as a baseline for the
configuration of target computers when the deployment process is complete. You
configure the reference computer to comply with the business, technical, and security
requirements of the organization. After configuring the reference computer, capture an
image of the reference computer that you can then deploy to the target computers.

Only in rare circumstances will you be able to deploy the images from the Windows
distribution media unmodified to the reference and target computers. Instead, create
customized images that include the Windows operating system, language, packs,
applications, device drivers, software updates, and other software.

The MDT deployment process allows for the creation of customized images that are first
deployed to a reference computer, then captured from the reference computer, and
finally deployed to target computers. MDT manages the customization of images so that
you can create them with less effort and higher levels of automation. For example, the
Deployment Workbench in MDT can automatically inject the appropriate device drivers
into images.

<!-- p.28 -->

VMs work well when creating a reference image for Windows because the historical HAL
issues are no longer applicable.

  ７ Note

  VMs typically do not have the same performance as physical computers, so
  creating the reference images may take longer.

Choosing Thick, Thin, or Hybrid Images
As part of the planning process, determine the types of images that you will create. The
types of images you can create fall into these categories:

     Thick images. Thick images are monolithic images that contain core applications,
     language packs, and other files. Part of the image-development process is
     installing core applications and language packs on the reference computer before
     capturing the disk image.

     Thin images. Thin images contain few if any core applications or language packs,
     as these components are installed separately from the disk image, which typically
     takes more network transfer time at the computer.

     Hybrid images. Hybrid images mix thin and thick image strategies by installing
     applications and language packs from a network shared folder. Hybrid images
     have most of the advantages of thin images, but they are not as complex to
     develop and do not require a software-distribution infrastructure. They do require
     longer installation times, however, which can raise initial deployment costs.

Table 4 lists the advantages and disadvantages of the thick, thin, and hybrid images
types.

Table 4. Advantages and Disadvantages of Thick, Thin, and Hybrid
Images

                                                                              ﾉ   Expand table

 Method    Advantage                             Disadvantage

 Thick     - Can be simpler to deploy, because   - Requires more storage for each image.
           all applications and language packs
           are in the image.                     - Requires more time to download over network
                                                 connections than thin or hybrid images.

<!-- p.29 -->

 Method      Advantage                              Disadvantage

             - Reduced initial complexity,
             because advanced scripting is not      - Requires an increased image maintenance
             typically required.                    effort, because any updates to operating
                                                    systems, device drivers, applications, or
             - Applications and language packs      language packs requires the creation of a new
             are available immediately after        image.
             deployment is complete.

             - Does not require software-
             distribution software, such as the
             Application Management feature in
             Configuration Manager.

 Thin        - Requires less storage for each       - Can be more complex to createinitially,
             image.                                 because additional steps are required during
                                                    image creation.
             - Requires less time than thick
             images to download over network        - Potential for increased complexity, because
             connections.                           advanced scripting may be required.

             -Reduced image maintenance             - Applications and languages are not
             effort, because the image contains     immediately available after image deployment
             fewer components.                      is complete.

 Hybrid      - Requires less storage than thick     - Can be more complex than a thick image (but
             images for each image.                 not than a thin image) to create, because
                                                    additional steps are required during image
             - Requires less time to than thick a   creation.
             thick image to download over
             network connections.                   - Potential for increased complexity, because
                                                    advanced scripting (though not as advanced as
             - Reduced image maintenance            in thin images) may be required.
             effort, because the image contains
             fewer components.                      - pplications and languages are not immediately
                                                    available after image deployment is complete.
             - Does not require separate
             software-distribution software.

The costs associated with building, maintaining, and deploying disk images includes:

        Development costs. Development costs include creating a well-engineered image
        to lower future support costs and improve security and reliability. Higher levels of
        automation reduce development costs.

        Test costs. These costs include the time and labor involved in testing the standard
        image and the applications that might reside inside it in addition to applications

<!-- p.30 -->

       applied after deployment. Test costs also include the development time required to
       stabilize disk images.

       Storage costs. Storage costs include storing the distribution points, disk images,
       migration data, and backup images. Storage costs can be significant depending on
       the number of disk images, the number of computers in each deployment run, and
       so on.

       Network costs. Network costs include moving disk images to distribution points
       and to computers. The disk-imaging technologies that Microsoft provides do not
       support multicasting, so network costs scale linearly with the number of
       distribution points you must replicate and the number of computers in the
       deployment project.

       As the size of image files increases, costs increase. Large images have more
       updating, testing, distribution, network, and storage costs associated with them.
       Even if only a small portion of the image is updated, the entire image must be
       redistributed.

Identifying Deployment Scenarios
Table 5 lists the deployment scenarios and provides a brief description of each.

Table 5. Deployment Scenarios

                                                                                    ﾉ   Expand table

 Scenario       Description                                 Migrates     Uses             Preserves
                                                            user state   existing         file system
                                                                         target
                                                                         computer

 New            A new installation of a Windows operating   No           No               No
 Computer       system is deployed to a new computer.

 Refresh        A computer is refreshed, including          Yes          Yes              No
 Computer       computers that must be re-imaged for
                image standardization or to address a
                problem.

 Replace        One computer replaces another computer.     Yes          No               No
 Computer       The existing user state migration data is
                saved from the original computer. Then, a
                new installation of Windows is deployed

<!-- p.31 -->

 Scenario    Description                                  Migrates     Uses       Preserves
                                                          user state   existing   file system
                                                                       target
                                                                       computer

             to a new computer. Finally, the user state
             data is restored to the new computer.

MDT does not support in-place upgrade deployments. You can perform:

     An in-place upgrade manually by running Setup.exe from the original Windows
     media

       ７ Note

       To perform an in-place upgrade manually by running Setup.exe from the
       original Windows media, use the original install.wim file. Custom .wim files are
       not supported for in-place upgrades.

     The Refresh Computer scenario as an alternative for deploying a new operating
     system and applications on the target computer

     As part of the Replace Computer deployment scenario, wipe the disk partitions of
     the original computer. The standard format as performed by Windows operating
     systems does not perform a secure wipe of the disk as defined by U.S. Department
     of Defense standard 5520.22M. If required, perform secure wipes of hard disks in
     target computers using tools provided by non-Microsoft vendors.

Planning for BitLocker Drive Encryption
BitLocker is included in Windows so include planning decisions for BitLocker in your
environment. One BitLocker decision you must make is the storage of the recovery keys.
You can store BitLocker recovery keys in:

     A local folder. Select this option to store the recovery key on UFDs, which each

     user manages.

     A network folder. Select this option to centrally store the recovery keys in a
     network shared folder, which network administrators manage.

     Active Directory® Domain Services (AD DS). Select this option to store the
     recovery keys in AD DS, which Active Directory administrators manage.

<!-- p.32 -->

      Also, elect the methods users will employ to start their computers after BitLocker is
      enabled. Users can start their computers using one of the following methods:

      Trusted Platform Module (TPM) version 1.2 or later. TPM is a cryptographic
      hardware chip installed on the target computer. If the target computer does not
      support TPM, a UFD or PIN must be used to start the computer. This is the
      preferred method if the target computer supports TPM.

           ７ Note

           You can provide a PIN that users can enter in conjunction with TPM, or you
           can use a UFD to strengthen the security when starting a computer.

      UFD. In this method, the required encryption keys are stored on a UFD, which must
      be present in the computer when the computer starts. This is the preferred method
      if the target computer does not support TPM.

      For more information on BitLocker, see BitLocker Drive Encryption Overview.

Evaluating Target Computer Readiness
As part of the planning process, evaluate target computer readiness for the deployment
of the target operating system, device drivers, applications, and other components.
Evaluate target computer readiness using automated hardware and software inventory
tools, such as Configuration Manager or the Microsoft Assessment and Planning (MAP)
Toolkit.

Evaluate target computer readiness for deployment by:

      Verifying target computer readiness for running the MDT scripts as described in
      Verify Target Computer Readiness for Running MDT Scripts

      Verifying that target computers have adequate software and hardware system
      resources as described in Verify Adequate Target Computer Resources

      Identifying the differences in the deployment process between 32-bit and 64-bit
      computers as described in Identify Differences in 64-bit and 32-bit Deployments

Verify Target Computer Readiness for Running MDT
Scripts

<!-- p.33 -->

Before running the rest of the MDT scripts, run ZTIPrereq.vbs to ensure that the target
computer meets the requirements for running the remaining MDT scripts. Script
prerequisites include:

     Windows Script Host (WSH) version 5.6 or later installed and running

     Microsoft XML Core Services (MSXML) version 3.0 (any service pack level) installed
     and running

        ７ Note

        The version of MSXML must be version 3.0. MSXML versions 4.0 and 6.0 are
        not compatible with the MDT scripts.

Verify Adequate Target Computer Resources
After ZTIPrereq.vbs determines that the computer meets the requirements for running
the remaining scripts, ZTIValidate.wsf determines whether the target computer has the
appropriate software and hardware system resources to deploy the target operating
system. These requirements include:

     The target computer has WSH 5.6 or later installed

     In any scenario except New Computer (which does not migrate user data), the
     existing operating system must be a client operating system if the new operating
     system is a client operating system. Similarly, only a server operating system can
     be deployed to a computer currently running a server operating system.

     The OSInstall property, if defined, must be set to YES for the deployment to
     continue

     The target computer memory must meet the requirements of the operating system

        ７ Note

        The minimum recommended amount of physical memory for the target
        computer is 1 GB.

     The target computer processor must meet the requirements of the operating
     system

<!-- p.34 -->

     The target computer must have sufficient available disk space for the image being
     deployed to it

     The current operating system on the target computer must be running on the C
     partition (Refresh Computer scenario only)

     Drive C must be the first partition on the first disk of the target computer (Refresh
     Computer scenario only)

     Additional available disk space is required when user state migration data and
     deployment logs are stored locally on the target computer

     The target computer must have sufficient free disk space (approximately 150 MB)
     to hold Windows PE log files

     The target computer must have sufficient total disk space to hold Windows PE and
     the image (expanded image size plus 150 MB)

     The target computer must have a direct network connection to Windows
     Deployment Services servers and deployment shares (Unsupported network
     connections include virtual private network [VPN] and wireless connections.)

       ７ Note

       Target computers that attempt to install an image over a VPN or wireless
       connection will not be able to connect to a deployment share after restarting
       in Windows PE, causing the deployment process to fail.

     Determine whether any existing computers have inadequate system resources
     using Configuration Manager or another software inventory tool. Upgrade the
     system resources on these target computers prior to deploying Windows, if
     necessary.

Identify Differences in 64-bit and 32-bit Deployments
Most functions and features found in 32-bit versions of Windows are the same in 64-bit
versions of Windows. However, take the following differences into consideration when
deploying 64-bit versions of Windows:

     For LTI deployments, the version of Windows PE must match the version of
     Windows being deployed. If deploying a 64-bit version of Windows, use a 64-bit
     version of Windows PE.

<!-- p.35 -->

     Applications are installed in separate Program Files folders. On 64-bit versions of
     Windows, 64-bit applications are installed in the Program Files folder, and 32-bit
     applications are installed in the Program Files (x86) folder. Check the appropriate
     folder structure when looking for previously installed applications.

     Processor architecture discovery in Windows Deployment Services may need to be
     forced for 64-bit computers. Not all 64-bit computers properly report the
     processor type; therefore, MDT may not properly detect that the processor is a 64-
     bit processor. Use the following command to force Windows Deployment Services
     to deploy 64-bit versions:

       Windows Command Prompt

       WDSUTIL /set-server /architecturediscovery:yes

     For more information, see the Windows Deployment Services Help files.

     64-bit versions of Windows PE do not run 32-bit applications. Ensure that any
     compiled applications used by a 64-bit version of Windows PE are 64-bit versions.

     64-bit versions of Windows require 64-bit device drivers. You cannot use 32-bit
     device drivers in 64-bit versions of Windows.

Planning Performance and Power Management
Windows includes a number of features that help improve the performance and power
utilization of computers. You can incorporate these improvements as part of the
configuration settings you deploy to the target computers using MDT.

Review the following resources to identify performance and power-management
configuration settings to include when performing your target computer deployments:

     Windows Performance Analysis Tools

     Sustainable Computing: Enforce Power Management Settings in your Organization
     with Group Policy

     Mobile Battery Life Solutions for Windows 7

     Power Policy Configuration and Deployment in Windows

Planning Target Computer Security

<!-- p.36 -->

When planning the configuration of the Windows operating systems for target
computers, ensure that the target computers are deployed in compliance with the
requirements in your organization. Microsoft has developed Security Solution
Accelerators that can help you deploy your target computers in a secured configuration.

The Security Solution Accelerators include guidance and tools to help you secure
Windows. For more information about deploying target computers in a secured
configuration using these solution accelerators, see Security Solution Accelerators.

Choosing LTI, ZTI, or UDI Deployments
LTI, ZTI, and UDI deployments use the same common set of scripts and configuration
files (such as CustomSettings.ini) for deploying target computers. Table 6 compares LTI,
ZTI, and UDI deployments.

Table 6. Comparison of LTI, ZTI, and UDI Deployments

                                                                                  ﾉ   Expand table

 LTI deployment                  ZTI deployment                    UDI deployment

 Allows selection of the level   Supports only fully automated     Allows selection of the level of
 of automation                   deployments                       automation

 Has minimal infrastructure      Requires Configuration            Requires Configuration
 requirements                    Manager                           Manager

 Supports deployments over       Supports deployments over a       Supports deployments over a
 a network using a shared        network using Configuration       network using Configuration
 folder or locally using         Manager distribution points or    Manager distribution points or
 removable storage such as a     locally using removable storage   locally using removable storage
 CD, DVD, or UFD                 such as a CD, DVD, or UFD         such as a CD, DVD, or UFD

 The deployment process          The installation process can be   The installation process can be
 can be initiated manually or    initiated by Configuration        initiated by Configuration
 automatically using             Manager, or Windows               Manager, or Windows
 Windows Deployment              Deployment Services               Deployment Services
 Services

 The deployment process is       The deployment process is         The deployment process is
 configured using the            configured using the              configured using the
 Deployment Workbench            Configuration Manager console     Configuration Manager console
                                                                   and the UDI Wizard Designer.

 Can require less initial IT     Requires more initial IT          Requires more initial IT
 administration configuration    administration configuration      administration configuration

<!-- p.37 -->

LTI deployment                  ZTI deployment                    UDI deployment

time                            time                              time

Can require interaction by      Requires no interaction by the    Can require interaction by the
the user or deployment          user or deployment technician     user or deployment technician
technician

Increases the risk of           Reduces the risk of introducing   Increases the risk of introducing
introducing configuration       configuration errors              configuration errors
errors

Requires users or               Users and deployment              Requires users or deployment
deployment technicians to       technicians are not required to   technicians to have credentials
have credentials with           have credentials with elevated    with elevated permissions
elevated permissions            permissions

Requires that users or          Users and deployment              Requires that users or
deployment technicians          technicians do not need to        deployment technicians know
know some configuration         know configuration settings       some configuration settings
settings prior to initiating    prior to initiating the MDT       prior to initiating the MDT
the MDT deployment              deployment process                deployment process
process

Can be used with slow           Requires a high-speed,            Requires a high-speed,
connections or in instances     persistent connection             persistent connection
where no network
connectivity exists

Requires little or no           Requires an infrastructure        Requires an infrastructure
infrastructure to support       sufficient to deploy operating    sufficient to deploy operating
deployment                      system images                     system images

Supports deployment over        Supports deployment over the      Supports deployment over the
the network or local to the     network or local to the           network or local to the
computer from media             computer from media               computer from media

Does not require                Requires that target computers    Requires that target computers
management of target            be managed using                  be managed using
computers using                 Configuration Manager             Configuration Manager
Configuration Manager

Supports security policies in   Supports only security in which   Supports only security in which
which automatic software        automatic software installation   automatic software installation
installation is prohibited      is allowed.                       is allowed.

Supports deployment to          Requires remote procedure call    Requires RPC communication
target computers isolated       (RPC) communication with          with target computers
by firewalls                    target computers

<!-- p.38 -->

At some point in the MDT process, you must provide all the information necessary to
install Windows and the applications on target computers. The question is, when do you
provide this information? The more information you provide in advance, the less
interaction is required during deployment.

Table 7 lists the advantages and disadvantages of performing fully automated
deployments (using LTI, ZTI, or UDI) and partially automated deployments (using LTI or
UDI).

Table 7. Advantages and Disadvantages of Fully and Partially
Automated Deployments

                                                                                   ﾉ    Expand table

 Method      Advantages                                   Disadvantages

 Fully       - No interaction with the user or            - More time is needed to provide
             deployment technician is required.           configuration information required for
                                                          fully automated deployment.
             - The risk of introducing configuration
             errors is decreased.                         - Credentials to access network resources
                                                          and that have elevated permissions are
             - Users or deployment technicians do not     stored in configuration files that must be
             need to know any configuration               protected.
             information prior to initiating the MDT
             deployment process.

 Partially   - Less time is required to prepare for       - Interaction with the user or deployment
             deployment, because configuration            technician is required.
             information can be provided interactively.
                                                          - The risk of introducing configuration
                                                          errors is increased.

                                                          - Users or deployment technicians must
                                                          have credentials that require elevated
                                                          permissions.

                                                          - Users or deployment technicians must
                                                          know some configuration information
                                                          prior to initiating the MDT deployment
                                                          process.

Reviewing Known Issues, Limitations, and
Recommendations for MDT

<!-- p.39 -->

Review the know issues, limitations, and recommendations for:

     General issues in MDT as described in Review General Known Issues, Limitations,
     and Recommendations for MDT

     Windows as described in Review Known Issues, Limitations, and Recommendations
     That Relate to Windows

     Disks and partitioning as described in Review Known Issues, Limitations, and
     Recommendations That Relate to Disks and Partitioning

     BitLocker as described in Review Known Issues, Limitations, and Recommendations
     That Relate to BitLocker

     LTI deployments as described in Review Known Issues, Limitations, and
     Recommendations for LTI Deployments

     ZTI deployments using Configuration Manager as described in Review Known
     Issues, Limitations, and Recommendations for ZTI Deployments Using
     Configuration Manager

     UDI deployments as described in Review Known Issues, Limitations, and
     Recommendations for UDI Deployments

     Running task sequences on target computers as described in Review Known Issues,
     Limitations, and Recommendations for Running Task Sequences on Target
     Computers

     Saving and restoring user information as described in Review Known Issues,
     Limitations, and Recommendations for Saving and Restoring User Information

Review General Known Issues, Limitations, and Recommendations
for MDT
The following are a list of known general issues, limitations, and recommendations that
relate to MDT:

     MDT supports the Windows Assessment and Deployment Kit (Windows ADK) for
     Windows 8.1, Windows PE version 5.0, System Center 2012 R2 Configuration
     Manager.

     Language packs, applications, and device drivers that are disabled in the
     Deployment Workbench are not installed, unless you add them manually to the
     CustomSettings.ini file.

<!-- p.40 -->

When you select the Install Language Pack Offline action, you must select
language pack CAB files within subfolders of the main package.

When you specify IP addresses (for example, when identifying Domain Name
System [DNS] and Windows Internet Naming Service [WINS] servers), they must
exclude unnecessary zero prefixes, which will be misevaluated. For example, if the
IP address is typed 10.010.10.1, the Deployment Workbench evaluates it as 10.8.10.1.
To avoid this problem, enter IP addresses carefully, and do not add unnecessary
zeroes.

When specifying a Run As account, you must specify a user who is a member of
the Administrators group on the server. Otherwise, the account will not have
sufficient privileges to access network connections established by administrators.

When creating deployment shares on computers that have 8.3 file names disabled
(see the Microsoft Support article How to Disable the 8.3 Name Creation on NTFS
Partitions   ), the Deployment Workbench fails to generate the Windows PE image.
If 8.3 file names have been disabled, re-enable them by setting the
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem\NtfsDis
able8dot3NameCreation registry value to 0.

Within a folder, avoid creating a subfolder and a file with the same name. For
example, within the Files folder, you should not name a subfolder Item, and then
create a file named Item.

When performing an upgrade, network and media deployment shares created in
earlier versions of MDT must have valid shares.

If custom images captured by directly running ImageX (without using MDT to
capture the image) do not work properly, troubleshoot the issues by capturing and
adding the image using MDT to ensure that all prerequisites are configured
properly. Add Setup files to the Deployment Workbench by adding a complete
operating system distribution or by pointing the Deployment Wizard to the
location of source files. When manually capturing images, use the Wimscript.ini file
that MDT supplies in the \Distribution\tools\_platform folder, where platform is
either x86 (for 32-bit) or x64 (for 64-bit), to exclude the folders or files from the
image. Also be aware of preexisting Unattend.xml files in the image. Specify the
correct /FLAGS value when capturing Windows images using ImageX or Windows
Deployment Services capture processes.

At the completion of MDT deployment, a summary page displays warnings about
errors encountered during the process. (This page is not displayed when
conducting the Server Core installation because it does not include the required
