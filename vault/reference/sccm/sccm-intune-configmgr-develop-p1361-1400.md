---
title: "Configuration Manager SDK documentation — pages 1361-1400"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1361-1400
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1361-1400
family: sccm
documentKind: "doc"
abstract: "Parameter Type Description connection - Managed: A valid connection to the SMS Provider. WqlConnectionManager swbemServices - VBScript: SWbemServices swbemContext - VBScript: SWbemContext A valid context object. For more information, see How to Add a Configuration Manager Contex"
---

# Configuration Manager SDK documentation — pages 1361-1400

<!-- p.1361 -->

 Parameter           Type                       Description

 connection          - Managed:                 A valid connection to the SMS Provider.
                     WqlConnectionManager
 swbemServices       - VBScript:
                     SWbemServices

 swbemContext        - VBScript: SWbemContext   A valid context object. For more information,
                                                see How to Add a Configuration Manager
                                                Context Qualifier by Using WMI.

 enableDisableFlag   - Managed: String          Flag to enable or disable the client agent.
                     - VBScript: String

 siteCode            - Managed: String          The site code.
                     - VBScript: String
 siteToChange

Compiling the Code
The C# example requires:

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

<!-- p.1362 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Software distribution overview About software distribution setup and configuration
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1363 -->

How to Configure Software Distribution
Advertised Programs Client Agent
Settings
Article • 10/04/2022

In Configuration Manager, the site control file maintains configuration for the
configuration of the site. This topic shows how to configure software distribution
advertised programs client agent settings in the site control file. For more information
about reading from and writing to the site control file, see About the site control file.

  Ｕ Caution

  You should be experienced in managing a site's configuration before using the SMS
  Provider classes to modify the site configuration. You should use caution or avoid
  using the SMS_SCI_FileDefinition and SMS_SCI_SiteDefinition classes altogether.
  These classes manage the site control file itself. You can cause significant damage
  to a site by changing some configurable items.

To configure client agent settings
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Make a connection to the software distribution client component section of the
      site control file by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the property changes to the site control file.

Example
The following example queries for specific items in the software distribution client
component section of the site control file, and modifies those specific client agent
settings.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

<!-- p.1364 -->

vbs

Sub ConfigureClientAgentSettings(swbemServices, swbemContext, siteToChange,
enableDisableSWDClientAgent, enableDisableRequestUserPolicy,
setPolicyRefreshInterval, enableDisableVisibleSignalOnAvailable,
enableDisableAudibleSignalonAvailable,enableDisableCountdownSignal,setCountd
ownMinutes, enableDisableShowIcon)

    ' Load site control file and get SWD client component section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteToChange & """", "Refresh", , , swbemContext
    Set objSWbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteToChange & "',ItemName='Software
Distribution'", , swbemContext)

      ' Display SWD client agent settings before change.
      Wscript.Echo " "
      Wscript.Echo "Before Change"
      Wscript.Echo "-------------"

    Wscript.Echo " "
    Wscript.Echo objSWbemInst.ClientComponentName
    Wscript.Echo "Current value: " & objSWbemInst.Flags & " (0 = Disabled, 1
= Enabled)"
    Wscript.Echo " "
    objSWbemInst.Flags = enableDisableSWDClientAgent

    ' Enumerate though the property array, but display only the properties
that we're specifically interested in.
    ' Note: A list of all properties could be generated by just using the
following code:
    '     PropertyArray = objSwbemInst.props
    '     For i = 0 to ubound(PropertyArray)
    '        Wscript.Echo PropertyArray(i).PropertyName
    '        Wscript.Echo "Current value: " & PropertyArray(i).Value
    '     Next

      PropertyArray = objSwbemInst.props
      For i = 0 to ubound(PropertyArray)

         ' Client settings: Allow user targeted advertisement requests.
         If PropertyArray(i).PropertyName = "Request User Policy" Then
             Wscript.Echo PropertyArray(i).PropertyName
             Wscript.Echo "Current value: " & PropertyArray(i).Value
             Wscript.Echo " "
             PropertyArray(i).Value = enableDisableRequestUserPolicy
         End If

         ' Client settings: Policy polling interval (minutes).
         If PropertyArray(i).PropertyName = "Policy Refresh Interval" Then
             Wscript.Echo PropertyArray(i).PropertyName
             Wscript.Echo "Current value: " & PropertyArray(i).Value

<!-- p.1365 -->

              Wscript.Echo " "
              PropertyArray(i).Value = setPolicyRefreshInterval
          End If

        ' When new advertised programs are available: Display a notification
message.
        If PropertyArray(i).PropertyName = "Visible Signal on Available"
Then
            Wscript.Echo PropertyArray(i).PropertyName
            Wscript.Echo "Current value: " & PropertyArray(i).Value
            Wscript.Echo " "
            PropertyArray(i).Value = enableDisableVisibleSignalOnAvailable
        End If

          ' When new advertised programs are available: Play a sound.
          If PropertyArray(i).PropertyName = "Audible Signal on Available"
