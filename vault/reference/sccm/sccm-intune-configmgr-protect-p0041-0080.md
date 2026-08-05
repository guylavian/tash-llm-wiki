---
title: "Protect data and infrastructure documentation — pages 41-80"
type: reference
domain: sccm
slug: sccm-intune-configmgr-protect-p0041-0080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-protect-p0041-0080
family: sccm
documentKind: "doc"
abstract: "Configure definition updates for Endpoint Protection Article • 10/04/2022 Applies to: Configuration Manager (current branch) With Endpoint Protection in Configuration Manager, you can use any of several available methods to keep antimalware definitions up to date on client compu"
---

# Protect data and infrastructure documentation — pages 41-80

<!-- p.41 -->

Configure definition updates for
Endpoint Protection
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

With Endpoint Protection in Configuration Manager, you can use any of several available
methods to keep antimalware definitions up to date on client computers in your
hierarchy. The information in this topic can help you to select and configure these
methods.

To update antimalware definitions, you can use one or more of the following methods:

      Updates distributed from Configuration Manager - This method uses
      Configuration Manager software updates to deliver definition and engine updates
      to computers in your hierarchy.

      Updates distributed from Windows Server Update Services (WSUS) - This method
      uses your WSUS infrastructure to deliver definition and engine updates to
      computers.

      Updates distributed from Microsoft Update - This method allows computers to
      connect directly to Microsoft Update in order to download definition and engine
      updates. This method can be useful for computers that are not often connected to
      the business network.

      Updates distributed from Microsoft Malware Protection Center - This method will
      download definition updates from the Microsoft Malware Protection Center.

      Updates from UNC file shares - With this method, you can save the latest definition
      and engine updates to a share on the network. Clients can then access the network
      to install the updates.

      You can configure multiple definition update sources and control the order in
      which they are assessed and applied. This is done in the Configure Definition
      Update Sources dialog box when you create an antimalware policy.

  ） Important

  For Windows 10 or later PCs, you must configure Endpoint Protection to update
  malware definitions for Windows Defender.

<!-- p.42 -->

How to Configure Definition Update Sources
Use the following procedure to configure the definition update sources to use for each
antimalware policy.

   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, expand Endpoint Protection, and then
     click Antimalware Policies.

   3. Open the properties page of the Default Antimalware Policy or create a new
     antimalware policy. For more information about how to create antimalware
     policies, see How to create and deploy antimalware policies for Endpoint
     Protection.

   4. In the Security Intelligence updates section of the antimalware properties dialog
     box, click Set Source.

          The Definition updates section was renamed to Security Intelligence
          updates starting in Configuration Manager version 1902.

   5. In the Configure Definition Update Sources dialog box, select the sources to use
     for definition updates. You can click Up or Down to modify the order in which
     these sources are used.

   6. Click OK to close the Configure Definition Update Sources dialog box.

Configure Endpoint Protection definitions
     Updates distributed from Configuration Manager - This method uses
     Configuration Manager software updates to deliver definition and engine updates
     to computers in your hierarchy.

     Updates distributed from Windows Server Update Services (WSUS) - This method
     uses your WSUS infrastructure to deliver definition and engine updates to
     computers.

     Updates distributed from Microsoft Update - This method allows computers to
     connect directly to Microsoft Update in order to download definition and engine
     updates. This method can be useful for computers that are not often connected to
     the business network.

     Updates distributed from Microsoft Malware Protection Center - This method will
     download definition updates from the Microsoft Malware Protection Center.

<!-- p.43 -->

     Updates from UNC file shares - With this method, you can save the latest definition
     and engine updates to a share on the network. Clients can then access the network
     to install the updates.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.44 -->

Use Configuration Manager to deliver
definition updates
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can configure Configuration Manager software updates to automatically deliver
definition updates to client computers. Before you begin to create automatic
deployment rules, make sure to configure Configuration Manager software updates. For
more information, see Introduction to software updates.

  ７ Note

  This procedure is specific to Endpoint Protection. For more general information
  about automatic deployment rules, see Automatically deploy software updates.

   1. In the Configuration Manager console, go to the Software Library workspace.
      Expand Software Updates, and then select Automatic Deployment Rules.

   2. On the Home tab of the ribbon, in the Create group, select Create Automatic
      Deployment Rule.

   3. On the General page of the Create Automatic Deployment Rule Wizard, specify
      the following information:

            Name: Enter a unique name for the automatic deployment rule.

            Collection: Select the device collection to which you want to deploy
            definition updates.

              ７ Note

              You can't deploy definition updates to a user collection.

   4. Select Add to an existing Software Update Group.

   5. Select Enable the deployment after this rule is run.

   6. On the Deployment Settings page of the wizard, for the Detail level, select Only
      error messages.

<!-- p.45 -->

    ７ Note

    When you select Only error messages, it reduces the number of state
    messages that the definition deployment sends. This configuration helps
    reduce the CPU processing on the Configuration Manager servers.

7. On the Software Updates page:

  a. Select the Update Classification property filter. In the Search criteria list, select
     <items to find>.

     In the Search Criteria window, select Definition Updates, then select OK.

  b. Select the Product property filter. In the Search criteria list, select <items to
     find>.

     In the Search Criteria window, select System Center Endpoint Protection for
     Windows 8.1 and earlier or Windows Defender for Windows 10 and later, then
     select OK.

    ７ Note

    Optionally, you can filter out superseded updates. Select the Superseded
    property filter. In the Search criteria list, select <items to find>. In the Search
    Criteria window, select No, then select OK.

