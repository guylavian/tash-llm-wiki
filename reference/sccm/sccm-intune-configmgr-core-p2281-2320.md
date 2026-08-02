---
title: "Core infrastructure documentation — pages 2281-2320"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2281-2320
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2281-2320
family: sccm
documentKind: "doc"
abstract: "CMEnroll: Requests and installs the client certificate for a Mac computer so that you can then install the Configuration Manager client Enroll the Mac client Enroll individual clients with the Mac computer enrollment wizard. To automate enrollment for many clients, use the CMEnr"
---

# Core infrastructure documentation — pages 2281-2320

<!-- p.2281 -->

           CMEnroll: Requests and installs the client certificate for a Mac computer so
           that you can then install the Configuration Manager client

Enroll the Mac client
Enroll individual clients with the Mac computer enrollment wizard.

To automate enrollment for many clients, use the CMEnroll tool.

Enroll the client with the Mac computer enrollment
wizard
   1. After you install the client, the Computer Enrollment wizard opens. To manually
     start the wizard, select Enroll from the Configuration Manager preference page.

   2. On the second page of the wizard, provide the following information:

           User name: The user name can be in the following formats:

              domain\name . For example: contoso\mnorth

              user@domain . For example: mnorth@contoso.com

                ） Important

                When you use an email address to populate the User name field,
                Configuration Manager automatically populates the Server name
                field. It uses the default name of the enrollment proxy point server
                and the domain name of the email address. If these names don't
                match the name of the enrollment proxy point server, fix the Server
                name during enrollment.

              The user name and corresponding password must match an Active
              Directory user account that has Read and Enroll permissions on the Mac
              client certificate template.

           Server name: The name of the enrollment proxy point server.

Client and certificate automation with CMEnroll
Use this procedure for automation of client installation and requesting and enrollment
of client certificates with the CMEnroll tool. To run the tool, you must have an Active

<!-- p.2282 -->

Directory user account.

   1. On the Mac computer, navigate to the folder where you extracted the contents of
     the Macclient.dmg file.

   2. Enter the following command: sudo ./ccmsetup

   3. Wait until you see the Completed installation message. Although the installer
     displays a message that you must restart now, don't restart, and continue to the
     next step.

   4. From the Tools folder on the Mac computer, type the following command: sudo
     ./CMEnroll -s <enrollment_proxy_server_name> -ignorecertchainvalidation -u

     '<user_name>'

     After the client installs, the Mac Computer Enrollment wizard opens to help you
     enroll the Mac computer. For more information, see Enroll the client by using the
     Mac computer enrollment wizard.

     Example: If the enrollment proxy point server is named server02.contoso.com, and
     you grant contoso\mnorth permissions for the Mac client certificate template,
     type the following command: sudo ./CMEnroll -s server02.contoso.com -
     ignorecertchainvalidation -u 'contoso\mnorth'

       ７ Note

       If the user name includes any of the following characters, enrollment fails:
        <>"+=, . Use an out-of-band certificate with a user name that doesn't include

       these characters.

       For a more seamless user experience, script the installation steps. Then users
       only have to supply their user name and password.

   5. Type the password for the Active Directory user account. When you enter this
     command, it prompts for two passwords. The first password is for the super user
     account to run the command. The second prompt is for the Active Directory user
     account. The prompts look identical, so make sure that you specify them in the
     correct sequence.

   6. Wait until you see the Successfully enrolled message.

   7. To limit the enrolled certificate to Configuration Manager, on the Mac computer,
     open a terminal window and make the following changes:

<!-- p.2283 -->

      a. Enter the command sudo /Applications/Utilities/Keychain
        Access.app/Contents/MacOS/Keychain Access

     b. In the Keychain Access window, in the Keychains section, choose System. Then
        in the Category section, choose Keys.

      c. Expand the keys to view the client certificates. Find the certificate with a private
        key that you installed, and open the key.

     d. On the Access Control tab, choose Confirm before allowing access.

      e. Browse to /Library/Application Support/Microsoft/CCM, select CCMClient, and
        then choose Add.

      f. Choose Save Changes and close the Keychain Access dialog box.

   8. Restart the Mac computer.

To verify that the client installation is successful, open the Configuration Manager item
in System Preferences on the Mac computer. Also update and view the All Systems
collection in the Configuration Manager console. Confirm that the Mac computer
appears in this collection as a managed client.

   Tip

  To help troubleshoot the Mac client, use the CMDiagnostics tool included with the
  Mac client package. Use it to collect the following diagnostic information:

       A list of running processes
       The macOS X operating system version
       macOS X crash reports relating to the Configuration Manager client including
       CCM*.crash and System Preference.crash.
       The Bill of Materials (BOM) file and property list (.plist) file created by the
       Configuration Manager client installation.
       The contents of the folder /Library/Application
       Support/Microsoft/CCM/Logs.

  The information collected by CmDiagnostics is added to a zip file that is saved to
  the desktop of the computer and is named cmdiag-<hostname>-<datetime>.zip

<!-- p.2284 -->

