---
title: "Configuration Manager SDK documentation — pages 841-880"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0841-0880
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0841-0880
family: sccm
documentKind: "doc"
abstract: "The following procedure creates the IConsoleView2 derived class. To create a console view class Create the following new class: public class MyViewDescription : IConsoleView2 { override protected Type TypeOfViewController { get { return typeof(MyViewController); } } override pro"
---

# Configuration Manager SDK documentation — pages 841-880

<!-- p.841 -->

The following procedure creates the IConsoleView2 derived class.

To create a console view class

     Create the following new class:

        public class MyViewDescription : IConsoleView2
        {
            override protected Type TypeOfViewController    {       get {
        return typeof(MyViewController); }     }
            override protected Type TypeOfView      {     get { return
        typeof(Overview); }     }        public override bool TryConfigure(ref
        XmlElement persistedConfigurationData)    {        return false;    }
        new public bool TryInitialize(ScopeNode scopeNode, AssemblyDescription
        resourceAssembly, ViewAssemblyDescription viewAssemblyDescription)    {
        return true;    }
        }

Create the extension node XML
The following XML is required in order to load your extension into the console. Note
that the DisplayName and Description properties refer to names in your assembly's
resource file.

  <RootNodeDescription NamespaceGuid="c192799c-82cd-43cc-bc11-12996bca800f"
  Id="MyViewNode" DisplayName="ViewNodeName"
  Description="ViewNodeDescription"> <ResourceAssembly>
  <Assembly>NameofMyAssembly.dll</Assembly>
  <Type>NameofMyAssembly.Resources.resources</Type> </ResourceAssembly>
  <ImagesDescription>    <ResourceAssembly>       <Assembly>
  NameofMyAssembly.dll</Assembly>      <Type>
  NameofMyAssembly.Resources.resources</Type>     </ResourceAssembly>
  <ImageResourceName>NodeIcon</ImageResourceName> </ImagesDescription>
  <ViewAssemblyDescriptions>    <ViewAssemblyDescription>       <Assembly>
  NameofMyAssembly.dll</Assembly>
  <Type>NameofMyAssembly.MyViewDescription</Type>
  </ViewAssemblyDescription> </ViewAssemblyDescriptions>
  </RootNodeDescription>

Deploy the Assembly

<!-- p.842 -->

The following procedure builds the assembly you have created and copies it to the
Configuration Manager console assemblies folder. For important information about
deploying Configuration Manager console extensions, see Configuration Manager
Console Extension Deployment.

To deploy the view assembly

   1. Build the project, and depending on where you created your project, the assembly
     should be created as \Visual Studio
     2010\Projects\ConfigMgrControl\ConfigMgrObjectsControl\bin\Debug\NameofMy
     Assembly.dll.

        ７ Note

        In other parts of the Console Extension section, the examples use an assembly
        named ConfigMgrObjectsControl.dll . If you are building the examples in
        other sections, make sure to name the assembly ConfigMgrObjectsControl.dll
        at this step (or change the other assembly references to your specific
        assembly name).

   2. Copy the assembly to the %ProgramFiles%\Microsoft Endpoint
     Manager\AdminConsole\bin folder.

See Also
About Configuration Manager Administrator Console Views
How to Create Node XML for a Configuration Manager Administrator Console View

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.843 -->

How to Create Node XML for a
Configuration Manager Console Grid
View
Article • 10/04/2022

To create the node XML for the Configuration Manager console default grid view you
create an XML file describing a RootNodeDescription element.

The XML in this procedure is used with the assembly you create in How to Create a
Configuration Manager Administrator Console View. When the user clicks on the "My
Node" node, it displays a list of SMS_SCI_SysResUse classes in the Configuration Manager
in the view pane.

The following elements and attributes are particularly important:

      RootNodeDescription . The attribute NamespaceGuid identifies the Site Configuration

      node.

To create the node XML for a view
   1. If it is open, close the Configuration Manager console.

   2. In Notepad, create an XML file that contains the following XML:

        <RootNodeDescription NamespaceGuid="c192799c-82cd-43cc-bc11-
        12996bca800f" Id="MyNode" DisplayName="NodeName"
        Description="NodeDescription">     <ResourceAssembly>
        <Assembly>UIExtensionsDemo.dll</Assembly>
        <Type>UIExtensionsDemo.Resources.resources</Type>
        </ResourceAssembly> <ImagesDescription>        <ResourceAssembly>
        <Assembly>UIExtensionsDemo.dll</Assembly>
        <Type>UIExtensionsDemo.Resources.resources</Type>
        </ResourceAssembly>      <ImageResourceName>NodeIcon</ImageResourceName>
        </ImagesDescription>    <ViewAssemblyDescriptions>
        <ViewAssemblyDescription>
        <Assembly>AdminUI.ConsoleView.dll</Assembly>
        <Type>Microsoft.ConfigurationManagement.AdminConsole.ConsoleView.ViewDe
        scription</Type>     <CustomData>           <ConfigurationData
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <PropertyItemsData>     <Properties>
        <string>RoleName</string>                   <string>SiteCode</string>
        </Properties>                 <ClassName>SMS_SCI_SysResUse</ClassName>

