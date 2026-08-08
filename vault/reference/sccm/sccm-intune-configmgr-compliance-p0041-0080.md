---
title: "Device compliance documentation — pages 41-80"
type: reference
domain: sccm
slug: sccm-intune-configmgr-compliance-p0041-0080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-compliance-p0041-0080
family: sccm
documentKind: "doc"
abstract: "The File system setting type doesn't support specifying a UNC path to a network share in the Path box. If you use the %USERPROFILE% environment variable in the Path or File or folder name boxes, the Configuration Manager client searches all user profiles on the client computer."
---

# Device compliance documentation — pages 41-80

<!-- p.41 -->

     The File system setting type doesn't support specifying a UNC path to a
     network share in the Path box.

     If you use the %USERPROFILE% environment variable in the Path or File or folder
     name boxes, the Configuration Manager client searches all user profiles on the
     client computer. This behavior could result in it finding multiple instances of the
     file or folder.

     If compliance settings don't have access to the specified path, a discovery error
     is generated. Additionally, if the file you are searching for is currently in use, a
     discovery error is generated.

         Tip

        Select Browse to configure the setting from values on a reference
        computer.

   File or folder name: Specify the name of the file or folder object to search for. You
   can specify system environment variables and the %USERPROFILE% environment
   variable in the file or folder name. You can also use the wildcards * and ? in the
   file name.
     If you specify a file or folder name and use wildcards, this combination might
     produce a high number of results. It could also result in high resource use on
     the client computer, and high network traffic when reporting results to
     Configuration Manager.

   Include subfolders: Also search any subfolders under the specified path.

   This file or folder is associated with a 64-bit application: If enabled, only search
   64-bit file locations such as %ProgramFiles% on 64-bit computers. If this option isn't
   enabled, search both 64-bit locations and 32-bit locations such as
   %ProgramFiles(x86)% .

     If the same file or folder exists in both the 64-bit and 32-bit system file locations
     on the same 64-bit computer, multiple files are discovered by the global
     condition.

IIS metabase
   Metabase path: Specify a valid path to the Internet Information Services (IIS)
   metabase. For example, /LM/W3SVC/ .

   Property ID: Specify the numeric property of the IIS metabase setting.

<!-- p.42 -->

Registry key
     Hive: Select the registry hive that you want to search
        Select Browse to configure the setting from values on a reference computer. To
        browse to a registry key on a remote computer, enable the Remote Registry
        service on the remote computer.

     Key: Specify the registry key name that you want to search for. Use the format
     key\subkey .

     This registry key is associated with a 64-bit application: Search 64-bit registry
     keys in addition to the 32-bit registry keys on clients that are running a 64-bit
     version of Windows.
        If the same registry key exists in both the 64-bit and 32-bit registry locations on
        the same 64-bit computer, both registry keys are discovered by the global
        condition.

Registry value
     Hive: Select the registry hive to search.
        Select Browse to configure the setting from values on a reference computer. To
        browse to a registry value on a remote computer, enable the Remote Registry
        service on the remote computer. You also need administrator permissions to
        access the remote computer.

     Key: Specify the registry key name to search for. Use the format key\subkey .

     Value: Specify the value that must be contained within the specified registry key.

     This registry key is associated with a 64-bit application: Search the 64-bit registry
     keys in addition to the 32-bit registry keys on clients that are running a 64-bit
     version of Windows.
        If the same registry key exists in both the 64-bit and 32-bit registry locations on
        the same 64-bit computer, both registry keys are discovered by the global
        condition.

Script
The value returned by the script is used to assess the compliance of the global
condition. For example, when using VBScript, you could use the command WScript.Echo
Result to return the Result variable value to the global condition. When you use
Windows PowerShell as a discovery or remediation script, the Configuration Manager

<!-- p.43 -->

client calls PowerShell with the -NoProfile parameter. This option starts PowerShell
without profiles. A PowerShell profile is a script that runs when PowerShell starts.

     Discovery script: Select Add Script, and enter or browse to a script. This script is
     used to find the value. You can use Windows PowerShell, VBScript, or Microsoft
     JScript scripts.

     Remediation script (optional): Select Add Script, and enter or browse to a script.
     This script is used to remediate non-compliant setting values. You can use
     Windows PowerShell, VBScript, or Microsoft JScript scripts.

        ） Important
           To properly report a remediation failure, scripts need to throw exceptions
           rather than a nonzero exit code.

     Run scripts by using the logged on user credentials: If you enable this option, the
     script runs on client computers that use the credentials of the signed-in user.

  ） Important

        When using a signed PowerShell script, ensure you select Open. You can't use
        copy and paste for a signed script.
        Starting in 2207, you can define a Script Execution Timeout (seconds) when
        configuring client settings for compliance settings.

SQL query
     SQL Server instance: Choose whether you want the SQL query to run on the
     default instance, all instances, or a specified database instance name. The instance
     name must refer to a local instance of SQL Server. To refer to a SQL Server Always
     On failover cluster instance or availability group, use a script setting.

     Database: Specify the name of the Microsoft SQL Server database against which
     you want to run the SQL query.

     Column: Specify the column name returned by the Transact-SQL statement that's
     used to assess the compliance of the global condition.

     Transact-SQL statement: Specify the full SQL query you want to use for the global
     condition. To use an existing SQL query, select Open.

<!-- p.44 -->

        ） Important

        SQL query settings don't support any SQL commands that modify the
        database. You can only use SQL commands that read information from the
        database.

WQL query
     Namespace: Specify the WMI namespace that's assessed for compliance on client
     computers. The default value is root\cimv2 .

     Class: Specify the target WMI class in the above namespace.

     Property: Specify the target WMI property in the above class.

     WQL query WHERE clause: Specify a qualifying clause to reduce the results. For
     example, to only query the DHCP service in the Win32_Service class, the WHERE
     clause could be Name = 'DHCP' and StartMode = 'Auto' .