8. On the Evaluation Schedule page of the wizard, select Run the rule after any
  software update point synchronization.

9. On the Deployment Schedule page of the wizard, configure the following settings:

       Time based on: If you want all clients to install the latest definitions at the
       same time, select UTC. The actual installation time will vary within two hours.

       Software available time: Specify the available time for the deployment that
       this rule creates. The specified time must be at least one hour after the
       automatic deployment rule runs. This configuration makes sure that the
       content has sufficient time to replicate to the distribution points. Some
       definition updates might also include antimalware engine updates, which
       might take longer to reach distribution points.

       Installation deadline: Select As soon as possible.

<!-- p.46 -->

             ７ Note

             Software update deadlines vary over a two-hour period. This behavior
             prevents all clients from requesting an update at the same time.

 10. On the User Experience page of the wizard, for User notifications, select Hide in
     Software Center and all notifications. With this configuration, the definition
     updates install silently.

 11. On the Deployment Package page of the wizard, select an existing deployment
     package or create a new one.

       ７ Note

       Consider placing definition updates in a package that doesn't contain other
       software updates. This strategy keeps the size of the definition update
       package smaller, which allows it to replicate to distribution points more
       quickly.

 12. If you create a new deployment package, on the Distribution Points page of the
     wizard, select one or more distribution points. The site copies the content for this
     package to these distribution points.

 13. On the Download Location page, select Download software updates from the
     Internet.

 14. On the Language Selection page, select each language version of the updates to
     download.

 15. On the Download Settings page, select the necessary software updates download
     behavior.

 16. Complete the wizard.

Verify that the Automatic Deployment Rules node of the Configuration Manager
console displays the new rule.

 Create and deploy antimalware policies

Feedback

<!-- p.47 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.48 -->

Enable Endpoint Protection malware
definitions to download from WSUS for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If you use WSUS to keep your antimalware definitions up to date, you can configure it to
auto-approve definition updates. Although using Configuration Manager software
updates is the recommended method to keep definitions up to date, you can also
configure WSUS as a method to allow users to manually update definitions. Use the
following procedures to configure WSUS as a definition update source.

Synchronize definition updates for
Configuration Manager
   1. In the Configuration Manager console, go to the Administration workspace,
      expand Site Configuration, and then select Sites.

   2. Select the site that contains your software update point. In the Settings group of
      the ribbon, select Configure Site Components, and then select Software Update
      Point.

   3. In the Software Update Point Component Properties window, switch to the
      Classifications tab. Select Definition Updates.

   4. To specify the Products updated with WSUS, switch to the Products tab.

            For Windows 10 and later: Under Microsoft > Windows, select Microsoft
            Defender Antivirus.

            For Windows 8.1 and earlier: Under Microsoft > Forefront, select System
            Center Endpoint Protection.

   5. Select OK to close the Software Update Point Component Properties window.

Approve definition updates
Endpoint Protection definition updates must be approved and downloaded to the
WSUS server before they're offered to clients that request the list of available updates.

<!-- p.49 -->

Clients connect to the WSUS server to check for applicable updates and then request
the latest approved definition updates.

Approve definitions and updates in WSUS
   1. In the WSUS administration console, select Updates. Then select All Updates or
     the classification of updates that you want to approve.

   2. In the list of updates, right-click the update or updates you want to approve for
     installation, and then select Approve.

   3. In the Approve Updates window, select the computer group for which you want to
     approve the updates, and then select Approved for Install.

Configure an automatic approval rule
You can also set an automatic approval rule for definition updates and Endpoint
Protection updates. This action configures WSUS to automatically approve Endpoint
Protection definition updates downloaded by WSUS.

   1. In the WSUS administration console, select Options, and then select Automatic
     Approvals.

   2. On the Update Rules tab, select New Rule.

   3. In the Add Rule window, under Step 1: Select properties, select the option: When
     an update is in a specific classification.

     a. Under Step 2: Edit the properties, select any classification.

     b. Clear all options except Definition Updates, and then select OK.

   4. In the Add Rule window, under Step 1: Select properties, select the option: When
     an update is in a specific product.

     a. Under Step 2: Edit the properties, select any product.

     b. Clear all options except System Center Endpoint Protection for Windows 8.1
        and earlier or Windows Defender for Windows 10 and later. Then select OK.

   5. Under Step 3: Specify a name, enter a name for the rule, and then select OK.

   6. In the Automatic Approvals dialog box, select the newly created rule, and then
     select Run rule.

<!-- p.50 -->

  ７ Note

  To maximize performance on your WSUS server and client computers, decline old
  definition updates. To accomplish this task, you can configure automatic approval
  for revisions and automatic declining of expired updates. For more information, see
  Microsoft Support article 938947        .

  Create and deploy antimalware policies

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.51 -->

Enable Endpoint Protection malware
definitions to download from Microsoft
Updates
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When you select to download definition updates from Microsoft Update, clients will
check the Microsoft Update site at the interval defined in the Security Intelligence
updates section of the antimalware policy dialog box.

This method can be useful when the client does not have connectivity to the
Configuration Manager site or when you want users to be able to initiate definition
updates.

  ） Important

        Clients must have access to Microsoft Update on the Internet to be able to
        use this method to download definition updates.
        The Definition updates section was renamed to Security Intelligence updates
        starting in Configuration Manager version 1902.

Using the Microsoft Malware Protection Center
to Download Definitions
You can configure clients to download definition updates from the Microsoft Malware
Protection Center. This option is used by Endpoint Protection clients to download
definition updates if they have not been able to download updates from another source.
This update method can be useful if there is a problem with your Configuration
Manager infrastructure that prevents the delivery of updates.

  ） Important

  Clients must have access to Microsoft Update on the Internet to be able use this
  method to download definition updates.

