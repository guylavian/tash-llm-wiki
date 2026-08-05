---
title: "App management documentation — pages 121-160"
type: reference
domain: sccm
slug: sccm-intune-configmgr-apps-p0121-0160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-apps-p0121-0160
family: sccm
documentKind: "doc"
abstract: "Create phased deployments with Configuration Manager Applies to: Configuration Manager (current branch) Phased deployments automate a coordinated, sequenced rollout of software across multiple collections. For example, deploy software to a pilot collection, and then automaticall"
---

# App management documentation — pages 121-160

<!-- p.121 -->

Create phased deployments with
Configuration Manager
Applies to: Configuration Manager (current branch)

Phased deployments automate a coordinated, sequenced rollout of software across multiple
collections. For example, deploy software to a pilot collection, and then automatically continue
the rollout based on success criteria. Create phased deployments with the default of two phases,
or manually configure multiple phases.

Create phased deployments for the following objects:

     Task sequence
        The phased deployment of task sequences doesn't support PXE or media installation
     Application
     Software update
        You can't use an automatic deployment rule (ADR) with a phased deployment

Prerequisites
Security scope
Deployments created by phased deployments aren't viewable to any administrative user that
doesn't have the All security scope. For more information, see Security scopes.

Distribute content
Before creating a phased deployment, distribute the associated content to a distribution point.

     Application: Select the target application in the console and use the Distribute Content
     action in the ribbon. For more information, see Deploy and manage content.

     Task sequence: You have to create referenced objects like the OS upgrade package before
     creating the task sequence. Distribute these objects before creating a deployment. Use the
     Distribute Content action on each object, or the task sequence. To view status of all
     referenced content, select the task sequence, and switch to the References tab in the details
     pane. For more information, see the specific object type in Prepare for OS deployment.

<!-- p.122 -->

     Software update: create the deployment package and distribute it. Use the Download
     Software Updates Wizard. For more information, see Download software updates.

Phase settings
These settings are unique to phased deployments. Configure these settings when creating or
editing the phases to control the scheduling and behavior of the phased deployment process.

Optionally, use the following Windows PowerShell cmdlets to manually configure phases for
software update and task sequence phased deployments:

     New-CMSoftwareUpdatePhase
     New-CMTaskSequencePhase

Criteria for success of the first phase
     Deployment success percentage: Specify the percent of devices that need to successfully
     complete the deployment for the first phase to succeed. By default, this value is 95%. In
     other words, the site considers the first phase successful when the compliance state for 95%
     of the devices is Success for this deployment. The site then continues to the second phase,
     and creates a deployment of the software to the next collection.

     Number of devices successfully deployed: Specify the number of devices that need to
     successfully complete the deployment for the first phase to succeed. This option is useful
     when the size of the collection is variable, and you have a specific number of devices to
     show success before moving to the next phase.

Conditions for beginning second phase of deployment after
success of the first phase
     Automatically begin this phase after a deferral period (in days): Choose the number of
     days to wait before beginning the second phase after the success of the first. By default, this
     value is one day.

     Manually begin the second phase of deployment: The site doesn't automatically begin the
     second phase after the first phase succeeds. This option requires that you manually start the
     second phase. For more information, see Move to the next phase.

       ７ Note

<!-- p.123 -->

        This option isn't available for phased deployments of applications.

Gradually make this software available over this period of time
(in days)
Configure this setting for the rollout in each phase to happen gradually. This behavior helps
mitigate the risk of deployment issues, and decreases the load on the network that is caused by
the distribution of content to clients. The site gradually makes the software available depending
on the configuration for each phase. Every client in a phase has a deadline relative to the time the
software is made available. The time window between the available time and deadline is the same
for all clients in a phase. The default value of this setting is zero, so by default the deployment
isn't throttled. Don't set the value higher than 30.

Configure the deadline behavior relative to when the software
is made available

<!-- p.124 -->

   Installation is required as soon as possible: Set the deadline for installation on the device
   as soon as the device is targeted.

   Installation is required after this period of time: Set a deadline for installation a certain
   number of days after device is targeted. By default, this value is seven days.

Automatically create a default two-phase deployment
 1. Start the Create Phased Deployment wizard in the Configuration Manager console. This
   action varies based on the type of software you're deploying:

        Application: Go to the Software Library, expand Application Management, and select
        Applications. Select an existing application, and then choose Create Phased
        Deployment in the ribbon.

        Software update: Go to the Software Library, expand Software Updates, and select
        All Software Updates. Select one or more updates, and then choose Create Phased
        Deployment in the ribbon.

        This action is available for software updates from the following nodes:
           Software Updates
              All Software Updates
              Software Update Groups
           Windows Servicing, All Windows Updates
           Office 365 Client Management, Office 365 Updates

        Task sequence: Go to the Software Library workspace, expand Operating Systems,
        and select Task Sequences. Select an existing task sequence, and then choose Create
        Phased Deployment in the ribbon.

 2. On the General page, give the phased deployment a Name, Description (optional), and
   select Automatically create a default two phase deployment.

 3. Select Browse and choose a target collection for both the First Collection and Second
   Collection fields. For a task sequence and software updates, select from device collections.
   For an application, select from user or device collections. Select Next.

     ） Important

     The Create Phased Deployment wizard doesn't notify you if a deployment is potentially
     high-risk. For more information, see Settings to manage high-risk deployments and