XPath query
     Path: Specify the path of the .xml file on client computers that is used to assess
     compliance. Configuration Manager supports the use of all Windows system
     environment variables and the %USERPROFILE% user variable in the path name.

     XML file name: Specify the file name containing the XML query in the above path.

     Include subfolders: Enable this option to search any subfolders under the specified
     path.

     This file is associated with a 64-bit application: Search the 64-bit system file
     location %Windir%\System32 in addition to the 32-bit system file location
      %Windir%\Syswow64 on Configuration Manager clients that are running a 64-bit

     version of Windows.

     XPath query: Specify a valid full XML path language (XPath) query.

     Namespaces: Identify namespaces and prefixes to be used during the XPath query.

If you attempt to discover an encrypted .xml file, compliance settings find the file, but
the XPath query produces no results. The Configuration Manager client doesn't generate
an error.

<!-- p.45 -->

If the XPath query isn't valid, the setting is evaluated as noncompliant on client
computers.

Configure compliance rules
Compliance rules specify the conditions that define the compliance of a configuration
item. Before a setting can be evaluated for compliance, it must have at least one
compliance rule. WMI, registry, and script settings let you remediate values that are
found to be noncompliant. You can create new rules or browse to an existing setting in
any configuration item to select rules in it.

To create a compliance rule
   1. On the Compliance Rules page of the Create Configuration Item Wizard, select
     New.

   2. In the Create Rule dialog box, provide the following information:

            Name: Enter a name for the compliance rule.

            Description: Enter a description for the compliance rule.

            Selected setting: Select Browse to open the Select Setting dialog box. Select
            the setting that you want to define a rule for, or select New Setting. When
            you're finished, choose Select.

               Tip

              To view information about the currently selected setting, select
              Properties.

            Rule type: Select the type of compliance rule that you want to use:

              Value: Create a rule that compares the value returned by the configuration
              item against a value that you specify. For more information on the
              additional settings, see Value rules.

              Existential: Create a rule that evaluates the setting depending on whether
              it exists on a client device or on the number of times it's found. For more
              information on the additional settings, see Existential rules.

   3. Select OK to close the Create Rule dialog box.

<!-- p.46 -->

Value rules
   Property: The property of the object to check varies depending upon the selected
   setting. The available properties vary based on the type of setting.

   The setting must comply with the following...: The available rules or permissions
   vary based on the type of setting.

   Remediate noncompliant rules when supported: Select this option for
   Configuration Manager to automatically remediate non-compliant rules.
   Configuration Manager supports this action with the following rule types:

      Registry value: If it's noncompliant, the client sets the registry value. If it doesn't
      exist, the client creates the value.

      Script: The client uses the remediation script that you specified with the setting.

      WQL query

     ） Important
        To properly report a remediation failure, scripts need to throw exceptions
        rather than a nonzero exit code.
        You can only remediate noncompliant rules when the rule operator is set to
        Equals.

   Report noncompliance if this setting instance is not found: If this setting isn't
   found on client computers, enable this option for the configuration item to report
   noncompliance.

   Noncompliance severity for reports: Specify the severity level that's reported in
   Configuration Manager reports if this compliance rule fails. The following severity
   levels are available:
      None
      Information
      Warning
      Critical
      Critical with event: Computers that fail this compliance rule report a failure
      severity of Critical. This severity level is also logged as a Windows event in the
      application event log.

Existential rules

<!-- p.47 -->

  ７ Note

  The options shown might vary depending on the setting type you're configuring a
  rule for.

     The setting must exist on client devices

     The setting must not exist on client devices

     The setting occurs the following number of times:

     Noncompliance severity for reports: Specify the severity level that's reported in
     Configuration Manager reports if this compliance rule fails. The following severity
     levels are available:
        None
        Information
        Warning
        Critical
        Critical with event: Computers that fail this compliance rule report a failure
        severity of Critical. This severity level is also logged as a Windows event in the
        application event log.

Track configuration item remediations
(Introduced in version 2002)

Starting in Configuration Manager version 2002, you can Track remediation history
when supported on your configuration item compliance rules. When this option is
enabled, any remediation that occurs on the client for the configuration item generates
a state message. The history is stored in the Configuration Manager database.

Build custom reports to view the remediation history by using the public view
v_CIRemediationHistory. The RemediationDate column is the time, in UTC, the client ran
the remediation. The ResourceID identifies the device. Building custom reports with the
v_CIRemediationHistory view helps you:

     Identify possible issues with your remediation scripts
     Find trends in remediations such as a client that is consistently non-compliant each
     evaluation cycle.

<!-- p.48 -->

Enable the Track remediation history when supported
option
     For new configuration items, add the Track remediation history when supported
     option in the Compliance Rules tab when you create a new setting on the wizard's
     Settings page.
     For existing configuration items, add the Track remediation history when
     supported option on the Compliance Rules tab in the configuration item
     Properties.

                                                                                

Next steps
Create configuration baselines

Feedback

<!-- p.49 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.50 -->

How to create child configuration items
in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Child configuration items in Configuration Manager are copies of configuration items
that retain a relationship to the original configuration item in that they inherit the
original configuration from the parent configuration item.

When you view the properties of a child configuration item in the Configuration
Manager console, you cannot edit the inherited objects and settings with their
validation criteria. However, you can add and then edit additional validation criteria to
the child configuration item, and you can also add new objects and settings to the child
configuration item. An example for creating and editing a child configuration item is to
refine the original configuration item to meet your business requirements.

  ７ Note

  You can only create child configuration items from configuration items of the type
  Windows Desktops and Servers (custom).

