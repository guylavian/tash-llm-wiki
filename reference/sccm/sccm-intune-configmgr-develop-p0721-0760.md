---
title: "Configuration Manager SDK documentation — pages 721-760"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0721-0760
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0721-0760
family: sccm
documentKind: "doc"
abstract: ".NET Framework Security For more information about securing Configuration Manager applications, see Configuration Manager role-based administration. See Also About Configuration Baselines and Configuration Items Objects overview How to Connect to a Configuration Manager Provider"
---

# Configuration Manager SDK documentation — pages 721-760

<!-- p.721 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About Configuration Baselines and Configuration Items
Objects overview How to Connect to a Configuration Manager Provider using Managed
Code
How to Connect to a Configuration Manager Provider Using WMI
SMS_BaselineAssignment Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.722 -->

How to List Configuration Assignments
Article • 10/04/2022

The following code examples show how to list the current configuration baseline
assignments and a specific set of properties for each assignment in Configuration
Manager.

To list Configuration Assignments
   1. Set up a connection to the SMS Provider.

   2. Query for all instances SMS_BaselineAssignment .

   3. Loop through the array of available configuration baseline assignments, listing
        each configuration baseline assignment and specific properties.

Example
The following example method shows how to list the current configuration baseline
assignments and a specific set of properties for each assignment in Configuration
Manager.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub DCMAssignments_ListProperties(swbemServices)

         On Error Resume Next

         Dim queryBaselineAssignmentResults
         Dim assignment

      ' Query assignments.
      Set queryBaselineAssignmentResults = swbemServices.ExecQuery("Select *
  From SMS_BaselineAssignment", , 0)

         If Err.Number<>0 Then
             Wscript.Echo "Couldn't get assignments."
             Exit Sub
         End If

         On Error Goto 0

<!-- p.723 -->

    ' List assignments and various assignment's properties.
    For Each assignment In queryBaselineAssignmentResults
        Wscript.Echo ""
        Wscript.Echo "Listing Assignment Properties for Assignment ID: " &
assignment.AssignmentID
        Wscript.Echo "Listing Assignment Properties for Assignment
Description: " & assignment.AssignmentDescription
        Wscript.Echo "------------------------------------------------------
-------------------------"
        Wscript.Echo "ApplyToSubTargets: " & assignment.ApplyToSubTargets
        Wscript.Echo "AssignmentAction: " & assignment.AssignmentAction
        Wscript.Echo "AssignmentID: " & assignment.AssignmentID
        Wscript.Echo "AssignmentName: " & assignment.AssignmentName
        Wscript.Echo "AssignmentDescription: " &
assignment.AssignmentDescription
        Wscript.Echo "AssignmentUniqueID: " & assignment.AssignmentUniqueID
        Wscript.Echo "Collection: " & assignment.TargetCollectionID
        Wscript.Echo "CreationTime: " & assignment.CreationTime
        Wscript.Echo "DesiredConfigType: " & assignment.DesiredConfigType
        Wscript.Echo "DPLocality: " & assignment.DPLocality
        Wscript.Echo "EvaluationSchedule: " & assignment.EvaluationSchedule
        Wscript.Echo "LogComplianceToWinEvent: " &
assignment.LogComplianceToWinEvent
        Wscript.Echo "NotifyUser: " & assignment.NotifyUser
        Wscript.Echo "SendDetailedNonComplianceStatus: " &
assignment.SendDetailedNonComplianceStatus
        Wscript.Echo "SourceSite: " & assignment.SourceSite
        Wscript.Echo "StartTime: " & assignment.StartTime
        Wscript.Echo "SuppressReboot: " & assignment.SuppressReboot
        Wscript.Echo "UseGMTTimes: " & assignment.UseGMTTimes
        Wscript.Echo
"===========================================================================
===="
    Next

     If queryBaselineAssignmentResults.Count = 0 Then
         Wscript.Echo "      no query results"
     End If

     set queryBaselineAssignmentResults = Nothing

End Sub

c#

public void DCMAssignments_ListProperties(WqlConnectionManager connection)
{

    IResultObject baselineAssignments =
connection.QueryProcessor.ExecuteQuery("SELECT * FROM
SMS_BaselineAssignment");

<!-- p.724 -->

    try
    {
        foreach (IResultObject assignment in baselineAssignments)
        {
            Console.WriteLine("Listing Assignment Properties for Assignment
ID: " + assignment["AssignmentID"].StringValue);
            Console.WriteLine("Listing Assignment Properties for Assignment
Description: " + assignment["AssignmentDescription"].StringValue);
            Console.WriteLine("---------------------------------------------
-----------------------------------");
            Console.WriteLine("ApplyToSubTargets: " +
assignment["ApplyToSubTargets"].BooleanValue);
            Console.WriteLine("AssignmentAction: " +
assignment["AssignmentAction"].IntegerValue);
            Console.WriteLine("AssignmentID: " +
assignment["AssignmentID"].StringValue);
            Console.WriteLine("AssignmentName: " +
assignment["AssignmentName"].StringValue);
            Console.WriteLine("AssignmentDescription: " +
assignment["AssignmentDescription"].StringValue);
            Console.WriteLine("AssignmentUniqueID: " +
assignment["AssignmentUniqueID"].StringValue);
            Console.WriteLine("Collection: " +
assignment["TargetCollectionID"].StringValue);
            Console.WriteLine("CreationTime: " +
assignment["CreationTime"].StringValue);
            Console.WriteLine("DesiredConfigType: " +
assignment["DesiredConfigType"].StringValue);
            Console.WriteLine("DPLocality: " +
assignment["DPLocality"].IntegerValue);
            Console.WriteLine("EvaluationSchedule: " +
assignment["EvaluationSchedule"].StringValue);
            Console.WriteLine("LogComplianceToWinEvent: " +
assignment["LogComplianceToWinEvent"].BooleanValue);
            Console.WriteLine("NotifyUser: " +
assignment["NotifyUser"].BooleanValue);
            Console.WriteLine("SendDetailedNonComplianceStatus: " +
assignment["SendDetailedNonComplianceStatus"].BooleanValue);
            Console.WriteLine("SourceSite: " +
assignment["SourceSite"].StringValue);
            Console.WriteLine("StartTime: " +
assignment["StartTime"].StringValue);
            Console.WriteLine("SuppressReboot: " +
assignment["SuppressReboot"].IntegerValue);
            Console.WriteLine("UseGMTTimes: " +
assignment["UseGMTTimes"].BooleanValue);

            // Process the array.
            int[] arrayofAssignedCIs =
assignment["AssignedCIs"].IntegerArrayValue;
            Console.Write("Assigned baseline ID(s): ");
            foreach (int i in arrayofAssignedCIs)
            {
                Console.Write(i + " ");

<!-- p.725 -->

                   }

                   Console.WriteLine();

              // NULL BY DEFAULT (on a generic assignment created through the
  user interface).
              //
              //Console.WriteLine("EnforcementDeadline: " +
  assignment["EnforcementDeadline"].StringValue);
              //Console.WriteLine("ExpirationTime: " +
  assignment["ExpirationTime"].StringValue);
              //Console.WriteLine("NonComplianceCriticality: " +
  assignment["NonComplianceCriticality"].IntegerValue);
              //Console.WriteLine("OverrideServiceWindows: " +
  assignment["OverrideServiceWindows"].BooleanValue);
              //Console.WriteLine("RebootOutsideOfServiceWindows: " +
  assignment["RebootOutsideOfServiceWindows"].BooleanValue);
              //Console.WriteLine("WoLEnabled: " +
  assignment["WoLEnabled"].BooleanValue);

  Console.WriteLine("=========================================================
  =======================");

             }

      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to list assignment properties. Error: " +
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                               ﾉ   Expand table

 Parameter             Type                              Description

 - connection          - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
 - swbemServices       - VBScript: SWbemServices

Compiling the Code

Namespaces

<!-- p.726 -->

System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About Configuration Baselines and Configuration Items
Objects overview How to Connect to a Configuration Manager Provider using Managed
Code
How to Connect to a Configuration Manager Provider Using WMI
SMS_BaselineAssignment Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.727 -->

About Compliance Settings (DCM)
Extensibility
Article • 01/12/2024

The content in this section provides information about extending the functionality of
desired configuration management configuration items in Configuration Manager.

In application configuration items, it's possible to detect applications or settings by
using a script.

If the script returns a non-zero exit code, the result is a discovery failure.

If the script returns a zero exit code, the script output is evaluated.

It's the echoed output of a script that is detected and evaluated. For example:

      No echoed output equals no instances detected.

      "n" lines of output equals "n" instances detected.

      In there's an application detection, two lines of output would indicate that two
      instances of the application are detected.

      If there's a settings detection, no lines of output would indicate that no instances
      of the setting are detected.

      In all cases, the evaluation of the script output is determined by the rule.

  ７ Note

  In the case of settings detection, the script output is cast to the type of setting
  being detected. If the cast of the script output fails, a discovery failure is returned.
  For example, a script that reads and returns registry values, passes a set of values
  back to the rule; however, one value is a string (1, 2, x). If the rule is expecting only
  integer values back, it will cast all of the values to integers, causing a failure. In this
  case, the rule returns an evaluation failure.

Feedback
Was this page helpful?

<!-- p.728 -->

                            Yes    No

Provide product feedback

<!-- p.729 -->

About authoring configuration baselines
and configuration items
Article • 10/04/2022

Configuration Manager supports the authoring of configuration data, which consists of
configuration baselines and configuration items. Configuration Manager presents this
configuration data in a user-friendly format called DCM Digest. This format is a
specialized XML document that Configuration Manager uses. You can author
configuration data by using the Configuration Manager console, or by directly authoring
a DCM Digest XML file.

When you create configuration data with the Configuration Manager console, you can
export it into a .cab file. When configuration data is imported into Configuration
Manager, the format is DCM Digest XML only.

Authoring configuration data
Create configuration data in the following ways:

      You can create configuration data externally with an XML editor. If you then
      package it as a .cab file, you can import it into Configuration Manager.

      You can create configuration data within Configuration Manager by using the
      following wizards:

         Create Application Configuration Item Wizard

         Create Operating System Configuration Item Wizard

         Create Configuration Baseline

  ） Important

  You create and manage software update configuration items through the software
  updates management feature in Configuration Manager. You can reference these
  configuration items by configuration baselines. However, don't directly author them
  by using configuration items or the DCM Digest.

You can also import configuration data that software vendors and solution providers
have published.

<!-- p.730 -->

  ７ Note

  You can digitally sign published configuration data. Then you can verify the
  publishing source and be sure that no one has tampered with the data. If the digital
  signature verification check fails, Configuration Manager warns you to continue
  with the import. Only import configuration data from external sources if it has a
  valid digital signature from a trusted publisher.

After the site imports the configuration data, you can then work with it in the
Configuration Manager console.

Next steps
About authoring configuration baselines and items

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.731 -->

About Configuration Baselines
Article • 10/04/2022

In Configuration Manager, baselines are used to define the configuration of a product or
a system that is established at a specific point in time, capturing both structure and
details. Configuration baselines in Configuration Manager contain a defined set of
desired configurations that are evaluated for compliance as a group.

Configuration baselines contain one or more configuration items with associated rules,
and they are assigned to computers through collections, together with a compliance
evaluation schedule.

  ７ Note

  Although you can assign configuration baselines to a collection that contains users,
  the configuration baselines will be evaluated only by computers in the collection,
  and not by users in the collection.

You can create your own configuration baselines with the Configuration Manager
console, and you can import configuration baselines from the following sources:

      A Best Practices configuration baseline from Microsoft or other vendors

      Custom authored configuration baselines from within your own organization, but
      external to Configuration Manager

      Another Configuration Manager site

      When configuration baselines are imported, unless they were originally created in
      the same Configuration Manager site, you will not be able to directly modify them
      in the Configuration Manager console. If you need to refine the configuration
      items to meet your business requirements, the recommended path is:

   1. Create child configuration items with your custom values.

   2. Duplicate the configuration baseline.

   3. Edit the duplicated baseline, and replace the configuration items with your edited
      child configuration items.

Configuration Baseline Rules

<!-- p.732 -->

Configuration baselines rules are used to specify how the configuration items that are
included in the configuration baseline are to be assessed for compliance on client
computers. There are fixed types of configuration baseline rules that cannot be changed
in Configuration Manager. Configuration items can be added to the following
configuration baseline rules:

     One of the following operating system configuration items must be present and
     properly configured.

     These applications and general configuration items are required and must be
     properly configured.

     If these optional application configuration items are detected, they must be
     properly configured.

     These software updates must be present.

     These application configuration items must not be present.

     These configuration baselines must also be validated.

RequiredItems
     These applications and general configuration items are required and must be
     properly configured.

ProhibitedItems
     These application configuration items must not be present.

OptionalItems
     If these optional application configuration items are detected, they must be
     properly configured.

OperatingSystems
     One of the following operating system configuration items must be present and
     properly configured.

SoftwareUpdates

<!-- p.733 -->

     These software updates must be present.

Baselines
     These configuration baselines must also be validated.

OtherConfigurationItems
     References to content defined as raw Service Modeling Language (SML).

See Also
About authoring configuration baselines and items

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.734 -->

Configuration Baseline Example 1
Article • 10/04/2022

The following Baseline Configuration Item Instance example references an application
configuration item that checks whether the Configuration Manager client and
Notepad.exe are installed on systems that are running Windows XP SP2.

Configuration Baseline Example
  XML

  <?xml version="1.0" encoding="utf-8"?>

  <!--
  The root element for any DCM Digest document is the
  DesiredConfigurationDigest element referenced below. All of the XML
  elements/attributes are defined in the DCM Digest schema definition
  namespace.
  -->

  <DesiredConfigurationDigest
  xmlns="http://schemas.microsoft.com/SystemsCenterConfigurationManager/2006/0
  3/24/DesiredConfiguration">

  <!--
  Every digest must contain exactly one configuration item. Specifically one
  of the following: an application, operatingsystem, general or baseline.
  This is a baseline configuration item.
  The baseline configuration item provides a way to group other configuration
  items (including other baselines) for deployment to clients. Other types of
  configuration items cannot be directly deployed to clients, they must be
  referenced within a baseline configuration item, which is then deployed to
  clients.

  The unique identify of the configuration item is the combination of the
  attributes AuthoringScopeID, LogicalName and Version.
  Each attribute is part of the unique identity of the configuration item; the
  actual identity is AuthoringScopeID + LogicalName + Version.

  AuthoringScopeID (string) - This attribute corresponds to the author's
  namespace or identity.
  LogicalName (string) - This attribute identifies the configuration item
  within the authoring scope.
  Version (string) - This attribute specifies the version of the configuration
  item.
  -->

      <Baseline AuthoringScopeId="ScopeId_F348CC96-19CA-4F5D-9D4F-
  D1451B5BEB1E" LogicalName="Baseline_ab095740-707a-46b6-8408-a72be147514c"

<!-- p.735 -->

Version="1">
        <Annotation>
            <DisplayName Text="Sample Baseline" />
            <Description Text="A baseline that includes the sample CI." />
        </Annotation>

<!--
Only application and general configuration item references can be used in
the RequiredItems section.

Below is a reference to an application configuration item that checks to see
whether the Configuration Manager 2007 client is installed on the system.
The application configuration item can be found in the Application
Configuration Item Schema Example 1 (link below)
-->

        <RequiredItems>
            <ApplicationReference AuthoringScopeId="ScopeId_F348CC96-19CA-
4F5D-9D4F-D1451B5BEB1E" LogicalName="Application_5cb68ff1-a234-41ed-a7d4-
14174d8108b7" Version="1" />
        </RequiredItems>

<!--
Only application configuration item references can appear in
ProhibitedItems.
-->

       <ProhibitedItems>
       </ProhibitedItems>

<!--
Only application configuration items can appear in OptionalItems.

Below is a reference to an application configuration item that checks to see
whether Notepad.exe is installed on the system. The application
configuration item can be found in the Application Configuration Item Schema
Example 2 (link below)
-->

        <OptionalItems>
            <ApplicationReference AuthoringScopeId="ScopeId_F348CC96-19CA-
4F5D-9D4F-D1451B5BEB1E" LogicalName="Application_171bae6f-5661-4bb8-a703-
270b131e4c4c" Version="1" />
        </OptionalItems>

<!--
Only operating system configuration items can appear in OperatingSystems.
At least one of the operating systems in the referenced OperationSystem
configuration items must be detected on the targeted computer.

Below is a reference to an operating system configuration item that checks
to see whether Windows XP SP2 is installed on the system. The application
configuration item can be found in the Operating System Configuration Item
Schema Example 1 (link below)
-->

<!-- p.736 -->

          <OperatingSystems>
              <OperatingSystemReference AuthoringScopeId="ScopeId_F348CC96-
  19CA-4F5D-9D4F-D1451B5BEB1E" LogicalName="OperatingSystem_8aa19644-7801-
  411c-a7fa-8e7a33d0d8fe" Version="3" />
          </OperatingSystems>

  <!--
  Only SoftwareUpdates and SoftwareUpdateBundles can appear in
  SoftwareUpdates. Software Updates configuration items are created and
  administered through the Software Updates Management feature in
  Configuration Manager. The Software Updates configuration items can be
  referenced in configuration baselines; however, they should not be directly
  authored via DCM or the DCM Digest.
   -->

            <SoftwareUpdates>
            </SoftwareUpdates>

  <!-- Only baseline configuration item references can appear in Baselines.
  References to other baselines. -->
          <Baselines>
          </Baselines>

  <!--
  Only references to content defined as System Definition Model language (SDM)
  can appear in OtherConfigurationItems.
  -->

            <OtherConfigurationItems>
            </OtherConfigurationItems>

      </Baseline>
  </DesiredConfigurationDigest>

See Also
About authoring configuration baselines and items

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.737 -->

About Application Configuration Items
Article • 10/04/2022

Application configuration items include all the functionality of general configuration
items, but their identity can be detected independently of its settings and objects.
Desired Configuration Management in Configuration Manager supports two methods
for detecting the presence of an application configuration item: (1) Windows Installer
package and (2) Script-based discovery. Configuration item (level) discoverability allows
application configuration items to be referenced as prohibited or optional within the
context of a configuration baseline.

Examples of application configuration items might include:

      Microsoft Office Professional 2003

      Microsoft Word

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.738 -->

Application Configuration Item Example
1
Article • 10/04/2022

The following Application Configuration Item Instance example determines whether the
Configuration Manager client is installed on the system by using Microsoft Windows
Installer-based detection.

Application Configuration Item Example
  XML

  <?xml version="1.0" encoding="utf-8"?>

  <!--
  The root element for any DCM Digest document is the
  DesiredConfigurationDigest element referenced below. All of the XML
  elements/attributes are defined in the DCM Digest schema definition
  namespace.
  -->

  <DesiredConfigurationDigest
  xmlns="http://schemas.microsoft.com/SystemsCenterConfigurationManager/2006/0
  3/24/DesiredConfiguration">

  <!--
  Every DCM Digest must contain exactly one configuration item. Specifically
  one of the following: an application, operatingsystem, general or baseline.
  This digest defines an application configuration item.

  The unique identity of the configuration item is the combination of the
  attributes AuthoringScopeID, LogicalName and Version.
  Each attribute is part of the unique identity of the configuration item; the
  actual identity is AuthoringScopeID + LogicalName + Version.

  AuthoringScopeID (string) - This attribute corresponds to the author's
  namespace or identity.
  LogicalName (string) - This attribute identifies the configuration item
  within the authoring scope.
  Version (string) - This attribute specifies the version of the configuration
  item.
  -->

      <Application AuthoringScopeId="ScopeId_F348CC96-19CA-4F5D-9D4F-
  D1451B5BEB1E" LogicalName="Application_5cb68ff1-a234-41ed-a7d4-14174d8108b7"
  Version="1" Is64Bit="false">
          <Annotation>
              <DisplayName Text="Configuration Manager Client" />

<!-- p.739 -->

            <Description Text="Configuration Manager Client (Windows
Installer-based detection)" />
        </Annotation>