Manage certificates external to Configuration
Manager
You can use a certificate request and installation method independent from
Configuration Manager. Use the same general process, but include the following
additional steps:

     When you install the Configuration Manager client, use the MP and SubjectName
     command-line options. Enter the following command: sudo ./ccmsetup -MP
     <management point internet FQDN> -SubjectName <certificate subject name> . The

     certificate subject name is case-sensitive, so type it exactly as it appears in the
     certificate details.

     Example: The management point's internet FQDN is server03.contoso.com. The
     Mac client certificate has the FQDN of mac12.contoso.com as a common name in
     the certificate subject. Use the following command: sudo ./ccmsetup -MP
     server03.contoso.com -SubjectName mac12.contoso.com

     If you have more than one certificate that contains the same subject value, specify
     the certificate serial number to use for the Configuration Manager client. Use the
     following command: sudo defaults write com.microsoft.ccmclient SerialNumber -
     data "<serial number>" .

     For example: sudo defaults write com.microsoft.ccmclient SerialNumber -data
     "17D4391A00000003DB"

Renew the Mac client certificate
This procedure removes the SMSID. The Configuration Manager client for Mac requires
a new ID to use a new or renewed certificate.

  ） Important

  After you replace the client SMSID, when you delete the old resource in the
  Configuration Manager console, you also delete any stored client history. For
  example, hardware inventory history for that client.

   1. Create and populate a device collection for the Mac computers that must renew
     the computer certificates.

<!-- p.2285 -->

 2. In the Assets and Compliance workspace, start the Create Configuration Item
   Wizard.

 3. On the General page of the wizard, specify the following information:

         Name: Remove SMSID for Mac

         Type: Mac OS X

 4. On the Supported Platforms page, select all macOS X versions.

 5. On the Settings page, select New. In the Create Setting window, specify the
   following information:

         Name: Remove SMSID for Mac

         Setting type: Script

         Data type: String

 6. In the Create Setting window, for Discovery script, select Add script. This action
   specifies a script to discover Mac computers configured with an SMSID.

 7. In the Edit Discovery Script window, enter the following shell script:

      Shell

      defaults read com.microsoft.ccmclient SMSID

 8. Choose OK to close the Edit Discovery Script window.

 9. In the Create Setting window, for Remediation script (optional), choose Add
   script. This action specifies a script to remove the SMSID when it's found on Mac
   computers.

10. In the Create Remediation Script window, enter the following shell script:

      Shell

      defaults delete com.microsoft.ccmclient SMSID

11. Choose OK to close the Create Remediation Script window.

12. On the Compliance Rules page, choose New. Then in the Create Rule window,
   specify the following information:

         Name: Remove SMSID for Mac

<!-- p.2286 -->

           Selected setting: Choose Browse and then select the discovery script that
           you previously specified.

           In the following values field: The domain/default pair of
           (com.microsoft.ccmclient, SMSID) does not exist.

           Enable the option to Run the specified remediation script when this setting
           is noncompliant.

 13. Complete the wizard.

 14. Create a configuration baseline that contains this configuration item. Deploy the
     baseline to the target collection.

     For more information, see How to create configuration baselines.

 15. After you install a new certificate on Mac computers that have the SMSID removed,
     run the following command to configure the client to use the new certificate:

        Shell

        sudo defaults write com.microsoft.ccmclient SubjectName -string
        <subject_name_of_new_certificate>

See also
Prepare to deploy clients to Macs

Maintain Mac clients

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2287 -->

How to assign clients to a site in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you install the Configuration Manager client, before you can manage the client, it
needs to join a Configuration Manager primary site. The site that a client joins is called
its assigned site. You can't assign a client to a central administration site or a secondary
site.

The assignment process happens after you successfully install the client and it
determines which site manages the computer. You can either directly assign the client to
a site, or use automatic site assignment. With automatic assignment, the client finds an
appropriate site based on its current network location. The client may assign to a
fallback site, if you configure it for the hierarchy.

   ７ Note

   Always assign clients to sites running the same version of Configuration Manager.
   Avoid assigning a client from a later release to a site on an earlier release. If
   necessary, update the primary site to the same Configuration Manager version that
   you use for the clients.

After the client assigns to a site, it remains assigned to that site, even if it changes its IP
address or roams to another site. Only an administrator can manually assign the client
to another site or remove the client assignment.

   ２ Warning

   An exception to a client remaining assigned to a site is if you assign the client on a
   Windows Embedded device with write filters enabled. If you don't first disable write
   filters before you assign the client, the site assignment status of the client reverts to
   its original state when the device next restarts. For example, if you configure the
   client for automatic site assignment, it reassigns on startup and might assign to a
   different site. If the client requires manual site assignment, you have to manually
   reassign it before you can manage it.

   To avoid this behavior, disable the write filters before you assign the client on
   embedded devices. Then enable the write filters after you have verified that site

<!-- p.2288 -->

  assignment was successful.

If assignment fails, the client remains installed, but you can't manage it. A client is
considered unmanaged when it's installed but not assigned to a site. It's also
unmanaged when it's assigned to a site but it can't communicate with a management
point.

Manual site assignment
You can manually assign client computers to a site by using the following two methods:

      Use a client installation property that specifies the site code. For more information,
      see Client installation properties - SMSSITECODE.

      In the Windows Control Panel for Configuration Manager, specify the site code.

  ７ Note

  If you manually assign a client to a site code that doesn't exist, the site assignment
  fails.