<!-- p.125 -->

       the note when you Deploy a task sequence.

   4. On the Settings page, choose one option for each of the scheduling settings. For more
     information, see Phase settings. Select Next when complete.

   5. On the Phases page, see the two phases that the wizard creates for the specified collections.
     Select Next. These instructions cover the procedure to automatically create a default two-
     phase deployment. The wizard lets you add, remove, reorder, edit, or view phases for a
     phased deployment. For more information on these additional actions, see Create a phased
     deployment with manually configured phases.

   6. Confirm your selections on the Summary tab, and then select Next to complete the wizard.

  ７ Note

  Starting on April 21, 2020, Office 365 ProPlus is being renamed to Microsoft 365 Apps for
  enterprise. For more information, see Name change for Office 365 ProPlus. You may still
  see the old name in the Configuration Manager product and documentation while the
  console is being updated.

Optionally, use the following Windows PowerShell cmdlets for this task:

     New-CMApplicationAutoPhasedDeployment
     New-CMSoftwareUpdateAutoPhasedDeployment
     New-CMTaskSequenceAutoPhasedDeployment

Create a phased deployment with manually
configured phases
Create a phased deployment with manually configured phases for a task sequence. Add up to 10
additional phases from the Phases tab of the Create Phased Deployment wizard.

  ７ Note

  You can't currently manually create phases for an application. The wizard automatically
  creates two phases for application deployments.

   1. Start the Create Phased Deployment wizard for either a task sequence or software updates.

<!-- p.126 -->

2. On the General page of the Create Phased Deployment wizard, give the phased deployment
  a Name, Description (optional), and select Manually configure all phases.

3. From the Phases page of the Create Phased Deployment wizard, the following actions are
  available:

       Filter the list of deployment phases. Enter a string of characters for a case-insensitive
       match of the Order, Name, or Collection columns.

       Add a new phase:

        a. On the General page of the Add Phase Wizard, specify a Name for the phase, and
          then browse to the target Phase Collection. The additional settings on this page are
          the same as when normally deploying a task sequence or software updates.

        b. On the Phase Settings page of the Add Phase Wizard, configure the scheduling
          settings, and select Next when complete. For more information, see Settings.

               ７ Note

               You can't edit the phase settings, Deployment success percentage or Number
               of devices successfully deployed, on the first phase. These settings only apply
               to phases that have a previous phase.

        c. The settings on the User Experience and Distribution Points pages of the Add
          Phase Wizard are the same as when normally deploying a task sequence or
          software updates.

        d. Review the settings on the Summary page, and then complete the Add Phase
          Wizard.

       Edit: This action opens the selected phase's Properties window, which has tabs the
       same as the pages of the Add Phase Wizard.

       Remove: This action deletes the selected phase.

          ２ Warning

          There is no confirmation, and no way to undo this action.

<!-- p.127 -->

          Move Up or Move Down: The wizard orders the phases by how you add them. The
          most recently added phase is last in the list. To change the order, select a phase, and
          then use these buttons to move the phase's location in the list.

             ） Important

             Review the phase settings after changing the order. Make sure the following
             settings are still consistent with your requirements for this phased deployment:
                Criteria for success of the previous phase
                Conditions for beginning this phase of deployment after success of the
                previous phase

   4. Select Next. Review the settings on the Summary page, and then complete the Create
     Phased Deployment wizard.

Optionally, use the following Windows PowerShell cmdlets for this task:

     New-CMSoftwareUpdateManualPhasedDeployment
     New-CMTaskSequenceManualPhasedDeployment

After you create a phased deployment, open its properties to make changes:

     Add additional phases to an existing phased deployment.

     If a phase isn't active, you can Edit, Remove, or Move it up or down. You can't move it
     before an active phase.

     When a phase is active, it's read-only. You can't edit it, remove it, or move its location in the
     list. The only option is to View the properties of the phase.

     An application phased deployment is always read-only.

Next steps
Manage and monitor phased deployments:

     Application
     Software update
     Task sequence

<!-- p.128 -->

Last updated on 10/04/2022

<!-- p.129 -->

Approve applications in Configuration
Manager
ﾃ     Summarize this article for me

Applies to: Configuration Manager (current branch)

When deploying an application in Configuration Manager, you can require approval before
installation. Users request the application in Software Center, and then you review the request
in the Configuration Manager console. You can approve or deny the request.

    ７ Note

    Starting in version 2111, you can also use most approval behaviors with application
    groups.

Approval settings
The application approval behavior depends upon whether you enable the recommended
optional app approval experience. One of the following approval settings appears on the
Deployment Settings page of the application deployment:

An administrator must approve a request for this application
on the device

    ７ Note

    Configuration Manager doesn't enable this feature by default. Before using it, enable the
    optional feature Approve application requests for users per device. For more
    information, see Enable optional features from updates.

    If you don't enable this feature, you see the prior experience.

The administrator approves any user requests for the application before the user can install it
on the requested device. If the administrator approves the request, the user is only able to
install the application on that device. The user must submit another request to install the
application on another device. This option is grayed out when the deployment purpose is
Required, or when you deploy the application to a device collection.

<!-- p.130 -->

  ７ Note

  To take advantage of new Configuration Manager features, first update clients to the latest
  version. While new functionality appears in the Configuration Manager console when you
  update the site and console, the complete scenario isn't functional until the client version
  is also the latest.

View Application Requests under Application Management in the Software Library
workspace of the Configuration Manager console. There's a Device column in the list for each
request. When you take action on the request, the Application Request dialog also includes the
device name from which the user submitted the request.

If a request isn't approved within 30 days, it's removed. Reinstalling the client might cancel any
pending approval requests.

When you require approval on a deployment to a device collection, the app isn't displayed in
Software Center. If you require approval on a deployment to a user collection, the app is
displayed in Software Center. You can still hide it from users with the client setting, Hide
unapproved applications in Software Center. For more information, see Software Center client
settings.

After you've approved an application for installation, you can Deny the request in the
Configuration Manager console. If users haven't already installed the application, this action
stops them from installing new copies of the application from Software Center. If an
application was previously approved and installed, when you Deny the request for the
application, the client uninstalls the application from the user's device.