<!--
There are no parts defined for this configuration item.
Parts are physical things with fixed lists of properties.Mandatory element
tag for the section of the DCM Digest used to define Object parts,
including:
File
Folder
Assembly (registered in the Global Assembly Cache (GAC))
RegistryKey
-->

       <Parts>
           <ParentReferences />
       </Parts>

<!--
There are no settings defined for this configuration item.
Settings are configurable name/value pairs which influence the behavior of
hardware and software. DCM can discover settings using any of the supported
providers, including:
Registry
WMI (WQL query)
Microsoft SQL Server (SQL query)
Active Directory (LDAP)
XML (XPath query)
IIS Metabase
Script (JScript/VBScript/PowerShell)
-->

       <Settings>

<!--
RootComplexSetting is the root container for all settings. Every
configuration item has one of these, even if there are no actual settings
defined.
-->
            <RootComplexSetting />

       </Settings>

<!--
This application is discovered via Windows Installer-based discovery. If it
does exist (is discovered) the system then discovers the parts and settings.
Finally, the system evaluates the rules (if any) defined against the part
property values and the setting values.
-->

        <MsiDiscoveryInfo IsPerUser="false" ProductCode="{D7D7EE27-817F-
481D-865F-F5755FA89E2E}" Version="4.00.5507.0000" />

