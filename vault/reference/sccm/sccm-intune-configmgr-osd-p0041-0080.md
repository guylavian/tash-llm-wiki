---
title: "OS deployment documentation — pages 41-80"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0041-0080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0041-0080
family: sccm
documentKind: "doc"
abstract: "After saving the file, move it to a location for a Microsoft Configuration Manager package source. ） Important The configuration file can only contain one profile. Multiple JSON profile files can be used, but each one must be named AutopilotConfigurationFile.json . This requirem"
---

# OS deployment documentation — pages 41-80

<!-- p.41 -->

After saving the file, move it to a location for a Microsoft Configuration Manager package source.

  ） Important

  The configuration file can only contain one profile. Multiple JSON profile files can be used, but each one must be named
  AutopilotConfigurationFile.json . This requirement is for OOBE to follow the Windows Autopilot experience. To use more than one

  Windows Autopilot profile, create separate Configuration Manager packages.

  Windows OOBE doesn't follow the Windows Autopilot experience if the file is saved with one of the following criteria:

       Unicode encoding.
       UTF-8 encoding.
       A file name other than AutopilotConfigurationFile.json .

Create a package containing the JSON file
   1. In the Configuration Manager console, go to the Software Library workspace, expand Application Management, and select the
     Packages node.

   2. On the ribbon, select Create Package.

   3. In the Create Package and Program Wizard, enter the following details for the package:

           Name: Windows Autopilot for existing devices config
           Select This package contains source files
           Source folder: Specify the UNC network path that contains the AutopilotConfigurationFile.json file

     For more information, see Packages and programs in Configuration Manager.

   4. For the program, select the Program Type: Don't create a program

   5. Complete the wizard.

  ７ Note

  If the user-driven Windows Autopilot profile settings in Intune are changed at a later date, make sure to recreate and update the
  JSON file. After updating the JSON file, redistribute the associated Configuration Manager package.

Create a target collection

<!-- p.42 -->

  1. In the Configuration Manager console, go to the Assets and Compliance workspace, and select the Device Collections node.

  2. On the ribbon, select Create, and then select Create Device Collection. An existing collection can also be used. If using an existing
     collection, proceed to the Create a task sequence section.

  3. In the Create Device Collection Wizard, enter the following General details:

          Name: Windows Autopilot for existing devices collection
          Comment: Add an optional comment to further describe the collection
          Limiting collection: All Systems or if desired, an alternate collection.

  4. On the Membership Rules page, select Add Rule. Specify either a direct or query-based collection rule to add the target Windows
     devices to the new collection.

     For example, if the hostname of the computer to be wiped and reloaded is PC-01 , and Name is being used as the attribute:

     a. Select Add Rule, select Direct Rule to open the Create Direct Membership Rule Wizard, and select Next on the Welcome page.

     b. On the Search for Resources page, enter PC-01 as the Value.

     c. Select Next, and select PC-01 in the Resources.

  5. Complete the wizard with the default settings.

For more information, see How to create collections in Configuration Manager.

Create a task sequence
  1. In the Configuration Manager console, go to the Software Library workspace, expand Operating Systems and select the Task
     Sequences node.

  2. In the Home ribbon, select Create Task Sequence.

  3. In the Create new task sequence page, select the option to Deploy Windows Autopilot for existing devices.

  4. In the Task sequence information page, specify the following information:

          A name for the task sequence. For example, Windows Autopilot for existing devices.
          Optionally add a description to better describe the task sequence.
          Select a boot image. For more information on supported boot image versions, see Support for the Windows ADK in
          Configuration Manager.

  5. In the Install Windows page, select the Windows Image package. Then configure the following settings:

          Image index: Select either Enterprise, Education, or Professional, as required by the organization.

          Enable the option to Partition and format the target computer before installing the operating system.

          Configure task sequence for use with Bitlocker: If this option is enabled, the task sequence includes the steps necessary to
          enable BitLocker.

          Product key: If a product key needs to be specified for Windows activation, enter it here.

          Select one of the following options to configure the local administrator account in Windows:
             Randomly generate the local administrator password and disable the account on all support platforms (recommended)
             Enable the account and specify the local administrator password

  6. In the Install the Configuration Manager client page, add any necessary Configuration Manager client installation properties for the
     environment. For example, since the device is a Workgroup device and not domain joined during the Windows Autopilot for existing
     devices task sequence, the SMSMP or SMSMPLIST parameters might be needed to run certain tasks such as the Install Application
     or Install Software Updates tasks.

  7. The Include updates page selects by default the option to Do not install any software updates.

  8. In the Install applications page, applications to install during the task sequence can be selected. However, Microsoft recommends
     that to mirror the signature image approach with this scenario. After the device provisions with Windows Autopilot, apply all

<!-- p.43 -->

     applications and configurations from Microsoft Intune or Configuration Manager co-management. This process provides a
     consistent experience between users receiving new devices and those using Windows Autopilot for existing devices.

   9. In the System Preparation page, select the package that includes the Windows Autopilot configuration file. By default, the task
     sequence restarts the computer after it runs Windows Sysprep. The option to Shutdown computer after this task sequence
     completes can also be selected. This option allows preparation of a device and then delivery to a user for a consistent Windows
     Autopilot experience.

 10. Complete the wizard.

The Windows Autopilot for existing devices task sequence results in a device joined to Microsoft Entra ID.

  ７ Note

  For Windows Autopilot for existing devices task sequence, the Create Task Sequence Wizard purposely skips configuring and adding
  the Apply Network Settings task. If the Apply Network Settings task isn't specified in a task sequence, it uses Windows default
  behavior, which is to join a workgroup.

  The Windows Autopilot for existing devices task sequence runs the Prepare Windows for capture step, which uses the Windows
  System Preparation Tool (Sysprep). If the device is joined to a domain, Sysprep fails, so therefore the Windows Autopilot for existing
  devices task sequence joins a workgroup. For this reason, it isn't necessary to add the Apply Network Settings task to a Windows
  Autopilot for existing devices task sequence.

For more information on creating the task sequence, including information on other wizard options, see Create a task sequence to install
an OS.

If the task sequence is viewed, it's similar to the default task sequence to apply an existing OS image. This task sequence includes the
following extra steps:

     Apply Windows Autopilot configuration: This step applies the Windows Autopilot configuration file from the specified package. It's
     not a new type of step, it's a Run Command Line step to copy the file.

     Prepare Windows for Capture: This step runs Windows Sysprep, and has the setting to Shutdown the computer after running this
     action. For more information, see Prepare Windows for Capture.