<!-- p.844 -->

        </PropertyItemsData> </ConfigurationData>        </CustomData>
        </ViewAssemblyDescription>   </ViewAssemblyDescriptions>   <Actions>
        </Actions>   <Queries>      <QueryDescription NamespaceGuid="81957874-
        9c03-4261-84eb-3cf6c31bf251" Type="WQL">         <Query>SELECT * FROM
        SMS_SCI_SysResUse</Query>
        <ReturnedClassType>MyClass</ReturnedClassType>      </QueryDescription>
        </Queries></RootNodeDescription>

   3. Save the XML file in the folder
     %ProgramFiles%\AdminConsole\XmlStorage\Extensions\Nodes\c192799c-82cd-
     43cc-bc11-12996bca800f with the file name ConfigMgrObjectsView.xml. Be sure to
     save the file as type All Files . If the Extensions, Nodes, or GUID folders do not
     yet exist, create them.

   4. Start the Configuration Manager console, select Site Configuration in the tree
     view, and select the My Node node. You should see a list of SMS_SCI_SysResUse
     classes in the view.

See Also
About Configuration Manager Administrator Console Views
How to Create a Configuration Manager Administrator Console View
How to Find a Configuration Manager Node GUID

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.845 -->

How to Configure Heartbeat Discovery
Article • 10/04/2022

In Configuration Manager, you configure the Heartbeat Discovery settings by modifying
the necessary site control file settings.

To configure Heartbeat Discovery
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Heartbeat Discovery section of the site control file by
        using the SMS_SCI_Component class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example sets the Heartbeat Discovery settings by using the
SMS_SCI_Component class to connect to the site control file and change properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureHeartbeatDiscoverySettings1(swbemServices,
  _
                                           swbemContext,
  _
                                           siteCode,
  _
                                           serverName,
  _

  newHeartbeatSiteControlFileSchedule)

      ' Load site control file and get the SMS_SITE_CONTROL_MANAGER section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext

         Query = "SELECT * FROM SMS_SCI_Component " &                                _
         "WHERE ItemName = 'SMS_SITE_CONTROL_MANAGER|" & serverName & "' " &         _
         "AND SiteCode = '" & siteCode & "'"

<!-- p.846 -->

    ' Get the SMS Software Update Point properties.
    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

    ' Only one instance is returned from the query.
    For Each SCIComponent In SCIComponentSet

          ' Display the server name.
          wscript.echo "Server: " & SCIComponent.Name

          ' Loop through the array of embedded SMS_EmbeddedProperty instances.
          For Each vProperty In SCIComponent.Props

            ' Setting: Heartbeat Site Control File Schedule.
            If vProperty.PropertyName = "Heartbeat Site Control File
Schedule" Then
                wscript.echo " "
                wscript.echo vProperty.PropertyName
                wscript.echo "Current value " & vProperty.Value1

                'Modify the value.
                vProperty.Value1 = newHeartbeatSiteControlFileSchedule
                wscript.echo "New value " &
newHeartbeatSiteControlFileSchedule
            End If

            Next

            ' Update the component in your copy of the site control file. Get
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

' SEPARATE EXAMPLE TO ENABLE HEARTBEAT DISCOVERY ON THE CLIENT
Sub ConfigureHeartbeatDiscoverySettings2(swbemServices,
_
                                         swbemContext,
_
                                         siteCode,
_

<!-- p.847 -->

                                             enableDisableHeartbeatDDR)

    ' Load site control file and get the SMS_SCI_ClientConfig section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , swbemContext

     Query = "SELECT * FROM SMS_SCI_ClientConfig " &       _
     "WHERE ItemName = 'Client Properties'" & _
     "AND SiteCode = '" & siteCode & "'"

     Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

     ' Only one instance is returned from the query.
     For Each SCIComponent In SCIComponentSet

          'Loop through the array of embedded SMS_EmbeddedProperty instances.
          For Each vProperty In SCIComponent.Props

                 ' Setting: Enable Heartbeat DDR
                 If vProperty.PropertyName = "Enable Heartbeat DDR" Then
                     wscript.echo " "
                     wscript.echo vProperty.PropertyName
                     wscript.echo "Current value " & vProperty.Value

                     'Modify the value.
                     vProperty.Value = enableDisableHeartbeatDDR
                     wscript.echo "New value " & enableDisableHeartbeatDDR
                 End If

          Next

        ' Update the component in your copy of the site control file. Get
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

<!-- p.848 -->

public void ConfigureHeartbeatDiscoverySettings(WqlConnectionManager
connection,
                                                string siteCode,
                                                string serverName,
                                                string
newHeartbeatSiteControlFileSchedule,
                                                string
newEnableDisableHeartbeatDDR)
{

    try
    {
    // Change the Heartbeat Site Control File Schedule value.

        // Connect to SMS_SITE_CONTROL_MANAGER section of the site control
file.
         IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_Component.FileType=2,ItemType='Component',S
iteCode='" + siteCode + "',ItemName='SMS_SITE_CONTROL_MANAGER|" + serverName
+ "'");

        // Temporary copy of the embedded properties.
        Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {
            // Property: Heartbeat Site Control File Schedule
            if (kvp.Value.PropertyList["PropertyName"] == "Heartbeat Site
Control File Schedule")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties["Heartbeat Site Control File Schedule"]
["Value1"].StringValue);

                embeddedProperties["Heartbeat Site Control File Schedule"]
["Value1"].StringValue = newHeartbeatSiteControlFileSchedule;
                Console.WriteLine("New value    : " +
newHeartbeatSiteControlFileSchedule);
            }
        }

        // Store the settings that have changed.
        siteDefinition.EmbeddedProperties = embeddedProperties;

        // Save the settings.
        siteDefinition.Put();

    }
    catch (SmsException ex)