Automatic site assignment
Automatic site assignment typically happens during client deployment. To manually start
automatic site assignment, select Find Site on the Advanced tab of the Configuration
Manager control panel. The Configuration Manager client compares its network location
with the boundaries for the hierarchy. When the network location of the client falls
within a boundary group you enabled for site assignment, or the hierarchy is configured
for a fallback site, the client is automatically assigned to that site. This behavior lets
clients easily assign to a site and you don't have to specify a site code.

  ７ Note

  If a client computer has multiple network adapters and multiple IP addresses, the IP
  address used to evaluate client site assignment is assigned randomly.

For more information about how to configure boundary groups for site assignment, see
Define site boundaries and boundary groups.

<!-- p.2289 -->

Configuration Manager clients that use automatic site assignment attempt to find site
boundary groups that you publish to Active Directory Domain Services. If this process
fails, clients can get boundary group information from a management point. This
process can fail if you don't extend the Active Directory schema for Configuration
Manager, or clients are workgroup computers.

When you install the client, you can specify a management point for it to use, or the
client can locate a management point automatically. For more information, see How
clients find site resources and services.

If the client can't find a site in a boundary group for its network location, and the
hierarchy doesn't have a fallback site, the client retries every 10 minutes. It repeats this
process until it assigns to a site.

Configuration Manager clients can't automatically assign to a site if any of the following
conditions apply:

     They are currently assigned to a site.

     They are on the internet or configured as internet-only clients.

     Their network location doesn't fall within one of the boundary groups in the
     hierarchy, and there's no fallback site.

If any of these conditions apply, you have to manually assign the client.

Check site compatibility
After a client has found its assigned site, the site checks the version of the Configuration
Manager client and OS. This check is to make sure that the site can manage the client.
For example, a current branch site can't manage a Configuration Manager 2007 client, or
a client that runs Windows 2000.

If you try to assign a client that runs a legacy OS version, site assignment fails. When you
assign a Configuration Manager 2007 client or a System Center 2012 Configuration
Manager client to a current branch site, assignment succeeds to support automatic
client upgrade. However, until you upgrade the older generation clients, you can't
manage it.

  ７ Note

  To support the site assignment of a Configuration Manager 2007 or a System
  Center 2012 Configuration Manager client to a current branch site, configure

<!-- p.2290 -->

  automatic client upgrade for the hierarchy. For more information, see the How to
  upgrade clients for Windows computers.

Configuration Manager also checks that you've assigned the current branch client to a
site that supports it.

The site compatibility check requires one of the following conditions:

      The client can access site information published to Active Directory Domain
      Services.

      The client can communicate with a management point in the site.

If the site compatibility check fails to finish successfully, the site assignment fails. The
client remains unmanaged until the site compatibility check runs again and succeeds.

An exception to this site compatibility check is when you configure a client for an
internet-based management point. In this case, Configuration Manager doesn't check
site compatibility. If you assign clients to a site that contains internet-based site systems,
and you specify an internet-based management point, make sure that you assign the
client to the correct site.

Scenarios for assignment of legacy clients
The following scenarios might occur during migration from previous versions of
Configuration Manager:

You use automatic site assignment and boundaries overlap
between versions of Configuration Manager

In this case, the client automatically tries to find a current branch site.

The client first checks Active Directory Domain Services. If it finds a current branch site
published, site assignment succeeds. If this check fails, the client then checks for site
information from its assigned management point.

  ７ Note

  You can specify an initial management point for the client during client installation.
  For more information, see Client installation properties - SMSMP.

If both these methods fail, site assignment fails. You need to manually assign the client.

<!-- p.2291 -->

Accidental manual assignment to a legacy site version
For example, you assign a current branch client with a specific site code, and mistakenly
specify a site code for a version of Configuration Manager earlier than System Center
2012 R2 Configuration Manager.

In this case, site assignment fails. Manually reassign the client to a current branch site.

Locate a management point
After the client assigns to a site, it then tries to locate a management point. This process
in itself can be complex, depending upon the situation. For more information about how
the client locates management points and other site resources, see How clients find site
resources and services.

Download site settings
After the client finds a management point, it needs to get client-related site settings.
These settings include:

     The client certificate selection criteria
     Whether to use a certificate revocation list
     The client request port numbers

The client continues to check these settings on a periodic basis.

Clients get these settings from one of the following methods:

     If the client used Active Directory Domain Services for its site compatibility check, it
     downloads these settings for its assigned site from the domain.

     When clients can't get site settings from Active Directory, they download them
     from the management point.

     You specify the settings during client installation. For more information, see About
     client installation properties.

Download client settings
All clients download the default client settings policy and any applicable custom client
settings policies. For more information, see About client settings.

<!-- p.2292 -->

Software Center relies on these client configuration policies. It notifies users that it can't
run until the client downloads the configuration information. Depending on the client
settings that you configure, the initial download of client settings might take a while.
Some client management tasks might not run until this process is complete.