For more information on editing the task sequence, see Use the task sequence editor and Task sequence steps.

  ７ Note

  The Prepare Windows for Capture step deletes the AutopilotConfigurationFile.json file. For more information and a workaround,
  see Modify the task sequence to account for Sysprep command line configuration and Windows Autopilot - known issues:
  Windows Autopilot for existing devices doesn't work.

To make sure the user's data is backed up before the Windows upgrade, use OneDrive for work or school known folder move.

Distribute content to distribution points
Next distribute all content required for the task sequence to distribution points.

   1. Select the Windows Autopilot for existing devices task sequence, and in the ribbon select Distribute Content.

   2. On the Specify the content destination page, select Add to specify either a Distribution Point or Distribution Point Group.

   3. Specify content destinations that let the devices get the content.

   4. After specifying content distribution, complete the wizard.

For more information, see Manage task sequences to automate tasks.

Deploy the Windows Autopilot task sequence

<!-- p.44 -->

  1. Select the Windows Autopilot for existing devices task sequence, and in the ribbon select Deploy.

  2. In the Deploy Software Wizard, specify the following details:

           General

             Task Sequence: Windows Autopilot for existing devices

             Collection: Windows Autopilot for existing devices collection

           Deployment Settings

             Action: Install.

             Purpose: Available.

             Make available to the following: Only Configuration Manager Clients.

                ７ Note

                Select the option here that is relevant for the context of testing. If the target client doesn't have the Configuration
                Manager agent or Windows installed, the task sequence needs to be started via PXE or Boot Media.

           Scheduling
             Set a time for when this deployment becomes available

           User Experience
             Select Show Task Sequence progress

           Distribution Points
             Deployment options: Download content locally when needed by the running task sequence

  3. Complete the wizard.

Complete the deployment process
  1. On the target Windows device, go to the Start menu, enter Software Center , and open it.

  2. In the Software Library, under Operating Systems, select Windows Autopilot for existing devices, and then select Install.

The task sequence runs and does the following actions:

  1. Downloads content.

  2. Restarts the device into WinPE.

  3. Formats the drive.

  4. Installs Windows from the specified OS image.

  5. Prepares for Windows Autopilot.

  6. After the task sequence completes, the device boots into OOBE for the Windows Autopilot experience:

  ７ Note

  If devices need to be joined to Active Directory as part of a Microsoft Entra hybrid join scenario, don't do so through the task
  sequence and the Apply Network Settings Task. Instead, create a Domain Join device configuration profile. Since there's no
  Microsoft Entra device object for the computer to do group-based targeting, target the profile to All Devices. For more information,
  see User-driven mode for Microsoft Entra hybrid join.

Register the device for Windows Autopilot

<!-- p.45 -->

Devices provisioned with Windows Autopilot only receive the guided OOBE Windows Autopilot experience on first boot.

After Windows is updated on an existing device, make sure to register the device so it has the Windows Autopilot experience when the PC
resets. Automatic registration can be enabled for a device by using the Convert all targeted devices to Autopilot setting in the Windows
Autopilot profile that is assigned to a group that the device is a member of. For more information, see Create a Windows Autopilot
deployment profile.

Also see Adding devices to Windows Autopilot.

  ７ Note

        Typically, the target device isn't registered with the Windows Autopilot service. If the device is already registered, the assigned
        profile takes precedence. The Windows Autopilot for existing devices profile only applies if the online profile times out.

        When the assigned profile is applied, the enrollmentProfileName property of the device object in Microsoft Intune and
        Microsoft Entra ID match the Windows Autopilot profile name.

        When the Windows Autopilot for existing devices profile is applied, the enrollmentProfileName property of the device object in
        Microsoft Intune and Microsoft Entra ID are OffilineAutoPilotProfile-<ZtdCorrelationId>.

How to speed up the deployment process
To speed up the deployment process, see Windows Autopilot deployment for existing devices: Speed up the deployment process section
of the Windows Autopilot Tutorial.

Tutorial
For a detailed tutorial on configuring Windows Autopilot for existing devices, see the following article:

Step by step tutorial for Windows Autopilot deployment for existing devices in Intune and Configuration Manager

Related content
     New Windows Autopilot capabilities and expanded partner support simplify modern device deployment              .

<!-- p.46 -->

Refresh an existing computer with a
new version of Windows
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use Configuration Manager to partition and format an existing computer and then
install a new OS. This process is sometimes called reimaging or wipe and load. For this
scenario, choose from many different deployment methods, such as PXE, bootable
media, or Software Center. You can also use a state migration point to store settings,
and then restore them to the new OS.

To choose the right OS deployment scenario, see Scenarios to deploy enterprise
operating systems.

Plan

Plan for and implement infrastructure requirements
There are several infrastructure requirements that must be in place before you can
deploy an OS. Some of these requirements include the Windows ADK, the User State
Migration Tool (USMT), and Windows Deployment Services (WDS). For more
information, see Infrastructure requirements for OS deployment.

Install a state migration point
If you want to capture settings from an existing computer, and then restore the settings
to the new OS, consider using a state migration point. For more information, see State
migration point.

Configure

Prepare a boot image
Boot images start a computer in a Windows PE environment. Windows PE is a minimal
OS with limited components and services. From Windows PE, Configuration Manager
can then install a full Windows OS on the computer.

<!-- p.47 -->

For more information, see the following articles:

     Manage boot images

     Customize boot images

     Distribute content

Prepare an OS image
The OS image contains the files necessary to install the OS on the destination computer.

For more information, see the following articles:

     Manage OS images

     Distribute content

Create a task sequence to deploy an OS
Use a task sequence to automate the installation of the OS. Depending on the
deployment method that you choose, there might be additional considerations for the
task sequence.

For more information, see the following articles:

     Create a task sequence to install an OS

     Manage user state

Deploy
     Use one of the following deployment methods to deploy the OS:

        Use PXE to deploy Windows over the network

        Use multicast to deploy Windows over the network

        Create an image for an OEM in factory or a local depot

        Use stand-alone media to deploy Windows without using the network

        Use bootable media to deploy Windows over the network

        Use Software Center to deploy Windows over the network

<!-- p.48 -->