<!-- p.849 -->

    {
        Console.WriteLine();
        Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
    }

    try
    {
    // Change the Enable Heartbeat DDR value.

        // Connect to SMS_SCI_ClientConfig section of the site control file.
    IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientConfig.FileType=2,ItemType='Client
Configuration',SiteCode='" + siteCode + "',ItemName='Client Properties'");

        // Create temporary working copy of embedded properties.
        Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {
            // Setting: Enable Heartbeat DDR
            if (kvp.Value.PropertyList["PropertyName"] == "Enable Heartbeat
DDR")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
kvp.Value.PropertyList["Value"]);

               // Change value using the newEnableDisableHeartbeatDDR value
passed in.
                embeddedProperties["Enable Heartbeat DDR"]
["Value"].StringValue = newEnableDisableHeartbeatDDR;
                Console.WriteLine("New value    : " +
newEnableDisableHeartbeatDDR);
            }
        }

        // Store the settings that have changed.
        siteDefinition.EmbeddedProperties = embeddedProperties;

        // Save the settings.
        siteDefinition.Put();
    }

    catch (SmsException ex)
    {
        Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
        throw;
    }

}

<!-- p.850 -->

The example method has the following parameters:

                                                                             ﾉ   Expand table

 Parameter                             Type                   Description

 - connection                          - Managed:             A valid connection to the SMS
 - swbemServices                       WqlConnectionManager   Provider.
                                       - VBScript:
                                       SWbemServices

 swbemContext                          - VBScript:            A valid context object. For
                                       SWbemContext           more information, see How to
                                                              Add a Configuration Manager
                                                              Context Qualifier by Using
                                                              WMI.

 siteCode                              - Managed: String      The site code.
                                       - VBScript: String

 serverName                            - Managed: String      The server name.
                                       - VBScript: String

 newHeartbeatSiteControlFileSchedule   - Managed: String      The schedule defining how
                                       - VBScript: String     often the client will produce
                                                              heartbeat data discovery
                                                              records (DDRs).

 - newEnableDisableHeartbeatDDR        - Managed: String      A value to enable or disable
 - enableDisableHeartbeatDDR           - VBScript: String     the heartbeat DDR.

                                                              Disabled - 0

                                                              Enabled - 1

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

<!-- p.851 -->

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
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class
About schedules How to Create a Schedule Token

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.852 -->

How to Configure Network Discovery
Article • 10/04/2022

You configure the Network Discovery settings, in Configuration Manager, by modifying
the necessary site control file settings.

To configure Network Discovery
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Network Discovery section of the site control file by
        using the SMS_SCI_Component class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

   5. Make a connection to the Network Discovery section of the site control file by
        using the SMS_SCI_Configuration class.

   6. Loop through the array of available properties, making changes as needed.

   7. Commit the changes to the site control file.

Example
The following example sets the Network Discovery settings by using the
SMS_SCI_Component and SMS_SCI_Configuration classes to connect to the site control file

and change properties.

  ７ Note

  Network Discovery is unusual, in that it requires setting both the SMS_SCI_Component
  and SMS_SCI_Configuration class properties to enable the component.

For information about calling the smple code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureNetworkDiscoverySettings(swbemServices,               _

<!-- p.853 -->

                                        swbemContext,           _
                                        siteCode,               _
                                        enableDisableDiscovery)

    ' Load site control file and get the SMS_SCI_Component,
SMS_NETWORK_DISCOVERY section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , swbemContext

    ' Get the SMS_SCI_Component, SMS_NETWORK_DISCOVERY section of the site
control file.
    Query = "SELECT * FROM SMS_SCI_Component "       & _
    "WHERE ComponentName = 'SMS_NETWORK_DISCOVERY' " & _
    "AND SiteCode = '" & siteCode & "'"

    ' Get the SMS_NETWORK_DISCOVERY properties.
    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

    ' Only one instance is returned from the query.
    For Each SCIComponent In SCIComponentSet

       ' Display the server name.
       wscript.echo "Server: " & SCIComponent.Name

       ' Loop through the array of embedded SMS_EmbeddedProperty instances.
       For Each vProperty In SCIComponent.Props

               ' Setting: Discovery Enabled
               If vProperty.PropertyName = "Discovery Enabled" Then
                   wscript.echo " "
                   wscript.echo vProperty.PropertyName
                   wscript.echo "Current value: " & vProperty.Value1

                   ' Modify the value.
                   vProperty.Value1 = enableDisableDiscovery
                   wscript.echo "New value:     " & enableDisableDiscovery
               End If

            Next

            ' Update the component in your copy of the site control file. Get
the path
            ' to the updated object, which could be used later to retrieve the
instance.
          Set SCICompPath = SCIComponent.Put_(wbemChangeFlagUpdateOnly,
swbemContext)

    Next

    ' Get the SMS_SCI_Configuration, SMS_NETWORK_DISCOVERY section of the