To create a child configuration item
   1. In the Configuration Manager console, click Assets and Compliance > Compliance
      Settings > Configuration Items.

   2. In the Configuration Items list, select the configuration item for which you want to
      create a child configuration item, and then in the Home tab, in the Configuration
      Item group, click Create Child Configuration Item.

   3. On the General page of the Create Child Configuration Item Wizard, you can
      choose a specific revision of the parent configuration item to use to create the
      child. Other steps in this wizard are identical to those you would use to create a
      standard configuration item. For more information, see How to create custom
      configuration items for Windows desktop and server computers.

   4. Complete the wizard. The new child configuration item displays in the
      Configuration Items list.

<!-- p.51 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.52 -->

Create configuration baselines in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration baselines in Configuration Manager contain predefined configuration
items and optionally, other configuration baselines. After a configuration baseline is
created, you can deploy it to a collection so that devices in that collection download the
configuration baseline and assess their compliance with it.

   Tip

  There's no way to specify the order that the Configuration Manager client evaluates
  the configuration items in a baseline. It's non-deterministic.

Configuration baselines
Configuration baselines in Configuration Manager can contain specific revisions of
configuration items or can be configured to always use the latest version of a
configuration item. For more information about configuration item revisions, see
Management tasks for configuration data.

There are two methods that you can use to create configuration baselines:

      Import configuration data from a file. To start the Import Configuration Data
      Wizard, in the Configuration Items or Configuration Baselines node in the Assets
      and Compliance workspace, click Import Configuration Data. For more
      information, see Import configuration data.

      Use the Create Configuration Baseline dialog box to create a new configuration
      baseline.

Create a configuration baseline
To create a configuration baseline by using the Create Configuration Baseline dialog
box, use the following procedure:

<!-- p.53 -->

1. In the Configuration Manager console, click Assets and Compliance > Compliance
  Settings > Configuration Baselines.

2. On the Home tab, in the Create group, click Create Configuration Baseline.

3. In the Create Configuration Baseline dialog box, enter a unique name and a
  description for the configuration baseline. You can use a maximum of 255
  characters for the name and 512 characters for the description.

4. The Configuration data list displays all configuration items or configuration
  baselines that are included in this configuration baseline. Click Add to add a new
  configuration item or configuration baseline to the list. You can choose from the
  following items:

       Configuration Items

       Software Updates

       Configuration Baselines

           ） Important

           You must limit each configuration baseline to no more than 1000
           software updates.

5. Use the Change Purpose list to specify the behavior of a configuration item that
  you've selected in the Configuration data list. You can select from the following
  items:

       Required: The configuration baseline is evaluated as noncompliant if the
       configuration item isn't detected on a client device. If it's detected, it's
       evaluated for compliance

       Optional: The configuration item is only evaluated for compliance if the
       application it references is found on client computers. If the application is not
       found, the configuration baseline isn't marked as noncompliant (only
       applicable to application configuration items).

       Prohibited: The configuration baseline is evaluated as noncompliant if the
       configuration item is detected on client computers (only applicable to
       application configuration items).

    ７ Note

<!-- p.54 -->

        The Change Purpose list is available only if you clicked the option This
        configuration item contains application settings on the General page of the
        Create Configuration Item Wizard.

   6. Use the Change Revision list to select a specific or the latest revision of the
     configuration item to assess for compliance on client devices or select Always Use
     Latest to always use the latest revision. For more information about configuration
     item revisions, see Management tasks for configuration data.

   7. To remove a configuration item from the configuration baseline, select a
     configuration item, and then click Remove.

   8. Starting in version 1806, select if you want to Always apply this baseline for co-
     managed clients. When checked, this baseline will apply even on clients that are
     managed by Intune. This exception might be used to configure settings that are
     required by your organization but not yet available in Intune.

   9. Optionally, click on Categories to assign categories to the baseline for searching
     and filtering.

 10. Click OK to close the Create Configuration Baseline dialog box and to create the
     configuration baseline.

  ７ Note

  Modifying an existing baseline, such as setting Always apply this baseline for co-
  managed clients, will increment the baseline content version. Clients will need to
  evaluate the new version to update the baseline reporting.

Include custom configuration baselines as part
of compliance policy assessment
You can add evaluation of custom configuration baselines as a compliance policy
assessment rule. When you create or edit a configuration baseline, you have an option
to Evaluate this baseline as part of compliance policy assessment. When adding or
editing a compliance policy rule, you have a condition called Include configured
baselines in compliance policy assessment. For co-managed devices, and when you
configure Intune to take Configuration Manager compliance assessment results as part
of the overall compliance status, this information is sent to Microsoft Entra ID. You can

<!-- p.55 -->

then use it for Conditional Access to your Microsoft 365 Apps resources. For more
information, see Conditional Access with co-management.

To include custom configuration baselines as part of compliance policy assessment, do
the following:

     Create and deploy a compliance policy to a user collection with a rule to Include
     configured baselines in compliance policy assessment.
     Select Evaluate this baseline as part of compliance policy assessment in a
     configuration baseline deployed to a device collection.

  ） Important

        The configuration baseline must be deployed to a device collection. Baselines
        deployed to user collections aren't honored when these settings are used.
        When targeting devices that are co-managed, ensure you meet the co-
        management prerequisites. Co-managed clients ignore service windows for
        remediation when their compliance policies workload is managed by Intune.
        For devices managed by Configuration Manager, the client honors the service
        window for compliance policy remediation. To ignore the service window and
        remediate immediately, select Check compliance in the Software Center.