If you approve an app request in the console, and then deny it, you can approve it again. The
app is reinstalled on the client after you approve it.

Automate the approval process with the Approve-CMApprovalRequest PowerShell cmdlet. This
cmdlet includes the InstallActionBehavior parameter. Use this parameter to specify whether to
install the application right away or during non-business hours.

You can see which deployments require approval. Select an app in the Applications node. In
the details pane, switch to the Deployments tab. There's a column displayed by default,
Requires Approval.

Retry the install of pre-approved applications

You can retry the installation of an app that you previously approved for a user or device. The
approval option is only for available deployments. If the user uninstalls the app, or if the initial

<!-- p.131 -->

install process fails, Configuration Manager doesn't reevaluate its state and reinstall it. This
feature allows a support technician to quickly retry the app install for a user that calls for help.

   1. Open the Configuration Manager console as a user that has the Approve permission on
     the Application object. For example, the Application Administrator or Application
     Author built-in roles have this permission.

   2. Deploy an app that requires approval, and approve it.

         Tip

        Alternatively, install an application for a device. It creates an approved request for
        the app on the device.

If the application doesn't install successfully, or the user uninstalls the app, use the following
process to retry:

   1. In the Configuration Manager console, go to the Software Library workspace, expand
     Application Management, and select the Application Requests node.

   2. Select the previously approved app. In the Approval Request group of the ribbon, select
     Retry install.

Other app approval resources
     Application approval improvements in ConfigMgr 1810
     Updates to the application approval process in Configuration Manager

Require administrator approval if users request this
application

  ７ Note

  This experience applies if you don't enable the recommended optional app approval
  experience.

The administrator approves any user requests for the application before the user can install it.
This option is grayed out when the deployment purpose is Required, or when you deploy the
application to a device collection.

<!-- p.132 -->

Application approval requests are displayed in the Application Requests node, under
Application Management in the Software Library workspace. If a request isn't approved within
30 days, it's removed. Reinstalling the client might cancel any pending approval requests.

After you've approved an application for installation, you can Deny the request in the
Configuration Manager console. This action doesn't cause the client to uninstall the application
from any devices. It stops users from installing new copies of the application from Software
Center.

Email notifications
You can configure email notifications for application approval requests. When a user requests
an application, you receive an email. Click links in the email to approve or deny the request,
without requiring the Configuration Manager console.

You can define the email addresses of the users who can approve or deny the request while
creating a new deployment for the application. If you need to change the list of email
addresses afterwards, go to the Monitoring workspace, expand Alerts, and select the
Subscriptions node. Select Properties from one of the Approve application via email
subscriptions that's related to your application deployment.

If there is more than one alert, you can determine which alert goes with which deployment.
Open the alert properties, and view the list of Selected alerts on the General tab. The
deployment is enabled as the alert for this subscription.

Users can add a comment to the request from Software Center. This comment shows on the
application request in the Configuration Manager console. That comment also shows in the
email. Including this comment in the email helps the approvers make a better decision to
approve or deny the request.

Prerequisites

To send email notifications and take action on internal network

With these prerequisites, recipients receive an email with notification of the request. If they are
on the internal network, they can also approve or deny the request from the email.

     Enable the optional feature Approve application requests for users per device.

     Configure email notification for alerts.

          ７ Note

<!-- p.133 -->

       The administrative user that deploys the application needs permission to create an
       alert and subscription. If this user doesn't have these permissions, they'll see an error
       at the end of the Deploy Software Wizard: "You do not have security rights to
       perform this operation."

     Set up the administration service in Configuration Manager.

  ７ Note

  If you have multiple child primary sites in a hierarchy, configure these prerequisites for
  each primary site where you want to enable this feature. The links in the email notification
  are for the administration service at the primary site.

To take action from internet

With these additional optional prerequisites, recipients can approve or deny the request from
anywhere they have internet access.

     Enable the SMS Provider administration service through the cloud management gateway.
     In the Configuration Manager console, go to the Administration workspace, expand Site
     Configuration, and select the Servers and Site System Roles node. Select the server with
     the SMS Provider role. In the details pane, select the SMS Provider role, and select
     Properties in the ribbon on the Site Role tab. Select the option to Allow Configuration
     Manager cloud management gateway traffic for administration service.

     Install a supported version of the .NET Framework. Starting in version 2107, the SMS
     Provider requires .NET version 4.6.2, and version 4.8 is recommended. In version 2103 and
     earlier, this role requires .NET 4.5 or later. For more information, Site and site system
     prerequisites.

     Set up a cloud management gateway.

       ７ Note

       This scenario doesn't support CMG deployments with a virtual machine scale set
       until Configuration Manager version 2207 or later is installed.

     Onboard the site to Azure services for Cloud Management.

     Enable Microsoft Entra user Discovery.

<!-- p.134 -->

   Manually configure settings in Microsoft Entra ID:

      1. Go to the Azure portal   as a user with Global Administrator permissions. Go to
        Microsoft Entra ID, and select App registrations.

           ） Important

           The Microsoft Entra Global Administrator role is a highly privileged role and
           should only be used when another role can't be used. This feature requires the
           Global Administrator role. For other features, Microsoft recommends using
           roles with the fewest permissions. To learn more, see Fundamentals of role-
           based administration for Configuration Manager.

      2. Select the Client application created for Configuration Manager Cloud
        Management integration.

      3. In the Manage menu, select Authentication.

         a. Add a new Single-page application type if not already present.

         b. In the Redirect URIs section, paste in the following path: https://<CMG
           FQDN>/CCM_Proxy_ServerAuth/ImplicitAuth

         c. Replace <CMG FQDN> with the fully qualified domain name (FQDN) of your cloud
           management gateway (CMG) service. For example, GraniteFalls.Contoso.com.

         d. For Configuration Manager version 2111 and later, in the Implicit grant and
           hybrid flows section, select the following options:
              Access tokens (used for implicit flows)
              ID tokens (used for implicit and hybrid flows)

         e. Then select Save.

     ７ Note

     If on an existing Client Registration Application the Redirect URI needs to be
     updated, it will need to be created as SPA and older Redirect URI being removed.