Verify site assignment
You can verify site assignment success by any of the following methods:

     For clients on Windows computers, use the Configuration Manager control panel.
     Verify that it shows the correct site code on the Site tab.

     In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select the Devices node. Verify that the computer shows Yes in the
     Client column and the correct primary site code in the Site Code column.

     Use the reports for client assignment.

     Use the LocationServices.log file on the client.

Roaming to other sites
A client on the internal network is assigned to a primary site. You change the client
computer's network location. It's now in a boundary group for another site. In this
scenario, the client is roaming in the other site. When this site is a secondary site for the
client's assigned site, the client can use a management point in the secondary site to
download policy and upload data. This behavior avoids sending this data over a
potentially slow network. If the client roams into the boundary of another primary site, it
still uses a management point in its assigned site to download policy and upload data.

Clients that roam to other sites can always use management points in other sites for
content location requests. Management points in the current site can give clients a list
of distribution points that have the requested content.

When you configure clients for internet-only client management, they only
communicate with management points in their assigned site. These clients never
communicate with management points in secondary sites or with management points in
other primary sites. This behavior is the same for macOS and on-premises MDM devices
that you enroll to Configuration Manager.

Next steps

<!-- p.2293 -->

How to monitor client deployment status

Monitor and manage clients

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2294 -->

How to configure client status in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before you can monitor Configuration Manager clients and remediate problems,
configure the site's client status settings. These settings specify the parameters that the
site uses to mark clients as inactive. Also configure options to alert you if client activity
falls below a specified threshold.

Configure client status
   1. In the Configuration Manager console, go to the Monitoring workspace, and select
      the Client Status node. On the Home tab of the ribbon, in the Client Status group,
      select Client Status Settings.

   2. Configure the following settings:

        ７ Note

        If a client doesn't meet any of the settings, the site marks it as inactive.

            Client policy requests during the following days: Specify the number of days
            since the client requested policy from the site. The default value is 7 days.

            Compare this value to the Client policy polling interval setting in the Client
            Policy group of client settings. Its default is 60 minutes. In other words, a
            client should poll the site for policy every hour. If it doesn't request policy
            after one week, the site marks it as inactive.

            Heartbeat discovery during the following days: Specify the number of days
            since the client sent a heartbeat discovery record to the site. The default
            value is 7 days.

            Compare this value to the schedule for the Heartbeat discovery method. By
            default, the site runs heartbeat discovery once a week.

            Hardware inventory during the following days: Specify the number of days
            since the client sent a hardware inventory record to the site. The default value

<!-- p.2295 -->

        is 7 days.

        Compare this value to the Hardware inventory schedule setting in the
        Hardware Inventory group of client settings. Its default is seven days.

        Software inventory during the following days: Specify the number of days
        since the client sent a software inventory record to the site. The default value
        is 7 days.

        Compare this value to the Schedule software inventory and file collection
        setting in the Software Inventory group of client settings. Its default is seven
        days.

        Status messages during the following days: Specify the number of days
        since the client sent any status messages to the site. The default value is 7
        days. The client can send status messages for different kinds of activities,
        such as running a task sequence. The site deletes old status messages as part
        of the maintenance task, Delete Aged Status Messages.

 3. Specify the following value to determine how long the site keeps client status
   history data:

        Retain client status history for the following number of days: By default, the
        site keeps client status information for 31 days. This setting doesn't have any
        impact on client or site behavior. It's similar to a maintenance task for client
        status history.

Configure the schedule
 1. In the Configuration Manager console, go to the Monitoring workspace, and select
   the Client Status node. On the Home tab of the ribbon, in the Client Status group,
   select Schedule Client Status Update.

 2. Configure the interval at which you want client status to update.

     ７ Note

     When you change the schedule for client status updates, it doesn't take effect
     until the next scheduled client status update on the previous schedule.

Configure alerts

<!-- p.2296 -->

 1. In the Configuration Manager console, go to the Assets and Compliance
   workspace, and select the Device Collections node.

 2. Select the collection for which you want to configure alerts. On the Home tab of
   the ribbon, in the Properties group, select Properties.

      ７ Note

      You can't configure alerts for user collections.

 3. Switch to the Alerts tab, and select Add.

       Tip

      You can only view the Alerts tab if your security role has permissions for
      alerts.

   Choose the alerts that you want the site to generate for client status thresholds,
   and select OK.

 4. In the Conditions list of the Alerts tab, select each client status alert, and then
   specify the following information:

         Alert Name: Accept the default name or enter a new name for the alert.

         Alert Severity: Choose the alert level that the Configuration Manager console
         displays.

         Raise alert: Specify the threshold percentage for the alert.

Automatic remediation exclusion
 1. On the client computer where you want to disable automatic remediation, open
   the registry editor.

      ２ Warning

      If you use the registry editor incorrectly, you can cause serious problems that
      could require you to reinstall Windows. Microsoft can't guarantee that you
      can solve problems that result from using the registry editor incorrectly. Use it
      at your own risk.

<!-- p.2297 -->

   2. Navigate to the registry key
     HKEY_LOCAL_MACHINE\Software\Microsoft\CCM\CcmEval.

   3. Change the value for the NotifyOnly entry:

              TRUE : The client won't automatically remediate any problems that it finds. The

              site still notifies you in the Monitoring workspace about any problems with
              this client.

              FALSE : This setting is the default. The client automatically remediates

              problems when it finds them, and the site notifies you in the Monitoring
              workspace.

