---
title: "OS deployment documentation — pages 241-280"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0241-0280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0241-0280
family: sccm
documentKind: "doc"
abstract: "4. On the General page, specify the following information. Task sequence: Specify the task sequence to deploy. By default, this box displays the selected task sequence. Collection: Select the collection that contains the computers to run the task sequence. Don't deploy a task se"
---

# OS deployment documentation — pages 241-280

<!-- p.241 -->

4. On the General page, specify the following information.

       Task sequence: Specify the task sequence to deploy. By default, this box
       displays the selected task sequence.

       Collection: Select the collection that contains the computers to run the task
       sequence.

       Don't deploy a task sequence that installs an OS to inappropriate collections,
       such as a collection of all your data center servers. Be sure that the selected
       collection contains only those computers that you want to run the task
       sequence.

       For more information about high-risk deployments, see High-risk
       deployments.

       Use default distribution point groups associated to this collection: Store the
       task sequence content on the collection's default distribution point group. If
       you haven't associated the selected collection with a distribution point group,
       this option is grayed out.

       Automatically distribute content for dependencies: If any referenced
       content has dependencies, then the site also sends dependent content to
       distribution points.

       Pre-download content for this task sequence: For more information, see
       Configure pre-cache content.

       Select Deployment Template: Save and specify a deployment template for a
       task sequence.

          ） Important

          Some items aren't saved in the template. Make sure you apply the
          following items when you run the deployment wizard:
            Software Installation
            Scheduling
            Pre-download content

       Comments (optional): Specify additional information that describes this
       deployment of the task sequence.

5. On the Deployment Settings page, specify the following information:

<!-- p.242 -->

Purpose: From the drop-down list, choose one of the following options:

  Available: The user sees the task sequence in Software Center and can
  install it on demand.

  Required: Configuration Manager automatically runs the task sequence
  according to the configured schedule. If the task sequence isn't hidden, a
  user can still track its deployment status. They can also use Software
  Center to install the task sequence before the deadline.

  ７ Note

  If multiple users are signed into the device, package and task sequence
  deployments may not appear in Software Center.

Make available to the following: Specify whether the task sequence is
available to one of the following types:
  Only Configuration Manager clients
  Configuration Manager clients, media, and PXE
  Only media and PXE
  Only media and PXE (hidden)

  ） Important

  Use the Only media and PXE (hidden) setting for automated task
  sequence deployments. To have the computer automatically boot to the
  deployment with no user interaction, select Allow unattended operating
  system deployment and set the SMSTSPreferredAdvertID variable as
  part of the media. For more information about task sequence variables,
  see Task sequence variables.

Send wake-up packets: If the deployment is Required and you select this
option, the site sends a wake-up packet to computers before the client runs
the deployment. This packet wakes the computer from sleep at the
installation deadline time. Before using this option, computers and networks
must be configured for Wake On LAN. For more information, see Plan how to
wake up clients.

Allow clients on a metered Internet connection to download content after
the installation deadline, which might incur additional costs: This option is
only available for Required deployments. When you have a custom task

<!-- p.243 -->

       sequence that installs an application but doesn't deploy an OS, you can
       specify whether to allow clients to download content after an installation
       deadline when they use metered internet connections. Internet providers
       sometimes charge by the amount of data that you use when you're on a
       metered internet connection.

          ７ Note

          While using a metered internet connection might work for task
          sequences that don't deploy an OS, it's not supported.

6. On the Scheduling page, specify the following information:

    ） Important

    When a Windows PE client starts from PXE or boot media, the client doesn't
    evaluate deployment schedules. These schedules include start, expire, and
    deadline times. Only configure schedules in deployments to clients that start
    from the full Windows OS. Consider using other methods, such as
    maintenance windows, to control active task sequences deployed to clients
    that start from Windows PE.

       Schedule when this deployment will become available: Specify the date and
       time when the task sequence is available to run on the destination computer.
       When you select the UTC option, the task sequence is available for multiple
       computers at the same time. Otherwise the deployment is available at
       different times, according to the local time on each computer.

       If the start time is earlier than the required time, the client downloads the
       task sequence content at the start time.

       Schedule when this deployment will expire: Specify the date and time when
       the task sequence expires on the destination computer. When you select the
       UTC option, the task sequence expires on multiple destination computers at
       the same time. Otherwise the deployment expires at different times,
       according to the local time on each computer.

       Assignment schedule: For a Required deployment, specify when the client
       runs the task sequence. You can add multiple schedules. The assignment
       schedule can have one of the following configurations:
          A specific date and time

<!-- p.244 -->

  Monthly, weekly, or custom recurrence pattern
  As soon as possible
  Log on or log off events

  ７ Note

  If you schedule a start time for a required deployment that's earlier than
  the date and time when the task sequence is available, the Configuration
  Manager client downloads the content at the assigned start time. This
  behavior occurs even though you scheduled the task sequence to be
  available at a later time.

Rerun behavior: Specify when the task sequence reruns. Select one of the
following options:

  Never rerun deployed program: If the client has previously run the task
  sequence, it doesn't rerun. The task sequence doesn't rerun even if it
  originally failed or the task sequence files have changed.

  Always rerun program: The task sequence always reruns on the client
  when the deployment is scheduled. It reruns even if the task sequence has
  already run successfully. This setting is useful when you use recurring
  deployments in which the task sequence is routinely updated.

     ） Important

     This option is selected by default. However, it has no effect until you
     assign a required deployment. A user can always rerun available
     deployments.

  Rerun if failed previous attempt: The task sequence reruns when the
  deployment is scheduled, only if it previously failed to run. This setting is
  useful for a required deployment. If the last attempt to run was
  unsuccessful, it automatically tries to rerun according to the assignment
  schedule.

  Rerun if succeeded on previous attempt: The task sequence reruns only if
  it previously ran successfully on the client. This setting is useful when you
  use recurring deployments in which the task sequence is routinely
  updated, and each update requires that the previous update is installed
  successfully.

<!-- p.245 -->

          ７ Note

          A user can rerun an available task sequence deployment. Before you
          deploy an available task sequence in a production environment, first test
          what happens if a user reruns the task sequence multiple times.