Configure email approval
 1. In the Configuration Manager console, deploy an application as available to a user
   collection. On the Deployment Settings page, enable it for approval. Then enter one or

<!-- p.135 -->

     more email addresses to receive notification. Separate email addresses with a semi-colon
     ( ; ).

        ７ Note

        Anyone in your Microsoft Entra organization who receives the email can approve the
        request. Don't forward the email to others unless you want them to take action.

   2. As a user, request the application in Software Center.

   3. You receive an email notification within five minutes. The content of the email is similar to
     the following example:

  ７ Note

  The link to approve or deny is for one-time use. For example, you configure a group alias
  to receive notifications. Meg approves the request. Now Bruce can't deny the request.

Review the NotiCtrl.log file on the site server for troubleshooting.

Maintenance
Configuration Manager stores the information about the application approval request in the
site database. For requests that are canceled or denied, the site deletes the request history
after 30 days. You can configure this deletion behavior with the Delete Aged Application
Request Data site maintenance task. The site never deletes any approved or pending
application requests.

Next steps
Monitor applications from the Configuration Manager console

<!-- p.136 -->

Last updated on 02/24/2026

<!-- p.137 -->

Install applications for a device
Article • 10/04/2022

From the Configuration Manager console you can install applications to a device in real
time. This feature can help reduce the need for separate collections for every
application.

  ７ Note

  Starting in version 2111, this behavior also supports application groups. When this
  article refers to an application, it also applies to app groups.

Prerequisites
      Enable the optional feature Approve application requests for users per device.

      Deploy the application as Available to a device collection.

         On the Deployment Settings page of the deployment wizard, select the
         following option: An administrator must approve a request for this application
         on the device.

           ７ Note

           With these deployment settings, no policy is sent to the client. The app
           isn't shown as available in Software Center, and a user can't install the app
           with this deployment. After you use this action to install the app, the user
           can run it, and see its installation status in Software Center.

      Your user account needs the following permissions:

         Application: Read, Approve

         Collection: Read, Read Resource, Modify Resource, View Collected File

      For example, the Application Administrator built-in role has these permissions.

   Tip

<!-- p.138 -->

  In a hierarchy, wait for application and deployment information to replicate to the
  primary site to which the target client is assigned.

Process
   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select the Devices node. Select the target device, and then select
     the Install application action in the ribbon. Starting in version 2111, select the
     Install Application Group action for an app group.

   2. Select one or more applications from the list. The list only shows applications that
     you already deployed with the prerequisite settings.

This action triggers the installation of the selected pre-deployed applications on the
device.

To see status of the approval request, in the Software Library workspace, expand
Application Management, and select the Application Requests node.

Monitor the app installation the same as usual in the Deployments node of the
Monitoring workspace.

See also
Approve applications

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.139 -->

Check for running executable files
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configure an application deployment to check if certain executable files are running on
the client. Use this option to check for processes that might disrupt the installation of
the application. If one of these executable files is running, the client blocks the
installation of the deployment type. The user must close the running executable file
before the client can install the deployment type. For deployments with a purpose of
required, the client can automatically close the running executable file.

   1. Open the Properties for the deployment type.

   2. Switch to the Install Behavior tab, and select Add.

   3. In the Add Executable File window, enter the name of the target executable file.
      Optionally, enter a friendly name for the application to help you identify it in the
      list.

   4. Select OK to save and close the deployment type properties window.

   5. When you deploy the application, select the option to Automatically close any
      running executables you specified on the install behavior tab of the deployment
      type properties dialog box. This option is on the Deployment Settings tab of the
      deployment properties.

  ７ Note

  If you configure an application to check for running executable files, and include it
  in the Install Application task sequence step, the task sequence will fail to install it.
  If you don't configure this task sequence step to continue on error, then the entire
  task sequence fails.

Client behaviors and user notifications
After clients receive the deployment, the following behavior applies:

      If you deployed the application as Available, and a user tries to install it, the client
      prompts the user to close the specified running executable files before proceeding
      with the installation.

<!-- p.140 -->

     If you deployed the application as Required, and specified to Automatically close
     any running executables you specified on the install behavior tab of the
     deployment type properties dialog box, then the client displays a notification. It
     informs the user that the specified executable files are automatically closed when
     the application installation deadline is reached. If the user tries to install the
     application before the deadline, the deployment will fail. It notifies the user that
     the installation couldn't complete because the specified executables are running.

        Schedule these dialogs in the Computer Agent group of client settings. For
        more information, see Computer agent.

        If you don't want the user to see these messages, select the option to Hide in
        Software Center and all notifications on the User Experience tab of the
        deployment's properties. For more information, see User Experience settings.

     If you deployed the application as Required, and didn't specify to Automatically
     close any running executables you specified on the install behavior tab of the
     deployment type properties dialog box, then the installation of the app fails if
     one or more of the specified applications are running.

Next steps
     Plan for user notifications when you deploy applications

     Create deployment types for an application

     Deploy applications

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.141 -->

Share an application from Software
Center
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can copy a hyperlink to an application in Software Center using the       Share button
in the Application Details view. You can only share hyperlinks for applications. If the
application becomes unavailable, the hyperlink opens a window with an application
unavailable message.

   1. Choose Applications, and then choose the application.
   2. Select the       Share button.
   3. Select Copy in the window.
   4. Paste the URL into an email to share the application.

   Tip

  To create a link in an Outlook email, press CTRL + K and then paste the URL.