<!-- p.52 -->

  Next step >

  Back >

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.53 -->

Use the Microsoft Malware Protection
Center to download definitions
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can configure clients to download definition updates from the Microsoft Malware
Protection Center. This option is used by Endpoint Protection clients to download
definition updates if they have not been able to download updates from another source.
This update method can be useful if there is a problem with your Configuration
Manager infrastructure that prevents the delivery of updates.

  ） Important

  Clients must have access to Microsoft Update on the Internet to be able use this
  method to download definition updates.

  Next step >

  Back >

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.54 -->

Enable Endpoint Protection malware
definitions to download from a network
share
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can manually download the latest definition updates from Microsoft and then
configure clients to download these definitions from a shared folder on the network.
Users can also initiate definition updates when you use this update source.

  ７ Note

  Clients must have read access to the shared folder to be able to download
  definition updates.

For more information about how to download the definition and engine updates to
store on the file share, see Install the latest Microsoft antimalware and antispyware
software    .

To configure definition downloads from a file
share
   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, expand Endpoint Protection, and then
      click Antimalware Policies.

   3. Open the properties page of the Default Antimalware Policy or create a new
      antimalware policy. For more information about how to create antimalware
      policies, see How to create and deploy antimalware policies for Endpoint
      Protection.

   4. In the Security Intelligence updates section of the antimalware properties dialog
      box, click Set Source.

            The Definition updates section was renamed to Security Intelligence
            updates starting in Configuration Manager version 1902.

<!-- p.55 -->

   5. In the Configure Definition Update Sources dialog box, select Updates from UNC
     file shares.

   6. Click OK to close the Configure Definition Update Sources dialog box.

   7. Click Set Paths. Then, in the Configure Definition Update UNC Paths dialog box,
     add one or more UNC paths to the location of the definition updates files on a
     network share.

   8. Click OK to close the Configure Definition Update UNC Paths dialog box.

  Next step >

  Back >

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.56 -->

How to create and deploy antimalware
policies for Endpoint Protection in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can deploy antimalware policies to collections of Configuration Manager client
computers to specify how Endpoint Protection protects them from malware and other
threats. These policies include information about the scan schedule, the types of files
and folders to scan, and the actions to take when malware is detected. When you enable
Endpoint Protection, a default antimalware policy is applied to client computers. You can
also use one of the supplied policy templates or create a custom policy to meet the
specific needs of your environment.

Configuration Manager supplies a selection of predefined templates. These are
optimized for various scenarios and can be imported into Configuration Manager. These
templates are available in the folder <ConfigMgr Install
Folder>\AdminConsole\XMLStorage\EPTemplates.

  ） Important

  If you create a new antimalware policy and deploy it to a collection, this
  antimalware policy overrides the default antimalware policy.

Use the procedures in this topic to create or import antimalware policies and assign
them to Configuration Manager client computers in your hierarchy.

  ７ Note

  Before you perform these procedures, ensure that Configuration Manager is
  configured for Endpoint Protection as described in Configuring Endpoint
  Protection.

Modify the default antimalware policy
   1. In the Configuration Manager console, click Assets and Compliance.

<!-- p.57 -->

 2. In the Assets and Compliance workspace, expand Endpoint Protection, and then
   click Antimalware Policies.

 3. Select the antimalware policy Default Client Antimalware Policy and then, on the
   Home tab, in the Properties group, click Properties.

 4. In the Default Antimalware Policy dialog box, configure the settings that you
   require for this antimalware policy, and then click OK.

     ７ Note

     For a list of settings that you can configure, see List of Antimalware Policy
     Settings in this topic.

Create a new antimalware policy
 1. In the Configuration Manager console, click Assets and Compliance.

 2. In the Assets and Compliance workspace, expand Endpoint Protection, and then
   click Antimalware Policies.

 3. On the Home tab, in the Create group, click Create Antimalware Policy.

 4. In the General section of the Create Antimalware Policy dialog box, enter a name
   and a description for the policy.

 5. In the Create Antimalware Policy dialog box, configure the settings that you
   require for this antimalware policy, and then click OK. For a list of settings that you
   can configure, see List of Antimalware Policy Settings.

 6. Verify that the new antimalware policy is displayed in the Antimalware Policies list.

Import an antimalware policy
 1. In the Configuration Manager console, click Assets and Compliance.

 2. In the Assets and Compliance workspace, expand Endpoint Protection, and then
   click Antimalware Policies.

 3. In the Home tab, in the Create group, click Import.

 4. In the Open dialog box, browse to the policy file to import, and then click Open.

<!-- p.58 -->

   5. In the Create Antimalware Policy dialog box, review the settings to use, and then
     click OK.

   6. Verify that the new antimalware policy is displayed in the Antimalware Policies list.

Deploy an antimalware policy to client
computers
   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, expand Endpoint Protection, and then
     click Antimalware Policies.

   3. In the Antimalware Policies list, select the antimalware policy to deploy. Then, on
     the Home tab, in the Deployment group, click Deploy.

       ７ Note

       The Deploy option cannot be used with the default client malware policy.

   4. In the Select Collection dialog box, select the device collection to which you want
     to deploy the antimalware policy, and then click OK.