<!-- p.740 -->

      </Application>
  </DesiredConfigurationDigest>

See Also
About authoring configuration baselines and items

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.741 -->

Application Configuration Item Example
2
Article • 10/04/2022

In Configuration Manager, the following Application Configuration Item Instance
example determines whether Notepad.exe is installed.

Application Configuration Item Example
  XML

  <?xml version="1.0" encoding="utf-8"?>

  <!--
  The root element for any DCM Digest document is the
  DesiredConfigurationDigest element referenced below. All of the XML
  elements/attributes are defined in the DCM Digest schema definition
  namespace.
  -->

  <DesiredConfigurationDigest
  xmlns="http://schemas.microsoft.com/SystemsCenterConfigurationManager/2006/0
  3/24/DesiredConfiguration">

  <!--
  Every DCM Digest must contain exactly one configuration item. Specifically
  one of the following: an application, operatingsystem, general or baseline.
  This digest defines an application configuration item.

  The unique identify of the configuration item is the combination of the
  attributes AuthoringScopeID, LogicalName and Version.
  Each attribute is part of the unique identity of the configuration item; the
  actual identity is AuthoringScopeID + LogicalName + Version.

  AuthoringScopeID (string) - This attribute corresponds to the author's
  namespace or identity.
  LogicalName (string) - This attribute identifies the configuration item
  within the authoring scope.
  Version (string) - This attribute specifies the version of the configuration
  item.
  -->

      <Application AuthoringScopeId="ScopeId_F348CC96-19CA-4F5D-9D4F-
  D1451B5BEB1E" LogicalName="Application_171bae6f-5661-4bb8-a703-270b131e4c4c"
  Version="1" Is64Bit="false">
          <Annotation>
              <DisplayName Text="Notepad" />
              <Description Text="Detects Notepad.exe via script-based