When you install clients, you can exclude them from automatic remediation with the
NotifyOnly installation property. For more information, see About client installation
properties.

Next steps
Monitor clients

Feedback
Was this page helpful?        Yes    No

Provide product feedback

<!-- p.2298 -->

How to monitor client deployment
status in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Deploying clients across your site takes time and some installations are not successful
the first time. The Configuration Manager console provides a way to keep an eye on
client deployments within a collection by reporting client deployment status in real time.

  ７ Note

  The best and most reliable way to monitor client deployment is with the
  Configuration Manager console (as described in this article). The Client Status
  section of the Monitoring workspace in the console provides client deployment
  status accurately and in real time. You can monitor client deployments with other
  tools, such as Server Manager in Windows Server or System Center Operations
  Manager, but you may receive alarms from normal client installation activity.
  Because of how the client installation program (CCMSetup.exe) runs in various
  environments, these other tools may generate false alarms and warnings that do
  not accurately reflect the state of client deployments.

In the Monitoring workspace of the console, you can monitor the following statuses for
client deployments taking place within a collection that you specify:

      Compliant

      In progress

      Not compliant

      Failed

      Unknown

      Configuration Manager reports on deployments for production clients or pre-
      production clients. The Configuration Manager console also provides a chart of
      failed client deployments over a specified period of time to help you determine if
      actions you to take to troubleshoot deployments are improving the deployment
      success rate over time.

<!-- p.2299 -->

To monitor client deployments
     In the Configuration Manager console, click Monitoring > Client Status.

     Click Production Client Deployment or Pre-production Client Deployment
     depending on the version of client you want to monitor.

     Review the charts of client deployment status and client deployment failure.

     If you want to change the scope of the report, click Browse... and choose a
     different collection.

     To learn more about pre-production client deployments, see How to test client
     upgrades in a pre-production collection.

        ７ Note

        The deployment status on computers hosting site system roles in a pre-
        production collection may be reported as Not compliant even when the client
        was successfully deployed. When you promote the client to production, the
        deployment status is reported correctly.

     To monitor the status of deployed clients, see How to monitor clients

     You can use Configuration Manager reports to find out more information about
     the status of clients in your site. For more information about how to run reports,
     see Introduction to reporting.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2300 -->

Monitor and manage clients in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you install the client on devices in your organization, Configuration Manager
provides several ways to monitor and manage it. You can monitor clients to check their
status, and Configuration Manager can automatically fix some problems it detects. Use
the Configuration Manager console to manage clients for individual devices or device
collections.

      How to monitor clients

      How to manage clients

      Configure the content cache

      Manage clients on the internet

      Use collections

Co-management enables you to concurrently manage Windows devices by using both
Configuration Manager and Microsoft Intune. It lets you cloud-attach your existing
investment in Configuration Manager by adding new functionality. When you enable co-
management, you can use Intune for additional client management actions. For more
information, see What is co-management?.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2301 -->

How to monitor clients in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Once you install the Configuration Manager client on the Windows devices in your site,
monitor their health and activity in the Configuration Manager console.

About client status
Configuration Manager provides the following types of information as client status:

      Client online status: The site considers a device as online if it's connected to its
      assigned management point. To indicate that the client is online, it sends ping-like
      messages to the management point. If the management point doesn't receive a
      message in five minutes, the site considers the client as offline.

         Tip

        These messages use the client notification channel. For more information, see
        Ports used in Configuration Manager.

      Client activity: The site considers the client as active if it has communicated with
      Configuration Manager in the past seven days. The site considers the client
      inactive if it hasn't done the following actions in seven days:
         Requested policy update
         Sent a heartbeat message
         Sent hardware inventory

      Client check: The state of the periodic evaluation that the Configuration Manager
      client runs on the device. The evaluation checks the device and can remediate
      some of the problems it finds. For more information, see Client health checks.

      Client check runs automatically during the Windows maintenance window.

      You can configure remediation not to run on specific devices, for example, a
      business-critical server. For more information, see How to configure client status.

      If there are more items that you want to evaluate, use Configuration Manager
      compliance settings to monitor other configurations. For more information about

<!-- p.2302 -->

    compliance settings, see Plan for and configure compliance settings.

    Decommissioned: The site has marked the device record for deletion. This
    behavior can happen when a new registration for same device assigns to the same
    or a different primary site in a hierarchy. The site deletes these devices the next
    time it runs the site maintenance task Delete Aged Discovery Data.

    Obsolete: The site has discovered a new device record with the same hardware ID,
    so it marks the old record as obsolete. Reports don't count obsolete records of the
    same device multiple times. You can still target policies to obsolete devices. If the
    site doesn't get a heartbeat for an obsolete record after 90 days of inactivity, it
    removes the obsolete device when it runs the site maintenance task Delete
    Obsolete Client Discovery Data.

  Tip

 The Power BI sample reports for Configuration Manager includes a report called
 Client Status. This report can also help with monitoring clients.

