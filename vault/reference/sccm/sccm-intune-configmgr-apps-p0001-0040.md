---
title: "App management documentation — pages 1-40"
type: reference
domain: sccm
slug: sccm-intune-configmgr-apps-p0001-0040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-apps-p0001-0040
family: sccm
documentKind: "doc"
abstract: "App management documentation Use Configuration Manager to manage and deploy applications, scripts, and packages. Automate the deployments, or let users install apps from Software Center. About app management ｅ OVERVIEW Introduction to app management Plan for app management Plan"
---

# App management documentation — pages 1-40

<!-- p.1 -->

App management documentation
Use Configuration Manager to manage and deploy applications, scripts, and packages.
Automate the deployments, or let users install apps from Software Center.

  About app management

  ｅ OVERVIEW
  Introduction to app management

  Plan for app management

  Plan for Software Center

  ｇ TUTORIAL
  Create and deploy an app

  Get started

  ｃ HOW-TO GUIDE
  Create apps

  Create and run PowerShell scripts

  ｀ DEPLOY
  Deploy apps

  Deploy and update Microsoft Edge

  Top tasks

  ｃ HOW-TO GUIDE
  Create app groups

  Approve apps

<!-- p.2 -->

Install apps for a device

User device affinity

Monitor app usage with software metering

ｉ REFERENCE
Troubleshoot app deployments

Common error codes for app installation

Packages and programs

<!-- p.3 -->

Create and deploy an application with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

In this article, you'll learn how to create an application with Configuration Manager. In
this example, you'll create and deploy the CMPivot standalone installer. For the
purposes of this exercise, you'll configure it to only install on devices that are running
Windows 11. Along the way, you'll learn about many of the things you can do to
manage applications effectively.

   Tip

  The CMPivot standalone source file is in the Configuration Manager installation
  media or on the site server in the CD.Latest folder. Find it in the following folder:
   \SMSSETUP\TOOLS\CMPivot\CMPivot.msi

This procedure is designed to give you an overview of how to create and deploy
Configuration Manager applications. However, it doesn't cover all the configuration
options, or how to create and deploy applications for other platforms.

For specific details that are relevant to each platform, see one of the following articles:

      Create Windows applications
      Create Windows Phone applications
      Create Mac computer applications
      Create Windows Embedded applications

If you're already familiar with Configuration Manager applications, you can skip this
article. To learn about all the options that are available when you create and deploy
applications, see Create applications.

Before you start
Make sure that you've reviewed the information in Introduction to application
management. That article helps you prepare your site to install applications and
understand the terminology that's used here.

<!-- p.4 -->

Make sure that the installation files for the CMPivot standalone app are in an accessible
location on your network. This example uses the following path:
\\cm01.contoso.com\SMS_XYZ\cd.latest\SMSSETUP\TOOLS\CMPivot\CMPivot.msi

Create the application
Use the following procedure to start the Create Application Wizard and create the
application:

   1. In the Configuration Manager console, choose Software Library > Application
     Management > Applications.

   2. On the Home tab, in the Create group, choose Create Application.

   3. On the General page of the Create Application Wizard, choose Automatically
     detect information about this application from installation files. This action pre-
     populates some of the information in the wizard with information that's extracted
     from the installation .msi file. Then specify the following information:

           Type: Choose Windows Installer (*.msi file).

           Location: Select Browse to choose the location of the installation file
           CMPivot.msi. Make sure the location is specified in the form
           \\Server\Share\File.msi for Configuration Manager to locate the installation

           files.

     You'll end up with something that looks like the following screenshot:

<!-- p.5 -->

4. Choose Next. On the Import Information page, you'll see some information about
  the app and any associated files that were imported to Configuration Manager.
  Once you're done, choose Next again.

5. On the General Information page, you can supply further information about the
  application to help you sort and locate it in the Configuration Manager console.

  The Installation program field lets you specify the full command line that will be
  used to install the application on PCs. You can edit this field to add your own
  properties. For example, /q for an unattended installation.

     Tip

    Some of the fields on this page of the wizard might have been filled in
    automatically when you imported the application installation files.

  You'll end up with a screen that looks similar to the following screenshot:

<!-- p.6 -->

   6. Choose Next. On the Summary page, you can confirm your application settings
     and then complete the wizard.

You've finished creating the app. To find it, in the Software Library workspace, expand
Application Management, and then choose Applications. For this example, you'll see:

<!-- p.7 -->

Examine the properties
Now that you've created an application, you can refine the application settings if you
need to. To look at the application properties, select the app, and then, in the Home tab
in the Properties group, choose Properties.

In the CMPivot Properties dialog box, you'll see many items that you can configure to
refine the behavior of the application. For more information about all the settings you
can configure, see Create applications.