List of Antimalware Policy Settings
Many of the antimalware settings are self-explanatory. Use the following sections for
more information about the settings that might require more information before you
configure them.

     Scheduled Scans Settings
     Scan Settings
     Default Actions Settings
     Real-time Protection Settings
     Exclusion Settings
     Advanced Settings
     Threat Overrides Settings
     Cloud Protection Service
     Definition Updates Settings

Scheduled Scans Settings

<!-- p.59 -->

Scan type - You can specify one of two scan types to run on client computers:

     Quick scan - This type of scan checks the in-memory processes and folders where
     malware is typically found. It requires fewer resources than a full scan.

     Full Scan - This type of scan adds a full check of all local files and folders to the
     items scanned in the quick scan. This scan takes longer than a quick scan and uses
     more CPU processing and memory resources on client computers.

     In most cases, use Quick scan to minimize the use of system resources on client
     computers. If malware removal requires a full scan, Endpoint Protection generates
     an alert that is displayed in the Configuration Manager console. The default value
     is Quick scan.

  ７ Note

  When scheduling scans for times when endpoints are not in use, it’s important to
  note that the CPU throttling configuration is not honored. Scans will take full
  advantage of available resources to complete as quickly as possible.

Scan Settings
Scan email and email attachments - Set to Yes to turn on e-mail scanning.

Scan removable storage devices such as USB drives - Set to Yes to scan removable
drives during full scans.

Scan network files - Set to Yes to scan network files.

Scan mapped network drives when running a full scan - Set to Yes to scan any mapped
network drives on client computers. Enabling this setting might significantly increase the
scan time on client computers.

     The Scan network files setting must be set to Yes for this setting to be available to
     configure.

     By default, this setting is set to No, meaning that a full scan will not access
     mapped network drives.

Scan archived files - Set to Yes to scan archived files such as .zip or .rar files.

Allow users to configure CPU usage during scans - Set to Yes to allow users to specify
maximum percentage of CPU utilization during a scan. Scans will not always use the
maximum load defined by users, but they cannot exceed it.

<!-- p.60 -->

User control of scheduled scans - Specify level of user control. Allow users to set Scan
time only or Full control of antivirus scans on their devices.

Default Actions Settings
Select the action to take when malware is detected on client computers. The following
actions can be applied, depending on the alert threat level of the detected malware.

     Recommended - Use the action recommended in the malware definition file.

     Quarantine - Quarantine the malware but do not remove it.

     Remove - Remove the malware from the computer.

     Allow - Do not remove or quarantine the malware.

Real-time Protection Settings

                                                                                 ﾉ   Expand table

 Setting name          Description

 Enable real-time      Set to Yes to configure real-time protection settings for client computers.
 protection            We recommend that you enable this setting.

 Monitor file and      Set to Yes if you want Endpoint Protection to monitor when files and
 program activity on   programs start to run on client computers and to alert you about any
 your computer         actions that they perform or actions taken on them.

 Scan system files     This setting lets you configure whether incoming, outgoing, or incoming
                       and outgoing system files are monitored for malware. For performance
                       reasons, you might have to change the default value of Scan incoming
                       and outgoing files if a server has high incoming or outgoing file activity.

 Enable behavior       Enable this setting to use computer activity and file data to detect
 monitoring            unknown threats. When this setting is enabled, it might increase the time
                       required to scan computers for malware.

 Enable protection     Enable this setting to protect computers against known network exploits
 against network-      by inspecting network traffic and blocking any suspicious activity.
 based exploits

 Enable script         For Configuration Manager with no service pack only.
 scanning
                       Enable this setting if you want to scan any scripts that run on computers
                       for suspicious activity.

<!-- p.61 -->

 Setting name          Description

 Block Potentially     Potential Unwanted Applications (PUA) is a threat classification based on
 Unwanted              reputation and research-driven identification. Most commonly, these are
 Applications at       unwanted application bundlers or their bundled applications.
 download and prior
 to installation       Microsoft Edge also provides settings to block potentially unwanted
                       applications. Explore these options for complete protection against
                       unwanted applications.

                       This protection policy setting is available and set to Enabled by default.
                       When enabled, this setting blocks PUA at download and install time.
                       However, you can exclude specific files or folders to meet the specific
                       needs of your business or organization.

                       Starting in Configuration Manager version 2107, you can select to Audit
                       this setting. Use PUA protection in audit mode to detect potentially
                       unwanted applications without blocking them. PUA protection in audit
                       mode is useful if your company would like the gauge the impact that
                       enabling PUA protections will have in your environment. Enabling
                       protection in audit mode allows you to determine the impact to your
                       endpoints prior to enabling the protection in block mode.

Exclusion Settings
For information about folders, files, and processes that are recommended for exclusion
in Configuration Manager 2012 and Current Branch, see Recommended antivirus
exclusions for Configuration Manager 2012 and current branch site servers, site systems,
and clients    .

Excluded files and folders:

Click Set to open the Configure File and Folder Exclusions dialog box and specify the
names of the files and folders to exclude from Endpoint Protection scans.

If you want to exclude files and folders that are located on a mapped network drive,
specify the name of each folder in the network drive individually. For example, if a
network drive is mapped as F:\MyFolder and it contains subfolders named Folder1,
Folder2 and Folder 3, specify the following exclusions:

     F:\MyFolder\Folder1

     F:\MyFolder\Folder2

     F:\MyFolder\Folder3

<!-- p.62 -->

Beginning in version 1602, the existing Exclude files and folders setting in the Exclusion
settings section of an antimalware policy is improved to allow device exclusions. For
example, you can now specify the following as an exclusion: \device\mvfs (for
Multiversion File System). The policy does not validate the device path; the Endpoint
Protection policy is provided to the antimalware engine on the client which must be
able to interpret the device string.