Then
              Wscript.Echo PropertyArray(i).PropertyName
              Wscript.Echo "Current value: " & PropertyArray(i).Value
              Wscript.Echo " "
              PropertyArray(i).Value = enableDisableAudibleSignalonAvailable
          End If

          ' When a scheduled program is about to run: Provide a countdown.
          If PropertyArray(i).PropertyName = "Countdown Signal" Then
              Wscript.Echo PropertyArray(i).PropertyName
              Wscript.Echo "Current value: " & PropertyArray(i).Value
              Wscript.Echo " "
              PropertyArray(i).Value = enableDisableCountdownSignal
          End If

          ' Countdown length (minutes).
          If PropertyArray(i).PropertyName = "Countdown Minutes" Then
              Wscript.Echo PropertyArray(i).PropertyName
              Wscript.Echo "Current value: " & PropertyArray(i).Value
              Wscript.Echo " "
              PropertyArray(i).Value = setCountdownMinutes
          End If

          ' Show advertised program notification icons in the notification
area.
           If PropertyArray(i).PropertyName = "Show Icon" Then
               Wscript.Echo PropertyArray(i).PropertyName
               Wscript.Echo "Current value: " & PropertyArray(i).Value
               Wscript.Echo " "
               PropertyArray(i).Value = enableDisableShowIcon
           End If
       Next

    ' Save new client agent settings.
    objSWbemInst.Put_ , swbemContext
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteToChange & """", "Commit", , , swbemContext

       ' Refresh in-memory copy of the site control file and get the SWD client

<!-- p.1366 -->

component section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteToChange & """", "Refresh", , , swbemContext
    Set objSWbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteToChange & "',ItemName='Software
Distribution'", , swbemContext)

       ' Display SWD client agent settings after change.

       Wscript.Echo " "
       Wscript.Echo "After Change"
       Wscript.Echo "------------"

    Wscript.Echo " "
    Wscript.Echo objSWbemInst.ClientComponentName
    Wscript.Echo "Current value: " & objSWbemInst.Flags & " (0 = Disabled, 1
= Enabled)"
    Wscript.Echo " "

       PropertyArray = objSwbemInst.props
       For i = 0 to ubound(PropertyArray)

          ' Client settings: Allow user targeted advertisement requests.
          If PropertyArray(i).PropertyName = "Request User Policy" Then
              Wscript.Echo PropertyArray(i).PropertyName
              Wscript.Echo "Current value: " & PropertyArray(i).Value
              Wscript.Echo " "
          End If

          ' Client settings: Policy polling interval (minutes).
          If PropertyArray(i).PropertyName = "Policy Refresh Interval" Then
              Wscript.Echo PropertyArray(i).PropertyName
              Wscript.Echo "Current value: " & PropertyArray(i).Value
              Wscript.Echo " "
          End If

        ' When new advertised programs are available: Display a notification
message.
        If PropertyArray(i).PropertyName = "Visible Signal on Available"
Then
            Wscript.Echo PropertyArray(i).PropertyName
            Wscript.Echo "Current value: " & PropertyArray(i).Value
            Wscript.Echo " "
        End If

          ' When new advertised programs are available: Play a sound.
          If PropertyArray(i).PropertyName = "Audible Signal on Available"
Then
              Wscript.Echo PropertyArray(i).PropertyName
              Wscript.Echo "Current value: " & PropertyArray(i).Value
              Wscript.Echo " "
          End If

          ' When a scheduled program is about to run: Provide a countdown.

<!-- p.1367 -->

          If PropertyArray(i).PropertyName = "Countdown Signal" Then
              Wscript.Echo PropertyArray(i).PropertyName
              Wscript.Echo "Current value: " & PropertyArray(i).Value
              Wscript.Echo " "
          End If

          ' Countdown length (minutes).
          If PropertyArray(i).PropertyName = "Countdown Minutes" Then
              Wscript.Echo PropertyArray(i).PropertyName
              Wscript.Echo "Current value: " & PropertyArray(i).Value
              Wscript.Echo " "
          End If

          ' Show advertised program notification icons in the notification
area.
         If PropertyArray(i).PropertyName = "Show Icon" Then
             Wscript.Echo PropertyArray(i).PropertyName
             Wscript.Echo "Current value: " & PropertyArray(i).Value
             Wscript.Echo " "
         End If
     Next

End Sub

c#

public void ConfigureSWDClientAgentSettings(WqlConnectionManager connection,
string siteCode, string enableDisableSWDClientAgent, string
enableDisableRequestUserPolicy, string setPolicyRefreshInterval, string
enableDisableVisibleSignalOnAvailable, string
enableDisableAudibleSignalonAvailable, string enableDisableCountdownSignal,
string setCountdownMinutes, string enableDisableShowIcon)
{
try
{
    IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Software Distribution'");

     Console.WriteLine();
     Console.WriteLine("Before Change");
     Console.WriteLine("-------------");

    // Enable software distribution to clients.
    // Set SWD client agent by setting flags value to 0 or 1 using the
EnableDisableSWDClientAgent variable.
    Console.WriteLine("Software Distribution Client Agent");
    Console.WriteLine("Current value: " +
siteDefinition["Flags"].StringValue + " (0 = Disabled, 1 = Enabled)");
    siteDefinition["Flags"].StringValue = enableDisableSWDClientAgent;

    foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)

<!-- p.1368 -->

    {
        Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties; // temp copy

        // Client settings: Allow user targeted advertisement requests.
        if (kvp.Value.PropertyList["PropertyName"] == "Request User Policy")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " +
embeddedProperties["Request User Policy"]["Value"].StringValue);
            embeddedProperties["Request User Policy"]["Value"].StringValue =
enableDisableRequestUserPolicy;
        }

        // Client settings: Policy polling interval (minutes).
        if (kvp.Value.PropertyList["PropertyName"] == "Policy Refresh
Interval")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " + embeddedProperties["Policy
Refresh Interval"]["Value"].StringValue);
            embeddedProperties["Policy Refresh Interval"]
["Value"].StringValue = setPolicyRefreshInterval;
        }

        // When new advertised programs are available: Display a
notification message.
        if (kvp.Value.PropertyList["PropertyName"] == "Visible Signal on
Available")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " +
embeddedProperties["Visible Signal on Available"]["Value"].StringValue);
            embeddedProperties["Visible Signal on Available"]
["Value"].StringValue = enableDisableVisibleSignalOnAvailable;
        }

        // When new advertised programs are available: Play a sound.
        if (kvp.Value.PropertyList["PropertyName"] == "Audible Signal on
Available")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " +
embeddedProperties["Audible Signal on Available"]["Value"].StringValue);
            embeddedProperties["Audible Signal on Available"]