For the purposes of this example, you'll just be changing some properties of the
application's deployment type. In the app properties window, switch to the Deployment
Types tab. Select the CMPivot - Windows Installer (*.msi file) deployment type, and
then select Edit.

You'll see a dialog box like this one:

<!-- p.8 -->

Add a requirement
Requirements specify conditions that must be met before an application is installed on a
device. You can choose from built-in requirements or you can create your own. In this
example, you add a requirement that the application will only get installed on devices
that are running Windows 11.

   1. On the deployment type properties page, switch to the Requirements tab.

   2. Select Add to open the Create Requirement window. Specify the following
     information:

          Category: Device

          Condition: Operating system

          Rule type: Value

          Operator: One of

          From the OS list, select All Windows 11 (64-bit).

     You'll end up with a dialog box that looks like this:

<!-- p.9 -->

   3. Select OK to close each property page that you opened. Then return to the
     Applications list in the Configuration Manager console.

   Tip

  Requirements can help reduce the number of Configuration Manager collections
  you need. Because you just specified that the application can only get installed on
  devices that are running Windows 11, you can later deploy this to a collection that
  contains PCs that run many different operating systems. But the application will
  only get installed on Windows 11 devices.

Distribute the application content
Next, to deploy the application to PCs, make sure that the application content is copied
to a distribution point. PCs access the distribution point to install the application.

   Tip

<!-- p.10 -->

  To find out more about distribution points and content management in
  Configuration Manager, see Manage content and content infrastructure.

   1. In the Configuration Manager console, choose Software Library.

   2. In the Software Library workspace, expand Applications. Then, in the list of
     applications, select the CMPivot that you created.

   3. On the Home tab, in the Deployment group, choose Distribute Content.

   4. On the General page of the Distribute Content Wizard, check that the application
     name is correct, and then choose Next.

   5. On the Content page, review the information that will be copied to the distribution
     point, and then choose Next.

   6. On the Content Destination page, choose Add to select one or more distribution
     points, or distribution point groups on which to install the application content.

   7. Complete the wizard.

You can check that the application content was copied successfully to the distribution
point from the Monitoring workspace, under Distribution Status > Content Status.

Deploy the application
Next, deploy the application to a device collection in your hierarchy. In this example, you
deploy the application to the All Systems device collection.

   Tip

  Remember that only Windows 11 computers will install the application because of
  the requirements that you selected earlier.

   1. In the Configuration Manager console, choose Software Library > Application
     Management > Applications.

   2. From the list of applications, select the application that you created earlier
     (CMPivot), and then, on the Home tab in the Deployment group, choose Deploy.

   3. On the General page of the Deploy Software Wizard, choose Browse to select the
     All Systems device collection.

<!-- p.11 -->

   4. On the Content page, check that the distribution point from which you want PCs
     to install the application is selected.

   5. On the Deployment Settings page, make sure that the deployment action is set to
     Install, and the deployment purpose is set to Required.

         Tip

        By setting the deployment purpose to Required, you make sure that the
        application is installed on PCs that meet the requirements that you set. If you
        set this value to Available, then users can install the application on demand
        from Software Center.

   6. On the Scheduling page, you can configure when the application will be installed.
     For this example, select As soon as possible after the available time.

   7. On the User Experience page, choose Next to accept the default values.

   8. Complete the wizard.

Use the information in the following Monitor the application section to see the status
of your application deployment.

Monitor the application
In this section, you'll take a quick look at the deployment status of the application that
you deployed.

   1. In the Configuration Manager console, choose Monitoring > Deployments.

   2. From the list of deployments, select CMPivot.

   3. On the Home tab, in the Deployment group, choose View Status.

   4. Select one of the following tabs to see more status updates about the application
     deployment:

           Success: The application installed successfully on the indicated PCs.

           In Progress: The application is still installing.

           Error: An error occurred installing the application on the indicated PCs.
           Further information about the error is also displayed.

<!-- p.12 -->

           Requirements Not Met: No installation attempt was made on the indicated
           devices because they didn't meet the requirements you configured. In this
           example, because they don't run on Windows 11.

           Unknown: Configuration Manager was unable to report the status of the
           deployment. Check back again later.

   Tip

  There are a few ways you can monitor application deployments. For more
  information, see Monitor applications.

User experience
Users who have PCs that are managed by Configuration Manager and running Windows
11 see a message telling them that they must install the CMPivot application. Once they
accept the deployment, the application gets installed.

Next steps
User notifications

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.13 -->

Plan for and configure application
management in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the information in this article to help you implement the necessary dependencies to
deploy applications in Configuration Manager.