<!-- p.742 -->

discovery" />
        </Annotation>

<!--
There are no parts defined for this configuration item.
Parts are physical things with fixed lists of properties.Mandatory element
tag for the section of the DCM Digest used to define Object parts,
including:
File
Folder
Assembly (registered in the Global Assembly Cache (GAC))
RegistryKey
-->

       <Parts>
           <ParentReferences />
       </Parts>

<!--
There are no settings defined for this configuration item.
Settings are configurable name/value pairs which influence the behavior of
hardware and software. DCM can discover settings using any of the supported
providers, including:
Registry
WMI (WQL query)
Microsoft SQL Server (SQL query)
Active Directory (LDAP)
XML (XPath query)
IIS Metabase
Script (JScript/VBScript/PowerShell)
-->

       <Settings>

<!--
RootComplexSetting is the root container for all settings. Every
configuration item has one of these, even if there are no actual settings
defined.
-->
            <RootComplexSetting />

       </Settings>

<!--
This application is discovered via script-based discovery. If it does exist
(is discovered) the system then discovers the parts and settings. Finally,
the system evaluates the rules (if any) defined against the part property
values and the setting values.
-->

<!--
IMPORTANT: Insert a script here - not just the name of the script, but the
actual script code. Returning a value from the script indicates that the
application exists, not returning a value indicates that the application was
not found.