Excluded file types:

Click Set to open the Configure File Type Exclusions dialog box and specify the file
extensions to exclude from Endpoint Protection scans. You can use wildcards when
defining items in the exclusion list. For more information, see Use wildcards in the file
name and folder path or extension exclusion lists.

Excluded processes:

Click Set to open the Configure Process Exclusions dialog box and specify the
processes to exclude from Endpoint Protection scans. You can use wildcards when
defining items in the exclusion list, however, there are some limitations. For more
information, see Use wildcards in the process exclusion list

  ７ Note

  When a device is targeted with two or more Antimalware Policies, the settings for
  antivirus exclusions will merge before being applied to the client.

Advanced Settings
Enable reparse point scanning - Set to Yes if you want Endpoint Protection to scan
NTFS reparse points.

For more information about reparse points, see Reparse Points in the Windows Dev
Center.

Randomize the scheduled scan start times (within 30 minutes) - Set to Yes to help
avoid flooding the network, which can occur if all computers send their antimalware
scans results to the Configuration Manager database at the same time. For Windows
Defender Antivirus, this randomizes the scan start time to any interval from 0 to 4 hours,
or for FEP and SCEP, to any interval plus or minus 30 minutes. This can be useful in VM
or VDI deployments. This setting is also useful when you run multiple virtual machines
on a single host. Select this option to reduce the amount of simultaneous disk access for
antimalware scanning.

<!-- p.63 -->

Beginning in version 1602 of Configuration Manager, the antimalware engine may
request file samples to be sent to Microsoft for further analysis. By default, it will always
prompt before it sends such samples. Administrators can now manage the following
settings to configure this behavior:

Enable auto sample file submission to help Microsoft determine whether certain
detected items are Malicious - Set to Yes to enable auto sample file submission. By
default, this setting is No which means auto sample file submission is disabled and users
are prompted before sending samples.

Allow users to modify auto sample file submission settings - This determines whether
a user with local admin rights on a device can change the auto sample file submission
setting in the client interface. By default, this setting is "No" which means it can only be
changed from the Configuration Manager console, and local admins on a device cannot
change this configuration.
For example, the following shows this setting set by the administrator as enabled, and
greyed out to prevent changes by the user.

Threat Overrides Settings
Threat name and override action - Click Set to customize the remediation action to
take for each threat ID when it is detected during a scan.

  ７ Note

  The list of threat names might not be available immediately after the configuration
  of Endpoint Protection. Wait until the Endpoint Protection point has synchronized
  the threat information, and then try again.

Cloud Protection Service

<!-- p.64 -->

Cloud Protection Service enables the collection of information about detected malware
on managed systems and the actions taken. This information is sent to Microsoft.

Cloud Protection Service membership

     Do not join Cloud Protection Service - No information is sent
     Basic - Collect and send lists of detected malware
     Advanced - Basic information as well as more comprehensive information that
     could contain personal information. For example, file paths and partial memory
     dumps.

Allow users to modify Cloud Protection Service settings - Toggles user control of
Cloud Protection Service settings.

Level for blocking suspicious files - Specify the level at which the Endpoint Protection
Cloud Protection Service will block suspicious files.

     Normal - The default Windows Defender blocking level
     High - Aggressively blocks unknown files while optimizing for performance
     (greater chance of blocking non-harmful files)
     High with extra protection - Aggressively blocks unknown files and applies
     additional protection measures (might impact client device performance)
     Block unknown programs - Blocks all unknown programs

Allow extended cloud check to block and scan for up to (seconds) - Specifies the
number of seconds Cloud Protection Service can block a file while the service checks
that the file is not known to be malicious.

  ７ Note

  The number of seconds that you select for this setting is in addition to a default 10-
  second timeout. For example, if you enter 0 seconds, the Cloud Protection Service
  blocks the file for 10 seconds.

Details of Cloud Protection Service reporting

                                                                               ﾉ   Expand table

 Frequency             Data collected or        Use of data
                       sent

 When Windows          - Version of virus and   Microsoft uses this information to ensure the
 Defender updates      spyware definitions      latest virus and spyware updates are present on

<!-- p.65 -->

 Frequency              Data collected or         Use of data
                        sent

 virus and spyware      - Virus and spyware       computers. If not present, Windows Defender
 protection or          protection version        updates automatically so computer protection
 definition files                                 stays up-to-date.

 If Windows Defender    - Name of potentially     Windows Defender uses this information to
 finds potentially      harmful or unwanted       determine the type and severity of potentially
 harmful or unwanted    software                  unwanted software, and the best action to take.
 software on            - How the software        Microsoft also uses this information to help
 computers              was found                 improve the accuracy of virus and spyware
                        - Any actions that        protection.
                        Windows Defender
                        took to deal with the
                        software
                        - Files affected by the
                        software
                        - Information about
                        the computer from
                        the manufacturer
                        (Sysconfig, SysModel,
                        SysMarker)

 Once a month           - Virus and spyware       Windows Defender uses this information to verify
                        definition update         that computers have the latest virus and spyware
                        status                    protection version and definitions. Microsoft also
                        - Status of real-time     wants to make sure that real-time virus and
                        virus and spyware         spyware monitoring is turned on. This is a critical
                        monitoring (on or off)    part of helping protect computers from
                                                  potentially harmful or unwanted software.

 During installation,   List of running           To identify any processes that might have been
 or whenever users      processes in your         compromised by potentially harmful software.
 manually perform       computer's memory
 virus and spyware
 scan of your
 computer