Monitor
For more information, see Monitor OS deployments.

  ７ Note

  When you reimage a UEFI device, Windows Boot Manager creates a new entry in
  the boot loader. This behavior is most noticeable when you repeatedly reimage a
  device, such as in a test environment or a student lab. It generally doesn't impact
  the performance or usage of the device. If the list gets too large, some specific
  hardware devices may encounter functional issues. For example, not booting to an
  external USB drive, or not able to select the current boot entry from the list. Use the
  Windows bcdedit command to clear unused boot entries. For more information,
  see BCDEdit /deletevalue.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.49 -->

Install a new version of Windows on a
new computer (bare metal) with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic provides the general steps in Configuration Manager to install an operating
system on a new computer. For this scenario, you can choose from many different
deployment methods, such as PXE, OEM, or stand-alone media. If you are unsure that
this is the right operating system deployment scenario for you, see Scenarios to deploy
enterprise operating systems.

Use the following sections to refresh an existing computer with a new version of
Windows.

Plan
      Plan for and implement infrastructure requirements

      There are several infrastructure requirements that must be in place before you can
      deploy operating systems, such as Windows ADK, Windows Deployment Services
      (WDS), supported hard disk configurations, etc. For more information, see
      Infrastructure requirements for operating system deployment.

Configure
   1. Prepare a boot image

      Boot images start a computer in a Windows PE environment (a minimal operating
      system with limited components and services) that can then install a full Windows
      operating system on the computer. When you deploy operating systems, you must
      select a boot image to use and distribute the image to a distribution point. Use the
      following to prepare the boot image:

            To learn more about boot images, see Manage boot images.

            For more information about how to customize a boot image, see Customize
            boot images.

<!-- p.50 -->

        Distribute the boot image to distribution points. For more information, see
        Distribute content.

 2. Prepare an operating system image

   The operating system image contains the files necessary to install the operating
   system on the destination computer. Use the following to prepare the operating
   system image:

        To learn more about how to create an operating system image, see Manage
        operating system images.

        Distribute the operating system image to distribution points. For more
        information, see Distribute content.

     ７ Note

     New installations of Windows can also be performed from installation source
     files via OS upgrade packages, but use OS images such as install.wim instead.

     Deploying new installations of Windows via OS upgrade packages is still
     supported, but is dependent on drivers being compatible with this method.
     When installing Windows from an OS upgrade package, drivers are installed
     while still in Windows PE versus simply being injected while in Windows PE.
     Some drivers are not compatible with being installed while in Windows PE. If
     drivers are not compatible with being installed while in Windows PE, then use
     an OS image instead.

 3. Create a task sequence to deploy operating systems over the network

   Use a task sequence to automate the installation of the operating system over the
   network. Use the steps in Create a task sequence to install an operating system to
   create the task sequence to deploy the operating system. Depending on the
   deployment method that you choose, there might be additional considerations for
   the task sequence.

Deploy
   Use one of the following deployment methods to deploy the operating system:

     Use PXE to deploy Windows over the network

     Use multicast to deploy Windows over the network

<!-- p.51 -->

        Create an image for an OEM in factory or a local depot

        Use stand-alone media to deploy Windows without using the network

        Use bootable media to deploy Windows over the network

Monitor
     Monitor the task sequence deployment

     To monitor the task sequence deployment to install the operating system, see
     Monitor operating system deployments.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.52 -->

Replace an existing computer and
transfer settings with Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic provides the general steps in Configuration Manager to replace an existing
computer with a new computer. For this scenario, you can choose from many different
deployment methods, such as bootable media, multicast, or Software Center. You can
also choose to install a state migration point to store settings and then restore them to
the new operating system after it is installed. If you are unsure that this is the right
operating system deployment scenario for you, see Scenarios to deploy enterprise
operating systems.

Use the following sections to refresh an existing computer with a new version of
Windows.

Plan
      Plan for and implement infrastructure requirements

      There are several infrastructure requirements that must be in place before you can
      deploy operating systems, such as Windows ADK, User State Migration Tool
      (USMT), Windows Deployment Services (WDS), supported hard disk configurations,
      etc. For more information, see Infrastructure requirements for operating system
      deployment

      Install a state migration point (required only if you transfer settings)

      When you are going to capture settings from the existing computer, and then
      restore the settings to the new operating system, you must install a state migration
      point. For more information, see State migration point.

Configure
   1. Prepare a boot image

      Boot images start a computer in a Windows PE environment (a minimal operating
      system with limited components and services) that can then install a full Windows

<!-- p.53 -->

   operating system on the computer. When you deploy operating systems, you must
   select a boot image to use and distribute the image to a distribution point. Use the
   following to prepare the boot image:

        To learn more about boot images, see Manage boot images.

        For more information about how to customize a boot image, see Customize
        boot images.

        Distribute the boot image to distribution points. For more information, see
        Distribute content.

 2. Prepare an operating system image

   The operating system image contains the files necessary to install the operating
   system on the destination computer. Use the following to prepare the operating
   system image:

        To learn more about how to create an operating system image, see Manage
        operating system images.

        Distribute the operating system image to distribution points. For more
        information, see Distribute content.

 3. Create a task sequence to deploy operating systems over the network

   Use a task sequence to automate the installation of the operating system over the
   network. Use the steps in Create a task sequence to install an operating system to
   create the task sequence to deploy the operating system. Depending on the
   deployment method that you choose, there might be additional considerations for
   the task sequence.

     ７ Note

     In this scenario, if you capture and restore user settings and files, you can
     choose to use a state migration point or save the files locally. For more
     information, see Manage user state.

Deploy
   Use one of the following deployment methods to deploy the operating system:

     Use Software Center to deploy Windows over the network

<!-- p.54 -->

        Use bootable media to deploy Windows over the network

        Use multicast to deploy Windows over the network

        Create an image for an OEM in factory or a local depot

Monitor
     Monitor the task sequence deployment

     To monitor the task sequence deployment to install the operating system, see
     Monitor operating system deployments.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.55 -->

Security and privacy for OS deployment
in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article contains security and privacy information for the OS deployment feature in
Configuration Manager.

Security best practices for OS deployment
Use the following security best practices for when you deploy operating systems with
Configuration Manager:

Implement access controls to protect bootable media
When you create bootable media, always assign a password to help secure the media.
Even with a password, it only encrypts files that contain sensitive information, and all
files can be overwritten.

Control physical access to the media to prevent an attacker from using cryptographic
attacks to obtain the client authentication certificate.