Dependencies external to Configuration
Manager

Internet Information Services (IIS)
IIS is required on the servers that run the following site system roles:

      Management point
      Distribution point

For more information, see Site and site system prerequisites.

Certificates on code-signed applications for mobile
devices
When you code-sign applications to deploy them to mobile devices, don't use a
certificate that was generated by using a Version 3 template (Windows Server 2008,
Enterprise Edition). This certificate template creates a certificate that's incompatible with
Configuration Manager applications for mobile devices.

If you use Active Directory Certificate Services to code-sign applications for mobile
device applications, don't use a Version 3 certificate template.

Audit sign-in events for user device affinity
If you want to automatically create user device affinities, configure clients to audit sign-
in events.

To determine automatic user device affinities, the Configuration Manager client reads
sign-in events of type Success from the Windows security event log. Enable these events

<!-- p.14 -->

with the following two audit policies:

      Audit account logon events
      Audit logon events

To automatically create relationships between users and devices, make sure that these
two settings are enabled on client computers. You can use Windows Group Policy to
configure these settings.

For more information on user device affinity, see Link users and devices with user device
affinity.

Configuration Manager dependencies

Management point
Clients contact a management point to download client policy and to locate content.
Software Center uses the same management point for user-available application
deployments.

Distribution point
Before you can deploy applications to clients, you need at least one distribution point in
the hierarchy. By default, the site server has a distribution point site role enabled during
a standard installation. The number and location of distribution points vary according to
the specific requirements of your environment.

For more information about how to install distribution points and manage content, see
Manage content and content infrastructure.

Reporting services point
To use the reports in Configuration Manager for application management, first install
and configure a reporting services point.

For more information, see Introduction to reporting.

Client settings
Many client settings control how the client installs applications and the user experience
on the device. These client settings include the following groups:

<!-- p.15 -->

     Computer agent
     Computer restart
     Software Center
     Software deployment
     User and device affinity

For more information, see the following articles:

     About client settings
     How to configure client settings

Security permissions for application management
     The Application Author security role includes the required permissions to create,
     change, and retire applications.

     The Application Deployment Manager security role includes required permissions
     to deploy applications.

     The Application Administrator security role has all the permissions from both the
     Application Author and the Application Deployment Manager security roles.

For more information, see Configure role-based administration.

App-V 4.6 SP1 or later client to run virtual applications
To create virtual applications in Configuration Manager, install App-V 4.6 SP1 or later on
devices.

App-V is included with all supported versions of Windows 10 Enterprise edition. For
more information, see Getting started with App-V for Windows 10.

Remove the application catalog
Support ended for the application catalog roles with version 1910. Software Center can
deliver all app deployments without the application catalog. For more information, see
Removed and deprecated features.

Starting in version 2107, you can't update the site if it has either of the application
catalog site system roles. Remove these roles before you update to version 2107.

If your site still has an application catalog, use the following process to remove it:

<!-- p.16 -->

   1. Update all Configuration Manager clients to the latest supported version.

   2. Set branding for Software Center, instead of in the properties of the application
     catalog web site role. For more information, see Software Center client settings.

   3. Review the default and any custom client settings. In the Computer Agent group,
     make sure the Default Application Catalog website point is (none) .

   4. Remove the application catalog website and application catalog web service site
     system roles from all primary sites. For more information, see Uninstall a site
     system role.

After you remove the application catalog roles, Software Center starts using the
management point for user-targeted, available deployments. To verify this behavior on a
specific client, review the SCClient_<username>.log , and look for an entry similar to the
following line:

Using endpoint Url: https://mp.contoso.com/CMUserService_WindowsAuth, Windows
authentication

  ７ Note

  If you have any tools or automation that used the ApplicationViewService.asmx
  SOAP endpoint on the application catalog website point, you need to change it.
  Update the URL in your tool to use the management point user service endpoint.
  For example, https://mp.contoso.com/CMUserService_WindowsAuth

Next steps
Plan for Software Center

Understand user notifications

Security and privacy for application management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.17 -->

Plan for Software Center
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Users change settings, browse for applications, and install applications from Software
Center. When you install the Configuration Manager client on a Windows device, it
automatically installs Software Center as well.

Configure Software Center

  ） Important

  To take advantage of new Configuration Manager features, first update clients to
  the latest version. While new functionality appears in the Configuration Manager
  console when you update the site and console, the complete scenario isn't
  functional until the client version is also the latest.

