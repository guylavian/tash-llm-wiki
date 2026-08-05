---
title: "Configuration Manager SDK documentation — pages 681-720"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0681-0720
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0681-0720
family: sccm
documentKind: "doc"
abstract: "System.ComponentModel Microsoft.ConfigurationManagement.ManagementProvider Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine Assembly adminui.wqlqueryengine microsoft.configurationmanagement.managementprovider Robust Programming For more information about error"
---

# Configuration Manager SDK documentation — pages 681-720

<!-- p.681 -->

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
SMS_Collection Server WMI Class
Delete a collection Software distribution overview About deployments Objects overview
How to Connect to a Configuration Manager Provider using Managed Code
How to Connect to a Configuration Manager Provider Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.682 -->

How to Get the Properties of a
Collection
Article • 10/10/2022

To get the properties of a collection
   1. Set up a connection to the SMS Provider.

   2. Get the specific collection instance by using the collection ID provided.

   3. Get the collection properties.

Example
The following example method gets the properties of a collection.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ReadCollectionProperties(connection, collectionID)     Dim collection
  Dim statusText     Set collection =
  connection.Get("SMS_Collection.CollectionID='" & collectionID & "'")
  WScript.Echo "Processing Collection - " & CStr(collection.CollectionID)
  WScript.Echo "-- Name: " & collection.Name     WScript.Echo "-- Comment: " &
  collection.Comment     WScript.Echo "-- Members: " &
  CStr(collection.MemberCount)     statusText = "None"    Select Case
  collection.CurrentStatus     Case 1        statusText = "Ready"     Case 2
  statusText = "Refreshing"     Case 5        statusText = "Awaiting Refresh"
  End Select         WScript.Echo "-- Status: " & statusTextEnd Sub

  c#

  public void ReadCollectionProperties(WqlConnectionManager connection, string
  collectionID){    IResultObject collection =
  connection.GetInstance(string.Format("SMS_Collection.CollectionID='{0}'",
  collectionID));    string statusText = "None";
  Console.WriteLine("Processing Collection - " + collectionID);
  Console.WriteLine("-- Name: " + collection["Name"].StringValue);
  Console.WriteLine("-- Comment: " + collection["Comment"].StringValue);
  Console.WriteLine("-- Members: " +
  collection["MemberCount"].IntegerValue.ToString());      switch
  (collection["CurrentStatus"].IntegerValue)     {         case 1:
  statusText = "Ready";            break;          case 2:          statusText

<!-- p.683 -->

  = "Refreshing";            break;        case 5:                     statusText =
  "Awaiting Refresh";            break;        default:                     break;        }
  Console.WriteLine("-- Status: " + statusText);}

The example method has the following parameters:

                                                                           ﾉ     Expand table

 Parameter      Type                   Description

 connection     - Managed:             A valid connection to the SMS Provider.
                WqlConnectionManager
                - VBScript:
                SWbemServices

 collectionID   - Managed: String      Unique auto-generated ID containing eight
                - VBScript: String     characters. For more information, see the CollectionID
                                       property of SMS_Collection Server WMI Class.

Compiling the Code
The C# example requires:

Namespaces
System

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

<!-- p.684 -->

See Also
SMS_Collection Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.685 -->

How to Initiate a One-time Membership
Evaluation for a Collection
Article • 10/10/2022

To Initiate a One-time Membership Evaluation
   1. Set up a connection to the SMS Provider.

   2. Get the specific collection instance by using the collection ID provided.

   3. Refresh the collection membership using the RequestRefresh method in the
        SMS_Collection class.

Example
The following example method refreshes the collection membership for a specific
collection.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub RefreshCollection(connection, collectionID)    Dim collection    Set
  collection = connection.Get("SMS_Collection.CollectionID='" & collectionID &
  "'")    Call collection.RequestRefresh()End Sub

  c#

  public void RefreshCollection(WqlConnectionManager connection, string
  collectionID){    IResultObject collection =
  connection.GetInstance(string.Format("SMS_Collection.CollectionID='{0}'",
  collectionID));    collection.ExecuteMethod("RequestRefresh", null);}

The example method has the following parameters:

                                                                            ﾉ      Expand table

 Parameter       Type                    Description

 connection      - Managed:              A valid connection to the SMS Provider.
                  WqlConnectionManager

<!-- p.686 -->

 Parameter      Type                        Description

                - VBScript:
                SWbemServices

 collectionID   - Managed: String           Unique auto-generated ID containing eight
                - VBScript: String          characters. For more information, see the CollectionID
                                            property of SMS_Collection Server WMI Class.

Compiling the Code
The C# example requires:

Namespaces
System

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
SMS_Collection Server WMI Class

Feedback
Was this page helpful?    Yes        No

<!-- p.687 -->

Provide product feedback

<!-- p.688 -->

About Compliance Settings (DCM)
Setup and Configuration
Article • 10/04/2022