To help prevent a client from installing content or client policy that has been tampered
with, the content is hashed and must be used with the original policy. If the content
hash fails or the check that the content matches the policy, the client won't use the
bootable media. Only the content is hashed. The policy isn't hashed, but it's encrypted
and secured when you specify a password. This behavior makes it more difficult for an
attacker to successfully modify the policy.

Use a secure location when you create media for OS
images
If unauthorized users have access to the location, they can tamper with the files that you
create. They can also use all the available disk space so that the media creation fails.

Protect certificate files

<!-- p.56 -->

Protect certificate files (.pfx) with a strong password. If you store them on the network,
secure the network channel when you import them into Configuration Manager

When you require a password to import the client authentication certificate that you use
for bootable media, this configuration helps to protect the certificate from an attacker.

Use SMB signing or IPsec between the network location and the site server to prevent
an attacker from tampering with the certificate file.

Block or revoke any compromised certificates
If the client certificate is compromised, block the certificate from Configuration
Manager. If it's a PKI certificate, revoke it.

To deploy an OS by using bootable media and PXE boot, you must have a client
authentication certificate with a private key. If that certificate is compromised, block the
certificate in the Certificates node in the Administration workspace, Security node.

Secure the communication channel between the site
server and the SMS Provider
When the SMS Provider is remote from the site server, secure the communication
channel to protect boot images.

When you modify boot images and the SMS Provider is running on a server that isn't
the site server, the boot images are vulnerable to attack. Protect the network channel
between these computers by using SMB signing or IPsec.

Enable distribution points for PXE client communication
only on secure network segments
When a client sends a PXE boot request, you have no way to make sure that the request
is serviced by a valid PXE-enabled distribution point. This scenario has the following
security risks:

      A rogue distribution point that responds to PXE requests could provide a tampered
      image to clients.

      An attacker could launch a man-in-the-middle attack against the TFTP protocol
      that is used by PXE. This attack could send malicious code with the OS files. The
      attacker could also create a rogue client to make TFTP requests directly to the
      distribution point.

<!-- p.57 -->

     An attacker could use a malicious client to launch a denial of service attack against
     the distribution point.

Use defense in depth to protect the network segments where clients access PXE-
enabled distribution points.

  ２ Warning

  Because of these security risks, don't enable a distribution point for PXE
  communication when it's in an untrusted network, such as a perimeter network.

Configure PXE-enabled distribution points to respond to
PXE requests only on specified network interfaces
If you allow the distribution point to respond to PXE requests on all network interfaces,
this configuration might expose the PXE service to untrusted networks

Require a password to PXE boot
When you require a password for PXE boot, this configuration adds an extra level of
security to the PXE boot process. This configuration helps safeguard against rogue
clients joining the Configuration Manager hierarchy.

Restrict content in OS images used for PXE boot or
multicast
Don't include line-of-business applications or software that contains sensitive data in an
image that you use for PXE boot or multicast.

Because of the inherent security risks involved with PXE boot and multicast, reduce the
risks if a rogue computer downloads the OS image.

Restrict content installed by task sequence variables
Don't include line-of-business applications or software that contains sensitive data in
packages of applications that you install by using task sequences variables.

When you deploy software by using task sequences variables, it might be installed on
computers and to users who aren't authorized to receive that software.

<!-- p.58 -->

Secure the network channel when migrating user state
When you migrate user state, secure the network channel between the client and the
state migration point by using SMB signing or IPsec.

After the initial connection over HTTP, user state migration data is transferred by using
SMB. If you don't secure the network channel, an attacker can read and modify this data.

Use the latest version of USMT
Use the latest version of the User State Migration Tool (USMT) that Configuration
Manager supports.

The latest version of USMT provides security enhancements and greater control for
when you migrate user state data.

Manually delete folders on state migration points when
you decommission them
When you remove a state migration point folder in the Configuration Manager console
on the state migration point properties, the site doesn't delete the physical folder. To
protect the user state migration data from information disclosure, manually remove the
network share and delete the folder.

Don't configure the deletion policy to immediately delete
user state
If you configure the deletion policy on the state migration point to immediately remove
data that's marked for deletion, and if an attacker manages to retrieve the user state
data before the valid computer does, the site immediately deletes the user state data.
Set the Delete after interval to be long enough to verify the successful restore of user
state data.

Manually delete computer associations
Manually delete computer associations when the user state migration data restore is
complete and verified.

Configuration Manager doesn't automatically remove computer associations. Help to
protect the identity of user state data by manually deleting computer associations that
are no longer required.

<!-- p.59 -->

Manually back up the user state migration data on the
state migration point
Configuration Manager Backup doesn't include the user state migration data in the site
backup.

Implement access controls to protect the prestaged
media
Control physical access to the media to prevent an attacker from using cryptographic
attacks to obtain the client authentication certificate and sensitive data.

Implement access controls to protect the reference
computer imaging process
Make sure the reference computer you use to capture OS images is in a secure
environment. Use appropriate access controls so that unexpected or malicious software
can't be installed and inadvertently included in the captured image. When you capture
the image, make sure the destination network location is secure. This process helps
make sure the image can't be tampered with after you capture it.

Always install the most recent security updates on the
reference computer
When the reference computer has current security updates, it helps to reduce the
window of vulnerability for new computers when they first start up.

Implement access controls when deploying an OS to an
unknown computer
If you must deploy an OS to an unknown computer, implement access controls to
prevent unauthorized computers from connecting to the network.

Provisioning unknown computers provides a convenient method to deploy new
computers on demand. But it can also allow an attacker to efficiently become a trusted
client on your network. Restrict physical access to the network, and monitor clients to
detect unauthorized computers.

Computers responding to a PXE-initiated OS deployment might have all data destroyed
during the process. This behavior could result in a loss of availability of systems that are

<!-- p.60 -->

inadvertently reformatted.

Enable encryption for multicast packages
For every OS deployment package, you can enable encryption when Configuration
Manager transfers the package by using multicast. This configuration helps prevent
rogue computers from joining the multicast session. It also helps prevent attackers from
tampering with the transmission.

Monitor for unauthorized multicast-enabled distribution
points
If attackers can gain access to your network, they can configure rogue multicast servers
to spoof OS deployment.

When you export task sequences to a network location,
secure the location and secure the network channel
Restrict who can access the network folder.

Use SMB signing or IPsec between the network location and the site server to prevent
an attacker from tampering with the exported task sequence.