Feedback
Was this page helpful?      Yes        No

Provide product feedback

<!-- p.142 -->

Simulate application deployments with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can use simulated deployments to test an application deployment without installing
or uninstalling the application. A simulated deployment evaluates the detection method,
requirements, and dependencies for a deployment type. It reports the results in the
Deployments node of the Monitoring workspace. Use the procedure in this topic to
simulate an application deployment in Configuration Manager.

  ７ Note

  You cannot use simulated deployments for collections of mobile devices.

  You cannot deploy an application with a deployment purpose of Uninstall if a
  simulated deployment of the same application is active.

Configure a simulated application deployment
   1. In the Configuration Manager console, select one of the following:

            A collection of users.
            A collection of devices.
            A Configuration Manager application.

   2. On the Home tab, in the Deployment group, choose Simulate Deployment.

   3. In the Simulate Application Deployment Wizard, set the following details for your
      simulated deployment:

            Application. Choose Browse, and then select the application you want to
            create a simulated deployment for.

            Collection. Choose Browse, and then select the collection that you want to
            use for the simulated deployment.

            Action. From the drop-down list, select whether you want to simulate the
            installation or the uninstallation of the selected application.

<!-- p.143 -->

           Deploy automatically with or without user login. If this option is checked,
           the clients evaluate the simulated deployment whether or not the clients are
           logged in.

   4. Click Next, review the information on the Summary page, and then finish the
     wizard to create the simulated application deployment.

   5. Simulated applications appear in the Deployments node of the Monitoring
     workspace, with a purpose of Simulate. For more information about how to
     monitor application deployments, see Monitor applications from the Configuration
     Manager console.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.144 -->

Microsoft Edge Management
Article • 10/04/2022

Applies to: Configuration Manager (Current Branch)

The all-new Microsoft Edge is ready for business. You can deploy Microsoft Edge,
version 77 and later to your users. A PowerShell script is used to install the Microsoft
Edge build selected. The script also turns off automatic updates for Microsoft Edge so
they can be managed with Configuration Manager.

Deploy Microsoft Edge
Admins can pick the Beta, Dev, or Stable channel, along with a version of the Microsoft
Edge client to deploy. Each release incorporates learnings and improvements from our
customers and community. For more information, see Microsoft Edge release schedule.

Prerequisites for deploying
For clients targeted with a Microsoft Edge deployment:

      PowerShell Execution Policy can't be set to Restricted.
         PowerShell is executed to perform the installation.

      The Microsoft Edge installer, Attack Surface Reduction rules engine for tenant
      attach, and CMPivot are currently signed with the Microsoft Code Signing PCA
      2011 certificate. If you set PowerShell execution policy to AllSigned, then you need
      to make sure that devices trust this signing certificate. You can export the
      certificate from a computer where you've installed the Configuration Manager
      console. View the certificate on "C:\Program Files (x86)\Microsoft Endpoint
      Manager\AdminConsole\bin\CMPivot.exe" , and then export the code signing

      certificate from the certification path. Then import it to the machine's Trusted
      Publishers store on managed devices. You can use the process in the following
      blog, but make sure to export the code signing certificate from the certification
      path: Adding a Certificate to Trusted Publishers using Intune .

The device running the Configuration Manager console needs access to the following
endpoints for deploying Microsoft Edge:

                                                                          ﾉ   Expand table

<!-- p.145 -->

 Location                                                 Use

 https://aka.ms/cmedgeapi                                 Information about releases of
                                                          Microsoft Edge

 https://edgeupdates.microsoft.com/api/products?          Information about releases of
 view=enterprise                                          Microsoft Edge

 http://dl.delivery.mp.microsoft.com                      Content for Microsoft Edge
                                                          releases

Verify Microsoft Edge update policies
Starting in version 2002, you can create a Microsoft Edge application that's set up to
receive automatic updates rather than having automatic updates disabled. This change
allows you to choose to manage updates for Microsoft Edge with Configuration
Manager or allow Microsoft Edge to automatically update. When creating the
application, select Allow Microsoft Edge to automatically update the version of the
client on the end user's device on the Microsoft Edge Settings page. If you previously
used Group Policy to change this behavior, Group Policy will overwrite the setting made
by Configuration Manager during installation of Microsoft Edge. For more information,
see Microsoft Edge update policies.

<!-- p.146 -->

                                                                                      

Create a deployment
Create a Microsoft Edge application using the built-in application experience, which
makes Microsoft Edge easier to manage:

   1. In the console, under Software Library, there's a new node called Microsoft Edge
     Management.

   2. Select Create Microsoft Edge Application from either the ribbon, or by right-
     clicking on the Microsoft Edge Management node.

<!-- p.147 -->

3. On the Application Settings page of the wizard, specify a name, description, and
  location for the content for the app. Ensure the content location folder you specify
  is empty.

4. On the Microsoft Edge Settings page, select:

       The channel to deploy
       The version to deploy
       If you want to Allow Microsoft Edge to automatically update the version of
       the client on the end user's device (added in version 2002)

5. On the Deployment page, decide if you want to deploy the application. If you
  select Yes, you can specify your deployment settings for the application. For more
  information about deployment settings, see Deploy applications.

6. In Software Center on the client device, the user can see and install the
  application.

<!-- p.148 -->

Log files for deployment

                                                                                   ﾉ   Expand table

 Location      Log                   Use

 Site server   SMSProv.log           Shows details if the creation of the app or deployment fails.

 Varies        PatchDownloader.log   Shows details if the content download fails

 Client        AppEnforce.log        Shows installation information

Update Microsoft Edge
The All Microsoft Edge updates node is under Microsoft Edge Management. This node
helps you manage updates for all Microsoft Edge channels.

   1. To get updates for Microsoft Edge, ensure you have the Updates classification and
      the Microsoft Edge product selected for synchronization.

                                                                                              

   2. In the Software Library workspace, expand Microsoft Edge Management and click
      on the All Microsoft Edge Updates node.