Microsoft collects only the names of affected files, not the contents of the files
themselves. This information helps determine what systems are especially vulnerable to
specific threats.

Definition Updates Settings
Set sources and order for Endpoint Protection client updates - Click Set Source to
specify the sources for definition and scanning engine updates. You can also specify the
order in which these sources are used. If Configuration Manager is specified as one of

<!-- p.66 -->

the sources, then the other sources are used only if software updates fail to download
the client updates.

If you use any of the following methods to update the definitions on client computers,
then the client computers must be able to access the Internet.

     Updates distributed from Microsoft Update

     Updates distributed from Microsoft Malware Protection Center

  ） Important

  Clients download definition updates by using the built-in system account. You must
  configure a proxy server for this account to enable these clients to connect to the
  Internet.

  If you have configured a software updates automatic deployment rule to deliver
  definition updates to client computers, these updates will be delivered regardless
  of the definition updates settings.

  Next step >

  Back >

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.67 -->

Configure custom client settings for
Endpoint Protection
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This procedure configures custom client settings for Endpoint Protection, which you can
deploy to collections of devices in your hierarchy.

  ） Important

  Only configure the default Endpoint Protection client settings if you're sure that
  you want them applied to all computers in your hierarchy.

To enable Endpoint Protection and configure
custom client settings
   1. In the Configuration Manager console, click Administration.

   2. In the Administration workspace, click Client Settings.

   3. On the Home tab, in the Create group, click Create Custom Client Device Settings.

   4. In the Create Custom Client Device Settings dialog box, provide a name and a
      description for the group of settings, and then select Endpoint Protection.

   5. Configure the Endpoint Protection client settings that you require. For a full list of
      Endpoint Protection client settings that you can configure, see the Endpoint
      Protection section in About client settings.

        ） Important

        Install the Endpoint Protection site system role before you configure client
        settings for Endpoint Protection.

   6. Click OK to close the Create Custom Client Device Settings dialog box. The new
      client settings are displayed in the Client Settings node of the Administration
      workspace.

<!-- p.68 -->

   7. Next, deploy the custom client settings to a collection. Select the custom client
     settings you want to deploy. In the Home tab, in the Client Settings group, click
     Deploy.

   8. In the Select Collection dialog box, choose the collection to which you want to
     deploy the client settings and then click OK. The new deployment is shown in the
     Deployments tab of the details pane.

Clients are configured with these settings when they next download client policy. For
more information, see Initiate policy retrieval for a Configuration Manager client.

How to provision the Endpoint Protection
client in a disk image
Install the Endpoint Protection client on a computer that you intend to use as a disk
image source for Configuration Manager OS deployment. This computer is typically
called the reference computer. After you create the OS image, then use Configuration
Manager OS deployment to deploy the image.

  ） Important

  Starting in Windows 10 and Windows Server 2016, Windows Defender is installed
  by default. You don't need this procedure on those versions or later versions of
  Windows.

Use the following procedures to help you install and configure the Endpoint Protection
client on a reference computer.

Prerequisites
The following list contains the required prerequisites for installing the Endpoint
Protection client software on a reference computer.

     You must have access to the Endpoint Protection client installation package,
     scepinstall.exe. Find this package in the Client folder of the Configuration
     Manager installation folder on the site server.

     To deploy the Endpoint Protection client with your organization's required
     configuration, create and export an antimalware policy. Then specify this policy
     when you manually install the Endpoint Protection client. For more information,
     see How to create and deploy antimalware policies.

<!-- p.69 -->

       ７ Note

       You can't export the Default Client Antimalware Policy.

     If you want to install the Endpoint Protection client with the latest definitions,
     download them from Windows Defender Security Intelligence .

How to install the Endpoint Protection client on the
reference computer
Install the Endpoint Protection client locally on the reference computer from a
command prompt. First get the installation file scepinstall.exe. For more information,
see Install the Endpoint Protection client from a command prompt.

If necessary, also include a preconfigured antimalware policy or with an antimalware
policy that you previously exported.

To install the Endpoint Protection client from a
command prompt
   1. Copy scepinstall.exe from the Client folder of the Configuration Manager
     installation folder to the computer on which you want to install the Endpoint
     Protection client software.

   2. Open a command prompt as an administrator. Change directory to the folder with
     the installer. Then run scepinstall.exe , adding any additional command-line
     properties that you require:

                                                                                  ﾉ   Expand table

      Property     Description

       /s          Run the installer silently

       /q          Extract the setup files silently

       /i          Run the installer normally

       /policy     Specify an antimalware policy file to configure the client during installation

       /sqmoptin   Opt-in to the Microsoft Customer Experience Improvement Program (CEIP)

<!-- p.70 -->

   3. Follow the on-screen instructions to complete the client installation.

   4. If you downloaded the latest update definition package, copy the package to the
     client computer, and then double-click the definition package to install it.

        ７ Note

        After the Endpoint Protection client install completes, the client automatically
        performs a definition update check. If this update check succeeds, you don't
        have to manually install the latest definition update package.

Example: install the client with an antimalware policy
scepinstall.exe /policy <full path>\<policy file>

Verify the Endpoint Protection client
installation
After you install the Endpoint Protection client on your reference computer, verify that
the client is working correctly.

   1. On the reference computer, open System Center Endpoint Protection from the
     Windows notification area.

   2. On the Home tab of the System Center Endpoint Protection dialog box, verify that
     Real-time protection is set to On.

   3. Verify that Up-to-date is displayed for Virus and spyware definitions.

   4. To make sure that your reference computer is ready for imaging, under Scan
     options, select Full, and then click Scan now.