If you use the task sequence run as account, take
additional security precautions
If you use the task sequence run as account, take the following precautionary steps:

     Use an account with the least possible permissions.

     Don't use the network access account for this account.

     Never make the account a domain administrator.

     Never configure roaming profiles for this account. When the task sequence runs, it
     downloads the roaming profile for the account, which leaves the profile vulnerable
     to access on the local computer.

     Limit the scope of the account. For example, create different task sequence run as
     accounts for each task sequence. If one account is compromised, only the client
     computers to which that account has access are compromised. If the command
     line requires administrative access on the computer, consider creating a local

<!-- p.61 -->

      administrator account solely for the task sequence run as account. Create this local
      account on all computers that run the task sequence, and delete the account as
      soon as it's no longer required.

Restrict and monitor the administrative users who are
granted the OS deployment manager security role
Administrative users who are granted the OS deployment manager security role can
create self-signed certificates. These certificates can then be used to impersonate a
client and obtain client policy from Configuration Manager.

Use Enhanced HTTP to reduce the need for a network
access account
Starting in version 1806, when you enable Enhanced HTTP, several OS deployment
scenarios don't require a network access account to download content from a
distribution point. For more information, see Task sequences and the network access
account.

Security issues for OS deployment
Although OS deployment can be a convenient way to deploy the most secure operating
systems and configurations for computers on your network, it does have the following
security risks:

Information disclosure and denial of service
If an attacker can obtain control of your Configuration Manager infrastructure, they
could run any task sequences. This process might include formatting the hard drives of
all client computers. Task sequences can be configured to contain sensitive information,
such as accounts that have permissions to join the domain and volume licensing keys.

Impersonation and elevation of privileges
Task sequences can join a computer to domain, which can provide a rogue computer
with authenticated network access.

Protect the client authentication certificate that's used for bootable task sequence
media and for PXE boot deployment. When you capture a client authentication
certificate, this process gives an attacker an opportunity to obtain the private key in the

<!-- p.62 -->

certificate. This certificate lets them impersonate a valid client on the network. In this
scenario, the rogue computer can download policy, which can contain sensitive data.

If clients use the network access account to access data stored on the state migration
point, these clients effectively share the same identity. They could access state migration
data from another client that uses the network access account. The data is encrypted so
only the original client can read it, but the data could be tampered with or deleted.

Client authentication to the state migration point is
achieved by using a Configuration Manager token that is
issued by the management point.
Configuration Manager doesn't limit or manage the amount of data that's stored on the
state migration point. An attacker could fill up the available disk space and cause a
denial of service.

If you use collection variables, local administrators can
read potentially sensitive information
Although collection variables offer a flexible method to deploy operating systems, this
feature might result in information disclosure.

Privacy information for OS deployment
In addition to deploying an OS to computers without one, Configuration Manager can
be used to migrate users' files and settings from one computer to another. The
administrator configures which information to transfer, including personal data files,
configuration settings, and browser cookies.

Configuration Manager stores the information on a state migration point, and encrypts
it during transmission and storage. Only the new computer associated with the state
information can retrieve the stored information. If the new computer loses the key to
retrieve the information, a Configuration Manager administrator with the View Recovery
Information right on computer association instance objects can access the information
and associate it with a new computer. After the new computer restores the state
information, it deletes the data after one day, by default. You can configure when the
state migration point removes data marked for deletion. Configuration Manager doesn't
store the state migration information in the site database, and doesn't send it to
Microsoft.

<!-- p.63 -->

If you use boot media to deploy OS images, always use the default option to password-
protect the boot media. The password encrypts any variables stored in the task
sequence, but any information not stored in a variable might be vulnerable to
disclosure.

OS deployment can use task sequences to perform many different tasks during the
deployment process, which includes installing applications and software updates. When
you configure task sequences, you should also be aware of the privacy implications of
installing software.

Configuration Manager doesn't implement OS deployment by default. It requires several
configuration steps before you collect user state information or create task sequences or
boot images.

Before you configure OS deployment, consider your privacy requirements.

See also
Diagnostics and usage data

Security and privacy for Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.64 -->

Plan for OS deployment interoperability
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When different Configuration Manager sites in a single hierarchy use different versions,
some Configuration Manager functionality isn't available. Typically, functionality from
the newer version of Configuration Manager isn't accessible at sites or by clients that
run a lower version. For more information, see Interoperability between different
versions of Configuration Manager.

Objects
Consider the following objects when you upgrade the top-level site in your hierarchy
and other sites in your hierarchy run Configuration Manager with a lower version:

Client installation package
      The source for the default client installation package is automatically upgraded. All
      distribution points in the hierarchy are updated with the new client installation
      package. This behavior happens even on distribution points at sites in the
      hierarchy that are at a lower version.

      You can't assign new version clients to sites that you haven't yet upgraded to the
      new version. Assignment is blocked at the management point.

Boot images
      When you upgrade the top-level site to the latest version of Configuration
      Manager, it automatically updates the default boot images (x86 and x64). The
      update uses the version of the Windows ADK and Windows PE that you've
      installed. The files that are associated with the default boot images are updated
      with the latest Configuration Manager version of the files. The site doesn't
      automatically update custom boot images. You need to manually update custom
      boot images, which include older Windows PE versions.

      When your site hierarchy contains sites with different versions of Configuration
      Manager, avoid the use of dynamic media. Instead, use site-based media to
      contact a specific management point. After you update all sites to the same
      version of Configuration Manager, you can use dynamic media again.

<!-- p.65 -->

     Verify that the latest Configuration Manager boot images include your
     customizations. Then update all distribution points at the new version sites with
     the latest version of the new boot images.

User State Migration Tool (USMT)
When you upgrade the top-level site to the latest version of Configuration Manager, it
automatically updates the default USMT package to the latest version. It doesn't
automatically update any custom USMT packages. You need to manually update these
packages.

New task sequence steps
Periodically, new task sequence steps are introduced with new versions of Configuration
Manager. When you deploy a task sequence with a new step to older clients, the task
sequence step fails. Before you deploy a task sequence with a new step, make sure the
clients in the target collection are updated to the new version.

OS deployment media
When the site is updated to a new version, update all media with the new Configuration
Manager client package. These media types include bootable, capture, prestaged, and
stand-alone.

Third-party extensions to OS deployment
When you have third-party extensions to OS deployment and you have different
versions of Configuration Manager sites or Configuration Manager clients, there might
be issues with the extensions.