Use client settings to configure the appearance and behaviors of Software Center. For
more information, see Software Center client settings. The following list is a summary of
some of the configurations:

      Change the branding of Software Center to include your organization's name,
      colors, and logo. For more information, see Brand Software Center.

      Configure which default tabs are visible, and add up to five custom tabs to
      Software Center.

      In Configuration Manager 2103 and earlier, when single sign on with multifactor
      authentication is used, you may not be able to sign into custom tabs that load a
      website that's subject to Conditional Access policies.

      You can configure co-managed devices to use the Company Portal for both Intune
      and Configuration Manager apps. For more information, see Use the Company
      Portal app on co-managed devices.

You can allow users to set in Software Center if they regularly use the computer for
work. This option configures an affinity between the user and device, which can affect
some deployments. For more information, see Link users and devices with user device
affinity.

<!-- p.18 -->

Be aware of the following settings for features that are no longer supported:

      The client setting Use new Software Center in the Computer Agent group is
      enabled by default. The previous version of Software Center is no longer
      supported.

      The client setting Hide application catalog link in Software Center in the Software
      Center Customizations is enabled by default. This link would appear on the
      Installation Status tab of Software Center. The application catalog is no longer
      supported.

For more information, see Removed and deprecated features.

Software Center and user-available applications
When you deploy an app with the purpose Available to a user collection, users can see
these available applications in Software Center. This behavior provides a self-service
capability for users to easily install approved software, without requiring assistance from
IT staff.

Software Center gets application deployment information in policy from the
management point. It uses the same management point from the assigned primary site
as the Configuration Manager client. In a large environment, you can scale client
communication to management points by assigning them to boundary groups.

Users can browse and install user-available applications on Microsoft Entra joined
devices and internet-based, domain-joined devices. For more information, see
Prerequisites to deploy user-available applications.

The site optimizes user-available deployments to reduce policy traffic between the
server and clients. This behavior allows a large number of applications to be available for
the user without significantly affecting performance of the overall infrastructure.

Support for enhanced HTTP
Starting in version 2107, Software Center can take advantage of enhanced HTTP when
the management point is configured for HTTP. This site configuration provides secure
communication without the overhead of managing PKI certificates. When you enable
the site for enhanced HTTP, Software Center prefers secure communication over HTTPS
to get user-available applications from the management point.

    Tip

<!-- p.19 -->

  On any version of Configuration Manager, when you configure the site or the
  management point to require HTTPS communication, Software Center always uses
  HTTPS.

To validate this behavior, on a client review the following log files:

     CCMSDKProvider.log: Shows the client's selection of the HTTPS endpoint on the
     management point. For example: Management URL retrieved: https://...
     SCClient_*.log: Shows the endpoint URL that the client uses to communicate with
     the management point, which should use HTTPS. For example: Using endpoint
     Url: https://mp01.contoso.com:443/CMUserService, AAD authentication

  ７ Note

  To take full advantage of new Configuration Manager features, after you update the
  site, also update clients to the latest version. The complete scenario isn't functional
  until the client version is also the latest.

For more information on how to configure the site, see enhanced HTTP.

Brand Software Center
Change the appearance of Software Center to meet your organization's branding
requirements. This configuration helps users trust Software Center.

Configure Software Center branding
Customize the appearance of Software Center by adding your organization's branding
elements:

     Organization name: Software Center displays this name in the top banner.
     Color scheme: The primary color for the banner and other elements.
     Foreground color: By default, when you select an item, the font color is white.
     Starting in version 2103, you can change this color for better visibility with certain
     primary colors, and better accessibility.
     Logo for Software Center: Your organization's logo helps users to trust Software
     Center.

The following image shows an example of Software Center that's customized with all
four branding settings:

<!-- p.20 -->

Starting in version 2111, you can also configure a Logo for notifications. It's a separate
image file specifically for notifications on devices running Windows 10 or later. Your
organization's logo helps users to trust these notifications. When you deploy software to
a client, the user sees notifications with your logo. For example:

For more information, see the following articles:

     About client settings for Software Center
     How to configure client settings

Branding priorities
Configuration Manager applies the organization name for Software Center according to
the following priorities:

   1. Software Center Customization client setting for Company Name. For more
     information, see About client settings: Software Center.

   2. Computer Agent client setting for Organization name. For more information, see
     About client settings: Computer agent.

<!-- p.21 -->

Next steps
     Software Center user guide

     Plan for and configure application management

     Use the Company Portal app on co-managed devices

  ７ Note

  This article used to include more sections, which have moved to the following
  articles:

        User notifications for required deployments

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.22 -->

User notifications
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Configuration Manager client and Software Center can display notifications to users
that are signed-in to Windows. You can control many of these behaviors through client
settings and the deployment settings.

  ７ Note

  By default, Windows 11 enables focus assist for the first hour after a user signs on
  for the first time. For more information, see Reaching the Desktop and the Quiet
  Period.

  Software Center notifications are currently suppressed during this time. For more
  information, see Turn Focus assist on or off in Windows       .