Prepare the Endpoint Protection client for
imaging
Perform the following steps to prepare the Endpoint Protection client for imaging:

   1. On the reference computer, sign in as an administrator.

   2. Download and install PsExec from Windows SysInternals.

<!-- p.71 -->

   3. Run a command prompt as an administrator, change directory to the folder where
     you installed PsTools, and then type the following command:

     psexec.exe -s -i regedit.exe

        ） Important

        Use caution when you run the Registry Editor in this manner. PsExec.exe runs
        it in the LocalSystem context.

   4. In the Registry Editor, delete the following registry keys:

        ） Important

        Delete these registry keys as the last step before imaging the reference
        computer. The Endpoint Protection client recreates these keys when it starts. If
        you restart the reference computer, delete the registry keys again.

           HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft Antimalware\InstallTime

           HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft
           Antimalware\Scan\LastScanRun

           HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft

           Antimalware\Scan\LastScanType

           HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft

           Antimalware\Scan\LastQuickScanID

           HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft

           Antimalware\Scan\LastFullScanID

           HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\RemovalTools\MRT\GUID

You're now ready to prepare the reference computer for imaging.

When you deploy an OS image that contains the Endpoint Protection client, it
automatically reports information to the device's assigned Configuration Manager site.
The client downloads and applies any targeted antimalware policy.

See also

<!-- p.72 -->

For more information about OS deployment in Configuration Manager, see Manage OS
images.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.73 -->

Configure Endpoint Protection on a
standalone client
Article • 02/03/2023

Applies to: Configuration Manager (current branch)

Your organization may have a number of standalone clients that you cannot manage or
protect with Microsoft Configuration Manager. Without any endpoint protection in
place, these standalone clients are vulnerable to potential malware attacks. To protect
such standalone clients, you can manually configure them with Endpoint Protection, as
described in this topic.

  ７ Note

  If you install the endpoint protection client on a device that's not managed by
  Configuration Manager, a Management License (ML)           may be required for the
  device.

To configure Endpoint Protection on a standalone client manually:

      Create an antimalware policy for the standalone client
      Transfer Endpoint Protection client installation package to the standalone client
      Install Endpoint Protection on the standalone client

Prerequisites
The following are the prerequisites for configuring Endpoint Protection on a standalone
client:

      You must have access to the Endpoint Protection client installation package,
      scepinstall.exe. You can find this package in the C:\Program Files\Microsoft
      Configuration Manager\Client folder.
      Make sure that the January 2017 anti-malware platform update for Endpoint
      Protection clients   is installed.

Create an antimalware policy for the
standalone client

<!-- p.74 -->

In this step, you create a custom antimalware policy in the Configuration Manager
console and then transfer it to the standalone client.

When creating the antimalware policy, you must configure the definition update source
to keep the policy definitions up to date on the standalone client. You can configure the
definition update source as Microsoft Update and Microsoft Malware Protection Center,
if your standalone client is connected to the internet. Alternatively, select network share
as the definition distribution source and update it periodically with the latest definition
update package.

To create an antimalware policy for the standalone client:

   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, expand Endpoint Protection, and then
     click Antimalware Policies.

   3. On the Home tab, in the Create group, click Create Antimalware Policy.

   4. In the General section of the Create Antimalware Policy dialog box, enter a name
     and a description for the policy.

   5. In the Create Antimalware Policy dialog box, configure the settings that you
     require for this antimalware policy, and then click OK. For a list of settings that you
     can configure, see List of Antimalware Policy Settings.

        ７ Note

        For the Definition Updates setting, select Updates distributed from
        Microsoft Update and Updates distributed from Microsoft Malware
        Protection Center if your standalone client is connected to the internet.
        Alternatively, select Updates from UNC file shares to distribute the policy
        definitions through network share. Then, add one or more UNC paths to the
        location of the definition updates files on a network share.

   6. Export the newly created policy as an XML:
      a. In the Antimalware Policies list, right-click your policy.
      b. Select Export.
      c. Save the policy as an XML, for example, standalone.xml.

   7. Transfer the new antimalware policy XML to the target standalone client on which
     you want to configure Endpoint Protection.

<!-- p.75 -->

Transfer Endpoint Protection client installation
package to the standalone client
In this step, you copy the Endpoint Protection client installation package
(scepinstall.exe) from the Configuration Manager server and transfer it to the
standalone client.

   1. Log in to the Configuration Manager server.
   2. Navigate to the Client folder of the Configuration Manager installation folder
     (C:\Program Files\Microsoft Configuration Manager\Client).
   3. Copy scepinstall.exe.
   4. Transfer scepinstall.exe to the target standalone client on which you want to install
     the Endpoint Protection client software.

Install Endpoint Protection on the standalone
client
In this step, you run the installer package (scepinstall.exe) and the antimalware policy
(both previously transferred from the Configuration Manager server) from the command
prompt on the standalone client.

To install Endpoint Protection on the standalone client:

   1. On the standalone client, open a command prompt as an administrator.

   2. Change directory to the folder where you saved the scepinstall.exe installer file.

   3. Enter the following command to run scepinstall.exe with the antimalware policy:

        Windows Command Prompt

        scepinstall.exe /policy <full path>\<policy file>

     Replace full path with the path where you saved the antimalware policy XML file
     and policy file with the antimalware policy file name.

     The installer is extracted and the installation wizard is launched.

   4. Follow the on-screen instructions to complete the client installation.

     On the last screen of the installation wizard, the option to scan the computer for
     potential threats after getting the latest updates is selected by default. You can