7. On the User Experience page, specify the following information:

       Allow user to run the program independently of assignments: Specify
       whether a user can run a required deployment outside of the assignment
       schedule. This option is always enabled for available deployments.

       Show Task Sequence progress: Specify whether the Configuration Manager
       client displays the progress of the task sequence.

       Software installation: Specify whether the user is allowed to install software
       outside a configured maintenance window after the scheduled time.

       System restart (if required to complete the installation): Specify whether the
       user is allowed to restart the computer after a software installation outside a
       configured maintenance window after the assignment time.

       Write filter handling for Windows Embedded devices: This setting controls
       the installation behavior on Windows Embedded devices that are enabled
       with a write filter. Choose the option to commit changes at the installation
       deadline or during a maintenance window. When you select this option, a
       restart is required and the changes persist on the device. Otherwise, the
       application is installed to the temporary overlay, and committed later. When
       you deploy a task sequence to a Windows Embedded device, make sure the
       device is a member of a collection that has a configured maintenance
       window.

       Allow task sequence to run for client on the Internet: Specify whether the
       task sequence is allowed to run on an internet-based client. For more
       information, see Deploy a task sequence over the internet.

8. On the Alerts page, specify the alert settings that you want for this task sequence
  deployment.

9. On the Distribution Points page, specify the following information:

       Deployment options: For more information, see Deployment options.

<!-- p.246 -->

          Allow clients to use distribution points from the neighbor boundary group:
          Specify whether clients can use distribution points from a neighbor boundary
          group to download the content that's required by the task sequence.

          Allow clients to use distribution points from the default site boundary
          group: Specify if clients should download content from a distribution point in
          the site default boundary group, when it isn't available from a distribution
          point in the current or neighbor boundary groups.

             ７ Note

             When a device runs a task sequence and needs to acquire content, it
             uses boundary group behaviors similar to the Configuration Manager
             client. For more information, see Task sequence support for boundary
             groups.

 10. Starting in version 2103, if you use a feature update with the Upgrade OS task
     sequence step, the wizard also includes the Deployment Package page. Select one
     of the following options:

          Select a deployment package: Add the feature updates to an existing
          deployment package.

          Create a new deployment package: Add the feature updates to a new
          deployment package.

          No deployment package: When clients run the task sequence, they
          download the feature update from peers or the Microsoft cloud.

     For more information on these options, see step 11 for the Deployment Package
     page when you Create an automatic deployment rule (ADR).

 11. To save these settings to use again, on the Summary tab select Save As Template.
     Supply a name for the template and select the settings to save.

 12. Complete the wizard.

Deployment options
These options are on the Distribution Points tab of the task sequence deployment.
They're dynamic based upon other selections in the deployment and attributes of the
task sequence. You may not always see all options.

<!-- p.247 -->

  ７ Note

  When you use multicast to deploy an OS, download the content to the computers
  either as needed or before the task sequence runs.

     Download content locally when needed by the running task sequence: Specify
     that clients download content from the distribution point as it's needed by the task
     sequence. The client starts the task sequence. When a step in the task sequence
     requires content, it's downloaded before the step runs.

     Download all content locally before starting task sequence: Specify that clients
     download all the content from the distribution point before the task sequence
     runs. If you make the task sequence available to PXE and boot media deployments
     on the Deployment Settings page, this option isn't shown.

     Access content directly from a distribution point when needed by the running
     task sequence: Specify that clients run the content from the distribution point. This
     option is only available when you enable all packages associated with the task
     sequence to use a package share on the distribution point. To enable content to
     use a package share, see the Data Access tab in the Properties for each package.

  ） Important

  For greatest security, select the options to Download content locally when needed
  by the running task sequence or Download all content locally before starting task
  sequence. When you select either of these options, Configuration Manager hashes
  the package, so that it can ensure package integrity. When you select the option to
  Access content directly from a distribution point when needed by the running
  task sequence, Configuration Manager doesn't verify the package hash prior to
  running the specified program. Because the site can't ensure package integrity, it's
  possible for users with administrative rights to alter or tamper with package
  contents.

Example 1: One deployment option

You deploy an OS deployment task sequence that wipes the disk and applies an image.
On the Deployment Settings page, you make it available to an option that includes
media and PXE:

<!-- p.248 -->

On the Distribution Points page, there's only one deployment option:

     Download content locally when needed by the running task sequence

The option to Download all content locally before starting task sequence isn't
available because the deployment is made available to media and PXE.

The option to Access content directly from a distribution point when needed by the
running task sequence isn't available. Not all of the referenced content uses a package
share.

Example 2: Two deployment options

You deploy an OS deployment task sequence that wipes the disk and applies an image.
On the Deployment Settings page, you make it available to Only Configuration
Manager clients. On the Distribution Points page, there are two deployment options
available:

     Download content locally when needed by the running task sequence
     Download all content locally before starting task sequence

The option to Access content directly from a distribution point when needed by the
running task sequence isn't available. Not all of the referenced content uses a package
share.

Example 3: Three deployment options
You have several packages with administrative scripts and associated content. On the
Data Access tab of the package properties, you configure all of them to Copy the

<!-- p.249 -->

content in this package to a package share on distribution points.

You create a task sequence that only has several Install Package steps for these script
packages, and the deploy it. On the Deployment Settings page, the only option is to
make available to Only Configuration Manager clients. This option is the only available.
The task sequence isn't for OS deployment, because it doesn't have a boot image
associated with it. On the Distribution Points page, there are three deployment options
available:

     Download content locally when needed by the running task sequence
     Download all content locally before starting task sequence
     Access content directly from a distribution point when needed by the running
     task sequence

Deploy Windows in-place upgrade via CMG
The Windows in-place upgrade task sequence supports deployment to internet-based
clients managed through the cloud management gateway (CMG). This ability allows
remote users to more easily upgrade Windows without needing to connect to the
intranet.

For more information, see Deploy a task sequence over the internet.

High-risk deployments
When you deploy a high-risk deployment, such as an OS, the Select Collection window
displays only the custom collections that meet the deployment verification settings that
are configured in the site's properties. High-risk deployments are always limited to
custom collections, collections that you create, and the built-in Unknown Computers
collection. When you create a high-risk deployment, you can't select a built-in collection
such as All Systems. To see all custom collections that contain fewer clients than the
configured maximum size, disable the option to Hide collections with a member count
greater than the site's minimum size configuration. For more information, see Settings
to manage high-risk deployments.