<!-- p.743 -->

  -->
          <ScriptDiscoveryInfo ScriptType="VBScript">
              <Script>
                       Dim filesys
                       Set filesys =
  CreateObject("Scripting.FileSystemObject")
                       If filesys.FileExists("c:\notepad.exe") Then
                       wscript.echo("Notepad.exe Exists")
                       Else
                      ' Returning nothing, as the application does not exist.
                       End If
              </Script>
          </ScriptDiscoveryInfo>
      </Application>
  </DesiredConfigurationDigest>

See Also
About authoring configuration baselines and items

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.744 -->

About Operating System Configuration
Item Examples
Article • 10/04/2022

In Configuration Manager, operating system configuration items include all of the
functionality of general configuration items, but they're tightly coupled with a specific
version of the Windows operating system.

See Also
About authoring configuration baselines and items

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.745 -->

Operating System Configuration Item
Example 1
Article • 10/04/2022

In Configuration Manager, the following Operating System Configuration Item Schema
example checks for Windows XP SP2.

Operating System Configuration Item Example
  XML

  <?xml version="1.0" encoding="utf-8"?>

  <!--
  The root element for any DCM Digest document is the
  DesiredConfigurationDigest element referenced below. All of the XML
  elements/attributes are defined in the DCM Digest schema definition
  namespace.
  -->

  <DesiredConfigurationDigest
  xmlns="http://schemas.microsoft.com/SystemsCenterConfigurationManager/2006/0
  3/24/DesiredConfiguration">

  <!--
  Every DCM Digest must contain exactly one configuration item. Specifically
  one of the following: an application, operatingsystem, general or baseline.
  This digest defines an operating system configuration item.

  The unique identify of the configuration item is the combination of the
  attributes AuthoringScopeID, LogicalName and Version.
  Each attribute is part of the unique identity of the configuration item; the
  actual identity is AuthoringScopeID + LogicalName + Version.

  AuthoringScopeID (string) - This attribute corresponds to the author's
  namespace or identity.
  LogicalName (string) - This attribute identifies the configuration item
  within the authoring scope.
  Version (string) - This attribute specifies the version of the configuration
  item.
  -->

      <OperatingSystem AuthoringScopeId="ScopeId_F348CC96-19CA-4F5D-9D4F-
  D1451B5BEB1E" LogicalName="OperatingSystem_c745714d-1063-4dec-8447-
  a9414ec030e7" Version="1">
          <Annotation>
              <DisplayName Text="My WinXp SP2 Operating System CI" />
              <Description Text="Simple Operating System detection." />