Required deployments
When users receive required software, and select the Snooze and remind me setting,
they can choose from the following options:

      Later: Specifies that notifications are scheduled based on the notification settings
      configured in client settings.

      Fixed time: Specifies that the notification is scheduled to display again after the
      selected time. For example, if you select 30 minutes, the notification displays again
      in 30 minutes.

<!-- p.23 -->

The maximum snooze time is always based on the notification values configured in the
client settings at every time along the deployment timeline. For example:

     You configure the Deployment deadline greater than 24 hours, remind users
     every (hours) setting on the Computer Agent page for 10 hours.

     The client displays the notification dialog more than 24 hours before the
     deployment deadline.

     The dialog shows snooze options up to but never greater than 10 hours.

     As the deployment deadline approaches, the dialog shows fewer options. These
     options are consistent with the relevant client settings for each component of the
     deployment timeline.

For a high-risk deployment, such as a task sequence that deploys an OS, the user
notification experience is more intrusive. Instead of a transient taskbar notification, a
dialog box like the following displays each time you're notified that critical software
maintenance is required:

Replace toast notifications with dialog window

<!-- p.24 -->

Sometimes users don't see the Windows toast notification about a restart or required
deployment. Then they don't see the experience to snooze the reminder. This behavior
can lead to a poor user experience when the client reaches a deadline.

When software changes are required or deployments need a restart, you have the
option of using a more intrusive dialog window.

Software changes are required
When you deploy an application as required with a deadline in the future, on the User
Experience page of the Deploy Software Wizard, select the following user notification
options:

     Display in Software Center and show all notifications
     When software changes are required, show a dialog window to the user instead
     of a toast notification

Configuring this deployment setting changes the user experience for this scenario.

From the following toast notification:

To the following dialog window:

<!-- p.25 -->

Restart required
In the Computer Restart group of client settings, enable the following option: When a
deployment requires a restart, show a dialog window to the user instead of a toast
notification.

Configuring this client setting changes the user experience for all required deployments
that require a restart of the following types:

     Application
     Task sequence
     Software update

From the following toast notification:

To the following dialog window:

<!-- p.26 -->

Next steps
Device restart notifications

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.27 -->

Security and privacy for application
management in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Security guidance

Centrally specify user device affinity
Manually specify the user device affinity instead of letting users identify their primary
device. Don't enable usage-based configuration.

Don't consider information that's collected from users or from the device to be
authoritative. If you deploy software by using user device affinity that a trusted
administrator doesn't specify, the software might be installed on computers and to users
who aren't authorized to receive that software.

Don't run deployments from distribution points
Always configure deployments to download content from distribution points rather than
run from distribution points. When you configure deployments to download content
from a distribution point and run locally, the Configuration Manager client verifies the
package hash after it downloads the content. The client discards the package if the hash
doesn't match the hash in the policy.

If you configure the deployment to run directly from a distribution point, the
Configuration Manager client doesn't verify the package hash. This behavior means that
the Configuration Manager client can install software that's been tampered with.

If you must run deployments directly from distribution points, use NTFS least
permissions on the packages on the distribution points. Also use internet protocol
security (IPsec) to secure the channel between the client and the distribution points, and
between the distribution points and the site server.

Don't let users interact with elevated processes
If you enable the options to Run with administrative rights or Install for system, don't
let users interact with those applications. When you configure an application, you can

<!-- p.28 -->

set the option to Allow users to view and interact with the program installation. This
setting allows users to respond to any required prompts in the user interface. If you also
configure the application to Run with administrative rights or Install for system, an
attacker at the computer that runs the program could use the user interface to escalate
privileges on the client computer.

Use programs that use Windows Installer for setup and per-user elevated privileges for
software deployments that require administrative credentials. Setup must be run in the
context of a user who doesn't have administrative credentials. Windows Installer per-
user elevated privileges provide the most secure way to deploy applications that have
this requirement.

  ７ Note

  When the user starts the application installation process from Software Center, the
  option to Allow users to view and interact with the program installation can't
  control user interactions with any other processes created by the application
  installer. Because of this behavior, even if you don't select this option, the user may
  still be able to interact with an elevated process. To avoid this issue, don't deploy
  applications that create other processes with user interactions. If you have to install
  this type of application, deploy it as Required and configure the user notification
  experience to Hide in Software Center and all notifications.

Restrict whether users can install software interactively
Configure the Install permissions client setting in the Computer Agent group. This
setting restricts the types of users who can install software in Software Center.