<!-- p.250 -->

The deployment verification settings are based on the current membership of the
collection. After you deploy the task sequence, Configuration Manager doesn't
reevaluate the collection membership for the high-risk deployment settings.

For example, let's say you set Default size to 100 and the Maximum size to 1000. When
you create a high risk deployment, the Select Collection window only displays
collections that contain fewer than 100 clients. If you clear the Hide collections with a
member count greater than the site's minimum size configuration setting, the window
displays collections that contain fewer than 1000 clients.

When you select a collection that contains a site role, the following behavior applies:

     If the collection contains a site system server, and you configured the deployment
     verification settings to block collections with site system servers, then an error
     occurs. You can't continue creating the deployment.

     If one of the following criteria applies, then the Deploy Software Wizard displays a
     high-risk warning. To continue, you need to agree to create a high-risk
     deployment. The site generates an audit status message.

        If the collection contains a site system server, and you configured the
        deployment verification settings to warn on collections with site system servers

        If the collection exceeds the default size value

        If the collection contains a server

Next steps
Monitor OS deployments

Debug a task sequence

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.251 -->

Deploy a task sequence over the
internet
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager supports various methods to deploy a task sequence to remote
clients over the internet. You can deploy a Windows upgrade, use bootable media, or
start it from Software Center. This article covers the particular configurations for these
scenarios. First use Deploy a task sequence to create the basic deployment. Then use the
configurations in this article to customize it for internet-based clients.

  ２ Warning

  You can manage the behavior for high-risk task sequence deployments. A high-risk
  deployment is a deployment that is automatically installed and has the potential to
  cause unwanted results. For example, a task sequence that has a purpose of
  Required that deploys an OS is considered a high-risk deployment. For more
  information, see Settings to manage high-risk deployments.

Allow task sequence to run on internet
On the User Experience page of the Deploy Software Wizard, you can configure the
deployment to Allow task sequence to run for client on the Internet. This setting is
required for all internet-based client scenarios. The following sections cover the main
scenarios when you enable this setting.

  ７ Note

  The task sequence advanced setting to Run another program first doesn't apply to
  task sequences that run on clients that communicate via a cloud management
  gateway (CMG). This option uses the UNC network path of the package, which isn't
  accessible via CMG.

Windows in-place upgrade
Use this setting for deployments of a Windows in-place upgrade task sequence to
internet-based clients through the cloud management gateway (CMG). All supported

<!-- p.252 -->

versions of Configuration Manager support this scenario. For more information, see
Deploy Windows in-place upgrade via CMG.

Install a Windows imaging task sequence from Software
Center
Starting in version 2006, you can deploy a task sequence with a boot image to a device
that communicates through the CMG. The user needs to start the task sequence from
Software Center.

  ７ Note

  When a Microsoft Entra joined client runs an OS deployment task sequence, the
  client in the new OS won't automatically join Microsoft Entra ID. Even though it's
  not Microsoft Entra joined, the client is still managed.

  When you run an OS deployment task sequence on an internet-based client, that's
  either Microsoft Entra joined or uses token-based authentication, you need to
  specify the CCMHOSTNAME property in the Setup Windows and ConfigMgr step.

Use bootable media to install a Windows imaging task
sequence
Starting in version 2010, you can use bootable media to reimage internet-based devices
that connect through a CMG. This scenario helps you better support remote workers. If
Windows won't start so that the user can access Software Center, you can now send
them a USB drive to reinstall Windows. For more information, see Deploy an OS over
CMG using bootable media.

In version 2002 and earlier, operations that require a boot media aren't supported with
this setting. Allow a task sequence to run on the internet only for generic software
installations or script-based task sequences that run operations in the standard OS.

  ７ Note

  For all internet-based task sequence scenarios in version 2002 and earlier, start the
  task sequence from Software Center. They don't support Windows PE, PXE, or task
  sequence media.

<!-- p.253 -->

Deploy Windows in-place upgrade via CMG
The Windows in-place upgrade task sequence supports deployment to internet-based
clients managed through the cloud management gateway (CMG). This ability allows
remote users to more easily upgrade to Windows without needing to connect to the
intranet.

Make sure all of the content referenced by the in-place upgrade task sequence is
distributed to a content-enabled CMG. Enable the CMG setting: Allow CMG to function
as a cloud distribution point and serve content from Azure storage. Otherwise devices
can't run the task sequence.

When you deploy an upgrade task sequence, use the following settings:

     Allow task sequence to run for client on the Internet, on the User Experience tab
     of the deployment.

     Choose one of the following options on the Distribution Points tab of the
     deployment:

        Download content locally when needed by the running task sequence. The
        task sequence engine can download packages on-demand from a content-
        enabled CMG. This option provides additional flexibility with your Windows in-
        place upgrade deployments to internet-based devices.

        Download all content locally before starting task sequence. With this option,
        the Configuration Manager client downloads the content from the cloud source
        before starting the task sequence.

     (Optional) Pre-download content for this task sequence, on the General tab of the
     deployment. For more information, see Configure pre-cache content.

  ７ Note

  Start the task sequence from Software Center. This scenario doesn't support
  Windows PE, PXE, or task sequence media.

Bootable media support for cloud-based
content
Starting in version 2010, bootable media can download cloud-based content. For
example, you send a USB key to a user at a remote office to reimage their device. Or an

<!-- p.254 -->

office that has a local PXE server, but you want devices to prioritize cloud services as
much as possible. Instead of further taxing the WAN to download large OS deployment
content, boot media and PXE deployments can now get content from cloud-based
sources. For example, a cloud management gateway (CMG) that you enable to share
content.

  ７ Note

  The device still needs an intranet connection to the management point.

When the task sequence runs, it downloads content from the cloud-based sources.
Review smsts.log on the client.

Prerequisites for bootable media
     Enable the following client setting in the Cloud Services group: Allow access to
     cloud distribution point. Make sure the client setting is deployed to the target
     clients. For more information, see About client settings - Cloud services.

     For the boundary group that the client is in:

           Associate the content-enabled CMG. For more information, see Configure a
           boundary group.

           Enable the following option: Prefer cloud based sources over on-premises
           sources. For more information, see Boundary group options for peer
           downloads.

     Distribute the content referenced by the task sequence to the content-enabled
     CMG.