Example evaluation scenario
When a user is part of a collection targeted with a compliance policy that includes the
rule condition Include configured baselines in compliance policy assessment, any
baselines with the Evaluate this baseline as part of compliance policy assessment
option selected that are deployed to the user or the user's device are evaluated for
compliance. For example:

     User1 is part of User Collection 1 .

     User1 uses Device1 , which is in Device Collection 1 and Device Collection 2 .
     Compliance Policy 1 has the Include configured baselines in compliance policy

     assessment rule condition and is deployed to User Collection 1 .
     Configuration Baseline 1 has Evaluate this baseline as part of compliance policy

     assessment selected and is deployed to Device Collection 1 .
     Configuration Baseline 2 has Evaluate this baseline as part of compliance policy

     assessment selected and is deployed to Device Collection 2 .

<!-- p.56 -->

In this scenario, when Compliance Policy 1 evaluates for User1 using Device1 , both
Configuration Baseline 1 and Configuration Baseline 2 are evaluated too.

     User1 sometimes uses Device2 .
     Device2 is a member of Device Collection 2 and Device Collection 3 .

     Device Collection 3 has Configuration Baseline 3 deployed to it, but Evaluate

     this baseline as part of compliance policy assessment isn't selected.

When User1 uses Device2 , only Configuration Baseline 2 gets evaluated when
Compliance Policy 1 evaluates.

  ７ Note

  If the compliance policy evaluates a new baseline that has never been evaluated on
  the client before, it may report non-compliance. This occurs if the baseline
  evaluation is still running when the compliance is evaluated. To workaround this
  issue, click Check compliance in the Software Center.

Create and deploy a compliance policy with a rule for
baseline compliance policy assessment
   1. In the Assets and Compliance workspace, expand Compliance Settings, then
     select the Compliance Policies node.

   2. Click Create Compliance Policy in the ribbon to bring up the Create Compliance
     Policy Wizard.

   3. On the General page, select Compliance rules for devices managed with the
     Configuration Manager client.

           Devices must be managed with the Configuration Manager client to include
           custom configuration baselines as part of compliance policy assessment.

   4. Select your platforms on the Supported Platforms pages.

   5. On the Rules page, select New, then select the Include configured baselines in
     compliance policy assessment condition.

<!-- p.57 -->

  6. Click OK, then Next to get to the Summary page.

  7. Verify your selections and click Next then Close.

  8. In the Compliance Policies node, right-click on the policy you created, and select
    Deploy.

  9. Choose your collection, alert generation settings, and your compliance evaluation
    schedule for the policy.

 10. Click OK to deploy the compliance policy.

Select a configuration baseline and check "Evaluate this
baseline as part of compliance policy assessment"
  1. In the Assets and Compliance workspace, expand Compliance Settings, then
    select the Configuration Baselines node.

  2. Right-click on an existing baseline that's deployed to a device collection, then
    select Properties. If needed, you can create a new baseline.

          The baseline must be deployed to a device collection, not a user collection.

<!-- p.58 -->

  3. Enable the Evaluate this baseline as part of compliance policy assessment setting.

          For co-managed devices that have Intune as the Device configuration
          authority, ensure Always apply this baseline even for co-managed clients is
          also selected.

  4. Click OK to save the changes to your configuration baseline.

Log files for custom configuration baselines as part of
compliance policy assessment
     ComplianceHandler.log
     SettingsAgent.log
     DCMAgent.log
     CIAgent.log

Next steps
Import configuration data

<!-- p.59 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.60 -->

How to deploy configuration baselines in
Configuration Manager
Applies to: Configuration Manager (current branch)

Configuration baselines in Configuration Manager must be deployed to one or more collections
of users or devices before client devices in those collections can assess their compliance with the
configuration baseline.

Use the Deploy Configuration Baselines dialog box to define configuration baseline
deployments, which includes adding or removing configuration baselines from deployments in
addition to specifying the evaluation schedule.

Deploy a configuration baseline
   1. In the Configuration Manager console, click Assets and Compliance > Compliance Settings
     > Configuration Baselines.

   2. In the Configuration Baselines list, select the configuration baseline that you want to
     deploy, and then in the Home tab, in the Deployment group, click Deploy.

   3. In the Deploy Configuration Baselines dialog box, select the configuration baselines that
     you want to deploy in the Available configuration baselines list. Click Add to add these to
     the Selected configuration baselines list.

        ） Important

        If you change a configuration item that has been added to a deployed configuration
        baseline, the revised configuration item is not evaluated for compliance until its next
        scheduled evaluation time.

   4. Specify the following additional information:

           Remediate noncompliant rules when supported – Automatically remediates any rules
           that are noncompliant for Windows Management Instrumentation (WMI), the registry,
           scripts, and all settings for mobile devices that are enrolled by Configuration Manager.

<!-- p.61 -->

       Allow remediation outside the maintenance window – If a maintenance window has
       been configured for the collection to which you are deploying the configuration
       baseline, enable this option to let compliance settings remediate the value outside of
       the maintenance window. For more information about maintenance windows, see How
       to use maintenance windows.

5. Generate an alert – Configures an alert that is generated if the configuration baseline
  compliance is less than a specified percentage by a specified date and time. You can also
  specify whether you want an alert to be sent to System Center Operations Manager.

6. Collection - Click Browse to select the collection where you want to deploy the
  configuration baseline.