For example, create a custom client setting with Install permissions set to Only
administrators. Apply this client setting to a collection of servers. This configuration
prevents users without administrative permissions from installing software on those
servers.

For more information, see About client settings.

For mobile devices, only deploy signed applications
Deploy mobile device applications only if they're code-signed by a certification authority
(CA) that the mobile device trusts.

For example:

<!-- p.29 -->

     An application from a vendor, which is signed by a public and globally trusted
     certificate provider.

     An internal application that you sign independent from Configuration Manager by
     using your internal CA.

     An internal application that you sign by using Configuration Manager when you
     create the application type and use a signing certificate.

Secure the location of the mobile device application
signing certificate
If you sign mobile device applications by using the Create Application Wizard in
Configuration Manager, secure the location of the signing certificate file, and secure the
communication channel. To help protect against elevation of privileges and man-in-the-
middle attacks, store the signing certificate file in a secured folder.

Use IPsec between the following computers:

     The computer that runs the Configuration Manager console
     The computer that stores the certificate signing file
     The computer that stores the application source files

Instead, sign the application independent of Configuration Manager and before you run
the Create Application Wizard.

Implement access controls
To protect reference computers, implement access controls. When you configure the
detection method in a deployment type by browsing to a reference computer, make
sure that the computer isn't compromised.

Restrict and monitor administrative users
Restrict and monitor the administrative users who you grant the following application
management role-based security roles:

     Application Administrator
     Application Author
     Application Deployment Manager

Even when you configure role-based administration, administrative users who create
and deploy applications might have more permissions than you realize. For example,

<!-- p.30 -->

administrative users who create or change an application can select dependent
applications that aren't in their security scope.

Configure App-V apps in virtual environments with the
same trust level
When you configure Microsoft Application Virtualization (App-V) virtual environments,
select applications that have the same trust level in the virtual environment. Because
applications in an App-V virtual environment can share resources, like the clipboard,
configure the virtual environment so that the selected applications have the same trust
level.

For more information, see Create App-V virtual environments.

Make sure macOS apps are from a trustworthy source
If you deploy applications for macOS devices, make sure that the source files are from a
trustworthy source. The CMAppUtil tool doesn't validate the signature of the source
package. Make sure the package comes from a source that you trust. The CMAppUtil
tool can't detect whether the files have been tampered with.

Secure the cmmac file for macOS apps
If you deploy applications for macOS computers, secure the location of the .cmmac file.
The CMAppUtil tool generates this file, and then you import it to Configuration
Manager. This file isn't signed or validated.

Secure the communication channel when you import this file to Configuration Manager.
To help prevent tampering with this file, store it in a secured folder. Use IPsec between
the following computers:

         The computer that runs the Configuration Manager console
         The computer that stores the .cmmac file

Use HTTPS for web applications
If you configure a web application deployment type, use HTTPS to secure the
connection. If you deploy a web application by using an HTTP link rather than an HTTPS
link, the device could be redirected to a rogue server. Data that's transferred between
the device and server could be tampered with.

<!-- p.31 -->

Security issues
     Low-rights users can change files that record software deployment history on the
     client computer.

     Because the application history information isn't protected, a user can change files
     that report whether an application is installed.

     App-V packages aren't signed.

     App-V packages in Configuration Manager don't support signing. Digital
     signatures verify the content is from a trusted source and wasn't altered in transit.
     There's no mitigation for this security issue. Follow the security best practice to
     download the content from a trusted source and from a secure location.

     Published App-V applications can be installed by all users on the computer.

     When an App-V application is published on a computer, all users who sign in to
     that computer can install the application. You can't restrict the users who can
     install the application after it's published.

Privacy information
Application management lets you run any application, program, or script on any client in
the hierarchy. Configuration Manager has no control over the types of applications,
programs, or scripts that you run or the type of information that they transmit. During
the application deployment process, Configuration Manager might transmit information
that identifies the device and sign-in accounts between clients and servers.

Configuration Manager maintains status information about the software deployment
process. Unless the client communicates by using HTTPS, software deployment status
information isn't encrypted during transmission. The status information isn't stored in
encrypted form in the database.

The use of Configuration Manager application installation to remotely, interactively, or
silently install software on clients might be subject to software license terms for that
software. This use is separate from the Software License Terms for Configuration
Manager. Always review and agree to the Software Licensing Terms before you deploy
software by using Configuration Manager.

Configuration Manager collects diagnostics and usage data about applications, which is
used by Microsoft to improve future releases. For more information, see Diagnostics and
usage data.

<!-- p.32 -->

Application deployment doesn't happen by default and requires several configuration
steps.