["Value"].StringValue = enableDisableAudibleSignalonAvailable;
        }

        // When a scheduled program is about to run: Provide a countdown.
        if (kvp.Value.PropertyList["PropertyName"] == "Countdown Signal")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " +
embeddedProperties["Countdown Signal"]["Value"].StringValue);
            embeddedProperties["Countdown Signal"]["Value"].StringValue =

<!-- p.1369 -->

enableDisableCountdownSignal;
        }

        // Countdown length (minutes).
        if (kvp.Value.PropertyList["PropertyName"] == "Countdown Minutes")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " +
embeddedProperties["Countdown Minutes"]["Value"].StringValue);
            embeddedProperties["Countdown Minutes"]["Value"].StringValue =
setCountdownMinutes;
        }

        // Show advertised program notification icons in the notification
area.
        if (kvp.Value.PropertyList["PropertyName"] == "Show Icon")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " + embeddedProperties["Show
Icon"]["Value"].StringValue);
            embeddedProperties["Show Icon"]["Value"].StringValue =
enableDisableShowIcon;
        }

        // Store the settings that have changed.
        siteDefinition.EmbeddedProperties = embeddedProperties;
    }

    // Save the settings.
    siteDefinition.Put();

    // Verify change by reconnecting and getting the value again.
    IResultObject siteDefinition2 =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Software Distribution'");

    Console.WriteLine();
    Console.WriteLine("After Change");
    Console.WriteLine("-------------");

    // Enable software distribution to clients.
    Console.WriteLine("Software Distribution Client Agent");
    Console.WriteLine("Current value: " +
siteDefinition2["Flags"].StringValue + " (0 = Disabled, 1 = Enabled)");

    foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition2.EmbeddedProperties)
    {
        Dictionary<string, IResultObject> embeddedProperties =
siteDefinition2.EmbeddedProperties; // temp copy

        // Client settings: Allow user targeted advertisement requests.
        if (kvp.Value.PropertyList["PropertyName"] == "Request User Policy")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);

<!-- p.1370 -->

            Console.WriteLine("Current value: " +
embeddedProperties["Request User Policy"]["Value"].StringValue);
        }

        // Client settings: Policy polling interval (minutes).
        if (kvp.Value.PropertyList["PropertyName"] == "Policy Refresh
Interval")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " + embeddedProperties["Policy
Refresh Interval"]["Value"].StringValue);
        }

        // When new advertised programs are available: Display a
notification message.
        if (kvp.Value.PropertyList["PropertyName"] == "Visible Signal on
Available")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " +
embeddedProperties["Visible Signal on Available"]["Value"].StringValue);
        }

        // When new advertised programs are available: Play a sound.
        if (kvp.Value.PropertyList["PropertyName"] == "Audible Signal on
Available")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " +
embeddedProperties["Audible Signal on Available"]["Value"].StringValue);
        }

        // When a scheduled program is about to run: Provide a countdown.
        if (kvp.Value.PropertyList["PropertyName"] == "Countdown Signal")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " +
embeddedProperties["Countdown Signal"]["Value"].StringValue);
        }

        // Countdown length (minutes).
        if (kvp.Value.PropertyList["PropertyName"] == "Countdown Minutes")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " +
embeddedProperties["Countdown Minutes"]["Value"].StringValue);
        }

        // Show advertised program notification icons in the notification
area.
        if (kvp.Value.PropertyList["PropertyName"] == "Show Icon")
        {
            Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
            Console.WriteLine("Current value: " + embeddedProperties["Show
Icon"]["Value"].StringValue);

<!-- p.1371 -->

              }
      }

      Console.WriteLine(" ");
  }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
          throw;
      }

  }

The example method has the following parameters:

                                                                            ﾉ    Expand table

 Parameter                               Type                   Description

 connection                              - Managed:             A valid connection to the
                                         WqlConnectionManager   SMS Provider.
 swbemServices                           - VBScript:
                                         SWbemServices

 swbemContext                            - VBScript:            A valid context object. For
                                         SWbemContext           more information, see How
                                                                to Add a Configuration
                                                                Manager Context Qualifier
                                                                by Using WMI.

 siteCode                                - Managed: String      The site code.
                                         - VBScript: String
 siteToChange

 enableDisableSWDClientAgent             - Managed: String      Flag to enable or disable the
                                         - VBScript: String     client agent.

 setPolicyRefreshInterval                - Managed: String      Policy polling interval, in
                                         - VBScript: String     minutes.

 enableDisableRequestUserPolicy          - Managed: String      Flag to enable or disable
                                         - VBScript: String     targeted advertisement
                                                                requests.

 enableDisableVisibleSignalOnAvailable   - Managed: String      Flag to enable or disable
                                         - VBScript: String     display of a notification
                                                                when new advertised
                                                                programs are available.