<!-- p.149 -->

   3. If needed, click Synchronize Software Updates in the ribbon to start a
     synchronization. For more information, see Synchronize software updates.

   4. Manage and deploy Microsoft Edge updates like any other update, such as adding
     them to your automatic deployment rule. Some of the common updates tasks you
     can do from the All Microsoft Edge Updates node include:

          Create a phased deployment
          Manually deploy software updates
          Download software updates

Microsoft Edge Management dashboard
Starting in Configuration Manager 2002, the Microsoft Edge Management dashboard
provides you insights on the usage of Microsoft Edge and other browsers. In this
dashboard, you can:

     See how many of your devices have Microsoft Edge installed
     See how many clients have different versions of Microsoft Edge installed.
        This chart doesn't include Canary Channel.
     Have a view of the installed browsers across devices
     Have a view of preferred browser by device
        Currently for the 2002 release, this chart will be empty.

Prerequisites for the dashboard

<!-- p.150 -->

For Configuration Manager version 2203 or later, the WebView2 console extension must
be installed. If needed, select the notification bell in the top right corner of the console
to install the extension.

Enable the following properties in the below hardware inventory classes for the
Microsoft Edge Management dashboard:

     Installed Software - Asset Intelligence (SMS_InstalledSoftware)
        Software Code
        Product Name
        Product Version

     Default Browser (SMS_DefaultBrowser)
        Browser Program ID

     Browser Usage (SMS_BrowserUsage)
        BrowserName
        UsagePercentage

View the dashboard
From the Software Library workspace, click Microsoft Edge Management to see the
dashboard. Change the collection for the graph data by clicking Browse and choosing
another collection. By default your five largest collections are in the drop-down list.
When you select a collection that isn't in the list, the newly selected collection takes the
bottom spot on your drop-down list.

                                                                                        

<!-- p.151 -->

   Tip

  The Power BI sample reports for Configuration Manager includes a report called
  Edge Status. This report can also help with monitoring Edge deployment.

Known issues

Hardware inventory may fail to process
Hardware inventory for devices might fail to process. Errors similar to the one below
may be seen in the Dataldr.log file:

  text

  Begin transaction: Machine=<machine>
  *** [23000][2627][Microsoft][SQL Server Native Client 11.0][SQL
  Server]Violation of PRIMARY KEY constraint 'BROWSER_USAGE_HIST_PK'. Cannot
  insert duplicate key in object 'dbo.BROWSER_USAGE_HIST'. The duplicate key
  value is (XXXX, Y). : dbo.dBROWSER_USAGE_DATA
  ERROR - SQL Error in
  ERROR - is NOT retyrable.
  Rollback transaction: XXXX

Mitigation: To work around this issue, disable the collection of the Browser Usage
(SMS_BrowerUsage) hardware inventory class.

Next steps
Monitor applications

Monitor software updates

Manage and monitor phased deployments

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.152 -->

Deploy App-V virtual applications with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When you use Configuration Manager to manage virtual applications, you gain the
following benefits:

      A single management infrastructure

      Scalability, deployment, and content distribution features, like collections and user
      device affinity

      Advanced application management features

      Operating system deployment, software and hardware inventory, software
      metering, and asset intelligence to support virtual applications

For more information about how to create and sequence applications with Microsoft
Application Virtualization (App-V), see Application Virtualization 4 documentation.

In addition to the other Configuration Manager requirements and procedures for
creating an application, you must take the following considerations into account when
you create and deploy virtual applications:

      To deploy virtual applications to computers, you must have the Configuration
      Manager client and App-V Client installed on your computers. Client devices can
      include desktop and portable computers, and Virtual Desktop Infrastructure (VDI)
      clients. The Configuration Manager and App-V Client software work together to
      deliver, locate, and launch virtual application packages. The Configuration Manager
      client manages the delivery of virtual application packages to the App-V Client.
      The App-V Client runs the virtual application on the client.

      To deploy a virtual application, you must first create the virtual application by using
      the App-V Application Virtualization Sequencer. The sequencer monitors the
      installation and setup process for an application and records the information that
      is needed for the application to run in a virtual environment. You can also use the
      sequencer to set which files and configurations apply to all users, and which
      configurations users can customize.

      When you sequence an application, you must save the package to a location that
      Configuration Manager can access. You can then create an application deployment

<!-- p.153 -->

     that contains this virtual application.

     Configuration Manager does not support the use of the shared read-only cache
     feature of App-V 4.6.

     Configuration Manager supports the Shared Content Store feature in App-V 5.

     When you create a deployment type for a virtual application, Configuration
     Manager creates the deployment type by using the contents of the application
     manifest file. This is an XML file that has information about the virtual application.
     Additionally, Configuration Manager creates requirements for the deployment type
     based on the contents of the App-V .osd file that has information about the
     supported operating systems for the virtual application.

     To deploy virtual applications in Configuration Manager, client computers must
     have at minimum the App-V 4.6 SP1 or a later version of the client installed.

     Before you can successfully deploy virtual applications, update the App-V client
     with the latest hotfix.

     When you use connection groups in App-V 5.0, your deployed virtual applications
     can share the same file system and registry on client computers. Unlike standard
     virtual applications, these applications can share data with one another.
     Additionally, connection groups preserve user settings for the applications that
     they contain. App-V virtual environments in Configuration Manager are used to set
     up connection groups on client computers. Virtual environments are created or
     changed on client computers when the application is installed or when clients next
     evaluate their installed applications. You can prioritize these applications so that
     when multiple applications try to change a file system or registry value, the
     application that has the highest priority takes precedence. For more information,
     see Create App-V virtual environments.