The following features help efficient software deployment:

     User device affinity maps a user to devices. A Configuration Manager
     administrator deploys software to a user. The client automatically installs the
     software on one or more computers that the user uses most often.

     Software Center is installed automatically on a device when you install the
     Configuration Manager client. Users change settings, browse for software, and
     install software from Software Center.

User device affinity privacy information
     Configuration Manager might transmit information between clients and
     management point site systems. The information might identify the computer, the
     sign-in account, and the summarized usage for sign-in accounts.

     Unless you configure the management point to require HTTPS communication, the
     information that's transmitted between the client and server isn't encrypted.

     The computer and sign-in account usage information is used to map a user to a
     device. Configuration Manager stores this information on client computers, sends
     it to management points, and then stores it in the site database. By default, the site
     deletes old information from the database after 90 days. The deletion behavior is
     configurable by setting the Delete Aged User Device Affinity Data site maintenance
     task.

     Configuration Manager maintains status information about user device affinity.
     Unless you configure clients to communicate with management points by using
     HTTPS, they don't encrypt status information during transmission. The site doesn't
     store status information in encrypted form in the database.

     Computer and sign-in usage information that's used to establish user and device
     affinity is always enabled. Users and administrative users can supply user device
     affinity information.

Software Center privacy information
     Software Center lets the Configuration Manager administrator publish any
     application, program, or script for users to run. Configuration Manager has no

<!-- p.33 -->

     control over the types of programs or scripts that are published in Software Center
     or the type of information that they transmit.

     Configuration Manager might transmit information between clients and the
     management point. The information might identify the computer and sign-in
     accounts. Unless you configure the management point to require clients connect
     by using HTTPS, the information that's transmitted between the client and servers
     isn't encrypted.

     The information about the application approval request is stored in the
     Configuration Manager database. For requests that are canceled or denied, the
     corresponding request history entries are deleted after 30 days by default. You can
     configure this deletion behavior with the Delete Aged Application Request Data
     site maintenance task. The site never deletes application approval requests that are
     in approved and pending states.

     When you install the Configuration Manager client on a device, it automatically
     installs Software Center.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.34 -->

Prerequisites to deploy user-available
apps
Article • 11/07/2023

Applies to: Configuration Manager (current branch)

When you deploy applications as Available to user collections, then users can browse
Software Center and install the apps they need.

For on-premises domain-joined clients, Software Center uses the user's domain
credentials to get the list of available applications from the management point.

There are other requirements for clients that are internet-based, joined to Microsoft
Entra ID, or both.

Microsoft Entra joined devices
If you deploy applications as available to users, they can browse and install them
through Software Center on Microsoft Entra devices. Configure the following
prerequisites to enable this scenario:

      Enable HTTPS on the management point or enable Enhanced HTTP on the site.

      Integrate the site with Microsoft Entra ID for Cloud Management.
         Configure Microsoft Entra user Discovery.

      Deploy an application as available to a collection of users from Microsoft Entra ID.

      Enable the client setting Use new Software Center in the Computer agent group.

      The client OS must be Windows 10 or later, and joined to Microsoft Entra ID. Either
      as purely cloud domain-joined, or Microsoft Entra hybrid joined.

      To support internet-based clients:

         Deploy a cloud management gateway (CMG).

         Distribute any application content to a content-enabled CMG.

         Enable the client setting: Enable user policy requests from Internet clients in
         the Client Policy group.

      To support clients on the intranet:

<!-- p.35 -->

        Add the content-enabled CMG to a boundary group used by the clients.

        Clients must resolve the fully qualified domain name (FQDN) of the
        management point.

        ７ Note

        For a client detected as on the intranet, but communicating via the cloud
        management gateway (CMG), it uses Microsoft Entra identity for devices
        joined to Microsoft Entra ID. These devices can be cloud-joined or hybrid-
        joined.

Internet-based domain-joined devices
An internet-based, domain-joined device that isn't joined to Microsoft Entra ID and
communicates via a cloud management gateway (CMG) can get apps deployed as
available. The Active Directory domain user of the device needs a matching Microsoft
Entra identity. When the user starts Software Center, Windows prompts them to enter
their Microsoft Entra credentials. They can then see any available apps.

Configure the following prerequisites to enable this functionality:

     Windows 10 or later device, and:

        Joined to your on-premises Active Directory domain.

        Can communicate via CMG.

     The site has discovered the user by both Active Directory and Microsoft Entra user
     discovery.

  ７ Note

  If you apply a software restriction policy to the device, it can block the
  authentication prompt in Windows. Review any domain or local group policies that
  you apply to the device. Then remove any that might interfere with this Software
  Center behavior.

Next steps
Deploy applications

<!-- p.36 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.37 -->

Create applications in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