<!-- p.76 -->

      clear the checkbox to skip the scanning.

Change antimalware policy settings on a
standalone Endpoint Protection client
To change or update the antimalware policy on your standalone Endpoint Protection
client:

   1. Create an antimalware policy for the standalone client.
   2. Run the following command on the standalone client:

  Windows Command Prompt

   C:\Program Files\Microsoft Security Client\ConfigSecurityPolicy.exe <full
   path>\<policy file>

Replace full path with the path where you saved the new antimalware policy XML file
and policy file with the antimalware policy file name.

Next steps
For information on how to use Endpoint Protection to manage security and malware on
Configuration Manager client computers, see Configure Endpoint Protection.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.77 -->

Use Group Policy settings to manage
Endpoint Protection in previous versions
of Windows
Article • 10/04/2022

Applies to:

      Microsoft Defender for Endpoint
      System Center Endpoint Protection on the following down-level devices:
         Windows Server 2012 R2
         Windows 8.1
         Windows Server 2012
         Windows 8
         Windows Server 2008 R2 SP1
         Windows 7 SP1
         Windows Server 2008 SP2
         Windows Vista

You may have a number of down-level or legacy Windows devices that are enabled with
Endpoint Protection—but are outside of your Configuration Manager hierarchy. For
example, devices in a demilitarized zone or devices that are integrated through mergers
and acquisitions.

You can manage Endpoint Protection in such devices using Group Policy settings,
described as follows:

      Copy Endpoint Protection policy definitions
      Load Endpoint Protection policy definitions into any of the following locations:
         Central Store on a Domain Controller (Recommended)
         Local device

  ７ Note

  For information on how to use Group Policy settings to manage Microsoft Defender
  Antivirus in Windows 10, Windows Server 2019, Windows Server 2016, or later as
  well as on Windows Server 2012 R2 after installing Microsoft Defender for
  Endpoint using the modern, unified solution see Use Group Policy settings to
  configure and manage Microsoft Defender Antivirus.

<!-- p.78 -->

Copy Endpoint Protection policy definitions
On a down-level Windows device that is managed by Endpoint Protection, copy the
Endpoint Protection policy definition files.

   1. Go to C:\Program Files\Microsoft Security Client\Admx.

   2. Compress the following files into a zip file, for example SCEP_admx.zip:

              EndPointProtection.adml
              EndPointProtection.admx

   3. Copy the zip file into a temporary folder. For example, C:\temp_SCEP_GPO_admx.

   4. Extract the file.

  ７ Note

  The registry keys to configure Endpoint Protection policy settings are located in
  Hkey_Local_Machine\Software\Policies\Microsoft\Microsoft Antimalware.

Load Endpoint Protection Group Policy settings
into a Central Store on a domain controller
If you are using a Central Store for Group Policy Administrative Templates   , perform
the following steps to load and configure Endpoint Protection Group policy settings.
This is the recommended method.

   1. Go to the folder where you extracted the Endpoint Protection policy definition
     files.

   2. Copy the .admx and .adml files into the PolicyDefinitions folder on the domain
     controller:
      a. Copy EndPointProtection.admx into \\<forest.root>\SYSVOL\
         <domain>\Policies\PolicyDefinitions.
      b. Copy EndPointProtection.adml into \\<forest.root>\SYSVOL\
         <domain>\Policies\PolicyDefinitions\en-US.

     For example:

              Copy EndPointProtection.admx into
              \DC\SYSVOL\contoso.com\Policies\PolicyDefinitions.

<!-- p.79 -->

              Copy EndPointProtection.adml into
              \DC\SYSVOL\contoso.com\Policies\PolicyDefinitions\en-US.

     where DC is the name of your Domain Controller and contoso.com is your domain.

   3. Open the Group Policy Management Console and create a new Group Policy
     Object (GPO) in your domain, for example Endpoint Protection.

   4. Right-click the GPO for Endpoint Protection and click Edit.

   5. In the Group Policy Management Editor, go to Computer Configuration > Policies
     > Administrative Templates: Policy definitions > Windows Components >
     Endpoint Protection.

     The list of Endpoint Protection Group Policies is displayed.

   6. Expand the section that contains the setting you want to configure, double-click
     the setting to open it, and make configuration changes.

Load Endpoint Protection Group Policy settings
into your local device
Instead of using Central Store for loading Endpoint Protection policy definitions, you can
store them locally into your device.

   1. Go to the folder where you extracted the Endpoint Protection policy definition
     files.

   2. Copy the .admx and .adml files into your local PolicyDefinitions folder.
      a. Copy EndPointProtection.admx into %SystemRoot%/PolicyDefinitions.
     b. Copy EndPointProtection.adml into %SystemRoot%/PolicyDefinitions/en-US.

     For example:

              Copy EndPointProtection.admx into C:\Windows\PolicyDefinitions.
              Copy EndPointProtection.adml into C:\Windows\PolicyDefinitions\en-US.

   3. Open Local Group Policy Editor.

   4. Go to Computer Configuration > Administrative Templates > Windows
     Components > Endpoint Protection.

     The list of Endpoint Protection Group Policies is displayed.

<!-- p.80 -->

   5. Expand the section that contains the setting you want to configure, double-click
     the setting to open it, and make configuration changes.

Next steps
     For an overview on Endpoint Protection, see Endpoint Protection.
     For information on configuring Endpoint Protection on a standalone client
     manually, see Configure Endpoint Protection on a standalone client.

Feedback
Was this page helpful?      Yes    No

Provide product feedback