Latest version of Configuration Manager sites
in a mixed hierarchy
When you upgrade a site to latest version of Configuration Manager, task sequences
that reference the default client installation package automatically start to deploy the
latest Configuration Manager client version.

Task sequences that reference a custom client installation package continue to deploy
the version of the client that's contained in that custom package. Custom packages
likely include an earlier version of the Configuration Manager client. To avoid task

<!-- p.66 -->

sequence deployment failures, update any custom client installation packages to the
latest version.

When you configure a task sequence to use a custom client installation package, do one
of the following actions:

       Update the task sequence step to use the latest Configuration Manager version of
       the client installation package
       Update the custom package to use the latest Configuration Manager client
       installation source

  ） Important

  Don't deploy a task sequence that references the latest Configuration Manager
  client installation package to clients in an older Configuration Manager site. When
  clients assigned to an older Configuration Manager site are upgraded to the latest
  Configuration Manager client version, Configuration Manager blocks the
  assignment to the older Configuration Manager site. These clients are no longer
  assigned to any site. Until you manually assign the client to the latest Configuration
  Manager site, or reinstall the older Configuration Manager version of the client on
  the computer, these clients are unmanaged.

Older versions of Configuration Manager in a
mixed hierarchy
When you upgrade your central administration site to the latest version of Configuration
Manager, make sure that OS deployment task sequences that you deploy don't leave
those clients in an unmanaged state. For example, if you deploy to clients assigned to an
older Configuration Manager site that you haven't yet upgraded to the latest version of
Configuration Manager.

Make a copy of a task sequence that you use to deploy to clients in the latest version of
Configuration Manager site. Then modify the task sequence so you can deploy it to
clients in an older Configuration Manager site. Configure the task sequence to reference
a custom client installation package that uses the older Configuration Manager client
installation source. If you don't already have a custom client installation package that
references the older Configuration Manager client installation source, manually create
one.

Next steps

<!-- p.67 -->

Interoperability between different versions of Configuration Manager

Prepare site system roles for OS deployments

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.68 -->

Prepare site system roles for OS
deployments with Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To deploy operating systems in Configuration Manager, first prepare the following site
system roles that require specific configurations and considerations.

Distribution points
The distribution point site system role hosts source files for clients to download. This
content is for applications, software updates, OS images, boot images, and driver
packages. Control content distribution by using bandwidth, throttling, and scheduling
options.

It's important that you have enough distribution points to support the deployment of
operating systems to computers. It's also important that you plan for the placement of
these distribution points in your hierarchy. For more information, see Manage content
and content infrastructure. This article includes more planning considerations for
distribution points specific to OS deployment.

Additional planning considerations for distribution points

How can I prevent unwanted OS deployments?
Configuration Manager doesn't distinguish site servers from other destination
computers in a collection. If you deploy a required task sequence to a collection that
includes a site server, it runs the task sequence the same way as any other computer in
the collection. Make sure that your OS deployment uses a collection that includes the
intended clients.

Manage the behavior for high-risk task sequence deployments. A high-risk deployment
automatically installs on a client and has the potential to cause unwanted results. For
example, a task sequence with a purpose of required that deploys an OS. To reduce the
risk of an unwanted high-risk deployment, configure deployment verification settings.
For more information, see Settings to manage high-risk deployments.

<!-- p.69 -->

How many computers can receive an OS image at one time from a
single distribution point?

To estimate how many distribution points you need, consider the following variables:

     The processing speed of the distribution point
     The disk speed of the distribution point
     The available bandwidth on the network
     The size of the image package

For example, if you don't consider any other server resource factors, the maximum
number of computers that can process a 4-GB image package in one hour on a 100-
megabit/sec Ethernet network is 11 computers.

100 megabits/sec = 12.5 megabytes/sec = 750 megabytes/min = 45 gigabytes/hour = 11

images @ 4 GB per image

If you must deploy an OS to a specific number of computers within a specific time
frame, distribute the image to an appropriate number of distribution points.

Can I deploy an OS to a distribution point?

You can deploy an OS to a distribution point, but the OS image must be received from a
different distribution point.

Configuring distribution points to accept PXE requests
To deploy operating systems to Configuration Manager clients that make PXE boot
requests, configure one or more distribution points to accept PXE requests. Once you
configure the distribution point, it responds to PXE boot requests and determines the
appropriate deployment action to take. For more information, see Install or modify a
distribution point.

Customize the RamDisk TFTP block and window sizes on
PXE-enabled distribution points
You can customize the RamDisk TFTP block and window sizes for PXE-enabled
distribution points. If you've customized your network, a large block or window size
could cause the boot image download to fail with a time-out error. The RamDisk TFTP
block and window size customizations allow you to optimize TFTP traffic when using PXE
to meet your specific network requirements. To determine what configuration is most
efficient, test the customized settings in your environment.

<!-- p.70 -->

     TFTP block size: The block size is the size of the data packets that the server sends
     to the client that is downloading the file. A larger block size allows the server to
     send fewer packets, so there are fewer round-trip delays between the server and
     the client. However, a large block size leads to fragmented packets, which most
     PXE client implementations don't support.

     TFTP window size: TFTP requires an acknowledgment (ACK) packet for each block
     of data that is sent. The server doesn't send the next block in the sequence until it
     receives the ACK packet for the previous block. TFTP windowing enables you to
     define how many data blocks it takes to fill a window. The server sends the data
     blocks back-to-back until the window is filled, and then the client sends an ACK
     packet. If you increase this window size, it reduces the number of round-trip delays
     between the client and server, and it decreases the overall required time to
     download a boot image.

Modify the RamDisk TFTP window size
To customize the RamDisk TFTP window size, add the following registry key on PXE-
enabled distribution points:

     Location: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\DP
     Name: RamDiskTFTPWindowSize
     Type: REG_DWORD
     Value: (customized window size) The default value is 1 (one data block fills the
     window).

Modify the RamDisk TFTP block size

To customize the RamDisk TFTP window size, add the following registry key on PXE-
enabled distribution points:

     Location: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\DP
     Name: RamDiskTFTPBlockSize
     Type: REG_DWORD
     Value: (customized block size) The default value is 4096 .

  ７ Note

  Both Windows Deployment Services and the Configuration Manager PXE responder
  service support these TFTP configurations.

<!-- p.71 -->