A Configuration Manager application defines the metadata about application. An
application has one or more deployment types. These deployment types include the
installation files and information that are required to install software on devices. A
deployment type also has rules, such as detection methods, and requirements. These
rules specify when and how the client installs the software.

Create applications using the following methods:

      Automatically create an application and deployment types by reading the
      application installation files:
         Create an application and automatically detect application information
         Create a deployment type and automatically identify deployment type
         information

      Manually create an application and then add deployment types later:
         Create an application and manually specify application information
         Create a deployment type and manually specify deployment type information

      Import an application from a file

This article also includes the following information to configure a deployment type:

      Content
      Task Sequence
      Detection Method
      User Experience
      Requirements
      Return Codes
      Dependencies

Create an application
   1. In the Configuration Manager console, go to the Software Library workspace,
      expand Application Management, and select the Applications node.

<!-- p.38 -->

   2. On the Home tab of the ribbon, in the Create group, select Create Application.

Next, automatically detect or manually specify application information:

     Automatically detect application information to create a basic application with a
     single deployment type. For example, a Windows Installer file that has no
     dependencies or requirements. After you create an application by using this
     procedure, edit it as needed. You can add or change deployment types, and add
     detection methods, dependencies, or requirements.

     Manually specify application information to create more complex applications.
     Define more than one deployment type, dependencies, detection methods, or
     requirements.

Automatically detect application information
   1. On the General page of the Create Application wizard, select Automatically detect
     information about this application from installation files.

   2. In the Type drop-down list, select the application installation file type that you
     want to use to detect application information. For more information about the
     available installation types, see Deployment types supported by Configuration
     Manager.

   3. In the Location box, specify the application installation file that you want to use to
     detect application information. This location is either a network path
     ( \\server\share\filename ) or a store link. You must have access to the network
     path and any subfolders that include application content.

        ） Important

        When you select Windows Installer (*.msi file) as an application type, the site
        imports all of the files in the specified folder. It then sends these files to
        distribution points. Make sure that the specified folder contains only the files
        that are necessary to install the application. Microsoft tests Configuration
        Manager to support up to 20,000 files in the application package. If your
        application has more files, consider creating multiple applications with less
        files.

   4. On the Import Information page of the Create Application wizard, review the
     information, and then select Next. If necessary, select Previous to go back and fix
     any errors.

<!-- p.39 -->

5. On the General Information page of the Create Application wizard, specify the
  following information:

    ７ Note

    If Configuration Manager automatically detects this information from the
    application installation files, it's already populated here. Additionally, the
    displayed options might be different depending on the application type that
    you create.

       General information about the application, like the application Name,
       Administrator comments, Publisher, and Software version. To help you find
       the application in the Configuration Manager console, specify an Optional
       reference, or select Administrative categories.

       Installation program: Specify the installation program and any required
       properties that are needed to install the application deployment type.

           Tip

          If the installation program doesn't appear, choose Browse and browse to
          the installation program location.

       Install behavior: Select one of the three options for how Configuration
       Manager installs this deployment type. For more information on these
       options, see User Experience.

       Use an automatic VPN connection (if configured): If you've deployed a VPN
       profile to the device on which the user launches the app, connect the VPN
       when the app starts. This option is only for Windows 8.1 and Windows Phone
       8.1. On Windows Phone 8.1 devices, if you deploy more than one VPN profile
       to the device, automatic VPN connections aren't supported. For more
       information, see VPN profiles.

       Provision this application for all users on the device: Provision an
       application with a Windows app package for all users on the device. For more
       information, see Create Windows applications.

           Tip

<!-- p.40 -->

             If you're modifying an existing application, this setting is on the User
             Experience tab of the Windows app package deployment type
             properties.

   6. Choose Next, review the application information on the Summary page, and then
     finish the Create Application wizard.

The new application now appears in the Applications node of the Configuration
Manager console. You've finished creating an application.

To add more deployment types or configure other settings, see Create deployment
types for the application.

Manually specify application information
   1. On the General page of the Create Application wizard, select Manually specify the
     application information, and then choose Next.

   2. Specify General Information about the application:

           The application Name is required and must be fewer than 256 characters.

           Administrator comments, Publisher, and Software version are additional
           metadata to further describe the application.

           To help you find the application in the Configuration Manager console,
           specify an Optional reference, or select Administrative categories.

           Date published

           Select users or groups who are responsible for this application as Owners
           and Support contacts. By default, these values are set to your username.

   3. On the Software Center page of the Create Application wizard, specify the
     following information:

           Selected language: In the drop-down list, select the language version of the
           application that you want to set up. Choose Add/Remove to set up more
           languages for this application.

           Localized application name: Specify the application name in the selected
           language.

             ） Important