To use desired configuration management on your Configuration Manager site, the
following needs to be in place:

      The site must be running Configuration Manager.

      Clients must be running the Configuration Manager client.

      The desired configuration management client agent must be enabled.

      Client computers must have installed the .NET Framework 2.0 or a later version.

Enabling the desired configuration management client agent makes it possible for
Configuration Manager clients that are assigned to this site to evaluate compliance with
assigned configuration baselines. This client agent is enabled by default, but it will not
evaluate its compliance until it downloads one or more configuration baselines and
evaluates them at the configured schedule.

Disabling the desired configuration client agent prevents Configuration Manager clients
that are assigned to this site from evaluating compliance with assigned configuration
baselines.

This setting to enable or disable the desired configuration management client agent,
together with any assigned configuration baselines, is downloaded to client computers
according to the Policy Polling Interval in the Computer Client Agent Properties dialog
box (by default, every 60 minutes).

  ７ Note

  When the desired configuration management client agent is enabled on client
  computers, the Systems Management Properties dialog box displays a
  Configurations tab that lists the downloaded configuration baselines and the
  results of its compliance evaluation. When the desired configuration management
  client agent is disabled, the Configurations tab is not visible. If the Configurations
  tab is not visible, the client is not running the desired configuration management
  client agent. This might be because the site is not enabled for desired configuration
  management, the client computer has not yet downloaded the policy to enable the
  desired configuration management client agent, a local policy has disabled the

<!-- p.689 -->

  desired configuration management client agent, or the client is not a Configuration
  Manager client.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.690 -->

How to Enable or Disable the
Compliance Settings (DCM) Agent
Article • 10/04/2022

In Configuration Manager, you enable or disable the Desired Configuration
Management Client Agent by modifying the site control file settings.

To enable or disable the Desired Configuration
Management Client Agent
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Desired Configuration Management Client Agent section
        of the site control file by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example method enables or disables the Desired Configuration
Management Client Agent by using the SMS_SCI_ClientComp class to connect to the
site control file and change the Flag property.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub EnableDisableDCMClientAgent(swbemServices,   _
                                  swbemContext,    _
                                  siteCode,        _
                                  enableDisableFlag)

  ' Load site control file and get DCM client component section.
  swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext
  Set swbemInst =
  swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
  Component',Sitecode='" & siteCode & "',ItemName='Configuration Management
  Agent'", , swbemContext)

<!-- p.691 -->

' Display DCM client agent settings before change.
Wscript.Echo " "
Wscript.Echo "Properties - Before Change"
Wscript.Echo "---------------------------"
Wscript.Echo swbemInst.ClientComponentName
Wscript.Echo swbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

' Set DCM client agent by setting flags value to   0 or 1 using the
enableDisableFlag variable.
swbemInst.Flags = enableDisableFlag

' Save new client agent settings.
swbemInst.Put_ , swbemContext
swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Commit", , , swbemContext
Set swbemInst = Nothing

' Refresh in-memory copy of the site control file and get the DCM client
component section.
swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , swbemContext
Set swbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteCode & "',ItemName='Configuration Management
Agent'", , swbemContext)

' Display DCM client agent settings after change.
Wscript.Echo " "
Wscript.Echo "Properties - After Change"
Wscript.Echo "---------------------------"
Wscript.Echo swbemInst.ClientComponentName
Wscript.Echo swbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

Set swbemInst = Nothing

End Sub

c#

public void EnableDisableDCMClientAgent(WqlConnectionManager connection,
                                        string siteCode,
                                        string enableDisableFlag)
{

     try
     {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Configuration Management
Agent'");

<!-- p.692 -->

              // Display DCM client agent settings before change.
              Console.WriteLine();
              Console.WriteLine("Properties - Before Change");
              Console.WriteLine("---------------------------");

  Console.WriteLine(siteDefinition["ClientComponentName"].StringValue);
          Console.WriteLine(siteDefinition["Flags"].StringValue + " (0 =
  Disabled, 1 = Enabled)");

          // Set DCM client agent by setting flags value to 0 or 1 using the
  enableDisableFlag variable.
          siteDefinition["Flags"].StringValue = enableDisableFlag;

              // Save the settings.
              siteDefinition.Put();

          // Verify change by reconnecting and getting the value again.
          IResultObject siteDefinition2 =
  connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
  Component',SiteCode='" + siteCode + "',ItemName='Configuration Management
  Agent'");

              // Display DCM client agent settings after change.
              Console.WriteLine();
              Console.WriteLine("Properties - After Change");
              Console.WriteLine("--------------------------");

  Console.WriteLine(siteDefinition2["ClientComponentName"].StringValue);
          Console.WriteLine(siteDefinition2["Flags"].StringValue + " (0 =
  Disabled, 1 = Enabled)");

      }

      catch (SmsException eX)
      {
          Console.WriteLine("Failed. Error: " + eX.InnerException.Message);
          throw;
      }

  }