site control file.
    Query = "SELECT * FROM SMS_SCI_Configuration "       & _
    "WHERE ItemName = 'SMS_NETWORK_DISCOVERY' " & _
    "AND SiteCode = '" & siteCode & "'"

<!-- p.854 -->

    ' Get the SMS_NETWORK_DISCOVERY properties.
    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

     ' Only one instance is returned from the query.
     For Each SCIComponent In SCIComponentSet

          ' Loop through the array of embedded SMS_EmbeddedProperty instances.
          For Each vProperty In SCIComponent.Props

               ' Setting: Discovery Enabled
               If vProperty.PropertyName = "Discovery Enabled" Then
                   wscript.echo " "
                   wscript.echo vProperty.PropertyName
                   wscript.echo "Current value: " & vProperty.Value1

                   ' Modify the value.
                   vProperty.Value1 = enableDisableDiscovery
                   wscript.echo "New value:     " & enableDisableDiscovery
               End If

            Next

            ' Update the component in your copy of the site control file. Get
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

public void ConfigureNetworkDiscoverySettings(WqlConnectionManager
connection,
                                              string siteCode,
                                              string serverName,
                                              string enableDisableDiscovery)

<!-- p.855 -->

{
      try
      {
        // Connect to SMS_SCI_Component, SMS_NETWORK_DISCOVERY section of
the site control file.
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_Component.FileType=2,ItemType='Component',S
iteCode='" + siteCode + "',ItemName='SMS_NETWORK_DISCOVERY|" + serverName +
"'");

        // Create temporary copy of the embedded properties.
        Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

            // Enumerate through the embedded properties and makes changes as
needed.
        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {
            // Setting: Discovery Enabled
            if (kvp.Value.PropertyList["PropertyName"] == "Discovery
Enabled")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
kvp.Value.PropertyList["Value1"]);

                   // Change value using the newDiscoveryEnabled value passed
in.
                embeddedProperties["Discovery Enabled"]
["Value1"].StringValue = enableDisableDiscovery;
                Console.WriteLine("New value     : " +
enableDisableDiscovery);
            }
        }

            // Store the settings that have changed.
            siteDefinition.EmbeddedProperties = embeddedProperties;

            // Save the settings.
            siteDefinition.Put();
      }

      catch (SmsException ex)
      {
          Console.WriteLine();
          Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
      }

      try
      {
        // Connect to SMS_SCI_Configuration, SMS_NETWORK_DISCOVERY section
of the site control file.
        IResultObject siteDefinition =

<!-- p.856 -->

  connection.GetInstance(@"SMS_SCI_Configuration.FileType=2,ItemType='Configur
  ation',SiteCode='" + siteCode + "',ItemName='SMS_NETWORK_DISCOVERY'");

          // Create temporary copy of the embedded properties.
          Dictionary<string, IResultObject> embeddedProperties =
  siteDefinition.EmbeddedProperties;

             // Enumerate through the embedded properties and makes changes as
  needed.
          foreach (KeyValuePair<string, IResultObject> kvp in
  siteDefinition.EmbeddedProperties)
          {
              // Setting: Discovery Enabled
              if (kvp.Value.PropertyList["PropertyName"] == "Discovery
  Enabled")
              {
                  Console.WriteLine();
                  Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                  Console.WriteLine("Current value: " +
  kvp.Value.PropertyList["Value1"]);

                    // Change value using the newDiscoveryEnabled value passed
  in.
                  embeddedProperties["Discovery Enabled"]
  ["Value1"].StringValue = enableDisableDiscovery;
                  Console.WriteLine("New value     : " +
  enableDisableDiscovery);
              }
          }

             // Store the settings that have changed.
             siteDefinition.EmbeddedProperties = embeddedProperties;

             //Save the settings.
             siteDefinition.Put();
        }
        catch (SmsException ex)
        {
            Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
            throw;
        }
  }

The example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter               Type                   Description

 - connection            - Managed:             A valid connection to the SMS Provider.
 - swbemServices         WqlConnectionManager

<!-- p.857 -->

 Parameter                Type                       Description

                          - VBScript:
                          SWbemServices

 swbemContext             - VBScript: SWbemContext   A valid context object. For more
                                                     information, see How to Add a
                                                     Configuration Manager Context Qualifier
                                                     by Using WMI.

 siteCode                 - Managed: String          The site code.
                          - VBScript: String

 serverName               - Managed: String          The server name.
                          - VBScript: String

 enableDisableDiscovery   - Managed: String          A value to enable or disable the discovery
                          - VBScript: String         method.

                                                     Disabled - false

                                                     Enabled - true

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

<!-- p.858 -->

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class
About schedules How to Create a Schedule Token

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.859 -->

How to Configure Active Directory
Group Discovery
Article • 10/04/2022

You configure the Active Directory Group Discovery settings, in Configuration Manager,
by modifying the necessary site control file settings.

To configure Active Directory Group Discovery
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Active Directory Group Discovery section of the site
        control file by using the SMS_SCI_Component class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example sets the Active Directory Group Discovery settings by using the
SMS_SCI_Component class to connect to the site control file and change properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureADGroupDiscoverySettings(swbemServices,    _
                                        swbemContext,                    _
                                        siteCode,                        _
                                        serverName,                      _
                                        newStartupSchedule,              _
                                        enableDisableDiscovery)

      ' Load site control file and get the
  SMS_AD_SECURITY_GROUP_DISCOVERY_AGENT section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext

      Query = "SELECT * FROM SMS_SCI_Component " &                         _
      "WHERE ItemName = 'SMS_AD_SECURITY_GROUP_DISCOVERY_AGENT|" & serverName
  & "' " & _
      "AND SiteCode = '" & siteCode & "'"

<!-- p.860 -->

    ' Get the SMS_AD_SECURITY_GROUP_DISCOVERY_AGENT properties.
    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

    ' Only one instance is returned from the query.
    For Each SCIComponent In SCIComponentSet

       ' Display the server name.
       wscript.echo "Server: " & SCIComponent.Name

       ' Loop through the array of embedded SMS_EmbeddedProperty instances.
       For Each vProperty In SCIComponent.Props

               ' Setting: Startup Schedule
               If vProperty.PropertyName = "Startup Schedule" Then
                   wscript.echo " "
                   wscript.echo vProperty.PropertyName
                   wscript.echo "Current value " & vProperty.Value1

                   ' Modify the value.
                   vProperty.Value1 = newStartupSchedule
                   wscript.echo "New value " & newStartupSchedule
               End If

               ' Setting: SETTINGS
               If vProperty.PropertyName = "SETTINGS" Then
                   wscript.echo " "
                   wscript.echo vProperty.PropertyName
                   wscript.echo "Current value " & vProperty.Value1

                   ' Modify the value.
                   vProperty.Value1 = enableDisableDiscovery
                   wscript.echo "New value " & enableDisableDiscovery
               End If

            Next

            ' Update the component in your copy of the site control file. Get
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

<!-- p.861 -->

End Sub

c#

public void ConfigureADGroupDiscoverySettings(WqlConnectionManager
connection,
                                                      string siteCode,
                                                      string serverName,
                                                      string
newStartupSchedule,
                                                      string
enableDisableDiscovery)

{
      try
      {
        // Connect to SMS_AD_SECURITY_GROUP_DISCOVERY_AGENT section of the
site control file.
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_Component.FileType=2,ItemType='Component',S
iteCode='" + siteCode + "',ItemName='SMS_AD_SECURITY_GROUP_DISCOVERY_AGENT|"
+ serverName + "'");

        // Create temporary copy of the embedded properties.
        Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

            // Enumerate through the embedded properties and makes changes as
needed.
        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {
            // Setting: Startup Schedule
            if (kvp.Value.PropertyList["PropertyName"] == "Startup
Schedule")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
kvp.Value.PropertyList["Value1"]);

                   // Change value using the newStartupSchedule value passed
in.
                embeddedProperties["Startup Schedule"]["Value1"].StringValue
= newStartupSchedule;
                Console.WriteLine("New value    : " + newStartupSchedule);
            }

                // Setting: SETTINGS
                if (kvp.Value.PropertyList["PropertyName"] == "SETTINGS")
                {

<!-- p.862 -->

                  Console.WriteLine();
                  Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                  Console.WriteLine("Current value: " +
  kvp.Value.PropertyList["Value1"]);

                     // Change value using the newEnableHeartbeatDDR value passed
  in.
                  embeddedProperties["SETTINGS"]["Value1"].StringValue =
  enableDisableDiscovery;
                  Console.WriteLine("New value    : " +
  enableDisableDiscovery);
              }
          }

              // Store the settings that have changed.
              siteDefinition.EmbeddedProperties = embeddedProperties;

              // Save the settings.
              siteDefinition.Put();
        }

        catch (SmsException ex)
        {
            Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
            throw;
        }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter                Type                       Description

 - connection             - Managed:                 A valid connection to the SMS Provider.
 - swbemServices          WqlConnectionManager
                          - VBScript:
                          SWbemServices

 swbemContext             - VBScript: SWbemContext   A valid context object. For more
                                                     information, see How to Add a
                                                     Configuration Manager Context Qualifier
                                                     by Using WMI.

 siteCode                 - Managed: String          The site code.
                          - VBScript: String

 serverName               - Managed: String          The server name.
                          - VBScript: String