7. Specify the compliance evaluation schedule for this configuration baseline Specifies the
  schedule by which the deployed configuration baseline is evaluated on client computers.
  This can be either a simple or a custom schedule.

    ７ Note

    When the client actually evaluates the baseline

          Computer-targeted deployments. After the first evaluation on a given client, the
          baseline is evaluated within a 2-hour randomization window of each scheduled
          start time. The first evaluation on a Windows client device is additionally gated by
          two launch conditions: the device must be on power (above the low-battery
          threshold) and the user must be idle. If either condition isn't met at the scheduled
          time, the first evaluation is deferred until both become true, or until an internal
          24-hour deadline elapses, whichever happens first. On Windows Server, the idle
          check is skipped, so the first evaluation also runs within the 2-hour window.
          User-targeted deployments. The baseline is evaluated the next time the target
          user signs in to a client that has received the deployment policy. The 2-hour
          randomization window doesn't apply to user-targeted deployments.

    For details and how to confirm the client-side behavior in Scheduler.log , see How the
    Configuration Manager client evaluates a deployed baseline.

8. Click OK to close the Deploy Configuration Baselines dialog box and to create the
  deployment. For more information about how to monitor the deployment, see Monitor
  compliance settings.

<!-- p.62 -->

How the Configuration Manager client evaluates a
deployed baseline
The evaluation time you configure in the deployment ("Simple schedule" or "Custom schedule")
is a target time — it isn't a guaranteed run time. The Configuration Manager client applies launch
conditions and a 2-hour randomization window on top of your schedule. Understanding these
helps you reconcile the schedule you set in the console with what actually happens on the client
— which you can inspect in Scheduler.log , and, to a lesser extent, in the Configuration Manager
Support Center client tool.

Launch conditions
Every scheduled evaluation of a baseline carries two launch conditions:

                                                                                                ﾉ   Expand table

 Condition            How the client determines it

 Battery above the    On a laptop, the battery must be higher than the Windows "low battery" level, or the
 low threshold        device must be on AC power. Devices without a battery (desktops, servers) always
                      satisfy this.

 User is idle         Determined by a hidden Windows Task Scheduler task the Configuration Manager
                      client installs during setup. See How the client determines idle state.

If both conditions are met when the trigger fires, the evaluation runs within the built-in 2-hour
randomization window of the scheduled start time.

If either condition isn't met, the evaluation is placed in a pending queue on the client. It runs as
soon as the conditions become true (the client is notified when the user goes idle or the device is
plugged in), or when an internal 24-hour (1440-minute) deadline is reached — whichever
happens first.

How the client determines idle state

The Configuration Manager client doesn't measure idle state directly. Instead, at client installation
on Windows client editions, setup registers a hidden Windows Task Scheduler task:

 \Microsoft\Configuration Manager\Configuration Manager Idle Detection

<!-- p.63 -->

The task has the following characteristics:

     Trigger: On idle ( TASK_TRIGGER_IDLE ) — Windows Task Scheduler fires the task when its
     own idle heuristics report the machine as idle.
     Stop when the machine is no longer idle: enabled. When Windows reports the machine as
     no longer idle, the task is stopped.
     Runs on battery: yes — the task deliberately doesn't restrict itself to AC power, because
     Windows Task Scheduler itself governs whether idle work should run based on the current
     power state.
     Runs as: SYSTEM , hidden.
     Action: invokes a COM handler in the Configuration Manager client agent, which flips the
     client's cached idle state to "idle" while the task is running and to "not idle" when the task
     stops.

Because the trigger is a standard Windows idle trigger and the client doesn't override the
trigger's IdleDuration or WaitTimeout , the definition of "idle" is the one used by Windows Task
Scheduler itself — that is, low CPU and disk activity combined with no user input for the interval
configured in Windows. For a full description of how Windows Task Scheduler decides a machine
is idle, see Task Idle Conditions.

  ７ Note

        The idle launch condition is enforced on Windows client devices and not on Windows
        Server.
        For Windows client devices with continuously active users, If a user is signed in and
        using the device throughout the scheduled evaluation window (moving the mouse,
        typing, running CPU-intensive work), Windows Task Scheduler may never fire the idle
        trigger, so the client never reports "idle" and the first evaluation is deferred until the
        24-hour deadline elapses.

Why first-run timing differs from subsequent runs
Although launch conditions are checked on every scheduled evaluation, the client also keeps a
per-schedule history of the previous pending-queue wait. If the elapsed time since the last time
the schedule was pending is already greater than the 24-hour deadline (which is the case for any
recurring schedule of daily or longer cadence), the client shortens the pending timer to one
minute and lets the schedule fire without waiting for the launch conditions to become true.

<!-- p.64 -->

The net effect for administrators:

     First evaluation on a given client. No prior history exists, so the full 24-hour deadline
     applies. On a Windows client device where a user is actively signed in at the scheduled time,
     the first evaluation can be delayed by up to 24 hours.
     All subsequent evaluations. The client's history of the previous wait shortens the pending
     timer to one minute, so the evaluation runs within the 2-hour randomization window
     regardless of user presence or power state.
     Windows Server. The idle check is skipped entirely, so every evaluation — including the first
     — runs within the 2-hour window.

For example, a baseline configured to evaluate every Sunday at 03:00 will, on its first run:

     Evaluate on Sunday between 03:00 and 05:00 on machines where the user was idle at 03:00.
     Evaluate up to 24 hours later (Monday) on machines where a user was actively signed in and
     using the device at 03:00.

All subsequent Sunday runs on both machines evaluate on Sunday within the 2-hour
randomization window.

Troubleshoot evaluation timing on the client
Use one of the following options to inspect what the client is doing with a scheduled baseline
evaluation.

Find the schedule ID for your baseline deployment

The Configuration Manager client tracks each baseline deployment — not each baseline — using
the deployment's Assignment ID. That same Assignment ID appears in Scheduler.log (prefixed
with the schedule target) and in the client's WMI. Support Center also shows it as part of the
deployment policy. Getting this ID is the first step to correlate console-side and client-side data.