Deploy an OS over CMG using bootable media
Starting in version 2010, you can use boot media to reimage internet-based devices that
connect through a CMG. This scenario helps you better support remote workers. If
Windows won't start so that the user can access Software Center, you can now send
them a USB drive to reinstall Windows.

Prerequisites for boot media via CMG
     Set up a CMG

<!-- p.255 -->

   For all content referenced in the task sequence, distribute it to a content-enabled
   CMG. For more information, see Distribute content.

   Enable the following client settings in the Cloud services group:

      Allow access to cloud distribution point

      Enable clients to use a cloud management gateway

   Configure the Apply Network Settings task sequence step to join a workgroup.
   During the task sequence, the device can't join the on-premises Active Directory
   domain. It doesn't have connectivity to a domain controller to join the domain.

   When you deploy the task sequence to a collection, configure the following
   settings:

      User experience page: Allow task sequence to run for client on the internet

      Deployment settings page: Make available to an option that includes media.

      Distribution points page, deployment options: Download content locally when
      needed by the running task sequence. For more information, see Deployment
      options.

   Make sure the device has a constant internet connection while the task sequence
   runs. Windows PE doesn't support wireless networks, so the device needs a wired
   network connection.

   If you use a PKI-based certificate for the boot media, configure it for SHA256 with
   the Microsoft Enhanced RSA and AES provider. This certificate configuration is
   recommended but not required. The certificate can be a v3 (CNG) certificate.

   In versions 2010 and 2103, if you configure the management point to Allow
   internet-only connections, then you can't use boot media over a CMG. To work
   around this issue, configure the management point to Allow intranet and internet
   connections.

   If your CMG uses a PKI-based certificate, you need to add the trusted root
   certificate to the boot image. Otherwise, Windows PE can't communicate with the
   CMG because it doesn't trust the CMG's certificate. For more information, see Add
   a trusted root certificate to a boot image.

Create boot media to use a CMG

<!-- p.256 -->

Start the create task sequence media wizard for bootable media. For more information,
see Create bootable media. Modify the standard process using the following steps:

     On the Media Management page of the wizard, select the option for Site-based
     media.

     On the Security page, set a strong password to protect this media.

     On the Boot Image page, under Management point select the Cloud
     management gateway from the Add Management Points dialog.

When you boot an internet-connected device using this media, it communicates with
the specified CMG. The boot media downloads the policy for the task sequence
deployment via the CMG. As the task sequence runs, it downloads any additional
content and policies over the internet.

After the task sequence runs, the client uses token-based authentication.

Add a trusted root certificate to a boot image
If your CMG uses a PKI-based certificate, you need to add the trusted root certificate to
the boot image. Otherwise, Windows PE can't communicate with the CMG because it
doesn't trust the CMG's certificate.

Step 1: Export the certificate registry blob
On a system that has the trusted root certificate installed:

   1. Open the Start menu. Type run to open the Run window. Open mmc .

   2. From the File menu, choose Add/Remove Snap-in....

   3. In the Add or Remove Snap-ins dialog box, select Certificates, then select Add.

      a. In the Certificates snap-in dialog box, select Computer account, then select
        Next.

      b. In the Select Computer dialog box, select Local computer, then select Finish.

      c. In the Add or Remove Snap-ins dialog box, select OK.

   4. Expand Certificates, expand Trusted Root Certification Authorities, and select
     Certificates.

   5. Select the root certificate. On the Action menu, select Open.

<!-- p.257 -->

   6. Switch to the Details tab.

   7. Copy the value for the certificate's thumbprint. For example,
     eb971f84c0c44b9eb22a378fecb45747eb971f84

   8. From the Start menu, run regedit .

   9. Browse to the following registry key:
     Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SystemCertificates\AuthRoot\Cer
     tificates . For more information about this registry key, see System Store

     Locations.

 10. Select the registry key that matches the root certificate's thumbprint.

 11. On the File menu, select Export. Specify a file name, and save the .reg file.

 12. Edit the file in Notepad. In the key path, change SOFTWARE to winpe-offline , and
     save the file. For example:

     [HKEY_LOCAL_MACHINE\winpe-
     offline\Microsoft\SystemCertificates\AuthRoot\Certificates\eb971f84c0c44b9eb22

     a378fecb45747eb971f84]

 13. Copy this file to a location that you can access for the next step.

Step 2: Import the certificate registry blob to the offline boot
image
On a system that has the boot image file:

   1. Mount the WIM file. For example, DISM /Mount-image
     /imagefile:"C:\Sources\boot.wim" /Index:1 /MountDir:C:\Mount .

   2. From the Start menu, run regedit .

   3. Select HKEY_LOCAL_MACHINE. On the File menu, select Load Hive.

   4. Browse to C:\Mount\Windows\System32\config and select SOFTWARE. This file is the
     offline registry hive for the Windows PE image mounted to C:\Mount .

        ） Important

<!-- p.258 -->

        Make sure this path is to the mounted Windows PE image, not the default
        Windows OS path.

   5. Name the key for the loaded hive winpe-offline .

   6. On the File menu, select Import. Browse to the modified .reg file that you
     previously exported and modified. Select Open.

   7. Browse to the following registry key: Computer\HKEY_LOCAL_MACHINE\winpe-
     offline\Microsoft\SystemCertificates\AuthRoot\Certificates and confirm that the

     new key is added.

   8. Select the following registry key: Computer\HKEY_LOCAL_MACHINE\winpe-offline . On
     the File menu, select Unload Hive, and select Yes.

   9. Close the registry editor and any other windows that reference files in C:\Mount .

 10. Unmount the boot image and commit the changes. For example, DISM /Unmount-
     image /Commit /MountDir:C:\Mount

The boot image now includes the trusted root certificate.

Next steps
Monitor OS deployments

Manage task sequences to automate tasks

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.259 -->

Create phased deployments with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Phased deployments automate a coordinated, sequenced rollout of software across
multiple collections. For example, deploy software to a pilot collection, and then
automatically continue the rollout based on success criteria. Create phased deployments
with the default of two phases, or manually configure multiple phases.