The example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter           Type                    Description

 connection          - Managed:              A valid connection to the SMS Provider.
                      WqlConnectionManager
                     - VBScript:
                     SWbemServices

<!-- p.693 -->

 Parameter           Type                       Description

 swbemContext        - VBScript: SWbemContext   A valid context object. For more information,
                                                see How to Add a Configuration Manager
                                                Context Qualifier by Using WMI.

 siteCode            - Managed: String          The site code.
                     - VBScript: String

 enableDisableFlag   - Managed: String          Determines whether the Desired Configuration
                     - VBScript: String         Management Client Agent is enabled or
                                                disabled.

                                                0 - disabled

                                                1 - enabled

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

<!-- p.694 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About Compliance Settings (DCM) Setup and Configuration
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_ClientComp Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.695 -->

How to Configure the Default
Compliance Evaluation Schedule
Article • 10/04/2022

In Configuration Manager, the site control file maintains configuration for the
configuration of the site. These code samples query for the specific site control file item
Configuration Management Agent, and change the EvaluationSchedule value to set the
client agent evaluation schedule.

To configure the Default Compliance Evaluation Schedule
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Desired Configuration Management Client Agent section
        of the site control file by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following code example shows how to change the default compliance evaluation
schedule for the configuration management client agent.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ChangeDCMAgentEvaluationSchedule(swbemServices,    _
                                       swbemContext,     _
                                       siteCode,         _
                                       newAgentSchedule)

      ' The evaluation schedule is defined by a string stored in a schedule
  token format.
      ' Detailed information on the schedule token format can be found in the
  class SMS_ScheduleToken reference material.

      ' Load site control file and get DCM client component section.
  swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext

<!-- p.696 -->

Set swbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteCode & "',ItemName='Configuration Management
Agent'", , swbemContext)

      ' Loop through the array of embedded SMS_EmbeddedProperty instances for
the
      ' Number of Retries PropertyName. Get its value and display it.
      For Each vProperty In swbemInst.Props

         If vProperty.PropertyName = "EvaluationSchedule" Then

             ' Display DCM client agent evaluation schedule before change.
             Wscript.Echo " "
             Wscript.Echo "Evaluation Schedule - Before Change"
             Wscript.Echo "-----------------------------------"
             Wscript.Echo vProperty.Value2

            ' Set DCM client agent evaluation schedule using the
newAgentSchedule variable.
            vProperty.Value2 = newAgentSchedule

            ' Save new client agent settings
            swbemInst.Put_ , swbemContext
            swbemServices.ExecMethod