Configure distribution points to support multicast
Multicast is a network optimization method. Use it on distribution points when multiple
clients are likely to download the same OS image at the same time. When you use
multicast, multiple computers can simultaneously download the OS image as it's
multicast by the distribution point. Without multicast, the distribution point sends a
copy of the data to each client over a separate connection. For more information, see
Use multicast to deploy Windows over the network.

Before you deploy the OS, configure a distribution point to support multicast. For more
information, see Install and configure distribution points.

State migration point
The state migration point stores user state data that USMT captures on one computer,
and then restores on another computer. However, when you capture user settings for an
OS deployment on the same computer, such as a deployment where you refresh
Windows on the destination computer, you can choose whether to store the data on the
same computer by using hard-links or use a state migration point. For some computer
deployments, when you create the state store, Configuration Manager automatically
creates an association between the state store and the destination computer. As you
plan for the state migration point, consider the following factors:

User state size
The size of the user state directly affects disk storage on the state migration point and
network performance during the migration. Consider the size of the user state and the
number of computers to migrate. Consider also what settings to migrate from the
computer. For example, if the My Documents folder is already backed up to a server,
then perhaps you don't have to migrate it as part of the image deployment. Avoiding
unnecessary migrations keeps the overall size of the user state smaller, and decreases
the effect it would otherwise have on network performance and disk storage on the
state migration point.

User State Migration Tool
To capture and restore the user state during the deployment of the operating systems,
use a User State Migration Tool (USMT) package that points to the USMT source files.
Configuration Manager automatically creates this package in the Configuration Manager
console in Software Library > Application Management > Packages. Configuration

<!-- p.72 -->

Manager uses USMT to capture the user state from one OS and then restore it to
another. The Windows Assessment and Deployment Kit (ADK) for Windows includes
USMT.

For a description of different migration scenarios for USMT, see Common migration
scenarios in the Windows documentation.

Retention policy
When you configure the state migration point, specify the length of time to keep the
user state data that it stores. The length of time to keep the data on the state migration
point depends on two considerations:

        The effect that the stored data has on disk storage.

        The potential requirement to keep the data for a time in case you must migrate the
        data again.

State migration occurs in two phases: capturing the data, and restoring the data. When
you capture data, the user state data is collected and saved to the state migration point.
When you restore the data, the user state data is retrieved from the state migration
point, written to the destination computer, and then the Release State Store task
sequence step releases the stored data. When the data is released, the retention timer
starts. If you select the option to delete migrated data immediately, the user state data
is deleted as soon as it's released. If you select the option to keep the data for a certain
period of time, the data is deleted when that period of time elapses after the state data
is released. The longer you set the retention period, the more disk space you're likely to
require.

Select drive to store user state migration data
When you configure the state migration point, specify the drive on the server to store
the user state migration data. You select a drive from a fixed list of drives. However,
some of these drives might represent non-writable drives, such as the CD drive, or a
non-network share drive. Some drive letters might not be mapped to any drives on the
computer. Specify a writable, shared drive when you configure the state migration point.

Configure a state migration point
Use the following methods to configure a state migration point to store the user state
data:

<!-- p.73 -->

     Use the Create Site System Server Wizard to create a new site system server for
     the state migration point.

     Use the Add Site System Roles Wizard to add a state migration point to an
     existing server.

When you use these wizards, you're prompted to provide the following information for
the state migration point:

     The folders to store the user state data.

     The maximum number of clients that can store data on the state migration point.

     The minimum free space for the state migration point to store user state data.

     The deletion policy for the role. Either specify that the user state data is deleted
     immediately after it's restored on a computer, or after a specific number of days
     after the user data is restored on a computer.

     Whether the state migration point responds only to requests to restore user state
     data. When you enable this option, you can't use the state migration point to store
     user state data.

For the steps to install a site system role, see Add site system roles.

Next steps
Prepare for OS deployment

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.74 -->

Prepare for OS deployment in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

There are several things you must do in Configuration Manager before you can deploy
operating systems. Use the following articles to prepare for OS deployment:

      Manage boot images

      Manage OS images

      Manage OS upgrade packages

      Manage drivers

      Manage user state

      Prepare for unknown computer deployments

      Associate users with a destination computer

OS image size
OS images are large in size. For example, the image size for Windows 7 is 3 GB or more.
The size of the image and the number of computers to which you simultaneously deploy
the OS affects the network performance and available bandwidth. Make sure to test the
network performance. Testing the impact better gauges the effect the image
deployment might have and the time it takes to complete the deployment.
Configuration Manager activities that affect network performance include distributing
the image to a distribution point, distributing the image from one site to another, and
downloading the image to the client.

Also make sure that you plan for sufficient disk storage space on the distribution points
that host the OS images.

For more information, see Additional planning considerations for distribution points.

Client cache size

<!-- p.75 -->

When Configuration Manager clients download content, they automatically use
Background Intelligent Transfer Service (BITS), if it's available. When you deploy a task
sequence that installs an OS, you can set an option on the deployment so that
Configuration Manager clients download the full image to a local cache before the task
sequence runs.

When a Configuration Manager client must download an OS image, but there isn't
enough space in the cache, the client can clear space in its cache. It checks the other
packages in the cache to determine whether deleting any of the oldest packages will
free enough disk space to accommodate the image. If deleting packages doesn't free
enough space, the client doesn't download the image, and the deployment fails. This
behavior might occur if the cache has a large package that you configure to persist in
the cache. If deleting packages does free enough disk space in the cache, the client
deletes them, and then downloads the image into the cache.

The default cache size on Configuration Manager clients might not be large enough for
most OS image deployments. If you plan to download the full image to the client cache,
adjust the client cache size on the destination computers to accommodate the size of
the image that you're deploying.

For more information, see Configure the client cache.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.76 -->

Manage boot images with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

A boot image in Configuration Manager is a Windows PE (WinPE) image that's used
during an OS deployment. Boot images are used to start a computer in WinPE. This
minimal OS contains limited components and services. Configuration Manager uses
WinPE to prepare the destination computer for Windows installation.

Default boot images
Configuration Manager provides two default boot images: One to support x86 platforms
and one to support x64 platforms. These images are stored in the x64 or i386 folders in
the following share on the site server: \\<SiteServerName>\SMS_<sitecode>\osd\boot\ .
The default boot images are updated or regenerated depending on the action that you
take.