<!-- p.746 -->

       </Annotation>

<!--
There are no parts defined for this configuration item.
Parts are physical things with fixed lists of properties.Mandatory element
tag for the section of the DCM Digest used to define Object parts,
including:
File
Folder
Assembly (registered in the Global Assembly Cache (GAC))
RegistryKey
-->

       <Parts>
           <ParentReferences />
       </Parts>

<!--
There are no settings defined for this configuration item.
Settings are configurable name/value pairs which influence the behavior of
hardware and software. DCM can discover settings using any of the supported
providers, including:
Registry
WMI (WQL query)
Microsoft SQL Server (SQL query)
Active Directory (LDAP)
XML (XPath query)
IIS Metabase
Script (JScript/VBScript/PowerShell)
-->

       <Settings>

<!--
RootComplexSetting is the root container for all settings. Every
configuration item has one of these, even if there are no actual settings
defined.
-->
            <RootComplexSetting />

       </Settings>

<!--
OperatingSystem identifies how to determine whether or not this operating
system exists on the system. If it does exist (is discovered), then the
system discovers the parts and settings. Finally, the system evaluates the
rules(if any) defined against the part property values and the setting
values.
-->
         <OperatingSystemDiscoveryInfo BuildVersion="2600" MajorVersion="5"
MinorVersion="10" ServicePackMajorVersion="2" ServicePackMinorVersion="0" />
     </OperatingSystem>
</DesiredConfigurationDigest>

<!-- p.747 -->

See Also
About authoring configuration baselines and items

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.748 -->

About General Configuration Items
Article • 10/04/2022

In Configuration Manager, general configuration items are models of settings and
objects, which together represent a meaningful unit of configuration management
whose identity is defined by enumeration of its settings and objects.

  ７ Note

  General configuration items are referred to as BusinessPolicy configuration items in
  the DCMDigest.xsd

See Also
About authoring configuration baselines and items

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.749 -->

General Configuration Item Example 1
Article • 10/04/2022

The following example is a general configuration item schema example that checks the
registry to see whether, in this case, remote control is enabled in Configuration
Manager.

General Configuration Item Example

  <?xml version="1.0" encoding="utf-8"?>

  <!--
  The root element for any DCM Digest document is the
  DesiredConfigurationDigest element referenced below. All of the XML
  elements/attributes are defined in the DCM Digest schema definition
  namespace.
  -->

  <DesiredConfigurationDigest
  xmlns="http://schemas.microsoft.com/SystemsCenterConfigurationManager/2006/0
  3/24/DesiredConfiguration">

  <!--
  Every DCM Digest must contain exactly one configuration item. Specifically
  one of the following: an application, operatingsystem, general or baseline.
  This digest defines a general configuration item.
  Note: The term general configuration item has replaced business policy
  configuration item in recent desired configuration management documentation.
  The terms refer to the same type of configuration item.

  The unique identify of the configuration item is the combination of the
  attributes AuthoringScopeID, LogicalName and Version.
  Each attribute is part of the unique identity of the configuration item; the
  actual identity is AuthoringScopeID + LogicalName + Version.

  AuthoringScopeID (string) - This attribute corresponds to the author's
  namespace or identity.
  LogicalName (string) - This attribute identifies the configuration item
  within the authoring scope.
  Version (string) - This attribute specifies the version of the configuration
  item.
  -->

      <BusinessPolicy AuthoringScopeId="ScopeId_F348CC96-19CA-4F5D-9D4F-
  D1451B5BEB1E" LogicalName="BusinessPolicy_de5ad8df-1600-4984-91ab-
  7e33e0e7670b" Version="1">

<!-- p.750 -->

        <Annotation>
            <DisplayName Text="Remote Control Is Enabled" />
            <Description Text="This General CI detects whether remote
control is enabled by examining the registry and asserting that the expected
value is set (the expected value being 1)." />
        </Annotation>

<!--
There are no parts defined for this configuration item.
Parts are physical things with fixed lists of properties.Mandatory element
tag for the section of the DCM Digest used to define Object parts,
including:
File
Folder
Assembly (registered in the Global Assembly Cache (GAC))
RegistryKey
-->

       <Parts>
           <ParentReferences />
       </Parts>

<!--
There are no settings defined for this configuration item.
Settings are configurable name/value pairs which influence the behavior of
hardware and software. DCM can discover settings using any of the supported
providers, including:
Registry
WMI (WQL query)
Microsoft SQL Server (SQL query)
Active Directory (LDAP)
XML (XPath query)
IIS Metabase
Script (JScript/VBScript/PowerShell)
-->

       <Settings>

<!--
RootComplexSetting is the root container for all settings. Every
configuration item has one of these, even if there are no actual settings
defined.
-->

            <RootComplexSetting>

<!--
A simple setting.
-->

                <SimpleSetting LogicalName="RegSetting_60d3f52e-5afa-4864-
bbcf-83953c806275" DataType="String">
                    <Annotation>
                        <DisplayName Text="Remote control registry value"
ResourceId="ID-29d49a44-436a-4dbe-bc15-0db78557a4a6" />