To find the Assignment ID from the console:

   1. In the Configuration Manager console, go to Monitoring > Deployments.
   2. Filter the list by Feature Type = Baseline and locate your baseline deployment. If the
     Deployment ID column isn't shown, right-click the column header, choose Column
     Settings, and add it.
   3. Copy the value from the Deployment ID column — this is the Assignment ID, a GUID similar
     to {01234567-89AB-CDEF-0123-456789ABCDEF} .

<!-- p.65 -->

Alternatively, query the SMS Provider directly:

  PowerShell

  Get-CMBaselineDeployment -Name "<baseline name>" |
      Select-Object AssignmentName, AssignmentUniqueID, TargetCollectionID

The AssignmentUniqueID value is what you'll look for on the client.

  ７ Note

          In Scheduler.log , the Assignment ID is always prefixed with the schedule's target —
           Machine/ for device-targeted deployments, or <UserSID>/ for user-targeted

          deployments. For example, Machine/{01234567-89AB-CDEF-0123-456789ABCDEF} .
          The client also creates auxiliary schedules for the same deployment with event prefixes
          on the ID itself — for example, DEADLINE:<AssignmentUniqueID> for the enforcement
          deadline. The base Assignment ID (no event prefix) is the main evaluation schedule; the
          event-prefixed variants govern related events.

Inspect Scheduler.log

Open %WINDIR%\CCM\Logs\Scheduler.log on the client. Each scheduled fire of a baseline evaluation
is announced with an entry like the following, which contains both the internal trigger cookie and
the schedule ID (the deployment's Assignment ID, prefixed with Machine/ or the target user's
SID):

  SMSTrigger 'DA089D0000100008' for scheduler 'Machine/{01234567-89AB-CDEF-0123-
  456789ABCDEF}' will fire at 06/27/2026 05:10:00 PM with randomization.

See Find the schedule ID for your baseline deployment above for how to obtain the GUID from
the console. A two-pass search of Scheduler.log gives the complete picture:

   1. First pass — filter by the scheduler string (for example Machine/{01234567-89AB-CDEF-0123-
        456789ABCDEF} ) to see what happened to that specific deployment.

   2. Second pass — remove the filter and look at the surrounding timeframe for global
        resource events (idle, power). These entries don't carry a schedule ID, so they won't appear
        in the filtered view.

<!-- p.66 -->

Per-schedule entries (contain the schedule ID; visible in the filtered view):

                                                                                             ﾉ   Expand table

 Entry                                     What it means

 SMSTrigger '<cookie>' for scheduler       The next scheduled fire time for this deployment, including the
 '<Machine\|SID>/<id>' will fire at        randomization window that will be applied.
 <time> with randomization.

 Schedule '<id>' with condition 0xa is     The launch conditions aren't currently met. 0xa is the bitmask
 putted into the pending queue.            for on-battery-above-low + idle.

 >>> Adjusted deadline minutes from 1440   The client shortened the pending timer based on its history of
 to <N> for schedule '<id>' because it     the previous wait. On any recurring baseline of daily-or-longer
 was pending for a while.                  cadence, <N> is 1 , which is why the second and later
                                           evaluations don't wait for the launch conditions.

 >>> Delay firing schedule '<id>'          The launch conditions have been met (or the pending timer
                                           elapsed) and the evaluation is starting.

Global resource entries (no schedule ID; view without a filter):

                                                                                             ﾉ   Expand table

 Entry                                     What it means

 [Resource-Idle] Returning value 0.        The client currently considers the device not idle (a user is
                                           present or otherwise active).

 [Resource-Idle] Returning value 1.        The client currently considers the device idle.

 [Resource-Power] Raised event             The device's power state changed (AC / battery high / battery
 'PowerStatus : <state>'                   low / critical).

If you see a first-run "putted into the pending queue" entry followed hours later by "Delay firing
schedule" only after the timer elapsed, the device never went idle during the wait window — this
is expected first-run behavior on a Windows client device with an active user.

   Tip

  To evaluate a baseline immediately without waiting for the schedule or the launch
  conditions, open Configuration Manager in the Control Panel on the client, go to the
  Configurations tab, select the baseline, and click Evaluate. Results are cached for 15 minutes
  — see Monitor compliance settings for details.

<!-- p.67 -->

Last updated on 07/08/2026

<!-- p.68 -->

Manage configuration data in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you have created configuration items and configuration baselines in Configuration
Manager, further commands are available to help you perform various actions.

Manage configuration items
      In the Assets and Compliance workspace, expand Compliance Settings >
      Configuration Items, select the configuration item to manage, and then select a
      management task.

                                                                                      ﾉ   Expand table

 Management            Details
 task

 Create Child          Opens the Create Child Configuration Item Wizard where you can create a
 Configuration         child configuration item from the selected configuration item.
 Item
                       You cannot create a child configuration item from a mobile device
                       configuration item.

                       For details, see Create child configuration items.

 Revision History      Opens the Configuration Item Revision History dialog box where you can
                       view and manage previous revisions of the selected configuration item.

 View XML              Displays the XML definition file for the selected configuration item in a new
 Definition            window. This information can be useful when you want to author
                       configuration data manually.

 Export                Exports a configuration item in a cabinet (.cab) file format, providing that it
                       was created at that site. You can then import it to the same or a different
                       Configuration Manager site. Configuration data is converted to DCM Digest.

 Copy                  Creates a copy of the selected configuration item with a name you specify.
                       The new configuration item does not retain any relationship to the original
                       configuration item. This means that the duplicate configuration item does
                       not continue to inherit configuration information from the original
                       configuration item.

<!-- p.69 -->

Management          Details
task

Delete              Opens the Delete Configuration Item dialog box where you can review any
                    references to this configuration item.

                    You must remove all references to a configuration item before you can delete
                    the configuration item.