Monitor individual clients
 1. In the Configuration Manager console, go to the Assets and Compliance
    workspace. Select either the Devices node or choose a collection under Device
    Collections.

    The icons at the beginning of each row indicate the online status of the device:

                                                                          ﾉ   Expand table

     Icon           Description

                    Device is online.

                    Device is offline.

                    Online status is unknown.

                    Client isn't installed on the device.

 2. For more detailed online status, add the client online status information to the
    device view. Right-click the column header and select the online status fields you

<!-- p.2303 -->

     want to add:

           Device Online Status: Indicates whether the client is currently online or
           offline. (This status is the same information given by the icons.)

           Last Online Time: Indicates when the client online status changed to online.

           Last Offline Time indicates when the status changed to offline.

   3. Select an individual client in the list pane to see more status in the detail pane. This
     information includes client activity and client check status.

Monitor the status of all clients
   1. In the Configuration Manager console, go to the Monitoring workspace, and select
     the Client Status node. Review the overall statistics for client activity and client
     checks across the site. Change the scope of the information by choosing a
     different collection.

   2. To drill down into detail about the reported statistics, choose the name of the
     reported information. For example, Active clients that have passed client check or
     no results. Then review the information about the individual clients.

   3. Select Client Activity to see charts showing the client activity in your Configuration
     Manager site.

   4. Select Client Check to see charts showing the status of client checks in your
     Configuration Manager site.

     Configure alerts to notify you when client check results or client activity drops
     below a specified percentage. The site can also alert you when remediation fails on
     a specified percentage of clients. For more information, see How to configure
     client status.

For more information on the client's regular checks to keep healthy, see Client health
checks.

Next steps
Use the client health dashboard to view your client health, scenario health, and
common errors. Filter the view by several attributes to see any potential issues by OS
and client versions. For more information, see Client health dashboard.

<!-- p.2304 -->

For more information about the log files used by client deployment and management
operations, see Log files.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2305 -->

Client health dashboard
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You deploy software updates and other apps to help secure your environment, but these
deployments only reach healthy clients. Unhealthy Configuration Manager clients
adversely effect overall compliance. Determining client health can be challenging
depending upon the denominator: how many total devices should be in your scope of
management? For example, if you discover all systems from Active Directory, even if
some of those records are for retired machines, this process increases your
denominator.

Configuration Manager provides a dashboard with information about the health of
clients in your environment. View your client health, scenario health, and common
errors. Filter the view by several attributes to see any potential issues by OS and client
versions.

By default, the client health dashboard shows online clients, and clients active in the
past three days. So you may see different numbers in this dashboard than in other
historical sources of client health. For example, other nodes under Client Status, or
reports in the client status category.

In the Configuration Manager console, go to the Monitoring workspace. Expand Client
status, and select the Client health dashboard node.

<!-- p.2306 -->

                                                            

  ７ Note

  Configuration Manager version 2111 includes improvements to this dashboard.
  This article mainly focuses on the current experience. For more information on the
  dashboard appearance and behavior in version 2107 and earlier, see Version 2107
  and earlier.

To view this dashboard your account needs the Read Client Status Settings permission
on the Site object.

Configure
There are two actions in the ribbon to configure client health and the dashboard:

<!-- p.2307 -->

   Choose Default Collection: Set a persistent user preference for the collection to
   scope the dashboard.

   When you set the collection on the Filter tile of the dashboard, that selection
   resets when you refresh the dashboard.

   Client Status Settings: Adjust the evaluation periods for scenario health. By default,
   if a client doesn't send scenario-specific data in 7 days, Configuration Manager
   considers it unhealthy for that scenario.

      Tip

     You can also configure these settings from the ribbon of the Client Status
     node.

     Scenario health isn't measured from your configuration of client settings.
     These values can vary based upon the resultant set of policy per device.

Filters

<!-- p.2308 -->

The single Filter tile at the top of the dashboard lets you adjust the data that it displays.
It includes the following filters:

     Include client health for offline clients: By default, the dashboard displays only
     online clients. This state comes from the client notification channel that updates a
     client's status every five minutes. For more information, see About client status.

     Only show unhealthy client details: Scope the view to only devices that are
     reporting a client health failure.

         Tip

        Combine this filter with the tiles for Client Versions and OS Versions. For
        more information, see Version tiles.

     Clients active in last number of days: By default, the dashboard displays clients
     that are active in the last three days.

     Client health for clients in the following collections: By default, the dashboard
     displays devices in the All Systems collection. Browse for a device collection to
     scope the view to a subset of devices in a specific collection.

         Tip

        This filter is temporary. When you refresh the dashboard, it'll reset to the
        default. To change the collection scope so it's persistent, use the Choose

<!-- p.2309 -->

        default collection action in the ribbon. For more information, see Configure
        the dashboard.

Overall client health

This tile shows the percentage of all clients reporting healthy in your hierarchy. This
percentage should be as close to 100% as possible. It's on the top row, which makes it
easier to see when you view the dashboard.

A healthy Configuration Manager client has the following properties:

     Online
     Actively sending data
     Passes all client health evaluation checks

For more information, see About client status.

A healthy client successfully communicates with the site. It reports all data based on the
defined schedules.

Select a segment of this chart to drill down to a device list view.

Clients with any failure

<!-- p.2310 -->