<!-- p.751 -->

                        <Description Text="Contains the value obtained from
the remote control registry key." ResourceId="ID-bfe89599-45fc-4413-8a17-
5fea1ced7bea" />
                    </Annotation>

<!--
Optional element. We raise a warning if the source for this setting does not
exist. If so, we include the element and specify the severity of the error.
Otherwise, we do not use the element.
-->

                    <ExistentialRule Severity="Warning" />

<!--
The source of the setting's value. In this case, we're looking for a
particular value from the registry.
-->

                    <RegistryDiscoverySource Hive="HKEY_LOCAL_MACHINE"
Depth="Subtree" Is64Bit="false">

<Key>software\microsoft\sms\client\clientcomponents\remotecontrol</Key>
                        <ValueName>enabled</ValueName>
                    </RegistryDiscoverySource>

<!--
Rules defined against the value of the setting.
-->

                    <Rules>
                        <Rule
xmlns="http://schemas.microsoft.com/SystemsCenterConfigurationManager/2009/0
6/14/Rules" NonCompliantWhenSettingIsNotFound="false" Severity="Warning"
id="Rule_2849425d-0f2b-4d8f-bf63-8113f39c1618">
                            <Annotation>
                                <DisplayName ResourceId="ID-91baba67-94bc-
4b97-b3da-69ab7ba92235" Text="Remote control is enabled."/>
                                <Description ResourceId="ID-87277341-e734-
42ad-87e3-a89e87e9c320" Text="This checks the registry setting
HKEY_LOCAL_MACHINE\software\microsoft\sms\client\clientcomponents\remotecont
rol\enabled registry value to identify whether it is enabled (set to
"1")."/>
                            </Annotation>
                            <Expression> <Operator>Equals</Operator>
                                <Operands>
                                    <SettingReference
SettingSourceType="Registry" SettingLogicalName="RegSetting_1d07d7eb-23f9-
478e-9ed5-ae2fae31d5bf" Version="2" LogicalName="OperatingSystem_9658594e-
a4bc-48a7-bb45-6e07d1308d8a" AuthoringScopeId="ScopeId_6F782309-1BE1-43E8-
A529-177F93D1D8D2" DataType="Int64" Changeable="false" Method="Value"/>
<ConstantValue DataType="Int64" Value="1"/>
                                </Operands>
                            </Expression>
                        </Rule>
                    </Rules>

<!-- p.752 -->

                  </SimpleSetting>
              </RootComplexSetting>
          </Settings>
      </BusinessPolicy>
  </DesiredConfigurationDigest>

See Also
About authoring configuration baselines and items

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.753 -->

About Configuration Manager Console
Extension
Article • 01/05/2024

The Configuration Manager console has an XML-based architecture that can be easily
extended. The Configuration Manager console supports the following extensions:

Actions
An action is a task or command accessed through either a context menu or the ribbon.
Many standard actions are available, and you can extend them to add new functionality,
such as displaying a dialog box or launching an application.

Forms
You can extend the Configuration Manager console with dialog boxes or property
sheets. You can also add new property pages to existing Configuration Manager console
property sheets, such as the properties dialog for an object.

Nodes
You can add new nodes to the Configuration Manager console.

Views
You can create new views that are displayed in the result pane. You can also create new
home pages. For example, you might want to add a new home page that is associated
with a new navigation node that you have created.

Wizards
You can integrate your own custom wizards into the Configuration Manager console by
using a wizard framework of your choice.

Management Classes

<!-- p.754 -->

You can define your own custom classes that can be used by your Configuration
Manager console extension. For more information, see About console management
classes.

Unsupported Features
The Configuration Manager console doesn't support the following features:

Wizard Creation
You can't create wizards by using the existing Configuration Manager console
framework. You also can't modify or remove steps from the existing Configuration
Manager wizards.

Modification of Core Configuration Manager Console
Items
Don't change or remove items in the core Configuration Manager console XML, because
this could break the Configuration Manager console. The core XML is stored in
%ProgramFiles%\Microsoft Endpoint Manager\AdminConsole\XmlStorage\ConsoleRoot.

SMS 2003 IMMF Interfaces
The Configuration Manager console is built by using managed code and doesn't
support the SMS 2003 IMMF interfaces.

Registry-Based Extensions
Registry-based extensions, similar to those available in SMS 2003, aren't supported in
the Configuration Manager console.

Microsoft Management Console SDK Extensions
Extensions written with the Microsoft Management Console SDK aren't supported by
the Configuration Manager console.

Accessibility

<!-- p.755 -->

When developing console extensions, they should be based on designs with accessibility
considerations. For example, you can make use of color, layout, intelligent default
values, sound, and exposing appropriate keyboard focus. By using various accessibility
techniques, you'll make it easier for users with disabilities to use your software. For more
information, see Resources for designing accessible applications.

See Also
Configuration Manager Console Extension Architecture
About Configuration Manager console actions About console forms About console
management classes About console nodes About console views

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.756 -->

Configuration Manager Console
Extension Architecture
Article • 10/04/2022

The Configuration Manager console architecture is built on the following four distinct
layers.

      SMS Provider

      Managed SMS Provider SDK

      User interface framework

      Configuration Manager console XML

SMS Provider in Configuration Manager
The SMS Provider is essentially the same as the SMS 2007 Provider, with the addition of
new classes that support new Configuration Manager features. You can access the SMS
Provider through the usual WBEM interfaces, but for managed code you must use the
managed SMS Provider SDK.