<!-- p.1372 -->

 Parameter                               Type                 Description

 enableDisableAudibleSignalonAvailable   - Managed: String    Flag to enable or disable an
                                         - VBScript: String   audible notification when
                                                              new advertised programs are
                                                              available.

 enableDisableCountdownSignal            - Managed: String    Flag to enable or disable a
                                         - VBScript: String   countdown when a
                                                              scheduled program is about
                                                              to run.

 setCountdownMinutes                     - Managed: String    Countdown length, in
                                         - VBScript: String   minutes.

 enableDisableShowIcon                   - Managed: String    Flag to enable or disable the
                                         - VBScript: String   display of advertised
                                                              program notification icons in
                                                              the notification area.

Compiling the Code
The C# example requires:

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

<!-- p.1373 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Software distribution overview About software distribution setup and configuration
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1374 -->

How to Customize Advertisement
Branding Information in Configuration
Manager
Article • 10/04/2022

You set the software distribution branding information for the Configuration Manager
client by changing the SWDBrandingSubTitle property of the client agent component
section in the site control file.

To customize advertisement branding information
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the Client Agent site control file Client Component object from
        SMS_SCI_ClientComp Server WMI Class.

   3. Set the SWDBrandingSubtitle property to the value you want.

   4. Commit the changes back to the site control file.

Example
The following example method changes the software distribution branding text to the
supplied value.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub SetAdvertBranding(swbemServices,               _
                        swbemContext,                _
                        siteCode,                    _
                        brandingText)

      ' Load the site control file and get the Client Agent section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext

         Query = "SELECT * FROM SMS_SCI_ClientComp " & _
                 "WHERE ClientComponentName = 'Client Agent' " & _

<!-- p.1375 -->

                 "AND SiteCode = '" & siteCode & "'"

    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

     ' Only one instance is returned from the query.
     For Each SCIComponent In SCIComponentSet

          ' Loop through the array of embedded SMS_EmbeddedProperty instances.
          For Each vProperty In SCIComponent.Props

                 ' Setting: SWDBrandingSubTitle
                 If vProperty.PropertyName = "SWDBrandingSubTitle" Then
                     wscript.echo " "
                     wscript.echo vProperty.PropertyName
                     wscript.echo "Current value " & vProperty.Value1

                     ' Modify the value.
                     vProperty.Value1 = brandingText
                     wscript.echo "New value: " & brandingText
                 End If

          Next

                  ' Update the component in your copy of the site control file.
Get the path
                  ' to the updated object, which could be used later to retrieve
the instance.
                  Set SCICompPath = SCIComponent.Put_(wbemChangeFlagUpdateOnly,
swbemContext)
    Next

    ' Commit the change to the actual site control file.
    Set InParams =
swbemServices.Get("SMS_SiteControlFile").Methods_("CommitSCF").InParameters.
SpawnInstance_
    InParams.SiteCode = siteCode
    swbemServices.ExecMethod "SMS_SiteControlFile", "CommitSCF", InParams, ,
swbemContext

End Sub

c#