<!-- p.863 -->

 Parameter                Type                 Description

 newStartupSchedule       - Managed: String    The new schedule.
                          - VBScript: String

 enableDisableDiscovery   - Managed: String    A value to enable or disable the discovery
                          - VBScript: String   method.

                                               Disabled - INACTIVE

                                               Enabled - ACTIVE

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
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

<!-- p.864 -->

See Also
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class
About schedules How to Create a Schedule Token

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.865 -->

How to Configure Active Directory
System Discovery
Article • 10/04/2022

You configure the Active Directory System Discovery settings, in Configuration Manager,
by modifying the necessary site control file settings.

To configure Active Directory System Discovery
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Active Directory System Discovery section of the site
        control file by using the SMS_SCI_Component class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example sets the Active Directory System Discovery settings by using the
SMS_SCI_Component class to connect to the site control file and change properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureADSystemDiscoverySettings(swbemServices,                 _
                                        swbemContext,                   _
                                        siteCode,                       _
                                        serverName,                     _
                                        newStartupSchedule,             _
                                        enableDisableDiscovery)

      ' Load site control file and get the SMS_AD_SYSTEM_DISCOVERY_AGENT
  section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext

         Query = "SELECT * FROM SMS_SCI_Component " &                         _
         "WHERE ItemName = 'SMS_AD_SYSTEM_DISCOVERY_AGENT|" & serverName & "' " &
  _
         "AND SiteCode = '" & siteCode & "'"