Managed SMS Provider SDK
The managed SMS Provider SDK provides a managed code library that abstracts the
SMS Provider. It provides .NET Framework classes and interfaces that connect to the
SMS Provider, make queries, and otherwise manipulate Configuration Manager objects
and the site control file. You can use the managed SMS Provider SDK in stand-alone
applications, or you can use the user interface framework to extend the existing
Configuration Manager console.

User Interface Framework
The user interface framework lies on top of the managed SMS Provider SDK. The user
interface framework provides functionality for dialog boxes and the Configuration
Manager console, and it provides user interface validation within the Configuration
Manager console. You can extend this user interface framework to add your own forms
to the Configuration Manager console, or you can integrate your own forms within
existing Configuration Manager console forms.

<!-- p.757 -->

Configuration Manager Console XML
The Configuration Manager console XML defines how the Configuration Manager
console looks and behaves. The XML defines nodes, queries, actions, forms, and
everything else that is necessary to render the Configuration Manager console hierarchy,
the results pane, and the action pane.

The XML files that are used by the Configuration Manager console are stored under
%ProgramFiles%\Microsoft Endpoint Manager\AdminConsole\XmlStorage\. The
following table shows the subfolders.

                                                                                  ﾉ   Expand table

 Folder        Description

 ConsoleRoot   This folder contains various XML files that define built in user interface elements
               and classes.

               ManagementClassDescriptions.xml: definitions for the SMS Provider classes.

               ConnectedConsole.xml: definitions for sticky nodes and go-to navigation.

               AssetManagementNode.xml, MonitoringNode.xml, SiteConfigurationNode.xml,
               SoftwareLibraryNode.xml: definitions for each workspace in the Configuration
               Manager console.

 Extensions    Location for XML that is related to the SMS Provider. There are four types of
               extension folders:

               - Actions. XML files for Configuration Manager console actions. For more
               information, see About Configuration Manager console actions.
               - Forms. XML files for form extensions to the Configuration Manager console. For
               more information, see About console forms.
               - Nodes. XML files for node extensions to the Configuration Manager console. For
               more information, see About console nodes.
               - Management Classes. XML files for management class extensions to the
               Configuration Manager console. For more information, see About console
               management classes.

 Other         Various helper XML files.

 Validation    Validation rules for the Configuration Manager console forms.

See Also

<!-- p.758 -->

About Configuration Manager Console Extension
About Configuration Manager console actions About console forms About console
management classes About console nodes About console views

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.759 -->

Configuration Manager console
extension deployment
Article • 10/04/2022

The deployment of a typical Configuration Manager extension has to account for
actions, forms, views, management classes and node extensions.

When you deploy a Configuration Manager extension, you install the files in the
following directories:

                                                                             ﾉ   Expand table

 Extension Type          Directory

 Actions                 %ProgramFiles%\Microsoft Endpoint Manager\AdminConsole\bin for the
                         assembly

                         %ProgramFiles%\Microsoft Endpoint
                         Manager\AdminConsole\XmlStorage\Extensions\Actions for the action
                         XML files

 Forms                   %ProgramFiles%\Microsoft Endpoint Manager\AdminConsole\bin for the
                         assembly

                         %ProgramFiles%\Microsoft Endpoint
                         Manager\AdminConsole\XmlStorage\Extensions\Forms for the form XML
                         files

 Views                   %ProgramFiles%\Microsoft Endpoint
                         Manager\AdminConsole\XmlStorage\bin for the assembly

 Nodes                   %ProgramFiles%\Microsoft Endpoint Manager\AdminConsole\bin for the
                         assembly

                         %ProgramFiles%Microsoft Endpoint
                         Manager\AdminConsole\XmlStorage\Extensions\Nodes for the node XML
                         files

 ManagementClasses       %ProgramFiles%\Microsoft Endpoint Manager\AdminConsole\bin for the
                         assembly

                         %ProgramFiles%Microsoft Endpoint
                         Manager\AdminConsole\XmlStorage\Extensions\ManagementClasses for
                         the management classes XML files

<!-- p.760 -->

  ） Important

  Placing your assemblies and dependencies in the %ProgramFiles%\Microsoft
  Endpoint Manager\AdminConsole\bin folder may create conflicts with other
  console extensions and prevent your extension from loading.

You must also perform the following tasks during installing and uninstalling actions.

Custom Actions

Installing a Custom Action
To install a custom action XML file, copy the file to the %ProgramFiles%\Microsoft
Endpoint Manager\AdminConsole\XmlStorage\Extensions\Actions\<GUID> folder,
where <GUID> is the GUID identifier for the node that the action applies to.

Removing a Custom Action
To remove a custom action, delete the custom action XML file. If there are no other XML
files in the folder then it is safe to remove the folder.

Forms

Installing a Form
You copy the form assembly to either %ProgramFiles%\ Microsoft Endpoint
Manager\AdminConsole\bin or to your application's installation folder.

If you are deploying to a directory other than the %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\bin folder, the form XML< Assembly > attribute, Name , should
include the assembly filename and the full path to the file. For more information, see
How to Create Form XML for a Configuration Manager Property Sheet.

To install an extension property sheet XML file for a form, copy the file to the
%ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\XmlStorage\Extensions\Forms folder. Because all extension
forms are placed in this folder, you must ensure that your XML file has a unique name. It
is suggested that you use your company name as part of the file name.