This tile shows the percentage of clients that report any health issue. This percentage
should be as close to 0% as possible.

Hover over the segment to see the number of devices that are unhealthy. Select it to
drill down to a device list view.

   Tip

  This tile replaces the Combined (All) and Combined (Any) scenarios from earlier
  versions.

Version tiles
                                                                         ﾉ   Expand table

 Client Versions                              OS Versions

<!-- p.2311 -->

There are two tiles that show client health by Configuration Manager Client versions
and OS versions. These tiles are useful when you make changes to the filters, such as
Failure only. They can help highlight whether any issues are consistent across a specific
version. Use this information to help you make upgrade decisions.

Select a segment of these charts to drill down to a device list view.

Select Show table to switch to a table view of the data. You can select and copy the data
from the table. Select Show chart to show the donut chart. The following example
shows a chart of Configuration Manager client versions:

Scenario health

This bar chart shows the overall health for the following core scenarios:

     Client health evaluation (client policy)
     Policy request
     Software inventory
     Hardware inventory
     Heartbeat discovery
     Status messaging operational (status messages)

<!-- p.2312 -->

Health trends by scenario

This tile shows the percentage of healthy clients for the selected scenario. To adjust the
number of days the chart displays, use the slider control at the top of the tile.

  ７ Note

  The maximum value for the slider control is the same as the Retain client status
  history for the following number of days in Client Status Settings. It's 31 days by
  default.

  It's limited by the amount of client health data in the site database. For example,
  you configure it to display 31 days of history. There's only three days of available
  data, so the chart shows three days.

Top 10 client health failures

This chart lists the most common failures in your environment. These errors come from
Windows or Configuration Manager.

<!-- p.2313 -->

Select a row of this table to drill down to a device list view. This action lets you easily
create a collection of devices to target a remediation action or for more detailed
reporting.

Version 2107 and earlier

  ７ Note

  This section applies to version 2107 and earlier.

                                                                                         

Filters in 2107 and earlier
At the top of the dashboard, there's a set of filters to adjust the data displayed in the
dashboard.

     Client health for clients in the following collections: By default, the dashboard
     displays devices in the All Systems collection. Select a device collection to scope
     the view to a subset of devices in a specific collection.

<!-- p.2314 -->

     Client active in last number of days: By default, the dashboard displays clients that
     are active in the last three days.

     Include client health for offline clients: By default, the dashboard displays only
     online clients. This state comes from the client notification channel that updates a
     client's status every five minutes. For more information, see About client status.

     Only show unhealthy client details: Scope the view to only devices that are
     reporting a client health failure.

         Tip

        Use this filter along with the client version and OS version tiles. For more
        information, see Version tiles.

Overall client health in 2107 and earlier
This tile shows the overall client health in your hierarchy.

A healthy Configuration Manager client has the following properties:

     Online
     Actively sending data
     Passes all client health evaluation checks

For more information, see About client status.

A healthy client successfully communicates with the site. It reports all data based on the
defined schedules in client settings.

Select a segment of this chart to drill down to a device list view.

Version tiles in 2107 and earlier
There are two tiles that show client health by Configuration Manager client version and
OS version. These tiles are useful when you make changes to the filters, such as Failure
only. They can help highlight whether any issues are consistent across a specific version.
Use this information to help you make upgrade decisions.

Select a segment of these charts to drill down to a device list view.

Scenario health in 2107 and earlier

<!-- p.2315 -->

This bar chart shows the overall health for the following core scenarios:

     Client policy
     Heartbeat discovery
     Hardware inventory
     Software inventory
     Status messages

Use the selectors to adjust the focus on specific scenarios in the chart.

The following two bars are always shown:

     Combined (All): the combination of all scenarios (AND)
     Combined (Any): at least one of the scenarios (OR)

Top 10 client health failures in 2107 and earlier
This chart lists the most common failures in your environment. These errors come from
Windows or Configuration Manager.

Next steps
For more information on the client's regular checks to keep healthy, see Client health
checks.

Use the Surface device dashboard to see the use of Surface devices in your
environment.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2316 -->

Client health checks
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Configuration Manager client regularly runs the checks and remediations to keep
healthy. For more information, see How to monitor clients.

Client checks

Verify that the client was installed correctly
If the client isn't correctly installed, start by troubleshooting client install. Review the
ccmsetup.log. Often, remediation requires that you reinstall the client.

Verify that client prerequisites are installed
Verify that the client prerequisites are installed. It reads the file ccmsetup.xml in the
client installation folder to discover the prerequisites. By default:
C:\Windows\ccmsetup\ccmsetup.xml

Most client prerequisites are available by default in Windows, or installed automatically
by the Configuration Manager client. To remediate problems with prerequisites, you can
try to install them manually, or reinstall the client.

Verify that there is sufficient disk space
Verify that there is greater that 1% disk space remaining on C drive.

Verify the client service
There are three checks for the SMS Agent Host client service ( CcmExec ):

      First, it verifies that the service exists. If it doesn't exist, you need to reinstall the
      client.

      Next, it verifies that the service startup type is automatic. To remediate a failure
      with this check, reset the service startup type to automatic. Check group policies to
      make sure something isn't automatically configuring the service startup type.