Create phased deployments for the following objects:

      Task sequence
         The phased deployment of task sequences doesn't support PXE or media
         installation
      Application
      Software update
         You can't use an automatic deployment rule (ADR) with a phased deployment

Prerequisites

Security scope
Deployments created by phased deployments aren't viewable to any administrative user
that doesn't have the All security scope. For more information, see Security scopes.

Distribute content
Before creating a phased deployment, distribute the associated content to a distribution
point.

      Application: Select the target application in the console and use the Distribute
      Content action in the ribbon. For more information, see Deploy and manage
      content.

      Task sequence: You have to create referenced objects like the OS upgrade package
      before creating the task sequence. Distribute these objects before creating a
      deployment. Use the Distribute Content action on each object, or the task
      sequence. To view status of all referenced content, select the task sequence, and

<!-- p.260 -->

     switch to the References tab in the details pane. For more information, see the
     specific object type in Prepare for OS deployment.

     Software update: create the deployment package and distribute it. Use the
     Download Software Updates Wizard. For more information, see Download
     software updates.

Phase settings
These settings are unique to phased deployments. Configure these settings when
creating or editing the phases to control the scheduling and behavior of the phased
deployment process.

Optionally, use the following Windows PowerShell cmdlets to manually configure phases
for software update and task sequence phased deployments:

     New-CMSoftwareUpdatePhase
     New-CMTaskSequencePhase

Criteria for success of the first phase
     Deployment success percentage: Specify the percent of devices that need to
     successfully complete the deployment for the first phase to succeed. By default,
     this value is 95%. In other words, the site considers the first phase successful when
     the compliance state for 95% of the devices is Success for this deployment. The
     site then continues to the second phase, and creates a deployment of the software
     to the next collection.

     Number of devices successfully deployed: Specify the number of devices that
     need to successfully complete the deployment for the first phase to succeed. This
     option is useful when the size of the collection is variable, and you have a specific
     number of devices to show success before moving to the next phase.

Conditions for beginning second phase of deployment
after success of the first phase
     Automatically begin this phase after a deferral period (in days): Choose the
     number of days to wait before beginning the second phase after the success of the
     first. By default, this value is one day.

     Manually begin the second phase of deployment: The site doesn't automatically
     begin the second phase after the first phase succeeds. This option requires that

<!-- p.261 -->

     you manually start the second phase. For more information, see Move to the next
     phase.

        ７ Note

        This option isn't available for phased deployments of applications.

Gradually make this software available over this period of
time (in days)
Configure this setting for the rollout in each phase to happen gradually. This behavior
helps mitigate the risk of deployment issues, and decreases the load on the network
that is caused by the distribution of content to clients. The site gradually makes the
software available depending on the configuration for each phase. Every client in a
phase has a deadline relative to the time the software is made available. The time
window between the available time and deadline is the same for all clients in a phase.
The default value of this setting is zero, so by default the deployment isn't throttled.
Don't set the value higher than 30.

<!-- p.262 -->

Configure the deadline behavior relative to when the
software is made available
   Installation is required as soon as possible: Set the deadline for installation on the
   device as soon as the device is targeted.

   Installation is required after this period of time: Set a deadline for installation a
   certain number of days after device is targeted. By default, this value is seven days.

Automatically create a default two-phase
deployment
 1. Start the Create Phased Deployment wizard in the Configuration Manager console.
   This action varies based on the type of software you're deploying:

        Application: Go to the Software Library, expand Application Management,
        and select Applications. Select an existing application, and then choose
        Create Phased Deployment in the ribbon.

        Software update: Go to the Software Library, expand Software Updates, and
        select All Software Updates. Select one or more updates, and then choose
        Create Phased Deployment in the ribbon.

        This action is available for software updates from the following nodes:
           Software Updates
              All Software Updates
              Software Update Groups
           Windows Servicing, All Windows Updates
           Office 365 Client Management, Office 365 Updates

        Task sequence: Go to the Software Library workspace, expand Operating
        Systems, and select Task Sequences. Select an existing task sequence, and
        then choose Create Phased Deployment in the ribbon.

 2. On the General page, give the phased deployment a Name, Description (optional),
   and select Automatically create a default two phase deployment.

 3. Select Browse and choose a target collection for both the First Collection and
   Second Collection fields. For a task sequence and software updates, select from
   device collections. For an application, select from user or device collections. Select
   Next.

<!-- p.263 -->

          ） Important

          The Create Phased Deployment wizard doesn't notify you if a deployment is
          potentially high-risk. For more information, see Settings to manage high-risk
          deployments and the note when you Deploy a task sequence.

   4. On the Settings page, choose one option for each of the scheduling settings. For
     more information, see Phase settings. Select Next when complete.

   5. On the Phases page, see the two phases that the wizard creates for the specified
     collections. Select Next. These instructions cover the procedure to automatically
     create a default two-phase deployment. The wizard lets you add, remove, reorder,
     edit, or view phases for a phased deployment. For more information on these
     additional actions, see Create a phased deployment with manually configured
     phases.

   6. Confirm your selections on the Summary tab, and then select Next to complete
     the wizard.

  ７ Note

  Starting on April 21, 2020, Office 365 ProPlus is being renamed to Microsoft 365
  Apps for enterprise. For more information, see Name change for Office 365
  ProPlus. You may still see the old name in the Configuration Manager product and
  documentation while the console is being updated.

Optionally, use the following Windows PowerShell cmdlets for this task:

     New-CMApplicationAutoPhasedDeployment
     New-CMSoftwareUpdateAutoPhasedDeployment
     New-CMTaskSequenceAutoPhasedDeployment

Create a phased deployment with manually
configured phases
Create a phased deployment with manually configured phases for a task sequence. Add
up to 10 additional phases from the Phases tab of the Create Phased Deployment
wizard.

  ７ Note

<!-- p.264 -->

You can't currently manually create phases for an application. The wizard
automatically creates two phases for application deployments.

1. Start the Create Phased Deployment wizard for either a task sequence or software
  updates.

2. On the General page of the Create Phased Deployment wizard, give the phased
  deployment a Name, Description (optional), and select Manually configure all
  phases.