Manage configuration baselines
       In the Assets and Compliance workspace, expand Compliance Settings >
       Configuration Baselines, select the configuration baseline to manage, and then
       select a management task.

                                                                                  ﾉ   Expand table

Management          Details
task

Show Members        Displays all of the configuration items that are referenced by the
                    configuration baseline.

Schedule            Configures the schedule by which the data shown in the Configuration
Summarization       Baselines node in the Configuration Manager console is updated with the
                    latest information from the site database.

Run                 Summarization causes the data in the Configuration Baselines node to be
Summarization       refreshed with the latest data from the site database. This action might take
                    several minutes to complete. You might have to click Refresh before you can
                    see the latest data in the console.

View XML            Displays the XML definition file for the selected configuration baseline in a
Definition          new window. This information can be useful when you want to author
                    configuration data manually.

Enable              Enables a configuration baseline for compliance monitoring.

Disable             Disables a configuration baseline so it is no longer evaluated for compliance
                    on client computers. Configuration baselines that reference this configuration
                    baseline will also be disabled.

Export              Exports a configuration baseline in a cabinet (.cab) file format, providing that
                    it was created at that site. You can then import it to the same or a different
                    Configuration Manager site. Configuration data is converted to DCM Digest.

                    For information about how to import configuration data, see Import
                    configuration data.

<!-- p.70 -->

 Management          Details
 task

 Copy                Creates a copy of the selected configuration baseline with a name that you
                     specify. The new configuration baseline does not retain any relationship to
                     the original configuration baseline.

 Delete              Opens the Delete Configuration Baseline dialog box where you can review
                     any references to this configuration baseline.

                     You must remove all references to a configuration baseline before you can
                     delete the configuration baseline.

 Deploy              Opens the Deploy Configuration Baseline dialog box where you can deploy
                     one or more configuration baselines to devices in your hierarchy.

                     For details, see Deploy configuration baselines.

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.71 -->

Import configuration data with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

In addition to creating configuration baselines and configuration items in the
Configuration Manager console, you can import configuration data if it's contained in a
cabinet (.cab) file format and adheres to the supported Service Modeling Language
(SML) schema. You can import configuration data from:

      Best practice configuration data (Configuration Packs) that has been downloaded
      from Microsoft or from other software vendor sites.

      Configuration data that has been exported from System Center 2012 Configuration
      Manager and later.

      Configuration data that was externally authored and that conforms to the SML
      schema.

When you import a configuration baseline, some or all of the configuration items that
are referenced in the configuration baseline might also be included in the cabinet file.
During the import process, Configuration Manager verifies that all of the configuration
items that are referenced in the configuration baseline are either also included in the
cabinet file or already exist in the Configuration Manager site. The import process fails if
you attempt to import a configuration baseline that references configuration data that
Configuration Manager can't locate.

Other scenarios where the import process might fail include the following:

      The configuration data references configuration data that Configuration Manager
      can't locate, either in its database or in the cabinet file itself.

      The configuration data is already present in the Configuration Manager database
      with the same name and configuration data version, but the content version
      differs.

      The configuration data is already present in the Configuration Manager database
      with the same content version, but the hash calculation identifies it as being
      different.

      A newer version of the configuration data with same name is already present or
      has recently been deleted in the Configuration Manager database.

<!-- p.72 -->

     In a multi-site Configuration Manager hierarchy, the configuration data was
     originally imported from a parent site. You must update it from the same site and
     not a child site.

Import configuration data
   1. In the Configuration Manager console, click Assets and Compliance >
     Configuration Items or Configuration Baselines
   2. In the Home tab, in the Create group, click Import Configuration Data.
   3. On the Select Files page of the Import Configuration Data Wizard, click Add, and
     then in the Open dialog box, select the .cab files you want to import.
   4. Select the Create a new copy of the imported configuration baselines and
     configuration items check box if you want the imported configuration data to be
     editable in the Configuration Manager console.
   5. On the Summary page, review the actions that will be taken, and then complete
     the wizard.

The imported configuration data displays in the Compliance Settings node of the
Assets and Compliance workspace.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.73 -->

Create user data and profiles
configuration items in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

User data and profiles configuration items in Configuration Manager contain settings
that can manage folder redirection, offline files, and roaming profiles on computers that
run Windows 8 and later for users in your hierarchy. For example, you can:

      Redirect a user's Documents folder to a network share.

      Ensure that specified files stored on the network are available on a user's computer
      when the network connection is unavailable.

      Configure which files in a user's roaming profile are synchronized with a network
      share when the user logs on and off.

Unlike other configuration items in Configuration Manager, you don't add user data and
profile configuration items to a configuration baseline, which you then deploy. Instead,
you deploy the configuration item directly by using the Deploy User Data and Profiles
Configuration Item dialog box.

You can only deploy user data and profiles configuration items to user collections.

  ） Important

  If you deploy this policy, it restricts folder redirection group policy on the same
  devices. For more information, see Folder Redirection group policy is not applied
  in Windows 8, Windows 8.1, or Windows 10 and later.

Enable user data and profiles for compliance
settings
Use the following procedure to configure the default client setting for user data and
profiles compliance settings, which will apply to all computers in your hierarchy. If you
want this setting to apply to only some computers, create a custom device client setting
and assign it to a collection that contains the computers for which you want to use user

<!-- p.74 -->

data and profiles compliance settings. For more information about how to create
custom device settings, see How to configure client settings.

   1. In the Configuration Manager console, go to Administration > Client Settings >
     Default Settings.

   2. On the Home tab of the ribbon, in the Properties group, select Properties.

   3. In the Default Settings dialog box, select Compliance Settings.

   4. From the Enable User Data and Profiles drop-down list, select Yes.

   5. Select OK to close the Default Settings dialog box.