<!-- p.866 -->

    ' Get the SMS_AD_SYSTEM_DISCOVERY_AGENT properties.
    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

    ' Only one instance is returned from the query.
    For Each SCIComponent In SCIComponentSet

       ' Display the server name.
       wscript.echo "Server: " & SCIComponent.Name

       ' Loop through the array of embedded SMS_EmbeddedProperty instances.
       For Each vProperty In SCIComponent.Props

               ' Setting: Startup Schedule
               If vProperty.PropertyName = "Startup Schedule" Then
                   wscript.echo " "
                   wscript.echo vProperty.PropertyName
                   wscript.echo "Current value " & vProperty.Value1

                   ' Modify the value.
                   vProperty.Value1 = newStartupSchedule
                   wscript.echo "New value " & newStartupSchedule
               End If

               ' Setting: SETTINGS
               If vProperty.PropertyName = "SETTINGS" Then
                   wscript.echo " "
                   wscript.echo vProperty.PropertyName
                   wscript.echo "Current value " & vProperty.Value1

                   ' Modify the value.
                   vProperty.Value1 = enableDisableDiscovery
                   wscript.echo "New value " & enableDisableDiscovery
               End If

            Next

            ' Update the component in your copy of the site control file. Get
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

<!-- p.867 -->

End Sub

c#

public void ConfigureADSystemDiscoverySettings(WqlConnectionManager
connection,
                                               string siteCode,
                                               string serverName,
                                               string newStartupSchedule,
                                               string
enableDisableDiscovery)
{
    try
    {
        // Connect to SMS_AD_SYSTEM_DISCOVERY_AGENT section of the site
control file.
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_Component.FileType=2,ItemType='Component',S
iteCode='" + siteCode + "',ItemName='SMS_AD_SYSTEM_DISCOVERY_AGENT|" +
serverName + "'");

        // Create temporary copy of the embedded properties.
        Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

          // Enumerate through the embedded properties and makes changes as
needed.
        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {
            // Setting: Startup Schedule
            if (kvp.Value.PropertyList["PropertyName"] == "Startup
Schedule")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
kvp.Value.PropertyList["Value1"]);

                 // Change value using the newStartupSchedule value passed
in.
                embeddedProperties["Startup Schedule"]["Value1"].StringValue
= newStartupSchedule;
                Console.WriteLine("New value    : " + newStartupSchedule);
            }

              // Setting: SETTINGS
              if (kvp.Value.PropertyList["PropertyName"] == "SETTINGS")
              {
                  Console.WriteLine();
                  Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);

<!-- p.868 -->

                  Console.WriteLine("Current value: " +
  kvp.Value.PropertyList["Value1"]);

                      // Change value using the newEnableHeartbeatDDR value passed
  in.
                  embeddedProperties["SETTINGS"]["Value1"].StringValue =
  enableDisableDiscovery;
                  Console.WriteLine("New value    : " +
  enableDisableDiscovery);
              }
          }

              // Store the settings that have changed.
              siteDefinition.EmbeddedProperties = embeddedProperties;

              // Save the settings.
              siteDefinition.Put();
        }

        catch (SmsException ex)
        {
            Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
            throw;
        }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter                Type                       Description

 - connection             - Managed:                 A valid connection to the SMS Provider.
 - swbemServices          WqlConnectionManager
                          - VBScript:
                          SWbemServices

 swbemContext             - VBScript: SWbemContext   A valid context object. For more
                                                     information, see How to Add a
                                                     Configuration Manager Context Qualifier
                                                     by Using WMI.

 siteCode                 - Managed: String          The site code.
                          - VBScript: String

 serverName               - Managed: String          The server name.
                          - VBScript: String

 newStartupSchedule       - Managed: String          The new schedule.
                          - VBScript: String

<!-- p.869 -->

 Parameter                Type                 Description

 enableDisableDiscovery   - Managed: String    A value to enable or disable the discovery
                          - VBScript: String   method.

                                               Disabled - INACTIVE

                                               Enabled - ACTIVE

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
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also

<!-- p.870 -->

About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class
About schedules How to Create a Schedule Token

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.871 -->

How to Configure Active Directory User
Discovery
Article • 10/04/2022

In Configuration Manager, you configure the Active Directory User Discovery settings by
modifying the necessary site control file settings.

To configure Active Directory User Discovery
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Active Directory User Discovery section of the site
        control file by using the SMS_SCI_Component class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example sets the Active Directory User Discovery settings by using the
SMS_SCI_Component class to connect to the site control file and change properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureADUserDiscoverySettings(swbemServices,                  _
                                       swbemContext,                   _
                                       siteCode,                       _
                                       serverName,                     _
                                       newStartupSchedule,             _
                                       enableDisableDiscovery)

      ' Load site control file and get the SMS_AD_USER_DISCOVERY_AGENT
  section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext

         Query = "SELECT * FROM SMS_SCI_Component " &                         _
         "WHERE ItemName = 'SMS_AD_USER_DISCOVERY_AGENT|" & serverName & "' " &
  _
         "AND SiteCode = '" & siteCode & "'"