3. From the Phases page of the Create Phased Deployment wizard, the following
  actions are available:

        Filter the list of deployment phases. Enter a string of characters for a case-
        insensitive match of the Order, Name, or Collection columns.

        Add a new phase:

        a. On the General page of the Add Phase Wizard, specify a Name for the
            phase, and then browse to the target Phase Collection. The additional
            settings on this page are the same as when normally deploying a task
            sequence or software updates.

        b. On the Phase Settings page of the Add Phase Wizard, configure the
            scheduling settings, and select Next when complete. For more
            information, see Settings.

              ７ Note

              You can't edit the phase settings, Deployment success percentage or
              Number of devices successfully deployed, on the first phase. These
              settings only apply to phases that have a previous phase.

         c. The settings on the User Experience and Distribution Points pages of the
            Add Phase Wizard are the same as when normally deploying a task
            sequence or software updates.

        d. Review the settings on the Summary page, and then complete the Add
            Phase Wizard.

        Edit: This action opens the selected phase's Properties window, which has
        tabs the same as the pages of the Add Phase Wizard.

<!-- p.265 -->

          Remove: This action deletes the selected phase.

             ２ Warning

             There is no confirmation, and no way to undo this action.

          Move Up or Move Down: The wizard orders the phases by how you add
          them. The most recently added phase is last in the list. To change the order,
          select a phase, and then use these buttons to move the phase's location in
          the list.

             ） Important

             Review the phase settings after changing the order. Make sure the
             following settings are still consistent with your requirements for this
             phased deployment:
                Criteria for success of the previous phase
                Conditions for beginning this phase of deployment after success of
                the previous phase

   4. Select Next. Review the settings on the Summary page, and then complete the
     Create Phased Deployment wizard.

Optionally, use the following Windows PowerShell cmdlets for this task:

     New-CMSoftwareUpdateManualPhasedDeployment
     New-CMTaskSequenceManualPhasedDeployment

After you create a phased deployment, open its properties to make changes:

     Add additional phases to an existing phased deployment.

     If a phase isn't active, you can Edit, Remove, or Move it up or down. You can't
     move it before an active phase.

     When a phase is active, it's read-only. You can't edit it, remove it, or move its
     location in the list. The only option is to View the properties of the phase.

     An application phased deployment is always read-only.

Next steps

<!-- p.266 -->

Manage and monitor phased deployments:

     Application
     Software update
     Task sequence

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.267 -->

Manage and monitor phased
deployments
Article • 10/04/2022

This article describes how to manage and monitor phased deployments. Management
tasks include manually beginning the next phase, and suspend or resume a phase.

First, you need to create a phased deployment:

      Application
      Software update
      Task sequence

Move to the next phase
When you select the setting, Manually begin the second phase of deployment, the site
doesn't automatically start the next phase based on success criteria. You need to move
the phased deployment to the next phase.

   1. How to start this action varies based on the type of deployed software:

            Application: Go to the Software Library workspace, expand Application
            Management, and select Applications.

            Software update: Go to the Software Library workspace, and then select one
            of the following nodes:
               Software Updates
                  All Software Updates
                  Software Update Groups
               Windows Servicing, All Windows Updates
               Office 365 Client Management, Office 365 Updates

            Task sequence: Go to the Software Library workspace, expand Operating
            Systems, and select Task Sequences.

   2. Select the software with the phased deployment.

   3. In the details pane, switch to the Phased Deployments tab.

   4. Select the phased deployment, and click Move to next phase in the ribbon.

<!-- p.268 -->

Optionally, use the following Windows PowerShell cmdlet for this task: Move-
CMPhasedDeploymentToNext.

Suspend and resume phases
You can manually suspend or resume a phased deployment. For example, you create a
phased deployment for a task sequence. While monitoring the phase to your pilot
group, you notice a large number of failures. You suspend the phased deployment to
stop further devices from running the task sequence. After resolving the issue, you
resume the phased deployment to continue the rollout.

   1. How to start this action varies based on the type of deployed software:

          Application: Go to the Software Library workspace, expand Application
          Management, and select Applications.

          Software update: Go to the Software Library workspace, and then select one
          of the following nodes:
             Software Updates
                All Software Updates
                Software Update Groups
             Windows Servicing, All Windows Updates
             Office 365 Client Management, Office 365 Updates

          Task sequence: Go to the Software Library workspace, expand Operating
          Systems, and select Task Sequences. Select an existing task sequence, and
          then click Create Phased Deployment in the ribbon.

   2. Select the software with the phased deployment.

   3. In the details pane, switch to the Phased Deployments tab.

   4. Select the phased deployment, and click Suspend or Resume in the ribbon.

<!-- p.269 -->

  ７ Note

  Starting on April 21, 2020, Office 365 ProPlus is being renamed to Microsoft 365
  Apps for enterprise. For more information, see Name change for Office 365
  ProPlus. You may still see the old name in the Configuration Manager product and
  documentation while the console is being updated.

Optionally, use the following Windows PowerShell cmdlets for this task:

     Suspend-CMPhasedDeployment
     Resume-CMPhasedDeployment

Monitor
Phased deployments have their own dedicated monitoring node, making it easier to
identify phased deployments you have created and navigate to the phased deployment
monitoring view. From the Monitoring workspace, select Phased Deployments, then
double-click one of the phased deployments to see the status.

<!-- p.270 -->

This dashboard shows the following information for each phase in the deployment:

     Total devices or Total resources: How many devices are targeted by this phase.

     Status: The current status of this phase. Each phase can be in one of the following
     states:

        Deployment created: The phased deployment created a deployment of the
        software to the collection for this phase. Clients are actively targeted with this
        software.

        Waiting: The previous phase hasn't yet reached the success criteria for the
        deployment to continue to this phase.

        Suspended: An administrator suspended the deployment.

     Progress: The color-coded deployment states from clients. For example: Success, In
     Progress, Error, Requirements Not Met, and Unknown.

<!-- p.271 -->

Success criteria tile
Use the Select Phase drop-down list to change the display of the Success Criteria tile.
This tile compares the Phase Goal against the current compliance of the deployment.
With the default settings, the phase goal is 95%. This value means that the deployment
needs a 95% compliance to move to the next phase.

In the example, the phase goal is 65%, and the current compliance is 66.7%. The phased
deployment automatically moved to the second phase, because the first phase met the
success criteria.