public void SetAdvertBranding(WqlConnectionManager connection, string
siteCode, string brandingText)
{
    try
    {
        // Get the site control file client component section.
        IResultObject clientAgent =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Client Agent'");

<!-- p.1376 -->

          // Update the branding information.
          Dictionary<string, IResultObject> embeddedProperties =
  clientAgent.EmbeddedProperties;

          embeddedProperties["SWDBrandingSubTitle"]
  ["Value1"].StringValue=brandingText;

              clientAgent.EmbeddedProperties = embeddedProperties;
              // Commit the change back to the site control file.
              clientAgent.Put();

      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to set branding text: " + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                               ﾉ   Expand table

 Parameter        Type                       Description

 connection       - Managed:                 A valid connection to the SMS Provider.
                  WqlConnectionManager
 swbemServices    - VBScript:
                  SWbemServices

 swbemContext     - VBScript: SWbemContext   A valid context object. For more information, see
                                             How to Add a Configuration Manager Context
                                             Qualifier by Using WMI.

 siteCode         - Managed: String          The site code for the Configuration Manager site.
                  - VBScript: String

 brandingText     - Managed: String          The text used to update the branding text.
                  - VBScript: String

Compiling the Code
This C# example requires:

Namespaces
System

<!-- p.1377 -->

System.Collections.Generic

System.Text

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
Software distribution overview About software distribution setup and configuration
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1378 -->

How to Configure a Software
Distribution Mandatory Advertisement
for Wake On LAN
Article • 10/04/2022

You can configure an existing mandatory advertisement for Wake On LAN by using the
SMS_Advertisement class and properties.

To configure a mandatory advertisement for Wake On
LAN
   1. Set up a connection to the SMS Provider.

   2. Get the specific advertisement using the provided advertisement ID.

   3. Replace the AdvertFlags property value with the value indicating Wake On LAN.

   4. Save the advertisement with the new property

Example
The following example method configures a software distribution mandatory
advertisement for Wake On LAN.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub SetWOLOnAdvertisment(connection, existingAdvertisementID)

      ' Define a constant with the hexadecimal value for WAKE_ON_LAN_ENABLED.
      Const WAKE_ON_LAN_ENABLED = &H00400000
      Dim advertisementToModify
      ' Get the specific advertisement instance to modify.
      Set advertisementToModify =
  connection.Get("SMS_Advertisement.AdvertisementID='" &
  existingadvertisementID & "'")

        ' List the existing property values.
        Wscript.Echo " "
        Wscript.Echo "Values before change: "

<!-- p.1379 -->

    Wscript.Echo "--------------------- "
    Wscript.Echo "Advertisement Name:            " &
advertisementToModify.AdvertisementName
    Wscript.Echo "Advertisement Flags (integer): " &
advertisementToModify.AdvertFlags

    ' Set the new property value.
    advertisementToModify.AdvertFlags = advertisementToModify.AdvertFlags OR
WAKE_ON_LAN_ENABLED

     ' Save the advertisement.
     advertisementToModify.Put_

    ' Output the new property values.
    Wscript.Echo " "
    Wscript.Echo "Values after change: "
    Wscript.Echo "--------------------- "
    Wscript.Echo "Advertisement Name:                " &
advertisementToModify.AdvertisementName
    Wscript.Echo "Advertisement Flags (integer):     " &
advertisementToModify.AdvertFlags

End Sub

c#

public void SetWOLOnAdvertisment(WqlConnectionManager connection,
                                 string existingAdvertisementID)
{
    // Define a constant with the hexadecimal value for WAKE_ON_LAN_ENABLED.
    const Int32 WAKE_ON_LAN_ENABLED = 0x00400000;

     try
     {
        // Get the specific advertisement instance to modify.
        IResultObject advertisementToModify =
connection.GetInstance(@"SMS_Advertisement.AdvertisementID='" +
existingAdvertisementID + "'");

        // List the existing property values.
        Console.WriteLine();
        Console.WriteLine("Values before change:");
        Console.WriteLine("_____________________");
        Console.WriteLine("Advertisement Name:            " +
advertisementToModify["AdvertisementName"].StringValue);
        Console.WriteLine("Advertisement Flags (integer): " +
advertisementToModify["AdvertFlags"].IntegerValue);

           // Modify the AdvertFlags value to include the WAKE_ON_LAN_ENABLED
value.
           advertisementToModify["AdvertFlags"].IntegerValue =

<!-- p.1380 -->

  advertisementToModify["AdvertFlags"].IntegerValue | WAKE_ON_LAN_ENABLED;

              // Save the advertisement with the new value.
              advertisementToModify.Put();

              // Reload the advertisement to verify the change.
              advertisementToModify.Get();

          // List the existing (modified) property values.
          Console.WriteLine();
          Console.WriteLine("Values after change:");
          Console.WriteLine("_____________________");
          Console.WriteLine("Advertisement Name:            " +
  advertisementToModify["AdvertisementName"].StringValue);
          Console.WriteLine("Advertisement Flags (integer): " +
  advertisementToModify["AdvertFlags"].IntegerValue);
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to modify advertisement. Error: " +
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                        ﾉ   Expand table

 Parameter                 Type                        Description

 connection                - Managed:                  A valid connection to the SMS
                           WqlConnectionManager        Provider.
 swebemServices            - VBScript: SWbemServices

 existingAdvertisementID   - Managed: String           The ID of the advertisment.
                           - VBScript: String

Compiling the Code
The C# example requires:

Namespaces
System

Microsoft.ConfigurationManagement.ManagementProvider

<!-- p.1381 -->

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
About deployments Software distribution overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1382 -->

How to Enable the Partner Notification
API
Article • 10/04/2022

The Partner Notification API allows third-party partners to use the Wake on LAN feature
of Configuration Manager to receive a list of computers that need to be woken up
based on advertisements for software distribution.

Before you can enable the Partner Notification API, you must configure Wake on LAN
for each primary site for which you want to enable this feature. For more information
about configuring Wake on LAN, see How to configure Wake on LAN.

To enable the Partner Notification API
   1. Set the following registry keys on the computer for each primary site where you
      want to enable this feature:

            HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\COMPONENTS\SMS_WAKEONLAN_MANAG

            ER\CreatePartnerNotification Set the value to 1 to enable the Partner

            Notification API and create a partner notification file. This key is set to 0 by
            default.

            HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\COMPONENTS\SMS_WAKEONLAN_MANAG
            ER\DeletePartnerNotificationOlderThanDays Deletes partner notification files

            older than the indicated number of days. The default value is 3 days.

            The partner notification file is a .csv file that contains a list of computers, by
            their FQDN, that you can wake with your custom code.

   2. Restart the SMS_EXECUTIVE service on each computer where you updated the
      registry keys.

   3. Create an advertisement by using the SMS_Advertisement Server WMI Class. Set
      the OfferType value to 0 and the AdvertFlags value to 0x00400000. For more
      information about advertisements, see How to Create an Advertisement and How
      to Configure a Software Distribution Mandatory Advertisement for Wake On LAN.

   4. Use the AssignedSchedule and AssignedScheduleEnabled properties to set a
      schedule for your advertisement.

<!-- p.1383 -->

     When the advertisement deadline is met, and Configuration Manager attempts to
     wake the computers, a partner notification file is generated and stored in the
     following location: <Configuration Manager Installation
     Directory>\inboxes\WOLMGR.box\Partners. If the OfferType property in the
     advertisement is not set to 0, Configuration Manager will not try to wake up
     computers through Wake on LAN, thus notification files are not generated.

   5. Use the list of computers in the partner notification file to wake the computers
     with your custom code.

See Also
How to Create an Advertisement
How to Configure a Software Distribution Mandatory Advertisement for Wake On LAN

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1384 -->

How to List Distribution Points for a Site
Article • 10/04/2022

The following example shows how to assign a distribution point to a package by using
the SMS_DistributionPoint Server WMI Class class and class properties in Configuration
Manager.

You only need to assign a distribution point to a package if the package contains source
files. The package is not advertised until the program source files have been propagated
to a distribution point share. You can use the default distribution point share, or you can
specify a share to use. You can also specify more than one distribution point to use to
distribute your package source files, although the following example does not
demonstrate that.

  ７ Note

  To identify branch distribution points, check the IsPeerDP property of the specific
  SMS_DistributionPoint class instance. If the IsPeerDP property is true, then the
  distribution point is a branch distribution point.

To list distribution points for a site
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Run a query, which populates a variable with a collection of distribution point
        objects.

   3. Enumerate through the collection of and list the distribution points returned by the
        query.

Example
The following example method lists distribution points for a site.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

<!-- p.1385 -->

Sub ListDistributionPointsForSite(connection, siteCode)

    ' This query selects all distribution points for a site based on the
provided site code.
    Query = "SELECT * FROM SMS_SystemResourceList WHERE RoleName='SMS
Distribution Point' AND SiteCode='" & siteCode & "'"

    ' Run query, which populates listOfResources with a collection of
objects.
    Set ListOfResources = connection.ExecQuery(query, , wbemFlagForwardOnly
Or wbemFlagReturnImmediately)

     ' Output header for list of distribution points.
     Wscript.Echo "List of distribution points for site: " & siteCode
     Wscript.Echo "--------------------------------------------"

     ' Enumerate through the collection of objects returned by the query.
     For Each resource In listOfResources
         ' Output the server name for each distribution point.
         Wscript.Echo resource.ServerName
     Next

End Sub

c#

public void ListDistributionPointsForSite(WqlConnectionManager connection,
string siteCode)
{
    try
    {
        // This query selects all distribution points for a site based on
the provided site code.
        string query = "SELECT * FROM SMS_SystemResourceList WHERE
RoleName='SMS Distribution Point' AND SiteCode='" + siteCode + "'";

        // Run query, which populates 'listOfResources' with a collection of
objects.
        IResultObject listOfResources =
connection.QueryProcessor.ExecuteQuery(query);

        // Output header for list of distribution points.
        Console.WriteLine("List of distribution points for site: " +
siteCode);
        Console.WriteLine("--------------------------------------------");

          // Enumerate through the collection of objects returned by the
query.
          foreach (IResultObject resource in listOfResources)
          {
              // Output the server name for each distribution point.

<!-- p.1386 -->

                  Console.WriteLine(resource["ServerName"].StringValue);
              }
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to list distribution points. Error: " +
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                             ﾉ   Expand table

 Parameter         Type                        Description

 connection        - Managed:                  A valid connection to the SMS Provider.
                   WqlConnectionManager
 swebemServices    - VBScript: SWbemServices

 siteCode          - Managed: String           The site code for the site that supports the
                   - VBScript: String          distribution points.

Compiling the Code
The C# example requires:

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

<!-- p.1387 -->

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Software distribution overview About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class
SMS_DistributionPoint Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1388 -->

How to Set the Distribute on Demand
Flag
Article • 01/05/2024

The following example shows how to set the "distribute on demand" flag property of an
existing package by using the SMS_Package Server WMI Class class in Configuration
Manager.

To set the distribute on demand flag
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Load the existing package object by using SMS_Package Server WMI Class class.

   3. Populate the package flag property.

   4. Save the package and the new package properties.

Example
The following example method sets the "distribute on demand" flag for a package.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub SetDistributeOnDemandFlag(connection,              _
                                existingPackageID)

      ' Define a constant with the hexadecimal value for the
  DISTRIBUTE_ON_DEMAND.
      DISTRIBUTE_ON_DEMAND = &H40000000

      ' Get the specific package instance to modify.
      Set packageToModify = connection.Get("SMS_Package.PackageID='" &
  existingpackageID & "'")

         ' List the existing property values.
         Wscript.Echo " "
         Wscript.Echo "Values before change: "
         Wscript.Echo "--------------------- "
         Wscript.Echo "Package Name:             " & packageToModify.Name

<!-- p.1389 -->

     Wscript.Echo "Package Flags (integer): " & packageToModify.PkgFlags

    ' Set the new property value.
    packageToModify.PkgFlags = packageToModify.PkgFlags OR
DISTRIBUTE_ON_DEMAND

     ' Save the package.
     packageToModify.Put_

     ' Output the new property values.
     Wscript.Echo " "
     Wscript.Echo "Values after change: "
     Wscript.Echo "--------------------- "
     Wscript.Echo "Package Name:               " & packageToModify.Name
     Wscript.Echo "Package Flags (integer):    " & packageToModify.PkgFlags

End Sub

c#

public void SetDistributeOnDemandFlag(WqlConnectionManager connection,
                                      string existingPackageID)
{
    // Define a constant with the hexadecimal value for
DISTRIBUTE_ON_DEMAND.
    const Int32 DISTRIBUTE_ON_DEMAND = 0x40000000;

     try
     {
        // Get the specific package instance to modify.
        IResultObject packageToModify =
connection.GetInstance(@"SMS_Package.PackageID='" + existingPackageID +
"'");

        // List the existing property values.
        Console.WriteLine();
        Console.WriteLine("Values before change:");
        Console.WriteLine("_____________________");
        Console.WriteLine("Package Name:            " +
packageToModify["Name"].StringValue);
        Console.WriteLine("Package Flags (integer): " +
packageToModify["PkgFlags"].IntegerValue);

           // Modify the PkgFlags value to include the DISTRIBUTE_ON_DEMAND
value.
        packageToModify["PkgFlags"].IntegerValue =
packageToModify["PkgFlags"].IntegerValue | DISTRIBUTE_ON_DEMAND;

           // Save the package with the new value.
           packageToModify.Put();

<!-- p.1390 -->

              // Reload the package to verify the change.
              packageToModify.Get();

          // List the existing (modified) property values.
          Console.WriteLine();
          Console.WriteLine("Values after change:");
          Console.WriteLine("_____________________");
          Console.WriteLine("Package Name:            " +
  packageToModify["Name"].StringValue);
          Console.WriteLine("Package Flags (integer): " +
  packageToModify["PkgFlags"].IntegerValue);
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to modify package. Error: " + ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                             ﾉ   Expand table

 Parameter            Type                              Description

 connection           - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
                      - VBScript: SWbemServices
 swebemServices

 existingPackageID    - Managed: String                 The ID of the package.
                      - VBScript: String

Compiling the Code
The C# example requires:

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

<!-- p.1391 -->

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Software distribution overview Objects overview How to Connect to an SMS Provider in
Configuration Manager by Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
SMS_Package Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1392 -->

How to Enable or Disable Software
Metering
Article • 10/04/2022

You enable or disable the Software Metering Client Agent, in Configuration Manager, by
modifying the site control file settings.

   Tip

  For additional information on changing client settings, see How to Apply Custom
  Client Settings.

To enable or disable the software metering client agent
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Software Metering Client Agent section of the site
        control file by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example method enables or disables the Software Metering Client Agent
by using the SMS_SCI_ClientComp class to connect to the site control file and change
properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub EnableDisableSWMClientAgent(swbemServices,     _
                                  swbemContext,      _
                                  enableDisableFlag, _
                                  siteToChange )

         ' Load site control file and get SWM client component section.
         swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &

<!-- p.1393 -->

siteToChange & """", "Refresh", , , swbemContext
    Set objSWbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteToChange & "',ItemName='Software Metering
Agent'", , swbemContext)

     ' Display SWM client agent settings before change
     Wscript.Echo " "
     Wscript.Echo "Properties - Before Change"
     Wscript.Echo "---------------------------"
     Wscript.Echo objSWbemInst.ClientComponentName
     Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

    ' Set SWM client agent by setting Flags value to   0 or 1 using the
enableDisableFlag variable.
    objSWbemInst.Flags = enableDisableFlag

    ' Save new client agent settings.
    objSWbemInst.Put_ , swbemContext
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteToChange & """", "Commit", , , swbemContext

    ' Refresh in-memory copy of the site control file and get the client
component section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteToChange & """", "Refresh", , , swbemContext
    Set objSWbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteToChange & "',ItemName='Software Metering
Agent'", , swbemContext)

     ' Display SWM client agent settings after change.
     Wscript.Echo " "
     Wscript.Echo "Properties - After Change"
     Wscript.Echo "---------------------------"
     Wscript.Echo objSWbemInst.ClientComponentName
     Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

End Sub

c#

public void EnableDisableSWMClientAgent(WqlConnectionManager connection,
                                        string siteCode,
                                        string enableDisableFlag)

{
     try
     {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client

<!-- p.1394 -->

  Component',SiteCode='" + siteCode + "',ItemName='Software Metering Agent'");

              // Display client agent settings before changing the properties.
              Console.WriteLine();
              Console.WriteLine("Properties - Before Change");
              Console.WriteLine("---------------------------");

  Console.WriteLine(siteDefinition["ClientComponentName"].StringValue);
          Console.WriteLine(siteDefinition["Flags"].StringValue + " (0 =
  Disabled, 1 = Enabled)");

          // Set client agent by setting "Flags" value to 0 or 1 by using the
  enableDisableFlag variable.
          siteDefinition["Flags"].StringValue = enableDisableFlag;

              // Save the settings.
              siteDefinition.Put();

          // Verify the change by reconnecting and getting the value again.
          IResultObject siteDefinition2 =
  connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
  Component',SiteCode='" + siteCode + "',ItemName='Software Metering Agent'");

              // Display client agent settings after changing the properties.
              Console.WriteLine();
              Console.WriteLine("Properties - After Change");
              Console.WriteLine("--------------------------");

  Console.WriteLine(siteDefinition2["ClientComponentName"].StringValue);
          Console.WriteLine(siteDefinition2["Flags"].StringValue + " (0 =
  Disabled, 1 = Enabled)");
      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
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

<!-- p.1395 -->

 Parameter           Type                       Description

 swbemContext        - VBScript: SWbemContext   A valid context object. For more information,
                                                see How to Add a Configuration Manager
                                                Context Qualifier by Using WMI.

 siteCode            - Managed: String          The site code.
                     - VBScript: String

 enableDisableFlag   - Managed: String          Determines whether the Software Metering
                     - VBScript: String         Client Agent is enabled or disabled.

                                                0 - Disabled

                                                1 - Enabled

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

.NET Framework Security

<!-- p.1396 -->

For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager Software Development Kit
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1397 -->

How to Configure Automatic Software
Metering Rule Generation
Article • 10/04/2022

You configure Automatic Software Metering Rule Generation settings, in Configuration
Manager, by modifying the site control file.

  ） Important

  This setting is shared across the whole hierarchy, and only can be configured on the
  CAS or a standalone primary site.

To configure automatic software metering rule
generation
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Software Metering Client Agent section of the site
        control file by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the property changes to the site control file.

Example
The following example method configures various Software Metering Rule Generation
settings by using the SMS_SCI_ClientComp class to connect to the site control file and
change properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureAutomaticSWMRuleGeneration(swbemServices,                          _
                                          swbemContext,                           _
                                          siteCode,                               _
                                          enableAutoCreateDisabledRule,           _
                                          newAutoCreatePercentage,                _

<!-- p.1398 -->

                                         newAutoCreateThreshold)

    ' Load site control file and get the SMS_SCI_ClientComp section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , swbemContext

    Query = "SELECT * FROM SMS_SCI_ClientComp " &  _
    "WHERE ClientComponentName = 'Software Metering Agent'" & _
    "AND SiteCode = '" & siteCode & "'"

     Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

    ' Only one instance is returned from the query.
    For Each SCIComponent In SCIComponentSet

       'Loop through the array of embedded SMS_EmbeddedProperty instances.
       For Each vProperty In SCIComponent.Props

              ' Setting: Auto Create Disabled Rule
              If vProperty.PropertyName = "Auto Create Disabled Rule" Then
                  wscript.echo " "
                  wscript.echo vProperty.PropertyName
                  wscript.echo "Current value " & vProperty.Value

                  'Modify the value.
                  vProperty.Value = enableAutoCreateDisabledRule
                  wscript.echo "New value " & enableAutoCreateDisabledRule
              End If

              ' Setting: Auto Create Percentage
              If vProperty.PropertyName = "Auto Create Percentage" Then
                  wscript.echo " "
                  wscript.echo vProperty.PropertyName
                  wscript.echo "Current value " & vProperty.Value

                  ' Modify the value.
                  vProperty.Value = newAutoCreatePercentage
                  wscript.echo "New value " & newAutoCreatePercentage
              End If

              ' Setting: Auto Create Threshold
              If vProperty.PropertyName = "Auto Create Threshold" Then
                  wscript.echo " "
                  wscript.echo vProperty.PropertyName
                  wscript.echo "Current value " & vProperty.Value

                  ' Modify the value.
                  vProperty.Value = newAutoCreateThreshold
                  wscript.echo "New value " & newAutoCreateThreshold
              End If

       Next

       ' Update the component in your copy of the site control file. Get

<!-- p.1399 -->

the path
        ' to the updated object, which could be used later to retrieve the
instance.
        Set SCICompPath = SCIComponent.Put_(wbemChangeFlagUpdateOnly,
swbemContext)

     Next

    ' Commit the change to the actual site control file.
    Set InParams =
swbemServices.Get("SMS_SiteControlFile").Methods_("CommitSCF").InParameters.
SpawnInstance_
    InParams.SiteCode = siteCode
    swbemServices.ExecMethod "SMS_SiteControlFile", "CommitSCF", InParams, ,
swbemContext

End Sub

c#

public void ConfigureAutomaticSWMRuleGeneration(WqlConnectionManager
connection,
                                                string siteCode,
                                                string
enableAutoCreateDisabledRule,
                                                string
newAutoCreatePercentage,
                                                string
newAutoCreateThreshold)
{
    try
    {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Software Metering Agent'");

        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {
            // Create temporary working copy of embedded properties.
            Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

            //Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);

            // Setting: Auto Create Disabled Rule
            if (kvp.Value.PropertyList["PropertyName"] == "Auto Create
Disabled Rule")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);

<!-- p.1400 -->

                Console.WriteLine("Current value: " +
embeddedProperties["Auto Create Disabled Rule"]["Value"].StringValue);

                   // Change value using the enableAutoCreateDisabledRule value
passed in.
                embeddedProperties["Auto Create Disabled Rule"]
["Value"].StringValue = enableAutoCreateDisabledRule;
                Console.WriteLine("New value    : " +
enableAutoCreateDisabledRule);
            }

               // Setting: Auto Create Percentage
               if (kvp.Value.PropertyList["PropertyName"] == "Auto Create
Percentage")
               {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties["Auto Create Percentage"]["Value"].StringValue);

                   // Change value using the newAutoCreatePercentage value
passed in.
                embeddedProperties["Auto Create Percentage"]
["Value"].StringValue = newAutoCreatePercentage;
                Console.WriteLine("New value    : " +
newAutoCreatePercentage);
            }

               // Setting: Auto Create Threshold
               if (kvp.Value.PropertyList["PropertyName"] == "Auto Create
Threshold")
               {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties["Auto Create Threshold"]["Value"].StringValue);

                   // Change value using the newAutoCreateThreshold value
passed in.
                embeddedProperties["Auto Create Threshold"]
["Value"].StringValue = newAutoCreateThreshold;
                Console.WriteLine("New value    : " +
newAutoCreateThreshold);
            }

               // Store the settings that have changed.
               siteDefinition.EmbeddedProperties = embeddedProperties;
        }

        // Save the settings.
        siteDefinition.Put();

    }

    catch (SmsException ex)