<!-- p.872 -->

    ' Get the SMS_AD_USER_DISCOVERY_AGENT properties.
    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

    ' Only one instance is returned from the query.
    For Each SCIComponent In SCIComponentSet

       ' Display the server name.
       wscript.echo "Server: " & SCIComponent.Name

       ' Loop through the array of embedded SMS_EmbeddedProperty instances.
       For Each vProperty In SCIComponent.Props

               ' Setting: Startup Schedule
               If vProperty.PropertyName = "Startup Schedule" Then
                   wscript.echo " "
                   wscript.echo vProperty.PropertyName
                   wscript.echo "Current value " & vProperty.Value1

                   ' Modify the value.
                   vProperty.Value1 = newStartupSchedule
                   wscript.echo "New value " & newStartupSchedule
               End If

               ' Setting: SETTINGS
               If vProperty.PropertyName = "SETTINGS" Then
                   wscript.echo " "
                   wscript.echo vProperty.PropertyName
                   wscript.echo "Current value " & vProperty.Value1

                   ' Modify the value.
                   vProperty.Value1 = enableDisableDiscovery
                   wscript.echo "New value " & enableDisableDiscovery
               End If

            Next

            ' Update the component in your copy of the site control file. Get
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

<!-- p.873 -->

End Sub

c#

public void ConfigureADUserDiscoverySettings(WqlConnectionManager
connection,
                                             string siteCode,
                                             string serverName,
                                             string newStartupSchedule,
                                             string enableDisableDiscovery)
{
    try
    {
        // Connect to SMS_AD_USER_DISCOVERY_AGENT section of the site
control file.
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_Component.FileType=2,ItemType='Component',S
iteCode='" + siteCode + "',ItemName='SMS_AD_USER_DISCOVERY_AGENT|" +
serverName + "'");

        // Create temporary copy of the embedded properties.
        Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

          // Enumerate through the embedded properties and makes changes as
needed.
        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {
            // Setting: Startup Schedule
            if (kvp.Value.PropertyList["PropertyName"] == "Startup
Schedule")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
kvp.Value.PropertyList["Value1"]);

                 // Change value using the newStartupSchedule value passed
in.
                embeddedProperties["Startup Schedule"]["Value1"].StringValue
= newStartupSchedule;
                Console.WriteLine("New value    : " + newStartupSchedule);
            }

              // Setting: SETTINGS
              if (kvp.Value.PropertyList["PropertyName"] == "SETTINGS")
              {
                  Console.WriteLine();
                  Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                  Console.WriteLine("Current value: " +

<!-- p.874 -->

  kvp.Value.PropertyList["Value1"]);

                      // Change value using the enableDisableDiscovery value
  passed in.
                  embeddedProperties["SETTINGS"]["Value1"].StringValue =
  enableDisableDiscovery;
                  Console.WriteLine("New value    : " +
  enableDisableDiscovery);
              }
          }

              // Store the settings that have changed.
              siteDefinition.EmbeddedProperties = embeddedProperties;

              // Save the settings.
              siteDefinition.Put();
       }

       catch (SmsException ex)
       {
           Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
           throw;
       }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter                Type                       Description

 - connection             - Managed:                 A valid connection to the SMS Provider.
 - swbemServices          WqlConnectionManager
                          - VBScript:
                          SWbemServices

 swbemContext             - VBScript: SWbemContext   A valid context object. For more
                                                     information, see How to Add a
                                                     Configuration Manager Context Qualifier
                                                     by Using WMI.

 siteCode                 - Managed: String          The site code.
                          - VBScript: String

 serverName               - Managed: String          The server name.
                          - VBScript: String

 newStartupSchedule       - Managed: String          The new schedule.
                          - VBScript: String

<!-- p.875 -->

 Parameter                Type                 Description

 enableDisableDiscovery   - Managed: String    A value to enable or disable the discovery
                          - VBScript: String   method.

                                               Disabled - INACTIVE

                                               Enabled - ACTIVE

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
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also

<!-- p.876 -->

About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class
About schedules How to Create a Schedule Token

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.877 -->

About DDR Properties
Article • 10/04/2022

In Configuration Manager, the architecture for a resource is defined in both the
database and the data discovery record (DDR). If the architecture isn't defined in the
database, the definition is created from the setting in the DDR.

The architecture definition consists of properties and their types, maximum lengths, and
flag settings. Some flag settings can be taken only from the architecture definition in the
database, some can be overwritten by settings in the DDR, and others are taken only
from the DDR. Even flags that can be set only in the DDR have meaning in the
architecture definition in the database because these are used to set the flags on the
DDRs that are replicated to a site's parent. These replicated DDRs are sent up when an
incoming DDR is processing and are the combination of the incoming DDR and the
resource stored in the database.