The phase goal is the same as the Deployment success percentage on the Phase
Settings for the next phase. For the phased deployment to start the next phase, that
second phase defines the criteria for success of the first phase. To view this setting:

   1. Go to the phased deployment object on the software, and open the Phased
     Deployment Properties.

   2. Switch to the Phases tab. Select Phase 2 and click View.

   3. In the phase Properties window, switch to the Phase Settings tab.

   4. View the value for Deployment success percentage in the Criteria for success of the
     previous phase group.

For example, the following properties are for the same phase as the success criteria tile
shown above where the criteria is 65%:

<!-- p.272 -->

PowerShell
Use the following Windows PowerShell cmdlets to manage phased deployments:

Automatically create phased deployments
    New-CMApplicationAutoPhasedDeployment
    New-CMSoftwareUpdateAutoPhasedDeployment
    New-CMTaskSequenceAutoPhasedDeployment

Manually create phased deployments
    New-CMSoftwareUpdatePhase
    New-CMSoftwareUpdateManualPhasedDeployment
    New-CMTaskSequencePhase
    New-CMTaskSequenceManualPhasedDeployment

<!-- p.273 -->

Get existing phased deployment objects
     Get-CMApplicationPhasedDeployment
     Get-CMSoftwareUpdatePhasedDeployment
     Get-CMTaskSequencePhasedDeployment
     Get-CMPhase

Monitor phased deployment status
     Get-CMPhasedDeploymentStatus

Manage existing phased deployments
     Move-CMPhasedDeploymentToNext
     Resume-CMPhasedDeployment
     Suspend-CMPhasedDeployment

Modify existing phased deployments
     Set-CMApplicationPhasedDeployment
     Set-CMSoftwareUpdatePhase
     Set-CMSoftwareUpdatePhasedDeployment
     Set-CMTaskSequencePhase
     Set-CMTaskSequencePhasedDeployment
     Remove-CMApplicationPhasedDeployment
     Remove-CMSoftwareUpdatePhasedDeployment
     Remove-CMTaskSequencePhasedDeployment

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.274 -->

Manage Windows as a service using
Configuration Manager
Article • 06/20/2024

Applies to: Configuration Manager (current branch)

In Configuration Manager, you can view the state of Windows as a service in your
environment. Create servicing plans to form deployment rings, and keep Windows
systems up to date when new builds are released. You can also view alerts when
Windows clients are near end of support for the build version.

For more information about Windows servicing options, see Overview of Windows as a
Service.

Prerequisites
      For Configuration Manager version 2203 or later, the WebView2 console extension
      must be installed. If needed, select the notification bell in the top right corner of
      the console to install the extension.

      Windows computers must use Configuration Manager software updates with
      Windows Server Update Services (WSUS) for software update management. When
      a computer uses Windows Update for Business or Windows Insiders, it isn't
      evaluated in Windows servicing plans. For more information, see Integration with
      Windows Update for Business.

      Use a supported WSUS version:
           WSUS 10.0.14393 (role in Windows Server 2016) (2023-02 Cumulative Update,
           or a later cumulative update)
           WSUS 10.0.17763 (role in Windows Server 2019) (Requires Configuration
           Manager 1810 or later) (2023-02 Cumulative Update, or a later cumulative
           update)
           WSUS 10.0.20348 (role in Windows Server 2022) (2023-02 Cumulative Update,
           or a later cumulative update)

      Enable heartbeat discovery. The data that the Windows servicing dashboard
      displays comes from discovery. For more information, see Configure heartbeat
      discovery.

            Tip

<!-- p.275 -->

       The following Windows channel and build information is discovered and
       stored in the following attributes:

          Operating System Readiness Branch: Specifies the Windows channel.
                Don't defer upgrades ( 0 ): The semi-annual channel - targeted
                Defer upgrades ( 1 ): The semi-annual channel
                LTSB ( 2 ): The long-term servicing channel (LTSC)

          Operating System Build: Specifies the OS build. For example, 10.0.18362
          for Windows 10, version 1903, or 10.0.19041 for Windows 10, version
          2004.

     Configure the service connection point for Online, persistent connection mode.
     When the site is in offline mode, you don't see data updates in the dashboard until
     you get Configuration Manager servicing updates. For more information, see
     About the service connection point.

     Configure and synchronize software updates. Before any Windows feature
     upgrades are available in the Configuration Manager console, select the Upgrades
     classification, and synchronize software updates. For more information, see
     Prepare for software updates management.

     Verify the configuration of the following client settings, to make sure they're
     appropriate for your environment:
        Specify thread priority for feature updates
        Enable Dynamic Update for feature updates

Windows servicing dashboard in version 2103
or later
(Introduced in version 2103)

Starting in version 2103, the Windows Servicing dashboard was simplified to make it
more relevant. Servicing plan and Windows 10 ring information were removed from the
dashboard. The following charts are displayed for the selected Collection:

Feature Update Versions: Displays the distribution of Windows major releases. This
chart as previously called Windows 10 Usage.

Quality Update Versions: This chart displays the top five revisions of Windows across
your devices.

<!-- p.276 -->

Windows 10 Latest Feature Update (added in 2111): This chart shows the number of
devices that installed the latest feature update for Windows 10.

Windows 11 Latest Feature Update (added in 2111): This chart shows the number of
devices that installed the latest feature update for Windows 11.

Latest Feature Update (versions 2103 and 2107): This chart shows the number of
devices that installed the latest feature update.

Collection Errors: This tile shows the number of devices that failed with the specified
error code. For more information, see Analyze SetupDiag errors.

Errors Timeline: Displays the top errors and the number of devices with each error over
the course of time for the chosen collection.

                                                                                     

  ） Important

<!-- p.277 -->

       The Windows Servicing dashboard in Configuration Manager versions 2103
       and 2107 includes Windows 11 devices with the latest version of Windows 10.
       They don't distinguish a version for Windows 11.

       The information shown in the Windows servicing dashboard is provided for
       your convenience and only for use internally within your company. You should
       not solely rely on this information to confirm update compliance. Be sure to
       verify the accuracy of the information provided to you. For more detailed
       information about Windows builds, see the Product Lifecycle dashboard.