Create a user data and profiles configuration
item
   1. In the Configuration Manager console, go to Assets and Compliance >
     Compliance Settings > User Data and Profiles.

   2. On the Home tab, in the Create group, select Create User Data and Profiles
     Configuration Item.

   3. On the General page of the Create User Data and Profiles Configuration Item
     Wizard, specify the following information:

          Name: Enter a unique name for the configuration item. You can use a
          maximum of 256 characters.

          Description: Provide a description that gives an overview of the configuration
          item and other relevant information that helps to identify it in the
          Configuration Manager console. You can use a maximum of 256 characters.

          Folder redirection: Configure settings for folder redirection for this
          configuration item.

          Offline files: Configure settings for offline files for this configuration item.

          Roaming user profiles: Configure settings for roaming user profiles for this
          configuration item.

   4. On the Folder Redirection page of the Create User Data and Profiles
     Configuration Item Wizard, specify how you want the client computers of users
     that receive this configuration item to manage folder redirection. You can

<!-- p.75 -->

     configure settings for any device the user signs into or for only the user's primary
     devices.

       ７ Note

       This page only appears if you checked Folder redirection on the General
       page of the wizard.

  5. On the Offline Files page of the Create User Data and Profiles Configuration Item
     Wizard, you can enable or disable the use of offline files for users that receive this
     configuration item and configure settings for the behavior of the offline files. You
     can also specify offline files that will always be available on any computer that the
     user signs into.

       ７ Note

       This page only appears if you checked the box Offline files on the General
       page of the wizard.

  6. On the Roaming Profiles page of the Create User Data and Profiles Configuration
     Item Wizard, you can configure whether roaming profiles are available on
     computers that the user signs into and also configure further information about
     how these profiles behave.

       ７ Note

       This page only appears if you checked the box Roaming user profiles on the
       General page of the wizard.

  7. Complete the wizard.

The new configuration item is shown in the User Data and Profiles node of the Assets
and Compliance workspace.

Deploy a user data and profiles configuration
item
  1. In the Configuration Manager console, go to Assets and Compliance >
     Compliance Settings > User Data and Profiles.

<!-- p.76 -->

   2. Select the user data and profiles configuration item you want to deploy and then,
     in the Home tab, in the Deployment group, select Deploy.

   3. In the Deploy User Data and Profiles Configuration Item dialog box, specify the
     following information:

          Collection: Select Browse to select the user collection where you want to
          deploy the configuration item.

             ） Important

             You can only deploy user data and profiles configuration items to user
             collections.

          Remediate noncompliant rules when supported: Enable this option to
          automatically remediate any rules that are evaluated as noncompliant on
          client computers.

          Allow remediation outside the maintenance window: If you configured a
          maintenance window for the collection to which you're deploying the
          configuration item, enable this option. It lets compliance settings remediate
          the value outside of the maintenance window. For more information about
          maintenance windows, see How to use maintenance windows.

          Generate an alert: Enable this option to configure an alert that the site
          generates if the configuration item compliance is less than a specified
          percentage by a specified date and time. You can also specify whether you
          want an alert to be sent to System Center Operations Manager.

          Specify the compliance evaluation schedule for this configuration item:
          Specify the schedule by which clients evaluate the deployed configuration
          item. This schedule can be either a simple or a custom schedule.

   4. Select OK to close the Deploy User Data and Profiles Configuration Item dialog
     box and to create the deployment.

Next steps
Monitor this type of configuration item in the same way that you monitor other
compliance settings.

For more information, see How to monitor compliance settings.

<!-- p.77 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.78 -->

OneDrive for Business Profiles
Article • 10/04/2022

Starting in Configuration Manager version 1902, you can create OneDrive for Business
Profiles for moving Windows known folders to OneDrive for Business. These folders
include Desktop, Documents, and Pictures. In each profile, you can specify settings for
moving the Windows known folders. For more information on OneDrive for Business,
see Redirect and move Windows known folders to OneDrive.

Prerequisites
      Find your Microsoft 365 tenant ID

      Deploy the OneDrive sync client version 18.111.0603.0004 or later. For more
      information, see Deploy OneDrive apps by using Configuration Manager.

Move Windows known folders to OneDrive
Use Configuration Manager to move Windows known folders to OneDrive for Business.
These folders include Desktop, Documents, and Pictures. To simplify your Windows
upgrades, deploy these settings to Windows 7 clients before deploying a task sequence.

   1. In the Configuration Manager console, go to the Assets and Compliance
      workspace, expand Compliance Settings, and select the OneDrive for Business
      Profiles node.

<!-- p.79 -->

2. In the ribbon, select Create OneDrive for Business Profile.

3. Specify a name to identify this policy, and select Next.

4. Select the platforms that will be provisioned with the OneDrive for Business profile.
  When you're finished selecting the platforms, click Next.

<!-- p.80 -->

5. On the Settings page:

  a. Specify your Microsoft 365 tenant ID.

  b. Select one of the following options to move the known folders to OneDrive:

          Prompt users to move Windows known folders to OneDrive: With this
          option, the user sees a wizard to move their files. If they choose to
          postpone or decline moving their folders, OneDrive periodically reminds
          them.

          Silently move Windows known folders to OneDrive: When this policy
          applies to the device, the OneDrive client automatically redirects the
          known folders to OneDrive for Business.
             Show notification to users after folders have been redirected: If you
             enable this option, the OneDrive client notifies the user after it moves
             their folders.

  c. Prevent users from redirecting their Windows known folders back to their PC:
     Disables the option in OneDrive for Business on the client for users to move
     these folders back to the device.