Property Flags
                                                                               ﾉ   Expand table

 Name                                Value        Description

 DISCOVERY_FLAG_FULL_REPLACE         0x00000001   Replace all array values with those from
 DISCOVERY_FLAG_LOW_CONFIDENCE                    the DDR. Set only the scalar value if the
                                                  value is null .

 DISCOVERY_FLAG_GUID                 0x00000002   Configuration Manager unique ID,
                                                  specified in the database.

 DISCOVERY_FLAG_KEY                  0x00000008   A key property, which if present, uniquely
                                                  identifies the item.

 DISCOVERY_FLAG_ARRAY_PROP           0x00000010   The property is an array property.

 DISCOVERY_FLAG_NAME_PROP            0x00000040   The property should be used as the item
                                                  name, if present.

 DISCOVERY_FLAG_NAME2_PROP           0x00000080   The property should be used as the item
                                                  description.

 DISCOVERY_FLAG_FIRST                0x00010000   First choice for the name.

 DISCOVERY_FLAG_SECOND               0x00020000   Second choice for the name.

 DISCOVERY_FLAG_THIRD                0x00040000   Third choice for the name.

<!-- p.878 -->

 Name                                   Value         Description

 DISCOVERY_FLAG_FOURTH                  0x00080000    Fourth choice for the name.

 DISCOVERY_FLAG_FIFTH                   0x00100000    Fifth choice for the name.

GUID
The GUID (or SMSUID) definitively identifies a resource. If it exists in the DDR, it alone is
used to match the DDR to a record in the database. Because the value of this property
for a particular resource shouldn't change from discovery to discovery, it's an artificial
value that is generated by the client. The GUID property is always taken from the
architecture definition in the database. As a result, if this flag is set for a property in a
DDR, it's meaningful only if the architecture hasn't been created yet. For the System
architecture, the GUID is the string property "SMS Unique Identifier".

Prior to SMS 2003 SP1, changes were allowed to records if a DDR arrived with a new
GUID but with the same key properties. As of SMS 2003 SP1, this changed—a new GUID
generates a new record even if the key properties remain the same.

  ） Important

  GUIDs are case insensitive; however, the case should never vary after the GUID has
  been submitted to the database. GUID processing issues will arise, if the GUID
  changes case.

Key Properties
Key properties are physical properties that individually can be used to uniquely identify
a resource. Because they're physical properties, they might be subject to change. For
this reason, in addition to the fact that not all discovery agents can discover a particular
property, an architecture should have several key properties. The key property setting is
taken from the DDR, not the architecture definition in the database. For the System
architecture, the key properties are "MAC Addresses" and "NetBIOS Name".

Array Properties
A property can have either a single (scalar) value or multiple (array) values. The array flag
in the DDR should match the architecture definition.

<!-- p.879 -->

Full Replace and Low Confidence
The meaning of this flag depends on whether the property is a scalar property or an
array property. If it's a scalar value and this flag is set in the DDR, the DDR value should
overwrite the database value only if the database value is null (not set). Usually, the
value in the DDR overwrites the value in the database. If the property is an array
property, the set of values in the DDR should fully replace the values in the database.
Typically, the values in the DDR are added to the set of values in the database. This flag
setting varies from discovery agent to discovery agent and is taken from the DDR. One
example of this is the IP Addresses property reported by Network Discovery. Because
Network Discovery might not be able to discover all the IP addresses for a computer,
the Full Replace flag isn't set in its DDR.

Name Flags

Each resource has an auto-generated name property called Name, which is generated
by the Data Discovery Manager (DDM). This property is used as the display name of the
resource and shows up as the name in the collection membership. If a Name property
exists in the DDR, it's overwritten. The Name property is selected from the first non-null
DDR property with the Name flag set. The properties are tried in the order according to
the ordering flags. Each name candidate property should have both the Name flag and
an ordering flag set. If a Name2 flag is set, it's taken as the description and appended to
the Name property in parentheses: "<name> (<name2>)". The name flags are taken
from the architecture definition but can be overwritten in the DDR. The DDR is rejected
as corrupt if the Name property can't be populated. The name properties for the System
architecture in order of preference are "NetBIOS Name", "Resource Names", "IP
Addresses", and "MAC Addresses".

Property Type, Property Length, and Property
Value

Property Type

The property type defines the data type of the property. Each property type can be
either a scalar or an array property. Currently used and accepted ones are:

     Integer: 8
     String: 11
     Date/Time: 12

<!-- p.880 -->

The property type in the architecture must match the type in the DDR.

Property Length
The length setting is only applicable to string properties and represents the maximum
length of the string. The value in the DDR permanently overrides the value in the
architecture definition. Therefore, if this setting doesn't match, it permanently changes
the architecture definition.

Property Value

The property value should be represented in string format. Numbers should be
represented in base 10 and contain no non-numeric characters. Dates should be
formatted as "MM/DD/YY HH:MM:SS". If the property value is null , it should be set to
the string "(null)". The value for a string shouldn't exceed the maximum length.

Special System Properties

Operating System Name and Version
This property is used by the DDM to determine when to generate a client configuration
request (CCR) for push client installation. The property takes the format of "<operating
system name> <operating system version>". The operating system name should be the
common name of the operating system, not the name of the release ("Windows NT"
instead of "Windows 2000" or "Windows XP"). The recognized operating system names
for push installation are "Microsoft Windows NT Server" (servers products), "Microsoft
Windows NT Workstation" (workstation products), and "Microsoft Windows NT
Advanced Server".

Client Type

Client type 1 is the Configuration Manager client type.

Feedback
Was this page helpful?      Yes    No

Provide product feedback