Windows 10 servicing dashboard in version
2010 and earlier
The Windows 10 servicing dashboard provides you with information about Windows 10
computers in your environment, servicing plans, and compliance information. The data
in the Windows 10 servicing dashboard is dependent on the service connection point.
The dashboard has the following tiles:

     Windows 10 Usage: Provides a breakdown of public builds of Windows 10.
     Windows Insiders builds are listed as Other, and any builds that aren't yet known
     to your site. The service connection point downloads metadata that informs it
     about the Windows builds, and then this data is compared against discovery data.

     Windows 10 Rings: Provides a breakdown of Windows 10 by channel and
     readiness state. The LTSC segment includes all LTSC versions.

     Create Service Plan: Provides a quick way to create a servicing plan. You specify
     the name, collection, deployment package, and readiness state. It only displays the
     top 10 collections by size, smallest first, and the top 10 deployment packages by
     most recently modified. It uses default values for the other settings. Select
     Advanced Settings to start the Create Servicing Plan wizard, where you can
     configure all of the service plan settings.

     Expired: Displays the percentage of devices that are on a build of Windows 10
     that's past its end of service. Configuration Manager determines the percentage
     from the metadata downloaded by the service connection point and compares it
     against discovery data. A build that's past its end of service is no longer receiving
     monthly cumulative updates, which include security updates. Upgrade the
     computers in this category to the latest build version. Configuration Manager

<!-- p.278 -->

     rounds up to the next whole number. For example, if you have 10,000 computers
     and only one on an expired build, the tile displays 1% .

     Expire Soon: Displays the percentage of computers that are on a build that's within
     four months of its end of service. It's similar to the Expired tile otherwise.

     Alerts: Displays any active alerts.

     Service Plan Monitoring: Displays servicing plans that you've created and a chart
     of the compliance for each. This tile gives you a quick overview of the current state
     of the servicing plan deployments. If an earlier deployment ring meets your
     expectations for compliance, then you can select a later servicing plan (deploying
     ring). Select Deploy Now instead of waiting for the servicing plan rules to
     automatically trigger.

     Collection errors: Starting in version 2010, this tile shows the number of devices
     that failed with the specified error code. You can scope the tile to a specific
     collection. For more information, see Analyze SetupDiag errors.

For more detailed information about Windows 10 builds, see the Product Lifecycle
dashboard.

  ） Important

  The information shown in the Windows 10 servicing dashboard is provided for your
  convenience and only for use internally within your company. You should not solely
  rely on this information to confirm update compliance. Be sure to verify the
  accuracy of the information provided to you.

Drill through required updates
You can drill through compliance statistics to see which devices require a specific
Windows feature update. To view the device list, you need permission to view updates
and the collections the devices belong to.

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Windows Servicing, and select the All Windows Feature Updates node.

   2. Select any update that is required by at least one device.

   3. Look at the Summary tab and find the pie chart under Statistics.

<!-- p.279 -->

   4. To drill down into the device list, select View Required next to the pie chart. This
     action takes you to a temporary node under Devices. Here you can see the devices
     requiring the update. You can also take actions for the node such as creating a new
     collection from the list.

Servicing plan workflow
Windows servicing plans in Configuration Manager are much like automatic deployment
rules for software updates. You create a servicing plan with the following criteria that
Configuration Manager evaluates:

     Upgrades classification: Only updates that are in the Upgrades classification are
     evaluated.

     Readiness state: The readiness state defined in the servicing plan is compared with
     the readiness state for the upgrade. The metadata for the upgrade is retrieved
     when the service connection point checks for updates.

     Time deferral: The number of days that you specify for How many days after
     Microsoft has published a new upgrade would you like to wait before deploying
     in your environment in the servicing plan. If the current date is after the release
     date plus the configured number of days, Configuration Manager evaluates
     whether to include an upgrade in the deployment.

     When an upgrade meets the criteria, the servicing plan adds the upgrade to the
     deployment package, distributes the package to distribution points, and deploys
     the upgrade to the collection. It does these actions based on the settings that you
     configure in the servicing plan. Monitor the deployments with the Service Plan
     Monitoring tile on the Windows servicing dashboard. For more information, see
     Monitor software updates.

  ７ Note

  Windows 10, version 1903 and later was added to Microsoft Update as its own
  product rather than being part of the Windows 10 product like earlier versions. This
  change caused you to do a number of manual steps to make sure that your clients
  see these updates. We've helped reduce the number of manual steps you have to
  take for the new product in Configuration Manager version 1906. For more
  information, see Configuring products for versions of Windows 10.

<!-- p.280 -->

Windows servicing plan
As you deploy Windows, you can create one or more servicing plans. These plans define
the deployment rings that you want in your environment. Then monitor them in the
Windows servicing dashboard. Servicing plans use only the Upgrades software updates
classification, not cumulative updates for Windows. For cumulative updates, continue to
use the software updates workflow. The end-user experience with a servicing plan is the
same as with software updates, including the settings that you configure in the servicing
plan.

  ７ Note

  You can use a task sequence to deploy an upgrade for each Windows build, but it
  requires more manual work. You would need to import the updated source files as
  an OS upgrade package, and then create and deploy the task sequence to the
  appropriate set of computers. However, a task sequence provides additional
  customized options, such as the pre-deployment and post-deployment actions.

You can create a basic servicing plan from the Windows servicing dashboard. After you
specify the name, collection, deployment package, and readiness state, Configuration
Manager creates the servicing plan with default values for the other settings. You can
also start the Create Servicing Plan wizard to configure all of the settings.

Create a servicing plan with the Create Servicing Plan
wizard
   1. In the Configuration Manager console, go to the Software Library workspace,
        expand Windows Servicing, and then select the Servicing Plans node.

   2. On the Home tab of the ribbon, in the Create group, select Create Servicing Plan.

   3. On the General page of the Create Servicing Plan Wizard, configure the following
        settings:

             Name: Specify the name for the servicing plan. The name must be unique,
             help to describe the goal of the servicing plan, and identify it from others in
             the Configuration Manager site. The name can't include the following
             characters: less than ( < ), greater than ( > ), or ampersand ( & ).

             Description: Optionally, specify a description for the servicing plan. The
             description could provide an overview of the servicing plan. You might note