Consider the following behaviors for any of the actions described for default boot
images:

        The source driver objects must be valid. These objects include the driver source
        files. If the objects aren't valid, the site doesn't add the drivers to the boot images.

        Boot images that aren't based on the default boot images, even if they use the
        same Windows PE version, aren't modified.

        Redistribute the modified boot images to distribution points.

        Recreate any media that uses the modified boot images.

        If you don't want your customized/default boot images automatically updated,
        don't store them in the default location.

  ７ Note

  The Configuration Manager log tool (CMTrace) is added to all boot images in the
  Software Library. When you're in Windows PE, start the tool by typing cmtrace
  from the command prompt.

<!-- p.77 -->

  CMTrace is the default viewer for log files in Windows PE.

Use updates and servicing to install the latest version of
Configuration Manager
When you upgrade the Windows Assessment and Deployment Kit (ADK) version, and
then use updates and servicing to install the latest version of Configuration Manager,
the site regenerates the default boot images. This update includes the new WinPE
version from the updated Windows ADK, the new version of the Configuration Manager
client, drivers, and customizations. The site doesn't modify custom boot images.

  ７ Note

  The site always uses the production version of the Configuration Manager client in
  default boot images. Even if you configure automatic client upgrades to use a pre-
  production collection, that feature doesn't apply to boot images.

Upgrade from Configuration Manager 2012 to current
branch
When you upgrade Configuration Manager 2012 to current branch, the site regenerates
the default boot images. This update includes the new WinPE version from the updated
Windows ADK and the new version of the Configuration Manager client. All boot image
customizations remain unchanged. The site doesn't modify custom boot images.

Update distribution points with the boot image
When you use the Update Distribution Points action from the Boot Images node in the
console, the site updates the target boot image with the client components, drivers, and
customizations.

You can reload the boot image with the latest version of WinPE from the Windows ADK
installation directory. The General page of the Update Distribution Points wizard
provides the following information:

     The current Windows ADK version installed on the site server
     The current production client version
     The Windows ADK version of WinPE in the boot image
     The version of the Configuration Manager client in the boot image

<!-- p.78 -->

If the versions in the boot image are out of date, use the option to Reload this boot
image with the current Windows PE version from the Windows ADK.

  ） Important

  This action is available for both default and custom boot images. During this
  process to reload the boot image, the site doesn't retain any manual
  customizations made outside of Configuration Manager. These customizations
  include third-party extensions. This option rebuilds the boot image using the latest
  version of WinPE and the latest client version. Only the configurations that you
  specify on the properties of the boot image are reapplied.

The Boot Images node also includes a new column for (Client Version). Use this column
to quickly view the Configuration Manager client version in each boot image.

After you update the Windows ADK on the site server, the console won't immediately
show the new version. If you use one these actions to update a boot image, the site uses
the latest ADK version. To get the console to display the current ADK version, restart the
WMI service. For more information, see Starting and Stopping the WMI Service.

Customize a boot image
When a boot image is based on the WinPE version from the supported version of the
Windows ADK, you can customize or modify a boot image from the console. When you
upgrade a site and install a new version of the Windows ADK, custom boot images
aren't updated with the new version of Windows ADK. When that happens, you can't
customize the boot images in the Configuration Manager console. However, they
continue to work as they did before the upgrade.

When a boot image is based on a different version of the Windows ADK installed on a
site, you must customize the boot images. Use another method to customize these boot
images, such as using the Deployment Image Servicing and Management (DISM)
command-line tool. DISM is part of the Windows ADK. For more information, see
Customize boot images.

Add a boot image
During site installation, Configuration Manager automatically adds boot images that are
based on a WinPE version from the supported version of the Windows ADK. Depending
on the version of Configuration Manager, you can add boot images based on a different

<!-- p.79 -->

WinPE version from the supported version the Windows ADK. An error occurs when you
try to add a boot image that contains an unsupported version of WinPE.

Configuration Manager also supports Windows PE versions for boot images that aren't
customizable from the Configuration Manager console. For example, you install the
Windows ADK and WinPE add-on for Windows 11 on the site server. For x64 boot
images based on WinPE version 11 from the WinPE add-on for Windows 11, you can
customize them from the Configuration Manager console. However, while x86 boot
images based on WinPE version 10 are supported, you need to manually customize
them from a different computer. Use the version of DISM that's installed with the
Windows ADK for Windows 10. Then, you can add the boot image to the Configuration
Manager console.

For more information, see the following articles:

     Customize boot images
     Support for the Windows ADK
     DISM supported platforms

Use the following process to add a boot image in Configuration Manager:

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Operating Systems, and then select the Boot Images node.

   2. On the Home tab of the ribbon, in the Create group, select Add Boot Image. This
     action starts the Add Boot Image Wizard.

   3. On the Data Source page, specify the following options:

           In the Path box, specify the path to the boot image WIM file. The specified
           path must be a valid network path in the UNC format. For example:
           \\ServerName\ShareName\BootImageName.wim

           Select the boot image from the Boot Image drop-down list. If the WIM file
           contains multiple boot images, select the appropriate image.

   4. On the General page, specify the following options:

           In the Name box, specify a unique name for the boot image.

           In the Version box, specify a version number for the boot image.

           In the Comment box, specify a brief description of how you use the boot
           image.

   5. Complete the wizard.

<!-- p.80 -->

The boot image is now listed in the Boot Image node. Before using the boot image to
deploy an OS, distribute the boot image to distribution points.

   Tip

  In the Boot Image node of the console, the Size (KB) column displays the
  decompressed size for each boot image. When the site sends a boot image over
  the network, it sends a compressed copy. This copy is typically smaller than the size
  listed in the Size (KB) column.

Distribute boot images
Boot images are distributed to distribution points in the same way as you distribute
other content. Before you deploy an OS or create media, distribute the boot image to at
least one distribution point.

For more information on how to distribute a boot image, see Distribute content.

To use PXE to deploy an OS, consider the following points before you distribute the
boot image:

     Configure the distribution point to accept PXE requests.
     Distribute both an x86 and an x64 PXE-enabled boot image to at least one PXE-
     enabled distribution point.
     Configuration Manager distributes the boot images to the RemoteInstall folder on
     the PXE-enabled distribution point.

For more information about using PXE to deploy operating systems, see Use PXE to
deploy Windows over the network.

Modify a boot image
Add or remove device drivers to the image, or edit the properties of the boot image.
The drivers that you add or remove can include network or storage drivers. Consider the
following factors when you modify boot images:

     Before adding drivers to the boot image, import and enable them in the device
     driver catalog.

     When you modify a boot image, the boot image doesn't change any of the
     associated packages that the boot image references.