Supported App-V versions
Configuration Manager supports the following versions of App-V:

     App-V 4.6: To use virtual applications in Configuration Manager, client computers
     must have the App-V 4.6 SP1, App-V 4.6 SP2, or App-V 4.6 SP3 client installed.

     Before you can successfully deploy virtual applications, update the App-V 4.6 client
     with the latest hotfix.

     App-V 5, App-V 5.0 SP1, App-V 5.0 SP2, App-V 5.0 SP3, and App-V 5.1: For App-V
     5.0 SP2, you must install Hotfix Package 5    or use App-V 5.0 SP3.

<!-- p.154 -->

     App-V 5.2: This is built into Windows 10 Education (1607 and later), Windows 10
     Enterprise (1607 and later), and Windows Server 2016.

For more information about App-V in Windows 10, see the following topics:

     What's new in App-V
     Getting Started with App-V for Windows 10
     Upgrading to App-V for Windows 10 from an existing installation

Steps to manage App-V virtual applications
To manage App-V virtual applications, follow these steps:

   1. Sequence: Sequencing is the process of converting an application into a virtual
     application by using the App-V sequencer.

   2. Create: Use the Create Deployment Type Wizard to import the sequenced
     application into a Configuration Manager deployment type that you can then add
     to an application. You can also create virtual environments that allow multiple
     virtual applications to share settings.

   3. Distribute: Distribution is the process of making App-V applications available on
     Configuration Manager distribution points.

   4. Deploy: Deployment is the process of making the application available on client
     computers. This is called publishing and streaming in an App-V full infrastructure.

Configuration Manager virtual application
delivery methods
Configuration Manager supports two methods for delivery of virtual applications to
clients: streaming delivery and local delivery (download and execute).

When you're deciding which delivery method to use, compare the reduced disk space
requirement for streaming delivery against the guaranteed availability of App-V
applications in local delivery. The increased client disk space that is required for local
delivery might be preferable to streaming delivery so that users always have the
application available from any location.

Streaming delivery

<!-- p.155 -->

When you use Configuration Manager to manage the App-V Client, it supports the
streaming of virtual applications through HTTP or HTTPS from a distribution point.
Streaming through HTTP or HTTPS is enabled by default and is set up in the dialog box
for distribution point properties. When you deploy a virtual application to client
computers and a user runs the virtual application, the Configuration Manager client
contacts a management point to determine which distribution point to use. Then, the
application is streamed from the distribution point.

Use the information in this table to help you decide if streaming delivery is the best
delivery method for you:

                                                                                        ﾉ    Expand table

 Advantages                          Disadvantages

 This method uses standard           Virtual applications are not streamed until the user runs the
 network protocols to stream         application for the first time. In this scenario, a user might
 package content from                receive program shortcuts for virtual applications and then
 distribution points.                disconnect from the network before running the virtual
                                     applications for the first time. If the user tries to run the virtual
 Program shortcuts for virtual       application while the client is offline, the user sees an error and
 applications invoke a               can't run the virtualized application because a Configuration
 connection to the distribution      Manager distribution point is not available to stream the
 point, so the virtual application   application. The application will be unavailable until the user
 delivery is on demand.              reconnects to the network and runs the application.

 This method works well for          To avoid this, you can use the local delivery method for virtual
 clients with high-bandwidth         application delivery to clients, or you can enable the Internet-
 connections to the distribution     based client management for streaming delivery.
 points.

 Updated virtual applications
 distributed throughout the
 enterprise are available as
 clients receive policy that
 informs them that the current
 version is superseded and they
 download only the changes
 from the previous version.

 Access permissions are defined
 at the distribution point to
 prevent users from accessing
 unauthorized applications or
 packages.

<!-- p.156 -->

Local delivery (download and execute)
Download and execute is most common approach when using Configuration Manager
because this approach closely mimics how other application formats are delivered with
Configuration Manager. When you use the local delivery method, the Configuration
Manager client first downloads the entire virtual application package into the
Configuration Manager client cache. The Configuration Manager then instructs the App-
V Client to stream the application from the Configuration Manager cache into the App-
V cache. If you deploy a virtual application to client computers and its content is not in
the App-V cache, the App-V Client streams the application content from the
Configuration Manager client cache into the App-V cache, and then runs the
application. After the application runs successfully, you can set the Configuration
Manager client to delete any older versions of the package at the next deletion cycle, or
to persist them in Configuration Manager client cache. Persisting content locally can
take advantage of package content delivery optimization methods such as BranchCache
and PeerCache.

Use the information in this table to help you decide if local delivery is the best delivery
method for you:

                                                                                   ﾉ   Expand table

 Advantages                                                      Disadvantages

 The standard distribution point functionality is used to        Disk space that equals up to twice
 download the package by using Background Intelligent            the size of the virtual application
 Transfer Service (BITS).                                        package is required on the client
                                                                 when the virtual application is
 Virtual application package contents are delivered locally to   persisted in the Configuration
 the client. This means that users can run them when their       Manager cache.
 computer is not connected to the network.

 This method is suitable for slow or unreliable network
 connections and for computers that only occasionally
 connect to the network.

 Configuration Manager uses Remote Differential
 Compression (RDC) to send to clients only the bytes within
 the files that have changed when virtual application
 package content is updated. The Configuration Manager
 client uses RDC to build a new version of a virtual
 application package based on the current version of the
 package and any changes sent to the client.

 This method provides application resiliency for mobile users
 or disconnected users. Admins can choose to persist the

<!-- p.157 -->

 Advantages                                                          Disadvantages

 package in the Configuration Manager cache after delivery
 if the virtual application was deployed with an install action.
 The package in the Configuration Manager client cache
 serves as a local, reliable streaming source for the App-V
 Client to pull the package into its cache.