<!-- p.2317 -->

     Then it verifies that the client service is running. The remediation for this check is
     to start the client service. Then monitor it to make sure it keeps running. Review
     Windows event logs to see if there are any related activities that might be stopping
     the service. Review client logs to make sure it's not failing to start.

Verify that client check has recently run
Verify that the client check scheduled task ( CcmEval ) has run at least one time in the past
three days. You can manually run the scheduled task. Make sure that Windows can run
scheduled tasks.

Verify that the client database is healthy
The client uses a built-in version of SQL Server Compact Edition (CE) to locally store
information. If this check fails, reinstall the Configuration Manager client to remediate.

Verify WMI
There are several checks specific to WMI. The first three checks are for the Windows
Management Instrumentation (WMI) service ( Winmgmt ).

     Verify that the service exists. WMI is a fundamental component of Windows. If this
     service doesn't exist, you may need to reinstall Windows.

     Verify that the service startup type is automatic. To remediate a failure with this
     check, reset the service startup type to automatic. Check group policies to make
     sure something isn't automatically configuring the service startup type.

     Verify that the service is running. The remediation for this check is to start the WMI
     service. Then monitor it to make sure it keeps running. Review Windows event logs
     to see if there are any related activities that might be stopping the service.

There are two other checks to test the overall health of WMI on the device:

     The WMI repository integrity test checks that Configuration Manager client entries
     exist in WMI. If this check fails, reinstall the Configuration Manager client.

     The WMI event sink test checks whether the Configuration Manager-related WMI
     event sink is lost. If this check fails, restart the client service.

Verify the antimalware service

<!-- p.2318 -->

There are two checks for whatever antimalware service is registered with Windows:

     Verify that the antimalware service startup type is automatic. To remediate a failure
     with this check, reset the service startup type to automatic. Check group policies to
     make sure something isn't automatically configuring the service startup type.

     Verify that the antimalware service is running. The remediation for this check is to
     start the antimalware service. Then monitor it to make sure it keeps running.
     Review Windows event logs to see if there are any related activities that might be
     stopping the service.

If you're using Windows Defender, the Configuration Manager client also verifies the
Windows Defender Antivirus Network Inspection Service ( WdNisSvc ). It checks to make
sure the service startup type is manual.

Verify Windows Update service
This check verifies that the Windows Update service ( wuauserv ) startup type is
automatic or manual. To remediate a failure with this check, reset the service startup
type to automatic. Check group policies to make sure something isn't automatically
configuring the service startup type.

Verify the policy platform
There are three checks for the Microsoft Policy Platform service ( lppsvc ):

     Verify that the service exists. The policy platform is one of the prerequisite
     components that the Configuration Manager client automatically installs. If this
     service doesn't exist, reinstall the Configuration Manager client.

     Verify that the service startup type is manual. To remediate a failure with this check,
     reset the service startup type to manual. Check group policies to make sure
     something isn't automatically configuring the service startup type.

     Policy platform WMI integrity test. Repair the policy platform.

Verify BITS service
There are two checks for the Background Intelligent Transfer Service ( BITS ):

     Verify that the service exists. BITS is a fundamental component of Windows. If this
     service doesn't exist, you may need to reinstall Windows.

<!-- p.2319 -->

     Verify that the service startup type is automatic or manual. To remediate a failure
     with this check, reset the service startup type to automatic. Check group policies to
     make sure something isn't automatically configuring the service startup type.

Verify remote control
If you enable the remote control agent in client settings, there are two checks for the
Configuration Manager Remote Control service ( CmRcService ):

     Verify that the service type is automatic or manual. To remediate a failure with this
     check, reset the service startup type to automatic. Check group policies to make
     sure something isn't automatically configuring the service startup type.

     Verify that the service is running. The remediation for this check is to start the
     remote control service. Then monitor it to make sure it keeps running. Review
     Windows event logs to see if there are any related activities that might be stopping
     the service.

Verify wake-up proxy
If you enable the wake-up proxy in client settings, there are two checks for the
Configuration Manager Wake-up Proxy service:

     Verify that the service startup type is automatic. To remediate a failure with this
     check, reset the service startup type to automatic. Check group policies to make
     sure something isn't automatically configuring the service startup type.

     Verify that the service is running. The remediation for this check is to start the
     wake-up proxy service. Then monitor it to make sure it keeps running. Review
     Windows event logs to see if there are any related activities that might be stopping
     the service.

Most common check failures
The following checks have the most commonly reported failures. The numbers are
included to provide scale between the checks.

     Verify CcmEval task has run in recent cycles (4,950)
     Verify client prerequisites (554)
     Verify Windows Update service startup type (399)
     Verify Configuration Manager Remote Control service status (345)
     Verify Configuration Manager Remote Control service startup type (294)

<!-- p.2320 -->

     Verify SMS Agent Host service status (249)
     Verify SQL Server CE database is healthy (157)
     Verify client WMI Provider (131)
     Verify client installation (120)
     WMI event sink test (93)

Next steps
Client health dashboard

How to configure client status

How to deploy clients to Windows computers

Configuration Manager troubleshooting

Feedback
Was this page helpful?      Yes    No

Provide product feedback