"SMS_SiteControlFile.Filetype=1,Sitecode=""" & siteCode & """", "Commit", ,
, swbemContext

          End If
      Next

    ' Refresh in-memory copy of the site control file and get the DCM client
component section.
swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , swbemContext
Set swbemInst = Nothing

Set swbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteCode & "',ItemName='Configuration Management
Agent'", , swbemContext)

      For Each vProperty In swbemInst.Props

         If vProperty.PropertyName = "EvaluationSchedule" Then

             ' Sisplay DCM client agent evaluation schedule before change.
             Wscript.Echo " "
             Wscript.Echo "Evaluation Schedule - After Change"
             Wscript.Echo "----------------------------------"
             Wscript.Echo vProperty.Value2

          End If
      Next

<!-- p.697 -->

End Sub

c#

public void ChangeDCMAgentEvaluationSchedule(WqlConnectionManager
connection,
                                             string siteCode,
                                             string newAgentSchedule)
{

    // The evaluation schedule is defined by a string stored in a schedule
token format.
    // Detailed information on the schedule token format can be found in the
class SMS_ScheduleToken reference material.

     try
     {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Configuration Management
Agent'");

        if
(siteDefinition.EmbeddedProperties.ContainsKey("EvaluationSchedule"))
        {
            Dictionary<string, IResultObject> WorkingEmbeddedProperties =
siteDefinition.EmbeddedProperties; //get temporary copy

            // Display DCM client agent settings before change.
            Console.WriteLine();
            Console.WriteLine("DCM Client Agent Schedule - Before Change");
            Console.WriteLine("-----------------------------------------");
            Console.WriteLine("Schedule in token format: " +
WorkingEmbeddedProperties["EvaluationSchedule"]["Value2"].StringValue);

            // Set DCM client agent setting to new value.
            WorkingEmbeddedProperties["EvaluationSchedule"]
["Value2"].StringValue = newAgentSchedule;
            siteDefinition.EmbeddedProperties = WorkingEmbeddedProperties;

            // Save the settings.
            siteDefinition.Put();

            // Verify change by reconnecting and getting the value again.
            Dictionary<string, IResultObject> WorkingEmbeddedProperties2 =
siteDefinition.EmbeddedProperties; //Get temporary copy for change
verification.

            // Display DCM client agent settings after change.
            Console.WriteLine();
            Console.WriteLine("DCM Client Agent Schedule - After Change");

<!-- p.698 -->

              Console.WriteLine("-----------------------------------------");
              Console.WriteLine("Schedule in token format: " +
  WorkingEmbeddedProperties2["EvaluationSchedule"]["Value2"].StringValue);

              }
      }

      catch (SmsException eX)
      {
          Console.WriteLine("Failed. Error: " + eX.InnerException.Message);
          throw;
      }

  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter          Type                       Description

 connection         - Managed:                 A valid connection to the SMS Provider.
                    WqlConnectionManager
                    - VBScript:
                    SWbemServices

 swbemContext       - VBScript: SWbemContext   A valid context object. For more information, see
                                               How to Add a Configuration Manager Context
                                               Qualifier by Using WMI.

 siteCode           - Managed: String          The site code.
                    - VBScript: String

 newAgentSchedule   - Managed: String          The new schedule in string format. For more
                    - VBScript: String         information, see About schedules.

Compiling the Code

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

<!-- p.699 -->

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
About Compliance Settings (DCM) Setup and Configuration
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_ClientComp Server WMI Class
About schedules How to Create a Schedule Token

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.700 -->

About Configuration Baselines and
Configuration Items
Article • 10/04/2022

In Configuration Manager, baselines are used to define the configuration of a product or
system that is established at a specific point in time. Configuration baselines in
Configuration Manager contain a defined set of desired configurations that are
evaluated for compliance as a group.

Configuration Baselines
Configuration baselines contain one or more configuration items with associated rules,
and they are assigned to computers through collections, together with a compliance
evaluation schedule.

  ７ Note

  Although you can assign configuration baselines to a collection that contains users,
  the configuration baselines are evaluated only by computers in the collection.

You can create your own configuration baselines with the Configuration Manager
console, and you can import configuration baselines from the following sources:

      A Best Practices configuration baseline from Microsoft or other vendors

      Custom authored configuration baselines from within your own organization, but
      external to Configuration Manager

      Another Configuration Manager site

      When configuration baselines are imported, unless they were originally created in
      the same Configuration Manager site, you cannot directly modify them in the
      Configuration Manager console. If you need to refine the configuration items to
      meet your business requirements, the recommended path is as follows:

   1. Create child configuration items with your custom values.

   2. Duplicate the configuration baseline.

   3. Edit the duplicated baseline, and replace the configuration items with your edited
      child configuration items.

<!-- p.701 -->

Configuration Baseline Rules
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

Configuration Baseline Assignment
Before client computers can assess their compliance with configuration baselines in
Configuration Manager, the configuration baseline must be assigned to them through
collections of computers.

The assignment consists of the following properties:

     The configuration baseline itself

     Which collection to target for compliance evaluation, and whether it includes any
     defined sub-collections

     The compliance evaluation schedule, which is initially configured with the default
     compliance evaluation schedule but can be changed for each assignment

     Configuration baseline assignments are optional properties for a configuration
     baseline. A single configuration baseline can be assigned to multiple collections by
     defining multiple configuration baseline assignments.

Dependent Configuration Baseline

<!-- p.702 -->

One of the configuration baseline rules is to include another configuration baseline. This
nesting capability provides a layered method of defining a base configuration baseline
for a wide range of computers and then refining this base configuration with additional
configuration baselines that have more specific configurations for computers with
similar roles.

Dependent baselines are also used when you want to combine your own business
requirements with those of an imported configuration baseline (such as Best Practices
configuration baselines from Microsoft) that cannot be directly edited. When the Best
Practices configuration baseline is upgraded with a new version, you can import the
later version without having to create a new configuration baseline.

Dependent configuration baselines are displayed in the Configuration Manager console
as a property of a configuration baseline.

Duplicate Configuration Baseline
A duplicate configuration baseline in Configuration Manager is an exact copy of an
existing configuration baseline that does not retain any relationship to the original.
Creating a duplicate configuration baseline might be appropriate if you wanted to
create a number of similar but unrelated configuration baselines and you had one
configuration baseline that you use as a template. Another scenario is if you needed to
redefine the rules or configuration items in an imported configuration baseline.

You cannot duplicate an imported configuration baseline if it contains configuration
data that the Configuration Manager cannot interpret.

Configuration Items
Configuration items define a discrete unit of configuration to assess for compliance.
They can contain one or more elements and their validation criteria, and they typically
define a unit of configuration that you want to monitor at the level of independent
change.

Configuration items are the building blocks for configuration baselines, and
consequently the same configuration item can be used in multiple configuration
baselines.

Configuration Manager supports the following configuration item types:

Operating system configuration item
A configuration item to determine compliance for settings relating to the operating

<!-- p.703 -->

system version and configuration.

Application configuration item
A configuration item to determine compliance for an application. This can include
whether the application is installed as well as details about its configuration.

General configuration item
A configuration item to determine compliance for general settings and objects, where
their existence does not depend on the operating system, an application, or a software
update.

Software updates configuration item
A configuration item to determine compliance of software updates using the software
updates feature in Configuration Manager.

You cannot import, create, or configure software updates configuration items in the
Desired Configuration Management node. Instead, these are made available to
configuration baselines through the software updates feature when software updates
are downloaded. This means that software updates configuration items can be selected
to be included in configuration baselines, although they are not displayed under the
Configuration Items node.

The other configuration items can be imported, created, and configured with the
Configuration Manager console. These configuration items display a number of
properties, which include the following:

     General

     Objects

     Settings

     Windows version

     Applicability

     Detection method

     The properties that are available to each configuration item depend on the
     configuration item type. For example, you can configure an operating system
     configuration item to check for the exact version of the operating system. This
     property is not applicable to the other configuration items, so you do not see the
     Windows Version property that is available for other configuration items. The
     following table lists the configurable properties of a configuration item in

<!-- p.704 -->

       Configuration Manager, and it shows whether the configurable property is
       available for each configuration item type.

                                                                            ﾉ   Expand table

 Configuration    General   Windows    Objects   Settings   Detection   Applicability   Security
 Item Type                  Version                         Method

 General          √         Ø          √         √          Ø           √               √

 Application      √         Ø          √         √          √           √               √

 Operating        √         √          √         √          Ø           Ø               √
 System

 Software         √         Ø          Ø         Ø          Ø           Ø               √
 Updates

Key:

       √ = Available property

       Ø = Property not available

With the exception of software updates configuration items, you can view and edit the
properties of each configuration item in the Configuration Items node under Desired
Configuration Management in the Configuration Manager console. Use the Software
Updates node to view and edit software updates configuration items.

In addition to the configurable properties of a configuration item in the Desired
Configuration Management node, you also see displayed audit information in the
General properties, which shows when the configuration item was created, when it was
last edited, and by whom. Additionally, a Relationships property tab shows how the
configuration item relates to other configuration items and configuration baselines.

Child Configuration Item
A child configuration item is a copy of a configuration item that continues to inherit the
properties of the original configuration item. You cannot modify the child configuration
item's inherited objects and settings with their validation criteria, but you can add
additional validation criteria to the inherited objects and settings, and you can also add
new objects and settings to the child configuration item. The usual purpose for creating
and editing a child configuration item is that it refines the original configuration item to
meet your business requirements.

<!-- p.705 -->

Because of the dependency relationship of properties that are inherited from the parent
to the child configuration item, modifying the original configuration item affects the
child configuration item.

Child configuration items are appropriate when you have imported configuration data
from a Best Practices configuration baseline and you want to be able to update the
configuration data when new versions are released that will continue to pass their
properties onto the child configuration item.

Another scenario for using child configuration item is when you need to retain
inheritance for precise administration. For example, you can use a child configuration
item if you have a configuration item that defines a corporate security policy that all
computers must comply with, but your finance department computers are subject to
additional security requirements. In this situation, you might create a child configuration
item from the corporate security policy configuration item. The child configuration item
inherits all the properties from the corporate security policy, but it is edited to contain
the additional security requirements. If the corporate security policy changed, the
original configuration item could be modified without having to also modify the
configuration item for the computers in the finance department. Similarly, if the
requirements for the finance department computers changed, only the child
configuration item would need to be modified and not the original configuration item
that defines the corporate security policy.

Duplicate Configuration Item
A duplicate configuration item is an exact copy of another configuration item that does
not retain any relationship to the original configuration item. You can therefore use a
duplicate configuration item as a template to modify just a few properties and
independently retain both configuration items, or you can use it when you have
imported a read-only configuration item (for example, from a Best Practices
configuration baseline) and want to use the configuration item with modification and
not retain any inheritance from the original configuration item.

Additionally, if you want to use an imported configuration item but delete from it
objects or settings (or their related validation criteria), your only editing choice is to
create a duplicate configuration item and edit that duplicate configuration item
accordingly.

Feedback

<!-- p.706 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.707 -->

How to Import Configuration Baselines
and Configuration Items
Article • 10/04/2022

In Configuration Manager, importing a configuration baseline or configuration item by
using the Configuration Manager SDK requires a properly formatted XML file. Unlike the
Configuration Manager console, the Configuration Manager SDK does not support
directly importing a CAB file.

  ） Important

  The encoding of the XML file must be set to UTF-16 encoded Unicode. The XML
  encoding can be identified in the XML header:

   <?xml version="1.0" encoding="utf-16" ?>

When configuration data is imported into Configuration Manager, the format can be the
following:

      DCM Digest XML only

To import Configuration Baselines and Configuration
Items
   1. Set up a connection to the SMS Provider.

   2. Read the source XML file into a variable.

   3. Create an instance the SMS_ConfigurationItem class.

   4. Copy the source file contents (XML) into the SMS_ConfigurationItem property
      SDMPackageXML .

   5. Save the configuration item instance.

Example
The following code examples show how to create an instance of a configuration baseline
or a configuration item and then populate it by importing a configuration baseline or a
configuration item XML definition.

<!-- p.708 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub DCMImportBaselineOrCI(swbemServices,     _
                            pathToFile)

  ' Set required variables.
  readFile = 1 'constant
  fileContents          =   ""
  initialReadSucceeded =    ""
  triStateTrue = -1 ' This sets the file read to Unicode.

  ' Check if source xml file exists.
  set fileSytemObject = CreateObject("Scripting.FileSystemObject")
  If fileSytemObject.FileExists(pathToFile) Then
      set textFile = fileSytemObject.OpenTextFile(pathToFile, readFile, False,
  triStateTrue)
      fileContents = textFile.ReadAll
      textFile.Close

         initialReadSucceeded = true

         set textFile = Nothing

         Wscript.Echo " "
         Wscript.Echo "Successfully read " & pathToFile

  Else
         initialReadSucceeded = false

      Wscript.Echo " "
      Wscript.Echo "File does not exist."
  End If
  set fileSytemObject = Nothing

  If initialReadSucceeded Then

         On Error Resume Next

          ' Create an instance of configuration item.
          set newCI =
  swbemServices.Get("SMS_ConfigurationItem").SpawnInstance_()

          ' Copy specified file contents (XML) into SMS_ConfigurationItem
  property.
          newCI.SDMPackageXML = fileContents

            ' Save configuration item.
            newCI.Put_

            If Err.Number<>0 Then

<!-- p.709 -->

              Wscript.Echo "Couldn't create configuration item."
              Wscript.Echo "Possible duplicate configuration item or invalid
XML."
               Wscript.Quit
           End If
       On Error Goto 0
Else
    Wscript.Echo " "
    Wscript.Echo "Failed to create configuration item."
End If

End Sub

c#

public void DCMImportBaselineOrCI(WqlConnectionManager connection,
                                  string pathToFile)
{

       // Set required variables.
       string fileContents = null;
       bool initialReadSucceeded = false;

    // Load XML file using pathToFile variable.
    try
    {
        // Open the file specified by the pathToFile variable and read the
contents into a string.
        using (StreamReader sr = new StreamReader(pathToFile,
System.Text.Encoding.Unicode))
        {
            fileContents = sr.ReadToEnd();
        }

          Console.WriteLine("Successfully read " + pathToFile + ".");

          initialReadSucceeded = true;
    }
    catch (Exception ex)
    {
        Console.WriteLine("Unable to read " + pathToFile + "." + "\n" +
ex.Message);
        throw;
    }

       // Run only if the initial read was successful.
       if (initialReadSucceeded)
       {
           try
           {
               // Create an instance of Configuration Item.

<!-- p.710 -->

              IResultObject newCI =
  connection.CreateInstance("SMS_ConfigurationItem");

                   // Copy specified file contents (XML) into SMS_ConfigurationItem
  property.
                   newCI["SDMPackageXML"].StringValue = fileContents;

                   // Save new SMS_ConfigurationItem object.
                   newCI.Put();
          }
          catch (SmsException ex)
          {
              Console.WriteLine("Failed to create configuration item using " +
  pathToFile + ".");
              Console.WriteLine(ex.Details);
              throw;
          }
      }
  }

The example method has the following parameters:

                                                                              ﾉ    Expand table

 Parameter           Type                              Description

 - connection        - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
 - swbemServices     - VBScript: SWbemServices

 pathToFile          - Managed: String                 Path of the XML file to import.
                     - VBScript: String

Compiling the Code

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

<!-- p.711 -->

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
SMS_ConfigurationItem Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.712 -->

How to Export Configuration Baselines
and Configuration Items
Article • 10/04/2022

In Configuration Manager, to export a configuration baseline or configuration item
using the Configuration Manager SDK, read the relevant SMS_ConfigurationItem
instance and write the SDMPackageXML property (string) to a file.

  ） Important

  The encoding of the XML file must be set to UTF-16 encoded Unicode.

To export Configuration Baselines and Configuration
Items
   1. Set up a connection to the SMS Provider.

   2. Get the specific instance of SMS_ConfigurationItem class using the unique ID of
        the configuration item (CI_ID).

   3. Copy the configuration item XML (SDMPackageXML) into a variable.

   4. Write the configuration item XML content to a file.

Example
The following code example shows how to read an instance of a configuration baseline
or configuration item and then export it to a file.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub DCMExportBaselineOrCI(swbemServices, _
                            pathToFile,    _
                            configurationItemId)

  ' Set required variables.
  fileContents          =          ""

<!-- p.713 -->

configurationItemXML    =    null

' Get specified configuration item (configurationItemId variable).
Set getCIInfo = swbemServices.Get("SMS_ConfigurationItem.CI_ID=" &
configurationItemId )

' Copy configuration item XML into variable.
configurationItemXML = getCIInfo.SDMPackageXML

Wscript.Echo configurationItemXML

' Open file for write (Unicode option enabled by second true).
Set FSO = CreateObject("Scripting.FileSystemObject")
Set textFile = FSO.CreateTextFile(pathToFile, true, true)

' Write XML content to file specified by pathToFile.
textFile.Write configurationItemXML
textFile.Close

Wscript.Echo " "
Wscript.Echo "Successfully wrote " & pathToFile

End Sub

c#

public void DCMExportBaselineOrCI(WqlConnectionManager connection,
                                  string pathToOutputFile,
                                  string configurationItemId)
{

     // Set required variables.
     string configurationItemXML = null;

     try
     {
        // Get the specified configuration item (configurationItemId
variable).
        IResultObject getCIInfo =
connection.GetInstance(@"SMS_ConfigurationItem.CI_ID=" +
configurationItemId);

           // Copy configuration item XML into variable.
           configurationItemXML = getCIInfo["SDMPackageXML"].StringValue;
    }
    catch (SmsException ex)
    {
        Console.WriteLine("Failed to retrieve configuration item xml. " +
"\n" + ex.Message);
        throw;
    }

<!-- p.714 -->

      StreamWriter sw = null;
      try
      {
          // Open file for output.
          sw = new StreamWriter(pathToOutputFile, false,
  System.Text.Encoding.Unicode);

              // Write XML to output file.
              sw.Write(configurationItemXML);
      }
      catch (Exception ex)
      {
          Console.WriteLine("Failed to write configuration item XML to: " +
  pathToOutputFile + "\n" + ex.Message);
          throw;
      }
      finally
      {
          if (sw != null)
          {
              sw.Close();
          }
      }

      Console.WriteLine("Wrote configuration item XML to: " +
  pathToOutputFile);
  }

The example method has the following parameters:

                                                                          ﾉ   Expand table

 Parameter             Type                        Description

 connection            - Managed:                  A valid connection to the SMS
                       WqlConnectionManager        Provider.
                       - VBScript: SWbemServices

 - pathToOutputFile    - Managed: String           Path to the output file.
 - pathToFile          - VBScript: String

 configurationItemId   - Managed: String           Identifier of a configuration item to
                       - VBScript: String          export.

Compiling the Code

Namespaces

<!-- p.715 -->

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
SMS_ConfigurationItem Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.716 -->

How to Assign Configuration Baselines
Article • 10/04/2022

In Configuration Manager, to assign a configuration baseline to a collection, an
assignment instance is created, populated with a minimum set of required values, and
saved.

To assign Configuration Baselines
   1. Set up a connection to the SMS Provider.

   2. Create an instance of SMS_BaselineAssignment .

   3. Populate the instance properties.

   4. Save the new SMS_BaselineAssignment instance.

Example
The following code examples show how to create an instance of a baseline assignment.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub DCMCreateAssignment(swbemServices,                           _
                          baselineID,                              _
                          applyToSubTargets,                       _
                          assignmentAction,                        _
                          assignmentName,                          _
                          assignmentDescription,                   _
                          desiredConfigType,                       _
                          distributionPointLocality,               _
                          evaluationSchedule,                      _
                          logComplianceToWinEvent,                 _
                          notifyUser,                              _
                          sendDetailedNonComplianceStatus,         _
                          startTime,                               _
                          suppressReboot,                          _
                          targetCollectionID,                      _
                          useGMTTimes)

  ' Create new assignment object.
  set newAssignment =

<!-- p.717 -->

swbemServices.Get("SMS_BaselineAssignment").SpawnInstance_()

' Assign variable values to assignment properties.
'    //
'    // The following properties are set by the provider on put():
'    //     AssignmentID
'    //     AssignmentUniqueID
'    //     SourceSite
'    //     CreationTime

newAssignment.ApplyToSubTargets = applyToSubTargets
newAssignment.AssignmentAction = assignmentAction
newAssignment.AssignmentName = assignmentName
newAssignment.AssignmentDescription = assignmentDescription
newAssignment.DesiredConfigType = desiredConfigType
newAssignment.DPLocality = distributionPointLocality
newAssignment.EvaluationSchedule = evaluationSchedule
newAssignment.LogComplianceToWinEvent = logComplianceToWinEvent
newAssignment.NotifyUser = notifyUser
newAssignment.SendDetailedNonComplianceStatus =
sendDetailedNonComplianceStatus
newAssignment.StartTime = startTime
newAssignment.SuppressReboot = suppressReboot
newAssignment.TargetCollectionID = targetCollectionID
newAssignment.UseGMTTimes = useGMTTimes
newAssignment.AssignedCIs = Array(baselineID)

' Save assignment.
newAssignment.Put_

Wscript.Echo " "
Wscript.Echo "Created new assignment."

End Sub

c#

public void DCMCreateAssignment(WqlConnectionManager connection,
                                bool applyToSubTargets,
                                int assignmentAction,
                                string assignmentName,
                                string assignmentDescription,
                                string desiredConfigType,
                                int distributionPointLocality,
                                string evaluationSchedule,
                                bool logComplianceToWinEvent,
                                bool notifyUser,
                                bool sendDetailedNonComplianceStatus,
                                string startTime,
                                int suppressReboot,
                                string targetCollectionID,

<!-- p.718 -->

                                 bool useGMTTimes,
                                 int baselineID)
{

    // Set required variables.
    // Set AssignedCIs like array with a known baseline id (this is the
initial creation of the assignment, so no existing values).
    int[] arrayBaselineNumbers = new int[] { baselineID };

    try
    {
        // Create new assignment object.
        IResultObject newAssignment =
connection.CreateInstance("SMS_BaselineAssignment");

        // Assign variable values to assignment properties.
        //
        // The following properties are set by the provider on put():
        //     AssignmentID
        //     AssignmentUniqueID
        //     SourceSite
        //     CreationTime
        newAssignment["ApplyToSubTargets"].BooleanValue = applyToSubTargets;
        newAssignment["AssignmentAction"].IntegerValue = assignmentAction;
        newAssignment["AssignmentName"].StringValue = assignmentName;
        newAssignment["AssignmentDescription"].StringValue =
assignmentDescription;
        newAssignment["DesiredConfigType"].StringValue = desiredConfigType;
        newAssignment["DPLocality"].IntegerValue =
distributionPointLocality;
        newAssignment["EvaluationSchedule"].StringValue =
evaluationSchedule;
        newAssignment["LogComplianceToWinEvent"].BooleanValue =
logComplianceToWinEvent;
        newAssignment["NotifyUser"].BooleanValue = notifyUser;
        newAssignment["SendDetailedNonComplianceStatus"].BooleanValue =
sendDetailedNonComplianceStatus;
        newAssignment["StartTime"].StringValue = startTime;
        newAssignment["SuppressReboot"].IntegerValue = suppressReboot;
        newAssignment["TargetCollectionID"].StringValue =
targetCollectionID;
        newAssignment["AssignedCIs"].IntegerArrayValue =
arrayBaselineNumbers;
        newAssignment["UseGMTTimes"].BooleanValue = useGMTTimes;

          // Save assignment object.
          newAssignment.Put();
    }
    catch (SmsException ex)
    {
        Console.WriteLine("Failed to create new assignment." + "\\n" +
ex.Message);
        throw;
    }

<!-- p.719 -->

       Console.WriteLine("Created new assignment.");

  }

The example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter                         Type                   Description

 - connection                      - Managed:             A valid connection to the SMS
 - swbemServices                   WqlConnectionManager   Provider.
                                   - VBScript:
                                   SWbemServices

 applyToSubTargets                 - Managed: Boolean     true to apply the configuration
                                   - VBScript: Boolean    item assignment to a subcollection.

 assignmentAction                  - Managed: Integer     Action associated with the
                                   - VBScript: Integer    configuration item assignment.

 assignmentName                    - Managed: String      assignmentName
                                   - VBScript: String

 assignmentDescription             - Managed: String      The local assignment name.
                                   - VBScript: String

 desiredConfigType                 - Managed: String      The type of the configuration item.
                                   - VBScript: String

 distributionPointLocality         - Managed: Integer     Flags that determine how the client
                                   - VBScript: Integer    obtains distribution points,
                                                          according to distribution point
                                                          locality.

 evaluationSchedule                - Managed: String      The assignment evaluation
                                   - VBScript: String     schedule.

 logComplianceToWinEvent           - Managed: Boolean     true to log compliance status to
                                   - VBScript: Boolean    Windows event logs.

 notifyUser                        - Managed: Boolean     true to notify the user when a
                                   - VBScript: Boolean    configuration item is available.

 sendDetailedNonComplianceStatus   - Managed: Boolean     true to send a detailed non-
                                   - VBScript: Boolean    compliance status message.

 startTime                         - Managed: String      The date and time when the
                                   - VBScript: String     configuration item assignment was

<!-- p.720 -->

 Parameter                     Type                   Description

                                                      initially offered.

 suppressReboot                - Managed: Integer     Value indicating whether the client
                               - VBScript: Integer    should not reboot the computer, if
                                                      there is a reboot pending after the
                                                      configuration item is applied.

 targetCollectionID            - Managed: String      The identifier of the collection to
                               - VBScript: String     which the assignment is targeted.

 useGMTTimes                   - Managed: Boolean     true if the times and schedules are
                               - VBScript: Boolean    in Universal Coordinated Time
                                                      (UTC).

 baselineID                    - Managed: Integer     Array of IDs for the configuration
                               Array                  items targeted by the assignment.
                               - VBScript: Integer
                               Array

Compiling the Code

Namespaces
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