Deployment from an image
You can also preinstall virtual applications on a computer and then create an image of
that computer for deployment to other computers. But if the virtual application package
was created at a different site, the binary delta replication will not be used to download
updates to the application. This option can be useful in a virtual desktop infrastructure
when you want applications to be available immediately instead of downloading the
applications after the user logs on.

Migrating from an App-V infrastructure to a
Configuration Manager and App-V
infrastructure
Use the following table to help you plan a migration from an existing App-V
infrastructure to virtual application management with Configuration Manager.

                                                                                        ﾉ   Expand table

 Step                                                              More information

 Examine your current virtual applications to choose the           No additional information.
 applications that you want to migrate to your
 Configuration Manager infrastructure.

 Evaluate the users and devices to which the virtual               Create Configuration Manager
 applications will be deployed.                                    collections to group together the
                                                                   users and devices to which you want
                                                                   to deploy the virtual applications. See
                                                                   Introduction to collections.

 Migrate App-V 5 connection groups to Configuration                See the Migrate App-V 5 connection
 Manager virtual environments.                                     groups to Configuration Manager
                                                                   virtual environments section in this
                                                                   topic.

<!-- p.158 -->

Step                                                            More information

Investigate to find out if any of your virtual applications     For easier management, you can add
exist as full applications in your Configuration Manager        the virtual application as a new
infrastructure.                                                 deployment type to the existing full
                                                                application. See Create applications.

Create applications to replace your existing App-V              See Introduction to application
packages.                                                       management and Create applications.

Configuration Manager begins to manage virtual                  No additional information.
applications on a client after the first deployment of a
virtual application. After this, Configuration Manager
must manage all App-V applications on the computer.

Distribute the content to the appropriate distribution          See Manage content and content
points to enable local delivery of applications.                infrastructure.

Deploy the application to Configuration Manager clients.        See Deploy applications.

If the App-V application was created with an earlier
version of the sequencer that does not create a manifest
XML file, you can open it and save it in a newer version
of the sequencer to create the file. This file is required to
deploy virtual applications with Configuration Manager.

App-V supports the virtual application packages that are
created with the SoftGrid 4.1 SP1 or 4.2 versions of the
sequencer.

If the applications were previously installed locally, you
must uninstall them before you deploy a virtual version
of the application.

Configuration Manager no longer supports using                  See Planning for the migration of
packages and programs that contain virtual applications.        objects to Configuration Manager
When you migrate from Configuration Manager 2007 to             current branch.
Configuration Manager current branch, Configuration
Manager converts these packages into applications.

Configuration Manager 2007 advertisements are
converted into the following deployment types:

- Migrating App-V packages with no advertisement: One
deployment type that uses the default deployment type
settings.

- Migrating App-V packages with one advertisement:
One deployment type that uses the same settings as the
Configuration Manager 2007 advertisement.

<!-- p.159 -->

 Step                                                    More information

 - Migrating App-V packages with multiple
 advertisements: A deployment type, for each
 Configuration Manager 2007 advertisement, that uses
 the settings for that advertisement.

Migrating App-V 5 connection groups to
Configuration Manager virtual environments
App-V virtual environments in Configuration Manager allow virtual applications that you
have deployed to share the same file system and registry on client computers. This
means that unlike standard virtual applications, these applications can share data with
each other. Virtual environments are created or changed on client computers when the
application is installed or when clients next evaluate their installed applications. Virtual
environments are similar to connection groups in standalone App-V 5.

When you migrate connection groups from standalone App-V 5 to Configuration
Manager virtual environments, you must ensure that Configuration Manager correctly
manages the connection groups that already exist on client computers, and that the
user's environment within those connection groups is preserved.

To convert App-V 5 connection groups to Configuration Manager virtual environments:

   1. Create Configuration Manager applications for all applications that existed in App-
     V.

   2. Deploy the applications to users or devices with a deployment purpose of
     Required. Deployments to users must be deployed to the same users who used
     the application in App-V. Deployments to computers must be deployed to the
     same computers that had the application in App-V.

   3. After the deployment is finished, create virtual environments that match the
     connection groups that are published in standalone App-V. The virtual
     environment must have the same packages (specifically, App-V 5 deployment
     types) in the same order.

For information about how to create an App-V virtual environment, see How to create
App-V virtual environments.

Alternatively, you can delete all connection groups from the App-V Client before you
begin to deploy applications with Configuration Manager. But any settings that users

<!-- p.160 -->

might have saved in App-V connection groups will be lost.

Dynamic Suite Composition in App-V 4.6
Dynamic Suite Composition is a feature that lets you define one virtual application
package as having a dependency on another virtual application package. When the
application is run, the App-V Client hosts the primary package and the dependent
package in the same virtual environment for the application.

For you to use this feature with Configuration Manager, both packages must be
deployed and registered with the App-V Client. To ensure that dependent package
content is hosted locally on the client computer, set up the application deployment for
local delivery (download and execute).

For more information about App-V Dynamic Suite Composition, see your App-V
documentation.

Converting App-V 4.6 applications to App-V 5
applications
The application package format has changed between App-V 4.6 and App-V 5.
Applications that have been sequenced by using App-V 4.6 are no longer supported.
But App-V 5 has a package converter tool that you can use to convert applications. For
more information, see How to convert a package created in a previous version of App-V.

Use the following steps to convert App-V 4.6 applications to App-V 5 applications:

   1. Convert or resequence the App-V 4.6 packages into the App-V 5 format.

   2. Deploy the App-V 5 client to computers in your hierarchy.

   3. Create new applications that contain deployment types for your App-V 5
     applications, and create supersedence rules to supersede the App-V 4.6
     applications.

   4. Create virtual environments as required.

   5. Deploy the new App-V 5 applications to computers.

User and deployment configuration files
